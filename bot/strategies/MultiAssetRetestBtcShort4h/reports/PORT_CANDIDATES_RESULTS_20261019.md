# Cartera compartida de candidatas — resultados finales — 19/10/2026

La incorporación de PAXG MARKET y las candidatas SPY mejora el resultado histórico de una cuenta compartida. C presenta mayor neto y regularidad; B tiene menor exposición, menor drawdown y mayor Sharpe que C. No se declara objetivo global alcanzado: C supera los umbrales mensuales/trimestrales en periodos completos, pero al incluir las fronteras parciales queda por debajo del65% de meses activos positivos. El CAGR de todas sigue debajo de la aspiración20–30% anual.

Completadas cuatro variantes económicas congeladas y cuatro réplicas exclusivamente diagnósticas. Ocho fulls terminados, sin nuevos parámetros tras resultados ni ejecuciones pendientes. Las réplicas no cuentan como nuevas hipótesis ni validaciones independientes.

## Condiciones comparables

Cada cartera parte de10.000USDT COMPARTIDOS entre BTC/PAXG/SPY. Riesgo presupuestado1% por trade,8% agregado, isolated5x, techo nocional4.4x, sin piramidado. Comisión0.00045 por lado para todos los tipos. Reserva0.001 sólo sizing, no slippage aplicado. Misma asignación ex ante inversa a ATR relativo y ledger común incluyendo órdenes pendientes. Orden fijo de rutas BTC/PAXG/SPY.

BTC conserva exactamente señales y gestión original, incluido long retest y short continuación/target1.5ATR/72h. La copia normaliza TRADE_RISK3%→1%, coherente con estudios recientes. PAXG/SPY control son referencias Cq con quote guard fresco. Por eso CONTROL no replica ni se compara directamente con la referencia histórica de3%/28.83%CAGR. Las cuatro nuevas sí son comparables entre ellas a1%.

SPY conserva UTC Mon–Fri00–20 para historia y barras abiertas00–16 para entradas. BTC/PAXG sin calendario. Gestiones siempre activas. SPY/PAXG quote M1 exacta heredada; no cambio de datos/proxies. Rutas4h más tres auxiliaresM1, warmup240, motor normal fast/debugfalse en primarias. Ventana2020-10-15→2025-12-31 exclusiva: último día30/12.2026 reservado. Sin funding, instalaciones, framework/configglobal, reinicios, live/paper/Pi o research_scripts.

## Cuatro carteras completas

| Cartera | Composición PAXG/SPY | N | Neto USDT | CAGR% | DD motor% | PF | Sharpe | Meses+ completos/activos | Q+ completos |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| [CONTROL](http://localhost:9200/#/backtest/5cead429-3356-437b-b03d-9e861f10974e) | Retest/Retest | 222 | 7815.59 | 11.71 | -8.54 | 1.59 | 1.133 | 33/59 (55.93%) | 13/19 (68.42%) |
| [A](http://localhost:9200/#/backtest/5fb1aa55-6ed3-4ac4-bb84-08e82dad3d49) | MARKET/Retest | 225 | 8527.17 | 12.56 | -7.43 | 1.65 | 1.206 | 35/59 (59.32%) | 14/19 (73.68%) |
| [B](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f) | MARKET/MECH01 | 206 | 9234.19 | 13.37 | -7.50 | 1.80 | 1.324 | 37/57 (64.91%) | 16/19 (84.21%) |
| [C](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835) | MARKET/MECH05 | 213 | 9407.83 | 13.56 | -8.17 | 1.78 | 1.315 | 38/57 (66.67%) | 16/19 (84.21%) |

CONTROL usa PAXG/SPY Cq. A sustituye sólo PAXG por MARKET central. B/C mantienen PAXG MARKET y sustituyen SPY por MECH01 (sólo segunda oportunidad con retest) o MECH05 (oportunidades posteriores con MARKET). BTC igual en las cuatro en reglas. PF desde trades conciliado; métricas CAGR/DD/Sharpe de motor. Neto acumulado, no anual.

## Regularidad: conservar todos los denominadores

| Cartera | Positivos/todos los meses completos | Positivos/activos completos | Positivos/activos con parciales | Q+ completos | Q+ con parciales |
|---|---|---|---|---|---|
| CONTROL |33/61=54.10%|33/59=55.93%|33/61=54.10%|13/19=68.42%|14/21=66.67%|
| A |35/61=57.38%|35/59=59.32%|35/61=57.38%|14/19=73.68%|15/21=71.43%|
| B |37/61=60.66%|37/57=64.9123%|37/59=62.71%|16/19=84.21%|17/21=80.95%|
| C |38/61=62.30%|38/57=66.67%|38/59=64.41%|16/19=84.21%|17/21=80.95%|

Hay61meses y19Q completos. Con fronteras son63meses y21Q; los dos meses parciales están activos pero negativos en esta tanda. Por eso cambia el porcentaje de activos, sin cambiar el número de positivos. No escoger el denominador favorable ni redondear B64.9123 a65 para aceptarla.

C cumple>=65% meses activos y>=80%Q en periodos completos. Incluyendo parciales cumpleQ pero no meses. B cumpleQ pero no el umbral mensual ni siquiera en completos. Las cuatro cumplen DD no peor que−25%; ninguna cumple la aspiración anual20–30% a este riesgo. El conjunto del objetivo sigue pendiente; no se rebajan criterios ni se eleva riesgo para alcanzarlos.

## Aportes incrementales

A−CONTROL añade711.58USDT netos: PAXG+718.60, BTC+5.47 ySPY−12.49. Hay mejora histórica de PAXG en cuenta compartida y menor DD, aunque su dependencia temporal sigue: no demuestra superioridad universal de MARKET.

B−A añade707.03USDT: SPY+654.96, BTC+39.65 yPAXG+12.41. Fees bajan218.35. C−A añade880.66USDT: SPY+826.46, PAXG+63.89 yBTC−9.70. Son contribuciones de trades cerrados, no MTM por calendario. Cambiar una pata cambia saldo/tamaño y ocupación; no atribuir exclusivamente todo el incremento al mecanismo de esa pata sobre trades fijos.

C−B aporta173.63USDT adicionales en más de cinco años, pero paga91.85 más de fees y empeora DDmotor0.67puntos. Con10bpsRT extra la ventaja se reduce a71.58USDT. Elegir C sólo por máximo neto ignoraría este intercambio. C mejora un mes completo positivo frenteB; B conserva menor exposición, mejor Sharpe y menor drawdown observado.

| Cartera | BTC long neto | BTC short neto | PAXG neto | SPY neto |
|---|---:|---:|---:|---:|
| CONTROL | 4650.84 | 1223.61 | 938.76 | 1002.37 |
| A | 4652.94 | 1226.98 | 1657.37 | 989.88 |
| B | 4663.02 | 1256.56 | 1669.78 | 1644.84 |
| C | 4618.73 | 1251.49 | 1721.26 | 1816.34 |

Los BTC de todas tienen31long y125short con mismos timestamps/dirección. Precios coinciden dentro de precisión de coma flotante (diferencia máxima2.91e-11USDT); cantidades yPNL cambian por capital, sizing y reservas. No se modificó la lógicaBTC ni se sumaron curvas individuales.

## Fricción, concentración y exposición

| Cartera | Fees | Neto+10bpsRT | Sin3mejores | Sin3mejores+10bpsRT | Tiempo con alguna posición% | Nocional-tiempo/10k |
|---|---:|---:|---:|---:|---:|---:|
| CONTROL | 1549.64 | 6093.77 | 3899.67 | 2209.57 | 38.79 | 0.4240 |
| A | 1580.27 | 6771.31 | 4607.50 | 2883.49 | 39.88 | 0.4444 |
| B | 1361.92 | 7720.95 | 5275.69 | 3794.72 | 34.49 | 0.3620 |
| C | 1453.77 | 7792.53 | 5442.76 | 3859.92 | 36.96 | 0.4118 |

Son sensibilidades estáticas de mismos fills: no redimensionan capital ni generan nuevas oportunidades después de quitar trades o añadir costes. La cartera conserva beneficio con10bpsRT y al retirar sus tres mejores trades, también conjuntamente; no demuestra robustez independiente tras múltiples búsquedas históricas. Neto por pata comparte grandes episodios y riesgo común.

B reduce el tiempo con posiciones de38.79%control a34.49%; C a36.96%. El nocional-tiempo usa cantidad y precio de entrada sobre capital inicial y toda la ventana, no exposición marcada continua ni apalancamiento constante. Ninguna cifra equivale a máximo intradiario.

## Diversificación observada y pérdidas coincidentes

Correlaciones de contribuciones mensuales sobre61meses completos:
- Control: BTC/PAXG−.004, BTC/SPY−.054 yPAXG/SPY−.084.
- B:−.093,−.065 y−.047.
- C:−.093,−.111 y−.014.

Incluyen meses sin exposición/cero; no son correlaciones de precios ni garantía de cobertura futura. Se miraron también co-pérdidas: BTC/SPY ambos negativos pasan de6meses en control a0enB y2enC; PAXG/SPY de3a0/2. Las muestras donde ambas patas participan son menores paraB. No convertir cero co-pérdidas observadas en inmunidad.

Peores meses completos: control agosto2021−4.7019%, B agosto2021−4.3935%, C abril2021−4.6955%. EnC abril pierden las cuatro patas; correlación global baja no evita pérdidas conjuntas. Peor trimestreB−2.9682%, C−3.8299%. DD diarioUTC: control−8.5342%, A−7.4169%, B−7.4868%, C−8.2277%. No mezclar con muestreo DD del motor de la tabla principal.

Los retornos MTM anuales2021–2025 son positivos en las cuatro carteras. Esto no satisface por sí mismo la meta mensual;2020 y2025 tienen fronteras parciales. El detalle anual y las diez peores mensualidades con contribución por activo están íntegros en EXACT_AUDIT.

## Capacidad y operaciones omitidas

Se añadieron contadores pasivos, iguales en las seis copias. La simulación normal no persistió logs; se hicieron cuatro réplicas debugtrue para capturar doce JSON de terminate. Todos los trades económicos/cantidades/fees/PNL/fills son byte-exactos contra primarias. CurvasB/C exactas; CONTROL/A equivalentes numéricamente con máximo3.64e-12USDT de diferencia en16/9puntos, mismos1904timestamps. No presentarlas como cuatro curvas byte-exactas.

No se observaron planes que llegaran a sizing rechazados por capacidad nula o por redondeo de lote; tampoco recortes por margen o por presupuesto agregado8%. Sí18–19recortes de tamaño BTCshort por el mínimo de nocional global/cuota de volatilidad. No se pueden separar esos dos sublímites con este contador. PAXG ySPY no sufrieron esos recortes observados.

Los contadores cubren sólo planes calificados que alcanzan sizing estando flat y sin pending. No capturan señales mientras ocupado ni prueban qué habría llenado un plan omitido. Intentos STOP/LIMIT pueden cancelar sin llenar; no atribuir diferencia intentos−trades a falta de margen. La comparación real de cartera ya incorpora ocupación y tamaños.

## Decisión y siguiente foco

Se conservan dos carteras congeladas de investigación:
- C como candidata por regularidad y neto histórico.
- B como alternativa de eficiencia/exposición/drawdown.

Ninguna se promueve ni se abre2026. Los hallazgos aislados sobreviven la prueba de capital compartido, pero el objetivo global de regularidad sigue pendiente y el CAGR está por debajo de la aspiración. No declarar el sistema resuelto ni abrir otro barrido sobreSPY/PAXG.

Ahora el foco útil vuelve a BTC con un problema concreto: selectividad y costes de shorts, evaluados dentro de estas carteras, preservando los runners long. EnC BTCshort tiene125trades, net1251.49 yfees661.42; con10bpsRT extra conserva516.58. Es rentable globalmente y aportó en2022, por lo que no corresponde eliminarlo a ciegas.

El diagnóstico MTM por dirección muestra agosto2021: B−4.3935%, BTCshort−2.6912puntos yBTClong−1.7023. En abril2021 C−4.6955% incluyeBTCshort−1.9877puntos yBTClong−.9515. Otros meses malos vienen de longs/PAXG; mejorar sólo shorts no garantiza resolver regularidad. Los años no deben convertirse en filtros retrospectivos. Antes de nuevas ejecucionesBTC, definir hipótesis económica y contraste congelado contra B/C; esta tarea no los ejecutó.

## Verificación y limitaciones

Fuentes originales intactas. Seis copias verificadas por normalización exacta a sus bases, salvo BTC3%→1% y diagnóstico pasivo. _ledger/_committed/_capital/_volatility_share comunes. Códigos/rutas/config por sesión revisados, hiperparámetros registrados coinciden con defaults comunes; la sección del motor reporta un conjunto por sesión, no un registro separado por cada ruta. QA48assertions del AST real pasó. Primer fixture falló por omitirfee_rate y se corrigió sólo el fixture.

Auditoría principal9ed855c0d58f4062bfdcfbcb2ec3c4bb succeeded: fills/cantidades/fees/PNL/wallet yMTM de cuatro carteras concilian. EnC el contador preterminación1se reconcilia con cierre forzado de frontera; no hay posición residual sin explicar ni prueba de liquidez nativa. No se eliminó ese trade de resultados.

Captura/equivalencia860e4312396e4a6f9fa5b409066d49d8 yseguimientoa37ac71dbee84379ac8046cb17f906cc succeeded. La prueba estricta detectó diferencias de redondeo de curvas/precios; se cuantificaron y preservaron, sin modificar estrategia ni repetir otra vez. Diagnóstico de direccionesb4323faaedf541daba5bebe8ea6f1ad3 succeeded sobre mismos fills y capital, no backtest de patas aisladas.

Missing Data visual: portfolio_equity_drawdown.png fue generado, pero get_analysis_artifact devolvió artifact_changed dos veces. No se inspeccionó ni se usaron conclusiones visuales; no hubo fallback de archivos. Los JSON/CSV numéricos sí se recuperaron y conciliaron. No impide las conclusiones numéricas.

Toda la historia2020–2025 es desarrollo reutilizado. No OOS limpio, independencia entre variantes o validación de futuros nativos. Las restricciones de fuentes/proxies y ejecución siguen vigentes según protocolo, sin abrir nueva discusión de funding.

## Informes persistidos

Todos dentro del proyecto Jesse en la máquina que lo ejecuta, bajo strategies/MultiAssetRetestBtcShort4h/reports/:
- PORT_CANDIDATES_FROZEN_PROTOCOL_20261019.md
- PORT_CANDIDATES_IMPLEMENTATION_REVIEW_20261019.md
- PORT_CANDIDATES_STATE_QA_20261019.md
- PORT_CANDIDATES_SESSION_REGISTRY_20261019.md
- PORT_CANDIDATES_ANALYSIS_SOURCE_20261019.md
- PORT_CANDIDATES_EXACT_AUDIT_20261019.md
- PORT_CANDIDATES_PRIMARY_RESULTS_20261019.md
- PORT_CANDIDATES_CAPACITY_DIAGNOSTIC_PROTOCOL_20261019.md
- PORT_CANDIDATES_CAPACITY_DIAGNOSTIC_REGISTRY_20261019.md
- PORT_CANDIDATES_DIAGNOSTIC_EQUIVALENCE_SOURCE_20261019.md
- PORT_CANDIDATES_CAPACITY_RESULTS_20261019.md
- PORT_CANDIDATES_BTC_SIDE_DIAGNOSTIC_20261019.md

## Ocho sesiones

[CONTROL](http://localhost:9200/#/backtest/5cead429-3356-437b-b03d-9e861f10974e)

Dashboard: http://localhost:9200/#/backtest/5cead429-3356-437b-b03d-9e861f10974e

[A](http://localhost:9200/#/backtest/5fb1aa55-6ed3-4ac4-bb84-08e82dad3d49)

Dashboard: http://localhost:9200/#/backtest/5fb1aa55-6ed3-4ac4-bb84-08e82dad3d49

[B](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f)

Dashboard: http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f

[C](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835)

Dashboard: http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835

[DIAG_CONTROL](http://localhost:9200/#/backtest/c78f7c96-d16f-4e8e-a29c-7192bd93d1ec)

Dashboard: http://localhost:9200/#/backtest/c78f7c96-d16f-4e8e-a29c-7192bd93d1ec

[DIAG_A](http://localhost:9200/#/backtest/57adc5f5-59ad-4780-9011-0cb8a154235d)

Dashboard: http://localhost:9200/#/backtest/57adc5f5-59ad-4780-9011-0cb8a154235d

[DIAG_B](http://localhost:9200/#/backtest/4dfe4912-0565-43e6-a362-aaf045375a58)

Dashboard: http://localhost:9200/#/backtest/4dfe4912-0565-43e6-a362-aaf045375a58

[DIAG_C](http://localhost:9200/#/backtest/1c0f7bcb-f6b9-4deb-94ce-7046885c8a73)

Dashboard: http://localhost:9200/#/backtest/1c0f7bcb-f6b9-4deb-94ce-7046885c8a73

