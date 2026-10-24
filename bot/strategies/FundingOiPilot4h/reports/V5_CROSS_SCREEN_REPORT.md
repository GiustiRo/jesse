# V5 CROSS — auditoría de screening

[P terminado](http://localhost:9200/#/backtest/50827027-6d6f-4c5d-8c23-5f2f91d7d971):77trades,+90,529182% neto del período,DDmotor−17,695540%,37,49s. [POI terminado](http://localhost:9200/#/backtest/642c5e9e-8705-4a9f-860d-d7ec071ef510):57trades,+60,070882%,DDmotor−22,666194%,50,10s. Son40meses de desarrollo2020Sep→2024Jan, no retornos anuales. Root determina PF/años/gates y selección mediante snapshots completos; esta auditoría de ejecución no implica promoción.

Ambas sesiones fueron creadas/arrancadas por root tras tres smokesPASS. Root conserva raws y timeoutPOI resuelto en mismoID sin retry. El owner no inició nuevos motores/drafts/jobs ni alteró REGISTRY. Ambos tokens se devolvieron al terminar.

Por variante:40meses/7302barras4h, config nominal exacta contra smoke congelado, fuentes sectoriales4/4 idénticas trasSCREEN. Parámetros20/80,stop3ATR,hold180,targetnone,offset0 yreferenciaOI6barras. Logs completos2223(P)/2006(POI),trades completos77/57 leídos hasta has_morefalse y guardados en archivos_LOGS/_TRADES. Máxima línea estructurada1027<=1900.

134planes de entrada pasan cruce fresco/inclusiónprevia,ventana81,ATR15,stopdesde fill,qtyfloor8,cap1x,riesgo2%stop+fees,fundingasof,cuotaUTC ysinreversión en mismaT.57planesPOI también pasan disponibilidad/frescura,positividad,OIcreciente y referencia exactaT−24h. Valores de medias/timestamps se auditaron como evidencia registrada; el contenido/hash de velas no se recalculó desde mercado fuera del snapshot.

P:36stops,35salidas por cruce opuesto,5por holdingexacto180barras y1fold_end.76exits precierreAUDIT+1posterior=77trades. POI:26stops,28cruces y3holding180=57trades, sin cierre forzado final. Todas las salidas por cruce son MARKET posteriores alfill y satisfacen cruce contrario con sus81barras; holdingexacto30d comprobado. P tiene indicadoropen previo alfold_end; no implica posición residual.

Contadores all/direcciones/primary/features concilian. Hay156bucketsP/157POI, no160obligatorios. Seis/siete buckets direccionales fueron creados sólo por un cierre, bars0/exits1 y sin feature_reasons; se conserva la estructura, tratada como vacía únicamente con bars0. No se inventan barras para completar una grilla.

Auditorías respectivas AUDIT_ResearchV5CrossP4h_SCREEN.json y AUDIT_ResearchV5CrossOi4h_SCREEN.json; raws y referencias en V5_CROSS_PROGRESS.json. Sin cambios de parámetros, lectura2024+ o conclusión causal sobre utilidad aisladaOI. Espera de selección financiera central antes de fases futuras.