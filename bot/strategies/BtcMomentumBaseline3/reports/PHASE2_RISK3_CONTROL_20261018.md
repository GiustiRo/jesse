# Control de Fase 2: BTC con riesgo del 3%

Dashboard: http://localhost:9200/#/backtest/786c23cb-6785-449a-a191-193804ee0c0f

Resultado de desarrollo, no validación OOS. Período 2020-02-15 a 2025-12-31; 2026 sin utilizar. Copia de BtcMomentumCore4h con único cambio operativo: riesgo por trade de 5% a 3%. Original conservada. Binance Perpetual Futures, 4h, 5x isolated, capital 10000 USDT, fee 0.00045, 240 warmup, fast_mode=False.

45 longs, 0 shorts; saldo final 58650.516926743156 USDT; retorno neto 486.50516926743154%; CAGR publicado 35.10476109401557%; drawdown publicado -12.412642962831534%; Sharpe 1.3801891585390769; ratio ganancias/pérdidas bruto 68372.9938658828 / 19722.476939139644. Sin funding ni slippage simulado.

Limitación de medición: get_session_results devuelve equity_curve vacío, aunque has_chart_data y has_charts_image son verdaderos. No se certifican retornos mensuales mark-to-market ni comparaciones de drawdown entre modos hasta resolverlo. La repetición previa al 5% mantuvo trades y beneficio total de Fase 1 pero cambió el drawdown de -21.90% a -18.67%; requiere investigar muestreo/medición.

Este control fija la comparación a igual riesgo para la candidata de Fase 2. No se inició ninguna sesión live o paper.