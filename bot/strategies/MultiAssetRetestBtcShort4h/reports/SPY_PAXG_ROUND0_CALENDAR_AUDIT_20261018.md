# SPY/PAXG — auditoría independiente de la primera ronda

Fecha18oct2026 America/Montevideo. Seis full nuevos terminados: dos controles aislados1% y cuatro alternativas predeclaradas. Ninguna alternativa aceptada. Ventana2020-10-15→2025-12-31 exclusiva,2026intacto,capital10000USDT,fee.00045lado,5xaislado,fundingfuera. BTC y referencia sin cambios. Se verificaron cuatro backtests simultáneos aceptados por servicio; ningún cambio configuración global.

| Sesión | Trades | NetoUSDT | Antesfees sobre mismosfills | DDmotor | Meses+activos /todos | Trimestres+ |
|---|---:|---:|---:|---:|---|---|
|[SPYretestcontrol](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2)|31|751.35|1037.83|−5.21%|15/33;15/63|10/21|
|[SPYORB60](http://localhost:9200/#/backtest/a68dbfa8-3efe-410a-9c8b-861bf3609f38)|890|−6273.02|1286.19|−63.75%|15/61;15/63|0/21|
|[SPYDrive60](http://localhost:9200/#/backtest/98918ea4-78a2-4548-8f23-8c7459d07a30)|1162|−8700.06|869.41|−87.22%|11/63;11/63|1/21|
|[PAXGretestcontrol](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c)|35|546.11|792.72|−6.92%|15/32;15/63|9/21|
|[PAXGshockcontinuation](http://localhost:9200/#/backtest/73464795-1e47-4f0a-9239-fd8901775dc2)|235|−2140.19|−507.83|−30.66%|21/61;21/63|9/21|
|[PAXGshockreverse](http://localhost:9200/#/backtest/aca7b3b8-3781-4986-8ed6-0ede625ba31c)|245|−2398.95|−785.75|−26.46%|25/61;25/63|8/21|

## Método y verificación
Root leyó referencia y seis fuentes nuevas. Controles aislados son copia literal de referencia salvo nombre de clase y riesgo. Con una ruta shareATR=1: retornos no replican contribución de cuenta compartida. PAXG espejos difieren sólo RESPONSE,ATRprevio excluye señal,48h desde fill. SPY acepta rango primera hora conocido,NY/DST,60M1consecutivas y parityclose; ocho trades por política cruzan medianoche por cotizaciones ausentes, no se usó falso cashMTM.

AuditorV4 leído completo porMCP y ejecutado inline en run_analysis. Primer análisis8623effa4baa4d4492c7c286f6e6c65b falló por insuficientes anclasBTC, no por métricas económicas. Se cambió sólo selección de snapshots de anclaje a fade/reject/sleeves históricos conocidos; no datos/precios externos ni fuentes nuevas. Auditor definitivo a19d7e0afb404303aa33ca7cc1c19c53 succeeded,exit0. SelftestsPASS;21BTC,67PAXG(50timestamps),15SPY anclasMARKETmedianoche,escalas constantes a<2e-15,errornumérico. Benchmark2e943276... aporta sólo precios del mismo histórico; su estrategia antigua no se usa como evidencia económica.

Fees porfill,PNL,walletterminal y contadorespreterminaciónPAXG1/1 concilian. Cierre de frontera no certifica liquidez. Valoración diaria UTC porfills y cierres observados, arrastre sólo valoración de cierres mercado, sin fabricarvelasnegociables. NoPNLpor mescierre. Curva motor00:01 NOcierreUTC. DDcierresdiarios difiere:SPYbase−5.218,ORB−63.748,Drive−87.281;PAXGbase−6.922,continue−30.676,reverse−26.456.

Períodoscompletos:61meses,19trimestres. SPYbase15/33activos,9/19q;ORB15/59,0/19q;Drive11/61,1/19q. PAXGbase15/31,8/19q;continue20/60,8/19q;reverse25/60,6/19q. No se exige regularidad a señales; se informa para diagnóstico.

## Decisión
Archivar estas cuatro recetas sin rescatar horas/umbrales/direcciones. SPY pierde porque incremento bruto por giro (~1.53/0.82bps) es muy inferior a~9bpsfees. PAXG pierde también antesfees. No prueba que todas las estrategias de activos fallen. Segunda ronda predeclarada: exposición lenta SPY versus beta protegida, y reversión PAXGfinsemana versus controlweekday. No integración de candidatos perdedores ni abrir2026.

Artefactos temporales enjobdefinitivo:calendar_audit.json,*_calendar_month_returns.csv,*_daily_close_equity.csv,*_route_mtm_contributions.csv. Cadanuevo informe de agente persiste fuentes/sesiones/diagnósticos. Protocolos:SPY_PAXG_INDEPENDENT_RESEARCH_PROTOCOL_20261018.md y reportes específicosResearchSpyReference4h/ResearchPaxgShockContinue4h. Proxies aceptadospara investigación precio;fills/slippage/líquidez perpetua no demostrados. 2020–25desarrolloadaptativo, no OOSlimpio.