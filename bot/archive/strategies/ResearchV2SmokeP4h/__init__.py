from strategies.ResearchV2Core4h import ResearchV2Core4h
from strategies.ResearchV2Core4h.technical_checks import technical_self_checks, assert_real_bar


class ResearchV2SmokeP4h(ResearchV2Core4h):
    USE_OI = False
    OI_LAG_BARS = 0
    START = 1598918400000
    FINISH = 1599696000000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = technical_self_checks()
            self._log_json("V2_SELF_CHECKS", self.vars["self_checks"])
        assert_real_bar(self)
        super().before()
