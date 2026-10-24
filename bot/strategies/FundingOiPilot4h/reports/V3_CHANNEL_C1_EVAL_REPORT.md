# V3 CHANNEL — evaluación C1
Fecha: 2026-10-20. Intervalo UTC [2024-01-01, 2024-07-01).
Cada sesión empezó plana con 10.000 USDT. Son evaluaciones semestrales independientes; no se transportó el capital del entrenamiento ni del semestre anterior.

## Selección y resultados
SELECTION_V3_C1.json fue guardada por root antes de solicitar ambas evaluaciones. Seleccionó CHANNEL_POI por su menor drawdown de entrenamiento. El rendimiento posterior de P no cambia esa decisión.

| Sesión | Trades | Neto % | PF | DD motor % | Motor s |
|---|---:|---:|---:|---:|---:|
| [CHANNEL_P](http://localhost:9200/#/backtest/1ead2e5d-d907-43b2-8e9d-925aea5e3093) | 25 | 16.31 | 1.587211 | -18.35 | 6.11 |
| [CHANNEL_POI](http://localhost:9200/#/backtest/faeccf79-ea48-4d5a-93bf-8ab77a0c8095) | 22 | 11.99 | 1.500560 | -15.06 | 4.74 |

## Integridad y límites
Las fuentes sólo cambian START/FINISH mediante wrappers congelados y verificados por root. Padres, helper y base permanecen intactos. Configuración nominal: fee 0,00045 por lado, slippage cero, isolated 3x, cap notional C, presupuesto de riesgo 2% stop más fees, funding activo, OI versionado, warmup 240, debug activo y benchmark/exports desactivados.
Cada sesión registra 1092 decisiones de cuatro horas, seis meses y 22 buckets observados. Las direcciones sin eventos no generan buckets ficticios. Se verificaron las particiones primarias, all frente a direcciones, allowed igual a entradas y entradas frente a cierres. P tuvo 25 entradas y 25 cierres; POI tuvo 22 y 22. No hubo cierre forzado posterior a la auditoría.
La procedencia START/FINISH/use_oi/hold se contrastó con wrapper y form. Las auditorías AUDIT_ResearchV3CH_{P,OI}_C1V.json conservan todos los buckets y procedencia desde una cola suficiente; no sustituyen el histórico completo de gestión. Root registra la conciliación de fees, ledger, PNL y equity terminal desde snapshots completos. Este agente no ejecutó run_analysis.
El arranque de POI devolvió HTTP read timeout de diez segundos. Se preservó el raw completo y se consultó la misma sesión hasta finished, sin reintentar.
Un semestre no demuestra robustez ni rentabilidad anual. La reserva interna de 2024–2025 tiene exposición histórica de otras investigaciones; 2026 sigue cerrado. No hubo ajustes de parámetros, estrategia o configuración global. La siguiente etapa requiere su GO específico y cada evaluación futura una selección previa de root.
