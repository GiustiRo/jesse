# Cierre ronda1 — hipótesis de asignación descartada para regularidad
Dashboard: http://localhost:9200/#/backtest/72996434-7c02-4589-9400-42a23229ae02
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Protocolo y restricciones
ORCH_ALLOC_PROTOCOL_20261018.md guardado antes de correr. Fuentes/proxies originales BTC/PAXG/SPY4h, shortsBTC,longstres,10k/5xaislado,fee0.00045todasórdenes,riesgo<=3%/8%,2020-10-15→2025-12-31exclusivo.2026sellado.
## Resultado completo
CAGR31.755093%,DDmotor−17.683970%,Sharpe1.206608,neto32114.454825USDT,219operaciones.
AuditorMTMv3 ejecutado por el orquestador después de ambas pruebas: 55.74% de meses activos positivos y66.67% de trimestres positivos.
Referencia54.10%meses/71.43%trimestres. Objetivos65–70%meses y80%trimestres NO alcanzados.
## Decisión
DESCARTADA como solución de regularidad. Suma un mes positivo pero empeora trimestres yDD; mayorCAGRnojustificasustitución.
No barrer ventanas de volatilidad,anchorhorario,pesos o presupuestos después de resultados. Estrategia se conserva como control histórico, no candidata final. Referencia intacta.
Limitaciones de fuente y prioridad global siguen vigentes; sin framework/live/config. Próxima investigación debe cambiar estructura de gestión, no persiguir pesos por meses retrospectivos.
