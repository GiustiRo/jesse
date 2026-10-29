# r50 F1d: agenda cerrada (2026-10-25)

**Veredicto: la cartera final no pasa las compuertas de salida, así que no se avanza a la confirmación.**
- **La cartera final es P1** (R1 + rupturas cripto C6). X1 pasa sus compuertas de manga, pero al sumarlo baja el Sharpe de la cartera (1,44 → 1,19) y por eso no entra.
- **P1 pasa todo en 2018-09 → 2025** (la parte larga de la cartera): CAGR 36,9%, DD −14,3%, Sharpe 1,60, DSR 0,99.
- **P1 falla en la ventana común 2021–25:** CAGR 24,6% (meta 30%), mediana mensual 0,00% y DSR 0,76. Las metas de regularidad pasaron a seguimiento: meses positivos 49%, trimestres positivos 60%.
- **PBO = 0,28** sobre 20 canastas de r50 en 2011–25, por debajo del umbral de 0,3. El proceso de selección no luce sobreajustado, pero queda cerca del límite.
- **Hallazgo principal: K1, el carry de funding, tiene Sharpe ~7, CAGR ~22% y DD −0,4%.** Falla solo la compuerta de concentración (top-5 = 94% del PnL), que está pensada para mangas direccionales. Por regla no se rescata.

**N declarado: 90.** N efectivo estimado: ~57, por la correlación media de 0,37 entre canastas. **Corridas Jesse:** 0 de 10.

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1D_PROTOCOL.md`, commiteado antes del código (`579fe3ee`).

## Mangas (canastas; Sharpe de calendario √365)

| Manga | Común: Sharpe | CAGR | DD | Trim. + | Larga: Sharpe | DD | Mitades (≤2017 / ≥2018) | Top-5 / PnL | Compuertas |
|---|---|---|---|---|---|---|---|---|---|
| R1 (referencia) | 0,99 | 5,1% | −7,4% | 55% | 0,90 | −12,6% | 0,52 / 1,28 | 67% | — |
| C6 (referencia) | 1,53 | 8,6% | −3,4% | 65% | 1,47 (2018+) | −4,9% | — / 1,47 | 26% | — |
| T1 TSMOM 1/3/12 m | 0,77 | 2,5% | −5,0% | 50% | 0,68 | −12,9% | 0,33 / 1,14 | 71% | ✗ top-5 |
| T2 T1 + vol de rango | 0,82 | 2,4% | −4,2% | 50% | 0,71 | −12,0% | 0,41 / 1,14 | 69% | ✗ top-5 |
| T3 R1 + vol de rango | 1,04 | 5,2% | −7,1% | 60% | 0,88 | −12,3% | 0,48 / 1,29 | 64% | ✗ top-5, ✗ no mejora a R1 (0,88 contra 0,90) |
| **K1 carry de funding** | **7,20** | **22,2%** | **−0,4%** | **90%** | **7,07** (2020+) | −0,4% | 8,1 / 11,8 (2020–22 / 2023–25) | 93% | ✗ top-5 |
| **X1 momentum transversal 12-1** | 0,93 | 11,0% | −14,6% | 60% | 0,65 | −31,3% | 0,25 / 0,91 | n/a | **✓ pasa** |
| V1 reversión 36 meses | 0,40 | 2,6% | −9,2% | 30% | 0,49 | −32,2% | −0,07 / 0,81 | n/a | ✗ Sharpe, ✗ mitades |

## Carteras (construcción F2: riesgo inverso, vol 17%, k ≤ 8)

| Cartera | Ventana | CAGR | DD | Sharpe | PF | Mediana mes | Sin 2 mejores | DSR (N=90) | Meses + | Trim. + | Compuertas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1 = P2** (R1 + C6) | común 2021-03+ | 24,6% | −14,0% | 1,44 | 3,08 | 0,00% | +87% | 0,76 | 49% | 60% | ✗ CAGR, ✗ mediana, ✗ DSR |
| P1 = P2 | larga 2018-09+ | 36,9% | −14,3% | 1,60 | 3,56 | +0,39% | +471% | 0,99 | 58% | 70% | ✓ todas |
| T4 (tope por correlación) | común | 42,2% | −26,6% | 1,30 | — | 0,00% | — | 0,65 | 47% | 60% | no se aplica: empeora DD y Sharpe |

**Retornos por año de P1:**

| Ventana | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Común | — | — | — | +39,6% | −5,7% | +42,7% | +43,1% | +7,9% |
| Larga | −7,0% | +83,7% | +49,0% | +63,2% | −2,7% | +37,6% | +56,0% | +12,9% |

## Lectura
1. **Sin la reversión, la cartera de tendencia es más honesta pero más débil en 2021–25.** El C0 + C6 de F2 daba Sharpe 1,81 y CAGR 34%; R1 + C6 da 1,44 y 24,6%. La diferencia la aportaban las mangas de reversión, que F3 mostró que no generalizan.
2. **La tendencia v2 (T1, T2, T3) no mejora a R1:** la familia está saturada. El estimador de rango baja el DD un poco, pero no cambia el Sharpe.
3. **X1** (rotación por momentum 12-1) pasa sus compuertas, pero se correlaciona con R1 y no suma a la cartera.
4. **El carry de funding (K1) es, por lejos, la manga con mejor perfil y la más descorrelacionada.** Cobra el funding de los perpetuos cubriendo el precio con spot.
   - Falla la compuerta de concentración porque mantiene pocas posiciones de meses: en cinco años solo abre y cierra un puñado de veces. La compuerta se prerregistró para mangas direccionales y no para carry.
   - **Riesgos no modelados**, por los que el Sharpe de 7 sobreestima:
     - liquidación del corto perpetuo en un rally fuerte si el margen no se gestiona;
     - riesgo de contraparte del exchange;
     - basis que se dispara;
     - el capital inmovilizado en spot;
     - fees de spot reales;
     - funding que en 2026 puede comprimirse.
   - Necesita una auditoría contable antes de cualquier uso.
5. **El PBO de 0,28** indica que elegir la mejor canasta de r50 por su historia no es puro azar, pero está cerca del umbral.

## Decisiones del usuario
La regla vigente dice: sin mangas que pasen, se reporta y se espera. Opciones:
- **a) Prerregistrar compuertas específicas de carry** (por ejemplo, meses positivos, DD máximo y estrés de basis y liquidación en lugar de top-5), evaluar P1 + K1 y, si pasa, ir a la confirmación única. Los perpetuos de confirmación SOL, XRP, BNB y DOGE también tienen funding y sirven para validar K1 fuera de muestra. Suma a N y requiere tu autorización, porque cambia una compuerta prerregistrada.
- **b) Aceptar P1 tal cual e ir a la confirmación**, sabiendo que no pasa en la ventana común. Es una decisión tuya sobre la compuerta.
- **c) Cerrar r50** con el diagnóstico: la tendencia y las rupturas cripto son el núcleo robusto, la reversión no generaliza y el carry es la gran pista pendiente.

**Datos de confirmación:** la descarga del DAX está en curso como archivo y no se miró. Los perpetuos cripto no se importaron.
