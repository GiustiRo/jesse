from strategies.ResearchV3PullbackP4h import ResearchV3PullbackP4h
from strategies.ResearchV3Base4h.pullback_features import self_checks
from strategies.ResearchV3Base4h.base_checks import self_checks as base_checks


class ResearchV3PullbackSmoke4h(ResearchV3PullbackP4h):
    START = 1598918400000
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["base_checks"] = base_checks()
            self._log_json("V3_BASE_CHECKS", self.vars["base_checks"])
            self.vars["self_checks"] = self_checks()
            self._log_json("V3_SELF_CHECKS", self.vars["self_checks"])
        super().before()
