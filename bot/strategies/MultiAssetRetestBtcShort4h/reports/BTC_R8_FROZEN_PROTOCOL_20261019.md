# BTC — protocolo congelado R8

## Objetivo y presupuesto

Investigar selección de entradas/contexto original tras R7, sin seguir afinando defensas de salida. Dos investigadores: rootfamiliaV801..805,subagenteexperimentalX801..805.20backtestsnominales=10recetasB/C;2simultáneosporinvestigador,max4global;2análisismaxglobal. Cada investigador empieza con suprimerpar y pide ticketparaelsiguiente. Protocoloantesfuentes/drafts/resultados. Ceroañadidosposthoc.

N204=X03ExploreR204referenciaultimate. N503=N204ExploreR503yP604=N503CapacityR604candidatasnopromovidas. R7defensasgeneralesdeganancia fallaronentreambas semillas;S701replicóP604yS704P603. O700instrumentaciónparidadexactaN503264/271trades,375R/82eventos/11ocupados/67fills,registrodisponible. Noevidencianuevaalrepetiridénticatrayectoria.

## Familia de contexto

### V801 — BtcContextR801

Consumir eventoN204 original; veto si ERnoOK, conERexactoN5030<ER<=1/3. Control del latch: ERse aplica postevento, noalsetup/latchcomoN503.

### V802 — BtcContextR802

Consumir eventoN204; veto si Gactual=True. Transferencia explícita P601desdeN503aN204, no nuevoindicador.

### V803 — BtcContextR803

Consumir eventoN204; veto si ERnoOK ANDGactual. Recortar trayectorias directas sólo encontexto original.

### V804 — BtcContextR804

Consumir eventoN204; veto si ERnoOK ORGactual. Unióncontrolada para compararcon ERsolo/Gsolo/intersección.

### V805 — BtcContextR805

Consumir eventoN204; veto si ERnoOK ANDalgunoR(cFull[:-1]),R(cFull[:-2]),R(cFull[:-3])True. ExcluyecurrentR; recomputaciónprefijosdelbufferactual,noestadohistóricobuffer. Transferencia condicionada del R6P602queeraidénticoN503; no afirmar mecanismo inédito.

N204setup/latchfalse→trueoriginalintacto,geometría1..3ATRoriginal,rawsourceevent+occupiedcontadosANTESveto. Veto consume evento yborra explore_event,sinretry/cola mientrasN204setupTrue. R/GpuroR6:>=140velas4hcontiguascerradas,EMA120[-1]>[-10],C>EMA120−ATR,RSI3<=20paraR,sinRSIparaG;entrye=min(L,C−.25ATR),distance=EMA20−e entre1..3ATR y>=6fee*e. No llamar métodosdeorden ni mutarplan/ledger/capacidad. Vcontexto usa cFull=_explore_window(143),invalid=>veto+contadorinvalid,noinferirpreparación. V801sóloERusa14original. ContadoresER/G/recienteR/veto/aceptado: observacionales,no órdeneshipotéticas. Prefijoshistóricosesbufferactual,notracehistóricodeindicadores.

## Familia experimental

### X801 — BTCExploreR801

Reemplazar setup suplemento: W12previasthroughs;k=maxV,empatemásreciente;kverde,A=HLC3k;Cs>Cprev12,Cs>=A,troja,Ct<A. Costeproxydeeventodominante,no q/VWAPcohorte niER.

### X802 — BTCExploreR802

W6previasthroughs;L*=maxL,H*=minH;L*<H*,CsentreL*yH*inclusive,troja,Ct<L*. Salidabajistadezonacomúnnegociadaentodaslas6velas; noinsidebarindividual.

### X803 — BTCExploreR803

W12previas;k=min(C-O),empatemásreciente;kroja,knoúltima;M=(Ok+Ck)/2;desde k+1hastas almenosunC>=M yningunoC>Ok,Cs>=M;troja,Ct<M. Impulso→recuperaciónincompleta→pérdidademitad. Cs>=M implica existencia,condiciónredundante explícita.

### X804 — BTCExploreR804

W12previas,ri=Ci-Cprevio;sumVi*ri primeras6>0 yúltimas6<0;Cs>Cprev12;troja,Ct<min(Cs,Os). Transiciónvolumen-retornoentre cierres,no qdelocalización niER.

### X805 — BTCExploreR805

Cs>Cprev12,troja;exact240M1cerradas/contiguasdet4h,OHLCVválido,V>=0,totalV>0,últimoC1m=Ct. Cortartrasprimerminuto cuyoVcum>=.5Vtotal,enterocompletamentealprimergrupo;segundo=resto;ambosnovacíos yV>0. VWAPHLC3×Vcadauno,A2<A1,Ct<minLprimergrupo. FraccióndeVrealprimergrupo sólo diagnóstico;sinfraccionarcompartirOHLC,inventar intraminutofillsni afirmar mitadesexactas.

Sólosetupdel suplemento se reemplaza; latchfalse→trueavanzaocupado/pending,señalcompletacomovariantesprevias,sincola. Riesgo/d/orden/SL1R/TP2R/48h/priorityoriginal. d=max(Hs,Ht)+.25ATRt−Ctcongate1..3ATRinmutable. Todos usanventana14parad/gate; W6oW12segúnreceta. Datosprecios/volumenrealesOHLCVcerrados; q/HLC3×Vsonproxies,no flujotakerobservado. X805coberturaM1exacta240desde t.open a t.open+4h−1m,cierres<=decisión,shape2D6cols,OHLCfinitepositivo,L<=min(O,C)<=max(O,C)<=H,V>=0;últimoC=Ct exacto. Missing/corrupt/clock/mismatchfalseconcontadoresdistintos. Sinfeedsnuevos,interpolación niinferirordenintraminuto.

## Contrato fijo

2020-10-15→2025-12-31EXCLUSIVA,últimoprecio2025-12-30.2026CERRADO inclusoinspección; muestra de desarrollo reusada,noOOSni pruebaantisobreajuste.10000USDTshared,1%trade/8%agregado,isolated5x,nopyramid,cap4.4,reserva.001sizing;fee.00045porlado;warmup240,debugtrue,fastfalse,charttrue. RutasBTC/PAXG/SPY4h+3feeds1m. PAXGMarketBEfeeoriginal. SPYBSecondsegundaexacta/precioestructural;SPYCMarketdesde2/preciomercado. B/C no son muestrasindependientes. No cambiarHP,ledger,sizing,STOPshortolargooriginal,jerarquía,feeglobal,dataseries,live/paper/Pi ni funding.

## Auditoría y gates antes de resultados

Fills/qty/fees/PNL/wallet/terminal/MTMUTCdiario4anclashistóricas. CohortessuplementoMARKET/STOP/largo/otrasrutas,desplazamientoycapitalendógenos,no causalidadaislada. Overlays+5/+10bpsRTadicionales sobre fills/cantidades/precios/tiemposfijos,no mayorfeeengine ni slippagepuro. Mesesfull61/all63,Q19/21,activosycalendariomostrados,positivos>0sinredondeo.

TODOSambasB/C paraelegir:ΔnetN204>1e-7;+5Mactivos>=65%yQ>=80%full/included;+10net>=N204−1e-7;DDmotor>=−25%. Diversidadprefijada adaptada a entradas:suplemento>=30fills y>=10entradasdel suplementoañadidas+retiradasrespectoN204porclavesymbol/side/entrytype/open. Umbralesoperativos,no confianzaestadística. EnV mideeventosfiltrados;Xpuedesustituirsetup. AdemásΔMTMN204>1e-7enalmenos3de5bloquesanuales2021..2025,2025PARCIAL;ΔnetN204trasdescontar mejormesincremental>1e-7. Omitir sóloaritmético,no reejecucióncapitalni OOS. Parámetrosnocambianporresultados. Ranking mayor mínmargenM/Q,mayorminΔ+10,menorpeorDD,IDlex.

Unaúnica elegible despuésde20 activa6fullsadicionales:2feeengine.00070/ladoB/C vsN204altofeeB9a6c7c24-8847-42d1-aadb-206f21723c1f/C541d2bf4-ffca-4f2d-969b-c25165e7b960;exigirΔnetpositivo,M65/Q80full/allambas,DD25.4vecinosnominalesTP1.8R/2.2RcadaB/Csinmoverd/SL/48hresto. No elegirsegundasi falla,ni vecino ganador. Ningunaelegible=>ceroextras;máximototal26.

## QA, archivos y mantenimiento

Antesdelprimerparporfamilia:fuentesexactas/protectedmethods/ramasoriginales,fixturesfronteras/empates/ventanas/contexto/clocks/missing/ER,latchvsfiltropostevento,comentariosconstantesyrenovaciónstate. RevisióncruzadadespuésdeQAantesdeusardatoscomoavance. Testssintéticosdehelpersno pruebanlifecycle/financiero. Todoslos20formularios/60snapshots yfuentesfinalesleídos;auditoríasJSON/reportes/URLs yselecciónarchivados. Protocoloesperadorevisiónantesdeejecución;nodejarfuentesenestado ambiguo.

Jesserespondenormalmente;0backtestsactivosalinicio. No limpieza sin señal de necesidad. Noretirarfuentes/sesiones/reportesanteriores; sihacefaltaarchivarconservarcódigoexacto,dependencias,hipótesis,resultados,URLs,motivodescarteymanifiestorecuperaciónantes. ErrorPNGartifact_changedprevionoseatiendeborrandoestrategias;no repetirlecturasdeimagenconocidamentefallidas ni usarworkarounds externos.
