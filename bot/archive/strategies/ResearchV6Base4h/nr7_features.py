"""Causal NR7 contraction and next-close expansion; no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, atr_window, closed_window


def features(candles, now, atr, narrow_window=7):
    """Rank only prior bars; current close determines the exclusive direction."""
    invalid = dict(valid=False, direction=0, reason="nr7_data_invalid", details={})
    if (isinstance(narrow_window, bool) or not isinstance(narrow_window, int) or
            narrow_window < 2):
        return dict(valid=False, direction=0, reason="nr7_parameter_invalid", details={})
    rows = closed_window(candles, now, narrow_window + 1)
    if rows is None:
        return invalid
    try:
        # Risk must use current arithmetic14TR, not the pre-expansion offset.
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="nr7_atr_invalid", details={})
    except (KeyError, TypeError, ValueError):
        return dict(valid=False, direction=0, reason="nr7_atr_invalid", details={})
    prior = rows[:-1]
    ranges = prior[:, 3] - prior[:, 4]
    if not np.all(np.isfinite(ranges)) or np.any(ranges < 0):
        return invalid
    setup_range = float(ranges[-1])
    comparison_min = float(np.min(ranges[:-1]))
    narrow = bool(setup_range < comparison_min)
    close, upper, lower = (float(rows[-1, 2]), float(prior[-1, 3]), float(prior[-1, 4]))
    direction = (1 if close > upper else -1 if close < lower else 0) if narrow else 0
    # Zero range may qualify strictly; equal minima do not. No epsilon changes ranking.
    reason = "nr7_breakout" if direction else "nr7_no_breakout" if narrow else "nr7_not_narrow"
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(narrow_window=narrow_window, first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=narrow_window + 1, sha256=digest,
        setup_time=int(prior[-1, 0]), setup_high=upper, setup_low=lower,
        setup_range=setup_range, comparison_min=comparison_min,
        prior_ranges=[float(x) for x in ranges], narrow=narrow, close=close)
    return dict(valid=True, direction=direction, reason=reason, details=details)


def self_checks():
    """Synthetic algebra and clock checks; no claim about simulated broker fills."""
    count = 0

    def check(condition):
        nonlocal count
        assert condition
        count += 1

    def fixture():
        rows = np.array([[i*BAR, 100., 100., 102., 98., 1.] for i in range(15)])
        rows[-2, 3:5] = (100.5, 99.5)
        rows[-1, 2:5] = (103., 104., 99.)
        return rows

    now = 15 * BAR
    long = fixture()
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    for rows, expected in ((long, 1), (short, -1)):
        original = rows.copy()
        atr = atr_window(rows, now)
        result = features(rows, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "nr7_breakout")
        check(result["details"]["narrow"])
        check(result["details"]["setup_range"] == 1.)
        check(result["details"]["comparison_min"] == 4.)
        check(result["details"]["prior_ranges"] == [4.]*6 + [1.])
        check(result["details"]["first"] == now - 8*BAR)
        check(result["details"]["last"] == now - BAR)
        check(result["details"]["setup_time"] == now - 2*BAR)
        check(np.array_equal(rows, original))
        check(len("V6_FEATURES " + json.dumps(dict(time=now, line="NR7", **result),
              separators=(",", ":"), allow_nan=False)) <= 1900)
        for n in (6, 7, 8):
            item = features(rows, now, atr, n)
            check(item["direction"] == expected)
            check(item["details"]["bars"] == n + 1)
        prefix = rows[:4].copy()
        prefix[:, 0] -= 19 * BAR
        extended = np.vstack((prefix, rows))
        check(features(extended, now, atr) == result)
        extended[:4, 1:5] *= 1.5
        check(features(extended, now, atr) == result)
        future = np.array([[now, 1., float("nan"), float("inf"), -1., 0.]])
        extended = np.vstack((rows, future))
        check(features(extended, now, atr) == result)
        # Pattern depends on eight bars; ATR's independently frozen15-bar provenance stays supplied.
        check(features(rows[-8:], now, atr) == result)
        check(features(rows[-7:], now, atr)["valid"] is False)
        check(features(rows, now + 1, atr)["valid"] is False)
        check(features(rows[:-1], now, atr)["valid"] is False)
        changed = rows.copy()
        changed[-3, 3:5] = (100.5 if expected == 1 else 300.5,
                                  99.5 if expected == 1 else 299.5)
        check(features(changed, now, atr)["reason"] == "nr7_not_narrow")
    atr = atr_window(long, now)
    for value in (100.5, 99.5, 100.):
        changed = long.copy()
        changed[-1, 2] = value
        check(features(changed, now, atr)["direction"] == 0)
        check(features(changed, now, atr)["reason"] == "nr7_no_breakout")
    # B0 can traverse both previous extrema; only its final close decides, without retrofill.
    check(long[-1, 3] > long[-2, 3] and long[-1, 4] < long[-2, 4])
    check(features(long, now, atr)["direction"] == 1)
    changed = long.copy()
    changed[-1, 2] = 99.
    check(features(changed, now, atr)["direction"] == -1)
    changed[-1, 2] = 100.
    check(features(changed, now, atr)["direction"] == 0)
    # The expansion bar is never allowed to disqualify the prior NR7 contraction.
    changed = long.copy()
    changed[-1, 1:5] = (103., 103., 103.1, 102.9)
    check(features(changed, now, atr)["direction"] == 1)
    changed = long.copy()
    changed[-8, 3:5] = (100.25, 99.75)
    check(features(changed, now, atr, 6)["direction"] == 1)
    check(features(changed, now, atr, 7)["reason"] == "nr7_not_narrow")
    changed = long.copy()
    changed[-9, 3:5] = (100.25, 99.75)
    check(features(changed, now, atr, 7)["direction"] == 1)
    check(features(changed, now, atr, 8)["reason"] == "nr7_not_narrow")
    changed = long.copy()
    changed[-2, 1:5] = (100., 100., 100., 100.)
    check(features(changed, now, atr)["direction"] == 1)
    flat = np.array([[i*BAR, 100., 100., 100., 100., 1.] for i in range(15)])
    check(features(flat, now, atr)["reason"] == "nr7_not_narrow")
    check(atr_window(flat, now) is None)
    for column, value in ((0, now-3*BAR), (2, float("nan")), (3, 99.),
                          (4, 101.), (1, 0.)):
        changed = long.copy()
        changed[-2, column] = value
        check(features(changed, now, atr)["valid"] is False)
    for value in (0., -1., float("nan"), float("inf")):
        bad_atr = dict(atr, value=value)
        check(features(long, now, bad_atr)["reason"] == "nr7_atr_invalid")
    for key, value in (("offset_bars", 1), ("first", atr["first"]+BAR),
                       ("last", atr["last"]+BAR)):
        check(features(long, now, dict(atr, **{key:value}))["valid"] is False)
    check(features(long, now, None)["valid"] is False)
    for n in (0, 1, 7., True, None):
        check(features(long, now, atr, n)["reason"] == "nr7_parameter_invalid")
    # ATR supplied to entries is causal and includes the expansion's true range.
    previous_atr = atr_window(long, now, 1)
    check(previous_atr is None)
    sixteen = np.vstack((long[:1], long))
    sixteen[0, 0] -= BAR
    previous_atr = atr_window(sixteen, now, 1)
    check(previous_atr["value"] != atr["value"])
    check(features(sixteen, now, previous_atr)["reason"] == "nr7_atr_invalid")
    return dict(status="passed", assertions=count)
