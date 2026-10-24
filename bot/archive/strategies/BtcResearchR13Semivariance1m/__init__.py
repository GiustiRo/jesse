import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def semivariance_state(rows):
    """R20's quiet gate belongs to the state and therefore resets it to zero."""
    returns = np.diff(np.log(rows[-61:, 2]))
    atr = atr14(rows)
    up = float(np.square(returns[returns > 0]).sum())
    down = float(np.square(returns[returns < 0]).sum())
    if atr is None or up <= 0 or down <= 0 or abs(float(returns.sum())) > atr/float(rows[-1, 2]):
        return 0
    return 1 if up/down >= 3 else -1 if down/up >= 3 else 0


class BtcResearchR13Semivariance1m(BtcResearchR11Base1m):
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
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 61)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["semivariance_state"] = 0
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        state = semivariance_state(rows)
        previous = self.vars.get("semivariance_state", 0)
        self.vars["semivariance_state"] = state
        if not state or state == previous or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), state, 2*atr)
        if plan is None or self.price+state*1.5*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = state

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        assert qty*(plan["distance"]+self.fee_rate*(entry+stop)) <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, entry+direction*1.5*plan["distance"]
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")
