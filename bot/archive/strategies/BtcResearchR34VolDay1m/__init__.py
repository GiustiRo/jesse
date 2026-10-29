from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR34VolNormal1m import leaf_event, invalidate_leaf


class BtcResearchR34VolDay1m(BtcResearchR32SpecialistBase1m):
    LABEL = "VOL_DAY"
    HOLD_HOURS = 48
    TP_R = None

    def _event(self, rows, now):
        return leaf_event(self, rows, now, False)

    def _invalid_event(self, now):
        invalidate_leaf(self, now)
