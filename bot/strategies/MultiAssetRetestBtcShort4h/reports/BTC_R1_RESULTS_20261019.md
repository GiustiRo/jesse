# BTC R1 — resultados auditados — 2026-10-19

Encontramos **un candidato de investigación: BtcExploreR103**, probado en B y C. Mejora beneficio y CAGR en la muestra reutilizada de desarrollo y conserva una ventaja neta bajo costes adicionales. Su regularidad mensual/trimestral **no resiste +5bps RT**, por lo que no se promueve ni se declara cumplido el objetivo de robustez. Las otras ocho hipótesis no ofrecen una mejora conjunta; algunas reducen DD a cambio de rendimiento o regularidad.

## Contrato y ejecución

Tres agentes nuevos: selecciónshort, gestiónshort y mecanismos alternativos. Tres hipótesis distintas por agente, evaluadas por separado, cada una en B y C: **18 full backtests finished sin errores**, en pares B/C simultáneos, máximo4global. Nueve reglas congeladas antes de implementar; raíz leyó fuentes antes de tickets. No grid, combinaciones, rescates de ceros, ni segunda ronda automática.

2020-10-15→2025-12-31 **exclusivo** (último día de datos2025-12-30); 2026 cerrado. 10000USDT compartidos, riesgo1%trade/8%agregado, isolated5x, capnocional4.4, fee.00045lado para todos los tipos, reserve.001 sólo sizing. 4h/240warmup, M1auxiliares BTC/PAXG/SPY, debugtrue/fastfalse. PAXG/SPY congelados y proxies aceptados. Sin funding ni datos nuevos. Comparación con controles **1%**, no cartera histórica3%.

Controles: [B](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f), SPYSecond; [C](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835), SPYMarket. PAXGMarket y BTCbase iguales. B/C comparten muestra y mecanismo BTC: no son dos validaciones independientes.

Root verificó18formularios y54snapshots de fuentes3rutas, todos exactos a versiones congeladas. Cuatro originales re-leídos intactos. Sólo un comentario heredado sobre persistencia de logs se corrigió después en las tres copias Entry; executable inalterado, snapshots conservados y reversión byte-exacta verificada. QA sintética229checks PASS, más auditorías de órdenes reales Payoff sin violaciones detectadas. Estas QA prueban implementación/cronología, no capacidad predictiva.

## Matriz completa

Neto y estrés expresados en USDT sobre cuenta inicial10k; M=meses positivos/meses activos, Q=trimestres positivos/todos. Completo=61meses calendario/19Q; conparciales=63meses/21Q. Los meses inactivos se muestran además abajo y en auditorías exactas. DDmotor negativo. +10 es coste adicional estático de10bps RT sobre mismos fills y cantidades, sin reejecución ni sizing adaptado.

| Hipótesis/cartera | N | Neto | Δnet vscontrol | CAGR | DDmotor | Mcompletos | Qcompletos | Mconparciales | Qconparciales | Neto+10bps |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [E01B](http://localhost:9200/#/backtest/9de1ae4d-ef15-4d8f-9022-20ee1a830ec6) | 202 | 8869.03 | -365.17 | 12.95% | -7.51% | 36/57 | 15/19 | 36/59 | 16/21 | 7411.31 |
| [E01C](http://localhost:9200/#/backtest/1a62497a-7609-4bfd-9153-15c8640cf67a) | 209 | 9028.42 | -379.41 | 13.13% | -8.17% | 37/57 | 16/19 | 37/59 | 17/21 | 7469.53 |
| [E02B](http://localhost:9200/#/backtest/97d654d0-5917-4a26-b151-11ef396591e6) | 143 | 7157.31 | -2076.89 | 10.91% | -9.47% | 30/54 | 14/19 | 30/56 | 15/21 | 6116.78 |
| [E02C](http://localhost:9200/#/backtest/a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3) | 150 | 7323.18 | -2084.64 | 11.11% | -9.15% | 31/54 | 15/19 | 31/56 | 16/21 | 6187.91 |
| [E03B](http://localhost:9200/#/backtest/20ca6dae-a6c9-44ed-8349-5877e2d3827c) | 125 | 7628.67 | -1605.52 | 11.49% | -6.20% | 36/55 | 16/19 | 36/57 | 17/21 | 6566.63 |
| [E03C](http://localhost:9200/#/backtest/f551da25-c6c9-4a31-8ad9-7fc4f71ad823) | 132 | 7791.00 | -1616.83 | 11.68% | -6.92% | 34/55 | 16/19 | 34/57 | 17/21 | 6628.70 |
| [P01B](http://localhost:9200/#/backtest/17867dbb-3676-46e9-a427-d60694384528) | 208 | 9186.89 | -47.30 | 13.31% | -6.98% | 39/57 | 15/19 | 39/59 | 16/21 | 7653.86 |
| [P01C](http://localhost:9200/#/backtest/dc50d6e4-8799-437a-8d1e-8b81e22cf8ee) | 215 | 9342.08 | -65.75 | 13.49% | -7.01% | 39/57 | 14/19 | 39/59 | 15/21 | 7705.32 |
| [P02B](http://localhost:9200/#/backtest/85a2fe07-0f26-4271-88d0-4ebdcd8814f1) | 207 | 8658.49 | -575.71 | 12.71% | -7.87% | 37/57 | 15/19 | 37/59 | 16/21 | 7175.90 |
| [P02C](http://localhost:9200/#/backtest/b91112c0-e3f3-4c31-8dea-abf184cf2d40) | 214 | 8829.62 | -578.21 | 12.91% | -8.72% | 38/57 | 15/19 | 38/59 | 16/21 | 7247.12 |
| [P03B](http://localhost:9200/#/backtest/6eea0aa5-84fa-45b1-9e44-86d1e2c29a18) | 211 | 7599.73 | -1634.46 | 11.45% | -6.74% | 35/57 | 12/19 | 35/59 | 13/21 | 6122.93 |
| [P03C](http://localhost:9200/#/backtest/5652bfcb-64b2-4131-a757-3c5fcde4f886) | 218 | 7761.18 | -1646.64 | 11.65% | -6.74% | 35/57 | 14/19 | 35/59 | 15/21 | 6185.94 |
| [X01B](http://localhost:9200/#/backtest/77a80211-701a-4af4-9fb6-b77130b7b4c8) | 206 | 9234.19 | 0.00 | 13.37% | -7.50% | 37/57 | 16/19 | 37/59 | 17/21 | 7720.95 |
| [X01C](http://localhost:9200/#/backtest/9b5cbe51-91ee-4361-b080-c28c0cd38fdb) | 213 | 9407.83 | 0.00 | 13.56% | -8.17% | 38/57 | 16/19 | 38/59 | 17/21 | 7792.53 |
| [X02B](http://localhost:9200/#/backtest/56c48468-10dd-489e-b921-fa948dbd34ae) | 177 | 6279.08 | -2955.11 | 9.80% | -12.85% | 32/58 | 14/19 | 32/60 | 15/21 | 5176.79 |
| [X02C](http://localhost:9200/#/backtest/dd5b6e8d-6207-4e01-9bce-8a18c5d416e4) | 184 | 6418.73 | -2989.09 | 9.98% | -9.55% | 34/59 | 15/19 | 34/61 | 16/21 | 5222.25 |
| [X03B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127) | 273 | 11964.24 | 2730.04 | 16.29% | -8.25% | 41/61 | 16/19 | 41/63 | 17/21 | 9878.12 |
| [X03C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c) | 280 | 12135.88 | 2728.05 | 16.46% | -9.01% | 42/61 | 16/19 | 42/63 | 17/21 | 9942.01 |

### Lectura de las nueve hipótesis

- E01 Volumen direccional24h: pierde365–379USDT y regularidad. Shorts121; gate retiene120entradas de125, desplaza5 y habilita1distinta por ocupación. No mejora.
- E02 Caída distribuida sin vela dominante: shorts62, neto propio negativo y pérdida incluso antes de fees en ambas. La caída distribuida que selecciona no conserva el edge observado. No generalizar esta conclusión a todas las tendencias BTC.
- E03 Target sobre mínimo previo5d: reduceDD a6.20%/6.92%, pero pierde1606–1617USDT vscontrol; quedan44shorts con neto y bruto negativos. B pasa65% sólo con meses completos; conparciales36/57=63.16%; C falla ambas. No aceptación por redondeo.
- P01 Stopshort EMA20 descendente: DD6.98%/7.01% y39/57meses positivos; Q15/19B y14/19C, ambos bajo80%. Tradeoff útil para diagnóstico, sin promoción.
- P02 BEfee tras medio target: neto yDD peores.22latches/stopupdates, sólo4stopsBE modificados finalmente ejecutados por cartera. Shorts+10bps apenas104.90/87.41USDT.
- P03 Salida RSI3neutral: DDmenor pero shorts netos25.98/18.32, convertidos en −715.81/−724.74USDT con+10bps; regularidad peor.
- X01 Long tras shock/rechazo/recuperación: cero eventos elegibles completos contados, cero fills suplementarios; reproduce exactamente economía de controles. Los contadores no distinguen causas del cero. No relajar parámetros.
- X02 Sustituirshort por semivarianza persistente: sustituye los125shorts originales por96nuevos; neto−1319.89/−1324.64 y bruto negativo. Regla de varianza no aporta aquí.
- X03 Shortsuplementario desacuerdo precio/volumen+VWAP: candidato detallado a continuación.

## Candidato X03: qué hace

Mantiene runners long originales y prioridad de planes originales. Añade short tras dos barras cerradas:
1. En s=t−1, precio por encima del de12barras atrás, pero suma negativa de volumen ponderado por ubicación del cierre en el rango. q=V(2C−H−L)/(H−L), cero si rango0. Es proxy OHLCV, no flujo agresor observado.
2. Cierre_s>=VWAP12_s (HLC3); en t, vela bajista y cierre<VWAP12_s congelada al origen.
3. Primer false→true del setup completo, estado avanza aunque ocupado; MARKET al cierre, stop max(high_s,high_t)+.25ATR, distancia1..3ATR, TP2R, timeout48h. Sin trailing/BE ni cola retrospectiva.

No se eligieron12/2R/48h después del resultado. Fuente causal revisada y QA de estado antes de ejecución. Mantenerla congelada para validación posterior.

### Comparación nominal y denominadores

| Cartera | Neto | CAGR | PFtrades | Sharpe | DDmotor | Mfull activos | Mfull todos | Mparciales activos | Mparciales todos | Qfull | Qparciales |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bcontrol | 9234.19 | 13.37% | 1.796 | 1.324 | -7.50% | 37/57 (64.91%) | 37/61 | 37/59 (62.71%) | 37/63 | 16/19 | 17/21 |
| X03B | 11964.24 | 16.29% | 1.760 | 1.491 | -8.25% | 41/61 (67.21%) | 41/61 | 41/63 (65.08%) | 41/63 | 16/19 | 17/21 |
| Ccontrol | 9407.83 | 13.56% | 1.776 | 1.315 | -8.17% | 38/57 (66.67%) | 38/61 | 38/59 (64.41%) | 38/63 | 16/19 | 17/21 |
| X03C | 12135.88 | 16.46% | 1.745 | 1.480 | -9.01% | 42/61 (68.85%) | 42/61 | 42/63 (66.67%) | 42/63 | 16/19 | 17/21 |

Con fee base, X03 cumple65%meses activos y80%Q tanto completos como incluyendo parciales. B está sólo41/63=65.0794%, margen estrecho. El objetivo aspiracional70%meses y20–30%CAGR sigue sin alcanzarse. DD bajo25% en todos estos runs, pero X03 lo empeora frente a sus controles; no domina todas las dimensiones.

### Aporte, ocupación y concentración

- Cada X03 tiene79shorts suplementarios MARKET y113shorts originales STOP, total192shorts vs125control: **67más netos**, no79más netos. Se retienen112entradas shortbase, se desplazan13 y aparece1entrada original diferente. Los31long BTC conservan todos sus horarios de entrada y salida; las cantidades yPNL cambian con el capital.
- Neto suplemento:2107.76B/2087.17C, fees465.82/464.40. Con+10bps:1590.19/1571.17. Excluyendo3mejores suplementos:1069.65/1033.94; además+10bps:578.67/544.93. No depende sólo de sus3mejores trades.
- Aproximadamente80% del neto suplementario procede de2022+2025;2024 y el parcial2020 son negativos. Cuatro años completos positivos antes y después de+10bps, con2023 muy pequeño después de estrés. No presentar estabilidad uniforme ni años como OOS.
- Incremento neto de cartera2730.04B/2728.05C. Atribución cerrada BTC+2406.80/+2375.46, PAXG+187.56/+190.42, SPY+135.69/+162.17. La mejora de otras patas refleja sizing/capital endógenos; no es nueva señal en ellas.
- Tiempo con alguna posición:34.49→38.52%B y36.96→40.85%C. Notional×time/equityinicial:.3620→.4224B y.4118→.4763C. Más actividad/exposición bajo mismos límites; no afirmar igual camino económico o beneficio fijo por trade.
- Fees totales1361.92→1877.50B y1453.77→1974.48C; PF baja1.796→1.760B y1.776→1.745C aunque Sharpe sube. El mejor neto convive con costes yDD mayores.
- Excluir3mejores trades de cartera deja7640.01B/7807.60C; además+10bps deja5589.09/5649.10, vs3794.72/3859.92en controles. Eliminaciones mantienen resto de fills/cantidades; no son replay de capital.
- Peor Qnominal X03−3.9043%B/−4.7159%C, peores que controles−2.9682%/−3.8299%. DDdayclose−8.3135%/−9.0683% difiere del DDmotor−8.2540%/−9.0094%; no mezclarlos.
- Co-loss en61meses completos BTC/PAXG3, BTC/SPY0B/2C, PAXG/SPY0B/2C. Son descripciones de muestra reutilizada, sin inferir diversificación futura. Episodio DDdayclose2021-03-13→2021-06-17: BTC−770.17/PAXG−207.31/SPY0B; BTC−755.66/PAXG−204.50/SPY−95.96C.

## Validación adicional: regularidad bajo fricción

Se reconstruyó otra vez MTM por fill con+5/+10bps RT de coste proporcional adicional aplicado en sus timestamps, cantidades y precios congelados. No nuevos backtests ni modelo de ejecución, spread, gaps, latencia, funding o resizing. Las curvas no heredan el CAGRmotor nominal: CAGRoverlay se calcula de equity final estresada. B/Cbase yX03 se someten al mismo procedimiento.

| Cartera | Coste extraRT | Neto | Mfull | Qfull | Mparciales | Qparciales |
|---|---:|---:|---:|---:|---:|---:|
| B | 0bps | 9234.19 | 37/57 | 16/19 | 37/59 | 17/21 |
| B | 5bps | 8477.57 | 36/57 | 13/19 | 36/59 | 14/21 |
| B | 10bps | 7720.95 | 36/57 | 13/19 | 36/59 | 14/21 |
| C | 0bps | 9407.83 | 38/57 | 16/19 | 38/59 | 17/21 |
| C | 5bps | 8600.18 | 38/57 | 15/19 | 38/59 | 16/21 |
| C | 10bps | 7792.53 | 38/57 | 15/19 | 38/59 | 16/21 |
| X03B | 0bps | 11964.24 | 41/61 | 16/19 | 41/63 | 17/21 |
| X03B | 5bps | 10921.18 | 40/61 | 15/19 | 40/63 | 16/21 |
| X03B | 10bps | 9878.12 | 37/61 | 14/19 | 37/63 | 15/21 |
| X03C | 0bps | 12135.88 | 42/61 | 16/19 | 42/63 | 17/21 |
| X03C | 5bps | 11038.94 | 40/61 | 15/19 | 40/63 | 16/21 |
| X03C | 10bps | 9942.01 | 38/61 | 15/19 | 38/63 | 16/21 |

La ventaja de neto persiste:+10bps X03−control=+2157.17B/+2149.48C. **La regularidad objetivo no es robusta**: con+5bps, X03 queda40/63=63.49%meses y16/21=76.19%Q incluyendo parciales; incluso con periodos completos Q15/19=78.95%. Con+10bps X03C tiene38/61meses completos y38/63conparciales. Los controles también fallan parte de estos objetivos bajo coste extra. Beneficio resistente a un overlay de coste no equivale a regularidad resistente.

Meses pequeños que cambian signo están documentados en el informe de costes: X03C con+5bps noviembre2020 yseptiembre2025; con+10bps también marzo2023 yjulio2025. No modificar reglas para eliminar esos meses.

## Decisión y límite de evidencia

**Conservar X03B yX03C como candidatos congelados de desarrollo**, con B como variante de menorDD y C como variante de algo más beneficio/meses nominales. No elegir C sólo por máximo neto: ventajaC−B nominal171.64USDT y con+10bps63.89USDT, a cambio de másDD. Sin combinación conEMA20 ni otros filtros en esta ronda.

Las ocho alternativas se archivan o se conservan como tradeoffs diagnósticos descritos, no como promociones. No avanzar a despliegue ni declarar la cartera robustamente validada. Muestra2020–2025 intensamente reutilizada, selección entre9nuevas y muchas recetas anteriores, B/C no independientes,79suplementos, concentración temporal importante. Que sobreviva ex3 y coste adicional no corrige selección múltiple ni prueba edge fuera de muestra.2026 permanece cerrado.

Siguiente trabajo acotado sugerido: someter X03sin cambiar sus reglas a validación temporal y ejecución más realista, con criterios congelados; controlar estabilidad alrededor de ventanas/TP/timeout como sensibilidad, sin elegir el mejor vecino. Cualquier tramo reservado requiere acordar su apertura antes de consultarlo. Esta ronda finaliza sin nuevas pruebas económicas adaptativas.

## Evidencia persistida y reproducción

Todos los archivos siguientes están dentro del proyecto Jesse en la máquina que ejecuta Jesse, bajo strategies/MultiAssetRetestBtcShort4h/reports/:
- BTC_R1_FROZEN_PROTOCOL_20261019.md
- BTC_R1_ROOT_SOURCE_REVIEW_20261019.md
- BTC_R1_SESSION_REGISTRY_20261019.md (18dashboardlinks y checks)
- BTC_R1_AUDIT_BATCH1_20261019.md, BATCH2 yBATCH3 (fills/MTM/stress/rutas/co-loss/cohortes/path)
- BTC_R1_AUDITOR_SOURCE_20261019.md (código inline run_analysis)
- BTC_R1_COST_CALENDAR_20261019.md y BTC_R1_COST_CALENDAR_SOURCE_20261019.md
- PHASE2_HANDOFF_BTC_R1_20261019.md

Auditorías principales: ad66331f9c894766a156a4b6cd75d216, 831bac3de3cb4ff1953bd28756787b33, 46f434f9e40d46289f61102144344722; coste calendario:b103dc4be3a245e4a4c0f1b135b9a91b. QAExplore128checks job135ee4ae7efb43a6b12555be15de34b6; Payoff101checks1a560d1ce7e840f39c8fa5aa73fdef1b, P01órdenes6206e139bf2c40c9a706512b1773e76a, P02/P03órdenesf48bbd1e42684a9e8c00a2074f499bb9. Informes de cada agente bajo sus respectivas clases y referencias en registry. Las QA con stubs no recalculan indicadores históricos; snapshots de trades sólo contienen órdenes ejecutadas, no historial de modificaciones/cancelaciones. No se afirma revisión individual de379ratchets cancelados.

Contadores de capacidad: no se registran intentos con capacidad0, lotround0 o restricción de margen/riesgoagregado; sí recortes de tamaño por roomnocional/cuota de volatilidad. Se observan sólo planes que llegan a sizing, no señales mientras ocupado. events_occupied mide estado en before, no rechazos: el motor puede cerrar y reentrar con señal fresca en la misma barra. Cierres forzados al límite temporal conciliados porfills/fees/wallet; contador preterminaciónopen1 no es posición residual ni prueba de liquidez nativa al último precio.

## Revisión independiente final
El agente Entry leyó el informe completo sin nuevos datos, jobs ni backtests. Corrigió la expresión «hipótesis independientes» para evitar sugerir independencia estadística; se evalúan por separado, pero comparten muestra y base. No detectó errores materiales en denominadores, aritmética, conteos de desplazamiento o decisión. Root incorporó la corrección. Todos los18backtests y todos los análisis de esta ronda concluyeron; no queda proceso de investigación pendiente.
