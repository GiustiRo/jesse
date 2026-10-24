# Calendario semanal BTC — crítica y protocolo previo
18/10/2026. **Protocolo aprobado e implementado para revisión de fuentes; sin borradores, consultas de rendimiento ni corridas.** Releídos baseline, inventario central y protocolo SPY cambio de mes. No fuentes externas. Carpeta reservada AngleCombinedBtcWeekend4h sólo para este informe.

## Dictamen
El calendario semanal introduce información distinta de una transformación adicional del precio: pertenecer a fin de semana se sabe antes de observar la rentabilidad. No duplica exactamente RSI, pivots, compresión, permanencia ni retest. Sí comparte familia amplia de estacionalidad con el SPY cambio de mes ya descartado; activo, frecuencia semanal y operación24/7 son diferencias, no prueba de independencia.

**La premisa LONG de sábado a lunes es débil como alpha:** que cambie la composición de participantes durante el fin de semana no establece que el retorno esperado sea positivo ni superior al de cualquier48h de mercado alcista. No tenemos flujo observado ni evidencia específica en este diseño. Condicionar a EMA80 ascendente puede añadir simplemente beta alcista en huecos de exposición. No afirmar ventaja de calendario por ganar más dólares tras añadir riesgo.

Recomiendo no implementar esta narrativa como señal diferencial sin aceptar antes el control fijo descrito abajo. Si root decide una pantalla experimental, la única receta queda especificada sin parámetros de rescate.

## Receta única congelada
Clon completo de MultiAssetRetestBtcShort4h, tres rutas4h. BTC conserva evaluación original long y después short con longpriority. **Sólo si estáflat, no hay entrada pendiente y ninguno de esos planes originales es válido**, considerar el suplemento.

Calendario: decisión cuyo timestamp de cierre es exactamente sábado00:00UTC, una vez por semana. No usar día de apertura de la vela que cerró el viernes20UTC; no esperar al sábado04/08 si se perdió la decisión. Si posición/pending/planoriginal/riesgo impide actuar, se omite esa semana. Un STOP posterior tampoco habilita reentrada semanal.

Contexto conocido, fijado por root antes de código/resultados: EMA20>EMA80[-1]>EMA80[-5] y close>EMA80[-1]. Usa parámetros fast/slow originales(default20/80), sin rejilla; no requerir breakout,RSI niADX. Es régimen heredado, no el filtro completo de breakout que impediría nuevos planes.

Entrada MARKET al precio propio conocido y fresco del sábado00UTC, ejecutada por broker hacia delante. Stop protector fijo2ATR14 de4h conocido al decidir, anclado al fill real. Riesgo máximo1% incluyendo mismas fees/reserva, con presupuesto global8%,techo4,4x,margen90% y cuota inversaATR originales. No apalancar más para forzar retorno. Si no queda cantidad válida, omitir semana.

Salida MARKET en decisión lunes00UTC. Son48h **desde señal de sábado**, no otra regla fill+48h: si el fill se retrasa, no extenderla hasta lunes04. Usar deadline de calendario predefinido, no resultado del trade. Si falta callback/cotización propia fresca al deadline, diferir hasta primera disponible y explicitar exceso temporal, sin fill retroactivo. Protección STOP activa siempre. Sin target,breakeven,trailing ni salida de régimen adicional para este suplemento.

Guardar origen de cada posición desdeplan/fill: sólo WEEKEND usa esta salida; posiciones originales conservan on_open/update/exits textualmente. Otras rutas quedan intactas. No cerrar, cancelar ni redimensionar una posición original para abrir suplemento.

**Limitación de prioridad:** respetar el plan original en el sábado no preserva futuras oportunidades. Estar ocupado con WEEKEND puede bloquear señalesBTC del domingo, y el capital cambia otras cantidades. Eso es parte de la variante ejecutable y debe atribuirse. No describir97longs/123shorts como resultado garantizado ni sumar curvas independientes.

## Control indispensable, predeclarado; no buscar el mejor día
Una única comparación de fase calendario: **martes00UTC→jueves00UTC**,48h, misma regla de régimen en su propio inicio, mismoMARKET,stop2ATR,1%riesgo,fees,prioridad y restricciones. Es control de exposición alcista programada, no candidata alternativa de la que elegir el mejorweekday. No probar lunes/miércoles/otros días ni horas adicionales tras resultados. Martes fue fijado por root antes de código/datos/rendimiento; sustituye mi borrador inicial miércoles→viernes sin haber consultado retornos. No se construye una comparación para escoger el mejor día.

La referencia ya congelada es el ancla sin suplemento. La cartera con suplemento weekend y el control weekday serían dos políticas de cartera completas; el control es necesario para interpretar beta/calendario, no otra optimización. Si no se quiere gastar un control, descartar el diseño antes de código es preferible a afirmar que una nueva fuente de retorno proviene del sábado.

No son un experimento aleatorio perfecto: el régimen, riesgo disponible y señales que bloquean el bloque pueden diferir por fecha. Comparar también counts/admisiones,exposición-tiempo,notional,riesgo,fees,retornos normalizados por nocional y contribución por origen. No condicionar el martes a información del sábado futuro, ni seleccionar semanas después de ver qué bloque ganó. No introducir matching por el signo del retorno. Un contraste positivo aislado sería descriptivo de desarrollo, no prueba causal pura.

## Qué permite falsar sin tocar umbrales
1. Si no hay cotización/estado correcto o se confunde timestamp de vela y cierre, falla técnica. Corregir sólo defecto verificable antes de interpretar rendimiento; no convertir datos ausentes en una prima.
2. Si el suplemento pierde neto y no aporta mejora real de cuenta, descartar. Precio antes de fees separa señal sin margen de hurdle de costes; esos importes fijos no son backtestfee0.
3. Si weekend gana pero el control weekday produce beneficio comparable por exposición/riesgo y el calendario no avanza, no hay evidencia de especialidad semanal; no llamarlo alpha calendario. No elegir entonces el control ganador como nueva candidata.
4. Si el incremento es capital posterior de otros trades o másbeta/DD, atribuirlo; no adjudicarlo al signo de la estacionalidad.
5. Si no hay suficiente admisión porque baseline ocupaBTC, reportar muestra/ocupación. No relajar prioridad ni ampliar días para fabricar trades. Muestra pequeña no verifica ni refuta universalmente prima de fin de semana.
6. Si sólo mejoran ratios excluyendo meses cash o bordes, no promover. V4 debe incluir63meses/21trimestres y completos,neto/costes/DD y rescates/perjuicios, manteniendo65–70%/80% yDD25%.

Ventana común2020-10-15→2025-12-31exclusivo,fees0,00045todos tipos,5xaislado,normal. 2026 reservado. Todo es desarrollo adaptativo tras muchas exploraciones, no OOS. Sin ampliar stop/horas/días/régimen o apalancamiento después del resultado.

**Estado final de esta revisión:** mecanismo temporal distinto pero fundamento direccional insuficiente; sólo defendible como falsación experimental limitada con control de beta, no siguiente candidato prometido. Root revisa antes de implementación. Esta conclusión se formuló antes del código; root aceptó la comparación experimental con control fijo. Las dos fuentes nuevas se implementaron después, como consta a continuación.


## Fuentes listas para revisión root; todavía sin drafts ni runs
- Candidata: strategies/AngleCombinedBtcWeekend4h/__init__.py.
- Control NO seleccionable: strategies/AngleCombinedBtcWeekdayControl4h/__init__.py.
Ambos clones completos se guardaron y releyeron exactamente porMCP. Al normalizar clase/docstring/weekday son idénticos; la única diferencia económica es SUPPLEMENT_WEEKDAY=5 frente1. No se copió una configuración ni se cambió la referencia.

Se verificaron16métodos originales textualmente idénticos: hyperparameters,trading_hours,signal_candles,_entry_window,_ledger,_key,_capital,_committed,_volatility_share,_plan,should_long,should_short,go_long,_short_plan,go_short,should_cancel_entry. Hooksdeposición sólo añaden dispatch para origen calendar; si el origen esoriginal, ejecutan su gestión original sin modificarla. Antes de un nuevo fill original se limpia el indicador de leg, evitando arrastrar salida calendario a otra operación.

El suplemento usa presupuesto min(capital×0,01,capital×0,08−riesgo comprometido), mismo unitriskfees/reserva, roomglobal/cuotaATR, margen90% y precisiónBTC0,001 originales. MARKET(p=self.price) se distingue de LIMITbaseline, aunque ambos entran porgo_long original. Deadline se conserva desde señal+48h y el stop queda desdefill, sintrailing/TPsuplementario. Countersmiden retraso real de fill sin extender deadline.

**Frescura de ejecución:** los futuros drafts deben incluir data_route BTC1m EXISTENTE junto a las tres tradingroutes4h. _calendar_quote_fresh usa searchsorted para último open<=time−60000 y exige open+60000==time y cierreM1igualself.price. No descarga datos ni añade un instrumento. Si falta minuto, omite la entrada semanal; si falta aldeadline, difiere sólo la salida discrecional mientras protección permanece activa. No marca comofresh simplemente una vela4h con bucketcorrecto.

Telemetría final acotada porbefore_terminate/jh.debug: slots,occupied,pending,prioridadbaseline,evaluados,rechazosrégimen/riesgo,planes,fills,cierres,timeexits,retrasos yquotesausentes. before_terminate es previo a cierres sintéticos terminales: fills yclosed no se fuerzan iguales si queda una posición alfinish. Las entradas próximas al final pueden liquidarse por convención de muestra antes de48h; etiquetarlo explícitamente, no anticiparlo en estrategia.

Root revisará antes de crear ambos full normales/debug; loggingM1masivo desactivado. EvaluaciónV4conjunta y atribución de suplemento/baseline/exposición. La candidata sólo avanza si mejora objetivos conjuntos frente a referencia y supera el control de beta/riesgo; si controlgana, no se promociona ni se prueban otros días. Contraste descriptivo con estado endógeno de cuenta, sin causalidad/CI nuevos. No se pretende aprobación automática por sumar beneficio ni se modifica65/80.


## Etiqueta de terminación previa a cualquier corrida
Root pidió hacer explícito el instante de contabilidad: before_terminate imprime **counts_preterminal**, no totales de operaciones cerradas definitivas. La modificación de fuente cambia sólo esa etiqueta de log; readback exacto en ambos clones y reversión de la etiqueta devuelve la fuente anterior sin otra diferencia.

El control puede admitir un long el martes30/12/2025 cuyo deadline natural sea01/01/2026, después del finish31/12/2025. Si sigue abierto, el motor lo cerrará sintéticamente alfin. Eso no constituye incumplimiento de la regla48h, ni acredita cotización fresca/liquidez en ese instante, ni autoriza anticipar la salida consultando fin de muestra. El auditor debe etiquetar terminal synthetic y reconciliar fills/fees/wallet por su contrato; los contadores preterminal pueden tener fills>closed. No se cambia ventana, deadline, señal ni gestión.
