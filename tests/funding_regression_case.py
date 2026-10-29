"""Fixed BTC funding scenario whose output is pinned in tests/data/funding.

The golden JSON was produced by the BTC-only implementation before funding
became per symbol; the multi-symbol code must reproduce it byte for byte.
Fixtures are real Binance responses (fundingRate, BTCUSDT, 2024-01-01..04).
"""

import json
from pathlib import Path

import numpy as np

from jesse import research
from jesse.services import funding
from jesse.strategies import Strategy


DATA = Path(__file__).parent / 'data' / 'funding'
EXCHANGE = 'Binance Perpetual Futures'
START = 1_704_067_200_000
FINISH = 1_704_326_400_000
# Strategy-observed causal history; the store is reset when a backtest ends.
HISTORY: list = []


def load_fixture(name: str):
    return json.loads((DATA / name).read_text())


class _Response:
    def __init__(self, rows):
        self.rows = rows

    def raise_for_status(self):
        pass

    def json(self):
        return self.rows


def fake_binance_session(funding_rows: dict, mark_rows: dict | None = None):
    """Serve recorded fundingRate/markPriceKlines pages, honouring time filters."""
    mark_rows = mark_rows or {}

    class Client:
        def __enter__(self): return self
        def __exit__(self, *args): pass

        def get(self, url, params, timeout):
            if url.endswith('markPriceKlines'):
                rows = [r for r in mark_rows.get(params['symbol'], [])
                        if params['startTime'] <= r[0] <= params['endTime']]
            else:
                rows = [r for r in funding_rows.get(params['symbol'], [])
                        if params['startTime'] <= r['fundingTime'] <= params['endTime']]
            return _Response(rows[:params['limit']])

    return Client


def btc_prices(dataset: dict) -> np.ndarray:
    """Minute closes linearly interpolated through the real settlement marks."""
    times = [e['settled_at'] for e in dataset['events']]
    marks = [e['mark_price'] for e in dataset['events']]
    minutes = np.arange(START, FINISH, 60_000)
    return np.round(np.interp(minutes, times, marks), 2)


class RegressionFunding(Strategy):
    """Long across four settlements, flat, then short across three."""

    def should_long(self):
        return self.index == 10

    def go_long(self):
        self.buy = 1.5, self.price

    def should_short(self):
        return self.index == 2_000

    def go_short(self):
        self.sell = 1, self.price

    def update_position(self):
        if self.index in (1_500, 3_500):
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def before(self):
        if self.index in (0, 481, 2_000, 4_000):
            HISTORY.append(self.get_funding_history(3))


def run_backtest(dataset_id: str, funding_config: dict | None = None) -> dict:
    HISTORY.clear()
    dataset = funding.load_dataset(dataset_id)
    prices = btc_prices(dataset)
    rows = np.array([[START + i * 60_000, p, p, p, p, 10] for i, p in enumerate(prices)], dtype=float)
    config = {'starting_balance': 100_000, 'fee': .00045, 'type': 'futures',
              'futures_leverage': 3, 'futures_leverage_mode': 'isolated',
              'exchange': EXCHANGE, 'warm_up_candles': 0,
              'funding': funding_config or {'mode': 'historical', 'dataset_id': dataset_id}}
    candles = {f'{EXCHANGE}-BTC-USDT': {'exchange': EXCHANGE, 'symbol': 'BTC-USDT', 'candles': rows}}
    result = research.backtest(config, [{'exchange': EXCHANGE, 'symbol': 'BTC-USDT',
                                         'timeframe': '1m', 'strategy': RegressionFunding}],
                               [], candles, generate_equity_curve=True)
    # Trade UUIDs are random per run; replace them with the trade's ordinal.
    ordinals = {str(t['id']): n for n, t in enumerate(result['trades'])}
    metrics = result['metrics']
    for row in metrics['funding']['ledger']:
        row['trade_id'] = ordinals[row['trade_id']]
    return {'metrics': metrics,
            'trades': [{key: value for key, value in t.items() if key != 'id'}
                       | {'orders': [{key: value for key, value in o.items() if key not in ('id', 'trade_id')}
                                     for o in t['orders']]} for t in result['trades']],
            'history': list(HISTORY),
            'equity_tail': result['equity_curve'][0]['data'][-3:]}
