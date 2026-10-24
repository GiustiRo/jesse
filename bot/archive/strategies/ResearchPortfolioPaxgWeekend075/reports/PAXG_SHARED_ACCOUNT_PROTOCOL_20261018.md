# PAXG 0,75: contraste de cuenta compartida, protocolo previo

Fecha local: 18 de octubre de 2026. Se implementan dos clases nuevas, autocontenidas, sin modificar MultiAssetRetestBtcShort4h ni sus resultados. Este protocolo antecede los dos backtests y sus resultados. Root revisará ambas fuentes antes de lanzar.

## Pregunta y selección acumulada

La hipótesis de fin de semana de PAXG con EVENT_ATR 0,75 sobrevivió a un control hábil del mismo umbral y a retirar el target pasivo. Fue seleccionada después de observar vecinos. Esta continuación es desarrollo adaptativo de utilidad incremental, NO validación independiente, promoción definitiva ni reemplazo retrospectivo de la primaria de 1 ATR.

Preguntar si sustituir PAXG retest por esa política mejora la trayectoria de una cuenta compartida conservando BTC/SPY y un presupuesto PAXG del 1%. El contraste se realiza con interacción real de margen, reservas, tamaño y capital; no se suman curvas aisladas.

## Dos configuraciones congeladas

C: ResearchPortfolioPaxgRisk1Control4h. Las tres rutas BTC-USDT, PAXG-USDT y SPY-USDT operan a 4h con las reglas originales. Riesgo por trade BTC/SPY 3%, PAXG 1%. Data routes M1 de los tres activos.

T: ResearchPortfolioPaxgWeekend075. BTC/SPY conservan las mismas reglas y reloj 4h que C, riesgo 3%. PAXG ejecuta a 1h con riesgo 1% y receta de fin de semana 0,75: ancla viernes 16:00 NY, oportunidad domingo 16:00 NY si abs(movimiento)>=0,75 ATR 4h fijado al ancla; MARKET contrario al movimiento, target LIMIT en el ancla, stop 2 ATR y tiempo máximo de 24h desde el fill real. Se conserva cotización propia M1 fresca, paridad 1h/M1, ATR 4h completo y ZoneInfo para DST. Data M1 de todos los activos y PAXG 4h adicional; no duplicar rutas trading/data de igual timeframe.

Las clases son copias completas del baseline, sin importar estrategias ajenas. T añade dispatch sólo PAXG en before, señal y gestión de posición; go_long/go_short, should_cancel_entry y cierre usan el ledger compartido original. El plan PAXG contiene qty, entry, distance, target, risk y notional. Reservas se registran antes de enviar órdenes y se liberan en fill/cancel/cierre según el patrón original.

En AMBAS clases, el share de exposición ATR usa velas 4h de TODOS los activos obtenidas por get_candles, reteniendo sólo timestamps+4h<=tiempo actual y filtrando por trading_hours de cada ruta. Esto evita que PAXG 1h altere la asignación BTC/SPY por usar una volatilidad de distinto timeframe. Se mantienen mínimo EMA80+20 y participación inversa a ATR original. El techo individual original, capital*4,4*shareATR, también limita PAXG.

Es una adaptación común deliberada: C no es una reproducción exacta del tamaño de la referencia de riesgo PAXG 3%. C frente a referencia informa contexto de menor riesgo y reloj común; T frente a C es el contraste primario de política dentro de ese contrato. No confundir efectos.

## Contabilidad, datos y capacidad

Ventana 2020-10-15 a 2025-12-31 exclusiva, capital 10.000 USDT, Binance Perpetual Futures, modo normal, warmup 240 actual. Fee 0,00045 por lado en todas las órdenes, incluidos LIMIT; 5x aislado, riesgo planificado agregado máximo 8%, techo bruto 4,4x y reserva de 10 bps sólo para sizing. Capital presupuestable = min(wallet,MTM), sin ampliar por ganancias flotantes. Se conservan controles originales de margen, precisiones y reservas de órdenes pendientes.

SPY conserva trading_hours y entrada originales; PAXG permanece token continuo y su calendario define una oportunidad, no filtra artificialmente toda la historia. Stops y gestión permanecen activos fuera de ventanas de entrada. Si hay insuficiente historial completo para el share de 4h, no se inventa: startup cash queda incluido.

Cada evento dominical tiene una sola oportunidad; una posición ya abierta o falta de capital/reservas puede hacer perder el evento. No hay cola ni nuevo intento fuera de hora para recuperar señales. La interacción de las rutas y el tamaño endógeno son parte del resultado. No se afirma de antemano que los 60 trades aislados vayan a ejecutarse.

## Presupuesto, evaluación y aceptación

Dos full económicos nuevos y ningún ajuste posterior de riesgo, umbral, horarios, target, stop o asignación para rescatar resultados. Esperar revisión de root ANTES de ejecutar. Como máximo dos backtests propios y un análisis propio simultáneos. Sin framework, scripts nuevos, datos nuevos, instalaciones, fondos, live/paper, Pi ni 2026.

Comparación primaria T contra C: CAGR/neto, DD, MTM mensual/trimestral, meses rescatados y deteriorados, años, contribuciones por activo/sentido, fees, concentración y capacidad compartida. Referencia histórica actual sólo como contexto. Root ejecutará auditor V4 con snapshots completos, anclas y precios; no calcular regularidad por mes de cierre ni usar 00:01 del motor como fin de día.

Objetivos originales de cartera se conservan: mínimo 65% de meses activos positivos, aspiración 70%, mínimo 80% de trimestres positivos y DD no peor que −25%, con retorno útil resistente a costes. Reportar todos los meses de calendario, los completos y los conteos, sin excluir inactividad favorablemente. No declarar cumplimiento antes de MTM exacto.

No basta una mejora aislada de un porcentaje o menor DD obtenido por reducir exposición. Reportar el tradeoff completo y distinguir beneficio de la política frente al control con el mismo riesgo PAXG. Un resultado negativo se conserva; no abre más búsquedas automáticas en esta tanda.

La evidencia de spot no demuestra ejecución perpetual durante dislocaciones del token. Se puede evaluar este proxy aceptado para desarrollar, pero la transferencia nativa y estabilidad fuera de muestra siguen pendientes aun si la comparación de cartera mejora. No abrir 2026 automáticamente.
