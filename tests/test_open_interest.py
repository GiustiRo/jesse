"""Vendor-boundary and asof tests; no exchange account or real network is used."""

from dataclasses import asdict
from types import SimpleNamespace

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
