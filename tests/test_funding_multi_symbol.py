"""Per-symbol funding datasets: BTC regression, ETH import and multi-route accounting.

Vendor fixtures under tests/data/funding are recorded Binance USD-M responses,
including real quirks: millisecond settlement jitter (fundingTime ...015) and
2020 rows whose markPrice is an empty string.
"""

from dataclasses import asdict
import json
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient
import numpy as np
import pytest

from jesse import research
from jesse.config import reset_config
from jesse.controllers import funding_controller as controller
from jesse.services import funding
from jesse.services.auth import require_auth
from jesse.store import store
from jesse.strategies import Strategy
from tests import funding_regression_case as case


EXCHANGE = funding.EXCHANGE
START_2025 = 1_735_689_600_000
FINISH_2025 = 1_735_948_800_000
START_2020 = 1_577_836_800_000


@pytest.fixture(autouse=True)
def clean_state(tmp_path, monkeypatch):
    store.reset()
    reset_config()
    monkeypatch.setattr(funding, '_root', lambda: tmp_path / 'funding')
    monkeypatch.setattr(funding.time, 'sleep', lambda seconds: None)
    yield
    store.reset()
    reset_config()


def serve(monkeypatch, funding_rows: dict, mark_rows: dict | None = None):
    monkeypatch.setattr(funding.requests, 'Session', case.fake_binance_session(funding_rows, mark_rows))


def import_2025(monkeypatch, symbol: str) -> str:
    vendor = symbol.replace('-', '')
    rows = case.load_fixture(f'binance_fundingRate_{vendor}_20250101_20250104.json')
    serve(monkeypatch, {vendor: rows})
    return funding.import_binance_history(START_2025, FINISH_2025, symbol=symbol)['dataset_id']


def route(symbol):
    return SimpleNamespace(exchange=EXCHANGE, symbol=symbol)


def configure(options, routes, start=START_2025, finish=FINISH_2025):
    state = funding.FundingState()
    state.configure({'mode': 'historical'} | options, start, finish, [route(s) for s in routes])
    return state


def test_btc_only_backtest_is_identical_to_pre_multi_symbol_golden(monkeypatch):
    """Golden JSON was produced by the BTC-only implementation (before this change)."""
    golden = case.load_fixture('btc_regression_golden.json')
    serve(monkeypatch, {'BTCUSDT': case.load_fixture('binance_fundingRate_BTCUSDT_20240101_20240104.json')})
    imported = funding.import_binance_history(case.START, case.FINISH)
    # Same content hash: BTC datasets imported before the change remain valid IDs.
    assert imported == golden['imported']
    dataset_id = funding.save_dataset(case.load_fixture('btc_usdt_20240101_20240104.json'))
    assert dataset_id == golden['fixture_dataset_id'] == imported['dataset_id']
    result = case.run_backtest(dataset_id)
    # Serialized comparison keeps NaN metrics comparable and floats exact.
    assert json.dumps(result, sort_keys=True) == json.dumps(golden['backtest'], sort_keys=True)
    assert 'dataset_ids' not in result['metrics']['funding']


def test_btc_dataset_ids_list_applies_the_same_cashflows_as_legacy_dataset_id():
    golden = case.load_fixture('btc_regression_golden.json')['backtest']
    dataset_id = funding.save_dataset(case.load_fixture('btc_usdt_20240101_20240104.json'))
    result = case.run_backtest(dataset_id, {'mode': 'historical', 'dataset_ids': [dataset_id]})
    evidence = result['metrics']['funding']
    assert evidence['ledger'] == golden['metrics']['funding']['ledger']
    assert evidence['dataset_ids'] == [dataset_id]
    assert evidence['cashflow_by_symbol'] == {'BTC-USDT': golden['metrics']['funding']['cashflow']}
    assert result['trades'] == golden['trades']


def test_eth_import_uses_its_own_instrument_and_keeps_vendor_jitter(monkeypatch):
    calls = []
    rows = case.load_fixture('binance_fundingRate_ETHUSDT_20250101_20250104.json')

    class Client(case.fake_binance_session({'ETHUSDT': rows})):
        def get(self, url, params, timeout):
            calls.append(params['symbol'])
            return super().get(url, params, timeout)

    monkeypatch.setattr(funding.requests, 'Session', Client)
    result = funding.import_binance_history(START_2025, FINISH_2025, symbol='ETH-USDT')
    assert set(calls) == {'ETHUSDT'}
    assert result['symbol'] == 'ETH-USDT'
    assert result['status'] == 'ready'
    assert result['event_count'] == 9
    assert result['coverage_policy'].startswith('vendor_response; ETH maximum eight-hour gap')
    events = funding.load_dataset(result['dataset_id'])['events']
    assert {event['symbol'] for event in events} == {'ETH-USDT'}
    assert events[0]['settled_at'] == START_2025 + 15
    assert events[0]['mark_price'] == 3336.65582576
    assert events[0]['rate_decimal'] == .0001
    # Re-import of the same vendor history is idempotent and keeps the symbol.
    update = funding.update_dataset(result['dataset_id'], FINISH_2025)
    assert update['changed'] is False and update['symbol'] == 'ETH-USDT'
    assert [row['symbol'] for row in funding.list_datasets('ETH-USDT')] == ['ETH-USDT']
    assert funding.list_datasets('BTC-USDT') == []


def test_old_eth_rows_without_marks_use_eth_mark_candles_only_when_allowed(monkeypatch):
    finish = START_2020 + 24 * 3_600_000
    serve(monkeypatch, {'ETHUSDT': case.load_fixture('binance_fundingRate_ETHUSDT_20200101_20200102.json')},
          {'ETHUSDT': case.load_fixture('binance_markPriceKlines_ETHUSDT_1h_20200101.json')})
    with pytest.raises(ValueError, match='allow_mark_price_proxy'):
        funding.import_binance_history(START_2020, finish, symbol='ETH-USDT')
    result = funding.import_binance_history(START_2020, finish, True, 'ETH-USDT')
    assert result['mark_price_proxy_count'] == 3
    events = funding.load_dataset(result['dataset_id'])['events']
    # Hourly ETH mark-candle OPENs at each settlement, never BTC prices.
    assert [e['mark_price'] for e in events] == [129.14963635, 130.31677273, 132.06723268]
    assert {e['mark_price_source'] for e in events} == {'markPriceKlines.1h_open_proxy'}


def test_vendor_rows_of_another_instrument_are_refused(monkeypatch):
    # A mis-routed response must not be stored under the requested symbol.
    serve(monkeypatch, {'ETHUSDT': case.load_fixture('binance_fundingRate_BTCUSDT_20250101_20250104.json')})
    with pytest.raises(ValueError, match='Unexpected funding instrument'):
        funding.import_binance_history(START_2025, FINISH_2025, symbol='ETH-USDT')
    assert funding.list_datasets() == []


@pytest.mark.parametrize('symbol', ['ETHUSDT', 'eth-usdt', 'ETH-USD', 'ETH-BUSD', '', None])
def test_only_usdt_margined_jesse_symbols_are_accepted(symbol):
    with pytest.raises(ValueError, match='USD-M perpetual'):
        funding.import_binance_history(START_2025, FINISH_2025, symbol=symbol)


def test_routes_without_their_own_dataset_still_require_explicit_exclusion(monkeypatch):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    with pytest.raises(ValueError, match='only BTC-USDT funding is modeled'):
        configure({'dataset_id': btc}, ['BTC-USDT', 'ETH-USDT'])
    with pytest.raises(ValueError, match='only ETH-USDT funding is modeled'):
        configure({'dataset_id': eth}, ['BTC-USDT', 'ETH-USDT'])
    with pytest.raises(ValueError, match='requires a Binance ETH-USDT trading route'):
        configure({'dataset_id': eth}, ['BTC-USDT'])
    with pytest.raises(ValueError, match='only BTC-USDT, ETH-USDT funding is modeled'):
        configure({'dataset_ids': [btc, eth]}, ['BTC-USDT', 'ETH-USDT', 'PAXG-USDT'])
    state = configure({'dataset_ids': [btc, eth], 'exclude_symbols': ['PAXG-USDT']},
                      ['BTC-USDT', 'ETH-USDT', 'PAXG-USDT'])
    snapshot = state.snapshot()
    assert snapshot['scope'] == ['BTC-USDT', 'ETH-USDT']
    assert snapshot['excluded_symbols'] == ['PAXG-USDT']
    assert set(snapshot['datasets']) == {'BTC-USDT', 'ETH-USDT'}
    assert snapshot['dataset_id'] is None and snapshot['data'] is None


@pytest.mark.parametrize('options,match', [
    (lambda btc, eth: {'dataset_id': btc, 'dataset_ids': [eth]}, 'not both'),
    (lambda btc, eth: {'dataset_ids': []}, 'nonempty'),
    (lambda btc, eth: {'dataset_ids': [btc, btc]}, 'unique'),
    (lambda btc, eth: {'dataset_ids': btc}, 'list'),
    (lambda btc, eth: {'dataset_ids': [btc, eth], 'exclude_symbols': ['ETH-USDT']}, 'without a configured'),
])
def test_invalid_multi_dataset_configs_are_refused(monkeypatch, options, match):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    with pytest.raises(ValueError, match=match):
        configure(options(btc, eth), ['BTC-USDT', 'ETH-USDT'])


def test_two_datasets_of_one_symbol_are_refused(monkeypatch):
    eth = import_2025(monkeypatch, 'ETH-USDT')
    data = funding.load_dataset(eth)
    revised = funding.save_dataset(data | {'events': data['events'][:-1], 'finish': data['finish'] - 3_600_000})
    with pytest.raises(ValueError, match='different symbol'):
        configure({'dataset_ids': [eth, revised]}, ['ETH-USDT'], finish=FINISH_2025 - 3_600_000)


def test_each_dataset_is_validated_on_its_own(monkeypatch):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    data = funding.load_dataset(eth)
    # Dropping one ETH settlement opens a 16h ETH gap; BTC events must not mask it.
    gapped = funding.save_dataset(data | {'events': data['events'][:3] + data['events'][4:]})
    with pytest.raises(ValueError, match='ETH-USDT has a gap'):
        configure({'dataset_ids': [btc, gapped]}, ['BTC-USDT', 'ETH-USDT'])
    short = funding.save_dataset(data | {'events': data['events'][:-1], 'finish': data['finish'] - 3_600_000})
    with pytest.raises(ValueError, match='for ETH-USDT does not cover'):
        configure({'dataset_ids': [btc, short]}, ['BTC-USDT', 'ETH-USDT'])


def test_history_is_per_symbol_and_never_pooled(monkeypatch):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    state = configure({'dataset_ids': [btc, eth]}, ['BTC-USDT', 'ETH-USDT'])
    nobody = SimpleNamespace(positions=SimpleNamespace(get_position=lambda *args: None))
    state.settle(START_2025 + 8 * 3_600_000, nobody)
    now = START_2025 + 8 * 3_600_000 + 60_000
    assert [r['symbol'] for r in state.history(now, 5, 'ETH-USDT')] == ['ETH-USDT'] * 2
    assert [r['mark_price'] for r in state.history(now, 5, 'BTC-USDT')] == [93549.66175177, 93660.97108511]
    with pytest.raises(ValueError, match='pass the symbol'):
        state.history(now, 5)
    with pytest.raises(ValueError, match='No funding dataset is configured for SOL-USDT'):
        state.history(now, 5, 'SOL-USDT')
    # At 08:00 the 08:00 settlement is not yet published (+1m delay).
    assert state.known[(EXCHANGE, 'ETH-USDT')].mark_price == 3336.65582576
    state.settle(now, nobody)
    assert state.known[(EXCHANGE, 'ETH-USDT')].mark_price == 3345.84
    assert state.known[(EXCHANGE, 'BTC-USDT')].mark_price == 93660.97108511


def _prices(dataset_id: str) -> np.ndarray:
    events = funding.load_dataset(dataset_id)['events']
    minutes = np.arange(START_2025, FINISH_2025, 60_000)
    return np.round(np.interp(minutes, [e['settled_at'] for e in events], [e['mark_price'] for e in events]), 2)


class _ShortFirst(Strategy):
    """Short at the second candle and hold to the end, observing its own funding."""
    qty = 1

    def should_long(self):
        return False

    def go_long(self):
        pass

    def should_short(self):
        return self.index == 1

    def go_short(self):
        self.sell = self.qty, self.price

    def should_cancel_entry(self):
        return False

    def before(self):
        # Shortly after the 08:00 settlement is published (+1m).
        if self.index == 8 * 60 + 1:
            if self.symbol not in store.funding.symbols:
                return  # an explicitly excluded route has no funding of its own
            own = self.get_funding_history(10)
            assert [row['symbol'] for row in own] == [self.symbol] * 2
            assert self.settled_funding_rate == own[-1]['rate_decimal']
            other = 'BTC-USDT' if self.symbol == 'ETH-USDT' else 'ETH-USDT'
            if other in store.funding.symbols:
                assert {row['symbol'] for row in self.get_funding_history(10, other)} == {other}
            else:
                with pytest.raises(ValueError, match='No funding dataset'):
                    self.get_funding_history(10, other)


class _ShortEth(_ShortFirst):
    qty = 3


class _ShortBtc(_ShortFirst):
    qty = .1


def _run_two_routes(btc: str, eth: str, funding_config: dict) -> dict:
    config = {'starting_balance': 100_000, 'fee': .00045, 'type': 'futures',
              'futures_leverage': 3, 'futures_leverage_mode': 'isolated',
              'exchange': EXCHANGE, 'warm_up_candles': 0, 'funding': funding_config}
    candles = {}
    for symbol, dataset_id in (('BTC-USDT', btc), ('ETH-USDT', eth)):
        rows = np.array([[START_2025 + i * 60_000, p, p, p, p, 10] for i, p in enumerate(_prices(dataset_id))])
        candles[f'{EXCHANGE}-{symbol}'] = {'exchange': EXCHANGE, 'symbol': symbol, 'candles': rows}
    return research.backtest(config, [
        {'exchange': EXCHANGE, 'symbol': 'BTC-USDT', 'timeframe': '1m', 'strategy': _ShortBtc},
        {'exchange': EXCHANGE, 'symbol': 'ETH-USDT', 'timeframe': '1m', 'strategy': _ShortEth},
    ], [], candles)


def _expected_cashflows(dataset_id: str, qty: float) -> list:
    # Shorts opened at minute 1 skip the 00:00:00.015 settlement and hold to finish.
    events = funding.load_dataset(dataset_id)['events'][1:]
    return [-(-qty) * e['mark_price'] * e['rate_decimal'] for e in events]


def test_each_route_pays_funding_of_its_own_symbol(monkeypatch):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    result = _run_two_routes(btc, eth, {'mode': 'historical', 'dataset_ids': [btc, eth]})
    evidence = result['metrics']['funding']
    by_symbol = {s: [r for r in evidence['ledger'] if r['symbol'] == s] for s in ('BTC-USDT', 'ETH-USDT')}
    assert [r['cashflow'] for r in by_symbol['ETH-USDT']] == pytest.approx(_expected_cashflows(eth, 3))
    assert [r['cashflow'] for r in by_symbol['BTC-USDT']] == pytest.approx(_expected_cashflows(btc, .1))
    assert {r['qty'] for r in by_symbol['ETH-USDT']} == {-3}
    # Positive funding: shorts receive it.
    assert evidence['cashflow_by_symbol']['ETH-USDT'] > 0
    assert sum(evidence['cashflow_by_symbol'].values()) == pytest.approx(evidence['cashflow'])
    assert evidence['event_count'] == 16
    # 9 per symbol; the first of each settles before the shorts open.
    assert evidence['settlements_processed'] == 18
    # Same-minute BTC and ETH settlements are ordered deterministically.
    assert [r['symbol'] for r in evidence['ledger'][:2]] == ['BTC-USDT', 'ETH-USDT']
    # The open trade of each route carries exactly its own symbol's funding.
    trades = {t['symbol']: t for t in result['trades']}
    for symbol in ('BTC-USDT', 'ETH-USDT'):
        assert trades[symbol]['funding'] == pytest.approx(evidence['cashflow_by_symbol'][symbol])


def test_adding_a_symbol_does_not_change_the_other_symbols_cashflows(monkeypatch):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    both = _run_two_routes(btc, eth, {'mode': 'historical', 'dataset_ids': [btc, eth]})['metrics']['funding']
    store.reset()
    btc_only = _run_two_routes(btc, eth, {'mode': 'historical', 'dataset_id': btc,
                                         'exclude_symbols': ['ETH-USDT']})['metrics']['funding']
    strip = lambda rows: [{k: v for k, v in r.items() if k != 'trade_id'} for r in rows]
    assert strip(btc_only['ledger']) == strip([r for r in both['ledger'] if r['symbol'] == 'BTC-USDT'])
    assert btc_only['excluded_symbols'] == ['ETH-USDT']


def test_eth_only_short_first_backtest(monkeypatch):
    eth = import_2025(monkeypatch, 'ETH-USDT')
    rows = np.array([[START_2025 + i * 60_000, p, p, p, p, 10] for i, p in enumerate(_prices(eth))])
    result = research.backtest(
        {'starting_balance': 100_000, 'fee': 0, 'type': 'futures', 'futures_leverage': 3,
         'futures_leverage_mode': 'isolated', 'exchange': EXCHANGE, 'warm_up_candles': 0,
         'funding': {'mode': 'historical', 'dataset_id': eth}},
        [{'exchange': EXCHANGE, 'symbol': 'ETH-USDT', 'timeframe': '1m', 'strategy': _ShortEth}], [],
        {f'{EXCHANGE}-ETH-USDT': {'exchange': EXCHANGE, 'symbol': 'ETH-USDT', 'candles': rows}})
    evidence = result['metrics']['funding']
    assert evidence['scope'] == ['ETH-USDT']
    assert evidence['data']['symbol'] == 'ETH-USDT'
    assert evidence['cashflow'] == pytest.approx(sum(_expected_cashflows(eth, 3)))


def test_gapped_execution_candles_of_a_funded_symbol_are_refused(monkeypatch):
    btc, eth = import_2025(monkeypatch, 'BTC-USDT'), import_2025(monkeypatch, 'ETH-USDT')
    rows = {s: np.array([[START_2025 + i * 60_000, p, p, p, p, 10] for i, p in enumerate(_prices(d))])
            for s, d in (('BTC-USDT', btc), ('ETH-USDT', eth))}
    rows['ETH-USDT'] = np.delete(rows['ETH-USDT'], 100, axis=0)
    with pytest.raises(ValueError, match='uninterrupted ETH one-minute'):
        research.backtest(
            {'starting_balance': 100_000, 'fee': 0, 'type': 'futures', 'futures_leverage': 3,
             'futures_leverage_mode': 'isolated', 'exchange': EXCHANGE, 'warm_up_candles': 0,
             'funding': {'mode': 'historical', 'dataset_ids': [btc, eth]}},
            [{'exchange': EXCHANGE, 'symbol': s, 'timeframe': '1m', 'strategy': _ShortEth} for s in rows], [],
            {f'{EXCHANGE}-{s}': {'exchange': EXCHANGE, 'symbol': s, 'candles': r} for s, r in rows.items()})


@pytest.fixture
def http(monkeypatch):
    app = FastAPI()
    app.include_router(controller.router)
    app.include_router(controller.oi_router)
    app.dependency_overrides[require_auth] = lambda: None
    return TestClient(app)


def test_import_api_accepts_symbol_and_defaults_to_btc(monkeypatch, http):
    serve(monkeypatch, {'ETHUSDT': case.load_fixture('binance_fundingRate_ETHUSDT_20250101_20250104.json'),
                        'BTCUSDT': case.load_fixture('binance_fundingRate_BTCUSDT_20250101_20250104.json')})
    body = {'start_date': '2025-01-01', 'finish_date': '2025-01-04'}
    eth = http.post('/funding/import', json=body | {'symbol': 'ETH-USDT'})
    btc = http.post('/funding/import', json=body)
    assert eth.status_code == btc.status_code == 200
    assert eth.json()['symbol'] == 'ETH-USDT' and btc.json()['symbol'] == 'BTC-USDT'
    listed = http.post('/funding/datasets', json={'symbol': 'ETH-USDT'}).json()['datasets']
    assert [row['dataset_id'] for row in listed] == [eth.json()['dataset_id']]
    assert len(http.post('/funding/datasets', json={}).json()['datasets']) == 2
    bad = http.post('/funding/import', json=body | {'symbol': 'ETHUSDT'})
    assert bad.status_code == 400 and 'USD-M perpetual' in bad.json()['detail']


def test_mcp_import_forwards_symbol(monkeypatch):
    import asyncio
    from jesse.mcp.tools import funding as tools
    sent = []
    monkeypatch.setattr(tools, '_request', lambda path, payload: sent.append((path, payload)) or {})

    class Recorder:
        def __init__(self):
            self.tools = {}

        def tool(self):
            def register(function):
                self.tools[function.__name__] = function
                return function
            return register

    mcp = Recorder()
    tools.register_funding_tools(mcp)
    asyncio.run(mcp.tools['import_funding']('2025-01-01', '2025-01-04', symbol='ETH-USDT'))
    asyncio.run(mcp.tools['import_funding']('2025-01-01', '2025-01-04'))
    asyncio.run(mcp.tools['list_funding_datasets']('ETH-USDT'))
    assert sent[0] == ('import', {'start_date': '2025-01-01', 'finish_date': '2025-01-04',
                                  'allow_mark_price_proxy': False, 'symbol': 'ETH-USDT'})
    assert sent[1][1]['symbol'] == 'BTC-USDT'
    assert sent[2] == ('datasets', {'symbol': 'ETH-USDT'})


def test_session_evidence_matches_dataset_ids_config(monkeypatch):
    from tests.test_funding_api import create, request
    from peewee import SqliteDatabase
    from jesse.models.BacktestSession import BacktestSession
    ids = ['a' * 64, 'b' * 64]
    database = SqliteDatabase(':memory:', check_same_thread=False)
    with database.bind_ctx([BacktestSession]):
        database.connect()
        database.create_tables([BacktestSession])
        evidence = {'mode': 'historical', 'status': 'applied', 'applied': True, 'dataset_id': None,
                    'dataset_ids': ids, 'cashflow': 1.5, 'event_count': 1, 'ledger': []}
        row = create(status='finished', metrics={'funding': evidence},
                     config={'funding': {'mode': 'historical', 'dataset_ids': ids}})
        assert controller.session(request(row))['applied'] is True
        row = create(status='finished', metrics={'funding': evidence},
                     config={'funding': {'mode': 'historical', 'dataset_ids': ids[::-1]}})
        assert controller.session(request(row))['applied'] is False
        database.close()


def test_fixture_events_match_funding_event_schema():
    # The stored BTC slice must stay a valid dataset the engine accepts.
    data = case.load_fixture('btc_usdt_20240101_20240104.json')
    assert all(asdict(funding.FundingEvent(**row)) == row for row in data['events'])
