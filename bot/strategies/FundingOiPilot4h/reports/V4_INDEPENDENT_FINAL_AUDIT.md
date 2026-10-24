# V4 — auditoría final independiente

Fecha 2026-10-21T00:38:08.120Z. Auditor /root/atr_oi. Resultado: PASS de coherencia documental, gates, presupuesto, métricas centrales, sesiones y fuentes. La auditoría detallada FUNDING_FPOI ya fue entregada y leída: PASS; se retira el límite provisional anterior. Esta revisión conserva el alcance específico de cada evidencia. No se modificaron archivos centrales, ni se iniciaron jobs/motores.

Se leyeron por MCP, paginados completos: protocoloV4, V4_FINAL_METRICS.json, REGISTRY_V4.json (ECONOMIC_COMPLETE_FINAL_AUDIT), FROZEN_SHORTLIST_V4.md, WALK_FORWARD_EXPLORATION_V4.md, WALK_FORWARD_CONFIRMATION_AND_STRESS_V4.md, snapshotfinal yverificaciónfuentes/sesiones. Se consultaron directamente summarys de las9sesiones ylas14fuentesactuales.

## Gates y decisión

SCREEN exige N>=30, neto>0, PF>=1.2, absDDmotor<=25% y>=2/3años completos2021/22/23positivos.2020parcial queda fuera. N100/CAGR15% pertenecen a replay final, no a SCREEN; no se aplicaron indebidamente ni se relajaron.

| Variante | N>=30 | Neto>0 | PF>=1.2 | DD<=25 | Años positivos | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| ResearchV4OscillatorP1h | sí | NO | NO | NO | 1/3 | RECHAZADA |
| ResearchV4OscillatorOi1h | sí | NO | NO | NO | 0/3 | RECHAZADA |
| ResearchV4ShockPV1h | sí | NO | NO | NO | 0/3 | RECHAZADA |
| ResearchV4ShockPVOi1h | sí | NO | NO | NO | 0/3 | RECHAZADA |
| ResearchV4FundingFP1h | NO | NO | NO | sí | 0/3 | RECHAZADA |
| ResearchV4FundingFPOi1h | NO | NO | NO | sí | 0/3 | RECHAZADA |

Los flags base_eligible,screen_year_gate,screen_eligible coinciden con los cálculos independientes para6/6. Todas pierden yPF<1.2;OSC/SHOCK además DD>25;Funding además N26/N12. Shortlistvacía yselections/finalistsvacíos correctos. No hay fundamento para avanzar a confirmación ni cambiar reglas.

## Métricas, presupuesto y cronología

Seis filas finales coinciden exactamente con las filas correspondientes deREGISTRY; N/net/DD coinciden con summarys almacenados dentro de1e−6. Bruto−fees+funding=neto,capitalfinal−10000=neto yproxy+exacto+sinclasificar=funding concilian dentro de1e−6. Máximo errorcentral reportado1.000444171950221e−11USDT. Cada fila incluye40meses, cuatroaños identificados con2020parcial,fuentesfundingclasificadas ysinclasificar0. Este control revisa coherencia de resultados de snapshots centrales; no vuelve a procesar los ledgers completos.

Se consumieron6/40slots económicos y3/6técnicos.34omitidos=16WF+2replay+6cost+8neighbors+2lag. Los tres slots técnicos no usados son reserva de reemplazo porerror, no economía adicional. Las9IDs son únicas ysummarysactualesfinished/errornull:3smokes[2020Sep1,Sep8) y6SCREEN[2020Sep1,2024Jan1). Configsnominalesexactas en9/9. No se observó evaluación V4 de2024+ni2026 enestasnuevesesiones.

No hay selector económico futuro V4, por lo que el documento acierta al no fabricar un índice/curva0% de2024–25. Costes/vecinos/lag no se ejecutaron; sensibilidades fundingcantidadesfijas son descriptivas deSCREEN yno sustituyen robustez de motor.

## Fuentes y límites

Readback directo14/14fuentes coincide exactamente con snapshot congelado; SHA declarados del snapshot coinciden conREGISTRY. No se calculan hashes nuevos ni se invoca otro job. Las9sesiones yla verificación central conservan source_equaltrue. Al reconstruir inicialmente una copia del snapshot paginado se insertó localmente un salto extra entre páginas; se corrigió concatenando los contenidos sin añadir salto, yfunding_features coincide exactamente. No fue un cambio de archivo productivo ni divergencia real.

Auditorías técnicas no convierten PnLnegativo enéxito. FundingSmoke no tuvo fills; suPASS_NO_FILL_COVERAGE estápreservado. OIarchivo retrospectivo+disponibilidadasumida noPIT;el pasado ya fue observado en ciclosprevios, sinOOSvirgen. El detalle FPOI fue entregado en V4_FUNDING_FINAL_COUNTERS.json y V4_FUNDING_SCREEN_FINAL_REPORT.md: ambas variantes pasan auditoría de eventos/gates/planes/cierres, además de contabilidad central.

No divergencias materiales detectadas. Cerrar V4 SIN_CANDIDATA con todos los reportes detallados entregados, mantener V1–V4 yavanceV3 separados;no reasignar34slots a mineríaadaptativa niabrir2026 para salvarresultados. Evidenciamáquina enV4_INDEPENDENT_FINAL_AUDIT.json.

## Actualización de cierre y consolidado V1–V4

Se leyeron V4_FUNDING_FINAL_COUNTERS.json y V4_FUNDING_SCREEN_FINAL_REPORT.md. Cada variante funding concilia3651eventos,3651hashes y7302bloques,29208decisiones,40meses;recalculo3572paresnormalizables,78sigma0,1inicialización y122contextosreset. Los27setupsconfirmados separten FP26entradas+1posiciónbloqueada y FPOI12entradas+15OI_nonrising. Total38planes/cierres,0mismatch.21+8salidasSMA24 y5+4stops;hold72h/calendario noejercidos por estos fills, limitación preservada. Se verificaron todas las ventanas en logs; auditorías conservan ventanas seleccionadas y no afirman persistirlas todas fuera de la sesión. Límite provisional retirado.

FINAL_DECISION_V4.md coincide con6filas completas deV4_FINAL_METRICS.json, reglas ycontadores. La suma deplanes774+464+461+279+26+12=2016 es porconfiguración, no cartera deoperacionesindependientes.248checks=61+87+48+52;9sesiones=6económicas+3técnicas. Fases omitidas yausencia de selector/futuro se mantienen.

RESEARCH_CONSOLIDATED_DECISION_20261020.md contrastado con FINAL_DECISION_V1/V2/V3,REGISTRY_V2/REGISTRY_V3 yV3_FINAL_METRICS.json:
- Económicas nuevas151=96+16+33+6.
- Slotsnominales170=96+32+36+6, con19reutilizaciones=16V2+3V3.
- Intentostécnicos17=7V1+4V2+3V3+3V4; no se mezclan conPNL.
- V3CHANNEL_P individual:38.225856%neto,CAGR17.543463%,PF1.348511,DD18.413964,N95<100,2024+38.350263%,2025−0.089921%. VecinoN09CAGR4.306074%, sensibilidadexpresa. S1/S2/S3/N09/N11mantienennetopositivo/DD<=25; no rescatanNnominal.
- V3selector train-only eligióOIen4folds segúnregistry,con replayN84/CAGR10.840253/PF1.259787 yS3−2.307014%; no reemplazo expost porP. Los179tradesnominales=95+84coinciden con el reporte de conciliación.
- La referenciaP no es candidata y2026siguecerrado para esta investigación. No se proponen nuevas variantes automáticas.

Precisión editorial resuelta por root y verificada por lectura: FINAL_DECISION_V4.md ahora dice «órdenes reales», diferenciando las órdenes simuladas auditadas. No queda divergencia editorial pendiente; esta rama no modificó documentos centrales.

Resultado definitivo de esta auditoría: PASS sin límites provisionales pendientes, conservando límites de datosretrospectivos yramas reales noejercidas. No nuevos jobs/motores/cambiosproductivos. Fecha actualización 2026-10-21T00:40:13.993Z.
