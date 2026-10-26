# r55 F3: Brent–WTI con veto de quiebre estructural (2026-10-26)

**Resultado:** A3 v2 no pasa. El veto evita la pérdida de 2013, pero crea un DD más profundo en 2015 y bloquea trades buenos. A3 no entra a la cartera, ni siquiera como provisional. N pasa de 132 a 133.

- Protocolo: `PROTOCOL_R55.md` F3. El ensayo se registró antes de correrlo (`050d8480`).
- Script: `research_scripts/r55_a3.py`.
- Las barras de entrada se recortan al 2024-12-31: no entra ningún dato de 2025.

**Reproducción:** con el veto apagado, la curva es idéntica a la de A3 de r51 (lente de decisión) hasta el 2024-12-31.

## Regla
- A3 de r51 sin cambios.
- **Veto:** una entrada nueva solo se permite si un AR(1) de Δx sobre x(t−1), estimado en los 252 días hábiles previos, da t(b) ≤ −2 y una vida media entre 0 y 60 días.

## Resultados (hasta 2024-12-31)
| Lente | Versión | Desde | Sharpe | CAGR | DD | Trim. + | Trades | Top-5 | Señales bloqueadas |
|---|---|---|---|---|---|---|---|---|---|
| Decisión | **A3 v2** | 2018-09 | 0,88 | 5,2% | −5,5% | 50% | **28** | 58% | 36 |
| Decisión | A3 r51 | 2018-09 | 1,18 | 8,2% | −5,0% | 73% | 37 | 40% | — |
| 2021–24 | A3 v2 | 2020-10 | 1,02 | 5,9% | −5,5% | 65% | 23 | 64% | 5 |
| 2021–24 | A3 r51 | 2020-10 | 1,12 | 6,6% | −4,3% | 71% | 24 | 57% | — |
| Larga | **A3 v2** | 2012-12 | 0,60 | 3,7% | **−16,1%** | 45% | 48 | 54% | 114 |
| Larga | A3 r51 | 2012-12 | 0,76 | 5,8% | −12,7% | 63% | 70 | 35% | — |

**Retorno por año en la lente larga:**

| Versión | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2 | −1,5% | +7,8% | **−6,8%** | +20,0% | −1,5% | −4,4% | +1,6% | +7,0% | +7,3% | +16,7% | −3,3% | +5,0% |
| r51 | −4,6% | +10,3% | +3,9% | +13,5% | +0,6% | −0,5% | +9,2% | +11,2% | +7,3% | +16,7% | −0,8% | +5,0% |

- DD máximo de v2: −16,1%, del 2015-02 al 2016-01. En r51 fue −12,7%, en 2013.
- **Fracción de días con entradas permitidas:**

| 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021–24 |
|---|---|---|---|---|---|---|---|---|
| 9% | 47% | 74% | 94% | 67% | 32% | 21% | 98% | ~99% |

## Puertas (r51 F6)
| Puerta | Valor | |
|---|---|---|
| G1: Sharpe de decisión ≥ 0,3 | 0,88 | ✓ |
| G2: PnL en las ventanas bajistas del WTI > 0 | +6,8% | ✓ |
| G3: sin veto de lente larga | DD largo −16,1%, contra un tope de 1,5 × −5,5% = −8,3% | **✗** |
| G4: ρ con P1 ≤ 0,2 | −0,00 | ✓ |
| G5: ≥ 30 trades y top-5 < 60% | 28 trades | **✗** |

## Lectura
1. **El veto hace lo que promete en 2013** (−1,5% contra −4,6%): el AR(1) detecta que el spread dejó de revertir.
2. **Pero se equivoca en las dos direcciones.**
   - Deja entrar en 2015, cuando el spread se movía entre regímenes, y ahí aparece un DD peor que el de 2013.
   - Bloquea el 68–79% de los días en 2018–2019, que eran años buenos para A3: el Sharpe de decisión baja de 1,18 a 0,88.
3. **Una prueba de reversión a la media sobre 252 días es lenta**, igual que la señal B de F0: confirma el quiebre cuando ya pasó y tarda en reabrir.
4. A3 sigue siendo la regla de energía con más ventaja (Sharpe 1,18 sin veto en 2018-09 → 2024), pero su riesgo de quiebre no se resolvió con esta regla. No se prueba otra variante en r55: sería buscar el veto que mejor acomoda la historia conocida.

## Efecto en el plan
- **F4 sin A3.** Quedan los 5 activos marginales (Nasdaq, plata, cobre, EWY, EWJ), «R1 sin bono» y la cartera final.
- La base de F4 es P1, porque no entró ninguna pieza nueva.

## Archivos
- `research_scripts/r55_a3.py`.
- `research_scripts/data/r55/f3_a3.json`.
