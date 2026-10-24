import math
from datetime import datetime, timezone

from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR10Base4h import BAR


class BtcResearchR36WeekdayFade1m(BtcResearchR32SpecialistBase1m):
    """Fade one fixed 48h calendar displacement; no liquidity causal claim."""
    LABEL = "R36_WEEKDAY_FADE"
    HOLD_HOURS = 24
    TP_R = None
    SLOT_WEEKDAY = 3

    def _clock_counts(self):
        return self.vars.setdefault("r36_clock", dict(
            slots=0, invalid=0, zero=0, nonzero=0))

    def _consume_slot(self, now):
        # Bounds precede any return calculation, including START Thursday.
        if not self.START < now < self.FINISH or now % BAR:
            return False
        stamp = datetime.fromtimestamp(now/1000, timezone.utc)
        if stamp.weekday() != self.SLOT_WEEKDAY or stamp.hour or stamp.minute:
            return False
        if now <= self.vars.get("r36_last_slot", -1):
            return False
        self.vars["r36_last_slot"] = now
        self._clock_counts()["slots"] += 1
        return True

    def _invalid_event(self, now):
        # Missing history consumes this fixed slot; it cannot move to later.
        if self._consume_slot(now):
            self._clock_counts()["invalid"] += 1
            self._log("R36_SLOT", dict(label=self.LABEL, time=now,
                prior_close_time=now-12*BAR, actual_close_time=now,
                status="invalid_window"))

    def _event(self, rows, now):
        if not self._consume_slot(now):
            return None
        # Thirteen closes span exactly twelve already-closed 4h intervals.
        previous, current = float(rows[-13, 2]), float(rows[-1, 2])
        displacement = current-previous
        direction = -1 if displacement > 0 else 1 if displacement < 0 else 0
        counts = self._clock_counts()
        counts["nonzero" if direction else "zero"] += 1
        meta = dict(prior_close_time=now-12*BAR, actual_close_time=now,
                    prior_close=previous, actual_close=current,
                    displacement=displacement,
                    log_return=math.log(current)-math.log(previous),
                    formation_hours=48, weekday=self.SLOT_WEEKDAY)
        self._log("R36_SLOT", dict(label=self.LABEL, time=now,
            status="nonzero" if direction else "zero",
            direction=direction, **meta))
        return dict(direction=direction, meta=meta) if direction else None

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R36_CLOCK", dict(stage=stage, label=self.LABEL,
            weekday=self.SLOT_WEEKDAY, formation_hours=48,
            **self._clock_counts()))
