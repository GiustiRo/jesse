from strategies.ResearchV4Base1h import ResearchV4Base1h
from strategies.ResearchV4Base1h.shock_features import features as shock_features


class ResearchV4ShockPV1h(ResearchV4Base1h):
    LINE = "SHOCK"
    USE_OI = False
    ATR_OFFSET_BARS = 1
    STOP_MULTIPLIER = 1.
    REWARD_MULTIPLE = 1.
    TARGET_MODE = "r_multiple"
    MAX_HOLD_BARS = 6
    # Signal neighbors change only these two; risk neighbors change only STOP.
    SHOCK_MULTIPLIER = 2.
    VOLUME_MULTIPLIER = 2.

    def features(self, candles, now, atr):
        return shock_features(candles, now, atr, self.SHOCK_MULTIPLIER, self.VOLUME_MULTIPLIER)
