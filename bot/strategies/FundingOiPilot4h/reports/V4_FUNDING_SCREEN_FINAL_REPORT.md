# V4 FUNDING_RESET: cierre SIN_CANDIDATA

Ambas variantes fallan screening prerregistrado [2020-09-01,2024-01-01), BTC-USDT1h: muestra<30, neto negativo y PF<1.2. No hay shortlist de esta línea ni autorización de WF, vecinos, fricción o economía2024–25 V4.2026 sigue cerrado. El pasado2020–2025 ya fue visto por ciclos previos: no se presenta como OOS virgen.

| Sesión | Trades | Neto% | PF trades | DD motor% |
|---|---:|---:|---:|---:|
| [FUNDING_FP](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068) | 26 | -6.927536 | 0.590182 | -12.707734 |
| [FUNDING_FPOI](http://localhost:9200/#/backtest/786b270b-f497-4f48-b254-648ab7ea63af) | 12 | -7.656150 | 0.268212 | -8.551299 |

No se retocaron parámetros ni fuentes para reparar la economía. FundingFP saldo9307.246387, fees183.667556 y financiación−23.183822; FPOI saldo9234.385045, fees74.996173 y financiación−1.095742. La conciliación financiera completa de snapshots corresponde a root; el rechazo por gates ya es inequívoco y no requiere evaluar una reserva futura.

## Contadores y cobertura técnica

Se recorrieron TODAS las líneas por MCP,59páginas para cada sesión:12576FP y12410FPOI, sin saltos de next_offset. Máximos1029/1025caracteres.40meses y101buckets materializados por sesión;29208decisiones. FP26entradas/26cierres, FPOI12/12. allowed=entradas y sumas de causas/particiones direccionales verificadas.

Cada sesión tiene3651eventos únicos y7302bloques canónicos16+16. Todos3651SHA por sesión se recalcularon sobre tokens JSON originales, sin cambiar representaciones float. Accessor raw y último row coinciden3651/3651; timestamps disponibles<=decisión y antigüedad<=2h. Cero mismatches, gaps o unpublished. Baseline, sigma y z fueron recalculados independientemente para3572pares no constantes;78sigma0 y1inicialización.122resets financieros potenciales:95rechazos de precio y27confirmaciones.

Feature causes comunes por sesión:1funding_initialization,25557funding_repeated,3450funding_no_reset,78funding_sigma_zero,95funding_regime_reject,27funding_reset. FP permite26entradas y bloquea1señal por posición pendiente/abierta; FPOI permite12 y rechaza15por OI no creciente. En ambos hay1decisión final boundary_or_inactive que reemplaza el primaryfunding_repeated:25556primaryrepeated. El evento rechazado se consume y no se reintenta.

Se verificaron todos38planes nominales: precio/fill,ATRactual2x,stop desde fill,targetNone,sizing con fees2%,cap1x y cuota UTC. Las12entradasFPOI muestran OIqualityvalid/passed.38cierres presentes y ninguna entrada coincide con cierre anterior.21salidasSMA24 enFP y8enFPOI cumplen estado adverso yT>opened_at; restantes5/4sonstop-loss. No hubo maximum_hold,calendar_boundary nifold_end real: no se afirma cobertura de esas ramas por estos runs; están cubiertas por checks deterministas comunes.

Las fuentes pasaron staticfinal7e94800d008b4cba84b7aa8f4d9ab6af; smoke técnico previo completó52checkssectoriales+61comunes y21eventos/42bloques verificados sin trades. Auditorías económicas no ejecutaron nuevos jobs ni editaron el framework, core ni versiones previas.

## Evidencia y límites

AUDIT_ResearchV4FundingFP1h_SCREEN.json y AUDIT_ResearchV4FundingFPOi1h_SCREEN.json conservan todos los buckets, entradas, planes, cierres, salidasindicadoras, manifiesto hash del conjunto de eventos y ventanas inicio/medio/final más cada entrada. Aunque se verificaron todos los hashes durante el barrido, el archivo de auditoría conserva sólo esas ventanas seleccionadas; las restantes permanecen en los logs originales de la sesión. V4_FUNDING_FINAL_COUNTERS.json resume el cierre y V4_FUNDING_PROGRESS.json conserva configuración completa, respuestas crudas y timestamps.

La comparación independiente de valores usa tolerancia numérica1e−9 para evidencia float, sin cambiar desigualdades de señal ni ejecución. La confirmación de precio se verifica desde los contextos registrados; construcción de velas/semillas se acredita por fuentes estáticas y checks, no por reconstrucción completa de candles desde logs. La contabilidad de fees/funding/equity/trades y órdenes es central. OI usa archivo retrospectivo con disponibilidad supuesta, no certificación point-in-time. Resultado final de la línea: SIN_CANDIDATA.
