"""Opt-in deterministic adverse fills for perpetual-futures backtests only."""

import math


def validate_slippage_bps(value: object) -> float:
    # A sell haircut of 100% would create a nonpositive execution price.
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError('slippage_bps must be a finite number in [0, 10000)')
    result = float(value)
    if not math.isfinite(result) or not 0 <= result < 10_000:
        raise ValueError('slippage_bps must be a finite number in [0, 10000)')
    return result
