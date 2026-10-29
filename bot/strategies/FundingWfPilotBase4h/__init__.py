import json

import numpy as np

from jesse import utils
from jesse.strategies import Strategy


class FundingWfPilotBase4h(Strategy):
    """Frozen mechanical price control; no claim of a demonstrated trading edge."""

    FUNDING_FILTER = False
    DAY_MS = 86_400_000
    STOP_FRACTION = 0.02
    TARGET_FRACTION = 0.04
    RISK_PERCENT = 2
    MAX_HOLD_MS = DAY_MS
    REFERENCE_EVENTS = 30
    EXTREME_Z = 2.0

    def before(self):
        day = int(self.time) // self.DAY_MS * self.DAY_MS
        candles = self.candles
        # Only the previous completed UTC day supplies the breakout boundaries.
        previous = candles[(candles[:, 0] >= day - self.DAY_MS) & (candles[:, 0] < day)]
        direction = 0
        if len(previous) == 6 and len(set(previous[:, 0])) == 6:
            assert max(previous[:, 0]) + 4 * 3_600_000 <= self.time
            upper = float(np.max(previous[:, 3]))
            lower = float(np.min(previous[:, 4]))
            direction = 1 if self.price > upper else -1 if self.price < lower else 0

        rows = self.get_funding_history(count=self.REFERENCE_EVENTS + 1)
        assert all(row["available_at"] <= self.time for row in rows)
        valid = False
        adverse = False
        zscore = None
        if len(rows) == self.REFERENCE_EVENTS + 1:
            latest = rows[-1]
            reference = np.array([row["rate_decimal"] for row in rows[:-1]], dtype=float)
            deviation = float(np.std(reference, ddof=0))
            # Equal historical rates do not define a standardized surprise.
            # This frozen pilot requires nonzero dispersion in filtered entries.
            if np.ptp(reference) > 0 and deviation > 0 and np.isfinite(deviation):
                zscore = (latest["rate_decimal"] - float(np.mean(reference))) / deviation
                valid = bool(np.isfinite(zscore))
                adverse = valid and (
                    (direction == 1 and latest["rate_decimal"] > 0 and zscore > self.EXTREME_Z)
                    or (direction == -1 and latest["rate_decimal"] < 0 and zscore < -self.EXTREME_Z)
                )

        opportunity = direction != 0 and self.vars.get("entry_day") != day and self.is_close
        allowed = opportunity and (not self.FUNDING_FILTER or (valid and not adverse))
        self.vars["context"] = {"day": day, "direction": direction, "allowed": allowed}
        audit = self.vars.setdefault("audit", {
            "bars": 0, "price_opportunities": 0, "adverse_blocks": 0,
            "unavailable_blocks": 0, "entries": 0,
        })
        audit["bars"] += 1
        if opportunity:
            audit["price_opportunities"] += 1
            if self.FUNDING_FILTER and not valid:
                audit["unavailable_blocks"] += 1
            elif self.FUNDING_FILTER and adverse:
                audit["adverse_blocks"] += 1

    def should_long(self):
        context = self.vars["context"]
        return context["allowed"] and context["direction"] == 1

    def should_short(self):
        context = self.vars["context"]
        return context["allowed"] and context["direction"] == -1

    def _enter(self, direction):
        stop = self.price * (1 - direction * self.STOP_FRACTION)
        # Budget price loss plus both execution fees at the stop; funding and
        # slippage remain additional costs. Cap notional at available capital.
        capital = self.available_margin
        unit_loss = abs(self.price - stop) + self.fee_rate * (self.price + stop)
        notional = min(capital, capital * self.RISK_PERCENT / 100 / unit_loss * self.price)
        qty = utils.size_to_qty(notional, self.price, precision=8)
        self.vars["entry_day"] = self.vars["context"]["day"]
        if direction == 1:
            self.buy = qty, self.price
        else:
            self.sell = qty, self.price

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        direction = 1 if self.is_long else -1
        entry = self.position.entry_price
        self.stop_loss = abs(self.position.qty), entry * (1 - direction * self.STOP_FRACTION)
        self.take_profit = abs(self.position.qty), entry * (1 + direction * self.TARGET_FRACTION)
        self.vars["audit"]["entries"] += 1

    def update_position(self):
        if self.time - self.position.opened_at >= self.MAX_HOLD_MS:
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        self.log("PILOT_AUDIT " + json.dumps(self.vars.get("audit", {}), sort_keys=True))
