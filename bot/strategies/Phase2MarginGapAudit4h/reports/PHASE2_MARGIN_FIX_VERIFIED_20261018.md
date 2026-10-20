# Corrección de margen verificada — 2026-10-18

Cambio autorizado aplicado en FuturesExchange.on_order_execution. Libera reserva por submitted_price y conserva order.price real parafees/PNL. Regresión nueva reproduce fallo antes y pasa después. Total148pruebas:25 de gaps/broker y123 de estrategia/exchange/fronterasAPI. Sin instalaciones, reinicios ni accioneslive.

Auditoría histórica completa con gap-invariant y flat-invariant termina finished: http://localhost:9200/#/backtest/acc19ae1-4fc3-4b5a-8bd6-45a7a5142c4b . Todas sus métricas coinciden con el controlSTOP sininstrumentación http://localhost:9200/#/backtest/3c0fc5e0-d45e-43c8-9b83-832cb42ba6a9 :172trades,CAGR32.5548%,DD-35.4856%,final43464.31USDT. Antesdefix:169trades,CAGR10.4182%,final16764.92. La mejoría no es señal de estrategia nueva: es recuperación de capacidad de operación que el motor bloqueaba erróneamente.

ControlLIMIT sin refit http://localhost:9200/#/backtest/11c1a0a6-afe8-4718-80b9-a35e95adf40d :97trades,CAGR23.6650%,DD-14.0753%,final30265.50; antes23.6908%/-14.0763%/30298.42. Pequeñas diferencias de sizing por reservascorrectas, ninguna promesa de identidadcuandohaygaps.

Auditor run_analysis287a16c24c5e405a8d760cedccbc71b7: STOP53.97%mesesactivos/57.14%trimestres, peor mes-10.18%, top2share22.98%. LIMIT49.09%mesesactivos/66.67%trimestres, peor mes-4.39%, top2share37.01%. Ninguna cumple todavía65–70%meses/80%trimestres. DD es muestreo diario, no máximo intraminuto. Las3rutas danPNLpositivo en amboscontroles, pero soloLIMIT cumple límiteDD25%.

Por código, la rama real live retorna antes y no se modificó. SimulaciónMC/optimización que use esta contabilidad compartecorrección; no se ejecutó prueba de servicio real paper/live. 2026 intacto y reservadoparaespecificaciónfinalcombinada. Se reabrieron pruebas de shortscongeladas para juzgarlas con motorcorrecto.
