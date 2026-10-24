import math

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14
from strategies.BtcResearchR16LegacyBase1m import legacy_plan


def ordinal_structure(rows):
    """Prior26 excludes current extremes; flat valid ranges retain a midpoint."""
    prior = rows[-27:-1]
    upper, lower = max(float(x) for x in prior[:, 3]), min(float(x) for x in prior[:, 4])
    midpoint = upper/2.+lower/2.
    current = float(rows[-1, 2])
    if not all(math.isfinite(x) and x > 0 for x in (upper, lower, midpoint, current)):
        return None
    return dict(upper=upper, lower=lower, midpoint=midpoint, current=current)


class BtcResearchR38OrdinalBase1m(BtcResearchR11Base1m):
    """Ordinal of extreme closes, not independent attempts or failed-break learning."""
    LABEL = "abstract"
    ORDINAL = None

    def _counts(self):
        return self.vars.setdefault("r38_counts", dict(
            raw=0, raw_up=0, raw_down=0, events=0, plans=0, occupied=0,
            rejected_geometry=0, opens=0, closes=0, long_opens=0,
            short_opens=0, net=0.0, invalid_resets=0, midpoint_resets=0))

    def _machine(self):
        return self.vars.setdefault("r38_machine", dict(
            up=dict(seen=False, count=0), down=dict(seen=False, count=0)))

    def _invalidate(self, now, reason):
        for state in self._machine().values():
            state.update(seen=False, count=0)
        self.vars["r38_structure"] = None
        if not self.vars.get("r38_invalid", False):
            self._counts()["invalid_resets"] += 1
            self._log("R38_RESET", dict(label=self.LABEL, time=now,
                reason=reason, side="both", seen=False, count=0))
        self.vars["r38_invalid"] = True

    def _advance(self, structure, now):
        machine, counts = self._machine(), self._counts()
        current, midpoint = structure["current"], structure["midpoint"]
        # Reset BOTH sides at equality, before counting this close.
        for side, reset in (("up", current <= midpoint),
                            ("down", current >= midpoint)):
            state = machine[side]
            if reset:
                changed = not state["seen"] or state["count"] != 0
                state.update(seen=True, count=0)
                if changed:
                    counts["midpoint_resets"] += 1
                    self._log("R38_RESET", dict(label=self.LABEL, time=now,
                        reason="midpoint", side=side, seen=True, count=0,
                        **structure))
        side = ("up" if current > structure["upper"] else
                "down" if current < structure["lower"] else None)
        if side is None or not machine[side]["seen"]:
            return None
        state = machine[side]
        state["count"] += 1
        direction = 1 if side == "up" else -1
        counts["raw"] += 1
        counts["raw_up" if direction == 1 else "raw_down"] += 1
        selected = state["count"] == self.ORDINAL
        meta = dict(ordinal=state["count"], source_side=side,
                    signal_at=now, prior_end=now-BAR, **structure)
        self._log("R38_RAW", dict(label=self.LABEL, time=now,
            direction=direction, selected=selected, **meta))
        return dict(direction=direction, meta=meta) if selected else None

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract" and self.ORDINAL in (1, 2)
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        if now <= self.vars.get("r38_pre_at", -1):
            return
        self.vars["r38_pre_at"] = now
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["r38_structure_at"] = now
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 27)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._invalidate(now, "invalid_window")
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8), "R38_CURRENT_PRICE_PARITY"
        structure = ordinal_structure(rows)
        if structure is None:
            self._invalidate(now, "invalid_structure")
            return
        self.vars["r38_invalid"] = False
        self.vars["r38_structure"] = structure
        event = self._advance(structure, now)
        if event is None:
            return
        counts = self._counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0)+1
        # Ordinal is consumed even when account eligibility rejects this event.
        if not self.START < now < self.FINISH:
            return
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        atr = atr14(rows)
        if atr is None:
            counts["rejected_geometry"] += 1
            return
        candidate = dict(origin=self.LABEL, direction=event["direction"],
            entry=float(self.price), distance=2*atr, target_distance=None,
            hold_hours=None, order_kind="MARKET")
        plan = legacy_plan(candidate, .5*max(0.0, float(self.balance)),
                           .5*float(self.available_margin),
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        plan.update(signal_at=now, meta=event["meta"])
        self.vars["plan"] = plan
        self.vars["direction"] = plan["direction"]
        counts["plans"] += 1
        self._log("R38_PLAN", dict(label=self.LABEL, time=now,
            direction=plan["direction"], entry=plan["entry"], qty=plan["qty"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"], meta=plan["meta"]))

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        distance = plan["distance"]
        stop = entry-direction*distance
        actual_loss = qty*(distance+self.fee_rate*(entry+stop)+.001*entry)
        assert stop > 0 and math.isfinite(actual_loss)
        assert actual_loss <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        self.vars["r38_active"] = dict(plan, actual_entry=entry,
            opened_at=int(self.position.opened_at), stop=stop)
        self.vars.pop("r38_exit_reason", None)
        self.vars.pop("r38_exit_at", None)
        counts = self._counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._log("R38_OPEN", dict(label=self.LABEL, time=int(self.time),
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty, distance=distance,
            risk_budget=plan["risk_budget"], actual_loss=actual_loss, stop=stop,
            target=None, target_distance=None, hold_hours=None,
            ordinal=plan["meta"]["ordinal"], origin=plan["origin"]))
        self._observe("open")

    def _request_exit(self, reason):
        now = int(self.time)
        if not self.is_open or self.vars.get("r38_exit_at") == now:
            return
        self.vars["r38_exit_at"] = now
        self.vars["r38_exit_reason"] = reason
        self._log("R38_EXIT_REQUEST", dict(label=self.LABEL, time=now, reason=reason,
            direction=1 if self.is_long else -1,
            opened_at=int(self.position.opened_at),
            **self.vars["r38_structure"]))
        self.liquidate()

    def update_position(self):
        if not self.is_open:
            return
        now = int(self.time)
        if now >= self.FINISH:
            # Leave liquidation to the native terminal path; do not counterfeit
            # its origin/counters with a strategy MARKET request.
            return
        if now % BAR or now <= int(self.position.opened_at):
            return
        structure = self.vars.get("r38_structure")
        if self.vars.get("r38_structure_at") != now or structure is None:
            return
        # ATR is exclusively an entry metric: valid structure is sufficient.
        reset = (structure["current"] <= structure["midpoint"] if self.is_long
                 else structure["current"] >= structure["midpoint"])
        if reset:
            self._request_exit("reset")

    def on_close_position(self, order, closed_trade):
        identity = str(closed_trade.id)
        seen = self.vars.setdefault("r38_closed_ids", set())
        if identity in seen:
            return
        seen.add(identity)
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts = self._counts()
        counts["closes"] += 1
        counts["net"] += pnl
        submitted_via = getattr(order, "submitted_via", None)
        # Audited native enum spelling; unknown closes remain visibly unclassified.
        reason = self.vars.get("r38_exit_reason") or (
            "stop" if submitted_via == "stop-loss" else "native_unclassified")
        self._log("R38_CLOSE", dict(label=self.LABEL, time=int(self.time),
            trade_id=identity, net=pnl, reason=reason, submitted_via=submitted_via,
            order_type=getattr(order, "type", None)))
        self.vars["direction"] = 0
        self.vars["r38_active"] = None
        # Source ledger includes this trade before R11 may emit FINAL.
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars.setdefault("r38_exit_reason", "terminal")
        super().before_terminate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R38_SUMMARY", dict(stage=stage, label=self.LABEL,
            selected_ordinal=self.ORDINAL, hold_hours=None, tp_r=None, target=None,
            exit_mode="current channel midpoint reset",
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, **self._counts()))
