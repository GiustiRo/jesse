from jesse.strategies import Strategy


class OpenInterestIntegrationObserver1m(Strategy):
    """Data plumbing diagnostic only. Observes OI without placing orders."""

    def before(self):
        if self.open_interest is not None:
            assert self.open_interest > 0
            assert self.open_interest_timestamp <= self.time
            self.vars["oi_seen"] = True

    def before_terminate(self):
        assert self.vars.get("oi_seen", False), "No available OI observation reached the strategy"

    def should_long(self):
        return False

    def go_long(self):
        pass

    def should_cancel_entry(self):
        return False
