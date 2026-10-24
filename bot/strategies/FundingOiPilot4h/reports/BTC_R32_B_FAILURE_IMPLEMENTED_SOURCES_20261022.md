# R32 B — fuentes implementadas y justificación

Fecha local2026-10-22. Estado: tres fuentes creadas por MCP y leídas completas, pendientes de check sintético autorizado/revisión final; cero drafts o motores económicos. No se modificó ningún padre.

## Implementación

- BtcResearchR32FailureBase1m: helper puro failure_pattern y único hook _event.
- BtcResearchR32FailureAll1m: LABEL B_FAILURE_ALL, PERSIST_ONLY=False.
- BtcResearchR32FailurePersist1m: LABEL B_FAILURE_PERSIST, PERSIST_ONLY=True.

Las hojas comparten HOLD_HOURS48/TP_R2. La función usa26barras de contexto excluyendo b/f/r y clasifica cuatro categorías disjuntas. La única diferencia es seleccionar sólo interior en PERSIST. _event se consume antes de ocupación/sizing por el padre común; memo T<=last impide repetir logs o reusar el evento. Una línea compacta por fallo bruto conserva mismo denominador entre políticas, sin prometer operaciones que habrían llenado.

## Dependencia común actual y precisión documental

R32 actual leído completo: SHA256 205407530bc40ea95131a0e6f2ed3e997b7bb5616bb5c573f170a772317307e3, corresponde al padre aprobado por root con38checks y recibo BTC_R32_COMMON_EXECUTION_CHECK_RECEIPT_20261022.json según root. El anexo CODES, el literal incorporado en el check y los readbacks antes/después conservan exactamente esta MISMA fuente R32 y este hash. No hubo modificación del padre después de crearlo. El hash y literal verificados son la dependencia normativa antes de motores; no se copia nuevamente el anexo314k. Corrección documental: una frase previa de este informe atribuyó equivocadamente al CODES una versión anterior; comparación exacta de ambas cadenas confirma identidad, no cambio de padre.

La infraestructura valida64filas; sólo últimas29 entran en la fórmula. Filas anteriores finitas/coherentes no cambian el patrón, pero corromperlas sí invalida el contrato común. R10ATR14simple/legacy_plan.5wallet/.5margin/reserva.001/lote.001, ejecución, protección, R11 y plazos no se redefinen. No imports de estrategias reales dentro del análisis: sólo AST del source literal y stubs.

## Fuentes finales exactas

### BtcResearchR32FailureBase1m

SHA256 1ef5782f3d84973710372500c7aa276acb9219b89ae7784a3224f1b2b6e268aa; readback completo idéntico al envío, una creación exitosa sin correcciones.

```python
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
```

### BtcResearchR32FailureAll1m

SHA256 bd7611c9a3d60974beacff82593ca20fc16949823cb7d1b589216c5d5a5d7977; readback completo idéntico al envío, una creación exitosa sin correcciones.

```python
from strategies.BtcResearchR32FailureBase1m import BtcResearchR32FailureBase1m


class BtcResearchR32FailureAll1m(BtcResearchR32FailureBase1m):
    LABEL = "B_FAILURE_ALL"
    PERSIST_ONLY = False
```

### BtcResearchR32FailurePersist1m

SHA256 6b571f0e3880a9b2d9b5565a46d705ccf8abe37b2e2b4b66e82831141cb61d77; readback completo idéntico al envío, una creación exitosa sin correcciones.

```python
from strategies.BtcResearchR32FailureBase1m import BtcResearchR32FailureBase1m


class BtcResearchR32FailurePersist1m(BtcResearchR32FailureBase1m):
    LABEL = "B_FAILURE_PERSIST"
    PERSIST_ONLY = True
```

## Check preparado y alcance

BTC_R32_B_FAILURE_SUPPLIED_CHECK_20261022.md contiene el código íntegro que se ejecutará, incluido literal de seis fuentes suministradas. SHA256 del código Python: 6986f7fa5fcb61a7dcd5ccf5d2b053e52706e65ac8c986594d40168deb1452a4. Inputs=[]; salida JSON prevista output/b_failure_check.json. Oráculo Python de categorías contra funciónNumPy,125combinaciones fabricadas y10fixtures reflejados; límites26+3, igualdades, frontera congelada, consumo ocupado/pending/sameexit, reloj/gaps/asof, precio/tamaño1%, lote/reserva y logs.

R11 es stub sólo para el bridge before; su observador y la ejecución común tienen recibo separado, y ningún stub acredita órdenes nativas o funding. Export previsto<48k. No inflar conteo defixtures a confianza estadística. No precios observados ni datos, backtest virtual, frameworkimport, investigación en scripts o filesystem de estrategias.

## Incidentes

Tres creaciones y tres readbacks exitosos. Sin correcciones de fuente en esta versión. El primer ensamblado documental CODES previo falló por clave de memoria; quedó registrado allí, sin jobs/efecto económico. No error nuevo de implementación en esta entrega. La precisión sobre identidad R32 se corrigió documentalmente tras revisión de root; no cambió código ni se repitió análisis.
