# V3 — fuentes replay y robustez congeladas

Siete clases compiladas y AST/hashes/calendario verificados antes del primer replay. Job 93fc699d8de0433594ab56ce072c22d7. Padres V3 y V2 permanecen congelados. Datos2024–25, fin2026Jan exclusivo; sin velas2026. Calendarios individuales y selector global en V3_REPLAY_CALENDARS_FROZEN.json. Configs exactas y presupuesto14slots/13runs en V3_REPLAY_SCENARIOS_FROZEN.json.

## ResearchV3ChannelPReplay4h

SHA256 6682ccc3a8a5adbf8576130db1dfe0a97446b287fc67b8b52d1110da2b0eea9a

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3ChannelPReplay4h(ResearchV3ChannelP4h):
    # Train-only eligibility was frozen before replay; preserve each half-year.
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    STOP_MULTIPLIER = 2.
    TRAIL_MULTIPLIER = 3.
    MAX_HOLD_BARS = 42
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = (
        (1704067200000, 1719792000000),
        (1719792000000, 1735689600000),
        (1735689600000, 1751328000000),
        (1751328000000, 1767225600000),
    )
    # Strict entry bounds and liquidation prevent carry across each fold close.
    FORCE_BOUNDARIES = (
        1719792000000,
        1735689600000,
        1751328000000,
        1767225600000,
    )
```

## ResearchV3ChannelPReplayN09_4h

SHA256 dd3a308cd3372ed5ba8e29254ebc7b3fb9168572eabe02e326fd4c26a7f089f3

```python
from strategies.ResearchV3ChannelPReplay4h import ResearchV3ChannelPReplay4h


class ResearchV3ChannelPReplayN09_4h(ResearchV3ChannelPReplay4h):
    # Predeclared 0.9 neighbor changes only initial-stop and trailing distances.
    STOP_MULTIPLIER = 1.8
    TRAIL_MULTIPLIER = 2.7
```

## ResearchV3ChannelPReplayN11_4h

SHA256 926ec08db17bf4b2b798f33e9c60369003d3663ce37fd01ba1d7f77744de3f93

```python
from strategies.ResearchV3ChannelPReplay4h import ResearchV3ChannelPReplay4h


class ResearchV3ChannelPReplayN11_4h(ResearchV3ChannelPReplay4h):
    # Predeclared 1.1 neighbor changes only initial-stop and trailing distances.
    STOP_MULTIPLIER = 2.2
    TRAIL_MULTIPLIER = 3.3
```

## ResearchV3ChannelOiReplay4h

SHA256 4a20e12ae335ccc66052420917bd874f2b82414a7cc4160db933dfe9c85a77de

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3ChannelOiReplay4h(ResearchV3ChannelOi4h):
    START = 1704067200000
    FINISH = 1767225600000
    ACTIVE_WINDOWS = [[1704067200000,1719792000000],[1719792000000,1735689600000],[1735689600000,1751328000000],[1751328000000,1767225600000]]
    FORCE_BOUNDARIES = [1719792000000,1735689600000,1751328000000,1767225600000]
```

## ResearchV3ChannelOiReplayN09_4h

SHA256 6b3750c1dd338daad65df0acee28da3b301739ec0701ef273fd4a5c8baca994f

```python
from strategies.ResearchV3ChannelOiReplay4h import ResearchV3ChannelOiReplay4h


class ResearchV3ChannelOiReplayN09_4h(ResearchV3ChannelOiReplay4h):
    STOP_MULTIPLIER = 1.8
    TRAIL_MULTIPLIER = 2.7
```

## ResearchV3ChannelOiReplayN11_4h

SHA256 047a8399d4243022db3058d3da22bc7ec33c256f4ec06b8358099f1acbef7c7b

```python
from strategies.ResearchV3ChannelOiReplay4h import ResearchV3ChannelOiReplay4h


class ResearchV3ChannelOiReplayN11_4h(ResearchV3ChannelOiReplay4h):
    STOP_MULTIPLIER = 2.2
    TRAIL_MULTIPLIER = 3.3
```

## ResearchV3ChannelOiReplayLag4h

SHA256 6524610c3e34bec318de309546301146380fa4678af1a6241afc62a30d384a1d

```python
from strategies.ResearchV3ChannelOiReplay4h import ResearchV3ChannelOiReplay4h


class ResearchV3ChannelOiReplayLag4h(ResearchV3ChannelOiReplay4h):
    OI_LAG_BARS = 1
```
