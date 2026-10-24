import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def participation_event(rows, require_phase):
    """Same-UTC baselines are strictly prior to S, even for B's time slot."""
    window = rows[-170:]
    volume = window[:, 5]
    if not np.all(np.isfinite(volume)) or np.any(volume <= 0):
        return None
    setup, confirmation = window[-2], window[-1]
    previous = float(window[-3, 2])
    atr = atr14(window[:-2])
    displacement = float(setup[2])-previous
    if atr is None or abs(displacement) < atr:
        return None
    fraction = (float(confirmation[2])-float(setup[2]))/(-displacement)
    if not .5 <= fraction < 1:
        return None
    # The170-row exact4h window makes these28 prior daily observations
    # of each distinct UTC slot. Neither event bar enters either baseline.
    setup_reference = volume[np.arange(0, 168, 6)]
    confirmation_reference = volume[np.arange(1, 169, 6)]
    setup_median = float(np.median(setup_reference))
    confirmation_median = float(np.median(confirmation_reference))
    if require_phase and not (setup[5] <= .5*setup_median and confirmation[5] >= confirmation_median):
        return None
    return dict(direction=-1 if displacement > 0 else 1, distance=2*atr)


class BtcResearchR12ParticipationBase1m(BtcResearchR11Base1m):
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
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 170)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("PHASE", "PRICE")
        event = participation_event(rows, self.MODE == "PHASE")
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
