# Piloto A/B funding: reglas y selección prerregistradas
Fecha: 2026-10-20. Estado: reglas fijadas ANTES de ejecutar nuevas sesiones.
User autorizó ejecutar la validación, sin ML, sin OI como señal, sin2026.

## Dos variantes y reglas
A: FundingWfPilotBase4h. BTC-USDT Binance perpetual, decisiones4h sobre ejecución1m.
Entrada long si el cierre4h supera el máximo del día UTC anterior completo; short si está debajo del mínimo. Sólo se admite una nueva entrada por día UTC. Esta referencia mecánica es una elección del piloto, no una réplica ni una ventaja acreditada por el legacy.
Stop2%, target4%, salida al alcanzar24h en un cierre4h si sigue abierta. Qty calculada con presupuesto 2% del margen disponible dividido por pérdida por unidad al stop más comisiones de entrada y salida. Notional limitado al capital disponible; conversión size_to_qty precision8. Funding y slippage son costes adicionales fuera de ese presupuesto. Sin piramidar ni modificar salidas.
B: FundingWfPilotFiltered4h hereda A y cambia únicamente FUNDING_FILTER=True:
- referencia:30 eventos finales publicados anteriores, excluyendo el más reciente.
- z=(último-mean(referencia))/std(referencia), ddof0. Exigir31eventos totales, dispersión real (ptp>0), std>0 y valor finito.
- bloquear long con rate>0,z>2; bloquear short con rate<0,z<-2.
- historial insuficiente o varianza nula: no abre B. Esto se registra aparte de los bloqueos adversos.
- No se calcula una tasa estimada histórica ni se adelantan eventos.
Ambas variantes comprueban available_at<=self.time y usan exclusivamente velas cerradas del día previo. No se usa OI.

## Datos y costes comunes
Capital10000 USDT; fee0.00045 por ejecución; isolated3x; warmup240velas4h. Configuración por sesión, sin cambiar ajustes globales.
Funding contable ON en todas: dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 (hasta2025).
La biblioteca contiene marcas aproximadas antiguas: se reportarán los movimientos del piloto afectados. No se afirma exactitud de esos costes.
No hay modelo independiente de slippage en este primer A/B. Por tanto no acredita robustez de ejecución. Si surge una candidata, deberá superar después estrés de fricción; no se agregan reglas para mejorar su rentabilidad durante el piloto.
El motor hará replay completo de1m por funding aunque el draft solicite fast_mode.

## Ventanas inalterables
F1 desarrollo [2020-09-01,2022-01-01), validación [2022-01-01,2022-07-01).
F2 desarrollo [2020-09-01,2023-01-01), validación [2023-01-01,2023-07-01).
Los tramos de desarrollo se solapan por diseño expansivo; no sumar sus retornos como evidencia independiente.
Ejecutar A y B en ambos desarrollos. Registrar la selección usando exclusivamente esos resultados ANTES de lanzar las validaciones.
Después ejecutar A y B en ambas validaciones para la comparación controlada; ninguna selección posterior se atribuye a desarrollo.

## Selección fijada antes de resultados
Elegible en desarrollo:>=30trades, neto>0, PF>=1.2 y abs(max_drawdown)<=25%.
Entre elegibles: mayor net_profit_percentage; luego mayor PF; luego menor abs(DD); empate restante favorece A por menor complejidad.
Si ninguna es elegible, registrar SIN_CANDIDATA. No forzar ganadora ni rebajar criterios.
Los resultados de validación de candidatos no seleccionados se describirán como diagnóstico A/B y no como rendimiento de una estrategia seleccionada walk-forward.
Sin optimización de30/2 ni de stops, horizonte, rango, sizing o calendario. Máximo8sesiones económicas planeadas (4desarrollo+4validación), más reintentos sólo para errores técnicos documentados.

## Criterios del piloto
Técnico: sesiones terminadas, datos causales, ledgerreconciliado con cada trade, sin OI/2026; única diferencia de código entre A/B es el gate.
Económico: informar neto, PF, DD, Sharpe, trades, precio bruto, fees, funding, reparto direccional y estabilidad por fold.
No declarar edge por una mejora pequeña o un único fold; no confundir filtro que reduce exposición con mejora de señal.
Sin datos suficientes: inconcluso. Objetivos mensuales y aprobación para producción quedan fuera de este control.

## Código congelado A
```python
import json

import numpy as np

from jesse import utils
from jesse.strategies import Strategy


class FundingWfPilotBase4h(Strategy):
    """Frozen mechanical price control; no claim of a demonstrated trading edge."""

    FUNDING_FILTER = False
    DAY_MS = 86_400_000
    STOP_FRACTION = 0.02
    TARGET_FRACTION = 0.04
    RISK_PERCENT = 2
    MAX_HOLD_MS = DAY_MS
    REFERENCE_EVENTS = 30
    EXTREME_Z = 2.0

    def before(self):
        day = int(self.time) // self.DAY_MS * self.DAY_MS
        candles = self.candles
        # Only the previous completed UTC day supplies the breakout boundaries.
        previous = candles[(candles[:, 0] >= day - self.DAY_MS) & (candles[:, 0] < day)]
        direction = 0
        if len(previous) == 6 and len(set(previous[:, 0])) == 6:
            assert max(previous[:, 0]) + 4 * 3_600_000 <= self.time
            upper = float(np.max(previous[:, 3]))
            lower = float(np.min(previous[:, 4]))
            direction = 1 if self.price > upper else -1 if self.price < lower else 0

        rows = self.get_funding_history(count=self.REFERENCE_EVENTS + 1)
        assert all(row["available_at"] <= self.time for row in rows)
        valid = False
        adverse = False
        zscore = None
        if len(rows) == self.REFERENCE_EVENTS + 1:
            latest = rows[-1]
            reference = np.array([row["rate_decimal"] for row in rows[:-1]], dtype=float)
            deviation = float(np.std(reference, ddof=0))
            # Equal historical rates do not define a standardized surprise.
            # This frozen pilot requires nonzero dispersion in filtered entries.
            if np.ptp(reference) > 0 and deviation > 0 and np.isfinite(deviation):
                zscore = (latest["rate_decimal"] - float(np.mean(reference))) / deviation
                valid = bool(np.isfinite(zscore))
                adverse = valid and (
                    (direction == 1 and latest["rate_decimal"] > 0 and zscore > self.EXTREME_Z)
                    or (direction == -1 and latest["rate_decimal"] < 0 and zscore < -self.EXTREME_Z)
                )

        opportunity = direction != 0 and self.vars.get("entry_day") != day and self.is_close
        allowed = opportunity and (not self.FUNDING_FILTER or (valid and not adverse))
        self.vars["context"] = {"day": day, "direction": direction, "allowed": allowed}
        audit = self.vars.setdefault("audit", {
            "bars": 0, "price_opportunities": 0, "adverse_blocks": 0,
            "unavailable_blocks": 0, "entries": 0,
        })
        audit["bars"] += 1
        if opportunity:
            audit["price_opportunities"] += 1
            if self.FUNDING_FILTER and not valid:
                audit["unavailable_blocks"] += 1
            elif self.FUNDING_FILTER and adverse:
                audit["adverse_blocks"] += 1

    def should_long(self):
        context = self.vars["context"]
        return context["allowed"] and context["direction"] == 1

    def should_short(self):
        context = self.vars["context"]
        return context["allowed"] and context["direction"] == -1

    def _enter(self, direction):
        stop = self.price * (1 - direction * self.STOP_FRACTION)
        # Budget price loss plus both execution fees at the stop; funding and
        # slippage remain additional costs. Cap notional at available capital.
        capital = self.available_margin
        unit_loss = abs(self.price - stop) + self.fee_rate * (self.price + stop)
        notional = min(capital, capital * self.RISK_PERCENT / 100 / unit_loss * self.price)
        qty = utils.size_to_qty(notional, self.price, precision=8)
        self.vars["entry_day"] = self.vars["context"]["day"]
        if direction == 1:
            self.buy = qty, self.price
        else:
            self.sell = qty, self.price

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        direction = 1 if self.is_long else -1
        entry = self.position.entry_price
        self.stop_loss = abs(self.position.qty), entry * (1 - direction * self.STOP_FRACTION)
        self.take_profit = abs(self.position.qty), entry * (1 + direction * self.TARGET_FRACTION)
        self.vars["audit"]["entries"] += 1

    def update_position(self):
        if self.time - self.position.opened_at >= self.MAX_HOLD_MS:
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        self.log("PILOT_AUDIT " + json.dumps(self.vars.get("audit", {}), sort_keys=True))

```

## Código congelado B
```python
from strategies.FundingWfPilotBase4h import FundingWfPilotBase4h


class FundingWfPilotFiltered4h(FundingWfPilotBase4h):
    """The sole A/B change is the causal funding entry gate."""
    FUNDING_FILTER = True

```

Revisión previa a toda ejecución: se corrigió el sizing aproximado del helper para incluir ambas comisiones en el presupuesto; no se habían ejecutado ni visto resultados del piloto.
