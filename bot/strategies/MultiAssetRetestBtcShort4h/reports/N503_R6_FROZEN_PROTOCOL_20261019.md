# BTC N503 — protocolo congelado R6

Nueva ronda autorizada por el usuario: repetir exploración además de investigar convivencia entre suplemento y cortos originales. Dos agentes nuevos: btc_n503_r6 y btc_capacity_r6. Las diez hipótesis se fijan juntas antes de escribir fuentes, crear sesiones o consultar resultados nuevos. N204 continúa como referencia; N503 es semilla exploratoria no promovida.

2026 CERRADO incluso a inspección. Ventana2020-10-15→2025-12-31EXCLUSIVA, último día2025-12-30. Desarrollo histórico muy reutilizado, no OOS ni prueba anti-sobreajuste. No filtrar enero2021 ni otros periodos a posteriori para reparar la tasa de meses positivos.

## Presupuesto y contrato

Diez recetas×B/C=20fullsnominales. Cada agente dispara2simultáneos por ticketroot, máximo4global y2analysis. No siguientesparesautorizadosautomáticamente. No variantes nuevas, combinacionesposthoc ni búsquedas de umbrales después de ver resultados. Conservarcasosceros/bajamuestra/noefecto/fallos. Sólo un elegible tras20auditorías recibe6fulls adicionales:2feealtoy4vecinosdeTP. Si no hay elegibles, detener20. Reparacionesexclusivamentetécnicasse documentan,rawseconserva ysecuentanlosreintentosporseparado; no añadirhipótesis.

10000USDTshared;1%trade/8%agregado;isolated5x,nopyramid,cap4.4,reserva.001 sólo sizing;fee nominal.00045/lado. TresrutasBTC/PAXG/SPY4hBinancePerpetualFutures+tresfeeds1m,warmup240,debugtrue,fastfalse,charttrue. PAXGPortComparePaxgMarket4horiginalfeeBE;SPYBPortCompareSpySecond4h,CPortCompareSpyMarket4h. No adoptarBEfijoR3. No cambiosglobalconfig,framework,instalaciones,importspreventivos,Pi,live/paper,funding,research_scripts oHTTP/FSalternativo. Toda estrategia/datos/reportes medianteJesse-localMCP.

N204 yN503intactas,fuentes nuevas autocontenidasN503ExploreR601..605yN503CapacityR601..605. PreservarHP,originalesBTC long/STOPshort,prioridad,risk/sizing/ledger/capacidad/volatilityhelpers. Losrecorridoseconómicospuedencambiarporocupación/capital; noafirmaroriginalesidénticosencantidad/ejecuciónporbyteigualdad.

## Definiciones comunes

N503setupN204+ERfijo0<ER<=1/3. W=c[-13:-1]12barrashastas=c[-2],t=c[-1],D=t.open+14400000. AoriginalHLC3VWAPcohortq>0. d=max(Hs,Ht)+.25ATR_t-C_t,1..3ATR,MARKET,SL=fillE+d,TP=E−2d,48hdesdefill. No parciales. La lectura OHLCV es proxy, no observación de taker flow.

E601..605 añaden UNgate alsetup COMPLETOque alimenta explore_previous; el latch false→true avanza inclusoocupado/pending ysincola. ER yformulaA/q originalesintactos. Relojesexactos,datosinvalidosnoeventos. E604calculaelmismoddelasemilla,sinmoverobjetivos. E605usaúnicamenteminutosya cerradosdel trigger t, no minutos futuros ni posteriores a su decisión. IgualdadC1múltimo=Ctguardadebasesdeagregación;missing/mismatchquedaexpreso, no se vende comofallo de hipótesissi noobservable.

R(c) es READINESS TÉCNICO puro del originalSTOP, no elegibilidad económica: len>=140, finitosEMA120última/[-10],EMA20,ATR,RSI3;ATR>0,EMA120última>[-10],C>EMA120−ATR,RSI3<=20;e=min(L,C−.25ATR);dOriginal=EMA20−e;ATR<=dOriginal<=3ATR y dOriginal>=6*fee*e. G(c) es idéntico salvo que no exigeRSI3<=20. No llama_short_plan,_signal ni métodosconmutaciones; no usa margen/qty/capital/counterspara definirR/G. Reutiliza mismasfórmulas documentadasdeindicadoresoriginales, sinafirmarR=>ordenreal. P602recalculaRdelosprefijosvisiblesactualesc[:-1],[:-2],[:-3];noafirmaigualdadconestadohistóricoalmacenado bajo otrosbuffersrolling.

P601/P602vetanDESPUÉSdel latchN503 ygeometría,conevents/events_occupiedcontadosantesdelveto,nuevoscountersveto/accepted;eventoconsumidosinretry/cola mientrassetupN503sigaTrue. NoaplicarvetoalLatch(seríaotrahipótesis). P603..605entrada/latchN503exactos,modificansólosalidasdelsupp. Deadlines48hprioritarios. Sólo4hcompletaspostfill(open>=actualfill,close<=decision),contiguas;barclocksidempotentes,resetporfill. Nunca usarla vela parcialdeentrada. No forzaraperturaoriginalenlamismaevaluación,nilong/shortsimultáneo;el motor originaldecide en su ciclonormal. No inferirejecucionescontrafactuales deunshadowSTOP.

## Diez hipótesis
```json
{
  "explore": [
    {
      "id": "E601",
      "strategy": "N503ExploreR601",
      "seed": "N503",
      "rule": "Add to fullN503setup V_t>median(V W12throughs),strict. Mechanism exactlyR2N207 transferred to N503; notnewindicator/invention. ER<=1/3fixed."
    },
    {
      "id": "E602",
      "strategy": "N503ExploreR602",
      "seed": "N503",
      "rule": "Add previousbar s upperwicku=H_s-max(O_s,C_s)>0 AND u>=max(abs(C_s-O_s),min(O_s,C_s)-L_s). DistinctR2N206triggerbar t wick>=body; here s anddominanceoverlowerwicktoo."
    },
    {
      "id": "E603",
      "strategy": "N503ExploreR603",
      "seed": "N503",
      "rule": "Add composed rolling8hfromexactcontiguouss,t: C_t<O_s. NotUTC12henvelope;useslast2closed4hbars,nopartial,nofuture. Originaltredstillrequired."
    },
    {
      "id": "E604",
      "strategy": "N503ExploreR604",
      "seed": "N503",
      "rule": "Add roomtosupport: Lstar=minL W12throughs; requireC_t-Lstar>=2*d where d=max(H_s,H_t)+.25ATR_t-C_t exactN503geometry. ATRfinitepositive;original1..3ATRgate/order/2Rtargetunchanged. NochangeS/TPtosatisfyroom."
    },
    {
      "id": "E605",
      "strategy": "N503ExploreR605",
      "seed": "N503",
      "rule": "Add finalbar1macceptance: tclosed4h [t.open,D),D=t.open+4h. Requireexact240contiguousM1opensfromt.openthroughD-1m,noopen+1m>D,allOHLCfinitepositive/O,CwithinL,H/volume>=0. LastC1m==C_t exactsameaggregatedbasis elsefalse+countermismatch. RequirelastC1m<minL first180M1. Readsconfigured1mfeedonlyatdecision,nonewroute,nointraminuteordering. Coverageinvalidfalse+counter,notinterpolated."
    }
  ],
  "capacity": [
    {
      "id": "P601",
      "strategy": "N503CapacityR601",
      "seed": "N503",
      "rule": "AfterN503fullsetup/latch/1..3ATRgeometry,counteventthenVETOsupp if Gtechnicaloriginalshort True. G=RwithoutRSI<=20requirement;macro/price/distance/feegeometryretained. Consumeevent,noretrywhileN503setupremainsTrue. Nooriginalmethodcalls/mutations."
    },
    {
      "id": "P602",
      "strategy": "N503CapacityR602",
      "seed": "N503",
      "rule": "AfterN503latch/geometrycounteventthenVETO ifR(c[:-1])orR(c[:-2])orR(c[:-3]) withcurrentvisiblec>=143exactcontiguousclosed4hbars. CurrentbarRexcluded. Rprefixusesvisiblehistory,notclaimsameasoldrollingbufferindicator. Consumeevent,noretrywhileN503setupTrue."
    },
    {
      "id": "P603",
      "strategy": "N503CapacityR603",
      "seed": "N503",
      "rule": "Supponly:48hdeadlinefirst;firstcompletepostfill4hdecisionwithR(currentclosedcandles)=True closesMARKET. Neverforceopenoriginalinthiscallback,noconcurrentBTCpositions;originalentryreevaluatesbyunchangedenginecycle."
    },
    {
      "id": "P604",
      "strategy": "N503CapacityR604",
      "seed": "N503",
      "rule": "Supponly:deadlinefirst;whencompletepostfill4hbarhasRTrue,freezeitsoriginaltechnicaleSTOPshadowforEXACTnext4hbar. Atthatnextfullpostfillbar,ifL<=eSTOP ANDC<eSTOP closeMARKETatdecisionclose;notashadowSTOPfill. Shadowexpiresatnextbarwhetherusedornot,clockgapclears;Rcurrentcanrearmonexitbarifnolexit. Resetonfill."
    },
    {
      "id": "P605",
      "strategy": "N503CapacityR605",
      "seed": "N503",
      "rule": "Supponly:deadlinefirst;once>=6completecontiguouspostfill4hbars,ifNONEhasC<actualentryE ANDGcurrentTrue,closeMARKETatcurrentclose. AnyfavorablecompleteC<Epermanentlydisablesthisrulefortrade;resetonfill. Persistentchecksince6,notonlysixth. ExplicitcontextualreuseR4T402,notclaimnovelmechanism. Entry/SL1R/TP2R/48hrestunchanged."
    }
  ]
}
```

E601 es transferencia explícita de R2N207 a nueva semillaN503, no indicadorinédito. E602difiereN206porvelas(envezdet)ycomparamechainferiorademásdecuerpo. E603noesunbarrido12h→8hdelenvolventeR5:pruebasóloreversiónrollingdelcuerpocompuesto. P605reusaestancamientoR4T402concontextooriginalyregladesde6explícita;escenariocontrolado nuevo,no cinco inventosindependientes. Se distingue novedad de mecanismo de nueva combinación sobre semilla.

## Auditoría y puertas

Referencias ya resumidasantesR6: [N204B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142), [N204C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794), [N503B](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752), [N503C](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65). Comparación conN204para elegibilidad y conN503para atribución. Una mejora de regularidad respectoN503 con neto menor aN503puedeserútilSI superatodaslaspuertas frenteN204;no cambiar comparaciónultimate.

Auditor de fills/qty/fees/PNL/wallet/terminal/MTMUTCdiario,cuatroanclascongeladas,de61meses/19Qcompletos y63/21incluidos. Positivos>0sinredondear,activosycalendarioexpresos;cohortesdetradesnoseconfundenconMTM. DDmotor yDDcierrediarioseparados. SupplementMARKETvsoriginalSTOP/long,ex1/ex3+10,exposición/notional×time/años ydesplazamientoscomo diagnósticos, noalfaaislado. Overlays5/10bpsRTañaden.00025/.00050porfill,qty/precio/tiemposfijos,no rerun ni slippagepuro.

ElegibilidadTODOSambosB/C:ΔnetnominalN204>1e−7USDT;+5Mpositivos/activos>=65%yQpositivos>=80%encompletoseincluidos;+10net>=N204−1e−7;DDmotor>=−25%. Toleranciascontablesprefijadas, nofortalecerni relajarsegúnlosresultados. Rankingpredefinido:mayormínmargenM65/Q80deambosbins/B/C;mayormínΔnet+10;menorpeorDD;IDlex. Noelegible=>ceroverificaciones.

ÚNICOelegibletras20:feeengine.00070/ladoB/Cmismafuente,contraN204feealtoB9a6c7c24-8847-42d1-aadb-206f21723c1f/C541d2bf4-ffca-4f2d-969b-c25165e7b960. ExigirΔnet>1e−7,M65/Q80full/includedambos,DD>=−25;si falla,noseescogealternativa. Esefee puedecambiarsizing,PAXGBE yReadinessporcostegeometría,noesoverlaydeqtyfija. Otros4fullsnominalesvecinosTP1.8R/2.2RcadaB/C,SL/d/48/restofijos,noelegirmejorvecino,nuevafórmulaodeadline. Conservarla matriz de sensibilidad sin reclasificar vecinos como candidatos.

## QA y entregables

Antes de cada primerpar: fuenteexacta/protectedmethods/branchoriginal/prefijosinmutables,casosfrontera/datainvalid/clocksgapduplicatefuture,gestiónreset/deadline/entrada-parcial,ERoriginalfijo,semánticadeveto vssetup,shadowcaducaynoejecutaoriginal,progresoirreversibleP605. E605fixtures240M1cerrados/Cidentidad/missing/duplicados/V0/mismatch. Noclaim de pruebaMCPfrontendcon stubs; financiera secomprueba con fulls reales.

ReportesMCP:protocolo10,fuentesQA,métrica yURLdecada20fulls,matriz20,registro,sourcereadbacks,diagnósticodeconcurrenciaR/Gcounters/operacionesobservadas,selecciónyverificaciónúnicasiaplica,revisiónindependiente. No aumentarconfianza por repetiridénticasejecuciones, nocombinarseedganadoresposthoc. La regularidadconcostesreales y el sobreajuste siguen pendientes hastaevidenciacorrespondiente;2026continúacerrado.
