# r49 Fase 0: línea base (2026-10-24)

**Veredicto:** ninguna manga pasa las puertas r49. La OOS 2026 de `BtcMomentumCore4h` congelado pierde (−35,2% a riesgo 5%, −15,6% a riesgo 2%/3x; 1 de 10 trades ganadores). El ensamble Donchian nulo (Sharpe 1,04, DD 11,8%) queda como el listón real de la Fase 2. Ninguna referencia histórica supera DSR ≥0,95 con N efectivo ≈50, salvo K1001 B/C en el límite (0,945/0,941), y K1001 ya falló 2026.

## Configuración común
- Binance Perpetual Futures, BTC-USDT 4h, balance 10.000, fee 0,00045 por lado, aislado.
- Funding histórico aplicado y verificado (settlements > 0 en cada corrida con funding).
  - OOS 2026: dataset `0ab14bc2…` (2020-01-01→2026-10-24, importado en esta fase, cobertura completa).
  - 2020–2025: dataset `9c5618c2…`, el mismo de r10/r11.
- Presupuesto: 4 corridas económicas de 8 permitidas, máximo 2 simultáneas. Hubo 5 intentos técnicos fallidos, ninguno con resultado económico (ver *Incidencias*).

## Corridas nuevas

| Corrida | Sesión | Ventana | CAGR | DD | Sharpe | PF | Trades | Top-5 / PnL | Meses + | Trim. + | Expos. BTC media | Funding |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a. OOS Core 5%/5x | http://localhost:9200/#/backtest/ce3856a8-6ebe-47c4-9053-81e2adf27b82 | 2026-01-01→10-23 | −41,5% (neto −35,2%) | −35,2% | −2,95 | 0,005 | 10 | n/a (PnL < 0) | 0/10 | 0/4 | 0,14x | +7,5 USDT; 885 settlements |
| b. OOS Core R2 2%/3x | http://localhost:9200/#/backtest/00e1bb5f-707f-432b-9d6e-fa5544ed9f56 | 2026-01-01→10-23 | −19,0% (neto −15,6%) | −15,6% | −2,95 | 0,005 | 10 | n/a (PnL < 0) | 0/10 | 0/4 | 0,05x | +2,7 USDT; 885 settlements |
| Nulo (i) B&H 1x | http://localhost:9200/#/backtest/02e52011-7dcb-45bb-98c1-ce7f15e99a82 | 2020-10-15→2026-01-01 | 47,6% | −76,7% | 0,96 | — | 1 | 100% | 58% | 55% | 0,99x | **sin funding** (ver Incidencias) |
| Nulo (ii) Donchian ens. | http://localhost:9200/#/backtest/b4792187-8847-450d-9f52-320edb4a61dd | 2020-10-15→2026-01-01 | 12,9% | −11,8% | 1,04 | 6,34 | 11 ciclos | 118% | 47% | 41% | 0,19x | −2.377 USDT; 5.712 settlements |

Las métricas salen de las curvas diarias MTM de cada sesión, calculadas con `run_analysis`. El Sharpe coincide con el del motor.

- **B&H en 2026:** la serie benchmark de las sesiones a/b es solo precio. BTC −8,4% en la ventana (−10,3% anualizado), DD −39,5%.
- **B&H escalado a la exposición media:** −0,3% (a) y −0,1% (b) anualizado. Las dos OOS pierden contra el B&H, contra el B&H escalado y contra estar en efectivo.

### Diagnóstico de la OOS 2026
Hubo 10 entradas por ruptura Donchian 26 con filtros EMA/ADX. Nueve terminaron en el stop inicial (≈ −1R después de fees) y una cerró en break-even (+0,5%). Ninguna llegó al trailing.

En 2026 BTC marcó rupturas que no continuaron: de ~74k a ~63k y de ~80k a ~86k con reversiones rápidas. El sistema depende de pocas tendencias largas (en 2020–2025 el top-5 explicaba el 99% del PnL) y en 2026 no hubo ninguna. Es lo esperado para una manga de tendencia con 45 trades en 6 años. No alcanza para descartar la familia, pero sí para descartar esta receta como manga autónoma.

**Limitación:** el equipo vivió 2026 en tiempo real, aunque las reglas de `BtcMomentumCore4h` se congelaron antes de abrir el año. El código ejecutado es idéntico al del reporte de Fase 1 (sha256 `443e25cf…`, sin cambios en git desde el checkpoint `0dfb91d5` del 2026-10-20). Las sesiones de Fase 1 son anteriores a ese checkpoint.

## Deflated Sharpe

Método Bailey–López de Prado sobre retornos diarios, con T = días. SR* es el máximo esperado de N Sharpe nulos con varianza del estimador 1/T, expresado en Sharpe anual.

| Sesión | Sharpe | Skew | Kurt | SR* N=650 | DSR 650 | DSR 200 | DSR 50 | DSR 20 |
|---|---|---|---|---|---|---|---|---|
| OOS a / b (295 d) | −2,95 | −2,36 | 20,2 | 3,48 | 0,00 | 0,00 | 0,00 | 0,00 |
| Donchian nulo (1.904 d) | 1,04 | 0,71 | 13,3 | 1,37 | 0,22 | 0,35 | 0,54 | 0,69 |
| B&H nulo (1.904 d) | 0,96 | 0,28 | 6,9 | 1,37 | 0,17 | 0,28 | 0,46 | 0,61 |
| BtcMomentumCore4h iter9A (2.146 d)* | 1,32 | ≈0 | ≈3 | 1,29 | 0,52 | 0,66 | 0,82 | 0,90 |
| Baseline3 riesgo 3%* | 1,38 | ≈0 | ≈3 | 1,29 | 0,59 | 0,72 | 0,86 | 0,93 |
| K1001 B (1.903 d) | 1,66 | 1,64 | 17,3 | 1,37 | 0,76 | 0,86 | **0,945** | 0,98 |
| K1001 C (1.903 d) | 1,65 | 1,49 | 16,4 | 1,37 | 0,75 | 0,85 | 0,941 | 0,97 |
| V3 CHANNEL_P (731 d) | 0,90 | 2,55 | 18,3 | 2,21 | 0,02 | 0,06 | 0,14 | 0,25 |

\* Las dos referencias Core no tienen curva de equity guardada en la base. Su DSR usa el Sharpe del motor con momentos normales, que es una cota optimista. Con la curva reconstruida desde trades (equity realizada, skew 19 y kurtosis 444) el DSR a N=650 cae a 0,11.

**N declarado:**
- **650 es la cota superior.** Cuenta sesiones, no hipótesis independientes.
- **Agrupamiento de curvas:** sobre las 5 referencias con curva diaria 2021–2025 la razón de participación de autovalores da N_eff = 2,8. Core iter9A y Baseline3 tienen ρ = 1,00, K1001 B y C ρ = 0,99, y las demás ρ ≤ 0,25. Las variantes de una misma familia colapsan a un solo ensayo.
- **No hay curvas de los ~650 ensayos** (las sesiones archivadas no se cargaron). Por eso el N efectivo se estima contando familias de hipótesis en `HISTORY_SUMMARY.md`:
  - ~28 ciclos de descubrimiento r10–r48;
  - 6 ciclos de funding/OI V1–V6;
  - ~5 familias de Fase 1, incluida la selección Optuna de 200 trials;
  - ~10 familias de cartera y PAXG/SPY.
  
  Total ≈ **50 (N efectivo declarado)**, con sensibilidad 20–200.
- Con N = 50, ninguna referencia pasa DSR ≥ 0,95. K1001 B/C quedan a 0,005–0,01 del umbral, son carteras multiactivo y ya fallaron en 2026.

## Puertas de manga r49 (corridas nuevas)

| Puerta | a. OOS 5% | b. OOS 2% | Donchian nulo |
|---|---|---|---|
| DSR ≥ 0,95 (N = 50) | ✗ 0,00 | ✗ 0,00 | ✗ 0,54 |
| Sharpe neto ≥ 0,8 | ✗ −2,95 | ✗ −2,95 | ✓ 1,04 |
| Trades ≥ 100 (≥ 30 diaria) | ✗ 10 | ✗ 10 | ✗ 11 ciclos |
| Top-5 < 60% del PnL | ✗ (PnL < 0) | ✗ (PnL < 0) | ✗ 118% |
| Supera B&H / B&H escalado | ✗ / ✗ | ✗ / ✗ | ✗ en CAGR (12,9% vs 47,6%); ✓ vs B&H escalado (10,7%, DD 21,9%) y en Sharpe (1,04 vs 0,96) |
| Supera Donchian nulo | ✗ (sin nulo 2026; pierde en absoluto) | ✗ | — |

Ningún año con DD > 2× la mediana: no se evaluó, porque ninguna corrida llega a las puertas previas.

## Incidencias (técnicas, sin resultado económico)

1. **OOS a/b, intentos 1 y 2:** `BTC execution candles do not span the full funding backtest window`.
   - Faltaban las velas del 2026-10-20 al 24. Se importaron desde 2025-11-01 (regla de 2 meses).
   - El segundo intento siguió leyendo la caché de velas incompleta. Se resolvió con `clear_candle_cache`.
2. **B&H nulo con funding**, a 2x, 5x y 20x de margen aislado: `InsufficientMargin: Funding exhausts available margin`.
   - Un largo perpetuo ~1x sostenido desde 2020-10 paga en 2021–22 un funding acumulado que supera el equity libre.
   - El motor no modela el consumo de colateral aislado y se detiene.
   - El B&H se corrió **sin funding** (equivalente a BTC spot). Esto lo favorece: el Donchian nulo pagó 2.377 USDT de funding con solo 0,19x de exposición media.
   - Hallazgo lateral: el B&H en perpetuo no es un benchmark viable con este motor. El funding es un coste de primer orden para cualquier manga larga de baja rotación.

## Conclusiones
1. `BtcMomentumCore4h` como manga autónoma queda descartada en 2026: 10 trades, todos de pérdida o break-even. Su DSR histórico (≤0,82 a N = 50) ya no alcanzaba la puerta.
2. El Donchian sin optimizar, vol-targeted y long/flat, rinde Sharpe 1,04 con DD 11,8% en 2020–2025. Es comparable o mejor en Sharpe que todas las referencias BTC-only y no necesitó selección. Cualquier propuesta de tendencia BTC debe superarlo.
3. Las puertas de manga no son alcanzables por un solo activo con frecuencia de tendencia (11–45 ciclos en 5 años; top-5 > 60%). Confirma el diagnóstico de r49: la regularidad y el DSR deben salir de la cartera.
4. K1001 B/C son las únicas referencias cerca del DSR (≈0,94 a N = 50), pero son carteras y fallaron 2026. No se rescatan (regla r49).

## Recomendación para la Fase 2
- Usar el **ensamble Donchian 20/55/120/250 d vol-target 17%** (`R49NullDonchianEnsBtc`) como motor común. Aplicarlo sin cambios de lookbacks a PAXG y SPY (Massive, con trading hours) y medir la correlación de las tres curvas.
- Evaluar las puertas de trades y top-5 **a nivel cartera o familia**: con lookbacks de 20–250 días ninguna manga suelta tendrá ≥100 trades.
- Sustituir el conteo de trades por ciclos de exposición o rebalanceos, o reconocer explícitamente la excepción de manga diaria (≥ 30) con tesis.
- Modelar el funding como coste explícito en la sizing de mangas largas de BTC. Considerar un freno por funding alto (ya previsto como freno de riesgo) antes de añadir señales.
- Presupuesto restante r49: 11 corridas económicas. Fase 2 con 3 corridas (una por activo) y la Fase 3 de cartera.

Dashboard (sesiones nuevas):
- http://localhost:9200/#/backtest/ce3856a8-6ebe-47c4-9053-81e2adf27b82
- http://localhost:9200/#/backtest/00e1bb5f-707f-432b-9d6e-fa5544ed9f56
- http://localhost:9200/#/backtest/02e52011-7dcb-45bb-98c1-ce7f15e99a82
- http://localhost:9200/#/backtest/b4792187-8847-450d-9f52-320edb4a61dd

Análisis: job `e2d5ee40e2684443a0da1adc537c6ec6` (`run_analysis`, `output/summary.csv`).
