# Diagnóstico de muestreo diario fast/normal

Dashboard: http://localhost:9200/#/backtest/76bff9bb-c8f9-4119-b485-ab85ffd2018a

Comparación contra modo normal: http://localhost:9200/#/backtest/eef79402-f4cc-4b9c-8305-9ab870d639e5

Mismo control BtcMomentumBaseline3, 3% riesgo, BTC-USDT 4h, 2020-02-15 a 2025-12-31, 5x isolated, fee 0.00045. Resultado económico de los 45 trades idéntico según símbolo, lado, entrada, salida, qty, fechas, PNL y fee. Saldo final idéntico 58650.516926743156.

Cada curva conserva 2147 muestras: inicial/final 00:00 UTC; 2145 diarias intermedias en step a 00:01 UTC y skip/fast a 04:00 UTC. El código usa umbral inicial +86460000ms y el modo rápido lo cruza al completar su bloque de 4h. DD diario normal -12.412642962831534%; rápido -14.967745332901117%. Sharpe/Calmar también cambian con el muestreo. No son medidas del máximo drawdown intradía.

La corrección autorizada de persistencia no modificó ninguno de los dos simuladores ni su muestreo. Se fija fast_mode=False para comparaciones de Fase 2; cualquier Monte Carlo que use otro modo debe declarar esta diferencia. No atribuir cambios de drawdown a cambios de estrategia cuando solo cambió la hora observada. 2026 reservado sin usar.
