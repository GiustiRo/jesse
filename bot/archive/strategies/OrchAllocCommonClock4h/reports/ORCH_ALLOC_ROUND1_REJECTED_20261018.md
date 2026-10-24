# Cierre ronda1 — hipótesis de asignación descartada para regularidad
Dashboard: http://localhost:9200/#/backtest/9bbd9545-2154-4842-8902-8c926c7a4a56
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Protocolo y restricciones
ORCH_ALLOC_PROTOCOL_20261018.md guardado antes de correr. Fuentes/proxies originales BTC/PAXG/SPY4h, shortsBTC,longstres,10k/5xaislado,fee0.00045todasórdenes,riesgo<=3%/8%,2020-10-15→2025-12-31exclusivo.2026sellado.
## Resultado completo
CAGR23.135580%,DDmotor−14.171011%,Sharpe1.198382,neto19595.973990USDT,222operaciones.
AuditorMTMv3 ejecutado por el orquestador después de ambas pruebas: 54.10% de meses activos positivos y61.90% de trimestres positivos.
Referencia54.10%meses/71.43%trimestres. Objetivos65–70%meses y80%trimestres NO alcanzados.
## Decisión
DESCARTADA como solución de regularidad. Mismos meses positivos y peores trimestres; reduce retorno sin resolver el problema.
No barrer ventanas de volatilidad,anchorhorario,pesos o presupuestos después de resultados. Estrategia se conserva como control histórico, no candidata final. Referencia intacta.
Limitaciones de fuente y prioridad global siguen vigentes; sin framework/live/config. Próxima investigación debe cambiar estructura de gestión, no persiguir pesos por meses retrospectivos.
