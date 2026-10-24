import hashlib
import json
import math

import numpy as np

BAR = 14400000
HISTORY = 126


def features(candles, now, atr):
    """Three closed bars form the pattern; ATR controls risk only in the shared base."""
    rows = candles[candles[:, 0] + BAR <= now][-HISTORY:]
    if len(rows) != HISTORY or rows[-1, 0] != now - BAR:
        return dict(valid=False, direction=0, details=dict(reason="history_short"))
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return dict(valid=False, direction=0, details=dict(reason="history_gap"))
    prices = rows[:, 1:5]
    if not np.all(np.isfinite(rows[:, :5])) or np.any(prices <= 0):
        return dict(valid=False, direction=0, details=dict(reason="ohlc_invalid"))
    opens, closes, highs, lows = (rows[:, i] for i in (1, 2, 3, 4))
    if np.any(highs < np.maximum(opens, closes)) or np.any(lows > np.minimum(opens, closes)) or np.any(highs < lows):
        return dict(valid=False, direction=0, details=dict(reason="ohlc_invalid"))
    # Exact slices preserve each historical SMA's own closed-bar endpoint.
    fast = float(np.mean(closes[-20:]))
    fast_previous = float(np.mean(closes[-21:-1]))
    fast_older = float(np.mean(closes[-22:-2]))
    slow = float(np.mean(closes[-120:]))
    slow_previous_day = float(np.mean(closes[-126:-6]))
    if not np.all(np.isfinite([fast, fast_previous, fast_older, slow, slow_previous_day])):
        return dict(valid=False, direction=0, details=dict(reason="sma_invalid"))
    touch = bool(lows[-2] <= fast_previous <= highs[-2])
    long_regime = bool(closes[-1] > slow and slow > slow_previous_day)
    short_regime = bool(closes[-1] < slow and slow < slow_previous_day)
    long_pattern = bool(closes[-3] > fast_older and touch and closes[-1] > highs[-2] and closes[-1] > fast)
    short_pattern = bool(closes[-3] < fast_older and touch and closes[-1] < lows[-2] and closes[-1] < fast)
    go_long, go_short = long_regime and long_pattern, short_regime and short_pattern
    assert not (go_long and go_short)
    direction = 1 if go_long else -1 if go_short else 0
    # Window hash is the same canonical timestamp/OHLC format used for ATR provenance.
    window_hash = hashlib.sha256(json.dumps(rows[:, :5].tolist(), separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    result = dict(valid=True, direction=direction, details=dict(
        fast=fast, fast_previous=fast_previous, fast_older=fast_older,
        slow=slow, slow_previous_day=slow_previous_day, touch=touch,
        long_regime=long_regime, short_regime=short_regime,
        long_pattern=long_pattern, short_pattern=short_pattern,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), sha256=window_hash,
        pattern=rows[-3:, :5].tolist()))
    if direction == 0:
        result["reason"] = "regime_reject" if not (long_regime or short_regime) else "no_setup"
    return result


def self_checks():
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Linear closes make all SMA values independently calculable by arithmetic series.
    rows = np.array([[i * BAR, 100. + i, 100. + i, 101. + i, 99. + i, 1.] for i in range(126)])
    rows[-2, 4] = 213.
    rows[-1, 1:5] = [228., 228., 229., 227.]
    now = 126 * BAR
    result = features(rows, now, None)
    check(result["valid"] and result["direction"] == 1)
    expected = dict(fast=215.65, fast_previous=214.5, fast_older=213.5,
                    slow=165.525, slow_previous_day=159.5)
    for key, value in expected.items():
        check(math.isclose(result["details"][key], value, rel_tol=0, abs_tol=1e-12))
    check(result["details"]["first"] == 0 and result["details"]["last"] == now - BAR)

    # Reflection exchanges long/short while preserving the wick-touch geometry.
    mirror = rows.copy()
    mirror[:, 1] = 500 - rows[:, 1]
    mirror[:, 2] = 500 - rows[:, 2]
    mirror[:, 3] = 500 - rows[:, 4]
    mirror[:, 4] = 500 - rows[:, 3]
    check(features(mirror, now, None)["direction"] == -1)

    future = np.vstack([rows, [[now, 1e9, 1e9, 1e9, 1e9, 1.],
                             [now + BAR, 1e9, 1e9, 1e9, 1e9, 1.]]])
    check(features(future, now, None) == result)
    future[-2:, 1:5] = np.nan
    check(features(future, now, None) == result)
    older = np.vstack([[[-BAR, float("nan"), float("nan"), float("nan"), float("nan"), 1.]], rows])
    check(features(older, now, None) == result)

    changed_current = rows.copy()
    changed_current[-1, 1:5] = [100000., 100000., 100001., 99999.]
    changed = features(changed_current, now, None)
    for key in ("fast_previous", "fast_older", "slow_previous_day"):
        check(changed["details"][key] == result["details"][key])
    check(changed["details"]["fast"] != result["details"]["fast"])
    check(changed["details"]["slow"] != result["details"]["slow"])

    equal_touch = rows.copy()
    equal_touch[-2, 4] = expected["fast_previous"]
    check(features(equal_touch, now, None)["direction"] == 1)
    no_touch = rows.copy()
    no_touch[-2, 4] = 215.
    check(features(no_touch, now, None)["direction"] == 0)
    whole_below = rows.copy()
    whole_below[-2, 1:5] = [211., 211., 212., 210.]
    check(features(whole_below, now, None)["valid"])
    check(features(whole_below, now, None)["direction"] == 0)
    no_resumption = rows.copy()
    no_resumption[-1, 1:5] = [225., 225., 226., 224.]
    check(features(no_resumption, now, None)["direction"] == 0)
    flat = rows.copy()
    flat[:, 1:5] = [100., 100., 101., 99.]
    check(features(flat, now, None)["direction"] == 0)

    check(not features(rows[:125], now, None)["valid"])
    check(not features(np.delete(rows, 10, axis=0), now, None)["valid"])
    duplicate = rows.copy()
    duplicate[10, 0] = duplicate[9, 0]
    check(not features(duplicate, now, None)["valid"])
    check(not features(rows, now + 60000, None)["valid"])
    for field, value in ((1, float("nan")), (2, 0.), (3, 1.), (4, 1e6)):
        broken = rows.copy()
        broken[10, field] = value
        check(not features(broken, now, None)["valid"])
    # ATR does not gate the price signal; the shared base alone validates its risk input.
    check(features(rows, now, dict(value=9., first=0, last=now - BAR, bars=[])) == result)
    return dict(status="passed", assertions=checks)
