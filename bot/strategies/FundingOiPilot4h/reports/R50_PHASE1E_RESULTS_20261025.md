# r50 F1e: carry de funding realista y cartera P3 (2026-10-25)

**Veredicto:**
- **K1r pasa todas sus compuertas de carry.**
- **La cartera P3** (R1 + rupturas cripto C6 + K1r) **pasa todas las compuertas en la ventana larga y casi todas en la común.** Solo falla el CAGR de 2021–25: 23,9% contra la meta de 30%.

| Ventana | CAGR | DD | Sharpe | DSR (N=92) |
|---|---|---|---|---|
| Común (2021–25) | 23,9% | −9,1% | 2,03 | 0,98 |
| Larga (2020-06+) | 32,1% | −7,2% | 2,68 | 1,00 |

**Por qué falla el CAGR:** el factor k quedó en el techo de 8 (media 7,93) y el carry tiene su propio techo de 1,5x. La cartera no puede usar todo su presupuesto de vol. La causa es el límite de apalancamiento prerregistrado, no la falta de ventaja.

**Por regla, sin cartera que pase no se avanza a la confirmación:** se reporta y decide el usuario. **N declarado: 92. Corridas Jesse:** 0 de 10.

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1E_PROTOCOL.md`, commiteado antes del código (`0dcebff3`).

## K1r: carry de funding (BTC y ETH, 2020-02 → 2025)

| Métrica | Valor | Compuerta |
|---|---|---|
| Sharpe neto | 8,24 | ≥ 1,0 ✓ |
| CAGR | 7,9% | — |
| DD | −0,38% | ≤ 10% ✓ |
| Meses positivos | 84,5% | ≥ 70% ✓ |
| Trimestres positivos | 91,7% | — |
| Mitades 2020–22 / 2023–25 | 8,4 / 10,7 | > 0 ✓ |
| Funding × 0,5: Sharpe / CAGR | 5,08 / 3,0% | Sharpe ≥ 0,5 ✓ |
| Peor 30 días | −0,32% | ≥ −5% ✓ |
| Auditoría de funding | diferencia 2×10⁻¹⁵ | < 0,1% ✓ |

**Por año:**

| 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| +7,2% | +24,3% | +0,4% | +4,9% | +8,1% | +3,1% |

| Moneda | Funding cobrado | Costes | Re-hedges forzados | Días en posición |
|---|---|---|---|---|
| BTC | 5.834 USDT | 541 | 10 | 1.705 de 2.147 (79%) |
| ETH | 6.415 USDT | 412 | 8 | 1.562 de 1.965 (79%) |

**Lectura:** el carry de funding es la manga más estable de toda la investigación. Pero su retorno sin apalancar es modesto (~8% anual) y depende de un régimen de funding alto: 2021 aporta 24%, mientras 2022 y 2025 quedan cerca de cero.

**Riesgos que el backtest no captura:**
- contraparte del exchange: spot y perpetuo en Binance;
- separación de billeteras spot y futuros, que complica reponer margen;
- cambios de fórmula o de intervalo de funding;
- slippage en eventos de liquidez extrema, como marzo 2020 o mayo 2021;
- compresión estructural del funding en 2026 o después.

## Cartera P3 (construcción F2: riesgo inverso, vol 17%, k ≤ 8; carry k ≤ 1,5)

| Ventana | CAGR | DD | Sharpe | PF | Mediana mes | Sin 2 mejores | DSR (N=92) | Meses + | Trim. + | k medio | Compuertas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Común 2021-03+ | **23,9%** | −9,1% | 2,03 | 3,62 | +0,27% | +111% | 0,98 | 59% | 70% | 7,93 | ✗ CAGR; ✓ las demás |
| Larga 2020-06+ | 32,1% | −7,2% | 2,68 | 3,90 | +0,70% | +237% | 1,00 | 63% | 74% | 8,00 | ✓ todas |

**Por año:**

| Ventana | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| Común | — | +50,3% | −3,2% | +32,3% | +35,4% | +8,1% |
| Larga | +22,7% (jun–dic) | +81,7% | −0,9% | +32,4% | +42,7% | +10,9% |

**Pesos de riesgo finales:** R1 14%, C6 13% y K1r 74%. **La cartera es mayormente carry.**

## Lectura
1. **P3 es la mejor candidata de r50** por Sharpe (2,0–2,7), DD (< 10%) y DSR (≥ 0,98), y es la única que pasa la ventana larga con margen.
2. **La compuerta de CAGR falla por apalancamiento, no por ventaja.** Con k topado en 8, un Sharpe de 2 rinde ~24% anual. Para llegar a 30% habría que subir el techo de k o el del carry, y esa es una decisión de riesgo:
   - más apalancamiento en carry aumenta el riesgo de liquidación y de contraparte, que el backtest subestima;
   - un DD de −9% deja margen numérico, pero ese margen sale de un modelo que no ve esos riesgos.
3. **La concentración en carry (74% del riesgo)** convierte a P3 en una apuesta a que el funding de BTC y ETH siga alto. 2025 (+8%) muestra lo que pasa cuando se comprime.

## Decisiones del usuario
- **a) Aceptar P3 como candidata** con el CAGR observado (~24% en 2021–25, DD < 10%) e ir a la confirmación única ya prerregistrada:
  - K1r en SOL, XRP, BNB y DOGE;
  - R1/C6 en activos nuevos y 2026;
  - después F4 en Jesse.

  Equivale a aceptar ~24% como CAGR objetivo para este nivel de riesgo.
- **b) Subir el techo de apalancamiento** (k o carry) para buscar el 30%. Es una decisión de riesgo tuya y suma a N.
- **c) Cerrar r50** con P3 documentada como la mejor candidata sin confirmar.
