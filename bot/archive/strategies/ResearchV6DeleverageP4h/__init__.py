from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.deleverage_features import features as deleverage_features


class ResearchV6DeleverageP4h(ResearchV6Base4h):
    LINE = "DELEVERAGING"
    USE_OI = False
    OI_RULE = "declining"
    OI_DECLINE_FRACTION = .02
    DISPLACEMENT_MULTIPLIER = 2.
    STOP_MULTIPLIER = 2.
    REWARD_MULTIPLE = 2.
    TARGET_MODE = "r_multiple"
    MAX_HOLD_BARS = 12
    ATR_OFFSET_BARS = 0

    def features(self, candles, now, atr):
        return deleverage_features(candles, now, atr, self.DISPLACEMENT_MULTIPLIER)
