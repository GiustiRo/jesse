# R10 — validación congelada K1001
Autorizada por usuario tras recuperar MCP: completar R9, limpiar sin perder traza, validarK1001 igualqueY902 y tabla de progreso.2026cerrado incluso inspección; muestra de desarrollo reutilizada2020-10-15 inclusiva→2025-12-31 exclusiva, NO OOS.
## Hipótesis
El mismo eventoY902/N503 pide continuación por debajo del mínimo conjunto de s y t, no sólo mínimo de t. Pretende evitar ruptura de una sola vela que no supera soporte previo. Distancia técnica sigue original desdeCt; SLfill+d/TPfill−2d,48hdesde fill, pending una4h, riesgo/capital/sizing/prioridades exactos. K1001 sólo cambia5entradas por cartera frente aY902 yestafragilidad no se borra por pruebasadicionales.
## Contrato y carga
10000shared,riesgo1%trade/8%aggregate,5xisolatedcap4.4reserve.001sizing;BinancePerpetualFuturesBTC/PAXG/SPY4h y3feeds1m,SPYBSecond/CMarket,PAXGoriginalBEdependientefee,warm240debugtruefastfalsecharttrue. Sinfunding. Máximo2backtests globales y1analysis, consultas summaryfirst/listlimit2, no reinicios/purgas ni borrarfuentes/sesiones/velas/informes. Limpieza13workspacesR8terminados tras13archivosreproducibles, manifestMCP_CLEANUP_TRACE_MANIFEST_20261019.md.
## Ocho corridas nuevas exactas
K170 B/C:fuente BtcY902ExploreR1001 exacta,fee.00070porlado.
K195 B/C:mismafuente exacta,fee.00095porlado.
K118 B/C:BtcK1001RobustT18,TPsuplemento1.8R,fee.00045,restoexacto.
K122 B/C:BtcK1001RobustT22,TPsuplemento2.2R,fee.00045,restoexacto.
Vecinoscontrolan sensibilidad,no candidatos,no mejorvecinopromovido. Guardfísico entry>max(2d,target_distance)evitaTPnulo/negativo, conservando piso original. FuenteoriginalK1001/Y902 no se edita. No máscombinaciones, filtrosdecalendario ni nuevosescenarios postresultados. K1005nuevo hallazgoR9se registra sinheredarvalidaciónY902/K1001y sin corridasnuevasenesta fase.
Referencias preservadas: nominalN204/Y902/K1001; fee70N70/F70Y902;fee95N95/F95Y902; TPvecinosY902T18/T22 aigualfee. ComparaciónprincipalK1001vsY902 yN204 aMISMOfee. TodasconmismosPAXG/SPY/riesgo.
## Auditoría y diagnóstico
Run_analysisfinanzas desdeinputscompletos+4anclas:qty/fills/fees/PNL/wallet/terminal/MTMUTC. IdentificaciónsuppporlogsMCPcompletosybijectivepaths,time/entry/qtytol1e-7,target/d2o1.8/2.2;STOPpormerotipo noesoriginal. Artefactostextuales, noPNGbugconocido.
Reportarneto/retorno/CAGR/DD/PF/Sharpe/Sortino/Calmarytodasmétricas disponibles delmotor, trades/winrate/fees/exposición/turnover, MTMrutas/años/meses/trimestres nominalyoverlays+5/+10 separadosfeemotor,denominadorescalendario/activos yfull61/included63. 'Todasmétricas'conservarJSONrawmotor/auditor comoanexo,tablaslegiblesporcategoría; nocompletarcamposausentesconestimaciones.
Concentración aritméticaquitandomejormes/cadaaño,sinreplay,full61einc63. Bootstrap pareado circularbloques6meses,10000seed9022026,mismaindicesB/Cyfeeniveles,IC95%mediaMTMδUSDTmes yfracción>0 descriptiva. DoscomparadoresN204yY902enel mismojob10inputs(4anclas+6targets). No confianzaanti-overfit ni ajuste por búsquedas anteriores.
Diagnóstico operativoigualY902:fee70/95δvsN204>=0ambas,DD>=−25%;vecinosnet>0ambas yporcarteraalmenosunvecinoδN204>=0. Mostrar ademásδvsY902igualfee/TP ysiunladoempeora. No promoción automática nirelajarR8/R9gates. Guardarevidenciadelos5cambios, CIs yconcentraciónantesdeconcluir.
## Entregables
CerrarR9 y manifiesto; limpiezaarchivada;8corridas/auditoríasK1; incertidumbre3niveles; tabla de progresoprincipalN204→N503→P604→Y902→K1001→K1005 conB/Cseparadas ymatrices completasdeexploraciones. Distinguirfechaejecución/benchmark previo, costecomparable, resultadosduplicadosnoindependientes, validacionesnocompartidas entrecandidatas. TodosreportesporMCP.
