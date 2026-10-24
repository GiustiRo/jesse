from strategies.ResearchV6EfficiencyP4h import ResearchV6EfficiencyP4h
from strategies.ResearchV6Base4h.efficiency_features import self_checks
from strategies.ResearchV6Base4h.common_checks import self_checks as common_checks


class ResearchV6EfficiencySmoke4h(ResearchV6EfficiencyP4h):
    FINISH = 1599523200000  # Seven-day technical window ending2020-09-08UTC.

    def before(self):
        if not self.vars.get("efficiency_smoke_checks_done"):
            sector = self_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = dict(efficiency=sector, common=common)
            self._log_json("V6_SELF_CHECKS", sector)
            self._log_json("V6_COMMON_CHECKS", common)
            self.vars["efficiency_smoke_checks_done"] = True
        super().before()
