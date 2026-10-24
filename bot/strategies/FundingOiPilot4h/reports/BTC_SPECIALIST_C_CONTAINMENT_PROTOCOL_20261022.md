# Línea C — contención completa frente a contención del cierre
Fecha local2026-10-22. Estado: protocolo propuesto y revisado conceptualmente por root; sin implementación, draft, job, precio o motor. Root asignará implementación y slots. Complemento de A continuación por aceptación temporal y B fallo/reversión; no exige especialización por lado.

## Pregunta y mecanismo
¿Una vela previa enteramente contenida dentro del rango de una vela madre mejora la operativa de ruptura posterior de ESA madre, frente a exigir solamente que el cierre previo esté dentro?
La intuición económica es que el rango negociado se contrajo dentro de una referencia fija antes de su liberación. No se afirma demanda nueva ni volumen absorbido: OHLC sólo acredita contención. El rival es que las mechas intrabar no añadan nada al cierre, o que la restricción reduzca oportunidades sin mejorar calidad. Un resultado negativo cierra esta regla; uno positivo frente al control sólo acreditaría diferencia bajo estas políticas y desarrollo reutilizado.

No se añade condición de rango expandido en la vela de resolución: sería parcialmente mecánica respecto de la ruptura y confundiría la pregunta. No se supone compresión absoluta de volatilidad: la madre puede ser amplia.

## Antecedentes exactos y diferencia material
Se leyeron Hub20261022-r31/HANDOFF y K1001_LONG_SUPPLEMENT_CLOSURE_FINAL_20261022.md; diagnóstico cerrado, no se vuelve a explicarlo.
- V6_NR7_PROPOSAL.md: barra previa estrictamente menor de7rangos; cierre actual fuera del rango de ESA barra estrecha; TP3R/96h. C compara anidación H/L de B1 dentro B2 y salida del rangoMAYOR deB2, no rankingNR7 ni ruptura deB1. Sin afirmar fenómeno nuevo.
- BTCExploreR802 fuente completa porMCP: intersección de6rangos [maxL,minH], cierreB1dentro, B0roja y cierrepor debajo; suplemento sólo short de libro3activos conotrasreglas. Cusaúnicamadre2barrasatrás, ambasdirecciones y controlclose; nointersección ni veto decolor. Su negativoR8seconserva, no se traslada a esta cuenta.
- BTC_DISCOVERY_CD_FINAL_20261021.md y BtcResearchR11Base1m: absorción exige alto volumen/cuerpopequeño luegoescape; relojesDrompen3bloques. CnoeligealtoV,actividadreloj,shock ni cuerpopequeño.
- K1001/MARKET no es control equivalente: no usa madreanidada ni horizonte24h. No rescatarKconoffset,TTL,trailing/filtros.
- LíneaA confirmó no estudiarinsidebars; aceptaciónM1deuna frontera es otro eje. El parentesco amplio de ruptura se conserva y no se reclama independencia ni deduplicación universal.

## Reglas causales completas, simétricas
Ruta de ejecución BTC-USDT Binance Perpetual Futures1m; dato auxiliar propio4h. Decisiones T exactamente múltiplosUTC4h. B0=[T−4h,T), B1=[T−8h,T−4h), B2=[T−12h,T−8h), todas cerradas. B2 es MADRE; B1 contención; B0 resolución. No seleccionar otra madre retrospectivamente.
La base común valida64OHLC consecutivas y alineadas4h terminandoT; la señal sólo usa las últimas3 y ATR14 sólo las últimas15.  todoOHLCfinito,positivo y coherente L<=min(O,C)<=max(O,C)<=H. Gaps,duplicados,desalineación,NaN/Inf u overflow invalidan decisión sin imputación/compresión. Prefijos más viejos/futuro no influyen. Volumen no entra: no exigir volumenpositivo para regla deprecio.

CondiciónCOMÚN: H2>L2 y L2<C1<H2. TratamientoINSIDE añade H1<H2 yL1>L2 estrictos. ControlCLOSE_ONLY no exige contenciónH/L: incluyeinsidebars ymechasfuera si su cierreestádentro. IgualdadC1enbordes noadmite; igualdadH1=H2oL1=L2 excluyeINSIDE pero puedeadmitirCLOSE_ONLY. No agregar color,númerodeinsidebars,ADX,medias,volumen,OI,funding,horarioodía.
Dirección: +1siC0>H2;−1siC0<L2;0resto. C0igualborde noentra. Doble ruptura intrabar H0>H2 yL0<L2: el cierre seleccionaúnicamenteunlado; si vuelveadentro,nada. No inferir orden intrabar ni colocar fills enH2/L2retrospectivamente.
Oportunidad única de ESA tripleta al cierreT. Caduca enT después de evaluar, incluso ocupado,pendiente,mismosalida,ATRinválidaosizingfallido. Sin latch,cola,reversión ni orden diferida. Rearmado enT+4hcon nueva tripleta B2/B1/B0; una vela puede servir a dos tripletas con roles distintos y se declara, no son episodios independientes. No imponecuota diaria nueva: una posiciónBTCporcuenta ybloqueo noentradaenelmismotimestampdecierre.
La regla se computa antes de comprobarocupación en ambaspolíticas; validacionescomunesidénticas. Señaltratamiento es subconjuntoestático decontrol portripleta, pero las cuentasrealizadas no serán tradesemparejados necesariamente: ocupación/capitalcambian.

Entrada MARKET enT alprecioactualconocido,C0coincidente conprice (assertparidad), sólo start<T<finish,flat/sinpendiente/noexitmismoT. ATR14simpleactual: media de14 TRj=max(Hj−Lj,abs(Hj−Cjprev),abs(Lj−Cjprev)) deB13…B0con15cierres; incluyeB0, noWilder/EMA niATRprevio. ATR>0finito. Distancia d=2ATRcongelada. Stopdesde fillreal e−s*d;sinTP,BE,trailing,parciales,ratchetoseñaldesalida. Esta gestióncomún24h es comparacióncontrolada,noóptimo.
Salida MARKET enprimerafrontera4hconT−opened_at>=24h. Tiempoabsoluto, no número deventanasválidas; protecciónstopintrabarcontinua. Invalidezseñal no suspende salida/protección. Cierreterminalconcostosincluido; noabrirdatos2026. R11gestionaFINALpostliquidación cuando corresponda.

## Cuota y economía congeladas
Cada escenarioalternativo empieza10000USDTtotales, sólo cuota1%activa: legacy_plan(event,.5*wallet,.5*available_margin,3,.00045). No usar5000como denominador deCAGR ni reasignarcuotaociosa. Helperexistente2%aplicadoamediawallet hace1%dewallettotal; reserva.001sóloparasizing/lote.001/nocional4.4sobrecuota/margen90%segúnfuente. No alternarentry_planR10(.00000001sinreserva). Stopfees+reserva enpresupuestoprevisto, funding/gaps/slippagepuedensuperar; leverage no multiplicaqty/PnL otra vez.
BTCtotalfuturo2%eneventualescuotasiguales,global6%,isolated3x. Sin afirmarcuentaconjunta: no sumarscenarios.
Fee.00045takerdescuentoporlado,fundinghistóricoONsnapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,marksproxydeclaradas,slippagemodelado0. Sin señaldefunding/OI. UTC[2020-10-15,2026-01-01),warmup240 según configuración común,10kcontinuos. Desarrolloadaptativoreutilizado,noOOS.
R11wallet+PnLabiertoM1+fills,2.741.760marcas,63intervalos/62mesescompletos/20Qesperados. Fronterasmensualespostfunding/predecisión; noextremosintraminuto.

## Dos casos y presupuesto
INSIDE = BtcResearchR32InsideRange1m; CLOSE_ONLY = BtcResearchR32CloseRange1m. Máximo2motores económicos, uno porcaso, controlnoreutilizableporquecontrato/señaldifierendelprevioNR7/X802. Rootcoordina slots, fuentes,preflight,config,checksyauditoría. No ejecutar enesteentregable. Cualquierfallotécnicoseconserva; rootdecidecorrecciónmínimatécnica yrecuperaciónmismoIDantestodoreintento,noaprobaciónautomáticadeotrocaso.
Sinvecinos,grilla,optimización,sweepdedirección,eliminacióndeunladoorecortedeañosdespuésdePnL.

## Criterios y decisión
Reportaramboscongatesr9: CAGR>=30%,PFUSDTnet>=1.2,DDM1+fills<=25%(objetivo20),>=65%mesesactivoscompletospositivos,>=80%trimestrescompletospositivos,medianamensualcalendario>0(inactivosincluidos),netoaritméticosin2mejoresmeses>0,N>=100sólosuficienciaoperativapreliminar. No bajar30%porcuota1%,noaumentarriesgoparaaprobar.
AdemásN,señales,admisiones,exposición,turnover,amboslados,años,rolling12m,gross/fees/funding/regularidad yconcentración. MayorPFoCAGRrelativo noalcanzaparaaprobar. Siambasfallan,cerrarCsinpruebassustitutivas;controlmejornojustificapromoverloautomáticamente. SiINSIDEcumple,seríacandidatahistóricaparavalidaciónposterior/acuerdoconjunto,nooperación.
Estapreguntacambiaunadecisiónreal: si mantenercontenciónH/Lcomocaracterísticaevaluabledeunespecialistadeexpansión oretirarlaenestareceta, frenteausarcualquiercierreadentro. No determinaarquitectura2/3niotraspatas.

## Checks previos y evidencia
Sin jobs enesteprotocolo. Rootdebeverificarsintéticamente: B2/B1/B0,índices y validación64 común con ATR15,causalidad/prefijos/futuro,gaps/alineación/finitud;strictinsidevsclose,inclusióndelcontrol,igualdades,dobleruptura/cierreadentro,reflexiónlongshort;avanceocupado/sameexit/caducidad/nuevatripleta;oráculoATRinclB0;helpercuotareserva/lote/margen/stop/riesgo;MARKETactualsinTP;horizonte24h/últimoborde/terminal;observerR11intacto. Probarfuentesliteralescongeladas,AST/compile sin importarproyectoreal cuando corresponda.
R32_PLAN registra meta compacta con madre/bordes/inside y clocks; R32_OPEN común registra origen,signal_at/opened_at,fill/qty/distancia/stop/risk_budget; CLOSE y SUMMARY comunes. La reserva.001 está congelada en helper/fuente y no se duplica como gestión dehoja. Verificar con checks que cada línea emitida queda debajo1800caracteres antes del prefijoMCP; evitartruncado2000. R11mesesseparados;readbackexacto/hashespreengine.
Auditoría posteriorindependientefundingledger+fills, gross−fees+funding=PNLsum=equityfinal−10000conerror<1e−6;posicióndefinal,causas/tiposreales,quotarisk,conteos,transporteymesescompletos. SinprometerPITindependienteporchecks.

Prohibiciones: noestrés/riskgrid/nuevosdatos/spotperpimport/USDC/2026nuevo/cartera/livepaper/Pi/install/configglobal. ReporteyCODESporMCPdentrodelproyectoJesse.


## Actualización de infraestructura antes de implementar
Leída completa por MCP BtcResearchR32SpecialistBase1m y BTC_R32_COORDINATION_PROTOCOL_20261022.md. Esta actualización sustituye la base específica propuesta inicialmente, sin modificar señal, distancia, sizing o gestión de C. CODES contiene sólo dos hojas; ninguna gestión u observación duplicada.
La base compartida hereda R11, observa M1 y valida64barras4h mediante closed_window. En frontera4h llama _event(rows,now) antes de ocupación,guardasSTART/FINISHysizing. Las hojas devuelven None o dict(direction=±1,meta compacta); no tienen estado/latch y no requieren _invalid_event propio. Se consume cada tripleta al evaluarla; invalidación de64 común produce ausencia de evento y no arrastra madre.
Ambas hojas fijan HOLD_HOURS=24,TP_R=None y LABEL único C_INSIDE/C_CLOSE_ONLY. Heredan todas las órdenes, stop2ATR14, salida24h, helperlegacy.5/.5,reserva.001/lote.001,logsR32yobserverR11. Control importa sólo función pura containment_event desde móduloINSIDE: dependencia debe congelarse en manifiesto; no importa ni instancia una estrategia de cuentaalternativa.
No nueva base C, gestiónpropia, supuesto conteo de decisionesextra o promesa de logguard no presente en fuente común. Root verificará tamaño real de PLAN/OPEN/CLOSE/SUMMARY y la base compartida antes de motor. Reportes leídos completos, sin implementación/jobs/motores aún.
