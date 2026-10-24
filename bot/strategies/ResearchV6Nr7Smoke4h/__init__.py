from strategies.ResearchV6Nr7P4h import ResearchV6Nr7P4h
from strategies.ResearchV6Base4h.nr7_features import self_checks as sector_checks
from strategies.ResearchV6Base4h.common_checks import self_checks as common_checks


class ResearchV6Nr7Smoke4h(ResearchV6Nr7P4h):
    FINISH = 1599523200000  # Seven-day technical window; source economic rules stay unchanged.

    def before(self):
        if not self.vars.get("nr7_smoke_checks_done"):
            sector = sector_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = dict(sector=sector, common=common)
            self._log_json("V6_SELF_CHECKS", sector)
            self._log_json("V6_COMMON_CHECKS", common)
            self.vars["nr7_smoke_checks_done"] = True
        super().before()
