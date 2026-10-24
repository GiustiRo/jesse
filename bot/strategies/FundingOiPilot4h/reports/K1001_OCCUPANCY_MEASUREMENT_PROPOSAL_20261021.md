# K1001 — Propuesta de una medición de candidatos, sin modificar la operativa

Fecha: 2026-10-21. Estado: DISEÑO para revisión root; no implementación ni autorización de motor. Se permiten en esta tarea documentos y snapshots de fuentes existentes. No se crean estrategias, drafts, jobs o pruebas.

## Pregunta y alcance de la respuesta

¿Con qué frecuencia las tres reglas originales generan candidatos mientras el libro está ocupado, tiene una orden pendiente o selecciona una rama de mayor prioridad? ¿Se concentran esos casos en pocos episodios o años?

La medición observa candidatos y decisiones, no operaciones contrafactuales. Un candidato bloqueado no acredita que habría llenado, ganado o mejorado el libro. No se asignará PnL ficticio, no se prolongarán sus órdenes virtualmente y no se simularán stops/targets alternativos. Tampoco se decide dividir, quitar o cambiar componentes.

El diagnóstico previo identifica 192 fills, 313 planes, 121 cancelaciones y 82 eventos originales del suplemento. La ocupación calendario de 20,53% no responde a la pregunta de señales bloqueadas; su denominador tampoco es el número de decisiones de 4h.

## Control y futuro presupuesto

Referencia: [K1001 BTC individual de P](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4). Una futura wrapper propuesta, K1001OccupancyObserver1m, heredaría de BtcResearchR16LegacyK1001m, a su vez R16Base. Nombre propuesto, no creado.

Como máximo UN nuevo ID de backtest instrumental, cuando root autorice implementación, verificación y ejecución por separado. No se añade segundo motor si falla paridad ni se repite para obtener un resultado conveniente. Un fallo técnico se documenta y vuelve a root antes de decidir continuación. Cuenta como medición/reproducción, no como nueva hipótesis ganadora o muestra independiente. Contabilidad y estadísticas deben recuperar todos los registros, no una página parcial.

La configuración se copia del formulario genuino de P, salvo nombre de wrapper y texto de sesión: BTC-USDT Binance Perpetual Futures, ruta1m y data4h; [2020-10-15,2026-01-01) UTC; warmup2404h; 10.000 USDT; 2% histórico por operación del único libro/6% global/3x aislado; fee .00045 por lado; funding histórico ON dataset 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571, marcas proxy declaradas; slippage0; fast_mode false; debug y logging originales conservados. No nuevas velas, preinspección de cobertura, imports, datasets, scripts, configuraciones globales, estrés o economía 2026.

El 2% es necesario para reproducir este control histórico de posición única. No autoriza 2% por componente futuro. El acuerdo vigente de dos cuotas1% o tres cuotas2/3% sobre capital BTC común NO se implementa en este medidor. Sizing real sigue usando el wallet y legacy_plan originales; no sustituirlo por equity, quitar reserva .001, cambiar lote .001 o distribuir cupo.

## Fuentes congeladas y forma de instrumentar

- BtcResearchR16LegacyBase1m: SHA256 `56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542`.
- BtcResearchR16LegacyK1001m: SHA256 `bf88cb663d8561e107446bfce32024ed87531d096362671f7aafce72a09f25ad`.
- BtcResearchR11Base1m: SHA256 `be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87`.

Readbacks MCP completos, base R16 idéntica a la fuente almacenada en el manifiesto previo de P. Anexo con código exacto y formulario: K1001_OCCUPANCY_MEASUREMENT_SOURCES_20261021.md.

La wrapper puede añadir sólo estado bajo una clave propia, por ejemplo occupancy_audit, y logs. No escribe campos parent de latch, planes, dirección, tiempos, órdenes, reservas, ledger o indicadores. No reduce historia ni reemplaza ta.atr/EMA por una versión distinta. Las evaluaciones diagnósticas llaman helpers puros congelados, en variables/closures temporales, sin mutar eventos ni arrays de velas. No llama a should_* o _prepare_entry para investigar una rama que el motor no llamó. No instancia padres ni un segundo motor.

### before: preservar primero la máquina original

1. Al comenzar un T4h, capturar el valor ORIGINAL previous_setup antes de super.before(), junto con flags de posición/órdenes, origen, plan pendiente copiado, wallet, margen, leverage y fee observados.
2. Llamar super.before() exactamente una vez en TODOS los callbacks M1, sin cambiar su orden ni sustituir su observador.
3. Sólo después, si T4h pertenece a START<T<FINISH, auditar legacy_rows que el propio padre acaba de fijar. No volver a obtener un historial con otra ventana. Si faltan filas o falló integridad/asof, registrar el estado correspondiente sin candidatos inventados.
4. Evaluar legacy_long(rows) y legacy_short(rows) sin filtros de ocupación. Para suplemento, recalcular legacy_supplement(rows, "K1001", previous_setup_capturado). Su evento y setup deben coincidir con los que dejó super.before(). No usar previous_setup ya actualizado como argumento: perdería el evento fresco.
5. Para separar geometría persistente y consumo, otra evaluación pura legacy_supplement(rows, "K1001", False) proporciona setup y geometría ignorando únicamente el latch. Esto NO cambia previous_setup de la clase ni crea una emisión adicional. El evento diagnóstico original sigue siendo el evaluado con el previo capturado.
6. Los duplicados T y retrocesos se identifican y no vuelven a contar en el ledger diagnóstico. Eso NO elimina ni cambia llamadas parent. Ningún guard diagnóstico repara o cambia la máquina original.

Cualquier discrepancia de helpers/latch se registra como defecto técnico; no se corrige la receta ni se interpreta como señal nueva. El riesgo principal es que los cálculos extras afecten indirectamente estado/cache: se exige pureza por lectura de fuente, checks posteriores suministrados y réplica numérica completa antes de usar la medición.

### Definiciones que no se mezclarán

- LONG_RUNNER / CORE_SHORT raw_geometry: helper original devuelve evento distinto de None, con su geometría original, sin exigir libro plano.
- SUPPLEMENT setup: condición original incluyendo eficiencia K1001; se consume antes de ATR, geometría y cuenta.
- SUPPLEMENT raw_geometry: helper con previous=False devuelve evento. No es una orden fresca si el latch original ya estaba activo.
- SUPPLEMENT fresh_event: helper con previous_setup ANTERIOR devuelve evento. Es la única emisión que el padre podría considerar; no se rearmará desde una geometría tardía dentro de un setup ya consumido.
- candidate_actual_machine: raw_geometry para long/core y fresh_event para suplemento.
- plan_valid_at_observed_account: legacy_plan devuelve plan no None usando ese evento, wallet/margen/leverage/fee realmente observados en ESA fase. En una cuenta ocupada esto es diagnóstico de sizing condicionado a su margen presente, no plan elegible ni simulación de margen liberado.
- selected_plan / submitted / fill / cancel: eventos reales, diferentes entre sí. Un plan seleccionado LIMIT/STOP puede cancelarse sin fill.

No se calculará un plan flat hipotético, ni se liberará margen contablemente para medir qué habría pasado. Los casos no evaluables se registran como tales. None del helper significa no candidato bajo su contrato; no se fabrican causas detalladas como ADX/RSI sin medirlas explícitamente. Faltas de historia/integridad se separan de un predicado evaluable que resulta falso.

## Capturar la cadena real de cancelación y prioridad

Una pendiente al inicio de before NO equivale a bloqueo final. La fuente real del framework cancela si corresponde y puede reevaluar entradas en el mismo T. Los fills del minuto de expiry pueden ocurrir antes del callback de cancelación; no se reordena el broker.

- should_cancel_entry diagnóstico copia pending_plan antes de llamar super, devuelve exactamente su resultado y registra due/expiry/tiempos. La wrapper no cancela ni rearma nada manualmente.
- La wrapper de _prepare_entry observa sólo llamadas que realmente hacen should_short/long del framework. Captura la cuenta y las condiciones de admisión inmediatamente ANTES del super._prepare_entry real. Después registra retorno, prepared_at y origen seleccionado fresco.
- Si las guardas parent permiten entrar y prepared_at todavía no es T, evaluar en variables temporales TODOS los candidate_actual_machine y legacy_plan sobre la MISMA cuenta liberada por la cancelación. El primer plan viable long→core→supp debe coincidir con el elegido por super. No adelantar prepared_at ni crear plan diagnóstico en vars parent.
- La segunda llamada should_* del mismo T se identifica como memo; no agrega otra oportunidad, selección ni sizing. Los contadores se indexan por T y fase, no por cantidad de llamadas a should_*.
- Si las guardas parent rechazan por posición, órdenes, salida en T o fuera de ventana, registrar esa situación; no tratarla como comparación de prioridades efectuada.
- after llama super.after y observa el estado final del ciclo, sin forzar decisiones: posición restante, entrada pendiente, submit real, cancelación y/o last_exit_at==T. Los logs parent de apertura/cierre siguen dando fills y geometría efectiva.

Sólo se etiqueta prioridad_bloqueante cuando hubo preparación real elegible, la rama inferior tenía candidate_actual_machine y plan viable con la misma cuenta, y otra rama anterior fue efectivamente seleccionada. En cambio, candidato observado durante posición abierta se etiqueta ocupación observada. Pending inicial→cancelación→nueva selección se etiqueta explícitamente; no cuenta como oportunidad finalmente bloqueada por pending.

La tabla conserva flags y fases, no una causa única inventada. Por ejemplo, geometría persistente del suplemento puede coincidir con ocupación y latch consumido. Se publican intersecciones, además de totales, sin sumar categorías superpuestas.

## Episodios y subepisodios

Un episodio de raw_geometry por rama es una secuencia de cierres4h consecutivos evaluables con booleano verdadero. Inicio observado significa transición falso→verdadero entre dos T consecutivos; fin observado, verdadero→falso. Primer verdadero al arrancar o tras un gap es inicio censurado a izquierda, no transición observada. Un gap/integridad insuficiente rompe la continuidad y censura el episodio previo; no se inventa un falso económico. El cierre terminal censura a derecha, sin inventar fin ni nueva señal.

Para suplemento se conserva en paralelo el episodio de setup y el de raw_geometry, ligados por IDs. La transición de setup false→true y el fresh_event original pueden diferir si falló geometría al comienzo; ese caso se registra y permanece consumido.

Un subepisodio es un tramo contiguo dentro del episodio con el mismo vector observado de estado (origen ocupado/pending, latch fresco/no fresco, plan viable en fase observada, selección real/priority shadow cuando existe). Los cambios se fechan en T4h; no se interpolan estados intrabar ni se llaman horas continuas de elegibilidad a ese conteo. IDs deterministas por rama/episodio/subepisodio y banderas de censura evitan ambigüedad por index M1.

Por episodio se informa número de observaciones4h, inicio/fin/censura, si alguna vez coincidió con ocupación/pending, si llegó a preparación real, seleccionados/fills/cancelaciones asociados. Un episodio puede tener varios planes reales por rearmados4h; no se fuerza relación1:1. Una observación o episodio no es una muestra estadística independiente.

## Telemetría y transporte

Un registro compacto por T4h con las tres ramas, snapshots de las fases, IDs de episodio y campos de evento, más registros sólo al ocurrir preparación/cancelación/submisión/fill/cierre. No logs de millones de M1. El detalle mínimo incluye requested_entry, distance/target, tipo de orden, setup previo/actual, fresh/raw, origen de posición/pending, signal_at/expiry, wallet/margen y resultado de plan cuando exista. No series de velas ni campos de orden ficticios.

Se publican resúmenes online, por año y componente, con denominadores explícitos (T4h válidos, candidatos, episodios completos/censurados, planes reales, fills, cancelaciones e intersecciones de estados). Son medición del proceso original, no inferencia de potencia. Las sumas se concilian con el detalle. Emisiones PRETERMINAL/FINAL no duplican episodios ni totales; si FINAL reemplaza un resumen tras cierre terminal, se identifica como snapshot más reciente, no como suma.

El detalle se recupera por páginas MCP completas y se preserva en reportes de tamaño acotado con manifiesto/hash y límites efectivos de lectura; no usar páginas truncadas como universo. El wrapper puede emitir resúmenes verificables en logs; eso no convierte logs en inputs de run_analysis. El recurso actual no incluye logs en el snapshot de análisis: no se propone leer archivos del proyecto desde analysis ni pegar arrays reales en su código. La auditoría financiera de paridad sí usa únicamente inputs nativos de los dos backtests; cualquier validación adicional del trace tendrá que respetar el transporte permitido y declarar su alcance.

## Segundo output opcional en el MISMO replay: R de precio observado

Viable con hooks pequeños; si amenaza paridad, se retira del alcance ANTES de motor y se prioriza ocupación. No habrá un segundo replay para añadirlo. No modifica señales, protección, gestión, stops o targets.

Override _observe(stage) llama a super._observe(stage) UNA vez y devuelve su valor intacto. En stage=open, R16 ya fijó position_plan antes de llamar _observe: crear sólo el registro diagnóstico propio con entry real, distance inicial original, direction y Rprecio=0. En stage=pre, si la posición sigue abierta y el registro corresponde a ella, marcar Rprecio=direction*(closeM1-entry)/distance. Son cierres M1 observados mientras la posición está abierta; no tomar high/low de la vela ni precios previos al fill.

En on_close_position de wrapper, ANTES de super y de que R16 borre position_plan, agregar el fill de salida real como última marca; completar el registro y dejar su resumen listo antes del posible FINAL de R11. Después delegar al padre una sola vez. Un trade abierto y cerrado dentro de un minuto puede tener sólo0 y el fill final. No se fabrican cierres M1 mientras estuvo flat ni observaciones después del cierre. _observe(close) parent no vuelve a marcar un registro ya finalizado.

Registrar mínimo/máximo de Rprecio en este conjunto, timestamp y fase de su primera ocurrencia estricta, número de marks M1, tiempos primero/último, entry/exit/qty/distancia y origen. Empates no reinician reloj. Duplicados de la misma marca se ignoran sólo en el ledger propio. Estos extremos NO son MFE/MAE intraminuto ni el movimiento disponible si no hubiera existido el stop original. Funding y fees quedan fuera de Rprecio; el neto realizado es otro campo.

No optimizar captura, trailing o targets con el output. Su pregunta descriptiva limitada es qué cierres y fills se observaron durante la posición frente a su salida real, especialmente en un runner concentrado. Se conserva la selección original: no informa candidatos bloqueados ni movimientos tras una salida.

## Criterios previos y aceptación de la medición

Antes de implementar: root revisa este documento y anexo. Después, sólo con autorización, fuente nueva MCP/readback/hash y revisión independiente. Checks sintéticos de supplied source deberían probar transparencia de hooks y estados: latch capturado previo, consumo pese ocupación/geometría fallida, memo dos should_*, cancelación TTL+rearmado mismo T, salida mismaT sin reentrada, prioridad con plan anterior inviable, episodios/gaps/censura, marks open/pre/close y FINAL. No importar estrategias reales ni datos observados en esos checks.

Antes del único motor: manifiesto desde draft real con contrato/código/versiones y cuenta del ID de medición. Después: comparar ambos snapshots completos ignorando IDs nuevos pero NO diferencias económicas.

Paridad exigida:192 trades ordenados por tiempos y secuencia/origen;31/116/45; iguales side, qty, entrada/salida, opened_at/closed_at, fees, funding y PnL;313 planes seleccionados,121 cancelaciones y82 eventos originales del suplemento; fuente parent/indicadores/config/historia expuesta sin cambios. Timestamps y cantidades deben coincidir en su representación numérica; tolerancia sólo para sumas/reconciliación flotante, declarada antes de auditoría, no para aceptar otro trade o precio. Reconcilia gross-fees+funding=PnL=equityfinal-10000,1151 pagos asociados según diagnóstico, ledger por origen, M1/R11/meses/DD y estado terminal. Comparar fronteras/curvas completas disponibles, no sólo CAGR o un fingerprint numérico.

Si no hay réplica, no se atribuye la diferencia a bloqueo original ni se usan nuevos candidatos para diseñar variantes. Se declara medición no aceptada y se investiga la interferencia o diferencia técnica sin cambiar operativa ni consumir otro motor automáticamente.

## Qué podrá concluir root después

Se podrá responder si existen candidatos geométricos y emisiones frescas adicionales en episodios bloqueados, y si jerarquía o pending explican la selección observada. Si casi todos coinciden con los mismos episodios/filtros, también será un resultado informativo.

Seguirá sin saberse su fill, PnL, sizing futuro sobre otra trayectoria, margen conjunto, hedge exacto o rendimiento con cuotas repartidas. Ningún conteo de oportunidades permite promover una candidata ni sumar rentabilidades. Ésa sería otra pregunta futura, discutida tras comprender esta medición.

Fuentes de contexto: K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md; K1001_BTC_COMPONENT_ARCHITECTURE_FEASIBILITY_20261021.md; BTC_DISCOVERY_P_PROTOCOL_20261021.md; BTC_DISCOVERY_P_MANIFEST_20261021.json y auditoría P de callbacks/expiry. Ninguno queda sobrescrito. Framework/config/parents intactos.
