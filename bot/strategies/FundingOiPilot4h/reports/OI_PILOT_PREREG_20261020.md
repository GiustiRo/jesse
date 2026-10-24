# OI microvalidación prerregistrada 2026-10-20
Comparación exploratoria tras haber visto los resultados previos: no se presenta como OOS nuevo, ni selección walk-forward.
Política acordada: incluir features nuevas en validación técnica y comparaciones por ablación; su disponibilidad no obliga a usar todas como señales finales.
Hipótesis única sin tuning: OI creciente en24h confirma ruptura de precio, para ambos sentidos. No implica que OI creciente identifique dirección ni demuestre edge.
Cuatro sesiones nuevas: C=referencia+OI; D=referencia+funding+OI. Comparar con A/B existentes en [2022-01-01,2022-07-01) y [2023-01-01,2023-07-01), no sumar ni optimizar.
Mismas velas BTC4h, ejecución1m, capital10000, isolated3x,fee0.00045,stop2,target4,hold24h,sizing anterior.
OI dataset6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf, mode historical, allow_missing_observations=true, max_age600000ms. Archivo retrospectivo, lag label+6m asumido; no garantiza point-in-time original.
Funding dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 contable ON en todas; marca histórica proxy.
No se amplía el stale limit ni se rellena OI. Primer24h sin referencia produce exclusión explícita. Cambio relativo signo>0 sin umbral ajustado. Datos faltantes bloquean sólo entradas, nunca salidas.
Auditoría en callbacks: lag, antigüedad, existencia de datos y contadores log persistente con debug_mode=true. 45 tests existentes de OI aprobaron (incluyen disponibilidad retardada y staleness/gaps).
Sin2026, ML, live/paper ni cambios a legacy.
```python
import json
from strategies.FundingWfPilotBase4h import FundingWfPilotBase4h


class FundingOiPilot4h(FundingWfPilotBase4h):
    """Exploratory ablation: rising OI confirms the unchanged price breakout."""
    FUNDING_FILTER = False

    def before(self):
        super().before()
        value = self.open_interest
        label = self.open_interest_timestamp
        audit = self.vars.setdefault("oi_audit", {
            "bars": 0, "observed": 0, "missing": 0,
            "eligible_before_oi": 0, "blocked_missing": 0,
            "blocked_nonrising": 0, "passed": 0,
        })
        audit["bars"] += 1
        if value is not None:
            # Archive convention is label+6m; data older than 10m after
            # availability must be None. These assertions do not certify
            # original historical publication times.
            assert label is not None and value > 0
            assert label + 360_000 <= self.time <= label + 960_000
            audit["observed"] += 1
        else:
            assert label is None
            audit["missing"] += 1
        history = self.vars.setdefault("oi_history", [])
        history.append((int(self.time), value))
        # Seven 4h observations span exactly 24h. The first day is a
        # deliberate initialization exclusion; no backfill or interpolation.
        history[:] = history[-7:]
        old = history[0][1] if len(history) == 7 and history[0][0] == self.time - self.DAY_MS else None
        valid = value is not None and old is not None
        rising = valid and value > old
        context = self.vars["context"]
        if context["allowed"]:
            audit["eligible_before_oi"] += 1
            if not valid:
                audit["blocked_missing"] += 1
            elif not rising:
                audit["blocked_nonrising"] += 1
            else:
                audit["passed"] += 1
        context["allowed"] = context["allowed"] and rising

    def before_terminate(self):
        assert self.vars["oi_audit"]["observed"] > 0
        self.log("OI_PILOT_AUDIT " + json.dumps(self.vars["oi_audit"], sort_keys=True))
        super().before_terminate()

from strategies.FundingOiPilot4h import FundingOiPilot4h


class FundingOiCombinedPilot4h(FundingOiPilot4h):
    """Only add the previously frozen adverse settled-funding gate."""
    FUNDING_FILTER = True

```

## Corrección técnica antes de inspeccionar rendimientos
F1 C y D se detuvieron por assert value>0: el formato de archivo acepta OI literalmente cero, detectado en2022-03-07. No se usaron resultados económicos parciales. Se permite value>=0 para auditar el transporte y los ceros se cuentan aparte y se excluyen del cálculo igual que referencia inválida. Sin tocar umbrales, ventanas, sizing ni salidas. Reintentar sólo por este error técnico; conservar sesiones fallidas.
Código actualizado:
```python
import json
from strategies.FundingWfPilotBase4h import FundingWfPilotBase4h


class FundingOiPilot4h(FundingWfPilotBase4h):
    """Exploratory ablation: rising OI confirms the unchanged price breakout."""
    FUNDING_FILTER = False

    def before(self):
        super().before()
        value = self.open_interest
        label = self.open_interest_timestamp
        audit = self.vars.setdefault("oi_audit", {
            "bars": 0, "observed": 0, "missing": 0, "zero_values": 0,
            "eligible_before_oi": 0, "blocked_missing": 0,
            "blocked_nonrising": 0, "passed": 0,
        })
        audit["bars"] += 1
        if value is not None:
            # Archive convention is label+6m; data older than 10m after
            # availability must be None. These assertions do not certify
            # original historical publication times.
            assert label is not None and value >= 0
            assert label + 360_000 <= self.time <= label + 960_000
            audit["observed"] += 1
            # The archive permits literal zero quantities. Preserve provenance
            # in a separate counter but never use zero as a valid reference.
            if value == 0:
                audit["zero_values"] += 1
                value = None
        else:
            assert label is None
            audit["missing"] += 1
        history = self.vars.setdefault("oi_history", [])
        history.append((int(self.time), value))
        # Seven 4h observations span exactly 24h. The first day is a
        # deliberate initialization exclusion; no backfill or interpolation.
        history[:] = history[-7:]
        old = history[0][1] if len(history) == 7 and history[0][0] == self.time - self.DAY_MS else None
        valid = value is not None and old is not None
        rising = valid and value > old
        context = self.vars["context"]
        if context["allowed"]:
            audit["eligible_before_oi"] += 1
            if not valid:
                audit["blocked_missing"] += 1
            elif not rising:
                audit["blocked_nonrising"] += 1
            else:
                audit["passed"] += 1
        context["allowed"] = context["allowed"] and rising

    def before_terminate(self):
        assert self.vars["oi_audit"]["observed"] > 0
        self.log("OI_PILOT_AUDIT " + json.dumps(self.vars["oi_audit"], sort_keys=True))
        super().before_terminate()

```
