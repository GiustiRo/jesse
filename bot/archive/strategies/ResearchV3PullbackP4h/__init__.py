from strategies.ResearchV3Base4h import ResearchV3Base4h
from strategies.ResearchV3Base4h.pullback_features import features as pullback_features


class ResearchV3PullbackP4h(ResearchV3Base4h):
    LINE = "PULLBACK"
    TARGET_MODE = "r_multiple"
    REWARD_MULTIPLE = 3.
    MAX_HOLD_BARS = 18
    STOP_MULTIPLIER = 2.
    USE_OI = False

    def features(self, candles, now, atr):
        return pullback_features(candles, now, atr)
