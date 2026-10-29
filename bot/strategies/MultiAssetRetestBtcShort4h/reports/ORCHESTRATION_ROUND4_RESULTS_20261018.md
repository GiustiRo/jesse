# Ronda4: horizonte diario y rotación mensual
Fecha2026-10-18. Objetivo no alcanzado; referencia y2026 conservados.

| Diseño | CAGR | DD motor | Meses activos positivos | Todos los meses positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
|[Turtle diario BTC+PAXG, long/short](http://localhost:9200/#/backtest/a4a5837e-ed47-4179-82a1-2612fd899d14)|4.085%|−8.892%|24/57 (42.11%)|24/63|12/21|
|[Rotación mensual BTC/PAXG/SPY/cash, long](http://localhost:9200/#/backtest/56937ae5-e005-4d70-931d-c9d1e5215b42)|3.946%|−22.896%|31/55 (56.36%)|31/63|10/21|

Rechazados, sin subir riesgo ni retirar activos/sentidos después de observar resultados. Menor frecuencia redujo costes pero no creó regularidad ni rentabilidad útil por sí misma.

Turtle:64trades,net2321.38,fee140.12. Shorts agregados−430.81; no demuestra pata short útil. Cierres diarios completos:24/56activos,24/61calendario,11/19trimestres. Comprobación runtime demostró crecimiento del histórico desde warmup40 a56d sin inventar PAXG2019. No variar55/10/2ATR.
Rotación:28trades,net2235.73,fee80.05. BTC+1554.63/PAXG+793.93/SPY−112.84. Primera entrada verificada2021-02-03 a16UTC; startupcash incluido en63meses, sin excluir meses incómodos. Máxima exposición inicial≈.2945x por stop10% y límite de riesgo3%, no supuesta inversión1x. Períodos completos30/54activos,30/61calendario,9/19trimestres.

## Contador terminal: corrección del auditor, no del framework
Durante revisión se interpretó provisionalmente total_open_trades=1 como posición residual. Lectura de Strategy._terminate y métricas, más órdenes guardadas, demostraron que es contador ANTES del cierre sintético de final. En este run el último trade esPAXG (noSPY), salida completa MARKET EXECUTED alfinish; gross422.55635 coincide con open_pl preterminación; net419.234085 y fees3.322265, y todos los trades/fees/wallet actual reconcilian.
No se modificaron métricas originales ni se resimuló para ocultarlo. V4 ahora acepta ese contador sólo si número de cierres completos justo alfinish y PnL bruto de últimos slices explican contador/open_pl; inconsistencias siguen fallando. Autopruebas de contador válido e inconsistente pasan. Ese cierre sintético final no acredita liquidez de otros activos ni una acción live; es convención de cierre de muestra.
V4 reconstruyó ambas trayectorias con fills, fees y cantidades, incluyendo controles de períodos completos. Cambios sólo en auditor autorizado medianteMCP, sin nuevas modificaciones framework.

## Trazabilidad y continuación
Total económico completo en orquestación:15pruebas, todas conservadas; smoke/fallo por datos fuera de comparaciones económicas. Continúa pendiente full de overshoot relativo BTC/ETH al completar cobertura2025. OLS de retornos no demuestra cointegración ni reversión de spread; es hipótesis a falsar, con riesgo huérfano y ejecución no atómica documentados.
Siguiente control acotado: mismo componente short de referencia, salida a24h en lugar72h, resto exacto; decisión adaptativa de desarrollo explícita, un único plazo sin rejilla posterior. Protocolo/fuente pendientes de revisión antesrun. No cambiar criterios de regularidad.
