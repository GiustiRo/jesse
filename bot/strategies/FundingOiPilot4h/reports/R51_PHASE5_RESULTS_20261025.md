# r51 F5: pronósticos continuos estilo Carver (2026-10-25)

**Resultado:** T1 y T2 no reemplazan a R1 dentro de P1. R1, el ensamble Donchian, sigue en el núcleo. N pasa de 101 a 103.

Protocolo: `PROTOCOL_R51.md` F5/F6 (`8ac56348`).
- Reglas: EWMAC 16/64, 32/128 y 64/256 más una ruptura de 80 días.
- Escalares de *Systematic Trading*, sin ajuste.
- FDM de 1,2 y tope de ±20.
- Largo/plano en BTC, ETH, oro y SPX; largo/corto en WTI, gas y bono.
- T2 agrega la atenuación por percentil de vol.
- La enmienda de huecos de datos (`73a1c6da`) también aplica acá.

## Las mangas solas (canasta de los 7 activos)
| Ensayo | Decisión: Sharpe | CAGR | DD | Trim. + | 2021–25: Sharpe | Larga: Sharpe / DD | ρ con P1 |
|---|---|---|---|---|---|---|---|
| T1 | 1,12 | 9,1% | −9,2% | 71% | 0,94 | 0,18 / −44,9% | 0,54 |
| T2 | 1,19 | 12,3% | −12,4% | 58% | 0,91 | 0,29 / −39,7% | 0,56 |

**T1 por activo (Sharpe en decisión):**

| Activo | Sharpe |
|---|---|
| BTC | 0,92 |
| ETH | 0,83 |
| Oro | 1,05 |
| SPX | 0,62 |
| WTI | 0,03 |
| Gas | 0,13 |
| Bono | −0,03 |

- En el bono, T1 gana +23% en 2022 como corto y pierde en 2024–25.
- La lente larga hunde a WTI y gas: DD de −43% y −50%.
  - El CFD del gas tiene saltos diarios de hasta 37%, probablemente cambios de contrato. Es una advertencia de datos que ya venía de r50.

## Reemplazo de R1 dentro de P1 (misma regla de inclusión)
| Cartera | 2018-09+: CAGR | DD | Sharpe | Trim. + | 2021–25: CAGR | Sharpe | Trim. + |
|---|---|---|---|---|---|---|---|
| **P1 (R1 + C6)** | 36,9% | −14,3% | **1,60** | 21 / 30 | 24,3% | 1,42 | 12 / 20 |
| T1 + C6 | 35,5% | −17,4% | 1,53 | 19 / 30 | 23,1% | 1,38 | **14 / 20** |
| T2 + C6 | 36,2% | −21,9% | 1,52 | 17 / 30 | 23,0% | 1,32 | 12 / 20 |

- T1 baja el Sharpe de 2018-09+ en 0,07 y pierde 2 trimestres positivos, así que no reemplaza a R1.
- En 2021–25, T1 suma 2 trimestres positivos (70% contra 60%), aunque con menos Sharpe.

## Lectura
1. **El ensamble Donchian ya captura la tendencia de varias velocidades.** Pasar a pronósticos continuos no agrega Sharpe a la cartera y suma DD: la señal continua está invertida más tiempo.
2. **La regularidad de 2021–25 mejora con T1.** Es una pista, no un resultado: la regla preregistrada decide por 2018-09+. Queda anotado para r52, sin rescatarlo.
3. **La atenuación por vol (T2) empeora todo.** Coincide con la evidencia: el vol targeting no agrega Sharpe fuera de acciones.
4. **La parte largo/corto de T en energía y bono no aporta** (Sharpe de 0,03, 0,13 y −0,03).

## Archivos
- `research_scripts/data/r51/explore_T.json`.
- `research_scripts/data/r51/f6_portfolio.json` (reemplazo).
