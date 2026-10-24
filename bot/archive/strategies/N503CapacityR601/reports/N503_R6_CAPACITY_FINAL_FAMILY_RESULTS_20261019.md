# N503 R6 — familia de convivencia y ocupación

Cinco hipótesis, diez backtests nominales terminados sin error; no hubo reparaciones ni reintentos económicos. N204 sigue como referencia ultimate y N503 es semilla exploratoria no promovida. 2026 permanece cerrado incluso a inspección. Todas las ejecuciones y reportes se hicieron por Jesse-local MCP.

|Receta|Neto B, USDT|Neto C, USDT|Δ frente N204 B/C|Δ frente N503 B/C|
|---|---:|---:|---:|---:|
|P601|[13123.60](http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5)|[13307.81](http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f)|66.99 / 68.37|-205.11 / -229.09|
|P602|[13328.71](http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096)|[13536.90](http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7)|272.10 / 297.46|0.00 / 0.00|
|P603|[12143.86](http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523)|[12310.79](http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92)|-912.76 / -928.65|-1184.86 / -1226.11|
|P604|[13347.96](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52)|[13562.22](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb)|291.35 / 322.77|19.25 / 25.31|
|P605|[13328.71](http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9)|[13536.90](http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f)|272.10 / 297.46|0.00 / 0.00|

## Reglas y diagnóstico observado

P601 reserva la ruta si el contexto G original ya está preparado sin exigir RSI3<=20. Veta siete de82 eventos N503, incluye eventos ocupados; sólo66 suplementos se ejecutaron, frente67 de la semilla. Falla regularidad+5: B40/63 y C39/63 meses incluidos positivos. El resultado mejora N204 nominalmente, pero pierde frente N503. Mantener contadores de raw82 y accepted75 impide confundir veto con un nuevo latch.

P602 aplica cooldown de tres prefijos4h cerrados actualmente visibles, excluyendo la barra actual. No se activó ningún veto:82aceptados,67suplementos. Root confirmó identidad económica exacta de264/271 trades con N503; no es evidencia independiente. Los prefijos no se presentan como buffers indicadores históricos idénticos.

P603 cierra el suplemento cuando aparece readiness técnico R en una barra completa postfill. Trece salidas de este tipo,67suplementos, originalesSTOP116→125. Mayor disponibilidad no mejoró el neto: frente N503, suplemento B2599.405247→2093.715631 y STOP B1886.628164→1425.871321. Pasa regularidad+5 ambas carteras pero pierde aproximadamente913/929USDT frente N204 nominal. Trece salidas no equivalen a trece operaciones originales adicionales; sólo se observan nueve en el conteo agregado, con cambios de recorrido y capital compartido.

P604 exige ruptura confirmada al cierre de la siguiente vela exacta tras congelar un nivel técnico original. No se atribuye ejecución a ese STOP de observación; la salida real es MARKET al cierre. Cuatro liberaciones,67suplementos, STOP116→118. Mejora modestamente N503:19.25/25.31USDT. El suplemento sube a2661.450240/2633.157501; el grupo STOP baja a1863.073435/1872.004102, aun añadiendo dos operaciones. No atribuir la mejora a más STOPs rentables. Con+5 mantiene B41/61 completos y41/63 incluidos, C40/61 completos pero40/63 incluidos; C63.49% falla65%. Trimestres17/19 y18/21 ambas pasan. Δneto+10 frente N204301.685129/329.066473. No elegible.

P605 libera desde seis barras completas postfill sin ningún cierre favorable y con contexto G. Cualquier C<E completo desactiva para siempre esa salida durante el trade. No hubo liberaciones;67suplementos y netos nominales idénticos a N503. Root confirmó identidad económica exacta con N503 en264/271 operaciones; campos económicos con delta0 y tolerancia1e−7, fechas/tipo de entrada iguales. No aporta evidencia independiente.

## Límites y revisión

Readiness R/G es técnica, no una afirmación de margen/capacidad o elegibilidad real. Nunca se llama el planner original para observar, ni se alteran sus métodos, prioridad, HP, sizing o reservas. Los vetos P601/P602 se aplican después del latch N503 y geometría y consumen el evento sin retry; P603..605 preservan la entrada N503. Salidas sólo con velas4h completas postfill, excluyen parcial de entrada, con deadline48h prioritaria y sin rearmar artificialmente un original en el mismo callback.

QA311PASS, fixtures de implementación con adaptadores de indicadores y revisión de AST/branches/constantes. No representan evidencia de rentabilidad ni pruebas de infraestructura/frontend. Diez formas y30snapshots verificados antes, diezformas/BTCsnapshots/cincofuentesactuales confirmados idénticos después. Revisión independiente de las cinco fuentes exploratorias E601..605 sin desviaciones; no se editaron.

No se añadieron hipótesis, umbrales o combinaciones según resultados. La muestra2020–2025 ha sido muy reutilizada: ninguna ventaja es OOS ni prueba contra sobreajuste. Se preserva todo resultado de no efecto y adverso. Las20auditorías root están aprobadas y la matriz global cerró sin elegibles. La revisión independiente de aritmética de gates, márgenes, deltas, conteos y20resúmenes del motor confirmó selección vacía. No se ejecutan las seis verificaciones condicionales y no se promueve sustituta.

## Evidencia dentro del proyecto Jesse

- strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FROZEN_PROTOCOL_20261019.md
- strategies/N503CapacityR601/reports/N503_R6_CAPACITY_QA_SOURCE_20261019.md
- strategies/N503CapacityR601/reports/N503_R6_CAPACITY_SOURCE_QA_20261019.md
- strategies/N503CapacityR601/reports/N503_R6_CAPACITY_SESSION_REGISTRY_20261019.md
- strategies/N503CapacityR601/reports/N503_R6_CAPACITY_TERMINAL_JOURNAL_20261019.md
- strategies/N503CapacityR601/reports/N503_R6_INDEPENDENT_EXPLORE_SOURCE_REVIEW_20261019.md
