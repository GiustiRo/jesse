from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayR11_4h(ResearchV5FundingFPOiReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    STOP_MULTIPLIER = 3.3
