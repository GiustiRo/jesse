# V3 — confirmación y robustez completas

Estado: SIN_CANDIDATA, con avance parcial P. Datos [2024-01-01,2026-01-01), fin exclusivo,731días; no velas2026.10000USDT por cuenta continua nominal; funding histórico y costes explícitos. La shortlist congelada mantuvo OI/P; no se reordenó después de ver evaluaciones.

## Walk-forward

| Fold | P neto % | POI neto % | Selección previa |
|---|---:|---:|---|
|C1|16.3146|11.9916|OI por DDtrain|
|C2|18.9449|0.8132|OI por DDtrain|
|C3|1.8703|2.9807|OI por DDtrain|
|C4|-1.9242|5.6961|OI por DDtrain|

Cuatro trains expansivos aprobaron ambas; el selector global eligió OI por menor DDtrain en los cuatro folds. Cada SELECTION_V3_C*.json se guardó antes de runs correspondientes; auditoría independiente PASS en V3_CONFIRMATION_CHRONOLOGY_AUDIT.json. Trains C1 reutilizados exactamente;14 sesiones nuevas faseB,16slots. Todas las finalistas se evaluaron, pero P no reemplaza retrospectivamente al selector OI.

## Replays y pruebas predefinidas

| Familia | Escenario | N | Neto % | CAGR % | PF neto | DDmotor % |
|---|---|---:|---:|---:|---:|---:|
|P|NOMINAL|95|38.2259|17.5435|1.3485|-18.4140|
|P|S1|95|29.4462|13.7543|1.2712|-19.4237|
|P|S2|96|26.2630|12.3489|1.2310|-21.8733|
|P|S3|97|7.5006|3.6774|1.0651|-24.0833|
|P|N09|105|8.8101|4.3061|1.0731|-24.8434|
|P|N11|92|33.6787|15.5965|1.3307|-18.8690|
|P|LAG1 reutilizado|95|38.2259|17.5435|1.3485|-18.4140|
|Oi|NOMINAL|84|22.8903|10.8403|1.2598|-17.1684|
|Oi|S1|84|16.3330|7.8466|1.1870|-18.1007|
|Oi|S2|85|13.1766|6.3755|1.1433|-18.6503|
|Oi|S3|86|-2.3070|-1.1587|0.9756|-23.8137|
|Oi|N09|90|7.4787|3.6668|1.0744|-20.5495|
|Oi|N11|82|20.2319|9.6365|1.2468|-15.8538|
|Oi|LAG1|73|30.6130|14.2652|1.4750|-13.7970|

S1fee0.0009/slip0;S2fee0.00045/slip5bps;S3fee0.0009/slip10bps. Neighbors N09stop1.8A/trail2.7A,N11stop2.2A/trail3.3A, con fee/slip nominales. LAG1OI retrasa4h la información y referencia, respeta freshness original; P sinOI reutiliza nominal. Mismos cuatro intervalos separados de exposición nominal, sin reentrenar ni seleccionar en estrés.

P nominal:2024+38.3503%;2025−0.0899%. CAGR17.5435% combina un año fuerte con otro prácticamente plano; no equivale a20–30% cada año. Tres semestres positivos. Único gate nominal fallido:95<100. S1/S3 yambos vecinos siguen netos>0/DD<=25, pero N09 queda cerca del límiteDD24.8434 y beneficio8.8101%, versus nominal38.2259: sensibilidad económica relevante aunque pase el gate.

OI nominal:2024+12.9023%;2025+8.8466%;cuatro semestres positivos. FallaN84<100 yCAGR10.8403<15, además S3net−2.3070% implicaFRÁGIL. Su lag sale mejor pero no se promueve ni sustituye nominal. Ningún vecino se elige como estrategia nueva.

## Contabilidad y equivalencia

33 sesiones económicas únicas+3smokes,36slots económicos nominales (incluyen2trainsC1reutilizados ylagP). Todas finished; IDs únicos sin duplicaciones por timeouts. Máximo error de conciliación4.92e−11USDT; config/datasets/fechas/rates/cantidades/fills/saldos verificados. S2fillsajustados192P/170OI;S3 194P/172OI, proveniencia de slippage coherente con bps adversos de órdenes ejecutadas MARKET/STOP.

Comparación independiente diez snapshots:179/179 entradas/fechas/direcciones y tiempos de salida coinciden con WF; cantidades cambian con capital. Diferenciareplay vsWFreescalado P−0.000059USDT,OI+0.000113USDT por cuantización/redondeo. PF se calcula con trades propios; no se suman PF. El selector WFreescalado es aproximación rotulada, el replay es cuenta real simulada sin reset. No posiciones/cashflows en los cuatro bordes nominales: no hubo impacto observable de reinicialización OI aquí, ni ejercicio nominal de liquidación de calendario.58checks estáticos verifican las ramas; no acreditan fills reales del motor cuando no hubo evento.

Funding nominal2024–25 usa marcas de liquidación, sin proxy: sensibilidad proxy-only0.5/1.5 no cambia PNL. Sensibilidad global con cantidadesfijas: Pnet3979.8115/3665.3598USDT;OInet2427.1286/2150.9240; sin cambio de signo. No son replays ni nueva candidata. Fuentes exactas/cashflows separados en análisis nominales.

## Límites

2024–25 es reserva interna reutilizada, no OOS virgen. OI archivo retrospectivo noPIT, lag6min supuesto ymaxage10min desde disponibilidad; funding publicado con demora yrawjitter<=1s normalizado a effective_at. Auditor inicial que comparórawsettled_at conclosed_at falló por11–18ms de proveedor; diagnóstico y corrección preservados, sin cambiar economía. DDmotor usa curva muestreada; no garantiza máximo intraminuto. Ejecución1m/OHLC, qty8decimales y profundidad/latencia no certificadas. No live/paper/Pi/2026 ni ML.

Fuentes completas congeladas:V3_IMPLEMENTATION_SOURCE_20261020.md,V3_CONFIRMATION_WRAPPERS.json,V3_REPLAY_IMPLEMENTATION_SOURCE_20261020.md. Matrices/configs/IDs y resultados completos:REGISTRY_V3.json yV3_FINAL_METRICS.json. Comparación yraws en informes vinculados; jobs analíticos temporales exportados a artefactos persistentes.
