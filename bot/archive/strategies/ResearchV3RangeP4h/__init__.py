from strategies.ResearchV3Base4h import ResearchV3Base4h
from strategies.ResearchV3Base4h.range_features import features


class ResearchV3RangeP4h(ResearchV3Base4h):
    LINE = "RANGE"
    USE_OI = False
    TARGET_MODE = "frozen_mean"
    MAX_HOLD_BARS = 12
    STOP_MULTIPLIER = 2.

    def features(self, candles, now, atr):
        return features(candles, now, atr)
