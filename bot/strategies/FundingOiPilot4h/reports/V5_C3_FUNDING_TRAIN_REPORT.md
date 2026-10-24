# V5 C3 Funding TRAIN

Ventana [2020-09-01,2025-01-01),4h,nominal10000 por cuenta. Ambos finished/errornull, fuentes/config congeladas.

| Sesión | Trades | Neto% | PF | DD motor% |
|---|---:|---:|---:|---:|
| [ResearchV5FT_FP_C3T](http://localhost:9200/#/backtest/554153ca-048c-4568-9916-6d450f71ab65) | 209 | 29.382045 | 1.264905 | -15.723609 |
| [ResearchV5FT_OI_C3T](http://localhost:9200/#/backtest/74f1cbc5-5eee-4e87-98c8-36f1062aa2d7) | 162 | 33.645902 | 1.374710 | -13.022950 |

Fullsnapshot con código exacto V5_V6_ACCOUNTING_CODE.json y_expectedconfig/strategy/start/finish/timeframe: job51a38cc26f48446fbc7d2baf07895743 PASS,maxerror5.4569682106375694e-12USDT. Rows completos, calendarios,ejecución,proxy/sensibilidades yprovenance en V5_C3T_ACCOUNTING_BRANCH.json. No sumar trades de trains solapados como muestra independiente.

Gatestrain N>=30/net>0/PF>=1.2/DD<=25, sinannual/CAGR extra. Seleccionada ResearchV5FundingFPOi4h segúnSELECTION_V5_C3.json.

Auditorías de todosloslogs: FUNDING_FPOI: 9498decisiones,4749SHA/4749publicaciones,162entradas,162cierres precounter+0finales;causas{"carry_sign_reject":3605,"setup":2313,"no_setup_price":2176,"funding_mixed":1404};salidas{"funding_adverse":93,"stop-loss":13,"trend_adverse":55,"maximum_hold":1}. Evidencia AUDIT_ResearchV5FT_OI_C3T.json y5chunks con todo plan/features/publicación/cierre.

FUNDING_FP: 9498decisiones,4749SHA/4749publicaciones,209entradas,209cierres precounter+0finales;causas{"carry_sign_reject":3605,"setup":2313,"no_setup_price":2176,"funding_mixed":1404};salidas{"funding_adverse":117,"stop-loss":17,"trend_adverse":74,"maximum_hold":1}. Evidencia AUDIT_ResearchV5FT_FP_C3T.json y6chunks con todo plan/features/publicación/cierre.

Verificados trío disponible/rawaccessor/gaps/signos, señalesSMA120/C30,3ATRdesde fill,targetNone,2%fee/cap1x,cuotaUTC/no misma decisión yOI24hpositivo/fresco enentradasOI. Cada contador materializado concilia primaria/features/particiones direccionales. Todaspublicaciones fueron recorridas/hashverificados; los JSON de evidencia conservan muestras inicio/medio/final más cada entrada; restantes ventanas siguen enlogs originales. Medias registradas verificadas como contexto, construcción de ventanas certificada por fuentes/checks. Cobertura real de cada salida sólo si contador>0; no inventar ramas ejecutadas.

2024–25 fue visto antes: confirmación interna reutilizada, noOOSvirgen. Sin cambiosparámetros ni source/mainregistry, sinreplay ni2026. Un motorV5serial y unjob propio máximo. Progreso V5_WF_BRANCH_PROGRESS.json; rawstarts/timestamps/config preserved. Root fusiona registro.
