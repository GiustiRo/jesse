# r55 F4: integración (2026-10-26)

**Resultado:** ninguno de los 5 activos marginales entra. «R1 sin bono» sí entra. La cartera final P-r55 = P1 sin la manga R1/bono, congelada en `P55_FREEZE.md`. N pasa de 133 a 140.

- Protocolo: `PROTOCOL_R55.md` F4, con la enmienda F4 fijada antes de correr y los 6 ensayos registrados (`f569df80`).
- Script: `research_scripts/r55_portfolio.py`.
- Todo está cortado al 2024-12-31.

**Base:** P1, porque ninguna pieza de F1–F3 pasó. P1 da Sharpe 1,677 / 1,605, igual que en F0–F2.

**Enmienda previa:** en 2018-09+, P1 no tiene bono, así que con la regla de r51 «R1 sin bono» nunca podía pasar. Esa baja se decide en 2021–24.

## Activos marginales (orden fijo; cada uno sobre la cartera vigente)
| Activo | Sharpe largo propio (desde, hasta 2024) | ΔSharpe 2018-09+ | ΔSharpe 2021–24 | ΔTrim. + (largo / 21–24) | ΔDD (largo / 21–24) | Falla | Entra |
|---|---|---|---|---|---|---|---|
| Nasdaq | **0,75** (2013) | +0,018 | **+0,085** | −1 / +1 | −0,3 / +0,9 pp | inclusión: +0,018 < +0,05, y −1 trimestre | no |
| Plata | 0,05 (2011) | −0,060 | −0,105 | −2 / 0 | +0,2 / −1,4 pp | las 3 puertas | no |
| Cobre | 0,24 (2013) | −0,006 | −0,052 | −1 / −1 | +0,3 / −0,5 pp | Sharpe propio e inclusión | no |
| EWY | 0,23 (2001) | −0,049 | −0,144 | −2 / −1 | −0,1 / −0,8 pp | Sharpe propio e inclusión | no |
| EWJ | 0,12 (2001) | −0,073 | −0,099 | −1 / 0 | −1,2 / +0,1 pp | las 3 puertas | no |

**Lectura**
- **Solo el Nasdaq tiene ventaja propia** (0,75). Mejora 2021–24, pero en 2018-09+ apenas suma (+0,02) y pierde un trimestre positivo. Con ρ 0,87 con el SPX, repite lo que ya está. Coincide con r50.
- **Plata, cobre, EWY y EWJ restan** en las dos ventanas: su R1 tiene poco o nada de ventaja hasta 2024. A tu pregunta («si nos dan rendimiento claro»): hoy no lo dan.

## R1 sin bono
| Ventana | P1 | Sin bono | Δ |
|---|---|---|---|
| 2021–24, Sharpe | 1,605 | **1,723** | +0,118 |
| 2021–24, CAGR | 29,2% | 31,6% | +2,5 pp |
| 2021–24, DD | −14,0% | −12,4% | +1,6 pp |
| 2018-09+ | — | idéntica | 0 |

- **Entra** con la regla enmendada.
- Retornos por año en 2021–24: 2022 pasa de −5,7% a −4,8%, 2023 de +42,9% a +44,2% y 2024 de +42,2% a +49,4%.
- Trimestres laterales en 2021–24: la suma pasa de −2,3% a +0,4%.
- **Post-hoc declarado:** el bono acumula 22 reglas sin ventaja en r50–r51, y su 2025 ya se observó.

## P-r55 (congelada)
| Ventana | CAGR | DD | Sharpe | Trim. + | DSR (N = 139) | Alcistas | Bajistas | Laterales |
|---|---|---|---|---|---|---|---|---|
| 2018-09 → 2024 | 41,2% | −14,3% | 1,677 | 19/26 | 0,976 | +212% / 9 de 9 | +13,2% / 2 de 5 | +29,6% / 8 de 11 |
| 2021 → 2024 | 31,6% | −12,4% | 1,723 | 11/16 | 0,790 | +99% / 6 de 6 | +17,7% / 2 de 3 | +0,4% / 3 de 7 |

- Las columnas de régimen muestran suma y trimestres positivos sobre el total de cada clase.
- No hace falta ninguna corrida Jesse: todas las mangas restantes se confirmaron en r51.

## Sobre la mirada a 2025 (F5)
- **P-r55 no agrega ninguna manga nueva**, y la puerta de F5 aplica solo a mangas nuevas.
- El 2025 de P1 y el del bono ya se midieron en r50/r51, así que abrir 2025 no aportaría información independiente sobre esta cartera.
- **Recomendación:** no gastar la mirada única a 2025 en P-r55. Conviene reservarla para un candidato nuevo preregistrado (por ejemplo, ML3 congelado). El fuera de muestra limpio de P-r55 es 2026.
- **La decisión es del usuario.**

## Archivos
- `research_scripts/r55_portfolio.py`.
- `research_scripts/data/r55/f4_portfolio.json`.
- `RESEARCH_HUB/revisions/20261026-r55/P55_FREEZE.md`.
