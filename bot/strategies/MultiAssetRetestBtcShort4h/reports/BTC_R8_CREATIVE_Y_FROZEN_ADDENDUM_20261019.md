# BTC R8 — ampliación creativa Y solicitada por usuario

## Alcance y momento

El usuario pidió un subagente creativo adicional después de iniciada R8. Se fijan3hipótesisANTESdecrearfuentes/drafts/corridasY;elagentenoharecibidométricasnuevasV/X. Las20nominalesV/X siguenexactamentecongeladas. Ampliación6nominalesY=3recetasB/C;total26nominales,nomás. Elecciónúnicaglobaldespuésde26;puedeactivar6verificacionesprefijadas(feeengine2yTPvecinos4),max32total. Sinsegundaselecciónsi falla ni añadidosposthoc.

### Y901 — BTCNovelR901

Mismo eventoN503; SELL LIMIT candidatoA congelado conA>Ct, doriginaldelCtcongelado, sizingoriginalconentry=A yguardentry>2d. Pendienteúnicamentesiguientebarra4h, should_cancel_entryoriginal, sinreintento. SLfill+d/TPfill−2d,48hdesdeactualfill.

### Y902 — BTCNovelR902

MismoeventoN503; SELL STOP candidatoLt congelado sóloLt<Ct,igualdadrechaza,entry>2d. Sizingoriginalconentry=Lt,doriginalCt,pendientesólosiguientebarra4h,cancelaciónoriginal/sinretry;SL1RTP2R48hfill.

### Y903 — BTCNovelR903

EntradasN503idénticas; congelarAeventoenplan/varsfill. Deadline48hprioritario;sólo4hcompletaspostfillcontiguas,cuandocierre>A_frozen yqactual=V*(2C−H−L)/(H−L)>0(span0=>q0) yC>actualentry, cerrarMARKET. Invalidezadversa,no protecciónbeneficio;SLTPoriginales.

## Invariantes y ejecución real

N503seed,N204referenceultimate,P604contextocomparación. CódigooriginalBTC largo/STOPshort,HP,ledger,sizingfórmula/caps/prioridadsinmodificar. Y901/902sólopreciodeentradaen_explore_size para suplementos másmetadatosdeanchor/candidate. El presupuesto,feesunitrisk,reserve,volatilityquota ymargin se calculan alpreciocandidato;sin riesgoextra ni qtyfija. dsignalCt sigue1..3ATR,fijoalcrearorder; desplazarlafillmueveSL/TPalrededordelfillporlógicaexistente, nóvelaestructura originaldistinta. entry>2d esguardfísicodeTPpositivo,nodeunaoptimización.

Motor smartordereligeLIMIT/STOP/MARKET porrelaciónpreciocurrente;equal/nearpuedeaproximaraMARKET. No forzartipo ni afirmar100%LIMIT/STOP;registrarrequestedentryyprecios/tiposobservados. PendienteocupaBTCycapitalreservado duranteuna4h;esaocupaciónforma parte delexperimento. _signaloriginalmantieneprioridadantesdecrearorden. should_cancel_entryoriginalexpiraalsiguientecierre;no cola deeventosocupados, no reintento, no forzar aperturaoriginal en callback; motor normal gestiona su ciclo. Deadline desde fillreal,noarmado. FillsM1reales,noproyeccióncontrafactualniiordenintraminutoinventado.

Y903usaAevento congelado,semánticasetup/latchN503exacta,entryMARKETsin cambios. Excluirvelaentradaparcial;relojsfullclosed/idempotencia/resetporfill;span0q0;48hprioritario. Sólorecortapérdidasporreadmisióndehipótesiscompradora,nosefija objetivo de pérdida monetaria ni umbraloptimizado.

## Auditoría, identificación y gates

Mismosdatos/contrato/fechasR8;2026cerradoinclusoinspección,ventana2020-10-15→2025-12-31exclusiva.10000shared1%trade/8%total,isolated5x,cap4.4,reserva.001sizing,fee.00045lado;PAXGoriginalBEfee,SPYBSecond/CMarket,4h+1mfeeds,warm240debugtruefastfalsecharttrue. Riesgo de seleccióndevelopmentmuestrareutilizadanocambia.

Corefinanciero porrun_analysisdeinputscompletos: fills/qty/fees/PNL/wallet/terminal/MTMUTC4anclas,overlays5/10RTsobre fillsfijos. Snapshottradesincluyeórdenesejecutadas, no garantizabracketscancelados: NO etiquetarSTOPoriginalpormerotipoentrada ni porratioSL/TPausente. Y901/902 mezclansmarttypes;BTCshortSTOPenentry_type_groupsnoes necesariamenteoriginalSTOP.

ConciliaciónadicionaldemetadatosvíaMCP logscompletos: leerpáginaslogs hastafin(noestima),parseBTC_EXPLORE_FILL conreceta/actualtime/entry/qty/d/target yterminalBTC_EXPLOREcounts. Exigirnumlogsfill==terminalfills==matchesbijectivoscontrapathsdelanálisisporBTCshort/openclock/precio/qty(tol1e-7),target/d2.0,terminalcloses=fills. Cualquierunknown/faltante/ambiguo=>bloqueoelegibilidad, no imputar etiquetas. Lasetiquetassleeve se añaden a paths para selección porconciliacióndemetadatos,nosepasanarraysde resultados aPython ni seléeFS/DB. No presentarcohortesmonetariasdesupl/originalSTOP si elinputdelanálisis no soportaesas etiquetas; informar cartera/BTCglobalyconteosreconciliados. Esta conciliación no cambiaPNL/fees/MTM ni essegunda reconstrucciónfinanciera.

GateslegacyR8idénticosambasB/C:ΔnetN204>1e-7,+5Mactivos65/Q80full/included,+10net>=N204−1e-7,DDmotor>=−25%.>=30fillsdelsuplporlogsreconciliados. Diversidad adaptadaANTESresultados: Y901/902>=10entradasconcambiorealejecuciónvsN503(contartipo/tiempo/precio,altas/bajas;precios1e-7);Y903>=10salidasemparejadasmodificadasvsN503. Además>=3de5bloques2021..2025(2025parcial)ΔMTMN204positiva yΔnettrasdescontarmejormesincrementalpositivo. Filtrosoperativos,noconfianzaestadística niOOS. Rankingúnicoparalas13recetas,mismo mínimoM/Q,mínΔ+10,peorDD,IDlex;sinbononovedad. Si ningunaelegible,ceroextras.

## QA y trazabilidad

Fuentes23métodosprotegidos salvo los puntos declaradosdeejecución/metadata/ramasuple,posiciónriesgo/smartorder/cancelación/expiry/rearm/costos/qtyround/reset/clocks/deadlinevalidos;fixturesnogarantizanlifecycle. LeerfuentesporMCP,revisiónrootycrossreview,6formularios/18snapshots,datosfinancieros/metadatosreconciliadosantesselección. Sólo2runsYalavezcuandohaya2slotslibres,globalmáximo4; no interferirV/X, nopurgas ni modificacióndereferencias.

## Aclaración terminal anterior a las corridas Y

Los contadores de cierre de estrategia pueden preceder la liquidación forzada del motor al final. Se exige fillslogs=terminalfills=matches y cierresobservados+suplementoscerradosenboundaryreconciliada=fills; es admisiblecierres==fillsya deorigen. Si se usaajusteboundary, esexactamenteelnúmerodepathsdesuplementoclose==finishMs y MTMterminal_reconcilestrue, noestimaciónniimputación. Si loscontadoresincluyenlaclausurafinal,no se suma doble. Elcloseforzado nopruebaliquidez ejecutable fueradelmotor. No cambia hipótesis/precio/riesgo ni fechasY; corrigecriteriometadataalcomportamientoyaconocidodelmotorantesdeYresultados.
