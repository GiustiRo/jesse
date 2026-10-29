# Fase 2 — ablation de resistencia intacta (no seleccionada)

Dashboard: http://localhost:9200/#/backtest/c914f6dd-d539-4288-935c-1c95b4940c73

2020-02-15 a 2025-12-31, BTC-USDT 4h, capital 10000 USDT, 5x isolated, fee 0.00045, fast_mode=False. Riesgo fijo máximo 3% por trade, 8% total planeado; reserva sizing 10bps sin simular slippage. Original Fase 1 preservada; sin usar 2026.

Hipótesis antes del run: evitar rearmar el máximo de una ruptura ya fallida, usando resistencia de las 26 barras previas y exigiendo que la última vela no la haya tocado y que el cierre esté a menos de 0.5 ATR. Resto del prototipo v1 conservado. No se efectuó optimización de ese umbral.

35 trades, 14 ganadores, 21 perdedores; CAGR 13.9378%, beneficio neto 115.3658%, DD publicado -17.4943%, Sharpe 0.9157, Calmar 0.7967. Menor frecuencia y retorno que el control 3% (45 trades, CAGR 35.1048%, DD publicado -12.4126%). Se conserva para trazabilidad, no como candidata seleccionada.

La curva numérica no fue persistida por el framework anterior; esta corrida precede a la corrección de persistencia autorizada por el usuario. Las métricas son las publicadas por Jesse; no se ha certificado regularidad mensual MTM. Pendiente integración multi-activo, auditor completo, sensibilidad y validación independiente. No se inició live ni paper.
