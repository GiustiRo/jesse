# V5 Funding Trend — C2 trains

Trains expansivos [2020-09-01,2024-07-01),4h,10000 inicial cada uno. Ambos finished/errornull, fuentes/config nominales inalteradas. Ambos cumplen N>=30/net>0/PF>=1.2/DD<=25. No se añade gate anual a train; root debe guardar SELECTION_V5_C2 antes de cualquier evaluación siguiente. C1evaluación y elección OI se mantienen como fueron registradas.

| Train | Trades | Neto% | PF | DD motor% |
|---|---:|---:|---:|---:|
| [FUNDING_FPOI](http://localhost:9200/#/backtest/628fd490-2e32-46a6-bc37-78f2ec87f641) | 146 | 29.724527 | 1.367147 | -13.022950 |
| [FUNDING_FP](http://localhost:9200/#/backtest/ffdac79c-c8e2-4edd-a360-e68147b011ab) | 188 | 26.712406 | 1.267817 | -15.723609 |

OI saldo12972.452671,fees651.573675,funding+351.314939;FP saldo12671.240584,fees843.377748,funding+412.026564. CAGR de desarrollo7.025567/6.371572%,descriptivo. No sumar estos trades a SCREEN oC1: hay historia solapada ycapital continuo por train, distinto de cada evaluación reseteada.

Auditoría propia PASS en ambos. Logs completos19páginas/7475líneasOI,20/7973FP; máximos1028/1029caracteres.8394decisiones/46meses,4197publicaciones únicas ySHA4197verificados por sesión. Publicaciones3391funding_state/806funding_mixed; sin timestamp/accessor/asof/gap/signos inválidos. Causas featurecomunes3137carry_sign_reject/2109setup/1926no_setup_price/1222funding_mixed. OIprimary146allowed/1659open/291oi_nonrising/2oi_reference_invalid/11daily_limit/1boundary,FP188allowed/1910open/11daily_limit/1boundary,con las causas restantes de señal.

Todos334planes y334cierres revisados, preservados en nueve archivos de40entradas como máximo. Señal SMA120/C30/trío,hashes,distancias3ATRfijas desde fill,targetNone,2%stop+fees,cap1x ycuotaUTC correctos. OI actual/refexactaT−24h,positivos/crecientes,frescura/publicación en todas146entradas. Salidas deindicador cumplen postfill yestadoadverso.

OIcierres82funding/52trend/11stop/1fold_end;FP104funding/69trend/14stop/1fold_end. Counters se emiten precierre:OI145exits+1final=146,FP187+1=188. Metadataopen_trades1/open_pl no describe exposición final; V5_CLOSE final confirmado. Sin maximumhold30d ejecutado: cobertura de esa rama sólo determinista.

AUDIT_ResearchV5FT_OI_C2T.json yAUDIT_ResearchV5FT_FP_C2T.json contienen buckets/totales/manifiestopublicaciones/muestras yrefs. V5_C2T_FUNDING_FPOI_ENTRY_EVIDENCE_01..04.json yV5_C2T_FUNDING_FP_ENTRY_EVIDENCE_01..05.json conservan todo plan/features/publicación/cierre asociado; otraspublicaciones quedan en logs originales. V5_C2_BRANCH_PROGRESS.json conserva prerun/rawstarted/timestamps/config/resultados. Los starts respondieron started, sin reintentos. Root realiza contabilidad/equity/órdenes por snapshot completo. No nuevos jobs,drafts,fuentes niC2eval.2026 sigue cerrado; confirmación interna usa pasado ya visto.
