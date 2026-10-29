# MultiAssetRiskOffShort4h — motor corregido

Sesión: http://localhost:9200/#/backtest/5b58769a-32b8-4f7e-9e85-6b89af26ea89

Estado:finished. Ventana2020-10-15 a2025-12-31;10k compartidos,fee.00045,5xaislado,3%max/trade,8%agregado planificado,modo normal. Misma estrategia congelada; corregida liberación de reserva tras gap. 2026 intacto.

CAGR -1.4855223407368223%, DDdiario -26.079778227522542%, Sharpe -0.05403909595559608, 54trades (0long/54short), balancefinal 9249.351123033322, neto -750.6488769666748USDT, comisiones 518.6458556908542USDT.

Rechazada esta implementación:retorno neto negativo en el período completo. No implica imposibilidad de shorts en otras hipótesis. No ejecutar MC ni usar2026 para rescatarla.

DD de equity muestreada diariamente; proxiesPAXGspot/SPXCFD no son ejecución nativa futura. Resultados de desarrollo con múltiples familias exploradas, noOOS.
