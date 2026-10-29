# Propuesta: reloj de cambio direccional para shorts BTC
18/10/2026. **Implementada tras aprobación root; fuente para revisión, sin borrador ni run.** Receta única para revisión root. Sólo velas BTC existentes; no externos, scripts, indicadores latentes ni framework. Referencia y2026 intactos.

## Control y novedad limitada
Se leyó completa AngleCombinedBtcClockControl1m. [Control técnico](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1): root informa reproducción de220trades,440órdenes y45métricas de referencia. BTC1m es reloj de ejecución con auxiliarBTC4h cerrada; largos/gestión permanecen en fronteras4h. PAXG/SPY siguen4h.

La propuesta reemplaza la elegibilidad RSI3 short por **momentum con histéresis de amplitud**: una caída significativa desde el máximo de cierres observado durante una fase ascendente. El reloj avanza con desplazamientos del precio, no cada cuatro horas. No mide órdenes, liquidaciones ni agotamiento fundamental. No es un mero renombrado de RSI: varían los timestamps negociables, el extremo de referencia y la memoria path-dependent; puede seguir generando exposición muy parecida y no constituye un edge independiente.

Inventario contrastado: Pullback original usa RSI3/régimen ascendente; QuietChannel/SqueezeRelease usan compresión y ruptura de ventana; Structure usa pivots confirmados y primera pérdida de soporte; Reject/DailyPullback usan recuperación fallida de EMA; OneFill usa episodiosRSI y fill latch. Ninguno del inventario revisado implementa este reloj alternante basado en cierres. Seguimos en familia continuación: la independencia deberá medirse, no proclamarse.

## Una geometría predeclarada
Sea τ el momento en que acaba de cerrar M1 y p su cierre. Sólo filas con open+60000<=τ, última exactamente fresca; no high/low M1 para estado. ATR es **ATR14 de velas4h cerradas**, nunca barra parcial; δ=1×ATR, sin búsqueda de múltiplos.

Inicialización causal y sin entrada artificial: en el primer boundary4h del desarrollo con auxiliar240 cerradas válido (04:00 UTC en el reloj común/control), guardar p0 y δ0, estado NEUTRAL. Esperar primer cierre p>=p0+δ0 o p<=p0−δ0. Eso inicia fase UP o DOWN respectivamente, con extremo=p y δ congelado al ATR conocido en ese inicio; **no emite evento ni arma orden**. Así no se declara una tendencia inicial arbitraria ni se retrodata una entrada al precio inicial. El tramo de inicialización y su fecha quedan visibles en calendario; no se recortan para mejorar métricas.

En UP, máximo H=max(H,p). Si H−p>=δUP, emitir EVENT_DOWN con timestampτ. Iniciar DOWN en esa misma observación: mínimoL=p y nueva δDOWN=ATR4h conocido enτ. En DOWN, mínimoL=min(L,p). Si p−L>=δDOWN, emitir EVENT_UP, iniciar UP conH=p y nuevaδUP. Para cruzar se usa siempre δ de la fase que termina; el ATR actualizado sólo rige la siguiente. Un máximo nuevo NO mueve el umbralATR; sólo mueve el extremoH. No backdatear evento al máximo/mínimo.

Cada cierre sólo puede emitir un evento. Un salto grande no fabrica varios cambios intraminuto: únicamente observamos cierres, no conocemos trayectoria intermedia. Invalid/NaN no produce evento; falta inicialATR falla control técnico en vez de justificar arrancar tarde. No usar precios futuros ni revisar señales pasadas al recalcular ATR.

## Consumo y estrategia combinada
Actualizar fase/extremos en **before() BTC cada M1**, también con posición abierta u orden pendiente. EVENT_DOWN existe sólo paraτ y se consume independientemente de elegibilidad, órdenes, fills, STOP/TP o PnL. Un evento rechazado mientras open/pending o por riesgo no se conserva hasta estarflat. EVENT_UP sólo cambia fase; no abre long ni cierra short. No cooldown por horas ni uno por trade añadido.

Enflat, en frontera4h evaluar primero el long original; si éste produce plan, no abrir short aunque coincidaDOWN. En cualquier M1 fresca sin planlong, permitir short únicamente si hayDOWN deτ. Mantener régimenEMA120 ascendente/proximidad, EMA20, ATR14 y todos límites originales usando última4h estrictamente cerrada. Eliminar sólo RSI3 y el requisito de boundary4h para esta elegibilidad. Lectura de precio actual será p M1, no cierre4h antiguo.

STOP futuro **min(low de M1 DEL EVENTO,p−0,25ATR4h)**, ajuste aprobado antes de resultados. Se conserva operador/offset/tipoSTOP, pero NO se afirma que el nivel de entrada sea idéntico al original. El lowM1 es conocido en el evento y la ejecución sólo puede ser futura. Misma distanciaEMA20−entry entre1–3ATR y filtro de fees; TP1,5ATR, stop relativo al fill. Deadline exactoτ+4h para pendiente. Un evento mientras pendiente no renueva deadline ni reemplaza orden. Después de cancelar NO se rearma en ese mismo callback, igual que la secuencia del control. Un evento coincidente se consume; no se guarda para después.

Gestiónlong y timeoutshort conservan código del control: evaluación en fronteras4h; umbral72h desdefill puede liquidar en la siguiente frontera, no se promete precisiónM1. Órdenes protectoras siguen activas intrabar. BTC decisión única, sin piramidado/parciales. PAXG/SPY, largosBTC, asignación, capital/reservas, riesgo3%/8%, techo4,4x,5xaislado y fee0,00045todos tipos quedan congelados. Nuevos shorts pueden desplazar longs y capital; no afirmar invariancia de sus resultados realizados.

## Riesgos técnicos/económicos y falsación
- Eventos frecuentes pueden aumentar turnover y erosionar el pequeño colchón short original; histéresis1ATR no garantiza edge ni baja frecuencia.
- ATR congelado en fase larga puede volverse poco representativo; esa propiedad se conserva, no se cambia tras ver pérdidas. Ningún ATR futuro se aplica al umbral anterior.
- La secuenciaM1 pierde high/low intraminuto; no reconstruirla ni usar extremos4h como si fueran posteriores al fill.
- Procesamiento de estadoO(1) por minuto; indicadores4h sólo se recalculan cuando cambia la última4h cerrada, y elegibilidad completa sólo en eventos. Evitar recopiar/recalcular todo el histórico millones de veces. Esto es requisito de implementación eficiente, no reducción de memoria económica.
- Sin buena muestra de eventos realmente admitidos, no adjudicar falta de operaciones a que “el mecanismo no funciona”; distinguir coste/regla/ocupación y defecto técnico, conservando inicialización.

Root aprobó implementar la receta con los ajustes ex ante de lowM1 y comienzo en boundary4h. Fuente guardada medianteMCP y releída exactamente, para segunda revisión antes de draft/run. Invariantes: cadaM1seprocesauna vez, δfase>0 y fija, extremo formado sólo desdeiniciofase, timestamps/eventoid únicos, auxiliares cerradas, ningún evento reenviado porfill/cancel y longprioritypreservada. Smoke técnico predeclarado **2021-01-01→2021-04-01 exclusivo**: comprobar invariantes/ejecución, sin decidir alpha ni ajustar reglas por resultados. Sólo si pasa y root autoriza, una única corrida combinada normal2020-10-15→2025-12-31exclusivo, sin gridδ/clock/RSI.

Cuenta completa y atribuciónshort/cohortes/turnover/costes primero; V4MTM después con mesesactivos,63calendario/21quarters y completos. Comparar número y timestampsdeeventos con entradas para saber qué cambió y atribuir ganancia de longs al capital cuando corresponda. Mismasfeesallorders no acreditan spread/funding/fillslive. Mantenerobjetivos65–70%/80%/DD25%; no promesa. Si sólo aumenta costes o debilita neto/calendario, descartar receta sin reajustar amplitud ni buscar ventana ganadora.


## Verificación estática de la implementación y telemetría
Fuente strategies/AngleCombinedBtcEventClock1m/__init__.py, readback MCP exacto. Comparación de bloques confirmó idénticos _plan long, go_long, update_position/on_close_position y sufijo sizing/riesgo de _short_plan respecto al control. Otros activos usan las mismas reglas y sus ramas de before no hacen nada. La fuente añade estado y gates de short, no una nueva gestión de posiciones.

before verifica M1open+60000==self.time, precio igual a cierre, timestamps crecientes y low<=close. Primer boundary exige240aux4h y últimaauxopen+4h==ahora; caché ATR/EMA20/EMA120 se actualiza exclusivamente allí. La fase usa delta vieja antes de sustituirla; assert impide dos fases en el mismo timestamp. _signal conserva long priority y rechaza rearmar tras cancelación. go_short impide replay/orden duplicada deevento.

Contadores por añoUTC: minutes/down/up/blocked_open/blocked_pending/long_priority/rejected/plans/armed/fills. Sólo agregados (como máximo los años de la ventana), sin lista M1/eventos. jh.debug emite al cambio de año y en **before_terminate**, hook público confirmado por root mediante ejecución anterior. No terminate inventado ni fechas futuras dentro de decisiones. Las estadísticas de inicialización se guardan en vars; si MCP no exporta vars/logs, no inventar fechas/conteos.

El protocolo sigue siendo desarrollo adaptativo: una receta económica nueva, sin garantía de independencia. No se creó draft ni se lanzó smoke/full por esta implementación; root coordina ambos.
