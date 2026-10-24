from strategies.BtcResearchR16K1001LongOnly1m import BtcResearchR16K1001LongOnly1m
from strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_plan
from strategies.BtcResearchR16K1001QuotaBase1m import QUOTA
from strategies.BtcResearchR10Base4h import BAR


class BtcResearchR16K1001LongMarket1m(BtcResearchR16K1001LongOnly1m):
    """K long entry-policy ablation; original signal, quota and runner unchanged.

    Validate the complete frozen LIMIT recipe first. Only its requested entry
    changes to the exact decision price; native inherited submission handles
    MARKET execution. Compact terminal rows expose the existing real ledger,
    never hypothetical fills or a new economic decision.
    """
    ENTRY_POLICY = "MARKET_AT_DECISION_CLOSE"

    def _prepare_entry(self):
        now = int(self.time)
        if (now % BAR or self.vars.get("decision_at") != now
                or self.is_open or self.entry_orders
                or self.vars.get("last_exit_at") == now
                or not self.START < now < self.FINISH):
            return 0
        if self.vars.get("prepared_at") == now:
            return self.vars.get("direction", 0)
        self.vars["prepared_at"] = now
        rows = self.vars.get("legacy_rows")
        if rows is None:
            return 0
        # Includes H < close <= H+ATR and distance < H: MARKET must not relax
        # any original signal geometry, even when the new price is higher.
        original = legacy_long(rows)
        if original is None:
            return 0
        decision_price = float(self.price)
        candidate = dict(original, entry=decision_price, order_kind="MARKET")
        capital = max(0.0, float(self.balance))
        margin = float(self.available_margin)
        # Reprice sizing, fees and reserve at MARKET, with the same inactive
        # half-account allocation as LIMIT. Never recycle its quantity.
        plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            return 0
        self.vars["plan"] = dict(plan, signal_at=now, expiry=now+BAR)
        self.vars["direction"] = plan["direction"]
        self.vars["signals"] = self.vars.get("signals", 0)+1
        self._log("K1001_QUOTA_PLAN", dict(
            time=now, group=self.GROUP, origin=plan["origin"],
            qty=plan["qty"], risk_budget=plan["risk_budget"],
            capital_total=capital, capital_scaled=QUOTA*capital,
            margin_total=margin, margin_scaled=QUOTA*margin,
            planned_loss=plan["planned_loss"],
            planned_stop_fees=plan["planned_stop_fees"],
            reserve=plan["reserve"], gross_limited=plan["gross_limited"],
            margin_limited=plan["margin_limited"], expiry=now+BAR))
        # One record per admitted plan; memo calls produce no extra record.
        self._log("K1001_MARKET_PLAN", dict(
            time=now, entry_policy=self.ENTRY_POLICY, origin=plan["origin"],
            original_trigger_level=float(original["entry"]),
            decision_price=decision_price,
            original_distance=float(original["distance"]),
            requested_entry=plan["entry"], qty=plan["qty"],
            risk_budget=plan["risk_budget"], expiry=now+BAR))
        return plan["direction"]

    def _emit(self, stage):
        super()._emit(stage)
        state = self._quota_state()
        # Split the fixed schemas by origin and year so each complete record
        # stays below 1900 characters, beneath the MCP reader's 2000 cut.
        # Stages are snapshots, not additional ledger observations.
        self._log("K1001_MARKET_SUMMARY", dict(
            stage=stage, policy=self.ENTRY_POLICY,
            trace_errors=state["errors"], open_trace=state["active"] is not None))
        for origin, row in state["sources"].items():
            self._log("K1001_MARKET_SOURCE", dict(stage=stage, origin=origin, **row))
        for axis in ("open_years", "close_years"):
            for year, origins in state[axis].items():
                for origin, row in origins.items():
                    self._log("K1001_MARKET_COHORT", dict(
                        stage=stage, axis=axis, year=year, origin=origin, **row))
