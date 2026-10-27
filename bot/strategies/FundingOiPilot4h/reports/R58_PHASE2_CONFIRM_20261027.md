# r58 F2: confirmación única en N2 ∪ N3 (2026-10-27)

**N + 1 → 144.** Commit B: `e45621b7`. `r58.py confirm` → `data/r58/f2_confirm.json`.

- **Decisión del usuario:** el poder contra la mitad del efecto dio 0,30 (< 0,4) y el usuario decidió correr igual (2026-10-27).
- **Regla:** C6 entra solo si la alt está en compresión de la vol pasada (`persist_vol` = 0) **y** p(rango a 40 días) < 0,3874, ambas del último día cerrado.
- **Ventana:** del 2021-07-02 al 2024-12-31.
- **Datos nunca vistos por C6:** N2 (20 monedas) y N3 (30 monedas).

## Veredicto: **pasa** (5 de 5 criterios)
| Criterio (§3, commit B) | Resultado | ¿Cumple? |
|---|---|---|
| a) D en N2 ∪ N3 > 0, con percentil 10 del bootstrap semanal > 0 | **D = +0,60 R**, p10 +0,26, IC90 [+0,17, +1,00] (1.127 trades evaluables) | sí |
| b) D > 0 en cada banco | N2 **+0,40** (IC90 [−0,12, +0,94]); N3 **+0,77** (IC90 [+0,25, +1,26]) | sí |
| c) Sharpe de la canasta filtrada ≥ sin filtrar | **0,455 contra 0,132** | sí |
| d) a) con costos ×2 | D +0,59, p10 +0,25 | sí |
| d) c) con costos ×2 | 0,398 contra 0,065 | sí |

## Detalle
| | n evaluables | Retiene | R entra / excluido | Pierde del decil sup. | Canasta sin filtrar → filtrada |
|---|---|---|---|---|---|
| N2 | 514 | 52,7% | +0,26 / −0,13 | 27% | 0,256 → 0,399 |
| N3 | 613 | 53,8% | +0,29 / −0,49 | 19% | 0,037 → 0,397 |
| **N2 ∪ N3** | **1.127** | **53,3%** | **+0,28 / −0,32** | **24%** | **0,132 → 0,455** |

- **Canasta filtrada en N2 ∪ N3:** CAGR 0,38%, DD −1,3% y 36% de trimestres positivos.
- **Canasta sin filtrar:** 0,22%, −2,5% y 36%.
- Las dos son canastas de igual peso con 1% de riesgo por trade y por moneda. Lo que se compara es el Sharpe; el nivel se escala en la construcción de cartera.

## Validación tipo r54 de C6 sin condición (sin N)
| Banco | Monedas positivas | Colapsos | Sharpe de canasta 2021–24 |
|---|---|---|---|
| N2 | 11/20 | 4 | 0,57 |
| N3 | 13/30 | 8 | 0,01 |
| Unión | 24/50 (**falla** la mayoría) | 12 (**falla** el ≤ 10%) | 0,26 |

En U50, r54 había dado una canasta con Sharpe 1,03 y 32 de 48 positivas. **C6 sin filtro generaliza mucho peor a monedas más chicas.**

## Lectura
1. **La regla se confirma fuera de muestra.**
   - El efecto se achica, como se esperaba: de +0,82 en U50 a +0,60 en la unión.
   - Sigue con el mismo signo en los dos bancos y aguanta costos ×2.
   - La parte que excluye (sin compresión o con p(rango) alto) pierde plata en N2 y en N3.
2. **N2 sola no sería significativa** (IC cruza 0). La decisión de sumar N3 y confirmar con la unión fue la que dio poder.
3. **El valor está más en lo que la regla evita que en lo que gana.** Los trades que pasan el filtro dan +0,28 R, poco, y los excluidos −0,32.
   - En monedas donde C6 sin filtro casi no gana (N3, Sharpe 0,04), el filtro lleva la canasta a 0,40.
   - Encaja con el mecanismo de r57: la ruptura paga al salir de una compresión.
4. **Advertencias:**
   - Hay sesgo de supervivencia en los tres bancos.
   - Sharpe absoluto bajo (0,46) y 36% de trimestres positivos: la canasta filtrada de alts sola no es una estrategia. Su único uso posible es como pieza de cartera.
   - La regla pierde el 24% del decil superior de ganadores.
   - El antecedente de F3 sigue en contra: `R54_W1` y ML3.

## Siguiente: F3 (N + 1 → 145)
Construcción ML3 dentro de P-r55: C6' = 0,5 C6(BTC/ETH) + 0,5 canasta filtrada de las alts de U50, escalada a σ_C6.

- **Puertas:** inclusión r51 en las dos ventanas, las puertas de régimen de r55 (incluida la bajista) y costos ×2.
- **Descriptivo:** la regla aplicada a C6 en BTC/ETH.
- 2025 sigue sellado.
