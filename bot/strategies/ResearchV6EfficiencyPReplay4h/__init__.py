from strategies.ResearchV6EfficiencyP4h import ResearchV6EfficiencyP4h


class ResearchV6EfficiencyPReplay4h(ResearchV6EfficiencyP4h):
    # Individual TRAIN eligibility freezes 2024 semesters separately; 2025 stays inactive.
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    EFFICIENCY_THRESHOLD = 0.35
    STOP_MULTIPLIER = 2.5
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 60
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = ((1704067200000, 1719792000000), (1719792000000, 1735689600000),)
    FORCE_BOUNDARIES = (1719792000000, 1735689600000, 1751328000000, 1767225600000,)
