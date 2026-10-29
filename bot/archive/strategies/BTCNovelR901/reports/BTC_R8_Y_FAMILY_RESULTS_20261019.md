# BTC R8 creative Y — resultados finales de la familia

## Resultado

Se ejecutaron las tres hipótesis congeladas sobre N503, seis carteras completas B/C. Ninguna modificación económica después de resultados. **Y902 es un hallazgo positivo y queda retenida como candidata prometedora**: mejora neto, regularidad bajo costes y distribución por años. Aún no cumple todos los criterios del contrato congelado para reemplazar N204; un gate pendiente no prueba sobreajuste ni justifica descartarla. N204 sigue referencia; 2026 permaneció cerrado incluso a inspección.

| Receta | Cambio | Neto B USDT | Neto C USDT | Fills suplemento B/C |
|---|---|---:|---:|---:|
|Y901|Retesteo LIMIT al coste A congelado, una barra4h|11046.643830038218|11228.810189574662|33/33|
|Y902|Continuación STOP al mínimo de trigger, una barra4h|13446.23452557522|13680.349170886388|46/46|
|Y903|Salida adversa por readmisión sobre A con presión positiva|10679.172563829175|10898.840239454656|70/70|

- [Y901B](http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2) — ee4ecf79-a83d-4388-b4de-3f2e44d62fd2
- [Y901C](http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c) — fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c
- [Y902B](http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c) — cb305a17-1312-463e-bbf1-c8173dfae22c
- [Y902C](http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff) — b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff
- [Y903B](http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33) — 99393647-2bca-405b-b3f3-6c2b1a0bed33
- [Y903C](http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff) — 745952c3-9fef-4c4c-8450-9fe8b6d142ff

## Aprendizajes y límites

Y901 pierde rentabilidad: esperar retesteo redujo fills67→33 frente a N503 y alteró ocupación/reservas. Root concilió33 LIMIT por cartera. No se infiere el valor de las oportunidades no llenadas como si se hubieran operado.

Y902 mejora frente a N204 +389.619610497556/+440.906791039596 USDT y frente a N503 +117.52281275929/+143.446657826983 USDT. Root auditó finanzas y metadatos PASS,46suplementos:45STOP+1MARKET en cada cartera. El motor puede aproximar smartorders a MARKET; se informan tipos reales. +10bpsRT estático neto11477.310426/11594.998628, costes/calendario/años4de5 pasan según root. **Falla B al descontar su mejor mes incremental (enero2022): −19.760578 USDT; C +40.325146.** Ese −19.760578 es la diferencia incremental MTM acumulada del resto del período al retirar el mejor mes, **no una pérdida del escenario2022**. C conserva +40.325146. Este único gate pendiente bloquea el reemplazo bajo el contrato vigente, pero **no descarta Y902 ni demuestra sobreajuste**. Se retiene para estudiar concentración, estabilidad de ejecución y continuidad del mecanismo. La muestra sigue reutilizada y no constituye validación independiente. No se añadieron filtros a enero2022 ni se reajustaron umbrales.

Y903 intervino29veces por cartera y empeoró el neto a pesar de menor DD B. events82,occupied7,fills70,closes70 ambas. Root confirmó **29 salidas emparejadas del suplemento modificadas frente a N503**, misma entrada, superando el gate de diversidad sin contar efectos indirectos de cartera. Finanzas y metadatos auditados PASS;70/70fills MARKET reconciliados por cartera, +10bpsRT estático neto8711.308825975375/8823.544272012321. Prueba central: BTC_R8_Y903_SUPPLEMENT_EXIT_TRACE. Su resultado nominal ya no supera referencia.

Las atribuciones monetarias se limitan a cartera auditada; no se llama original a todo STOP porque Y902 mezcla tipos. Root hace unión bijectiva de logs BTC_EXPLORE_FILL contra paths por tiempo/entry/qty, ratios y terminalcounts; no se copiaron arrays financieros a código.

## Validación y reproducibilidad

QA final745b2036ce3c456c933267f36026baaf: **201PASS**; fixtures fuente/fórmula/clock/expiry/reset/SLTPdeadline/telemetría. PrimerQA200PASS; dos fallos iniciales sólo del harness quedaron corregidos/documentados. No sustituyen validación engine. Fuentes finales3 readbacks exactos,6sesiones finished sin excepción,6formas completas exactas y18snapshots exactos. Contrato10000USDTshared,1%trade/8%agregado,5xisolated,cap4.4,reserva.001,fee.00045lado;PAXG original ySPYB/C conservados. Fechas2020-10-15→2025-12-31 exclusiva; últimos precios2025-12-30. Duraciones:83.37/83.67s Y901,101.29/101.56s Y902,82.08/82.42s Y903. Sin fallos engine, limpieza ni cambios live/globalconfig.

Las seis corridas terminaron y root confirmó sus auditorías financieras y reconciliaciones de metadatos PASS. Matriz global26/26 final: ninguna elegible para reemplazo según contrato congelado. **Y902 se conserva como candidata prometedora**, sin promoción y sin nuevos backtests en esta ronda.
