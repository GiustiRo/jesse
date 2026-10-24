# Implementación V2 congelada antes de economía
Fecha: 2026-10-20. Estado inicial: implementada, validación técnica en curso; cero backtests económicos V2.

Protocolo: RESEARCH_PROTOCOL_V2_20261020.md. Core independiente sin herencia ni cambios en V1. 16 subclases ATR definidas para E1–E4 train/eval, y cuatro smokes de nueve días 2020-09-01→2020-09-10. Los controles fijos son las 16 sesiones V1 identificadas en REGISTRY_V2.json; código de subclase, config, fechas y estado terminados releídos mediante MCP y verificados. Core V1 SHA256 conserva 4512d21d8bab7bd33389db6e32315cf4ffaf50955cfa6e03f48d25082c1c2546.

55 assertions sintéticas aprobadas, 23 fuentes compilan. Job de análisis 68fd6a0170f24105949c5e7ccd4314ca. La compilación y checks puros se ejecutaron con AST sobre literales de fuentes capturadas, sin importar archivos del proyecto en run_analysis ni leer fuera de inputs/. No acredita aún integración del motor. Fuentes y hashes completos a continuación. No se ejecutó pytest de framework, que no se modifica.

El ATR es SMA de 14 TR sobre 15 OHLC cerradas; valor congelado en entrada; código y hash de ventana OHLC en procedencia. Los logs fallan si una línea supera 1900 caracteres, margen bajo truncación 2000 del servicio; tolerancia contable 1e-6 USDT sólo por redondeo numérico. El sizing floor8 y cap notional son contractuales, no ajuste económico.

La secuencia exclusiva de rechazos conserva estado/precio/cupo/OI de V1 y añade luego ATR/distancia/qty; flags simultáneos se guardan por oportunidad. Los primeros 6 pasos OI (7 en retraso) se inicializan dentro del período. Salidas temporales/finales se registran explícitamente, sin inferirlas en análisis. Stop/target toman submitted_via del motor. Cierre inválido tras fill se cuenta y solicita MARKET de inmediato.

El freeze efectivo de economía exige completar smokes y sus conciliaciones; cualquier corrección técnica conservará versión previa y motivo antes del primer resultado económico.

## ResearchV2Core4h
SHA256: 3bb9b1c4f9667fb2d6098a409d360d720fc154b6b570096b1b8b2e2a5322e6c5

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
            assert value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
                            available_at=label + 360000 if label is not None else None, status=status))
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

## technical_checks
SHA256: 9010a12c7a35d3828bb5fa94f9d955bbdb9efb7169a127734386c5cd757aac73

```python
import math
import numpy as np

from strategies.ResearchV2Core4h import (
    BAR, DAY, atr_window, entry_plan, h1_direction, oi_context, protective_prices,
)
from strategies.ResearchWfCore4h import price_direction as v1_direction
from strategies.ResearchWfCore4h import oi_context as v1_oi_context


def technical_self_checks():
    checks = 0
    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Exact arithmetic example: two gap TRs of 11 and twelve TRs of 2.
    rows = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(24)])
    now = 15 * BAR
    check(atr_window(rows, now)["value"] == 2.)
    gaps = rows.copy()
    gaps[1, 1:5] = [110., 110., 111., 109.]
    check(math.isclose(atr_window(gaps, now)["value"], 46 / 14, abs_tol=1e-12))
    for cutoff in (15 * BAR, 16 * BAR, 20 * BAR):
        prefix = gaps[gaps[:, 0] + BAR <= cutoff]
        changed = gaps.copy()
        changed[changed[:, 0] + BAR > cutoff, 1:5] = np.nan
        check(atr_window(prefix, cutoff) == atr_window(gaps, cutoff))
        check(atr_window(prefix, cutoff) == atr_window(changed, cutoff))
    check(atr_window(rows[:14], now) is None)
    check(atr_window(rows, now + 60000) is None)
    missing = np.delete(rows, 10, axis=0)
    check(atr_window(missing, now) is None)
    duplicate = rows.copy()
    duplicate[10, 0] = duplicate[9, 0]
    check(atr_window(duplicate, now) is None)
    for field, value in ((1, float("nan")), (2, 0.), (3, 99.), (4, 102.)):
        invalid = rows.copy()
        invalid[10, field] = value
        check(atr_window(invalid, now) is None)
    flat = rows.copy()
    flat[:, 1:5] = 100.
    check(atr_window(flat, now) is None)
    old_invalid = rows.copy()
    old_invalid[0, 1] = np.nan
    check(atr_window(old_invalid, 20 * BAR) == atr_window(rows, 20 * BAR))

    # Symmetric risk budget with asymmetric long/short round-trip fee bases.
    for side in (-1, 1):
        plan = entry_plan(100., 10000., .00045, side, 2.)
        unit = 2 + .00045 * (200 - side * 2)
        check(plan["qty"] == math.floor((200 / unit) * 1e8) / 1e8)
        check(plan["qty"] * unit <= 200. and plan["qty"] * 100 <= 10000)
        capped = entry_plan(100., 10000., .00045, side, .01)
        check(capped["qty"] == 100. and capped["planned_stop_loss"] < 200.)
        higher_fee = entry_plan(100., 10000., .0009, side, 2.)
        check(higher_fee["qty"] < plan["qty"])
        # ATR distance stays at 2 despite a hypothetical adverse fill on either side.
        fill = 100 * (1 + side * .001)
        prices = protective_prices(fill, side, 2.)
        check(math.isclose(abs(prices[0] - fill), 2., abs_tol=1e-12))
        check(math.isclose(abs(prices[1] - fill), 4., abs_tol=1e-12))
        fixed = protective_prices(fill, side, .02 * fill)
        check(math.isclose(abs(fixed[0] - fill), .02 * fill, abs_tol=1e-12))
    for args in ((100., 10000., .00045, 1, 100.), (100., 10000., .00045, -1, 50.),
                 (100., 0., .00045, 1, 2.), (100., 10000., .00045, 1, float("nan")),
                 (float("inf"), 10000., .00045, 1, 2.)):
        check(entry_plan(*args)["reason"] == "distance_invalid")
    check(entry_plan(100., 1e-12, .00045, 1, 2.)["reason"] == "qty_invalid")
    check(protective_prices(100., 0, 2.) is None)
    for direction in (-1, 1):
        prices = rows.copy()
        prices[13, 2] = 120 if direction == 1 else 80
        prices[13, 3:5] = [121, 79]
        t = 14 * BAR
        check(h1_direction(prices, t) == v1_direction(prices, t, 1) == direction)
        future = prices.copy()
        future[future[:, 0] + BAR > t, 1:5] = 1e9
        check(h1_direction(future, t) == direction)
    history = [dict(time=i * BAR, value=float(i + 1), status="valid", label=i * BAR - 600000)
               for i in range(10)]
    for lag in (0, 1):
        for t in (5 * BAR, 6 * BAR, 7 * BAR):
            check(oi_context(history, t, lag) == v1_oi_context(history, t, lag))
    for status in ("zero", "stale", "absent"):
        changed = [dict(r) for r in history]
        changed[6]["status"] = status
        check(oi_context(changed, 6 * BAR)["quality"] == status)
    changed = [dict(r) for r in history]
    changed[0]["status"] = "zero"
    check(oi_context(changed, 6 * BAR)["quality"] == "reference_invalid")
    changed = [dict(r) for r in history]
    for r in changed[7:]:
        r["value"] = 1e9
    check(oi_context(changed, 6 * BAR) == oi_context(history[:7], 6 * BAR))
    check(oi_context(history, 7 * BAR, 1) == oi_context(history, 6 * BAR))
    return dict(status="passed", assertions=checks)


def assert_real_bar(strategy):
    """Checks real prefix causality and exact H1 parity without judging trade PnL."""
    candles, now = strategy.candles, int(strategy.time)
    prefix = candles[candles[:, 0] + BAR <= now]
    assert h1_direction(candles, now) == v1_direction(candles, now, 1)
    assert atr_window(prefix, now) == atr_window(candles, now)
    current = atr_window(candles, now)
    if current is not None:
        raw = np.array(current["bars"])
        independent = [max(r[3] - r[4], abs(r[3] - prev[2]), abs(r[4] - prev[2]))
                       for prev, r in zip(raw[:-1], raw[1:])]
        assert math.isclose(sum(independent) / 14, current["value"], abs_tol=1e-9)

```

## ResearchWfCore4h
SHA256: 4512d21d8bab7bd33389db6e32315cf4ffaf50955cfa6e03f48d25082c1c2546

```python
import json
from datetime import datetime, timezone
import numpy as np
from jesse import utils
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000


def price_direction(candles, now, family):
    rows = candles[candles[:, 0] + BAR <= now]
    if len(rows) < 2 or rows[-1, 0] != now - BAR or rows[-2, 0] != now - 2 * BAR:
        return 0
    c, prev = float(rows[-1, 2]), float(rows[-2, 2])
    if family == 3:
        ref = rows[rows[:, 0] == now - DAY - BAR]
        if len(ref) != 1:
            return 0
        old = float(ref[0, 2])
        return 1 if c > old and c > prev else -1 if c < old and c < prev else 0
    day = now // DAY * DAY
    previous = rows[(rows[:, 0] >= day - DAY) & (rows[:, 0] < day)]
    if len(previous) != 6 or len(set(previous[:, 0])) != 6:
        return 0
    high, low = float(np.max(previous[:, 3])), float(np.min(previous[:, 4]))
    if family == 1:
        return 1 if c > high else -1 if c < low else 0
    assert family == 2
    if low <= c <= high:
        return 1 if prev < low else -1 if prev > high else 0
    return 0


def funding_context(rows, now, family, direction):
    need = 32 if family == 3 else 31
    visible = [r for r in rows if r["available_at"] <= now][-need:]
    result = dict(quality="funding_absent", passed=False, rate=None, z=None, prior_z=None)
    if len(visible) != need:
        return result
    result.update(settled_at=visible[-1].get("settled_at"), available_at=visible[-1]["available_at"])
    rates = np.array([r["rate_decimal"] for r in visible], dtype=float)
    def z_at(values):
        ref = values[:-1]
        std = float(np.std(ref, ddof=0))
        if np.ptp(ref) <= 0 or std <= 0 or not np.isfinite(std):
            return None
        z = (values[-1] - float(np.mean(ref))) / std
        return float(z) if np.isfinite(z) else None
    z = z_at(rates[-31:])
    prior_z = z_at(rates[:-1]) if family == 3 else None
    result.update(rate=float(rates[-1]), z=z, prior_z=prior_z)
    if z is None or (family == 3 and prior_z is None):
        result["quality"] = "funding_variance"
        return result
    result["quality"] = "valid"
    rate = float(rates[-1])
    if family == 1:
        passed = not ((direction == 1 and rate > 0 and z > 2) or
                      (direction == -1 and rate < 0 and z < -2))
    elif family == 2:
        passed = (direction == 1 and rate < 0 and z < -2) or (direction == -1 and rate > 0 and z > 2)
    else:
        old = float(rates[-2])
        passed = ((direction == 1 and old < 0 and prior_z < -2 and old < rate <= 0 and abs(z) <= 2) or
                  (direction == -1 and old > 0 and prior_z > 2 and 0 <= rate < old and abs(z) <= 2))
    result["passed"] = bool(passed)
    return result


def oi_context(history, now, lag_bars=0):
    # Delaying a recorded observation never changes its original freshness test.
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


def feature_self_checks():
    now = 8 * BAR
    candles = np.array([[i * BAR, 100., 100., 110., 90., 1.] for i in range(20)])
    candles[6, 2], candles[7, 2] = 80, 100
    assert price_direction(candles, now, 2) == 1
    candles[6, 2] = 120
    assert price_direction(candles, now, 2) == -1
    candles[6, 2], candles[7, 2] = 119, 120
    assert price_direction(candles, now, 1) == price_direction(candles, now, 3) == 1
    candles[6, 2], candles[7, 2] = 81, 80
    assert price_direction(candles, now, 1) == price_direction(candles, now, 3) == -1
    for family in (1, 2, 3):
        for cutoff in (8 * BAR, 9 * BAR, 12 * BAR):
            prefix = candles[candles[:, 0] + BAR <= cutoff]
            changed = candles.copy()
            changed[changed[:, 0] + BAR > cutoff, 1:5] = 1e9
            assert price_direction(prefix, cutoff, family) == price_direction(candles, cutoff, family)
            assert price_direction(changed, cutoff, family) == price_direction(prefix, cutoff, family)
    rows = [dict(available_at=i * 60000, rate_decimal=(-1 if i % 2 else 1) * .0001) for i in range(36)]
    cutoff = 31 * 60000
    for family in (1, 2, 3):
        for direction in (-1, 1):
            changed = [dict(r) for r in rows]
            for row in changed[32:]:
                row["rate_decimal"] = 1e9
            assert funding_context(rows, cutoff, family, direction) == funding_context(rows[:32], cutoff, family, direction)
            assert funding_context(changed, cutoff, family, direction) == funding_context(rows[:32], cutoff, family, direction)
    for direction in (-1, 1):
        r = [dict(v) for v in rows[:32]]
        r[-2]["rate_decimal"] = -.01 * direction
        r[-1]["rate_decimal"] = -.00001 * direction
        assert funding_context(r, cutoff, 3, direction)["passed"]
        r[-1]["rate_decimal"] = -.01 * direction
        assert funding_context(r, cutoff, 2, direction)["passed"]
        r[-1]["rate_decimal"] = .01 * direction
        assert not funding_context(r, cutoff, 1, direction)["passed"]
    equal = [dict(available_at=i, rate_decimal=.0001) for i in range(32)]
    assert funding_context(equal, 32, 3, 1)["quality"] == "funding_variance"
    history = [dict(time=i * BAR, value=float(i + 1), status="valid", label=i * BAR - 600000) for i in range(10)]
    assert oi_context(history[:6], 5 * BAR)["quality"] == "initialization"
    assert oi_context(history, 6 * BAR)["passed"]
    changed = [dict(v) for v in history]
    for r in changed[7:]:
        r["value"] = 1e9
    assert oi_context(changed, 6 * BAR) == oi_context(history[:7], 6 * BAR)
    changed[6]["status"] = "zero"
    assert oi_context(changed, 6 * BAR)["quality"] == "zero"
    changed[6]["status"] = "stale"
    assert oi_context(changed, 6 * BAR)["quality"] == "stale"
    changed[6]["status"] = "valid"
    changed[0]["status"] = "zero"
    assert oi_context(changed, 6 * BAR)["quality"] == "reference_invalid"
    assert oi_context(history, 7 * BAR, 1) == oi_context(history, 6 * BAR)
    return "passed"


class ResearchWfCore4h(Strategy):
    """Frozen V1 rules; per-fold subclasses set only identity and UTC bounds."""
    FAMILY = 1
    USE_FUNDING = False
    USE_OI = False
    START = 1598918400000
    FINISH = 1640995200000
    STOP = .02
    TARGET = .04
    OI_LAG_BARS = 0
    MASK_FUNDING = False
    MASK_OI = False

    def _bucket(self, month, direction):
        return self.vars.setdefault("audit", {}).setdefault(month + ":" + direction, dict(
            bars=0, opportunities=0, entries=0, exits=0, primary={}, flags={}))

    def before(self):
        now = int(self.time)
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = feature_self_checks()
        direction = price_direction(self.candles, now, self.FAMILY)
        rows = self.get_funding_history(count=32 if self.FAMILY == 3 else 31)
        assert all(r["available_at"] <= now for r in rows)
        funding = funding_context(rows, now, self.FAMILY, direction)
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            assert value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
            available_at=label + 360000 if label is not None else None, status=status))
        history[:] = history[-(8 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        day = now // DAY * DAY
        opportunity = (direction != 0 and self.is_close and not self.entry_orders and
                       self.vars.get("entry_day") != day and self.START < now < self.FINISH)
        flags = []
        if funding["quality"] != "valid":
            flags.append(funding["quality"])
        elif not funding["passed"]:
            flags.append("funding_economic")
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
        reason = "allowed"
        if not self.START < now < self.FINISH:
            reason = "boundary"
        elif direction == 0:
            reason = "no_price"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif (self.USE_FUNDING or self.MASK_FUNDING) and funding["quality"] != "valid":
            reason = funding["quality"]
        elif self.USE_FUNDING and not funding["passed"]:
            reason = "funding_economic"
        elif (self.USE_OI or self.MASK_OI) and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising"
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
            allowed=reason == "allowed", funding=funding, oi=oi)

    def should_long(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == 1

    def should_short(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == -1

    def _enter(self, direction):
        context = self.vars["context"]
        capital, price = self.available_margin, self.price
        stop = price * (1 - direction * self.STOP)
        unit = abs(price - stop) + self.fee_rate * (price + stop)
        qty = utils.size_to_qty(min(capital, .02 * capital / unit * price), price, precision=8)
        assert qty * unit <= .02 * capital + 1e-6
        self.vars["intent"] = dict(capital=capital, decision_price=price, qty=qty, context=context)
        if direction == 1:
            self.buy = qty, price
        else:
            self.sell = qty, price

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        context = self.vars["intent"]["context"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        self.stop_loss = qty, entry * (1 - direction * self.STOP)
        self.take_profit = qty, entry * (1 + direction * self.TARGET)
        self.vars["entry_day"] = context["day"]
        for d in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], d)["entries"] += 1
        # Bounded, durable intent/fill provenance; full source and parameters in registry.
        self.log("WF_ENTRY " + json.dumps(dict(time=int(self.time), direction=direction,
            capital=self.vars["intent"]["capital"], decision=self.vars["intent"]["decision_price"],
            fill=entry, qty=qty, stop=entry * (1 - direction * self.STOP),
            target=entry * (1 + direction * self.TARGET), funding=context["funding"], oi=context["oi"])))

    def on_close_position(self, order, closed_trade):
        assert abs(self.balance - self.vars["intent"]["capital"] - closed_trade.pnl) < 1e-6
        month = datetime.fromtimestamp((int(self.time) - 1) / 1000, timezone.utc).strftime("%Y-%m")
        for d in ("all", closed_trade.type):
            self._bucket(month, d)["exits"] += 1
        self.log("WF_CLOSE " + json.dumps(dict(time=int(self.time), pnl=closed_trade.pnl,
            balance=self.balance, trade_id=str(closed_trade.id))))

    def update_position(self):
        if self.time - self.position.opened_at >= DAY:
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        # Framework may force-close a remaining trade after this hook. Its final
        # WF_CLOSE record is authoritative for exits; do not hide that ordering.
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            self.log("WF_AUDIT " + json.dumps(dict(key=key, **value), sort_keys=True))
        self.log("WF_PROVENANCE " + json.dumps(dict(self_checks=self.vars.get("self_checks"),
            family=self.FAMILY, funding=self.USE_FUNDING, oi=self.USE_OI, stop=self.STOP,
            target=self.TARGET, hold_ms=DAY, oi_lag_bars=self.OI_LAG_BARS,
            start=self.START, finish=self.FINISH, final_exit_may_follow=True)))

```

## ResearchV2SmokeP4h
SHA256: 1cc3e4e7ec82ea67220c1e1af22b5a7655fedbb915d55facb46956b2e4ee7fe0

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h
from strategies.ResearchV2Core4h.technical_checks import technical_self_checks, assert_real_bar


class ResearchV2SmokeP4h(ResearchV2Core4h):
    USE_OI = False
    OI_LAG_BARS = 0
    START = 1598918400000
    FINISH = 1599696000000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = technical_self_checks()
            self._log_json("V2_SELF_CHECKS", self.vars["self_checks"])
        assert_real_bar(self)
        super().before()

```

## ResearchV2SmokeOi4h
SHA256: 39f843eb2ee86efca5c4bfa789517cd5a65623eec86d2d68ba11b0e847591d9d

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h
from strategies.ResearchV2Core4h.technical_checks import technical_self_checks, assert_real_bar


class ResearchV2SmokeOi4h(ResearchV2Core4h):
    USE_OI = True
    OI_LAG_BARS = 0
    START = 1598918400000
    FINISH = 1599696000000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = technical_self_checks()
            self._log_json("V2_SELF_CHECKS", self.vars["self_checks"])
        assert_real_bar(self)
        super().before()

```

## ResearchV2SmokeStress4h
SHA256: 634776fbdfffc899763d9ba15793a408bbba0b60bb216e6dbfc40ed6ad4969bf

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h
from strategies.ResearchV2Core4h.technical_checks import technical_self_checks, assert_real_bar


class ResearchV2SmokeStress4h(ResearchV2Core4h):
    USE_OI = False
    OI_LAG_BARS = 0
    START = 1598918400000
    FINISH = 1599696000000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = technical_self_checks()
            self._log_json("V2_SELF_CHECKS", self.vars["self_checks"])
        assert_real_bar(self)
        super().before()

```

## ResearchV2SmokeLag4h
SHA256: ca8c071a491b75b767dd1fdc456b3356056f7e504ff36ddbdcab4ba3a94c57e2

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h
from strategies.ResearchV2Core4h.technical_checks import technical_self_checks, assert_real_bar


class ResearchV2SmokeLag4h(ResearchV2Core4h):
    USE_OI = True
    OI_LAG_BARS = 1
    START = 1598918400000
    FINISH = 1599696000000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = technical_self_checks()
            self._log_json("V2_SELF_CHECKS", self.vars["self_checks"])
        assert_real_bar(self)
        super().before()

```

## ResearchV2_H1_ATR_P_E1T
SHA256: 304da2bbb7fb0ff27b3d1f6a292fce9b23e8e6cd5bf9843e2b25a83acc426d99

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E1T(ResearchV2Core4h):
    USE_OI = False
    START = 1598918400000
    FINISH = 1640995200000

```

## ResearchV2_H1_ATR_P_E1V
SHA256: 7fd6961257a9f9b21aeafa09c6385753caaec679c84c1fb45d3a7f573e01a22b

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E1V(ResearchV2Core4h):
    USE_OI = False
    START = 1640995200000
    FINISH = 1656633600000

```

## ResearchV2_H1_ATR_POI_E1T
SHA256: 96375624aed9cfb2d4657f85623c4987f8e37550e129007886e449e1019f8fe6

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E1T(ResearchV2Core4h):
    USE_OI = True
    START = 1598918400000
    FINISH = 1640995200000

```

## ResearchV2_H1_ATR_POI_E1V
SHA256: 1854b83e7c0eda63ab68876fd41613d1370b996dd97af0c64969b4381e4b4cb5

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E1V(ResearchV2Core4h):
    USE_OI = True
    START = 1640995200000
    FINISH = 1656633600000

```

## ResearchV2_H1_ATR_P_E2T
SHA256: ffb559296d81a0271b6fe594fb19b3d1e41773f491435bd6e6e7083f750deed7

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E2T(ResearchV2Core4h):
    USE_OI = False
    START = 1598918400000
    FINISH = 1656633600000

```

## ResearchV2_H1_ATR_P_E2V
SHA256: 855f41b9ea48c86eb66dc56e52043c004d5c24796b4e262869c4aa5ed831d2ff

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E2V(ResearchV2Core4h):
    USE_OI = False
    START = 1656633600000
    FINISH = 1672531200000

```

## ResearchV2_H1_ATR_POI_E2T
SHA256: d54c01af05ab9e39093ee2e0a83d090b421463cd2d8040e2f78e0b586fef80f1

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E2T(ResearchV2Core4h):
    USE_OI = True
    START = 1598918400000
    FINISH = 1656633600000

```

## ResearchV2_H1_ATR_POI_E2V
SHA256: 4d4755fe486bd3172ac820bda52ca9728f74783c858ac5bf72016b8c32a6f655

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E2V(ResearchV2Core4h):
    USE_OI = True
    START = 1656633600000
    FINISH = 1672531200000

```

## ResearchV2_H1_ATR_P_E3T
SHA256: 5016c1a7e5c93cf42c84419f0fbb17266c90367def6085010289051654486f24

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E3T(ResearchV2Core4h):
    USE_OI = False
    START = 1598918400000
    FINISH = 1672531200000

```

## ResearchV2_H1_ATR_P_E3V
SHA256: d23e9e42d206bb0ee9ba9d1568ee498186ed74c12b8e45c49ea6d9eeacee9d13

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E3V(ResearchV2Core4h):
    USE_OI = False
    START = 1672531200000
    FINISH = 1688169600000

```

## ResearchV2_H1_ATR_POI_E3T
SHA256: e2278f49a2042e3e3136999ddfacbf6ef172149c48bd3a169b718694cdfe8a8a

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E3T(ResearchV2Core4h):
    USE_OI = True
    START = 1598918400000
    FINISH = 1672531200000

```

## ResearchV2_H1_ATR_POI_E3V
SHA256: 1afaae6bb69a8ccc79037a974c9e8480dabafffe6abb1b456095973c95029475

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E3V(ResearchV2Core4h):
    USE_OI = True
    START = 1672531200000
    FINISH = 1688169600000

```

## ResearchV2_H1_ATR_P_E4T
SHA256: 434f37cb6638386d6786b243dd1a472de94d564d321d5adeb7fe13486271756d

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E4T(ResearchV2Core4h):
    USE_OI = False
    START = 1598918400000
    FINISH = 1688169600000

```

## ResearchV2_H1_ATR_P_E4V
SHA256: 1c813e33428bd1f50942934df23e72fbf6df216073320678943f1f9138ab76f0

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_P_E4V(ResearchV2Core4h):
    USE_OI = False
    START = 1688169600000
    FINISH = 1704067200000

```

## ResearchV2_H1_ATR_POI_E4T
SHA256: 6e9184f5ec92100169d327ac1972616f3829e669c5ad98ed8bb0dcbc9b874843

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E4T(ResearchV2Core4h):
    USE_OI = True
    START = 1598918400000
    FINISH = 1688169600000

```

## ResearchV2_H1_ATR_POI_E4V
SHA256: dbccd91fbf77661fa0f7525f3f0d414331f324674c41c1e222002dc0cfe6ccd8

```python
from strategies.ResearchV2Core4h import ResearchV2Core4h


class ResearchV2_H1_ATR_POI_E4V(ResearchV2Core4h):
    USE_OI = True
    START = 1688169600000
    FINISH = 1704067200000

```
