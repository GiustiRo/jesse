# BTC Discovery V — cierre

Se comparó VAR1 conjunto BTC/ETH con AR1 BTC exacto de G, bajo admisión compartida.242 cierres sincronizados,240 pares maduros,OLS centrado rank2 según NumPy default, seis pasos recursivos con ETH predicho. B usa filas predictor/columnas respuesta; no se usó ETH futuro. Sin regularización, clipping, filtros de estabilidad ni otro horizonte. El contraste comprende ambas ecuaciones y feedback; no aísla causalidad ETH→BTC.

Contrato UTC [2020-10-15,2026-01-01),10k,2%/6%/3x,fee.00045 por lado, funding BTC histórico aplicado/verificado con proxies, slippage0. R10 sizing, stop2ATRsimple, sinTP, timeout24h desde fill en primer cierre4h elegible; R11 M1 intacto. Forecast bruto de precio, no payoff neto. Warmup3004h. Desarrollo observado, no OOS.

|Política|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin dos mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[VAR](http://localhost:9200/#/backtest/abab7a82-4df9-489a-8528-e5ec8607f43e)|1533|-7.342609|0.967405|66.051916|25/62|7/20|-1.055285|-7652.471521|
|[AR](http://localhost:9200/#/backtest/01af3d1f-a881-468e-ab1a-5b67460591d3)|1481|-7.444034|0.968755|62.035364|27/62|8/20|-2.391767|-8850.377776|

VAR: bruto precio 7490.732181093577; fees 8634.453674758912; funding -2138.403656693383; neto -3282.125150358702; capital final 6717.874849641259. Años completos: {"2021":-6.819840348620643,"2022":-44.175767389881415,"2023":0.6145842419797987,"2024":0.26037308551167815,"2025":-16.66935237168311}. Peor/mejor12m: -48.10335250027398/32.43979210983709%.

AR: bruto precio 8047.125197941238; fees 9127.724066540486; funding -2239.797078290056; neto -3320.395946889291; capital final 6679.604053110798. Años completos: {"2021":-8.48446180932484,"2022":-34.88775759048261,"2023":6.4622502197481335,"2024":-8.9613052825667,"2025":-24.71978011505609}. Peor/mejor12m: -38.69394314966218/28.429765273779537%.

El nuevo control AR reproduce económicamente [G original](http://localhost:9200/#/backtest/c72b53d8-c986-4131-814b-788cdc0f49e2):1481 trades, mismos type/opened_at/closed_at y error0 en entry/exit/qty/fee/PNL/funding por fila, ignorando IDs/nombres. La admisión conjunta fue válida11424 veces en ambas políticas, por lo que no alteró G en esta trayectoria. No se presenta esa reproducción como evidencia independiente ni mejora. Se conservaron las dos ejecuciones nuevas por ID y la replicación se identifica separadamente; no se deduce un número de hipótesis independientes de los conteos.

Auditoría4967b36eb26749938cafc6ce0303a1f2 succeeded con snapshots completos VAR/AR y G sólo lectura: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. Artefacto audit.json incluye comparación G. AR usa FINAL tras liquidación terminal; rawopen1 era metadato previo. VAR PRETERMINAL coincide con final sin abiertas.63intervalos/62meses completos/20Q,2741760marcasM1 por cuenta,0invalidwindows; rank/forecasts válidos11424 de11424. DD M1+fills,no extremos intraminuto; corte mensual por fase postfunding/predecisión; mediana incluye inactivos.51ventanas12m solapadas,no independientes.

Check9f08bcad89ec485a8757da1d6650e9be PASS primer intento,12grupos materiales,NumPy1.26.4; padres intactos. Dos económicos completos,0fallos/reemplazos/backtests técnicos. No stress ni variantes de riesgo. N>=100 sólo suficiencia operativa preliminar.

Decisión: NO_CUMPLE ambas, ninguna candidata. La diferencia pequeña de neto no justifica conservar esta dinámica conjunta. Cerrar sin vecinos de240/horizonte/lag/rcond/regularización/clipping/hurdle/lado/estabilidad/gestión/coupling; no aislar segmentos o coeficientes ganadores. Sin nuevas pruebas2026/imports/live/paper/Pi.

42ejecuciones económicas desde r9 por ID; una reproduce trayectoria G ya medida.209legacy V1–V6 aparte, no censo global ni muestras independientes. W sólo protocolo en preparación, fijado antes del resultado V: estado de dos primeros pasajes con barreras competidoras, type+fast frente type. Overshoot y distancia residual impiden llamarlo velocidad pura. Sin fuentes/jobs/drafts/economía W hasta revisión root. Objetivo pendiente, continuar autónomamente.
