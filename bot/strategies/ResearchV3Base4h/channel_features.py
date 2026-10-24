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
