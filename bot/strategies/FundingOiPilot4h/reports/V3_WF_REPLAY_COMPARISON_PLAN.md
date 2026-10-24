# V3 — comparación independiente WF frente a replay

Estado: código preparado, **sin ejecutar**. Fuente: V3_WF_REPLAY_COMPARISON_SOURCE.json. Diez inputs completos: ocho evaluaciones C1–C4 P/OI y dos replays nominales, cuyos IDs permanecen como placeholders hasta recibirlos finished de root. Un único run_analysis autorizado para entonces; no crea motores ni nuevas sesiones.

El análisis conserva selector global OI en los cuatro folds y calendarios individuales elegibles de cuatro semestres separados para ambas variantes. Compara por equity los retornos de cada semestre del replay continuo y de cada evaluación reiniciada en10000. Calcula además producto sintético de ratios WF reescalados para cada variante y selector global, rotulado como comparación hipotética, sin equipararlo a una cuenta ejecutada. CAGR usa731 días completos y saldo terminal real; ni suma de PNL cerrados para semestres ni PF sumados/promediados.

Portfolio diario usa convención−61s salvo punto inicial; sólo el mes terminal se sustituye por finishing_balance postcierre, conservando curve_terminal_delta. No fabrica equity intraminuto. Registra muestras originales, diferencias equity/rebase y retornos semestrales de la misma cuenta.

Entradas se emparejan por opened_at y dirección, sin exigir mismas cantidades, salidas o precios. Exporta conjuntos exclusivos y coincidencias, ratiosqty, igualdad de precio/tiempo de salida y entradas de primeras28h. Distingue diferencias observadas de hipótesis causales: continuidadcapital/historiaOI/cuotas y trayectoria previa pueden interactuar.

En cada borde exporta ledger efectivo exacto y vecino±1min, cashflow, candidatos de posición, entradas/cierres exactos, órdenes ejecutadas vecinas y primera entrada posterior. Usa effective_at y conserva timestamps raw; entrada MARKETT sucede después de fundingT, salida MARKETT todavía puede pagarlo. Un cierre protector precedente exige inspección de órdenes. Final exclusivo2026Jan1 no admite ledger>=finish. WF finish-exclusive y replay con cierre interno pueden diferir legítimamente en funding de borde.

Limitación expresa: snapshots backtest no incluyen logs V3_AUDIT/V3_ENTRY. Inicialización nominal seis decisiones4h, reiniciada por sesión WF y continua entre bordes replay, es expectativa de fuente congelada; sin logs no se atribuirán diferencias inequívocamente a OI. Los dueños pueden guardar evidencia complementaria por MCP fuera del job; no se pegarán arrays de logs ni resultados en el código como sustituto de snapshots completos.

Este análisis es diagnóstico y no impone gates nuevos ni altera decisiones. Root concilia contabilidad y gates del replay en otro job. El código sólo lee inputs/ y escribe output/wf_replay_comparison.json. No ha sido compilado ni ejecutado durante esta preparación.
