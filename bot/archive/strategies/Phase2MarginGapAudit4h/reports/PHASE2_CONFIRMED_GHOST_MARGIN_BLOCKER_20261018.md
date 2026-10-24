# Bloqueo confirmado de investigación: margen fantasma tras entrada con gap

## Reproducción con datos históricos reales, sin tocar framework

Auditoría MCP: http://localhost:9200/#/backtest/376bbe77-9bcb-415c-9f8f-a74bf48fa7ab . Estado stopped por assert de diagnóstico deliberado, no por caída MCP. Clon de MultiAssetSession4h que, en on_open_position, comprueba que una entrada ya ejecutada no siga en el array de órdenes pendientes del exchange.

Fallo exacto:

```
AssertionError: PHASE2_GHOST_MARGIN symbol=SPY-USDT qty=57.633 submitted=411.9299 fill=411.9348 wallet=16134.499384043414 available_margin=4578.458033023417 unreleased_notional=23740.7559267
```

Reserva indebidamente retenida:23740.7559267/5=4748.15118534 USDT. La diferencia wallet-available en ese instante también incluye posiciones/órdenes legítimas; NO atribuir toda esa diferencia al fallo.

La comprobación corta2020–2021 no encontró una entrada gap y terminó; la ventana completa reproduce. Otra auditoría independiente de cuenta flat también incluye la misma comprobación on_open y se detuvo ahí: http://localhost:9200/#/backtest/1584dd3d-2d14-4adf-acc8-0b9df84c5d72 . Su invariant flat posterior aún no llegó a ejecutarse tras el primer gap.

## Causa en código

jesse/modes/backtest_mode.py::_execute_opening_gap_orders conserva order.vars['submitted_price'] y cambia order.price al precio de apertura realmente disponible. Esto es necesario para modelar ejecución yfees correctamente.

jesse/models/FuturesExchange.py::on_order_execution busca la reserva original con [order.qty, order.price]. Como order.price ya cambió, no encuentra [qty,precioenviado] y no elimina la fila. available_margin sigue descontando su notional/leverage en todas las operaciones siguientes y otras rutas. Por eso algunas familias muestran tamaños microscópicos desde2023 pese a preservar capital.

Los snapshots de sesión omiten order.vars; un análisis previo que buscó submitted_price en esos snapshots no podía detectar gaps y sus contadores cero NO prueban ausencia de gaps. La comprobación runtime anterior sí accede a las vars originales y reproduce el fallo.

## Corrección propuesta, TODAVÍA NO APLICADA

En on_order_execution de FuturesExchange, construir order_array con el precio original guardado cuando exista, manteniendo order.price real intacto para PnL/fees/posición. Si no hay repricing, usar order.price como hasta ahora. No corregirlo desde la estrategia ni desactivar gaps o falsear margen.

```
submitted_price = (order.vars or {}).get('submitted_price', order.price)
order_array = np.array([order.qty, submitted_price])
```

Complementar con regresión de entradas STOP y LIMIT long/short repriced al abrir gap, en modo normal y rápido, y garantías: reserva eliminada, posición con precio real, fees/PnL al precio real y margen restituido al cerrar. Mantener pruebas de salidas gap y broker. Repetir auditoría histórica y controles idénticos tras la corrección; no optimizar para compensar el bug.

## Alcance previsto

Cambia contabilidad de reservas simuladas en backtest y por tanto optimización/MonteCarlo que la reutilizan. Paper comparte parte de la contabilidad no-live, debe verificarse. La rama de live real retorna antes en on_order_execution y usa margen informado por exchange; no se propone tocar adapterlive ni operar producción. No prometer invariancia de resultados de simulación: precisamente se corrigen.

## Estado y revisión necesaria

Sin cambios nuevos al framework. Autorización previa solo cubría persistencia de equity; bot/AGENTS.md exige MCP para modificaciones de framework, y no hay herramienta MCP para este arreglo. Se necesita ampliar explícitamente esa excepción para aplicar el parche y regresiones locales. No reiniciar servidor ni tocar Pi. 2026 permanece reservado.

Todas las comparaciones de familias de esta tanda quedan provisionales hasta repetir con contabilidad correcta. No declarar ganadora LIMIT ni descartados definitivos los shorts por estos resultados. La existencia del bug no prueba que las estrategias tengan edge al corregirlo.
