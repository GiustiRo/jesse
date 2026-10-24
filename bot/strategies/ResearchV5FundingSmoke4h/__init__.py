from strategies.ResearchV5FundingFP4h import ResearchV5FundingFP4h
from strategies.ResearchV5Base4h.funding_features import self_checks
from strategies.ResearchV5Base4h.common_checks import self_checks as common_checks


class ResearchV5FundingSmoke4h(ResearchV5FundingFP4h):
    FINISH = 1599523200000

    def before(self):
        if not self.vars.get("funding_smoke_checks_done"):
            sector = self_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["funding_smoke_checks_done"] = True
            self.vars["self_checks"] = dict(sector=sector, common=common)
            self._log_json("V5_SELF_CHECKS", sector)
            self._log_json("V5_COMMON_CHECKS", common)
        super().before()
