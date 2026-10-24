from strategies.ResearchV6EfficiencyPReplay4h import ResearchV6EfficiencyPReplay4h


class ResearchV6EfficiencyPReplayA09_4h(ResearchV6EfficiencyPReplay4h):
    # One frozen overlay; eligibility calendar and nominal execution remain inherited.
    EFFICIENCY_THRESHOLD = 0.315
