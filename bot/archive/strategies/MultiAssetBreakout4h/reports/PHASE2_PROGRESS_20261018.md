# Fase 2 — estado consolidado

## Actualización vigente — traspaso final de las tres líneas frescas

Estado consolidado al18octubre2026local: tres agentes frescos COMPLETED, sin jobs pendientes propios. Leer primero strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_RESEARCH_HANDOFF_20261018.md. Este handoff sustituye los estados históricos pendientes/en ejecución/blocked como resumen actual, sin borrar la historia.

FreshStructureProbability: fullrun a3d3904dcb764db4b987fa0be7883d7d y auditoría ec58a9386a9f4151b3c1ac8764d28548 succeeded.11418forecasts;11411válidos/2ambiguos/5censurados;24controlesPASS. Pivots y combinado empeoran Brier/logloss globales, cada año y cohorte00UTC. ARCHIVAR recipe1D/4h+pivots/firsttouch24h/180d/shrink20, no retocar para rescate. Informe strategies/FreshStructureProbability/reports/INDEPENDENT_OBSERVER_NEGATIVE_RESULT_20261018.md. No tradingPnL ni2026.

FreshAuthorMethods: informe documental final strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md. Priorizar viabilidad de flujo real BTCperp propio; GEX opcional y estimado. Cobertura/asof/licencia/coste pendientes, sin descarga/compra. SPYCFDvol0/PAXGproxy no soportan inferencias microestructurales de otros instrumentos.

FreshPortfolioResearch: informe final strategies/FreshPortfolioResearch/reports/FRESH_PORTFOLIO_DIAGNOSIS_AND_DESIGN_20261018.md. Más participación deteriora eficienciaSPY/PAXG. IdeaSPYMR retirada antes de run por duplicación y evidencia previa negativa antes de comisiones. No nueva estrategia pendiente de ejecución.

Tanda por funciones10/01/11 cerrada y rechazada: primaria25.78%CAGR/DD−26.93%,38/63mesesactivospositivos60.32%/16/21q76.19%; referencia intacta28.83%CAGR/DD−14.89%,33/61activos/15/21q. Detalle PORTFOLIO_ROLES_RESULTS_20261018.md. Objetivo65–70%meses/80%q no conseguido, riesgo máximo3%/8%,fee.00045lado y2026reservado. No reiniciar conteo histórico ni tratar2020–25comoOOSlimpio. Próxima tarea: decisión de investigación fundada, no repetir modelos archivados ni esperar jobs ya terminados.


Actualizado el 18 de octubre de 2026. Estado: **investigación abierta; ninguna variante está aprobada**.

## Decisiones vigentes
- Referencia congelada: MultiAssetRetestBtcShort4h, longs en BTC/PAXG/SPY y shorts exclusivamente en BTC.
- Capital compartido de 10.000 USDT; 5x aislado; hasta 3% de riesgo por operación y 8% agregado planificado. Los gaps pueden superar la pérdida prevista.
- Comisión base de 0,045% por lado para todas las órdenes, incluidas LIMIT. No aplicar tarifa maker más barata.
- Objetivos mantenidos: 65–70% de meses activos positivos y 80% de trimestres positivos, junto con drawdown no peor que −25%.
- 2020–2025 es desarrollo ya observado. **2026 sigue reservado**, aunque haya velas de ese año almacenadas.
- No se inició live/paper, no se tocó la Pi ni se cambió la configuración global. No hay backtests o análisis activos al cerrar este informe.

## Infraestructura y fuentes
Se corrigieron bajo autorizaciones específicas la persistencia de equity y la liberación de reservas de margen tras un fill con gap. Se conserva el precio enviado para liberar la reserva y el precio real para posición/comisiones/PnL. Pasaron 148 pruebas; la auditoría histórica completa terminó sin reservas fantasma. No se hicieron nuevas modificaciones del framework en esta ronda.

BTC usa histórico de futuros. PAXG usa Spot como proxy. SPY usa SPX/USD CFD de HistData dividido por 10: 1.974.135 velas M1 BID, volumen cero, origen fixed EST convertido a UTC. Se conservan huecos; no se fabrican velas negociables. Indicadores SPY filtrados por horario común UTC, entradas en ventanas compatibles y salidas gestionadas cuando hay cotización.
Pendientes: feriados/early closes, paridad con instrumentos finales, spread/colas/impacto/fills LIMIT y financiación.

El auditor actual research_scripts/monthly_auditor_v4_orders.py reconstruye cierres UTC por fills, incluidas salidas parciales y comisiones. Requiere cierre completo demostrado y reconcilia saldo real; distingue el contador preterminación de posiciones realmente residuales. Sustituye v2 y amplía v3, con paridad verificada. Se ejecuta inline mediante run_analysis. Informa períodos completos además de conservar los bordes parciales; nunca se escoge el denominador favorable.

## Referencia y resultados anteriores
[Referencia congelada](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb):
97 longs y 123 shorts; CAGR 28,83%, drawdown del motor −14,89%, Sharpe 1,316; saldo 37.461,46 USDT.
33/61 meses activos positivos y 15/21 trimestres. Longs netos +22.174,44; shorts +5.287,02 USDT.

Una esquina del vecindario short RSI16/24 × objetivo1,25/1,75ATR pierde dinero en shorts. La selección de BTC para esa pata fue posterior a observar componentes de la muestra: no es OOS.
Las salidas temporales de shorts a 24/48h no mejoraron conjuntamente la referencia; se conserva 72h.
Los longs tienen winrate 44,33%, con ganancia media 1.031,99 y pérdida media 411,13 USDT. Los shorts: 55,28%, 293,58/266,85. No añadir un mínimo de 51% como sustituto de expectativa neta.
El mejor trade explica alrededor del 90% del neto individual de PAXG y del 94% del de SPY: concentración legítima posible en seguimiento tendencial, pero evidencia limitada por componente.

## Revisión independiente y atribución comparable
La revisión independiente leyó código, informes y snapshots sin modificar estrategias ni evaluar 2026. Priorizó atribución y realismo antes de nuevos filtros.

Se completó la comparación con las mismas reglas long, manteniendo tres rutas y sus pesos de contexto aunque un activo esté inactivo. No se redistribuye su capacidad en estos cuatro casos:

| Caso | CAGR | DD del motor | Meses activos positivos | Positivos sobre 63 meses | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| BTC long | 16,81% | −11,95% | 15/29 = 51,72% | 15/63 | 9/21 = 42,86% |
| BTC long + short | 21,71% | −13,01% | 34/56 = 60,71% | 34/63 | 14/21 = 66,67% |
| Tres activos long | 23,67% | −14,08% | 28/55 = 50,91% | 28/63 | 14/21 = 66,67% |
| Referencia combinada | 28,83% | −14,89% | 33/61 = 54,10% | 33/63 | 15/21 = 71,43% |

[BTC long](http://localhost:9200/#/backtest/bf52f5eb-f6fe-4491-a90e-e15d404b9de7),
[BTC ambos](http://localhost:9200/#/backtest/4623d369-05e7-4714-8f3b-5c10b1726663),
[tres activos long](http://localhost:9200/#/backtest/11c1a0a6-afe8-4718-80b9-a35e95adf40d).

Los shorts aportan beneficio y actividad, pero no rescatan uniformemente meses malos. Al añadir PAXG/SPY a BTC ambos se rescatan siete meses negativos y se convierten nueve positivos en negativos; también cambian meses planos. En los nueve perjudicados, la contribución de PAXG/SPY es negativa; en los siete rescatados es positiva. No se usan esas fechas para construir filtros retrospectivos.
El benchmark BTCMomentumBaseline3 utiliza otras reglas, por lo que no sirve para atribuir causalmente la diferencia a diversificar.

## Corrección del control de orden
**Pendiente: prioridad interna real.**
Permutar rutas en el formulario produjo resultados iguales, pero la inspección del motor confirmó que el replay de timestamps ordena internamente por exchange y símbolo. Por tanto, esos controles NO cambiaron la prioridad efectiva.
Se corrigió el informe anterior: la igualdad confirma invariancia frente al orden del formulario, no independencia de la prioridad de ejecución.
No se modificó el framework. Una opción nueva para alterar esa prioridad requeriría autorización específica; no se solicita ahora para certificar variantes que todavía incumplen regularidad.

## Costes con reglas de decisión fijas
Los controles anteriores de fee también cambiaban un filtro de elegibilidad short y el precio de breakeven long. Siguen siendo escenarios completos válidos, pero mezclan dos efectos.
Phase2FixedFeeRules4h congela ambos umbrales en la comisión base y deja variar costes efectivos, tamaños y capital. Su prueba base reproduce los 220 trades y resultados de la referencia dentro de tolerancia numérica.

| Coste adicional por operación completa | CAGR | DD del motor | Shorts netos | Meses activos positivos |
|---|---:|---:|---:|---:|
| Base | 28,83% | −14,89% | +5.287,02 USDT | 54,10% |
| +0,10% | 23,75% | −16,52% | +3.177,87 USDT | 50,82% |
| +0,25% | 16,54% | −18,98% | +723,65 USDT | 45,90% |

[Base equivalente](http://localhost:9200/#/backtest/f1208d5e-52a6-4aec-a3cb-4c7ff78bafc2),
[+0,10%](http://localhost:9200/#/backtest/66e5d910-56b8-47a2-99ab-bdfd74915a20),
[+0,25%](http://localhost:9200/#/backtest/d11139b0-194c-4457-9bfb-613d60f622f8).
No es un modelo de spread/slippage ni repite cantidades fijas. Los shorts conservan beneficio, con poco colchón en el escenario severo.

## Utilización del capital: prueba separada
Se retiró únicamente el techo nocional por activo, conservando 3%/8% de riesgo planificado, límite global de 4,4x y 5x aislado. La referencia sigue intacta.

| Caso | CAGR | DD del motor | Meses activos positivos | Trimestres positivos |
|---|---:|---:|---:|---:|
| BTC ambos, reserva individual | 21,71% | −13,01% | 60,71% | 66,67% |
| BTC ambos, capacidad compartida | 26,48% | −20,46% | 62,50% | 66,67% |
| Tres activos, referencia | 28,83% | −14,89% | 54,10% | 71,43% |
| Tres activos, capacidad compartida | 37,43% | −18,42% | 55,74% | 71,43% |

[BTC compartido](http://localhost:9200/#/backtest/bc516f87-1ebc-4fd9-b7eb-68b31d024304),
[tres activos compartidos](http://localhost:9200/#/backtest/9f7ac256-699a-4e4d-9d4d-a639c0158a85).
El peor mes de tres activos empeora de −7,02% a −13,40%; su exposición bruta media al cierre diario pasa de 0,609x a 0,807x. El máximo observado es 4,426x porque el límite de admisión no es un techo continuo después del movimiento de precios.
La repetición con formulario invertido también coincide, con la misma limitación de prioridad interna descrita arriba.

No promover esta rama por su CAGR: solo añade un mes positivo y no mejora trimestres. Retenerla como comparador de capital. Tampoco promover BTC compartido por su 62,5%: sigue sin cumplir la meta y aumenta sustancialmente el drawdown.

## Decisión y trabajo pendiente
La referencia principal no cambia. Fase 2 sigue sin aprobarse; objetivos y 2026 reservados se mantienen.
La evidencia no justifica perseguir únicamente un filtro short de premio/riesgo ni una cuadrícula de pesos. El problema también está en la combinación de patas, utilización de capital y dependencia de tendencias grandes.
Antes de más búsqueda de parámetros, definir una asignación justificable sin conocer los resultados y completar las comprobaciones de prioridad real/ejecución. El ATR de SPY sobre horarios filtrados y el de cripto continuo no representan exactamente el mismo reloj: sigue siendo una limitación de asignación pendiente.
El Monte Carlo actual remuestrea rutas por separado y no conserva necesariamente dependencias/calendario conjunto. La extensión conjunta sigue siendo una propuesta sin implementar ni autorizar; no usar MC independiente como certificado de cartera.

## Informes y verificación
Diez nuevos backtests terminaron en esta ronda: dos de atribución, dos de orden del formulario, tres de costes y tres de capacidad compartida.
Análisis MCP completados correctamente: 9a54544d46e54aeaae5ff4295d7fc088 (atribución), 97cfed55e0804d5ca80f93ce13320adf (permutación del formulario), f36b013822404e04b7b273def00421e2 (costes), 434a696e8f7b4f289c6b0d4e1170641e (meses cambiados), 952f460501534c16b970c977512b12ef (capacidad compartida). Autocontroles MTM y reconciliaciones pasaron. git diff --check limpio. No se hicieron nuevas modificaciones del framework.

Informes dentro de strategies/MultiAssetRetestBtcShort4h/reports/:
- PHASE2_COMPARABLE_ATTRIBUTION_RESULTS_20261018.md
- PHASE2_ROUTE_ORDER_RESULTS_20261018.md (interpretación corregida)
- PHASE2_FIXED_FEE_RULES_RESULTS_20261018.md
- PHASE2_MONTHLY_COMPONENT_ATTRIBUTION_20261018.md
- PHASE2_SHARED_CAPACITY_RESULTS_20261018.md

Los datos descargados, exportaciones y registros generados están excluidos de Git. Se conservan código, informes, scripts y auditorías; no se borraron archivos ni se revirtieron cambios previos.


## Orquestación autónoma:18 pruebas adicionales terminadas
Objetivo sigue sin alcanzarse.18 es el recuento adicional de esta orquestación, no el total de investigación ni réplicas independientes. El inventario global comprende muchas más hipótesis. Referencia inmutable;2026no evaluado. Importación ETH terminada con3.248.443velasM1; se almacenó2026sin consultar rendimiento.

| Comparación | CAGR | DD motor | Meses activos positivos | Trimestres positivos |
|---|---:|---:|---:|---:|
|[Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb)|28,83%|−14,89%|33/61|15/21|
|[Longs salida5R](http://localhost:9200/#/backtest/efc9d485-56ea-49fb-95ed-0f93aa690e71)|20,85%|−22,43%|39/61|16/21|
|[Longs parcial2R+runner](http://localhost:9200/#/backtest/0c6cfad7-c5da-465d-a45e-7009d284a1ec)|23,48%|−9,96%|35/61|14/21|
|[Una entrada short por episodio](http://localhost:9200/#/backtest/74b84b33-2030-4b9c-ba19-03a18ef68420)|29,36%|−14,90%|33/61|15/21|

Ninguna se promueve.5R y referencia empatan14/19trimestres COMPLETOS: su aparente mejora depende de bordes parciales. Wilson/McNemar son diagnósticos descriptivos después de selección, sin nuevos criterios p/CI. Parcial mejora DD pero no regularidad suficiente. OneFill añade principalmente beneficio long por trayectoria del capital, no una gran mejora del short.

Otros diseños ensayados: dos controles de asignación, fallo de rango, filtros/invalidación short, corto con régimen diario, salida completa3R, dos guardas mensuales, reversión rápida, ruptura tras compresión, Turtle diario, rotación mensual, calendarioSPY y shock relativo BTC/ETH. Algunos pierden antes de fees; reducir turnover o correlación de piernas no crea expectativa. No rescatar con rejillas tras el fallo. Se detectó y evitó duplicar24h/48h ya investigados.

[BTC/ETH full](http://localhost:9200/#/backtest/62b9f852-8b48-4b4c-b59b-537e9e687a64):1247baskets completos,net−3403,17,CAGR−7,67%,DD−34,37%,10/63meses y1/21trimestres positivos.191baskets tienen desfase entre cierres de patas;no ejecución atómica. OLS de retornos no acredita reversión. No más umbrales/horas para rescatarlo.

Actualizaciones completas dentro de strategies/MultiAssetRetestBtcShort4h/reports/:
- ORCHESTRATION_RESEARCH_LEDGER_20261018.md
- ORCHESTRATION_ACCEPTANCE_CARD_20261018.md
- ORCHESTRATION_ROUND1_RESULTS_20261018.md hasta ORCHESTRATION_ROUND5_RESULTS_20261018.md
- ORCHESTRATION_LOCKBOX_CONTINUITY_20261018.md
Inventario global: strategies/OrchManageTurtleDaily/reports/ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md.

## Próximo alcance y límites
Se estudiaron propuestas pre-FOMC y cicloFed con fuentes primarias y calendarios exante, pero evidencia actualizada de desaparición/inversión aconsejó descartarlas ANTESde correr. No se invirtió retrospectivamente el signo ni se probaron más horas.
Existe propuesta concreta de auditoría pública de funding/basisBTC/ETH2020–2025: strategies/OrchLateralRelativeShock1h/reports/ORCH_CARRY_FEASIBILITY_PROTOCOL_20261018.md. Se solicitó autorización específica para el descargador/módulo research por reglaopt-in de bot/AGENTS.md. Ningún script de esa nueva línea creado ni descarga iniciada. Primera fase sería sólo datos/cobertura/costes potenciales, no un sistema carry ni autorización de cambios del framework.
No hay backtests/análisis/importaciones activos al cerrar esta actualización. El objetivo permanece activo con esa pregunta pendiente. No modificar la referencia, bajar los criterios ni abrir2026 mientras se decide el siguiente alcance.

MCP read_strategy(BtcTrendMaster) devuelve500 específico de ese legado; lectura opcional abandonada sin filesystem alternativo. Resultados, importación y guardado de reportes del MCP comprobados operativos. No se reinició nada ni se tocó ese archivo.
