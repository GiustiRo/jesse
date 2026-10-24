# BTC: cierre J–M

Siete nuevas políticas terminadas; ninguna cumple los objetivos r9. No hay candidata ni autorización operativa. Veinticuatro corridas económicas completadas desde r9 (A/B3+C/D4+E–I10+J–M7); no son muestras independientes. Los 209 casos V1–V6 se conservan como bloque histórico separado.

|Política|Trades|CAGR neto base|DD M1/eventos|PF|Meses activos +|Trimestres +|
|---|---:|---:|---:|---:|---:|---:|
|[Confirmación ETH](http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a)|225|-8.90%|44.24%|0.708|24/61|4/20|
|[Control BTC](http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0)|6808|-81.57%|99.99%|0.884|9/62|1/20|
|[Semivarianza](http://localhost:9200/#/backtest/823a2c19-0f0c-49f3-8ae8-8aeb34e2af66)|1|0.13%|0.93%|no estimable|1/1|1/20|
|[Rechazo 1000n](http://localhost:9200/#/backtest/431ae3a6-de3d-480c-a891-903804e5c655)|2198|-72.84%|99.90%|0.801|10/62|1/20|
|[Rechazo 1000n+500](http://localhost:9200/#/backtest/038b592a-dc86-4d81-b93f-16abf2fcae99)|1992|-68.09%|99.79%|0.821|14/62|0/20|
|[Geometría condicional](http://localhost:9200/#/backtest/d0f70f5f-e12d-400c-957a-59fb9112b3f6)|857|-16.25%|67.09%|0.857|17/58|6/20|
|[Respuesta global](http://localhost:9200/#/backtest/5a437423-be6d-4f13-a9de-32631ef3c66d)|361|-3.07%|34.18%|0.931|14/32|6/20|

## Lectura y decisiones

J: ETH como confirmación reduce actividad frente al control BTC, pero ambos pierden. El control tiene precio bruto positivo y costos superiores a esa ganancia; no se omiten comisiones. K: una operación ganadora no permite estimar ventaja ni PF sin pérdidas; falla CAGR, regularidad trimestral, mediana y concentración. L: ambos niveles nominales pierden también antes de costos; 1000n+500 sigue siendo un número redondo, no un control psicológico perfecto. M: la media condicionada por geometría y la global causal pierden; no se eligen bins, signos ni ventanas después de ver resultados.

Se cierran estas recetas y vecinos locales. No se retiran shorts ni se cambian riesgo/costos para rescatarlas. N estudia composición A/F y B/F con gestión original por origen, una sola posición BTC; el diagnóstico de tiempos standalone justifica probar capacidad conjunta, sin sumar curvas ni asumir diversificación.

## Contrato y límites

Ventana [2020-10-15,2026-01-01) UTC, desarrollo ya observado; sin nueva economía2026. Capital virtual10000, riesgo objetivo2%/límite agregado6%, aislado3x; taker .00045 por lado y funding histórico aplicado/verificado con proxies declarados, slippage modelado0. Neto significa esos costos modelados. Sin estrés hasta candidata y acuerdo conjunto.

Cada ledger completo reconcilia precio bruto−comisiones+funding=PnL=capital final−10000 con error<1e−6. Telemetría completa:2741760marcas M1,63meses/62completos,20trimestres, ventanas inválidas0; mediana calendario incluye meses inactivos. DD wallet+PnL abierto en M1 y ejecuciones, no extremos intraminuto. Frontera mensual post-funding/predecisión por fase; no intervalo contable estrictamente [inicio,fin). M condicional usa FINAL posterior a liquidación terminal, incluido costo de cierre. K PF null no equivale a infinito. Casos con capital casi agotado no acreditan paridad de mínimos nativos de la bolsa.

Fuentes, checks sintéticos, manifiestos previos, reportes individuales, recibos de contabilidad y telemetría se enlazan en revision.json y RESULTS.json. 12442 registros de operaciones entre políticas alternativas; no observaciones independientes. Sin fallos o reemplazos económicos ni backtests técnicos nuevos.
