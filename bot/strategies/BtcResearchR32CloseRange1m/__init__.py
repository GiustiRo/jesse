from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR32InsideRange1m import containment_event


class BtcResearchR32CloseRange1m(BtcResearchR32SpecialistBase1m):
    LABEL = "C_CLOSE_ONLY"
    HOLD_HOURS = 24
    TP_R = None

    def _event(self, rows, now):
        return containment_event(rows, now, False)
