# V5 C4 Funding EVAL

Ventana [2025-07-01,2026-01-01),4h,nominal10000 por cuenta. Ambos finished/errornull, fuentes/config congeladas.

| Sesión | Trades | Neto% | PF | DD motor% |
|---|---:|---:|---:|---:|
| [ResearchV5FT_FP_C4V](http://localhost:9200/#/backtest/579ef0bc-f58e-43d3-8be8-858c5744512c) | 30 | -1.145369 | 0.931456 | -8.746835 |
| [ResearchV5FT_OI_C4V](http://localhost:9200/#/backtest/82032d8e-1310-4dd7-acac-6f2688c3b738) | 23 | -3.313639 | 0.786895 | -10.166356 |

Fullsnapshot con código exacto V5_V6_ACCOUNTING_CODE.json y_expectedconfig/strategy/start/finish/timeframe: job2bd9330ca47343579c7153aa1dd9693e PASS,maxerror5.4569682106375694e-12USDT. Rows completos, calendarios,ejecución,proxy/sensibilidades yprovenance en V5_C4V_ACCOUNTING_BRANCH.json. No sumar trades de trains solapados como muestra independiente.

Elección train anterior a evaluación permanece fija. Seleccionada ResearchV5FundingFPOi4h segúnSELECTION_V5_C4.json.

Auditorías de todosloslogs: FUNDING_FPOI: 1104decisiones,552SHA/552publicaciones,23entradas,23cierres precounter+0finales;causas{"no_setup_price":302,"setup":335,"carry_sign_reject":330,"funding_mixed":137};salidas{"trend_adverse":8,"stop-loss":5,"funding_adverse":10}. Evidencia AUDIT_ResearchV5FT_OI_C4V.json y1chunks con todo plan/features/publicación/cierre.

FUNDING_FP: 1104decisiones,552SHA/552publicaciones,30entradas,30cierres precounter+0finales;causas{"no_setup_price":302,"setup":335,"carry_sign_reject":330,"funding_mixed":137};salidas{"trend_adverse":13,"funding_adverse":13,"stop-loss":4}. Evidencia AUDIT_ResearchV5FT_FP_C4V.json y1chunks con todo plan/features/publicación/cierre.

Verificados trío disponible/rawaccessor/gaps/signos, señalesSMA120/C30,3ATRdesde fill,targetNone,2%fee/cap1x,cuotaUTC/no misma decisión yOI24hpositivo/fresco enentradasOI. Cada contador materializado concilia primaria/features/particiones direccionales. Todaspublicaciones fueron recorridas/hashverificados; los JSON de evidencia conservan muestras inicio/medio/final más cada entrada; restantes ventanas siguen enlogs originales. Medias registradas verificadas como contexto, construcción de ventanas certificada por fuentes/checks. Cobertura real de cada salida sólo si contador>0; no inventar ramas ejecutadas.

2024–25 fue visto antes: confirmación interna reutilizada, noOOSvirgen. Sin cambiosparámetros ni source/mainregistry, sinreplay ni2026. Un motorV5serial y unjob propio máximo. Progreso V5_WF_BRANCH_PROGRESS.json; rawstarts/timestamps/config preserved. Root fusiona registro.
