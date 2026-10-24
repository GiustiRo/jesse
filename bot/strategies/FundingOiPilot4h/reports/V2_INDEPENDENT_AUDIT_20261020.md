# Auditoría independiente V2 — cierre de exploración
Fecha: 2026-10-20. Sólo Jesse MCP local para sesiones, snapshots y artefactos. No se iniciaron backtests desde este sector auditor.

Se conciliaron E1V,E2T,E2V,E3T,E3V,E4T,E4V por etapas de cuatro sesiones, incluyendo controles fijos V1 reutilizados. E1T utiliza evidencia ya guardada en WALK_FORWARD_E1T_RESULTS_V2.md. Los entrenamientos expansivos se conservaron separados; no se sumaron sus operaciones repetidas.

Las selecciones E1–E4 fueron SIN_CANDIDATA. Ninguna configuración superó los gates de su entrenamiento; las dos ATR mejoran descriptivamente protección, costos y evaluaciones, pero no cumplen el protocolo de promoción. Los cuatro semestres positivos de ATR_POI no convierten esa configuración en seleccionada antes de evaluar. La shortlist debe permanecer vacía y no corresponde abrir confirmación/estrés ni2024–2025 para estas reglas.2026 no fue consultado por esta auditoría.

## Cuatro evaluaciones por configuración
| Configuración | Trades únicos | Suma nominal netos USDT | PF agregado | Semestres positivos | Neto sin mejor semestre USDT |
|---|---:|---:|---:|---:|---:|
| H1_ATR_P | 332 | 2004.83 | 1.093 | 3/4 | 157.45 |
| H1_FIXED_P | 342 | -754.85 | 0.975 | 1/4 | -2787.33 |
| H1_ATR_POI | 223 | 2474.37 | 1.172 | 4/4 | 1392.89 |
| H1_FIXED_POI | 228 | 872.46 | 1.042 | 2/4 | -321.63 |

Cada semestre comienza con10.000USDT. Estas sumas de PnL y el PF de trades nominales no son rentabilidad de una cuenta continua ni rendimiento anual. No se agregan configuraciones entre sí y sus muestras no son independientes. El índice del selector permanece plano24meses por ausencia de exposición, no por probar rentabilidad.

ATR frente a FIXED con igual uso de OI reduce DD y turnover en los cuatro semestres; mejora neto en E1,E2,E4 y lo reduce en E3. Las salidas modifican ocupación, sizing y entradas futuras; no se identifica un efecto puro del stop entre trades idénticos. El ATR nominal con OI presenta PF1,172, aún por debajo de1,2; no se redondea para aprobar.

## Integridad
Run_analysis usó snapshots completos; nominal config, estrategia y ventanas exactas se validaron antes de analizar. Precio bruto−fees+ledger funding=PNL, fees sobre fills, funding por trade y saldo final conciliaron. Error máximo en las etapas nuevas auditadas:5,093170329928398e-11USDT (E4T); en las cuatro evaluaciones agregadas:1,4551915228366852e-11USDT. Tolerancia1e-6.
PF se reconstruyó dividiendo PnL positivo por absoluto del negativo. La exposición deriva de segundos en posiciones y duración de sesión, turnover del notional de fills/10000. Se guardan24meses completos por configuración en V2_FINAL_COMPARISON.json y los resultados por etapa, sin promediar PF ni sumar DD.
Los indicadores total_open_trades/open_pl pueden capturarse antes del cierre forzado del framework. En ATR_P E1V y E4V, las auditorías de sector confirman cierre fold_end posterior al resumen; el snapshot contiene90 y69 trades cerrados respectivamente y sus saldos concilian. No se infiere una posición residual activa desde esos indicadores.
Las etiquetas de equity00:00/00:01 se asignan al día previo con61segundos de desplazamiento, excepto saldo inicial, igual queV1. Es resolución diaria aproximada; no acredita DD intraminuto de un índice reescalado.

## Límites
Exploración2022–2023 ya observada; controles y ventanas conocidos no son validación independiente. Los cargos funding conservan marcas proxy y OI es archivo retrospectivo sin certificación point-in-time. El nominal usa slippage0; la prueba técnica de fills adversos no demuestra robustez económica. No se ejecutaron bootstrap, MonteCarlo, nuevos parámetros, operaciones live/paper ni accesos a cuentas desde auditoría.
Los timeouts de arranque que reportaron los sectores no se trataron como fallos económicos ni se duplicaron sesiones. Root conserva las respuestas crudas y cronología. Una lectura de progreso auditor se paginó al exceder1000líneas; no implicó mutaciones.

## Evidencia
- V2_AUDIT_E1V.json, E2T, E2V, E3T, E3V, E4T y E4V: fuente de análisis, manifiestos y resultados.
- V2_FINAL_COMPARISON.json: agregados, comparaciones ATR/FIXED por fold, meses, costos, dirección, exposición y concentración; fuentes completas de los dos jobs finales.
- Jobs finales:44602b6f1f6f4279844c048955092cec, 56bde294ea06424aab344fb7a0f77c9a.
- Las URLs reales de cada sesión están en esos artefactos y en los reportes de root. No se sustituyen por IDs como enlaces inventados.

Conclusión auditora: integridad contable y separación cronológica de selección respaldadas por la evidencia disponible; V2 cierra sin candidata bajo sus reglas, aunque las distancias por volatilidad ofrecen una mejora exploratoria que podría motivar una hipótesis futura declarada. Este resultado no autoriza retuning dentro deV2 ni promoción de su mejor evaluación.
