# V6 — prerregistro de eficiencia, reducción de OI y contracción NR7

Emitido 2026-10-21 00:50:43 UTC. Antes de implementación o economía V6 y ANTES de resultados V5: sus tres sectores sólo están implementándose, sin backtests. El usuario autorizó expresamente V5 y V6 después de conocer el cierre V4. No se eligen estas líneas para rescatar el PNL de V5.

## Alcance y documentos normativos

Se incorporan íntegramente V6_EFFICIENCY_PROPOSAL.md, V6_DELEVERAGING_PROPOSAL.md y V6_NR7_PROPOSAL.md. Reglas económicas, selección, presupuesto, ejecución, calendario y auditoría comunes de RESEARCH_PROTOCOL_V5_20261020.md se aplican a V6, con las diferencias y matriz exactas de este documento. Esta referencia no autoriza reutilizar resultados de una regla anterior como si fueran V6.

Sólo BTC-USDT Binance Perpetual Futures,4h UTC, ejecución1m completa. Dueños dedicados /root/v6_efficiency,/root/v6_deleverage,/root/v6_nr7; root mantiene núcleo, registro y finanzas. V1–V4 cerraron sin candidata,151sesiones económicas nuevas y170slots nominales.2020–2025 ya observados;2024–25 confirmación interna reutilizada,noOOSvirgen.2026 cerrado. SinML/RST no solicitado/live/paper/órdenes reales/Pi/cuentas/instalaciones/restarts/CLI investigación/DB/env/commits/push.

## Tres reglas y seis nominales

Nombres/IDs/atributos en REGISTRY_V6.json. Cada sector aporta precio solo y precio+OI; funding contableON en todas.

EFFICIENCY: E_k=(C_k−C_(k+24))/sumabs24deltas de su propia ventana25cierres. Plano válidoE=0. Entrada26cierres paraE0/E1: longE1<=.35 yE0>.35; shortE1>=−.35 yE0<−.35. Sin otros filtros de precio. Suma normalizada por mayorabsdelta para evitar overflow, sin epsilon/clamp. Salida estadoE0<=0long/>=0short después del fill,25cierres válidos, independiente deATR/OI. Stop2.5ATRsimple14 fijo,sinTP/trailing,hold60barras4h=10d. Vecinos riesgo2.25/2.75ATR; señalh.315/.385,ventana24deltas ysalida0 fijas.

DELEVERAGING: D=C0−C6, Q=C0−C1, A=ATR14simpleactual. LongD<=−2A yQ>0; shortD>=2A yQ<0. Estado repetible por decisión, no cruce/latch. Entrada15OHLC porATR. P sólo precio. POI exige además OI0/OI24<=.98, valores base positivos/finitos/asof/frescos; NO se aplica filtro OI creciente. Es proxy de reducción de posiciones,no identifica liquidaciones reales ni su lado. Stop2A/TP2R=4A desde fill,hold12barras4h=48h,sinotra salida indicadora/trailing. Vecinos riesgo1.8/2.2A mantienenRR2; señaldisplacement1.8/2.2A ycaídaOI.018/.022 (ratios.982/.978) conjuntamente; P sólo cambia desplazamiento. Períodos ycorrección estricta quedan fijos. OI no gobierna salidas.

NR7: rangoRk=Hk−Lk. B−1 mínimoESTRICTO entre siete barrasprevias: R1<min(R2..R7); B0 excluida. LongC0>H1,shortC0<L1. Oportunidad sólo barra inmediatamente siguiente, sin latch ni retrofill al nivel. Señal8OHLC,ATR15dominaentrada. Empates bloquean; rango0 deB−1 válido si esmínimoestricto. B0puede negociaramboextremos,sólocierredefineúnicadirección. Stop2A/TP3R=6A,hold24barras4h=4d,sinotra salida/trailing. Vecinos riesgo1.8/2.2A mantienenRR3; señalNR6/NR8(enteros redondeados desde6.3/7.7, variaciónreal±14.2857%,noexacta10%). No cambiar objetivo si resulta demasiado lejano.

## Núcleo y OI explícito

Nuevo ResearchV6Base4h deriva de la fuente V5Base4h congelada antes de economía V6. Hooks neutrales deV2 inmutables. BAR14400000,DAY86400000, referenciaOI6barras24h,buffer8;lag4h=1barra,currentT−4h/refT−28h,buffer9. Slotsausentes/cero/stale conservados,sinwarmupOI. Calidad de reloj original,label+6min,fresh10min;noPITcertificado.

El nuevo núcleo agrega OI_RULE explícito 'rising' o 'declining' yOI_DECLINE_FRACTION. ParaEFFICIENCY/NR7 rising igualV5. ParaDELEVERAGING declining compara ratio<=1−fraction yregistra ratio/fraction/regla con motivos propios: oi_decline_below_threshold no significa oi_nonrising. Calidad inválida siempre bloqueaPOI antes de comparar; cero no representa100%caída. P no exige calidadOI aunque registre contexto. No invertir booleanos en secreto ni aplicar rising adicional.

La ratio debe ser finita para comparación declining; no normalizar pornotional/value_quote,cuya caída podría deberse a precio. Se usa accessor público open_interest de cantidadbase ymetadataoriginal. Mismo retardo se aplica al parOItarget/referencia, no a señalprecio. No ampliarfreshness ni reagereference.

ATR media14TR de15OHLC cerradas offset0; toda aritmética finita. Datos alineados/consecutivos/positivos/coherentes,última aperturaT−BAR. Warmup240barras4h=40d,sinoperar. Precioactualincluyeúltimabarra ya cerrada; fuentesfuturas/prefijosmásviejosnoinfluyen. NR7no usa ATRprevio.

Capital10000,isolated3x,capnotional1x, riesgo2%stop+ambosfees,quantityfloor8,fee.00045/slip0/fundingON,configexactaV5. Stop/TP desdefill real usando distancia congelada. Funding/gaps/slippage pueden superar presupuesto;noresizingretrospectivo. Una entrada ejecutada/díaUTC,longshortcomparten,unaposición,sinpirámides/parciales. No reentrada enmisma decisión quecierre. Señalesbloqueadasno latch;DELEVERAGINGrecalculaestado nuevoenfuturasdecisiones.

Prioridadprotecciónintrabar delmotor,calendario,holdabsolutoygestiónindicadora sóloT>fill. NingunaOHLCconapertura>=finish nifundingefectivo>=finish. CierreTfinish deúltimavela2025noesdatode2026. Replaysmantienenhistoria/capitalinactivo ycierrantodoslosbordessemestrales.

Datasets mismosV5: funding9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571, OI6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf. Fastsolicitadotrue/efectivofalseporfunding;debugtrue,exports/benchmarkfalse;sinconfigglobal.

## Fases y gates independientes de V5

A: seisSCREEN[2020-09-01,2024-01-01),10000continuos cadauno. N>=30,net>0,PF>=1.2,DDmotor<=25,almenos2/3añoscompletos2021–23positivospor equity.2020parcialfuera. CAGRdesarrolloinformativo.

Hasta2finalistas rankingmenorDD,mayorPF,menorturnover,menosfeaturesOI,IDlex. Shortlist/fuentes/config/hashes ANTESdeeconomía2024–25V6. Sin elegibles, cierreSIN_CANDIDATA;slotsrestantesnoseusanparatuning. V5 yV6secierran porseparado,aunquecompartaninfraestructura/datos. No sumartradesentresectores/ciclos paraaprobarN.

B: cuatrofolds2024H1/H2,2025H1/H2;trainexpansivo2020Sep→inicioeval;C1trainreutilizaSCREENsiexacto. GatestrainN30/net/PF/DD;guardar elegibilidades/selecciónANTESdeevaluaciones.16slotsmáximo(2×4×train/eval),hasta2reusos. Selector global distinguido devariantesindividuales;calendarios individuales detrain no cambianporPNLfuturo.

C: dosreplaysmáximo[2024-01-01,2026-01-01),731días,capitalcontinuo10000,4semestres separadosycierresbordes. Candidatahistórica:net>0,PF>=1.2,DD<=25,N>=100,>=3/4semestrespositivos,CAGR>=15%(365/731). Meta20–30%orientativa,sinrelajar100siquedan95.

S1fee.0009/slip0,S2fee.00045/slip5bps,S3fee.0009/slip10bps. S1/S3net>0DD<=25obligatorio;S2informativo. Cuatrovecinosarriba,todosnet>0DD<=25;calendariofijo,nuevossizing/fillsdelmotor. LagOI4hnet>0DD<=25;sinOIreusonominal. Proxy/globalfunding×.5/1.5cantidadesfijasdescriptivo,noreplay. Noelegirganadorvecino nirepararnominalconescenariomejor.

## Presupuesto, pruebas y cierre

40slots económicos=6SCREEN+16WF+2REPLAY+6COST+8VECINOS+2LAG. Hasta6técnicos:uno7d2020Sep1→Sep8porsector,máximo unreemplazoportécnicoerror,noPnLtuning. Global2motores/peragentemáx2/analysisjobs2. V5/V6compartenestosmáximos,no4motoresporserdosversiones.

Antes de economíaV6:compile/AST/hash/readbacks,testsdeterministassectores ycore(adicionalOIdecliningratioexacta.98/.982/.978,risingindependiente,zero/calidad/lag/sincompresión),riesgo+fees/cap/cuota/sameT/fill/protección/calendario/hold/JSON<=1900. Smokesmotor,assertsenhooks;sinfillrealnoacreditarbranch. Fuentessecongelan despuésdechecksyantesdeSCREEN.

Finanzas sólo snapshots completos viarun_analysis,inputs/→output/,sinlecturaDB/env/proyecto/IOexterna,niarrancarmotoresdesdeanálisis. Estadísticadefuentesconliteralescapturados/ASTpura,sinimportsdeproyecto. Contabilidad1e−6USDT,incluyeraw/effectivefundingjitter<=1000ms,feesórdenes/slippageadverso,balances,PFtradesúnicos,DDmotor,curvadiaria,meses/años/semestres,longshort,Sharpe/disponibilidad,turnover/exposición,concentración.

Reportes.md por save_strategy_report,JSONporwrite_project_file;logs/planes/causas/windowhashybranchcoverageconlímitesexplícitos. Timeoutstartguardarraw yrecuperarlecturaMISMOID,noretryduplicado;MCPunavailable suspendedependientes,sinworkaround/CLI/restart.

Si fallan las seislíneas,se cierraV6sin candidata,conevidenciapreviasinpromoción. Siaprueban,completarconfirmaciónyrobustez delpresupuesto,conresultadosnegativosincluidos. NiV5niV6seendulzan a posteriori;2026cerrado. El alcanceactual autorizaestosdosciclos,nobúsquedailimitada nitrading.
