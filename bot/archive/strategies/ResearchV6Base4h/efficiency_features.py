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
