# V6 replay — fuentes y verificación congeladas

Autor: /root/audit. Resultado **PASS técnico**, sin motores ni drafts iniciados.

Única fuente de calendario: V6_REPLAY_CALENDAR.json, SHA256 canónico 330177d3e6ae5e5adb909b9a3c256ea0881f4aa37d44ffe186aa53409cfb661f. START1704067200000; FINISH1767225600000. ACTIVE_WINDOWS conserva 2024H1 y 2024H2 separados. C3/C4 de2025 están OFF exclusivamente por elegibilidad TRAIN; no se usó su rentabilidad diagnóstica. FORCE_BOUNDARIES mantiene los cuatro finales hasta2026Jan, sin unión de intervalos. El horizonte global731días conserva capital y evita anualizar sólo el tiempo activo.

Cinco clases: nominal Efficiency P, R09/R11 stop2.25/2.75 y A09/A11 umbral.315/.385. Nominalstop2.5,umbral.35,hold60,ATRoffset0,TARGETnone,USE_OIFalse,OIlag0. No claseLag porque el slot sinOI reutiliza nominal. Sin atributos SMA/RETURN_LAG/FUNDING_COUNT deV5. S1/S2/S3 usarán configuración de sesión sobre clase nominal.

Readback exacto5/5. Job6250322c5af84459bc71dbff1a5c5c68 succeeded con **606 comprobaciones PASS**: compile/AST literal/herencia sin hooks/calls; calendario y bloqueos2025; prioridad calendar sobre holding/indicador y dedup; capital/historia preservados; hold60; salida posterior al fill; protección desde fill/distancia congelada; sizing2%stop+fees/cap1x; historiaOI actualizada aun inactiva y OIausente sin gate; cuotaUTCdiaria; binding exacto de umbrales y salida25closes independienteATR; logs<=1900 y hookfinal.

Core/helper/padre V6 actuales tienen SHA idénticos al freeze/registro. V2capturado sinmodificar. La prueba ejecuta ASTcapturado sin importar proyecto ni acceder datos/motor. No demuestra fills reales ni secuencia contable del motor: cashflow funding ocurre ANTES de decisióncalendar en borde interno según contrato contable previo. Cierre final real puede seguir a before_terminate; será auditado en ledger/logs de futuros replays. Config nominal SHA8f9e73c52ecf50f01b6f1f3efdfa98e06081151b15820d46588b5874da5f35cb.

Manifiesto V6_REPLAY_WRAPPERS.json, resultados V6_REPLAY_TEST_RESULTS.json, código V6_REPLAY_TEST_CODE.json y raws V6_REPLAY_SOURCE_VERIFICATION.json.

## strategies/ResearchV6EfficiencyPReplay4h/__init__.py

SHA256 82a4def22fffb40af0bbbf8bea24560472e5b2cbbe68c3beb4c306635f05d05f

```python
from strategies.ResearchV6EfficiencyP4h import ResearchV6EfficiencyP4h


class ResearchV6EfficiencyPReplay4h(ResearchV6EfficiencyP4h):
    # Individual TRAIN eligibility freezes 2024 semesters separately; 2025 stays inactive.
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    EFFICIENCY_THRESHOLD = 0.35
    STOP_MULTIPLIER = 2.5
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 60
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = ((1704067200000, 1719792000000), (1719792000000, 1735689600000),)
    FORCE_BOUNDARIES = (1719792000000, 1735689600000, 1751328000000, 1767225600000,)
```

## strategies/ResearchV6EfficiencyPReplayR09_4h/__init__.py

SHA256 cab512fd681daa321e742dec5537e6818e846a0cdab091aad9f85305d8ce6849

```python
from strategies.ResearchV6EfficiencyPReplay4h import ResearchV6EfficiencyPReplay4h


class ResearchV6EfficiencyPReplayR09_4h(ResearchV6EfficiencyPReplay4h):
    # One frozen overlay; eligibility calendar and nominal execution remain inherited.
    STOP_MULTIPLIER = 2.25
```

## strategies/ResearchV6EfficiencyPReplayR11_4h/__init__.py

SHA256 dad9ac84c7aced7cf406f37be9b8a111e11c3dd23448e79435605c1ceff49e44

```python
from strategies.ResearchV6EfficiencyPReplay4h import ResearchV6EfficiencyPReplay4h


class ResearchV6EfficiencyPReplayR11_4h(ResearchV6EfficiencyPReplay4h):
    # One frozen overlay; eligibility calendar and nominal execution remain inherited.
    STOP_MULTIPLIER = 2.75
```

## strategies/ResearchV6EfficiencyPReplayA09_4h/__init__.py

SHA256 c994bfc526c3ed9fac4064cc31aeb79256996534f26bb5020ef10fdc56899dc5

```python
from strategies.ResearchV6EfficiencyPReplay4h import ResearchV6EfficiencyPReplay4h


class ResearchV6EfficiencyPReplayA09_4h(ResearchV6EfficiencyPReplay4h):
    # One frozen overlay; eligibility calendar and nominal execution remain inherited.
    EFFICIENCY_THRESHOLD = 0.315
```

## strategies/ResearchV6EfficiencyPReplayA11_4h/__init__.py

SHA256 1f1f080b96a981063863f3b7b747d694ca427cc7f14cc5d7c9944a9911ccba42

```python
from strategies.ResearchV6EfficiencyPReplay4h import ResearchV6EfficiencyPReplay4h


class ResearchV6EfficiencyPReplayA11_4h(ResearchV6EfficiencyPReplay4h):
    # One frozen overlay; eligibility calendar and nominal execution remain inherited.
    EFFICIENCY_THRESHOLD = 0.385
```

# Dependencias capturadas para verificación

## ResearchV2Core4h

SHA256 577b84ebd15f27f5f598af5a4d1a3d3ed98313797656206c7691d29ad877564b

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

## ResearchV6Base4h

SHA256 fdcd1eaffbcc7845dc5701bb04d8f2bda6317dbd2e780bfa737c8b6e770776e6

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, ACCOUNTING_TOLERANCE,
)

# V6 4h decisions use explicit local clocks; only neutral V2 hooks are inherited.
BAR = 14400000
DAY = 86400000
OI_REFERENCE_BARS = 6


def closed_window(candles, now, count):
    """Finite OHLC with exactly the causal, consecutive window requested."""
    if (not isinstance(candles, np.ndarray) or candles.ndim != 2 or
            candles.shape[1] < 5 or count < 1 or now % BAR):
        return None
    rows = candles[candles[:, 0] + BAR <= now][-count:]
    if len(rows) != count or rows[-1, 0] != now - BAR or not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    o, c, h, low = (rows[:, i] for i in (1, 2, 3, 4))
    if np.any(h < np.maximum(o, c)) or np.any(low > np.minimum(o, c)) or np.any(h < low):
        return None
    return rows


def atr_window(candles, now, offset_bars=0):
    """Arithmetic TR, with shock risk frozen before the event when offset is one."""
    if offset_bars not in (0, 1):
        return None
    rows = closed_window(candles, now, 15 + offset_bars)
    if rows is None:
        return None
    if offset_bars:
        rows = rows[:-offset_bars]
    close, high, low = (rows[:, i] for i in (2, 3, 4))
    tr = np.maximum(high[1:] - low[1:],
                    np.maximum(abs(high[1:] - close[:-1]), abs(low[1:] - close[:-1])))
    value = float(np.mean(tr))
    if not math.isfinite(value) or value <= 0:
        return None
    return dict(value=value, first=int(rows[0, 0]), last=int(rows[-1, 0]),
                bars=rows[:, :5].tolist(), offset_bars=offset_bars)


def _oi_record_valid(record):
    """Freshness remains attached to its original decision, including delayed tests."""
    try:
        value, label, available, observed = (record[k] for k in
                                             ("value", "label", "available_at", "time"))
        return (record["status"] == "valid" and value is not None and
                math.isfinite(value) and value > 0 and label is not None and
                available == label + 360000 and available <= observed <= available + 600000)
    except (KeyError, TypeError, ValueError):
        # Missing/malformed provenance is invalid data, never an as-of replacement.
        return False


def oi_context(history, now, lag_bars=0, rule="rising", decline_fraction=.02):
    assert rule in ("rising", "declining")
    assert math.isfinite(decline_fraction) and 0 < decline_fraction < 1
    target = now - lag_bars * BAR
    current = next((r for r in reversed(history) if r["time"] == target), None)
    reference = next((r for r in reversed(history) if r["time"] == target - DAY), None)
    result = dict(quality="initialization", passed=False, current=current, reference=reference,
                  rule=rule, decline_fraction=decline_fraction if rule == "declining" else None, ratio=None)
    if current is None:
        return result
    if current["status"] != "valid":
        result["quality"] = current["status"]
    elif not _oi_record_valid(current):
        result["quality"] = "invalid"
    elif reference is None:
        result["quality"] = "initialization"
    elif not _oi_record_valid(reference):
        result["quality"] = "reference_invalid"
    else:
        result["quality"] = "valid"
        ratio = current["value"] / reference["value"]
        result["ratio"] = float(ratio) if math.isfinite(ratio) else None
        if rule == "declining":
            # A zero/invalid observation never masquerades as a complete position reduction.
            if not math.isfinite(ratio):
                result["quality"] = "arithmetic_invalid"
            else:
                result["passed"] = bool(ratio <= 1. - decline_fraction)
        else:
            result["passed"] = bool(current["value"] > reference["value"])
    return result


def v6_entry_plan(price, capital, fee, direction, distance):
    """Risk includes both taker fees; absence of TP does not create a fake target."""
    stop = price - direction * distance
    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in (price, capital, distance, stop)):
        return dict(reason="distance_invalid")
    if not math.isfinite(fee) or fee < 0:
        return dict(reason="distance_invalid")
    unit = distance + fee * (price + stop)
    # Eight decimals and 2% plus the notional cap are frozen research conventions.
    qty = math.floor(min(capital / price, .02 * capital / unit) * 1e8) / 1e8
    if qty <= 0:
        return dict(reason="qty_invalid")
    assert qty * unit <= .02 * capital + ACCOUNTING_TOLERANCE
    assert qty * price <= capital + ACCOUNTING_TOLERANCE
    return dict(reason="allowed", price=price, capital=capital, fee=fee, qty=qty,
                distance=distance, stop=stop, unit_loss=unit,
                risk_budget=.02 * capital, planned_stop_loss=qty * unit)


class ResearchV6Base4h(ResearchV2Core4h):
    """4h context and execution; frozen V2 contributes only clock-neutral hooks."""
    LINE = "abstract"
    TARGET_MODE = "none"
    REWARD_MULTIPLE = 1.
    MAX_HOLD_BARS = 24
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    START = 1598918400000
    FINISH = 1704067200000
    USE_OI = False
    OI_LAG_BARS = 0
    OI_RULE = "rising"
    OI_DECLINE_FRACTION = .02
    ACTIVE_WINDOWS = None
    FORCE_BOUNDARIES = ()

    def features(self, candles, now, atr):
        raise NotImplementedError

    def on_v6_open(self):
        pass

    def manage_position(self, atr):
        pass

    def _log_json(self, label, payload):
        # Preserve inherited accounting labels while identifying this new hourly cycle.
        if label.startswith("V2_"):
            label = "V6_" + label[3:]
        super()._log_json(label, payload)

    def _entry_window(self, now):
        return (self.START < now < self.FINISH and
                (self.ACTIVE_WINDOWS is None or any(a < now < b for a, b in self.ACTIVE_WINDOWS)))

    def _target(self, price, direction, distance, features):
        if self.TARGET_MODE == "none":
            return None
        assert self.TARGET_MODE == "r_multiple"
        return price + direction * self.REWARD_MULTIPLE * distance

    @staticmethod
    def _target_valid(target, price, direction):
        return target is None or (math.isfinite(target) and target > 0 and direction * (target - price) > 0)

    def before(self):
        now = int(self.time)
        atr = atr_window(self.candles, now, self.ATR_OFFSET_BARS)
        features = self.features(self.candles, now, atr)
        assert isinstance(features, dict) and features["direction"] in (-1, 0, 1)
        assert isinstance(features["valid"], bool) and isinstance(features.get("reason", "no_setup"), str)
        direction = int(features["direction"])
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            # Frozen retrospective policy: availability label+6m, freshness another10m.
            assert math.isfinite(value) and value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
                            available_at=label + 360000 if label is not None else None, status=status))
        # Exact 24h reference in this clock, delayed scenario and one spare; no backfill.
        history[:] = history[-(OI_REFERENCE_BARS + 2 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS, self.OI_RULE, self.OI_DECLINE_FRACTION)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.vars.get("v6_last_exit_at") != now and
                           self._entry_window(now))
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
            flags.append("oi_nonrising" if self.OI_RULE == "rising" else "oi_decline_below_threshold")
        if atr is None:
            flags.append("atr_invalid")
        if not features["valid"]:
            flags.append("features_invalid")
        plan = None
        reason = "allowed"
        if not self._entry_window(now):
            reason = "boundary_or_inactive"
        elif atr is None:
            reason = "atr_invalid"
        elif not features["valid"]:
            reason = "features_invalid"
        elif direction == 0:
            reason = features.get("reason", "no_setup")
        elif self.vars.get("v6_last_exit_at") == now:
            reason = "same_decision_exit"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif self.USE_OI and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising" if self.OI_RULE == "rising" else "oi_decline_below_threshold"
        else:
            distance = self.STOP_MULTIPLIER * atr["value"]
            plan = v6_entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
            reason = plan["reason"]
            if reason == "allowed":
                target = self._target(plan["price"], direction, distance, features)
                if not self._target_valid(target, plan["price"], direction):
                    reason = "target_invalid"
        if reason in ("distance_invalid", "qty_invalid", "target_invalid"):
            flags.append(reason)
        month = datetime.fromtimestamp((now - 1) / 1000, timezone.utc).strftime("%Y-%m")
        key = "long" if direction == 1 else "short" if direction == -1 else "none"
        for bucket_direction in ("all", key):
            bucket = self._bucket(month, bucket_direction)
            feature_reason = features.get("reason", "no_setup")
            reasons = bucket.setdefault("feature_reasons", {})
            reasons[feature_reason] = reasons.get(feature_reason, 0) + 1
            bucket["bars"] += 1
            bucket["opportunities"] += int(opportunity)
            bucket["primary"][reason] = bucket["primary"].get(reason, 0) + 1
            if opportunity:
                for flag in flags:
                    bucket["flags"][flag] = bucket["flags"].get(flag, 0) + 1
        self.vars["context"] = dict(time=now, day=day, month=month, direction=direction,
            allowed=reason == "allowed", oi=oi, atr=atr, plan=plan, funding=funding, features=features)

    def request_exit(self, reason):
        # Multiple close conditions at the same decision must not double-submit exits.
        if not self.is_open or self.vars.get("v6_exit_requested_at") == int(self.time):
            return
        self.vars["v6_exit_requested_at"] = int(self.time)
        self.vars["exit_reason"] = reason
        self._log_json("V6_EXIT_REQUEST", dict(time=int(self.time), reason=reason))
        self.liquidate()

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"]
        stop = entry - direction * distance
        target = self._target(entry, direction, distance, context["features"])
        self.vars.pop("v6_exit_requested_at", None)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        self._log_json("V6_FEATURES", dict(time=int(self.time), line=self.LINE,
                                        **context["features"]))
        self._log_json("V6_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=distance, distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=stop, target=target, atr=dict(value=atr["value"], first=atr["first"], last=atr["last"],
                                             bars=15, offset_bars=self.ATR_OFFSET_BARS, sha256=digest), oi=context["oi"], funding=context["funding"]))
        self.vars["v6_trade"] = dict(entry_at=int(self.position.opened_at), entry_atr=atr["value"],
                                    entry_fill=entry, distance=distance, stop_price=stop, target_price=target)
        if not math.isfinite(stop) or stop <= 0 or not self._target_valid(target, entry, direction):
            for side in ("all", "long" if direction == 1 else "short"):
                bucket = self._bucket(context["month"], side)
                bucket["flags"]["invalid_after_fill"] = bucket["flags"].get("invalid_after_fill", 0) + 1
            self.request_exit("invalid_after_fill")
            return
        self.stop_loss = qty, stop
        if target is not None:
            self.take_profit = qty, target
        self.on_v6_open()

    def update_position(self):
        # Calendar and elapsed holding exits take priority over indicator normalization.
        if any(self.time - BAR < boundary <= self.time for boundary in self.FORCE_BOUNDARIES):
            self.request_exit("calendar_boundary")
            return
        if self.time - self.position.opened_at >= self.MAX_HOLD_BARS * BAR:
            self.request_exit("maximum_hold")
            return
        # Indicator exits may only use a close after the fill, never its entry decision.
        if self.time > self.position.opened_at:
            self.manage_position(self.vars["context"]["atr"])

    def on_close_position(self, order, closed_trade):
        self.vars["v6_last_exit_at"] = int(closed_trade.closed_at)
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V6_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            assert value["bars"] == sum(value.get("feature_reasons", {}).values())
            self._log_json("V6_AUDIT", dict(key=key, **value))
        self._log_json("V6_PROVENANCE", dict(line=self.LINE, use_oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, oi_rule=self.OI_RULE,
            oi_decline_fraction=self.OI_DECLINE_FRACTION, stop_multiplier=self.STOP_MULTIPLIER,
            bar_ms=BAR, oi_reference_bars=OI_REFERENCE_BARS,
            atr_offset_bars=self.ATR_OFFSET_BARS, target_mode=self.TARGET_MODE,
            reward_multiple=self.REWARD_MULTIPLE, max_hold_bars=self.MAX_HOLD_BARS,
            start=self.START, finish=self.FINISH, active_windows=self.ACTIVE_WINDOWS,
            force_boundaries=self.FORCE_BOUNDARIES, final_exit_may_follow=True,
            self_checks=self.vars.get("self_checks")))
```

## efficiency_features

SHA256 ecfcc5fe4b77a2faee9edcdaea1bd391e33ec7fe73112e48718a2a8b90790bcf

```python
"""Finite directional path efficiency; pure algebra, with no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, closed_window


def _digest(rows):
    return hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def efficiency24(candles, now):
    """Twenty-four deltas use exactly25closed prices; a flat path is neutral."""
    rows = closed_window(candles, now, 25)
    if rows is None:
        return dict(valid=False, value=None, reason="efficiency_window_invalid")
    closes = [float(value) for value in rows[:, 2]]
    deltas = [right - left for left, right in zip(closes, closes[1:])]
    displacement = closes[-1] - closes[0]
    if not math.isfinite(displacement) or not all(math.isfinite(x) for x in deltas):
        return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
    scale = max(abs(x) for x in deltas)
    # Common normalization preserves the ratio while avoiding an overflowing raw sum.
    if scale == 0:
        normalized_path = normalized_displacement = value = 0.
    else:
        normalized_path = math.fsum(abs(x) / scale for x in deltas)
        normalized_displacement = displacement / scale
        if (not math.isfinite(normalized_path) or normalized_path <= 0 or
                not math.isfinite(normalized_displacement)):
            return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
        value = normalized_displacement / normalized_path
    if not math.isfinite(value):
        return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
    return dict(valid=True, value=float(value),
        reason="efficiency_flat" if scale == 0 else "efficiency_valid",
        displacement=float(displacement), step_scale=float(scale),
        normalized_displacement=float(normalized_displacement),
        normalized_path=float(normalized_path), first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=25, sha256=_digest(rows))


def _cross_direction(current, previous, threshold):
    if previous <= threshold and current > threshold:
        return 1
    if previous >= -threshold and current < -threshold:
        return -1
    return 0


def features(candles, now, atr, threshold=.35):
    if (isinstance(threshold, (bool, str)) or
            not isinstance(threshold, (int, float, np.integer, np.floating)) or
            not math.isfinite(threshold) or not 0 < threshold < 1):
        return dict(valid=False, direction=0, reason="efficiency_threshold_invalid", details={})
    # A fresh crossing needs two independent25-close windows: their union is26.
    rows = closed_window(candles, now, 26)
    if rows is None:
        return dict(valid=False, direction=0, reason="efficiency_window_invalid", details={})
    try:
        atr_valid = (isinstance(atr, dict) and math.isfinite(atr["value"]) and atr["value"] > 0)
    except (KeyError, TypeError, ValueError):
        atr_valid = False
    if not atr_valid:
        return dict(valid=False, direction=0, reason="efficiency_atr_invalid", details={})
    current = efficiency24(candles, now)
    previous = efficiency24(candles, now - BAR)
    if not current["valid"] or not previous["valid"]:
        return dict(valid=False, direction=0, reason="efficiency_arithmetic_invalid", details={})
    direction = _cross_direction(current["value"], previous["value"], float(threshold))
    reason = "efficiency_setup" if direction else "efficiency_no_cross"
    details = dict(threshold=float(threshold), current=current, previous=previous,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=26, sha256=_digest(rows))
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Independent finite-path oracles, boundaries and causal mutation checks."""
    count = 0

    def check(condition):
        nonlocal count
        assert bool(condition)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes))*BAR + first,
            closes, closes, closes*1.001, closes*.999, np.ones(len(closes))))

    def oracle(values):
        # Raw unnormalized arithmetic is independent of the scaled implementation.
        changes = [float(right - left) for left, right in zip(values, values[1:])]
        total = math.fsum(abs(x) for x in changes)
        return 0. if total == 0 else (float(values[-1]) - float(values[0])) / total

    closes = 100. + np.cumsum([0.] + [1., -1.]*12 + [14.])
    long = candles(closes)
    now = 26*BAR
    atr = dict(value=2.)
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    for case, expected in ((long, 1), (short, -1)):
        result = features(case, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "efficiency_setup")
        check(result["details"]["bars"] == 26)
        check(result["details"]["current"]["bars"] == 25)
        check(result["details"]["previous"]["bars"] == 25)
        check(len("V6_FEATURES " + json.dumps(dict(time=now, line="EFFICIENCY", **result),
              separators=(",", ":"), allow_nan=False)) <= 1900)
        for offset in (0, 1):
            state = efficiency24(case, now-offset*BAR)
            values = case[-25-offset:len(case)-offset if offset else None, 2]
            check(abs(state["value"] - oracle(values)) < 1e-12)
            check(state["last"]+BAR == now-offset*BAR)
            check(state["first"] == now-(25+offset)*BAR)
            mutated = case.copy()
            mutated[:len(case)-25-offset, 1:5] *= 1.1
            check(efficiency24(mutated, now-offset*BAR) == state)
        check(efficiency24(case[:-1], now-BAR) == efficiency24(case, now-BAR))
        check(features(case, now, atr, .315)["direction"] == expected)
        check(features(case, now, atr, .385)["direction"] == 0)
        check(features(case[-25:], now, atr)["valid"] is False)
        check(efficiency24(case[-25:], now)["valid"])
        future = candles([500., 600.], first=now)
        appended = np.vstack((case, future))
        check(features(appended, now, atr) == result)
        appended[-2:, 1:5] = float("nan")
        check(features(appended, now, atr) == result)
        older = candles(np.arange(40)+30., first=-40*BAR)
        extended = np.vstack((older, case))
        check(features(extended, now, atr) == result)
        extended[:40, 1:5] *= 2.
        check(features(extended, now, atr) == result)
        scaled = case.copy()
        scaled[:, 1:5] *= 2.
        check(abs(efficiency24(scaled, now)["value"] - result["details"]["current"]["value"]) < 1e-12)
        translated = case.copy()
        translated[:, 1:5] += 50.
        check(abs(efficiency24(translated, now)["value"] - result["details"]["current"]["value"]) < 1e-12)
        check(features(translated, now, atr)["direction"] == expected)
    check(abs(efficiency24(long, now)["value"] - 13./37.) < 1e-12)
    flat = candles([100.]*26)
    check(efficiency24(flat, now)["value"] == 0.)
    check(efficiency24(flat, now)["reason"] == "efficiency_flat")
    check(features(flat, now, atr)["valid"])
    check(features(flat, now, atr)["direction"] == 0)
    for values, expected in ((np.arange(26)+100., 1.), (200.-np.arange(26), -1.)):
        case = candles(values)
        check(efficiency24(case, now)["value"] == expected)
        check(features(case, now, atr)["direction"] == 0)
    zigzag = candles([100.] + [110., 100.]*11 + [110., 124.])
    straight = candles(np.arange(25)+100.)
    check(zigzag.shape[0] == 25)
    check(efficiency24(zigzag, 25*BAR)["displacement"] == efficiency24(straight, 25*BAR)["displacement"])
    check(efficiency24(zigzag, 25*BAR)["value"] < efficiency24(straight, 25*BAR)["value"])
    for h in (.315, .35, .385):
        check(_cross_direction(h+.01, h, h) == 1)
        check(_cross_direction(h, h-.01, h) == 0)
        check(_cross_direction(h+.01, h+.01, h) == 0)
        check(_cross_direction(-h-.01, -h, h) == -1)
        check(_cross_direction(-h, -h+.01, h) == 0)
        check(_cross_direction(-h-.01, -h-.01, h) == 0)
    for threshold in (0., 1., -.35, float("nan"), float("inf"), None, True, "0.35"):
        check(features(long, now, atr, threshold)["valid"] is False)
    for risk in (None, {}, dict(value=0.), dict(value=float("nan")), dict(value=float("inf"))):
        check(features(long, now, risk)["valid"] is False)
    for column, value in ((2, float("nan")), (1, 0.), (3, 1.), (4, 1000.), (0, now-2*BAR)):
        broken = long.copy()
        broken[-1, column] = value
        check(features(broken, now, atr)["valid"] is False)
        check(efficiency24(broken, now)["valid"] is False)
    check(features(long[:-1], now, atr)["valid"] is False)
    check(features(long, now+1, atr)["valid"] is False)
    check(efficiency24(long[-24:], now)["valid"] is False)
    # The raw path sum would overflow; scaling preserves a finite neutral result.
    large = candles([1e307 if i%2 == 0 else 9e307 for i in range(25)])
    large_state = efficiency24(large, 25*BAR)
    check(large_state["valid"] and large_state["value"] == 0.)
    check(large_state["normalized_path"] == 24.)
    check(len(json.dumps(large_state, allow_nan=False)) < 1000)
    original = long.copy()
    features(long, now, atr)
    check(np.array_equal(original, long))
    return dict(status="passed", assertions=count)
```

## ResearchV6EfficiencyP4h

SHA256 315e3a0d3edf8f6e0f7ef3665556000e98159c7286706695c3d6892c8720a3a3

```python
from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.efficiency_features import features, efficiency24


class ResearchV6EfficiencyP4h(ResearchV6Base4h):
    LINE = "EFFICIENCY"
    USE_OI = False
    EFFICIENCY_THRESHOLD = .35
    STOP_MULTIPLIER = 2.5
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 60
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.EFFICIENCY_THRESHOLD)

    def manage_position(self, atr):
        # Entry uses26prices; neutral-state exit needs only its own25valid closes.
        state = efficiency24(self.candles, int(self.time))
        if state["valid"] and ((self.is_long and state["value"] <= 0.) or
                               (self.is_short and state["value"] >= 0.)):
            self._log_json("V6_EFFICIENCY_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at),
                direction=1 if self.is_long else -1, **state))
            self.request_exit("efficiency_neutral")
```
