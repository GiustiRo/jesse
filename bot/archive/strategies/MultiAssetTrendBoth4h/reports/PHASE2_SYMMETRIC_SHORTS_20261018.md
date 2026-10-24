# Shorts simétricos: hipótesis rechazada

Dashboard: http://localhost:9200/#/backtest/257b9df2-77be-4a69-8b36-3276e7b337e4

BTC+PAXG 4h, 2020-10-15 a 2025-12-31, cuenta compartida 10000 USDT, 5x isolated, fee 0.00045, fast_mode=False, warmup 240, 3%/8% de riesgo máximo planeado y nocional 4.4x con cuota por volatilidad. PAXG Spot simulado como futuros.

Prueba predeclarada de simetría: reflejar EMA, pendiente, RSI y Donchian a cortos manteniendo parámetros de la variante long-only; no optimización adicional. Resultado: 247 trades, 129 longs y 118 shorts. Win rate longs 39.53%, shorts 22.03%; CAGR 9.3073%, saldo final 15903.9572 USDT, beneficio neto 59.0396%, drawdown diario -48.1573%, Sharpe 0.4273, Calmar 0.1933. La simetría mecánica empeora mucho el resultado. No se incorporará por defecto a la prueba de tres activos.

Desarrollar cortos requeriría una hipótesis distinta, no simplemente invertir compras. La prueba no demuestra que ningún corto sea viable, solo rechaza esta especificación. 2026 no utilizado. Sin live/paper ni Monte Carlo de una candidata fallida.