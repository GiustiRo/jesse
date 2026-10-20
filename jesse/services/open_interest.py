"""Causal, opt-in Binance USD-M BTC open-interest observations, independent of cash fees.

The recent REST series is not a substitute for a point-in-time historical archive.
Missing observations remain missing, and stale values are never replaced by zero.
"""

from bisect import bisect_right
from collections import OrderedDict, deque
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import csv
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import io
import json
import math
import os
from pathlib import Path
import re
import tempfile
import threading
import time
from typing import Callable
import xml.etree.ElementTree as ET
import zipfile

import requests


EXCHANGE = 'Binance Perpetual Futures'
SYMBOL = 'BTC-USDT'
SOURCE = 'binance-usdm-openInterestHist-v1'
ARCHIVE_SOURCE = 'binance-usdm-metrics-archive-v1'
AUTO_SOURCE = 'binance-usdm-open-interest-auto-v1'
PERIOD_MS = 300_000
# Binance documents period-end timestamps but does not publish original release
# timestamps. An extra full interval plus one minute is an explicit conservative
# research assumption, not a claim of certified point-in-time provenance.
AVAILABILITY_LAG_MS = PERIOD_MS + 60_000
REST_RETENTION_MS = 30 * 86_400_000
DEFAULT_MAX_AGE_MS = 2 * PERIOD_MS
MAX_PAGE_BUCKETS = 500
ARCHIVE_PREFIX = 'data/futures/um/daily/metrics/BTCUSDT/'
ARCHIVE_BASE = 'https://data.binance.vision/' + ARCHIVE_PREFIX
# Daily metrics archives are ~12KiB compressed in the audited samples. These
# generous bounds reject an unexpected product/ZIP bomb without external tools.
MAX_ARCHIVE_BYTES = 4 * 1024 * 1024
MAX_ARCHIVE_CSV_BYTES = 16 * 1024 * 1024
DAY_MS = 86_400_000
ARCHIVE_WORKERS = 4
# Library views need summaries, not another in-memory copy of each multi-year
# series. Keep at most one small summary per recently listed immutable file.
METADATA_CACHE_LIMIT = 200
_metadata_cache: OrderedDict[str, tuple[tuple[int, int, int], dict]] = OrderedDict()
_metadata_cache_lock = threading.RLock()


@dataclass(frozen=True)
class OpenInterestObservation:
    exchange: str
    symbol: str
    observed_at: int
    available_at: int
    quantity_base: float
    value_quote: float | None

    def __post_init__(self):
        if (self.exchange != EXCHANGE or self.symbol != SYMBOL
                or type(self.observed_at) is not int or self.observed_at < 0
                or type(self.available_at) is not int or self.available_at < self.observed_at
                or not math.isfinite(self.quantity_base) or self.quantity_base < 0
                or (self.value_quote is not None
                    and (not math.isfinite(self.value_quote) or self.value_quote < 0))):
            raise ValueError('Invalid Binance BTC open-interest observation')


def _root() -> Path:
    return Path('storage/open-interest')


def _path(dataset_id: str) -> Path:
    if not isinstance(dataset_id, str) or not re.fullmatch(r'[0-9a-f]{64}', dataset_id):
        raise ValueError('Open-interest dataset ID must be a SHA-256 digest')
    return _root() / f'{dataset_id}.json'


def _encode(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def _validate_dataset(dataset: dict) -> list[OpenInterestObservation]:
    if (dataset.get('schema') != 1 or dataset.get('source') not in (SOURCE, ARCHIVE_SOURCE, AUTO_SOURCE)
            or dataset.get('exchange') != EXCHANGE or dataset.get('symbol') != SYMBOL
            or dataset.get('period_ms') != PERIOD_MS
            or dataset.get('availability_lag_ms') != AVAILABILITY_LAG_MS
            or type(dataset.get('start')) is not int or type(dataset.get('finish')) is not int
            or not 0 <= dataset['start'] < dataset['finish']):
        raise ValueError('Unsupported open-interest dataset')
    if dataset['source'] != SOURCE and dataset.get('archive_assumptions_acknowledged') is not True:
        raise ValueError('Archive OI requires explicit retrospective availability assumptions')
    observations = [OpenInterestObservation(**row) for row in dataset.get('observations', [])]
    timestamps = [row.observed_at for row in observations]
    if not observations or timestamps != sorted(set(timestamps)):
        raise ValueError('Empty, duplicate or unordered open-interest observations')
    if any(not dataset['start'] <= row.observed_at < dataset['finish']
           or row.observed_at % PERIOD_MS != 0
           or row.available_at != row.observed_at + AVAILABILITY_LAG_MS for row in observations):
        raise ValueError('Open-interest observation outside coverage or invalid availability policy')
    return observations


def save_dataset(dataset: dict) -> str:
    """Persist immutable canonical snapshots; revisions acquire a new content ID."""
    _validate_dataset(dataset)
    payload = _encode(dataset)
    dataset_id = sha256(payload).hexdigest()
    path = _path(dataset_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as file:
        temporary = file.name
        file.write(payload)
    try:
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return dataset_id


def load_dataset(dataset_id: str) -> dict:
    payload = _path(dataset_id).read_bytes()
    if sha256(payload).hexdigest() != dataset_id:
        raise ValueError('Open-interest dataset checksum mismatch')
    dataset = json.loads(payload)
    _validate_dataset(dataset)
    return dataset


def describe_dataset(dataset_id: str, dataset: dict) -> dict:
    observations = _validate_dataset(dataset)
    timestamps = [row.observed_at for row in observations]
    gaps = [b - a for a, b in zip(timestamps, timestamps[1:])]
    first_expected = ((dataset['start'] + PERIOD_MS - 1) // PERIOD_MS) * PERIOD_MS
    last_expected = ((dataset['finish'] - 1) // PERIOD_MS) * PERIOD_MS
    expected_count = max(0, (last_expected - first_expected) // PERIOD_MS + 1)
    missing_count = expected_count - len(observations)
    leading_gap = timestamps[0] - first_expected
    trailing_gap = last_expected - timestamps[-1]
    files = dataset.get('archive_files', [])
    return {key: value for key, value in dataset.items() if key not in ('observations', 'archive_files')} | {
        'dataset_id': dataset_id,
        'observation_count': len(observations),
        'expected_observation_count': expected_count,
        'missing_observation_count': missing_count,
        'coverage_complete': missing_count == 0,
        'status': 'ready' if missing_count == 0 else 'incomplete',
        'leading_gap_ms': leading_gap, 'trailing_gap_ms': trailing_gap,
        'first_observation': timestamps[0], 'last_observation': timestamps[-1],
        'first_available_at': observations[0].available_at,
        'last_available_at': observations[-1].available_at,
        'largest_gap_ms': max([leading_gap, trailing_gap, *gaps], default=0),
        'gap_count': sum(gap > PERIOD_MS for gap in gaps),
        'availability_policy': ('retrospective_archive_period_label_plus_6m_assumption; original_publication_unknown'
                                if dataset['source'] != SOURCE else
                                'period_label_plus_6m_assumption; original_publication_unknown'),
        'history_limit': ('Official daily metrics archive; earliest verified listing 2020-09-01'
                         if dataset['source'] != SOURCE else
                         'REST latest 1 month; importer conservatively accepts latest 30 days'),
        'point_in_time_certified': False,
        'missing_policy': 'no interpolation; unavailable or stale values return None',
        'cashflow': False,
        'archive_file_count': len(files),
        'archive_verified_file_count': sum(row['status'] == 'verified' for row in files),
        'archive_missing_days': [row['date'] for row in files if row['status'] != 'verified'][:10],
        'archive_missing_day_count': sum(row['status'] != 'verified' for row in files),
        'archive_identical_duplicate_rows': sum(row.get('identical_duplicate_rows', 0) for row in files),
    }


def list_datasets(limit: int = 100) -> list[dict]:
    if type(limit) is not int or not 1 <= limit <= 200:
        raise ValueError('Open-interest dataset list limit must be between 1 and 200')
    paths = sorted(_root().glob('*.json'), key=lambda path: path.stat().st_mtime, reverse=True)
    root = os.path.abspath(_root())
    existing = {os.path.abspath(path) for path in paths}
    with _metadata_cache_lock:
        for key in list(_metadata_cache):
            if os.path.dirname(key) == root and key not in existing:
                del _metadata_cache[key]
    return [_listed_dataset_metadata(path) for path in paths[:limit]]


def _metadata_fingerprint(path: Path) -> tuple[int, int, int]:
    stat = path.stat()
    return stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


def _listed_dataset_metadata(path: Path) -> dict:
    # The named absolute path keeps separate projects/test roots independent,
    # even if two copies share a content ID. Do not resolve symlink aliases.
    key = os.path.abspath(path)
    fingerprint = _metadata_fingerprint(path)
    with _metadata_cache_lock:
        cached = _metadata_cache.get(key)
        if cached is not None and cached[0] == fingerprint:
            _metadata_cache.move_to_end(key)
            return deepcopy(cached[1])
        _metadata_cache.pop(key, None)
    # Cold reads retain checksum/schema verification. Explicit load_dataset
    # calls never use this cache and always verify the stored bytes.
    summary = describe_dataset(path.stem, load_dataset(path.stem))
    if _metadata_fingerprint(path) != fingerprint:
        raise ValueError('Open-interest dataset changed while its metadata was being read')
    with _metadata_cache_lock:
        _metadata_cache[key] = fingerprint, deepcopy(summary)
        _metadata_cache.move_to_end(key)
        while len(_metadata_cache) > METADATA_CACHE_LIMIT:
            _metadata_cache.popitem(last=False)
    return summary


def _fetch_history(start: int, finish: int, progress_callback: Callable[[dict], None] | None = None) -> list[dict]:
    observations = {}
    # Binance rounds startTime to the five-minute bucket. A +1ms cursor can
    # therefore return the previous final row forever, especially at a window
    # tail. Ask only for full bucket labels inside the requested half-open range.
    cursor = ((start + PERIOD_MS - 1) // PERIOD_MS) * PERIOD_MS
    with requests.Session() as client:
        while cursor < finish:
            # This endpoint can select the most recent `limit` observations
            # in a broad range. Bound time as well as row count so that a nine-
            # day request cannot silently return only its latest 500 rows.
            window_finish = min(finish, cursor + MAX_PAGE_BUCKETS * PERIOD_MS)
            response = client.get('https://fapi.binance.com/futures/data/openInterestHist', params={
                'symbol': 'BTCUSDT', 'period': '5m', 'startTime': cursor,
                'endTime': window_finish - 1, 'limit': MAX_PAGE_BUCKETS,
            }, timeout=30)
            response.raise_for_status()
            rows = response.json()
            if not isinstance(rows, list) or len(rows) > MAX_PAGE_BUCKETS:
                raise ValueError('Unexpected Binance open-interest response')
            if not rows:
                # An omitted/no-trade window does not imply that every later
                # window is empty. Preserve that gap and continue to the end.
                cursor = window_finish
                if progress_callback is not None:
                    progress_callback({'phase': 'rest', 'source': 'rest', 'fetched_days': 0, 'total_days': 0,
                                       'current_date': None, 'processed_buckets': (cursor - start) // PERIOD_MS,
                                       'total_buckets': (finish - start) // PERIOD_MS})
                continue
            last = -1
            last_new = None
            for row in rows:
                timestamp = int(row['timestamp'])
                if (row.get('symbol') != 'BTCUSDT' or not start <= timestamp < window_finish
                        or timestamp % PERIOD_MS != 0 or timestamp < last):
                    raise ValueError(f'Unexpected open-interest instrument, order or timestamp: '
                                     f'symbol={row.get("symbol")}, timestamp={timestamp}, '
                                     f'expected=[{cursor},{window_finish}), previous={last}')
                observation = asdict(OpenInterestObservation(
                    EXCHANGE, SYMBOL, timestamp, timestamp + AVAILABILITY_LAG_MS,
                    float(row['sumOpenInterest']), float(row['sumOpenInterestValue']),
                ))
                last = timestamp
                if timestamp in observations:
                    if observations[timestamp] != observation:
                        raise ValueError('Conflicting open-interest observations')
                    continue
                if timestamp < cursor:
                    raise ValueError('Unexpected unrequested older open-interest observation')
                observations[timestamp] = observation
                last_new = timestamp
            if last_new is None:
                # A stale nonempty page is not evidence that this requested
                # window was exhausted, unlike an explicit empty response.
                raise ValueError('Binance open-interest pagination did not advance')
            cursor = window_finish
            if progress_callback is not None:
                progress_callback({'phase': 'rest', 'source': 'rest', 'fetched_days': 0, 'total_days': 0,
                                   'current_date': None, 'processed_buckets': (cursor - start) // PERIOD_MS,
                                   'total_buckets': (finish - start) // PERIOD_MS})
            # Below the documented 1,000 requests/5min for one importer. Vendor
            # 429/418 and network errors fail without publishing partial coverage.
            time.sleep(0.4)
    if not observations:
        raise ValueError('No open interest returned; refusing an empty historical dataset')
    return list(observations.values())


def import_binance_history(start: int, finish: int, period: str = '5m', source: str = 'rest',
                           allow_archive_assumptions: bool = False,
                           progress_callback: Callable[[dict], None] | None = None) -> dict:
    """Import public recent BTC OI; [start,finish), ms UTC, immutable per snapshot.

    Archive observations use the same explicit label+6m research lag. This is not
    certified original publication time; downloading a revised archive today
    cannot certify that its exact values were available to a strategy in 2020.
    """
    now = int(time.time() * 1000)
    if source not in ('rest', 'archive', 'auto'):
        raise ValueError('OI source must be rest, archive or auto')
    if period != '5m':
        raise ValueError('Only the explicit five-minute open-interest feed is supported')
    if (type(start) is not int or type(finish) is not int or start < 0
            or not start < finish <= now):
        raise ValueError('Expected a nonempty past millisecond interval')
    if source == 'rest' and start < now - REST_RETENTION_MS:
        raise ValueError('Binance OI REST covers only the latest month; dates older than 30 days are refused')
    if source != 'rest':
        dataset = _collect_archive_or_auto(start, finish, source, allow_archive_assumptions, progress_callback)
    else:
        dataset = _rest_dataset(start, finish, progress_callback)
    dataset['import_source'] = source
    if source == 'auto':
        # Preserve the user's policy even when the initial window happens to
        # contain archives only, so later updates can use REST at the recent tail.
        dataset['archive_assumptions_acknowledged'] = allow_archive_assumptions
    dataset_id = save_dataset(dataset)
    if progress_callback is not None:
        progress_callback({'phase': 'complete', 'source': source, 'fetched_days': len(dataset.get('archive_files', [])),
                           'total_days': len(dataset.get('archive_files', [])), 'current_date': None})
    return describe_dataset(dataset_id, dataset)


def _rest_dataset(start: int, finish: int, progress_callback=None) -> dict:
    return {'schema': 1, 'source': SOURCE, 'exchange': EXCHANGE, 'symbol': SYMBOL,
            'period_ms': PERIOD_MS, 'availability_lag_ms': AVAILABILITY_LAG_MS,
            'start': start, 'finish': finish, 'observations': _fetch_history(start, finish, progress_callback)}


def get_archive_catalog() -> dict:
    """Read the publisher's ordered listing, not an inferred first observation date."""
    response = requests.get('https://s3-ap-northeast-1.amazonaws.com/data.binance.vision/',
                            params={'list-type': '2', 'prefix': ARCHIVE_PREFIX, 'max-keys': 2}, timeout=30)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    namespace = {'s3': 'http://s3.amazonaws.com/doc/2006-03-01/'}
    for content in root.findall('s3:Contents', namespace):
        key = content.findtext('s3:Key', namespaces=namespace) or ''
        match = re.fullmatch(re.escape(ARCHIVE_PREFIX) + r'BTCUSDT-metrics-(\d{4}-\d{2}-\d{2})\.zip', key)
        if match:
            return {'source': ARCHIVE_SOURCE, 'first_archive_date': match.group(1),
                    'first_archive_url': 'https://data.binance.vision/' + key,
                    'first_archive_last_modified': content.findtext('s3:LastModified', namespaces=namespace),
                    'point_in_time_certified': False}
    raise ValueError('Official OI archive listing did not contain an identifiable first daily ZIP')


def _archive_observations(payload: bytes, day: str) -> tuple[list[dict], int]:
    expected_name = f'BTCUSDT-metrics-{day}.csv'
    midnight = int(datetime.strptime(day, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp() * 1000)
    observations = {}
    duplicate_count = 0
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        members = archive.infolist()
        if (len(members) != 1 or members[0].filename != expected_name
                or members[0].file_size > MAX_ARCHIVE_CSV_BYTES):
            raise ValueError('Unexpected OI archive member or uncompressed size')
        with archive.open(members[0]) as file:
            reader = csv.DictReader(io.TextIOWrapper(file, encoding='utf-8-sig', newline=''))
            required = {'create_time', 'symbol', 'sum_open_interest', 'sum_open_interest_value'}
            if not required <= set(reader.fieldnames or []):
                raise ValueError('OI archive CSV schema does not match Binance metrics')
            for row in reader:
                timestamp = int(datetime.strptime(row['create_time'], '%Y-%m-%d %H:%M:%S')
                                .replace(tzinfo=timezone.utc).timestamp() * 1000)
                # Old daily files may include the next day's 00:00 label. Keep
                # that boundary for cross-file conflict detection, never choose
                # silently between two different versions at the same label.
                if (row['symbol'] != 'BTCUSDT' or not midnight <= timestamp <= midnight + DAY_MS
                        or timestamp % PERIOD_MS != 0):
                    raise ValueError('Unexpected OI archive instrument or observation label')
                observation = asdict(OpenInterestObservation(
                    EXCHANGE, SYMBOL, timestamp, timestamp + AVAILABILITY_LAG_MS,
                    float(row['sum_open_interest']), float(row['sum_open_interest_value']),
                ))
                if timestamp in observations:
                    if observations[timestamp] != observation:
                        raise ValueError('Conflicting OI observations within daily archive')
                    duplicate_count += 1
                observations[timestamp] = observation
    if not observations:
        raise ValueError('OI archive CSV contains no observations')
    return [observations[t] for t in sorted(observations)], duplicate_count


def _read_archive(client, day: str) -> tuple[list[dict], dict]:
    filename = f'BTCUSDT-metrics-{day}.zip'
    url = ARCHIVE_BASE + filename
    checksum_response = client.get(url + '.CHECKSUM', timeout=30)
    if checksum_response.status_code == 404:
        return [], {'date': day, 'status': 'missing_checksum', 'url': url}
    checksum_response.raise_for_status()
    fields = checksum_response.text.strip().split()
    if len(fields) != 2 or not re.fullmatch(r'[0-9a-fA-F]{64}', fields[0]) or fields[1].lstrip('*') != filename:
        raise ValueError('Invalid official OI archive CHECKSUM response')
    checksum = fields[0].lower()
    cache = _root() / 'archives' / f'{checksum}.zip'
    if cache.exists():
        payload = cache.read_bytes()
    else:
        response = client.get(url, timeout=30)
        response.raise_for_status()
        payload = response.content
    if len(payload) > MAX_ARCHIVE_BYTES or sha256(payload).hexdigest() != checksum:
        raise ValueError('OI archive checksum mismatch or unexpected compressed size')
    observations, duplicate_count = _archive_observations(payload, day)
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=cache.parent, delete=False) as file:
            temporary = file.name
            file.write(payload)
        try:
            os.replace(temporary, cache)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    return observations, {'date': day, 'status': 'verified', 'url': url, 'sha256': checksum,
                          'checksum_last_modified': checksum_response.headers.get('Last-Modified'),
                          'identical_duplicate_rows': duplicate_count,
                          'unique_observation_count': len(observations)}


def _fetch_archive_day(day: str) -> tuple[list[dict], dict]:
    # Requests Session is not shared between the bounded download workers.
    with requests.Session() as client:
        return _read_archive(client, day)


def _collect_archive_or_auto(start: int, finish: int, source: str, acknowledged: bool, progress_callback=None) -> dict:
    now = int(time.time() * 1000)
    # Auto uses archives outside the recent REST window and REST for its final
    # 29 complete days. That avoids depending on same-day archive publication.
    cutoff = ((now - 29 * DAY_MS) // DAY_MS) * DAY_MS
    archive_finish = min(finish, cutoff) if source == 'auto' else finish
    if archive_finish <= start:
        return _rest_dataset(start, finish, progress_callback)
    if acknowledged is not True:
        raise ValueError('Archive OI original publication provenance is unknown; explicitly set allow_archive_assumptions=True')
    catalog = get_archive_catalog()
    first_date = datetime.strptime(catalog['first_archive_date'], '%Y-%m-%d').replace(tzinfo=timezone.utc)
    first_timestamp = int(first_date.timestamp() * 1000)
    if start < first_timestamp:
        raise ValueError(f'Official Binance OI archive begins {catalog["first_archive_date"]}; requested earlier dates are unavailable')
    if archive_finish <= first_timestamp:
        raise ValueError(f'Official Binance OI archive begins {catalog["first_archive_date"]}; earlier history is unavailable')
    day = datetime.fromtimestamp(max(start, first_timestamp) / 1000, tz=timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0)
    combined = {}
    files = []
    total_days = (archive_finish - int(day.timestamp() * 1000) + DAY_MS - 1) // DAY_MS
    if progress_callback is not None:
        progress_callback({'phase': 'archive', 'source': source, 'fetched_days': 0,
                           'total_days': total_days, 'current_date': day.strftime('%Y-%m-%d')})
    pending = deque()
    with ThreadPoolExecutor(max_workers=ARCHIVE_WORKERS) as executor:
        def submit_next():
            nonlocal day
            if int(day.timestamp() * 1000) < archive_finish:
                pending.append(executor.submit(_fetch_archive_day, day.strftime('%Y-%m-%d')))
                day += timedelta(days=1)

        for _ in range(ARCHIVE_WORKERS):
            submit_next()
        try:
            while pending:
                # Ordered consumption makes cross-day conflicts deterministic.
                # Only four requests are in flight, so cancellation never leaves
                # thousands of eagerly queued downloads running in the background.
                rows, manifest = pending.popleft().result()
                files.append(manifest)
                for row in rows:
                    timestamp = row['observed_at']
                    if timestamp in combined and combined[timestamp] != row:
                        raise ValueError('Conflicting OI labels across daily archives; inspect timestamp convention revisions')
                    combined[timestamp] = row
                if progress_callback is not None:
                    progress_callback({'phase': 'archive', 'source': source, 'fetched_days': len(files),
                                       'total_days': total_days, 'current_date': manifest['date']})
                submit_next()
        finally:
            for future in pending:
                future.cancel()
    rest_start = max(start, archive_finish)
    has_rest = source == 'auto' and rest_start < finish
    if has_rest:
        def rest_progress(value):
            if progress_callback is not None:
                progress_callback(value | {'source': source, 'fetched_days': len(files), 'total_days': total_days})
        for row in _fetch_history(rest_start, finish, rest_progress):
            timestamp = row['observed_at']
            if timestamp in combined and combined[timestamp] != row:
                raise ValueError('Conflicting OI archive and REST boundary observations')
            combined[timestamp] = row
    observations = [combined[t] for t in sorted(combined) if start <= t < finish]
    if not observations:
        raise ValueError('No official OI observations returned for the archive window')
    dataset = {'schema': 1, 'source': AUTO_SOURCE if has_rest else ARCHIVE_SOURCE,
               'exchange': EXCHANGE, 'symbol': SYMBOL, 'period_ms': PERIOD_MS,
               'availability_lag_ms': AVAILABILITY_LAG_MS, 'start': start, 'finish': finish,
               'observations': observations, 'archive_assumptions_acknowledged': True,
               'archive_files': files, 'archive_catalog': catalog,
               'original_publication_known': False,
               'rest_range': {'start': rest_start, 'finish': finish} if has_rest else None}
    return dataset


def update_dataset(dataset_id: str, finish: int, progress_callback: Callable[[dict], None] | None = None) -> dict:
    """Append fresh recent REST observations while keeping the original snapshot intact."""
    dataset = load_dataset(dataset_id)
    if type(finish) is not int or not dataset['finish'] < finish <= int(time.time() * 1000):
        raise ValueError('Updated OI finish must be later than coverage and no later than now')
    # Refresh the final observation too: a revised vendor row is an explicit
    # conflict rather than a silently changed input to existing research.
    overlap_start = dataset['observations'][-1]['observed_at']
    uses_archives = dataset['source'] != SOURCE or dataset.get('import_source') == 'auto'
    if uses_archives:
        source = dataset.get('import_source') or ('auto' if dataset['source'] == AUTO_SOURCE else 'archive')
        acknowledged = dataset.get('archive_assumptions_acknowledged') is True
        refreshed_dataset = _collect_archive_or_auto(overlap_start, finish, source, acknowledged, progress_callback)
        refreshed = refreshed_dataset['observations']
        files = {row['date']: row for row in dataset.get('archive_files', [])}
        for row in refreshed_dataset.get('archive_files', []):
            previous = files.get(row['date'])
            if (previous is not None and previous.get('sha256') is not None
                    and previous.get('sha256') != row.get('sha256')):
                raise ValueError('Vendor revised an existing OI archive; import a separate snapshot')
            files[row['date']] = row
    elif overlap_start < int(time.time() * 1000) - REST_RETENTION_MS:
        raise ValueError('OI update cannot bridge a gap beyond the REST retention window')
    else:
        refreshed = _fetch_history(overlap_start, finish, progress_callback)
    by_time = {row['observed_at']: row for row in dataset['observations']}
    for row in refreshed:
        timestamp = row['observed_at']
        if timestamp in by_time and by_time[timestamp] != row:
            raise ValueError('Vendor revised an existing OI observation; import a separate snapshot')
        by_time[timestamp] = row
    updated = dataset | {'finish': finish, 'observations': [by_time[t] for t in sorted(by_time)]}
    if uses_archives:
        updated['archive_files'] = [files[day] for day in sorted(files)]
        has_rest = dataset.get('rest_range') is not None or refreshed_dataset['source'] in (SOURCE, AUTO_SOURCE)
        updated['source'] = AUTO_SOURCE if files and has_rest else ARCHIVE_SOURCE if files else SOURCE
        if refreshed_dataset['source'] == SOURCE:
            previous_rest = dataset.get('rest_range') or {'start': overlap_start}
            updated['rest_range'] = {'start': previous_rest['start'], 'finish': finish}
        elif refreshed_dataset.get('rest_range') is not None:
            updated['rest_range'] = refreshed_dataset['rest_range']
        updated['archive_assumptions_acknowledged'] = acknowledged
        if 'archive_catalog' not in updated and 'archive_catalog' in refreshed_dataset:
            updated['archive_catalog'] = refreshed_dataset['archive_catalog']
    new_id = save_dataset(updated)
    if progress_callback is not None:
        progress_callback({'phase': 'complete', 'source': source if uses_archives else 'rest',
                           'fetched_days': len(updated.get('archive_files', [])),
                           'total_days': len(updated.get('archive_files', [])), 'current_date': None})
    return describe_dataset(new_id, updated)


def get_current(symbol: str = SYMBOL) -> dict:
    """A live public sample becomes available on receipt, never retroactively."""
    if symbol != SYMBOL:
        raise ValueError('Only Binance BTC-USDT open interest is supported')
    response = requests.get('https://fapi.binance.com/fapi/v1/openInterest',
                            params={'symbol': 'BTCUSDT'}, timeout=15)
    response.raise_for_status()
    row = response.json()
    if not isinstance(row, dict) or row.get('symbol') != 'BTCUSDT':
        raise ValueError('Unexpected Binance current open-interest instrument')
    received_at = int(time.time() * 1000)
    observed_at = int(row['time'])
    if abs(received_at - observed_at) > 60_000:
        raise ValueError('Current Binance open interest is stale or clock skew exceeds one minute')
    observation = OpenInterestObservation(EXCHANGE, SYMBOL, observed_at,
                                         max(received_at, observed_at), float(row['openInterest']), None)
    return asdict(observation) | {'source': 'binance-usdm-openInterest-v1',
                                 'received_at': received_at, 'value_quote': None,
                                 'cashflow': False}


class OpenInterestState:
    """Asof lookup over available_at; no forward fill beyond an explicit stale limit."""

    def __init__(self):
        self.dataset_id: str | None = None
        self.observations: list[OpenInterestObservation] = []
        self._availability: list[int] = []
        self.max_age_ms = DEFAULT_MAX_AGE_MS
        self._timestamp = -1
        self._current: OpenInterestObservation | None = None
        self.description: dict | None = None
        self.allow_missing_observations = False

    @property
    def enabled(self) -> bool:
        return self.dataset_id is not None

    def configure(self, options: dict | None, start: int, finish: int, routes: list):
        # A new configuration must never inherit the previous run's clock or
        # observations, including when a UI keeps a dataset ID while disabling.
        self.__init__()
        if options is None or (isinstance(options, dict) and options.get('mode') == 'disabled'):
            return
        if not isinstance(options, dict) or options.get('mode') != 'historical':
            raise ValueError('open_interest.mode must be disabled or historical')
        dataset_id = options.get('dataset_id', '')
        dataset = load_dataset(dataset_id)
        if not dataset['start'] <= start < finish <= dataset['finish']:
            raise ValueError('Open-interest dataset does not cover the requested observation interval')
        if not any(route.exchange == EXCHANGE and route.symbol == SYMBOL for route in routes):
            raise ValueError('Open-interest history requires a Binance BTC-USDT route')
        max_age_ms = options.get('max_age_ms', DEFAULT_MAX_AGE_MS)
        if type(max_age_ms) is not int or not PERIOD_MS <= max_age_ms <= 86_400_000:
            raise ValueError('OI stale limit must be between five minutes and one day')
        description = describe_dataset(dataset_id, dataset)
        allow_missing = options.get('allow_missing_observations', False)
        if type(allow_missing) is not bool:
            raise ValueError('allow_missing_observations must be a boolean')
        # Multi-year vendor archives can contain real holes. Consumption requires
        # acknowledging those holes; missing values remain None, never synthetic.
        if dataset['source'] != SOURCE and not description['coverage_complete'] and not allow_missing:
            raise ValueError('Historical OI contains gaps; explicitly set allow_missing_observations=True '
                             'to consume it with missing/stale observations returning None')
        self.observations = _validate_dataset(dataset)
        self._availability = [row.available_at for row in self.observations]
        self.dataset_id = dataset_id
        self.max_age_ms = max_age_ms
        self.description = description
        self.allow_missing_observations = allow_missing

    def advance(self, timestamp: int):
        if timestamp < self._timestamp:
            raise ValueError('Open-interest replay time must not move backwards')
        self._timestamp = timestamp
        index = bisect_right(self._availability, timestamp) - 1
        self._current = self.observations[index] if index >= 0 else None

    def current(self, exchange: str, symbol: str, timestamp: int | None = None) -> OpenInterestObservation | None:
        if exchange != EXCHANGE or symbol != SYMBOL:
            return None
        timestamp = self._timestamp if timestamp is None else timestamp
        index = bisect_right(self._availability, timestamp) - 1
        if index < 0:
            return None
        row = self.observations[index]
        # Age begins when the model considers the value available; otherwise a
        # lagged observation would already be stale the instant it becomes usable.
        return row if timestamp - row.available_at <= self.max_age_ms else None

    def snapshot(self) -> dict:
        row = self.current(EXCHANGE, SYMBOL)
        return {'mode': 'historical' if self.enabled else 'disabled',
                'dataset_id': self.dataset_id, 'max_age_ms': self.max_age_ms,
                'applied': self.enabled, 'status': 'applied' if self.enabled else 'disabled',
                'scope': [SYMBOL] if self.enabled else [], 'data': self.description,
                'allow_missing_observations': self.allow_missing_observations,
                'observation_count': len(self.observations), 'cashflow': False,
                'availability_lag_ms': AVAILABILITY_LAG_MS,
                'availability_policy': (self.description or {}).get(
                    'availability_policy', 'period_label_plus_6m_assumption; original_publication_unknown'),
                'current': asdict(row) if row is not None else None}
