# R60 SPY — sensibilidad individual de la referencia

Diez perturbaciones fijadas antes de resultados no producen una mejora económica material que justifique reemplazar la referencia. Hay una zona local con exactamente la misma trayectoria ejecutada: Cq, GapMax75, Donchian24, Donchian28 y EMA rápida16. Eso aporta una observación de estabilidad del resultado ante esos cambios, pero sigue siendo una sola trayectoria de31 trades, no cinco validaciones independientes.

Las diez corridas terminaron. Se mantuvieron intactos gestión, riesgo, frescura, calendario y datos. No se combinaron parámetros ni se eligió el mayor retorno. La única variante con neto superior al de Cq, EMA rápida24, aumenta apenas0.364237 USDT en toda la ventana; no demuestra una mejora material.

## Resultados completos

| ID | Cambio individual | N | Neto | PF | DD motor % | Sharpe motor | Tiempo abierto % |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | Referencia existente | 31 | 751.35 | 1.49 | −5.21 | 0.458 | 15.26 |
| [S01](http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21) | 0.10 < g ≤ 1 | 23 | 82.95 | 1.07 | -6.65 | 0.076 | 11.08 |
| [S02](http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae) | 0.25 < g ≤ 1 | 14 | 245.87 | 1.34 | -4.10 | 0.232 | 6.82 |
| [S03](http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e) | 0 < g ≤ 0.50 | 30 | 743.97 | 1.49 | -6.13 | 0.460 | 14.44 |
| [S04](http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35) | 0 < g ≤ 0.75 | 31 | 751.35 | 1.49 | -5.21 | 0.458 | 15.26 |
| [S05](http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134) | Donchian 24 | 31 | 751.35 | 1.49 | -5.21 | 0.458 | 15.26 |
| [S06](http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2) | Donchian 28 | 31 | 751.35 | 1.49 | -5.21 | 0.458 | 15.26 |
| [S07](http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60) | ADX mínimo 24 | 39 | 597.94 | 1.30 | -8.10 | 0.338 | 18.11 |
| [S08](http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb) | ADX mínimo 28 | 24 | 686.03 | 1.56 | -5.89 | 0.473 | 12.02 |
| [S09](http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f) | EMA rápida 16 | 31 | 751.35 | 1.49 | -5.21 | 0.458 | 15.26 |
| [S10](http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a) | EMA rápida 24 | 31 | 751.71 | 1.49 | -5.21 | 0.458 | 15.25 |


Capital inicial10 000, riesgo presupuestado1% por trade, fee0.00045 por lado incluyendo LIMIT. g=(close−máximo Donchian previo)/ATR, y la referencia usa0<g≤1, Donchian26, ADX mínimo26 y EMA rápida20. Cada fila cambia una sola pieza. Son diez controles de sensibilidad sobre una misma estrategia, no diez mecanismos nuevos.

N son operaciones cerradas, no fills ni observaciones independientes. DD y Sharpe de la tabla son los calculados por el motor; no se presentan como estadísticas de cierre diario UTC. Los valores completos, incluidos CAGR, fees, turnover, exposición ponderada y cohortes, están en R60_SPY_EXACT_RESULTS_20261019.md. Root completó la auditoría MTM independiente de las diez sesiones. S09/S10 conservan15/61 meses completos positivos y9/19 trimestres positivos, con DD diario−5.2179629%, igual a Cq; no se toma esa igualdad de calendario como independencia. No se duplican sus marks ni se usa la curva Portfolio del motor como cierre UTC.

## Qué cambió al restringir la distancia al canal

S01 exige un breakout superior a0.10ATR; baja a23 trades, net82.95 y Sharpe0.076. Con5bps adicionales por roundtrip termina−34.83. S02 exige más de0.25ATR; queda en14 trades y net245.87. Su DD observado es menor, pero también hay menos exposición:6.82% del tiempo frente15.26% en Cq. Sin su mejor trade pierde73.85. La muestra de14 operaciones no permite afirmar que esa selección mejore el riesgo de forma estable.

S03 limita el exceso sobre el canal a0.50ATR. Conserva30 trades y net743.97, casi el mismo retorno que Cq, pero DD motor−6.13% frente−5.21%. El neto por notional de entrada pasa de23.64 a24.24bps; esa pequeña diferencia no establece una política superior cuando cambian las entradas y su ocupación.

S04 limita g a0.75 y reproduce exactamente todos los campos económicos de los31 trades y la curva numérica completa de Cq. Esto se refiere a ejecución observada. Los snapshots no incluyen toda señal ni orden cancelada: no se afirma que el límite jamás rechazara un arming sin efecto posterior.

## Zona de trayectoria idéntica y pequeños cambios

La comparación de snapshots completos verifica igualdad exacta de símbolo, lado, timestamps de entrada/salida, precios, cantidades, PnL, fee y duración de todos los trades, además de la curva numérica completa, entre:

- Cq, referencia existente.
- S04, máximo0.75ATR.
- S05, Donchian24.
- S06, Donchian28.
- S09, EMA rápida16.

N24/N28 alrededor del26 y Fast16 frente20 no desestabilizan el resultado ejecutado de esta ventana. Es evidencia local de insensibilidad económica de esos cambios, no prueba de robustez global, independencia ni de inactividad de todos los filtros. La fuente de datos y la ventana son las mismas; la concentración original se conserva sin alteración.

S10, EMA rápida24, tiene30 entradas exactas en común con Cq y una distinta en cada política. Su curva NO es idéntica. El neto pasa de751.3477149671152 a751.7119522395761, con fees de286.47552620734854 a286.7708466456683. El neto por notional rotado baja ligeramente, de23.6431 a23.6302bps. No se elige esta fila por ser el máximo nominal del lote.

## Sensibilidad al umbral ADX

S07, ADX mínimo24, sube a39 trades y18.11% del tiempo abierto. Gana597.94, con DD motor−8.10% y Sharpe0.338: más participación no mejora la relación observada entre retorno y riesgo frente a Cq.

S08, ADX mínimo28, reduce a24 trades y12.02% del tiempo. Neto686.03, PF1.555 y Sharpe0.473 frente1.493/0.458 en Cq. También tiene menor retorno total y DD motor algo peor,−5.89%. Con10bps adicionales gana442.72 frente433.04 de Cq; esa diferencia pequeña, con muestra y exposición distintas, no basta para reemplazar el umbral original tras mirar diez variantes. Suprimir los tres mejores deja−360.35.

Estas comparaciones son de políticas completas. Una entrada omitida puede liberar espacio para una señal posterior; no basta llamar a una variante «subconjunto» de Cq para atribuir causalmente la diferencia a las entradas retiradas.

| Variante | Entradas comunes exactas con Cq | Sólo Cq | Sólo variante |
| --- | ---: | ---: | ---: |
| S01 | 17 | 14 | 6 |
| S02 | 8 | 23 | 6 |
| S03 | 29 | 2 | 1 |
| S04 | 31 | 0 | 0 |
| S05 | 31 | 0 | 0 |
| S06 | 31 | 0 | 0 |
| S07 | 26 | 5 | 13 |
| S08 | 19 | 12 | 5 |
| S09 | 31 | 0 | 0 |
| S10 | 30 | 1 | 1 |


Los pares usan mismo símbolo, lado y timestamp real de fill, sin emparejamiento por cercanía. PnL normalizado por notional de entrada se conserva en los archivos de pares. Esa normalización no elimina selección por doble fill ni ocupación endógena. Ejemplo: S01 tiene seis entradas que no están en Cq pese a usar un predicado de señal más restrictivo; no se presume una historia idéntica de oportunidades mientras hubo posiciones abiertas.

## Costes y concentración

| ID | Neto +5 bps RT | Neto +10 bps RT | Sin mejor trade | Sin tres mejores |
| --- | ---: | ---: | ---: | ---: |
| Cq | 592.19 | 433.04 | 349.58 | −298.22 |
| S01 | -34.83 | -152.62 | -251.69 | -690.99 |
| S02 | 176.23 | 106.58 | -73.85 | -512.81 |
| S03 | 590.29 | 436.60 | 342.46 | -302.32 |
| S04 | 592.19 | 433.04 | 349.58 | -298.22 |
| S05 | 592.19 | 433.04 | 349.58 | -298.22 |
| S06 | 592.19 | 433.04 | 349.58 | -298.22 |
| S07 | 403.23 | 208.53 | 198.38 | -451.92 |
| S08 | 564.38 | 442.72 | 290.37 | -360.35 |
| S09 | 592.19 | 433.04 | 349.58 | -298.22 |
| S10 | 592.39 | 433.08 | 349.92 | -297.90 |


Los costes adicionales son un descuento estático sobre los mismos fills y tamaños, usando el notional de ambas piernas. No simulan spread, cambio de ejecución, colas, impacto ni nuevo sizing. Todas las variantes salvo S01 permanecen positivas con10bpsRT adicionales en esta ventana, pero todas quedan negativas al retirar los tres mejores trades. Esto conserva la dependencia de runners de la referencia y no equivale por sí solo a descarte automático de una estrategia que deja correr ganancias. No debe presentarse la positividad tras costes como prueba de repetibilidad.

S01/S02 son las únicas filas que también pierden al retirar sólo su mejor trade. El resto mantiene neto positivo sin el mejor, aunque no sin los tres mayores. La observación más estable del lote es continuidad de una trayectoria ya conocida en varios vecinos; no surgieron diez muestras nuevas de ganancias.

## Condiciones preservadas y límites

SPY-USDT4h con data route1m, warmup240, fast_mode=false y debug_mode=false. Historia UTC Mon-Fri00:00–20:00; barras elegibles de entrada abiertas00:00–16:00. Mismo guard de quote M1T−60s con finitud y paridad; cancelación y gestión sin cambios. No se cambió a RTH.

Stop2ATR, BE2.25R, trail4.2ATR con tightening heredado en5R/8R. Capital10 000, presupuesto de riesgo1%, cartera8%, gross máximo4.4, isolated5x, margen90%, step.001 y reserva.001 sólo para sizing. El presupuesto no garantiza pérdida realizada máxima ante gaps. Funding fuera; proxySPXCFDBID/10 aceptado para investigación de precio. No se afirma paridad de spreads, liquidez, lot sizes o ejecución de Binance perpetual.

Ventana2020-10-15→2025-12-31 exclusiva;2026 cerrado. Historial extensamente reutilizado, no OOS limpio. No se modificaron referencia, framework, BTC, datos, configuración global ni instalaciones. Sin live/paper/Pi/restarts/scripts nuevos. Todos los resultados se conservan en la selección acumulada.

La igualdad de fills no identifica señales rechazadas que no llegaron a ejecutarse. Las cohortes anuales por año de cierre son diagnósticos de operaciones y NO retornos anuales MTM. Una posición que atraviesa meses no aporta una observación independiente por mes. La regularidad de cartera no se impone como requisito a cada señal aislada.

## Trazabilidad

Protocolo R60_SPY_PROTOCOL_20261019.md guardado antes de código/resultados. Fuente común y diffs exhaustivos en R60_SPY_IMPLEMENTATION_REVIEW_20261019.md; readback exacto10/10 y revisión root antes de lanzar. Snapshots completos de código en las notes de los diez dashboards antes de cada run. Baseline Cq existente no se volvió a ejecutar.

Dos jobs de análisis completos succeeded:50bf614e29144b658757ad2d275e77ca y e16f88c74fc3409bb25b796d88f7ff6c. El primero incluyóCq+S01..05; el segundoCq+S06..10 y S04/S05 para certificar grupos sin nuevosfulls. Resúmenes JSON íntegros de21 366 y34 514bytes, ambos<50KB, preservados en R60_SPY_AUDIT_BATCH1_20261019.md y BATCH2. Fuente original en R60_SPY_ANALYSIS_SOURCE_20261019.md; comparador de identidad en R60_SPY_PATH_IDENTITY_ANALYSIS_ADDENDUM_20261019.md.

Diez filas exactas y baseline separado: R60_SPY_EXACT_RESULTS_20261019.md. Pares completos Cqcontra cada variante persistidos íntegros en R60_SPY_COMMON_ENTRIES_S01_20261019.md hasta S10. Registro terminal: R60_SPY_SESSION_REGISTRY_20261019.md. No se afirma inspección visual adicional de PNG: la identidad se verificó numéricamente sobre snapshots y curvas completas.

## Dashboards

Referencia Cq:

Dashboard: http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639

S01 — R60SpyGapMin10

Dashboard: http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21

S02 — R60SpyGapMin25

Dashboard: http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae

S03 — R60SpyGapMax50

Dashboard: http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e

S04 — R60SpyGapMax75

Dashboard: http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35

S05 — R60SpyN24

Dashboard: http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134

S06 — R60SpyN28

Dashboard: http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2

S07 — R60SpyAdx24

Dashboard: http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60

S08 — R60SpyAdx28

Dashboard: http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb

S09 — R60SpyFast16

Dashboard: http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f

S10 — R60SpyFast24

Dashboard: http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a


No se promueve una variante ni se combina parámetros a partir de este lote. El resultado justifica conservar la referencia para próximos contrastes y documentar qué vecinos resultan económicamente idénticos, cuáles alteran participación y dónde continúa la dependencia de pocos runners.
