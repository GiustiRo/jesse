# r58 F3: integración del filtro a P-r55 (2026-10-27)

**N + 1 → 145.** Enmienda E3 (`41686f11`), commiteada antes de correr. `r58.py integrate` → `data/r58/f3_integrate.json`.

- **I1:** la construcción ML3, C6' = 0,5 C6(BTC/ETH) + 0,5 canasta de C6 filtrada en las 48 alts de U50, escalada a σ_C6, desde el 2021-07-02.
- **Filtro:** compresión ∧ p(rango) < 0,3874.
- **Base:** P-r55 reproducida (1,677 / 1,723).

## Veredicto: **no pasa**
| Puerta (`r55_engine.gates`) | I1 | ¿Cumple? |
|---|---|---|
| g1 bajista (suma ≥ P-r55, mediana ≥ 0) | 0,100 contra 0,132 (ventana larga, trimestres) | **no** |
| g2 lateral | 0,194 contra 0,296; común −0,099 contra +0,004 | **no** |
| g3 alcista | 2,191 contra 2,117 | sí |
| g4 inclusión r51 | ΔSharpe **−0,040** larga, **−0,040** común; −2 trimestres positivos | **no** |
| g4 con costos ×2 | −0,049 / −0,061 | **no** |

## Cartera
| Ventana | | Sharpe | CAGR | DD | Trim. + |
|---|---|---|---|---|---|
| 2018-09→24 | **P-r55** | **1,677** | 41,2% | −14,3% | 19/26 |
| | I1 (canasta filtrada) | 1,638 | 39,8% | −16,3% | 17/26 |
| | Referencia: canasta sin filtrar | 1,613 | 39,1% | −15,3% | 16/26 |
| 2021→24 | **P-r55** | **1,723** | 31,6% | −12,4% | 11/16 |
| | I1 | 1,682 | 29,9% | −17,2% | 10/16 |
| | Referencia sin filtrar | 1,620 | 28,8% | −15,9% | 10/16 |

- **Canasta de alts de U50, 2021-07→24:** filtrada **1,017** (736 trades) contra **0,868** sin filtrar (1.910 trades).
- **Descriptivo, la regla aplicada a C6 BTC/ETH de P-r55:** Sharpe 1,547 / 1,526, contra 1,677 / 1,723. Resta.

## Lectura
1. **El filtro mejora la canasta de alts, pero eso no alcanza para mejorar la cartera.**
   - Dentro de la construcción ML3, filtrar suma +0,025 de Sharpe en la ventana larga y +0,062 en la común frente a la canasta sin filtrar.
   - Aun así, las alts restan frente a P-r55: es el mismo patrón de `R54_W1` y de ML3.
   - **Los trimestres bajistas y laterales empeoran.** La canasta de alts se mueve con BTC/ETH justo cuando C6 BTC/ETH sufre, así que no diversifica.
2. **Aplicado a BTC/ETH, el filtro resta (−0,13 / −0,20).** En dos monedas, la compresión saca demasiadas rupturas buenas. Ya el descriptivo de F1 tenía pocos trades por clase.
3. **El resultado de F2 sigue en pie como conocimiento.** La compresión previa más p(rango) bajo separa rupturas buenas de malas de C6 en monedas nuevas. Lo que no hay es una forma de cartera en la que eso le gane a P-r55.
