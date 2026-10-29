# K1001 LONG MARKET: fuente implementada y readback

Fecha: 2026-10-21. Estado: una fuente nueva implementada mediante MCP y pendiente de revisión, checks y eventual autorización de motor. No se ejecutaron análisis, tests, drafts ni backtests en esta tarea.

## Fuente y alcance

Nombre: BtcResearchR16K1001LongMarket1m.
Ruta MCP: strategies/BtcResearchR16K1001LongMarket1m/__init__.py.
SHA256 del contenido completo leído después de crear: f3aeb9be8082cfb7f5cbd4a310da1b741a7bec9d675e25d657131754f5e8b32b.
Creación: un intento exitoso. Readback completo exacto contra el contenido enviado, sin correcciones ni versiones supersedidas.

Documentos normativos leídos completos antes de escribir: K1001_LONG_MARKET_PROTOCOL_20261021.md, K1001_LONG_MARKET_CODES_20261021.md y K1001_LONG_MARKET_DEDUP_AND_VOI_20261021.md, bajo este mismo ancla FundingOiPilot4h/reports. La autorización posterior de root permite implementación y mantiene prohibidos jobs, drafts y economía hasta revisión.

## Decisiones y justificación

La clase hereda de LongOnly y sólo define ENTRY_POLICY, _prepare_entry y _emit. GROUP LONG_ONLY, MODE K1001, before y latch suplemento, should_long/short, go_long/short, _submit, cancelación, apertura, cierre, runner y observación Rprecio siguen heredados. No monkeypatch, fallback, cambio global o modificación de padres.

_prepare_entry copia literalmente las guardas y memo del padre cuota. Invoca legacy_long congelado completo antes de leer el nuevo precio para construir una copia local. Por ello conserva todas las restricciones originales, incluidas H<close<=H+ATR y distance<H. Sólo entry=float(self.price) y order_kind=MARKET cambian en el evento copiado; el original permanece intacto.

legacy_plan recalcula cantidad y costos de sizing al nuevo precio con QUOTA=.5 importada del padre y los mismos argumentos .5*max(0,balance), .5*available_margin, leverage y fee. No se reutiliza cantidad LIMIT. Plan, signal_at, expiry, direction y signals mantienen la secuencia original. K1001_QUOTA_PLAN conserva el esquema anterior; K1001_MARKET_PLAN registra una vez por admisión la política, H original, precio de decisión, distancia original, precio solicitado, qty y risk_budget. Los retornos memo no generan más registros.

_emit llama super exactamente una vez y sólo lee el estado quota ya actualizado. Añade SUMMARY, una SOURCE por origen y una COHORT por año/origen/eje. No cambia contadores, no recalcula trades y no agrega logs M1. Dividir los esquemas fijos en filas pequeñas evita empaquetar cohortes en una línea y permite verificar en los checks pendientes el límite prefijado menor de1900 caracteres. PRETERMINAL y FINAL siguen siendo snapshots separados, no sumandos.

## Precisión de ejecución recibida de root

La etiqueta order_kind del plan no acredita el tipo nativo. Root identificó el umbral heredado is_price_near .00015 antes de clasificar LIMIT/STOP: el control long tiene27 órdenes LIMIT y4 MARKET nativas, aunque su etiqueta de plan sea LIMIT. No se toca esa semántica histórica ni se fuerza LIMIT. El tratamiento solicita exactamente self.price, diferencia0, y su auditoría posterior deberá acreditar TODAS las entradas nativas MARKET en órdenes reales. Esta precisión no cambia el código aprobado ni demuestra ejecución mediante stubs. El addendum normativo queda a cargo de root/reversion.

## Padres verificados

Leídos mediante read_strategy antes de escribir y nuevamente tras la creación; contenidos idénticos, sin mutación:
- BtcResearchR16K1001LongOnly1m: 703a63b968d532e57527fd485c83493685ed77c39a486c9dff97674f6e6a3289
- BtcResearchR16K1001QuotaBase1m: 5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884
- BtcResearchR16LegacyBase1m: 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542

Resto de dependencias congeladas y fuentes completas: anexo CODES normativo existente; este reporte no atribuye un nuevo readback a dependencias que no volvió a consultar.

## Pendientes y límites

Root e independiente deben revisar esta fuente y su readback. No se ejecutaron sintéticos ni se certifica aquí compilación/import o comportamiento del broker. Los checks posteriores supplied-source deben verificar predicados originales, bordes, inmutabilidad, guards/memo, .5/.5, cantidad a nuevo precio, herencia y filas compactas sin mutación económica. La clasificación real requiere auditoría de framework/órdenes del eventual motor, no sólo el campo de plan.

Presupuesto futuro normativo: un ID económico nuevo, control archivado reutilizado, sin reemplazo automático. Esta entrega consume cero IDs económicos y cero análisis técnicos. No datos observados, velas, importaciones, scripts, instalación, framework o configuración global.

## Fuente completa creada y leída

```python
from strategies.BtcResearchR16K1001LongOnly1m import BtcResearchR16K1001LongOnly1m
from strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_plan
from strategies.BtcResearchR16K1001QuotaBase1m import QUOTA
from strategies.BtcResearchR10Base4h import BAR


class BtcResearchR16K1001LongMarket1m(BtcResearchR16K1001LongOnly1m):
    """K long entry-policy ablation; original signal, quota and runner unchanged.

    Validate the complete frozen LIMIT recipe first. Only its requested entry
    changes to the exact decision price; native inherited submission handles
    MARKET execution. Compact terminal rows expose the existing real ledger,
    never hypothetical fills or a new economic decision.
    """
    ENTRY_POLICY = "MARKET_AT_DECISION_CLOSE"

    def _prepare_entry(self):
        now = int(self.time)
        if (now % BAR or self.vars.get("decision_at") != now
                or self.is_open or self.entry_orders
                or self.vars.get("last_exit_at") == now
                or not self.START < now < self.FINISH):
            return 0
        if self.vars.get("prepared_at") == now:
            return self.vars.get("direction", 0)
        self.vars["prepared_at"] = now
        rows = self.vars.get("legacy_rows")
        if rows is None:
            return 0
        # Includes H < close <= H+ATR and distance < H: MARKET must not relax
        # any original signal geometry, even when the new price is higher.
        original = legacy_long(rows)
        if original is None:
            return 0
        decision_price = float(self.price)
        candidate = dict(original, entry=decision_price, order_kind="MARKET")
        capital = max(0.0, float(self.balance))
        margin = float(self.available_margin)
        # Reprice sizing, fees and reserve at MARKET, with the same inactive
        # half-account allocation as LIMIT. Never recycle its quantity.
        plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            return 0
        self.vars["plan"] = dict(plan, signal_at=now, expiry=now+BAR)
        self.vars["direction"] = plan["direction"]
        self.vars["signals"] = self.vars.get("signals", 0)+1
        self._log("K1001_QUOTA_PLAN", dict(
            time=now, group=self.GROUP, origin=plan["origin"],
            qty=plan["qty"], risk_budget=plan["risk_budget"],
            capital_total=capital, capital_scaled=QUOTA*capital,
            margin_total=margin, margin_scaled=QUOTA*margin,
            planned_loss=plan["planned_loss"],
            planned_stop_fees=plan["planned_stop_fees"],
            reserve=plan["reserve"], gross_limited=plan["gross_limited"],
            margin_limited=plan["margin_limited"], expiry=now+BAR))
        # One record per admitted plan; memo calls produce no extra record.
        self._log("K1001_MARKET_PLAN", dict(
            time=now, entry_policy=self.ENTRY_POLICY, origin=plan["origin"],
            original_trigger_level=float(original["entry"]),
            decision_price=decision_price,
            original_distance=float(original["distance"]),
            requested_entry=plan["entry"], qty=plan["qty"],
            risk_budget=plan["risk_budget"], expiry=now+BAR))
        return plan["direction"]

    def _emit(self, stage):
        super()._emit(stage)
        state = self._quota_state()
        # Split the fixed schemas by origin and year so each complete record
        # stays below 1900 characters, beneath the MCP reader's 2000 cut.
        # Stages are snapshots, not additional ledger observations.
        self._log("K1001_MARKET_SUMMARY", dict(
            stage=stage, policy=self.ENTRY_POLICY,
            trace_errors=state["errors"], open_trace=state["active"] is not None))
        for origin, row in state["sources"].items():
            self._log("K1001_MARKET_SOURCE", dict(stage=stage, origin=origin, **row))
        for axis in ("open_years", "close_years"):
            for year, origins in state[axis].items():
                for origin, row in origins.items():
                    self._log("K1001_MARKET_COHORT", dict(
                        stage=stage, axis=axis, year=year, origin=origin, **row))
```
