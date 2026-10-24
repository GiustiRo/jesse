# Hipótesis macro diaria: evaluación aplazada por warmup

Sesión: http://localhost:9200/#/backtest/62351620-1a1d-4c68-ab49-b27757db57d1 . Estado stopped por cobertura requerida, sin resultados de rendimiento.

Error exacto: Missing candles for PAXG-USDT on Binance Perpetual Futures. This run needs data from 2019-06-23 to 2025-12-31 (which includes 240 warm-up candles before the start date).

La adición de BTC1D como data_route amplía el warmup exigido por el cargador a todas las rutas. El proxyPAXG Spot solo existe desde2020-08-28; la fuenteSPX elegida empieza2020. Este intento no evalúa la calidad de la hipótesis y no permite afirmar que falle o funcione. Se conserva el código para un protocolo con ventana común suficiente y controles iguales, o un cargador capaz de warmup específico porruta. Ninguno de esos cambios se aplicó aquí y no se fabricó cobertura histórica.

Reglas predeclaradas: shortsBTC, confirmación diariaEMA50<EMA200 decreciente y cierrebajoEMA200, usando exclusivamente velas diarias completamente cerradas. Entrada/stop/trailing4h de familia crisis sin cambios. 2026 reservado.
