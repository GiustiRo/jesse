# V4 — prerregistro común de mecanismos horarios
Fecha local2026-10-20; emitido 2026-10-21 00:13:36 UTC. Estado: ANTES DE IMPLEMENTACIÓN Y ECONOMÍA V4.

## Alcance y evidencia previa
Usuario autorizó investigación autónoma con subagentes por sector y hasta dos backtests por agente. Se mantienen dos motores GLOBALES y dos jobs analíticos como máximos por estabilidad local. DOCS vigente permite «Timeframes: A explorar/definir» yprioriza rentabilidad, no frecuencia.
Sólo BTC-USDT Binance Perpetual Futures,1h,24/7,una posición neta por sesión, sin pirámides. Cambiar de4h a1h consume seis configuraciones nuevas y cambia duración del warmup; no es ajuste invisible deV3 ni búsqueda de frecuencia para llenar muestra. Tres sectores independientes con dueños /root/audit OSCILLATOR, /root/atr_oi SHOCK, /root/atr_p FUNDING_RESET; root núcleo común/registro/auditoría.
V1 terminó sin candidata96slots;V2sin candidata32slots;V3sin candidata36slots(33runs+3reutilizaciones), con P cerca del objetivo financiero pero95<100 y2025casi plano. OI también falló CAGR y estrés combinado. Resultados anteriores conservados; no sustituir nominal por vecinos o lag más favorables.
2020–2025 ya fue visto en ciclos previos.2024–25 es confirmación interna reutilizada, no OOS virgen.2026 sigue cerrado; excepciónK1001 no aplica. SinML/live/paper/Pi/cuentas/restarts/instalaciones/commits. Objetivo orientativo20–30%anual negociable; umbrales de promoción no se disminuyen.

## Especificaciones nuevas y configuraciones
Las tres propuestas completas forman parte del prerregistro:
- V4_OSCILLATOR_1H_PROPOSAL.md: RSI2Wilder FINITO32cierres, semilla2deltas+29recurrencias. R0/R1 cadauno ventana propia. Tendencia C0>SMA200(0)>SMA200(24) y espejo short. LongRprev>10,Rnow<=10;shortRprev<90,Rnow>=90. Stop2ATR14simple actual; salidaRSI>=50long/<=50short sólo en cierre posterior alfill;hold24h. SinTP/trailing.224cierres para entrada;32válidos bastan para gestionar salida.
- V4_VOLUME_SHOCK_1H_PROPOSAL.md: última vela shock con abs(C0−C1)>=2ATRprev yvolumen>=2media24previa, ambos cálculos excluyen shock. Entrada contraria inmediata; stop1ATRprev yTP1ATRprev desdefill;hold6h;sin régimen adicional ni trailing.25cierres; volúmenes finitos>=0, media>0.
- V4_FUNDING_RESET_1H_PROPOSAL.md: oportunidad sólo por evento nuevo publicado; primera decisión inicializa sin entrar; cada nuevo evento se consume aunque rechazado. History32eventos: baseline media/desvío poblacional de30estrictamente anteriores alpar, fijo paraambos. LongZprev>=1 yZnow∈[0,.5];shortZprev<=−1 yZnow∈[−.5,0]. Confirmación espejo C0>SMA72(0)>SMA72(24),C0>SMA24,C0>C6.96cierres. Stop2ATRactual,sinTP/trailing;salida estado C0<SMA24long/>SMA24short sólo T>opened_at,igualdadmantiene;hold72h. Inicialización/eventoviejo/historiainválida no se reintenta después.
Clarificaciones previas a código: baseline totalmente constante se declara desvío0 de forma explícita(max==min),sin epsilon; evento debe satisfacer0<T−settled_at<=2h con rawjitter preservado yavailable_at<=T.32eventos crecientes únicos,separaciones8h±1000ms; accesores settled yúltimo row deben coincidir, sin fallbackprivado. Señal no usa mark_price ni próxima tasa. Historial de funding anterior al comienzo puede observarse sólo mediante API pública asofT; no representa cashflows anteriores de una posición inexistente.
Clases/IDs yatributos nominales exactos están en REGISTRY_V4.json. FP significa funding+precio;PV precio+volumen, no controles de precio solo. Cada sector tiene ablación con/sin OI24h; eso no prueba causalidad del resto de features.

## Reloj, núcleo y economía
BAR=3600000,DAY=86400000. Sólo velas cerradas t+BAR<=T, última t=T−BAR, horasUTC alineadas yconsecutivas;OHLCfinito>0 ycoherente. Aritmética finita, sin rellenos ni barra futura.
Núcleo V4 nuevo. Se reutilizan sólo componentes de ejecución/auditoría de V2 comprobados independientes del BAR; before,on_open,update_position,terminate ytodoindicador/ATR/OI quedan definidos explícitamente en V4. V1–V3 no se modifican. ATR media14TR/15OHLC; SHOCKusa offset1(última vela excluida),restooffset0. Exigir protección fija desde fill ymetadataoffset/ventanas.
Warmup240velas1h=10días, suficiente para224/25/96;sin operar durantewarmup. No importar datos nuevos porCLI. Datasets versionados:
funding 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571
OI 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf
OI se guarda en cada decisión horaria, incluidos slots ausentes/ceros/stale; referencia EXACTA T−24h observada entonces. Primeras24decisiones inicialización, referencia posible25ª. Buffer26nominal. Publicación supuesta label+6min,frescura10min desde disponibilidad;archivo retrospectivo noPIT. Variante sinOI nunca exige calidadOI. Replays conservan historia en períodos inactivos.
EntradaMARKET,cuota una entrada ejecutada/díaUTCcompartida longshort;untrade de seguridad también consume. No entradas en misma decisión que cierre previo; no latch de señales. Entrada estricta start<T<finish ypara cada intervalo activo a<T<b, sin fusionar intervalos.
Prioridad gestión: protección intrabar del motor; en decisión cierre de calendario, luego holding absoluto, luego salida indicadora sólo T>opened_at. Stop nunca se afloja; noATRrecálculo de distancia protectora. Cierre final se incluye en trades/saldo aunque metadataopen_pl sea precierre. Velas con apertura>=finish yfundingefectivo>=finish excluidos; cierreTfinish de última vela2025 no es dato2026.
Capital inicial10000 por sesión,isolated3x,capnotional1x,tamaño NOmultiplicado por leverage. Plan a precio p con distancia d:
q=floor8(min(C/p,.02*C/(d+f*(p+stop_pre)))),stop_pre=p−s*d>0.
Stop/target se anclan fill usando d congelada. Fee del escenario entra en sizing. Funding/gaps/slippage pueden superar2% y capprefill, se reportan; no redimensionamiento retrospectivo. Bruto−fees+funding=PNL ycapital transportado en replay, sin depósitos.
Nominalfee.00045/slip0,funding históricoON también sin filtroOI;debug/fastsolicitadostrue,fast efectivo false por funding,benchmark/exportsfalse,config exacta por sesión enregistro.

## A — screening seis mecanismos/ablaciones
Ventana [2020-09-01,2024-01-01),una sesión continua10000 por cada una de seis configs. No optimización ni barrido.
Gates >=30trades,neto>0,PFneto>=1.2,absDDmotor<=25;almenos2/3años completos2021/22/23 positivos por equity.2020parcial separado. Reportar CAGRreal, sin gateCAGRdesarrollo.
Hasta dos finalistas, ranking menorabsDD,mayorPF,menorturnover,menosfeaturesOI,IDlex. Shortlist/fuentes/config/hashes guardados ANTES deconsultar economía2024–25 deV4.
Si ninguna pasa,cerrarSIN_CANDIDATA,conservar mejor avanceprevio,no retocar umbrales/períodos/salidas para salvarlínea ni expandir indefinidamente configuraciones sobre misma reserva. Cualquier línea adicional exige justificación nueva yprerregistro, no renovación automática por deseo de beneficio.

## B — cuatro semestres de confirmación
C1 2024H1,C2 2024H2,C3 2025H1,C4 2025H2. Train expansivo desde2020Sep hasta comienzoeval. C1train equivale SCREEN, reutilizar si exacto. Gatestrain N>=30,net>0,PF>=1.2,DD<=25;sin nuevo gateanual fuera del screening.
Para cada fold registrar elegibilidades individuales yelección global con ranking fijo antes deeval. Ambas finalistas pueden evaluarse para diagnóstico; sólo elegida integra selector. No reasignar por retornoevaluado.16slots máximo(2finalistas×4×train/eval),hasta2reutilizados.
Calendarios de replay individuales son ventanas donde la finalista aprobó train nominal. No dependen de evaluación futura ni cambian bajo costes. Fuente de wrappers cambia sóloSTART/FINISH,sinmutar nominales. Mantener decisiones/shortlist inmutables después deeval.

## C — replay, fricción y dos tipos de vecinos
Hasta dos replays [2024-01-01,2026-01-01),731días,10000 iniciales,capital continuo. Entradas sólo en intervalos individuales elegibles,intervalos semestrales separados;cierre en TODOS los bordes semestrales, sin reset de capital/OI. SelectorWFsintético reescalado se informa aparte.
Nominal para candidata histórica: net>0,PF>=1.2,absDDmotor<=25,N>=100,>=3/4semestres positivos por equity de esa cuenta yCAGR>=15%. CAGR=(saldo_final/10000)^(365/731)−1;no tiempo expuesto ni promedio dePF.
S1fee.0009/slip0;S2fee.00045/slip5bps;S3fee.0009/slip10bps. Replays completos del motor,calendarionominal fijo. S1/S3 deben seguir net>0/DD<=25;reportarS2sincrear gateextra. Slippage adversoMARKET/STOP,limit según contratoactual;no haircut sustituye ejecución.
Cuatro vecinos por finalista sin seleccionar ganador, todosfee/slip nominales ycalendariofijo:
R09/R11 riesgo: multiplicar distancias protectoras por.9/1.1;OSC/FRstop1.8A/2.2A, exitsindicadores iguales;SHOCKstop/TP.9A/1.1A conRR1.
A09/A11 señal: OSCumbralentrada9/91 y11/89;RSIexit50,seed32,trend200/24 iguales. SHOCKumbralesprecio/volumen1.8/1.8 y2.2/2.2,stop/TP1A iguales. FRunidadeszextremo/reset.9/.45 y1.1/.55,baselinemedia30 yconfirmacionesprecio iguales. No otros períodos/semillas/hold. Cada vecino debe net>0/DD<=25;si no,FRÁGIL. Esto añade sensibilidad de alfa a riesgo, no prueba exhaustividad de parámetros.
Para quienusaOI: retraso adicional CUATRO HORAS DE RELOJ =4barras1h (no1barra), currentT−4h/refT−28h con calidaden reloj original. Buffer30;primeras28decisiones inicialización,referenciaposible29ª. Debe net>0/DD<=25. Variante sinOI reutiliza nominal para ese slot.
Sensibilidades informativas fijas: sólo cashflowproxy×.5/1.5 yglobalfunding×.5/1.5, cantidades/fills fijos,fuentes desconocidas separadas. No replay/no nueva candidata/ningún gatefavorable escogido.

## Presupuesto, pruebas y final
Máximo40slots económicos nominales =6SCREEN+16WF+2REPLAY+6FRICCIÓN+8VECINOS+2LAG;referenciasreutilizadas cuentan slots, no nuevos motores. Hasta seis smokes técnicos:uno por sector de7d[2020-09-01,2020-09-08),ycomo máximo un reemplazo por sector sólo por error técnico documentado;ninguna rentabilidad guía parámetros. Errores/IDs/fuentes yreparaciones se conservan;si se agota reparación sinconformidad,no economía deesa línea.
Antes de economía: compile/AST/hashes de todas fuentes ytests deterministas de RSIsemilla/prefijos/futuro,ejehorario/ATRoffset/volumen, baselinefunding/exclusiónpar/sigma0/dedup/asof,OI24/lag4h/cero/stale,cuotaUTC/no reentrada,protecciónfill/fees/cap,prioridadesholding/calendario ydatosinválidos. Smokes acreditan importación/API/motor;sin eventoreal no afirmar cobertura de fills.
Fuentes yconfigs congeladas antes decada fase;no modificar V1–V3. Core/helpers/tests se guardan porMCP;reports save_strategy_report,JSONwrite_project_file. run_analysis sólo fuentesliterales capturadas/AST o snapshots COMPLETOS eninputs/,output/;sin leerproyecto/DB/env ni research_scripts. Máximo2jobsanálisis;no motoresdesdeanálisis.
Timeout de arranque: guardarraw yconsultar MISMOID, jamás duplicar por respuesta perdida. MCPunavailable suspende dependientes hasta read exitoso,sin workaround. No packages/restarts/SSH/live.
Contabilidad tolerancia1e−6USDT;config/datasets/fechas/fullcalendario verificables. Métricas net/gross/fees/funding,PFtradesúnicos,DDmotor ymuestreado final,meses/años/semestres,longshort,turnover/exposición,concentración,qty/fills/slip,causas ybranchcoverage. Logs cada línea<=1900chars,dividir ventanasfunding32 en bloquescanónicos conhash,no truncar.
Estados SIN_CANDIDATA,RECHAZADA,FRÁGIL,INCONCLUSA,CANDIDATA_HISTÓRICA oavanceparcial sinpromoción. Historial V1–V4 yreserva reutilizada siempre visibles. Este ciclo termina las tres hipótesis nuevas justificadas aquí; no convierte búsqueda ilimitada sobre mismo pasado en evidencia independiente. Si fallan, cerrar honestamente el alcance con mejor avance ylimitaciones, sinbajar gates ni autoabrir2026.
