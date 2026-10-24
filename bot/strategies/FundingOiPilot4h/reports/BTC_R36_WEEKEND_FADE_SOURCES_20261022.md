# R36 A — freeze previo al check

Fuentes guardadas y releídas exactamente por MCP. Una precisión precheck añade now % BAR a la guarda del slot para rechazar segundos/milisegundos sueltos incluso al invocar directamente el helper; el padre ya exige frontera4h. Sin jobs/resultados entre versiones. La primera versión se creó con guardas de weekday/hour/minute, luego se endureció este contrato técnico antes del harness; no cambió señal económica.

- BtcResearchR10Base4h: 8100 caracteres, SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9.
- BtcResearchR11Base1m: 10150 caracteres, SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87.
- BtcResearchR16LegacyBase1m: 14948 caracteres, SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542.
- BtcResearchR32SpecialistBase1m: 6263 caracteres, SHA256 205407530bc40ea95131a0e6f2ed3e997b7bb5616bb5c573f170a772317307e3.
- BtcResearchR36WeekendFade1m: 2706 caracteres, SHA256 b04cae7980e5b3fb5539485a4b2653b934b9250d210b4f0c4c7088e8edad3551.
- BtcResearchR36WeekdayFade1m: 2706 caracteres, SHA256 6c917bb7012c0a56f8b40d476345000df6a2b72538d8e8ed15345b244362548a.

## Hojas finales

### BtcResearchR36WeekendFade1m

```python
import math
from datetime import datetime, timezone

from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR10Base4h import BAR


class BtcResearchR36WeekendFade1m(BtcResearchR32SpecialistBase1m):
    """Fade one fixed 48h calendar displacement; no liquidity causal claim."""
    LABEL = "R36_WEEKEND_FADE"
    HOLD_HOURS = 24
    TP_R = None
    SLOT_WEEKDAY = 0

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

```
### BtcResearchR36WeekdayFade1m

```python
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

```
