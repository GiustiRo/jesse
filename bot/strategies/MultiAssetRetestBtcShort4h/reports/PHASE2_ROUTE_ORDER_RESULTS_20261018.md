# Permutación de rutas en el formulario: resultado y corrección de alcance

## Corrección importante
La igualdad observada NO demuestra que la estrategia sea independiente de la prioridad real de ejecución.
El simulador de timestamps usado para históricos con calendarios distintos construye routes_info con sorted(router.routes, key=(exchange, symbol, timeframe, strategy_name)), antes de ejecutar los callbacks. Fuente inspeccionada en modo lectura: jesse/modes/backtest_mode.py, alrededor de las líneas 959–963 y 1012–1014.

Por tanto, permutar las rutas del formulario conserva la misma prioridad interna BTC/PAXG/SPY en estos casos. Las simulaciones verifican invariancia ante orden de entrada del formulario, no un contrafactual con BTC procesado después de SPY.

## Evidencia observada
[Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb),
[formulario SPY/PAXG/BTC](http://localhost:9200/#/backtest/34198355-675c-42b4-8442-43497028a255),
[formulario PAXG/BTC/SPY](http://localhost:9200/#/backtest/c9fa1945-f447-4200-8b35-377315188ed1).
220 trades en todos, mismos símbolos/direcciones/timestamps/cantidades/precios/fees/PnL dentro de rtol1e-12 y atol1e-9. Máxima diferencia de equity: 3.64e-12 USDT.
Análisis MCP 97cfed55e0804d5ca80f93ce13320adf completado correctamente; MTM reconciliado, 33/61 meses activos y 15/21 trimestres positivos.

## Consecuencia
El control de prioridad interna sigue pendiente. No interpretar resultados iguales como prueba de reparto equitativo de margen cuando coinciden señales.
El MCP de backtests no expone una opción para cambiar esa prioridad. No se modificó el framework; cualquier nueva extensión para ello necesita autorización específica. No se solicita ampliar ahora el framework para certificar variantes que todavía incumplen regularidad.
Se corrige la interpretación del informe anterior; sus cifras de igualdad siguen siendo correctas. Referencia y 2026 intactos.
