# Línea C — dos hojas propuestas para infraestructura R32 común
Fecha local2026-10-22. Sustituye la propuesta inicial de base C duplicada. Sólo fuentes literales para revisión; ningún archivo de estrategia escrito ni importado, ningún job/check/motor ejecutado.
Leídos completos porMCP BtcResearchR32SpecialistBase1m (6263caracteres) y BTC_R32_COORDINATION_PROTOCOL_20261022.md. Ambas hojas sólo definen evento causal y constantes; capital/órdenes/ATR/stop/salida/observador/logs son responsabilidad de esa base. Señal,24h y ausenciaTP no cambian.

## strategies/BtcResearchR32InsideRange1m/__init__.py
```python
from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m


def containment_event(rows, now, require_inside):
    """Resolve one fixed B2 mother after B1; no stored or deferred episode."""
    mother, prior, current = rows[-3:]
    high, low = float(mother[3]), float(mother[4])
    inside = bool(float(prior[3]) < high and float(prior[4]) > low)
    close_inside = bool(low < float(prior[2]) < high)
    if not high > low or not close_inside or (require_inside and not inside):
        return None
    close = float(current[2])
    direction = 1 if close > high else -1 if close < low else 0
    if direction == 0:
        return None
    # The close resolves even a bar that traded beyond both mother boundaries.
    return dict(direction=direction, meta=dict(
        mother_at=int(mother[0]), prior_at=int(prior[0]), resolution_at=now,
        mother_high=high, mother_low=low, prior_close=float(prior[2]),
        prior_inside=inside, resolution_close=close))


class BtcResearchR32InsideRange1m(BtcResearchR32SpecialistBase1m):
    LABEL = "C_INSIDE"
    HOLD_HOURS = 24
    TP_R = None

    def _event(self, rows, now):
        return containment_event(rows, now, True)
```

## strategies/BtcResearchR32CloseRange1m/__init__.py
```python
from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR32InsideRange1m import containment_event


class BtcResearchR32CloseRange1m(BtcResearchR32SpecialistBase1m):
    LABEL = "C_CLOSE_ONLY"
    HOLD_HOURS = 24
    TP_R = None

    def _event(self, rows, now):
        return containment_event(rows, now, False)
```

BtcResearchR32CloseRange1m importa containment_event, función pura definida en móduloINSIDE; usa la misma regla con el único cambio require_inside=False. No instancia la otrahoja ni comparte posición/estado. Manifiesto/checks deben incluir ambas fuentes y basecomún/dependencias.
_event recibe64OHLC cerradas/validadas por base. Sólo usaúltimas3 para señal; ATR15 común no está en hojas. B2madre fija,B1contenida,B0resuelve; igualdadfuera/ningúnlado→None; si ambos extremos rotos manda cierre; no latchni rearmado oculto. Tripleta nueva en siguiente4h y evaluaciónantesocupación/sizingporbase.
LABEL únicos C_INSIDE/C_CLOSE_ONLY,HOLD_HOURS24,TP_RNone. Helperlegacy(.5wallet,.5margin),reserva.001/lote.001 yR11heredados, sin cuota diaria añadida ni overrides de before/on_open/update_position/_emit. R32_PLAN contiene meta compacta,OPENseñal/fill/qty/D/risk_budget, CLOSE/SUMMARYcompartidos.
Antes de implementar root revisa y autoriza hojas. Checks sintéticos aún pendientes según protocolo; no afirmar compile,oráculos,riesgo,ordenes o clocks verificados por esteentregable.
