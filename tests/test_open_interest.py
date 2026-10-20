"""Vendor-boundary and asof tests; no exchange account or real network is used."""

from dataclasses import asdict
from datetime import datetime, timezone
from hashlib import sha256
import io
from types import SimpleNamespace
import zipfile

import pytest

from jesse.services import open_interest as oi


NOW = 1_999_999_800_000  # Five-minute historical labels are aligned to UTC epoch buckets.
START = NOW - 3_600_000


@pytest.fixture(autouse=True)
def isolated_data(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(oi.time, 'time', lambda: NOW / 1000)
    monkeypatch.setattr(oi.time, 'sleep', lambda seconds: None)


def _observation(timestamp=START, quantity=20000.0):
    return asdict(oi.OpenInterestObservation(
        oi.EXCHANGE, oi.SYMBOL, timestamp, timestamp + oi.AVAILABILITY_LAG_MS,
        quantity, quantity * 100_000,
    ))


def _dataset(observations=None, start=START, finish=NOW):
    return {'schema': 1, 'source': oi.SOURCE, 'exchange': oi.EXCHANGE, 'symbol': oi.SYMBOL,
            'period_ms': oi.PERIOD_MS, 'availability_lag_ms': oi.AVAILABILITY_LAG_MS,
            'start': start, 'finish': finish,
            'observations': observations if observations is not None else [_observation()]}


def _vendor_row(timestamp, quantity='20000.0'):
    # Field names and period-end timestamp follow Binance's public REST schema.
    # Publication time is absent, so the importer supplies a declared lag policy.
    return {'symbol': 'BTCUSDT', 'timestamp': timestamp,
            'sumOpenInterest': quantity, 'sumOpenInterestValue': '2000000000.0'}


class _Response:
    def __init__(self, payload, error=None):
        self.payload, self.error = payload, error

    def raise_for_status(self):
        if self.error is not None:
            raise self.error

    def json(self):
        return self.payload


def _mock_pages(monkeypatch, pages):
    calls = []
    iterator = iter(pages)

    class Client:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def get(self, url, params, timeout):
            calls.append((url, dict(params), timeout))
            return _Response(next(iterator))

    monkeypatch.setattr(oi.requests, 'Session', Client)
    return calls


def test_snapshots_are_idempotent_checksum_verified_and_traversal_is_refused():
    dataset = _dataset()
    dataset_id = oi.save_dataset(dataset)
    assert oi.save_dataset(dataset) == dataset_id
    assert oi.load_dataset(dataset_id) == dataset
    assert oi.list_datasets()[0]['dataset_id'] == dataset_id
    oi._path(dataset_id).write_text('{}')
    with pytest.raises(ValueError, match='checksum'):
        oi.load_dataset(dataset_id)
    with pytest.raises(ValueError, match='SHA-256'):
        oi.load_dataset('../secrets')


def test_import_exhausts_ascending_inclusive_pages_and_records_gaps(monkeypatch):
    finish = START + 1001 * oi.PERIOD_MS
    monkeypatch.setattr(oi.time, 'time', lambda: (finish + oi.PERIOD_MS) / 1000)
    calls = _mock_pages(monkeypatch, [
        [_vendor_row(START), _vendor_row(START + oi.PERIOD_MS)],
        [_vendor_row(START + 501 * oi.PERIOD_MS)], [],
    ])
    result = oi.import_binance_history(START, finish)
    assert result['observation_count'] == 3
    assert result['gap_count'] == 1
    assert result['largest_gap_ms'] == 500 * oi.PERIOD_MS
    assert result['trailing_gap_ms'] == 499 * oi.PERIOD_MS
    assert result['missing_observation_count'] == 998
    assert result['status'] == 'incomplete'
    assert result['cashflow'] is False
    assert result['availability_lag_ms'] == 360_000
    assert calls[0][1] == {'symbol': 'BTCUSDT', 'period': '5m', 'startTime': START,
                            'endTime': START + 500 * oi.PERIOD_MS - 1, 'limit': 500}
    assert calls[1][1]['startTime'] == START + 500 * oi.PERIOD_MS
    assert calls[2][1]['startTime'] == START + 1000 * oi.PERIOD_MS
    dataset = oi.load_dataset(result['dataset_id'])
    assert dataset['observations'][0]['quantity_base'] == 20000
    assert dataset['observations'][0]['available_at'] == START + 360_000


def test_listing_reuses_verified_metadata_without_deserializing_again(monkeypatch):
    identifier = oi.save_dataset(_dataset())
    original_load = oi.load_dataset
    loaded = []

    def load(dataset_id):
        loaded.append(dataset_id)
        return original_load(dataset_id)

    monkeypatch.setattr(oi, 'load_dataset', load)
    first = oi.list_datasets()
    assert loaded == [identifier]
    first[0]['status'] = 'caller modified this copy'
    assert oi.list_datasets()[0]['status'] == 'incomplete'
    assert loaded == [identifier]
    # Explicit reads still verify and deserialize on every invocation.
    oi.load_dataset(identifier)
    assert loaded == [identifier, identifier]


def test_listing_invalidates_changed_or_removed_files_instead_of_hiding_corruption():
    identifier = oi.save_dataset(_dataset())
    assert oi.list_datasets()[0]['dataset_id'] == identifier
    path = oi._path(identifier)
    path.write_text('{}')
    with pytest.raises(ValueError, match='checksum'):
        oi.list_datasets()
    assert str(path.absolute()) not in oi._metadata_cache
    oi.save_dataset(_dataset())
    assert oi.list_datasets()[0]['dataset_id'] == identifier
    path.unlink()
    assert oi.list_datasets() == []
    assert str(path.absolute()) not in oi._metadata_cache


def test_listing_cache_never_crosses_project_roots(tmp_path, monkeypatch):
    first_root, second_root = tmp_path / 'first-project', tmp_path / 'second-project'
    monkeypatch.setattr(oi, '_root', lambda: first_root)
    identifier = oi.save_dataset(_dataset())
    assert oi.list_datasets()[0]['dataset_id'] == identifier
    monkeypatch.setattr(oi, '_root', lambda: second_root)
    assert oi.save_dataset(_dataset()) == identifier
    oi._path(identifier).write_text('{}')
    with pytest.raises(ValueError, match='checksum'):
        oi.list_datasets()
    monkeypatch.setattr(oi, '_root', lambda: first_root)
    assert oi.list_datasets()[0]['dataset_id'] == identifier


def test_listing_metadata_cache_evicts_older_summaries(monkeypatch):
    # A small test cap exercises the same LRU bound without creating 201 files.
    monkeypatch.setattr(oi, 'METADATA_CACHE_LIMIT', 2)
    for index in range(3):
        oi.save_dataset(_dataset([_observation(quantity=20_000 + index)]))
    assert len(oi.list_datasets()) == 3
    assert len(oi._metadata_cache) <= 2
    assert all('observations' not in summary and 'archive_files' not in summary
               for _, summary in oi._metadata_cache.values())


def test_last_five_minute_bucket_finishes_without_a_rounded_plus_one_ms_query(monkeypatch):
    # Reproduces the actual MCP tail: Binance repeated the 23:55 observation
    # for startTime=23:55:00.001 because it rounds down to the five-minute label.
    finish = 1_792_368_000_000
    start = finish - 3 * oi.PERIOD_MS
    monkeypatch.setattr(oi.time, 'time', lambda: (finish + 60_000) / 1000)
    rows = [_vendor_row(timestamp) for timestamp in range(start, finish, oi.PERIOD_MS)]
    calls = _mock_pages(monkeypatch, [rows])
    result = oi.import_binance_history(start, finish)
    assert result['observation_count'] == 3
    assert result['last_observation'] == 1_792_367_700_000
    assert len(calls) == 1
    assert calls[0][1]['endTime'] == finish - 1


def test_page_overlap_is_deduplicated_without_skipping_the_next_bucket(monkeypatch):
    first, second, third = START, START + 499 * oi.PERIOD_MS, START + 500 * oi.PERIOD_MS
    finish = third + oi.PERIOD_MS
    monkeypatch.setattr(oi.time, 'time', lambda: (finish + oi.PERIOD_MS) / 1000)
    calls = _mock_pages(monkeypatch, [
        [_vendor_row(first), _vendor_row(second)],
        [_vendor_row(second), _vendor_row(third)], [],
    ])
    result = oi.import_binance_history(START, finish)
    rows = oi.load_dataset(result['dataset_id'])['observations']
    assert [row['observed_at'] for row in rows] == [first, second, third]
    assert calls[1][1]['startTime'] == third


def test_nonprogress_or_conflicting_overlapping_pages_fail_without_publishing(monkeypatch):
    finish = START + 501 * oi.PERIOD_MS
    monkeypatch.setattr(oi.time, 'time', lambda: (finish + oi.PERIOD_MS) / 1000)
    for repeated, message in [(_vendor_row(START), 'did not advance'),
                               (_vendor_row(START, '21000'), 'Conflicting')]:
        _mock_pages(monkeypatch, [[_vendor_row(START)], [repeated]])
        with pytest.raises(ValueError, match=message):
            oi.import_binance_history(START, finish)
        assert oi.list_datasets() == []


def test_unaligned_window_start_uses_the_first_bucket_inside_it(monkeypatch):
    first = START + oi.PERIOD_MS
    calls = _mock_pages(monkeypatch, [[_vendor_row(first)], []])
    result = oi.import_binance_history(START + 1, NOW)
    assert calls[0][1]['startTime'] == first
    assert result['first_observation'] == first


def test_bounded_windows_survive_the_vendor_most_recent_500_selection(monkeypatch):
    finish = START + 9 * 86_400_000
    monkeypatch.setattr(oi.time, 'time', lambda: (finish + oi.PERIOD_MS) / 1000)
    calls = []

    class Client:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def get(self, url, params, timeout):
            calls.append(dict(params))
            # Real endpoint behavior observed through MCP: for a broad range
            # it returns its latest 500 labels rather than the earliest 500.
            labels = list(range(params['startTime'], params['endTime'] + 1, oi.PERIOD_MS))
            return _Response([_vendor_row(timestamp) for timestamp in labels[-params['limit']:]])

    monkeypatch.setattr(oi.requests, 'Session', Client)
    result = oi.import_binance_history(START, finish)
    assert result['observation_count'] == 9 * 288
    assert result['first_observation'] == START
    assert result['last_observation'] == finish - oi.PERIOD_MS
    assert result['coverage_complete'] is True
    assert result['status'] == 'ready'
    assert result['missing_observation_count'] == 0
    assert result['leading_gap_ms'] == result['trailing_gap_ms'] == 0
    assert len(calls) == 6
    assert all(call['endTime'] - call['startTime'] < 500 * oi.PERIOD_MS for call in calls)


def test_empty_middle_window_is_preserved_and_later_windows_are_still_requested(monkeypatch):
    finish = START + 1001 * oi.PERIOD_MS
    monkeypatch.setattr(oi.time, 'time', lambda: (finish + oi.PERIOD_MS) / 1000)
    calls = _mock_pages(monkeypatch, [
        [_vendor_row(START)], [], [_vendor_row(START + 1000 * oi.PERIOD_MS)],
    ])
    result = oi.import_binance_history(START, finish)
    assert len(calls) == 3
    assert result['observation_count'] == 2
    assert result['missing_observation_count'] == 999
    assert result['status'] == 'incomplete'
    assert result['last_observation'] == finish - oi.PERIOD_MS


def test_old_truncated_snapshot_is_reported_incomplete_without_rewriting_it():
    finish = START + 9 * 86_400_000
    rows = [_observation(timestamp) for timestamp in range(finish - 500 * oi.PERIOD_MS, finish, oi.PERIOD_MS)]
    dataset = _dataset(rows, finish=finish)
    dataset_id = oi.save_dataset(dataset)
    original = oi._path(dataset_id).read_bytes()
    metadata = oi.describe_dataset(dataset_id, oi.load_dataset(dataset_id))
    assert metadata['observation_count'] == 500
    assert metadata['expected_observation_count'] == 2592
    assert metadata['missing_observation_count'] == 2092
    assert metadata['leading_gap_ms'] == 2092 * oi.PERIOD_MS
    assert metadata['trailing_gap_ms'] == 0
    assert metadata['coverage_complete'] is False
    assert metadata['status'] == 'incomplete'
    assert oi._path(dataset_id).read_bytes() == original


@pytest.mark.parametrize('rows', [
    [], {'code': -1},
    [_vendor_row(START + 1), _vendor_row(START)],
    [_vendor_row(START), _vendor_row(START, '21000')],
    [_vendor_row(START - 1)],
    [_vendor_row(NOW)],
    [_vendor_row(START, 'NaN')],
    [_vendor_row(START, '-1')],
    [_vendor_row(START) | {'symbol': 'ETHUSDT'}],
])
def test_malformed_or_missing_data_never_publishes_coverage(monkeypatch, rows):
    _mock_pages(monkeypatch, [rows])
    with pytest.raises(ValueError):
        oi.import_binance_history(START, NOW)
    assert oi.list_datasets() == []


def test_retention_archive_and_future_windows_fail_before_http(monkeypatch):
    def unexpected():
        pytest.fail('Rejected requests must not access the network')
    monkeypatch.setattr(oi.requests, 'Session', unexpected)
    with pytest.raises(ValueError, match='latest month'):
        oi.import_binance_history(NOW - oi.REST_RETENTION_MS - 1, NOW)
    with pytest.raises(ValueError, match='provenance'):
        oi.import_binance_history(START, NOW, source='archive')
    with pytest.raises(ValueError, match='five-minute'):
        oi.import_binance_history(START, NOW, period='1h')
    with pytest.raises(ValueError, match='past millisecond'):
        oi.import_binance_history(START, NOW + 1)


def test_update_preserves_original_and_rejects_revisions(monkeypatch):
    old = _dataset(finish=START + oi.PERIOD_MS)
    old_id = oi.save_dataset(old)
    _mock_pages(monkeypatch, [[_vendor_row(START), _vendor_row(START + oi.PERIOD_MS)], []])
    result = oi.update_dataset(old_id, START + 2 * oi.PERIOD_MS)
    assert result['dataset_id'] != old_id
    assert oi.load_dataset(old_id) == old
    assert result['observation_count'] == 2
    _mock_pages(monkeypatch, [[_vendor_row(START, '21000')], []])
    with pytest.raises(ValueError, match='revised'):
        oi.update_dataset(old_id, START + 2 * oi.PERIOD_MS)


def test_causal_lookup_is_delayed_then_stale_without_inventing_zero():
    row = _observation()
    dataset_id = oi.save_dataset(_dataset())
    state = oi.OpenInterestState()
    route = SimpleNamespace(exchange=oi.EXCHANGE, symbol=oi.SYMBOL)
    state.configure({'mode': 'historical', 'dataset_id': dataset_id}, START, NOW, [route])
    available_at = row['available_at']
    state.advance(available_at - 1)
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is None
    state.advance(available_at)
    assert state.current(oi.EXCHANGE, oi.SYMBOL).quantity_base == 20000
    assert state.current(oi.EXCHANGE, 'ETH-USDT') is None
    state.advance(available_at + state.max_age_ms)
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is not None
    state.advance(available_at + state.max_age_ms + 1)
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is None
    assert state.snapshot()['current'] is None
    with pytest.raises(ValueError, match='backwards'):
        state.advance(available_at)


def test_configure_refuses_uncovered_window_or_wrong_route():
    dataset_id = oi.save_dataset(_dataset())
    state = oi.OpenInterestState()
    options = {'mode': 'historical', 'dataset_id': dataset_id}
    route = SimpleNamespace(exchange=oi.EXCHANGE, symbol=oi.SYMBOL)
    with pytest.raises(ValueError, match='cover'):
        state.configure(options, START - 1, NOW, [route])
    with pytest.raises(ValueError, match='route'):
        state.configure(options, START, NOW, [])
    with pytest.raises(ValueError, match='stale limit'):
        state.configure(options | {'max_age_ms': 0}, START, NOW, [route])
    assert state.enabled is False


def test_disabled_reconfiguration_clears_previously_visible_observations():
    dataset_id = oi.save_dataset(_dataset())
    state = oi.OpenInterestState()
    route = SimpleNamespace(exchange=oi.EXCHANGE, symbol=oi.SYMBOL)
    state.configure({'mode': 'historical', 'dataset_id': dataset_id}, START, NOW, [route])
    state.advance(START + oi.AVAILABILITY_LAG_MS)
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is not None
    state.configure({'mode': 'disabled', 'dataset_id': dataset_id}, START, NOW, [route])
    assert state.enabled is False
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is None


def test_current_snapshot_records_receipt_and_does_not_manufacture_quote_value(monkeypatch):
    monkeypatch.setattr(oi.requests, 'get', lambda *args, **kwargs: _Response({
        'symbol': 'BTCUSDT', 'time': NOW - 200, 'openInterest': '123.45',
    }))
    row = oi.get_current()
    assert row['quantity_base'] == 123.45
    assert row['available_at'] == NOW
    assert row['observed_at'] == NOW - 200
    assert row['value_quote'] is None
    assert row['cashflow'] is False
    with pytest.raises(ValueError, match='Only Binance'):
        oi.get_current('ETH-USDT')
    monkeypatch.setattr(oi.requests, 'get', lambda *args, **kwargs: _Response({
        'symbol': 'BTCUSDT', 'time': NOW - 60_001, 'openInterest': '123.45',
    }))
    with pytest.raises(ValueError, match='stale'):
        oi.get_current()


@pytest.mark.parametrize('mutation', [
    {'observations': []},
    {'source': 'unknown'},
    {'observations': [_observation(), _observation()]},
    {'observations': [_observation() | {'available_at': START}]},
    {'observations': [_observation() | {'exchange': 'Other exchange'}]},
])
def test_invalid_snapshot_is_not_persisted(mutation):
    with pytest.raises(ValueError):
        oi.save_dataset(_dataset() | mutation)
    assert oi.list_datasets() == []


class _ArchiveResponse(_Response):
    def __init__(self, content=b'', status=200):
        super().__init__(None)
        self.content = content
        self.status_code = status
        self.headers = {'Last-Modified': 'Wed, 18 Mar 2026 12:30:27 GMT'}

    @property
    def text(self):
        return self.content.decode()

    def raise_for_status(self):
        if self.status_code >= 400:
            raise oi.requests.HTTPError(f'HTTP {self.status_code}')


def _archive_zip(day, *, duplicate=False, conflict=False, include_next_midnight=False, quantity='20000'):
    # Exact audited Binance daily metrics field names. Old files contain exact
    # duplicate rows; a different OI value at the same label must never be chosen.
    start = int(datetime.strptime(day, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp() * 1000)
    rows = ['create_time,symbol,sum_open_interest,sum_open_interest_value']
    for timestamp in range(start, start + oi.DAY_MS + (oi.PERIOD_MS if include_next_midnight else 0), oi.PERIOD_MS):
        label = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        rows.append(f'{label},BTCUSDT,{quantity},200000000')
        if duplicate:
            rows.append(f'{label},BTCUSDT,{"21000" if conflict else quantity},200000000')
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(f'BTCUSDT-metrics-{day}.csv', '\n'.join(rows))
    return output.getvalue()


def _archive_http(monkeypatch, payloads, *, checksum_corrupt=False):
    calls = []
    xml = (f'<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">'
           f'<Contents><Key>{oi.ARCHIVE_PREFIX}BTCUSDT-metrics-2020-09-01.zip</Key>'
           '<LastModified>2026-03-18T12:30:27Z</LastModified></Contents></ListBucketResult>').encode()
    monkeypatch.setattr(oi.requests, 'get', lambda *args, **kwargs: _ArchiveResponse(xml))

    class Client:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def get(self, url, timeout, params=None):
            calls.append(url)
            if url.endswith('/futures/data/openInterestHist'):
                labels = range(params['startTime'], params['endTime'] + 1, oi.PERIOD_MS)
                return _Response([_vendor_row(timestamp) for timestamp in labels])
            filename = url.rsplit('/', 1)[-1].removesuffix('.CHECKSUM')
            day = filename.removeprefix('BTCUSDT-metrics-').removesuffix('.zip')
            payload = payloads.get(day)
            if payload is None:
                return _ArchiveResponse(status=404)
            if url.endswith('.CHECKSUM'):
                checksum = '0' * 64 if checksum_corrupt else sha256(payload).hexdigest()
                return _ArchiveResponse(f'{checksum}  {filename}'.encode())
            return _ArchiveResponse(payload)

    monkeypatch.setattr(oi.requests, 'Session', Client)
    return calls


def test_archive_catalog_and_verified_duplicate_rows_provide_2020_history(monkeypatch):
    day = '2020-09-01'
    start = 1_598_918_400_000
    calls = _archive_http(monkeypatch, {day: _archive_zip(day, duplicate=True)})
    progress = []
    result = oi.import_binance_history(start, start + oi.DAY_MS, source='archive',
                                      allow_archive_assumptions=True, progress_callback=progress.append)
    assert result['source'] == oi.ARCHIVE_SOURCE
    assert result['observation_count'] == 288
    assert result['archive_identical_duplicate_rows'] == 288
    assert result['archive_verified_file_count'] == 1
    assert result['status'] == 'ready'
    assert result['point_in_time_certified'] is False
    assert result['original_publication_known'] is False
    assert result['archive_catalog']['first_archive_date'] == day
    assert 'archive_files' not in result  # Metadata stays bounded for multi-year MCP results.
    dataset = oi.load_dataset(result['dataset_id'])
    manifest = dataset['archive_files'][0]
    assert manifest['sha256'] == sha256(_archive_zip(day, duplicate=True)).hexdigest()
    assert manifest['checksum_last_modified'] == 'Wed, 18 Mar 2026 12:30:27 GMT'
    assert progress[-1]['phase'] == 'complete'
    assert progress[-1]['fetched_days'] == progress[-1]['total_days'] == 1
    assert len(calls) == 2


def test_archive_requires_explicit_assumptions_and_refuses_before_first_published_date(monkeypatch):
    _archive_http(monkeypatch, {})
    start = 1_598_918_400_000
    with pytest.raises(ValueError, match='allow_archive_assumptions'):
        oi.import_binance_history(start, start + oi.DAY_MS, source='archive')
    with pytest.raises(ValueError, match='begins 2020-09-01'):
        oi.import_binance_history(start - oi.DAY_MS, start + oi.DAY_MS, source='archive',
                                 allow_archive_assumptions=True)


def test_archive_cache_reuses_only_checksum_verified_content(monkeypatch):
    day = '2020-09-01'
    start = 1_598_918_400_000
    payload = _archive_zip(day)
    calls = _archive_http(monkeypatch, {day: payload})
    first = oi.import_binance_history(start, start + oi.DAY_MS, source='archive', allow_archive_assumptions=True)
    second = oi.import_binance_history(start, start + oi.DAY_MS, source='archive', allow_archive_assumptions=True)
    assert first['dataset_id'] == second['dataset_id']
    assert sum(url.endswith('.zip') for url in calls) == 1
    assert sum(url.endswith('.CHECKSUM') for url in calls) == 2
    cache = oi._root() / 'archives' / f'{sha256(payload).hexdigest()}.zip'
    cache.write_bytes(b'corrupt')
    with pytest.raises(ValueError, match='checksum'):
        oi.import_binance_history(start, start + oi.DAY_MS, source='archive', allow_archive_assumptions=True)


@pytest.mark.parametrize('conflict, checksum_corrupt, message', [
    (True, False, 'Conflicting'), (False, True, 'checksum'),
])
def test_conflicting_or_corrupt_archives_never_publish_a_dataset(monkeypatch, conflict, checksum_corrupt, message):
    day = '2020-09-01'
    start = 1_598_918_400_000
    _archive_http(monkeypatch, {day: _archive_zip(day, duplicate=True, conflict=conflict)},
                  checksum_corrupt=checksum_corrupt)
    with pytest.raises(ValueError, match=message):
        oi.import_binance_history(start, start + oi.DAY_MS, source='archive', allow_archive_assumptions=True)
    assert oi.list_datasets() == []


def test_archive_cross_day_boundary_conflicts_are_never_silently_deduplicated(monkeypatch):
    start = 1_598_918_400_000
    _archive_http(monkeypatch, {'2020-09-01': _archive_zip('2020-09-01', include_next_midnight=True),
                               '2020-09-02': _archive_zip('2020-09-02', quantity='21000')})
    with pytest.raises(ValueError, match='across daily archives'):
        oi.import_binance_history(start, start + 2 * oi.DAY_MS, source='archive', allow_archive_assumptions=True)
    assert oi.list_datasets() == []


def test_archive_missing_day_is_explicit_and_update_preserves_original_snapshot(monkeypatch):
    start = 1_598_918_400_000
    payloads = {'2020-09-01': _archive_zip('2020-09-01')}
    _archive_http(monkeypatch, payloads)
    first = oi.import_binance_history(start, start + oi.DAY_MS, source='archive', allow_archive_assumptions=True)
    result = oi.update_dataset(first['dataset_id'], start + 2 * oi.DAY_MS)
    assert result['status'] == 'incomplete'
    assert result['archive_missing_days'] == ['2020-09-02']
    assert result['missing_observation_count'] == 288
    assert oi.load_dataset(first['dataset_id'])['finish'] == start + oi.DAY_MS


def test_archive_update_rejects_changed_publisher_checksum_even_if_overlap_oi_is_equal(monkeypatch):
    start = 1_598_918_400_000
    payloads = {'2020-09-01': _archive_zip('2020-09-01')}
    _archive_http(monkeypatch, payloads)
    first = oi.import_binance_history(start, start + oi.DAY_MS, source='archive', allow_archive_assumptions=True)
    # Identical OI values but a replaced ZIP (now with duplicate rows) are still
    # a different source version, not a silently accepted extension of the old one.
    payloads['2020-09-01'] = _archive_zip('2020-09-01', duplicate=True)
    payloads['2020-09-02'] = _archive_zip('2020-09-02')
    with pytest.raises(ValueError, match='revised an existing OI archive'):
        oi.update_dataset(first['dataset_id'], start + 2 * oi.DAY_MS)
    assert len(oi.list_datasets()) == 1


def test_auto_policy_and_retrospective_evidence_survive_archive_only_initial_window(monkeypatch):
    start = 1_598_918_400_000
    _archive_http(monkeypatch, {'2020-09-01': _archive_zip('2020-09-01'),
                               '2020-09-02': _archive_zip('2020-09-02')})
    first = oi.import_binance_history(start, start + oi.DAY_MS, source='auto', allow_archive_assumptions=True)
    assert first['source'] == oi.ARCHIVE_SOURCE
    assert first['import_source'] == 'auto'
    updated = oi.update_dataset(first['dataset_id'], start + 2 * oi.DAY_MS)
    assert updated['import_source'] == 'auto'
    assert updated['observation_count'] == 576
    state = oi.OpenInterestState()
    route = SimpleNamespace(exchange=oi.EXCHANGE, symbol=oi.SYMBOL)
    state.configure({'mode': 'historical', 'dataset_id': updated['dataset_id']}, start,
                    start + 2 * oi.DAY_MS, [route])
    state.advance(start + oi.AVAILABILITY_LAG_MS - 1)
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is None
    state.advance(start + oi.AVAILABILITY_LAG_MS)
    assert state.current(oi.EXCHANGE, oi.SYMBOL).quantity_base == 20000
    assert state.snapshot()['availability_policy'].startswith('retrospective_archive')
    assert state.snapshot()['data']['point_in_time_certified'] is False


def test_auto_merges_verified_archives_and_recent_rest_without_gaps(monkeypatch):
    cutoff = ((NOW - 29 * oi.DAY_MS) // oi.DAY_MS) * oi.DAY_MS
    start, finish = cutoff - oi.DAY_MS, cutoff + oi.DAY_MS
    day = datetime.fromtimestamp(start / 1000, tz=timezone.utc).strftime('%Y-%m-%d')
    _archive_http(monkeypatch, {day: _archive_zip(day)})
    result = oi.import_binance_history(start, finish, source='auto', allow_archive_assumptions=True)
    assert result['source'] == oi.AUTO_SOURCE
    assert result['observation_count'] == 576
    assert result['status'] == 'ready'
    assert result['rest_range'] == {'start': cutoff, 'finish': finish}
    assert result['archive_verified_file_count'] == 1


def test_archive_cancellation_preserves_cache_and_does_not_publish_incomplete_snapshot(monkeypatch):
    start = 1_598_918_400_000
    days = ['2020-09-01', '2020-09-02', '2020-09-03', '2020-09-04', '2020-09-05']
    calls = _archive_http(monkeypatch, {day: _archive_zip(day) for day in days})

    def cancel(progress):
        if progress['phase'] == 'archive' and progress['fetched_days'] == 1:
            raise RuntimeError('cancelled by job')

    with pytest.raises(RuntimeError, match='cancelled by job'):
        oi.import_binance_history(start, start + 5 * oi.DAY_MS, source='archive',
                                 allow_archive_assumptions=True, progress_callback=cancel)
    assert oi.list_datasets() == []
    assert list((oi._root() / 'archives').glob('*.zip'))
    assert sum(url.endswith('.zip') for url in calls) <= oi.ARCHIVE_WORKERS


def test_archive_gaps_require_explicit_consumption_acknowledgement_and_remain_none(monkeypatch):
    start = 1_598_918_400_000
    _archive_http(monkeypatch, {'2020-09-01': _archive_zip('2020-09-01')})
    result = oi.import_binance_history(start, start + 2 * oi.DAY_MS, source='archive',
                                      allow_archive_assumptions=True)
    assert result['missing_observation_count'] == 288
    options = {'mode': 'historical', 'dataset_id': result['dataset_id']}
    state = oi.OpenInterestState()
    routes = [SimpleNamespace(exchange=oi.EXCHANGE, symbol=oi.SYMBOL)]
    with pytest.raises(ValueError, match='allow_missing_observations=True'):
        state.configure(options, start, start + 2 * oi.DAY_MS, routes)
    state.configure(options | {'allow_missing_observations': True}, start, start + 2 * oi.DAY_MS, routes)
    state.advance(start + oi.AVAILABILITY_LAG_MS)
    assert state.current(oi.EXCHANGE, oi.SYMBOL).quantity_base == 20000
    state.advance(start + oi.DAY_MS + oi.AVAILABILITY_LAG_MS + oi.DEFAULT_MAX_AGE_MS)
    assert state.current(oi.EXCHANGE, oi.SYMBOL) is None
    assert state.snapshot()['allow_missing_observations'] is True
