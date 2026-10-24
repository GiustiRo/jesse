from strategies.ResearchV4Base1h import ResearchV4Base1h
from strategies.ResearchV4Base1h.funding_features import features, ma24_state


class ResearchV4FundingFP1h(ResearchV4Base1h):
    LINE = "FUNDING_RESET"
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 72
    TARGET_MODE = "none"
    EXTREME_Z = 1.
    RESET_Z = .5

    def features(self, candles, now, atr):
        result = features(candles, now, atr, self.get_funding_history(count=32),
                          self.settled_funding_rate, self.settled_funding_timestamp,
                          self.vars.get("funding_last_seen"), self.EXTREME_Z, self.RESET_Z)
        self.vars["funding_last_seen"] = result["next_seen"]
        if result["event_new"]:
            event = result["event"]
            # New rejected events are logged too; canonical halves preserve evidence below1900chars.
            self._log_json("V4_FUNDING_EVENT", dict(time=now, settled_at=event["settled_at"],
                reason=result["reason"], valid=result["valid"], direction=result["direction"],
                sha256=event["sha256"], count=len(event["window"]), details=result["details"]))
            for index in (0, 1):
                self._log_json("V4_FUNDING_WINDOW", dict(time=now, settled_at=event["settled_at"],
                    sha256=event["sha256"], part=index, rows=event["window"][index*16:(index+1)*16]))
        return {key: result[key] for key in ("valid", "direction", "reason", "details")}

    def manage_position(self, atr):
        # Core enforces T>opened_at; the exit is an adverse state, not a crossing latch.
        state = ma24_state(self.candles, int(self.time))
        if state is not None and ((self.is_long and state["close"] < state["sma24"]) or
                                  (self.is_short and state["close"] > state["sma24"])):
            self._log_json("V4_FUNDING_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at), direction=1 if self.is_long else -1, **state))
            self.request_exit("ma24_adverse")
