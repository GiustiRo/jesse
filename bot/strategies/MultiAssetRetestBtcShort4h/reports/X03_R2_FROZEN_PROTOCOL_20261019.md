# X03 R2 — protocolo congelado — 2026-10-19

El usuario autoriza validación de X03, regularidad bajo costes y al menos diez variantes nuevas, con 2026 cerrado. Tres agentes nuevos: x03_validate_r2, x03_cost_r2 y x03_explore10_r2. Esta matriz se congela antes de código y resultados nuevos. No se elige el mejor vecino para promoverlo.

## Alcance económico

Siete pruebas de validación (seis vecinos de un factor y retraso fuerte), cuatro mecanismos de costes y diez variantes de operativa:21fuentes, cada una enB/C=42full backtests. Dos controles adicionales X03B/C con comisión motor .00070 por lado (+5bpsRT frente .00045) verifican efectos endógenos de coste. Si una variante económica cumple elegibilidad predeclarada, se permite un único par adicional con .00070 por lado, misma fuente congelada: máximo48fulls incluyendo los controles de atribución descritos abajo. Si ninguna califica, máximo46. No nuevas recetas, combinación de ganadores o tercera ronda automática.

Cada ticket root permite solamente un parB/C simultáneo; máximo global4backtests,2analysis. GuardarIDs antes de run y reconciliar cualquier respuesta desconocida antes de reintentar. Fuentes/drafts mediante JesseMCP, informes consave_strategy_report. Root lee fuentes y verifica snapshots3rutas/form antes deejecución. No producción/live/paper/Pi,restart,instalaciones,funding,nuevosdatos,research_scripts ni cambio config global.

## Contrato común

2020-10-15→2025-12-31EXCLUSIVO, último día2025-12-30;2026 ni inspección. Dataset2020–2025 intensamente reutilizado de desarrollo, no nuevoOOS. Cuenta10000USDTshared, riesgo1%trade/8%agregado,isolated5x,cap4.4,reserve.001sizingonly;comisión.00045lado todos tipos excepto par stress motor explícito .00070. Nopyramiding. Ledger/helper/volshare4h intactos, longrunners y shortoriginal preservados, salvo nuevas reglas explícitas suplemento. PAXGPortComparePaxgMarket4h;SPYSecondB/SPYMarketC. RutasBTC/PAXG/SPY4h y3M1data,warmup240,debugtrue,fastfalse,charttrue. OriginalX03 intacto.

Referencias sin repetir: X03B53937852-34a3-48c7-ab35-fac586341127;X03C3935efb3-2b27-4ada-86ce-94123d7a6e2c. SinX03 B29387384-c48c-4ac9-94bd-632a2ec3bb7f;C30ab3788-51bb-4435-8c21-9b12c45f8835. Riesgo3%histórico no comparable.

## Recetas exactas

```json
{
  "validation": [
    {
      "id": "V201",
      "change": "Horizon8 replaces12 jointly in return comparison, q-window and HLC3 VWAP; min10closedbars, sourceATR unchanged."
    },
    {
      "id": "V202",
      "change": "Horizon16 replaces12 jointly; min18closedbars."
    },
    {
      "id": "V203",
      "change": "TP1.5R instead2R, other rules unchanged."
    },
    {
      "id": "V204",
      "change": "TP2.5R instead2R."
    },
    {
      "id": "V205",
      "change": "Supplement timeout24h instead48h."
    },
    {
      "id": "V206",
      "change": "Supplement timeout72h instead48h."
    },
    {
      "id": "V207",
      "change": "Strong timing stress: consume source setup t once, schedule exactly next4h close; original plans priority, expire if occupied/pending/overridden/missingclock, no queue. No revalidation; freeze original distance/TP geometry at signal, place MARKET at due close with current budget and original helpers; protection relative actualfill;48h fromfill. New original events update state independently."
    }
  ],
  "cost": [
    {
      "id": "K201",
      "change": "After original false-to-true latch and1..3ATRgeometry, require ATR_t>=4*(2*.00095*C_t). MARKET/stop/2R/48 unchanged. Latch tracks base setup even gate rejects. .00095 is fee proxy including+10bpsRT, not actualmotorfee."
    },
    {
      "id": "K202",
      "change": "Source event unchanged; SELL LIMIT at frozenVWAP_s>close_t, lifetime next4hbar only. Absolute S=max(H_s,H_t)+.25ATR_t, d=S-VWAP, require1..3ATR_t, TP2d,48h fromfill; sameoriginalspriority/ledger, sizingusesplannedVWAPentry, protectionrelativeactualfill. Samefeealltypes, no discount."
    },
    {
      "id": "K203",
      "change": "Source event t consumed; exactly nextbar u=t+4h confirmation requires C_u<originVWAP and ATR_t<=S-C_u<=3ATR_t, S=max(H_s,H_t)+.25ATR_t frozen. MARKETdistanceS-C_u,TP2d,48h fromfill. Expireifmissingclock/occupied/pending/originalpriority; neverqueue. DistinctV207 no revalidation and frozen distance vs this persistent anchor/geometry test."
    },
    {
      "id": "K204",
      "change": "Source signal/marketstopdistance/size/48h unchanged. Cost-aware net2R TP withproxy c=.00095: S=E+d; L=d+c*(E+S); T=(E*(1-c)-2*L)/(1+c). Validate TpositiveandbelowE beforeorder usingplannedentry; calculatefrozenTPfromactualfill E. No targetupdates."
    }
  ],
  "explore": [
    {
      "id": "N201",
      "change": "Replace q only with V*(C-O)/(H-L),zero span0. Same12bar window, originalVWAP andreturn condition."
    },
    {
      "id": "N202",
      "change": "Replace q only with V*(C-Cprev)/TR,TR=max(H-L,abs(H-Cprev),abs(L-Cprev));zeroTR0. Twelvebars, restsame."
    },
    {
      "id": "N203",
      "change": "Replace onlyVWAP A: latest maximum-volume bar in12barW asanchor, HLC3volumeVWAP fromanchor throughs. Bothpricecrosschecks useA, frozenforconfirmation."
    },
    {
      "id": "N204",
      "change": "Replace onlyA: HLC3volumeVWAP ofWbars whereoriginalq>0; ifnone setupfalse. Otherqsum andreturn unchanged."
    },
    {
      "id": "N205",
      "change": "Add C_t<L_s tocompleteoriginalsetup; latchtracksfullmodifiedsetup."
    },
    {
      "id": "N206",
      "change": "Add upperwick_t=H_t-max(O_t,C_t)>=abs(C_t-O_t) tocompleteoriginalsetup."
    },
    {
      "id": "N207",
      "change": "Add V_t>median(V of12barW) tocompleteoriginalsetup."
    },
    {
      "id": "N208",
      "change": "Originalentries;storefrozenA. Supplementonly: first fullpostfill4hclose C>=A liquidateMARKET. Originalstop/2R/48h;deadlinepriority."
    },
    {
      "id": "N209",
      "change": "Originalentries. Supplementonly: after6fullpostfillbars open>=fill, sumoriginalq oflatest6; if>=0 closeMARKET. Stop/2R/48h."
    },
    {
      "id": "N210",
      "change": "Originalentries. After>=2fullpostfillbars, latchwhenclose<=fill-initialD(1R). Then eachclosedbarstopcandidate=max(highs latest2fullpostfillbars)+.25ATR_current, updateonly price<candidate<currentstop. TP2R/48h unchanged."
    }
  ]
}
```

Nuevos setups N201..207 avanzan false→true sobre su setup completo. K201 gate posterior nunca rearma setup original rechazado. Estados avanzan con ruta ocupada/pending, sin colas retrospectivas. V207 yK203 vencen exactamente unabarra; currentoriginalplanspriority. GestiónN208..210 sólo barras completas postfill(open>=filltime), nunca highs/closes parcialmente anteriores. ATR14 existente, OHLCV manual explícito y causal; cero rango definido enq. No indicadores inventados.

## Criterios congelados

Principal: meses positivos/activos>=65%, Qpositivos>=80%, tanto bins completos como incluyendo parciales, bajo +5bpsRT; mostrar también todos los meses calendario, base y+10. DDmotor ydayclose separados, tolerancia máxima−25%. Beneficio útil a costes y valor incremental frente X03 en ambas carteras; aspiración70%meses/20–30%CAGR no nuevo gate ni motivo para forzar búsqueda.

Las14variantes económicas K201..204,N201..210 se comparan con X03 ysinX03; los7vecinos V quedan fuera de selección. Elegibilidad para par de verificación de coste motor: ambosB/C pasan objetivo completo+parcial conoverlay+5, incrementonetocon+10>=0 frenteX03ambos,DDnominaldentro25%. Ranking fijo: mayor mínimo margen sobre65%meses/80%Q a+5 enambascarteras/ambosbins; empate por mayor mínimo incremento neto+10 B/C; luego menor máximoDD; luego IDlexicográfico. Sólo1candidato ypar de estrés, no segunda elección si falla. Aun pasándolo sería validación de desarrollo condicionada por selección, no OOS.

Vecinos: matriz completa y fracción que mantienen beneficio suplementario/incrementalpor familia, sin seleccionar pico ni nuevo umbral de aceptación trasresultados. Retraso4h es estrés fuerte de timing, no modelo de latencia de minutos. Ninguna garantía de no sobreajuste dentro muestra reutilizada.

## Auditoría y análisis

Root reutiliza auditor validado de fills/qty/fees/PNL/wallet/terminal yMTMUTCdiario con4anchors de precios y hasta6targets porjob(max10inputs). Costes estáticos+5/+10RT porfill a mitadlado mantienen qty/precios/timestamps, sinresizing; stressmotor.00070 sí reejecuta gestión/sizing y se etiqueta aparte. Full61meses/19Q, parciales63/21, activosytodos, >0 sin redondeo de aprobación. Guardar fallos/ceros ytodoslosintentos.

Porfuente: suplementovsoriginalBTC, desplazamientos, notional×time/ocupación, fechasfillsretainedlong,fees,PF/Sharpe/CAGR/DD,ex1/ex3suplemento ycartera con+10,cohortesaño distintosMTM, concentración2022+2025,co-loss e incrementootraspatasendógeno.

ValidaciónA: fuente causal+vecinos; bootstrap pareado de incrementosmensualesX03−sinX03,61mesesfullprincipal; bloquescirculares3mesesprimario/6sensibilidad,10000réplicas seed20261019, mismosíndicesB/C/costes sinagruparB/C. Intervalos2.5/50/97.5yfracción>0condicionadosamuestra; no pvalue confirmatorio/probabilidadnooverfit ni DDsimulado. Leave-one-year-out aritmético noOOS. No MonteCarlo candlemultiasset sin garantías de correlación/semillas documentadas; no tradesMC niRST. El remuestreo no elimina selecciónmúltiple ni crea datos no vistos.

## Entregables

Rootregistro46–48sesiones con URLs verificadas, protocolo ysourceQA, auditorías MTM/costes+enginefee, matriz42variantesB/C completa, informe de estabilidad/selecciónmúltiple yhandoff. Cadaagentereporta fuentesyQA, no duplica MTMroot. ReportesguardadosenproyectoJesse. No tocar2026.

## Addendum de controles de atribución — antes de seleccionar candidato
Fee5engine terminó con cambios de salida PAXG: fuente congelada usa stopBE=entry*(1+2.5*fee_rate). En la posición2025-01-03(entry2661), elevarfee.00045→.00070 cambiaBE2663.993625→2665.65675 y la salida ejecutada pasa deFebrero runner aEneroBE, conreentrada posterior. No es costeestático ni evidencia de fallo exclusivo deBTC. ParaaislarincrementoX03 se añaden SOLAMENTE dos controles sinX03 B/C PortCompareBtc4h a.00070 porlado, mismoPAXG/SPY/riesgo/ventana. No nuevasrecetas ni ajuste deparámetros; elegibilidad/rankingcandidato inalterados. Presupuesto total42+2X03Fee5+2sinX03Fee5+[0o2candidatoFee5]=46–48fulls. Todos son desarrollo reutilizado.
