# CROSS_P archivada — protocolo de evaluación bajo contrato actual

Fecha local: 2026-10-22. Estado: diseño normativo para revisión de root antes de fuente nueva. Decisión de root: UN motor; se retira la posibilidadCLOCK_ONLY del documento de propuesta previo antes de toda implementación o economía. Sin nuevos precios, datos, jobs, drafts o motores. CODES acotado acompaña fuente congelada y snapshot descriptivo.

## Pregunta y oportunidad pendiente

¿La receta CROSS_P ya elegible en su screening, con entrada y salida por cruces opuestos20/80 y gestión congelada, acredita una operativa individual viable bajo la cuota y medición actuales en la trayectoria completa2020–25?

No es un nuevo indicador ni una ablación para fabricar slots. CardCROSS_P, FROZEN_SHORTLIST_V5.md y FINAL_DECISION_V5.md acreditan que quedó tercera por rankingDD/cupo2, no que falló una confirmación2024–25: esa fase no se ejecutó para CROSS. No cambiar retrospectivamente el rankingV5 después de ver las pérdidas deFunding.

[Referencia archivada descriptiva](http://localhost:9200/#/backtest/50827027-6d6f-4c5d-8c23-5f2f91d7d971):77trades, neto9052.918199USDT/+90.5292% del período, CAGR21.329231%, PF1.7118 y DD diarioframework17.695540%. Ventana2020-09-01→2024-01-01. No alcanza por sí solaCAGR30/N100 actuales y no tieneDDM1/cortesR11 exigidos hoy. Snapshot summary nativo íntegro preservado, sin reauditación nueva de sus77trades.

Selección actual adaptativa y anunciada después de leer el historial. La ventana extendida2024–25 ya fue observada en muchas otras líneas; NO esOOS/holdout ni confirmación ciega, y no se llama walk-forward a un único replay continuo.

## Reglas de señal exactas e invariantes

Sólo BTC-USDT4hUTC cerrado. BAR=14400000ms. T múltiplo deBAR; usar81OHLC consecutivos, última aperturaT−BAR y todasopen+BAR<=T, finitas/positivas/coherentes. No interpolar, rellenar gaps o leer velas nuevas. En ruta ejecutora1m, get_candles(exchange,"BTC-USDT","4h") alimenta el helper causal congelado, nunca self.candlesM1 como sustituto.

Reutilizar literalmente cross_state de strategies/ResearchV5Base4h/cross_features.py, SHA2565df66fdb107fe3f16484ee5cd1ca91c121c4c8bea0095e3fd95799a354f5e1e0. Calcula:
F0=SMA20(C0..C19),F1=SMA20(C1..C20);
S0=SMA80(C0..C79),S1=SMA80(C1..C80).
Su media usa math.fsum de valores escalados porn para evitar overflow; no sustituir porEMA, npmean o suma distinta. Actual incluye su propia barra cerrada; previa termina una antes.
Long F1<=S1 yF0>S0; short F1>=S1 yF0<S0; en igualdad actual o ausencia de cruce,0. Sin bandaepsilon/SMA200/pendiente/régimen/ADX/RSI/volumen/OI/funding económico.

Before en cadaM1 conserva _observe("pre")R11 exactamente una vez y limpia dirección de entrada. Sólo cadaT4h calcula el cruce, lo registra/consume aun ocupado; no cola o latch que reintente el estado. El mismoT repetido no duplica conteos/plan y un reloj retrospectivo no rearma. START=1602720000000,FINISH=1767225600000,guardSTART<T<FINISH. Los datos previos calentados no generan órdenes ni reinician cuenta al empezar2024.

Entradas MARKET a exactamentefloat(self.price), plano/sin pending/sin last_exit_at=T, máximoUNA apertura efectiva por díaUTC compartida longshort. La cuota se consume en on_open, no en un cruce bloqueado por ocupado o sizing. Si se liquida por seguridad tras apertura inválida, esa apertura también consume cuota. La cuota diaria se reinicia naturalmente al cambiarUTCday, no por lado, cierre o frontera mensual. No trade de selección a otroTsin cruce fresco.

Comprobar paridad de close4h causal con self.priceM1 rel1e−10/abs1e−8 ANTES de admisión. Mismatch es bloqueo técnico visible/assert, no señal neutral rentable ni sustitución de datos. ATR y exit siguen sus propias validaciones: faltaATR no debe desactivar un cruce de salida válido.

## Gestión congelada, no búsqueda de plazos o ganancias

ATR14 SIMPLE sobre15OHLC4h cerrados actuales, offset0, media14TR; usar atr_window de ResearchV5Base4h congelada. DistanciaD=3ATR conocida en la decisión y conservada desde fill. No2ATR deR32. Stop=fill−sD, finito/positivo, sin recalcularD ni moverstop después. SinTP, trailing, BE, parcial o scaleout.

Salida de long al aparecer cruce short; salida de short al aparecer cruce long. Misma función20/80 y reglas de igualdad. SóloT4h>opened_at. Usa81cierres válidos/asof, no ATR actual u OI; si faltan81 no reconstruir un cruce perdido desde el mero estado, y mantener SL/plazo. Si el precio no coincideasof no calcular un exit de otra serie silenciosamente.

Límite absoluto180BAR=720h=30d desde opened_at. Salida MARKET en primerT4h cuya edad>=720h aun si indicadores/datos actuales inválidos. No prueba27/33d,24/48h o plazos elegidos porretorno. Preservar prioridad nativaSLintrabar; en decisiónFINISH/cierreterminal, luego plazo y luego cruce opuesto. No evaluar el close anterior alfill como salida del mismoT.

NO stop-and-reverse: el cruce que cierra se consume, no abre contrario enTni se difiere aT+1. Próxima entrada requiere nuevo cruce estando plano y cuota diaria libre. Ni stop ni plazo crean reentradas automáticas por estado. Salida terminal incluye fees/funding y no se descarta para mejorar métricas. Counter total_open_trades nativo refleja posición antes de cierre forzado; verificar órdenes/trade/PNL postfee y PRE/FINAL, sin exigir artificialmente0enesecontador.

## Sizing actual con techo original1x conservado

Cuenta alternativa BTCtotal10000, cuota de riesgo activa1%, otra cuota ociosa, sin redistribución;6%global,3xaislado. Llamar legacy_plan(event,.5*max(0,wallet),.5*available_margin,3,fee), conentry actual, direction s,D=3ATR,target_distance=None,hold_hours720,order_kindMARKET. Reserva.001 sólo sizing, lote.001floor y buffer90% sobre media cuota de margen permanecen.

Se conserva además el techo nocional1x originalV5 como restricción adicional de exposición: Ccap=available_margin TOTAL capturado flat/sin pending antes de orden; qcap=floor((Ccap/entry)/.001)*.001; qfinal=min(qhelper,qcap). Calcularfloor sólo paraqcap, no volver a redondearqhelper ya flooreada y perder un lote por idempotencia flotante. Siqfinal<=0, cash. No grilla entre cap1x y caphelper; ésta es la única exposición propuesta.

Recalcular campos planned_loss=qfinal*(D+fee*(entry+stop)+.001entry) yplanned_stop_fees=qfinal*(D+fee*(entry+stop)); qtyfinal mantiene presupuestohelper y no lo aumenta. Conservar helper original inmutable; añadir cap_1x_limited,helper_qty,cap_qty/capitalcap y ratio real en logs. Guardar capital/margen total y escalado para verificar no subcuenta5000. En fill auditar qty/precio/pérdida con reserva<=riskbudget, protección válida y cuotaUTC. Si se requiere manejar una excepción técnica, guardar el trade/costo y detener interpretación económica hasta resolverla, sin redimensionar retrospectivamente.

V5 sizing era .02*Ccap con cap1x/floor8 y sinreserva. Ahora1%total víahelperhalf y lote.001/reserva .001, manteniendo cap1x. No es dividirpor2 la curva antigua ni el mismo contrato económico. Cambian cantidades, capitalización y eventualmente selección por lotes; no atribuir deltas contra archivo a efecto puro de gestión.

## Arquitectura aislada propuesta

Nueva base pequeña heredada directamente de BtcResearchR11Base1m, con helperlegacy_plan congelado y cross_state/atr_window congelados. R32 queda intacta: su contrato64filas/2ATR/24–48h no admite81filas/3ATR/720h; no agregar excepciones allí. No heredar señales K, suplemento, accesoOI o calendariosWF del viejoV5base; importar sólo helpers puros que ya existen no implica instanciar su estrategia.

Antes de escribir fuente, root revisará este protocolo y CODES. Posteriormente fuente nueva y readback/hash/checkprovidedsource con stubs, no imports reales de estrategia/framework dentroanálisis. Verificar paridad dehelperllamado con el literal capturado,81cierres/igualdades, cuota porfillUTC, consumo ocupado, noreverse, salida sinATR, gestión720h pese invalidwindow y riesgo/cap/lote. Los mocks no certifican broker, funding o ramas no ejercidas por nativo.

## Contrato y mediciones

Binance Perpetual Futures BTC-USDT, ruta1m+data4h, warmup2404h predeclarado comoV5 (no recorte por sólo81);UTC[2020-10-15,2026-01-01). Una cuenta continua, sin resets o semestrescalendarioOFF/forzados intermedios.10000,3xaislado,fee.00045taker descontada porlado;fundinghistóricoON snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxies explícitos;slippage modelado0. FundingYAestabaONenV5, no nueva feature. OI desactivado porque CROSS_P no lo exige; no importar/consultar datasets nuevos ni cobertura previa.

R11M1+fills equitywallet+PnLabierto raw y fronteras postfunding/predecisión. Todos62mesescompletos/20Q esperados según ventana, incluyendoinactivos, sin fabricarlos si faltan; DDdiario separado deDDM1. No MFE/MAE intraminuto ni retornos de subcuenta. Años2021–25 y51ventanas12m descriptivas/solapadas, no OOS ni51réplicas.

Gatesr9 sinrelajar:CAGRnet>=30%,PFnetUSDT>=1.2,DDM1+fills<=25%(objetivo20),Mactivos>=65%,Q>=80%,medianacalendario>0,netoaritmético sin2mejoresmeses>0,N>=100preliminar/no potencia. Reportar metas/denominadores íntegros, no elegirlado nipromoverpor retorno relativo alarchivo. Negativo o muestra insuficiente cierra esta evaluación actual, no rescate por riesgo,medias,stop,plazo,cap,reverse o nuevofiltro.

Instrumentación neutral R34, cada línea<1800caracteres y sin logsM1:
- R34_PLAN: time,label,direction,entry,qty,distance,risk_budget,planned_loss,planned_stop_fees,meta,cap_1x_limited. Meta compacta conserva F0/F1/S0/S1, timestamp/hash81, ATR, capital/margen total/escalado y helper_qty/cap_qty, sin pegar81filas.
- R34_OPEN: time,signal_at,opened_at,label,direction,entry,qty,distance,risk_budget,stop,target_distance=null,hold_hours=720.
- R34_CLOSE: time,label,net,reason. Usar pricecross/hold/terminal sólo cuando esté acreditada la causa; SL mediante orden nativa. No adivinar el motivo por tipoMARKET, ni llamar terminal a cualquier cierre próximo al final.
- R34_SUMMARY: stage,label,opens,closes,long_opens,short_opens,net,events,plans,occupied,rejected_geometry,risk_total=.01,capital_denominator="total BTC wallet",redistribution=false,hold_hours=720,tp_r=null. Contadores de cupo diario y cap/margen se documentan en filas aparte o meta acotada, sin alterar schema.
Registrar el cruce de salida y motivo ANTES de liquidate; actualizar ledger antes de super.on_close_position porque R11 puede emitirFINAL. Preservar causa en caso de cierre forzado mediante before_terminate observacional, sin inventar callbackFINAL ni exigir total_open_trades0. Semántica nativa _terminate ya auditada por root.
Eventos brutos/consumo y rechazos ocupado/pending/cupo/sameexit/ATR/sizing deben tener denominadores explícitos; no sumar flags solapados como operaciones. Extracción paginada completa.

Auditoría nativa reconciliagross−fees+funding=PNL=saldo−10000 con tolerancia1e−6;pagos completos/asof/proxies ycampofundingausente sólo0verificado;MARKETreal/clocks/precio/cantidad/SL/30d/cuota;terminalyR11totales. No afirmar paridad económica deloldscreen desde helpers/stubs o restaurar fills antiguos manualmente.

## Presupuesto y cierres

UN motor económico máximo, control viejo sólo descriptivo reutilizado. Cero segundoSL-only/CLOCK_ONLY, vecinos,smokeeconómicooculto o reemplazoautomático. Cualquier fallo técnico conserva evidencia y vuelvearoot; unmalresultado noautorizaotroID. Concurrenciaglobalmáximo2motores+1analysis coordinado; esta documentación ocupa0slots.

Secuencia: revisiónroot/independiente→fuenteaislada/checksintético autorizado→revisiónfuente/recibo→draftgenuino/manifiesto/config/funding/snapshots→únicomotor→auditoría/decisión/cierre. No cambiosframework/R32/otros padres/configglobal,install/restarts,research_scripts,datasetsnuevos,2026nuevo,USDC,estrés,riesgogrids,cartera,live/paper/Pi.

El protocolo no hereda las fases de40slots/vecinos deV5. Sus reglas/checks/selección originales quedan conservados; nueva autorización tiene presupuesto1ycontratoactual explícitos.
