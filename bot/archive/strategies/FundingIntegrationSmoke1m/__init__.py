from jesse.strategies import Strategy


class FundingIntegrationSmoke1m(Strategy):
    """Integration diagnostic only: fixed quantity, one-day hold, no research signal."""

    def should_long(self):
        return self.index == 0

    def go_long(self):
        self.buy = 0.01, self.price

    def update_position(self):
        if self.index >= 1439:
            self.liquidate()

    def should_cancel_entry(self):
        return False
