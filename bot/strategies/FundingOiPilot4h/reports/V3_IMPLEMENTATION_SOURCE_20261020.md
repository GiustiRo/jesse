# V3 — fuentes congeladas antes de resultados económicos
Fecha:2026-10-20. Quince fuentes compiladas,164assertions puras aprobadas:base28,CHANNEL47,PULLBACK31,RANGE58. Job 2891f7593f674a379dd536bc006c1b0b. La ejecución de pruebas usó AST de literales capturados, sin importar archivos del proyecto ni leer fuera de inputs/ en run_analysis. Los smokes pendientes verificarán importación/runtime real; no confundir compilación con integración de motor.

BaseV3 comparte únicamente ejecución/instrumentación heredada de V2 inmutable, con hooks nuevos de features/protección. Su fuente y dependenciaV2 completas quedan aquí. Fakes de base verifican superficie pública de Strategy, no simulan fills. Un fallo inicial por atributo time ausente del fake se corrigió antes de cualquier backtest (jobc7ea3dc6f36d419daaaacfb95b6f7092); no cambio económico. Reglas/criterios en RESEARCH_PROTOCOL_V3_20261020.md. No2026.

## strategies/ResearchV3Base4h/__init__.py
SHA256: f5d77eecabb089d7ca719648cd7e8d4aed79e6ac5e3c54722f2c24b9d2f6df1a

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, atr_window, oi_context, BAR, DAY, ACCOUNTING_TOLERANCE,
)


def closed_window(candles, now, count):
    """Finite OHLC with exactly the causal, consecutive window requested."""
    rows = candles[candles[:, 0] + BAR <= now][-count:]
    if len(rows) != count or rows[-1, 0] != now - BAR or not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    o, c, h, low = (rows[:, i] for i in (1, 2, 3, 4))
    if np.any(h < np.maximum(o, c)) or np.any(low > np.minimum(o, c)) or np.any(h < low):
        return None
    return rows


def v3_entry_plan(price, capital, fee, direction, distance):
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


class ResearchV3Base4h(ResearchV2Core4h):
    """Shared execution and audit only; sectors implement causal feature functions."""
    LINE = "abstract"
    TARGET_MODE = "none"
    REWARD_MULTIPLE = 3.
    MAX_HOLD_BARS = 6
    STOP_MULTIPLIER = 2.
    TRAIL_MULTIPLIER = 3.
    START = 1598918400000
    FINISH = 1704067200000
    USE_OI = False
    OI_LAG_BARS = 0
    ACTIVE_WINDOWS = None
    FORCE_BOUNDARIES = ()

    def features(self, candles, now, atr):
        raise NotImplementedError

    def on_v3_open(self):
        pass

    def manage_position(self, atr):
        pass

    def _log_json(self, label, payload):
        # Reuse the bounded logger and accounting hook without mislabeling V3 as V2.
        if label.startswith("V2_"):
            label = "V3_" + label[3:]
        super()._log_json(label, payload)

    def _entry_window(self, now):
        return (self.START < now < self.FINISH and
                (self.ACTIVE_WINDOWS is None or any(a < now < b for a, b in self.ACTIVE_WINDOWS)))

    def _target(self, price, direction, distance, features):
        if self.TARGET_MODE == "none":
            return None
        if self.TARGET_MODE == "r_multiple":
            return price + direction * self.REWARD_MULTIPLE * distance
        assert self.TARGET_MODE == "frozen_mean"
        return features["mean_target"]

    @staticmethod
    def _target_valid(target, price, direction):
        return target is None or (math.isfinite(target) and target > 0 and direction * (target - price) > 0)

    def before(self):
        now = int(self.time)
        atr = atr_window(self.candles, now)
        features = self.features(self.candles, now, atr)
        assert isinstance(features, dict) and features["direction"] in (-1, 0, 1)
        direction = int(features["direction"])
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            # Frozen retrospective policy: availability label+6m, freshness another10m.
            assert value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
                            available_at=label + 360000 if label is not None else None, status=status))
        # Current plus six4h steps, optionallag and one spare; no fabricated warmup OI.
        history[:] = history[-(8 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self._entry_window(now))
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
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif self.USE_OI and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising"
        else:
            distance = self.STOP_MULTIPLIER * atr["value"]
            plan = v3_entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
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
            bucket["bars"] += 1
            bucket["opportunities"] += int(opportunity)
            bucket["primary"][reason] = bucket["primary"].get(reason, 0) + 1
            if opportunity:
                for flag in flags:
                    bucket["flags"][flag] = bucket["flags"].get(flag, 0) + 1
        self.vars["context"] = dict(time=now, day=day, month=month, direction=direction,
            allowed=reason == "allowed", oi=oi, atr=atr, plan=plan, funding=funding, features=features)

    def request_exit(self, reason):
        # Updating a trailing stop and a holding boundary must not double-submit exits.
        if not self.is_open or self.vars.get("v3_exit_requested_at") == int(self.time):
            return
        self.vars["v3_exit_requested_at"] = int(self.time)
        self.vars["exit_reason"] = reason
        self._log_json("V3_EXIT_REQUEST", dict(time=int(self.time), reason=reason))
        self.liquidate()

    def replace_stop(self, candidate):
        """Closed-bar ratchet; a crossed threshold exits now, never at a past price."""
        trade = self.vars["v3_trade"]
        direction = 1 if self.is_long else -1
        old = trade["stop_price"]
        if not math.isfinite(candidate) or candidate <= 0 or direction * (candidate - old) <= 0:
            return
        if direction * (self.price - candidate) <= 0:
            self.request_exit("trailing_crossed_at_decision")
            return
        trade["stop_price"] = candidate
        self._log_json("V3_STOP_UPDATE", dict(time=int(self.time), old=old, new=candidate))
        self.stop_loss = abs(self.position.qty), candidate

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"]
        stop = entry - direction * distance
        target = self._target(entry, direction, distance, context["features"])
        self.vars.pop("v3_exit_requested_at", None)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        self._log_json("V3_FEATURES", dict(time=int(self.time), line=self.LINE,
                                        **context["features"]))
        self._log_json("V3_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=distance, distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=stop, target=target, atr=dict(value=atr["value"], first=atr["first"], last=atr["last"],
                                             bars=15, sha256=digest), oi=context["oi"], funding=context["funding"]))
        self.vars["v3_trade"] = dict(entry_at=int(self.position.opened_at), entry_atr=atr["value"],
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
        self.on_v3_open()

    def update_position(self):
        # A calendar close or maximum hold takes priority at the same close as a ratchet.
        if any(self.time - BAR < boundary <= self.time for boundary in self.FORCE_BOUNDARIES):
            self.request_exit("calendar_boundary")
            return
        if self.time - self.position.opened_at >= self.MAX_HOLD_BARS * BAR:
            self.request_exit("maximum_hold")
            return
        self.manage_position(self.vars["context"]["atr"])

    def before_terminate(self):
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V3_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            self._log_json("V3_AUDIT", dict(key=key, **value))
        self._log_json("V3_PROVENANCE", dict(line=self.LINE, use_oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, stop_multiplier=self.STOP_MULTIPLIER,
            trail_multiplier=self.TRAIL_MULTIPLIER, target_mode=self.TARGET_MODE,
            reward_multiple=self.REWARD_MULTIPLE, max_hold_bars=self.MAX_HOLD_BARS,
            start=self.START, finish=self.FINISH, active_windows=self.ACTIVE_WINDOWS,
            force_boundaries=self.FORCE_BOUNDARIES, final_exit_may_follow=True,
            self_checks=self.vars.get("self_checks")))

```

## strategies/ResearchV3Base4h/base_checks.py
SHA256: 8a5dcd739ef091fd22dc53ab30d2d4f7543c40d5ec9deda9e52edec155cf2641

```python
import math
from types import SimpleNamespace

import numpy as np

from strategies.ResearchV3Base4h import ResearchV3Base4h, closed_window, v3_entry_plan, BAR


class StopSurface:
    """Public strategy surface only; this fake never simulates fills or broker PnL."""
    def __init__(self, direction):
        self.is_long = direction == 1
        self.price = 100.
        self.time = 1000000
        self.position = SimpleNamespace(qty=direction * 2.)
        self.vars = {"v3_trade": {"stop_price": 95. if direction == 1 else 105.}}
        self.stop_loss = None
        self.events = []

    def request_exit(self, reason):
        self.events.append(reason)

    def _log_json(self, label, payload):
        self.events.append(label)


class ExitSurface:
    def __init__(self):
        self.is_open = True
        self.time = 1000000
        self.vars = {}
        self.exits = 0

    def _log_json(self, label, payload):
        pass

    def liquidate(self):
        self.exits += 1


def self_checks():
    count = 0
    def check(value):
        nonlocal count
        assert value
        count += 1

    rows = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(150)])
    now = 144 * BAR
    check(len(closed_window(rows, now, 144)) == 144)
    changed = rows.copy()
    changed[changed[:, 0] + BAR > now, 1:5] = np.nan
    check(np.array_equal(closed_window(changed, now, 144), closed_window(rows[:144], now, 144)))
    gap = np.delete(rows, 30, axis=0)
    check(closed_window(gap, now, 144) is None)
    check(closed_window(rows[:143], now, 144) is None)
    for direction in (-1, 1):
        plan = v3_entry_plan(100., 10000., .00045, direction, 2.)
        unit = 2 + .00045 * (200 - direction * 2)
        check(plan["qty"] == math.floor(200 / unit * 1e8) / 1e8)
        check(plan["qty"] * unit <= 200.)
        check(v3_entry_plan(100., 10000., .00045, direction, .01)["qty"] == 100.)
        check(v3_entry_plan(100., 1e-12, .00045, direction, 2.)["reason"] == "qty_invalid")
        fake = StopSurface(direction)
        old = fake.vars["v3_trade"]["stop_price"]
        ResearchV3Base4h.replace_stop(fake, old - direction)
        check(fake.stop_loss is None and not fake.events)
        ResearchV3Base4h.replace_stop(fake, old + direction)
        check(fake.stop_loss == (2., old + direction))
        ResearchV3Base4h.replace_stop(fake, 100 + direction)
        check(fake.events[-1] == "trailing_crossed_at_decision")
        check(fake.vars["v3_trade"]["stop_price"] == old + direction)
        check(ResearchV3Base4h._target_valid(110 if direction == 1 else 90, 100, direction))
        check(not ResearchV3Base4h._target_valid(90 if direction == 1 else 110, 100, direction))
    fake = ExitSurface()
    ResearchV3Base4h.request_exit(fake, "one")
    ResearchV3Base4h.request_exit(fake, "two")
    check(fake.exits == 1 and fake.vars["exit_reason"] == "one")
    fake.time += BAR
    ResearchV3Base4h.request_exit(fake, "next")
    check(fake.exits == 2 and fake.vars["exit_reason"] == "next")
    check(v3_entry_plan(100., 10000., .00045, 1, 100.)["reason"] == "distance_invalid")
    check(ResearchV3Base4h._target_valid(None, 100., 1))
    return dict(status="passed", assertions=count)

```

## strategies/ResearchV2Core4h/__init__.py
SHA256: 577b84ebd15f27f5f598af5a4d1a3d3ed98313797656206c7691d29ad877564b

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

## strategies/ResearchV3Base4h/channel_features.py
SHA256: 3c49769786b7d6a50a11bfc4e063de54e4ffc92bdf4b08b60e48179469b78590

```python
import math

import numpy as np

from strategies.ResearchV3Base4h import closed_window
from strategies.ResearchV2Core4h import BAR


def features(candles, now, atr):
    """Channel excludes the signal bar; the two SMA120 windows end six bars apart."""
    rows = closed_window(candles, now, 126)
    if rows is None or atr is None:
        return dict(valid=False, direction=0, details=dict(quality="history_or_atr_invalid"))
    value = float(atr["value"])
    if not math.isfinite(value) or value <= 0:
        return dict(valid=False, direction=0, details=dict(quality="atr_invalid"))
    close = float(rows[-1, 2])
    high = float(np.max(rows[-21:-1, 3]))
    low = float(np.min(rows[-21:-1, 4]))
    mean = float(np.mean(rows[-120:, 2]))
    old_mean = float(np.mean(rows[-126:-6, 2]))
    breakout = 1 if close > high else -1 if close < low else 0
    trend_long = close > mean and mean > old_mean
    trend_short = close < mean and mean < old_mean
    direction = breakout if (breakout == 1 and trend_long) or (breakout == -1 and trend_short) else 0
    details = dict(first=int(rows[0, 0]), last=int(rows[-1, 0]), close=close,
                   high20=high, low20=low, sma120=mean, sma120_6=old_mean,
                   breakout=breakout, trend_long=bool(trend_long), trend_short=bool(trend_short))
    return dict(valid=True, direction=direction, details=details,
                reason="regime_reject" if breakout and not direction else "no_setup")


def post_entry_extremes(candles, now, entry_at, previous_high, previous_low):
    """Ignore pre-fill/partial bars; incomplete post-entry history never resets extremes."""
    # Entry is normally aligned. Ceil also excludes the partial bar of an off-grid fill.
    first_open = ((int(entry_at) + BAR - 1) // BAR) * BAR
    count = (int(now) - first_open) // BAR
    if count <= 0:
        return previous_high, previous_low
    rows = closed_window(candles, now, count)
    if rows is None or rows[0, 0] != first_open:
        return None
    return max(previous_high, float(np.max(rows[:, 3]))), min(previous_low, float(np.min(rows[:, 4])))


def trailing_level(direction, high_water, low_water, atr_value, old_stop, multiplier=3.):
    """ATR may expand, but the protection can only ratchet in the favorable direction."""
    if direction not in (-1, 1) or not all(math.isfinite(x) and x > 0 for x in
                                         (high_water, low_water, atr_value, old_stop, multiplier)):
        return None
    if high_water < low_water:
        return None
    return max(old_stop, high_water - multiplier * atr_value) if direction == 1 else min(
        old_stop, low_water + multiplier * atr_value)


def self_checks():
    checks = 0
    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Known channel 99..101; the signal's own new high/low must be excluded.
    rows = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(150)])
    now = 126 * BAR
    atr = dict(value=2.)
    for side in (-1, 1):
        changed = rows.copy()
        changed[125, 2] = 120. if side == 1 else 80.
        changed[125, 3:5] = [121., 79.]
        result = features(changed, now, atr)
        check(result["direction"] == side)
        check(result["details"]["high20"] == 101. and result["details"]["low20"] == 99.)
        expected = (119 * 100 + changed[125, 2]) / 120
        check(math.isclose(result["details"]["sma120"], expected, abs_tol=1e-12))
        check(result["details"]["sma120_6"] == 100.)
        # Prefix and future mutations must leave the complete result identical.
        prefix = changed[changed[:, 0] + BAR <= now]
        check(features(prefix, now, atr) == result)
        future = changed.copy()
        future[future[:, 0] + BAR > now, 1:5] = np.nan
        check(features(future, now, atr) == result)
        old = changed.copy()
        old[0, 2] = changed[125, 2]
        old[0, 3:5] = [121., 79.]
        tied = features(old, now, atr)
        check(tied["direction"] == 0 and tied["reason"] == "regime_reject")
        against = changed.copy()
        against[:6, 1:5] = [200., 200., 201., 199.] if side == 1 else [50., 50., 51., 49.]
        rejected = features(against, now, atr)
        check(rejected["direction"] == 0 and rejected["reason"] == "regime_reject")
    check(features(rows, now, atr)["direction"] == 0)
    check(not features(rows[:125], now, atr)["valid"])
    check(not features(rows, now + 60000, atr)["valid"])
    check(not features(rows, now, None)["valid"])
    check(not features(rows, now, dict(value=0.))["valid"])
    missing = np.delete(rows, 80, axis=0)
    check(not features(missing, now, atr)["valid"])
    duplicate = rows.copy()
    duplicate[80, 0] = duplicate[79, 0]
    check(not features(duplicate, now, atr)["valid"])
    for field, value in ((1, np.nan), (2, 0.), (3, 99.), (4, 102.)):
        invalid = rows.copy()
        invalid[80, field] = value
        check(not features(invalid, now, atr)["valid"])
    # Earlier history is outside both finite SMA windows and cannot change the signal.
    shifted = rows.copy()
    shifted[131, 2:5] = [120., 121., 99.]
    before = features(shifted, 132 * BAR, atr)
    shifted[0, 1] = np.nan
    check(features(shifted, 132 * BAR, atr) == before)
    # A breakout with positive SMA slope still fails when price is below the mean.
    level = rows.copy()
    level[:6, 1:5] = [50., 50., 51., 49.]
    level[6:105, 1:5] = [180., 180., 181., 179.]
    level[125, 2:5] = [120., 121., 99.]
    rejected = features(level, now, atr)
    check(rejected["details"]["breakout"] == 1 and rejected["details"]["sma120"] > 120.)
    check(rejected["details"]["sma120"] > rejected["details"]["sma120_6"] and rejected["direction"] == 0)
    # Exact equality to a previous channel boundary does not count as a breakout.
    boundary = rows.copy()
    boundary[125, 2] = 101.
    check(features(boundary, now, atr)["direction"] == 0)

    path = rows.copy()
    path[39, 3] = 1000.  # Before entry: including this high would cause a false ratchet.
    path[40, 3:5] = [111., 98.]
    path[41, 3:5] = [112., 97.]
    check(post_entry_extremes(path, 40 * BAR, 40 * BAR, 105., 105.) == (105., 105.))
    check(post_entry_extremes(path, 41 * BAR, 40 * BAR, 105., 105.) == (111., 98.))
    check(post_entry_extremes(path, 42 * BAR, 40 * BAR, 105., 105.) == (112., 97.))
    # A fill just after an open cannot use that partial bar.
    check(post_entry_extremes(path, 41 * BAR, 40 * BAR + 1, 105., 105.) == (105., 105.))
    check(post_entry_extremes(path, 42 * BAR, 40 * BAR + 1, 105., 105.) == (112., 97.))
    future = path.copy()
    future[42:, 3] = 1e9
    check(post_entry_extremes(future, 42 * BAR, 40 * BAR, 105., 105.) == (112., 97.))
    absent = np.delete(path, 40, axis=0)
    check(post_entry_extremes(absent, 42 * BAR, 40 * BAR, 105., 105.) is None)
    check(post_entry_extremes(path, 42 * BAR, 40 * BAR, 120., 90.) == (120., 90.))
    check(trailing_level(1, 111., 98., 2., 101.) == 105.)
    check(trailing_level(-1, 111., 97., 2., 109.) == 103.)
    check(trailing_level(1, 111., 98., 3., 105.) == 105.)
    check(trailing_level(-1, 111., 97., 3., 103.) == 103.)
    check(trailing_level(1, 111., 98., 2., 101.) >= 104.)
    check(trailing_level(-1, 111., 97., 2., 109.) <= 104.)
    check(trailing_level(1, 111., 98., float("nan"), 101.) is None)
    check(trailing_level(-1, 111., 97., 0., 109.) is None)
    return dict(status="passed", assertions=checks)

```

## strategies/ResearchV3ChannelP4h/__init__.py
SHA256: 16c4218be8adc458029363da17a3c3b8063bd465a7a9657cc0147f134dc50e56

```python
from strategies.ResearchV3Base4h import ResearchV3Base4h
from strategies.ResearchV3Base4h.channel_features import features as channel_features
from strategies.ResearchV3Base4h.channel_features import post_entry_extremes, trailing_level


class ResearchV3ChannelP4h(ResearchV3Base4h):
    LINE = "CHANNEL"
    TARGET_MODE = "none"
    MAX_HOLD_BARS = 42
    STOP_MULTIPLIER = 2.
    TRAIL_MULTIPLIER = 3.
    USE_OI = False

    def features(self, candles, now, atr):
        return channel_features(candles, now, atr)

    def on_v3_open(self):
        trade = self.vars["v3_trade"]
        self.vars["channel_trailing"] = dict(high=trade["entry_fill"], low=trade["entry_fill"],
                                             last_evaluated=trade["entry_at"])

    def _trailing_invalid(self, reason):
        # These are position-management events, separate from entry-opportunity quality.
        context = self.vars["context"]
        for side in ("all", "long" if self.is_long else "short"):
            bucket = self._bucket(context["month"], side)
            bucket["flags"]["trailing_data_invalid"] = bucket["flags"].get("trailing_data_invalid", 0) + 1
        self._log_json("V3_TRAILING_SKIPPED", dict(time=int(self.time), reason=reason))

    def manage_position(self, atr):
        trade = self.vars["v3_trade"]
        state = self.vars["channel_trailing"]
        now = int(self.time)
        if now <= state["last_evaluated"]:
            return
        state["last_evaluated"] = now
        extremes = post_entry_extremes(self.candles, now, trade["entry_at"], state["high"], state["low"])
        if extremes is None:
            self._trailing_invalid("post_entry_history_invalid")
            return
        state["high"], state["low"] = extremes
        if atr is None:
            self._trailing_invalid("atr_invalid")
            return
        direction = 1 if self.is_long else -1
        candidate = trailing_level(direction, state["high"], state["low"], atr["value"],
                                   trade["stop_price"], self.TRAIL_MULTIPLIER)
        if candidate is None:
            self._trailing_invalid("trailing_level_invalid")
            return
        if direction * (candidate - trade["stop_price"]) > 0:
            self._log_json("V3_TRAIL_CONTEXT", dict(time=now, high=state["high"], low=state["low"],
                atr=atr["value"], old_stop=trade["stop_price"], candidate=candidate))
            # Base handles a crossed new level with MARKET now; no retroactive stop fill.
            self.replace_stop(candidate)

```

## strategies/ResearchV3ChannelOi4h/__init__.py
SHA256: 09f11849d30af8f11c37fea43169c8652d6e8d8217760e45c5e1cf486497355e

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3ChannelOi4h(ResearchV3ChannelP4h):
    USE_OI = True

```

## strategies/ResearchV3ChannelSmoke4h/__init__.py
SHA256: d23a2c0fc054d1d5a5b9947caaa0856e3493e75729a37d73a9ad9e801d29b861

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h
from strategies.ResearchV3Base4h.channel_features import self_checks
from strategies.ResearchV3Base4h.base_checks import self_checks as base_checks


class ResearchV3ChannelSmoke4h(ResearchV3ChannelP4h):
    START = 1598918400000
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = self_checks()
            self._log_json("V3_SELF_CHECKS", self.vars["self_checks"])
            self.vars["base_checks"] = base_checks()
            self._log_json("V3_BASE_CHECKS", self.vars["base_checks"])
        super().before()

```

## strategies/ResearchV3Base4h/pullback_features.py
SHA256: 14abd2aedf9497bf3d4fd8cb2767211a1c9116e1a3db9b1859b0e90840804809

```python
import hashlib
import json
import math

import numpy as np

BAR = 14400000
HISTORY = 126


def features(candles, now, atr):
    """Three closed bars form the pattern; ATR controls risk only in the shared base."""
    rows = candles[candles[:, 0] + BAR <= now][-HISTORY:]
    if len(rows) != HISTORY or rows[-1, 0] != now - BAR:
        return dict(valid=False, direction=0, details=dict(reason="history_short"))
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return dict(valid=False, direction=0, details=dict(reason="history_gap"))
    prices = rows[:, 1:5]
    if not np.all(np.isfinite(rows[:, :5])) or np.any(prices <= 0):
        return dict(valid=False, direction=0, details=dict(reason="ohlc_invalid"))
    opens, closes, highs, lows = (rows[:, i] for i in (1, 2, 3, 4))
    if np.any(highs < np.maximum(opens, closes)) or np.any(lows > np.minimum(opens, closes)) or np.any(highs < lows):
        return dict(valid=False, direction=0, details=dict(reason="ohlc_invalid"))
    # Exact slices preserve each historical SMA's own closed-bar endpoint.
    fast = float(np.mean(closes[-20:]))
    fast_previous = float(np.mean(closes[-21:-1]))
    fast_older = float(np.mean(closes[-22:-2]))
    slow = float(np.mean(closes[-120:]))
    slow_previous_day = float(np.mean(closes[-126:-6]))
    if not np.all(np.isfinite([fast, fast_previous, fast_older, slow, slow_previous_day])):
        return dict(valid=False, direction=0, details=dict(reason="sma_invalid"))
    touch = bool(lows[-2] <= fast_previous <= highs[-2])
    long_regime = bool(closes[-1] > slow and slow > slow_previous_day)
    short_regime = bool(closes[-1] < slow and slow < slow_previous_day)
    long_pattern = bool(closes[-3] > fast_older and touch and closes[-1] > highs[-2] and closes[-1] > fast)
    short_pattern = bool(closes[-3] < fast_older and touch and closes[-1] < lows[-2] and closes[-1] < fast)
    go_long, go_short = long_regime and long_pattern, short_regime and short_pattern
    assert not (go_long and go_short)
    direction = 1 if go_long else -1 if go_short else 0
    # Window hash is the same canonical timestamp/OHLC format used for ATR provenance.
    window_hash = hashlib.sha256(json.dumps(rows[:, :5].tolist(), separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    result = dict(valid=True, direction=direction, details=dict(
        fast=fast, fast_previous=fast_previous, fast_older=fast_older,
        slow=slow, slow_previous_day=slow_previous_day, touch=touch,
        long_regime=long_regime, short_regime=short_regime,
        long_pattern=long_pattern, short_pattern=short_pattern,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), sha256=window_hash,
        pattern=rows[-3:, :5].tolist()))
    if direction == 0:
        result["reason"] = "regime_reject" if not (long_regime or short_regime) else "no_setup"
    return result


def self_checks():
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Linear closes make all SMA values independently calculable by arithmetic series.
    rows = np.array([[i * BAR, 100. + i, 100. + i, 101. + i, 99. + i, 1.] for i in range(126)])
    rows[-2, 4] = 213.
    rows[-1, 1:5] = [228., 228., 229., 227.]
    now = 126 * BAR
    result = features(rows, now, None)
    check(result["valid"] and result["direction"] == 1)
    expected = dict(fast=215.65, fast_previous=214.5, fast_older=213.5,
                    slow=165.525, slow_previous_day=159.5)
    for key, value in expected.items():
        check(math.isclose(result["details"][key], value, rel_tol=0, abs_tol=1e-12))
    check(result["details"]["first"] == 0 and result["details"]["last"] == now - BAR)

    # Reflection exchanges long/short while preserving the wick-touch geometry.
    mirror = rows.copy()
    mirror[:, 1] = 500 - rows[:, 1]
    mirror[:, 2] = 500 - rows[:, 2]
    mirror[:, 3] = 500 - rows[:, 4]
    mirror[:, 4] = 500 - rows[:, 3]
    check(features(mirror, now, None)["direction"] == -1)

    future = np.vstack([rows, [[now, 1e9, 1e9, 1e9, 1e9, 1.],
                             [now + BAR, 1e9, 1e9, 1e9, 1e9, 1.]]])
    check(features(future, now, None) == result)
    future[-2:, 1:5] = np.nan
    check(features(future, now, None) == result)
    older = np.vstack([[[-BAR, float("nan"), float("nan"), float("nan"), float("nan"), 1.]], rows])
    check(features(older, now, None) == result)

    changed_current = rows.copy()
    changed_current[-1, 1:5] = [100000., 100000., 100001., 99999.]
    changed = features(changed_current, now, None)
    for key in ("fast_previous", "fast_older", "slow_previous_day"):
        check(changed["details"][key] == result["details"][key])
    check(changed["details"]["fast"] != result["details"]["fast"])
    check(changed["details"]["slow"] != result["details"]["slow"])

    equal_touch = rows.copy()
    equal_touch[-2, 4] = expected["fast_previous"]
    check(features(equal_touch, now, None)["direction"] == 1)
    no_touch = rows.copy()
    no_touch[-2, 4] = 215.
    check(features(no_touch, now, None)["direction"] == 0)
    whole_below = rows.copy()
    whole_below[-2, 1:5] = [211., 211., 212., 210.]
    check(features(whole_below, now, None)["valid"])
    check(features(whole_below, now, None)["direction"] == 0)
    no_resumption = rows.copy()
    no_resumption[-1, 1:5] = [225., 225., 226., 224.]
    check(features(no_resumption, now, None)["direction"] == 0)
    flat = rows.copy()
    flat[:, 1:5] = [100., 100., 101., 99.]
    check(features(flat, now, None)["direction"] == 0)

    check(not features(rows[:125], now, None)["valid"])
    check(not features(np.delete(rows, 10, axis=0), now, None)["valid"])
    duplicate = rows.copy()
    duplicate[10, 0] = duplicate[9, 0]
    check(not features(duplicate, now, None)["valid"])
    check(not features(rows, now + 60000, None)["valid"])
    for field, value in ((1, float("nan")), (2, 0.), (3, 1.), (4, 1e6)):
        broken = rows.copy()
        broken[10, field] = value
        check(not features(broken, now, None)["valid"])
    # ATR does not gate the price signal; the shared base alone validates its risk input.
    check(features(rows, now, dict(value=9., first=0, last=now - BAR, bars=[])) == result)
    return dict(status="passed", assertions=checks)

```

## strategies/ResearchV3PullbackP4h/__init__.py
SHA256: ca3be20d7677ee9f73b0f4d38b57aacd10002426814ccacdef44caba54e87067

```python
from strategies.ResearchV3Base4h import ResearchV3Base4h
from strategies.ResearchV3Base4h.pullback_features import features as pullback_features


class ResearchV3PullbackP4h(ResearchV3Base4h):
    LINE = "PULLBACK"
    TARGET_MODE = "r_multiple"
    REWARD_MULTIPLE = 3.
    MAX_HOLD_BARS = 18
    STOP_MULTIPLIER = 2.
    USE_OI = False

    def features(self, candles, now, atr):
        return pullback_features(candles, now, atr)

```

## strategies/ResearchV3PullbackOi4h/__init__.py
SHA256: c35ca7985802ae54708166d8770f15e1b4c33e287776d3cde467d444d8aa744a

```python
from strategies.ResearchV3PullbackP4h import ResearchV3PullbackP4h


class ResearchV3PullbackOi4h(ResearchV3PullbackP4h):
    USE_OI = True

```

## strategies/ResearchV3PullbackSmoke4h/__init__.py
SHA256: 8bc7e51353fc953bbae7c1cf36c96b4716abd464d482325dbbb004b61798f942

```python
from strategies.ResearchV3PullbackP4h import ResearchV3PullbackP4h
from strategies.ResearchV3Base4h.pullback_features import self_checks
from strategies.ResearchV3Base4h.base_checks import self_checks as base_checks


class ResearchV3PullbackSmoke4h(ResearchV3PullbackP4h):
    START = 1598918400000
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["base_checks"] = base_checks()
            self._log_json("V3_BASE_CHECKS", self.vars["base_checks"])
            self.vars["self_checks"] = self_checks()
            self._log_json("V3_SELF_CHECKS", self.vars["self_checks"])
        super().before()

```

## strategies/ResearchV3Base4h/range_features.py
SHA256: 281583938ef90880f4fbbc05fee685245c4f173c7d9d122ebacb5615c64811d4

```python
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV3Base4h import BAR, closed_window

# Frozen RANGE design: two 120-close means separated by 24 four-hour bars.
WINDOW = 144
BAND_PERIOD = 20
SLOW_PERIOD = 120
SLOW_LAG = 24
Z_LIMIT = 2.
REGIME_LIMIT = .5


def _invalid(reason):
    return dict(valid=False, direction=0, mean_target=None, reason=reason,
                details=dict(reason=reason))


def features(candles, now, atr):
    """Fresh outward band crossing, admitted only when slow drift is small."""
    rows = closed_window(candles, now, WINDOW)
    if rows is None:
        return _invalid("history_invalid")
    if atr is None:
        return _invalid("atr_invalid")
    a = float(atr["value"])
    if not math.isfinite(a) or a <= 0:
        return _invalid("atr_invalid")
    closes = rows[:, 2]
    current, previous = closes[-BAND_PERIOD:], closes[-BAND_PERIOD - 1:-1]
    # Each band includes its own closed bar, not a later band's threshold.
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        mean, prior_mean = float(np.mean(current)), float(np.mean(previous))
        sigma, prior_sigma = float(np.std(current, ddof=0)), float(np.std(previous, ddof=0))
        slow = float(np.mean(closes[-SLOW_PERIOD:]))
        slow_lag = float(np.mean(closes[-WINDOW:-SLOW_LAG]))
    if not all(math.isfinite(v) for v in (mean, prior_mean, sigma, prior_sigma, slow, slow_lag)):
        return _invalid("statistics_nonfinite")
    if sigma <= 0 or prior_sigma <= 0:
        return _invalid("std_invalid")
    z, prior_z = (float(closes[-1]) - mean) / sigma, (float(closes[-2]) - prior_mean) / prior_sigma
    regime = abs(slow - slow_lag) / a
    if not all(math.isfinite(v) for v in (z, prior_z, regime)):
        return _invalid("statistics_nonfinite")
    passed = regime <= REGIME_LIMIT
    direction = 0
    if passed:
        if prior_z >= -Z_LIMIT and z < -Z_LIMIT:
            direction = 1
        elif prior_z <= Z_LIMIT and z > Z_LIMIT:
            direction = -1
    # Canonical OHLC hash preserves the complete 144-bar signal provenance.
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(), separators=(",", ":"),
                                      allow_nan=False).encode()).hexdigest()
    reason = "signal" if direction else "no_setup" if passed else "regime_reject"
    return dict(valid=True, direction=direction, mean_target=mean, reason=reason,
                details=dict(mean20=mean, std20=sigma, z=z, mean20_prev=prior_mean,
                             std20_prev=prior_sigma, z_prev=prior_z,
                             slow_mean=slow, slow_mean_lag24=slow_lag,
                             regime_ratio=regime, regime_passed=passed, atr=a,
                             first_open=int(rows[0, 0]), last_open=int(rows[-1, 0]),
                             bars=WINDOW, window_sha256=digest, reason=reason))


def _fixture(closes):
    """Synthetic OHLC encloses each chosen close; one-unit wicks keep it coherent."""
    return np.array([[i * BAR, c, c, c + 1., c - 1., 1.] for i, c in enumerate(closes)], dtype=float)


def self_checks():
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    base = [99.9 if i % 2 == 0 else 100.1 for i in range(160)]
    now = WINDOW * BAR
    atr = dict(value=2.)
    for direction, shock in ((1, 95.), (-1, 105.)):
        values = list(base)
        values[143] = shock
        rows = _fixture(values)
        result = features(rows, now, atr)
        # Hand-counted last20: ten 99.9, nine 100.1 and the shock.
        mean = (10 * 99.9 + 9 * 100.1 + shock) / 20
        variance = (10 * (99.9 - mean) ** 2 + 9 * (100.1 - mean) ** 2 + (shock - mean) ** 2) / 20
        check(result["valid"] and result["direction"] == direction)
        check(math.isclose(result["mean_target"], mean, abs_tol=1e-12))
        check(math.isclose(result["details"]["std20"], math.sqrt(variance), abs_tol=1e-12))
        check(math.isclose(result["details"]["mean20_prev"], 100., abs_tol=1e-12))
        check(math.isclose(result["details"]["z_prev"], -1., abs_tol=1e-10))
        check(math.isclose(result["details"]["slow_mean_lag24"], 100., abs_tol=1e-12))
        check(math.isclose(result["details"]["regime_ratio"], abs(shock - 100.1) / 120 / 2, abs_tol=1e-12))
        check(direction * (result["mean_target"] - shock) > 0)
        check(result["details"]["last_open"] + BAR == now)
        check(result["details"]["last_open"] - result["details"]["first_open"] == 143 * BAR)
        for cutoff in (144 * BAR, 145 * BAR, 150 * BAR):
            prefix = rows[rows[:, 0] + BAR <= cutoff]
            changed = rows.copy()
            changed[changed[:, 0] + BAR > cutoff, 1:5] = np.nan
            check(features(prefix, cutoff, atr) == features(rows, cutoff, atr))
            check(features(changed, cutoff, atr) == features(prefix, cutoff, atr))
        # An adverse volatility gate is a neutral valid signal, not invalid provider data.
        blocked = features(rows, now, dict(value=.001))
        check(blocked["valid"] and blocked["direction"] == 0 and blocked["reason"] == "regime_reject")
        # The target is the same past mean, irrespective of which ATR passed the gate.
        check(features(rows, now, dict(value=3.))["mean_target"] == result["mean_target"])

    trend = _fixture([100. + i for i in range(160)])
    boundary = features(trend, now, dict(value=48.))
    check(boundary["valid"] and boundary["details"]["regime_ratio"] == .5)
    check(boundary["details"]["regime_passed"])
    check(not features(trend, now, dict(value=47.9))["details"]["regime_passed"])

    persistent = list(base)
    persistent[142], persistent[143] = 95., 94.
    result = features(_fixture(persistent), now, atr)
    check(result["valid"] and result["details"]["z_prev"] < -2 and result["direction"] == 0)
    reentry = list(base)
    reentry[142], reentry[143] = 95., 100.
    check(features(_fixture(reentry), now, atr)["direction"] == 0)

    flat = _fixture([100.] * 160)
    check(features(flat, now, atr)["reason"] == "std_invalid")
    previous_flat = [100.] * 160
    previous_flat[143] = 95.
    check(features(_fixture(previous_flat), now, atr)["reason"] == "std_invalid")
    rows = _fixture(base)
    check(not features(rows[:143], now, atr)["valid"])
    check(not features(rows, now + 60000, atr)["valid"])
    check(not features(np.delete(rows, 20, axis=0), now, atr)["valid"])
    duplicate = rows.copy()
    duplicate[20, 0] = duplicate[19, 0]
    check(not features(duplicate, now, atr)["valid"])
    for field, value in ((1, float("nan")), (2, 0.), (3, 90.), (4, 110.)):
        invalid = rows.copy()
        invalid[20, field] = value
        check(not features(invalid, now, atr)["valid"])
    for a in (None, dict(value=0.), dict(value=-1.), dict(value=float("nan")), dict(value=float("inf"))):
        check(not features(rows, now, a)["valid"])
    check(features(rows, now, atr)["direction"] == 0)
    check(all(k not in features(rows, now, atr) for k in ("time", "line")))
    return dict(status="passed", assertions=checks)

```

## strategies/ResearchV3RangeP4h/__init__.py
SHA256: 85602799522849cd857a3f66ed6524d5560cbc27e26d14bef05fe59556de365d

```python
from strategies.ResearchV3Base4h import ResearchV3Base4h
from strategies.ResearchV3Base4h.range_features import features


class ResearchV3RangeP4h(ResearchV3Base4h):
    LINE = "RANGE"
    USE_OI = False
    TARGET_MODE = "frozen_mean"
    MAX_HOLD_BARS = 12
    STOP_MULTIPLIER = 2.

    def features(self, candles, now, atr):
        return features(candles, now, atr)

```

## strategies/ResearchV3RangeOi4h/__init__.py
SHA256: 4c6d9fa3691e61d77a732cc0519114dd82adaf541eeb9077aac4665b43869f6e

```python
from strategies.ResearchV3RangeP4h import ResearchV3RangeP4h


class ResearchV3RangeOi4h(ResearchV3RangeP4h):
    USE_OI = True

```

## strategies/ResearchV3RangeSmoke4h/__init__.py
SHA256: 4b09cb6dee8f86df95e9cdd35bfc6c202bf84a9f89a7418bf06e4791ccf8607d

```python
from strategies.ResearchV3RangeP4h import ResearchV3RangeP4h
from strategies.ResearchV3Base4h.range_features import self_checks
from strategies.ResearchV3Base4h.base_checks import self_checks as base_checks


class ResearchV3RangeSmoke4h(ResearchV3RangeP4h):
    START = 1598918400000
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["base_checks"] = base_checks()
            self._log_json("V3_BASE_CHECKS", self.vars["base_checks"])
            self.vars["self_checks"] = self_checks()
            self._log_json("V3_SELF_CHECKS", self.vars["self_checks"])
        super().before()

```
