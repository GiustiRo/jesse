# K1001 — Fuentes implementadas de escenarios cuota1%

Fecha: 2026-10-21. Implementación autorizada por root después de revisión del protocolo y anexo. Sólo tres fuentes nuevas mediante MCP. No drafts, jobs, checks sintéticos, backtests, velas, imports de datos, instalaciones ni cambios al framework o padres. Este informe no declara PASS técnico o rentabilidad.

## Contrato y justificación

Se aplica K1001_QUOTA_SCENARIOS_PROTOCOL_20261021.md y su SOURCES, incluida la aclaración final: el medidor de ocupación permanece HOLD. No se capturó previous_setup ni se recomputó suplemento; no hay override de before. El before y su máquina originales son heredados.

La única sustitución de selección es _prepare_entry con las guardas/memo del padre: LONG_ONLY permite sólo legacy_long; SHORT_BOOK permite legacy_short y luego el supplement_event original, con fallback si el primer plan no es viable. La historia inválida retorna antes de leer un evento antiguo. Se reutiliza legacy_plan con .5*max(wallet,0) y .5*available_margin, leverage y fee reales. El helper fija presupuesto1% de la cuenta total10000 y reserva la mitad del margen; no se transfiere cuota ni se inicializa una cuenta5000. No sumar las dos trayectorias.

Se heredan submit, cancelación/rearmado TTL, entradas, indicadores, stops/targets/trailing y reloj de gestión. No se exige replicar192trades porque cambian la selección y cuota; se exige paridad de reglas excepto esas dos sustituciones.

El observador común llama super._observe una vez y devuelve su valor intacto. Open registra0; pre sólo marca cuando T>opened_at; salida real se registra antes del super.on_close y posible FINAL. Open y salida al mismoT son fases separadas. Empates conservan primera fase/fecha por comparaciones estrictas. Se usa self.price de cierreM1 del pre, nunca high/low ni precios tras salir. No logs M1: configuración, planes reales, una traza agregada al cierre y estadísticas finales.

Ledger por origen y cohortes UTC de apertura/cierre, con netos de closed_trade.pnl. Es atribución de fills de cada escenario, no retornos mensuales MTM por cohorte. Un error de traza queda visible y trace_missing; no repara precios o altera órdenes.

## Readbacks completos

```json
[
  {
    "name": "BtcResearchR16K1001QuotaBase1m",
    "status": "success",
    "identical": true,
    "sha256": "5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884"
  },
  {
    "name": "BtcResearchR16K1001LongOnly1m",
    "status": "success",
    "identical": true,
    "sha256": "703a63b968d532e57527fd485c83493685ed77c39a486c9dff97674f6e6a3289"
  },
  {
    "name": "BtcResearchR16K1001ShortBook1m",
    "status": "success",
    "identical": true,
    "sha256": "23b553cd55a0a8dd7e965ea3f27b74da3bdcae603196bdedad4a57660b8f4d86"
  },
  {
    "name": "BtcResearchR16LegacyBase1m",
    "status": "success",
    "identical": true,
    "sha256": "56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542"
  },
  {
    "name": "BtcResearchR16LegacyK1001m",
    "status": "success",
    "identical": true,
    "sha256": "bf88cb663d8561e107446bfce32024ed87531d096362671f7aafce72a09f25ad"
  },
  {
    "name": "BtcResearchR11Base1m",
    "status": "success",
    "identical": true,
    "sha256": "be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87"
  }
]
```

## Autoauditoría y corrección previa a checks

La versión inicial de base tenía SHA256 `463867e1bfca62c30ac7745abf65cb944f10e037f6b432aba6a2d03adbde5634`. Contaba fills propios sólo después de crear una traza válida. Se corrigió contabilidad diagnóstica: una identidad de fill nueva incrementa fills, año de apertura y secuencia ANTES de validar éxito de trace; last_fill_identity evita duplicados. Si la traza falla, no desaparece la ejecución. No se añadió on_open ni una llamada al padre. Root y revisor independiente detectaron la misma debilidad al leer la primera versión; se les informó la corrección.

Un intento de orquestación JavaScript para esa edición devolvió SyntaxError antes de ejecutar herramientas por usar comillas triples de Python en JavaScript. No creó job ni modificó fuente. El siguiente intento aplicó la edición por write_strategy y readback confirmó igualdad. No hubo errores de MCP ni de motor.

Las fuentes finales están abajo. La inicial se conserva al final para trazabilidad; no usarla en futuros drafts.

## Fuente final: BtcResearchR16K1001QuotaBase1m

SHA256: `5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884`.

```python
import math
from datetime import datetime, timezone

from strategies.BtcResearchR16LegacyK1001m import BtcResearchR16LegacyK1001m
from strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_short, legacy_plan
from strategies.BtcResearchR10Base4h import BAR

# The account still starts at10000. Both halves are fixed allocations of its
# current wallet/free margin, not a second account or a redistribution rule.
QUOTA = .5


def quota_counts():
    return dict(fills=0, closes=0, net=0.0, trace_completed=0, trace_missing=0)


def quota_year(timestamp):
    return str(datetime.fromtimestamp(timestamp / 1000, timezone.utc).year)


class BtcResearchR16K1001QuotaBase1m(BtcResearchR16LegacyK1001m):
    """Original K1001 groups with1% total-account risk; observational trace only.

    before, supplement latch, indicators, order lifetime and management remain
    inherited. Only the permitted group and the .5/.5 sizing arguments change.
    Observed R uses open0, later closed M1 marks and the actual exit fill; it is
    neither intraminute MFE/MAE nor a counterfactual path after the real exit.
    """
    GROUP = "abstract"

    def _quota_state(self):
        state = self.vars.get("k1001_quota")
        if state is None:
            assert self.GROUP in ("LONG_ONLY", "SHORT_BOOK")
            state = dict(active=None, trade_sequence=0, last_fill_identity=None, errors={},
                         sources={name: quota_counts() for name in
                                  ("LONG_RUNNER", "CORE_SHORT", "SUPPLEMENT")},
                         open_years={}, close_years={})
            self.vars["k1001_quota"] = state
            self._log("K1001_QUOTA_CONFIG", dict(
                group=self.GROUP, mode=self.MODE, account_start=10000,
                capital_fraction=QUOTA, margin_fraction=QUOTA,
                target_risk_total=.01, aggregate_limit=.06, leverage=3,
                reserve=.001, lot=.001, redistribution=False,
                price_trace="open0_pre_strictly_after_open_exit_fill"))
        return state

    def _quota_error(self, reason):
        state = self._quota_state()
        count = state["errors"].get(reason, 0) + 1
        state["errors"][reason] = count
        # Record the first example; counters expose repeated failures without
        # producing one error line per M1 callback.
        if count == 1:
            self._log("K1001_QUOTA_TRACE_ERROR", dict(
                reason=reason, time=int(self.time), group=self.GROUP))

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
        # Use only the event generated by inherited before. In particular, no
        # second supplement evaluation or previous_setup write is permitted.
        if self.GROUP == "LONG_ONLY":
            candidates = (legacy_long(rows),)
        else:
            assert self.GROUP == "SHORT_BOOK"
            candidates = (legacy_short(rows), self.vars.get("supplement_event"))
        capital = max(0.0, float(self.balance))
        margin = float(self.available_margin)
        for candidate in candidates:
            if candidate is None:
                continue
            # Keep the frozen .02 helper: .02*.5 ==.01 of this account's wallet.
            # Its .90 buffer on half free margin leaves the other half unused.
            plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,
                               float(self.leverage), float(self.fee_rate))
            if plan is not None:
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
                return plan["direction"]
        return 0

    @staticmethod
    def _quota_identity(plan):
        return (plan["origin"], int(plan["signal_at"]), int(plan["filled_at"]),
                float(plan["actual_entry"]), float(plan["qty"]),
                float(plan["distance"]), int(plan["direction"]))

    def _quota_start_trace(self):
        state = self._quota_state()
        plan = self.vars.get("position_plan")
        if plan is None:
            self._quota_error("open_without_position_plan")
            return
        identity = self._quota_identity(plan)
        if state["last_fill_identity"] == identity:
            return  # Same open hook, not a second executed fill.
        state["last_fill_identity"] = identity
        state["trade_sequence"] += 1
        state["sources"][plan["origin"]]["fills"] += 1
        year = quota_year(identity[2])
        rows = state["open_years"].setdefault(year, {})
        rows.setdefault(plan["origin"], quota_counts())["fills"] += 1
        # Execution counts are independent of whether its observational trace
        # can be completed. A trace failure must not erase a real native fill.
        active = state["active"]
        if active is not None:
            active["broken"] = True
            self._quota_error("overlapping_trace_identity")
            return
        entry, distance = identity[3], identity[5]
        if not (math.isfinite(entry) and entry > 0
                and math.isfinite(distance) and distance > 0):
            self._quota_error("invalid_open_price_or_distance")
            return
        opened = identity[2]
        state["active"] = dict(
            identity=identity, trace_id=state["trade_sequence"],
            origin=plan["origin"], signal_at=int(plan["signal_at"]),
            opened_at=opened, entry=entry, qty=float(plan["qty"]),
            distance=distance, direction=int(plan["direction"]),
            min_r=0.0, max_r=0.0, min_at=opened, max_at=opened,
            min_stage="open", max_stage="open", first_at=opened,
            last_at=opened, last_stage="open", last_pre_at=None,
            marks=1, m1_marks=0, broken=False)

    def _quota_mark(self, trace, price, timestamp, stage):
        if stage == "pre":
            if timestamp <= trace["opened_at"]:
                return False  # A close at the fill timestamp is not post-fill.
            previous = trace["last_pre_at"]
            if previous is not None and timestamp <= previous:
                if timestamp < previous:
                    trace["broken"] = True
                    self._quota_error("backward_pre_timestamp")
                return False
        if not math.isfinite(price) or price <= 0:
            trace["broken"] = True
            self._quota_error("nonfinite_or_nonpositive_mark")
            return False
        if timestamp < trace["last_at"]:
            trace["broken"] = True
            self._quota_error("backward_mark_timestamp")
            return False
        value = trace["direction"]*(price-trace["entry"])/trace["distance"]
        if not math.isfinite(value):
            trace["broken"] = True
            self._quota_error("nonfinite_price_r")
            return False
        # Strict changes retain the first phase/time on ties. Open and exit
        # remain distinct even when a real trade has zero holding time.
        if value < trace["min_r"]:
            trace.update(min_r=value, min_at=timestamp, min_stage=stage)
        if value > trace["max_r"]:
            trace.update(max_r=value, max_at=timestamp, max_stage=stage)
        trace.update(last_at=timestamp, last_stage=stage, marks=trace["marks"]+1)
        if stage == "pre":
            trace["last_pre_at"] = timestamp
            trace["m1_marks"] += 1
        return True

    def _observe(self, stage):
        value = super()._observe(stage)
        # Never call the parent observer twice or alter its returned equity.
        state = self._quota_state()
        if stage == "open":
            self._quota_start_trace()
        elif stage == "pre" and self.is_open:
            trace = state["active"]
            plan = self.vars.get("position_plan")
            if trace is None or plan is None:
                self._quota_error("pre_without_trace_or_plan")
            elif trace["identity"] != self._quota_identity(plan):
                trace["broken"] = True
                self._quota_error("pre_identity_mismatch")
            else:
                # self.price here is the same already-closed M1 close supplied
                # to R11's pre observer. Do not use high/low or later prices.
                self._quota_mark(trace, float(self.price), int(self.time), "pre")
        return value

    def on_close_position(self, order, closed_trade):
        # Complete our observer before R16 clears its plan and R11 can emit FINAL.
        state = self._quota_state()
        plan = self.vars["position_plan"]
        origin = plan["origin"]
        trace = state["active"]
        complete = False
        if trace is not None and trace["identity"] == self._quota_identity(plan):
            marked = self._quota_mark(
                trace, float(closed_trade.exit_price),
                int(closed_trade.closed_at), "exit")
            complete = marked and not trace["broken"]
        else:
            self._quota_error("close_identity_missing_or_mismatch")
        net = float(closed_trade.pnl)
        opened_year = quota_year(int(plan["filled_at"]))
        closed_year = quota_year(int(closed_trade.closed_at))
        open_rows = state["open_years"].setdefault(opened_year, {})
        close_rows = state["close_years"].setdefault(closed_year, {})
        # All three ledgers refer to executed trades, never signal cohorts.
        for row in (state["sources"][origin],
                    open_rows.setdefault(origin, quota_counts()),
                    close_rows.setdefault(origin, dict(
                        closes=0, net=0.0, trace_completed=0, trace_missing=0))):
            row["closes"] += 1
            row["net"] += net
            row["trace_completed" if complete else "trace_missing"] += 1
        payload = dict(
            group=self.GROUP, origin=origin, trade_id=str(closed_trade.id),
            signal_at=int(plan["signal_at"]), opened_at=int(plan["filled_at"]),
            closed_at=int(closed_trade.closed_at), entry=float(plan["actual_entry"]),
            exit=float(closed_trade.exit_price), qty=float(plan["qty"]),
            distance=float(plan["distance"]), net=net, trace_complete=complete,
            exit_order_id=str(order.id), exit_order_type=order.type,
            exit_submitted_via=order.submitted_via)
        if trace is not None and trace["identity"] == self._quota_identity(plan):
            payload.update({key: trace[key] for key in (
                "trace_id", "min_r", "max_r", "min_at", "max_at", "min_stage",
                "max_stage", "first_at", "last_at", "last_stage", "marks", "m1_marks")})
        self._log("K1001_QUOTA_PRICE_TRACE", payload)
        state["active"] = None
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        state = self._quota_state()
        self._log("K1001_QUOTA_STATS", dict(
            stage=stage, group=self.GROUP, sources=state["sources"],
            open_years=state["open_years"], close_years=state["close_years"],
            trace_errors=state["errors"],
            open_trace=state["active"] is not None))
```

## Fuente final: BtcResearchR16K1001LongOnly1m

SHA256: `703a63b968d532e57527fd485c83493685ed77c39a486c9dff97674f6e6a3289`.

```python
from strategies.BtcResearchR16K1001QuotaBase1m import BtcResearchR16K1001QuotaBase1m


class BtcResearchR16K1001LongOnly1m(BtcResearchR16K1001QuotaBase1m):
    GROUP = "LONG_ONLY"
```

## Fuente final: BtcResearchR16K1001ShortBook1m

SHA256: `23b553cd55a0a8dd7e965ea3f27b74da3bdcae603196bdedad4a57660b8f4d86`.

```python
from strategies.BtcResearchR16K1001QuotaBase1m import BtcResearchR16K1001QuotaBase1m


class BtcResearchR16K1001ShortBook1m(BtcResearchR16K1001QuotaBase1m):
    GROUP = "SHORT_BOOK"
```

## Base inicial supersedida, sólo archivo histórico

```python
import math
from datetime import datetime, timezone

from strategies.BtcResearchR16LegacyK1001m import BtcResearchR16LegacyK1001m
from strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_short, legacy_plan
from strategies.BtcResearchR10Base4h import BAR

# The account still starts at10000. Both halves are fixed allocations of its
# current wallet/free margin, not a second account or a redistribution rule.
QUOTA = .5


def quota_counts():
    return dict(fills=0, closes=0, net=0.0, trace_completed=0, trace_missing=0)


def quota_year(timestamp):
    return str(datetime.fromtimestamp(timestamp / 1000, timezone.utc).year)


class BtcResearchR16K1001QuotaBase1m(BtcResearchR16LegacyK1001m):
    """Original K1001 groups with1% total-account risk; observational trace only.

    before, supplement latch, indicators, order lifetime and management remain
    inherited. Only the permitted group and the .5/.5 sizing arguments change.
    Observed R uses open0, later closed M1 marks and the actual exit fill; it is
    neither intraminute MFE/MAE nor a counterfactual path after the real exit.
    """
    GROUP = "abstract"

    def _quota_state(self):
        state = self.vars.get("k1001_quota")
        if state is None:
            assert self.GROUP in ("LONG_ONLY", "SHORT_BOOK")
            state = dict(active=None, trade_sequence=0, errors={},
                         sources={name: quota_counts() for name in
                                  ("LONG_RUNNER", "CORE_SHORT", "SUPPLEMENT")},
                         open_years={}, close_years={})
            self.vars["k1001_quota"] = state
            self._log("K1001_QUOTA_CONFIG", dict(
                group=self.GROUP, mode=self.MODE, account_start=10000,
                capital_fraction=QUOTA, margin_fraction=QUOTA,
                target_risk_total=.01, aggregate_limit=.06, leverage=3,
                reserve=.001, lot=.001, redistribution=False,
                price_trace="open0_pre_strictly_after_open_exit_fill"))
        return state

    def _quota_error(self, reason):
        state = self._quota_state()
        count = state["errors"].get(reason, 0) + 1
        state["errors"][reason] = count
        # Record the first example; counters expose repeated failures without
        # producing one error line per M1 callback.
        if count == 1:
            self._log("K1001_QUOTA_TRACE_ERROR", dict(
                reason=reason, time=int(self.time), group=self.GROUP))

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
        # Use only the event generated by inherited before. In particular, no
        # second supplement evaluation or previous_setup write is permitted.
        if self.GROUP == "LONG_ONLY":
            candidates = (legacy_long(rows),)
        else:
            assert self.GROUP == "SHORT_BOOK"
            candidates = (legacy_short(rows), self.vars.get("supplement_event"))
        capital = max(0.0, float(self.balance))
        margin = float(self.available_margin)
        for candidate in candidates:
            if candidate is None:
                continue
            # Keep the frozen .02 helper: .02*.5 ==.01 of this account's wallet.
            # Its .90 buffer on half free margin leaves the other half unused.
            plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,
                               float(self.leverage), float(self.fee_rate))
            if plan is not None:
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
                return plan["direction"]
        return 0

    @staticmethod
    def _quota_identity(plan):
        return (plan["origin"], int(plan["signal_at"]), int(plan["filled_at"]),
                float(plan["actual_entry"]), float(plan["qty"]),
                float(plan["distance"]), int(plan["direction"]))

    def _quota_start_trace(self):
        state = self._quota_state()
        plan = self.vars.get("position_plan")
        if plan is None:
            self._quota_error("open_without_position_plan")
            return
        identity = self._quota_identity(plan)
        active = state["active"]
        if active is not None:
            if active["identity"] == identity:
                return  # Same open hook, not a second fill.
            active["broken"] = True
            self._quota_error("overlapping_trace_identity")
            return
        entry, distance = identity[3], identity[5]
        if not (math.isfinite(entry) and entry > 0
                and math.isfinite(distance) and distance > 0):
            self._quota_error("invalid_open_price_or_distance")
            return
        state["trade_sequence"] += 1
        opened = identity[2]
        state["active"] = dict(
            identity=identity, trace_id=state["trade_sequence"],
            origin=plan["origin"], signal_at=int(plan["signal_at"]),
            opened_at=opened, entry=entry, qty=float(plan["qty"]),
            distance=distance, direction=int(plan["direction"]),
            min_r=0.0, max_r=0.0, min_at=opened, max_at=opened,
            min_stage="open", max_stage="open", first_at=opened,
            last_at=opened, last_stage="open", last_pre_at=None,
            marks=1, m1_marks=0, broken=False)
        state["sources"][plan["origin"]]["fills"] += 1
        year = quota_year(opened)
        rows = state["open_years"].setdefault(year, {})
        rows.setdefault(plan["origin"], quota_counts())["fills"] += 1

    def _quota_mark(self, trace, price, timestamp, stage):
        if stage == "pre":
            if timestamp <= trace["opened_at"]:
                return False  # A close at the fill timestamp is not post-fill.
            previous = trace["last_pre_at"]
            if previous is not None and timestamp <= previous:
                if timestamp < previous:
                    trace["broken"] = True
                    self._quota_error("backward_pre_timestamp")
                return False
        if not math.isfinite(price) or price <= 0:
            trace["broken"] = True
            self._quota_error("nonfinite_or_nonpositive_mark")
            return False
        if timestamp < trace["last_at"]:
            trace["broken"] = True
            self._quota_error("backward_mark_timestamp")
            return False
        value = trace["direction"]*(price-trace["entry"])/trace["distance"]
        if not math.isfinite(value):
            trace["broken"] = True
            self._quota_error("nonfinite_price_r")
            return False
        # Strict changes retain the first phase/time on ties. Open and exit
        # remain distinct even when a real trade has zero holding time.
        if value < trace["min_r"]:
            trace.update(min_r=value, min_at=timestamp, min_stage=stage)
        if value > trace["max_r"]:
            trace.update(max_r=value, max_at=timestamp, max_stage=stage)
        trace.update(last_at=timestamp, last_stage=stage, marks=trace["marks"]+1)
        if stage == "pre":
            trace["last_pre_at"] = timestamp
            trace["m1_marks"] += 1
        return True

    def _observe(self, stage):
        value = super()._observe(stage)
        # Never call the parent observer twice or alter its returned equity.
        state = self._quota_state()
        if stage == "open":
            self._quota_start_trace()
        elif stage == "pre" and self.is_open:
            trace = state["active"]
            plan = self.vars.get("position_plan")
            if trace is None or plan is None:
                self._quota_error("pre_without_trace_or_plan")
            elif trace["identity"] != self._quota_identity(plan):
                trace["broken"] = True
                self._quota_error("pre_identity_mismatch")
            else:
                # self.price here is the same already-closed M1 close supplied
                # to R11's pre observer. Do not use high/low or later prices.
                self._quota_mark(trace, float(self.price), int(self.time), "pre")
        return value

    def on_close_position(self, order, closed_trade):
        # Complete our observer before R16 clears its plan and R11 can emit FINAL.
        state = self._quota_state()
        plan = self.vars["position_plan"]
        origin = plan["origin"]
        trace = state["active"]
        complete = False
        if trace is not None and trace["identity"] == self._quota_identity(plan):
            marked = self._quota_mark(
                trace, float(closed_trade.exit_price),
                int(closed_trade.closed_at), "exit")
            complete = marked and not trace["broken"]
        else:
            self._quota_error("close_identity_missing_or_mismatch")
        net = float(closed_trade.pnl)
        opened_year = quota_year(int(plan["filled_at"]))
        closed_year = quota_year(int(closed_trade.closed_at))
        open_rows = state["open_years"].setdefault(opened_year, {})
        close_rows = state["close_years"].setdefault(closed_year, {})
        # All three ledgers refer to executed trades, never signal cohorts.
        for row in (state["sources"][origin],
                    open_rows.setdefault(origin, quota_counts()),
                    close_rows.setdefault(origin, dict(
                        closes=0, net=0.0, trace_completed=0, trace_missing=0))):
            row["closes"] += 1
            row["net"] += net
            row["trace_completed" if complete else "trace_missing"] += 1
        payload = dict(
            group=self.GROUP, origin=origin, trade_id=str(closed_trade.id),
            signal_at=int(plan["signal_at"]), opened_at=int(plan["filled_at"]),
            closed_at=int(closed_trade.closed_at), entry=float(plan["actual_entry"]),
            exit=float(closed_trade.exit_price), qty=float(plan["qty"]),
            distance=float(plan["distance"]), net=net, trace_complete=complete,
            exit_order_id=str(order.id), exit_order_type=order.type,
            exit_submitted_via=order.submitted_via)
        if trace is not None and trace["identity"] == self._quota_identity(plan):
            payload.update({key: trace[key] for key in (
                "trace_id", "min_r", "max_r", "min_at", "max_at", "min_stage",
                "max_stage", "first_at", "last_at", "last_stage", "marks", "m1_marks")})
        self._log("K1001_QUOTA_PRICE_TRACE", payload)
        state["active"] = None
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        state = self._quota_state()
        self._log("K1001_QUOTA_STATS", dict(
            stage=stage, group=self.GROUP, sources=state["sources"],
            open_years=state["open_years"], close_years=state["close_years"],
            trace_errors=state["errors"],
            open_trace=state["active"] is not None))
```

## Estado de validación

Fuentes y readbacks entregados a root e independiente. Los controles sintéticos de selección/cuota, fallback/memo, herencia, Rprecio fases/tiempo0/identidad/errores y FINAL están pendientes de su siguiente autorización/ejecución coordinada. No se importó framework o estrategias para probar ni se inició un análisis. Tampoco se crearon manifiestos o IDs de backtests ficticios.
