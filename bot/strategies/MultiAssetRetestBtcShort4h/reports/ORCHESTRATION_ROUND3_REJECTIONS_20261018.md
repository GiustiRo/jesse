# Tercera ronda: dos rechazos económicos y controles de regularidad
Fecha2026-10-18. Fuente y umbrales congelados antes de cada prueba. Desarrollo común2020-10-15 a2025-12-31 exclusivo.2026 no evaluado.

| Caso | Trades | Neto USDT | CAGR | DD motor | Meses activos positivos | Todos los meses positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|---:|---:|
|[BTC reversión rápida](http://localhost:9200/#/backtest/df044178-559e-4d34-848f-820825479701)|258long|−72.23|−0.139%|−5.213%|31/53|31/63|11/21|
|[BTC ruptura tras baja volatilidad](http://localhost:9200/#/backtest/c4514079-275c-4586-b773-ea464d5cf1bf)|123short|−239.93|−0.465%|−26.660%|19/53|19/63|8/21|

Ambos rechazados. No reajustar RSI, ventanas o ratio después de ver el fallo.
FastMR:67.83% acierto y payout0.466; beneficio antes de fees519.98 frente592.20fees. Acierto alto no demuestra esperanza neta positiva. +10bps RT sobre los mismos fills implica−730.23, sin atribuirle nuevoCAGR/DD ni llamarlo backtest.
QuietChannel:buffer>=722bars validado en cada callback conwarmup800. No se confunde fallo técnico con cero trades; la prueba sí se ejecutó y falló económicamente. DD MTM al cierre diario−26.708%, también sobre límite.
V4 reconcilió fills, fees y wallet terminal de ambos. Conteos incluyen bordes parciales; reportar completos al evaluar candidatura.

## Investigación retirada antes de ejecutar
OvernightSPY no justifica un run: prima publicada de una franja nocturna pequeña frente9bpsRT, proxiesBID sinspread y cobertura irregular de horas16NY en invierno. Esto no es medición del PnL de una estrategia overnight propia. Informe detallado del agente documenta fuente primaria y limita esa inferencia.

## Incertidumbre de regularidad
Referencia33/61 meses activos; FixedR5 39/61; parcial35/61. Wilson95 nominal respectivamente41.72–65.99%,51.39–74.83%,44.90–68.98%. Dependencia temporal y selección adaptativa hacen esas bandas meramente descriptivas.
En63meses pareados FixedR5 rescata10yestropea4 respecto a referencia;pMcNemar nominal.1796. Parcial rescata3yestropea1;p.625. No se declaran mejoras confirmadas ni se añaden nuevas restricciones de p/CI.
En períodos COMPLETOS hay61meses y19trimestres: referencia33/59activos y14/19quarters; FixedR5 38/59 y14/19; parcial35/59 y13/19. El aparente avance trimestral de FixedR5 al incluir bordes desaparece en períodos completos. Principales conteos originales se conservan, sin seleccionar el denominador favorable.
Ver informe del agente: strategies/OrchManageFixedR54h/reports/ORCH_REGULARITY_UNCERTAINTY_20261018.md.

Total económico de orquestación:13 pruebas. Smoke técnico y fallo por datos se registran por separado. No hay candidata aceptada. Próximos trabajos: rotación mensual simple BTC/PAXG/SPY/cash con stop10% y exposición reducida para respetar3%riesgo, y pares BTC/ETH pendiente de cobertura histórica. No sumar curvas como cartera ejecutable; Binance one-way requiere una decisión neta por símbolo.
