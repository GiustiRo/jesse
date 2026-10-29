from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayA09_4h(ResearchV5FundingFPOiReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    PRICE_SMA_PERIOD = 108
    RETURN_LAG = 27
