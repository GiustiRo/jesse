# Inventario global de mecanismos y prevención de duplicados
Fecha: 18 de octubre de 2026. Inventario de solo lectura; no crea una estrategia, simulación ni autorización de nueva línea.
## Alcance y selección acumulada
El listado MCP disponible contiene67 carpetas de estrategia,66 archivos __init__.py y106 informes Markdown. Estos conteos NO son número de hipótesis independientes: existen clones de control, fuentes antiguas, auditorías, copias de informes y borradores sin corrida completa.
Las15 pruebas económicas completas citadas por el registro central pertenecen ÚNICAMENTE a esta orquestación. La selección global incluye mucha investigación previa, optimización, controles de parámetros/ejecución/costes y propuestas descartadas antes de simular. No describir15 como toda la búsqueda ni reiniciar el contador para obtener una muestra limpia.
2020–2025 es desarrollo ampliamente observado. 2026 permanece reservado; nada de este inventario lo abre.

## Fuentes revisadas
- MultiAssetBreakout4h/reports/PHASE2_PROGRESS_20261018.md.
- MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_RESEARCH_LEDGER_20261018.md.
- MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND4_RESULTS_20261018.md.
- MultiAssetRetestBtcShort4h/reports/PHASE2_SHORT_DIAGNOSIS_20261018.md.
- MultiAssetRetestBtcShort4h/reports/PHASE2_SHORT_EXPIRY_RESULTS_20261018.md.
- Inventario recursivo MCP de418 entradas, incluidos nombres de estrategias e informes.
- Fuentes puntuales ya leídas: BtcAdaptiveTrend2h, BtcRegimeBreakout1h, BtcMomentumCore4h, MultiAssetTrendBoth4h, MultiAssetSleeves4h, referencia y las variantes propias de esta orquestación; fuente/protocolo de rotación revisados en otra tarea.
No se leyeron67 fuentes completas. Los nombres sin fuente o informe leído se indican como existencia documental, no como prueba de resultados particulares.

## Mapa de familias
| Mecanismo | Implementaciones/documentos identificados | Estado y riesgo de duplicación |
|---|---|---|
| Ruptura tendencial intradía | TrendBreakout5m, TrendPullback5m, H1Pullback5m; posteriores BtcMomentumCore4h/BtcMomentumBaseline3 | Familia antigua. DOCS declara descartes de los primeros sistemas5m; H1Pullback existe pero aquí no se reauditan sus reglas ni resultados. No presentar un cambio de marco como edge independiente. |
| Alineación de medias / impulso multimarco | BtcRegimeBreakout1h, BtcAdaptiveTrend2h, TemaTrendFollowing | Fuentes leídas confirman TEMA1h/4h+EMA100+ADX/CMO y Keltner/SuperTrend/ER con filtro4h. TemaTrendFollowing existe; no se infiere su resultado por el nombre. Cambiar EMA/TEMA/SuperTrend ya ocupa un espacio de filtros intensamente explorado. |
| Compresión y expansión | SqueezeRelease5m, OrchShortQuietChannel1h | SqueezeRelease fue descartada; QuietChannel revisita compresión con volatilidad72h/720h y fue rechazada. No renombrar Bollinger/Keltner/quietness como un mecanismo nuevo. |
| Reversión de rango / fallo de ruptura | RangeFade5m, OrchLateralFailedRange4h | Rango y recuperación del borde ya explorados. El fallo de rango simétrico con ER bajo fue rechazado; una nueva forma de vela de rechazo puede ser un casi duplicado. |
| Rupturas multi-activo STOP | MultiAssetBreakout4h/Near4h/Session4h/TrendBoth4h/VolBudget4h | Variaciones de distancia al canal, filtro de sesión y presupuesto de exposición. Las corridas previas al arreglo de margen deben tratarse según controles corregidos; no comparar cifras viejas como nuevas mejoras. |
| Retest LIMIT de ruptura | MultiAssetRetest4h/SessionRetest4h/RetestBtcShort4h | Longs en los tres activos, con contexto y sizing compartidos. STOP→LIMIT ya fue contrastado. Fee sigue taker0.00045 aunque la entrada sea LIMIT. |
| Sensibilidad de ruptura y stop | RetestD20S16/D20S24/D32S16/D32S24 | Vecindario ya probado; no repetir20/32 y1.6/2.4 como hipótesis originales. Parte del coste en concentración de PAXG está documentado. |
| Shorts de tendencia y crisis | CrisisShort4h, RiskOffShort4h, MacroShort4h, TrendBoth4h | Hay documentos de resultados corregidos y limitación de warmup diario en MacroShort. Esa última interrupción es una limitación de datos, no evidencia de edge negativa. Macro bear/breakout no es un espacio virgen. |
| Shorts de rechazo y rally fade | Reject4h/RejectShort4h/RallyFade4h | Contratendencia/rechazo de rallies ya explorados; no volver a llamar nueva una vela bajista bajo EMA20 sin una diferencia causal material. |
| Continuación corta del selloff en régimen alcista | PullbackShort4h/BtcPullbackShort4h/RetestBtcShort4h | La referencia utiliza esta pata BTC, no una cobertura bajista demostrada. Selección de BTC fue posterior al análisis por componentes. |
| Elegibilidad, invalidación y régimen de shorts | OrchShortRewardRisk4h/ReclaimExit4h/DailyPullback4h | Premio/riesgo mínimo, recuperación del máximo de señal y régimen diario ya probados y rechazados. No basta añadir un filtro equivalente con otro nombre. |
| Sensibilidad RSI y objetivo short | BothR16T125/R16T175/R24T125/R24T175 | Esquinas ya corridas; una dejó shorts negativos. No recomenzar otra cuadrícula RSI/ATR fingiendo independencia. |
| Caducidad short | MultiAssetShortExpiry24h/48h | DUPLICADO CONFIRMADO: se probaron24 y48h frente72h, con entradas/longs/stops/targets/riesgo idénticos. Ninguna mejoró conjuntamente cartera. Ver sección específica siguiente. |
| Toma de beneficio y gestión long | OrchManageFixedR34h/FixedR54h/ScaleOutHalf2R4h | TP completo3R/5R y parcial50%a2R+runner ya corridos. 5R se acerca en puntos estimados, pero el vecino3R es débil y la mejora trimestral depende de bordes. Parcial reduce DD sin resolver regularidad. |
| Guardas mensuales de cartera | OrchManageMonthly2x1/4x2 | Las dos recetas de giveback mensual ya existen con protocolos/resultados. No barrer sus niveles como nueva familia. El mero traslado de PnL realizado no mejora retorno MTM. |
| Compra de dip / reversión rápida | MultiAssetSleeves4h, OrchManageFastMrBtc4h | SPY: RSI3/EMA120, LIMIT bajo dip, targetEMA20 congelado y5d. BTC posterior: MARKET, RSI2/EMA200 y salidaSMA5 dinámica/48h. La segunda pertenece a la misma premisa revisitada y perdió trasfees pese67.83% de acierto. |
| Gestión del capital y reloj | Blend/Relative/Equal, Phase2SharedBudget/SharedBtcContext, OrchAllocCommonClock/EqualRisk | InversoATR, mitad igualdad/volatilidad, igualdad, eliminación de techo nocional, riesgo8%/3 y volatilidad sobre cierres comunes ya explorados. Más exposición no es una ventaja nueva ni mejora de regularidad. |
| Atribución de componentes | Phase2BtcLongContext/BtcBothContext y controleslong de tres activos | Son pruebas de contribución con reglas comparables; no nuevos alpha. Cambiar rutas altera capital/reservas, por lo que sumar curvas aisladas no sustituye cartera. |
| Costes y reglas de decisión | Phase2FixedFeeRules4h, estrés previo y repetido | Se separaron mayoresfees de filtros/BE que dependían del fee. No duplicar controles ni afirmar que recargosfijos a fills son nuevos CAGR/DD. |
| Trend diario simplificado | OrchManageTurtleDaily |55dprevios/stop2ATR20/canal10d,BTC+PAXG,long/short,1%riesgo. Rechazado: ambos shorts negativos y regularidad claramente inferior. No variar55/10 después del fallo. |
| Rotación mensual relativa y absoluta | OrchRotateMonthlyMomentum4h |3meses calendario, ganador positivo o cash, cotizaciones16UTC comunes, entrada posterior y deudas de salida propias. Corrida completa rechazada, con startupcash incluido. No recortar inicio a febrero2021 para mejorar cociente. |
| Valor relativo entre criptos | OrchLateralRelativeShock1h | BTC/ETH, horizonte1h. Smoke técnico y un full detenido por datos NO equivalen a resultado económico. El full sigue condicionado a terminar cobertura; no duplicarlo ni afirmar cointegración por OLS de retornos. |
| Horarios/SPY y adaptación de datos | MultiAssetSession* y fuente HistData | Horario común/filtro de velas es adaptación de fuente, no alpha de sesión demostrado. Se conservan huecos; proxyBID y PAXGSpot no garantizan paridad del instrumento final. |
| Overnight SPY | Informe ORCH_OVERNIGHT_PRETEST_REJECTION_20261018.md | Retirado ANTES de simular por costes/fuente. No existe un PnL propio ni una estrategia overnight ejecutada. Tampoco volver a proponerlo ignorando9bpsRT. |

## Duplicado24h: evidencia concreta que debe consultarse antes de proponer otra corrida
Referencia72h: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
Control24h: http://localhost:9200/#/backtest/e474571a-bcad-47a9-b650-4ab14cc5029e
Control48h: http://localhost:9200/#/backtest/13c71d3e-17fe-44f2-8ce5-95f466ccda22

El informe leído PHASE2_SHORT_EXPIRY_RESULTS_20261018.md registra:
-72h:28.8294%CAGR/14.8905%DD,33/61 meses activos y15/21 trimestres.
-24h:26.2184%CAGR/16.2880%DD,34/61 meses activos y14/21 trimestres.
-48h:27.6810%CAGR/14.9067%DD,33/61 meses activos y14/21 trimestres.
Mismas97operaciones long; cambian los shorts y el capital de la cuenta. No hay una diferencia de señales que justifique repetir24h para “comprobarlo”. La propuesta repetida fue retirada sin lanzar.

## Ideas retiradas, interrupciones y errores no equivalen al mismo tipo de evidencia
Mantener separados: corrida económica completa; smoke técnico; run detenido por datos; propuesta descartada antes de simular; control contable; lectura opcional fallida. Los148tests del arreglo del framework son validación funcional, no148hipótesis de trading.
Las cifras antiguas de auditorV2 (muestreo00:01), margen previo y controles de orden del formulario fueron corregidas; no resucitarlas como resultados comparables. El motor conserva prioridad interna por exchange/símbolo: permutar formulario nunca acreditó otra prioridad.

## Qué NO encontré como mecanismo probado en las fuentes revisadas
No veo una segunda combinación de indicadores OHLC que pueda llamarse nueva con honestidad: el mapa ya cubre tendencia, rangos, compresión, reversión, horizontes, horarios, rotación y amplias variaciones de gestión.
Dos líneas serían de otra naturaleza, pero NO se proponen para ejecutar ahora:
1. Carry de financiación o basis, cubriendo el riesgo direccional con legs compatibles. Requiere financiación histórica real, base spot/perpetual, costes porleg, préstamos/capital y simulación del cashflow. Nada de eso puede inferirse de OHLC ni del PAXGSpotproxy; funding estuvo explícitamente excluido. No hay backtest de esta fuente de ingresos en el inventario.
2. Estrategia condicionada a eventos públicos programados, con calendario histórico conocido exante y timestamps de publicación verificados, en lugar de elegir horarios/meses a posteriori. No encontré esa clase de información en las fuentes revisadas. Requiere construir datos causales y evaluar costes/muestra; no se afirma que exista una ventaja, ni que una prima bruta sobreviva9bpsRT.
Estos son tipos de información/mecanismo distintos, no recomendaciones financieras ni promesas de cumplir la meta. Su ausencia aquí no prueba que nadie los haya investigado fuera de este proyecto. Cualquier implementación requeriría un diseño y soporte de datos nuevos.

## Limitación de lectura opcional y estado del servicio
read_strategy(BtcTrendMaster) devolvió HTTP500 “Internal Server Error”. Se detuvo esa lectura; no se abrió el archivo por filesystem ni por una vía alternativa. Root confirmó después que el MCP seguía respondiendo en consultas independientes y autorizó guardar este inventario con las fuentes ya disponibles.
BtcTrendMaster queda sin clasificar por fuente ni rendimiento. No es necesario reparar una estrategia antigua ajena para continuar la investigación. No se borró, ocultó ni modificó ningún material previo.

## Regla operativa propuesta para evitar repeticiones
Antes de cada diseño nuevo, buscar su mecanismo y “qué cambia” en este mapa y en el registro central. Si la modificación ya está ejecutada, enlazar su informe; si sólo cambia un umbral dentro de una familia rechazada, justificar una falsación material antes de escribir fuente. No reiniciar el contador de selección ni presentar desarrollo como OOS.
Objetivos originales, referencia, fees y2026 quedan intactos. Este inventario no edita informes canónicos de otros agentes.
