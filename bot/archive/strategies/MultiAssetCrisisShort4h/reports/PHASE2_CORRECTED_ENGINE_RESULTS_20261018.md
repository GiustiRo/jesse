# MultiAssetCrisisShort4h — repetición con motor corregido

Sesión: http://localhost:9200/#/backtest/facc2347-5ce4-4452-98e0-7509fd1e69a1

Estado: finished. Ventana2020-10-15 a2025-12-31;10k compartidos,fee.00045,5xaislado,3%max/trade,8%agregado planificado,modo normal. Misma estrategia congelada; corregida liberación de reserva tras gap. 2026 intacto.

CAGR -4.475591251230515%, DDdiario -29.917727473393143%, Sharpe -0.25822661668074254, 73trades (0long/73short), balancefinal 7876.300135192262, neto -2123.699864807748USDT, comisiones 606.3890466289404USDT.

Rechazada esta implementación:retorno neto negativo en el período completo. No implica imposibilidad de shorts en otras hipótesis. No ejecutar MC ni usar2026 para rescatarla.

DD de equity muestreada diariamente; proxiesPAXGspot/SPXCFD no son ejecución nativa futura. Resultados de desarrollo con múltiples familias exploradas, noOOS. Mantener control positivo LIMIT e investigar robustez local con protocolo previo, sin seleccionar mejor esquina.
