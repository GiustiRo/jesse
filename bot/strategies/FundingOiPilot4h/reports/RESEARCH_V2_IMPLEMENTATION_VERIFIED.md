# V2 implementada y verificada técnicamente
Fecha: 2026-10-20. Estado: IMPLEMENTED_AND_TECHNICALLY_VERIFIED. Cero backtests económicos nuevos V2.

## Resultado
Core independiente ResearchV2Core4h, helper de pruebas y 16 subclases ATR (P/POI, E1–E4 train/eval) creados por MCP. No se modificó el padre V1 ni las reglas económicas congeladas. Sus 16 controles H1_P/H1_POI fueron releídos y verifican fuente, config y fechas para reutilización; las evaluaciones ya se vieron y no son datos nuevos.
ATR = media de 14 TR de 15 OHLC cerradas, 2A/4A; cantidad floor8 con presupuesto 2% incluyendo fees y notional máximo C. Sin leverage multiplicador. Entradas y hold24h conservados. Distancia ATR congelada en decisión y aplicada desde el fill real. Motivos de salida explícitos y auditoría causal persistida.

## Verificación
- Las 23 fuentes de implementación/técnicas compilaron; 55 assertions sintéticas aprobaron. Job 68fd6a0170f24105949c5e7ccd4314ca.
- Pruebas de gaps TR conocidos, aritmética exacta, 15 barras necesarias, huecos/duplicados, OHLC inválidos y cero rango, prefijos y mutación futura, H1 equivalente a V1, OI/reference/stale/zero/lag, sizing long/short con fee nominal/duplicada y cap de notional, cantidades mínimas y protección desde fill.
- Cuatro sesiones técnicas de nueve días: [2020-09-01,2020-09-10), 54 decisiones 4h cada una. Las cuatro aprobaron nuevamente los checks sintéticos y verificaron en cada barra real H1 contra V1, prefijo ATR y media TR independiente.
- Siete trades cerrados en total; 21 eventos funding; 14 órdenes ejecutadas MARKET. El smoke de estrés aplicó 10bps a seis fills, en ambos lados, con fee 0,0009 y leverage3.
- Conciliación independiente de snapshots completos: bruto−fees+ledger funding=PNL; fees de fills; saldo final; cashflows por trade; holding; configuración y effective_fast_mode=false. Error máximo 3.637979e-12 USDT, tolerancia 1e-6.
- Los cuatro logs completos concilian barras, partición exclusiva, allowed=entradas=trades y salidas. Las entradas verifican tamaño, stop/target, A congelada y timestamps OI incluyendo un cierre4h adicional. Longitud máxima registrada de línea: 1019 caracteres.
- Logs separados en AUDIT_<smoke>.json; fuentes y hashes en RESEARCH_V2_IMPLEMENTATION.md y REGISTRY_V2.json. Código de reconciliación preservado al final de este reporte.

## Sesiones técnicas
| Sesión | Duración motor s | Trades | Funding eventos | Fills con slip |
|---|---:|---:|---:|---:|
| [ResearchV2SmokeP4h](http://localhost:9200/#/backtest/d4a36a26-5ac0-4f1a-9a93-e726f294d738) | 1.48 | 3 | 9 | 0 |
| [ResearchV2SmokeOi4h](http://localhost:9200/#/backtest/0e979089-e012-4b8d-b978-f0421566a123) | 1.03 | 0 | 0 | 0 |
| [ResearchV2SmokeStress4h](http://localhost:9200/#/backtest/fd0ede47-a8cc-4aa5-9515-41c88211119e) | 1.1 | 3 | 9 | 6 |
| [ResearchV2SmokeLag4h](http://localhost:9200/#/backtest/4a87382f-5d48-487e-9cb1-46d1b812449c) | 1.22 | 1 | 3 | 0 |

El nominal POI no entró: nueve oportunidades, cuatro rechazadas por inicialización y cinco por OI no creciente. El retraso adicional habilitó una entrada en esta ventana; se verificó contra su observación original y referencia24h, sin ampliar stale. Ninguna de estas diferencias ni la rentabilidad de los smokes elige parámetros.

## Límites de cobertura
Todos los cierres ejecutados de los smokes fueron de mercado al límite24h. No hubo ejecución STOP/LIMIT, posición abierta al borde final ni liquidación invalid_after_fill; sus ramas están implementadas pero no se afirman ejercitadas aquí. La colocación geométrica protectora y los cálculos se verificaron con funciones sintéticas y procedencia real; las pruebas de integración anteriores del framework están documentadas en V1, no son nuevas pruebas de estas ramas V2.
El nominal OI no produjo una entrada habilitada; el smoke retrasado sí. No ampliar ni elegir otra ventana para forzar un resultado favorable o gastar más de los cuatro smokes prerregistrados.
No se corrió pytest de framework: no se modificó el framework. Runtime de Jesse ya existente; sin instalar ni crear entornos.
OI continúa retrospectivo sin certificación PIT y funding con proxy. Slippage real está probado técnicamente, pero no hay conclusión de viabilidad económica.

## Freeze de código
Core probado por los cuatro smokes: 3bb9b1c4f9667fb2d6098a409d360d720fc154b6b570096b1b8b2e2a5322e6c5.
Core final: 577b84ebd15f27f5f598af5a4d1a3d3ed98313797656206c7691d29ad877564b.
Después de los smokes se añadieron sólo tres comentarios de racional: riesgo2% con fees, política de disponibilidad/stale OI y longitud del buffer24h. AST completo idéntico, excluidas posiciones de fuente, y compilación final exitosa en job 3f5a02aa9c92481497f4143fc40653a9. No cambio ejecutable ni rerun necesario. La fuente probada permanece en el snapshot inicial y technical_core_source del registry; la final se conserva abajo y en registry.sources.
V1 conserva 4512d21d8bab7bd33389db6e32315cf4ffaf50955cfa6e03f48d25082c1c2546.
Snapshots del framework y runtime heredados del freeze V1 identificados en registry; no afirmar un rebuild o reinicio nuevo.

## Estado operativo y próximo lote
No hay backtests activos. No se iniciaron sesiones económicas V2, no se abrió 2024–2025 ni 2026. Sin ML, RST, cuentas, Pi, live/paper, reinicio, instalaciones, commit o push. Cambios preexistentes preservados.
La implementación queda lista para train E1 de H1_ATR_P y H1_ATR_POI, con controles fijos reutilizados. Guardar selección E1 antes de consultar/ejecutar nuevas evaluaciones ATR. Continuar las reglas de RESEARCH_PROTOCOL_V2_20261020.md; no abrir confirmación con shortlist vacía.
Presupuesto económico intacto: 32 slots exploración, 8 confirmación, 24 robustez, máximo64 contando reutilizaciones; cuatro smokes técnicos consumidos.
Este cierre completa implementación/verificación; no presenta resultados económicos V2 ni una candidata.

## Incidentes de orquestación
Dos errores locales de JavaScript (copia structuredClone no disponible y parser inicial de logs sin coincidencias) se corrigieron antes de la operación dependiente; no hubo errores MCP ni backtests duplicados. No se cambió la estrategia por resultados de PnL.
Jobs de reconciliación: f44e3aa5d28149b4b9479f0cf175750a, 94068a476e6e44b482f3bda78ca31243, 41d0c0e9e7d24e4fb097e53432ba7030.

## Core final
```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000
ATR_PERIOD = 14
QTY_SCALE = 100000000
ACCOUNTING_TOLERANCE = 1e-6


def atr_window(candles, now):
    """Fourteen arithmetic TRs require fifteen complete, consecutive OHLC bars."""
    rows = candles[candles[:, 0] + BAR <= now][-15:]
    if len(rows) != 15 or rows[-1, 0] != now - BAR:
        return None
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    o, c, h, low = (rows[:, i] for i in (1, 2, 3, 4))
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(h < np.maximum(o, c)) or np.any(low > np.minimum(o, c)) or np.any(h < low):
        return None
    tr = np.maximum(h[1:] - low[1:], np.maximum(abs(h[1:] - c[:-1]), abs(low[1:] - c[:-1])))
    value = float(np.mean(tr))
    if not math.isfinite(value) or value <= 0:
        return None
    return dict(value=value, first=int(rows[0, 0]), last=int(rows[-1, 0]),
                bars=rows[:, :5].tolist())


def h1_direction(candles, now):
    rows = candles[candles[:, 0] + BAR <= now]
    if len(rows) < 2 or rows[-1, 0] != now - BAR or rows[-2, 0] != now - 2 * BAR:
        return 0
    day = now // DAY * DAY
    previous = rows[(rows[:, 0] >= day - DAY) & (rows[:, 0] < day)]
    if len(previous) != 6 or len(set(previous[:, 0])) != 6:
        return 0
    high, low = float(np.max(previous[:, 3])), float(np.min(previous[:, 4]))
    close = float(rows[-1, 2])
    return 1 if close > high else -1 if close < low else 0


def oi_context(history, now, lag_bars=0):
    # Freshness belongs to the original observation, including the lagged scenario.
    target = now - lag_bars * BAR
    current = next((r for r in reversed(history) if r["time"] == target), None)
    reference = next((r for r in reversed(history) if r["time"] == target - DAY), None)
    result = dict(quality="initialization", passed=False, current=current, reference=reference)
    if current is None:
        return result
    if current["status"] != "valid":
        result["quality"] = current["status"]
    elif reference is None:
        result["quality"] = "initialization"
    elif reference["status"] != "valid":
        result["quality"] = "reference_invalid"
    else:
        result["quality"] = "valid"
        result["passed"] = current["value"] > reference["value"]
    return result


def protective_prices(entry, direction, distance):
    """The distance is frozen at decision for ATR, and based on fill for FIXED."""
    stop, target = entry - direction * distance, entry + direction * 2 * distance
    if direction not in (-1, 1) or not all(math.isfinite(x) and x > 0 for x in (entry, distance, stop, target)):
        return None
    return stop, target


def entry_plan(price, capital, fee, direction, distance):
    if not all(math.isfinite(x) and x > 0 for x in (price, capital)):
        return dict(reason="distance_invalid")
    prices = protective_prices(price, direction, distance)
    if prices is None or not math.isfinite(fee) or fee < 0:
        return dict(reason="distance_invalid")
    stop, target = prices
    # Protocol budgets 2% for stop plus round-trip fees; leverage never scales quantity.
    unit = distance + fee * (price + stop)
    raw = min(capital / price, .02 * capital / unit)
    qty = math.floor(raw * QTY_SCALE) / QTY_SCALE
    if qty <= 0:
        return dict(reason="qty_invalid")
    assert qty * unit <= .02 * capital + ACCOUNTING_TOLERANCE
    assert qty * price <= capital + ACCOUNTING_TOLERANCE
    return dict(reason="allowed", price=price, capital=capital, fee=fee, qty=qty,
                distance=distance, stop=stop, target=target, unit_loss=unit,
                risk_budget=.02 * capital, planned_stop_loss=qty * unit)


class ResearchV2Core4h(Strategy):
    """Independent V2 implementation; V1 source is never modified or inherited."""
    USE_ATR = True
    USE_OI = False
    ATR_MULTIPLIER = 2.
    FIXED_STOP = .02
    OI_LAG_BARS = 0
    START = 1598918400000
    FINISH = 1640995200000

    def _bucket(self, month, direction):
        return self.vars.setdefault("audit", {}).setdefault(month + ":" + direction, dict(
            bars=0, opportunities=0, entries=0, exits=0, primary={}, flags={}))

    def _log_json(self, label, payload):
        line = label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False)
        # Framework truncates long log lines; fail instead of silently losing provenance.
        assert len(line) <= 1900
        self.log(line)

    def before(self):
        now = int(self.time)
        direction = h1_direction(self.candles, now)
        atr = atr_window(self.candles, now)
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            # Frozen archive policy: label +6m availability, then at most 10m of freshness.
            assert value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
                            available_at=label + 360000 if label is not None else None, status=status))
        # Six 4h steps form 24h; keep current, lag and one spare without backfilling.
        history[:] = history[-(8 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.START < now < self.FINISH)
        flags = []
        current, reference = oi["current"], oi["reference"]
        if current is None:
            flags.append("oi_initialization")
        elif current["status"] != "valid":
            flags.append("oi_" + current["status"])
        if reference is None:
            if "oi_initialization" not in flags:
                flags.append("oi_initialization")
        elif reference["status"] != "valid":
            flags.append("oi_reference_invalid")
        if oi["quality"] == "valid" and not oi["passed"]:
            flags.append("oi_nonrising")
        if atr is None:
            flags.append("atr_invalid")
        plan = None
        reason = "allowed"
        # Preserve V1 gate precedence; the new distance checks follow the OI gates.
        if not self.START < now < self.FINISH:
            reason = "boundary"
        elif direction == 0:
            reason = "no_price"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif self.USE_OI and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising"
        elif self.USE_ATR and atr is None:
            reason = "atr_invalid"
        else:
            distance = self.ATR_MULTIPLIER * atr["value"] if self.USE_ATR else self.FIXED_STOP * self.price
            plan = entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
            reason = plan["reason"]
        if reason in ("distance_invalid", "qty_invalid"):
            flags.append(reason)
        month = datetime.fromtimestamp((now - 1) / 1000, timezone.utc).strftime("%Y-%m")
        key = "long" if direction == 1 else "short" if direction == -1 else "none"
        for bucket_direction in ("all", key):
            bucket = self._bucket(month, bucket_direction)
            bucket["bars"] += 1
            bucket["opportunities"] += int(opportunity)
            bucket["primary"][reason] = bucket["primary"].get(reason, 0) + 1
            if opportunity:
                for flag in flags:
                    bucket["flags"][flag] = bucket["flags"].get(flag, 0) + 1
        self.vars["context"] = dict(time=now, day=day, month=month, direction=direction,
                                   allowed=reason == "allowed", oi=oi, atr=atr, plan=plan, funding=funding)

    def should_long(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == 1

    def should_short(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == -1

    def _enter(self, direction):
        context = self.vars["context"]
        plan = context["plan"]
        assert plan and plan["reason"] == "allowed" and context["direction"] == direction
        self.vars.pop("exit_reason", None)
        self.vars["intent"] = dict(plan=plan, context=context)
        if direction == 1:
            self.buy = plan["qty"], plan["price"]
        else:
            self.sell = plan["qty"], plan["price"]

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"] if self.USE_ATR else self.FIXED_STOP * entry
        prices = protective_prices(entry, direction, distance)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        provenance = None
        if atr is not None:
            # Hash canonical UTF-8 OHLC payload, not a platform-dependent ndarray buffer.
            digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
            provenance = dict(value=atr["value"], first=atr["first"], last=atr["last"], bars=15, sha256=digest)
        self._log_json("V2_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=plan["distance"], distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=prices[0] if prices else None, target=prices[1] if prices else None,
            atr=provenance, oi=context["oi"], funding=context["funding"]))
        if prices is None:
            # No invalid protective order is submitted. Entry remains in the audit and PnL.
            self.vars["exit_reason"] = "invalid_after_fill"
            for side in ("all", "long" if direction == 1 else "short"):
                bucket = self._bucket(context["month"], side)
                bucket["flags"]["invalid_after_fill"] = bucket["flags"].get("invalid_after_fill", 0) + 1
            self._log_json("V2_EXIT_REQUEST", dict(time=int(self.time), reason="invalid_after_fill"))
            self.liquidate()
            return
        self.stop_loss = qty, prices[0]
        self.take_profit = qty, prices[1]

    def update_position(self):
        if self.time - self.position.opened_at >= DAY:
            self.vars["exit_reason"] = "holding_24h"
            self._log_json("V2_EXIT_REQUEST", dict(time=int(self.time), reason="holding_24h"))
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        intent = self.vars["intent"]
        assert abs(self.balance - intent["plan"]["capital"] - closed_trade.pnl) < ACCOUNTING_TOLERANCE
        direction = 1 if closed_trade.type == "long" else -1
        gross = direction * (closed_trade.exit_price - closed_trade.entry_price) * closed_trade.qty
        reason = self.vars.get("exit_reason") or order.submitted_via or "unclassified"
        assert reason != "unclassified"
        month = datetime.fromtimestamp((int(self.time) - 1) / 1000, timezone.utc).strftime("%Y-%m")
        for side in ("all", closed_trade.type):
            self._bucket(month, side)["exits"] += 1
        self._log_json("V2_CLOSE", dict(time=int(self.time), trade_id=str(closed_trade.id),
            reason=reason, pnl=closed_trade.pnl, balance=self.balance, gross=gross,
            risk_budget=intent["plan"]["risk_budget"],
            realized_loss=max(0., -closed_trade.pnl),
            loss_over_budget=max(0., -closed_trade.pnl - intent["plan"]["risk_budget"])))

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        # Framework closes positions after this hook; preserve the explicit border motive.
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V2_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            self._log_json("V2_AUDIT", dict(key=key, **value))
        self._log_json("V2_PROVENANCE", dict(atr=self.USE_ATR, period=ATR_PERIOD,
            multiplier=self.ATR_MULTIPLIER, fixed_stop=self.FIXED_STOP, oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, hold_ms=DAY, start=self.START, finish=self.FINISH,
            final_exit_may_follow=True, self_checks=self.vars.get("self_checks")))

```

## Análisis de conciliación reproducible
Lectura sólo de inputs/; escritura sólo output/. Sin acceso a archivos del proyecto, red ni backtests.
```python
import json, math
from pathlib import Path
rows=[]
for p in Path("inputs").glob("s*.json"):
 d=json.load(open(p)); s=d["summary"]; m=d["metrics"]; ts=d["trades"]
 ledger=m.get("funding",{}).get("ledger",[]); errors=[]; adjusted=[]; kinds={}; sides=set()
 config=s["form"]["config"]; fee=config["exchange"]["fee"]; bps=config["exchange"]["slippage_bps"]
 for t in ts:
  sign=1 if t["type"]=="long" else -1
  gross=sign*(t["exit_price"]-t["entry_price"])*t["qty"]
  fund=math.fsum(x["cashflow"] for x in ledger if x["trade_id"]==t["id"])
  errors.extend([abs(gross-t["fee"]+fund-t["PNL"]),abs(fund-t.get("funding",0))])
  orders=[o for o in t["orders"] if o["status"]=="EXECUTED"]
  expected_fee=math.fsum(abs(o["filled_qty"])*o["price"]*fee for o in orders)
  errors.append(abs(expected_fee-t["fee"]))
  for o in orders:
   kinds[o["type"]]=kinds.get(o["type"],0)+1
   sides.add(o["side"])
   if bps and o["type"] in ("MARKET","STOP"):
    slip=o["slippage"]; side=1 if o["side"]=="buy" else -1
    errors.append(abs(o["price"]-slip["reference_price"]*(1+side*bps/10000)))
    assert slip["bps"]==bps
    adjusted.append(o["id"])
   else:
    assert "slippage" not in o
  assert math.isclose(t["holding_period"],(t["closed_at"]-t["opened_at"])/1000,abs_tol=1e-9)
 net=math.fsum(t["PNL"] for t in ts)
 errors.append(abs(net-(m.get("net_profit") or 0)))
 if ts:errors.append(abs(10000+net-m["finishing_balance"]))
 assert max(errors,default=0)<1e-6,errors
 assert config["exchange"]["futures_leverage"]==3
 assert config["warm_up_candles"]==240
 assert m.get("funding",{}).get("effective_fast_mode") is False
 rows.append(dict(session_id=s["session_id"],trades=len(ts),funding_events=len(ledger),orders=kinds,
  sides=sorted(sides),bps=bps,fee=fee,adjusted_fills=len(adjusted),max_error=max(errors,default=0),
  complete=True))
json.dump(rows,open("output/reconciliation.json","w"),indent=2)
print(json.dumps(rows))

```
