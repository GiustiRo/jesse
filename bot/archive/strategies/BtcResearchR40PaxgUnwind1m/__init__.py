from strategies.BtcResearchR40PaxgTimingBase1m import BtcResearchR40PaxgTimingBase1m


class BtcResearchR40PaxgUnwind1m(BtcResearchR40PaxgTimingBase1m):
    MODE = "UNWIND"
    LABEL = "R40_PAXG_UNWIND"
    HOLD_HOURS = 48
    TP_R = None
