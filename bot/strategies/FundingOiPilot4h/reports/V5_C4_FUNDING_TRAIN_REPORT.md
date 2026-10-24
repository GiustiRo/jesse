# V5 C4 Funding TRAIN

Ventana [2020-09-01,2025-07-01),4h,nominal10000 por cuenta. Ambos finished/errornull, fuentes/config congeladas.

| Sesión | Trades | Neto% | PF | DD motor% |
|---|---:|---:|---:|---:|
| [ResearchV5FT_FP_C4T](http://localhost:9200/#/backtest/0b0fea0e-c7cd-4abb-b746-56427cf792a6) | 246 | 31.166751 | 1.234976 | -15.723609 |
| [ResearchV5FT_OI_C4T](http://localhost:9200/#/backtest/d45530ac-ffe0-4e5e-b5a4-15fdfafaba2e) | 192 | 29.723517 | 1.267955 | -13.022950 |

Fullsnapshot con código exacto V5_V6_ACCOUNTING_CODE.json y_expectedconfig/strategy/start/finish/timeframe: jobe71cdfe483354b22a853bf6759d4c835 PASS,maxerror2.9103830456733704e-11USDT. Rows completos, calendarios,ejecución,proxy/sensibilidades yprovenance en V5_C4T_ACCOUNTING_BRANCH.json. No sumar trades de trains solapados como muestra independiente.

Gatestrain N>=30/net>0/PF>=1.2/DD<=25, sinannual/CAGR extra. Seleccionada ResearchV5FundingFPOi4h segúnSELECTION_V5_C4.json.

Auditorías de todosloslogs: FUNDING_FPOI: 10584decisiones,5292SHA/5292publicaciones,192entradas,192cierres precounter+0finales;causas{"carry_sign_reject":3908,"setup":2576,"no_setup_price":2437,"funding_mixed":1663};salidas{"funding_adverse":114,"stop-loss":15,"trend_adverse":62,"maximum_hold":1}. Evidencia AUDIT_ResearchV5FT_OI_C4T.json y5chunks con todo plan/features/publicación/cierre.

FUNDING_FP: 10584decisiones,5292SHA/5292publicaciones,246entradas,246cierres precounter+0finales;causas{"carry_sign_reject":3908,"setup":2576,"no_setup_price":2437,"funding_mixed":1663};salidas{"funding_adverse":143,"stop-loss":20,"trend_adverse":82,"maximum_hold":1}. Evidencia AUDIT_ResearchV5FT_FP_C4T.json y7chunks con todo plan/features/publicación/cierre.

Verificados trío disponible/rawaccessor/gaps/signos, señalesSMA120/C30,3ATRdesde fill,targetNone,2%fee/cap1x,cuotaUTC/no misma decisión yOI24hpositivo/fresco enentradasOI. Cada contador materializado concilia primaria/features/particiones direccionales. Todaspublicaciones fueron recorridas/hashverificados; los JSON de evidencia conservan muestras inicio/medio/final más cada entrada; restantes ventanas siguen enlogs originales. Medias registradas verificadas como contexto, construcción de ventanas certificada por fuentes/checks. Cobertura real de cada salida sólo si contador>0; no inventar ramas ejecutadas.

2024–25 fue visto antes: confirmación interna reutilizada, noOOSvirgen. Sin cambiosparámetros ni source/mainregistry, sinreplay ni2026. Un motorV5serial y unjob propio máximo. Progreso V5_WF_BRANCH_PROGRESS.json; rawstarts/timestamps/config preserved. Root fusiona registro.
