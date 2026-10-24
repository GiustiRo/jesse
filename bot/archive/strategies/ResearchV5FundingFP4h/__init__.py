from strategies.ResearchV5Base4h import ResearchV5Base4h
from strategies.ResearchV5Base4h.funding_features import features, exit_state


class ResearchV5FundingFP4h(ResearchV5Base4h):
    LINE = "FUNDING_TREND"
    USE_OI = False
    PRICE_SMA_PERIOD = 120
    RETURN_LAG = 30
    FUNDING_COUNT = 3
    STOP_MULTIPLIER = 3.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        result = features(candles, now, atr, self.get_funding_history(count=self.FUNDING_COUNT),
                          self.settled_funding_rate, self.settled_funding_timestamp,
                          self.PRICE_SMA_PERIOD, self.RETURN_LAG, self.FUNDING_COUNT)
        evidence = result["evidence"]
        event = evidence["settled_at"]
        # Deduplicate publication evidence only. Repeated funding states remain eligible.
        if event is not None and event != self.vars.get("funding_logged_timestamp"):
            self.vars["funding_logged_timestamp"] = event
            self._log_json("V5_FUNDING_PUBLICATION", dict(time=now, **evidence))
        return {key: result[key] for key in ("valid", "direction", "reason", "details")}

    def manage_position(self, atr):
        # The core enforces post-fill timing. Funding and price invalidity are independent.
        state = exit_state(self.candles, int(self.time), 1 if self.is_long else -1,
                           self.get_funding_history(count=1), self.settled_funding_rate,
                           self.settled_funding_timestamp, self.PRICE_SMA_PERIOD, self.RETURN_LAG)
        if state["reason"]:
            self._log_json("V5_FUNDING_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at), direction=1 if self.is_long else -1, **state))
            self.request_exit(state["reason"])
