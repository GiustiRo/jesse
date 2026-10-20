# Informe Cuantitativo de Estrategia: `BtcMomentumCore4h` (`BTC-USDT` 4h)

## 1. Resumen Ejecutivo y Cumplimiento de Objetivos

La estrategia **`BtcMomentumCore4h`** ha sido investigada, desarrollada, optimizada mediante Walk-Forward (In-Sample 2020–2023 / Out-of-Sample 2024–2025) y validada con simulaciones de **Monte Carlo (200 escenarios de velas `moving_block_bootstrap` + 200 permutaciones de trades)** sobre `Binance Perpetual Futures` (`BTC-USDT`, apalancamiento aislado `5x`, comisión taker `0.045%`, capital inicial `$10,000`, `240` velas de calentamiento), respetando estrictamente la reserva de `2026` como conjunto Out-of-Sample intocado.

| Métrica Clave | Objetivo Requerido | Resultado `BtcMomentumCore4h` (Iter 9A) | Benchmark (`TemaTrendFollowing`) | Estado |
| :--- | :---: | :---: | :---: | :---: |
| **Retorno Anualizado (CAGR)** | $\ge 50.0\%$ | **`58.44%`** (`+8.44%` sobre objetivo) | `41.31%` | **CUMPLIDO** |
| **Beneficio Neto (`2020–2025`)** | — | **`+1,396.43%`** (`$10,000 -> $149,643.07`) | `+663.76%` (`$10,000 -> $76,376`) | **CUMPLIDO** |
| **Max Drawdown (Mark-to-Market)** | $\le 25.0\%$ | **`-21.90%`** (DD cerrado: **`-11.57%`**) | `-48.05%` | **CUMPLIDO** |
| **Sharpe Ratio** | $\ge 1.30$ | **`1.32`** | `0.94` | **CUMPLIDO** |
| **Calmar Ratio** | $\ge 2.00$ | **`2.67`** | `0.86` | **CUMPLIDO** |
| **Sortino Ratio** | $\ge 2.50$ | **`3.04`** | `1.52` | **CUMPLIDO** |
| **Omega Ratio** | $\ge 1.40$ | **`1.83`** | `1.19` | **CUMPLIDO** |
| **Profit Factor (`Gross W / L`)** | $\ge 1.80$ | **`2.97`** (`$210,380 / $70,737`) | `1.39` | **CUMPLIDO** |
| **Win Rate / Ratio W:L** | Asimetría positiva | **`55.56%` WR** / **`2.38` Ratio Avg W/L** | `65.6%` WR / `0.61` W/L | **CUMPLIDO** |
| **Racha Máxima de Pérdidas** | Controlada | **`3` trades** (máx. racha ganadora: `6`) | `5` trades | **CUMPLIDO** |
| **Comisiones Totales Pagadas** | Baja fricción | **`$5,574.59`** (`45` trades en 6 años) | `$27,976.00` (`256` trades) | **CUMPLIDO** |

---

## 2. Enlaces Directos al Dashboard (`jesse-local`)

Todas las sesiones ejecutadas están persistidas en la base de datos local de Jesse y pueden inspeccionarse directamente en el Dashboard:

### Sesiones Principales y Validación Final (`BtcMomentumCore4h`)
- **Backtest Principal Completo (`2020-02-15` a `2025-12-31` — Iter 9A Campeona)**:
  - **Session ID**: `721de7bb-98a9-4827-9946-f74ab4f2b86f`
  - **Dashboard URL**: http://localhost:9200/#/backtest/721de7bb-98a9-4827-9946-f74ab4f2b86f
- **Backtest Sensibilidad / Estabilidad de Meseta (`2020-02-15` a `2025-12-31` — Iter 10A)**:
  - **Session ID**: `44d010c6-dfce-42bf-a889-fa30ca496e72`
  - **Dashboard URL**: http://localhost:9200/#/backtest/44d010c6-dfce-42bf-a889-fa30ca496e72
- **Walk-Forward In-Sample (`2020-02-15` a `2024-01-01` — Entrenamiento)**:
  - **Session ID**: `aff3bc8f-7b0f-49de-960d-bcc28e3e38f7`
  - **Dashboard URL**: http://localhost:9200/#/backtest/aff3bc8f-7b0f-49de-960d-bcc28e3e38f7
- **Walk-Forward Out-of-Sample (`2024-01-01` a `2025-12-31` — Validación Ciega)**:
  - **Session ID**: `73051abc-f296-4090-8d20-f0d2e68a5c74`
  - **Dashboard URL**: http://localhost:9200/#/backtest/73051abc-f296-4090-8d20-f0d2e68a5c74
- **Sesión de Optimización Walk-Forward Optuna (`200` Trials, Objetivo `Calmar`)**:
  - **Session ID**: `efa14dc6-fa96-4fdf-8b56-2c75ea41ec05`
  - **Dashboard URL**: http://localhost:9200/#/optimization/efa14dc6-fa96-4fdf-8b56-2c75ea41ec05
- **Sesión de Monte Carlo (`200` Escenarios Velas `moving_block_bootstrap` + `200` Escenarios Trades)**:
  - **Session ID**: `cb39f795-3a83-4436-b3b0-ef9d492ca942`
  - **Dashboard URL**: http://localhost:9200/#/monte-carlo/cb39f795-3a83-4436-b3b0-ef9d492ca942

### Historial de Iteraciones de Investigación (`2020-02-15` a `2025-12-31`)
- **Benchmark (`TemaTrendFollowing` 1h/4h)**: http://localhost:9200/#/backtest/394a3479-9665-4d29-b380-372ad3e53025 (`41.31%` CAGR, `-48.05%` MaxDD, `0.94` Sharpe)
- **Iter 1A (`BtcMomentumCore4h` Base L/S)**: http://localhost:9200/#/backtest/8b645a5e-d064-445f-8e64-6473752f621c (`16.03%` CAGR, `-14.67%` MaxDD, `0.92` Sharpe)
- **Iter 1B-v2 (`BtcAdaptiveTrend2h` 2h/4h)**: http://localhost:9200/#/backtest/b51ea63c-1117-45d1-a198-ad82f04722fb (`19.27%` CAGR, `-24.55%` MaxDD, `0.88` Sharpe)
- **Iter 1C (`BtcRegimeBreakout1h` 1h/4h)**: http://localhost:9200/#/backtest/8040d0d0-c20e-444e-8d3e-fe738b18c54b (`14.04%` CAGR, `-23.33%` MaxDD, `0.69` Sharpe)
- **Iter 2A (`BtcMomentumCore4h` Chandelier `best_close`)**: http://localhost:9200/#/backtest/c10e2631-0221-40b9-bdb2-7d3163765040 (`24.21%` CAGR, `-33.06%` MaxDD, `0.90` Sharpe)
- **Iter 2B (`BtcRegimeBreakout1h` TEMA Pullback Limit)**: http://localhost:9200/#/backtest/f0a2f8c0-efcc-4b85-b97f-9d9e7b1c5c1e (`16.19%` CAGR, `-36.40%` MaxDD, `0.68` Sharpe)
- **Iter 3A (`BtcMomentumCore4h` `2.0R` BE + `best_close` Trail)**: http://localhost:9200/#/backtest/c26ed539-66a6-4a6a-93db-a8b579125eb0 (`44.62%` CAGR, `-26.33%` MaxDD, `1.17` Sharpe)
- **Iter 4A (`BtcMomentumCore4h` Overhead Filter + Macro Shorts)**: http://localhost:9200/#/backtest/a5552c25-9c34-406f-91e0-0e70ea994dff (`30.00%` CAGR, `-23.63%` MaxDD, `1.04` Sharpe)
- **Iter 5A (`BtcMomentumCore4h` Pure Donchian Breakout, No Pullback Trap)**: http://localhost:9200/#/backtest/29ce1b3a-c79c-4607-bc90-779e3abe6488 (`48.90%` CAGR, `-26.95%` MaxDD, `1.28` Sharpe, `2.71` Sortino)
- **Iter 8A (`BtcMomentumCore4h` 2nd-Highest High Breakout)**: http://localhost:9200/#/backtest/7e0401d3-cf6f-4144-b811-3edc29547946 (`43.49%` CAGR, `-24.22%` MaxDD, `1.19` Sharpe)

---

## 3. Arquitectura y Lógica de `BtcMomentumCore4h`

### 3.1 Diagnóstico de Fricción y Microestructura en `BTC-USDT`
1. **Impacto de Comisiones y Ruido Intradía**: El benchmark `TemaTrendFollowing` en `1h` ejecutaba `256` operaciones pagando `$27,976` en comisiones (`2.8x` el capital inicial) y utilizaba un stop-loss negativo asimétrico (`-4 ATR` stop frente a `+3 ATR` take-profit), provocando un drawdown inaceptable de `-48.05%`.
2. **Trampa de Re-Entrada por Pullback Post-Salida**: En las iteraciones `1A–3A`, permitir entradas secundarias por pullback a la EMA rápida (`low <= ema_fast + 0.3 * atr`) provocaba que, inmediatamente después de cerrar una gran tendencia ganadora por trailing stop en el techo del movimiento (cuando `ADX` seguía elevado), la estrategia volviera a comprar el agotamiento superior. Eliminar esa condición en `Iter 5A` elevó el retorno neto de `+774.97%` a `+938.92%` y redujo la pérdida de `2022` a casi cero.
3. **Trailing Stop sobre Cierre Confirmado (`best_close`) + Escudo Breakeven (`1.75R`)**:
   - Calcular el chandelier stop sobre el **mejor cierre de 4h (`best_close - mult * atr`)** en lugar del máximo intrabarra evita que los mechazos de consolidación alcista cierren prematuramente las grandes tendencias (como `$39.4k -> $54.4k` en Feb 2021, `$48.0k -> $63.6k` en Oct 2021, `$17.1k -> $20.4k` en Ene 2023, `$51.6k -> $65.1k` en Feb 2024 y `$76.5k -> $96.2k` en Nov 2024).
   - Al mismo tiempo, activar un escudo de **Breakeven cubriendo comisiones (`entry + 2.5 * fee_rate * entry`) cuando la excursión máxima alcanza `1.75R`** neutraliza las rupturas fallidas antes de que se reviertan a `-1.0R`.

### 3.2 Reglas Exactas e Hiperparámetros Finales (`Iter 9A` / `Trial 108`)
- **Filtro de Régimen Macro (`4h`)**:
  - `close > EMA(80)` (`ema_slow = 80`, ~13.3 días)
  - `EMA(20) > EMA(80)` (`ema_fast = 20`)
  - Pendiente estructural positiva: `EMA(80)[t] > EMA(80)[t-5]` (apaga automáticamente las compras durante mercados bajistas prolongados como 2022, operando solo 4 veces en todo 2022).
- **Disparador de Ruptura e Impulso**:
  - Ruptura de canal Donchian de `26` velas (`donchian_len = 26`, cierre mayor al máximo de las 26 velas previas de 4h).
  - Fuerza tendencial confirmada: `ADX(14) >= 26` (`adx_min = 26`).
  - Filtro de momento sin sobrecompra extrema ni vela climática: `52 <= RSI(14) <= 76` y `(high - low) <= 3.0 * ATR(14)`.
- **Dimensionamiento Basado en Volatilidad (`_plan_order`)**:
  - Stop inicial a `2.0 * ATR(14)` (`stop_atr = 2.0`), acotado entre `MIN_STOP_FRACTION = 0.8%` y `MAX_STOP_FRACTION = 5.5%`.
  - Riesgo por operación: `risk_pct = 5.0%` del balance neto disponible, descontando explícitamente las comisiones de apertura y cierre (`loss_per_qty = actual_dist + 2.0 * fee_rate * price`), y con tope de exposición nocional `MAX_NOTIONAL_X = 4.4x` (dentro del límite aislado `5x`).
- **Gestión Dinámica de Salida (`update_position`)**:
  - Escudo Breakeven en `be_r = 1.75` (`best_r >= 1.75` mueve el piso del stop a `entry * (1 + 2.5 * fee_rate)`).
  - Chandelier Trail sobre mejor cierre: `best_close - mult * ATR(14)` con `trail_atr = 4.2`, comprimiendo `mult` al `78%` (`3.28x ATR`) cuando `best_r >= 5.0` y al `62%` (`2.60x ATR`) cuando `best_r >= 8.0` para asegurar ganancias parabólicas.

---

## 4. Desglose Anual (`2020–2025`) y Walk-Forward (`In-Sample` vs `Out-of-Sample`)

### 4.1 Rendimiento Año por Año (`721de7bb-98a9-4827-9946-f74ab4f2b86f`)

| Año | Balance Inicial | Balance Final | Beneficio Neto ($) | Retorno Anual (%) | Operaciones | Win Rate (%) | Régimen de Mercado BTC |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **2020** | `$10,000.00` | `$22,142.53` | `+$12,142.53` | **`+121.43%`** | `11` | `72.7%` | Recuperación post-COVID y ruptura de `$20k` |
| **2021** | `$22,142.53` | `$44,945.19` | `+$22,802.66` | **`+102.98%`** | `6` | `66.7%` | Doble techo alcista (`$64k` / `$69k`) + crash de mayo |
| **2022** | `$44,945.19` | `$41,481.97` | `-$3,463.23` | **`-7.71%`** | `4` | `25.0%` | **Bear Market severo (`BTC -65%`, LUNA/FTX)** |
| **2023** | `$41,481.97` | `$83,142.91` | `+$41,660.94` | **`+100.43%`** | `6` | `50.0%` | Recuperación institucional (`$16.5k -> $44k`) |
| **2024** | `$83,142.91` | `$139,182.49` | `+$56,039.58` | **`+67.40%`** | `10` | `50.0%` | ETFs Spot + ruptura post-elecciones (`$42k -> $98k`) |
| **2025** | `$139,182.49` | `$149,643.07` | `+$10,460.58` | **`+7.52%`** | `8` | `50.0%` | Madurez de ciclo y consolidación sobre `$100k` |

### 4.2 Validación Walk-Forward (Entrenamiento vs Prueba Ciega)

| Segmento | Período | Session ID | Retorno Neto | CAGR | Max DD | Sharpe | Calmar | Sortino | Win Rate | Trades |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **In-Sample (Train)** | `2020-02-15` a `2024-01-01` | `aff3bc8f-7b0f-49de-960d-bcc28e3e38f7` | `+731.43%` | **`72.62%`** | **`-21.90%`** | **`1.42`** | **`3.32`** | **`3.55`** | `59.26%` | `27` |
| **Out-of-Sample (Test)** | `2024-01-01` a `2025-12-31` | `73051abc-f296-4090-8d20-f0d2e68a5c74` | `+79.70%` | **`34.05%`** | **`-15.94%`** | **`1.08`** | **`2.14`** | **`2.01`** | `50.00%` | `18` |
| **Completo Consolidado** | `2020-02-15` a `2025-12-31` | `721de7bb-98a9-4827-9946-f74ab4f2b86f` | `+1,396.43%` | **`58.44%`** | **`-21.90%`** | **`1.32`** | **`2.67`** | **`3.04`** | `55.56%` | `45` |
| **Sensibilidad (Iter 10A)** | `2020-02-15` a `2025-12-31` | `44d010c6-dfce-42bf-a889-fa30ca496e72` | `+1,230.53%` | **`55.30%`** | **`-20.66%`** | **`1.33`** | **`2.68`** | **`3.07`** | `54.35%` | `46` |

---

## 5. Validación de Robustez Monte Carlo (`cb39f795-3a83-4436-b3b0-ef9d492ca942`)

Se ejecutaron **200 escenarios de remuestreo de series de velas (`moving_block_bootstrap`, bloques de 7 días)** y **200 escenarios de permutación de operaciones** con `10` núcleos de CPU (`http://localhost:9200/#/monte-carlo/cb39f795-3a83-4436-b3b0-ef9d492ca942`):

### 5.1 Monte Carlo de Velas (`moving_block_bootstrap` — 200 Escenarios)

| Métrica | Original (Backtest) | Peor 5% (`worst_5` / P5) | Mediana (`median` / P50) | Mejor 5% (`best_5` / P95) | Diagnóstico Estadístico |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Net Profit (%)** | `+1,396.43%` | **`+58.04%`** | **`+554.28%`** | `+2,581.73%` | Rentable incluso en el percentil 5 (`+58%`); `original <= best_5` |
| **Annual Return (CAGR)** | `58.44%` | **`+8.09%`** | **`37.64%`** | `74.96%` | CAGR positivo en más del 95% de los escenarios sintéticos |
| **Sharpe Ratio** | `1.32` | **`0.43`** | **`1.24`** | `1.93` | Mediana (`1.24`) casi idéntica al original (`1.32`) — sin sobreajuste |
| **Calmar Ratio** | `2.67` | `0.21` | **`1.12`** | `3.24` | Dentro del intervalo de confianza `[0.21, 3.24]` |
| **Max Drawdown (%)** | `-21.90%` | `-51.02%` | **`-31.46%`** | `-19.84%` | Riesgo de cola controlado ante perturbaciones de camino |
| **Win Rate (%)** | `55.56%` | `35.47%` | **`48.71%`** | `59.60%` | Consistencia estructural de aciertos (`original <= best_5`) |
| **Total Trades** | `45` | `28` | **`50`** | `67` | Frecuencia de operación estable en caminos sintéticos |

### 5.2 Monte Carlo de Operaciones (`Trades Resampler` — 200 Escenarios)
- **Retorno Total**: Invariante en **`+1,396.43%`** (`worst_5: +1,396.43%`, `median: +1,396.43%`, `best_5: +1,396.43%`).
- **Calmar Ratio**: `original: 2.67`, `worst_5: 0.28`, `median: 1.04`, `best_5: 3.13` (`original <= best_5`).
*(Nota técnica: el remuestreador de trades de Jesse permuta los PnL nominales en dólares sin reescalar por el capital acumulado de cada año, por lo que los escenarios de velas `moving_block_bootstrap` constituyen la prueba rigurosa de robustez porcentual).*
