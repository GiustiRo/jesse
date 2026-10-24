from strategies.ResearchV5Base4h import ResearchV5Base4h
from strategies.ResearchV5Base4h.cross_features import cross_state, features


class ResearchV5CrossP4h(ResearchV5Base4h):
    LINE = "CROSS"
    USE_OI = False
    FAST_PERIOD = 20
    SLOW_PERIOD = 80
    STOP_MULTIPLIER = 3.
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ATR_OFFSET_BARS = 0

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.FAST_PERIOD, self.SLOW_PERIOD)

    def manage_position(self, atr):
        # The core already prioritizes calendar/holding and post-fill timing.
        # This exit cross has no ATR/OI requirement and never schedules reversal.
        state = cross_state(self.candles, int(self.time), self.FAST_PERIOD, self.SLOW_PERIOD)
        if state["valid"] and ((self.is_long and state["direction"] == -1) or
                               (self.is_short and state["direction"] == 1)):
            self._log_json("V5_CROSS_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at),
                direction=1 if self.is_long else -1, **state["details"]))
            self.request_exit("opposite_cross")
