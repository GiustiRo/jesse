# r50 F1b: screening de 10 candidatas «todo terreno» (2026-10-25)

**Veredicto: pasa solo N4, la cartera 50/50 R1 + M2a.**
- **N4:** Sharpe 1,08 contra 0,99 de R1 y trimestres positivos 55%, igual que R1. Ventana larga: Sharpe 0,90 y DD −8,8%. DSR 0,50 en la común y 0,85 en la larga (N=73).
- **Casi pasan, pero no se rescatan:**
  - **R1, R2 y R3** cumplen Sharpe ≥ 0,8 (0,99, 0,99 y 0,92) y no los veta la ventana larga, pero fallan por concentración. Los 5 mejores trades son el 91%, 61% y 71% del PnL.
  - **R6** (rotación mensual) da Sharpe 1,06, CAGR 14% y 80% de trimestres positivos en la común, pero la veta la ventana larga: DD −33%, peor que −25%.
- **Corridas Jesse:** 0 de 10. **N declarado: 73.**

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1B_PROTOCOL.md`, commiteado antes del código (`18313e7d`). Costes, datos y ventanas son los de F1.

## Canastas de 7 activos (equiponderadas; Sharpe de calendario √365)

| Candidata | Rol | Común: Sharpe | CAGR | DD | Trim. + | Trades/año | Top-5 / PnL | ρ con R1 (trim. negativos de R1) | Larga: Sharpe / DD | DSR común / larga |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 Donchian r49 (4h) | tendencia | 0,99 | 5,1% | −7,4% | 55% | 17 | 91% | — | 0,90 / −12,6% | 0,42 / 0,85 |
| R2 ruptura Core4h (4h) | tendencia | 0,99 | 2,6% | −2,8% | 70% | 57 | 61% | 0,44 (0,43) | 0,67 / −8,1% | 0,42 / 0,57 |
| R3 retest K1001 (4h) | tendencia | 0,92 | 2,1% | −1,6% | 75% | 44 | 71% | 0,38 (0,37) | 0,60 / −5,7% | 0,35 / 0,46 |
| R4 Turtle diario | tendencia | 0,78 | 1,3% | −2,1% | 60% | 25 | 55% | 0,69 (0,62) | 0,66 / −6,2% | 0,25 / 0,55 |
| R5 M2a en 4h | diversificador | −1,06 | −3,2% | −16,9% | 25% | 362 | — | 0,49 (0,52) | −0,74 / −44% | 0,00 / 0,00 |
| R6 rotación mensual | tendencia | 1,06 | 14,0% | −19,9% | 80% | 10 | n/a | 0,77 (0,76) | 0,85 / **−33,2%** | 0,48 / 0,80 |
| N1 pullback en tendencia | diversificador | 0,52 | 1,2% | −3,3% | 65% | 48 | 50% | 0,36 (0,31) | 0,30 / −10,4% | 0,10 / 0,11 |
| N2 compresión → ruptura | tendencia | 0,65 | 1,1% | −2,2% | 65% | 18 | 108% | 0,69 (0,59) | 0,62 / −8,3% | 0,17 / 0,50 |
| N3 Faber 10 meses | tendencia | 0,59 | 3,9% | −12,0% | 50% | 8 | 208% | 0,80 (0,88) | 0,59 / −23,8% | 0,13 / 0,45 |
| **N4 R1 + M2a** | combinación | **1,08** | 3,4% | −4,5% | 55% | 48 | n/a | 0,92 (0,92) | **0,90 / −8,8%** | 0,50 / 0,85 |

Los CAGR por canasta son chicos porque promedian 7 mangas, cada una de 1% de riesgo por trade o vol 17% con exposición parcial. El escalado a vol de cartera es tarea de F2. R6 opera como un solo libro, así que su CAGR no está diluido.

## Puertas (PHASE1B_PROTOCOL.md §3)

| Candidata | Puerta principal | Veto de la ventana larga | Resultado |
|---|---|---|---|
| R1 | Sharpe ✓, top-5 ✗ (91%) | no | no pasa |
| R2 | Sharpe ✓, top-5 ✗ (61%), mejora a R1 en trimestres positivos ✓ | no | no pasa (por 1 pp) |
| R3 | Sharpe ✓, top-5 ✗ (71%), mejora a R1 ✓ | no | no pasa |
| R4 | Sharpe ✗ (0,78) | no | no pasa |
| R6 | Sharpe ✓, mejora a R1 ✓ | **sí** (DD −33%) | no pasa |
| N2 | Sharpe ✗ (0,65) | no | no pasa |
| N3 | Sharpe ✗ (0,59), no mejora a R1 | no | no pasa |
| R5 | Sharpe ✗ (−1,06), ρ ✗ | sí | no pasa |
| N1 | Sharpe ✓ (0,52), trades ✗ (48 < 50), ρ ✗ (0,31) | no | no pasa |
| N4 | Sharpe > R1 ✓, trimestres positivos ≥ R1 ✓ | no | **pasa** |

## Por activo (Sharpe, ventana común)

| Activo | R1 | R2 | R3 | R4 | R5 | N1 | N2 | N3 |
|---|---|---|---|---|---|---|---|---|
| BTC | 0,62 | **1,18** | 0,95 | 0,33 | −0,45 | 0,05 | 0,29 | 0,75 |
| ETH | 0,50 | **1,26** | **1,24** | 0,60 | −0,03 | −0,52 | −0,09 | −0,10 |
| Oro | **1,31** | 0,54 | −0,01 | 0,73 | −0,75 | 0,47 | 1,06 | 1,04 |
| SPX | 0,80 | −0,10 | 0,18 | 0,31 | −0,32 | **0,96** | 0,37 | 0,66 |
| WTI | 0,06 | −0,18 | 0,23 | 0,49 | −0,02 | **0,61** | 0,14 | −0,18 |
| Gas | 0,33 | 0,29 | 0,02 | 0,23 | 0,13 | **0,44** | 0,31 | 0,10 |
| Bono (sin lente larga) | −1,29 | −0,93 | −0,64 | −0,74 | −3,09 | −0,83 | −0,39 | −1,09 |

Ventana larga, en el mismo orden (BTC/ETH en spot desde 2018; oro, SPX, WTI y gas desde 2011–13):
- R2: 1,21 / 1,10 / 0,27 / 0,08 / −0,17 / −0,02.
- R3: 1,02 / 1,24 en cripto.
- R1: 1,22 / 0,89 / 0,76 / 0,64 / −0,09 / 0,06.

Detalle completo en `research_scripts/data/r50/f1b_screen.json`.

## Correcciones técnicas (sin cambio de reglas)
1. **Tres errores de código que abortaron corridas antes de producir resultados:** un import circular de Jesse, una llamada a `_step` y el armado de canastas. Ninguna corrida abortada produjo métricas.
2. **Puerta top-5 omitida en la primera evaluación.** El evaluador comparaba un `numpy.bool_` con `is not False`, así que la puerta nunca bloqueaba y R1, R2 y R3 aparecían como «pasa».
   - Se corrigió a booleanos de Python y las puertas se re-evaluaron sobre las mismas métricas guardadas (`gates_note` en el JSON).
   - Es una corrección técnica, no un ensayo nuevo.
3. R1 aplica el slippage extra del bono y del gas mediante `SlipAccount`, según la enmienda 4b. Los demás motores ya lo aplicaban.

## Lectura
1. **El eje de cripto + ruptura es el más fuerte.** R2 y R3 dan Sharpe 1,0–1,26 en BTC y ETH en las dos ventanas.
   - En los CFD (oro, SPX, WTI, gas y bono) las rupturas de 4h no aportan; ahí funcionan R1 en oro y SPX y el pullback (N1) o M2a en SPX y WTI.
   - Ninguna regla «todo terreno» rinde igual en todos los activos.
2. **La concentración (top-5) es la puerta que más filtra a la tendencia.** Es la propiedad conocida de la familia: pocas tendencias largas explican el resultado.
3. **R6 tiene la mejor regularidad** (80% de trimestres positivos en 2021–25), pero un DD de −33% en la larga, en 2013–15 con oro y commodities en caída. No pasa.
4. **La reversión en 4h (R5) muere por costes:** 362 trades/año.
5. **N4 pasa por poco.** Mejora el Sharpe de R1 (1,08 contra 0,99) con la misma regularidad, gracias a la baja correlación de M2a con R1 (0,22 en los trimestres negativos de R1).
   - Ojo: sus dos componentes fallan sus propias puertas de manga (R1 por top-5; M2a en F1 por frecuencia).
   - Su DSR (0,50 común / 0,85 larga) queda lejos de 0,95.

## Siguiente paso
Por protocolo, N4 pasa a F2, la combinación con vol de cartera 17% y las puertas r9. Antes conviene que decidas:
- **Avanzar a F2 con N4.** Se espera que no alcance Q80 ni el DSR, pero da la cifra de cartera escalada.
- **Cerrar F1b sin F2** y redefinir el objetivo.
