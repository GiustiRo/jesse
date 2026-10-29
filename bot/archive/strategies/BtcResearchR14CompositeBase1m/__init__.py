import math
import numpy as np

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import (
    BAR, closed_window, breadth_signal, breadth_state, atr14, entry_plan,
)
from strategies.BtcResearchR12JumpBase1m import closed_hours, jump_state


def select_origin(core_event, impulse_event):
    """One order at most: aligned events coalesce to CORE; disagreement is cash."""
    assert core_event in (-1, 0, 1) and impulse_event in (-1, 0, 1)
    if core_event and impulse_event:
        if core_event == impulse_event:
            return core_event, "CORE", "aligned"
        return 0, None, "conflict"
    if core_event:
        return core_event, "CORE", "core_only"
    if impulse_event:
        return impulse_event, "IMPULSE", "impulse_only"
    return 0, None, "none"


def management_policy(mode, origin):
    """Preserve parent management, rather than selecting it from later performance."""
    assert mode in ("FIXED", "STATE") and origin in ("CORE", "IMPULSE")
    if mode == "STATE" and origin == "CORE":
        return dict(target_r=None, hold_bars=180, exit_opposite=True)
    return dict(target_r=2, hold_bars=12, exit_opposite=False)


class BtcResearchR14CompositeBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def _ledger(self):
        return self.vars.setdefault("source_ledger", {
            "CORE": dict(fills=0, closes=0, net=0.0),
            "IMPULSE": dict(fills=0, closes=0, net=0.0),
        })

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("FIXED", "STATE")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 26)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["jump_state"] = 0
            self.vars["core_state"] = 0
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # CORE state must remain available for B's opposite-state exit even if
        # hourly history is missing. Shared hourly validity gates new entries only.
        core_event = breadth_signal(rows)
        self.vars["core_state"] = breadth_state(rows[-25:, 2])
        hourly = closed_hours(self.get_candles(self.exchange, self.symbol, "1h"), now)
        if hourly is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["jump_state"] = 0
            return
        assert math.isclose(float(hourly[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)

        # Both machines advance before occupancy or arbitration. No old blocked
        # event can be queued for the next free minute or four-hour close.
        atr = atr14(rows)
        current_jump = jump_state(hourly, atr, float(self.price))
        previous_jump = self.vars.get("jump_state", 0)
        self.vars["jump_state"] = current_jump
        impulse_event = current_jump if current_jump and current_jump != previous_jump else 0
        direction, origin, arbitration = select_origin(core_event, impulse_event)

        if not self.START < now < self.FINISH:
            return
        self.vars["core_events"] = self.vars.get("core_events", 0)+int(bool(core_event))
        self.vars["impulse_events"] = self.vars.get("impulse_events", 0)+int(bool(impulse_event))
        key = "arbitration_"+arbitration
        self.vars[key] = self.vars.get(key, 0)+1
        if direction:
            self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            if core_event or impulse_event:
                self.vars["occupied"] = self.vars.get("occupied", 0)+1
                self.vars["core_discarded"] = self.vars.get("core_discarded", 0)+int(bool(core_event))
                self.vars["impulse_discarded"] = self.vars.get("impulse_discarded", 0)+int(bool(impulse_event))
            return
        if not direction or atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        # B inherits this hypothetical 2R admission guard from R10 even though
        # its actual position has no take-profit. Preserve that parent boundary.
        if self.price+direction*2*plan["distance"] <= 0:
            return
        policy = management_policy(self.MODE, origin)
        self.vars["plan"] = dict(plan, origin=origin, policy=policy)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        plan = self.vars["plan"]
        origin = plan["origin"]
        policy = dict(plan["policy"])
        assert self.vars.get("position_origin") is None
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        assert qty*(plan["distance"]+self.fee_rate*(entry+stop)) <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        if policy["target_r"] is not None:
            self.take_profit = qty, entry+direction*policy["target_r"]*plan["distance"]
        self.vars["position_origin"] = origin
        self.vars["position_policy"] = policy
        self._ledger()[origin]["fills"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")
        self._log("R14_COMPOSITE_OPEN", dict(
            time=int(self.time), mode=self.MODE, origin=origin, direction=direction,
            entry=entry, qty=qty, stop=stop, policy=policy))

    def update_position(self):
        now = int(self.time)
        if now % BAR:
            return
        policy = self.vars["position_policy"]
        opened = int(self.position.opened_at)
        if now-opened >= policy["hold_bars"]*BAR:
            self.liquidate()
            return
        if now <= opened or not policy["exit_opposite"]:
            return
        state = self.vars.get("core_state", 0)
        if (self.is_long and state == -1) or (self.is_short and state == 1):
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        origin = self.vars["position_origin"]
        ledger = self._ledger()[origin]
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        ledger["closes"] += 1
        ledger["net"] += pnl
        self.vars["position_origin"] = None
        self.vars["position_policy"] = None
        self._log("R14_COMPOSITE_CLOSE", dict(time=int(self.time), origin=origin, net=pnl))
        # The parent may emit FINAL inside this callback. Its terminal source
        # ledger must already contain this close, including final fees/funding.
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        ledger = self._ledger()
        self._log("R14_COMPOSITE_STATS", dict(
            stage=stage, mode=self.MODE, sources=ledger,
            fills=sum(v["fills"] for v in ledger.values()),
            closes=sum(v["closes"] for v in ledger.values()),
            net=sum(v["net"] for v in ledger.values()),
            core_events=self.vars.get("core_events", 0),
            impulse_events=self.vars.get("impulse_events", 0),
            aligned=self.vars.get("arbitration_aligned", 0),
            conflicts=self.vars.get("arbitration_conflict", 0),
            core_only=self.vars.get("arbitration_core_only", 0),
            impulse_only=self.vars.get("arbitration_impulse_only", 0),
            core_discarded=self.vars.get("core_discarded", 0),
            impulse_discarded=self.vars.get("impulse_discarded", 0)))
