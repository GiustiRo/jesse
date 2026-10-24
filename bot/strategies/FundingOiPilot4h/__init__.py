import json
from strategies.FundingWfPilotBase4h import FundingWfPilotBase4h


class FundingOiPilot4h(FundingWfPilotBase4h):
    """Exploratory ablation: rising OI confirms the unchanged price breakout."""
    FUNDING_FILTER = False

    def before(self):
        super().before()
        value = self.open_interest
        label = self.open_interest_timestamp
        audit = self.vars.setdefault("oi_audit", {
            "bars": 0, "observed": 0, "missing": 0, "zero_values": 0,
            "eligible_before_oi": 0, "blocked_missing": 0,
            "blocked_nonrising": 0, "passed": 0,
        })
        audit["bars"] += 1
        if value is not None:
            # Archive convention is label+6m; data older than 10m after
            # availability must be None. These assertions do not certify
            # original historical publication times.
            assert label is not None and value >= 0
            assert label + 360_000 <= self.time <= label + 960_000
            audit["observed"] += 1
            # The archive permits literal zero quantities. Preserve provenance
            # in a separate counter but never use zero as a valid reference.
            if value == 0:
                audit["zero_values"] += 1
                value = None
        else:
            assert label is None
            audit["missing"] += 1
        history = self.vars.setdefault("oi_history", [])
        history.append((int(self.time), value))
        # Seven 4h observations span exactly 24h. The first day is a
        # deliberate initialization exclusion; no backfill or interpolation.
        history[:] = history[-7:]
        old = history[0][1] if len(history) == 7 and history[0][0] == self.time - self.DAY_MS else None
        valid = value is not None and old is not None
        rising = valid and value > old
        context = self.vars["context"]
        if context["allowed"]:
            audit["eligible_before_oi"] += 1
            if not valid:
                audit["blocked_missing"] += 1
            elif not rising:
                audit["blocked_nonrising"] += 1
            else:
                audit["passed"] += 1
        context["allowed"] = context["allowed"] and rising

    def before_terminate(self):
        assert self.vars["oi_audit"]["observed"] > 0
        self.log("OI_PILOT_AUDIT " + json.dumps(self.vars["oi_audit"], sort_keys=True))
        super().before_terminate()
