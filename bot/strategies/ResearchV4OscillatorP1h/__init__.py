from strategies.ResearchV4Base1h import ResearchV4Base1h
from strategies.ResearchV4Base1h.oscillator_features import features, rsi32


class ResearchV4OscillatorP1h(ResearchV4Base1h):
    LINE = "OSCILLATOR"
    USE_OI = False
    RSI_ENTRY_LEVEL = 10.
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 24
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.RSI_ENTRY_LEVEL)

    def manage_position(self, atr):
        # Core already prioritizes calendar/hold and requires a post-fill close.
        # Exit needs only 32 valid bars, never the entry trend's 224-bar history.
        oscillator = rsi32(self.candles, int(self.time))
        if oscillator["valid"] and ((self.is_long and oscillator["value"] >= 50.) or
                                   (self.is_short and oscillator["value"] <= 50.)):
            self.request_exit("rsi_normalized")
