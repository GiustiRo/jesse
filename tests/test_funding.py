"""Deterministic public-data and minute-engine funding accounting regressions."""

from dataclasses import asdict
from types import SimpleNamespace

import numpy as np
import pytest

from jesse import research
from jesse.config import reset_config
from jesse.exceptions import InsufficientMargin
from jesse.models import ClosedTrade
from jesse.services import funding
from jesse.store import store
from jesse.strategies import Strategy


START = 1_577_836_800_000
EXCHANGE = funding.EXCHANGE


@pytest.fixture(autouse=True)
def clean_state(tmp_path, monkeypatch):
    store.reset()
    reset_config()
    monkeypatch.setattr(funding, '_root', lambda: tmp_path / 'funding')
    yield
    store.reset()
    reset_config()


def dataset(events, finish=START + 15 * 60_000):
    rows = [asdict(funding.FundingEvent(EXCHANGE, 'BTC-USDT', time, rate, mark))
            for time, rate, mark in events]
    return funding.save_dataset({'schema': 1, 'source': funding.SOURCE, 'exchange': EXCHANGE,
                                'symbol': 'BTC-USDT', 'start': START, 'finish': finish, 'events': rows})


def configure(dataset_id, start=START, finish=START + 15 * 60_000):
    state = funding.FundingState()
    state.configure({'mode': 'historical', 'dataset_id': dataset_id}, start, finish,
                    [SimpleNamespace(exchange=EXCHANGE, symbol='BTC-USDT')])
    return state


class _PartialFunding(Strategy):
    direction = 1

    def should_long(self):
        return self.index == 0 and self.direction == 1

    def should_short(self):
        return self.index == 0 and self.direction == -1

    def go_long(self):
        self.buy = 2, self.price

    def go_short(self):
        self.sell = 2, self.price

    def on_open_position(self, order):
        self.take_profit = [(1, 100 + self.direction), (1, 100 + 2 * self.direction)]

    def should_cancel_entry(self):
        return False

    def before(self):
        if self.index == 2:
            assert self.settled_funding_rate is None
        if self.index == 3:
            assert self.settled_funding_rate == .01
            assert self.settled_funding_timestamp == START + 3 * 60_000
            assert self.get_funding_history()[-1]['rate_decimal'] == .01
            assert all(row['available_at'] <= self.time for row in self.get_funding_history())
        if self.index == 7:
            assert self.settled_funding_rate == .01
        if self.index == 8:
            assert self.settled_funding_rate == -.01

    def on_close_position(self, order, closed_trade):
        assert closed_trade.funding == -self.direction
        assert closed_trade.pnl == pytest.approx(self.balance - 10_000)
        assert closed_trade.pnl == pytest.approx(3 - self.direction - closed_trade.fee)
        assert [row['qty'] for row in store.funding.ledger] == [2 * self.direction, self.direction]
        assert closed_trade.to_dict['funding'] == closed_trade.funding
        assert closed_trade.to_json['funding'] == closed_trade.funding


def run(strategy, dataset_id=None, fast=False, sparse_other=False, prices=None):
    config = {'starting_balance': 10_000, 'fee': .00045, 'type': 'futures',
              'futures_leverage': 3, 'futures_leverage_mode': 'isolated',
              'exchange': EXCHANGE, 'warm_up_candles': 0}
    if dataset_id:
        config['funding'] = {'mode': 'historical', 'dataset_id': dataset_id}
    direction = getattr(strategy, 'direction', 1)
    prices = prices or [100] * 5 + [100 + direction] * 5 + [100 + 2 * direction] * 5
    rows = np.array([[START + i * 60_000, p, p, p, p, 10] for i, p in enumerate(prices)], dtype=float)
    candles = {f'{EXCHANGE}-BTC-USDT': {'exchange': EXCHANGE, 'symbol': 'BTC-USDT', 'candles': rows}}
    data_routes = []
    if sparse_other:
        data_routes = [{'exchange': EXCHANGE, 'symbol': 'ETH-USDT', 'timeframe': '1m'}]
        candles[f'{EXCHANGE}-ETH-USDT'] = {'exchange': EXCHANGE, 'symbol': 'ETH-USDT', 'candles': rows[[0, 4, 14]].copy()}
    return research.backtest(config, [{'exchange': EXCHANGE, 'symbol': 'BTC-USDT',
                                       'timeframe': '1m', 'strategy': strategy}],
                             data_routes, candles, fast_mode=fast, generate_equity_curve=True)


@pytest.mark.parametrize('direction', [1, -1])
@pytest.mark.parametrize('fast', [False, True])
@pytest.mark.parametrize('sparse_other', [False, True])
def test_partial_long_short_wallet_trade_ledger_and_causal_access(direction, fast, sparse_other):
    identifier = dataset([(START + 3 * 60_000, .01, 100), (START + 8 * 60_000, -.01, 100)])
    strategy = type('PartialFunding', (_PartialFunding,), {'direction': direction})
    result = run(strategy, identifier, fast, sparse_other)
    evidence = result['metrics']['funding']
    assert evidence['cashflow'] == -direction
    assert evidence['event_count'] == 2
    assert evidence['effective_fast_mode'] is False
    assert evidence['dataset_id'] == identifier


class _BoundaryFunding(Strategy):
    def should_long(self):
        return self.index == 2

    def go_long(self):
        self.buy = 2, self.price

    def update_position(self):
        if self.index == 7:
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def on_close_position(self, order, closed_trade):
        assert closed_trade.funding == -2
        assert self.balance - 10_000 == pytest.approx(closed_trade.pnl)


def test_entry_at_settlement_does_not_pay_but_exit_at_next_settlement_does():
    identifier = dataset([(START + 3 * 60_000, .01, 100), (START + 8 * 60_000, .01, 100)])
    result = run(_BoundaryFunding, identifier, prices=[100] * 15)
    assert result['metrics']['funding']['event_count'] == 1
    assert result['metrics']['funding']['ledger'][0]['settled_at'] == START + 8 * 60_000


class _Observer(Strategy):
    def should_long(self):
        return False

    def go_long(self):
        pass

    def should_cancel_entry(self):
        return False


def test_no_trade_session_records_applied_with_zero_cashflow():
    identifier = dataset([(START, .01, 100)])
    result = run(_Observer, identifier)
    assert result['metrics']['funding']['applied'] is True
    assert result['metrics']['funding']['cashflow'] == 0
    assert result['metrics']['funding']['ledger'] == []


def test_disabled_shape_and_no_funding_trade_roundtrip_loss():
    result = run(_Observer)
    assert not result['metrics'] or 'funding' not in result['metrics']
    assert ClosedTrade({'funding': -1.25}).funding == -1.25


def test_timestamp_jitter_retained_but_rate_delayed_one_minute():
    identifier = dataset([(START + 1, .0001, 10_000)])
    state = configure(identifier)
    state.settle(START, store)
    assert state.known == {}
    state.settle(START + 60_000, store)
    event = state.known[(EXCHANGE, 'BTC-USDT')]
    assert event.settled_at == START + 1
    assert event.available_at == START + 60_000


@pytest.mark.parametrize('events,match', [
    ([(START, .01, 100), (START, .02, 100)], 'Duplicate'),
    ([(START, .01, 100), (START + 1, .01, 100)], 'one execution minute'),
    ([(START - 1, .01, 100)], 'outside'),
    ([(START + 2000, .01, 100)], 'finer execution'),
])
def test_bad_settlement_clock_is_refused(events, match):
    with pytest.raises(ValueError, match=match):
        configure(dataset(events))


def test_gap_or_short_coverage_is_not_zero_filled():
    identifier = dataset([(START, .01, 100)], finish=START + 24 * 3_600_000)
    with pytest.raises(ValueError, match='gap'):
        configure(identifier)
    identifier = dataset([(START, .01, 100)])
    with pytest.raises(ValueError, match='cover'):
        configure(identifier, finish=START + 24 * 3_600_000)


def test_checksum_and_path_confinement():
    identifier = dataset([(START, .01, 100)])
    assert funding.save_dataset(funding.load_dataset(identifier)) == identifier
    funding._path(identifier).write_text('{}')
    with pytest.raises(ValueError, match='checksum'):
        funding.load_dataset(identifier)
    with pytest.raises(ValueError):
        funding.load_dataset('../outside')


def test_settlement_finish_is_exclusive():
    identifier = dataset([(START + 3 * 60_000, .01, 100)])
    state = configure(identifier, finish=START + 3 * 60_000)
    state.settle(START + 3 * 60_000, store)
    assert state.index == 0
    assert state.latest == {}


def test_rate_fraction_unit_and_sign_with_mock_engine():
    for qty, rate, expected in [(1, .0001, -1), (-1, .0001, 1), (1, -.0001, 1), (-1, -.0001, -1)]:
        state = configure(dataset([(START, rate, 10_000)]))
        trade = SimpleNamespace(id='trade', funding=0)
        cash = []
        position = SimpleNamespace(is_open=True, qty=qty, exchange=SimpleNamespace(
            apply_funding=lambda amount, position: cash.append(amount)))
        fake = SimpleNamespace(positions=SimpleNamespace(get_position=lambda *args: position),
                               closed_trades=SimpleNamespace(_get_current_trade=lambda *args: trade))
        state.settle(START, fake)
        state.settle(START, fake)
        assert cash == [expected]
        assert trade.funding == expected


def test_exhausted_margin_fails_instead_of_inventing_liquidation():
    from tests import test_broker
    test_broker.set_up_without_fee(is_futures_trading=True)
    with pytest.raises(InsufficientMargin, match='Funding exhausts'):
        test_broker.exchange.apply_funding(-1001)
    assert test_broker.exchange.wallet_balance == 1000


class _Response:
    def __init__(self, rows):
        self.rows = rows

    def raise_for_status(self):
        pass

    def json(self):
        return self.rows


def test_import_pages_idempotently_without_keys_and_exclusive_end(monkeypatch):
    calls = []
    rows = [{'symbol': 'BTCUSDT', 'fundingTime': START, 'fundingRate': '.0001', 'markPrice': '10000'}]

    class Client:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def get(self, url, params, timeout):
            calls.append(params)
            return _Response(rows if params['startTime'] == START else [])

    monkeypatch.setattr(funding.requests, 'Session', Client)
    monkeypatch.setattr(funding.time, 'sleep', lambda seconds: None)
    result = funding.import_binance_history(START, START + 60_000)
    assert calls[0]['endTime'] == START + 60_000 - 1
    assert calls[1]['startTime'] == START + 1
    assert result['status'] == 'ready'
    assert result['rate_unit'] == 'decimal_fraction'
    assert funding.update_dataset(result['dataset_id'], START + 60_000)['changed'] is False


def test_old_missing_mark_requires_explicit_proxy_and_records_approximation(monkeypatch):
    calls = []

    class Client:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def get(self, url, params, timeout):
            calls.append(url)
            if url.endswith('markPriceKlines'):
                return _Response([[START, '10000', '10001', '9999', '10000']])
            if params['startTime'] == START:
                return _Response([{'symbol': 'BTCUSDT', 'fundingTime': START,
                                   'fundingRate': '.0001', 'markPrice': ''}])
            return _Response([])

    monkeypatch.setattr(funding.requests, 'Session', Client)
    monkeypatch.setattr(funding.time, 'sleep', lambda seconds: None)
    with pytest.raises(ValueError, match='allow_mark_price_proxy'):
        funding.import_binance_history(START, START + 60_000)
    result = funding.import_binance_history(START, START + 60_000, True)
    assert result['mark_price_proxy_count'] == 1
    assert result['allow_mark_price_proxy'] is True
    assert 'proxy' in result['mark_price_source']
    row = funding.load_dataset(result['dataset_id'])['events'][0]
    assert row['mark_price'] == 10_000
    assert row['mark_price_source'] == 'markPriceKlines.1h_open_proxy'


def test_multiasset_requires_explicit_unfunded_scope():
    identifier = dataset([(START, .01, 100)])
    routes = [SimpleNamespace(exchange=EXCHANGE, symbol=s) for s in ['BTC-USDT', 'PAXG-USDT']]
    state = funding.FundingState()
    with pytest.raises(ValueError, match='exclude_symbols'):
        state.configure({'mode': 'historical', 'dataset_id': identifier}, START, START + 60_000, routes)
    state.configure({'mode': 'historical', 'dataset_id': identifier, 'exclude_symbols': ['PAXG-USDT']},
                    START, START + 60_000, routes)
    assert state.snapshot()['excluded_symbols'] == ['PAXG-USDT']


class _HoldFunding(_BoundaryFunding):
    def should_long(self):
        return self.index == 0

    def update_position(self):
        pass

    def on_close_position(self, order, closed_trade):
        assert closed_trade.funding == -4
        assert self.balance - 10_000 == pytest.approx(closed_trade.pnl)


def test_terminal_close_includes_costs_but_finish_settlement_is_excluded():
    identifier = dataset([(START + n * 60_000, .01, 100) for n in (3, 14, 15)],
                         finish=START + 16 * 60_000)
    result = run(_HoldFunding, identifier, prices=[100] * 15)
    assert result['metrics']['funding']['cashflow'] == -4
