from strategies.ResearchV3ChannelPReplay4h import ResearchV3ChannelPReplay4h


class ResearchV3ChannelPReplayN09_4h(ResearchV3ChannelPReplay4h):
    # Predeclared 0.9 neighbor changes only initial-stop and trailing distances.
    STOP_MULTIPLIER = 1.8
    TRAIL_MULTIPLIER = 2.7
