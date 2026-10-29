# V4 — cierre del screening SHOCK1h

Ambas variantes nominales quedan RECHAZADAS: neto negativo, PF<1.2 y drawdown>25%. Cumplen N>=30, pero eso no compensa los gates fallidos. No se retocan umbrales/salidas/hold ni se elige un vecino. No hay shortlist SHOCK, confirmación2024–25 ni motores posteriores autorizados de esta línea.

| Config | N | Neto | PFtrades | DD absoluto motor | Saldo final | Fees | Funding |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [SHOCK_PV](http://localhost:9200/#/backtest/02499a0c-1bc8-45ad-8f3a-bf4df11c404b) | 461 | -65.900410% | 0.528257 | 68.231522% | 3409.959046 | 2493.863365 | 15.609687 |
| [SHOCK_PVOI](http://localhost:9200/#/backtest/2980adc0-9379-4f04-bb2a-0a6b931c1af0) | 279 | -51.806642% | 0.475469 | 53.089429% | 4819.335788 | 1733.273081 | 8.687533 |

Ventana[2020-09-01,2024-01-01),BTC-USDT Binance Perpetual Futures1h,10000 inicial cada una,aislado3x,cap1x,risk2%stop+fees,fee.00045/slip0,fundingON,datasetsversionados,warmup240,un fillUTCdía. Reglas yfuentes congeladas sin modificaciones: shock>=2ATR14simpleprevio yvolumen>=2media24previa,entrada contraria,stop1A/TP1A desdefill,hold6h. Sólo PVOI añade OI24hpositivo.

Las dos sesiones se ejecutaron secuencialmente con un token. PV inicio respondió started; PVOI devolvió HTTP9000readtimeout10s,rawcompleto preservado,misma sesión consultada hasta finished sinretry/duplicación. Antes de iniciar se persistieron drafts/config/form/sourcehashes yautorización; después respuestas raw ysummarys.

Auditorías de logs pasan para ambas:29208decisiones,40meses,particiones primary/features/dirección; entradas=trades=cierres (461/279),0forzados,0metadataopen;cuotaUTC,ATRoffset1 ymetadataprevia,protección1A desde fill,plan2%inclfees/cap1x,OIasof24h sólo PVOI,configexacta ylíneas<=1900.
PV:270stoploss,180takeprofit,11maximumhold. PVOI:165stoploss,107takeprofit,7maximumhold. La rama hold6h sí fue ejercida por screening. Ambas procesan596features_setup idénticos; losgatesdedía/OI explican seleccióndiferente:PV135daily_limit;PVOI86daily_limit,230oi_nonrising,1oi_stale. OIflagsenPV son observación, no gate. No se afirma que el cambio de PnL pruebe causalidad de OI.

Evidencias guardadas: V4_SHOCK_PROGRESS.json; V4_SHOCK_SCREEN_PRERUN.json; AUDIT_ResearchV4ShockPV1h_SCREEN.json; AUDIT_ResearchV4ShockPVOi1h_SCREEN.json; V4_SHOCK_PV_ENTRYPLAN_AUDIT.json; V4_SHOCK_PVOI_ENTRYPLAN_AUDIT.json;13páginasrawlogsPV y9PVOI en V4_SHOCK_PV_SCREEN_LOGS_XX.json y V4_SHOCK_PVOI_SCREEN_LOGS_XX.json. Se releyó metadata de los26artefactos de audit/entryplan/logs para comprobar persistencia.

Root realiza conciliación contable completa mediante snapshots, sin jobs de análisis de este sector. PFyCAGRsummary son informativos aquí; no se calcula aprobaciónanual con equity incompleta. Las pérdidas/DDrechazan sin depender de esa comprobación adicional. V4 conserva cronología reutilizada, noOOSvirgen; no se consultaron datos2024+ni2026 paraestaetapa.

Estado final sector: RECHAZADA, técnicoPASS, contabilidadcentralpendiente. Motor token liberado. Sin nuevas estrategias, variantes, runs o reparaciones económicas.
