import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR13ExternalBase1m import HOUR, closed_hour_window
from strategies.BtcResearchR10Base4h import atr14, entry_plan


def round_event(rows, consumed, offset):
    """Fixed grids, no favorable choice among multiple barriers in one bar."""
    consumed = dict(consumed)
    atr = atr14(rows[:-1])
    if atr is None:
        return None, {}
    previous, close = float(rows[-2, 2]), float(rows[-1, 2])
    low, high = float(rows[-1, 4]), float(rows[-1, 3])
    rearmed = set()
    for level in list(consumed):
        if abs(close-level) > atr:
            consumed.pop(level)
            rearmed.add(level)
    first, last = math.ceil((low-offset)/1000), math.floor((high-offset)/1000)
    if last-first+1 != 1:
        return None, consumed
    level = float(1000*first+offset)
    if level in consumed or level in rearmed:
        return None, consumed
    direction = 0
    if previous < level and high >= level+.25*atr and close < level:
        direction = -1
    elif previous > level and low <= level-.25*atr and close > level:
        direction = 1
    if not direction:
        return None, consumed
    consumed[level] = int(rows[-1, 0])+HOUR
    return dict(direction=direction, distance=atr), consumed


class BtcResearchR13RoundBase1m(BtcResearchR11Base1m):
    OFFSET = 0

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % HOUR:
            return
        rows = closed_hour_window(self.get_candles(self.exchange, self.symbol, "1h"), now)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["round_consumed"] = {}
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.OFFSET in (0, 500)
        event, consumed = round_event(rows, self.vars.get("round_consumed", {}), self.OFFSET)
        self.vars["round_consumed"] = consumed
        if event is None or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = event["direction"]
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, event["distance"])
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def update_position(self):
        if int(self.time) % HOUR == 0 and int(self.time)-int(self.position.opened_at) >= 12*HOUR:
            self.liquidate()
