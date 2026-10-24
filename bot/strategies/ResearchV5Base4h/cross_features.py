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
