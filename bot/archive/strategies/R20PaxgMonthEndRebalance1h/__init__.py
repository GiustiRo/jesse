import math
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing only; fills do not simulate these extra costs.
FEE_FORECAST_HURDLE = 0.0019  # Fixed 9 bps modeled round trip plus 10 bps reserve.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 3600000


class R20PaxgMonthEndRebalance1h(Strategy):
    """PAXG20-10: predeclared price-only development, not independent validation."""

    def _fresh_quote(self, symbol=None):
        symbol = self.symbol if symbol is None else symbol
        c = self.get_candles(self.exchange, symbol, '1m')
        if not len(c) or int(c[-1, 0]) != int(self.time)-60000:
            return None
        price = float(c[-1, 2])
        if not (math.isfinite(price) and price > 0):
            return None
        if symbol == self.symbol and not math.isclose(
                price, float(self.price), rel_tol=1e-10, abs_tol=1e-8):
            return None
        return price

    def _atr(self, c=None):
        c = self.candles if c is None else c
        if len(c) < 30:
            return None
        value = float(ta.atr(c))
        return value if math.isfinite(value) and value > 0 else None

    def _fourhour_atr(self):
        c = self.get_candles(self.exchange, self.symbol, '4h')
        c = c[c[:, 0]+4*HOUR_MS <= int(self.time)]
        return self._atr(c)

    def _local_time(self):
        return datetime.fromtimestamp(int(self.time)/1000, tz=NEW_YORK)

    def _paired_fix(self):
        local = self._local_time()
        if local.weekday() > 4 or local.hour != 16 or local.minute != 0:
            return None
        own, spy = self._fresh_quote(), self._fresh_quote('SPY-USDT')
        if own is None or spy is None:
            return None
        fixes = self.vars.setdefault('paired_fixes', [])
        day = local.date().isoformat()
        if fixes and fixes[-1]['date'] == day:
            return None
        fixes.append({'date': day, 'time': int(self.time), 'own': own, 'spy': spy})
        # These models need at most 22 observations; retain a wider history for gaps.
        self.vars['paired_fixes'] = fixes[-200:]
        return self.vars['paired_fixes']

    def before(self) -> None:
        if self.vars.get('processed_index') == self.index:
            return
        self.vars['processed_index'] = self.index
        # State and episode consumption run even when a position is open.
        # An occupied event is discarded on the next bar, never queued.
        self.vars['r20_event'] = self._model_event()

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        event = self.vars.get('r20_event')
        if self.symbol != 'PAXG-USDT' or not event or self._fresh_quote() is None:
            return 0
        entry = float(self.price)
        distance = float(event['distance'])
        direction = int(event['direction'])
        if not (math.isfinite(distance) and 0 < distance < entry and direction in (-1, 1)):
            return 0
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        stop = entry-direction*distance
        unit_risk = distance+self.fee_rate*(entry+stop)+SLIPPAGE_RESERVE*entry
        room = min(capital*NOTIONAL_CAP,
                   max(0.0, float(self.leveraged_available_margin)*0.90))
        qty = min(capital*TRADE_RISK/unit_risk, room/entry)
        # Existing PAXG research precision, not proof of native contract lot rules.
        qty = math.floor(qty/0.0001)*0.0001
        if qty <= 0:
            return 0
        self.vars['r20_plan'] = dict(event, qty=qty, entry=entry)
        self.vars['signal_value'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['r20_plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['r20_plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; unexpected pending entries cannot persist.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['r20_plan']
        self.vars['r20_opened'] = int(self.position.opened_at)
        self.vars['r20_hours'] = float(plan['hours'])
        self.vars['r20_month_exit'] = bool(plan.get('month_exit', False))
        self.vars['r20_open_month'] = self._local_time().strftime('%Y-%m')
        self.vars['r20_exit_fixings'] = 0
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        self.stop_loss = abs(self.position.qty), entry-direction*plan['distance']
        if plan.get('tp') is not None:
            self.take_profit = abs(self.position.qty), entry+direction*plan['tp']

    def update_position(self) -> None:
        elapsed = int(self.time)-self.vars['r20_opened']
        due = elapsed >= self.vars['r20_hours']*HOUR_MS
        if self.vars.get('r20_month_exit'):
            due = due or self.vars.get('r20_exit_fixings', 0) >= 3
        if due and self._fresh_quote() is not None:
            self.liquidate()

    def _model_event(self):
        fixes = self._paired_fix()
        if fixes is None:
            return None
        local = self._local_time()
        # Count observed paired fixings, not fabricated business-day candles.
        if self.is_open and local.strftime('%Y-%m') != self.vars.get('r20_open_month'):
            self.vars['r20_exit_fixings'] = self.vars.get('r20_exit_fixings', 0)+1
        if len(fixes) < 22:
            return None
        next_day = local.date()+timedelta(days=1)
        while next_day.weekday() > 4:
            next_day += timedelta(days=1)
        if next_day.month == local.month:
            return None
        month = local.strftime('%Y-%m')
        if self.vars.get('month_consumed') == month:
            return None
        own = np.array([f['own'] for f in fixes[-22:]], dtype=float)
        spy = np.array([f['spy'] for f in fixes[-22:]], dtype=float)
        relative = np.diff(np.log(own))-np.diff(np.log(spy))
        sigma = float(np.std(relative[:-1], ddof=1))
        # sqrt(20) is a fixed scale heuristic, not an IID confidence claim.
        scale = math.sqrt(20)*sigma
        movement = math.log(own[-1]/own[-21])-math.log(spy[-1]/spy[-21])
        if not (math.isfinite(scale) and scale > 0 and math.isfinite(movement)):
            return None
        if abs(movement) < scale:
            return None
        self.vars['month_consumed'] = month
        atr = self._fourhour_atr()
        if atr is None:
            return None
        return {'direction': -1 if movement > 0 else 1,
                'distance': 2*atr, 'tp': None, 'hours': 240, 'month_exit': True}

