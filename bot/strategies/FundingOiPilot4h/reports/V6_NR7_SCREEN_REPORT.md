# V6 NR7 — SCREEN cerrado, ambas variantes rechazadas

BTC-USDT Binance Perpetual Futures, 4h, [2020-09-01,2024-01-01). Regla fija: B−1 menor rango estricto entre siete barras previas y siguiente cierre fuera de su high/low. Entrada MARKET actual, stop2ATR14 simple actual, TP3R y máximo96h. Sin cambios de fuentes o parámetros tras resultados.

| Variante | Trades | Neto del período | PF | DD motor | Sharpe | Duración motor |
|---|---:|---:|---:|---:|---:|---:|
| NR7_P | 269 | 56.205784% | 1.177679 | -35.076572% | 0.718112 | 29.81s |
| NR7_POI | 203 | 13.886488% | 1.059113 | -30.318213% | 0.296318 | 25.48s |

Dashboard NR7_P: http://localhost:9200/#/backtest/2a536f25-acd0-41fc-9cf4-00204fa87f23
Sesión: 2a536f25-acd0-41fc-9cf4-00204fa87f23.

Dashboard NR7_POI: http://localhost:9200/#/backtest/b97711e0-f25d-49a1-8803-8b5b48e3eec2
Sesión: b97711e0-f25d-49a1-8803-8b5b48e3eec2.

Son retornos de 40 meses, no anuales. Ambas cumplen el mínimo de 30 trades del SCREEN, pero fallan PF>=1,2 y DD<=25%. No se redondea PF de P para aprobar. Ninguna puede integrar la shortlist por su neto positivo.

OI redujo trades y drawdown, pero también retorno y PF. Es una comparación de trayectorias con sizing y ocupación diferentes, no un efecto aislado sobre los mismos trades. No se cambia el filtro, stop o TP para rescatar la línea.

## Validación de ejecución

Se usaron los dos drafts existentes autorizados, con configuración y fuentes verificadas. Prerun y start_requested se persistieron antes de un solo start por ID. Ambos respondieron started, sin timeout ni reintento. Máximo dos motores concurrentes; ambos tokens están liberados.

Cada variante cuenta 40 meses y 7.302 decisiones. Logs completos: P 4.182 líneas en 21 páginas; POI 3.487 líneas en 18 páginas. Máximo de línea 1.111/1.110 caracteres. Las cuatro fuentes permanecen idénticas a las capturadas.

Todos los 472 planes conforman: 269 P y 203 POI. Se verificaron ranking estricto, ruptura por cierre, ventanas de ocho OHLC y ATR actual de quince, stop2A y TP3R desde fill, floor8/riesgo2% con ambos fees/cap1x, cuota UTC, no reentrada en decisión de cierre y funding publicado asof. Los 203 gates OI de POI cumplen referencia exacta T−24h, valores positivos crecientes y freshness del reloj original.

Los resúmenes before_terminate registran 268/202 cierres. Cada sesión agrega un cierre final forzado: total 269/203 trades y V6_CLOSE reconciliados. Motivos:
- P: 110 máximo holding, 123 stop, 35 TP y un fold_end.
- POI: 75 máximo holding, 102 stop, 25 TP y un fold_end.

Los maximum_hold fueron a 96 horas exactas; los demás trades no excedieron ese límite. Se ejercieron fills de stop/TP, holding y cierre final. No hubo frontera semestral de replay en estas sesiones SCREEN.

Root comunicó PASS de ambos snapshots financieros completos en V6_NR7_SCREEN_ACCOUNTING.json. Ledger, órdenes, equity anual y sensibilidades pertenecen a esa auditoría central; esta rama no ejecutó jobs de análisis.

## Límites e incidente de auditoría

Los rangos y cierres de entrada se recalcularon desde valores logueados. Los hashes identifican ventanas congeladas, pero las OHLC completas no están en esos logs: no se afirma recomputación independiente del hash o valor ATR desde velas originales. Su construcción causal está cubierta por fuente y 89 checks sectoriales, más 67 comunes ejecutados en smoke.

La primera auditoría comparó con igualdad exacta el fill de orden y VWAP del trade. Hubo 24 casos P y 15 POI con residuos de redondeo de hasta 7,28e−12. Sólo ese comparador pasó a tolerancia absoluta de precio 1e−8. No cambiaron estrategia, sizing o desigualdades de señal. El diagnóstico se conserva en V6_NR7_AUDIT_FLOAT_COMPARISON_DIAGNOSTIC.json.

## Evidencia y continuidad

V6_NR7_PROGRESS.json contiene fuentes, readbacks y raws de draft/start/summary. AUDIT_ResearchV6Nr7P4h_SCREEN.json y AUDIT_ResearchV6Nr7Oi4h_SCREEN.json conservan todos los contadores y planes/cierres enlazados. Los 39 shards V6_NR7_*_SCREEN_LOGS_XX.json guardan los logs completos originales.

Estado sectorial SCREEN_COMPLETE_REJECTED. Sin nuevas corridas ni cambios desde esta rama. Root puede congelar la shortlist global con otras líneas elegibles. 2026 permanece cerrado; no live/paper ni órdenes reales.
