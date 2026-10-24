# V5 C3 Funding EVAL

Ventana [2025-01-01,2025-07-01),4h,nominal10000 por cuenta. Ambos finished/errornull, fuentes/config congeladas.

| Sesión | Trades | Neto% | PF | DD motor% |
|---|---:|---:|---:|---:|
| [ResearchV5FT_FP_C3V](http://localhost:9200/#/backtest/14598ad7-2ac2-47e6-ba71-c7e9af290a55) | 37 | 1.379702 | 1.082177 | -7.748996 |
| [ResearchV5FT_OI_C3V](http://localhost:9200/#/backtest/13962ea9-197d-49b2-bb9a-69c6c7e7c038) | 29 | -0.983972 | 0.930326 | -7.817199 |

Fullsnapshot con código exacto V5_V6_ACCOUNTING_CODE.json y_expectedconfig/strategy/start/finish/timeframe: job4b8c4b0ad6d34fd790ba3c686a129909 PASS,maxerror5.4569682106375694e-12USDT. Rows completos, calendarios,ejecución,proxy/sensibilidades yprovenance en V5_C3V_ACCOUNTING_BRANCH.json. No sumar trades de trains solapados como muestra independiente.

Elección train anterior a evaluación permanece fija. Seleccionada ResearchV5FundingFPOi4h segúnSELECTION_V5_C3.json.

Auditorías de todosloslogs: FUNDING_FPOI: 1086decisiones,543SHA/543publicaciones,29entradas,29cierres precounter+0finales;causas{"setup":263,"no_setup_price":261,"carry_sign_reject":303,"funding_mixed":259};salidas{"funding_adverse":21,"trend_adverse":7,"stop-loss":1}. Evidencia AUDIT_ResearchV5FT_OI_C3V.json y1chunks con todo plan/features/publicación/cierre.

FUNDING_FP: 1086decisiones,543SHA/543publicaciones,37entradas,37cierres precounter+0finales;causas{"setup":263,"no_setup_price":261,"carry_sign_reject":303,"funding_mixed":259};salidas{"stop-loss":3,"trend_adverse":8,"funding_adverse":26}. Evidencia AUDIT_ResearchV5FT_FP_C3V.json y1chunks con todo plan/features/publicación/cierre.

Verificados trío disponible/rawaccessor/gaps/signos, señalesSMA120/C30,3ATRdesde fill,targetNone,2%fee/cap1x,cuotaUTC/no misma decisión yOI24hpositivo/fresco enentradasOI. Cada contador materializado concilia primaria/features/particiones direccionales. Todaspublicaciones fueron recorridas/hashverificados; los JSON de evidencia conservan muestras inicio/medio/final más cada entrada; restantes ventanas siguen enlogs originales. Medias registradas verificadas como contexto, construcción de ventanas certificada por fuentes/checks. Cobertura real de cada salida sólo si contador>0; no inventar ramas ejecutadas.

2024–25 fue visto antes: confirmación interna reutilizada, noOOSvirgen. Sin cambiosparámetros ni source/mainregistry, sinreplay ni2026. Un motorV5serial y unjob propio máximo. Progreso V5_WF_BRANCH_PROGRESS.json; rawstarts/timestamps/config preserved. Root fusiona registro.
