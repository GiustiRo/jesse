# V5 FUNDING_TREND — screening nominal y auditoría

Las dos sesiones [2020-09-01,2024-01-01),4h,terminaron sin error. Cumplen preliminarmente N>=30/net>0/PF>=1.2/DD<=25. La elegibilidad anual2021/22/23 y la selección global corresponden a root; este informe no congela shortlist ni autoriza2024–25. CAGR de screening se reporta descriptivamente, sin imponerle el gate15% de replay.

| Variante | Trades | Neto% | PF neto | DD motor% | CAGR motor% |
|---|---:|---:|---:|---:|---:|
| [FUNDING_FP](http://localhost:9200/#/backtest/2c40635d-6a44-4bea-9a49-6b1ce1b8742d) | 171 | 30.678816 | 1.362704 | -15.723609 | 8.355761 |
| [FUNDING_FPOI](http://localhost:9200/#/backtest/e5bd6218-1066-4181-9ee6-7d5de2fae0c4) | 132 | 34.036948 | 1.505844 | -13.022950 | 9.183473 |

FP19long/152short, saldo13067.881564, fees765.059914 yfunding+338.081609. FPOI16long/116short, saldo13403.694835, fees584.205199 yfunding+288.984104. Se conserva predominio short previsto por signos y tendencia; no se fuerza balance direccional. Root concilia trades/funding/fees/equity completos y años por calendario antes de elegibilidad.

## Evidencia técnica completa

Recorridos todos los logs por next_offset: FP18páginas/7028líneas, FPOI17páginas/6568líneas; máximos1029/1028caracteres. Cada sesión7302decisiones/40meses.3651publicaciones únicas,3651SHA recalculados de los tokens JSON originales por sesión; tres pagos asof, gaps8h±1000ms, rawaccessor/últimoevento ysignos verificados. Ninguna ausencia,zero,accessormismatch,stale,gapounpublished observada en los contextos de publicación de estas sesiones. Constancia de tasas válidas no excluye varianza0: aquí no hay gate de sigma.

Features por sesión idénticas:1758setup,2677carry_sign_reject,1686no_setup_price,1181funding_mixed. Estado se evalúa cada4h; dedup sólo evita repetir logs de publicación. FPprimary171allowed,1577in_position_or_pending,9daily_limit,1boundary final,además de las tres causas no_setup/carry/mixed. FPOI132allowed,1380in_position_or_pending,234oi_nonrising,2oi_reference_invalid,9daily_limit,1boundary,además de las mismas causas de señal. Flags simultáneos de calidad no se suman como trades.

Todos303planes/entradas y303cierres fueron capturados y revisados: precio de señal/SMA120/C30, trío estricto yhashcorrecto,ATRactual3x,distancia fija desdefill,targetNone,sizing stop+fees2%,cap1x,una entradaUTCdía,no misma decisión de cierre yOIvalid/passed en132entradasFPOI. Referencias de precio son valores registrados; la construcción de ventanas yprefijos/futuro corresponde a fuentes estáticas/checks, no a reconstrucción de candles desde logs.

FPcierres:100funding_adverse,58trend_adverse,12stop-loss,1fold_end. FPOI78funding_adverse,45trend_adverse,8stop-loss,1fold_end. Estados fundingadverse tienen tasa válida perjudicial; estados trendadverse cumplen igualdad incluida yT>opened_at. No maximumhold30d en estas muestras: no se afirma ejecución de esa rama, sólo su cobertura determinista. Stop-trigger sí apareció en ambos.

Cada counter mensual se emite antes del último cierre forzado: FP170exits+1final=171 yFPOI131+1final=132. total_open_trades1/open_pl en summary esmetadata precierre; V5_CLOSE final aporta el cierre real. El agregador de auditoría inicial trató páginas newest→older como cronología global al contar cierres posteriores a provenance. Se corrigió únicamente el contador de auditoría para identificar fold_end con time=finish; las estrategias, sesiones y economía no cambiaron. Todos los counters finales concilian.

## Artefactos y límites

AUDIT_ResearchV5FundingFP4h_SCREEN.json y AUDIT_ResearchV5FundingFPOi4h_SCREEN.json contienen todos los buckets ylos contadores validados. V5_FUNDING_FP_ENTRY_EVIDENCE_01.json a05 yV5_FUNDING_FPOI_ENTRY_EVIDENCE_01.json a04 conservan cada entrada con features, publicación canónica y cierre/exit asociado. Se dividieron40entradas por archivo para evitar truncamiento; ninguna se omitió. Otras publicaciones permanecen en los logs originales; manifiesto de hashes y muestras inicio/medio/final en auditoría. V5_FUNDING_SCREEN_COUNTERS.json y V5_FUNDING_PROGRESS.json conservan configuración, rawstarted, timestamps, métricas ypaths.

Mismo código/config/datasets prerregistrados, sin nueva calibración por resultados. Dos motores iniciados una vez, sin timeout, sinjobs de análisis propios. No hubo ejecución ni consulta2024+ deestas configuraciones.2020–2025 ya observado en ciclos anteriores, OI retrospectivo ypublicación histórica asumida: no afirmar OOSvirgen ni autorizaciónlive. Estado del sector: screening completo, auditoría propia PASS, a la espera de decisión central anual/shortlist.
