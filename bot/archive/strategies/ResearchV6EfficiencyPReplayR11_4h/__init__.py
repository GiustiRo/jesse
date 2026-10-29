from strategies.ResearchV6EfficiencyPReplay4h import ResearchV6EfficiencyPReplay4h


class ResearchV6EfficiencyPReplayR11_4h(ResearchV6EfficiencyPReplay4h):
    # One frozen overlay; eligibility calendar and nominal execution remain inherited.
    STOP_MULTIPLIER = 2.75
