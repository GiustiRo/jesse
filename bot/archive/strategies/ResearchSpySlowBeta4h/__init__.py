import math
from datetime import datetime, timezone
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils

RISK = 0.01
TAIL = 0.10
GROSS_CAP = 4.4
RESERVE = 0.001  # Sizing reserve, not a simulated adverse fill.
LOOKBACK = 200  # Daily observed-price adaptation, not the Faber ten-month recipe.


class ResearchSpySlowBeta4h(Strategy):
    """SPY slow price-premium exposure with the same tail stop and no trend filter.

    Quotes are observed at16UTC, not the NYSE close. Missing observations
    remain missing. Both the defense and beta control retain startup cash.
    """
    USE_FILTER = False

    def trading_hours(self):
        return {'timezone': 'UTC', 'hours': {'Mon-Fri': '12:00-16:00'}}

    @property
    @cached
    def observation_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _fresh(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(c):
            return False
        i = int(np.searchsorted(c[:, 0], self.time - 60000, side='right')) - 1
        if i < 0 or int(c[i, 0]) + 60000 != int(self.time):
            return False
        assert math.isclose(self.price, float(c[i, 2]), rel_tol=1e-10, abs_tol=1e-8), 'SLOW_QUOTE_MISMATCH'
        return True

    def before(self):
        self.vars['review_due'] = False
        self.vars.setdefault('observations', [])
        if not self.is_trading_hours or not self._fresh():
            return
        c = self.observation_candles
        if not len(c) or int(c[-1, 0]) != self.closed_candle_open_time:
            return
        day = datetime.fromtimestamp(self.time / 1000, timezone.utc).strftime('%Y-%m-%d')
        if self.vars.get('observation_day') == day:
            return
        self.vars['observation_day'] = day
        observations = self.vars['observations']
        observations.append(float(c[-1, 2]))
        # Retain exactly the fixed daily lookback; no synthetic holiday candles.
        self.vars['observations'] = observations[-LOOKBACK:]
        if len(observations) < LOOKBACK:
            return
        month = day[:7]
        if self.vars.get('review_month') == month:
            return
        self.vars.update(review_month=month, review_due=True)
        self.vars['want_long'] = not self.USE_FILTER or self.price > float(np.mean(observations[-LOOKBACK:]))
        # Consume the month's review even while held. A later stop leaves cash
        # until a NEW month's review, never an immediate same-month re-entry.
        if self.is_open and not self.vars['want_long']:
            self.vars['exit_pending'] = True

    def should_long(self):
        if (self.symbol != 'SPY-USDT' or len(self.routes) != 1
                or not self.vars.get('review_due') or not self.vars['want_long']
                or self.vars.get('exit_pending') or not self._fresh()):
            return False
        entry = float(self.price)
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        stop = entry * (1 - TAIL)
        # This budget implies about0.0982x notional, not a full-capital index bet.
        unit_risk = entry - stop + self.fee_rate * (entry + stop) + RESERVE * entry
        qty = min(capital * RISK / unit_risk, capital * GROSS_CAP / entry,
                  max(0.0, self.leveraged_available_margin * 0.90) / entry)
        qty = math.floor(qty / 0.001) * 0.001  # Same research precision as baseline.
        if qty <= 0:
            return False
        self.vars['qty'] = qty
        return True

    def should_short(self):
        return False

    def go_long(self):
        self.buy = self.vars['qty'], self.price

    def go_short(self):
        pass

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        self.stop_loss = abs(self.position.qty), self.position.entry_price * (1 - TAIL)

    def update_position(self):
        # All-hour management honors an existing exit debt at the first fresh
        # quote. The protective stop remains active independently of this callback.
        if self.vars.get('exit_pending'):
            if self._fresh():
                self.liquidate()
            return
        if self.vars.get('review_due') and self._fresh():
            stop = float(self.price) * (1 - TAIL)
            if self.average_stop_loss < stop < self.price:
                self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade):
        self.vars['exit_pending'] = False
