import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# New, unvalidated reversal logic starts below the user-approved maximum risk.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Buffer within configured isolated5x.
SLIPPAGE_RESERVE = 0.001  # Sizing only, not fill friction.

class OrchLateralFailedRange4h(Strategy):
    """Symmetric market-entry reversals of rejected range extensions.

    Exploratory economic hypothesis, not validated complementarity or live-ready.
    """

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # Retain the reference's conservative SPY decision intersection: the
        # last eligible bar opens at12:00 and decides at16:00. These MARKET
        # entries do not rely on a pending order surviving a session boundary.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

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


    def _signal(self) -> int:
        # Cache both decisions together so the second direction cannot overwrite a plan.
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        if not self._entry_window():
            return 0
        c = self.signal_candles
        if len(c) < 100:
            return 0
        atr = float(ta.atr(c))
        close = c[-21:, 2]
        noise = float(np.sum(np.abs(np.diff(close))))
        efficiency = abs(float(close[-1] - close[0])) / noise if noise > 0 else 0.0
        # Twenty 4h observations represent several days of local auction context;
        # low efficiency distinguishes an oscillating auction from directional drift.
        if not math.isfinite(atr) or atr <= 0 or efficiency > 0.25:
            return 0
        lower = float(np.min(c[-21:-1, 4]))
        upper = float(np.max(c[-21:-1, 3]))
        middle = 0.5 * (lower + upper)
        side = 0
        if float(c[-1, 4]) < lower < self.price < middle:
            side = 1
            stop = float(c[-1, 4]) - 0.25 * atr
        elif float(c[-1, 3]) > upper > self.price > middle:
            side = -1
            stop = float(c[-1, 3]) + 0.25 * atr
        if side == 0:
            return 0
        entry = float(self.price)
        distance = abs(entry - stop)
        reward = side * (middle - entry)
        # Eligibility uses fixed BASE fees so effective-fee stresses leave signals fixed.
        # Minimum1R avoids a consumed reversal; ATR bounds reject tiny/noisy or huge stops.
        if not (atr <= distance <= 3 * atr and reward >= distance
                and reward >= 8 * 0.00045 * entry):
            return 0
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        # Equal route caps avoid comparing session ATR with continuous crypto ATR.
        route_count = sum(route.exchange == self.exchange for route in self.routes)
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP / max(1, route_count))
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision: native target-venue lot/min-notional remain unverified.
        step = 0.0001 if self.symbol == 'PAXG-USDT' else 0.001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return 0
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target': middle, 'side': side}
        self.vars['signal_value'] = side
        return side

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # MARKET should fill immediately; never retain an unexpected entry.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['plan']
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        self.vars['opened_time'] = int(self.time)
        if self.is_long:
            self.stop_loss = qty, entry - plan['distance']
        else:
            self.stop_loss = qty, entry + plan['distance']
        self.take_profit = qty, plan['target']
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        # A failed reversal must resolve within two days. Exits remain active
        # outside entry hours; missing SPY quotes can postpone actual liquidation.
        if self.time - self.vars['opened_time'] >= 48 * 60 * 60 * 1000:
            self.liquidate()

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
