# MultiAssetRallyFade4h — motor corregido

Sesión: http://localhost:9200/#/backtest/b6f5562e-2144-4a54-9d27-108155680338

Estado:finished. Ventana2020-10-15 a2025-12-31;10k compartidos,fee.00045,5xaislado,3%max/trade,8%agregado planificado,modo normal. Misma estrategia congelada; corregida liberación de reserva tras gap. 2026 intacto.

CAGR -7.2898233917571%, DDdiario -42.57329468043138%, Sharpe -0.7611016196854907, 169trades (0long/169short), balancefinal 6739.2600372615125, neto -3260.7399627384752USDT, comisiones 1488.47856312891USDT.

Rechazada esta implementación:retorno neto negativo en el período completo. No implica imposibilidad de shorts en otras hipótesis. No ejecutar MC ni usar2026 para rescatarla.

DD de equity muestreada diariamente; proxiesPAXGspot/SPXCFD no son ejecución nativa futura. Resultados de desarrollo con múltiples familias exploradas, noOOS.
