from strategies.ResearchV6DeleverageP4h import ResearchV6DeleverageP4h
from strategies.ResearchV6Base4h.deleverage_features import self_checks
from strategies.ResearchV6Base4h.common_checks import self_checks as common_checks


class ResearchV6DeleverageSmoke4h(ResearchV6DeleverageP4h):
    FINISH = 1599523200000  # Seven-day technical window ending 2020-09-08 UTC.

    def before(self):
        if not self.vars.get("deleverage_smoke_checks_done"):
            sector = self_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = dict(sector=sector, common=common)
            self._log_json("V6_SELF_CHECKS", sector)
            self._log_json("V6_COMMON_CHECKS", common)
            self.vars["deleverage_smoke_checks_done"] = True
        super().before()
