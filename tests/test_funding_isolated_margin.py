"""Funding on a sustained isolated-margin position (Binance USD-M semantics).

Binance pays funding from the available balance first; once that is gone the
rest comes out of the position margin and moves the liquidation price
("Introduction to Binance Futures Funding Rates", binance.com support FAQ
360033525031). The scenario below is a BTC-USDT perpetual held at ~1x
notional with 2x isolated leverage, fee 0, so every number is exact:

- entry 99 @ 100: initial margin 4,950, free balance 5,050;
- every settlement pays 99 * 100 * 0.02 = 198 (longs pay a positive rate);
- the 26th settlement exhausts the free balance (the old engine stopped here);
- after 30 settlements 5,940 was paid and 890 came out of the isolated margin,
  so the long liquidation price is 50.4 + 890 / 99 instead of 50.4;
- the 51st settlement would leave the isolated margin below maintenance at the
  current price, which is a venue liquidation the engine does not simulate.
"""

from dataclasses import asdict

import numpy as np
import pytest

from jesse import research
from jesse.config import reset_config
from jesse.exceptions import InsufficientMargin
from jesse.services import funding
from jesse.store import store
from jesse.strategies import Strategy


START = 1_577_836_800_000
EXCHANGE = funding.EXCHANGE
QTY = 99
RATE = .02
PAYMENT = QTY * 100 * RATE
DRAWN = 30 * PAYMENT - 5_050


@pytest.fixture(autouse=True)
def clean_state(tmp_path, monkeypatch):
    store.reset()
    reset_config()
    monkeypatch.setattr(funding, '_root', lambda: tmp_path / 'funding')
    yield
    store.reset()
    reset_config()


def dataset(count, direction, minutes):
    # An entry decided on the first candle pays from the next minute on; the
    # sign makes the held side the payer (shorts pay negative rates).
    rows = [asdict(funding.FundingEvent(EXCHANGE, 'BTC-USDT', START + (i + 2) * 60_000, direction * RATE, 100))
            for i in range(count)]
    return funding.save_dataset({'schema': 1, 'source': funding.SOURCE, 'exchange': EXCHANGE,
                                'symbol': 'BTC-USDT', 'start': START, 'finish': START + minutes * 60_000,
                                'events': rows})


def run(strategy, events, prices, mode='isolated'):
    direction = getattr(strategy, 'direction', 1)
    config = {'starting_balance': 10_000, 'fee': 0, 'type': 'futures',
              'futures_leverage': 2, 'futures_leverage_mode': mode,
              'exchange': EXCHANGE, 'warm_up_candles': 0,
              'funding': {'mode': 'historical', 'dataset_id': dataset(events, direction, len(prices))}}
    rows = np.array([[START + i * 60_000, p, p, p, p, 10] for i, p in enumerate(prices)], dtype=float)
    candles = {f'{EXCHANGE}-BTC-USDT': {'exchange': EXCHANGE, 'symbol': 'BTC-USDT', 'candles': rows}}
    return research.backtest(config, [{'exchange': EXCHANGE, 'symbol': 'BTC-USDT',
                                       'timeframe': '1m', 'strategy': strategy}],
                             [], candles, generate_equity_curve=True)


class _SustainedHold(Strategy):
    direction = 1

    def should_long(self):
        return self.index == 0 and self.direction == 1

    def should_short(self):
        return self.index == 0 and self.direction == -1

    def go_long(self):
        self.buy = QTY, self.price

    def go_short(self):
        self.sell = QTY, self.price

    def should_cancel_entry(self):
        return False


class _HoldThenReduce(_SustainedHold):
    def before(self):
        if self.index == 31:
            # All 30 settlements are paid; the free balance is fully used.
            assert self.position.funding_margin_drawn == pytest.approx(DRAWN)
            assert self.available_margin == pytest.approx(0, abs=1e-6)
            assert self.balance == pytest.approx(10_000 - 30 * PAYMENT)
            if self.direction == 1:
                assert self.position.liquidation_price == pytest.approx(50.4 + DRAWN / QTY)
            else:
                assert self.position.liquidation_price == pytest.approx(149.6 - DRAWN / QTY)
            self.vars['liquidation_price'] = self.position.liquidation_price
        if self.index == 34:
            # Releasing half the size releases half the consumed collateral.
            assert abs(self.position.qty) == pytest.approx(QTY / 2)
            assert self.position.funding_margin_drawn == pytest.approx(DRAWN / 2)
            assert self.position.liquidation_price == pytest.approx(self.vars['liquidation_price'])

    def update_position(self):
        if self.index == 31:
            self.take_profit = QTY / 2, self.price

    def on_close_position(self, order, closed_trade):
        assert closed_trade.funding == pytest.approx(-30 * PAYMENT)
        assert self.balance == pytest.approx(10_000 - 30 * PAYMENT)


@pytest.mark.parametrize('direction', [1, -1])
def test_funding_beyond_free_balance_is_taken_from_isolated_margin(direction):
    strategy = type('HoldThenReduce', (_HoldThenReduce,), {'direction': direction})
    result = run(strategy, 30, [100] * 40)
    evidence = result['metrics']['funding']
    assert evidence['event_count'] == 30
    assert evidence['cashflow'] == pytest.approx(-30 * PAYMENT)


class _LiquidatedAtShiftedPrice(_SustainedHold):
    def on_close_position(self, order, closed_trade):
        # 55 is above the unfunded liquidation price (50.4) but below the
        # shifted one, so the position is liquidated at its bankruptcy price
        # and the whole isolated margin, funding included, is lost.
        assert store.app.total_liquidations == 1
        assert closed_trade.exit_price == pytest.approx(50 + DRAWN / QTY)
        assert self.balance == pytest.approx(0, abs=1e-6)
        self.vars['closed'] = True

    def terminate(self):
        assert self.vars.get('closed')


def test_drawn_isolated_margin_moves_the_price_liquidation():
    run(_LiquidatedAtShiftedPrice, 30, [100] * 35 + [55] * 5)


def test_funding_that_would_liquidate_at_settlement_still_stops():
    with pytest.raises(InsufficientMargin, match='would liquidate'):
        run(_SustainedHold, 51, [100] * 60)


def test_cross_margin_keeps_failing_when_available_margin_is_exhausted():
    with pytest.raises(InsufficientMargin, match='Funding exhausts available margin'):
        run(_SustainedHold, 30, [100] * 40, mode='cross')
