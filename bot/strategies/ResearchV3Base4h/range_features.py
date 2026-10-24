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
