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


class R20PaxgPathAnalogue4h(Strategy):
    """PAXG20-02: predeclared price-only development, not independent validation."""

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
        if self.is_open:
            return None
        c = self.candles
        n = len(c)
        if n < 740:
            return None
        close = c[:, 2].astype(float)
        if not np.all(np.isfinite(close)) or np.any(close <= 0):
            return None
        r = np.diff(np.log(close))
        atrs = ta.atr(c, sequential=True)
        j = n-1
        # Origin k's label ends at k+6. Leave eight bars to the current
        # pattern as well, avoiding overlapping training/current input windows.
        origins = np.arange(max(8, j-720), j-8+1, dtype=int)
        scales = atrs[origins-8]/close[origins-8]
        valid = np.isfinite(scales) & (scales > 0)
        origins, scales = origins[valid], scales[valid]
        current_scale = float(atrs[j-8]/close[j-8])
        if len(origins) < 20 or not math.isfinite(current_scale) or current_scale <= 0:
            return None
        # One ATR series and a vectorized view, not 720 repeated indicator calls.
        windows = np.lib.stride_tricks.sliding_window_view(r, 8)
        current = windows[j-8]/current_scale
        vectors = windows[origins-8]/scales[:, None]
        distances = np.sum((vectors-current)**2, axis=1)
        chosen = []
        for ix in np.argsort(distances):
            origin = int(origins[ix])
            if all(abs(origin-other) >= 8 for other in chosen):
                chosen.append(origin)
                if len(chosen) == 20:
                    break
        if len(chosen) < 20:
            return None
        chosen = np.array(chosen, dtype=int)
        forecast = float(np.mean(np.log(close[chosen+6]/close[chosen])))
        atr = self._atr()
        if atr is None or not math.isfinite(forecast) or abs(forecast) <= FEE_FORECAST_HURDLE:
            return None
        return {'direction': 1 if forecast > 0 else -1,
                'distance': 2*atr, 'tp': None, 'hours': 24}

