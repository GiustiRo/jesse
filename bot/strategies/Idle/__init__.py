from jesse.strategies import Strategy


class Idle(Strategy):
    """Placeholder strategy: connects live but never opens a position."""

    def should_long(self) -> bool:
        return False

    def should_short(self) -> bool:
        return False

    def should_cancel_entry(self) -> bool:
        return False

    def go_long(self):
        pass

    def go_short(self):
        pass
