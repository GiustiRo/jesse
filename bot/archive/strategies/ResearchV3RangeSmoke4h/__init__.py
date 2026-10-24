from strategies.ResearchV3RangeP4h import ResearchV3RangeP4h
from strategies.ResearchV3Base4h.range_features import self_checks
from strategies.ResearchV3Base4h.base_checks import self_checks as base_checks


class ResearchV3RangeSmoke4h(ResearchV3RangeP4h):
    START = 1598918400000
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["base_checks"] = base_checks()
            self._log_json("V3_BASE_CHECKS", self.vars["base_checks"])
            self.vars["self_checks"] = self_checks()
            self._log_json("V3_SELF_CHECKS", self.vars["self_checks"])
        super().before()
