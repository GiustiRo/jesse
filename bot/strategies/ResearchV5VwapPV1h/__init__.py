from strategies.ResearchV5Base1h import ResearchV5Base1h
from strategies.ResearchV5Base1h.vwap_features import features as vwap_features, exit_state


class ResearchV5VwapPV1h(ResearchV5Base1h):
    LINE = "VWAP"
    USE_OI = False
    ATR_OFFSET_BARS = 0
    STOP_MULTIPLIER = 2.
    TARGET_MODE = "none"
    MAX_HOLD_BARS = 24
    BAND_MULTIPLIER = 2.

    def features(self, candles, now, atr):
        return vwap_features(candles, now, atr, self.BAND_MULTIPLIER)

    def manage_position(self, atr):
        # Exit normalization needs24 valid volume bars, not entry25 or a valid ATR.
        if int(self.time) <= int(self.position.opened_at):
            return
        result = exit_state(self.candles, int(self.time), 1 if self.is_long else -1)
        if not result["valid"]:
            self._log_json("V5_VWAP_EXIT_SKIPPED", dict(time=int(self.time), reason="vwap_invalid"))
        elif result["exit"]:
            self._log_json("V5_VWAP_EXIT_CONTEXT", dict(time=int(self.time), **result["details"]))
            self.request_exit("vwap_normalization")
