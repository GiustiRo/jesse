# Tanda Q — desplazamiento BTC relativo a ETH frente a precio BTC

Prerregistro2026-10-21, antes de nuevas fuentes/drafts/economía. Pregunta: ¿normalizar el nivel logBTC por una beta histórica de retornos frenteETH produce una operativa BTC individual de reversión útil, comparada con la misma regla de precio BTC con beta0? Dos recetas cerradas, no quitar la pata de un par existente ni refinar el filtroETH de J.

## Antecedentes y selección

Leídos completos por MCP: OrchLateralRelativeShock1h (parBTC/ETH de dos patas, OLS96retornos1h,shock2h yconfirmación), R40PaxgBetaResidual1h (PAXG/SPY,OLSlogniveles de60fixings,z1.5 ysalida residual), BtcResearchR13ExternalBase1m de J (ETHconfirmación1h deimpulso, BTCdirection). Son antecedentes materiales conservados; no afirmar novedad universal. Q cambia pregunta/variables/horizonte y opera sóloBTC:β de retornos4h previos y desplazamiento de niveles conβcomún a toda referencia; salida fixed independiente del modelo. No deriva PnL BTC de las dos patas antiguas ni suma curvas, no usa desempeño2026para selección. Los datos2020–2025 ya fueron examinados por muchas tandas; Q es desarrollo adaptativo, no OOS ni prueba independiente. P se cerró sin candidata y no se rescata con vecinos.

HashesSHA256 de textos completos:
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- OrchLateralRelativeShock1h: 4a0fb55580b5eda3b5bd954b829860eb15c40fb1b5f592d143d418f11956a610
- R40PaxgBetaResidual1h: f445b96c2b92686228a7976943bf8b4c1ab9ae53b1c77bc8792c6d58f3a8f4f8
- BtcResearchR13ExternalBase1m: aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a

## Regla exacta causal en T4h

Datos BTC4h yETH4h:242 barras cerradas consecutivas porstream, últimaopen=T-4h, timestampsidénticos; incluir sóloopen+4h<=T. Validez común en AMBOS modelos:242exactas,sync,OHLCfinito/positivo ycoherente,ninguna vela parcial. BTCúltimoclosealineadoconprecioactual. Sin imputación, no preinspección de cobertura. Si faltan datos el motor informa; sin importaciones.

βT=cov(rBTC,rETH)/var(rETH) sobre241closesPREVIOS rows[-242:-1], dando240retornoslog4h. Excluyeamboscurrentclosesdelajuste. Usarcentrado/denominador deOLS equivalentea covarianza/varianza conmisma normalización. Si varETH<=0 o nofinita,βnofinita:commoninvalid,resetestado0/noentrada enAMBOS, incluidoβ0. Sin eps,clipping,regularización,winsorizing ni vetoβnegativa.

Tratamiento RESIDUAL:levels=logBTC−βTlogETH. Control PRICE:levels=logBTC conβmodelo0. En ambos reference=levels[-61:-1],60nivelesPREVIOS;mean/reference,std(ddof1),currentlevel=levels[-1],z=(current−mean)/std. EnRESIDUAL usar EL MISMOβT al recalcular toda referencia ycurrent; no mezclar residuosdebetashistóricas. Encontrol la validación/βTETHsigue común aunque no se resteETH. σ<=0/nofinita o z nofinito implicaestado0; no epsilon. Umbral fijo:estado+1(long) si z<=−2;estado−1(short) si z>=2;resto0. No flipdireccióntrasPnL.

Evento nuevo sólo estadoactual no nulo distinto delestadoalmacenado;actualizarestado cada4h,aunocupado/pendiente/sameexit. CambiarβT/μ/σpuedeoriginartransición aunqueBTCquieto: aceptadoahora, no esconderlocomomeanreversioncausalprobada. Gap/commoninvalid reiniciaestado0; recuperacióndatospuede crearun nuevoevento. Estado0porσplana tambiénconsume/reset. Ocupado descartar sincola; noentrada tras salida enmismotimestamp. MARKETBTC alcloseconocido, ceroórdenesETH. Una única posición2%total.

## Gestión, riesgo, costos y medición congelados

Tres fuentes nuevas: BtcResearchR17RelativeBase1m, BtcResearchR17RelativeResidual1m y BtcResearchR17RelativePrice1m. Base hereda observador/fill/gestión/cierre R11 sin cambiarlo. R10 closed_window/atr14/entry_plan sin cambios:ATR14SIMPLE4hBTCactual,stop2ATR/TP2R y48h,gestiónsólocierres4h,proteccionesM1; noTPdinámicoβ,ratio,recovery,refit otradeETH.

RutaBTC-USDT BinancePerpetualFutures1m,dataBTC4h+ETH4h,warmup3004h. Ventana[2020-10-15,2026-01-01)UTC,10k,2%poroperación/6%agregado/3xaislado,fee.00045porlado takerdescuento,fundingBTChistóricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado/proxydeclarado,slippageaplicado0. SizingR10 feeaware90%margen/floor8 sin reservaextra deP ni cambiosriesgo. Fecha final excluye2026. Sin estrés/riskvariants/nuevosdatos/import/live/paper/Pi/framework/global/install/restarts/scripts.

No claim de cointegración, estacionariedad, par neutral ni arbitraje:BTCsolo puede perder aunqueelratioseacerque, siETHse mueve. βdescriptiva de retornos no garantiza nivel estable ni beneficio después deSL/TP/costos.

R11congelado equity=wallet+PnLabierto M1/fills,cortesUTC00postfunding/predecisión porfase,DDM1+eventos sinextremosintraminuto. Logscompactos de fill incluyen beta ajustada/modelo,μ/σ/z/n ysentido; fillsrealizados separados deeventosdescartados. Resumen final acompañaR11 sin milloneslíneasM1.

## Presupuesto y puertas

Exact2económicas RESIDUAL/PRICE; hasta2reemplazos sólo técnicosdocumentados, nunca porPnL. No barrer242/240/60/2/βclip/plazo/direccióntrasresultado. Una misma validez/muestreoexógeno paraambas, pero sus estados/ocupación pueden diferir. Si PRICEfalla no prueba queETHmejora; comparar diferenciasdescriptivas con dependencia/selecciónreconocidas y exigir cada cuenta susgates.

Gatesr9: CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activospositivos,Q80completos,medianaretornomensualcalendario>0 incluidosinactivos,netoaritmético quitandomejores2meses>0,N>=100preliminar no confianza/potencia porconteo. Aspiraciones40–50%+/M70 no sustituyengates. NO_CUMPLEalfallareconomía,INCONCLUSA si favorableconmediciónfaltante. No OOSreclamado.

Antes de economía:readback/hashfuentesnuevas/deps ychecks temporales supplied-sourceAST, sin importingestrategiasreales/framework ni datosobservados. Cubrir242/241/240/60índices,betaexcluyecurrentambos,oráculocov/var,βnegativapermitida,commonvalidETHenPRICE,normalizaciónmismaβenreference/current,σ0noeps,signos±2/transiciones/refit/gaps/sync/futuros,advanceocupado/noqueue,sameexit,ATR/risk/SLTP48hheredados. Guardarcódigo/resultados/errores yCODES completos. Sinbacktestdesdeanalysis. Root revisa fuentes y manifiesto genuino/drafts/preflight antes motor. Después auditoría completa gross−fees+funding=PNLsum=equityfinal−10k1e-6USDT,2.741.760marcasM1,63intervalos/62meses/20Q yterminalfee. Hubinmutable archivosprimero/índiceúltimo. Si falla,cerrar presupuesto y otra pregunta material sin retocarQ.

## Límite numérico preeconómico

La implementación usa directamente logBTC−βTlogETH y std(ddof1) declarados, sin epsilon económico. En relación proporcional perfecta, logaritmos/OLS y resta pueden producir sigma residual positiva casi0 por redondeo en lugar de0 matemático; se aplica literalmente el z/umbral resultante si sigma>0, yestado0 si sigma<=0/no finita. Esto puede producir eventos sensibles al redondeo en casos degenerados; no se interpreta como ventaja ni cointegración. El check incluye caso proporcional con diagnóstico explícito, además de invariancia de unidadesBTC/ETH en caso no degenerado. No se observó mercado para elegir estabilización o tolerancia. La alternativa de centrar algebraicamente no se añade después de resultados.
