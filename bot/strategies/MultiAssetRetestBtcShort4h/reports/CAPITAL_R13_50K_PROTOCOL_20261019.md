# R13 — K1001 con capital inicial 50.000 USDT
El usuario expresa preferencia por el perfil 2%/6% a 3x y pregunta por los resultados con 50k. Se registra esa preferencia para la investigación; no autoriza iniciar o modificar live/paper.

## Matriz previa a resultados
Cuatro corridas nuevas K1001: B/C × fee nominal0.00045 / estrés0.00095 por lado. Único cambio respecto de las cuatro anclas R12: capital inicial de10000 a50000 USDT en form.config.exchange.balance. Leverage3x isolated, riesgo objetivo2%/agregado6%, fuentes originales del perfil R12, mismo sizing/cuotas/cap4.4/buffer90%/reserva.001.
Misma ventana2020-10-15 inclusiva a2025-12-31 exclusiva, cuatro rutas base nominal/estrés (tres activos BTC/PAXG/SPY4h, tres feeds1m), warmup240, fast_modefalse, debugtrue. B usa SPY Second; C SPY Market. 2026 cerrado incluso inspección.
Las fuentes de las cuatro clases se leyeron y verificaron con TRADE_RISK=.02 y PORTFOLIO_RISK=.06. Sin edición de código ni configuración global. Máximo2backtests simultáneos y1analysis.

## Pregunta y auditoría
No asumir escalado exacto por5: ejecutar el motor con50000 y comparar contra10000, porque redondeo de cantidades puede producir pequeñas diferencias de capitalización.
Conciliar neto de trades/motor y equity terminal; comparar firmas de entradas/salidas a igual perfil/fee, neto50k menos5×neto10k, CAGR/DD/PF/Sharpe/fees, ganancias y saldo final. Mostrar tabla anual y caída absoluta observada desde picos de equity diaria.
Los presupuestos iniciales son1000USDT por operación al stop y3000USDT agregado; no margen de1000USDT ni pérdida máxima garantizada. Se recalculan al variar capital y pueden recortarse por capacidad.
Distinguir rendimiento histórico compuesto de una proyección futura. Sin slippage simulado, impacto de mercado, liquidez ni funding;50k nominales en el motor no certifican capacidad real de ejecución. B/C no son muestras independientes. Fee mayor puede alterar órdenes por reglas dependientes de fee.
Guardar resultados y datos completos vía MCP. No abrir2026 ni operar fondos.
