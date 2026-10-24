# Protocolo previo: shock relativo BTC/ETH1h

Segunda hipótesis estructural, no modificación fina de la reversión de rangos fallida. La relación se modela en retornos; no se asume cointegración, reversión de precios ni arbitraje libre de riesgo. Ningún dato de2026 entra en evaluación.

## Señal fijada antes del primer run
Dos rutas BTC/ETH1h,normal,2020-10-15→2025-12-31exclusivo,warmup240,10000,5xaislado,fee0.00045porlado. Cien cierrescontiguos1h idénticos timestamps entre activos. Fit OLS de96retornoslog estrictamente anteriores a2horasshock+1horaconfirmación; beta=Cov(BTC,ETH)/VarETH,alpha=meanBTC−beta*meanETH,sigma=stdresiduos. Rechazar varianza cero,beta fuera0.25–4,σnula,preciosno finitos o datosnosincronizados; no clippingbeta ni relleno de huecos.

Shock=sumadosresiduos2h previas>=2σsqrt2 envalorabsoluto. Últimahora confirma incrementoopuesto,pero residual3h mantiene signooriginal. Comprarperdedorrelativo/venderganador;ETHnotional=beta*BTCnotional. Elegibilidad exige beneficioaproximadoreversiónlog>=2roundtripscompletosdoslegs aBASEfee,thresholdfijoaunque seestresenfeesreales.

## Riesgo y salidas
Ambasqty/fees/margen/stops calculados antesde armar cualquiera. Stopindividualemergencia3ATR dehistorial ANTERIORa3barrasseñal. Riesgoinicialconjunto<=1%capitalconservador(minwallet/equity),cada pierna<=0.5%,fees+reserva10bps incluidos. Capglobal8% satisfecho porprototipoaislado;exigeexactamente2rutas ynointegraciónsilenciosaconreferencia. Gross<=4.4x,90%freemargintrasfeesambas. Cantidadesredondeadasabajopaso.001investigación,nativeconstraints pendientes.

Alpha/beta/sigma/preciospre-shock se congelan al entrar. Residualactivo=logBTC/refBTC−beta*logETH/refETH−alpha*horasdesdebase. Targetcruzacero;stopbasket alejamientoσsqrt2 desdeentrada;caducidad12h; controles debasket solo cierreshorarios. Cada3ATRstop sigueactivo intrabar. No parciales/piramidado,unaentrada yunasalidaporleg.

## Ejecución secuencial, no atómica
BTCleader crea plan compartido SOLOconambashistoriascerradassincronizadas;BTC/ETH callbacksencolanMARKET contra misma reserva. FollowerrequiereleaderQUEUED,nofilled: motor ejecutamarketsdespuéscallbacks. Cadaon_open adjuntastop yregistrafill;solo2fillscoherentes→ACTIVE. Verificacióncohesiónsegundofill+beforeciclosiguiente. Error dehora/precio/cantidad,pendinginesperadoouna legfalta→abortflag,cancelentryenpróximocallback yliquidarlegabiertaenpropio update. on_close deuna legactivaexitflag; contrapierna liquidaenpróximaupdate. STOPintrabarpuededejarhuérfana hasta1h,más outage;noafirmaratomicidad,coberturacontinuaniaprobaciónlive. Su propio3ATRstop limita riesgo planificado,peregaps superan.

Invariantes estrategia: timestamps<=closedtime,rejilla1hidéntica,96fitobservaciones,no parciales/piramidado,fees+margendoslegsreservados,riesgocada<=0.5%/basket<=1%/global<=8%,gross<=4.4,hedgerounding acotadoporpérdidadeunlot. Logsarm/exit y contabilizaciónbaskets/aborts/huérfanos para auditoría; no está implementado control de fillrechazado a nivel de exchange real.

## Falsación y controles
No promoverporWRalto. Descartar neto<=0ocostefrágil,DD>25%,exposiciónhuérfanasincontrol,edgeconcentradoenpicos. Menos100baskets→evidenciainsuficiente. Si promete, contrastepredeclaradoshock1hcon1horaconfirmaciónadicional;nooptimizar96/2sigma/12h buscando picos;períodosdesarrolloyaobservadosyvecindario solo después. Análisisbasket por pares completos yfeesdoslegs;auditorMTMv3ROOT para regularidad/calendario. Ningunalectura2026. NoMCindependientecomo certificado.

Todavía SIN run. ROOTrevisaráestado/draft. Si primerbacktestfallaETHmissing,importarBinancePerpetualETHdesde2020-08-15víaMCP;noavailabilityprecheck,nilocalbypass. Protocolo/precios/logcálculospuedenrequerirreparaciones de implementación,quetambiénsepreservarán.