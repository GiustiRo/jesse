# V3 CHANNEL — evaluación C3
Intervalo UTC [2025-01-01,2025-07-01). Sesiones independientes reiniciadas con 10.000 USDT y configuración nominal. SELECTION_V3_C3.json fue guardada antes de arranque y seleccionó POI por menor DD de train; los resultados posteriores no modifican esa selección.

| Sesión | Trades | Neto % | PF | DD motor % |
|---|---:|---:|---:|---:|
| [CHANNEL_P](http://localhost:9200/#/backtest/03753b45-bdb2-45c9-88ca-015a2bd374c5) | 25 | 1.87 | 1.082809 | -12.38 |
| [CHANNEL_POI](http://localhost:9200/#/backtest/2004cd16-ad77-4d80-b1bd-0e54809126bf) | 22 | 2.98 | 1.143178 | -12.42 |

Ambas sesiones registran 1.086 decisiones, seis meses y 22 buckets observados. P tiene 25 entradas/cierres; POI tiene 22; no hubo cierre forzado posterior. Se verificaron particiones mensuales, entradas/allowed y procedencia de fechas/use_oi/hold contra wrappers y form. Auditorías por wrapper guardadas.
Root concilia snapshots completos y registra diferencias de equity terminal; este agente no ejecuta análisis propios. El timeout de arranque POI fue resuelto leyendo el mismo ID, con raw preservado y sin retry.
Sin cambios de fuentes, reglas o datos; sin consultas de 2026. C4 requiere su GO y su evaluación una selección previa.
