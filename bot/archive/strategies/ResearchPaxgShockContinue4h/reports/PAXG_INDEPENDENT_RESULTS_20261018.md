# PAXG independiente — resultado de primera ronda
Fecha local18octubre2026. Tres full económicos nuevos terminados; dos recetas nuevas rechazadas y un control existente. Ninguna promoción; referencia y2026 intactos. No barridos, scripts, fuentes nuevas, framework ni operativa.

## Contrato y trazabilidad
Protocolo anterior a runs: PAXG_INDEPENDENT_PROTOCOL_20261018.md en esta carpeta. Capital10000USDT,riesgo1%trade/8%agregado,5xaislado,gross<=4.4,fee.00045porlado inclusoLIMIT. PAXGspot como proxy de precio aceptado por el usuario para destino Binance perpetual; funding fuera de etapa.
Ventana común2020-10-15→2025-12-31 exclusiva,4h+M1,modo normal/warmup240.
Dos hipótesis opuestas sobre shock4h>=1.5ATR14PREVIO: continuación o reversión; stop2ATRprevio,MARKET,48h desde fill,simetría long/short, sinfiltrosmacro/trailing/TP/BE. Control copiaexactabaseline salvoclase/riesgo1%,PAXGaislado.

| Diseño y dashboard | Trades | Neto USD | Antes fees USD | Fees USD | PF neto | CAGR motor | DD motor |
|---|---:|---:|---:|---:|---:|---:|---:|
|[Continuación](http://localhost:9200/#/backtest/73464795-1e47-4f0a-9239-fd8901775dc2)|235|−2140.19|−507.83|1632.36|0.7705|−4.514%|−30.658%|
|[Reversión](http://localhost:9200/#/backtest/aca7b3b8-3781-4986-8ed6-0ede625ba31c)|245|−2398.95|−785.75|1613.20|0.7427|−5.125%|−26.465%|
|[Retest control1%](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c)|35|546.11|792.72|246.61|1.3083|1.025%|−6.919%|

CAGR/DD/Sharpe anteriores son del motor; DD de cierre diarioMTM puede diferir. Control no equivale a contribución original de cartera ni permite sumar curvas independientes. ShareATR=1 y capital aislado hacen tamaños diferentes.

## Qué se aprende
Ambos espejos fallan antes y después de fees. Aumentar actividad sobre shocks no entrega expectativa positiva a48h con stops probados; reducir costes no basta sobre estosfills. No inferir imposibilidad de todo momentum ni toda reversión de PAXG. No variar1.5/14/2ATR/48h tras resultado.
Ambasdirecciones pierden: continuaciónlong120net−835.95,short115net−1304.24; reversiónlong114net−879.40,short131net−1519.55. No retirar shorts ni escoger añosfavorables para rescatar.
Mismos eventos definidos, pero no misma muestra emparejada de trades: stops/salidas cambian ocupación y próximos eventos admitidos. Por eso PFespejo no identifica respuesta causal ni permite comparar eventoaeven­to.
Neto sobre suma nocionalentrada:−11.802bpscontinuación,−13.385reversión,19.959control. Antesfees−2.800/−4.384/28.972bps. Con5bps extra ida/vuelta sobre mismosfills neto−3046.91/−3295.06/409.30;con10bps−3953.63/−4191.16/272.50. Sensibilidad estática no backtest dinámico ni coste nativo observado. Sinfunding simulado.
Exposición temporal18.37%/18.95%/13.36%;holding medio35.70h/35.32h/174.30h. Shocks incrementan turnover unas6.7–7veces frente35ret­ests sin beneficio útil. No confundir ocupación con alpha.

Control conserva PF>1.2pero es señal de runner escasa, no avance nuevo: top3ganadores1466.66=268.56%delneto;sinellos−920.55descriptivo. No se exige mecánicamente a una tendencia sobrevivir quitar runners, pero esta concentración limita confianza con35trades. Ganancia realizada por cohortes de cierre2021−203.71,2022−87.14,2023−55.79,2024+495.50,2025+397.25: NO son retornos anualesMTM, no reinterpretar como pruebaOOS.

## Auditoría técnica
Análisis completo por snapshots aa21b5ab23ab40449bd367ed22386bfc succeeded/exit0:235+245+35trades, órdenesejecutadas,curvas y métricas. Numericapersistente PAXG_INDEPENDENT_AUDIT_20261018.md.
Fees reconstruidas .00045×nocionalentrada+salida coinciden(error<1.8e−15);grossporfills−fees concilia PNL(error<1.6e−12);cantidadesentrada/salida coinciden;walletconciliada<4e−11;sin posiciones superpuestas. Máxima exposición inicial/pree­ntrywallet1.571x/1.570x/1.222x, bajo4.4. Se verifica cap inicial, no exposición marcada cada instante.
235/245entradasMARKET;102/107salidasSTOP;133/138salidasMARKET. Excluyendo cierre sintético de fin, todas132/137salidasMARKETocurrenexacto48hdesde fill;0violaciones. Control35LIMIT/35STOP.
Ambosespejosmarcantotal_open_trades=1 antesliquidaciónterminal, pero salida plenaMARKETenfinishreconciliada:continuacióngross210.463668=metricopen_pl,net204.078793,40h;reversióngross18.171920=open_pl,net13.027247,32h. Son cierresdeconvención, no residualni evidenciaejecuciónnativa.
QuoteM1 se valida por timestamp exactoT−60s+preciofinito/positivo; código NO comprueba igualdadM1close/4hclose ni detecta barrasdelproveedorrellenadas. No se alteró receta después de empezar. Snapshots no incluyenvelas, por lo que auditoríadefills no certifica esa igualdadni paridadperp.
Curva persistida:1904puntos,1902a00:01UTCy2fronterasa00:00. No usarla como cierreUTCmensual. Root coordinaMTMunificadoV4desdebenchmarks/anchors; calendario exacto no calculado aquí. PNGcreadopero get_analysis_artifact devolvióartifact_changeddosveces; JSONnumérico sí recuperado y persistido, sinfallback.
save_strategy_report acepta.md; primerintento.jsonrechazadosincambios y datos luego guardados.md.

## Decisión y siguiente gate
ARCHIVAR ambosrecipes shocks enesta ronda. No ejecutarcuartofull reservadoarobustez porque nohay superviviente. No integrar pata perdedoraen cartera esperando que correlación arregle expectativa.
Tresfulleconómicos nuevos se añaden al historial global existente; no contarcontrol como nuevaalpha ni llamar2020–25OOS. Regularidad65–70%meses/80%q esobjetivodecartera, no condición de cada señal. NoMCpararescatar fallosfundamentales.
No existe siguiente hipótesis lista que supere control de duplicación: exposición persistentedeoro/tendencia lenta solapaTurtle/rotación; respuesta riskoffentremercadossolapadivergencia. Esto no pruebaquevelasesténagotadas: requiere un mecanismo distinto y contraste fijado antes de gastar otrofull, en vez de cambiarnombre/indicadores. Se conservabaseline.
