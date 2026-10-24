# Calendario semanal BTC — comparación final cerrada

[Candidata sábado–lunes](http://localhost:9200/#/backtest/b3157b7b-1745-4e0a-8314-77205763f58c) · [Control martes–jueves, no seleccionable](http://localhost:9200/#/backtest/dd37b90d-f28b-460d-9354-81122f7a4b0b) · [Referencia congelada](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

**Candidata descartada; control no promovido.** Ventana2020-10-15→2025-12-31exclusivo, normal/debug, tres rutas4h y auxiliarBTC1m para frescura. Capital10000USDT,5xaislado,fees0,00045porlado todas órdenes. 2026 permanece reservado.

## Contrato que se probó
Clones completos de referencia: primero planes originales long y short; sóloflat/sinplanoriginal en slotUTC00, suplemento long con EMA20>EMA80>EMA80[-5] yclose>EMA80. Stop fijo2ATR14 desdefill, riesgo máximo1% y caps originales3%/8%/4,4x para el conjunto; MARKET y deadline señal+48h, stop siempre activo.

Candidata sábado00→lunes00; control martes00→jueves00 fijado antes de resultados y **no seleccionable como ganador alternativo**. Los días no se barrieron. El borrador inicial de control miércoles→viernes se sustituyó por decisión root antes de código/consultarretornos; no fue elección por rendimiento.

Se conservan reglas/prioridad originales, no sus futuras entradas ni cantidades: la ocupaciónBTC bloquea oportunidades posteriores y el capital compartido afecta otras patas. La comparación calendario/beta es descriptiva con estado de cuenta endógeno, no causalidad pura de estacionalidad.

## Cuenta completa

| Medida | Referencia | Candidata | Control |
|---|---:|---:|---:|
| CAGR |28,8294%|23,254926%|30,629469%|
| DD motor |−14,8905%|−14,722209%|−16,490738%|
| Neto USDT |27461,46|19745,835839|30272,040985|
| Fees USDT |—|3981,314336|5360,317581|
| Trades long/short |97/123|176/119|186/112|
| Duración de ejecución |—|292,14s|286,36s|

La candidata reduce sustancialmente retorno y beneficio conjunto, pese a suplemento positivo. El control elevaCAGR pero empeoraDD y no supera regularidad; no se selecciona por descarte.

## V4 MTM y calendario

| Medida | Candidata | Control |
|---|---:|---:|
| Meses activos positivos |34/61=55,7377%|33/62=53,2258%|
| Meses positivos sobre63calendario |34/63=53,9683%|33/63=52,3810%|
| Trimestres positivos |14/21=66,6667%|14/21=66,6667%|
| Meses activos completos |34/59|32/60|
| Meses calendario completos |34/61|32/61|
| Trimestres completos |13/19|13/19|
| Meses rescatados/perjudicados vs referencia |3/2|4/4|

Referencia33/61activos,33/63todos,15/21trimestres; completos33/59activos y14/19trimestres. El mes neto extra de la candidata no compensa pérdida de trimestres ni rentabilidad. No se cambian65–70%/80%/DD25% ni denominadores; todas las métricas siguen siendo desarrollo ampliamente observado.

## Atribución del suplemento

| Leg añadido | Sábado–lunes | Martes–jueves |
|---|---:|---:|
| Operaciones |81|95|
| Neto USDT |747,794704|283,291325|
| Fees USDT |376,496926|733,861167|
| Ganadoras |42|39|
| Horas acumuladas de posición |3748,4833h|3400,6h|
| Salidas MARKET al deadline |71|50|
| Salidas STOP |10|45|

El mayor neto propio del fin de semana no demuestra una prima causal estable: cambian admisiones,exposición,precios,tamaños y oportunidades de cuenta. Un suplemento positivo puede reducir la cuenta combinada mediante sustitución de señales y trayectoria de capital; no atribuir toda diferencia dólar por dólar a una sola causa sin contrafactuales.

Todos los fills del suplemento sonMARKET con created=executed=opened yslotexacto. SalidasMARKET coinciden condeadline48h;STOPocurre a/beforedeadline. Ambos legs terminaronflat: **no ocurrió cierre sintético terminalBTC**. La posibilidad prevista para martes30Dic no se presenta como hecho ocurrido ni fallo48h.

## Logs preterminal y poblaciones
Leídos directamente con get_session_results/logs. Candidata: slots272,occupied51,pending2,baseline_priority3,evaluated218,regime_rejected136,risk_rejected1,plans/fills/closed81,time_exits71. Control: slots272,occupied41,pending4,baseline_priority6,evaluated226,regime_rejected130,risk_rejected1,plans/fills/closed95,time_exits50.

Ambos: delayed_fills0,delayed_time_exits0,stale_entry_quotes0,deferred_exit_quotes0. Son **counts_preterminal**, no totales garantizados después de liquidación terminal. Evaluated reconcilia136+1+81=218 y130+1+95=226. Slots/occupied/pending/baseline_priority/evaluated no son una partición aditiva observada; no sumar categorías ni inventar causa del solapamiento.

## Corrección del auditor, sin modificación de estrategia
El primer análisis a4c07e227e9c4d8183029236090532e5 falló un assert de clasificación ingenua: **MARKET por sí solo no identifica el suplemento**, porque el baseline también registra4entradasMARKET fuera del slot en cada sesión. No fue un fallo de estrategia ni razón para resimular.

El análisis final **6767173c23d84f06bb9f7af287b9ab6f succeeded** clasifica con MARKET+slotexacto y concilia81/95 con counters. V4 reconcilió fills,fees,wallet yMTM; la atribución anterior procede de esa clasificación corregida. No se alteraron fuentes, órdenes, resultados ni métricas para pasar el auditor.

## Decisión operativa
Cerrar esta comparación. La candidata no mejora objetivos conjuntos frente a referencia; el control no habilita promover martes ni probar otros días. No nuevas variantes,horas,EMA,stops,riesgo o runs. Conservar los resultados positivos del leg y negativos de integración: no esconder ninguno.

Posible estancamiento local reconocido: diagnóstico de cartera antes de elegir otra familia, manteniendo la referencia y2026 intactos. No se prueban nuevas fuentes ni se crean scripts/framework/live. Este informe es el único cambio del cierre; root mantiene notasUI y agregado.
