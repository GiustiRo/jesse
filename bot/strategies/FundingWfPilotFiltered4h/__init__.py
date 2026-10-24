from strategies.FundingWfPilotBase4h import FundingWfPilotBase4h


class FundingWfPilotFiltered4h(FundingWfPilotBase4h):
    """The sole A/B change is the causal funding entry gate."""
    FUNDING_FILTER = True
