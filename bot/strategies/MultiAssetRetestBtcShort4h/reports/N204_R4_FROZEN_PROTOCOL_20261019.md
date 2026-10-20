# N204 R4 — protocolo exploratorio congelado
Fecha2026-10-19. Usuario autoriza tres agentes (entradas,salidas,experimental). N204 congelada permanece referencia, toda variante nueva separada.2026 cerrado incluso a inspección. Reglas siguientes fijadas ANTES de resultados de diagnóstico y backtests de esta ronda.

## Hipótesis y presupuesto
E: calidad de entradas en contexto/estructura/participación.
T: gestión condicionada al recorrido, sin repetir salidasR2.
X: reemplazos experimentales independientes del generador suplementario, preservando infraestructura de cartera. Su parentesco OHLCV no da evidencia independiente.
Doce variantes (4porfamilia) porB/C=24fulls. Diagnóstico observacional sin cambios económicos porB/C=2fulls antes de evaluar salidas. Sólo si elegible, un candidato recibe2fulls al fee.00070 y4fulls de sensibilidad de targets: totalmáximo32; sin elegible total26. No otrasrecetas, combinaciones ni rescates. FuenteQA yreviewroot antesdetickets; guardarIDsantesrun. Cada ticketroot permite un parB/C simultáneo, máximo4backtests/2analysis globales; noautorización para lanzar otros pares.

## Contrato
2020-10-15→2025-12-31EXCLUSIVO,últimodía2025-12-30. Desarrollo reutilizado,no nuevoOOS.10000USDTshared,riesgo1%portrade/8%agregado,isolated5x,cap4.4,reserve.001sizingonly. Fee.00045porlado todos los tipos, excepto2runs explícitas.00070. Rutas BTC/PAXG/SPY4h y3feeds1m eneseorden,warmup240,debugtrue,fastfalse,charttrue. BPortCompareSpySecond4h,CSpyMarket4h. PAXGPortComparePaxgMarket4h originalfee-dependentBE,NOfixedBE. Sinpyramiding,instalaciones,reinicios,configglobal,nuevosdatos,live/paper,funding,RST/MC,research_scripts. Estrategias/datos/reportes sóloMCP.

BTCoriginal long yshort prioritarios,códigos/HP/sizing/ledger/helpers intactos. VariantesEañadenun gate alsetupcompletoN204; latch false→true completoavanza tambiénocupado/pending, sincolas. VariantesX reemplazan sólo generador deeventos, misma semántica false→trueyprioridad. N204geometry común: s=t-1,d=max(Hs,Ht)+.25ATR14_t−Ct, requireATR<=d<=3ATR, MARKETclose,TP2d,48hdesdeactualfill,protecciónrelativaactualfill. Validarventana4hcerradacontigua/finita/positiva yATR sobrehistoriacausal. Min14bars,salvoX40215,E401suficientesparadosdíasenteros. VariantesT mantienen entry/latchexactos; gestión sólo suplementos yfullpostfillbars(open>=filltime,barclose<=decision),nodefillbarnihighprefill. Deadlineprimero. Nadaoptimizadoapartirdeexcursiones.

## Recetas exactas
```json
{
  "entry": [
    {
      "id": "E401",
      "strategy": "N204EntryR401",
      "rule": "Add gate to complete N204 setup: latest two contiguous complete UTC days (six contiguous4h bars each; dayend<=decisionclose) must have closeD<closeDprev. Missing exact days false. Current midnight may use day justclosed. No partial day."
    },
    {
      "id": "E402",
      "strategy": "N204EntryR402",
      "rule": "W12 prior bars throughs: sumq(first6)<0 AND sumq(last6)<0, originalq formula, originalN204otherconditions. Full modifiedsetup latch."
    },
    {
      "id": "E403",
      "strategy": "N204EntryR403",
      "rule": "min(low last6ofW)<min(low first6ofW); originalsetup unchanged otherwise; not C_t<low_s. Full modifiedsetup latch."
    },
    {
      "id": "E404",
      "strategy": "N204EntryR404",
      "rule": "sumV over q<0 W12 >sumV overq>0; qzero excluded; qformula andcohortVWAPunchanged. Full modifiedsetup latch."
    }
  ],
  "exit": [
    {
      "id": "T401",
      "strategy": "N204ExitR401",
      "rule": "Onlysupplement: deadlinefirst;>=3completepostfill4h bars; latest3L strictlyincreasing andlatestC>previousH thenMARKETclose. SL/TP2R/48 unchanged."
    },
    {
      "id": "T402",
      "strategy": "N204ExitR402",
      "rule": "Onlysupplement: exactly sixth completecontiguouspostfill4h bar, if min(first6C)>=fillE thenMARKETclose. IfanyC<E neverexitvia rule. Missingclock no delayedcheck. SL/2R/48otherwise."
    },
    {
      "id": "T403",
      "strategy": "N204ExitR403",
      "rule": "Onlysupplement: firstcompletepostfill4h close>=E+.5d latchesadverse; fromnextfullbar close<=E exitsMARKET. NotnetBE. NoSL/TP/48change."
    },
    {
      "id": "T404",
      "strategy": "N204ExitR404",
      "rule": "OnlysupplementTPsplit: q1=floor((q/2)/.001)*.001 atE-d,q2=q-q1 atE-2d; ifq1zero retainall2R. StoppriceE+d remains,stopqty matchesremaining afterreduction,48hfrominitialfill. NoBE/trailing/newentrygate."
    }
  ],
  "experimental": [
    {
      "id": "X401",
      "strategy": "N204ExperimentalR401",
      "rule": "Replace supplementsetup. rj=t-j: highpivotr5 H5>H6,H5>=H4; lowpivotr3 L3<L4,L3<=L2; highpivotr1 H1>H2,H1>=H0; H1<H5; C1>=L3 andC0<L3. Pivotsconfirmedwithavailableclosedbars, nofuture."
    },
    {
      "id": "X402",
      "strategy": "N204ExperimentalR402",
      "rule": "Replace supplementsetup. W=c[-15:-3]12bars, a=c[-3],b=c[-2],t=c[-1]; U=maxH_W,L=minL_W. C_a>U,C_b>U,L<=C_t<U,C_t<O_t. Frozenrangeforthissetup, nohistorysearch/retestqueue."
    },
    {
      "id": "X403",
      "strategy": "N204ExperimentalR403",
      "rule": "Replace supplementsetup. Motherc[-4],I1[-3],I2[-2],t[-1]. BothinsideH<=Hm,L>=Lm, atleast1strictinequalitypereachinside;motherH>L. C_t<Lm. Eventonlyclosedt."
    },
    {
      "id": "X404",
      "strategy": "N204ExperimentalR404",
      "rule": "Replace supplementsetup. a[-4],b[-3],s[-2],t[-1]; C_b>O_b andL_s>H_a, thenC_t<H_a andC_t<O_t. Immediateinvalidationonly,nosearchforpastgaps. OHLCVproxy,noorderflowclaim."
    }
  ]
}
```

## Diagnóstico N204PathDiagnosticR400
CopiaautocontenidaN204 coninstrumentaciónnodeterminante: mismoentry/exit/SL/TP/sizing. CapturaE,q,d,opened_atdocumentado. beforecada4hrecolectaM1cerradaspostfill(open>=entrytime,open+1m<=time);onclose descarta todaminutaconclose>=exittime yrecolectagaprestante. No tomarOHLC4hpreconstruido. VerificargridM1esperado,duplicados/gaps/finito;coveragefalseexplícito,nointerpolar. MFE/MAE deM1completas sonlowerboundsobservados, excluyenminutosparcialesentry/exit, no identificanordenintraminuto. None si sinfullM1. Progreso6/12/24h sólo cierreM1exactamenteenfilltime+h y<exit; Noneconrazónsinoobservable. NoatributosClosedTradeinventados;PnL/fees seunenporentrykeyconlosresultadosreales. Bufferactivo yresumen79registros,mismosperdedoresyganadores,sinsampling;logsdiagnósticosenpartes<=35KBconmanifesttotal/partcount,notruncar. Paridadfills/qty/prices/timing/fees/PNLabs<=1e-7 conreferenciasN204B/C antesdeinterpretar; B/Cnoobservacionesindependientes. NohipótesisseedadaalverMFE. Si log/APIdefectuoso,reparar sóloinstrumentación,no reglas deoperativa.

## Auditoría económica y criterios
Todaslas24runs, incluidosceros/fallos/bajamuestra, secomparanconN204originalnominalBbc5aaba6-2746-4e90-b0de-7b7955b66142,C6dead093-4663-4da9-ac62-c2ad9f9bb794. Auditorfills/qty/fees/PNL/wallet/terminal,MTMUTCdiario con4anclascongeladas,61meses/19Qcompletos y63/21incluidos;positivos>0sinredondear,activosytodos. DDmotor ydayclose separados. Overlays+5/+10bpsRT aumentanfee porfill .00025/.00050;precios/qty/timestamps fijos,noreregla gestión, ni slippagepuro. Comisiónmotor.00070 síreejecutasizing/gestión yPAXGBE; etiquetaraparte. SupplementMARKETvsoriginalSTOP/long,desplazamientos/exposición/notional×time,ex1/ex3+10ycohortesaño como diagnósticos, no OOS ni causalalpha.

Elegibilidad para ÚNICA verificación:
- Neto nominal>referenciaN204 ambosB/C.
- Mesespositivos/activos>=65%yQpositivos>=80% aoverlay+5,tanto completoscomoincluidos,ambosB/C.
- Neto aoverlay+10>=N204mismocoste ambosB/C.
- DDmotor nominal>=−25%.
Ranking fijo: mayor mínimo margenM65/Q80en4contextos; luego mayor mínimoΔneto+10; luego menorpeorDD; luegoIDlexicográfico E/T/X. NoelegirporCAGRsolo.Noelegible=>no runsadicionales.

Candidatoúnicoalfee.00070B/Cmismafuente: contrastarN204feealtoB9a6c7c24-8847-42d1-aadb-206f21723c1f,C541d2bf4-ffca-4f2d-969b-c25165e7b960. Para confirmarobjetivo: Δneto>0ambos,M65/Q80completoseincluidosambos,DD>=−25%. Nocandidatoalternativosi falla.
Dosvecinosdevalidaciónnocandidatos: multiplicartodoslostargetssuplementariospor.9 y1.1,respectivamente; incluyeambosTPdeT404 proporcionalmente,SL yrestofijos. CadaunoporB/C=4runsnominales. Seexponelamatrizsinseleccionarelmejorvecino,incrementonetosuplementarioperfamilyyregularidad; nocriterioretrospectivonuevoparaaprobar.Nooptimizaciones,bootstrapselectivo,nuevoranking devecinos.

Entregables: protocolo,13fuentesnuevas(12+diag)ysourceQA,26–32URLs,diagnósticocobertura/excursionesyparidad,matriz24runs+costes,selección/verificaciónsiaplica,revisiónindependiente,resultadosyhandoff. N204referenciaintactay2026cerrado.
