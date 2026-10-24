# SPY — investigación independiente terminada, cinco fulls
Fecha local18oct2026. Dos familias predeclaradas, cinco backtests económicos completos. Ninguna candidata nueva promovida. No quedan backtests ni análisis propios en ejecución. Referencia de cartera inmutable; BTC congelado y2026sin evaluar. No ampliar búsqueda con vecinos para rescatar fallos.

## Qué se investigó y con qué datos
Usuario acepta SPX CFD BID/10 disponible como proxy de precio para aprender reglas trasladables a SPY Binance Perpetual. Ese supuesto se respetó: no impuse nuevas fuentes ni funding (no implementado, fuera de etapa). Se evita volumen ficticio. Toda actividad por Jesse MCP; sin scripts de investigación, shell, framework, instalaciones, live/paper o fondos.

2020-10-15→2025-12-31exclusivo es desarrollo ampliamente adaptativo, NO OOS limpio. Cuenta10k, comisión.00045 por lado incluidasLIMIT, 5xisolated y techo bruto4.4. Nuevas comparaciones aisladas a1% de riesgo por trade; riesgo incluye fees y reserva10bps únicamente sizing. No aumentar tamaño para rescatar rentabilidad. La regularidad es objetivo de CARTERA, no requisito de cada señal.

Lecturas previas: handoff/ledger/inventario global, informes de diagnóstico, código referencia, MR sleeves, crisis shorts y calendario4/4. Se evitaron repeticiones MR/participación/calendario. Fuente primaria conceptual de segunda ronda: [Faber timing model](https://mebfaber.com/timing-model/) y [discusión del autor](https://mebfaber.com/2017/12/13/episode-86-quantitative-approach-tactical-asset-allocation/); la adaptación200quotes NO replica el modelo10meses ni prueba su edge.

## Resultados económicos, todos terminal finished
| Política / fuente | N | Neto USDT | Fees | CAGR motor | DD motor | PF |
|---|---:|---:|---:|---:|---:|---:|
|[ResearchSpyReference4h](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2)|31|751.35|286.48|1.399%|−5.213%|1.493|
|[ResearchSpyOpeningRange60](http://localhost:9200/#/backtest/a68dbfa8-3efe-410a-9c8b-861bf3609f38)|890|−6273.02|7559.20|−17.247%|−63.748%|0.661|
|[ResearchSpyOpeningDrive60](http://localhost:9200/#/backtest/98918ea4-78a2-4548-8f23-8c7459d07a30)|1162|−8700.06|9569.47|−32.384%|−87.217%|0.613|
|[ResearchSpySlowDefense4h](http://localhost:9200/#/backtest/12c25b07-a649-450a-979a-2bbd21c4ae5d)|7|284.88|6.27|0.540%|−3.389%|2.331|
|[ResearchSpySlowBeta4h](http://localhost:9200/#/backtest/531fdbfd-a092-44cc-b879-228a51c45e14)|7|385.77|6.31|0.729%|−3.304%|2.663|

Referencia aislada copia exacta de reglas referencia salvo class y riesgo1%; root verificó fuente. No confundir751USDT aislados con3660USDT de SPY en cartera3%/capitalcompartido. Políticas aisladas tienen distintos tamaños/capital-tiempo; sumar curvas no genera cartera.

## Familia1: aceptación de apertura cash NY
Protocolo SPY_OPENING_AUCTION_PROTOCOL_20261018.md, aclaracionesSPY_PROTOCOL_IMPLEMENTATION_NOTES_20261018.md. Range60 define primera hora09:30–10:30NY con dosvelas30m, exige60M1contiguas y primera confirmación posteriorcerrada11:00/11:30/12:00. Drive60 entra10:30 en dirección primera hora como contraste. Stops opuesto al rango, salida15:30 con quoteM1fresh, una entrada porfecha. ScheduleNY/ZoneInfomanejaDST; stop activo24/7 ydeuda de salida.

Fracaso neto inequívoco en AMBAS políticas y AMBOS lados. Precio antesfees +1286.19/+869.41 equivaleaprox1.53/0.82bps por nocional de entrada, frente~9bpsroundtrip modelados. No es evidencia que bajar un poco costes arregle la receta. Mayor actividad aquí destruye capital. No conservar sólo longs, mover hora, filtrar años o retocar stop tras resultados.

Entradas verificadas ORB11:00(563),11:30(221),12:00(106); Drive10:30(1162). Cero díasduplicados. Cada una tiene8trades que cruzan medianocheUTC por huecos/cierres tempranos; no fingirliquidación15:30 sin quote. No calendarioNYSEfestivo completo ni certificación de rellenoupstream. El protocolo contempladeuda.

## Familia2: prima direccional lenta frente a beta protegida
Protocolo SPY_SLOW_BETA_PROTOCOL_20261018.md. Registro de200quotesdiarias observadas16UTC, no cierreNYSE ni velasdailyimputadas. Primerreview tras200quotes y luego primer16UTCfresh mensual. H2 largo siquote>SMA200, cash si no; C2ignora filtro. Ambos stopinicial10%, ratchet mensual90%quote sinaflojar, sin retarget/TP/BE/rebalanceqty. Trasstopcash hastasiguientemes. Fuente íntegra leída root y snapshots guardados antes derun.

Primeraentrada ambos2021-07-29 16UTC: todo cash previo permanece en cuenta y métricas. Riesgo máximo inicial auditado0.999986% y nocionalmáximo0.0981774xequity. Es exposición pequeña por stopcola10% y presupuesto1%, no índice1x ni retorno extrapolable a él. Horasposicionado30417.10defensa/36456.23beta; referencia6971.42, ORB3357.18,Drive3485.97.

Filtro lento obtuvo MENOR retorno y DDmotorligeramentePEOR que control; no hay ventaja demostrada para promoverlo. Pocastransiciones (7trades con largastendencias, uno cerrado en frontera) impiden validar generalizaciones. No rechaza toda tendencia ni prueba que beta protegida mejore cartera. Referencia aislada también supera su retorno, con exposición diferente.

Defensa pierde33.76USDT excluyendo su mayor runner318.64; beta queda+107.03 sinmejortrade y−231.97 sin3mejores. Concentración descriptiva esperable en tendencia, no permiso para eliminar ganadores ni evidencia confirmatoria. Ambos dependen de trayectoria alcista/precio; no se atribuyealpha por PFalto con7observaciones.

## Costes, auditoría y MTM
Auditorías snapshots completos concilian PNL,fees ywallet; no se usan páginas parciales. Fees exactos.00045×nocional de cada lado. Adversidad estática sobre los mismosfills, +5/+10bpsRT:
- Referencia +592.19 / +433.04USDT.
- ORB −10472.57 / −14672.13.
- Drive −14016.43 / −19332.81.
- Defensa +281.40 / +277.92.
- Beta +382.27 / +378.76.
Estos son recargos contables, NO backtests dinámicos ni CAGR/DD nuevos. Slow resistecoste estático por turnoverbajo, sin que eso convierta filtradoinferior en ventaja.

MTMapertura rootV4a19d7e0afb404303aa33ca7cc1c19c53 succeeded con anclas y reconciliación:
referencia15/33mesesactivospositivos,15/63todos,10/21q,DDdiario−5.218%;
ORB15/61activos,15/63todos,0/21q,DD−63.748%;
Drive11/63activosytodos,1/21q,DD−87.281%.
Ver SPY_OPENING_MTM_ADDENDUM_20261018.md para completos.
MTMslow está en auditoría unificada root al cierre de este informe; no reportar años/meses por PnL realizado ni curvasmotor00:01. En slow contador1abiertopreterminal convive con tradecerradoterminal en snapshot; root debe conciliar como convención de cierrefrontera, no asumirprecioejecutable de medianoche.

## Registro técnico y persistencia
Todos los5backtests terminaron sinerror deestrategia. Comparaciónaperturaanalysis0c056e6b2f6a4fe3a86cf6253e117550 succeeded; slowanalysis6b7d9804d2504b4198332f7413b797a9 succeeded. Hubo intento04562648d83a4f3c82d584e84e9f88a8 fallido por asercióncorrecta aldescubrir8crucesUTC; no ocultarlo ni usar suMTM. Se corrigióanálisis paraomitir cashMTMinválido, noestrategiasniresultados. La figuratemporalapertura sólo dibujareferencia; no usar. Figuraslow explícitamentecurvamotor, no cierresUTC.

Código fuenteenlas5estrategias y snapshotsnotasdesesiones. Reportes/protocolos permanecen bajo ResearchSpyReference4h/reports. Artefactostemporales pueden caducar; principales cifras y metodología persistidas aquí. Root consolidará MTMslow, ledger y conclusionesdecartera.

## Decisión de continuación
Cerrar ambas familias probadas sin promoción. No mover ventanas/medias/lados ni añadir indicadores para rescatar. No hay candidataSPY que justifique abrir2026, MonteCarlo o integracióncompartida ahora.

Pregunta concreta para futura línea: ¿existe un tipo de evento de precio o estado observable exante, diferente de apertura/RSIMR/rupturamacro yaarchivados, con movimiento condicional suficientemente grande para superar9bpsRT? Antes de otro full debe formular trigger, reloj y control económico, y cotejar historial. Para una propuesta beta, comparar explícitamente retorno/riesgo/capital-tiempo frente a beta protegida; llamarla asignación y exposición, no nuevaalpha. Ninguna nueva fuente ni funding son requisito impuesto por este informe.