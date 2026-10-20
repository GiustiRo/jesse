import math
from jesse.strategies import Strategy
import jesse.indicators as ta

# Predeclared exploratory controls, not optimized or approved for live trading.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing reserve only; simulated fills do not include slippage.
SHOCK_ATR = 1.5  # Material four-hour close displacement relative to pre-event volatility.
STOP_ATR = 2.0  # Fixed invalidation distance; no trailing or profit target.
MAX_HOLD_MS = 48 * 60 * 60 * 1000  # Two-day response, independent of slow trend state.


class ResearchPaxgShockReverse4h(Strategy):
    """PAXG price-proxy shock response; both directions and a fixed horizon.

    No gold-market microstructure is inferred from token spot candles.
    No market-session calendar is imposed on the continuously traded PAXG proxy.
    Only one position per route; overlapping events while open are ignored.
    """
    RESPONSE = -1

    def _fresh_quote(self) -> bool:
        c = self.get_candles(self.exchange, self.symbol, '1m')
        return (len(c) > 0 and int(c[-1, 0]) == int(self.time) - 60000
                and math.isfinite(float(c[-1, 2])) and float(c[-1, 2]) > 0)

    def _capital(self) -> float:
        # Floating gains do not enlarge risk; floating losses reduce the budget.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            s = route.strategy
            if not s.is_open:
                continue
            qty = abs(float(s.position.qty))
            value = abs(float(s.position.value))
            mark = value / qty if qty else float(s.position.entry_price)
            stop = float(s.average_stop_loss)
            distance = max(0.0, mark-stop) if s.is_long else max(0.0, stop-mark)
            risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
            notional += value
        return risk, notional

    def _signal(self) -> int:
        # Jesse checks both directions in one cycle; cache so planning stays stable.
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal']
        self.vars['signal_index'] = self.index
        self.vars['signal'] = 0
        if self.symbol != 'PAXG-USDT' or not self._fresh_quote():
            return 0
        c = self.candles
        if len(c) < 30:
            return 0
        # Excluding the event bar prevents its range from diluting its own surprise.
        atr = float(ta.atr(c[:-1]))
        change = float(c[-1, 2] - c[-2, 2])
        entry = float(self.price)
        if not (math.isfinite(atr) and atr > 0 and math.isfinite(change)
                and entry > 0 and abs(change) >= SHOCK_ATR * atr):
            return 0
        direction = (1 if change > 0 else -1) * self.RESPONSE
        distance = STOP_ATR * atr
        if distance >= entry:
            return 0
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK-risk))
        stop = entry - direction * distance
        unit_risk = distance + self.fee_rate * (entry+stop) + SLIPPAGE_RESERVE * entry
        # Gross and margin ceilings apply even when volatility is unusually small.
        room = min(max(0.0, capital * NOTIONAL_CAP-notional),
                   max(0.0, float(self.leveraged_available_margin)*0.9))
        qty = min(budget/unit_risk, room/entry)
        # Research precision matches existing PAXG strategies; venue lots unverified.
        qty = math.floor(qty/0.0001)*0.0001
        if qty <= 0:
            return 0
        self.vars['plan'] = {'qty': qty, 'distance': distance}
        self.vars['signal'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; an unexpected pending order cannot persist.
        return True

    def on_open_position(self, order) -> None:
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['opened_time'] = int(self.position.opened_at)
        stop = entry-distance if self.is_long else entry+distance
        self.stop_loss = abs(self.position.qty), stop

    def update_position(self) -> None:
        # Management remains active round the clock, independent of event formation.
        # If the proxy has no fresh M1 quote, defer the scheduled MARKET exit.
        if int(self.time)-self.vars['opened_time'] >= MAX_HOLD_MS and self._fresh_quote():
            self.liquidate()
