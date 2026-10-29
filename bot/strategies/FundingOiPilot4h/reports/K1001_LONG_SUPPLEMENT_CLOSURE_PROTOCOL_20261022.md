# K1001 long y suplemento: cierre diagnóstico
Fecha local2026-10-22. Reanálisis descriptivo, cero nuevos backtests o precios.

Pregunta: ¿la caída observada2024–25 proviene descriptivamente de menos aciertos, menor tamaño de ganadoras, pérdidas mayores o costos? ¿Qué muestran los cierres del suplemento? No identifica causas ni nuevos regímenes.

Inputs:203registros ya auditados de las cuentas alternativas LONG_ONLY31 ySHORT_BOOK172, con origen de logs, funding verificado y trazasM1+fills. Se suministran filas compactas del recibo previo, no nuevas consultas de mercado. CORE_SHORT sólo referencia diferenciada.

Grupos congelados: toda la muestra, aperturas2020 parcial separadas,2021–23 y2024–25 según comparación ya publicada. No elegir cortes, umbrales, filtros o trades favorables. Describir N, tasa de acierto neta, media ganadoras/perdedoras, media bruta/comisión/funding/netaR, máximo y giveback observados, duración y tipo nativo de salida. Desglose por salida para toda muestra y períodos, sin selección de ganador.

Identidades: media netR=pWin*mediaWin+pLoss*mediaLoss; grossR-feeR+fundingR=netR; maxR-givebackR=grossR por fila. Última es algebraica, no comparación causal con salida alternativa. Máximo censurado por salida propia, sóloM1+fills, no precio ejecutable ni MFEintraminuto. PF_R distinto de PFUSDT; no anualizar contribuciones del suplemento como cuenta independiente. N pequeño no certifica régimen estable.

Concentración long: tres mayoresR y resto como sumas aritméticas a tamaños normalizados congelados, sin reconstruir cuenta. Sin remover trades ni optimizar targets/BE/trailing. Presupuesto: un job de registros, artefactoJSON menor48k; conservar fallo si ocurre y corregir sólo técnica. Sin nuevo motor, scripts de proyecto,2026nuevo, imports/datasets, estrés, cambio de riesgo o live/paper.

Cierre: responder preguntas y preparar mapa de pruebas posteriores que pueda segmentar por comportamiento/entrada/régimen observable causal, no forzar Long/Short. No se ejecutan variantes económicas dentro de este protocolo.
