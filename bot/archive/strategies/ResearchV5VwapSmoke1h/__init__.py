from strategies.ResearchV5VwapPV1h import ResearchV5VwapPV1h
from strategies.ResearchV5Base1h.vwap_features import self_checks
from strategies.ResearchV5Base1h.common_checks import self_checks as common_checks


class ResearchV5VwapSmoke1h(ResearchV5VwapPV1h):
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = self_checks()
            self.vars["base_checks"] = common_checks()
            self._log_json("V5_SELF_CHECKS", self.vars["self_checks"])
            self._log_json("V5_BASE_CHECKS", self.vars["base_checks"])
        super().before()
