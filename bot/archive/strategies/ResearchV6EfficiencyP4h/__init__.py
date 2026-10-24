from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.efficiency_features import features, efficiency24


class ResearchV6EfficiencyP4h(ResearchV6Base4h):
    LINE = "EFFICIENCY"
    USE_OI = False
    EFFICIENCY_THRESHOLD = .35
    STOP_MULTIPLIER = 2.5
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 60
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.EFFICIENCY_THRESHOLD)

    def manage_position(self, atr):
        # Entry uses26prices; neutral-state exit needs only its own25valid closes.
        state = efficiency24(self.candles, int(self.time))
        if state["valid"] and ((self.is_long and state["value"] <= 0.) or
                               (self.is_short and state["value"] >= 0.)):
            self._log_json("V6_EFFICIENCY_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at),
                direction=1 if self.is_long else -1, **state))
            self.request_exit("efficiency_neutral")
