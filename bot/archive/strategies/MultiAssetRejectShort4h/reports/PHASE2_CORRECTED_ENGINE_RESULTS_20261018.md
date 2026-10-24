# MultiAssetRejectShort4h — motor corregido

Sesión: http://localhost:9200/#/backtest/5c8e7296-fdc3-46a6-8663-ff00ff0b1d20

Estado:finished. Ventana2020-10-15 a2025-12-31;10k compartidos,fee.00045,5xaislado,3%max/trade,8%agregado planificado,modo normal. Misma estrategia congelada; corregida liberación de reserva tras gap. 2026 intacto.

CAGR -17.187317904381562%, DDdiario -64.27970275486837%, Sharpe -1.2075913484331933, 307trades (0long/307short), balancefinal 3740.9479192311833, neto -6259.052080768796USDT, comisiones 2080.8222436585397USDT.

Rechazada esta implementación:retorno neto negativo en el período completo. No implica imposibilidad de shorts en otras hipótesis. No ejecutar MC ni usar2026 para rescatarla.

DD de equity muestreada diariamente; proxiesPAXGspot/SPXCFD no son ejecución nativa futura. Resultados de desarrollo con múltiples familias exploradas, noOOS.
