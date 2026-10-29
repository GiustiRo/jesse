# Tanda U — reloj externo ETH frente a reloj BTC, libro BTC completo

## Estado y pregunta
2026-10-21. Root aprobó posteriormente IMPLEMENTACIÓN y checks sintéticos únicamente. Siguen sin autorización drafts/economía o consultas de velas observadas. Requiere revisión root e independiente de fuentes/check antes de borradores. Nombres nuevos: BtcResearchR21ExternalClockBase1m/BtcResearchR21BtcClock1m/BtcResearchR21EthClock1m. Presupuesto futuro limitado, sin compromiso de ejecutarlo.

Pregunta material: ¿cambiar únicamente la frontera temporal de la lectura X805, desde50% del volumen BTC a50% del volumen ETH de la misma vela ya cerrada, aporta información económica incremental a un libro BTC completo? ETH sólo es dato del reloj; no precio predictor, beta, señal direccional, órdenes, fondos o funding ETH. El factor nuevo es distribución temporal de actividad externa; no se comparan volúmenes brutos entre monedas. No se afirma liderazgo causal, liquidez u orderflow real.

2020–25 ampliamente explorado: desarrollo adaptativo con historial global conservado, no OOS ni nueva muestra independiente. U no se justifica porque T/R/S fallaran. El diseño se fija antes de nuevas fuentes/resultados U y no cambia según futuras auditorías ajenas.

## Antecedente exacto y cierres
Estrategia BTCExploreR805, fuente strategies/BTCExploreR805/__init__.py. Se leyeron completos fuente y:
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FROZEN_PROTOCOL_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md
- strategies/BTCExploreR801/reports/BTC_R8_EXPERIMENTAL_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_CREATIVE_Y_FROZEN_ADDENDUM_20261019.md
- strategies/BTCNovelR901/reports/BTC_R8_Y_FAMILY_RESULTS_20261019.md

X805 B/C fueron negativos respecto a su referencia, sobreoperaron y no habilitaron extras R8:
Dashboard: http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8
Dashboard: http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41
Eran carteras BTC/PAXG/SPY,1%/8%/5x,sin funding: no son resultados BTC individual actuales. X805 sólo sustituía suplemento; sus ramas originales seguían y la ocupación cambió ejecuciones. No aislar su aporte monetario ni derivar de esas carteras un CAGR BTC.

R8 dice que descarta esas reglas concretas sin ajustar umbrales y cierra presupuesto/extras; no hay prohibición explícita de un reloj con información ETH que nunca se utilizó. U no cambia50%,240M1,setup,geometría,signo o gestión por PnL; contrasta un input distinto con control completo. No reabre selección R8/Y ni los experimentos del libro P. El final P cierra vecinos/ablaciones de componentes,risk,prioridad,gestión/plazos; U conserva todas las tres ramas BTC y sólo sustituye input del suplemento X805 en AMBOS libros, sin eliminar componentes ni añadir exposición. Reusar lifecycle/sizing R16 no equivale a reutilizar la candidata cerrada de P como nueva ganadora.

J: ETH confirma dirección BTC con retornos/sigmas horarios; Q: niveles BTC/ETH bajo beta de retornos y zscore. Protocolos/finales y fuentes J/Q completos guardados en CODES. Ninguno usa volumen ETH. Sus cierres siguen intactos; U no añade un filtro a esas recetas ni cambia beta/z/horas/ventanas. D ya prueba buckets BTC propios; X/Y volumen/cohortes y X805 propio son antecedentes conservados. No afirmar novedad universal.

## Fuentes existentes y reutilización
Leídas completas MCP antes de este documento: BTCExploreR805, BtcResearchR16LegacyBase1m, BtcResearchR11Base1m, BtcResearchR10Base4h, BtcResearchR13ExternalBase1m y BtcResearchR17RelativeBase1m. Textos completos/hashes y cierres se preservan en BTC_DISCOVERY_U_CODES_20261021.md. DOCS.md y bot/AGENTS.md previamente leídos desde entorno autorizado; no filesystem de estrategias.

Hashes:
- BTCExploreR805: 246150464d5636e3a107ba8ad69eb63d3ca98de4d1410d75e12044ef0d36e08a
- BtcResearchR16LegacyBase1m: 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- BtcResearchR13ExternalBase1m: aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a
- BtcResearchR17RelativeBase1m: b40f428caaa728a117953fc97e4eee3372b895e622ba927c695fdef665dfefb8

Viabilidad: R16 separa legacy_long/legacy_short/legacy_plan de legacy_supplement; puede reutilizarse sin modificar padres. Futuro U sustituye before para preparar ambos relojes y generar evento X805; conserva _prepare_entry lazy, órdenes, cancel/rearm, fill/gestión/cierre/ledger/observador. No llamar before padre para generar N204 y sobrescribirlo después: consumiría un latch equivocado. MODE nuevo debe validarse sólo en before U; resto del lifecycle lee MODE para telemetría, no elige reglas K/N. No monkeypatch de módulos/padres. Todo cambio futuro debe auditarse contra textos suministrados, con allowlist de before/helper suplemento y telemetría U.

## Libro y contrato idénticos entre políticas
Dos cuentas alternativas completas BTC100%: LONG_RUNNER, CORE_SHORT, SUPPLEMENT. Prioridad y posibilidad de intentar siguiente receta si la anterior no forma plan/qty iguales R16. No long-only, no short-only, no aislar suplemento ni sumar curvas. Única diferencia entre control BTC_CLOCK y tratamiento ETH_CLOCK: índice de corte elegido para el suplemento. Igual disponibilidad y cálculo de ambos cortes en ambas políticas, igual contrato/datos/gestión.

BTC-USDT Binance Perpetual Futures ruta1m observación/ejecución; data-only BTC4h,ETH1m yETH4h prefijados desde este protocolo. M1 BTC proviene de ruta base y ETH1m se declara explícitamente: no asumir que un feed4h expone su M1 subyacente. Son datasets existentes, no importación/dataset nuevo ni búsqueda de timeframe. No cambiar esta elección por PnL. No comprobar cobertura de mercado por herramientas antes del motor; revisar contrato API/framework/documentación si hace falta, sin velas. El motor es autoridad para falta de cobertura y se registra limitación sin importar/reemplazar feeds ni rellenar. Una falta de datos exigidos por motor es fallo técnico, no evidencia económica.

[2020-10-15,2026-01-01)UTC,10k,warmup240 del mayor timeframe4h como P. Riesgo2% por trade/6% agregado/3x aislado,una posición sin pirámides. BTC cuota100%; max(0,balance) al sizing flat. Reutilizar literalmente legacy_plan R16: fee-aware,riskbudget.02capital,RESERVE.001 en sizing,LOT.001 hacia abajo,gross cap4.4 heredado no vinculante por margen3x,90%margen con fee buffer. La reserva10bps NO se cobra ni simula slippage. Ninguna variante de sizing/riesgo.

Fee.00045porlado takerdescuento,fundingBTC histórico ON/aplicado/verificado dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 y marksproxy declaradas,slippage aplicado0. Sin estrés, nuevos datos/importaciones,2026 económico nuevo,ML,scripts,instalaciones,reinicios,globalconfig/framework,Pi,paper/live.

## Historia, reloj y validez común
Cada T múltiplo4h usa legacy_history BTC4h existente sin recortar: sólo open+4h<=T,últimaopen=T-4h,datos consecutivos/positivos/finitos/OHLC coherente. Precio decisión BTC coincide con último close. Mantener toda historia expuesta, crecimiento/retención y llamadas ta del padre. ATR=ta.atr(c) real Wilder14/default sobre c completo, con semántica interna del runtime existente como P; NO sustituir atr14 simple R10 ni fabricar semilla Wilder propia. Mantener taEMA/ADX/RSI existentes.

BTC4h inválido: mismo bloqueo de libro/runner update que R16, reset previous_setup=False, sin señal nueva; stops/deadlines siguen. Historial BTC4h válido pero M1 BTC/ETH inválido: sólo SUPPLEMENT queda neutral y su latch se reiniciaFalse, en AMBAS políticas. NO borrar legacy_rows ni impedir LONG_RUNNER/CORE_SHORT por falta ETH. Contar clock_invalid separado de invalid_windows BTC del observador. Igual tratamiento en control y tratamiento. M1missing no se convierte en lowvolume ni permite señal posterior en ese T.

Para el reloj usar M1 en [t.open,T), exactamente240 filas por activo,open t.open+i*60000,últimaopen=T-60000,timestamps idénticos por activo. Todos pasados/cerrados asofT; ignorar cualquier fila>=T, rechazar huecos/duplicados/noexactas. OHLCVfinito,OHLCpositivo/coherente,V>=0 por minuto; totalV por activo finito>0. Último close M1 BTC debe igualar Ct como X805; no exigir movimiento/retorno ETH. Su OHLC se valida como integridad de datos, no feature de alpha. Ventana14BTC del setup conserva también los requisitos _explore_window de X805: todos finitos,OHLCVpositivo en sus14últimas4h y demás chequeos del padre. Esto no obliga a cada M1 tener V>0: ceros individuales permitidos, nunca imputados.

Normalización independiente por activo del MISMO intervalo cerrado. Para conservar exactamente la aritmética del corte X805, fijar sumV=np.sum(V) y cum=np.cumsum(V), ambos finitos, e índice np.searchsorted(cum,.5*sumV,side='left'). Interpretar fracción cum/sumV y registrar esa fracción normalizada; no comparar cantidades de dos activos. No prescaling opcional,epsilon,clipping,redondeo de empates o comparación USD/base/notional. Rechazar total0/no finito o cualquier acumulado no finito, como validez común. La invariancia a escala/proporcionalidad es matemática: en float, sumas cercanas a50% pueden redondear de modo distinto. No prometer invariancia universal ni reparar con epsilon. Checks usan escalas exactas/no ambiguas y empates prefijados; se preserva aritmética raw del padre. Esto no acredita estabilidad de unidad/feed a través del tiempo.

kBTC y kETH = primer índice0..239 cuyo acumulado cumple cum>=.5*sumV, equivalente matemáticamente a fracción>=.5, bajo aritmética exacta fijada arriba. La M1 frontera se asigna ENTERA a first=0..k;second=k+1..239. No partir OHLC, compartir minuto ni reconstruir orden intraminuto. Igualdad50% usa primer índice y primero incluye ese minuto. Overshoot pertenece al primer grupo, se registra, no se recicla.

Validez compartida antes de elegir modo: AMBOS cortes deben producir grupos no vacíos y suma de volumen BTC positiva/finita en los dos grupos de CADA corte. ETHsecond puede sumar0 aunque tenga filas y BTCvol positivo: NO añade filtro, porque ETH sólo determina su corte. Si cualquiera de las guardas explícitas de grupos/BTCpesos falla, ambos modelos invalidan sólo suplemento/reset latchFalse. No sustituir un corte por otro, por tiempo fijo o por .5 interpolado. No exigir que los cortes difieran: si coinciden las condiciones/evidencia deben ser idénticas. Volúmenes temporales proporcionales entre activos producen identidad; verificarlo sintéticamente.

## Setup X805 exacto y única sustitución
En c BTC4h,s=c[-2],t=c[-1],Cprev12=c[-14,close]. Condición base Cs>Cprev12 y Ct<Ot. Para cada corte k, tomar filas BTC first/second definidas arriba; costos:
A1=sum(VBTC_i*HLC3BTC_i)/sum(VBTC_i) de first;
A2 igual de second.
HLC3=(H+L+C)/3 como fuente. Pesos/costos son SIEMPRE BTC, en ambos modos; nunca ETHvolume como ponderación de precios ni ETHprice como predictor. Setup completo_k = base y A2<A1 y Ct<min(LBTC_first), comparaciones estrictas. Validar finitud de HLC3, productos, sumas ponderadas y costos intermedios de AMBOS cortes; cualquier overflow/no finito es invalidez común de datos para suplemento, no clipping/reparación ni ponderación ETH. No simetrizar largos ni quitar base legacy.

BTC_CLOCK selecciona setup_kBTC;ETH_CLOCK selecciona setup_kETH. Calcular ambos setups/costes aun ocupado y guardar desacuerdo/cortes como diagnóstico, sin seleccionar según PnL. Estado previous_setup es del setup COMPLETO del reloj elegido; puede diferir entre políticas aunque validez común sea idéntica. Actualizar previous_setup antes de cualquier ATR/distancia/capital/ocupación. Sólo nuevo True trasFalse emite intento de evento. Si setupTrue previoTrue no reintentar aunque geometría mejore; datos inválidos resetFalse de forma compartida, sin cola.

Después de consumir transición, ATR real finito>0, d=max(Hs,Ht)+.25ATR-Ct y ATR<=d<=3ATR;entry=Ct,SELL MARKET. Validar0<d<entry y target_planeado=entry-2d>0 antes de construir evento en AMBOS. Guard exacto físico, sin buffer ni optimización; el latch ya se actualizó incluso si se rechaza. No cambiar distancia para forzar TPpositivo. Resultado evento originSUPPLEMENT,direction-1,distance d,target_distance2d,hold48h,order_kindMARKET,con evidencia ambos relojes.

Targetguard nuevo se limita al suplemento. No modificar legacy_plan ni ampliar _prepare_entry/fallthrough por target CORE_SHORT. Conservar asserts R16 al fill sobre stop/target/riesgo/qty; un caso core físicamente inválido sería bloqueo técnico a investigar como P, nunca oportunidad para optimizar reglas. Se prefiere lifecycle literal sin pre-submit adicional.

## Ramas originales, gestión y ejecución preservadas
LONG_RUNNER literal legacy_long: canal26 previo,EMA20/80/ADX26/RSI52–76 y rango<=3ATR,BUY LIMIT siguiente4h,distancia2ATR. SinTP/plazo; trailing4.2ATR,BE2.25R,multiplicadores.78 desde5R/.62desde8R. Sólo cierres4h estrictamente posteriores al fill y stop ratcheting.

CORE_SHORT literal legacy_short: EMA120 creciente,precio>macro-ATR,RSI3<=20,STOPmin(L,C-.25ATR),distance=EMA20-entry entre1..3ATR y>=6fee*entry,TP1.5ATR de señal,72h desde fill real. Sin runner/gestión nueva.

SUPPLEMENT MARKET al close conocido,fill realE:SL=E+d,TP=E-2d,48h desde opened_at,gestión sólo4h. Sin trailing/BE/reparación/cambio de gestión por origen reloj. Ninguna orden ETH ni modificación long/core por sus datos.

R16 lazy _prepare_entry memoizado por T,una elección de plan/prioridad,sizing tras cancelación liberar margen. Pendientes LIMIT/STOP originales viven una4h; no cancelar cadaM1. Replay minuto de expiry antes de cancelación y rearmado en el MISMO cierre si broker queda plano conforme P; no rearmar tras cierre de posición en ese T ni en minutos intermedios. Suplemento consumido aun pendiente/ocupado/ganó otra prioridad; sin cola ni reversa. Protecciones M1 siempre activas; TTL de pendientes4h y plazos de posiciones72h/48h desde fill son distintos, con salida temporal sólo en fronteras4h.

## Medición y trazabilidad
R11 equity=wallet+PnLabierto M1/fills,cortes00UTC postfunding/predecisión porfase,no agrupación estricta evento por mes civil. DD M1+fills,no todos extremosintraminuto. Ledger R16 por LONG_RUNNER/CORE_SHORT/SUPPLEMENT: cierre/net se actualiza ANTES de callbackR11 que puede emitir FINAL; conciliar fills/closes/net con cuenta incluido terminal. No inferir aporte standalone desde suma ramas.

Telemetría agregada de todos cierres4h del intervalo: entradas M1válidas/clockinvalid por motivo,ambos k,timestamps/fracciones y diferencias,kcoincidente,proportionalidentity sintética,base true,setupBTC/setupETH/acuerdo/desacuerdo,transiciones seleccionadas y geometrías rechazadas,ocupación/prioridad/cancelaciones/fills. Calcular desacuerdo aun ocupado; no sólo sobre fills. En fills suplemento incluir ambos costos/cortes y reloj elegido; emisiones finales compactas y resumen perbranch. No logs por cadaM1 ni llamar entrada a evento/no ocultar volumenETHausente.

## Verificación futura y presupuesto
Antes de código root revisa este protocolo/objeciones. Luego, sólo si autoriza: CODES completos/readbacks/hash, revisión independiente, checks sintéticos suppliedsource/stubs sin velas observadas/importsestrategias reales/framework ni backtests anidados. Oráculos: exact240M1/sync/futuros/ceros/totales/cortes=.5/overshoot/minutoentero/nonempty,ambos cortes válidos comunes,escala poractivo yproporcionalidadidentidad,noETHpricealpha,mismaBTCVWAP con distinta frontera,setup completo/base/latch antes geometría,invalidETH sólo suplemento yBTC4h invalid todo,ocupado/noqueue ynoesperarATRgate,ta real/fullhistory contrato sin sustituirsimple,paridad originallong/core/sizing/gestión/deadlines/cancelrearm,guard físico sólosuplyterminalledgerfee. Fakes no prueban semilla real ni cobertura/runtime de indicadores/broker; documentar límites.

Presupuesto futuro exactamente2económicas BTC_CLOCK/ETH_CLOCK, hasta2reemplazos exclusivamente técnicosdocumentados, nunca por PnL. Requiere aprobación root adicional y motores libres; máximo2backtests globales/1análisispropio coordinado. No crear borradores ahora. No vecinos de.5/240/setup/horizonte/gestión,otros activos reloj,quitar componentes/lados,usar sólo desacuerdos,refinar filtros o umbrales por resultados. Si falla cerrar U y conservar ambas.

Cada libro debe cumplir gatesr9 propios: CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activoscompletos,Q80completos,mediana retorno mensual calendario>0 con inactivos,neto aritmético sin2mejores meses>0,N>=100 preliminar operativo sin confianza/potencia porconteo; aspiraciones40–50%+/M70. Ganar alcontrol no basta ni prueba causalidad. No winner sustituto si sólo GLOBAL/BTCcontrol mejora.

Auditoría futura de snapshots completos gross-fees+funding=PNLsum=equityfinal-10k a1e-6USDT,ledger3ramas suma yfundingconciliados,2.741.760marcasM1,63intervalos/62meses/20Q yterminalfee. NO_CUMPLE si falla economía;INCONCLUSA si favorable sinmedición/suficiencia. No promoción/estrésautomático. ReportesMCP/Hub inmutable archivosprimero/índiceúltimo cuando corresponda.

## Objeciones registradas
El volumen total y su forma pueden reflejar factores comunes/horarios y sesgos de feed; normalización no demuestra información adicional. Cortes actuales iguales implican mismos costos/setups actuales, NO iguales transiciones/órdenes si previous_setup difiere por pasado. Identidad completa de políticas sólo con traza proporcional y misma inicialización; no se conoce frecuencia de coincidencias sin motor y no se inspeccionará antes. Diferencia de PnL mezcla selección/ocupación/capital compartido dentro del mismo libro, no efecto causal aislado. Reutilizar historia seleccionada no recupera OOS. Riesgo/gaps/funding pueden superar stop monetario. No hay razón para importar ni fabricar cobertura ETH si la infraestructura no la entrega.

## Precisión de comparación heredada
El control U usa mismo reloj raw BTC X805 pero nueva admisibilidad compartida con ETH y cuenta BTC individual/riesgo/costos r9. Por ello NO es reproducción idéntica de la cartera histórica X805 ni una nueva prueba independiente de ese negativo. Las tres ramas originales se preservan; input externo es el único contraste entre dos libros U.

## Pre-check technical performance correction
After root source review and before any check job, use searchsorted over sorted runtime M1 timestamps for [T-4h,T) and slice view, not a mask/full copy/astype over growing historical buffers. Sorted store contract was audited in P; retain exact240/timestamp/OHLCV validations inside slice. Synthetic checks compare against independent mask oracle and prove older sorted prefixes/future rows do not affect context. No alpha, threshold or history-window change. Initial and current full base sources preserved in CODES; parents/wrappers unchanged.

## Check técnico y estado antes de economía
Fuentes nuevas creadas y padre R16/R11/R10/X805/J/Q sin cambios. Root/independiente detectó una fuente técnica inválida2174… con backslash-n literal al sustituir mask por searchsorted; corregido antes de jobs y preservado en CODES. Fuente final base caa81c… no cambió entre tres checks. Primer job e8166fd2a19240cb85d1175b5dbe8828 falló por predicate AST del harness que confundió binding local raw con mutación; segundo72629f2a9b064d2b973bf9bf3d7bf60a falló por fixture ETHsecond0 incorrecto; sólo harness/fixture corregidos. Tercero2d9df9fc38ef470f983d39e1a3f17acc succeeded172 assertions, inputs[], supplied AST/stubs, sin datos observados/importsestrategias reales/framework/backtests internos. Recibo completo BTC_DISCOVERY_U_TECHNICAL_CHECK_RECEIPT_20261021.json conserva tres códigos/estados/errores/artefacto y nueve readbacks exactos. Check incluye oráculo máscara vs binary slice, arrays sin mutación incluyendo NaNs fuera de ventana, costos/cortes manuales, raw tie/escala exacta, ETHsecond0, identidad de traza y distinta transición con corte actual igual, preservar core/runner cuando ETHmissing, actual fill/48h/ledger terminal y herencia literal. TA stubs no prueban semilla Wilder runtime ni cobertura/broker. Slot análisis liberado. No drafts/economía autorizados; revisión root e independiente siguen antes de motores.
