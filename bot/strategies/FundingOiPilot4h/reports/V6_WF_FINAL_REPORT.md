# V6 EFFICIENCY: walk forward completado

Los cuatro folds terminaron con auditorías financieras y estructurales PASS. La elegibilidad TRAIN congeló el calendario individual ON, ON, OFF, OFF. No se seleccionó ningún semestre utilizando su propio resultado futuro.

| Fold | TRAIN N | TRAIN net % | TRAIN PF | TRAIN DD % | Selección | EVAL N | EVAL net % |
|---|---:|---:|---:|---:|---|---:|---:|
| C1 2024H1 |148|40.0166|1.24777|−21.8696|ON|19|9.20745|
| C2 2024H2 |167|52.9086|1.28843|−21.8696|ON|25|−8.17605|
| C3 2025H1 |192|40.4067|1.18028|−21.8696|OFF|24|−16.6626|
| C4 2025H2 |216|17.0113|1.06493|−31.4945|OFF|22|7.73245|

C3 falla PF ≥1.2. C4 falla PF ≥1.2 y DD absoluto ≤25%. Los resultados diagnósticos posteriores no alteran esas decisiones. Sólo 44 operaciones EVAL pertenecen a semestres activos; las 46 de 2025 son diagnósticas y quedan excluidas del umbral N≥100. No se suman rentabilidades de cuentas reiniciadas para atribuir CAGR continuo.

Los siete motores nuevos y la reutilización del SCREEN C1 terminaron sin modificar parámetros. Las auditorías verifican config exacta, ruta 4h, fechas, contabilidad completa, financiación, ejecuciones, señales, límites de riesgo, UTC y cierres. No hubo cierres forzados. La cronología selección antes de creación EVAL pasó para los cuatro folds, registrada en V6_WF_SELECTION_CHRONOLOGY.json.

Datos completos: V6_WF_FINAL_ROWS.json y V6_WF_BRANCH_PROGRESS.json. Cada fold contiene referencias a snapshots financieros, logs, operaciones, formularios e inicio único. Calendario congelado: V6_REPLAY_CALENDAR.json. La fase siguiente evalúa capital continuo desde 2024-01-01 hasta 2026-01-01 exclusivo, manteniendo separados los dos semestres activos de 2024 y efectivo durante 2025; todavía no se atribuye resultado a ese replay.
