"""Finite rolling24 HLC3/volume reversal; this is not anchored-day/tick VWAP."""

import hashlib
import json
import math

import numpy as np

from strategies.ResearchV5Base1h import BAR, atr_window, closed_window


def vwap_state(candles, now, dispersion=True):
    """Exit may use mean alone even when variance/ATR cannot be evaluated."""
    rows = closed_window(candles, now, 24)
    if rows is None or rows.shape[1] < 6:
        return None
    volume = rows[:, 5]
    if not np.all(np.isfinite(volume)) or np.any(volume < 0):
        return None
    maximum = float(np.max(volume))
    if maximum <= 0:
        return None
    # Scaling weights prevents overflow in a sum of otherwise finite large volumes.
    with np.errstate(over="ignore", invalid="ignore"):
        weights = volume / maximum
        weights = weights / np.sum(weights)
        typical = rows[:, 3] / 3. + rows[:, 4] / 3. + rows[:, 2] / 3.
        mean = float(np.sum(weights * typical))
    if not math.isfinite(mean) or mean <= 0:
        return None
    state = dict(mean=mean, close=float(rows[-1, 2]), first=int(rows[0, 0]),
                 last=int(rows[-1, 0]), zero_volumes=int(np.sum(volume == 0)))
    if dispersion:
        with np.errstate(over="ignore", invalid="ignore"):
            variance = float(np.sum(weights * (typical - mean) ** 2))
        if not math.isfinite(variance) or variance < 0:
            return None
        state["sigma"] = math.sqrt(variance)
    state["sha256"] = hashlib.sha256(json.dumps(
        rows[:, :6].tolist(), separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    return state


def entry_direction(c0, c1, m0, m1, s0, s1, multiplier):
    """Closed reentry includes outer equality but never enters past the mean."""
    values = (c0, c1, m0, m1, s0, s1, multiplier)
    if not all(math.isfinite(v) for v in values) or min(s0, s1, multiplier) <= 0:
        return 0
    lower0, upper0 = m0 - multiplier * s0, m0 + multiplier * s0
    lower1, upper1 = m1 - multiplier * s1, m1 + multiplier * s1
    if not all(math.isfinite(v) for v in (lower0, upper0, lower1, upper1)):
        return 0
    if c1 < lower1 and lower0 <= c0 < m0 and c0 > c1:
        return 1
    if c1 > upper1 and m0 < c0 <= upper0 and c0 < c1:
        return -1
    return 0


def features(candles, now, atr, band_multiplier=2.0):
    invalid = dict(valid=False, direction=0, reason="vwap_data_invalid", details={})
    rows = closed_window(candles, now, 25)
    if rows is None or rows.shape[1] < 6:
        return invalid
    try:
        if not math.isfinite(band_multiplier) or band_multiplier <= 0:
            return invalid
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return invalid
    except (KeyError, TypeError, ValueError):
        return invalid
    current = vwap_state(candles, now)
    previous = vwap_state(candles, now - BAR)
    atr_previous = atr_window(candles, now, 1)
    if current is None or previous is None or atr_previous is None:
        return invalid
    scale0 = max(current["sigma"], float(atr["value"]))
    scale1 = max(previous["sigma"], atr_previous["value"])
    # Reject overflow instead of allowing an unbounded band to produce a false reentry.
    if not all(math.isfinite(v) for v in (
            current["mean"] - band_multiplier * scale0,
            current["mean"] + band_multiplier * scale0,
            previous["mean"] - band_multiplier * scale1,
            previous["mean"] + band_multiplier * scale1)):
        return invalid
    direction = entry_direction(current["close"], previous["close"], current["mean"],
        previous["mean"], scale0, scale1, band_multiplier)
    details = dict(close=current["close"], close_previous=previous["close"],
        mean=current["mean"], mean_previous=previous["mean"],
        sigma=current["sigma"], sigma_previous=previous["sigma"],
        atr=float(atr["value"]), atr_previous=atr_previous["value"],
        scale=scale0, scale_previous=scale1, band_multiplier=float(band_multiplier),
        first=int(rows[0, 0]), last=int(rows[-1, 0]),
        current_sha256=current["sha256"], previous_sha256=previous["sha256"],
        zero_volumes=current["zero_volumes"], zero_volumes_previous=previous["zero_volumes"])
    return dict(valid=True, direction=int(direction),
                reason="vwap_reentry" if direction else "vwap_no_reentry", details=details)


def exit_state(candles, now, direction):
    """State condition; no ATR, dispersion, fresh crossing or previous25th row."""
    state = vwap_state(candles, now, dispersion=False)
    if state is None or direction not in (-1, 1):
        return dict(valid=False, exit=False, details={})
    return dict(valid=True, exit=bool(direction * (state["close"] - state["mean"]) >= 0),
                details=state)


def self_checks():
    """Pure algebra/window checks; broker/time priorities remain common checks."""
    count = 0

    def check(value):
        nonlocal count
        assert value
        count += 1

    now = 25 * BAR
    flat = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(25)])
    state = vwap_state(flat, now)
    check(abs(state["mean"] - 100.) < 1e-12)
    check(state["sigma"] < 1e-12)
    check(state["first"] == BAR and state["last"] == 24 * BAR)
    weighted = flat.copy()
    for i in range(25):
        p = 100. + i
        weighted[i, 1:5] = [p, p, p + 1., p - 1.]
        weighted[i, 5] = i + 1.
    oracle_mean = sum((i + 1.) * (100. + i) for i in range(1, 25)) / sum(range(2, 26))
    oracle_var = sum((i + 1.) * (100. + i - oracle_mean) ** 2 for i in range(1, 25)) / sum(range(2, 26))
    result = vwap_state(weighted, now)
    check(abs(result["mean"] - oracle_mean) < 1e-12)
    check(abs(result["sigma"] - math.sqrt(oracle_var)) < 1e-12)
    scaled = weighted.copy()
    scaled[:, 5] *= 8.
    scaled_result = vwap_state(scaled, now)
    check(result["mean"] == scaled_result["mean"])
    check(result["sigma"] == scaled_result["sigma"])
    large = flat.copy()
    large[:, 5] = 1e308
    check(vwap_state(large, now) is not None)
    single = flat.copy()
    single[:, 5] = 0.
    single[-1, 5] = 3.
    check(vwap_state(single, now)["mean"] == 100.)
    check(vwap_state(single, now)["sigma"] == 0.)
    check(vwap_state(single, now)["zero_volumes"] == 23)
    all_zero = single.copy()
    all_zero[-1, 5] = 0.
    check(vwap_state(all_zero, now) is None)
    # One prior outlier then a recovering close; volume stays positive and unchanged.
    setup = flat.copy()
    setup[-2, 1:5] = [80., 80., 81., 79.]
    setup[-1, 1:5] = [90., 90., 91., 89.]
    atr = atr_window(setup, now)
    signal = features(setup, now, atr)
    check(signal["valid"] and signal["direction"] == 1)
    mirror = setup.copy()
    mirror[:, 1] = 200. - setup[:, 1]
    mirror[:, 2] = 200. - setup[:, 2]
    mirror[:, 3] = 200. - setup[:, 4]
    mirror[:, 4] = 200. - setup[:, 3]
    check(features(mirror, now, atr_window(mirror, now))["direction"] == -1)
    check(signal["details"]["atr_previous"] == atr_window(setup, now - BAR)["value"])
    check(signal["details"]["mean_previous"] == vwap_state(setup[:-1], now - BAR)["mean"])
    check(entry_direction(96., 95., 100., 100., 2., 2., 2.) == 1)
    check(entry_direction(104., 105., 100., 100., 2., 2., 2.) == -1)
    check(entry_direction(96., 96., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(100., 95., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(100., 105., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(95., 94., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(105., 106., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(96., 95., 100., 110., 2., 2., 2.) == 1)
    check(entry_direction(95., 95., 100., 110., 3., 2., 2.) == 0)
    check(features(setup, now, atr, 1.8)["valid"])
    check(features(setup, now, atr, 2.2)["valid"])
    future = np.array([[now, 100., 100., 101., 99., float("nan")]])
    check(features(np.vstack((setup, future)), now, atr) == signal)
    older = flat.copy()
    older[:, 0] -= 25 * BAR
    check(features(np.vstack((older, setup)), now, atr) == signal)
    original = setup.copy()
    features(setup, now, atr)
    check(np.array_equal(setup, original))
    check(not features(setup[-24:], now, atr)["valid"])
    check(exit_state(flat[-24:], now, 1)["valid"])
    check(exit_state(single[-24:], now, 1)["exit"])
    check(exit_state(single[-24:], now, -1)["exit"])
    check(not exit_state(setup[-24:], now, 1)["exit"])
    check(exit_state(setup[-24:], now, -1)["exit"])
    check(not exit_state(flat[-23:], now, 1)["valid"])
    check(not features(setup, now + 1, atr)["valid"])
    check(not features(setup, now, None)["valid"])
    check(not features(setup, now, atr_window(setup, now, 1))["valid"])
    check(not features(setup[:, :5], now, atr)["valid"])
    for column, value in ((0, 3 * BAR), (1, 0.), (2, float("nan")),
                          (3, 50.), (4, 150.), (5, -1.), (5, float("inf"))):
        bad = setup.copy()
        bad[2, column] = value
        check(not features(bad, now, atr)["valid"])
    bad = setup.copy()
    bad[:, 5] = 0.
    check(not features(bad, now, atr)["valid"])
    bad = setup.copy()
    bad[-1, 5] = 0.
    check(features(bad, now, atr)["valid"])
    for k in (0., -1., float("nan"), float("inf")):
        check(not features(setup, now, atr, k)["valid"])
    check(len("V5_FEATURES " + json.dumps(dict(time=int(now), line="VWAP", **signal),
                                        allow_nan=False, separators=(",", ":"))) <= 1900)
    check("sigma" not in exit_state(flat, now, 1)["details"])
    return dict(status="passed", assertions=count)
