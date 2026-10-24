from strategies.FundingOiPilot4h import FundingOiPilot4h


class FundingOiCombinedPilot4h(FundingOiPilot4h):
    """Only add the previously frozen adverse settled-funding gate."""
    FUNDING_FILTER = True
