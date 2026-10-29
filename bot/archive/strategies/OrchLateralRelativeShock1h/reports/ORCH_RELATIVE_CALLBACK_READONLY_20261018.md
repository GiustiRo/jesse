# Revisión read-only: cierre de contrapierna desde callback

Sin cambios de código ni framework. Lectura autorizada del motor y contraste con jesse://strategy/strategy_examples. La firma real es on_route_close_position(self,strategy).

## Orden observado en fuente
Strategy._on_close_position (Strategy.py:1251) emite _broadcast('route-close-position') ANTES de su propio on_close_position. _broadcast(:496) llama al callback de la otra ruta y después a su _detect_and_handle_entry_and_exit_modifications. Por tanto el callback puede convertir self.liquidate() en una orden MARKET sin esperar al próximo callback horario.

Pero liquidate(:1723) escribe self.price como precioTP/SL; self.price(:1506) deriva del current_candle de la propia ruta, salvo caché durante ejecución. Broker.reduce_position_at(:82) identifica MARKET al comparar ese precio; Sandbox.market_order(:15) guarda current_price en order.price. order_service.execute_simulated_market_orders(:137) llama execute_order(:59), que ejecuta al order.price ya guardado: NO lo actualiza con el último mark al ejecutar. Fees también usan ese precio.

## Asimetría de cotizaciones
_step_simulator(backtest_mode.py:1055,loop~1160) publica/procesa cada símbolo secuencialmente: addM1/price-effects/stops y luego siguiente símbolo. Un stopBTC puede hacer que callbackETH vea todavía el último minuto ANTERIOR. Si se crea allí MARKETETH, conservará ese precio viejo incluso cuando se ejecute al final del minuto tras actualizarETH. Cambiar48min por0min así podría fabricar una mejora con fillstale.

_timestamp_simulator/_apply_timestamp_replay_event(:913/:748) publica todas las filasM1 del evento antes de price-effects, y después procesa símbolos. self.price puede reconstruir la vela formando con M1actual, pero position.current_price y stops del siguiente símbolo pueden no haber sido procesados. El evento se etiqueta por fin de minuto y no conoce orden de ticks entre activos; no existe atomicidadintraminuto demostrada.

Conclusión: NO añadir hookliquidate a la versión actual por suposición. El smoke actual sigue siendo la referencia técnica y conserva48minhuérfanos reales. No afirmar que el callback sea inútil: tramita órdenes, pero falta asegurar la procedencia temporal del precio y el estado de ambas rutas.

## Alternativa de diseño, aún no implementada
Una versión claramente separada podría ejecutar ambas rutas en1m, mantener señales/fits solo sobre1h cerradas como data_routes, conservar decisiones baskettarget/stop/expiryhorarias y usar exitflag por emergencia para cerrar contrapierna en el próximo callback1m DESPUÉS de procesar ambas fuentes. Eso evita leer al siguiente símbolo antes de su actualización y reduce ventana huérfana modelada a próximo minuto, sin prometer ticks/atomicidad. Requiere smoke y comparación específica de cohortes/fees/cierres; no mezclar con baselinepares ni cambiar parámetros para mejorar PnL.

ImportETH sigue en curso; ninguna lectura2026performance ni modificación de servidores/sistemas.