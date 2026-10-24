from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayLag4h(ResearchV5FundingFPOiReplay4h):
    # One 4h decision of additional OI lag; price and funding keep their own clocks.
    OI_LAG_BARS = 1
