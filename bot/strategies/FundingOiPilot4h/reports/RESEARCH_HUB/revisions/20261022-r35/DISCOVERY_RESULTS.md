# R34 — cinco evaluaciones terminadas, ninguna candidata

La ronda respondió tres preguntas distintas. Todas las cuentas terminaron positivas, pero ninguna alcanzó los objetivos conjuntos de retorno y regularidad. Dos mecanismos generaron muy pocas oportunidades; el tercero tuvo actividad suficiente, con rentabilidad modesta y regularidad insuficiente.

|Prueba|Operaciones|CAGR neto base|DD M1 y fills|Meses activos positivos|Resultado|
|---|---:|---:|---:|---:|---|
|[A_VALUE](http://localhost:9200/#/backtest/eafeebb7-faa4-4c27-a998-05a530955c67)|6|0.170%|0.831%|4/4|NO_CUMPLE|
|[A_R2](http://localhost:9200/#/backtest/d726bd52-56fe-4a22-aac5-9a44f4f00056)|6|0.553%|0.831%|4/4|NO_CUMPLE|
|[B_CROSS](http://localhost:9200/#/backtest/949c6c55-5845-4fc1-beec-ebcd618692ec)|117|6.846%|10.916%|30/62|NO_CUMPLE|
|[C_NORMAL](http://localhost:9200/#/backtest/36040b37-aa26-403c-9416-ee2f32185959)|5|0.755%|1.527%|3/6|NO_CUMPLE|
|[C_DAY](http://localhost:9200/#/backtest/f6697dd8-24d2-44cb-9fb5-c901385237c6)|5|0.740%|1.444%|4/6|NO_CUMPLE|

**Valor diario frente a 2R.** Sólo hubo seis patrones brutos, todos ejecutados en cada alternativa. Sin huecos de datos, rechazos de objetivos, ocupación o salidas de seguridad. El objetivo en valor diario produjo menos neto que2R. Ambas medianas calendario son cero y sólo3/20trimestres fueron positivos. El100% de meses activos ganadores corresponde a4/62meses calendario, no a una entrega regular.

**Cruces de tendencia archivados.** La receta pendiente de evaluación actual produjo117operaciones, neto+4125.65USDT yPF1.516. Sin embargo, CAGR6.846%, meses30/62, trimestres13/20 y mediana−0.307% incumplen las metas. El archivo previo permanece descriptivo: ventana y sizing diferentes impiden atribuir causalmente el cambio de retorno. No se elige long-only a partir de la atribución observada.

**Normalización posterior a volatilidad frente a esperar24h.** Ambos brazos operaron los mismos cinco episodios. La normalización añadió apenas7.90USDT con mayor DD y menos meses positivos. PF alto conN5 no acredita ventaja persistente ni justifica relajar el umbral para fabricar frecuencia.

Las comparaciones son cuentas alternativas sobre el mismo capital total de10000, con cuota1% activa y el resto ocioso; no se suman sus curvas. Conservan3xaislado, fees taker descontadas.00045porlado, funding histórico aplicado y reserva.001 sólo de sizing. Slippage modelado cero. La ventana [2020-10-15,2026-01-01) es historia ya observada y adaptativa; no OOS nuevo ni validación prospectiva.

Se conciliaron139trades y3324pagos de funding, órdenes ejecutadas, geometría, cantidades, plazos, balances y cortes mensuales. Tres checks sintéticos y tres auditorías de snapshots pasaron al primer intento; no hubo motores fallidos, reemplazos ni reruns. Los207outcomes sintéticos comprueban implementación con datos fabricados, sin acreditar rentabilidad. Las tres revisiones independientes interpretaron resultados completos y universos; no repitieron por segunda vez todos los fills.

Se cierran las tres preguntas y su presupuesto de cinco motores, sin vecinos de parámetros, selección retrospectiva de lados o cambios de riesgo. La siguiente pregunta deberá justificar una fuente de oportunidades distinta y suficientemente recurrente, contrastada con el historial. Buscar más frecuencia relajando estas mismas reglas no constituye por sí solo una explicación económica de ventaja.

El objetivo global sigue pendiente: ninguna candidata nueva, ningún libro conjunto y ninguna promoción. La investigación autónoma continúa dentro de los límites acordados; esta ronda no autoriza nuevos datos, estrés,2026,cartera o ejecución live/paper.

Detalles y evidencias: BTC_R34_A_FINAL_20261022.md, BTC_R34_B_FINAL_20261022.md, BTC_R34_C_FINAL_20261022.md; sus RESULTS/DURABLE_INDEX/UNIVERSE_CHECK y críticas independientes. Cada archivo de resultados conserva los recibos de auditoría y referencias a registros completos.
