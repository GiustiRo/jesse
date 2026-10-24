import math
import numpy as np

from strategies.ResearchV2Core4h import (
    BAR, DAY, atr_window, entry_plan, h1_direction, oi_context, protective_prices,
)
from strategies.ResearchWfCore4h import price_direction as v1_direction
from strategies.ResearchWfCore4h import oi_context as v1_oi_context


def technical_self_checks():
    checks = 0
    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Exact arithmetic example: two gap TRs of 11 and twelve TRs of 2.
    rows = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(24)])
    now = 15 * BAR
    check(atr_window(rows, now)["value"] == 2.)
    gaps = rows.copy()
    gaps[1, 1:5] = [110., 110., 111., 109.]
    check(math.isclose(atr_window(gaps, now)["value"], 46 / 14, abs_tol=1e-12))
    for cutoff in (15 * BAR, 16 * BAR, 20 * BAR):
        prefix = gaps[gaps[:, 0] + BAR <= cutoff]
        changed = gaps.copy()
        changed[changed[:, 0] + BAR > cutoff, 1:5] = np.nan
        check(atr_window(prefix, cutoff) == atr_window(gaps, cutoff))
        check(atr_window(prefix, cutoff) == atr_window(changed, cutoff))
    check(atr_window(rows[:14], now) is None)
    check(atr_window(rows, now + 60000) is None)
    missing = np.delete(rows, 10, axis=0)
    check(atr_window(missing, now) is None)
    duplicate = rows.copy()
    duplicate[10, 0] = duplicate[9, 0]
    check(atr_window(duplicate, now) is None)
    for field, value in ((1, float("nan")), (2, 0.), (3, 99.), (4, 102.)):
        invalid = rows.copy()
        invalid[10, field] = value
        check(atr_window(invalid, now) is None)
    flat = rows.copy()
    flat[:, 1:5] = 100.
    check(atr_window(flat, now) is None)
    old_invalid = rows.copy()
    old_invalid[0, 1] = np.nan
    check(atr_window(old_invalid, 20 * BAR) == atr_window(rows, 20 * BAR))

    # Symmetric risk budget with asymmetric long/short round-trip fee bases.
    for side in (-1, 1):
        plan = entry_plan(100., 10000., .00045, side, 2.)
        unit = 2 + .00045 * (200 - side * 2)
        check(plan["qty"] == math.floor((200 / unit) * 1e8) / 1e8)
        check(plan["qty"] * unit <= 200. and plan["qty"] * 100 <= 10000)
        capped = entry_plan(100., 10000., .00045, side, .01)
        check(capped["qty"] == 100. and capped["planned_stop_loss"] < 200.)
        higher_fee = entry_plan(100., 10000., .0009, side, 2.)
        check(higher_fee["qty"] < plan["qty"])
        # ATR distance stays at 2 despite a hypothetical adverse fill on either side.
        fill = 100 * (1 + side * .001)
        prices = protective_prices(fill, side, 2.)
        check(math.isclose(abs(prices[0] - fill), 2., abs_tol=1e-12))
        check(math.isclose(abs(prices[1] - fill), 4., abs_tol=1e-12))
        fixed = protective_prices(fill, side, .02 * fill)
        check(math.isclose(abs(fixed[0] - fill), .02 * fill, abs_tol=1e-12))
    for args in ((100., 10000., .00045, 1, 100.), (100., 10000., .00045, -1, 50.),
                 (100., 0., .00045, 1, 2.), (100., 10000., .00045, 1, float("nan")),
                 (float("inf"), 10000., .00045, 1, 2.)):
        check(entry_plan(*args)["reason"] == "distance_invalid")
    check(entry_plan(100., 1e-12, .00045, 1, 2.)["reason"] == "qty_invalid")
    check(protective_prices(100., 0, 2.) is None)
    for direction in (-1, 1):
        prices = rows.copy()
        prices[13, 2] = 120 if direction == 1 else 80
        prices[13, 3:5] = [121, 79]
        t = 14 * BAR
        check(h1_direction(prices, t) == v1_direction(prices, t, 1) == direction)
        future = prices.copy()
        future[future[:, 0] + BAR > t, 1:5] = 1e9
        check(h1_direction(future, t) == direction)
    history = [dict(time=i * BAR, value=float(i + 1), status="valid", label=i * BAR - 600000)
               for i in range(10)]
    for lag in (0, 1):
        for t in (5 * BAR, 6 * BAR, 7 * BAR):
            check(oi_context(history, t, lag) == v1_oi_context(history, t, lag))
    for status in ("zero", "stale", "absent"):
        changed = [dict(r) for r in history]
        changed[6]["status"] = status
        check(oi_context(changed, 6 * BAR)["quality"] == status)
    changed = [dict(r) for r in history]
    changed[0]["status"] = "zero"
    check(oi_context(changed, 6 * BAR)["quality"] == "reference_invalid")
    changed = [dict(r) for r in history]
    for r in changed[7:]:
        r["value"] = 1e9
    check(oi_context(changed, 6 * BAR) == oi_context(history[:7], 6 * BAR))
    check(oi_context(history, 7 * BAR, 1) == oi_context(history, 6 * BAR))
    return dict(status="passed", assertions=checks)


def assert_real_bar(strategy):
    """Checks real prefix causality and exact H1 parity without judging trade PnL."""
    candles, now = strategy.candles, int(strategy.time)
    prefix = candles[candles[:, 0] + BAR <= now]
    assert h1_direction(candles, now) == v1_direction(candles, now, 1)
    assert atr_window(prefix, now) == atr_window(candles, now)
    current = atr_window(candles, now)
    if current is not None:
        raw = np.array(current["bars"])
        independent = [max(r[3] - r[4], abs(r[3] - prev[2]), abs(r[4] - prev[2]))
                       for prev, r in zip(raw[:-1], raw[1:])]
        assert math.isclose(sum(independent) / 14, current["value"], abs_tol=1e-9)
