from strategies.ResearchV4OscillatorP1h import ResearchV4OscillatorP1h
from strategies.ResearchV4Base1h.oscillator_features import self_checks
from strategies.ResearchV4Base1h.common_checks import self_checks as base_checks


class ResearchV4OscillatorSmoke1h(ResearchV4OscillatorP1h):
    FINISH = 1599523200000  # Seven-day technical window ending 2020-09-08 UTC.

    def before(self):
        if not self.vars.get("v4_smoke_checks_done"):
            sector = self_checks()
            common = base_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = sector
            self.vars["v4_base_checks"] = common
            self._log_json("V4_SELF_CHECKS", sector)
            self._log_json("V4_BASE_CHECKS", common)
            self.vars["v4_smoke_checks_done"] = True
        super().before()
