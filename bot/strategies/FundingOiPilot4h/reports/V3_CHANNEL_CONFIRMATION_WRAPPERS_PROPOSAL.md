# V3 CHANNEL — propuesta de wrappers de confirmación
Estado al especificar: sólo diseño, sin clases/drafts/backtests creados. Posteriormente root congeló shortlist CHANNEL_POI/CHANNEL_P; la creación se registra en V3_CONFIRMATION_WRAPPERS.json.

Dos padres nominales inmutables; cada wrapper únicamente declara START yFINISH. C1train reutiliza los screenings [2020-09-01,2024-01-01). Los siete stages porpadre son C1V,C2T,C2V,C3T,C3V,C4T,C4V. Fin2026-01-01 esexclusivo y no consulta datos2026. Los resets/warmup/configpertenecen a sesión y no a wrapper.

SHA256 de cada fuente ASCII equivale UTF8; generado por JS puro con dos vectores estándar de control (vacío/abc). Root lo comprobará independientemente al congelar. No compilación/run_analysis delsector.

## ResearchV3CH_P_C1V
Padre: ResearchV3ChannelP4h. IntervaloUTC [2024-01-01,2024-07-01). SHA256: ab4e539e5cab188f9fb516ade3b1603bc820fcd5328a84343a19ac9f31a5ff76

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C1V(ResearchV3ChannelP4h):
    START = 1704067200000
    FINISH = 1719792000000

```

## ResearchV3CH_P_C2T
Padre: ResearchV3ChannelP4h. IntervaloUTC [2020-09-01,2024-07-01). SHA256: 8fb126060d21e9e06c2d992073d9cdfd78d8b7952f1c08114a2fc6966303f0f3

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C2T(ResearchV3ChannelP4h):
    START = 1598918400000
    FINISH = 1719792000000

```

## ResearchV3CH_P_C2V
Padre: ResearchV3ChannelP4h. IntervaloUTC [2024-07-01,2025-01-01). SHA256: 86dabd7539292bcb7e0747cf4e1a5dcde0f2f83340a6916b2c903fd14e830132

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C2V(ResearchV3ChannelP4h):
    START = 1719792000000
    FINISH = 1735689600000

```

## ResearchV3CH_P_C3T
Padre: ResearchV3ChannelP4h. IntervaloUTC [2020-09-01,2025-01-01). SHA256: 98828973ba276d9a0c5b987a489b22ece5b4677edaf72a331d49c723dd48ed0f

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C3T(ResearchV3ChannelP4h):
    START = 1598918400000
    FINISH = 1735689600000

```

## ResearchV3CH_P_C3V
Padre: ResearchV3ChannelP4h. IntervaloUTC [2025-01-01,2025-07-01). SHA256: 909bd476f721ebf1d6b033499f6a73fb3740f027cec19bedfebf183ee8b41da2

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C3V(ResearchV3ChannelP4h):
    START = 1735689600000
    FINISH = 1751328000000

```

## ResearchV3CH_P_C4T
Padre: ResearchV3ChannelP4h. IntervaloUTC [2020-09-01,2025-07-01). SHA256: c4ecefa350f7344728d6fdc92de9d136c88220d144baa8c2add44ae695c510ba

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C4T(ResearchV3ChannelP4h):
    START = 1598918400000
    FINISH = 1751328000000

```

## ResearchV3CH_P_C4V
Padre: ResearchV3ChannelP4h. IntervaloUTC [2025-07-01,2026-01-01). SHA256: 3ce1ebc10da9aec3d77c48ab5e232cbc8de080c0ec79554b92ba238205f72e31

```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3CH_P_C4V(ResearchV3ChannelP4h):
    START = 1751328000000
    FINISH = 1767225600000

```

## ResearchV3CH_OI_C1V
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2024-01-01,2024-07-01). SHA256: 8deb991ee9172b96a71545e5cdc0ab2cf0ae33e5a7c965d1b8f79b2eb8b94598

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C1V(ResearchV3ChannelOi4h):
    START = 1704067200000
    FINISH = 1719792000000

```

## ResearchV3CH_OI_C2T
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2020-09-01,2024-07-01). SHA256: 182e2634564a085e0d5c544982c8c9e3565d2e2a4bd34e803db44f69449d16b4

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C2T(ResearchV3ChannelOi4h):
    START = 1598918400000
    FINISH = 1719792000000

```

## ResearchV3CH_OI_C2V
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2024-07-01,2025-01-01). SHA256: 571905c3e8ac711b5e56e83d68fe5481080b97b7bc611184b294cbf3884d6920

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C2V(ResearchV3ChannelOi4h):
    START = 1719792000000
    FINISH = 1735689600000

```

## ResearchV3CH_OI_C3T
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2020-09-01,2025-01-01). SHA256: 5e2d7cac3dcc3e08d6a97f279de437bffa4d098ba3e9ac7bf2e20118f9d6f500

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C3T(ResearchV3ChannelOi4h):
    START = 1598918400000
    FINISH = 1735689600000

```

## ResearchV3CH_OI_C3V
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2025-01-01,2025-07-01). SHA256: 9ca7eebe71b463054c05a1ad0c76196f238dab4c9fca60bf4568ec57d07168c7

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C3V(ResearchV3ChannelOi4h):
    START = 1735689600000
    FINISH = 1751328000000

```

## ResearchV3CH_OI_C4T
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2020-09-01,2025-07-01). SHA256: 6a8a17b240ff49084e0d42ef662dbc13c22c4a98bc3fd64ed27206060d3c9b08

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C4T(ResearchV3ChannelOi4h):
    START = 1598918400000
    FINISH = 1751328000000

```

## ResearchV3CH_OI_C4V
Padre: ResearchV3ChannelOi4h. IntervaloUTC [2025-07-01,2026-01-01). SHA256: 1d98d79478c0794bc8336e786d999b04bd317755834bc094c6f9631206a92366

```python
from strategies.ResearchV3ChannelOi4h import ResearchV3ChannelOi4h


class ResearchV3CH_OI_C4V(ResearchV3ChannelOi4h):
    START = 1751328000000
    FINISH = 1767225600000

```
