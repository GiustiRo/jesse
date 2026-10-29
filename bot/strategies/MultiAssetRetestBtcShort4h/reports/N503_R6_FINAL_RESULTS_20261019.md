# BTC — cierre de la ronda R6

## Decisión

Se completaron 20 backtests nominales: diez hipótesis, cada una en las carteras B y C, con dos agentes nuevos y dos backtests simultáneos por agente. Ninguna supera todos los criterios congelados. N204 continúa como referencia; N503 y P604 son candidatos de investigación, sin promoción. No se activan las seis verificaciones condicionales: el protocolo las reservaba para una única receta elegible después de los veinte resultados. No se escoge otra regla ni se flexibilizan umbrales tras ver resultados.

N204: neto B 13056.61, C 13239.44 USDT.

N503: neto B 13328.71, C 13536.90 USDT.

La mayor mejora nominal de la ronda es P604. Frente a N204 suma 291.35 / 322.77 USDT; frente a N503 suma 19.25 / 25.31. En C, sus 40 meses positivos de 63 activos bajo +5 bps adicionales de coste por ida y vuelta son 63,49%, por debajo del 65% exigido. No alcanza la regularidad necesaria.

## Diseño y lectura de los resultados

B usa SPY Second: segunda oportunidad exacta del episodio y precio estructural original. C usa SPY Market: desde la segunda oportunidad y repricing a precio actual. Ambas usan el mismo BTC, PAXG y capital compartido; no son dos muestras independientes.

Todas las reglas parten de N503, con ER original fijado en 0<ER<=1/3. Cinco filtros nuevos o combinaciones explícitas de mecanismos ya probados; cinco reglas para estudiar la convivencia del suplemento MARKET con el corto STOP original. Fuentes, hipótesis, prioridad, fechas, puertas y ranking quedaron fijados antes de los resultados. No se modificó la operativa original, el dimensionamiento ni el contrato de cartera. La ocupación y el capital sí pueden cambiar las ejecuciones observadas.

|Hipótesis|Idea|Neto B|Neto C|Δ N204 B / C|+5 meses activos B / C, incluidos|Resultado|
|---|---|---:|---:|---:|---|---|
|E601|Volumen del gatillo superior a la mediana|[12139.28](http://localhost:9200/#/backtest/9a11306e-c60c-4453-800a-34cac602dbdc)|[12329.38](http://localhost:9200/#/backtest/b12c2e5d-2a3b-4036-be2a-3de93ee3b359)|-917.34 / -910.06|39/62 / 39/62|Falla nominal, calendar, plus10|
|E602|Mecha superior dominante en la vela previa|[12229.55](http://localhost:9200/#/backtest/19a83d39-c77e-41a4-a0b7-0edabd14b136)|[12426.75](http://localhost:9200/#/backtest/4da71fcf-5806-4aaa-9f52-5c7a62761040)|-827.06 / -812.69|41/61 / 42/61|Falla nominal, calendar, plus10|
|E603|Cuerpo compuesto de 8 horas bajista|[12378.55](http://localhost:9200/#/backtest/0fff0dca-c5c4-4745-a1f7-1926300d7867)|[12551.14](http://localhost:9200/#/backtest/aabc659d-e33f-472b-942a-e9b2adcc0abe)|-678.06 / -688.30|41/63 / 40/63|Falla nominal, calendar, plus10|
|E604|Espacio hasta soporte para el objetivo de 2R|[9055.47](http://localhost:9200/#/backtest/3a0b72cf-183b-4920-a863-845b77a9443e)|[9206.39](http://localhost:9200/#/backtest/a20faa2e-315a-4319-8138-44a12b84d49b)|-4001.15 / -4033.05|36/59 / 38/59|Falla nominal, calendar, plus10|
|E605|Cierre de última hora rompe mínimos de las primeras tres|[11674.38](http://localhost:9200/#/backtest/fbae9638-daef-4a34-ba29-5fdfd1c796e6)|[11883.70](http://localhost:9200/#/backtest/adfde635-9272-4a1c-ad63-347d7a0cd826)|-1382.24 / -1355.74|41/61 / 42/61|Falla nominal, calendar, plus10|
|P601|Reservar espacio si existe contexto técnico original|[13123.60](http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5)|[13307.81](http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f)|66.99 / 68.37|40/63 / 39/63|Falla calendar|
|P602|Vetar si hubo preparación técnica en tres prefijos previos|[13328.71](http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096)|[13536.90](http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7)|272.10 / 297.46|41/63 / 40/63|Falla calendar|
|P603|Liberar al aparecer preparación técnica original|[12143.86](http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523)|[12310.79](http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92)|-912.76 / -928.65|43/63 / 41/63|Falla nominal, plus10|
|P604|Liberar tras confirmación del precio en la vela siguiente|[13347.96](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52)|[13562.22](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb)|291.35 / 322.77|41/63 / 40/63|Falla calendar|
|P605|Liberar estancamiento desde seis velas con contexto original|[13328.71](http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9)|[13536.90](http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f)|272.10 / 297.46|41/63 / 40/63|Falla calendar|

`nominal`: superar N204 en neto por más de 1e-7 USDT en ambas carteras; `calendar`: bajo +5 bps adicionales, meses positivos/activos>=65% y trimestres positivos>=80%, tanto periodos completos como incluidos; `plus10`: neto con +10 bps no inferior a N204 con el mismo recargo, tolerancia 1e-7; `dd`: drawdown del motor no peor que -25%. Positivos estrictamente >0, sin redondeo. Matriz completa: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_RESULTS_MATRIX_20261019.md`.

## Qué se aprendió

P602 y P605 son económicamente idénticas a N503 en las dos carteras: mismos tiempos, tipos de entrada, precios, cantidades, comisiones y PNL, con tolerancia 1e-7; cero diferencia máxima. El veto de P602 y la salida de P605 nunca se activaron. Repetir esa trayectoria no añade evidencia independiente.

P603 efectuó 13 liberaciones y el conteo agregado de STOP subió de 116 a 125 por cartera; ambas cohortes de cortos ganaron menos. Cumple la regularidad +5 de ambas carteras, a costa de perder aproximadamente 913 / 929 USDT frente a N204. No se puede identificar cada liberación con una entrada adicional ni interpretar preparación técnica como orden realmente ejecutable.

P604 hizo cuatro liberaciones; el conteo STOP subió de 116 a 118. El suplemento siguió en 67 operaciones, su neto mejoró, mientras el neto de los STOP bajó ligeramente frente a N503. La cartera mejora poco y sigue fallando el criterio mensual de C. El shadow STOP sólo fija una condición de salida al cierre de la vela siguiente; no se contabiliza como ejecución hipotética de un STOP.

E602 reduce drawdown, pero pierde rentabilidad; E604 descarta demasiadas oportunidades y se aleja notablemente de la referencia. E605 tuvo 115 evaluaciones M1 válidas: 46 pasaron y 69 no; cero faltantes de reloj, datos corruptos o diferencias entre el cierre M1 y el 4h. Generó29 operaciones por cartera. Su caída de rentabilidad no se explica por falta de cobertura en esas evaluaciones. E604 produjo sólo una operación del suplemento; E602 produjo24. Estos recuentos pequeños limitan cualquier conclusión universal sobre sus mecanismos. El informe de la familia exploratoria conserva los contadores. No se mezclaron a posteriori filtros y salidas ganadores ni se ajustaron fechas problemáticas.

## Alcance, costes y verificación

Ventana 2020-10-15 hasta 2025-12-31 exclusiva. 2026 permaneció cerrado incluso a inspección. Es una muestra de desarrollo reutilizada en numerosas rondas; no constituye OOS, prueba contra sobreajuste ni validación para operar. La multiplicidad de búsqueda acumulada sigue pendiente.

Contrato: 10000 USDT compartidos; 1% por operación / 8% agregado; isolated 5x; sin piramidación; cap nocional 4.4; reserva .001 sólo para sizing; fee nominal .00045 por lado. PAXG mantiene su break-even dependiente del fee. Tres rutas 4h y tres feeds 1m; warmup240, debug true, fast false, chart true. No se implementó funding.

Los recargos +5/+10 bps por ida y vuelta se aplican a fills, cantidades, precios y tiempos fijos. No simulan cambios de sizing, prioridad ni break-even dependiente del fee; no son una corrida con mayor fee real. Al no haber candidata elegible no se ejecutaron las dos corridas engine .00070 por lado ni las cuatro sensibilidades TP1.8R/2.2R previstas condicionalmente.

Auditoría de los veinte: fills, cantidades, comisiones, PNL, wallet, liquidación terminal y MTM diario UTC reconciliados, cuatro anclas históricas congeladas. Se distinguen drawdown del motor, drawdown diario y cohortes de trades. Los contadores de posiciones abiertas previos a liquidación final no se interpretan como posiciones restantes después del cierre; el auditor reconcilia la frontera. Conteos full: 61 meses /19 trimestres; incluidos63/21; meses activos variables y calendario completo se muestran por separado.

QA de código: 196 comprobaciones finales exploratorias y311 de convivencia; revisión cruzada independiente de las dos familias; lectura final exacta de17 fuentes;20 formularios y60 snapshots coinciden. Se preservan las31 entradas largas de BTC y sus tiempos de salida en cada corrida; pueden variar cantidades por capital. Verificaciones y fuentes de auditor/ranking están archivadas en reportes R6. No hubo operaciones live/paper ni cambios de configuración global.

## Continuación recomendada

Conservar N204 como referencia y P604 como pequeño avance nominal pendiente. Antes de sumar otra batería, estudiar si la mejora de P604 depende de muy pocas operaciones y cuantificar la selección acumulada. Una siguiente investigación debe fijar de antemano una hipótesis económica de convivencia, con pocos grados de libertad y criterios de estabilidad bajo costes; conservar 2026 cerrado hasta decidir por escrito el protocolo final de evaluación. No buscar una regla para rescatar un mes o una fecha concretos.

## Trazabilidad

Protocolo: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FROZEN_PROTOCOL_20261019.md`.

Auditor/ranking: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_AUDITOR_SOURCE_20261019.md`.

Revisión root: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_ROOT_SOURCE_REVIEW_20261019.md`.

Revisiones cruzadas: `strategies/N503ExploreR601/reports/N503_R6_INDEPENDENT_CAPACITY_SOURCE_REVIEW_20261019.md` y `strategies/N503CapacityR601/reports/N503_R6_INDEPENDENT_EXPLORE_SOURCE_REVIEW_20261019.md`.

Auditorías financieras por pareja: `strategies/MultiAssetRetestBtcShort4h/reports/N204_R6_AUDIT_<E601..E605 o P601..P605>_20261019.md`.

El registro adjunto conserva URLs, IDs, estado, fee y fuente; el manifiesto de cierre conserva formularios, snapshots, jobs y paridades económicas.

## Revisión independiente de cierre

El agente de convivencia recalculó las puertas y ranking de la matriz final: 351 comprobaciones aprobadas. Contrastó los20 resúmenes MCP de sesiones finalizadas sin error, neto, DD y número de operaciones, con concordancia menor de1e-7. Selección vacía confirmada; P604 falla C40/63 y P603 falla nominal/+10. Esta revisión verifica el ranking y su trazabilidad; no es una segunda reconstrucción independiente del MTM.

Revisión: `strategies/N503CapacityR601/reports/N503_R6_INDEPENDENT_FINAL_MATRIX_REVIEW_20261019.md`.

Informes familiares: `strategies/N503CapacityR601/reports/N503_R6_CAPACITY_FINAL_FAMILY_RESULTS_20261019.md` y `strategies/N503ExploreR601/reports/N503_R6_E_FINAL_FAMILY_RESULTS_20261019.md`.

Manifiesto y registro completo: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FINAL_REGISTRY_AND_MANIFEST_20261019.md`.
