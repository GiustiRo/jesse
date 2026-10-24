from strategies.ResearchV3Base4h import ResearchV3Base4h
from strategies.ResearchV3Base4h.channel_features import features as channel_features
from strategies.ResearchV3Base4h.channel_features import post_entry_extremes, trailing_level


class ResearchV3ChannelP4h(ResearchV3Base4h):
    LINE = "CHANNEL"
    TARGET_MODE = "none"
    MAX_HOLD_BARS = 42
    STOP_MULTIPLIER = 2.
    TRAIL_MULTIPLIER = 3.
    USE_OI = False

    def features(self, candles, now, atr):
        return channel_features(candles, now, atr)

    def on_v3_open(self):
        trade = self.vars["v3_trade"]
        self.vars["channel_trailing"] = dict(high=trade["entry_fill"], low=trade["entry_fill"],
                                             last_evaluated=trade["entry_at"])

    def _trailing_invalid(self, reason):
        # These are position-management events, separate from entry-opportunity quality.
        context = self.vars["context"]
        for side in ("all", "long" if self.is_long else "short"):
            bucket = self._bucket(context["month"], side)
            bucket["flags"]["trailing_data_invalid"] = bucket["flags"].get("trailing_data_invalid", 0) + 1
        self._log_json("V3_TRAILING_SKIPPED", dict(time=int(self.time), reason=reason))

    def manage_position(self, atr):
        trade = self.vars["v3_trade"]
        state = self.vars["channel_trailing"]
        now = int(self.time)
        if now <= state["last_evaluated"]:
            return
        state["last_evaluated"] = now
        extremes = post_entry_extremes(self.candles, now, trade["entry_at"], state["high"], state["low"])
        if extremes is None:
            self._trailing_invalid("post_entry_history_invalid")
            return
        state["high"], state["low"] = extremes
        if atr is None:
            self._trailing_invalid("atr_invalid")
            return
        direction = 1 if self.is_long else -1
        candidate = trailing_level(direction, state["high"], state["low"], atr["value"],
                                   trade["stop_price"], self.TRAIL_MULTIPLIER)
        if candidate is None:
            self._trailing_invalid("trailing_level_invalid")
            return
        if direction * (candidate - trade["stop_price"]) > 0:
            self._log_json("V3_TRAIL_CONTEXT", dict(time=now, high=state["high"], low=state["low"],
                atr=atr["value"], old_stop=trade["stop_price"], candidate=candidate))
            # Base handles a crossed new level with MARKET now; no retroactive stop fill.
            self.replace_stop(candidate)
