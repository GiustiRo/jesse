# Continuidad r27

El diagnóstico K1001 está terminado y revisado. Primero se entendieron los192 trades originales; sólo después se aprobó documentalmente el siguiente experimento. No repetir diagnóstico ni K original. Fuentes y resultados en referencias de revision.json.

La propuesta de instrumentar candidatos bloqueados queda HOLD: cero fuentes/jobs. Cambia la decisión hacia dos escenarios nativos, LONG_ONLY y SHORT_BOOK(core→suplemento), cada uno con totalBTC10.000 y sólo su cuota1% activa. legacy_plan usa .5*balance y .5*available_margin; conserva2% interno, reserva/lote y3x. Cuota inactiva sin redistribución. No son dos cuentas financiadas simultáneamente ni curvas sumables. K original2% sólo referencia y diferencia no causal de ocupación.

Implementación nueva prevista: QuotaBase1m/LongOnly1m/ShortBook1m con prefijoBtcResearchR16K1001. before parent literal; no capturar ni recomputar suplemento. Rprecio observado obligatorio en ambas, parentobserve una vez, open0/pre estricto/exitfill antes FINAL. Padres intocados.

Siguiente: readback de fuentes/revisión, checks sintéticos en1slotanalysis, manifiestos con formularios genuinos antes de motores. Exactamente2economías nuevas previstas, ninguna ejecutada en esta publicación. Luego auditar ambas incluso negativas.48económicaspreviasdesde r9; análisis no son backtests ni muestrasindependientes. No nueva economía2026, estrés, variantes de riesgo, USDC, cartera, live/paper, instalaciones ni configglobal. Objetivo no alcanzado; autonomía continúa.
