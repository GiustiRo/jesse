import numpy as np

from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m


def failure_pattern(rows):
    """Classify 26 prior ranges, then breakout/failure/resolution closes.

    R32 validates the full 64-row clock/OHLC contract before calling the leaf.
    Only the last 29 rows define this pattern; no signal-bar extreme moves
    the frozen boundary. Equality is never an interior or exterior crossing.
    """
    context = rows[-29:-3]
    lower = float(np.min(context[:, 4]))
    upper = float(np.max(context[:, 3]))
    if lower >= upper:
        return None
    breakout, failure, resolution = rows[-3], rows[-2], rows[-1]
    c_b, c_f, c_r = (float(row[2]) for row in (breakout, failure, resolution))
    side = 1 if c_b > upper else -1 if c_b < lower else 0
    if side == 0 or not lower < c_f < upper:
        return None
    if lower < c_r < upper:
        category = "interior"
    elif c_r == lower or c_r == upper:
        category = "boundary"
    elif (side == 1 and c_r > upper) or (side == -1 and c_r < lower):
        category = "recovered_original"
    else:
        category = "crossed_opposite"
    return dict(
        breakout_at=int(breakout[0]), failure_at=int(failure[0]),
        resolution_at=int(resolution[0]), lower=lower, upper=upper,
        breakout_close=c_b, failure_close=c_f, resolution_close=c_r,
        breakout_side=side, category=category)


class BtcResearchR32FailureBase1m(BtcResearchR32SpecialistBase1m):
    """Observe the same raw failures before policy, occupancy and sizing."""
    PERSIST_ONLY = None
    HOLD_HOURS = 48
    TP_R = 2.0

    def _event(self, rows, now):
        assert isinstance(self.PERSIST_ONLY, bool)
        previous = self.vars.get("r32_b_last_event")
        if previous is not None and now <= previous:
            return None
        self.vars["r32_b_last_event"] = now
        pattern = failure_pattern(rows)
        if pattern is None:
            return None
        selected = not self.PERSIST_ONLY or pattern["category"] == "interior"
        # One compact row per raw pattern, including rejected and occupied
        # events. These denominators describe opportunities, not native fills.
        self._log("R32_B_PATTERN", dict(
            policy=self.LABEL, time=int(now), selected=selected, **pattern))
        if not selected:
            return None
        return dict(direction=-pattern["breakout_side"], meta=pattern)
