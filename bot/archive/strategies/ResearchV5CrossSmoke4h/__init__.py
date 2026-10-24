from strategies.ResearchV5CrossP4h import ResearchV5CrossP4h
from strategies.ResearchV5Base4h.cross_features import self_checks
from strategies.ResearchV5Base4h.common_checks import self_checks as base_checks


class ResearchV5CrossSmoke4h(ResearchV5CrossP4h):
    FINISH = 1599523200000  # Fixed seven-day technical window, 2020-09-08 UTC.

    def before(self):
        if not self.vars.get("v5_cross_checks_done"):
            sector = self_checks()
            common = base_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = sector
            self.vars["v5_base_checks"] = common
            self._log_json("V5_SELF_CHECKS", sector)
            self._log_json("V5_BASE_CHECKS", common)
            self.vars["v5_cross_checks_done"] = True
        super().before()
