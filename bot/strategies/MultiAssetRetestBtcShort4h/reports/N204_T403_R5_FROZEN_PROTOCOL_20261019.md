# N204 / T403 — protocolo R5 congelado antes de resultados

Usuario autorizó una nueva ronda con dos agentes nuevos. Semillas: N204 ganadora vigente; T403 candidata no promovida, no ganadora alternativa. Todas las hipótesis siguientes se fijan juntas antes de crear fuentes o sesiones. R4 se conserva íntegra. 2026 CERRADO incluso a inspección. Ventana2020-10-15→2025-12-31EXCLUSIVA(últimodía2025-12-30). Muestra intensamente reutilizada de desarrollo, no OOS ni prueba anti-sobreajuste.

## Presupuesto y controles
10recetas×B/C=20backtestsnominales. Cada uno de dos nuevos agentes dispara2simultáneos por ticketroot;máximo4global y2análisis. Ninguna receta nueva tras mirar resultados, sin combinaciones de ganadores ni umbrales de rescate. Conservartodosincluidosceros/sinoperaciones/bajamuestra. Un máximo de6fulls de verificación paraUNcandidatoelegible tras terminar20:2fees+.00025/lado y4vecinos de target .9/1.1. Si ninguno elegible, detener20. Reparaciones exclusivamente técnicas se documentan y repiten porpareja; rawpreservadoapartado, no son ideasnuevas. Sinrestarts/imports preventivos/configglobal/live/paper/Pi/instalaciones/research_scripts/funding.

Contrato vigente:10000USDTshared,1%trade/8%agregado,isolated5x,nopyramid,cap4.4,reserva.001sólosizing. Fee nominal.00045/lado,todosordertypes. BTC/PAXG/SPY4h+3feeds1m enBinancePerpetualFutures,warmup240,debugtruefastfalsecharttrue. PAXGPortComparePaxgMarket4horiginalfeeBE(noadoptarBEfijoR3),SPYBPortCompareSpySecond4h,CPortCompareSpyMarket4h. OriginalesBTC long/STOP short,HP,prioridad,sizing,ledger/volatility/budget intactos. Noafirmarejecucionesoriginalesidénticas:ocupación/capitalcompartidopuededesplazar.

NuevasfuentesautocontenidasN204ExploreR501..505 yT403ExploreR501..505. N501..505añadenunsetupcompletoalN204; latchfalse→true delsetupMODIFICADO seactualizainclusoocupado/pending,sincolas. C501..505mantienenN204entry/latch deT403con excepciónlabelyAextraenC504sinmodificarcriterios. Sóloactúansobre suplementoMARKET, originalesintactos. E=fillreal,d=distanciaplaninicial,SL=E+d,TP=E-2d,deadline48hdesdefill. No parciales. Sólo4hcompletaspostfill,contiguas,clockcandleopen>=fill,close<=decision yprimerfull=ceil(fill/4h)*4h; idempotencia,resetporfill ydeadlineprimero. Antesdeladverso seprocesaprogresoC505; misma-baradverso no puede recuperar porcondicionescontrarias, comprobartiemposestrictos. N504UTCclockcalendario,ningunbarpartial/futura. OHLCVpresiónproxy,noobservedflow.

## Hipótesis exactas
```json
{
  "n204": [
    {
      "id": "N501",
      "strategy": "N204ExploreR501",
      "seed": "N204",
      "rule": "N204 fullsetup AND Bneg<Apos: W12 originalq; HLC3 VWAP B with volume ofq<0cohort; Aoriginalpositivecohort; emptynegfalse. Noqweight/Achange."
    },
    {
      "id": "N502",
      "strategy": "N204ExploreR502",
      "seed": "N204",
      "rule": "N204fullsetup AND median(TRlast6W)<median(TRfirst6W) AND TR_t>median(TRW). TR_i=max(H-L,abs(H-Cprev),abs(L-Cprev)),includesgap,priorcloseavailable14bars. Strict inequalities."
    },
    {
      "id": "N503",
      "strategy": "N204ExploreR503",
      "seed": "N204",
      "rule": "N204fullsetup AND0<ER<=1/3,ER=(C_s-C_s12)/sum12abs(closechanges throughs);denominator0false. NoERthresholdsweep."
    },
    {
      "id": "N504",
      "strategy": "N204ExploreR504",
      "seed": "N204",
      "rule": "N204fullsetup AND latest2completeUTC12h bars each3exactcontiguous4h, end=floor(decisionclose/12h)*12h: previousgreen Cp>Op,latestred Cl<Ol,Ol>=Cp,Cl<=Op. Currentpartial12hexcluded,daymidnightjustclosedincluded. Missing/duplicate/reorderfalse."
    },
    {
      "id": "N505",
      "strategy": "N204ExploreR505",
      "seed": "N204",
      "rule": "N204fullsetup AND atleast8of12Wcloses>=originalA. Acalculatedonceoriginalcohort. Fixed8/12nostepsweep."
    }
  ],
  "t403": [
    {
      "id": "C501",
      "strategy": "T403ExploreR501",
      "seed": "T403",
      "rule": "RetainN204entry/T403adverseactivationfirstcomplete4hclose>=E+.5d. Require2consecutivecomplete4hcloses<=E strictlyAFTERadversebeforeMARKETexit atsecond. Anyclose>Ereset0. SL1RTP2R48hunchanged,deadlinefirst."
    },
    {
      "id": "C502",
      "strategy": "T403ExploreR502",
      "seed": "T403",
      "rule": "Afterfirstadverse>=E+.5d, firststrictlylaterfull4hclose<=E freezes thatbarhigh recovery_high,doesnotexit. Onlystrictlylaterfull4hclose>recovery_highexitsMARKET; barrierfixeduntilclose,noSLmove. SL1RTP2R48hdeadlinefirst."
    },
    {
      "id": "C503",
      "strategy": "T403ExploreR503",
      "seed": "T403",
      "rule": "AfterT403adverseactivation,strictlylaterfull4hclose<=E exitsMARKETonlyifH>LandC>=(H+L)/2 ofthatbar. Recoveryclosedinlowerhalfmaintain/re-evaluatelaterbars. Noentryfilter/SLmove,deadlinefirst."
    },
    {
      "id": "C504",
      "strategy": "T403ExploreR504",
      "seed": "T403",
      "rule": "CaptureoriginaleventApositivecohortHLC3VWAPinplan/fill,fixedfortrade. AfterT403adverseactivation,strictlylaterfull4hclose<A exitsMARKET,replacesclose<=E(notAND). NoArecursion/recalculation/noentrysetupchange. SL1RTP2R48hdeadlinefirst."
    },
    {
      "id": "C505",
      "strategy": "T403ExploreR505",
      "seed": "T403",
      "rule": "Ifanycompletepostfill4hclose<=E-d BEFOREfirstadverseclose>=E+.5d,permanentlydisableT403rescueforthattrade. OtherwiseT403exact. ProgressobservedCnotintrabarL,adverse/progresscannotbothoccur,sweepnone. SL1RTP2R48hdeadlinefirst."
    }
  ]
}
```

## Evaluación congelada
AuditorreutilizafillsyMTMUTCcon4anclascongeladasR4; cantidades/fees/PNL/wallet/terminal/partialsexactos ypreciosanchorcheck.61meses/19Qcompletos,63/21incluidos,mesesactivosycalendarioexplícitos,positivos>0sinredondeo. Overlays+5/+10bpsRT sobrecadarealfillañaden.00025/.00050porlado,qty/precios/timestampsfijos; no reruns/slippagepuro. DDMotor ydayclose separados,cohortesnoMTMporaperturaseparadas. SupplementMARKETvsoriginalSTOP/long,ex1/ex3+10,exposición,notional×time,cohortesaño,capital/desplazamientoscomo diagnósticos.

Comparaciones: todascontraN204B/C nominal para elegibilidad;líneaCademáscontraT403B/C paraatribuircambio. ReferenciasN204Bbc5aaba6-2746-4e90-b0de-7b7955b66142,C6dead093-4663-4da9-ac62-c2ad9f9bb794;T403B9014f7d9-fa7e-4af7-94b7-dc98940f21b8,Cbd5f78dd-b730-48ad-ab01-e4c3f4726d29. TodasyaresumidasMCPfinished/errornull antescongelar.

ElegibilidadTODOSenB/C:nominalnet>N204;+5Mpositivos/activos>=.65 yQpositivos>=.80,encompletoseincluidos;+10net>=N204mismocoste;DDmotor>=-25%. BatirT403noalcanza. Rankingfijo:mayormínmargenM65/Q80sobreambosbins/B/C;mayormínΔnet+10;menorpeorDD;IDlex. Noelegible=>ceroverificaciones. Unaúnicarecetaelegible(tras20auditados) seconfirmafee.00070/ladoB/C mismasfuentescontraN204feealtoB9a6c7c24-8847-42d1-aadb-206f21723c1f/C541d2bf4-ffca-4f2d-969b-c25165e7b960. Exigirdelta>0M65Q80ambosbinsambascarteras,DD>=-25. Si falla,noseescogealternativa. Dosvecinosdevalidaciónnoelegiblesparaescoger:TPsuplementario1.8R/2.2R(.9/1.1×2R),SL/restointactos,cadaB/Cnominal4fulls. Reportarmatrizsin elegirmejorvecino.

QA antesfulls:fuentesmétodosprotegidos/dedupR4,rangos/finito/igualdad/clock full,latch/occupied/pending/reset,idempotencia,indicadoresnuevossólodocumentados(nohanpropuestonuevos),casosnoobservablesfalse. NopegararraysderesultadosenPython,nofuturosniM1preconstruidosparapostfill. Inventarios/objetivohipótesisno justificanpromoción. Root revisa las10fuentes y lasbases antes de lanzar,cadafuente3snapshots/formsexactos. Criteriosnoadaptadosdespués. ReportesMCPobligatoriosporfamilia,matriz20,registro,diagnósticos yrevisiónindependienteantesfinal.


Precisión numérica previa a resultados: los porcentajes de meses/Q siguen >0 sin redondear; no se fuerza cero. Para incremento de neto, diferencias absolutas <=1e-7USDT se etiquetan identidad numérica y no mejora, tanto nominal como en confirmación fee. Conservar delta bruto; nominal elegible requiere delta>1e-7. Comparación no-inferior de +10 admite tolerancia contable1e-7. Es una tolerancia de conciliación de floats, no un umbral elegido por resultados. Fuente/riesgo no cambian.
