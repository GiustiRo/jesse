import hashlib
import json
import math

import numpy as np

from strategies.ResearchV4Base1h import BAR, closed_window


def _number(value):
    # Reject bool/string coercions and sanitize nonfinite data before JSON evidence.
    if isinstance(value, (bool, str)) or not isinstance(value, (int, float, np.integer, np.floating)):
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def _timestamp(value):
    number = _number(value)
    return int(number) if number is not None and number >= 0 and number == int(number) else None


def canonical_window(history):
    """Bounded evidence contains only identity, publication and decimal rate."""
    rows = history if isinstance(history, (list, tuple)) else []
    result = []
    for row in rows[-32:]:
        row = row if isinstance(row, dict) else {}
        result.append([_timestamp(row.get("settled_at")),
                       _timestamp(row.get("available_at")), _number(row.get("rate_decimal"))])
    return result


def window_hash(window):
    return hashlib.sha256(json.dumps(window, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def reset_signal(previous, current, baseline, extreme_z=1., reset_z=.5):
    """Both events share the strictly preceding baseline; constant history has sigma zero."""
    if len(baseline) != 30 or not all(math.isfinite(x) for x in baseline):
        return dict(direction=0, reason="funding_baseline_invalid")
    try:
        mean = math.fsum(x / 30 for x in baseline)
        # Constant positive rates may have a tiny floating residual: detect equality directly.
        sigma = 0. if max(baseline) == min(baseline) else math.sqrt(math.fsum((x - mean) ** 2 / 30 for x in baseline))
    except (OverflowError, ValueError):
        return dict(direction=0, reason="funding_baseline_invalid")
    if not math.isfinite(sigma) or sigma <= 0:
        return dict(direction=0, reason="funding_sigma_zero", baseline=mean, sigma=sigma if math.isfinite(sigma) else None)
    zprev, znow = (previous - mean) / sigma, (current - mean) / sigma
    if not all(math.isfinite(x) for x in (zprev, znow)):
        return dict(direction=0, reason="funding_z_invalid", baseline=mean, sigma=sigma)
    direction = 1 if zprev >= extreme_z and 0 <= znow <= reset_z else -1 if zprev <= -extreme_z and -reset_z <= znow <= 0 else 0
    return dict(direction=direction, reason="funding_reset" if direction else "funding_no_reset",
                baseline=mean, sigma=sigma, zprev=zprev, znow=znow)


def ma24_state(candles, now):
    """A state exit needs only 24 closed prices, independent of entry warmup."""
    rows = closed_window(candles, now, 24)
    if rows is None:
        return None
    # Finite individual OHLC can still overflow an aggregate; never emit Infinity.
    with np.errstate(over="ignore", invalid="ignore"):
        close, average = float(rows[-1, 2]), float(np.mean(rows[:, 2]))
    if not all(math.isfinite(value) for value in (close, average)):
        return None
    return dict(close=close, sma24=average)


def features(candles, now, atr, history32, current_rate, current_timestamp,
             last_seen, extreme_z=1., reset_z=.5):
    """Pure event evaluation. next_seen consumes new events even when a gate rejects."""
    window = canonical_window(history32)
    event = _timestamp(current_timestamp)
    result = dict(valid=True, direction=0, reason="funding_repeated", details={},
                  next_seen=last_seen, event_new=False,
                  event=dict(settled_at=event, window=window, sha256=window_hash(window)))

    def reject(reason, valid=False):
        result.update(valid=valid, reason=reason)
        return result

    if event is None:
        return reject("funding_missing")
    if last_seen is None:
        result.update(next_seen=event, event_new=True)
        return reject("funding_initialization", True)
    if event < last_seen:
        return reject("funding_clock_regression")
    if event == last_seen:
        return result
    result.update(next_seen=event, event_new=True)
    params = [_number(extreme_z), _number(reset_z)]
    if None in params or not 0 < params[1] < params[0]:
        return reject("funding_params_invalid")
    if not 0 < now - event <= 2 * BAR:
        return reject("funding_event_age")
    if not isinstance(history32, (list, tuple)) or len(history32) != 32:
        return reject("funding_history_count")
    if any(t is None or a is None or rate is None for t, a, rate in window):
        return reject("funding_history_invalid")
    if any(a > now or a <= t for t, a, rate in window):
        return reject("funding_unpublished")
    if any(not 8 * BAR - 1000 <= right[0] - left[0] <= 8 * BAR + 1000
           for left, right in zip(window, window[1:])):
        return reject("funding_history_gap")
    if window[-1][0] != event or _number(current_rate) != window[-1][2]:
        return reject("funding_accessor_mismatch")
    # Thirty prior payments span about ten days; the final pair never enters the baseline.
    signal = reset_signal(window[-2][2], window[-1][2],
                          [row[2] for row in window[:30]], extreme_z, reset_z)
    direction = signal.pop("direction")
    reason = signal.pop("reason")
    result["details"] = signal
    result["event"].update(available_at=window[-1][1], rate_decimal=window[-1][2])
    if direction == 0:
        return reject(reason, reason == "funding_no_reset")
    # 72 current closes and the 72-window shifted24h require exactly96, not84.
    rows = closed_window(candles, now, 96)
    if rows is None:
        return reject("funding_price_window")
    if not isinstance(atr, dict) or _number(atr.get("value")) is None or atr["value"] <= 0:
        return reject("funding_atr_invalid")
    close = rows[:, 2]
    current = float(close[-1])
    # Aggregate overflow is invalid data, even when every original OHLC is finite.
    with np.errstate(over="ignore", invalid="ignore"):
        sma72, old72 = float(np.mean(close[-72:])), float(np.mean(close[-96:-24]))
        sma24 = float(np.mean(close[-24:]))
    old6 = float(close[-7])
    if not all(math.isfinite(value) for value in (current, sma72, old72, sma24, old6)):
        return reject("funding_price_arithmetic")
    result["details"].update(close=current, sma72=sma72, sma72_previous24=old72,
                             sma24=sma24, close_previous6=old6, funding_direction=direction)
    passed = (current > sma72 > old72 and current > sma24 and current > old6) if direction == 1 else (current < sma72 < old72 and current < sma24 and current < old6)
    result.update(direction=direction if passed else 0, reason="funding_reset" if passed else "funding_regime_reject")
    return result


def self_checks():
    """Deterministic synthetic cases exercise event time, symmetry and immutable inputs."""
    assertions = 0

    def check(condition):
        nonlocal assertions
        assert condition
        assertions += 1

    now = 2000 * BAR
    event = now - BAR
    history = [dict(settled_at=event - (31 - i) * 8 * BAR,
                    available_at=event - (31 - i) * 8 * BAR + 60000,
                    rate_decimal=(-.0001 if i % 2 == 0 else .0001)) for i in range(32)]
    history[-2]["rate_decimal"] = .0002
    history[-1]["rate_decimal"] = .000025
    prices = np.arange(100., 196.)
    candles = np.array([[now - (96 - i) * BAR, p, p, p + 1, p - 1, 1] for i, p in enumerate(prices)])
    atr = dict(value=2.)
    original = json.dumps(history, sort_keys=True)
    candle_copy = candles.copy()

    def call(h=None, c=None, t=now, rate=None, stamp=event, seen=event-8*BAR, risk=atr):
        h = history if h is None else h
        return features(candles if c is None else c, t, risk, h,
                        h[-1]["rate_decimal"] if rate is None else rate, stamp, seen)

    result = call()
    check(result["direction"] == 1 and result["valid"])
    check(result["next_seen"] == event and result["event_new"])
    check(result["details"]["baseline"] == 0.)
    check(abs(result["details"]["sigma"] - .0001) < 1e-15)
    check(json.dumps(history, sort_keys=True) == original)
    check(np.array_equal(candles, candle_copy))
    check(call(seen=None)["reason"] == "funding_initialization")
    check(call(seen=event)["event_new"] is False)
    check(call(seen=event+1)["reason"] == "funding_clock_regression")
    check(call(stamp=None)["reason"] == "funding_missing")
    check(call(t=event)["reason"] == "funding_event_age")
    check(call(t=event+2*BAR+1)["reason"] == "funding_event_age")
    check(call(h=history[:-1])["next_seen"] == event)
    check(call(h=history[:-1])["reason"] == "funding_history_count")
    check(call(rate=.0123)["reason"] == "funding_accessor_mismatch")
    for key, value, reason in [("available_at", now+1, "funding_unpublished"),
                               ("available_at", event, "funding_unpublished"),
                               ("rate_decimal", float("nan"), "funding_history_invalid"),
                               ("settled_at", history[-2]["settled_at"], "funding_history_gap")]:
        changed = [dict(r) for r in history]
        changed[-1][key] = value
        check(call(h=changed)["reason"] == reason)
    changed = [dict(r) for r in history]
    changed[1]["settled_at"] += 1001
    check(call(h=changed)["reason"] == "funding_history_gap")
    changed = [dict(r) for r in history]
    changed[-1]["settled_at"] += 4
    changed[-1]["available_at"] = event+60000
    check(call(h=changed, stamp=event+4)["direction"] == 1)
    flat = [dict(r, rate_decimal=.0001) for r in history]
    check(call(h=flat)["reason"] == "funding_sigma_zero")
    flat = [dict(r, rate_decimal=0.) for r in history]
    check(call(h=flat)["reason"] == "funding_sigma_zero")
    check(call(c=candles[-95:])["reason"] == "funding_price_window")
    check(call(risk=None)["reason"] == "funding_atr_invalid")
    future = np.vstack([candles, [now, 500, 500, 501, 499, 1]])
    check(call(c=future)["direction"] == 1)
    broken = candles.copy()
    broken[4, 0] += 1
    check(call(c=broken)["reason"] == "funding_price_window")
    broken = candles.copy()
    broken[-1, 2] = 80
    broken[-1, 4] = 79
    check(call(c=broken)["reason"] == "funding_regime_reject")
    for scale in (1., -1.):
        baseline = [scale*x for x in [-1., 1.]*15]
        signal = reset_signal(scale, scale*.5, baseline)
        check(signal["direction"] == int(scale))
        check(reset_signal(scale, 0., baseline)["direction"] == int(scale))
        check(reset_signal(scale, -scale*.01, baseline)["direction"] == 0)
        check(reset_signal(scale*.999, scale*.1, baseline)["direction"] == 0)
        check(reset_signal(scale, scale*.50001, baseline)["direction"] == 0)
        shifted = reset_signal(2.+scale, 2.+scale*.5, [x+2. for x in baseline])
        check(shifted["direction"] == int(scale))
    short_history = [dict(r, rate_decimal=-r["rate_decimal"]) for r in history]
    descending = candles.copy()
    descending[:, 1:5] = np.column_stack([400-prices, 400-prices, 401-prices, 399-prices])
    check(call(h=short_history, c=descending)["direction"] == -1)
    state = ma24_state(candles, now)
    check(state["close"] > state["sma24"])
    check(ma24_state(candles[-23:], now) is None)
    # Huge yet coherent finite OHLC must reject overflowing means without JSON NaN/Infinity.
    huge = candles.copy()
    huge[:, 1:5] = 1e308
    invalid = call(c=huge)
    check(invalid["valid"] is False and invalid["reason"] == "funding_price_arithmetic")
    check(invalid["next_seen"] == event)
    check(ma24_state(huge, now) is None)
    check(json.loads(json.dumps(invalid, allow_nan=False))["direction"] == 0)
    check(len(result["event"]["window"]) == 32)
    check(result["event"]["sha256"] == window_hash(canonical_window(history)))
    bad = canonical_window([dict(settled_at=event, available_at=now, rate_decimal=float("nan"))])
    check(bad[0][2] is None)
    for block in (result["event"]["window"][:16], result["event"]["window"][16:]):
        check(len(json.dumps(dict(time=now, sha256=result["event"]["sha256"], rows=block), allow_nan=False)) < 1800)
    return dict(status="passed", assertions=assertions)
