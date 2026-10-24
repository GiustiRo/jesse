# V5 — auditoría independiente de shortlist y selección C1

Resultado: **PASS**. Revisión por MCP de artefactos guardados, sin motores, jobs, cambios de estrategia o escritura del registro global. No se consultaron resultados económicos C1; las únicas consultas de sesiones fueron summaries SCREEN anteriores a 2024.

Se verificaron seis screenings únicos, cuatro elegibles y dos rechazados. Los gates se recalcularon con N, neto, PF, DD y años completos de V5_SCREENING_FINAL.json; 2020 parcial se excluyó.

| Orden | Variante | DD absoluto | Años positivos 2021–23 | Resultado |
|---|---|---:|---:|---|
| 1 | [ResearchV5FundingFPOi4h](http://localhost:9200/#/backtest/e5bd6218-1066-4181-9ee6-7d5de2fae0c4) | 13.022950% | 3/3 | Finalista |
| 2 | [ResearchV5FundingFP4h](http://localhost:9200/#/backtest/2c40635d-6a44-4bea-9a49-6b1ce1b8742d) | 15.723609% | 2/3 | Finalista |
| 3 | [ResearchV5CrossP4h](http://localhost:9200/#/backtest/50827027-6d6f-4c5d-8c23-5f2f91d7d971) | 17.695540% | 2/3 | Elegible fuera del cupo |
| 4 | [ResearchV5CrossOi4h](http://localhost:9200/#/backtest/642c5e9e-8705-4a9f-860d-d7ec071ef510) | 22.666194% | 2/3 | Elegible fuera del cupo |
| — | [ResearchV5VwapPV1h](http://localhost:9200/#/backtest/46f494e4-aca0-455e-979e-f279d3d87106) | 40.951584% | 1/3 | Rechazada |
| — | [ResearchV5VwapPVOi1h](http://localhost:9200/#/backtest/6b21c3d2-69f7-4d70-8f8d-56d69974c270) | 38.282996% | 0/3 | Rechazada |

El orden FUNDING_OI→FUNDING_FP→CROSS_P→CROSS_OI coincide con menor DD. No hay empate que invoque PF/turnover/features/ID. El límite fijo de dos finalistas excluye CROSS aunque tenga mayor retorno y PF de desarrollo. Las dos finalistas de funding son variantes correlacionadas del mismo mecanismo, no evidencia independiente por duplicación.

Shortlist guardada **2026-10-21 01:10:16 UTC**. Selección C1 guardada **01:11:54 UTC** y elige ResearchV5FundingFPOi4h por DD train de 13,022950% frente a 15,723609% de FP. Ambos pasan el gate train; no se usan retornos futuros para elegir.

C1train reutiliza exactamente SCREEN: mismas IDs, ventana2020-09-01→2024-01-01, estrategia, ruta4h, configuración nominal y métricas de selección. No se creó un entrenamiento distinto. Se compararon las cuatro fuentes económicas actuales —base4h, helper funding y dos padres— con sus textos congelados; coinciden y sus hashes archivados coinciden con REGISTRY_V5. No se ejecutó un nuevo hashing job.

Los14 wrappers actuales coinciden con el manifiesto. Sólo importan el padre y definen START/FINISH; fechas UTC y atributos coinciden. El job AST/hash de root16253360af274c78840d8f51f52b9693 terminó succeeded con14 verificados. No hay alteraciones de SMA120/C30, tres pagos, stop3ATR, hold180, targetnone, offset0 o política OI.

| Evaluación C1 | Solicitud UTC | Margen desde selección |
|---|---|---:|
| [ResearchV5FT_OI_C1V](http://localhost:9200/#/backtest/f9c5a6f5-e7f7-45f8-9cd4-c7f51bd977f0) | 2026-10-21T01:12:42.515Z | 48.515s |
| [ResearchV5FT_FP_C1V](http://localhost:9200/#/backtest/b3a5c7e3-99b2-4540-a928-6927af51a602) | 2026-10-21T01:13:02.344Z | 68.344s |

Evidencia: V5_C1_BRANCH_PROGRESS.json, prerun en estado draft/configuración exacta y respuestas raw de arranque preservadas en JSON auditor. FP tuvo timeout HTTP asociado a la misma ID; no autoriza duplicación. No se abrieron sus summaries económicos para esta revisión.

El primer draft muestra creación01:11:54 y la selección tiene resolución de un segundo: no puede demostrarse orden estricto entre ambos con esos sellos. El segundo se creó01:11:55. La creación de drafts no es ejecución ni consulta de resultados; el orden relevante selección→arranque es inequívoco para ambos. Los timestamps guardados tampoco sustituyen un log inmutable de todos los accesos históricos.

Detalle completo en V5_C1_SELECTION_INDEPENDENT_AUDIT.json. V6 permanece separado y congelado antes de su desarrollo; esta auditoría no cambia ni consulta su economía.