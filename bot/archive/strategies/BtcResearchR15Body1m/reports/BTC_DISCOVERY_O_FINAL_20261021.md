# Tanda O: orden de extremos intradiarios, cierre

Dos políticas prefijadas sin candidata. REPAIR supera al controlBODY dentro del desarrollo, pero falla CAGR30%,M65yQ80. BODYpierde y falla economía. No se cambian dirección, resolución, empates, tamaño delcuerpo o protección ni se combinan retrospectivamente conN. PresupuestoOcerrado, sinvecinos locales.

|Política|N|CAGR|PF|DD M1+fills|M+ activos|Q+|Mediana mensual|Neto sin2mejores|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[repair](http://localhost:9200/#/backtest/964af419-18ca-40e4-acad-cb8bb3ba8630)|156|9.2614%|1.4185|13.9383%|34/60|14/20|0.3052%|3663.5716|0.8430|
|[body](http://localhost:9200/#/backtest/fae557b4-7b60-411f-a92b-8d213b009152)|850|-13.7700%|0.9045|61.7234%|24/62|8/20|-1.6914%|-7521.1448|-0.4584|

## Diseño preservado

En cada00:00UTC se toma el día cerrado,6bloques4h; admisibilidad común: signo diario no0, H/Lúnicos en bloques distintos, datosválidos/exactos. BODYopera signo diario; REPAIRsólo(HantesL+bodypositivo)o(LantesH+bodynegativo). MismoSL2ATR14simple4h,TP2R,48hgestión4h,unaposición2%feeaware. Ventana[2020-10-15,2026-01-01)UTC, BinancePerpetualFuturesBTC-USDT,10k/2%/6%/3x,fee.00045lado,fundingONhistóricoaplicado/verificado,slippage0. Neto cubre esos costosmodelados; no ejecuciónreal ni todosloscostos.

## Recibos y cuentas

[BtcResearchR15Repair1m](http://localhost:9200/#/backtest/964af419-18ca-40e4-acad-cb8bb3ba8630):brutoprecio7301.822403,fee1261.149008,funding-167.649768,neto5873.023627(58.7302%),equityfinal15873.023627USDT. DD diarioframework-12.2311% esdistintodelM1. Estadísticas:{"stage":"PRETERMINAL","counts":{"repair":187,"body_only":1638},"signals":187,"entries":156,"occupied":31}.

[BtcResearchR15Body1m](http://localhost:9200/#/backtest/fae557b4-7b60-411f-a92b-8d213b009152):brutoprecio-1259.000552,fee3732.991163,funding-390.931821,neto-5382.923535(-53.8292%),equityfinal4617.076465USDT. DD diarioframework-60.4847% esdistintodelM1. Estadísticas:{"stage":"FINAL","counts":{"repair":187,"body_only":1638},"signals":1825,"entries":850,"occupied":975}.

Ambas observaron1825díasadmisibles,187repair y1638body_only; porocupación REPAIRllenó156de187 yBODY850de1825. Diferencias enPnL no son efecto puro de un filtro sobre tradesiguales: ocupación, capital y tamaños cambian. El controlador no representa todoslosdíasBTC, sino días con admisibilidadcompartida. No hay selección deañosolados después delresultado.

Auditoríac3b0d733a5634abb815ce3b549bbcdbf succeeded:1006tradescompletos entre políticas alternativas, no muestrasindependientes; bruto−fees+funding=PnL=equityfinal−10000 error<1e−6USDT. Fundingcuadra,mismofrozenBTCdataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxiesdeclarados. Telemetríacompleta2.741.760marcasM1,63meses/62completos,20Q,invalid0; telescopíacuadra. BODYusaFINALpostliquidación/cierrecomisión; total_open_trades1 escontadorpreterminal,no pendiente económico. REPAIRPRETERMINALsinposición.

Equitywallet+PnLabierto/M1+fills no todosextremosintraminuto; cortesmensualespostfunding/predecisiónporfase, no agrupación estrictaporfecha. Mediana incluye mesescalendarioinactivos; M65denominadormesescompletosactivos. N>=100espreliminaroperativo, no potenciaestadística. Historiaintensamentereutilizada, noOOSnuevo.

Checksintético118PASS,revisiónindependiente/rootconforme; protocolofijadoantesresultadoN ymanifiestoantesmotores. Recibotécnico faltante trasinterrupciónMCP confirmadoausente y recuperadodeljobexistente, sinrerun.2economíasnuevas,0errores/reemplazos/backteststécnicos. Totaldesde r9:28completadas, bloque209V1–V6 separado,sinindependencia. Sin estrés/riesgovariantes/nuevaeconomía2026/live/paper/Pi/global/instalaciones. Continuar pregunta materialP: aislarBTCdeK1001/N204,protocoloenpreparación; ningunaautorizaciónoperativa.
