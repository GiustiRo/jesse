import json
import numpy as np
from jesse.strategies import Strategy


def closed_price_context(candles, now):
    # Retain only closed 4h candles; future rows must not alter earlier signals.
    rows = candles[candles[:, 0] + 14400000 <= now]
    day = now // 86400000 * 86400000
    previous = rows[(rows[:, 0] >= day - 86400000) & (rows[:, 0] < day)]
    if len(rows) == 0 or len(previous) != 6 or len(set(previous[:, 0])) != 6:
        return 0
    price = float(rows[-1, 2])
    return 1 if price > np.max(previous[:, 3]) else -1 if price < np.min(previous[:, 4]) else 0


def causal_funding_z(rows, now):
    visible = [r for r in rows if r["available_at"] <= now][-31:]
    if len(visible) < 31:
        return None
    rates = np.array([r["rate_decimal"] for r in visible[:-1]], dtype=float)
    deviation = float(np.std(rates, ddof=0))
    if np.ptp(rates) <= 0 or deviation <= 0 or not np.isfinite(deviation):
        return None
    z = (visible[-1]["rate_decimal"] - float(np.mean(rates))) / deviation
    return float(z) if np.isfinite(z) else None


def causal_oi_status(rows, now, max_age=600000):
    visible = [r for r in rows if r["available_at"] <= now]
    if not visible:
        return "absent", None
    row = visible[-1]
    if now - row["available_at"] > max_age:
        return "stale", None
    if row["quantity_base"] == 0:
        return "zero", None
    return "valid", row["quantity_base"]


def prefix_mutation_checks():
    # Synthetic rows exercise exact availability boundaries, not market returns.
    step = 14400000
    candles = np.array([[i*step, 100., 100.+i, 101.+i, 99., 1.] for i in range(20)])
    now = 8*step
    expected = closed_price_context(candles[:8], now)
    changed = candles.copy()
    changed[8:, 2:5] = 1e9
    assert closed_price_context(candles, now) == expected == closed_price_context(changed, now)
    rows = [dict(available_at=i*60000, rate_decimal=(i%5)*.0001) for i in range(36)]
    cutoff = 31*60000
    expected_z = causal_funding_z(rows[:32], cutoff)
    changed_rows = [dict(r) for r in rows]
    for row in changed_rows[32:]:
        row["rate_decimal"] = 1e9
    assert causal_funding_z(rows, cutoff) == expected_z == causal_funding_z(changed_rows, cutoff)
    assert causal_funding_z([dict(available_at=i, rate_decimal=.0001) for i in range(31)], 31) is None
    oi = [dict(available_at=360000, quantity_base=10.),
          dict(available_at=660000, quantity_base=11.),
          dict(available_at=960000, quantity_base=12.)]
    assert causal_oi_status(oi, 359999) == ("absent", None)
    assert causal_oi_status(oi, 360000) == ("valid", 10.)
    assert causal_oi_status(oi, 959999) == causal_oi_status(oi[:2], 959999)
    changed_oi = [dict(r) for r in oi]
    changed_oi[-1]["quantity_base"] = 1e9
    assert causal_oi_status(changed_oi, 959999) == causal_oi_status(oi[:2], 959999)
    assert causal_oi_status(oi[:1], 960000) == ("valid", 10.)
    assert causal_oi_status(oi[:1], 960001) == ("stale", None)
    assert causal_oi_status([dict(available_at=360000, quantity_base=0.)], 360000) == ("zero", None)
    return 10


class ResearchFeatureAudit4h(Strategy):
    """Persist prefix/mutation checks and runtime timestamp checks without trading."""
    def before(self):
        if "checks" not in self.vars:
            self.vars["checks"] = prefix_mutation_checks()
        rows = self.get_funding_history(count=31)
        assert all(row["available_at"] <= self.time for row in rows)
        z = causal_funding_z(rows, self.time)
        assert z is None or np.isfinite(z)
        value, label = self.open_interest, self.open_interest_timestamp
        assert value is None or (label + 360000 <= self.time <= label + 960000)
        assert closed_price_context(self.candles, self.time) in (-1, 0, 1)
        self.vars["bars"] = self.vars.get("bars", 0) + 1

    def should_long(self):
        return False

    def go_long(self):
        raise AssertionError("Feature audit must never trade")

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        self.log("FEATURE_PREFIX_AUDIT " + json.dumps(self.vars, sort_keys=True))
