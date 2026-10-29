# V6 EFFICIENCY: costes prescritos

Los tres escenarios de costes finalizaron con contabilidad completa y logs PASS. S1 y S3 fallan la robustez prescrita por rentabilidad negativa; S2 es informativo. El rechazo nominal queda inmutable.

| Escenario | N | Net % | PF | DD % | CAGR % |
|---|---:|---:|---:|---:|---:|
|NOMINAL|44|0.278594|1.006229|-17.553569|0.139010|
|S1|44|-1.920348|0.957002|-18.627561|-0.963515|
|S2|45|-4.027645|0.915336|-20.875287|-2.031764|
|S3|45|-7.895715|0.836047|-23.171310|-4.023624|

S1 usa fee 0.0009 y slip 0; S2 fee 0.00045 y slip 5 bps; S3 fee 0.0009 y slip 10 bps. Cada escenario ejecuta su propio motor con capital continuo inicial 10000, el mismo calendario ON/ON/OFF/OFF y cuatro bordes fijos. Los tamaños se recalculan con su comisión y capital; no se resta un coste a cantidades congeladas. La primera entrada pasa de 0.14083594 BTC nominal a 0.13695228 BTC con comisión duplicada. Los 44 tiempos de entrada comunes conservan hashes de señal idénticos. El deslizamiento produce una secuencia de 45 operaciones en S2/S3.

Los snapshots validan precios ajustados, comisiones, financiación, libros completos, ausencia de posiciones/funding durante 2025 y efectivo constante en sus doce meses. Los logs validan capital por entrada, ventanas, stops desde fill, riesgo y cap, UTC, sin TP ni cambios de calendario. Evidencias completas en V6_REPLAY_{S1,S2,S3}_ACCOUNTING.json y sus LOG_AUDIT; comparación de tamaños en V6_REPLAY_COST_QUANTITY_COMPARISON.json.

El nominal también es frágil a una sensibilidad contable de financiación global ×1.5: net −0.946104%. Esa sensibilidad mantiene cantidades fijas y se etiqueta como diagnóstico; los costes de la tabla son replays reales.
