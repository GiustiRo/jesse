import math

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14
from strategies.BtcResearchR16LegacyBase1m import legacy_plan


class BtcResearchR32SpecialistBase1m(BtcResearchR11Base1m):
    """Frozen one-percent specialist execution; leaves define causal events only."""
    LABEL = "abstract"
    HOLD_HOURS = 48
    TP_R = 2.0

    def _event(self, rows, now):
        raise NotImplementedError

    def _invalid_event(self, now):
        # Stateful leaves may invalidate an episode; rolling leaves need no state.
        pass

    def _r32_counts(self):
        return self.vars.setdefault("r32_counts", dict(events=0, plans=0,
            occupied=0, rejected_geometry=0, opens=0, closes=0,
            long_opens=0, short_opens=0, net=0.0))

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract"
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - .00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            assert self.HOLD_HOURS in (24, 48)
            assert self.TP_R in (None, 2.0)
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"),
                             now, 64)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self._invalid_event(now)
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8)
        # Evaluate/consume before occupancy and account guards, identically in
        # both leaves of a comparison. Never defer an occupied event to later.
        event = self._event(rows, now)
        if event is None:
            return
        direction = event["direction"]
        assert direction in (-1, 1)
        counts = self._r32_counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if not self.START < now < self.FINISH:
            return
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        atr = atr14(rows)
        if atr is None:
            counts["rejected_geometry"] += 1
            return
        entry = float(self.price)
        distance = 2 * atr
        target_distance = None if self.TP_R is None else self.TP_R * distance
        if target_distance is not None and entry + direction * target_distance <= 0:
            counts["rejected_geometry"] += 1
            return
        candidate = dict(origin=self.LABEL, direction=direction, entry=entry,
            distance=distance, target_distance=target_distance,
            hold_hours=self.HOLD_HOURS, order_kind="MARKET")
        plan = legacy_plan(candidate, .5 * max(0.0, float(self.balance)),
                           .5 * float(self.available_margin),
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        plan.update(signal_at=now, meta=event.get("meta", {}))
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        counts["plans"] += 1
        self._log("R32_PLAN", dict(label=self.LABEL, time=now,
            direction=direction, entry=entry, distance=distance,
            qty=plan["qty"], risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"], meta=plan["meta"]))

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        stop = entry - direction * plan["distance"]
        unit = plan["distance"] + self.fee_rate * (entry + stop) + .001 * entry
        assert stop > 0 and qty * unit <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        if plan["target_distance"] is not None:
            target = entry + direction * plan["target_distance"]
            assert target > 0
            self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        counts = self._r32_counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self._log("R32_OPEN", dict(label=self.LABEL, time=int(self.time),
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty,
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            stop=stop, target_distance=plan["target_distance"],
            hold_hours=plan["hold_hours"]))
        self._observe("open")

    def update_position(self):
        # Management remains on closed four-hour clocks; MARKET entry at that
        # same clock cannot trigger its own time exit.
        now = int(self.time)
        if now % BAR == 0 and now - int(self.position.opened_at) >= self.HOLD_HOURS * 3600000:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        counts = self._r32_counts()
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts["closes"] += 1
        counts["net"] += pnl
        self.vars["direction"] = 0
        self._log("R32_CLOSE", dict(label=self.LABEL, time=int(self.time), net=pnl))
        # Source totals must precede any terminal observer emission.
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R32_SUMMARY", dict(stage=stage, label=self.LABEL,
            hold_hours=self.HOLD_HOURS, tp_r=self.TP_R,
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, **self._r32_counts()))
