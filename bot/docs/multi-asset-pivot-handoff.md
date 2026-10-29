# Instructivo de Handoff para Agentes: Pivote Fase 2 (Multi-Activo Descorrelacionado + Ejecución Intra-Vela)

> **Propósito de este documento:** Este archivo contiene todo el contexto técnico, resultados de la Fase 1, lecciones aprendidas, restricciones duras y el plan de arquitectura aprobado por el usuario para la **Fase 2**. Está diseñado para que un nuevo agente de IA (en cualquier IDE) pueda retomar el trabajo de inmediato sin perder contexto ni repetir caminos descartados.

---

## 1. Contexto General y Reglas Operativas del Repositorio

Antes de ejecutar cualquier acción, el agente **debe** leer:
1. [`DOCS.md`](../../DOCS.md) — Índice general y decisiones vigentes del proyecto.
2. [`AGENTS.md`](../../AGENTS.md) — Convenciones del framework Jesse.
3. [`bot/AGENTS.md`](../AGENTS.md) — Reglas específicas para operar estrategias mediante el servidor MCP de Jesse.
4. [`bot/strategies/BtcMomentumCore4h/__init__.py`](../strategies/BtcMomentumCore4h/__init__.py) y su reporte oficial [`bot/strategies/BtcMomentumCore4h/reports/BTCUSDT_MomentumCore4h_Report.md`](../strategies/BtcMomentumCore4h/reports/BTCUSDT_MomentumCore4h_Report.md).

### Entorno de Ejecución Local
* **Instancia local de investigación:** Corriendo en `http://localhost:9200` (directorio de ejecución: `c:\dev\trading\regime-trade\jesse\bot`).
* **Servidor MCP:** `jesse-local` (`http://localhost:9200/mcp`). Usar las herramientas MCP nativas de Jesse para importar velas, correr backtests, optimizaciones y simulaciones Monte Carlo.
* **Producción (NO TOCAR salvo pedido explícito):** Raspberry Pi (`http://192.168.1.10:9100`, MCP `jesse-pi`). Toda la investigación se hace en `jesse-local`.
* **Regla crítica de datos Out-of-Sample (OOS):** Calibrar, investigar y optimizar **únicamente con datos desde `2020-01-01` hasta `2025-12-31`**. El año **`2026` está estrictamente reservado** como conjunto de validación final (Out-of-Sample puro).

---

## 2. Resumen de lo Logrado en la Fase 1 (Línea Base)

En la Fase 1 se desarrolló, optimizó (Walk-Forward Optuna) y validó mediante Monte Carlo la estrategia **`BtcMomentumCore4h`** ([`bot/strategies/BtcMomentumCore4h/__init__.py`](../strategies/BtcMomentumCore4h/__init__.py)) operando únicamente `BTC-USDT` en `Binance Perpetual Futures` (`4h`, `5x` Isolated, `0.045%` fee, `$10,000` capital inicial, `240` warmup candles):

* **Período validado:** `2020-02-15` a `2025-12-31`
* **Retorno Anualizado (CAGR):** **`58.44%`** (Objetivo: $\ge 50\%$)
* **Retorno Neto Acumulado:** **`+1,396.43%`** (`$10,000` $\rightarrow$ `$149,643.07`)
* **Max Drawdown (Equity):** **`-21.90%`** (`-11.57%` en trades cerrados)
* **Sharpe / Sortino / Calmar / Omega:** **`1.32` / `3.04` / `2.67` / `1.83`**
* **Profit Factor / Win Rate:** **`2.97`** / **`55.56%`** (`45` trades totales; `35` longs y `10` shorts)
* **Walk-Forward:** In-Sample (`2020–2023`): `59.45%` CAGR, `1.29` Sharpe | Out-of-Sample (`2024–2025`): `55.66%` CAGR, `1.37` Sharpe, `-17.43%` MaxDD.
* **Monte Carlo (200 escenarios Candles + 200 Trades):** Mediana CAGR `56.60%` (Candles) / `58.44%` (Trades), percentil 5 de CAGR `28.99%`.
* **IDs de Sesiones en Base de Datos Local (`jesse-local`):**
  * Backtest Principal (`Iter 9A`): `721de7bb-98a9-4827-9946-f74ab4f2b86f`
  * Test de Sensibilidad (`Iter 10A`): `44d010c6-dfce-42bf-a889-fa30ca496e72`
  * Walk-Forward IS (`2020–2023`): `aff3bc8f-7b0f-49de-960d-bcc28e3e38f7`
  * Walk-Forward OOS (`2024–2025`): `73051abc-f296-4090-8d20-f0d2e68a5c74`
  * Optimización Optuna: `efa14dc6-fa96-4fdf-8b56-2c75ea41ec05`
  * Monte Carlo: `cb39f795-3a83-4436-b3b0-ef9d492ca942`

### ¿Por qué hacemos el Pivote a la Fase 2?
Aunque `BtcMomentumCore4h` cumplió holgadamente el objetivo de $>50\%$ anual con bajo drawdown, **solo realizó 45 operaciones en casi 6 años (~7.6 trades/año)** y, al depender de rupturas de tendencia de un único activo (`BTC-USDT`) esperando al cierre de la vela de 4h:
1. Pasa meses enteros sin operar cuando BTC lateraliza.
2. Al entrar al **cierre de la vela de 4h** (`self.buy = qty, self.price`), si la vela de ruptura tiene una gran expansión, entra tarde y lejos del borde del rango (empeorando el precio de entrada y agrandando la distancia al Stop Loss).

---

## 3. Caminos Explícitamente Descartados (NO REPETIR)

El nuevo agente **NO debe proponer ni implementar** ninguno de los siguientes enfoques, que ya fueron probados por el usuario o descartados con evidencia técnica:

1. **PROHIBIDO usar Hidden Markov Models (HMM) + LightGBM / Triple-Barrier ML ni features de Derivados (`Funding Rate`, `Open Interest`):**
   * El usuario ya desarrolló y probó durante meses un sistema completo inspirado en Marcos López de Prado (`3-state Gaussian HMM` con confirmación de 6 barras de 4h + `LightGBM` multiclase de 1200 árboles con Triple-Barrier labels y 8 variables de Funding/OI de Binance).
   * **Por qué falló en la práctica:**
     * Las variables de derivados de un solo exchange (`funding_rate`, `oi_change`, etc.) no son estacionarias: con la llegada de los ETFs Spot (IBIT), CME y el arbitraje institucional *cash-and-carry*, el significado del Funding y OI en Binance cambió estructuralmente respecto a 2020–2023, además de ignorar eventos en Kraken/Coinbase/CME.
     * La confirmación del HMM (`6` velas de 4h = `24h`) introduce un retraso severo ante reversiones en V.
     * Los árboles de decisión (`max_depth=5`, `min_confidence=0.36`, `margin=0.02`) sobre-ajustan el lockbox pero son inestables fuera de muestra.
2. **PROHIBIDO usar Altcoins Cripto (`ETH`, `SOL`, `BNB`, etc.) como supuesto "portafolio descorrelacionado":**
   * En momentos de estrés o liquidaciones de mercado, la correlación entre altcoins y BTC tiende a `0.85 – 0.95`. Operar múltiples criptomonedas con la misma lógica equivale a multiplicar el apalancamiento en el mismo factor de riesgo.
3. **PROHIBIDO usar Take-Profits Parciales Tempranos (ej. 50% en 1R y 50% en 2R):**
   * Con un Win Rate cercano al `50%`, perder el `100%` de la posición en los Stop Loss (`-1.0R`) y cobrar solo el `50%` en el primer objetivo destruye la esperanza matemática de una estrategia seguidora de tendencia. Incluso en el bot previo del usuario, el sistema solo sobrevivió cuando se retrasó el Breakeven a `2.25R` y el Trailing a `3.0R`.
4. **PROHIBIDO usar el Ulcer Index como objetivo de optimización:**
   * Es una métrica pasiva de 1987 que no actúa sobre las posiciones ni garantiza regularidad mensual. En su lugar se usará el **Auditor de Consistencia Mensual** descrito en la Sección 4.4.

---

## 4. Arquitectura Aprobada para la Fase 2 (El Pivote)

El objetivo de la Fase 2 es **aumentar la frecuencia de operaciones de calidad y lograr consistencia de retornos mes a mes, independientemente del estado de un mercado individual**, apoyándonos en **4 pilares**:

---

### Pilar 1: Ejecución Intra-Vela en el Borde del Rango (`STOP` + `LIMIT`) y Comisiones

#### Problema en Fase 1
En `BtcMomentumCore4h`, la estrategia esperaba a que la vela de 4h cerrara por encima del canal Donchian (`close > donchian_high`) y enviaba una orden a precio de cierre (`self.buy = qty, self.price`). Si la vela rompía con fuerza, la entrada se ejecutaba muy lejos del nivel de ruptura.

#### Solución en Fase 2: Órdenes Pre-Colocadas en el Borde del Rango
* En Jesse ([`jesse/strategies/Strategy.py`](../../jesse/strategies/Strategy.py#L674-L685)), el método `_submit_buy_orders()` y `_submit_sell_orders()` selecciona automáticamente el tipo de orden según la relación entre el precio de la orden (`o[1]`) y el precio actual (`self.price`):
  * **Ruptura Intra-Vela (`STOP` Order):** Si en `update_position()` / `go_long()` la tendencia macro y la compresión previa están habilitadas mientras el precio está **dentro** del rango (`self.price < breakout_level`), colocar `self.buy = qty, breakout_level` hace que Jesse envíe `self.broker.start_profit_at(sides.BUY, qty, breakout_level)`.
    * **Efecto:** El simulador de Jesse ejecuta la entrada **intra-vela (al minuto exacto)** en que el precio cruza `breakout_level`, entrando en el borde exacto del rango sin esperar al cierre de la vela de 4h. Si es una falsa ruptura, estamos pegados al rango con un Stop Loss mucho más corto; si es verdadera, capturamos todo el cuerpo de la vela expansiva.
  * **Entrada en Retroceso / Re-testeo (`LIMIT` Maker Order):** Si el precio ya rompió y queremos entrar en un *pullback* hacia el borde del rango roto (`limit_price < self.price` para Long), colocar `self.buy = qty, limit_price` envía `self.broker.buy_at(qty, limit_price)` (orden `LIMIT` pasiva).

#### Cuadro Oficial de Comisiones Binance USDⓈ-M Futures (VIP 0 + BNB) y Regla de Simulación
* **Tarifa real en Binance USDⓈ-M Futures (`VIP 0` con 10% de descuento usando BNB en la billetera de Futuros):**
  * **Maker (`LIMIT` pasiva):** **`0.018%`** (`0.00018`) — *(Sin BNB: `0.020%`)*
  * **Taker (`MARKET` o `STOP` de ruptura intra-vela):** **`0.045%`** (`0.00045`) — *(Sin BNB: `0.050%`)*
* **REGLA OBLIGATORIA DE BACKTEST Y MONTE CARLO:**
  * Configurar siempre el fee de backtest y Monte Carlo fijo en **`0.00045` (`0.045%`)**.
  * De esta forma, todas las simulaciones asumen el peor escenario (100% Taker). En live trading, la fracción de órdenes que se ejecute como `LIMIT` Maker (`0.018%`) rendirá un extra por encima del backtest.

---

### Pilar 2: Portafolio de Sectores Realmente Descorrelacionados (`BTC-USDT` + `PAXG-USDT` + `SPY-USDT`)

En lugar de forzar sobre-operativa en `BTC-USDT`, aplicaremos la lógica de rupturas estructurales sobre **3 clases de activos macroeconómicamente independientes** disponibles en `Binance Perpetual Futures`:
1. **Cripto / Riesgo Digital:** `BTC-USDT` (opera 24/7)
2. **Oro / Refugio Inflacionario y Geopolítico:** `PAXG-USDT` (opera 24/7)
3. **Renta Variable EE. UU. (10% S&P 500):** `SPY-USDT` (opera horario de mercado/extendido)

#### Desafío de Datos Históricos y Solución Gratuita Verificada (`2020–2025`)

Se verificó directamente contra la API de Binance la fecha de inicio de cada contrato:
* `Binance Perpetual Futures` $\rightarrow$ `PAXGUSDT` inicia recién el **`2025-03-27`** y `SPYUSDT` inicia el **`2026-04-06`**.
* El proveedor `Massive` (`api.massive.com`, ex Polygon.io) integrado en Jesse **NO sirve en su plan gratuito para llegar a 2020**, ya que su tier gratuito limita el histórico a una ventana móvil de **2 años** y `5 requests/minuto` ([`jesse/services/historical_data/massive_stocks.py`](../../jesse/services/historical_data/massive_stocks.py#L60-L61)).

Por lo tanto, el agente debe construir el conjunto de datos `2020-01-01` a `2025-12-31` usando **fuentes 100% gratuitas** y las herramientas nativas de Jesse (`clean_and_import_custom_candle_csv` y `copy_candles`):

1. **Ingesta de `PAXG-USDT` (Oro):**
   * **Hecho verificado:** En **`Binance Spot`**, el par **`PAXG-USDT` tiene velas de 1 minuto completas y continuas (24/7) desde el `2020-08-28`** hasta el presente.
   * **Paso A:** Usar `import_candles` en el MCP `jesse-local` con `exchange="Binance Spot"`, `symbol="PAXG-USDT"`, `start_date="2020-08-28"`.
   * **Paso B (Opcional para cubrir `2020-01-01` a `2020-08-27`):** Descargar las velas de 1m de `XAUUSD` desde **Dukascopy** (gratuito) para los primeros 8 meses de 2020, importarlas con `clean_and_import_custom_candle_csv` y unificarlas, o bien iniciar el backtest multi-activo en `2020-09-01` (más de 5 años completos de datos 100% nativos de Binance).
   * **Paso C:** Usar la herramienta MCP **`copy_candles`** (`exchange="Binance Spot"`, `symbol="PAXG-USDT"`, `target_exchange="Binance Perpetual Futures"`, `target_symbol="PAXG-USDT"`) para habilitar su simulación en futuros perpetuos.

2. **Ingesta de `SPY-USDT` (S&P 500):**
   * Descargar velas de 1 minuto desde `2020-01-01` hasta `2025-12-31` mediante un script en `bot/research/` usando una de estas dos fuentes gratuitas:
     * **Opción Preferida — Dukascopy Historical Feed (`USA500.IDX/USD` dividido por 10 o `SPY.US/USD`):** El feed histórico de Dukascopy es 100% gratuito sin API key desde 2010 (accesible vía Python / `dukascopy-python` o endpoints directos `.bi5`). Usar `USA500.IDX/USD` (dividiendo precios `OHLC` por `10` para empatar la escala de `SPY`) tiene la ventaja de cotizar **23h/5d** (acompañando a los futuros del S&P 500 durante la noche, mucho más parecido al contrato perpetuo `SPYUSDT` de Binance que las 6.5h del ETF de NYSE).
     * **Opción Alternativa — Alpaca Markets Free Data API (`SPY`):** Con una cuenta gratuita Paper de Alpaca (`data.alpaca.markets/v2/stocks/SPY/bars`), descargar `1Min` desde `2020-01-01` incluyendo *pre-market* y *after-hours*.
   * Guardar el CSV limpio en el proyecto e importarlo con la herramienta MCP **`clean_and_import_custom_candle_csv`** (`symbol="SPY-USDT"`, `invalid_row_policy="reject"`).
   * Ejecutar **`copy_candles`** desde `"Custom Data"` (`symbol="SPY-USDT"`) hacia `target_exchange="Binance Perpetual Futures"`, `target_symbol="SPY-USDT"`.
   * *Nota sobre el motor de Jesse:* El simulador por timestamps de Jesse ([`_timestamp_simulator` en `jesse/modes/backtest_mode.py`](../../jesse/modes/backtest_mode.py#L910-L925)) ya soporta nativamente mezclar activos continuos 24/7 (`BTC-USDT`, `PAXG-USDT`) con activos que cierran los fines de semana (`SPY-USDT`).

---

### Pilar 3: Nuevos Componentes de Ingeniería Multi-Activo

Al operar conjuntamente `BTC-USDT` (volatilidad anualizada `~55%`), `PAXG-USDT` (volatilidad `~15%`) y `SPY-USDT` (volatilidad `~15%`), la estrategia debe incorporar dos módulos técnicos clave:

1. **Normalizador de Volatilidad entre Sectores y Presupuesto de Margen Compartido (*Cross-Asset Volatility Parity*):**
   * `PAXG` y `SPY` tienen un `ATR%` diario ~3.5 a 4 veces menor que `BTC`.
   * Todos los umbrales de ruptura, compresión y expansión deben estar expresados en **unidades de `ATR` o desviaciones estándar propias de cada activo** (nunca porcentajes fijos de precio).
   * **Control de Margen y Apalancamiento por Activo:** Como `PAXG` y `SPY` tienen Stop Losses porcentualmente muy cortos (ej. `0.7%` de distancia), una fórmula de riesgo del `2%` sin tope adecuado pediría apalancamientos altos. El dimensionador de posición (`qty`) debe respetar:
     * El tope de apalancamiento aislado por ruta (`5x` máximo del capital asignado o margen disponible en la cuenta compartida).
     * Un presupuesto de margen libre (`self.available_margin`) para que si `BTC`, `PAXG` y `SPY` coinciden en señal simultáneamente, ninguna orden sea rechazada por falta de margen.

2. **Fuerza Relativa y Flujo Inter-Mercado (*Cross-Asset Relative Strength / Risk-On vs Risk-Off*):**
   * En Jesse, cualquier ruta puede consultar las velas de los otros activos mediante `self.get_candles(self.exchange, 'PAXG-USDT', '4h')`, `self.get_candles(self.exchange, 'BTC-USDT', '4h')` y `self.get_candles(self.exchange, 'SPY-USDT', '4h')`.
   * Evaluar un filtro/priorizador simple y objetivo basado en precio:
     * Comparar el momentum normalizado por volatilidad (`ROC / ATR%`) entre Riesgo (`BTC`, `SPY`) y Refugio (`PAXG`).
     * Cuando hay múltiples señales o para filtrar falsas rupturas, dar prioridad al activo con mayor Fuerza Relativa (o bloquear compras agresivas en riesgo cuando el capital global huye violentamente hacia `PAXG` mientras `SPY` y `BTC` marcan mínimos).

---

### Pilar 4: El "Auditor de Consistencia Mensual" (`bot/research/monthly_auditor.py`)

El criterio de éxito de la Fase 2 **no es solo el CAGR total**, sino la **regularidad mensual del portafolio combinado**.

El agente debe crear un script evaluador en `bot/research/monthly_auditor.py` (ejecutable vía terminal o `run_research_script` del MCP) que lea los trades y la curva de equity de cada sesión de backtest y calcule:
1. **Porcentaje de Meses Rentables (% Winning Months):** Meta $\ge 65\% - 70\%$ de los meses activos en positivo.
2. **Porcentaje de Trimestres Rentables (% Winning Quarters):** Meta $\ge 80\%$.
3. **Peor Mes y Peor Trimestre Histórico:** Controlar que ningún mes aislado destruya la cuenta.
4. **Frecuencia de Operaciones Anual y Mensual:** Verificar que el portafolio combinado supere ampliamente los ~7.5 trades/año de la Fase 1 (apuntando a un flujo activo pero sin caer en overtrading que erosione comisiones).
5. **Matriz de Correlación de Retornos entre `BTC-USDT`, `PAXG-USDT` y `SPY-USDT`:** Confirmar empíricamente que los retornos mensuales de las tres rutas estén descorrelacionados ($\text{corr} < 0.25$).
6. **Concentración de Ganancias (Outlier Dependency Check):** Verificar cuánto cae el CAGR si se eliminan los 2 mejores trades de los 6 años (el sistema no debe depender de un único trade suertudo).

---

## 5. Hoja de Ruta Paso a Paso para el Próximo Agente

Cuando el usuario inicie la nueva sesión y pida ejecutar este plan, seguir estrictamente este orden:

### Paso 1: Verificación del Entorno y Pipeline de Datos (`2020–2025`)
1. Verificar conexión al MCP `jesse-local` (`get_existing_candles`). Confirmar que `BTC-USDT` (`2020-01-01` a `2025-12-31`) ya está en `Binance Perpetual Futures`.
2. Importar `PAXG-USDT` desde `Binance Spot` (`2020-08-28` a `2025-12-31`) y usar `copy_candles` hacia `Binance Perpetual Futures` (`PAXG-USDT`). *(Si se decide completar `2020-01-01` a `2020-08-27`, descargar `XAUUSD` 1m de Dukascopy e integrarlo antes de copiar).*
3. Crear y ejecutar el script descargador gratuito para `SPY-USDT` (`2020-01-01` a `2025-12-31` desde Dukascopy `USA500.IDX/USD` `/10` o Alpaca `SPY` 1m), validar e importar con `clean_and_import_custom_candle_csv` y copiar con `copy_candles` a `Binance Perpetual Futures / SPY-USDT`.
4. Confirmar con `get_existing_candles` que los 3 pares (`BTC-USDT`, `PAXG-USDT`, `SPY-USDT`) están disponibles bajo `Binance Perpetual Futures` hasta `2025-12-31` (dejando `2026` sin usar).

### Paso 2: Construcción del Auditor de Consistencia Mensual
1. Implementar `bot/research/monthly_auditor.py` para auditar cualquier sesión de backtest de Jesse (extrayendo métricas mensuales, trimestrales, meses sin operar, correlación entre rutas y dependencia de outliers).
2. Correr el auditor sobre la sesión ganadora de Fase 1 (`721de7bb-98a9-4827-9946-f74ab4f2b86f` de `BtcMomentumCore4h`) para establecer la línea base exacta de meses positivos y meses vacíos que queremos superar.

### Paso 3: Evolución a Ejecución Intra-Vela (`STOP` en Borde de Rango + `LIMIT` en Pullback)
1. Crear una nueva estrategia (no sobrescribir `BtcMomentumCore4h`, mantenerla intacta como referencia de Fase 1), por ejemplo **`MultiAssetBreakout4h`** (o probar primero el motor intra-vela sobre `BTC-USDT` y `PAXG-USDT`).
2. Reemplazar la entrada tardía al cierre de la vela (`self.buy = qty, self.price`) por órdenes `STOP` pre-colocadas en el borde exacto del canal Donchian / rango (`self.buy = qty, upper_band` cuando `upper_band > self.price`) y evaluar la combinación con órdenes `LIMIT` en retrocesos superficiales.
3. Mantener fijo `fee = 0.00045` (`0.045%`) en todas las pruebas.

### Paso 4: Integración Multi-Activo, Paridad de Volatilidad y Fuerza Relativa
1. Ejecutar el backtest multi-ruta simultáneo en Jesse con `routes`:
   * `Binance Perpetual Futures` / `BTC-USDT` / `4h`
   * `Binance Perpetual Futures` / `PAXG-USDT` / `4h`
   * `Binance Perpetual Futures` / `SPY-USDT` / `4h`
2. Ajustar el módulo de **Paridad de Volatilidad y Presupuesto de Margen Compartido** para que los 3 activos aporten riesgo equilibrado sin exceder el margen de la cuenta en `5x` Isolated.
3. Probar el filtro/priorizador de **Fuerza Relativa Inter-Mercado** (`Risk-On` vs `Risk-Off`) y medir su impacto real con el Auditor Mensual (mantenerlo solo si mejora objetivamente el % de meses rentables y el Calmar/Drawdown fuera de muestra).

### Paso 5: Validación Walk-Forward, Monte Carlo y Reporte Final
1. Validar que el sistema funcione tanto en `2020–2023` (In-Sample) como en `2024–2025` (Out-of-Sample Walk-Forward).
2. Ejecutar Monte Carlo (`Candles` + `Trades`, $\ge 200$ escenarios) con `fee = 0.045%`.
3. Guardar el reporte comparativo (Fase 1 Mono-Activo vs Fase 2 Multi-Activo Intra-Vela) con el desglose mes a mes del Auditor.
