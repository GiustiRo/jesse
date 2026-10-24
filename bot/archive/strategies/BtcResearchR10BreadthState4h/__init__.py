from strategies.BtcResearchR10Base4h import (
    BtcResearchR10Base4h, BAR, breadth_state, closed_window,
)


class BtcResearchR10BreadthState4h(BtcResearchR10Base4h):
    """Transfer a known state-exit policy; entries and initial risk stay frozen."""
    MODE = "BREADTH"

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        distance = plan["distance"]
        stop = entry - direction * distance
        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        # No profit-target order: this entire management policy is the intervention.
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._log("R10B_ENTRY", dict(time=int(self.time), direction=direction, entry=entry,
                                    qty=qty, stop=stop, target=None, plan=plan))

    def update_position(self):
        now = int(self.time)
        opened = int(self.position.opened_at)
        if now - opened >= 180 * BAR:
            self.liquidate()
            return
        if now <= opened:
            return
        rows = closed_window(self.candles, now, 26)
        if rows is None:
            return
        state = breadth_state(rows[-25:, 2])
        if (self.is_long and state == -1) or (self.is_short and state == 1):
            self.liquidate()
