from strategies.BtcResearchR40PaxgTimingBase1m import BtcResearchR40PaxgTimingBase1m


class BtcResearchR40PaxgClock1m(BtcResearchR40PaxgTimingBase1m):
    MODE = "CLOCK"
    LABEL = "R40_PAXG_CLOCK"
    HOLD_HOURS = 48
    TP_R = None
