from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayA09_4h(ResearchV5FundingFPReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    PRICE_SMA_PERIOD = 108
    RETURN_LAG = 27
