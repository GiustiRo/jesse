import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

HOUR = 3600000


def closed_hours(candles, now):
    """Exact 25 closed hourly prices; no US-session filter on continuous BTC."""
    rows = candles[candles[:, 0]+HOUR <= now][-25:]
    if len(rows) != 25 or rows[-1, 0] != now-HOUR:
        return None
    if not np.all(np.diff(rows[:, 0]) == HOUR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])) or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def jump_state(hourly, atr, price):
    """Finite-window RV/BV heuristic, never an asymptotic jump significance test."""
    increments = np.diff(np.log(hourly[:, 2]))
    rv = float(np.square(increments).sum())
    if not math.isfinite(rv) or rv <= 0 or atr is None:
        return 0
    bv = (math.pi/2)*(24/23)*float(np.abs(increments[1:]*increments[:-1]).sum())
    fraction = max(rv-bv, 0.)/rv
    total = float(increments.sum())
    if fraction < 1/3 or abs(total) < .5*atr/price:
        return 0
    return 1 if total > 0 else -1 if total < 0 else 0


class BtcResearchR12JumpBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 15)
        hourly = closed_hours(self.get_candles(self.exchange, self.symbol, "1h"), now)
        if rows is None or hourly is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["jump_state"] = 0
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert math.isclose(float(hourly[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        atr = atr14(rows)
        state = jump_state(hourly, atr, float(self.price))
        previous = self.vars.get("jump_state", 0)
        self.vars["jump_state"] = state
        if not state or state == previous or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        assert self.MODE in ("FADE", "FOLLOW")
        direction = -state if self.MODE == "FADE" else state
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction
