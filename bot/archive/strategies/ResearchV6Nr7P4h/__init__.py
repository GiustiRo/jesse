from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.nr7_features import features


class ResearchV6Nr7P4h(ResearchV6Base4h):
    LINE = "NR7"
    USE_OI = False
    OI_RULE = "rising"
    NARROW_WINDOW = 7
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    TARGET_MODE = "r_multiple"
    REWARD_MULTIPLE = 3.
    MAX_HOLD_BARS = 24

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.NARROW_WINDOW)
