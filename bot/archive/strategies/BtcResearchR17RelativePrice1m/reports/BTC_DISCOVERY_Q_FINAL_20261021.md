# Q: desplazamiento relativo BTC/ETH, cierre

Ambas políticas pierden yningunacumpleobjetivos. RESIDUALmejorarelativamente aPRICEenCAGR/PF,pero no seafirmaedge validada/superioridadindependiente. FallanCAGR30%,PF1.2,DD25%,M65,Q80,medianapositiva yconcentración aritmética. No retirarshorts,invertirregla,z,beta,ventanas,TPoplazopararescate. PresupuestoQcerrado.

|ModeloBTCsolo|N|CAGRneto|PF|DDM1+fills|M+activos|Q+|Mediana mensual|Neto sin2mejores|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[residual](http://localhost:9200/#/backtest/e73bf5e8-688e-4c5f-9ef9-d54f135b3329)|319|-8.3625%|0.8646|54.6898%|24/62|8/20|-1.4710%|-5843.2633|-0.4808|
|[price](http://localhost:9200/#/backtest/dd092c9a-f668-412f-aca7-b73ecf1cb76b)|312|-12.7061%|0.7761|54.5700%|22/62|6/20|-1.2504%|-6436.6213|-0.8049|

## Contraste y contrato

242barras4hBTC/ETHsincronizadas;βOLS240retornosPREVIOSexclactual,60lognivelespreviosyactualbajoMISMOβT. RESIDUALlogBTC−βlogETH,PRICEβ0. VarETHpositivafinita/sharedvalidityparaambos;βnegpermitido,sinclip/epsilon;σ<=0neutral. z<=−2long/z>=2short,freshstateavanzaaunocupado,refitpuedetransicionar. NoETHorders,nocointegraciónni neutralidaddecarteraacreditadas; una recuperación de ratio porETHno garantizagananciaBTC. No rescatarparlegacyquitandopataETHnifiltrarJdenuevo.

GestiónR11/R10frozen:unaposición2%feeaware,6%capnovinculante,3xaislado,margen90%floor8;SL2ATR14simple4h/TP2R/48hgestión4h,proteccionesM1.10k,BTC-USDTBinancePerpetualFutures,ruta1m/datosBTC4hETH4h,warmup300;[2020-10-15,2026-01-01)UTCdesarrolloobservado. Fee.00045porlado takerdescuento,fundingBTCdatasetfrozen9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571aplicado/verificado,marksproxydeclaradas,slippage0. Neto trasfees/fundingmodelados,no todoscostosreales. SinfundingETHporqueETHnooperó.

## Cuentas y calendario
[BtcResearchR17RelativeResidual1m](http://localhost:9200/#/backtest/e73bf5e8-688e-4c5f-9ef9-d54f135b3329):bruto-1824.640484,fee1803.336986,funding-31.039806,neto-3659.017276(-36.5902%),capitalfinal6340.982724USDT. DDdiarioframework-54.1618% distintoM1. Stats{"stage":"FINAL","mode":"RESIDUAL","long_fills":144,"short_fills":175,"signals":452,"occupied":133}. AñoscompletosdesdeM1mensual{"2021":9.77927073437872,"2022":27.990403894111427,"2023":-28.642193744798373,"2024":-23.34925698029996,"2025":-8.94588687871558};rolling12{"N":51,"positive":22,"min":{"start":"2023-11","finish":"2024-10","return_pct":-36.220949261646},"max":{"start":"2021-11","finish":"2022-10","return_pct":38.016726103780044}}.

[BtcResearchR17RelativePrice1m](http://localhost:9200/#/backtest/dd092c9a-f668-412f-aca7-b73ecf1cb76b):bruto-4001.107926,fee1365.602994,funding288.773547,neto-5077.937373(-50.7794%),capitalfinal4922.062627USDT. DDdiarioframework-53.5384% distintoM1. Stats{"stage":"PRETERMINAL","mode":"PRICE","long_fills":144,"short_fills":168,"signals":400,"occupied":88}. AñoscompletosdesdeM1mensual{"2021":-2.8059636410820876,"2022":-11.668302440882329,"2023":-1.113060755528894,"2024":-17.86436776885797,"2025":-21.402335504990212};rolling12{"N":51,"positive":10,"min":{"start":"2023-10","finish":"2024-09","return_pct":-28.278348351408933},"max":{"start":"2021-06","finish":"2022-05","return_pct":6.609939306708412}}.

Calendario descriptivo calculado aritméticamente deintervalosR11completosMCP;2020incompletono entra en añocompleto,51ventanas12mesessolapadasno independientes ni OOS. Resultadosporladoexplicanledger,noseusanpararetirarshorts.

## Verificación y límites

Auditoríaa55de9597b6e4e61a6f0b1a1f40ae29dsucceeded;631registrosdepolíticasalternativasnoindependientes. Fullsnapshotsgross−fees+funding=PnL=equityfinal−10000 error<1e−6USDT,fundingconciliado. Telemetríavalidada2.741.760marcasM1,63intervalos/62meses/20Q,invalid0entimestampsBTCyETH,fillcounts319y312igualesmetrics;monthlytelescopingcuadra. RESIDUALFINALpostliquidaciónterminalfeeincluida;rawopen1esmetadataPRE,no pendiente económico. PRICEPREsinposiciónterminal.

DDwallet+PnLabiertoM1/fillsno todosextremosintraminuto; cortesUTCpostfunding/predecisiónporfase,no agrupaciónestrictaeventosfecha. Mediana calendarioconinactivos,M65activoscompletos; N>=100preliminaroperativo,nopotencia/confianza.

Doschecksintéticosexitosos(99y108assertions),0errores,CODES8readbacksidénticos,root+indepreviewconformes,protocolo/manifiestoantes2motores. ExtensiónreescalaBTC/ETH ydiagnósticoproporciónperfectaδσ2.239e−16/z.9916neutral, sin cambiarfuenteeconómicaniañadirepsilon. Noclaimderobustezeconómicaporcheckmatemático. Dosbacktestseconómicoscompletados,0fallos/reemplazos/backteststécnicos. TotalA–Qdesde r9:32económicas,noindependientes;V1–V6209separadas.

No estrés/riskvariants,nuevos2026/live/paper/Pi/framework/global/install/restarts/scripts. ContinuidadR: pregunta distinta deformasmultibarra/kNNNumPymínimoconcontrolmediaglobal,protocolo/checkenpreparación,no economíaaún. R20PAXGanálogosnegativoyM/G/Angleestadospreservados, nonewfamilyclaim. No promociónoperativani estrésautomático.
