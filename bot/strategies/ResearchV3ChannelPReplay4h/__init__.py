from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3ChannelPReplay4h(ResearchV3ChannelP4h):
    # Train-only eligibility was frozen before replay; preserve each half-year.
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    STOP_MULTIPLIER = 2.
    TRAIL_MULTIPLIER = 3.
    MAX_HOLD_BARS = 42
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = (
        (1704067200000, 1719792000000),
        (1719792000000, 1735689600000),
        (1735689600000, 1751328000000),
        (1751328000000, 1767225600000),
    )
    # Strict entry bounds and liquidation prevent carry across each fold close.
    FORCE_BOUNDARIES = (
        1719792000000,
        1735689600000,
        1751328000000,
        1767225600000,
    )
