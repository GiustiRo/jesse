import math
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing reserve only, not simulated adverse fills.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 60 * 60 * 1000
EVENT_ATR = 1.0  # Material two-calendar-day displacement; fixed before outcomes.
STOP_ATR = 2.0  # Same safety distance for weekend and weekday controls.
MAX_HOLD_MS = 24 * HOUR_MS


class ResearchPaxgWeekendReturn1h(Strategy):
    """Reversion of PAXG own price; not observed gold fair value.

    Paxos documents Friday17ET/Sunday18ET primary-market closure, with the
    secondary order book continuing. Friday16/Sunday16 fixings precede
    those edges; the weekday control tests generic two-day reversion.
    """
    ANCHOR_DAY = 4
    EVENT_DAY = 6

    def _fixing(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(c) or int(c[-1, 0]) != int(self.time)-60000:
            return None
        price = float(c[-1, 2])
        if not (math.isfinite(price) and price > 0):
            return None
        # Consistency invariant: both current route and M1 end at this fixing.
        if not math.isclose(float(self.price), price, rel_tol=1e-10, abs_tol=1e-8):
            return None
        return price

    def _local_time(self):
        # IANA timezone handles the spring/autumn weekend's 47/49-hour anchor lag.
        return datetime.fromtimestamp(int(self.time)/1000, tz=NEW_YORK)

    def before(self) -> None:
        local = self._local_time()
        if local.weekday() != self.ANCHOR_DAY or local.hour != 16 or local.minute != 0:
            return
        price = self._fixing()
        if price is None:
            return
        c = self.get_candles(self.exchange, self.symbol, '4h')
        # Causal partial higher-timeframe bars are excluded from the fixed ATR recipe.
        c = c[c[:, 0]+4*HOUR_MS <= int(self.time)]
        if len(c) < 30:
            return
        atr = float(ta.atr(c))
        if not (math.isfinite(atr) and atr > 0):
            return
        self.vars['anchor'] = {'date': local.date().isoformat(), 'price': price,
                               'atr': atr, 'time': int(self.time)}

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal']
        self.vars['signal_index'] = self.index
        self.vars['signal'] = 0
        if self.symbol != 'PAXG-USDT':
            return 0
        local = self._local_time()
        if local.weekday() != self.EVENT_DAY or local.hour != 16 or local.minute != 0:
            return 0
        anchor = self.vars.get('anchor')
        if not anchor or anchor['date'] != (local.date()-timedelta(days=2)).isoformat():
            return 0
        price = self._fixing()
        if price is None:
            return 0
        move = price-anchor['price']
        if abs(move) < EVENT_ATR*anchor['atr']:
            return 0
        direction = -1 if move > 0 else 1
        distance = STOP_ATR*anchor['atr']
        if distance >= price:
            return 0
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        risk, notional = 0.0, 0.0
        for route in self.routes:
            if route.exchange != self.exchange or not route.strategy.is_open:
                continue
            s = route.strategy
            qty = abs(float(s.position.qty))
            value = abs(float(s.position.value))
            mark = value/qty if qty else float(s.position.entry_price)
            stop = float(s.average_stop_loss)
            gap = max(0.0, mark-stop) if s.is_long else max(0.0, stop-mark)
            risk += qty*(gap+mark*(self.fee_rate+SLIPPAGE_RESERVE))
            notional += value
        stop = price-direction*distance
        unit_risk = distance+self.fee_rate*(price+stop)+SLIPPAGE_RESERVE*price
        budget = min(capital*TRADE_RISK, max(0.0, capital*PORTFOLIO_RISK-risk))
        room = min(max(0.0, capital*NOTIONAL_CAP-notional),
                   max(0.0, float(self.leveraged_available_margin)*0.90))
        qty = min(budget/unit_risk, room/price)
        # Existing research precision; native lot restrictions remain unverified.
        qty = math.floor(qty/0.0001)*0.0001
        if qty <= 0:
            return 0
        self.vars['plan'] = {'qty': qty, 'distance': distance, 'target': anchor['price']}
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
        # MARKET entries should not survive; unexpected pending orders expire.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['plan']
        entry = float(self.position.entry_price)
        self.vars['opened_time'] = int(self.position.opened_at)
        stop = entry-plan['distance'] if self.is_long else entry+plan['distance']
        self.stop_loss = abs(self.position.qty), stop
        self.take_profit = abs(self.position.qty), plan['target']

    def update_position(self) -> None:
        # Management stays continuous; overdue time exits await a fresh fixing.
        if int(self.time)-self.vars['opened_time'] >= MAX_HOLD_MS and self._fixing() is not None:
            self.liquidate()
