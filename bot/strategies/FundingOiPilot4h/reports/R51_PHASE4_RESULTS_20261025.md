# r51 F4: bloque B, cortos en activos con deriva y valor relativo (2026-10-25)

**Resultado:** ninguno de los 3 ensayos pasa las compuertas de manga diversificadora. N pasa de 98 a 101.

Protocolo: `PROTOCOL_R51.md` F4/F6 (`8ac56348`). Código: `r51_sleeves.py` y `r51_explore.py` (`83f9e6ab`).

**Enmienda `73a1c6da`, hecha después de ver la primera corrida de B3:**
- Ninguna regla de r51 mantiene posición a través de un hueco de datos de más de 6 días.
- La primera corrida de B3 había registrado −51% el 2020-08-04 por el hueco abr–jul 2020 del WTI, en que se excluyeron los precios negativos.
- No cambia ninguna regla ni ningún parámetro.
- B1 y B2 dan idéntico con y sin la enmienda.

**Decisiones de implementación fijadas antes de los resultados:**
- B3 usa la unión de las ventanas bajistas de los 7 activos para la compuerta 2.
- En 2021–25, las mangas cripto diarias usan barras spot más el funding real del perpetuo, porque el perpetuo no tiene 252 días de historia en 2020.
- B1 opera el perpetuo 4h en 2021–25.

## Resultados (canasta del ensayo)
| Ensayo | Lente decisión: Sharpe | CAGR | DD | Trim. + | 2021–25: Sharpe | Larga: Sharpe / DD | PnL en bajistas | ρ con P1 | Trades | Pasa |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 corto cripto 4h | 0,23 | +0,2% | −1,9% | 19% | −0,07 | 0,23 / −1,9% | +1,9% | −0,03 | 38 | no (G1, G5) |
| B2 corto-o-plano de crisis | −0,25 | −1,7% | −16,9% | 13% | −0,20 | −0,12 / −20,3% | **+69%** | **−0,26** | 56 | no (G1, G3) |
| B3 momentum entre activos | 0,03 | −0,3% | −21,6% | 44% | 0,05 | 0,21 / −28,1% | +14% | 0,11 | — | no (G1) |

Notas de la tabla:
- La lente de decisión es spot desde 2018 para cripto y CFD desde 2018-09 para el resto; B3 arranca en 2019-04.
- «PnL en bajistas» es la suma de los retornos diarios de cada manga dentro de sus ventanas bajistas.
- En B1 la lente larga coincide con la de decisión, porque spot empieza en 2017-08.
- La compuerta top-5 de B1 da 373% del PnL: el PnL total es casi cero.

**B2 por activo (Sharpe en decisión):**
- SPX −0,25 (DD −21%).
- Oro −0,64 (DD −31%).
- BTC +0,18; en 2021–25, +0,30.

## Lectura
1. **Los cortos en activos con deriva ganan en los bajistas y pierden afuera.**
   - B2 suma +69% en sus ventanas bajistas y es la manga más anticorrelacionada con P1 (−0,26).
   - Pero el filtro (retorno a 12 meses < 0 y precio bajo la SMA200) entra tarde y sale tarde. Paga los rebotes y los mercados laterales, sobre todo en el oro.
   - Coincide con la evidencia: en activos con deriva, la pata corta compra cobertura de crisis a costa del retorno medio (Hamill-Rattray-Van Hemert).
2. **El corto cripto 4h casi no opera.** Hacen falta régimen bajista diario y ruptura de mínimos con ADX y RSI a la vez: 38 trades en 7,5 años, con un aporte cercano a cero.
3. **El momentum entre los 7 activos** no tiene ventaja con un universo tan chico. Coincide con lo publicado para pocos activos correlacionados.
4. Lo mejor del bloque es la cobertura de B2 en bajistas, pero el protocolo exige Sharpe ≥ 0,3 y que no lo vete la lente larga. **No se rescata ni se ajusta.**

## Archivos
- `research_scripts/data/r51/explore_B.json`.

## Siguiente paso
- F5 (pronósticos continuos T1/T2), ya corrida: se informa aparte.
- F3, el bloque A, cuando terminen las descargas de Brent y EURUSD.
