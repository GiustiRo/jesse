# r51 F2: diagnóstico de P1 (2026-10-25)

Fase descriptiva. No suma a N, que sigue en 98. Protocolo: `PROTOCOL_R51.md` F2.

## P1 con la corrección de F1
| Ventana | CAGR | DD | Sharpe | Trim. + |
|---|---|---|---|---|
| 2021–25 (bono de Jesse) | 24,3% | −14,0% | 1,42 | 60% |
| 2018-09+ (sin bono, como en r50) | 36,9% | −14,3% | 1,60 | 70% |

- En 2021–25 la corrección del bono resta 0,3 pp de CAGR y 0,014 de Sharpe frente a r50 (24,6% / 1,44).
- La ventana 2018-09+ reproduce r50 exacto. Eso valida la atribución por componente.

## Quién aporta (suma de contribuciones diarias de la cartera)
| Ventana | Cripto (R1 + C6) | Metales | Acciones | Energía | Bono |
|---|---|---|---|---|---|
| 2018-09+ | +191% | +35% | +17% | +0,4% | — |
| 2021–25 | +85% | +22% | +14% | +1,5% | **−10%** |

- Las mangas que más aportan son C6/BTC (+68%), C6/ETH (+56%), R1/BTC (+40%), R1/oro (+35%) y R1/ETH (+27%).
- R1/WTI resta en las dos ventanas.
- **Todo el PnL de P1 es largo: no tiene pata corta.**

## Trimestres objetivo (P1 ≤ 0)
**2018-09+: 8 trimestres** (2018Q3 dura un día y no cuenta):

| Trimestre | P1 | Qué cayó (comprar y mantener) | Cota corta ideal más grande |
|---|---|---|---|
| 2018Q4 | −7,0% | BTC −44%, ETH −44%, SPX −14%, WTI −38% | acciones +28%, energía +14%, cripto +13% |
| 2019Q3 | −2,5% | BTC −24%, ETH −38% | cripto +7% |
| 2022Q2 | −1,3% | BTC −56%, ETH −67%, SPX −17%, oro −7% | cripto +17%, acciones +14% |
| 2022Q3 | −4,9% | WTI −25%, oro −8%, SPX −5% | metales +10%, energía +5% |
| 2022Q4 | −2,0% | gas −35%, BTC −15% | energía +5%, cripto +4% |
| 2023Q3 | −4,2% | BTC −12%, ETH −14% | cripto +6%, acciones +5% |
| 2025Q1 | −0,9% | ETH −45%, BTC −12%, SPX −5% | cripto +9%, acciones +7% |
| 2025Q4 | −2,6% | ETH −28%, BTC −23% | cripto +12% |

**2021–25:** se agregan 2023Q2 y 2025Q2. Ahí el bono cayó en 2022Q2, 2022Q3, 2023Q2 y 2023Q3; su cota ideal es de +12%, +10%, +4% y +15%.

La cota es un techo informativo: corto a vol 17% justo en los trimestres en que el subyacente cayó.

## Lectura
1. **En 6 de los 8 trimestres negativos de 2018-09+, la caída fue de cripto.** R1 cripto pierde 1–2% en cada uno por los rebotes falsos.
   - Es la familia donde un corto con régimen tiene más para cubrir (B1, B2).
   - La evidencia externa advierte que los perdedores cripto rebotan fuerte.
2. **El bono cae en 4 de los 10 trimestres negativos de 2021–25.** R1, solo largo, le resta 10% a la cartera en esa ventana.
   - Es el caso más claro para A1/A2, tendencia largo/corto con o sin compuerta de correlación.
3. **Energía y acciones:** pocas caídas grandes en esos trimestres (2018Q4, 2022Q2 y Q3).
   - La cota de acciones viene casi toda de 2018Q4 y 2022Q2. Para B2 la ventana es chica.
4. **El oro compensa en 5 de los 8 trimestres** (2018Q4, 2019Q3, 2022Q4, 2025Q1 y 2025Q4). Es la fortaleza a conservar.
5. **WTI** pierde en 6 de los 8, como largo que compra rebotes. No aporta como está.

## Archivos
- `research_scripts/r51_lib.py`: P1 reconstruida y atribución.
- `research_scripts/r51_f2.py`.
- `research_scripts/data/r51/f2_diagnosis.json`.

## Siguiente paso
F3, el bloque A (bono, WTI y gas), con las reglas fijadas en el protocolo. Suma 5 a N.
