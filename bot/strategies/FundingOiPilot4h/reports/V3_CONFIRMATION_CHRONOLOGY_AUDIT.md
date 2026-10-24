# Auditoría independiente de cronología V3 — C1 a C4

**PASS: cuatro selecciones anteriores a sus evaluaciones y calendarios individuales coherentes.** Revisión por MCP; sin motores, jobs ni cambios productivos. Observación final de progreso: 2026-10-20T23:45:58+00:00. C4 se incorporó sólo con selección, calendario y metadatos de progreso; no se consultaron métricas económicas C4V.

Shortlist guardada 2026-10-20 **23:27:55 UTC**, acuse conservador 23:28:15 UTC, anteriores a todos los arranques.

| Fold | Selección guardada UTC | Evaluación | Solicitud UTC | Margen |
|---|---|---|---|---:|
| C1 | 2026-10-20T23:28:15+00:00 | [ResearchV3CH_P_C1V](http://localhost:9200/#/backtest/1ead2e5d-d907-43b2-8e9d-925aea5e3093) | 2026-10-20T23:29:35.321Z | 80.321 s |
| C1 | 2026-10-20T23:28:15+00:00 | [ResearchV3CH_OI_C1V](http://localhost:9200/#/backtest/faeccf79-ea48-4d5a-93bf-8ab77a0c8095) | 2026-10-20T23:29:53.811Z | 98.811 s |
| C2 | 2026-10-20T23:34:31+00:00 | [ResearchV3CH_P_C2V](http://localhost:9200/#/backtest/e670ca1a-26d3-42d3-94de-a4292b6ae972) | 2026-10-20T23:35:10.887Z | 39.887 s |
| C2 | 2026-10-20T23:34:31+00:00 | [ResearchV3CH_OI_C2V](http://localhost:9200/#/backtest/0ca32a2d-e9b5-4420-94bd-58113244d560) | 2026-10-20T23:35:29.639Z | 58.639 s |
| C3 | 2026-10-20T23:39:28+00:00 | [ResearchV3CH_P_C3V](http://localhost:9200/#/backtest/03753b45-bdb2-45c9-88ca-015a2bd374c5) | 2026-10-20T23:39:58.762Z | 30.762 s |
| C3 | 2026-10-20T23:39:28+00:00 | [ResearchV3CH_OI_C3V](http://localhost:9200/#/backtest/2004cd16-ad77-4d80-b1bd-0e54809126bf) | 2026-10-20T23:40:17.448Z | 49.448 s |
| C4 | 2026-10-20T23:44:31+00:00 | [ResearchV3CH_P_C4V](http://localhost:9200/#/backtest/36b23618-bda4-44b3-b1c1-e9e97fdd23a1) | 2026-10-20T23:45:18.729Z | 47.729 s |
| C4 | 2026-10-20T23:44:31+00:00 | [ResearchV3CH_OI_C4V](http://localhost:9200/#/backtest/2ebd9039-498f-4bd7-9cc3-dbf36fb77682) | 2026-10-20T23:45:36.353Z | 65.353 s |

Se conservan respuestas raw completas en JSON. C4 P y OI figuraban start_requested; el timeout HTTP OI queda asociado a la misma ID, sin duplicar sesión. La creación de un draft no equivale a ejecución o consulta de resultados y puede preceder selección: el criterio auditado usa start_requested_at y raw run.

C1 reutiliza exactamente SCREEN:

- [ResearchV3ChannelOi4h](http://localhost:9200/#/backtest/eb4ea7d5-dc0c-4f08-9450-1584f49cdfe0): misma sesión, ventana 2020-09-01→2024-01-01, configuración nominal y métricas coincidentes.
- [ResearchV3ChannelP4h](http://localhost:9200/#/backtest/05828944-d350-4852-b13d-af24c2815bc5): misma sesión, ventana 2020-09-01→2024-01-01, configuración nominal y métricas coincidentes.

Cinco dependencias económicas CHANNEL/base/helper fueron comparadas completas con los textos archivados congelados y coincidieron. Los hashes consignados son los del manifiesto previo, sin nuevo hashing job.

**OI seleccionado en C1–C4 por menor drawdown absoluto train**, 22,7195696% frente a 23,6201155% de P. No se activan desempates posteriores. P ganó más en C1eval (16,3146258% frente a 11,9915798%), pero esa evaluación sucedió después de su selección. En C3 y C4 P tiene también mayor net/PF train, sin desplazar a OI: DD sigue siendo la primera clave. Decisiones anteriores preservadas, sin reconstrucción usando retornos futuros.

El calendario V3_REPLAY_CALENDARS_FROZEN.json se guardó **23:44:31 UTC**, antes de ambos arranques C4V. Comprobación independiente sobre las cuatro selecciones: ambas variantes pasan en cada train n>=30, net>0, PF>=1,2 y |DD|<=25. Cada calendario mantiene exactamente estos cuatro intervalos separados, sin fusionarlos:

| Fold | Inicio inclusivo | Fin exclusivo |
|---|---|---|
| C1 | 2024-01-01 | 2024-07-01 |
| C2 | 2024-07-01 | 2025-01-01 |
| C3 | 2025-01-01 | 2025-07-01 |
| C4 | 2025-07-01 | 2026-01-01 |

Sellos milisegundo coinciden con fechas UTC; force_boundaries coincide exactamente con los cuatro finales. Configuración del calendario coincide con nominal congelada. Elegibilidad individual permite conservar los cuatro semestres de P aun cuando nunca fue elegido por el selector global, que contiene OI en C1–C4. No se cambia exposición futura por evaluación o estrés.

Para contabilidad se usa **effective_at** y se conserva settled_at raw: V3_FUNDING_RAW_VS_EFFECTIVE_CLOCK_DIAGNOSTIC.json documenta jitter raw de 11–18 ms al cierre. Tfinish como reloj final de decisión/cierre basado en última vela histórica no introduce datos 2026; 2026-01-01 sigue siendo límite exclusivo.

Alcance: timestamps guardados no constituyen un log inmutable de todos los accesos históricos. Se verifica la evidencia de selección/calendario→solicitud y raw run, sin afirmar ausencia exhaustiva de consultas externas. El job train C4 f94a1dbe444a412db93274164b909754 fue informado por root; esta revisión cronológica no lo reejecuta ni valida sus snapshots económicos. Detalle íntegro en V3_CONFIRMATION_CHRONOLOGY_AUDIT.json.
