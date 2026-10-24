from strategies.ResearchV4ShockPV1h import ResearchV4ShockPV1h
from strategies.ResearchV4Base1h.shock_features import self_checks
from strategies.ResearchV4Base1h.common_checks import self_checks as common_checks


class ResearchV4ShockSmoke1h(ResearchV4ShockPV1h):
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            # Pure source checks precede motor context; this smoke adds no signal rule.
            self.vars["self_checks"] = self_checks()
            self.vars["base_checks"] = common_checks()
            self._log_json("V4_SELF_CHECKS", self.vars["self_checks"])
            self._log_json("V4_BASE_CHECKS", self.vars["base_checks"])
        super().before()
