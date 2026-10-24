import math
import numpy as np
from jesse.strategies import Strategy, cached
import jesse.indicators as ta

# A new sleeve starts at 1% risk; not a return-maximization parameter.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing reserve only; no simulated fill impact.


class OrchShortDailyPullback4h(Strategy):
    """BTC-only daily bear regime and failed 4h recovery.

    Conventional finite-memory SMA200 regime replaces the short-lived 4h
    regime of earlier failed rejection tests. No fixed target or time expiry
    truncates a bear leg. Experimental research only; 2026 is excluded.
    """

    @property
    @cached
    def daily_state(self):
        daily = self.get_candles(self.exchange, self.symbol, '1D')
        # Explicitly exclude any forming daily candle. Daily data is a separate
        # declared data route, never synthesized using an incomplete 4h session.
        daily = daily[daily[:, 0] + 86_400_000 <= self.time]
        if len(daily) < 210:
            return None
        slow = ta.sma(daily, period=200, sequential=True)
        close = float(daily[-1, 2])
        now, before = float(slow[-1]), float(slow[-11])
        if not all(math.isfinite(x) for x in (close, now, before)):
            return None
        return close < now and now < before, close > now

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional


    def should_long(self) -> bool:
        return False

    def go_long(self) -> None:
        return

    def should_short(self) -> bool:
        if self.symbol != 'BTC-USDT':
            return False
        regime = self.daily_state
        if regime is None or not regime[0]:
            return False
        c = self.candles
        if len(c) < 40:
            return False
        fast = ta.ema(c, period=20, sequential=True)
        atr = float(ta.atr(c))
        if not all(math.isfinite(x) for x in (fast[-1], fast[-2], atr)) or atr <= 0:
            return False
        # A completed rally above the local mean fails back below it. We avoid
        # RSI extremes and fresh-channel-low requirements from earlier tests.
        if not (c[-2, 2] >= fast[-2] and c[-1, 2] < fast[-1]
                and c[-1, 2] < c[-1, 1]):
            return False
        entry = float(c[-1, 4])
        if not 0 < self.price - entry <= atr:
            return False
        # The last three closed bars approximate the failed recovery's swing;
        # 0.25ATR clears its wick. Existing 1–3ATR bounds avoid tiny/huge stops.
        distance = max(atr, float(np.max(c[-3:, 3])) + 0.25 * atr - entry)
        if distance > 3 * atr:
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK,
                     max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = max(0.0, capital * NOTIONAL_CAP - notional)
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Historical BTC precision only; native lot/min-notional remains unverified.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # A failed recovery signal gets one future 4h bar to confirm.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        if self.is_short:
            entry = float(self.position.entry_price)
            self.vars['best_close'] = entry
            self.stop_loss = abs(self.position.qty), entry + self.vars['plan']['distance']
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        if not self.is_short:
            return
        regime = self.daily_state
        # Exit on observed daily regime invalidation; a slope flattening alone
        # blocks new entries without forcing a potentially noisy immediate exit.
        if regime is not None and regime[1]:
            self.liquidate()
            return
        atr = float(ta.atr(self.candles))
        if not math.isfinite(atr) or atr <= 0:
            return
        self.vars['best_close'] = min(self.vars['best_close'], self.price)
        # No pre-entry wick is inherited. A common 3ATR trailing distance leaves
        # room for a bear swing and is frozen before the first run.
        stop = self.vars['best_close'] + 3 * atr
        if self.price < stop < self.average_stop_loss:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
