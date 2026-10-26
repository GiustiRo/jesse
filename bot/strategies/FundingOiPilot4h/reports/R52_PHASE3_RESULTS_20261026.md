# r52 F3: permiso de régimen con jump model sobre BTC (2026-10-26)

**Resultado:** J1 no pasa la regla de inclusión. P1 sigue sin cambios. N pasa de 108 a 109.

Protocolo: `PROTOCOL_R52.md` F3 (`840747c3`). Las ventanas de P1 se cortaron al 2024-12-31: 2025 sigue sellado.

## Regla
- *Statistical jump model* de 2 estados sobre BTC spot diario.
- Rasgos: desvío negativo y Sortino EWMA, con vidas medias de 5, 10 y 21 días.
- λ = 50 fijo, re-ajuste mensual y 1 día de demora.
- En el estado de riesgo, R1/BTC, R1/ETH y C6 van a la mitad de tamaño.

## Resultados (hasta 2024-12-31)
| Ventana | Versión | CAGR | DD | Sharpe | Trim. + |
|---|---|---|---|---|---|
| 2018-09 → 2024 | P1 | 41,2% | −14,3% | **1,68** | **19/26** |
| 2018-09 → 2024 | P1 + J1 | 41,3% | −14,8% | 1,61 | 18/26 |
| 2021 → 2024 | P1 | 29,2% | −14,0% | 1,61 | 11/16 |
| 2021 → 2024 | P1 + J1 | 30,1% | −15,3% | 1,62 | 11/16 |

- ΔSharpe en 2018-09+: **−0,06**, con −1 trimestre positivo; en 2021–24: +0,015.
- El DD empeora levemente en las dos ventanas.

**Estado de riesgo por año (porcentaje de días):**

| Año | Días en riesgo |
|---|---|
| 2018 (desde mayo) | 38% |
| 2019 | 14% |
| 2020 | 14% |
| 2021 | 23% |
| 2022 | 23% |
| 2023 | 6% |
| 2024 | 0% |

- En total, 31 cambios de estado.
- Con λ = 50, el modelo detecta caídas cortas y bruscas (BTC −0,8% diario en ese estado), no los mercados laterales o bajistas largos.
- Eso hace que reduzca el tamaño justo antes de los rebotes.

## Lectura
- El filtro de régimen sobre BTC no mejora a P1. El ensamble Donchian ya sale solo en los bajistas largos, así que lo que agrega el jump model es más rotación en las caídas bruscas.
- Coincide con la evidencia: el beneficio publicado es sobre comprar y mantener, no sobre tendencia.
- Anotado para r53: el modelo con otra penalización o con otros rasgos sería un ensayo nuevo, sin rescate.

## Archivos
- `research_scripts/r52_j1.py`.
- `research_scripts/data/r52/j1.json`, con los diagnósticos de cada ajuste.
