"""Research report namespace only; deliberately emits no trading signals."""
from jesse.strategies import Strategy

class FreshStructureProbability(Strategy):
    def should_long(self):
        return False

    def should_short(self):
        return False

    def go_long(self):
        raise RuntimeError("Research-only namespace cannot trade")

    def go_short(self):
        raise RuntimeError("Research-only namespace cannot trade")

    def should_cancel_entry(self):
        return False
