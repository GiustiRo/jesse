"""Pure local live-input/reconciliation tests: no account, sessions or orders on a venue."""

from copy import deepcopy
from types import SimpleNamespace

import pytest

from jesse.store import store
from jesse_live.binance import BinanceFuturesClient
from jesse_live.exchange import BinancePerpetualFuturesDriver
from jesse_live import funding
from jesse_live.funding import LiveFunding, read_live_funding_status, validate_live_features


NOW = 1_700_000_000_000
SESSION = '55f5a885-dc0e-4054-803d-640422a335e7'
EXCHANGE = 'Binance Perpetual Futures'


class Client:
    def __init__(self):
        self.now = NOW
        self.rows = []
        self.calls = []
        self.fail_public = False
        self.fail_income = False

    def premium_index(self, symbol):
        self.calls.append(('premium', symbol))
        if self.fail_public:
            raise RuntimeError('private vendor response must not be persisted')
        return {'symbol': 'BTCUSDT', 'lastFundingRate': '.0001', 'markPrice': '10000',
                'time': self.now, 'nextFundingTime': self.now + 8 * 3_600_000}

    def open_interest(self, symbol):
        self.calls.append(('interest', symbol))
        return {'symbol': 'BTCUSDT', 'openInterest': '1234.56', 'time': self.now}

    def latest_funding_settlements(self, symbol):
        self.calls.append(('settled', symbol))
        return [{'symbol': 'BTCUSDT', 'fundingTime': self.now - 60_000,
                 'fundingRate': '-.0002'}]

    def funding_income(self, symbol, start, finish):
        self.calls.append(('income', symbol, start, finish))
        if self.fail_income:
            raise RuntimeError('private vendor response must not be persisted')
        return deepcopy(self.rows)


def income(identity='123', amount='-1.00000000', stamp=NOW):
    # Binance documents signed cashflows and tranId identity for FUNDING_FEE.
    return {'symbol': 'BTCUSDT', 'incomeType': 'FUNDING_FEE', 'income': amount,
            'asset': 'USDT', 'time': stamp, 'tranId': identity}


@pytest.fixture
def setup(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(funding.time, 'time', lambda: NOW / 1000)
    position = SimpleNamespace(_funding_rate=None, _mark_price=None, _next_funding_timestamp=None,
                               _funding_rate_timestamp=None, _open_interest=None,
                               _open_interest_timestamp=None,
                               exchange=SimpleNamespace(assets={'USDT': 10_000}))
    client = Client()
    manager = LiveFunding(SESSION, NOW - 60_000, True, True, account_key='test-account')
    return manager, client, position


def test_live_sources_publish_decimal_estimate_and_base_open_interest(setup):
    manager, client, position = setup
    assert manager.refresh(client, position, NOW)
    assert position._funding_rate == .0001
    assert position._mark_price == 10_000
    assert position._next_funding_timestamp == NOW + 8 * 3_600_000
    assert position._settled_funding_rate == -.0002
    assert position._settled_funding_timestamp == NOW - 60_000
    assert position._open_interest == 1234.56
    assert manager.snapshot()['rate_kind'] == 'estimate'
    assert manager.interest_snapshot()['units'] == 'BTC'
    assert read_live_funding_status(SESSION)['status'] == 'ready'
    client.now += 10_000
    assert manager.refresh(client, position, NOW + 10_000)
    assert len(client.calls) == 4  # Public 30s, income 60s; not every live-loop tick.


@pytest.mark.parametrize('amount', ['-1.00000000', '1.00000000'])
def test_reconcile_never_debits_wallet_and_is_durable_idempotent(setup, amount):
    manager, client, position = setup
    client.rows = [income(amount=amount), income(amount=amount)]
    assert manager.refresh(client, position, NOW)
    assert position.exchange.assets['USDT'] == 10_000
    state = read_live_funding_status(SESSION, include_ledger=True)
    assert state['event_count'] == 1
    assert state['cashflow'] == float(amount)
    assert state['wallet_debit_applied'] is False
    assert state['account_scope'] is True
    restarted = LiveFunding(SESSION, NOW + 60_000, True, True, account_key='test-account')
    assert restarted.payload['started_at'] == NOW - 60_000
    client.now += 60_000
    client.rows = [income(amount=str(float(amount)))]
    assert restarted.refresh(client, position, client.now)
    assert restarted.snapshot()['event_count'] == 1


def test_public_failure_cannot_be_hidden_by_successful_income_poll(setup):
    manager, client, position = setup
    assert manager.refresh(client, position, NOW)
    client.fail_public = True
    client.now += 60_000
    assert not manager.refresh(client, position, client.now)
    assert manager.snapshot()['status'] == 'error'
    assert manager.snapshot()['error'] == 'RuntimeError'
    assert position._funding_rate is None
    assert 'private vendor' not in manager.path.read_text()


def test_income_failure_blocks_entries_until_reconciliation_recovers(setup):
    manager, client, position = setup
    client.fail_income = True
    assert not manager.refresh(client, position, NOW)
    client.now += 30_000
    assert not manager.refresh(client, position, client.now)
    client.fail_income = False
    client.now += 30_000
    assert manager.refresh(client, position, client.now)
    assert manager.snapshot()['status'] == 'ready'


def test_stale_observation_is_invalidated_and_reported_after_process_stops(setup, monkeypatch):
    manager, client, position = setup
    assert manager.refresh(client, position, NOW)
    monkeypatch.setattr(funding.time, 'time', lambda: (NOW + 100_000) / 1000)
    state = read_live_funding_status(SESSION)
    assert state['status'] == 'stale'
    assert state['open_interest']['status'] == 'stale'
    assert not manager.refresh(client, position, NOW + 100_000)
    assert position._funding_rate is None
    assert position._open_interest is None


@pytest.mark.parametrize('patch', [
    {'incomeType': 'COMMISSION'}, {'asset': 'BTC'}, {'symbol': 'ETHUSDT'},
    {'income': 'NaN'}, {'income': 'Infinity'}, {'income': '1e999'},
    {'time': NOW + 1}, {'tranId': '../oops'},
])
def test_malformed_income_does_not_advance_durable_cursor(setup, patch):
    manager, client, position = setup
    client.rows = [income() | patch]
    assert not manager.refresh(client, position, NOW)
    assert manager.snapshot()['event_count'] == 0
    assert manager.snapshot()['last_reconciled_at'] is None
    assert read_live_funding_status(SESSION, include_ledger=True)['ledger'] == []


def test_conflicting_transactions_are_not_overwritten(setup):
    manager, client, position = setup
    client.rows = [income()]
    assert manager.refresh(client, position, NOW)
    client.now += 60_000
    client.rows = [income(amount='-2')]
    assert not manager.refresh(client, position, client.now)
    assert manager.snapshot()['cashflow'] == -1
    assert manager.snapshot()['last_reconciled_at'] == NOW


def test_journal_write_failure_keeps_payments_recoverable(setup, monkeypatch):
    manager, client, position = setup
    assert manager.refresh(client, position, NOW)
    old = manager.path.read_bytes()
    original_write = funding._write

    def cannot_write(*args):
        raise OSError('disk full')

    monkeypatch.setattr(funding, '_write', cannot_write)
    client.rows = [income()]
    client.now += 60_000
    assert not manager.refresh(client, position, client.now)
    assert manager.path.read_bytes() == old
    assert manager.snapshot()['last_reconciled_at'] == NOW
    assert manager.snapshot()['event_count'] == 0
    monkeypatch.setattr(funding, '_write', original_write)
    restarted = LiveFunding(SESSION, client.now, True, True, account_key='test-account')
    assert restarted.refresh(client, position, client.now)
    assert restarted.snapshot()['event_count'] == 1


def test_account_identity_cannot_mix_journals(setup):
    manager, client, position = setup
    assert manager.refresh(client, position, NOW)
    with pytest.raises(ValueError, match='another account'):
        LiveFunding(SESSION, NOW, True, True, account_key='another-account')


def test_long_recovery_gap_is_not_presented_as_complete(setup):
    manager, client, position = setup
    manager.payload['started_at'] = NOW - funding.RETENTION_MS - 1
    assert not manager.refresh(client, position, NOW)
    assert 'three-month retention' in manager.snapshot()['error']
    assert not any(call[0] == 'income' for call in client.calls)


def test_saturated_income_window_is_bisected_without_losing_ties(setup):
    manager, _, _ = setup
    calls = []

    class Dense:
        def funding_income(self, symbol, start, finish):
            calls.append((start, finish))
            return [income()] * 1000 if (start, finish) == (10, 20) else [str(start)]

    assert manager._income_rows(Dense(), 10, 20) == ['10', '16']
    assert calls == [(10, 20), (10, 15), (16, 20)]


def test_private_client_routes_require_keys_and_explicit_income_filter(monkeypatch):
    client = object.__new__(BinanceFuturesClient)
    client.api_key, client.api_secret = '', b''
    with pytest.raises(ValueError, match='authenticated'):
        client.funding_income('BTC-USDT', NOW - 1, NOW)
    client.api_key, client.api_secret = 'test', b'test'
    calls = []
    monkeypatch.setattr(client, '_signed', lambda *args: calls.append(args) or [])
    assert client.funding_income('BTC-USDT', NOW - 1, NOW) == []
    assert calls == [('GET', '/fapi/v1/income', {
        'symbol': 'BTCUSDT', 'incomeType': 'FUNDING_FEE', 'startTime': NOW - 1,
        'endTime': NOW, 'limit': 1000,
    })]


@pytest.mark.parametrize('mode', ['papertrade', 'backtest'])
def test_paper_does_not_consume_real_account_funding(mode):
    with pytest.raises(ValueError, match='paper mode'):
        validate_live_features({'funding': {'mode': 'live'}}, mode, EXCHANGE, [{'symbol': 'BTC-USDT'}])


def test_disabled_features_preserve_existing_configuration():
    assert validate_live_features({}, 'papertrade', EXCHANGE, []) == (False, False)
    with pytest.raises(ValueError, match='disabled or live'):
        validate_live_features({'funding': {'mode': 'historical'}}, 'livetrade', EXCHANGE, [])


def test_entry_guard_preserves_protective_reduce_only_orders(monkeypatch):
    store.reset()
    try:
        driver = object.__new__(BinancePerpetualFuturesDriver)
        calls = []
        driver.client = SimpleNamespace(place_order=lambda payload: calls.append(payload) or {'orderId': 123})
        monkeypatch.setattr('jesse_live.exchange.allow_trading', lambda: True)
        store.app.session_info['funding'] = {'mode': 'live', 'status': 'stale'}
        with pytest.raises(ValueError, match='New entry blocked'):
            driver._maybe_place({'reduceOnly': 'false'})
        assert driver._maybe_place({'reduceOnly': 'true'}) == '123'
        assert calls == [{'reduceOnly': 'true'}]
    finally:
        store.reset()


def test_storage_identity_cannot_escape_session_directory():
    with pytest.raises(ValueError):
        read_live_funding_status('../secrets')


def test_settlement_boundary_forces_refresh_before_poll_cadence(setup, monkeypatch):
    manager, client, position = setup
    original = client.premium_index

    def expiring(symbol):
        row = original(symbol)
        row['nextFundingTime'] = NOW + 10_000
        return row

    monkeypatch.setattr(client, 'premium_index', expiring)
    assert manager.refresh(client, position, NOW)
    client.now += 10_000
    monkeypatch.setattr(client, 'premium_index', original)
    assert manager.refresh(client, position, client.now)
    assert len([call for call in client.calls if call[0] == 'premium']) == 2
    assert position._next_funding_timestamp > client.now


def test_live_loop_refresh_publishes_funding_and_interest_to_session_info(setup, monkeypatch):
    from jesse_live import live_mode

    manager, client, position = setup
    store.reset()
    try:
        monkeypatch.setattr(store.positions, 'get_position', lambda *args: position)
        monkeypatch.setattr(live_mode.logger, 'info', lambda *args, **kwargs: None)
        live_mode._refresh_live_inputs(manager, client, EXCHANGE, 'BTC-USDT', NOW)
        assert store.app.session_info['funding']['status'] == 'ready'
        assert store.app.session_info['open_interest']['value'] == 1234.56
    finally:
        store.reset()


def test_public_client_routes_have_no_signed_account_dependency(monkeypatch):
    client = object.__new__(BinanceFuturesClient)
    calls = []
    monkeypatch.setattr(client, '_public', lambda *args: calls.append(args) or {})
    assert client.premium_index('BTC-USDT') == {}
    assert client.open_interest('BTC-USDT') == {}
    assert client.latest_funding_settlements('BTC-USDT') == {}
    assert calls == [('/fapi/v1/premiumIndex', {'symbol': 'BTCUSDT'}),
                     ('/fapi/v1/openInterest', {'symbol': 'BTCUSDT'}),
                     ('/fapi/v1/fundingRate', {'symbol': 'BTCUSDT', 'limit': 2})]


def test_open_interest_only_mode_does_not_request_account_funding(setup):
    _, client, position = setup
    manager = LiveFunding(SESSION, NOW, False, True)
    assert manager.refresh(client, position, NOW)
    assert [call[0] for call in client.calls] == ['interest']
    assert manager.snapshot()['mode'] == 'disabled'


def test_disabled_features_perform_no_polling(setup):
    _, client, position = setup
    manager = LiveFunding(SESSION, NOW, False, False)
    assert manager.refresh(client, position, NOW)
    assert client.calls == []


def test_non_btc_live_input_route_is_refused():
    with pytest.raises(ValueError, match='BTC-USDT only'):
        validate_live_features({'open_interest': {'mode': 'live'}}, 'livetrade', EXCHANGE,
                               [{'symbol': 'ETH-USDT'}])


def test_live_settled_rate_keeps_previous_value_during_publication_delay(setup, monkeypatch):
    manager, client, position = setup
    boundary = NOW - NOW % 60_000
    monkeypatch.setattr(client, 'latest_funding_settlements', lambda symbol: [
        {'symbol': 'BTCUSDT', 'fundingTime': boundary, 'fundingRate': '.002'},
        {'symbol': 'BTCUSDT', 'fundingTime': boundary - 8 * 3_600_000, 'fundingRate': '-.001'},
    ])
    assert manager.refresh(client, position, NOW)
    assert position._settled_funding_rate == -.001
    client.now = boundary + 60_000
    assert manager.refresh(client, position, client.now)
    assert position._settled_funding_rate == .002


@pytest.mark.parametrize('history', [
    [],
    [{'symbol': 'BTCUSDT', 'fundingTime': NOW + 1, 'fundingRate': '.0001'}],
    [{'symbol': 'ETHUSDT', 'fundingTime': NOW - 60_000, 'fundingRate': '.0001'}],
    [{'symbol': 'BTCUSDT', 'fundingTime': NOW - 60_000, 'fundingRate': '.0001'},
     {'symbol': 'BTCUSDT', 'fundingTime': NOW - 60_000, 'fundingRate': '.0002'}],
])
def test_missing_or_invalid_final_rates_do_not_become_live_inputs(setup, monkeypatch, history):
    manager, client, position = setup
    monkeypatch.setattr(client, 'latest_funding_settlements', lambda symbol: history)
    assert not manager.refresh(client, position, NOW)
    assert position._funding_rate is None
    assert getattr(position, '_settled_funding_rate', None) is None


def test_changing_live_flags_requires_new_session(setup):
    manager, client, position = setup
    assert manager.refresh(client, position, NOW)
    with pytest.raises(ValueError, match='configuration changed'):
        LiveFunding(SESSION, NOW, False, True, account_key='test-account')


class ReconcileClient:
    def __init__(self):
        self.rows = []
        self.orders = {}
        self.canceled = []
        self.fail_cancel = False
        self.fail_read = False

    @staticmethod
    def to_binance_symbol(symbol):
        return symbol.replace('-', '')

    def position_mode(self):
        return {'dualSidePosition': False}

    def position_information(self, symbol):
        return self.rows

    def open_orders(self, symbol):
        return []

    def cancel_order(self, symbol, identity, **kwargs):
        self.canceled.append(identity)
        if self.fail_cancel:
            raise RuntimeError('cancel failed')
        return {'status': 'CANCELED'}

    def get_order(self, symbol, identity, **kwargs):
        if self.fail_read:
            raise RuntimeError('read failed')
        return self.orders[identity]

    def set_position(self, qty, entry=100):
        self.rows = [{'symbol': 'BTCUSDT', 'positionSide': 'BOTH', 'positionAmt': str(qty),
                      'entryPrice': str(entry if qty else 0), 'markPrice': '101',
                      'liquidationPrice': '10'}] if qty else []


@pytest.fixture
def native_position(monkeypatch):
    import jesse.helpers as jh
    from jesse.services import order_service
    from tests.test_broker import set_up_without_fee

    set_up_without_fee(is_futures_trading=True)
    position = store.positions.get_position('Sandbox', 'BTC-USDT')
    callbacks = []
    position.strategy = SimpleNamespace(
        leverage=1, timeframe='1m', name='FundingNativeTest',
        _on_updated_position=lambda order: callbacks.append((position.previous_qty, position.qty, order.status)),
    )
    # Exercise native futures-live lifecycle without database writes/network.
    # jh.is_live remains false in the unit backtest environment for persistence.
    monkeypatch.setattr(jh, 'is_livetrading', lambda: True)
    monkeypatch.setattr(order_service.logger, 'info', lambda *args, **kwargs: None)

    def create(identity, qty, side='buy', reduce_only=False, order_type='LIMIT'):
        return order_service.create_order({
            'id': identity, 'exchange_id': identity, 'exchange': 'Sandbox', 'symbol': 'BTC-USDT',
            'side': side, 'qty': qty, 'price': 100, 'type': order_type,
            'reduce_only': reduce_only,
        }, should_silent=True)

    yield position, create, callbacks
    store.reset()


def test_native_live_fills_update_position_and_close_trade(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, create, callbacks = native_position
    client = ReconcileClient()
    entry = create('100', 1)
    client.orders['100'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '100', 'updateTime': 1}
    client.set_position(1)
    assert synchronize_fills(client, 'Sandbox', 'BTC-USDT')['fills_applied'] == 1
    assert position.qty == 1
    assert position.entry_price == 100
    assert len(callbacks) == 1
    assert entry.is_executed
    assert synchronize_fills(client, 'Sandbox', 'BTC-USDT')['fills_applied'] == 0
    exit_order = create('200', -1, side='sell', reduce_only=True, order_type='STOP')
    client.orders['200'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '102', 'updateTime': 2}
    client.set_position(0)
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == 0
    assert exit_order.is_executed
    assert len(store.closed_trades.trades) == 1
    assert store.closed_trades.trades[0].pnl == 2


def test_partial_fill_reconciliation_uses_incremental_vwap_and_is_idempotent(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, create, callbacks = native_position
    client = ReconcileClient()
    entry = create('100', 1)
    client.orders['100'] = {'status': 'PARTIALLY_FILLED', 'executedQty': '.4', 'avgPrice': '100', 'updateTime': 1}
    client.set_position(.4)
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == .4
    assert entry.is_partially_filled
    assert synchronize_fills(client, 'Sandbox', 'BTC-USDT')['fills_applied'] == 0
    client.orders['100'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '106', 'updateTime': 2}
    client.set_position(1, entry=106)
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == 1
    assert position.entry_price == pytest.approx(106)
    trade = store.closed_trades._get_current_trade('Sandbox', 'BTC-USDT')
    assert trade.entry_price == pytest.approx(106)
    assert len(callbacks) == 2


def test_unexplained_account_position_is_never_adopted(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, _, callbacks = native_position
    client = ReconcileClient()
    client.set_position(2)
    with pytest.raises(ValueError, match='Unexplained venue position'):
        synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == 0
    assert callbacks == []


def test_stale_inputs_cancel_entries_and_preserve_protective_orders(native_position):
    from jesse_live.reconciliation import cancel_pending_entries, synchronize_fills

    position, create, _ = native_position
    client = ReconcileClient()
    entry = create('100', 1)
    protective = create('200', -1, side='sell', reduce_only=True, order_type='STOP')
    client.orders['100'] = {'status': 'CANCELED', 'executedQty': '0', 'updateTime': 1}
    client.orders['200'] = {'status': 'NEW', 'executedQty': '0', 'updateTime': 1}
    result = cancel_pending_entries(client, 'Sandbox', 'BTC-USDT')
    assert client.canceled == ['100']
    assert result['canceled_count'] == 1
    assert result['pending_count'] == 0
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert entry.is_canceled
    assert protective.is_active
    assert position.qty == 0


@pytest.mark.parametrize('status,amount', [('FILLED', '1'), ('CANCELED', '.4')])
def test_cancel_race_full_and_partial_fills_are_reconciled(native_position, status, amount):
    from jesse_live.reconciliation import cancel_pending_entries, synchronize_fills

    position, create, _ = native_position
    client = ReconcileClient()
    entry = create('100', 1)
    client.fail_cancel = True
    client.orders['100'] = {'status': status, 'executedQty': amount, 'avgPrice': '100', 'updateTime': 1}
    client.set_position(float(amount))
    result = cancel_pending_entries(client, 'Sandbox', 'BTC-USDT')
    assert result['pending_count'] == 0
    assert result['race_fill_count'] == 1
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == float(amount)
    assert entry.is_executed if status == 'FILLED' else entry.is_canceled


def test_failed_cancellation_stays_pending_and_blocks_recovered_feed_entry(setup, native_position, monkeypatch):
    from jesse_live.reconciliation import cancel_pending_entries

    manager, source, position = setup
    _, create, _ = native_position
    create('100', 1)
    client = ReconcileClient()
    client.fail_cancel = client.fail_read = True
    result = cancel_pending_entries(client, 'Sandbox', 'BTC-USDT')
    assert result['pending_count'] == 1
    assert result['errors'] == [{'order_id': '100', 'category': 'RuntimeError'}]
    assert manager.refresh(source, position, NOW)
    manager.record_entry_cancellations(result)
    store.app.session_info['funding'] = manager.snapshot()
    driver = object.__new__(BinancePerpetualFuturesDriver)
    monkeypatch.setattr('jesse_live.exchange.allow_trading', lambda: True)
    with pytest.raises(ValueError, match='cancellation is unconfirmed'):
        driver._maybe_place({'reduceOnly': 'false'})
    state = read_live_funding_status(SESSION)
    assert state['entry_cancellations']['pending_count'] == 1


def test_live_startup_requires_flat_and_one_way_account():
    from jesse_live.reconciliation import require_flat_start

    client = ReconcileClient()
    require_flat_start(client, 'BTC-USDT')
    client.set_position(1)
    with pytest.raises(ValueError, match='flat BTC position'):
        require_flat_start(client, 'BTC-USDT')
    client.position_mode = lambda: {'dualSidePosition': True}
    with pytest.raises(ValueError, match='one-way position mode'):
        require_flat_start(client, 'BTC-USDT')


def test_live_startup_leaves_unowned_orders_untouched():
    from jesse_live.reconciliation import require_flat_start

    client = ReconcileClient()
    client.open_orders = lambda symbol: [{'orderId': 'other-bot-entry'}]
    with pytest.raises(ValueError, match='pre-existing BTC orders'):
        require_flat_start(client, 'BTC-USDT')
    assert client.canceled == []


def test_same_poll_entry_and_exit_are_applied_in_venue_update_order(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, create, callbacks = native_position
    client = ReconcileClient()
    create('100', 1)
    create('200', -1, side='sell', reduce_only=True)
    client.orders['100'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '100', 'updateTime': 1}
    client.orders['200'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '102', 'updateTime': 2}
    assert synchronize_fills(client, 'Sandbox', 'BTC-USDT')['fills_applied'] == 2
    assert position.qty == 0
    assert len(callbacks) == 2
    assert store.closed_trades.trades[0].pnl == 2


def test_algo_execution_queries_actual_order_id_for_fill_proof(monkeypatch):
    client = object.__new__(BinanceFuturesClient)
    calls = []

    def signed(method, path, params):
        calls.append((method, path, params))
        if path.endswith('algoOrder'):
            return {'algoId': 123, 'actualOrderId': '456', 'algoStatus': 'FINISHED'}
        return {'orderId': 456, 'status': 'FILLED', 'executedQty': '.2', 'avgPrice': '100'}

    monkeypatch.setattr(client, '_signed', signed)
    remote = client.get_order('BTC-USDT', '123', is_algo=True)
    assert remote['executedQty'] == '.2'
    assert remote['actualOrderId'] == '456'
    assert calls == [('GET', '/fapi/v1/algoOrder', {'symbol': 'BTCUSDT', 'algoId': '123'}),
                     ('GET', '/fapi/v1/order', {'symbol': 'BTCUSDT', 'orderId': '456'})]


@pytest.mark.parametrize('wallet', [None, 0, -1, float('nan'), float('inf'), -float('inf'), '', {}, True])
def test_enabled_live_inputs_refuse_missing_or_invalid_wallet_without_orders(monkeypatch, wallet):
    from jesse_live import live_mode

    store.reset()
    accounting = SimpleNamespace(_wallet_balance=500, _available_margin=500, _started_balance=500,
                                 settlement_currency='USDT', assets={'USDT': 500})
    monkeypatch.setattr(store.exchanges, 'get_exchange', lambda name: accounting)
    monkeypatch.setattr(live_mode, 'allocation_pct', lambda: 10)
    calls = []
    driver = object.__new__(BinancePerpetualFuturesDriver)
    driver.client = SimpleNamespace(place_order=lambda payload: calls.append(payload))
    monkeypatch.setattr('jesse_live.exchange.allow_trading', lambda: True)
    try:
        with pytest.raises(ValueError, match='finite positive Binance wallet'):
            live_mode._apply_wallet_allocation(EXCHANGE, wallet, strict=True)
        assert accounting.assets == {'USDT': 500}
        assert accounting._wallet_balance == accounting._available_margin == accounting._started_balance == 500
        assert store.app.session_info['live_position']['status'] == 'error'
        with pytest.raises(ValueError, match='account position reconciliation failed'):
            driver._maybe_place({'reduceOnly': 'false'})
        assert calls == []
    finally:
        store.reset()


def test_enabled_live_inputs_allocate_actual_wallet_and_disabled_demo_behavior_is_preserved(monkeypatch):
    from jesse_live import live_mode

    store.reset()
    accounting = SimpleNamespace(settlement_currency='USDT', assets={'USDT': 0})
    monkeypatch.setattr(store.exchanges, 'get_exchange', lambda name: accounting)
    monkeypatch.setattr(live_mode, 'allocation_pct', lambda: 25)
    try:
        assert live_mode._apply_wallet_allocation(EXCHANGE, 20_000, strict=True) == 5000
        assert accounting.assets['USDT'] == accounting._wallet_balance == 5000
        assert live_mode._apply_wallet_allocation(EXCHANGE, None) == 1000
        assert accounting.assets['USDT'] == 1000
    finally:
        store.reset()


@pytest.mark.parametrize('percent', [0, 101, float('nan'), float('inf')])
def test_live_wallet_validation_rejects_invalid_allocation(monkeypatch, percent):
    from jesse_live import live_mode

    store.reset()
    monkeypatch.setattr(live_mode, 'allocation_pct', lambda: percent)
    try:
        with pytest.raises(ValueError, match='finite positive Binance wallet'):
            live_mode._apply_wallet_allocation(EXCHANGE, 10_000, strict=True)
    finally:
        store.reset()


def test_tied_entry_and_reduce_only_exit_never_invent_a_short_from_random_ids(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, create, callbacks = native_position
    client = ReconcileClient()
    # The exit's random Jesse ID sorts first; it cannot open a short when flat.
    create('ffffffff', 1)
    create('00000000', -1, side='sell', reduce_only=True)
    client.orders['ffffffff'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '100', 'updateTime': 1}
    client.orders['00000000'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '102', 'updateTime': 1}
    assert synchronize_fills(client, 'Sandbox', 'BTC-USDT')['fills_applied'] == 2
    assert callbacks[0][:2] == (0, 1)
    assert callbacks[1][:2] == (1, 0)
    assert position.qty == 0
    assert store.closed_trades.trades[0].type == 'long'
    assert store.closed_trades.trades[0].pnl == 2


def test_ambiguous_same_millisecond_fills_fail_before_mutating_positions(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, create, callbacks = native_position
    client = ReconcileClient()
    # Both are entries: the net flat snapshot cannot identify which opened first.
    first = create('ffffffff', 1)
    second = create('00000000', -1, side='sell')
    client.orders['ffffffff'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '100', 'updateTime': 1}
    client.orders['00000000'] = {'status': 'FILLED', 'executedQty': '1', 'avgPrice': '102', 'updateTime': 1}
    with pytest.raises(ValueError, match='Ambiguous same-millisecond'):
        synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == 0
    assert first.is_active and second.is_active
    assert callbacks == []
    assert store.closed_trades.count == 0


def test_decimal_reduce_fills_close_exactly_without_phantom_short(native_position):
    from jesse_live.reconciliation import synchronize_fills

    position, create, callbacks = native_position
    client = ReconcileClient()
    create('100', .3)
    client.orders['100'] = {'status': 'FILLED', 'executedQty': '.3', 'avgPrice': '100', 'updateTime': 1}
    client.set_position(.3)
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    create('200', -.1, side='sell', reduce_only=True)
    create('300', -.2, side='sell', reduce_only=True)
    client.orders['200'] = {'status': 'FILLED', 'executedQty': '.1', 'avgPrice': '102', 'updateTime': 2}
    client.orders['300'] = {'status': 'FILLED', 'executedQty': '.2', 'avgPrice': '102', 'updateTime': 3}
    client.set_position(0)
    synchronize_fills(client, 'Sandbox', 'BTC-USDT')
    assert position.qty == 0
    assert callbacks[-1][:2] == (.2, 0)
    assert len(store.closed_trades.trades) == 1
    assert store.closed_trades.trades[0].type == 'long'
    assert store.closed_trades.trades[0].pnl == pytest.approx(.6)
