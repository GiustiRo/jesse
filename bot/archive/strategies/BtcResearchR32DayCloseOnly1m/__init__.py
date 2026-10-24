from strategies.BtcResearchR32DayAcceptanceBase1m import BtcResearchR32DayAcceptanceBase1m


class BtcResearchR32DayCloseOnly1m(BtcResearchR32DayAcceptanceBase1m):
    LABEL = "A_CLOSE_ONLY"
    REQUIRE_ACCEPTANCE = False
