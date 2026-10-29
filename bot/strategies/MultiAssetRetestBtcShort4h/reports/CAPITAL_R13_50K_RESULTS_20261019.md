# R13 — Resultados con 50.000 USDT: K1001, riesgo 2%/6%, 3x
Fecha:2026-10-19. El usuario elige continuar con2%/6%a3x y pregunta por una cartera de50k. Se registra como perfil preferido de investigación; no se aplicó una modificación live/paper.

## Resultado principal
En cartera C, 50.000 USDT iniciales terminan en236.427,68 USDT, con186.427,68 USDT de beneficio neto de comisiones nominales modeladas, retorno acumulado372,86%, CAGR34,71% y DD diario−13,85%.
La cartera B termina en228.914,25 USDT, con178.914,25 de beneficio, CAGR33,88% y DD−13,36%.
Con fee mayor, cartera C termina en173.614,00 USDT, beneficio123.614,00, CAGR26,97% y DD−14,55%; B termina en170.674,59, CAGR26,55% y DD−14,60%.
Son resultados ejecutados con balance50000 en el motor, no una multiplicación asumida del resultado10k. Todos incluyen capitalización; no representan un pago anual constante ni una proyección futura.

## Contrato
Cuatro nuevas corridas, B/C × fee0.00045/0.00095 por lado, y cuatro anclas10k R12. Único cambio por sesión: exchange.balance10000→50000. Se verificó igualdad completa del form al restituir el balance a10000.
2020-10-15 inclusiva →2025-12-31 exclusiva. Cuenta compartida, BTC/PAXG/SPY4h y feeds1m, isolated3x, warmup240, fast_modefalse, debugtrue. B=SPY Second; C=SPY Market; rutas y orden idénticos. Fuentes perfil R12 leídas y verificadas con riesgo.02/agregado.06, sin edición.
Cap nominal4.4, cuotas inversas ATR, buffer de margen90% y reserva sizing.001 preservados. El porcentaje objetivo puede reducirse por límites de capacidad.
2026 continúa cerrado incluso inspección. El histórico es desarrollo reutilizado, no OOS.

## Resultados completos 50k
|Cartera / sesión|Coste|Saldo final|Beneficio neto|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[B_F95_50k](http://localhost:9200/#/backtest/6fef38ab-eecc-4932-9e62-695905f71c09)|0.00095|170674.59|120674.59|241.35|26.55|-14.60|1.819|1.443|1.785|242|39079.66|291|
|[B_N_50k](http://localhost:9200/#/backtest/5a3febae-535e-4a86-a22e-08a150c23ec5)|0.00045|228914.25|178914.25|357.83|33.88|-13.36|2.536|1.743|2.057|242|21941.94|278|
|[C_F95_50k](http://localhost:9200/#/backtest/3fbb3516-50f0-44f1-91db-1bb586a2a667)|0.00095|173614.00|123614.00|247.23|26.97|-14.55|1.853|1.444|1.775|249|41199.11|223|
|[C_N_50k](http://localhost:9200/#/backtest/263d4d0c-b44e-44d0-9776-5fbfd3bd9149)|0.00045|236427.68|186427.68|372.86|34.71|-13.85|2.506|1.756|2.056|249|23393.56|215|

## Escalado frente a 10k

|Caso|Neto50k|5 × neto10k|Diferencia USDT|Entradas nuevas / retiradas|Salidas cambiadas|
|---|---:|---:|---:|---:|---:|
|B_F95_50k|120674.59|120321.70|352.89|0 / 0|0|
|B_N_50k|178914.25|178635.35|278.89|0 / 0|0|
|C_F95_50k|123614.00|123260.02|353.98|0 / 0|0|
|C_N_50k|186427.68|185924.15|503.53|0 / 0|0|

La diferencia es pequeña frente al escalado total, pero no nula: redondeo de cantidades y capitalización producen diferencias en los tamaños. En C nominal el neto50k supera5×neto10k en503,53 USDT; no se atribuye a una mejora del edge por aumentar capital.

## Caídas en dinero y porcentaje
El drawdown porcentual se calcula desde el máximo previo de equity, no siempre sobre los50.000 iniciales. La caída máxima en dinero puede ocurrir en otro episodio distinto al máximo porcentual.

|Caso|Mayor caída USDT|Fecha de mayor caída USDT|Máximo DD %|Fecha del máximo DD %|Pico del episodio porcentual|Pérdida USDT en ese episodio|
|---|---:|---|---:|---|---:|---:|
|B_F95_50k|20179.70|2024-08-21T00:01:00+00:00|-14.60|2024-08-21T00:01:00+00:00|138231.59|20179.70|
|B_N_50k|20645.60|2024-08-21T00:01:00+00:00|-13.36|2024-08-21T00:01:00+00:00|154513.08|20645.60|
|C_F95_50k|20759.68|2024-08-23T00:01:00+00:00|-14.55|2024-08-23T00:01:00+00:00|142639.34|20759.68|
|C_N_50k|21362.47|2024-08-23T00:01:00+00:00|-13.85|2021-06-18T00:01:00+00:00|67459.04|9342.96|

C nominal: DD porcentual máximo13,85% sobre un pico de67.459,04 USDT en2021, pérdida9.342,96 USDT. La mayor caída absoluta es21.362,47 USDT en2024 con capital ya mayor. No equiparar ambas fechas ni calcular la pérdida histórica máxima como13,85%×50.000.
Resolución de equity diaria: no certifica la máxima caída intraminuto.

## Evolución anual desde equity
2020* comienza15octubre y2025* termina30diciembre (fecha final exclusiva31diciembre). Ambos extremos son parciales. Los importes reflejan capitalización y ganancias flotantes en la equity; no son cohortes de trades cerrados.

|Caso|Año|Equity inicio del período|Equity final|Ganancia USDT|Retorno %|
|---|---|---:|---:|---:|---:|
|B_F95_50k|2020*|50000.00|53175.11|3175.11|6.35|
|B_F95_50k|2021|53175.11|76567.07|23391.96|43.99|
|B_F95_50k|2022|76567.07|87967.09|11400.02|14.89|
|B_F95_50k|2023|87967.09|113823.75|25856.66|29.39|
|B_F95_50k|2024|113823.75|145258.52|31434.77|27.62|
|B_F95_50k|2025*|145258.52|170674.59|25416.07|17.50|
|B_N_50k|2020*|50000.00|53674.70|3674.70|7.35|
|B_N_50k|2021|53674.70|80246.11|26571.41|49.50|
|B_N_50k|2022|80246.11|94244.74|13998.64|17.44|
|B_N_50k|2023|94244.74|125226.57|30981.83|32.87|
|B_N_50k|2024|125226.57|167572.73|42346.16|33.82|
|B_N_50k|2025*|167572.73|228914.25|61341.52|36.61|
|C_F95_50k|2020*|50000.00|53091.16|3091.16|6.18|
|C_F95_50k|2021|53091.16|74266.90|21175.73|39.89|
|C_F95_50k|2022|74266.90|85694.83|11427.93|15.39|
|C_F95_50k|2023|85694.83|117690.32|31995.49|37.34|
|C_F95_50k|2024|117690.32|148627.69|30937.37|26.29|
|C_F95_50k|2025*|148627.69|173614.00|24986.31|16.81|
|C_N_50k|2020*|50000.00|53585.20|3585.20|7.17|
|C_N_50k|2021|53585.20|78099.34|24514.14|45.75|
|C_N_50k|2022|78099.34|92247.63|14148.29|18.12|
|C_N_50k|2023|92247.63|131079.58|38831.94|42.10|
|C_N_50k|2024|131079.58|173674.56|42594.99|32.50|
|C_N_50k|2025*|173674.56|236427.68|62753.12|36.13|

## Presupuesto inicial y efecto del crecimiento
Con50.000 USDT, riesgo objetivo2%=1.000 USDT por operación al stop; límite agregado6%=3.000 USDT al admitir nuevas entradas. No son montos de margen ni garantía de pérdida máxima ante gaps/slippage.
El stop técnico no cambia: cambia la cantidad. Se usa capital conservador max(0,min(wallet,equity)); cuotas, margen, notional y redondeo pueden limitarla. Si la cuenta crece a100.000 USDT, el objetivo2% sube a2.000 USDT; si cae a40.000, baja a800. Por eso las pérdidas absolutas posteriores pueden superar los importes iniciales.
3x es apalancamiento de margen y no multiplica de nuevo2% a6% por trade. Tres activos comparten la cuenta y el presupuesto agregado.

## Auditoría y límites
Cuatro ejecuciones terminadas, cambio único de balance verificado. Ocho snapshots completos analizados. Neto calculado de trades igual al del motor dentro0,01 USDT; balance inicial + neto = saldo final dentro0,01; brecha terminal equity/wallet cero.
Sin entradas nuevas/retiradas ni cambios de tiempo/precio de salida respecto de10k al mismo fee y cartera; sólo cantidades y su capitalización. No confundir esa paridad con nominal vsestrés: el cambio de fee sí puede alterar gestión y fills.
PF50knominal2,056–2,057 yestresado1,775–1,785; todas positivas yDDdiario mejor que−25%, puertas descriptivas del proyecto, no aprobación OOS.
B/C comparten muestra: no se consideran independientes. Reserva de sizing.001 no simula slippage. No se modelaron impacto de mercado, liquidez, funding, fiscalidad ni capacidad real de ejecutar esas órdenes; el backtest50k no certifica escalabilidad live. SPY mantiene proxy SPX CFD y calendario heredado.
Configuración global al final sigue balance10000, leverage5 yfee.00045; las corridas usan overrides por sesión. Sin cambios de código, live/paper ni2026.

## Archivos persistentes
- CAPITAL_R13_50K_PROTOCOL_20261019.md: protocolo previo y preferencia del usuario.
- CAPITAL_R13_50K_SESSION_REGISTRY_20261019.md: cuatro corridas, anclas, auditoría.
- CAPITAL_R13_50K_ANALYSIS_SOURCE_20261019.md: código reproducible.
- CAPITAL_R13_50K_DATA_20261019.md: métricas completas del motor, años y todos los meses.
El job temporal de análisis esc55af8bdd23d41f892a78409b5015db8; incluye gráficoequity_50k.png. Los datos anteriores permanecen guardados aunque el workspace temporal expire.
