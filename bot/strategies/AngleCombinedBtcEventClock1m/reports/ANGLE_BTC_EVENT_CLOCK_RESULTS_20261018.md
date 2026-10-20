# Reloj de eventos BTC — resultado final: descartado

[Backtest combinado completo](http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967). Desarrollo 2020-10-15→2025-12-31 exclusivo, modo normal, BTC1m con auxiliar4h cerrada; PAXG/SPY4h conservados. Cuenta compartida10000USDT,5xaislado,fee0,00045por lado para todas las órdenes, riesgo máximo3%portrade/8%agregado y techo bruto4,4x. **2026 permanece reservado y la referencia no cambia.**

## Política evaluada y selección
Una receta predeclarada: eventos alternantes desde extremos de cierresM1 al revertir una ATR14 de4h, congelada al inicio de cada fase. Inicialización neutral en primer boundary4h válido, sin señal artificial; eventos consumidos también durante posiciones y órdenes pendientes. DOWN reemplaza elegibilidadRSI3 y permite señal short entre fronteras4h. Conserva régimenEMA120,proximidad,EMA20/distancia1–3ATR,TP1,5ATR y gestión72h evaluada4h.

El STOP usa min(lowM1delevento,p−0,25ATR4h), adaptación aprobada antes de ver resultados. Por tanto esta prueba cambia conjuntamente lectura de señal, cadencia y nivel de entrada: **no aísla causalmente el efecto del reloj**. Longs y demás activos conservan reglas, aunque capital y ocupación puedan cambiar sus fills/cantidades.

El [control BTC1m](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1) reprodujo220trades/440órdenes registradas y45métricas de referencia. El [smoke técnico Q1-2021](http://localhost:9200/#/backtest/124865f1-ec3c-4c0a-a6d9-7dcb5ad3bda6) precedió al full; su beneficio no eligió parámetros ni autorizó alpha. Se añadió sólo telemetría first/init/last después, con identidad de decisiones verificada. No hubo ajuste de umbrales entre smoke y full.

## Resultado de cuenta y componentes

| Medida | Resultado |
|---|---:|
| CAGR |17,599567%|
| DD del motor |−15,669916%|
| Sharpe |0,910326|
| Neto USDT |13284,891739|
| Fees USDT |3097,647678|
| Trades |185:96longs/89shorts|

La referencia tiene28,83%CAGR,DD−14,89%,97longs/123shorts y neto27461,46USDT. Esta variante reduce retorno y no mejora DD.

ShortsBTC: **neto−3848,835196USDT**,fees831,283090,PF0,671347 yWR41,573%. PnL de precio a los fills/cantidades efectivamente observados **−3017,552106** antes de fees: el fallo no es exclusivamente coste de comisión. No es una simulación independiente fee cero.

Contribución long neta por activo, no rendimiento de cuentas aisladas: BTC30trades,+11091,5055;SPY31,+2874,64545;PAXG35,+3167,57601USDT. Su total cambia pese a reglas congeladas; no adjudicarlo a nueva señal long ni sumar curvas independientes.

## Auditoría MTM y regularidad

Root confirmó **V4 succeeded**,job cabb99082ffd47ec99028fcd2d1c8d6d, con reconciliación técnica.

| Medida | Todos los bins, incluidos extremos parciales | Sólo períodos completos |
|---|---:|---:|
| Meses activos positivos |28/58=48,2759%|28/56=50%|
| Meses positivos sobre calendario |28/63=44,4444%|28/61=45,9016%|
| Trimestres positivos |11/21=52,3810%|10/19=52,6316%|

Peor mes−6,32194%;peor trimestre−8,99910%;retornoMTM2022−8,93226%. La comparación pareada rescata2meses y perjudica7 frente a referencia; esas fechas no se transforman en filtros. Se mantienen criterios65–70%mesesactivos/80%trimestres/DDnopeorque−25%, sin cambiar denominadores ni elegir bordes favorables.

## Cobertura y contadores finales

Full: **2740320callbacks M1 exactos**,primero2020-10-15T00:01Z,inicialización2020-10-15T04:00Z,último2025-12-31T00:00Z. La cobertura completa está comprobada; la inicialización previa a trading se conserva en la ventana y no se elimina como cash incómodo.

EventosDOWN2009=316bloqueadosporposición+1porpendiente+0prioridadlong+1582rechazados+110planes. Armed110,fills89;UP2008. Identidad global reconciliada y alternancia coherente. Armed/fills anuales no serían cohortes equivalentes si una orden cruza de año; no forzar igualdad anual. Eventos ignorados no reaparecen al quedarflat ni renuevan deadline.

El smoke tuvo125340callbacks frente129600minutos del trimestre nominal. No hay causa verificada para ese inicio/cobertura efectivos: no atribuirlo a SPY,feriado o error de precio sin evidencia. El full muestra cobertura exacta propia; no se proyecta al smoke una explicación inventada.

## Decisión y límites

**Rechazar esta receta.** Con ejecución/cobertura válidas, los shorts pierden antes y después de fees, el retorno conjunto cae y la regularidad empeora. No sustituye referencia ni alcanza objetivo. No se hace grid de amplitudδ,ATR,STOP,inicialización,timeout ni ventanas para rescatarla; no hacen falta nuevas corridas de costes para descartar este resultado.

El fallo no invalida toda representación por eventos ni demuestra que la referencia esté validada por sobrevivir. Es una formulación adaptativa dentro de desarrollo ya observado; no edge independiente ni OOS. La fuente ejecutada, protocolo y descarte se conservan. Root gestiona notas UI y registro agregado. Este cierre sólo guarda el informe propio: sin cambios de alpha, nuevas fuentes, scripts ni simulaciones.
