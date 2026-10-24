from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayR09_4h(ResearchV5FundingFPReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    STOP_MULTIPLIER = 2.7
