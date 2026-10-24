# CROSS_P archivada — CODES acotado previo a implementación

Fecha local2026-10-22. Sólo documentación, padres inmutables. Nuevo presupuesto UN motor todavía no ejecutado. No CLOCK_ONLY. La receta archivada no equivale al contrato nuevo: este anexo conserva fuentes, helper y snapshot descriptivo sin volver a copiar cientos de miles de antecedentes.

## Fuentes originales exactas

### ResearchV5CrossP4h

SHA256 6e102adcf255761c49599d9aa7c37c39db5396d9eeb18f063927c88e174d6574. Fuente completa recibida por MCP.

```python
from strategies.ResearchV5Base4h import ResearchV5Base4h
from strategies.ResearchV5Base4h.cross_features import cross_state, features


class ResearchV5CrossP4h(ResearchV5Base4h):
    LINE = "CROSS"
    USE_OI = False
    FAST_PERIOD = 20
    SLOW_PERIOD = 80
    STOP_MULTIPLIER = 3.
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ATR_OFFSET_BARS = 0

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.FAST_PERIOD, self.SLOW_PERIOD)

    def manage_position(self, atr):
        # The core already prioritizes calendar/holding and post-fill timing.
        # This exit cross has no ATR/OI requirement and never schedules reversal.
        state = cross_state(self.candles, int(self.time), self.FAST_PERIOD, self.SLOW_PERIOD)
        if state["valid"] and ((self.is_long and state["direction"] == -1) or
                               (self.is_short and state["direction"] == 1)):
            self._log_json("V5_CROSS_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at),
                direction=1 if self.is_long else -1, **state["details"]))
            self.request_exit("opposite_cross")
```

### ResearchV5Base4h

SHA256 5e0124dbc86305cccfdbbd857ba158a2e7dc10c9fdf2a905f31cfc1dd59890aa. Fuente completa recibida por MCP.

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, ACCOUNTING_TOLERANCE,
)

# V5 4h decisions use explicit local clocks; only neutral V2 hooks are inherited.
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


def oi_context(history, now, lag_bars=0):
    target = now - lag_bars * BAR
    current = next((r for r in reversed(history) if r["time"] == target), None)
    reference = next((r for r in reversed(history) if r["time"] == target - DAY), None)
    result = dict(quality="initialization", passed=False, current=current, reference=reference)
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
        result["passed"] = bool(current["value"] > reference["value"])
    return result


def v5_entry_plan(price, capital, fee, direction, distance):
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


class ResearchV5Base4h(ResearchV2Core4h):
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
    ACTIVE_WINDOWS = None
    FORCE_BOUNDARIES = ()

    def features(self, candles, now, atr):
        raise NotImplementedError

    def on_v5_open(self):
        pass

    def manage_position(self, atr):
        pass

    def _log_json(self, label, payload):
        # Preserve inherited accounting labels while identifying this new hourly cycle.
        if label.startswith("V2_"):
            label = "V5_" + label[3:]
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
        oi = oi_context(history, now, self.OI_LAG_BARS)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.vars.get("v5_last_exit_at") != now and
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
        elif self.vars.get("v5_last_exit_at") == now:
            reason = "same_decision_exit"
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
            plan = v5_entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
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
        if not self.is_open or self.vars.get("v5_exit_requested_at") == int(self.time):
            return
        self.vars["v5_exit_requested_at"] = int(self.time)
        self.vars["exit_reason"] = reason
        self._log_json("V5_EXIT_REQUEST", dict(time=int(self.time), reason=reason))
        self.liquidate()

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"]
        stop = entry - direction * distance
        target = self._target(entry, direction, distance, context["features"])
        self.vars.pop("v5_exit_requested_at", None)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        self._log_json("V5_FEATURES", dict(time=int(self.time), line=self.LINE,
                                        **context["features"]))
        self._log_json("V5_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=distance, distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=stop, target=target, atr=dict(value=atr["value"], first=atr["first"], last=atr["last"],
                                             bars=15, offset_bars=self.ATR_OFFSET_BARS, sha256=digest), oi=context["oi"], funding=context["funding"]))
        self.vars["v5_trade"] = dict(entry_at=int(self.position.opened_at), entry_atr=atr["value"],
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
        self.on_v5_open()

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
        self.vars["v5_last_exit_at"] = int(closed_trade.closed_at)
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V5_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            assert value["bars"] == sum(value.get("feature_reasons", {}).values())
            self._log_json("V5_AUDIT", dict(key=key, **value))
        self._log_json("V5_PROVENANCE", dict(line=self.LINE, use_oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, stop_multiplier=self.STOP_MULTIPLIER,
            bar_ms=BAR, oi_reference_bars=OI_REFERENCE_BARS,
            atr_offset_bars=self.ATR_OFFSET_BARS, target_mode=self.TARGET_MODE,
            reward_multiple=self.REWARD_MULTIPLE, max_hold_bars=self.MAX_HOLD_BARS,
            start=self.START, finish=self.FINISH, active_windows=self.ACTIVE_WINDOWS,
            force_boundaries=self.FORCE_BOUNDARIES, final_exit_may_follow=True,
            self_checks=self.vars.get("self_checks")))
```

### cross_features.py

SHA256 5df66fdb107fe3f16484ee5cd1ca91c121c4c8bea0095e3fd95799a354f5e1e0. Fuente completa recibida por MCP.

```python
"""Finite four-hour SMA crosses; no state, engine IO, ATR or OI in exit signals."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV5Base4h import BAR, closed_window


def _periods_valid(fast_period, slow_period):
    return (isinstance(fast_period, int) and not isinstance(fast_period, bool) and
            isinstance(slow_period, int) and not isinstance(slow_period, bool) and
            0 < fast_period < slow_period)


def _mean(values):
    # Scale before summation: a finite mean need not have a representable raw sum.
    value = math.fsum(float(x) / len(values) for x in values)
    return value if math.isfinite(value) else None


def _direction(fast_now, fast_previous, slow_now, slow_previous):
    """Equality is allowed on the prior bar, never on the current bar."""
    if fast_previous <= slow_previous and fast_now > slow_now:
        return 1
    if fast_previous >= slow_previous and fast_now < slow_now:
        return -1
    return 0


def cross_state(candles, now, fast_period=20, slow_period=80):
    """ATR-independent entry/exit cross; each average has its own finite window."""
    if not _periods_valid(fast_period, slow_period):
        return dict(valid=False, direction=0, reason="periods_invalid",
                    details=dict(reason="periods_invalid"))
    rows = closed_window(candles, now, slow_period + 1)
    if rows is None:
        return dict(valid=False, direction=0, reason="window_invalid",
                    details=dict(reason="window_invalid"))
    closes = rows[:, 2]
    try:
        fast_now = _mean(closes[-fast_period:])
        fast_previous = _mean(closes[-fast_period-1:-1])
        slow_now = _mean(closes[-slow_period:])
        slow_previous = _mean(closes[:-1])
    except (OverflowError, ValueError):
        # Invalid arithmetic blocks a signal; it is never converted to a trend.
        fast_now = fast_previous = slow_now = slow_previous = None
    if any(x is None for x in (fast_now, fast_previous, slow_now, slow_previous)):
        return dict(valid=False, direction=0, reason="mean_invalid",
                    details=dict(reason="mean_invalid"))
    direction = _direction(fast_now, fast_previous, slow_now, slow_previous)
    reason = "setup" if direction else "no_setup"
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(reason=reason, fast_period=fast_period, slow_period=slow_period,
        fast_now=fast_now, fast_previous=fast_previous,
        slow_now=slow_now, slow_previous=slow_previous,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=slow_period + 1,
        bar_ms=BAR, sha256=digest)
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def features(candles, now, atr, fast_period=20, slow_period=80):
    result = cross_state(candles, now, fast_period, slow_period)
    if not result["valid"]:
        return result
    value = atr.get("value") if isinstance(atr, dict) else None
    if (isinstance(value, bool) or not isinstance(value, (int, float, np.integer, np.floating)) or
            not math.isfinite(value) or value <= 0):
        # This check belongs only to new exposure. Exit crosses remain usable.
        return dict(valid=False, direction=0, reason="atr_invalid",
                    details=dict(reason="atr_invalid"))
    return result


def self_checks():
    """Deterministic algebra, sign symmetry and window/future independence; no IO."""
    count = 0

    def check(value):
        nonlocal count
        assert bool(value)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes)) * BAR + first,
            closes, closes, closes + .01, closes - .01, np.ones(len(closes))))

    def reflection(rows):
        result = rows.copy()
        result[:, 1] = 400. - rows[:, 1]
        result[:, 2] = 400. - rows[:, 2]
        result[:, 3] = 400. - rows[:, 4]
        result[:, 4] = 400. - rows[:, 3]
        return result

    atr = dict(value=2.)
    for fast_period, slow_period in ((20, 80), (18, 72), (22, 88)):
        # Flat long history, twenty (or neighboring count) weak closes, then a
        # positive close: the current fast/slow cross is fresh, not a state entry.
        prices = [100.] * (slow_period - fast_period) + [99.] * fast_period + [130.]
        rows = candles(prices)
        now = len(rows) * BAR
        original = rows.copy()
        for data, side in ((rows, 1), (reflection(rows), -1)):
            state = cross_state(data, now, fast_period, slow_period)
            result = features(data, now, atr, fast_period, slow_period)
            check(state["valid"])
            check(state["direction"] == side)
            check(result == state)
            detail = state["details"]
            check(detail["bars"] == slow_period + 1)
            check(detail["last"] + BAR == now)
            check(detail["last"] - detail["first"] == slow_period * BAR)
            for key, values in (("fast_now", data[-fast_period:, 2]),
                                ("fast_previous", data[-fast_period-1:-1, 2]),
                                ("slow_now", data[-slow_period:, 2]),
                                ("slow_previous", data[:-1, 2])):
                check(abs(detail[key] - sum(float(x) for x in values) / len(values)) < 1e-12)
            check(len(json.dumps(result, allow_nan=False)) < 1700)
            future = np.vstack((data, candles([150., 151.], first=now)))
            check(cross_state(future, now, fast_period, slow_period) == state)
            future[-2:, 1:5] *= 10.
            check(cross_state(future, now, fast_period, slow_period) == state)
            prefix = candles([90.] * 10, first=-10 * BAR)
            extended = np.vstack((prefix, data))
            check(cross_state(extended, now, fast_period, slow_period) == state)
            extended[:10, 1:5] *= 2.
            check(cross_state(extended, now, fast_period, slow_period) == state)
            prior = cross_state(extended[:-1], now - BAR, fast_period, slow_period)
            check(prior["valid"])
            check(abs(prior["details"]["fast_now"] - detail["fast_previous"]) < 1e-12)
            check(abs(prior["details"]["slow_now"] - detail["slow_previous"]) < 1e-12)
            check(cross_state(data[:-1], now, fast_period, slow_period)["valid"] is False)
            check(cross_state(data, now + 1, fast_period, slow_period)["valid"] is False)
            # ATR can prevent an entry, never the independently evaluated exit.
            check(features(data, now, None, fast_period, slow_period)["valid"] is False)
            check(cross_state(data, now, fast_period, slow_period) == state)
        check(np.array_equal(rows, original))
        flat = candles([100.] * (slow_period + 1))
        flat_state = cross_state(flat, now, fast_period, slow_period)
        check(flat_state["valid"] and flat_state["direction"] == 0)
        rising = candles(100. + np.arange(slow_period + 1))
        falling = reflection(rising)
        check(cross_state(rising, now, fast_period, slow_period)["direction"] == 0)
        check(cross_state(falling, now, fast_period, slow_period)["direction"] == 0)
    check(_direction(2., 1., 1., 1.) == 1)
    check(_direction(1., 2., 2., 2.) == -1)
    check(_direction(1., 0., 1., 1.) == 0)
    check(_direction(1., 2., 1., 1.) == 0)
    check(_direction(2., 2., 1., 1.) == 0)
    check(_direction(1., 1., 2., 2.) == 0)
    nominal = candles([100.] * 60 + [99.] * 20 + [130.])
    now = 81 * BAR
    detail = cross_state(nominal, now)["details"]
    check(abs(detail["fast_previous"] - 99.) < 1e-12)
    check(abs(detail["slow_previous"] - 99.75) < 1e-12)
    check(abs(detail["fast_now"] - 100.55) < 1e-12)
    check(abs(detail["slow_now"] - 100.125) < 1e-12)
    for value in (None, 0., -1., True, float("nan"), float("inf")):
        check(features(nominal, now, dict(value=value))["valid"] is False)
    for fast_period, slow_period in ((0, 80), (20, 20), (80, 20), (20., 80), (True, 80)):
        check(cross_state(nominal, now, fast_period, slow_period)["valid"] is False)
    for column, value in ((2, float("nan")), (2, float("inf")), (3, 1.), (4, 1000.), (1, 0.)):
        broken = nominal.copy()
        broken[-1, column] = value
        check(cross_state(broken, now)["valid"] is False)
        check(features(broken, now, atr)["valid"] is False)
    broken = nominal.copy()
    broken[-10, 0] -= BAR
    check(cross_state(broken, now)["valid"] is False)
    check(cross_state(nominal[-80:], now)["valid"] is False)
    # The raw sum would overflow; scaled finite arithmetic must remain JSON-safe.
    huge = np.tile([0., 1e308, 1e308, 1e308, 1e308, 1.], (81, 1))
    huge[:, 0] = np.arange(81) * BAR
    large_state = cross_state(huge, now)
    check(large_state["valid"])
    check(large_state["direction"] == 0)
    check(len(json.dumps(large_state, allow_nan=False)) < 1700)
    return dict(status="passed", assertions=count)
```

## Sizing actual reutilizable, extracto exacto

Fuente completa padre BtcResearchR16LegacyBase1m SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542, leída íntegra; se conserva únicamente helper que será reutilizado, no señales/gestión K. Constantes exactas RESERVE=.001 y LOT=.001. Extracto NO equivale a snapshot entero del padre; no se editará.

```python
RESERVE = .001
LOT = .001

def legacy_plan(event, capital, margin, leverage, fee):
    """BTC100%; preserve reserve/lot, with the common 90%-margin fee buffer."""
    entry, distance, direction = event["entry"], event["distance"], event["direction"]
    stop = entry-direction*distance
    if (direction not in (-1, 1)
            or not all(math.isfinite(v) and v > 0 for v in
                       (entry, distance, stop, capital, margin, leverage))
            or not math.isfinite(fee) or fee < 0):
        return None
    unit = distance+fee*(entry+stop)+RESERVE*entry
    budget = .02*capital
    risk_qty = budget/unit
    gross_qty = 4.4*capital/entry  # Legacy ceiling; 3x margin prevents 4.4x exposure.
    margin_qty = .90*margin*leverage/(entry*(1+fee*leverage))
    qty = math.floor(min(risk_qty, gross_qty, margin_qty)/LOT)*LOT
    if qty <= 0:
        return None
    assert qty*unit <= budget+1e-6
    return dict(event, qty=qty, risk_budget=budget, planned_loss=qty*unit,
                planned_stop_fees=qty*(distance+fee*(entry+stop)),
                margin_limited=margin_qty < risk_qty,
                gross_limited=gross_qty < risk_qty,
                reserve=RESERVE)

```

## Observador R11 congelado completo

SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87. Nueva fuente aislada debe heredarlo, no modificarlo; una llamada por fase.

```python
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cusum_step(rows, accumulators):
    """Transfer the R40 design:60 past log returns, drift0.25, boundary4."""
    returns = np.diff(np.log(rows[-62:, 2]))
    sigma = float(np.std(returns[:-1], ddof=1))
    if not math.isfinite(sigma) or sigma <= 0:
        return 0, (0.0, 0.0)
    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)
    if not math.isfinite(z):
        return 0, (0.0, 0.0)
    up = max(0.0, accumulators[0] + z - 0.25)
    down = max(0.0, accumulators[1] - z - 0.25)
    if up >= 4 or down >= 4:
        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1
        return direction, (0.0, 0.0)
    return 0, (up, down)


def absorption_signal(rows):
    """Large volume but small body, followed by escape of that closed bar."""
    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]
    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):
        return 0
    average_volume = float(np.mean(window[:, 5]))
    prior_atr = atr14(window)
    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:
        return 0
    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:
        return 0
    if confirmation[2] > setup[3]:
        return 1
    if confirmation[2] < setup[4]:
        return -1
    return 0


def month_name(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime("%Y-%m")


def monthly_summary(boundaries, active_months):
    """Declared post-settlement/pre-decision UTC cuts; no00:01 approximation."""
    points = sorted(boundaries.items())
    months = []
    for (start, before), (finish, after) in zip(points, points[1:]):
        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)
        month = stamp.strftime("%Y-%m")
        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0
        if before <= 0:
            continue
        months.append(dict(month=month, start=start, finish=finish,
                           complete=complete, active=month in active_months,
                           pnl=after-before, return_fraction=after/before-1))
    complete = [m for m in months if m["complete"]]
    active = [m for m in complete if m["active"]]
    quarter_groups = {}
    for m in months:
        quarter = m["month"][:4] + "Q" + str((int(m["month"][5:])-1)//3+1)
        quarter_groups.setdefault(quarter, []).append(m)
    quarters = [q for q in quarter_groups.values()
                if len(q) == 3 and all(m["complete"] for m in q)]
    returns = [m["return_fraction"] for m in complete]
    contributions = sorted([m["pnl"] for m in months], reverse=True)
    return dict(months=months, complete_months=len(complete), active_months=len(active),
                positive_active=sum(m["pnl"] > 0 for m in active),
                positive_calendar=sum(m["pnl"] > 0 for m in complete),
                median_return=float(np.median(returns)) if returns else None,
                complete_quarters=len(quarters),
                positive_quarters=sum(sum(m["pnl"] for m in q) > 0 for q in quarters),
                pnl_without_best_two=sum(m["pnl"] for m in months)-sum(contributions[:2]))


class BtcResearchR11Base1m(Strategy):
    """M1 accounting observer; signal and management decisions remain4h."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, payload):
        # Event logs stay small; monthly history is emitted as separate rows.
        self.log(label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False))

    def _observe(self, stage):
        now = int(self.time)
        # BTC-only futures equity. portfolio_value multiplies open PnL by
        # leverage in this checkout, so it is deliberately not used here.
        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)
        assert math.isfinite(equity)
        self.vars["peak"] = max(self.vars.get("peak", 10000.0), equity)
        drawdown = equity / self.vars["peak"] - 1
        self.vars["dd"] = min(self.vars.get("dd", 0.0), drawdown)
        self.vars["sequence"] = self.vars.get("sequence", 0) + 1
        self.vars["last_equity"] = equity
        active = self.vars.setdefault("active_months", set())
        if self.is_open:
            # Pre marks describe exposure during the minute that just closed;
            # an opening fill at T instead belongs to the new interval.
            active.add(month_name(now if stage == "open" else now-1))
        boundaries = self.vars.setdefault("boundaries", {self.START: 10000.0})
        if stage == "pre":
            self.vars["minute_marks"] = self.vars.get("minute_marks", 0) + 1
            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)
            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:
                boundaries[now] = equity
        if now >= self.FINISH:
            # A later terminal close callback replaces the mark with post-fee equity.
            boundaries[self.FINISH] = equity
        return equity

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        # This is signal alignment, not a market-session/calendar filter.
        if now % BAR != 0:
            return
        count = 62 if self.MODE == "CUSUM" else 26
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, count)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self.vars["cusum"] = (0.0, 0.0)
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        if self.MODE == "CUSUM":
            direction, state = cusum_step(rows, self.vars.get("cusum", (0.0, 0.0)))
            self.vars["cusum"] = state
        else:
            assert self.MODE == "ABSORPTION"
            direction = absorption_signal(rows)
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware
        # plan, eight-decimal research precision and90% margin ceiling.
        capital = max(0.0, float(self.balance))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or self.price + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        self.buy = self.vars["plan"]["qty"], self.price

    def go_short(self):
        self.sell = self.vars["plan"]["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        stop = entry - direction * plan["distance"]
        target = entry + direction * 2 * plan["distance"]
        assert qty * (plan["distance"] + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._observe("open")

    def update_position(self):
        # Preserve the four-hour management clock despite the M1 observer.
        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        now = int(self.time)
        active = self.vars.setdefault("active_months", set())
        active.add(month_name(now-1))
        # At a month boundary, retain both the held interval and any fee-only
        # execution month. Terminal liquidation belongs to the final interval.
        if now < self.FINISH:
            active.add(month_name(now))
        self.vars["last_exit_at"] = now
        self._observe("close")
        if now >= self.FINISH and self.vars.get("emitted"):
            self._emit("FINAL")

    def _emit(self, stage):
        summary = monthly_summary(self.vars["boundaries"], self.vars.get("active_months", set()))
        # Emit rows at the end, so one bounded log page can retrieve all months.
        for item in summary.pop("months"):
            self._log("R11_MONTH", dict(stage=stage, **item))
        summary.update(stage=stage, equity=self.vars["last_equity"],
                       dd_m1_events=self.vars.get("dd", 0),
                       minute_marks=self.vars.get("minute_marks", 0),
                       sequence=self.vars.get("sequence", 0),
                       signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
                       invalid_windows=self.vars.get("invalid_windows", 0))
        self._log("R11_SUMMARY", summary)

    def before_terminate(self):
        self._observe("terminal")
        self.vars["emitted"] = True
        self._emit("PRETERMINAL")
```

## Dependencias transitivas y contrato

ResearchV5Base4h importa ResearchV2Core4h sólo para la clase histórica. Hash padre leído completo 577b84ebd15f27f5f598af5a4d1a3d3ed98313797656206c7691d29ad877564b. No instanciar esa estrategia ni heredar accesoOI/ventanasWF en la adaptación. Helpers puros cross_state/atr_window conservan sus dependencias originales. R11 importa R10Base4h; hash congelado conocido2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9. No se mutan R10/R11/R16/R32/V5.

Única receta actual: SMA20/80 fresca,3ATRsimple,sinTP/BE/trailing,cruceopuesto y máximo180BAR720h/cuotaUTC porfill/no reverse. Helper .5wallet/.5margin, lote.001/reserva.001; cap1x adicional del margen TOTAL preorden conservado: qcap=floor(Ctotal/entry/LOT)*LOT; qfinal=min(qhelper,qcap), recalcular planned_loss/stopfees para qfinal. No vecino de exposición ni duplicación automática de cap/ riesgo.

R34 logs neutrales PLAN/OPEN/CLOSE/SUMMARY según protocolo, todos<1800caracteres. Nueva base aisladaR11 requerida porque R32 sólo64filas/2ATR/24–48h; no cambiarla para acomodar CROSS. Nombre definitivo de fuente pendiente de aprobación/root; no se crea aquí.

## Snapshot nativo del control archivado

Summary íntegro también guardado separadamente en BTC_CROSS_ARCHIVE_CONTROL_SUMMARY_20261022.json. Fuente descriptiva, no control pareado ni nueva consulta de trades/precios/candles.

```json
{
  "action": "get_session_results",
  "status": "success",
  "session_type": "backtest",
  "session_id": "50827027-6d6f-4c5d-8c23-5f2f91d7d971",
  "session_status": "finished",
  "title": "MCP Backtest: V5 SCREEN CROSS_P",
  "description": "Preregistered V5 screening; fixed rules, costs and datasets; no tuning. Waiting root motor token.",
  "description_truncated": false,
  "created_at": 1792544275000,
  "updated_at": 1792544467000,
  "execution_duration": 37.49,
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "ResearchV5CrossP4h"
      }
    ],
    "data_routes": [],
    "start_date": "2020-09-01",
    "finish_date": "2024-01-01",
    "debug_mode": true,
    "export_csv": false,
    "export_json": false,
    "export_chart": false,
    "fast_mode": true,
    "benchmark": false,
    "config": {
      "logging": {
        "order_submission": false,
        "order_cancellation": false,
        "order_execution": false,
        "position_opened": false,
        "position_increased": false,
        "position_reduced": false,
        "position_closed": false,
        "shorter_period_candles": false,
        "trading_candles": false,
        "balance_update": false
      },
      "warm_up_candles": 240,
      "exchange": {
        "name": "Binance Perpetual Futures",
        "type": "futures",
        "balance": 10000,
        "fee": 0.00045,
        "futures_leverage_mode": "isolated",
        "futures_leverage": 3,
        "slippage_bps": 0
      },
      "funding": {
        "mode": "historical",
        "dataset_id": "9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571"
      },
      "open_interest": {
        "mode": "historical",
        "dataset_id": "6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf",
        "allow_missing_observations": true,
        "max_age_ms": 600000
      }
    }
  },
  "metrics": {
    "total": 77,
    "total_winning_trades": 22,
    "total_losing_trades": 55,
    "starting_balance": 10000,
    "finishing_balance": 19052.918199267067,
    "win_rate": 0.2857142857142857,
    "win_rate_longs": 0.23529411764705882,
    "win_rate_shorts": 0.32558139534883723,
    "ratio_avg_win_loss": 4.279534271863092,
    "longs_count": 34,
    "longs_percentage": 44.15584415584416,
    "shorts_percentage": 55.84415584415584,
    "shorts_count": 43,
    "fee": 431.11912034662885,
    "net_profit": 9052.918199267087,
    "net_profit_percentage": 90.52918199267087,
    "average_win": 989.5917535765547,
    "average_loss": 231.23818871667467,
    "expectancy": 117.57036622424795,
    "expectancy_percentage": 1.1757036622424795,
    "expected_net_profit_every_100_trades": 117.57036622424795,
    "average_holding_period": 804642.077922078,
    "average_winning_holding_period": 1684145.4545454546,
    "average_losing_holding_period": 452840.7272727273,
    "gross_profit": 21771.0185786842,
    "gross_loss": -12718.100379417107,
    "max_drawdown": -17.695540126860376,
    "max_underwater_period": 523,
    "annual_return": 21.329231458266907,
    "annualization": 365,
    "sharpe_ratio": 1.0386898252303687,
    "calmar_ratio": 1.2053450363965372,
    "sortino_ratio": 1.738723018832068,
    "omega_ratio": 1.2383869149752904,
    "serenity_index": null,
    "total_open_trades": 1,
    "open_pl": 63.88712848900104,
    "winning_streak": 3,
    "losing_streak": 7,
    "largest_losing_trade": -398.7765502430101,
    "largest_winning_trade": 5032.155430745771,
    "current_streak": 1,
    "avg_trades_per_day": 0.06327030079070757,
    "avg_trades_per_week": 0.442892105534953,
    "avg_trades_per_month": 1.9259479560691386,
    "funding": {
      "mode": "historical",
      "dataset_id": "9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571",
      "cashflow": -759.7452673639507,
      "rate_kind": "settled",
      "event_count": 2140,
      "settlements_processed": 3651,
      "mark_price_proxy_count": 2061,
      "status": "applied",
      "applied": true,
      "scope": [
        "BTC-USDT"
      ],
      "excluded_symbols": [],
      "data": {
        "allow_mark_price_proxy": true,
        "exchange": "Binance Perpetual Futures",
        "finish": 1767225600000,
        "mark_price_proxy_count": 4198,
        "schema": 1,
        "source": "binance-usdm-fundingRate-v1",
        "start": 1577836800000,
        "symbol": "BTC-USDT",
        "dataset_id": "9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571",
        "event_count": 6576,
        "first_settlement": 1577836800000,
        "last_settlement": 1767196800001,
        "largest_gap_ms": 28800047,
        "status": "ready",
        "coverage_complete": true,
        "supported_timestamps": true,
        "coverage_policy": "vendor_response; BTC maximum eight-hour gap with one-second boundary jitter",
        "timestamp_policy": "minute boundary; vendor jitter <=1000ms retained in raw settled_at",
        "publication_delay_ms": 60000,
        "rate_unit": "decimal_fraction",
        "mark_price_source": "mixed; settlement marks + explicit markPriceKlines.1h_open_proxy"
      },
      "effective_fast_mode": false,
      "boundary_policy": "before_strategy_decisions; finish_exclusive",
      "publication_delay_ms": 60000
    },
    "open_interest": {
      "mode": "historical",
      "dataset_id": "6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf",
      "max_age_ms": 600000,
      "applied": true,
      "status": "applied",
      "scope": [
        "BTC-USDT"
      ],
      "data": {
        "archive_assumptions_acknowledged": true,
        "archive_catalog": {
          "first_archive_date": "2020-09-01",
          "first_archive_last_modified": "2026-03-18T12:30:27.000Z",
          "first_archive_url": "https://data.binance.vision/data/futures/um/daily/metrics/BTCUSDT/BTCUSDT-metrics-2020-09-01.zip",
          "point_in_time_certified": false,
          "source": "binance-usdm-metrics-archive-v1"
        },
        "availability_lag_ms": 360000,
        "exchange": "Binance Perpetual Futures",
        "finish": 1767225600000,
        "import_source": "auto",
        "original_publication_known": false,
        "period_ms": 300000,
        "rest_range": null,
        "schema": 1,
        "source": "binance-usdm-metrics-archive-v1",
        "start": 1598918400000,
        "symbol": "BTC-USDT",
        "dataset_id": "6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf",
        "observation_count": 560390,
        "expected_observation_count": 561024,
        "missing_observation_count": 634,
        "coverage_complete": false,
        "status": "incomplete",
        "leading_gap_ms": 0,
        "trailing_gap_ms": 0,
        "first_observation": 1598918400000,
        "last_observation": 1767225300000,
        "first_available_at": 1598918760000,
        "last_available_at": 1767225660000,
        "largest_gap_ms": 37800000,
        "gap_count": 156,
        "availability_policy": "retrospective_archive_period_label_plus_6m_assumption; original_publication_unknown",
        "history_limit": "Official daily metrics archive; earliest verified listing 2020-09-01",
        "point_in_time_certified": false,
        "missing_policy": "no interpolation; unavailable or stale values return None",
        "cashflow": false,
        "archive_file_count": 1948,
        "archive_verified_file_count": 1948,
        "archive_missing_days": [],
        "archive_missing_day_count": 0,
        "archive_identical_duplicate_rows": 75255
      },
      "allow_missing_observations": true,
      "observation_count": 560390,
      "cashflow": false,
      "availability_lag_ms": 360000,
      "availability_policy": "retrospective_archive_period_label_plus_6m_assumption; original_publication_unknown",
      "current": {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "observed_at": 1704066600000,
        "available_at": 1704066960000,
        "quantity_base": 73951.1,
        "value_quote": 3128205481.1
      }
    }
  },
  "error": null,
  "has_chart_data": false,
  "has_charts_image": true,
  "sections": {
    "trades": {
      "count": 77
    },
    "equity_curve": {
      "series": [
        {
          "name": "Portfolio",
          "points": 1218
        }
      ]
    },
    "hyperparameters": {
      "count": 0
    },
    "logs": {
      "log_size_bytes": 321898
    }
  },
  "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
  "dashboard_url": "http://localhost:9200/#/backtest/50827027-6d6f-4c5d-8c23-5f2f91d7d971"
}
```

## Evidencia documental y alcance de lectura

Leídos completos: V5_CROSS_PROPOSAL.md, RESEARCH_PROTOCOL_V5_20261020.md, V5_CROSS_SCREEN_REPORT.md, FROZEN_SHORTLIST_V5.md, card RESEARCH_HUB/revisions/20261021-r2/cards/CROSS_P.json y cierre FINAL_DECISION_V5.md ya conservado previamente. Confirman elegible pero fuera de cupo, no confirmada2024–25. REGISTRY_V5.json lectura dirigida primera página2000líneas, configuración/hashes y registro de screen50827027; no claim de lectura íntegra179k ni auditoría porfill. Current Hubr33 leída completa.

V5screen2020Sep→2024Jan/cap1x/riesgo2%/floor8/sinreserva no equivale a replay actual2020Oct→2026Jan/cuota1%/legacyhalf/lote.001/reserva.001/R11M1. Funding ya estabaON, mismo snapshot9c5618... La nueva historia sigue adaptativa, noOOS ni WF. No reducir gatesr9 o modificar clocks/parametría para crear elegibilidad.

No nuevos precios/datasets/imports, análisis/jobs/drafts/motores o estrategias. Las fuentes y código sintético se prepararán sólo tras revisión de protocolo y este anexo. El recibo del control viejo no acredita paridad del runtime de la fuente nueva antes de auditarla.
