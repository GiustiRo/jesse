# r55: congelamiento de P-r55 (2026-10-26)

**P-r55 = P1 sin la manga R1/bono.** Es el único cambio que pasó en r55: «R1 sin bono», F4, `R55_F4_NOBOND`.

## Qué se congela
- **Código:** el arnés y los motores de P1 congelados en `5caf4a53` (`r50_harness.py`, `r50_engines.py`, `r50_f1b.py`, `r50_f1c.py` y `r50_f2.py`), y el armado de r55 en `research_scripts/r55_portfolio.py`, en el commit que contiene este archivo.
- **R1:** el ensamble Donchian r49 en 4h, con las configuraciones de `r50_f1b.R1_CFG`, en **BTC, ETH, oro, SPX, WTI y gas**. Sale el bono.
- **C6:** rupturas R2 + R3 50/50 en BTC y ETH, sin cambios.
- **Construcción:** la de r50 F2, sin cambios: riesgo inverso con vol expansiva, vol objetivo 17%, k ≤ 8, rebalanceo mensual y sin freno.
- **Confirmación en Jesse:** todas las mangas restantes ya se confirmaron en r51 F1, así que no hace falta ninguna corrida nueva.

## Métricas de referencia (hasta el 2024-12-31; N = 140)
| Ventana | CAGR | DD | Sharpe | Trim. + | DSR |
|---|---|---|---|---|---|
| 2018-09 → 2024 | 41,2% | −14,3% | 1,677 | 19/26 | 0,976 |
| 2021 → 2024 | 31,6% | −12,4% | 1,723 | 11/16 | 0,790 |

- La ventana 2018-09+ es idéntica a P1: P1 no tenía bono antes de ~2019-03.
- En 2021–24, P1 da 29,2%, −14,0% y Sharpe 1,605.

## Advertencias
- **Es una decisión post-hoc, y así se declara.** El bono resta en las 22 reglas probadas en r50–r51, y su 2025 ya se observó en r50/r51 (R1/bono −9%).
- **Por eso la mirada a 2025 no sería independiente para este cambio.** P1 ya se midió hasta 2025 en r50/r51, y P-r55 no agrega ninguna manga nueva.
  - La puerta de F5 aplica a las mangas nuevas, y no hay ninguna.
  - El único fuera de muestra limpio de P-r55 es 2026, que sigue reservado y requiere autorización del usuario.
