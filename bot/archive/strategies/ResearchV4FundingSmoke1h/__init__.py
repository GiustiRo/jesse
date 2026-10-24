from strategies.ResearchV4FundingFP1h import ResearchV4FundingFP1h
from strategies.ResearchV4Base1h.funding_features import self_checks
from strategies.ResearchV4Base1h.common_checks import self_checks as common_checks


class ResearchV4FundingSmoke1h(ResearchV4FundingFP1h):
    FINISH = 1599523200000

    def before(self):
        if not self.vars.get("funding_smoke_checks_done"):
            self.vars["funding_smoke_checks_done"] = True
            result = self_checks()
            common = common_checks()
            self.vars["self_checks"] = dict(funding=result, common=common)
            self._log_json("V4_SELF_CHECKS", result)
            self._log_json("V4_COMMON_CHECKS", common)
        super().before()
