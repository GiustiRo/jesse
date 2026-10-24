# V2 — ejecución paralela autorizada
Fecha UTC: 2026-10-20T22:43:19.852Z.
El usuario autoriza continuar la investigación de forma autónoma, con un subagente por sector nuevo y hasta dos backtests simultáneos por subagente.
Sectores nominales ya congelados: H1_ATR_P y H1_ATR_POI, un subagente para cada uno. Un tercer subagente audita snapshots; root registra selecciones y es único escritor de REGISTRY_V2.json.
Esta instrucción reemplaza la restricción operativa anterior de un backtest activo. Máximo operativo inicial: cuatro motores simultáneos (dos por sector). Si el servicio presenta errores o demoras, reducir concurrencia sin cambiar reglas económicas ni duplicar runs.
Se permite ejecutar evaluación del fold actual y preparar entrenamiento del siguiente en paralelo, porque ambas decisiones ya pertenecen a ventanas cerradas y el train siguiente no habilita su evaluación por sí mismo. Cada evaluación nueva requiere que root guarde primero selección del fold correspondiente basada exclusivamente en sus cuatro trains.
La selección E1 SIN_CANDIDATA fue guardada en 2026-10-20T22:33:49.399Z; las nuevas E1V aún no fueron iniciadas. No se cambia ninguna selección V1/V2 previa ni regla/umbral, datos, fuente, shortlist o presupuesto.
Primera tanda: E1V+E2T de ambas ramas; siguientes: E2V+E3T, E3V+E4T y E4V, siempre detrás de su selección previa. Root conserva la dependencia cronológica aunque cálculo de train siguiente termine antes.
Los archivos de progreso de rama son V2_BRANCH_P_PROGRESS.json y V2_BRANCH_POI_PROGRESS.json, sin escritores compartidos. Auditoría de cuatro sesiones por etapa mediante run_analysis y snapshots completos; un auditor coordina la cuota de jobs.
No nuevas familias económicas sin protocolo específico previo y subagente dedicado. El paralelismo no autoriza más configuraciones ni ampliar presupuesto64slots.
Confirmación2024–2025 sólo tras shortlist congelada, estrés sólo segúnprotocolo. 2026 cerrado, sinML/live/paper/Pi/cuentas/reinicios/instalaciones/commit/push.
