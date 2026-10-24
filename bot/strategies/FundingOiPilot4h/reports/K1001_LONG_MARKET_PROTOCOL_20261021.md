# K1001 LONG_ONLY: contraste nativo MARKET frente a LIMIT

Fecha documental: 2026-10-21. Estado: protocolo y anexo CODES para revisión de root e independiente, antes de nuevas fuentes. No implementación, drafts, jobs ni motores desde esta tarea.

## Pregunta y alcance

¿La política de comprar inmediatamente al cierre de decisión, conservando TODA la señal long original K1001 y su gestión, mejora de forma defendible la trayectoria de LONG_ONLY frente a esperar el retesteo mediante LIMIT?

Es una ablación de política de entrada de K, no una nueva familia. Existe autorización de continuidad material tras el diagnóstico y los dos escenarios cerrados. Se conoce ese histórico: selección adaptativa declarada, sin OOS nuevo. No se presenta la ausencia de un contraste exactamente equivalente como invención del breakout a mercado.

Control reutilizado, sin nuevo motor: [LONG_ONLY LIMIT congelado](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c), BtcResearchR16K1001LongOnly1m. Tratamiento propuesto: BtcResearchR16K1001LongMarket1m, heredado de ese LongOnly. Presupuesto futuro exactamente UN nuevo ID económico, sin nueva réplica de control ni segundo escenario MARKET.

## Motivación y explicación rival

La señal actual exige que el close haya superado el máximo previo y permanezca como máximo a un ATR de él, pero compra sólo si el precio regresa al nivel. Comprar ahora puede acceder a continuaciones que no retestean, a cambio de un precio mayor y exposición inmediata. Puede también incorporar más falsos breakouts y empeorar capitalización, costos y ocupación; el retesteo puede ser una selección beneficiosa.

El control tuvo 45 planes admitidos, 31 fills y 14 cancelaciones. No son todas las señales raw. Las 14 cancelaciones forman 13 grupos cronológicos bajo una agrupación descriptiva; no son muestras independientes ni retornos desconocidos que puedan contarse como ganancia potencial. Tampoco 45 es techo de trades MARKET: cambiar ocupación cambia la secuencia posterior.

El control mantuvo las mismas 31 trayectorias long del K original; el deterioro reciente se acompañó de menor recorrido favorable observado. No demuestra que una entrada MARKET lo resuelva. No ajustar trailing desde máximos posteriores ni suponer que recuperar no-fills compensa pagar más por los fills comunes.

## Transformación exacta: validar primero, reemplazar después

La nueva clase conserva GROUP=LONG_ONLY y MODE=K1001 heredados. Su _prepare_entry mantiene las guardas, memo, registro de plan y secuencia del LongOnly actual. No llama super._prepare_entry para preparar primero una LIMIT ni monkeypatchea legacy_long.

1. Sólo en T4h con decision_at=T, plano, sin entry_orders, sin last_exit_at=T y START<T<FINISH. prepared_at memo como el control; rows=None retorna cash y no usa eventos antiguos.
2. Invocar legacy_long(rows) congelado, completo y sin cambiar su código. Si retorna None, no hay entrada ni fallback.
3. El helper original debe haber validado len>=100; EMA20/80 y pendiente; ADX>=26; RSI14 entre52 y76; ATR14 real positivo; rango actual<=3ATR; máximo previo H=max(high de26 barras anteriores); H<close<=H+ATR; distance=2ATR y 0<distance<H. Se conservan incluso las guardas de distancia respecto al trigger original, aunque al nuevo precio pudieran ser menos restrictivas. No retirar el límite superior de extensión, sustituir H o adelantar la señal.
4. Sólo después de un evento original válido, crear una copia local del dict: entry=float(self.price), order_kind=MARKET. Conservar origin LONG_RUNNER, direction=1, distance original, target_distance=None y hold_hours=None. No mutar el dict de un padre o helper. Registrar el trigger H del evento original por separado, como evidencia, no como nuevo stop.
5. Recalcular legacy_plan sobre el evento MARKET con .5*max(0,balance) y .5*available_margin, leverage3 y fee real. No reciclar qty o riesgo del plan LIMIT; cambian entry y sus costos de sizing. Si helper rechaza, cash, sin convertir a LIMIT ni reducir distancia para forzar admisión.
6. Guardar plan real con signal_at=T, expiry=T+BAR, direction y signals exactamente como el control. Expiry se conserva por contrato/lifecycle aunque MARKET se ejecute inmediatamente; no existe espera artificial hasta expiry. Log de política y trigger original una vez por plan seleccionado, sin contar llamadas memo como oportunidades nuevas.

before R16 ya filtra exclusivamente barras4h cerradas y contrasta close4h con self.price. Para la orden usar exactamente float(self.price), no otro close aproximado: _submit heredado establece buy=(qty,entry) y el runtime nativo reconoce el precio actual como MARKET. El campo order_kind sólo documenta el plan y no sustituye al broker. No cambiar _submit, go_long, broker, timestamps ni precio de fill manualmente. Auditar que la orden realmente ejecutada sea MARKET al precio de decisión de este runtime, sin next-open futuro ni fill retrospectivo dentro de la vela que acaba de cerrar. Si el runtime no satisface esta semántica, bloqueo técnico; no cambiar silenciosamente a otra ejecución.

## Riesgo, capital y costos idénticos al control

Cada política tiene una trayectoria alternativa de UNA cuenta BTC total inicial10.000 USDT y sólo cuota1% activa. No subcuenta de5.000 ni dos cuentas financiadas simultáneamente; no sumar o compoundear resultados.

Se conserva legacy_plan(.5*wallet,.5*available_margin,3,fee): presupuesto .02*.5*wallet=.01*wallet total cuando flat, equivalente entonces a equity total. Margen efectivo<=45% del available_margin por el buffer90% heredado. Lote .001 con floor, reserva .001 sólo sizing, techo nocional y todas las guardas originales. No redistribuir la cuota inactiva, quitar reserva, subir riesgo o escalar resultados a2%. El contrato global6% permanece; una sola posición objetivo1% no acredita un libro conjunto2% ni garantiza pérdida máxima ante gaps/funding.

Contrato clonado del formulario genuino del control: BTC-USDT, Binance Perpetual Futures, ruta1m y data4h, UTC[2020-10-15,2026-01-01),warmup240,10.000,3x aislado, taker .00045 por lado, funding histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 y proxies declarados, slippage modelado0, fast_mode=false, debug/logging/export del control. Sólo cambia strategy y metadatos de identificación del nuevo escenario. No velas nuevas, precheck de cobertura, importaciones, 2026 nuevo, estrés, otros activos, USDC, ML, instalaciones o cambios globales/live/paper/Pi.

## Gestión y observación congeladas

Toda la cadena LongOnly→QuotaBase→R16K→R16Base→R11 permanece intacta. Máquina suplemento sigue avanzando aunque no opere; ninguna nueva señal short. Stops desde fill real: E−distance, distance2ATR de señal original; sin TP ni plazo. Runner y BE/trailing se aplican literalmente en cierres4h estrictamente posteriores al fill, jamás en el mismo T usando el close que generó la entrada. Mantener best_close inicial=E y los ajustes heredados de5R/8R, sin modificar umbrales.

Una posición, sin pirámide, cola, scaleout o reentrada en el timestamp de cierre. Los hooks de apertura/cierre/terminal y contabilidad R11 son heredados. No reemplazar ATR Wilder por simple ni recortar historia EMA; todas las llamadas y retención P/control se conservan.

Rprecio hereda exactamente el observador ya auditado: open0; pre sólo now>opened_at; exitfill real y fases distintas aun holding0; empates conservan primera ocurrencia. No es MFE/MAE intraminuto ni máximo ejecutable. Ledger real por origen/año y trace se mantienen; no episodios o órdenes virtuales.

Instrumentación nueva mínima: entry_policy=MARKET_AT_DECISION_CLOSE, original_trigger_level=H, decision_price, original_distance, T, requested_entry y qty/risk_budget del nuevo plan. Los logs parent siguen intactos. Para resolver el recorte real del lector, la nueva clase añade un override _emit sólo observacional: llama super()._emit(stage) EXACTAMENTE UNA vez y después emite filas completas de longitud <1900 caracteres: K1001_MARKET_SUMMARY(stage,policy,trace_errors,open_trace); K1001_MARKET_SOURCE(stage,origin,**row) por cada origen; K1001_MARKET_COHORT(stage,axis=open_years/close_years,year,origin,**row) por cada cohorte existente. Usa estado propio heredado ya actualizado, sin recomputar trades ni modificar contadores. PRETERMINAL/FINAL son snapshots con stage, no sumandos. Comprobar formato/longitud desde synthetics y readbacks. La fila vieja K1001_QUOTA_STATS seguirá heredada y podría recortarse; no tocar el padre, inferir su sufijo ni rerun por ello. Las nuevas filas completas son evidencia redundante paginable, conciliada con trades/pagos, no lógica económica. No logs M1.

## Controles, deduplicación y restricciones de cierre

El anexo CODES conserva las fuentes completas y el informe K1001_LONG_MARKET_DEDUP_AND_VOI_20261021.md, leído íntegro y con readback SHA256 efa037ec85c24ac292cc9203194e23aefe7a75e1abe10a76385f1b80055bb0c8. Antecedentes muy próximos:
- BtcMomentumCore4h/Baseline3 ya compran Donchian a mercado, pero difieren en extensión máxima, stop/floor, BE/gestión y contrato. No son el mismo experimento K1%.
- TrendBreakout5m ya estudió MARKET frente a retesteo con otro reloj, señal y gestión. No se redescubre su pregunta genérica. Las cifras de neto citadas en comentarios ancestrales son afirmaciones del código, no resultados pareados reauditados ni evidencia económica actual.
- Preposicionar Donchian STOP, reclaim M1, R14 filtroslong y otras recetas modifican disparador o gestión; no se trasladan sus resultados como control exacto.
- P/U/cuotas conservaron la política long original. Sus negativos y cierres siguen vigentes. La excepción actual permite sólo esta ablación de ejecución solicitada/aprobada, no vecinos de riesgo, filtro, TTL o trailing.

No afirmar búsqueda exhaustiva global ni equivalencia numérica con Core/Baseline. No vuelve a ejecutarse una política equivalente por nombre nuevo. Si revisión encuentra un experimento exactamente equivalente con fuentes/contrato acreditados, reutilizarlo y no gastar el ID.

## Evaluación prefijada y decisión

Auditar ambas trayectorias completas, control archivado y MARKET nativo nuevo, incluyendo nueva selección, precio, exposición, tamaños y capitalización. El contraste define una diferencia de política a nivel de cuenta, pero los trades comunes no son pares aleatorios ni permite asignar PnL MARKET a las14 órdenes canceladas de LIMIT. No condicionar el análisis a los fills que coincidan ni asumir que ocupación permanece igual.

Reportar N, bruto, fees, funding, neto/final, CAGR sobre10.000, PFneto USDT y porR separados, DD M1+fills, calendario completo/activo, trimestres, mediana y concentración. Reconciliar gross−fees+funding=sumPNL=final−10.000 con tolerancia<1e−6 en sumas. Funding ausente en snapshot sólo puede ser0 si ledger completo acredita ausencia de pagos. Verificar terminal flat y resumenFINALpostfee si procede, trazas completas unidas a fills y ledger de origen. Recuperar todo por páginas/exports acotados y hashes, nunca datos truncados.

Gates r9 sin relajar: CAGR neto>=30%, PF>=1.2, DD M1+fills<=25%(objetivo20%), meses completos activos positivos>=65%, trimestres completos positivos>=80%, mediana mensual calendario>0 incluyendo inactivos, neto aritmético sin dos mejores meses>0; N>=100 mínimo operativo preliminar, no potencia/confianza. Años2021–25 y51 ventanas12m son descriptivos solapados, no OOS ni filtros posteriores. Mantener aspiraciones40–50%+/M70 aparte.

Control LIMIT conocido:31trades,CAGR6.7078977%,PF3.5519634,DD8.4730045%,M13/28,Q8/20,mediana0; NO_CUMPLE. Reportar diferencias continuas de retorno, riesgo y regularidad sin inventar un cutoff ex post. Mejorar una métrica relativa no sustituye objetivo absoluto ni demuestra edge. No se define un puntaje o umbral nuevo de «mejora material» después del resultado: si falla una puerta económica, conserva NO_CUMPLE; si hay intercambio de métricas, se informa completo y no se declara dominancia. Reportar suficiencia separada: N<100 es muestra operativa insuficiente y no prueba una pérdida económica; si además falla CAGR u otra puerta, registrar ambos hechos. Un resultado favorable sin medición completa es INCONCLUSO, no aprobado. Candidatura exige gates r9 y suficiencia, sin autorización de operar.

Al cerrar este único contraste, no rescatar mediante offsets, caducidades, extensión distinta, reclaim, filtros, lados, cuota, stops, TP, BE/trailing o plazo. La exposición adaptativa del histórico y los antecedentes negativos permanecen declarados. Cualquier pregunta posterior requiere materialidad propia; no repetir esta búsqueda por decepción.

## Secuencia y presupuesto técnico

Ahora sólo docs. Después de revisión root e independiente, autorización separada de implementación de una fuente nueva propuesta. Readback completo/hash, sin editar padre. Checks sintéticos supplied-source/AST/stubs coordinados en máximo1analysisglobal: predicados originales falsos/bordes siguen falsos antes del clone; límite extensión preservado; dict original inmutable; MARKET entry=self.price exacto; distance igual; qty rehecha por helper.5/.5; guardas/memo/rowsNone/sameexit; gestión/observer heredados y no monkeypatch; _emit nuevo llama super una vez, produce summary/source/cohort <1900 caracteres sin cambiar estado económico y sin duplicar stages. No imports de estrategias reales, datos observados o backtest anidado. Los stubs no certifican por sí solos semántica del broker real; ésta debe contrastarse con framework ya auditado y órdenes del motor.

Tras fuente/check/reviews conformes, root crea un draft genuino y manifiesto con formulario, funding, fuentes/runtime/control reutilizado antes de ejecutar. Presupuesto económico exactamente1IDnuevo; ningún reemplazo automático por error o mal resultado. Fallos técnicos documentados vuelven a root. No hay segundo motor observacional de cancelaciones ni recálculo nuevo del control.

## Precisión normativa posterior antes del único motor: política nominal y tipos nativos

La auditoría estática root del framework y las órdenes completas de las cuotas verifican que Strategy clasifica primero mediante helpers.is_price_near: tolerancia fraccional.00015=0.015%. Por ello, el control LONG_ONLY es una POLÍTICA LIMIT con conversión nativa por cercanía:27entradasLIMIT y4MARKET reales, no31LIMIT estrictas. SHORT_BOOK tiene171STOP+1MARKET. Se conservan fuentes, resultados, comisiones taker y geometría; no es fallo financiero ni motivo de repetir motores. Esta precisión gobierna cualquier frase anterior que pudiera entenderse como espera de retesteo estricta en todos los fills.

Nueva MARKET: precio exacto self.price, por lo que el runtime debe crear todas las entradas como MARKET. La revisión estática/read-only precede al único motor; verificar sus órdenes reales DESPUÉS de ese motor, nunca mediante un preflight económico adicional. order_kind documenta intención y no demuestra ejecución. Preservar este control nativo como contrafactual completo; no forzar ahora27/4 a31LIMIT ni modificar el helper, broker o fuentes frozen.

Evidencia primaria con órdenes, OPENlogs, proporciones trigger/entry y hashes de siete archivos framework: strategies/FundingOiPilot4h/reports/K1001_LONG_MARKET_FRAMEWORK_AND_ENTRY_TYPES_20261021.json y Markdown homónimo. Mercado Sandbox usa current_price del cierreM1 y cola procesada después de estrategia en el mismo paso; self.price cacheado, slippage default0 confirmado en perfil. Prueba estática no es certificación de los futuros fills ni de ejecución real de exchange.
