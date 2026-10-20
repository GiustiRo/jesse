"""Causal, opt-in Binance USD-M BTC open-interest observations, independent of cash fees.

The recent REST series is not a substitute for a point-in-time historical archive.
Missing observations remain missing, and stale values are never replaced by zero.
"""

from bisect import bisect_right
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import re
import tempfile
import time

import requests


EXCHANGE = 'Binance Perpetual Futures'
SYMBOL = 'BTC-USDT'
SOURCE = 'binance-usdm-openInterestHist-v1'
PERIOD_MS = 300_000
# Binance documents period-end timestamps but does not publish original release
# timestamps. An extra full interval plus one minute is an explicit conservative
# research assumption, not a claim of certified point-in-time provenance.
AVAILABILITY_LAG_MS = PERIOD_MS + 60_000
REST_RETENTION_MS = 30 * 86_400_000
DEFAULT_MAX_AGE_MS = 2 * PERIOD_MS
MAX_PAGE_BUCKETS = 500


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
    if (dataset.get('schema') != 1 or dataset.get('source') != SOURCE
            or dataset.get('exchange') != EXCHANGE or dataset.get('symbol') != SYMBOL
            or dataset.get('period_ms') != PERIOD_MS
            or dataset.get('availability_lag_ms') != AVAILABILITY_LAG_MS
            or type(dataset.get('start')) is not int or type(dataset.get('finish')) is not int
            or not 0 <= dataset['start'] < dataset['finish']):
        raise ValueError('Unsupported open-interest dataset')
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
    return {key: value for key, value in dataset.items() if key != 'observations'} | {
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
        'availability_policy': 'period_label_plus_6m_assumption; original_publication_unknown',
        'history_limit': 'REST latest 1 month; importer conservatively accepts latest 30 days',
        'missing_policy': 'no interpolation; unavailable or stale values return None',
        'cashflow': False,
    }


def list_datasets(limit: int = 100) -> list[dict]:
    if type(limit) is not int or not 1 <= limit <= 200:
        raise ValueError('Open-interest dataset list limit must be between 1 and 200')
    paths = sorted(_root().glob('*.json'), key=lambda path: path.stat().st_mtime, reverse=True)
    return [describe_dataset(path.stem, load_dataset(path.stem)) for path in paths[:limit]]


def _fetch_history(start: int, finish: int) -> list[dict]:
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
            # Below the documented 1,000 requests/5min for one importer. Vendor
            # 429/418 and network errors fail without publishing partial coverage.
            time.sleep(0.4)
    if not observations:
        raise ValueError('No open interest returned; refusing an empty historical dataset')
    return list(observations.values())


def import_binance_history(start: int, finish: int, period: str = '5m', source: str = 'rest') -> dict:
    """Import public recent BTC OI; [start,finish), ms UTC, immutable per snapshot.

    Archive mode is refused until its observation/publication provenance has been
    audited. Downloading a revised archive today cannot certify availability in 2020.
    """
    now = int(time.time() * 1000)
    if source != 'rest':
        raise ValueError('Historical OI archives require a separate publication-provenance audit; use recent REST')
    if period != '5m':
        raise ValueError('Only the explicit five-minute open-interest feed is supported')
    if (type(start) is not int or type(finish) is not int or start < 0
            or not start < finish <= now):
        raise ValueError('Expected a nonempty past millisecond interval')
    if start < now - REST_RETENTION_MS:
        raise ValueError('Binance OI REST covers only the latest month; dates older than 30 days are refused')
    dataset = {'schema': 1, 'source': SOURCE, 'exchange': EXCHANGE, 'symbol': SYMBOL,
               'period_ms': PERIOD_MS, 'availability_lag_ms': AVAILABILITY_LAG_MS,
               'start': start, 'finish': finish, 'observations': _fetch_history(start, finish)}
    dataset_id = save_dataset(dataset)
    return describe_dataset(dataset_id, dataset)


def update_dataset(dataset_id: str, finish: int) -> dict:
    """Append fresh recent REST observations while keeping the original snapshot intact."""
    dataset = load_dataset(dataset_id)
    if type(finish) is not int or not dataset['finish'] < finish <= int(time.time() * 1000):
        raise ValueError('Updated OI finish must be later than coverage and no later than now')
    # Refresh the final observation too: a revised vendor row is an explicit
    # conflict rather than a silently changed input to existing research.
    overlap_start = dataset['observations'][-1]['observed_at']
    if overlap_start < int(time.time() * 1000) - REST_RETENTION_MS:
        raise ValueError('OI update cannot bridge a gap beyond the REST retention window')
    refreshed = _fetch_history(overlap_start, finish)
    by_time = {row['observed_at']: row for row in dataset['observations']}
    for row in refreshed:
        timestamp = row['observed_at']
        if timestamp in by_time and by_time[timestamp] != row:
            raise ValueError('Vendor revised an existing OI observation; import a separate snapshot')
        by_time[timestamp] = row
    updated = dataset | {'finish': finish, 'observations': [by_time[t] for t in sorted(by_time)]}
    new_id = save_dataset(updated)
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
        self.observations = _validate_dataset(dataset)
        self._availability = [row.available_at for row in self.observations]
        self.dataset_id = dataset_id
        self.max_age_ms = max_age_ms
        self.description = describe_dataset(dataset_id, dataset)

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
                'observation_count': len(self.observations), 'cashflow': False,
                'availability_lag_ms': AVAILABILITY_LAG_MS,
                'availability_policy': 'period_label_plus_6m_assumption; original_publication_unknown',
                'current': asdict(row) if row is not None else None}
