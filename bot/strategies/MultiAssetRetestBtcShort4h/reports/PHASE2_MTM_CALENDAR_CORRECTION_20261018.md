# Auditoría corregida: cierre de calendario y contribuciones MTM

Candidata: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb . CAGRJesse28.8294%,DDJesse-14.8905%,220trades,97long/123short,PNLneto27461.46USDT. 2026 intacto.

## Limitación de auditor v2 identificada

El motor guarda equity diaria alrededor00:01UTC. ResampleME.last toma el punto al comienzo delúltimodía delmes, dejando fuera casi ese último día. El dato previamente comunicado60.66%mesesactivos/76.19%trimestres corresponde a ese corte observado, no al cierre real del mes. No usarlo como objetivo de calendario estricto.

## Reconstrucción y verificación

Se usaron benchmarks diarios guardados en http://localhost:9200/#/backtest/2e943276-7815-4280-96c8-d634d2dab817 :sontransformacioneslineales de preciosdecierre reales,independientesdelbugdemargen de aquellasesión. Las escalas se recuperan por órdenesMARKET ejecutadas exactamente a medianoche(preciódelcierreprevio), validando múltiples anclajes independientes. BTC29anclajes,oro12,SPY15;discrepanciasmáximasrelativas<2e-15. No se inventaronvelasni se importódatoextra.

Se reconstruyó cada posición conqty,entrada,salidayfeesreales:PNLrealizado+PNLabierto al cierreUTCdel día, descontando feeentrada mientras abierta. En cierresdelmercadosevalúa alúltimoprecioobservado, sin añadirvelasnegociables. ElPNLterminalreconstruido porrutaytotalreconcilia contradesywalletfinal. Ventanasparcialesprimera/últimase conservan;dic2025 termina30porfinishexclusive31.

## Resultado de cierreal mes

Auditoría run_analysis085535266e664019a50f46208044b640: cartera combinada52.38%mesespositivostotales,54.10%mesesactivospositivos (61activos),71.43%trimestrespositivos; peormes2021-08:-7.02%,peortrimestre2023Q3:-4.24%. DDdecierrediario-14.8784%,muyparecidoalJesse00:01. Son seriesdiarias, no máximo intraminuto. Metas65–70%/80% NOalcanzadas.

Correlación de contribuciones mensualesMTM,realesenlacuenta compartida:BTC/PAXG-0.0388,BTC/SPY0.0043,PAXG/SPY-0.1136. Se incluyeron posicionesabiertas almes, no solo tradescerrados. Máx|corr|0.114 cumple0.25 paraestascontribucionesenestamuestra;no equivalena estrategiasindependientes con capitalpropio ni garantiza correlaciónfutura.

Como control de exposiciónsubyacente,correlaciónde62retornosmensuales buyhold:finesnov2020–dic2025conúltimomesparcial,BTC/SPY0.5379,BTC/oro-0.0473,oro/SPY0.0420. Por eso independencia macro no puede asumirse al remuestrearcartera.

## Coste adicional

Análisis d3066f904a48465cb04e5afd5316eeab:manteniendoejecucionesytamañosfijos, añadir10bpsroundtrip(5porlado) dejaPNLshortdecartera+3627.35USDT frente+5287.02base;25bpsroundtripdeja+1137.86. Enshortsolo+1393.27/+124.52frente+2239.10base. No son nuevosbacktestsniCAGR/DDcontrafactuales; cambiarejecuciones cambia tambiénsizingyseñales.
