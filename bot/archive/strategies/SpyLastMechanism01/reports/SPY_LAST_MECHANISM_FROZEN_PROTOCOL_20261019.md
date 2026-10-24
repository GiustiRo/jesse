# SPY última ronda: seis contrastes de mecanismo BR02

Fecha local2026-10-19. Estado: fuentes creadas/readback6/6, pendiente revisiónroot; ningún draft/run de esta tanda todavía. Exactamente seis fulls nuevos, sin otras rondas. Base SpyStructR1BR02 original intacta.

Referencia económica existente[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639). Candidata base[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810):N16/net874,79585655/DDmotor−3,8005064/Sharpe0,7183939. No réplicas nuevas.

## Matriz fijada antes de resultados

|ID|Fuente|Cambio único de mecanismo|
|---|---|---|
|MECH01|SpyLastMechanism01|Operar únicamente ordinal2 de señalesCq calificantes desde reset|
|MECH02|SpyLastMechanism02|Operar ordinal>=3|
|MECH03|SpyLastMechanism03|Operar únicamente ordinal3|
|MECH04|SpyLastMechanism04|Operar ordinal2o3|
|MECH05|SpyLastMechanism05|Ordinal>=2original, entrada MARKETactual enveznivelDonchian; mismo evento/ATR, recalcularqtyconentradaactual|
|MECH06|SpyLastMechanism06|Ordinal>=2, pero contar y operar sólo INICIO de rachas de señalesCqcalificantes consecutivas|

01/03aislan oportunidades ordinales;02pregunta si resultado necesita segunda;04si necesita colasordinalesposteriores;05separa sensibilidad de ejecución pasiva;06si la aparente señal depende de repetir barras contiguas de un mismo estado. No son seis muestras independientes ni nueva evidenciaOOS: misma historia2020–2025 reutilizada.

## Semántica causal exacta conservada

Reset al cierre<=mitad entre máximo y mínimo de26velas PREVIAS filtradas; momento de reset reiniciaepoch_count0. Inicio de ventana censurado hasta reset observado. _origin(context) exige régimenoriginal/entrywindow/fresh M1 exacta y level<price<=level+ATR y0<2ATR<level, sin posición, cash, sizing o margen.

before borra struct_event en CADA tick; sólo procesa velas4h cerradas pertenecientes al calendario y cuyo timestamp coincideconclosed_candle_open_time. Cuenta oportunidades aunque ocupado; la oportunidad no ejecutada se consume, sin cola/replay. Stop y gestión actúan como original, sinfiltrohorario añadido.

MECH06:
- En TODA vela filtrada cerrada calcular eligible=bool(_origin(context)), aunqueocupado y aunqueFalse.
- previous=prev_eligible; guardarprev_eligible=eligible. Si noepochseen, dejaprevFalse y no cuenta.
- En reset, guardarprevFalse ademásdecount0; noarrastrarrachaentreépocas.
- Contar sóloeligible and notprevious; siFalse cortar racha. Una falta de quote, ventana cerrada o régimenfalso también corta la racha, por definición declarada.
- Sóloinicioordinal>=2 emiteevento; noemite niincrementa en barraseligiblecontiguas.
- Barras excluidas del calendario no son observacionesfiltradas; la velaabierta16UTC sípertenecehistoria y su ventanaentradaFalsecorta racha normalmente.
- No contador dependiente de fills o cierres; rachas seobservan incluso con posición.

MECH05 conserva elegibilidad de frontera antes de repricing: _origin y _set_struct_event originales validan la frontera, _plan validaotra vezdistanciaboundary y despuésentry=float(self.price),finitey0<distancia<entry. Sizing/stop se basan nuevaentradaMARKET/distanciaATRoriginal. No prometer fillsidénticos, selección/ocupación/saldo cambian.

01..04 resto fuente idéntica salvoclassname,comentariopropósito y predicadoordinal.05 sóloclassname yrepricing_plan.06 sóloclassname yactualizaciónbeforedeinicio rachas/reset. Ramasheredadas BR_MODE>2 y BTCshortinactivas, sinrutasBTC/PAXG o datosextra.

## Contrato y ejecución

2020-10-15→2025-12-31exclusiva;2026cerrado. SPY-USDT4h+M1únicamente, proxySPXCFDBID/10aceptado,UTCMonFri00–20historia/baropen00–16entrada, warm240,fast/debugfalse.10k/riesgo1%/fee0,00045todosladosytipos/isolated5x/cap4,4/sinpiramidar/reserva0,001sólosizing. Stop2ATR/BE2,25R/trail4,2/tightening5R8R/ledger/sizing/cancelunabarra/fresh original. Sinfunding/datosnuevos/scripts/instalaciones/framework/configglobal/restarts/live/Pi.

Trasrevisiónroot correr01/02,03/04,05/06; máximo2míos simultáneos/4globales, slots llenos sihay>=2listos. TítulosSPY LAST MECH01..06. Notas fuentescompletasydrafts IDs/URL guardados antesrun. No cambiar tras observar resultados.

Análisis8snapshots(seis+Cq+BR02),unslotmío/dosglobales. Fills/qty/feePNL/wallet/nooverlap/terminal; N/net/grossfees/PF/Sharpe/CAGR/DD/holding/tiempoexpuesto/notionalentrytime/turnover/costes5/10bpsRT/exbest/ex3/cohortes por añoCIERRE/tiposórdenes. Artefactosresumen<50KB y detallesporfila; rootMTMpor separado. Estáticos costes conservanqty/fills. Nocionaltiempoavalorentrada no es nocionalMTM.
No elegirordinalganadorcomoresultadoindependiente ni prometer robustez conNpequeño. Registraridentidadesexactasypérdidas. Noinsistirhastaganadora; ésta es última rondaautorizada.

Leídos DOCS/skillfrontmatter/reglasbot; backtest-expert yjesse://strategy ya completos en contexto. Sin acciones fuera MCP para proyecto.
