"""Finite RSI2 pullbacks; this module has no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV4Base1h import BAR, closed_window

RSI_BARS = 32
TREND_BARS = 200
TREND_OFFSET = 24


def _digest(rows):
    return hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def rsi32(candles, now):
    """Each decision seeds its own 32 closes, never an unbounded persistent RSI."""
    rows = closed_window(candles, now, RSI_BARS)
    if rows is None:
        return dict(valid=False, value=None, reason="rsi_window_invalid")
    closes = [float(x) for x in rows[:, 2]]
    differences = [b - a for a, b in zip(closes, closes[1:])]
    if not all(math.isfinite(x) for x in differences):
        return dict(valid=False, value=None, reason="rsi_arithmetic_invalid")
    gains = [max(x, 0.) for x in differences]
    losses = [max(-x, 0.) for x in differences]
    # Period two: arithmetic seed over exactly two deltas, then 29 Wilder updates.
    # Half first avoids overflowing a finite seed when two large changes agree.
    gain = seed_gain = .5 * gains[0] + .5 * gains[1]
    loss = seed_loss = .5 * losses[0] + .5 * losses[1]
    for up, down in zip(gains[2:], losses[2:]):
        gain = .5 * gain + .5 * up
        loss = .5 * loss + .5 * down
    total = gain + loss
    if not all(math.isfinite(x) and x >= 0 for x in (gain, loss, total)):
        return dict(valid=False, value=None, reason="rsi_arithmetic_invalid")
    # A flat window is neutral; no epsilon alters threshold comparisons.
    value = 50. if total == 0 else 100. * (gain / total)
    return dict(valid=True, value=float(value), seed_gain=float(seed_gain),
        seed_loss=float(seed_loss), final_gain=float(gain), final_loss=float(loss),
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=RSI_BARS,
        updates=29, sha256=_digest(rows))


def _cross_direction(current, previous, entry_level):
    """Strict prior/inclusive current inequalities encode a fresh extreme."""
    if previous > entry_level and current <= entry_level:
        return 1
    if previous < 100. - entry_level and current >= 100. - entry_level:
        return -1
    return 0


def features(candles, now, atr, entry_level=10.0):
    details = dict(reason="window_invalid")
    invalid = dict(valid=False, direction=0, reason="window_invalid", details=details)
    if not isinstance(entry_level, (int, float)) or not math.isfinite(entry_level) or not 0 < entry_level < 50:
        return dict(valid=False, direction=0, reason="entry_level_invalid",
                    details=dict(reason="entry_level_invalid"))
    rows = closed_window(candles, now, TREND_BARS + TREND_OFFSET)
    if rows is None:
        return invalid
    try:
        atr_valid = isinstance(atr, dict) and math.isfinite(atr["value"]) and atr["value"] > 0
    except (KeyError, TypeError, ValueError):
        atr_valid = False
    if not atr_valid:
        return dict(valid=False, direction=0, reason="atr_invalid",
                    details=dict(reason="atr_invalid"))
    current = rsi32(candles, now)
    # The previous RSI has its OWN seed/window, exactly as at the previous close.
    previous = rsi32(candles, now - BAR)
    if not current["valid"] or not previous["valid"]:
        return dict(valid=False, direction=0, reason="rsi_invalid",
                    details=dict(reason="rsi_invalid", current=current, previous=previous))
    close = float(rows[-1, 2])
    average = float(np.mean(rows[-TREND_BARS:, 2]))
    old_average = float(np.mean(rows[:TREND_BARS, 2]))
    if not all(math.isfinite(x) for x in (close, average, old_average)):
        return dict(valid=False, direction=0, reason="trend_arithmetic_invalid",
                    details=dict(reason="trend_arithmetic_invalid"))
    trend = 1 if close > average > old_average else -1 if close < average < old_average else 0
    crossing = _cross_direction(current["value"], previous["value"], float(entry_level))
    direction = crossing if crossing == trend else 0
    reason = "setup" if direction else "regime_reject" if crossing else "no_setup"
    details = dict(reason=reason, rsi_now=current, rsi_previous=previous,
        entry_level=float(entry_level), short_entry_level=float(100. - entry_level),
        close=close, sma200=average, sma200_24h_ago=old_average, trend=trend,
        crossing=crossing, first=int(rows[0, 0]), last=int(rows[-1, 0]),
        bars=TREND_BARS + TREND_OFFSET, sha256=_digest(rows))
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Deterministic algebra, boundaries, prefixes and future mutation; no IO."""
    count = 0

    def check(value):
        nonlocal count
        assert bool(value)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes)) * BAR + first,
            closes, closes, closes + .05, closes - .05, np.ones(len(closes))))

    def oracle(values):
        # Closed-form weights are independent of the recurrence implementation.
        delta = [float(b - a) for a, b in zip(values, values[1:])]
        up = [max(x, 0.) for x in delta]
        down = [max(-x, 0.) for x in delta]
        def weighted(changes):
            seed = (changes[0] + changes[1]) / 2
            return seed * 2. ** -29 + math.fsum(changes[j] * 2. ** -(31 - j) for j in range(2, 31))
        gain, loss = weighted(up), weighted(down)
        return 50. if gain + loss == 0 else 100 * gain / (gain + loss)

    now = 224 * BAR
    base = candles(100. + np.arange(224) * .1)
    long = base.copy()
    long[-2, 1:5] = (121.6, 121.6, 121.65, 121.55)
    long[-1, 1:5] = (120.6, 120.6, 120.65, 120.55)
    # Reflection preserves a positive OHLC window and swaps highs/lows.
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    atr = dict(value=.2)
    for case, expected in ((long, 1), (short, -1)):
        result = features(case, now, atr)
        check(result["valid"])
        check(result["direction"] == expected)
        check(result["reason"] == "setup")
        check(len(json.dumps(result, allow_nan=False)) < 1700)
        for offset in (0, 1):
            r = rsi32(case, now - offset * BAR)
            values = case[-32-offset:len(case)-offset if offset else None, 2]
            check(abs(r["value"] - oracle(values)) < 1e-12)
            check(r["updates"] == 29)
            check(r["last"] + BAR == now - offset * BAR)
            # Older prefixes must not influence either finite RSI window.
            mutated = case.copy()
            mutated[:len(case)-32-offset, 1:5] *= 1.1
            check(rsi32(mutated, now - offset * BAR) == r)
        # Replaying the previous prefix gives its independently seeded prior RSI.
        check(rsi32(case[:-1], now - BAR) == rsi32(case, now - BAR))
        future = candles([99., 98.], first=now)
        appended = np.vstack((case, future))
        check(features(appended, now, atr) == result)
        appended[-2:, 1:5] *= 10.
        check(features(appended, now, atr) == result)
        prefix = candles(np.arange(40) + 60., first=-40 * BAR)
        extended = np.vstack((prefix, case))
        check(features(extended, now, atr) == result)
        extended[:40, 1:5] *= 2.
        check(features(extended, now, atr) == result)
        check(features(case[:-1], now, atr)["valid"] is False)
        check(features(case, now + BAR // 2, atr)["valid"] is False)
        for level in (9., 10., 11.):
            check(features(case, now, atr, level)["direction"] == expected)
    for values, expected in ((np.ones(32)*100, 50.), (np.arange(32)+100, 100.),
                             (200.-np.arange(32), 0.)):
        check(rsi32(candles(values), 32*BAR)["value"] == expected)
    alternating = 100. + np.cumsum(np.tile([1., -2.], 16))
    check(abs(rsi32(candles(alternating), 32*BAR)["value"] - oracle(alternating)) < 1e-12)
    for level in (9., 10., 11.):
        check(_cross_direction(level, level+1., level) == 1)
        check(_cross_direction(level, level, level) == 0)
        check(_cross_direction(100-level, 99-level, level) == -1)
        check(_cross_direction(100-level, 100-level, level) == 0)
        check(_cross_direction(level+1., level+2., level) == 0)
    flat = candles(np.ones(224)*100)
    check(features(flat, now, atr)["direction"] == 0)
    check(features(flat, now, atr)["valid"])
    check(features(long, now, None)["valid"] is False)
    for bad in (0., -1., float("nan"), float("inf")):
        check(features(long, now, dict(value=bad))["valid"] is False)
    for level in (0., 50., float("nan"), float("inf"), None):
        check(features(long, now, atr, level)["valid"] is False)
    for column, value in ((2, float("nan")), (3, 1.), (4, 1000.), (1, 0.)):
        broken = long.copy()
        broken[-1, column] = value
        check(features(broken, now, atr)["valid"] is False)
        check(rsi32(broken, now)["valid"] is False)
    broken = long.copy()
    broken[-10, 0] -= BAR
    check(features(broken, now, atr)["valid"] is False)
    check(rsi32(long[-31:], now)["valid"] is False)
    # Exit RSI remains usable without the 224 bars required for new exposure.
    check(rsi32(long[-32:], now)["valid"])
    check(features(long[-32:], now, atr)["valid"] is False)
    return dict(status="passed", assertions=count)
