# V3 CHANNEL — evaluación C4
Intervalo UTC [2025-07-01,2026-01-01), fin exclusivo sin datos de 2026. Sesiones independientes con 10.000 USDT iniciales y configuración nominal. SELECTION_V3_C4.json fue guardada antes de arranque y seleccionó POI por menor DD de train.

| Sesión | Trades | Neto % | PF | DD motor % |
|---|---:|---:|---:|---:|
| [CHANNEL_P](http://localhost:9200/#/backtest/36b23618-bda4-44b3-b1c1-e9e97fdd23a1) | 24 | -1.92 | 0.918100 | -12.18 |
| [CHANNEL_POI](http://localhost:9200/#/backtest/2ebd9039-498f-4bd7-9cc3-dbf36fb77682) | 18 | 5.70 | 1.339496 | -7.09 |

Contadores: ambas sesiones tienen 1.104 decisiones y seis meses. P registra 23 buckets, 24 entradas y 24 cierres; POI registra 23 buckets, 18 entradas y 18 cierres. Las sumas de primarias y direcciones, allowed igual a entradas y cierres posteriores se verificaron. La procedencia coincide con las fechas de wrapper/form.
Auditorías completas de buckets guardadas por wrapper; root concilia snapshots completos. El timeout de arranque POI fue resuelto leyendo el mismo ID, con raw completo preservado y sin retry.
No hubo ajustes. La fase B queda completa: 14 sesiones nuevas y dos trains C1 reutilizados desde screening. Estas curvas semestrales reiniciadas no sustituyen el replay de capital continuo ni prueban robustez.
Fuentes OI de fase C creadas y releídas según calendario ya congelado; no ejecutadas hasta freeze y GO de root. Pasa a dueño de P el subagente designado por root; este sector gestionará OI con un token global.
