# BTC: diez pruebas nuevas cerradas, objetivo todavía pendiente

Se completaron las tandas E–I con reglas y presupuestos previos. Las diez políticas incumplen los objetivos. El resultado de participación secuencial tiene, además, una sola operación y no permite estimar una ventaja. La investigación autónoma continúa; este cierre conserva evidencia y no promueve ninguna estrategia.

## Resultados

| Prueba | CAGR neto base | Caída máxima M1 y ejecuciones | PF neto | Meses activos positivos | Trimestres positivos | Operaciones |
|---|---:|---:|---:|---:|---:|---:|
| E · [Nivel latente (Kalman)](http://localhost:9200/#/backtest/9a7ce958-13d0-481e-992d-401e03b579fd) | -13.35% | 62.82% | 0.894 | 25/62 | 8/20 | 1200 |
| E · [Recuperación de excursiones](http://localhost:9200/#/backtest/ce148b26-9a50-4ef9-9874-a784a9067c4e) | 2.89% | 16.78% | 1.092 | 34/60 | 11/20 | 167 |
| F · [Saltos: reversión](http://localhost:9200/#/backtest/80fa4bf7-d510-4c9a-967c-88b75cc49752) | -22.10% | 74.20% | 0.668 | 18/62 | 4/20 | 382 |
| F · [Saltos: continuación](http://localhost:9200/#/backtest/8b78a705-a8f3-4656-9705-e56300623ddf) | 13.16% | 24.24% | 1.256 | 32/62 | 13/20 | 381 |
| G · [Autorregresión AR1](http://localhost:9200/#/backtest/c72b53d8-c986-4131-814b-788cdc0f49e2) | -7.44% | 62.04% | 0.969 | 27/62 | 8/20 | 1481 |
| G · [Control de deriva media](http://localhost:9200/#/backtest/cbfafdb4-ea81-48f7-bd40-5ade91a3bfa4) | -3.62% | 56.12% | 0.983 | 26/62 | 8/20 | 1355 |
| H · [Mechas de rechazo](http://localhost:9200/#/backtest/77ec643b-9761-492d-aca0-01681e0cd203) | 5.56% | 20.07% | 1.217 | 34/61 | 14/20 | 193 |
| H · [Control de localización del cierre](http://localhost:9200/#/backtest/658d7534-0034-49f3-8f12-f3271002b2f7) | 5.49% | 18.44% | 1.112 | 38/62 | 10/20 | 297 |
| I · [Participación secuencial](http://localhost:9200/#/backtest/17494d8a-eaf8-437e-8b7d-fac709a8d092) | -0.39% | 2.50% | 0.000 | 0/1 | 0/20 | 1 |
| I · [Control de reparación de precios](http://localhost:9200/#/backtest/a091d445-a502-4214-b153-182eb3d2af8d) | -3.68% | 39.87% | 0.869 | 22/56 | 9/20 | 121 |

Ventana común: 2020-10-15 inclusivo a 2026-01-01 exclusivo. Cinco años completos más 2020 parcial, ya examinados: desarrollo reutilizado, no validación independiente. Capital virtual 10.000 USDT por política; riesgo objetivo 2% por trade, límite agregado 6% y 3x aislado. Comisiones 0,00045 por lado, taker con descuento según supuesto confirmado; funding histórico aplicado y verificado, con marcas proxy declaradas; slippage modelado cero. No se ejecutaron estrés de costos, variantes de riesgo ni pruebas económicas nuevas de 2026.

## Decisiones obtenidas

**E — Exceso y recuperación.** El modelo de nivel latente perdió y la recuperación de excursiones ganó sólo 2,89% anual. Son transferencias explícitas desde antecedentes PAXG, con contrato BTC declarado; no mecanismos inventados ni extrapolaciones de cifras entre activos. Cerrar ambas sin rescatar ventanas, lados o coeficientes.

**F — Revertir o seguir un desplazamiento concentrado.** Continuación superó claramente a reversión, con 13,16% anual y PF 1,256. Aun así, sus 32/62 meses y 13/20 trimestres positivos no cumplen la regularidad y su retorno no alcanza 30%. La descomposición RV/BV sobre 24 incrementos horarios es una heurística de trayectoria, no un test estadístico certificado de saltos. El comparador favorable no sustituye las puertas absolutas.

**G — Dependencia de retornos frente a deriva.** El AR1 perdió y empeoró al control de media reciente. Ambos usaron el mismo entrenamiento causal de 240 pares ya observados, horizonte de seis pasos y umbral. No se seleccionó retrospectivamente sólo el lado largo o un signo de beta. Sin barrer ventanas o coeficientes después del fallo.

**H — Mechas frente a cierres.** Ambos obtuvieron cerca de 5,5% anual. Mechas alcanzó PF 1,217 y 14/20 trimestres positivos, todavía por debajo de la regularidad y del retorno exigidos. Su caída M1 de 20,07% supera ligeramente el objetivo informativo de 20%, aunque respeta el techo de 25%. El control de cierre consiguió 38/62 meses positivos, 61,29%, por debajo de 65%. No combinar retrospectivamente los dos para rescatar H.

**I — Porción creativa.** Se registró la secuencia impulso con volumen bajo → recuperación con participación normal, contrastada contra el mismo patrón de precios sin ese filtro. La normalización usa 28 días anteriores del mismo bloque UTC, todos conocidos antes del impulso. PHASE produjo sólo una operación; PRICE tuvo 121 y perdió. No hay evidencia suficiente para atribuir una ventaja al filtro, y el control tampoco es candidata. Cerrar esa formulación sin suavizarla tras observar su escasez.

Antes de E se retiró por duplicación la propuesta genérica de falso rompimiento de rango y regreso al centro: ya existía en OrchLateralFailedRange4h y sus continuaciones. Esta retirada no cuenta como backtest ni rechazo económico nuevo.

## Puertas y medición

Todas fallan CAGR mínimo 30%, 65% de meses completos activos positivos y 80% de trimestres completos positivos. Las aspiraciones de 40–50%+ y 70% mensual se conservan. PF mínimo 1,2; caída máxima permitida 25% con objetivo 20%; mediana mensual calendario positiva incluyendo inactivos; resultado aritmético positivo al quitar los dos mejores meses. N≥100 es un umbral preliminar operativo, no potencia ni confianza estadística. Las puertas completas por política están en RESULTS.json, con medianas y concentración.

Cada política registró 2.741.760 marcas M1 más ejecuciones, 63 intervalos mensuales contiguos, 62 meses completos y 20 trimestres completos. Se verificaron fronteras, unicidad, equity final y suma de contribuciones. No hubo ventanas de señal inválidas. Equity es wallet más PnL abierto, sin multiplicarlo otra vez por apalancamiento.

DD representa muestras M1 y eventos de ejecución, no todos los extremos dentro del minuto. Las fronteras mensuales siguen el contrato R11: 00:00 UTC después del funding efectivo y antes de nuevas decisiones. El pago en esa frontera pertenece al intervalo que termina según esta convención por fase; no equivale a agrupar todos los eventos en meses civiles estrictamente [inicio,fin).

## Auditoría y trazabilidad

Se auditaron 5578 registros de operaciones entre diez políticas alternativas. Es un recuento contable, no una muestra de operaciones independientes. En todas, PnL bruto − comisiones + funding = suma del PnL de trades = equity final − 10.000, error menor a 1e−6 USDT. Funding aplicado y dataset fijo verificados. Los contadores de posiciones abiertas preterminales se conservaron como metadata: los resúmenes FINAL y snapshots incluyen la liquidación del motor y sus fees; no son posiciones reales activas.

Análisis completos: E 4eb2134c9dd34ca88619b96843619adf; F f1aa6ed658934d40b573af21da372858; G f54b317db242406da4d9f5c6e544cb67; H 4a5ae769d6c443a691a291bd398cee02; I c330fae100fc4c0bbd271a07bee69348. Todos terminaron correctamente. Checks sintéticos y revisión separada precedieron a cada tanda. El primer harness E corrigió una igualdad exacta exp(logprecio) a tolerancia; se retiró una guarda ficticia de objetivo 2R para Kalman antes de economía y se volvió a verificar. Cero backtests técnicos, errores económicos o reemplazos en E–I.

Protocolos, manifiestos con fuentes/configuración y hashes, auditorías y telemetrías completas se conservan como BTC_DISCOVERY_E… I en reports/. Los informes individuales también se guardaron en cada estrategia. No se modificó el framework ni la configuración global.

## Continuidad autónoma

Desde r9 se completaron 17 corridas económicas nuevas: A/B tres, C/D cuatro y E–I diez. El bloque V1–V6 mantiene su conteo histórico de 209; no es censo global ni se convierte en muestras independientes al añadir estas pruebas. Toda selección posterior debe reconocer el histórico ampliamente examinado.

El usuario pidió continuar sin detener la investigación al cerrar una pregunta. Ese permiso sigue vigente. La siguiente línea en revisión es información ETH→BTC con ETH sólo como dato, frente a control definido exclusivamente con BTC; no una cartera ni una recuperación del par residual ORCH eliminando una pata. Antes de ejecutar requiere comparación exacta con antecedentes, reglas y presupuesto propios. Mientras no se registre, es propuesta, no experimento iniciado.

Mantener BTC individual, riesgo/costos acordados y creatividad con hipótesis falsables. No rescatar vecinos de E–I, bajar puertas o elevar exposición para fabricar el objetivo. Estrés queda condicionado a candidata y acuerdo conjunto. Paper/live, Pi y PAXG/SPY/cartera conservan sus autorizaciones separadas.
