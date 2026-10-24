from strategies.ResearchV3ChannelPReplay4h import ResearchV3ChannelPReplay4h


class ResearchV3ChannelPReplayN11_4h(ResearchV3ChannelPReplay4h):
    # Predeclared 1.1 neighbor changes only initial-stop and trailing distances.
    STOP_MULTIPLIER = 2.2
    TRAIL_MULTIPLIER = 3.3
