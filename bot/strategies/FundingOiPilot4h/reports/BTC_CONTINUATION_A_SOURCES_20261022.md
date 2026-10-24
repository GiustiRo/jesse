# Continuacion A: fuentes creadas, lectura y freeze previo a checks
Fecha local2026-10-22. Tresfuentes nuevas autorizadas porroot creadas porMCP y readback completo exacto. Ningun padre modificado. Cerojobs,drafts,motores o endpoints avelas desde esta tarea.

## Correspondencia con protocolo
Infraestructura R32 se usa literalmente,48h/TP2R/cuotahalf/reserva/lote. Las hojas solo _event/_invalid_event yconstantes. Origen REAL=LABEL A_ACCEPTED/A_CLOSE_ONLY; DAY_ACCEPTANCE delprimertexto era ilustrativo y se sustituyo enprotocolo antes dechecks/economia. No existe uncuartogrupo de cuenta.

Estado comundayD poraperturabloque,primercierre fuera consumeantesfiltro/cuenta y rejectionsnoesperanotra4h. M1vista exacta240asof,paridadOHLC,invalidezconsumeD,≥120strictoutsidenivelprevio; igualdadnocuenta. begin_day previeneT<=last sinreprocesarmatematica. A_EVENT/A_INVALID compactos y un A_M1_READY de prueba deaccesibilidad inicial, sinlogsM1continuos. R32 cuentaeventosdevueltosno raw; universo comun se audita porA_EVENT.

## Hashes y fuentes exactas

### BtcResearchR32DayAcceptanceBase1m
SHA256 UTF8: 740fe4e337f96d9d01d59c82c2a84ed337940e1df4138d5d724a4017dd654193; 4749caracteres. Readbackexacto.

```python
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

```

### BtcResearchR32DayAccepted1m
SHA256 UTF8: a110425ac45a1f4019b62b51c73fa98cba592e1e4302ddb51af1c6f3912a5a50; 218caracteres. Readbackexacto.

```python
from strategies.BtcResearchR32DayAcceptanceBase1m import BtcResearchR32DayAcceptanceBase1m


class BtcResearchR32DayAccepted1m(BtcResearchR32DayAcceptanceBase1m):
    LABEL = "A_ACCEPTED"
    REQUIRE_ACCEPTANCE = True

```

### BtcResearchR32DayCloseOnly1m
SHA256 UTF8: 12aae7b292d76547febf4a513ca94c9ec212274fc6acc846045d3177c03610fd; 222caracteres. Readbackexacto.

```python
from strategies.BtcResearchR32DayAcceptanceBase1m import BtcResearchR32DayAcceptanceBase1m


class BtcResearchR32DayCloseOnly1m(BtcResearchR32DayAcceptanceBase1m):
    LABEL = "A_CLOSE_ONLY"
    REQUIRE_ACCEPTANCE = False

```

## Dependencia comun
BtcResearchR32SpecialistBase1m SHA256 205407530bc40ea95131a0e6f2ed3e997b7bb5616bb5c573f170a772317307e3, leida completa6263caracteres, no editada. R10/R11/R16LegacyBase releidas e identicas a CODES. El manifiesto root debe comprobar que R32 vigente sigueestehash o registrar/revisarcualquierfixtecnico antesdechecks/economia.

## Check preparado, NO ejecutado
Se prepara BTC_CONTINUATION_A_SUPPLIED_SYNTHETIC_CHECK_20261022.md con siete textos completos yhashes, AST sinimportsreales yfixtures OHLC/M1 fabricados. Ningun PASS se afirma hasta ejecucion root/slotautorizado; ninguna validacionnativaMARKET se deduce delstub. Resultado previsto output/BTC_CONTINUATION_A_SYNTHETIC_RESULT.json enworkspace temporal analysis. Fuentes congeladas antesdelresultado, errorestecnicosseconservan ynotuningalpha.
