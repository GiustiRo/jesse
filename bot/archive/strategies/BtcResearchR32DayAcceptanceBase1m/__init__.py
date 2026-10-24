import numpy as np

from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR10Base4h import BAR, DAY

MINUTE = 60000


def begin_day(strategy, now):
    """Day belongs to the OPEN of the closed block, including the20-24 block."""
    assert now % BAR == 0
    state = strategy.vars.setdefault("r32_a_day", dict(
        day=None, consumed=False, last=None, invalid_logged=False))
    if state["last"] is not None and now <= state["last"]:
        return None
    state["last"] = now
    day = (now-BAR)//DAY*DAY
    if day != state["day"]:
        state.update(day=day, consumed=False, invalid_logged=False)
    return state


def invalidate_day(strategy, state, now, reason):
    # Unknown first-event history must never be backfilled later the same day.
    state["consumed"] = True
    if not state["invalid_logged"]:
        state["invalid_logged"] = True
        strategy._log("A_INVALID", dict(label=strategy.LABEL, time=now,
            day_D=state["day"], reason=reason))


def previous_day_range(rows, day):
    required = day-DAY+np.arange(6, dtype=np.int64)*BAR
    indexes = np.searchsorted(rows[:, 0], required)
    if (np.any(indexes >= len(rows))
            or not np.array_equal(rows[indexes, 0], required)):
        return None
    reference = rows[indexes]
    high, low = float(np.max(reference[:, 3])), float(np.min(reference[:, 4]))
    if not np.isfinite(high) or not np.isfinite(low) or not 0 < low < high:
        return None
    return high, low


def minute_block(candles, bar, now):
    """Bounded view of240closed M1; no full-history mask or gap repair."""
    if candles is None or np.ndim(candles) != 2 or candles.shape[1] < 5:
        return None, "M1_shape"
    start = now-BAR
    left = int(np.searchsorted(candles[:, 0], start, side="left"))
    right = int(np.searchsorted(candles[:, 0], now, side="left"))
    minutes = candles[left:right]
    expected = start+np.arange(240, dtype=np.int64)*MINUTE
    if len(minutes) != 240 or not np.array_equal(minutes[:, 0], expected):
        return None, "M1_timestamps"
    if (not np.all(np.isfinite(minutes[:, :5]))
            or np.any(minutes[:, 1:5] <= 0)
            or np.any(minutes[:, 3] < np.maximum(minutes[:, 1], minutes[:, 2]))
            or np.any(minutes[:, 4] > np.minimum(minutes[:, 1], minutes[:, 2]))):
        return None, "M1_OHLC"
    aggregate = np.array([minutes[0, 1], minutes[-1, 2],
                          np.max(minutes[:, 3]), np.min(minutes[:, 4])])
    # Float representation tolerance is data parity only, never a trading band.
    if not np.allclose(aggregate, bar[[1, 2, 3, 4]], rtol=1e-10, atol=1e-8):
        return None, "M1_4h_parity"
    return minutes, None


class BtcResearchR32DayAcceptanceBase1m(BtcResearchR32SpecialistBase1m):
    """First daily range escape, with optional time-outside acceptance.

    Raw event is consumed BEFORE context/occupancy/risk. Both policies have
    identical market state and common M1 validity, irrespective of their fills.
    """
    REQUIRE_ACCEPTANCE = None
    HOLD_HOURS = 48
    TP_R = 2.0

    def _invalid_event(self, now):
        state = begin_day(self, now)
        if state is not None:
            invalidate_day(self, state, now, "4h_window")

    def _event(self, rows, now):
        state = begin_day(self, now)
        if state is None or state["consumed"]:
            return None
        bounds = previous_day_range(rows, state["day"])
        if bounds is None:
            invalidate_day(self, state, now, "reference")
            return None
        minutes, reason = minute_block(self.candles, rows[-1], now)
        if minutes is None:
            invalidate_day(self, state, now, reason)
            return None
        if not self.vars.get("r32_a_m1_verified"):
            self.vars["r32_a_m1_verified"] = True
            self._log("A_M1_READY", dict(label=self.LABEL, time=now, count=240))
        high, low = bounds
        close = float(rows[-1, 2])
        direction = 1 if close > high else -1 if close < low else 0
        if not direction:
            return None
        state["consumed"] = True
        count = int(np.count_nonzero(
            minutes[:, 2] > high if direction == 1 else minutes[:, 2] < low))
        accepted = count >= 120  # At least half; equality to the level is excluded.
        meta = dict(day_D=state["day"], H=high, L=low, n_out=count,
                    accepted=accepted)
        self._log("A_EVENT", dict(label=self.LABEL, time=now,
            direction=direction, **meta))
        assert self.REQUIRE_ACCEPTANCE in (True, False)
        if self.REQUIRE_ACCEPTANCE and not accepted:
            return None
        return dict(direction=direction, meta=meta)
