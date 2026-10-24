"""Causal hourly shock reversal; thresholds are frozen before economic testing."""

import json
import math

import numpy as np

from strategies.ResearchV4Base1h import BAR, atr_window, closed_window


def features(candles, now, atr, shock_multiplier=2.0, volume_multiplier=2.0):
    # Twenty-four prior volumes plus the event; no future confirmation or latch.
    rows = closed_window(candles, now, 25)
    invalid = dict(valid=False, direction=0, reason="shock_data_invalid", details={})
    if rows is None or rows.shape[1] < 6:
        return invalid
    volumes = rows[:, 5]
    if not np.all(np.isfinite(volumes)) or np.any(volumes < 0):
        return invalid
    try:
        if (not math.isfinite(shock_multiplier) or shock_multiplier <= 0 or
                not math.isfinite(volume_multiplier) or volume_multiplier <= 0):
            return invalid
        # Reject a current-bar ATR accidentally supplied by another sector.
        if (atr is None or atr["offset_bars"] != 1 or
                atr["first"] != now - 16 * BAR or atr["last"] != now - 2 * BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="shock_atr_invalid", details={})
    except (KeyError, TypeError, ValueError):
        return invalid
    average_volume = float(np.mean(volumes[:-1]))
    displacement = float(rows[-1, 2] - rows[-2, 2])
    current_volume = float(volumes[-1])
    # A finite input sum can still overflow; reject rather than emit NaN/Infinity.
    if (not math.isfinite(average_volume) or average_volume <= 0 or
            not math.isfinite(displacement)):
        return invalid
    price_threshold = float(shock_multiplier * atr["value"])
    volume_threshold = float(volume_multiplier * average_volume)
    if not math.isfinite(price_threshold) or not math.isfinite(volume_threshold):
        return invalid
    price_event = bool(abs(displacement) >= price_threshold)
    volume_event = bool(current_volume >= volume_threshold)
    direction = (-1 if displacement > 0 else 1) if price_event and volume_event else 0
    # Only Python scalars: source windows live in bounded ATR/provenance logs.
    details = dict(first=int(rows[0, 0]), last=int(rows[-1, 0]),
        displacement=displacement, atr_previous=float(atr["value"]),
        volume=current_volume, volume_mean_previous=average_volume,
        shock_multiplier=float(shock_multiplier), volume_multiplier=float(volume_multiplier),
        price_event=price_event, volume_event=volume_event)
    reason = "shock_setup" if direction else "shock_price_below" if not price_event else "shock_volume_below"
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Pure deterministic surfaces; these checks make no claims about broker fills."""
    count = 0

    def check(condition):
        nonlocal count
        assert condition
        count += 1

    def fixture(sign=1):
        # Prior14 true ranges are exactly2; minimum shock is4 and volume20.
        rows = np.array([[i * BAR, 100., 100., 101., 99., 10.] for i in range(25)])
        rows[-1, 2] = 100. + sign * 4.
        rows[-1, 3] = max(101., rows[-1, 2] + 1.)
        rows[-1, 4] = min(99., rows[-1, 2] - 1.)
        rows[-1, 5] = 20.
        return rows

    now = 25 * BAR
    up, down = fixture(), fixture(-1)
    atr = atr_window(up, now, 1)
    check(atr["value"] == 2.)
    check(atr["first"] == 9 * BAR and atr["last"] == 23 * BAR)
    check(len(atr["bars"]) == 15 and atr["offset_bars"] == 1)
    short, long = features(up, now, atr), features(down, now, atr_window(down, now, 1))
    check(short["valid"] and short["direction"] == -1)
    check(long["valid"] and long["direction"] == 1)
    check(short["details"]["displacement"] == -long["details"]["displacement"])
    check(short["details"]["volume_mean_previous"] == 10.)
    check(short["details"]["volume"] == 20.)
    check(short["reason"] == long["reason"] == "shock_setup")
    check(len(json.dumps(short, allow_nan=False)) < 1000)
    before = up.copy()
    features(up, now, atr)
    check(np.array_equal(up, before))
    below = up.copy()
    below[-1, 2] = 103.999
    check(features(below, now, atr)["direction"] == 0)
    check(features(below, now, atr)["reason"] == "shock_price_below")
    below = up.copy()
    below[-1, 5] = 19.999
    check(features(below, now, atr)["direction"] == 0)
    check(features(below, now, atr)["reason"] == "shock_volume_below")
    check(features(up, now, atr, 1.8, 1.8)["direction"] == -1)
    check(features(up, now, atr, 2.2, 2.2)["direction"] == 0)
    wide_event = up.copy()
    wide_event[-1, 3], wide_event[-1, 4] = 200., 1.
    check(atr_window(wide_event, now, 1)["value"] == 2.)
    check(features(wide_event, now, atr)["direction"] == -1)
    huge_volume = up.copy()
    huge_volume[-1, 5] = 10000.
    check(features(huge_volume, now, atr)["details"]["volume_mean_previous"] == 10.)
    check(not features(up, now, atr_window(up, now, 0))["valid"])
    check(not features(up, now, None)["valid"])
    malformed_atr = dict(atr, value=float("nan"))
    check(not features(up, now, malformed_atr)["valid"])
    malformed_atr = dict(atr, first=0)
    check(not features(up, now, malformed_atr)["valid"])
    future = np.array([[now, 100., 100., 101., 99., float("nan")]])
    check(features(np.vstack((up, future)), now, atr) == short)
    # More history cannot seed a different value: only the last25 closed rows matter.
    older = up.copy()
    older[:, 0] -= 25 * BAR
    check(features(np.vstack((older, up)), now, atr) == short)
    check(not features(up[:-1], now, atr)["valid"])
    check(not features(up, now + 1, atr)["valid"])
    gap = up.copy()
    gap[2, 0] += 1
    check(not features(gap, now, atr)["valid"])
    for column, value in ((1, 0.), (2, float("nan")), (3, 90.), (4, 110.),
                          (5, -1.), (5, float("nan")), (5, float("inf"))):
        bad = up.copy()
        bad[5, column] = value
        check(not features(bad, now, atr)["valid"])
    zero_mean = up.copy()
    zero_mean[:-1, 5] = 0.
    check(not features(zero_mean, now, atr)["valid"])
    zero_event = up.copy()
    zero_event[-1, 5] = 0.
    check(features(zero_event, now, atr)["valid"] and features(zero_event, now, atr)["direction"] == 0)
    check(not features(up[:, :5], now, atr)["valid"])
    for parameter in (0., -1., float("nan"), float("inf")):
        check(not features(up, now, atr, parameter, 2.)["valid"])
        check(not features(up, now, atr, 2., parameter)["valid"])
    # A zero prior candle volume is allowed when its24-hour average remains positive.
    one_zero = up.copy()
    one_zero[0, 5] = 0.
    check(features(one_zero, now, atr)["valid"])
    return dict(status="passed", assertions=count)
