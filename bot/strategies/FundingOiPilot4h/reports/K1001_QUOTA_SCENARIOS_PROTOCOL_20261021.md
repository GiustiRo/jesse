# K1001: dos escenarios nativos originales con cuota BTC de1%

Fecha documental2026-10-21. Estado: PROTOCOLO Y FUENTES para revisión root. Cero implementación, drafts, motores o jobs autorizados por este documento. El diagnóstico existente está completo; el medidor de ocupación queda HOLD, sin wrapper creada ni jobs. No se borra su propuesta ni su revisión.

## Pregunta humana y alcance

¿Cómo se comportan las reglas originales de K1001 cuando sólo LONG_RUNNER está habilitado, o cuando sólo el libro CORE_SHORT→SUPPLEMENT está habilitado, cada escenario con cuota1% del capital BTC total de su propia trayectoria? Son dos contrafactuales nativos de selección y sizing. No son nuevas señales, réplica de192 trades ni prueba causal de que quitar competencia mejore el resultado.

La motivación es evaluar la división propuesta por el usuario después de entender el libro original. La elección es adaptativa y conoce el diagnóstico previo; no es OOS ni confirmación independiente. No se escoge sólo suplemento por su PF ni se elimina core por menor aporte. Se conservan long original y TODO el libro short original, sin filtros nuevos.

Nombres previstos, todavía NO creados:
- BtcResearchR16K1001QuotaBase1m: base común derivada de BtcResearchR16LegacyK1001m.
- BtcResearchR16K1001LongOnly1m: escenario LONG_ONLY.
- BtcResearchR16K1001ShortBook1m: escenario SHORT_BOOK.

## Denominador y cuota: definición normativa

Cada escenario comienza con UNA cuenta total BTC de10000USDT. En esa cuenta sólo su grupo está habilitado; la otra cuota permanece inactiva. Son alternativas, no dos cuentas financiadas simultáneamente ni una simulación de posiciones hedge. Toda fee, funding y ganancia/pérdida actualiza el wallet total propio de ese escenario. Los siguientes tamaños se calculan sobre su trayectoria propia, que puede divergir desde el primer trade.

La preparación sólo ocurre flat, cuando balance=equity de la cuenta total. Aplicar exactamente el helper congelado:
legacy_plan(event, .5*max(0.0,float(self.balance)), .5*float(self.available_margin), float(self.leverage), float(self.fee_rate)).
El .02 interno del helper multiplicado por .5*balance fija risk_budget=.01*balance total. No se inicializa una cuenta de5000 ni se aplica1% a5000; no se permite2% deltotal al único grupo activo. El saldo no invertido no genera rendimiento nuevo.

La mitad de available_margin es cuota fija sin redistribución: con el buffer90% heredado, margen de la orden<=45% del margen disponible total, con fees según fórmula original. La leverage nativa sigue3x; el helper conserva su techo nocional4.4*(.5*balance)=2.2*balance, normalmente no vinculante frente al techo de margen1.35*available_margin/(1+fee*3). No explorar límites ni quitarlos. Lote.001 y floor pueden impedir que qty sea exactamente la mitad de la referencia; no redondear hacia arriba. RESERVE=.001 es reserva de sizing, no cargo ni slippage.

El límite global6% permanece como contrato de admisión; con una sola posición objetivo1% no vincula por sí mismo. Stops/gaps/funding no garantizan pérdida máxima1%. El escenario aislado no demuestra cumplimiento de un libro conjunto2% ni financiación/margen/capital simultáneo. NO sumar curvas, multiplicar retornos o compoundear las dos trayectorias. Una combinación conjunta sería otra pregunta, todavía sin motor.

## Reglas y ciclo exactos

Heredar R16K1001/R16Base, MODE K1001 intacto. No tocar fuentes parent, framework, indicadores o configuración global. before del padre se ejecuta literalmente: misma historia creciente4h/P, ta.atr Wilder real con semántica escalar existente, EMA secuencial completa; no cambiar a ATR simple ni truncar. La máquina del suplemento avanza siempre, incluso en LONG_ONLY, ocupado o pendiente, sin política de estado por órdenes.

Única sustitución económica: _prepare_entry conserva literalmente guardas de T4h, decision_at==T, flat, ausencia de entry_orders, last_exit_at!=T, START<T<FINISH; memo prepared_at==T y su retorno. Tras fijar prepared_at, si rows=None retorna0. LONG_ONLY considera exclusivamente legacy_long(rows). SHORT_BOOK considera legacy_short(rows) y luego supplement_event original. Cada candidato se pasa al helper escalado anterior; primer plan viable gana, incluso si core tenía geometría pero no qty. No llamar super._prepare_entry porque seleccionaría ramas excluidas. Conservar plan=dict(plan,signal_at=T,expiry=T+BAR),direction,signals y retorno como el padre. No recomputar suplemento ni alterar previous_setup. Un supplement_event antiguo tras rows=None NO puede usarse.

Se heredan literalmente _submit/go_long/go_short, should_*, should_cancel_entry y TTL4h, on_open_position y protecciones relativas al fillreal, update_position, callbacks de cierre y R11. Ninguna entrada retrospectiva, cola, reentrada en timestamp de cierre, pirámide o scaleout. Framework puede cancelar vencida y reevaluar en el mismoT con margen liberado, memo único; fill del minuto expiry se procesa antes conforme runtime auditado P.

LONG_RUNNER: condición/entry LIMIT26/EMA20,80/ADX26/RSI52–76; stop2ATR; BE2.25R y trailing4.2ATR con ajustes heredados5/8R; sinTP/plazo. CORE_SHORT: EMA120ascendente,RSI3<=20,STOP estructural; stop a distancia EMA20−entry,TP1.5ATR,primerT4h>=fill+72h. SUPPLEMENT: cohorteVWAP/eficiencia<=1/3,K1001 STOP,min(s.low,t.low),latchoriginal; SL1R/TP2R,primerT4h>=fill+48h. Todos los predicados, guardas y distancias son los helpers completos del anexo, sin parámetros nuevos. Este resumen no reemplaza la fuente.

## Contrato y datos

Copiar formulario P del anexo cambiando sólo strategy y metadatos de escenario: Binance Perpetual Futures BTC-USDT, ruta1m y data4h, UTC[2020-10-15,2026-01-01),warmup240,10000,aislado3x,fee.00045porlado takercon descuento,funding históricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxies declarados,slippage0,fastfalse,logging/debugP. El cambio1% está en el helper aplicado algrupo, no en formulario global. No datasets/imports/cobertura previa/2026nuevo/estrés/USDC/otrosactivos/livepaper/Pi/reinicios/instalaciones/ML.

## Instrumentación mínima del libro REAL

Estado nuevo sólo bajo namespace propio. Sin episodios ni registros de todos los candidatos4h. Logs parent R16_LEGACY_OPEN/CLOSE/STATS y R11 quedan intactos. Añadir log de configuración de escenario/cuota; al seleccionar planreal, registrar T/origen/qty/risk_budget/capitaltotal/capitalscaled/margentotal/margenscaled/planned_loss/planned_stop_fees/reserve/gross_limited/margin_limited/expiry. No planflat virtual.

Un ledger propio de ejecuciones/cierres por origen y añoUTC del evento real, conciliable con trades; distinguir año de apertura y de cierre, nunca llamar retornos MTM a sus cohortes. Guardar fills reales E/qty/stop/distancia/target,signal_at/opened_at/closed_at,neto y orden de salida. Fees/funding finales provienen del ledger del motor, no estimaciones de señales.

Rprecio observado obligatorio en ambas wrappers mediante la misma base común pequeña: _observe llama al padre una sola vez y devuelve su valor intacto. Estado diagnóstico puede inicializarse desde open antes del primer before. Open crea marca0 con identidad propia. Pre sólo añade direction*(closeM1−E)/distance cuando now>opened_at y posición/registro corresponden. Antes de super.on_close_position se añade exitfill real y se finaliza, porque padre limpia position_plan y puede emitirFINAL. Trades con holding0 se conservan con open0 y exitfill mismoT; dedup por(trade,stage,T), nunca porT solo. Extremos se actualizan estrictamente y conservan primer empate. Registrar min/max/primeras fases y timestamps,conteoM1,primera/última marca y resumen portrade; resumen anual de conteos/traces completados/faltantes por año de apertura/cierre. No logs por cadaM1.

Rprecio excluye fees/funding y no es MFE/MAE intraminuto ni potencial después de salir. No selector de entrada/salida ni permiso para cambiar trailing. Toda instrumentación observacional termina antes de una emisiónFINAL, sin duplicar ledger ni incrementar contadoresparent. Datos nofinitos/identidad rota producen evidencia de fallo técnico deltrace; no reparar prices ni modificar decisiones.

## Medición y aceptación económica prefijadas

Cada escenario reporta SU cuenta total de10000 con cuota1%; no normalizar a capital5000 ni anualizar a2%. R11 equity=wallet+openPnL,DDM1+fills y fronterasUTCpostfunding/predecisión; terminalFINALpostfee si hay liquidación posterior. Auditar rawopen/equityfinal/fee/funding proxies/ledger completo, gross−fees+funding=net=sumPNL=equityfinal−10000,tolerancia<1e−6en sumas. Recuperar todos logs/trades/pagos por páginas completas; manifest/hash y transporte sin truncamiento.

Reportar CAGRneto>=30%,PF>=1.2,DDM1+eventos<=25%(objetivo20%),mesescompletosACTIVOSpositivos>=65%,trimestrescompletospositivos>=80%,mediana retornomensual CALENDARIO>0coninactivos,neto aritmético sin2mejores meses>0,N>=100preliminar operativo(no potencia). Aspiración40–50%+/M70 no sustituye gates. Cohortes, años2021–25 y51ventanas12m se describen, no nuevos filtros. Si muestra menor, separar insuficiencia de evidencia de falloeconómico; no cambiar mínimos, excluir meses ni subircuota para aprobar. No se relajan gates porque sólo está activa media cuota.

Comparar con Koriginal sólo como referencia: selección/identidad de trades comunes/nuevos,Rprecio/neta y perfiles; sin exigir192ni cantidadesiguales ni atribuir diferencias exclusivamente a competencia, pues cuota y trayectoria de capital también cambian. Referencia192/31/116/45,CAGR26.8148,DD16.5039,M37/58,Q15/20 conserva NO_CUMPLE. No repetir Kpara fabricar control. No interpretar mejora relativa ni mejor short histórico como candidata aprobada.

## Control de repetición y cierre anterior

P y su FINAL prohibían ablaciones/componentes/riesgo/gestión después dePnL. La presente pregunta es una excepción explícita de alcance solicitada por el usuario tras diagnóstico, aprobada por root para DOCUMENTAR antes de probar; no se borra ni reinterpreta P como autorización previa. No es continuaciónautomática de una receta fallida ni rankingporlado. No reabre N204,U,X805,F,AA u otrosvecinos.

R8 estableció BTCindividualantescartera y distingue regularidad de mediana; no medía estos dos escenarios ni autoriza simultaneidad. R14 previo: R1401 quitó suplemento, R1402/3 añadieron filtroslong; las12corridas mantuvieron3rutas compartidas. No equivalen a longsolo/shortbookBTCnativo con cuota1%,fundingM1/2020–25 completos; sus negativos siguen vigentes y no justifican afinarlos aquí. K/NlegacyR12 fueroncarteras, no prueba de cuentascomponentes. Earlylegacy preflight conserva fallos localizados de lookaheadOI/fundingdoble100 y no se importa código defectuoso: sólo R16auditado. Inventario acotado de documentos leídos, no censo universal ni claim de novedad de las señales.

## Presupuesto y secuencia

Exactamente2económicas nuevas futuras, LONG_ONLY ySHORT_BOOK, una por escenario; no engineinstrumentalocupación. Checks técnicos sólo sintéticos en máximo1analysisglobal coordinado. Este documento NO inicia ninguno. Fallo técnico se preserva y vuelve a root, sin reemplazo económico automático ni presupuesto oculto. No grid/riskvariants/gestiónalternativa/soloSUPP/COREsolo/flips/filtradoanual/vecinos trasresultados.

Antes de fuentes: root e independiente revisan protocolo ySOURCES. Luego implementación por agente autorizado en tresfuentesnuevasMCP,readback/hash yreview; syntheticsuppliedAST/stubs sin frameworkreal/importestrategias/velasobservadas/backtestanidado. Oráculos: únicamenteorígenespermitidos;helpercapital/margenscalado al.5exacto,budget.01total conlotfloor,reserve,fees/gap,corefallback;beforelatchsiempreadvance;invalidhistorynoevento stale;memo/TTLcancelrearm/sameexit;gestiónliteral/oneposition;hooksM1prestrict/zeroholding/tie/FINAL/idempotencia;padresintactos. No exigir réplica económica deK, sino transparencia de decisiones originales exceptoallowlist+cuota.

TrasPASS/reviewroot:2draftsgenuinos ymanifestos con formularios/funding/fuentes/runtime antes deejecución. Despuésauditoría/cierredeambos incluso negativos, sin selección silenciosa. Objetivo noalcanzado hasta gatesyvalidacióndefendibles; ningúnresultado autoriza operar ni combina cuentas.

## Aclaración de revisión previa a fuentes

Los invariantes del anexo reproducidos desde la propuesta de ocupación son una instantánea histórica de un diseño en HOLD. No gobiernan estas fuentes nuevas: NO capturar previous_setup ni recomputar legacy_supplement en el observador. El before original se hereda literalmente; la selección utiliza exclusivamente supplement_event producido por él, sujeto a legacy_rows válido. Rprecio es obligatorio y común a ambos escenarios, sin efectos económicos.
