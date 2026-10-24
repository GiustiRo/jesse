"""Causal 24h price displacement and a closed-bar correction; OI belongs to the core."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, atr_window, closed_window


def _direction(displacement, correction, threshold):
    # Inclusive displacement, strict correction: a flat last bar is never a turn.
    if displacement <= -threshold and correction > 0:
        return 1
    if displacement >= threshold and correction < 0:
        return -1
    return 0


def features(candles, now, atr, displacement_multiplier=2.):
    """Finite fifteen-OHLC context; no state, OI access, fill assumptions or IO."""
    invalid = dict(valid=False, direction=0, reason="deleverage_data_invalid", details={})
    rows = closed_window(candles, now, 15)
    if rows is None:
        return invalid
    if (isinstance(displacement_multiplier, bool) or
            not isinstance(displacement_multiplier, (int, float)) or
            not math.isfinite(displacement_multiplier) or displacement_multiplier <= 0):
        return dict(valid=False, direction=0, reason="deleverage_multiplier_invalid", details={})
    try:
        # Guard the common-core interface against a prior-bar ATR or another clock.
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="deleverage_atr_invalid", details={})
        average_range = float(atr["value"])
    except (KeyError, TypeError, ValueError):
        return dict(valid=False, direction=0, reason="deleverage_atr_invalid", details={})
    close, prior, day_ago = (float(rows[index, 2]) for index in (-1, -2, -7))
    displacement, correction = close - day_ago, close - prior
    threshold = float(displacement_multiplier * average_range)
    if not all(math.isfinite(value) for value in (displacement, correction, threshold)) or threshold <= 0:
        return dict(valid=False, direction=0, reason="deleverage_arithmetic_invalid", details={})
    direction = _direction(displacement, correction, threshold)
    reason = ("deleverage_setup" if direction else
              "deleverage_displacement_below" if abs(displacement) < threshold else
              "deleverage_correction_reject")
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(close=close, previous_close=prior, close_24h_ago=day_ago,
        displacement_24h=displacement, correction_4h=correction,
        atr=average_range, displacement_multiplier=float(displacement_multiplier),
        displacement_threshold=threshold, first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=15, reference_bars=6, sha256=digest)
    return dict(valid=True, direction=direction, reason=reason, details=details)


def self_checks():
    """Synthetic finite-window and boundary checks; no broker/provider emulation."""
    assertions = 0

    def check(condition):
        nonlocal assertions
        assert bool(condition)
        assertions += 1

    def candles(values, first=0):
        values = np.asarray(values, dtype=float)
        return np.column_stack((first + np.arange(len(values)) * BAR,
            values, values, values + .5, values - .5, np.ones(len(values))))

    now = 15 * BAR
    long = candles([104.] * 8 + [104., 102., 100., 98., 96., 95., 96.])
    short = long.copy()
    short[:, 1] = 200. - long[:, 1]
    short[:, 2] = 200. - long[:, 2]
    short[:, 3] = 200. - long[:, 4]
    short[:, 4] = 200. - long[:, 3]
    for source, expected in ((long, 1), (short, -1)):
        original = source.copy()
        atr = atr_window(source, now)
        result = features(source, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "deleverage_setup")
        check(result["details"]["reference_bars"] == 6)
        check(result["details"]["close_24h_ago"] == source[-7, 2])
        check(result["details"]["previous_close"] == source[-2, 2])
        check(result["details"]["first"] == 0 and result["details"]["last"] == 14 * BAR)
        check(len(json.dumps(result, allow_nan=False)) < 1000)
        for multiplier in (1.8, 2., 2.2):
            check(features(source, now, atr, multiplier)["direction"] == expected)
        # A different older prefix cannot alter either the feature or ATR context.
        prefix = candles([80., 81., 82.], first=-3 * BAR)
        extended = np.vstack([prefix, source])
        check(features(extended, now, atr_window(extended, now)) == result)
        extended[:3, 1:5] *= 1.1
        check(features(extended, now, atr_window(extended, now)) == result)
        future = candles([120., 121.], first=now)
        appended = np.vstack([source, future])
        check(features(appended, now, atr_window(appended, now)) == result)
        appended[-2:, 1:5] *= 2.
        check(features(appended, now, atr_window(appended, now)) == result)
        check(np.array_equal(original, source))
        check(not features(source[-14:], now, atr)["valid"])
        check(not features(source, now + 1, atr)["valid"])
        check(not features(source[:-1], now, atr)["valid"])
    # Exact scalar boundaries isolate inequalities from fixture-dependent ATR values.
    check(_direction(-4., 1., 4.) == 1)
    check(_direction(4., -1., 4.) == -1)
    check(_direction(-4. + 1e-8, 1., 4.) == 0)
    check(_direction(4. - 1e-8, -1., 4.) == 0)
    for correction in (0., -1.):
        check(_direction(-4., correction, 4.) == 0)
    for correction in (0., 1.):
        check(_direction(4., correction, 4.) == 0)
    check(_direction(0., 1., 4.) == 0)
    flat = candles([100.] * 15)
    flat_result = features(flat, now, atr_window(flat, now))
    check(flat_result["valid"] and flat_result["direction"] == 0)
    check(flat_result["reason"] == "deleverage_displacement_below")
    no_correction = long.copy()
    no_correction[-1, 1:5] = (94., 94., 94.5, 93.5)
    check(features(no_correction, now, atr_window(no_correction, now))["reason"] == "deleverage_correction_reject")
    good_atr = atr_window(long, now)
    for multiplier in (0., -1., float("nan"), float("inf"), None, True):
        check(not features(long, now, good_atr, multiplier)["valid"])
    for bad_atr in (None, {}, dict(good_atr, value=0.),
                    dict(good_atr, value=float("nan")), dict(good_atr, offset_bars=1),
                    dict(good_atr, first=-BAR), dict(good_atr, last=now)):
        check(features(long, now, bad_atr)["reason"] == "deleverage_atr_invalid")
    for column, value in ((2, float("nan")), (1, 0.), (3, 1.), (4, 1000.),
                          (0, now - 2 * BAR)):
        broken = long.copy()
        broken[-1, column] = value
        check(not features(broken, now, good_atr)["valid"])
    broken = long.copy()
    broken[-8, 0] -= BAR
    check(not features(broken, now, good_atr)["valid"])
    # A finite multiplier times a finite ATR can overflow: reject JSON-incompatible evidence.
    huge_atr = dict(good_atr, value=1e308)
    overflow = features(long, now, huge_atr, 2.)
    check(not overflow["valid"] and overflow["reason"] == "deleverage_arithmetic_invalid")
    check(len(json.dumps(overflow, allow_nan=False)) < 1000)
    # No OI appears in this pure price helper; the core separately checks declining ratios.
    check("oi" not in features(long, now, good_atr)["details"])
    return dict(status="passed", assertions=assertions)
