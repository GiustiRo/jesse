# Corrección autorizada de reservas tras gap — implementación

El usuario autorizó explícitamente corregir, comprobar y continuar la fase2. Se aplicó un cambio mínimo en FuturesExchange.on_order_execution: para retirar la reserva usa order.vars['submitted_price'] cuando existe, con order.price como fallback normal. El precio de fill real permanece en order.price para posición,fees yPNL. La rama live real retorna antes y no cambia. Las simulaciones que usan esta contabilidad sí pueden cambiar y deben repetirse.

Regresión añadida en tests/test_price_gap_backtest.py, siguiendo el patrón de hooks de estrategia. Matriz16casos: long/short × STOP/LIMIT × normal/rápido × cross/isolated, leverage5. Gap en interior de bloque5m; comprueba precio de ejecución distinto del enviado, fees reales, ausencia de reserva tras fill, coste de posición real, PNL igual a variaciónwallet y devolución de margen al cerrar. Primero se ejecutó contra código anterior: falla al quedar1reservaBUY, como esperado. Tras corrección:25pruebas pasan en test_price_gap_backtest.py+test_broker.py. Pruebas ampliadas en curso al guardar. Python3.11.17 del entornoDocker existente; sin instalaciones ni reinicios.

Auditoría histórica con la misma estrategia y asserts: http://localhost:9200/#/backtest/acc19ae1-4fc3-4b5a-8bd6-45a7a5142c4b . Controles congelados STOP yLIMIT: http://localhost:9200/#/backtest/3c0fc5e0-d45e-43c8-9b83-832cb42ba6a9 y http://localhost:9200/#/backtest/11c1a0a6-afe8-4718-80b9-a35e95adf40d . Aún ejecutándose al guardar. No atribuir beneficios nuevos al arreglo antes de terminar.

2026 reservado, producción intacta. No se cambiaron reglas ni se ajustaron parámetros para estos controles. Se preservan los cambios ajenos preexistentes y la corrección previa de equity.
