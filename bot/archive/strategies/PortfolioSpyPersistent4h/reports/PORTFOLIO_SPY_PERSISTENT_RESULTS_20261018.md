# SPY01: participación persistente — resultado individual

Fecha: 18 de octubre de 2026. [Corrida SPY01](http://localhost:9200/#/backtest/3315ba00-2a40-4e8c-9b5a-690e1b4e5006). [Referencia inmutable](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

## Conclusión y alcance

La sustitución individual de la política SPY no reúne los objetivos. Mejora la cantidad de meses positivos y el CAGR de esta cuenta, pero empeora los trimestres, el drawdown y las pérdidas de los peores períodos. El componente SPY tiene un margen pequeño frente a costes adicionales. No se promueve esta variante individual.

Esto NO prejuzga la combinada11, predeclarada y en ejecución por root cuando se redacta este informe. Sus interacciones deben evaluarse con sus propios fills y MTM, sin sumar curvas ni modificar reglas tras SPY01. No se lanzó ninguna corrida adicional desde este agente.

SPY01 es una cuenta de tres activos: conserva BTC long/short y PAXG de referencia, y reemplaza sólo la entrada SPY por participación MARKET con pausa fija de168h tras cada cierre. No es un backtest aislado de SPY. Conserva protección, ATR, trailing, BE y presupuestos originales. Es un control económico de participación, no una nueva alpha ni cobertura anticíclica demostrada.

## Resultado de la cuenta

Corrida terminada sin excepción. Formulario común 2020-10-15→2025-12-31 exclusivo, modo normal, capital inicial10000, fee0.00045 por lado para todas las órdenes, isolated5x, límites originales3%/8% y gross4.4.2026 permanece sellado.

| Métrica | SPY01 |
|---|---:|
| Trades totales |314:189long y125short |
| Saldo final |39486.127438 |
| Neto |29486.127438 |
| Fees |8104.106552 |
| CAGR |30.136615% |
| DD del motor |−17.732683% |
| Sharpe |1.163531 |

El CAGR de referencia es28.8294% y su DD−14.8905%; el incremento de retorno no resuelve la regularidad.

Root V4 individual af6bb6056f5a43fc953224c729a4f9f0 succeeded, con contabilidad terminal y wallet reconciliados:
- 37/63 meses activos y calendario positivos:58.7302%.
- 13/21 trimestres positivos:61.9048%, frente15/21 de referencia.
- Períodos completos:37/61 meses y12/19 trimestres.
- Rescata10meses y perjudica6. Esto es clasificación descriptiva de resultados ya observados, no una selección de fechas negociables.
- Peor mes−9.19437%; peor trimestre−12.17653%.

Los objetivos65–70% de meses activos,80% de trimestres y DD≤25% siguen intactos. SPY01 no cumple los dos primeros y aumenta la adversidad de los peores períodos.

## Atribución observada

| Componente de la cuenta | Trades | Neto | Fees | PF |
|---|---:|---:|---:|---:|
| SPY long |123|4165.797456|4723.876116|1.112964|
| BTC long |31|14938.161511|—|—|
| BTC short |125|5230.897276|—|—|
| PAXG long |35|5151.271194|—|—|

Las reglas BTC/PAXG son idénticas, pero sus tamaños/resultados y el número de shorts pueden cambiar por capital compartido. El mayor CAGR no se atribuye exclusivamente al PnL SPY ni a diversificación independiente.

SPY genera8889.673572 de PnL de precio antes de sus fees, y4165.797456 después. Tiene48ganadores de123trades; el winrate no es criterio de promoción. Sus123trades, frente31SPY de referencia, muestran que la política aumenta considerablemente el turnover.

Concentración descriptiva de SPY:
| Ganancias mayores | Suma neta | % del neto SPY | % de suma de trades ganadores netos |
|---|---:|---:|---:|
|Top1|2981.077574|71.5608%|7.2633%|
|Top3|7454.777920|178.9520%|18.1633%|
|Top5|10823.560668|259.8197%|26.3712%|

Los porcentajes sobre neto pueden superar100% porque hay pérdidas compensatorias. No se retiró ningún trade ni se simuló una curva sin sus ganadores.

Holding SPY: mediana123.4h, media193.5359h y máximo870.1667h. Son duraciones reales entre fills, incluidas horas de fin de semana/cierre de fuente; no horas de cotización continua.

## Auditoría independiente de fuente, logs y órdenes

Sólo lecturas MCP y cálculos sobre sus resultados; ningún script, dataset o job nuevo.

Fuente actual19588caracteres, idéntica a la versión revisada antes del run, incluido searchsorted para seleccionar la M1 cerrada exacta T−60000 sin consultar OHLC de filas forming.

Lectura completa de23páginas de logs (hasta500entradas, respetando límite de tamaño API), conservando131renglones de telemetría relevantes;4páginas de trades para los314trades completos.

Comprobaciones sobre los123trades SPY:
- Cada fill tiene exactamente un log long_fill y una entrada ejecutada MARKET; una sola salida completa ejecutada. Precios y cantidades de logs/fills coinciden.
- Todas las entradas son lunes a viernes, a04/08/12/16UTC. Corresponden a barras de apertura00/04/08/12 y respetan el gate heredado, sin afirmar horario NYSE.
- En cada log quote_at=opened_at−60000; la fuente comprueba la frescura exacta y coincidencia de cierre. No se reconsultó el histórico M1 durante esta auditoría.
- En las122reentradas, previous_closed_at coincide exactamente con el closed_at REAL del trade SPY anterior. Todas esperan≥168h: mínimo168.1h y máximo229.6667h. El exceso refleja esperar el siguiente callback elegible, no acortar la pausa.
- Primera entrada2020-10-15T04:00UTC, sin cooldown artificial de startup.
- Las identidades de PnL por precio/cantidad/fee reconcilian. No apareció ninguna inconsistencia de los checks anteriores.

Contadores finales:
eligible_flat_callbacks2439 = cooldown_blocked2316 + fresh_quote123.
positive_plans123 = long_fills123.
full_closes122 antes de terminación →123 después de terminación.
No aparecen stale/missing/invalid quotes, zero_quantity o historia insuficiente; como los contadores son dispersos, ausencia significa cero.
Los resúmenes anuales se refieren al año del evento, no necesariamente al año de entrada de cada trade.

## Única salida terminal sintética

El motor conserva total_open_trades=1 y open_pl203.6286072 previos a su liquidación terminal. El trade final SPY abre2025-12-23T04:00UTC y tiene una salida ejecutada MARKET completa en2025-12-31T00:00UTC.

Gross203.6286072 menos fees totales de ese trade68.0299501 = net135.5986571, incluido en el saldo final. Los contadores pasan explícitamente de final_preterminal_close122 a final_after_terminal_close123, con terminal_full_closes1.

El contador previo no significa una posición residual sin cerrar. Tampoco la salida sintética demuestra una cotización fresca ejecutable a00UTC: es la convención de fin de muestra heredada. Root V4 la reconcilió con fills, gross y wallet; no se editaron métricas ni se adelantó el cierre con conocimiento del final.

Salidas SPY:122STOP —incluye stops con ganancia por trailing— y1MARKET terminal. No hay TP, rebalanceo mensual, cierres calendarizados, parciales ni piramidado.

## Sensibilidad aritmética de costes y límites

Diagnóstico de cantidades/fills CONGELADOS, no un nuevo backtest:
- Añadir10bps por operación completa equivale a0.0005 por lado sobre el nominal ejecutado.
- Neto SPY resultante =4165.797456 − (4723.876116/0.00045)*0.0005 =−1082.953783.
- El colchón aritmético es aproximadamente7.9367bps adicionales por operación completa antes de que su neto llegue a cero.

No son nuevos CAGR/DD ni simulan impacto, colas, spread, funding, margen o redimensionamiento. La fuente SPX CFD BID/10 carece de spread ask validado y no es SPY ETF ni total return; pagar MARKET en esa fuente hace este límite especialmente relevante. No se cambió la comisión base para favorecer LIMIT o MARKET.

No se abrió2026, añadió fuente externa, editó framework o retocó la receta tras resultados. Este resultado queda conservado junto al protocolo. La evaluación conjunta de los cuatro casos de cartera y la combinada11 corresponde a root; este informe sólo concluye que SPY01, por sí sola, no cumple los objetivos.
