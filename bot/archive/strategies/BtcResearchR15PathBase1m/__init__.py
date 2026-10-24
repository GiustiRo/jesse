import math
import numpy as np

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

DAY = 86400000


def day_path(rows):
    """Pure daily path label; reject extrema whose order is unidentified."""
    if rows.ndim != 2 or rows.shape[1] < 5 or len(rows) < 6:
        return None
    block = rows[-6:]
    # Volume is deliberately unused in both policies. A forming or displaced
    # day is never relabelled by shifting the six-bar window.
    if not np.all(np.isfinite(block[:, :5])):
        return None
    times = block[:, 0]
    start = float(times[0])
    if start % DAY != 0 or not np.array_equal(times, start + np.arange(6) * BAR):
        return None
    if np.any(block[:, 1:5] <= 0):
        return None
    if (np.any(block[:, 3] < np.maximum(block[:, 1], block[:, 2]))
            or np.any(block[:, 4] > np.minimum(block[:, 1], block[:, 2]))):
        return None
    opening, close = float(block[0, 1]), float(block[-1, 2])
    if close == opening:
        return None
    highs = np.flatnonzero(block[:, 3] == np.max(block[:, 3]))
    lows = np.flatnonzero(block[:, 4] == np.min(block[:, 4]))
    # Do not resolve ties by a favorable first/last occurrence, or infer the
    # high/low order inside the same four-hour bar.
    if len(highs) != 1 or len(lows) != 1 or highs[0] == lows[0]:
        return None
    high_index, low_index = int(highs[0]), int(lows[0])
    direction = 1 if close > opening else -1
    repair = ((direction == 1 and high_index < low_index)
              or (direction == -1 and low_index < high_index))
    return dict(direction=direction, repair=bool(repair),
                label="repair" if repair else "body_only",
                high_index=high_index, low_index=low_index)


class BtcResearchR15PathBase1m(BtcResearchR11Base1m):
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
        # A UTC data-aggregation clock on continuous BTC, not market hours.
        if now % DAY:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 15)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("REPAIR", "BODY")
        event = day_path(rows)
        if event is None:
            return
        if not self.START < now < self.FINISH:
            return
        counts = self.vars.setdefault("day_path_counts", {"repair": 0, "body_only": 0})
        counts[event["label"]] += 1
        if self.MODE == "REPAIR" and not event["repair"]:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        # Daily entries retain the common four-hour ATR protection. The current
        # day's closed bars are known; this is not a daily-ATR substitution.
        atr = atr14(rows)
        if atr is None:
            return
        direction = event["direction"]
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = dict(plan, path_label=event["label"],
                                 high_index=event["high_index"], low_index=event["low_index"])
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        # Persist the observed label only after an actual simulated opening fill.
        self._log("R15_PATH_OPEN", dict(
            time=int(self.time), path_label=plan["path_label"],
            high_index=plan["high_index"], low_index=plan["low_index"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R15_PATH_STATS", dict(
            stage=stage, counts=self.vars.get("day_path_counts", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
