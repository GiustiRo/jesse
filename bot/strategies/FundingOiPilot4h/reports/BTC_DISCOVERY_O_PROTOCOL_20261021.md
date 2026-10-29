# Tanda O: orden de extremos dentro del día BTC

Registro previo a resultados O y fijado sin consultar el resultado de N: 2026-10-21 19:29:55 UTC. Esta preparación no crea drafts, backtests ni jobs de análisis. La ejecución económica esperará el cierre de N y los dos slots libres, después de checks, revisión y manifiesto de fuentes/configuración.

## Pregunta y dos políticas

¿Un día que recupera una excursión interna predice continuidad mejor que el signo de su vela diaria por sí solo? Se compara REPAIR contra BODY con la misma dirección, protección y admisibilidad de datos. La señal usa el orden temporal de los bloques que contienen los extremos diarios, información que una vela OHLC diaria no conserva. No supone conocer el orden de precios dentro de una vela 4h.

BODY opera el signo del cuerpo diario en cada día admisible. REPAIR opera ese mismo signo sólo cuando el máximo precede al mínimo en un día positivo, o el mínimo precede al máximo en un día negativo. En el primer caso hubo un extremo alto seguido por un extremo bajo y recuperación al cierre por encima de la apertura; el espejo describe una caída final tras un extremo alto tardío. La interpretación es una hipótesis de reparación temporal, no evidencia de inventario real, flujo o causalidad económica.

La selección de esta pregunta no depende del PnL de N y no modifica sus padres ni recetas. Ambas políticas se evaluarán por separado y contra objetivos absolutos; superar al control no basta.

## Antecedentes exactos revisados

- strategies/N204ExperimentalR402/__init__.py: rango de doce barras congelado, dos cierres por encima y tercero de vuelta dentro, suplemento short de 48h. Es una aceptación fallida de barrera previa; cambiar sólo 4h por diario no justificaría otra receta. O no utiliza canal ni cierres fuera/dentro de un nivel.
- strategies/OrchLateralFailedRange4h/__init__.py: rechazo de rango20 con filtro ER y objetivo centro. O no es ese fallo de rango ni una variación de sus umbrales.
- strategies/OrchManageTurtleDaily/__init__.py: ruptura de 55 días y salida de canal10 días. strategies/OrchShortDailyPullback4h/__init__.py: régimen SMA200 diario y recuperación fallida EMA20 4h. strategies/OrchRotateMonthlyMomentum4h/__init__.py: momentum de tres meses y rotación. La cadencia diaria no convierte O en una transferencia de estos mecanismos.
- strategies/AngleCombinedBtcEventClock1m/__init__.py: eventos de cambio de dirección por distancia ATR con macro y operativa basal. No compara el orden de los extremos de un día cerrado.
- strategies/R40SpyRangeCloseInformation/__init__.py: relación entre variación de cierres y estimador de rangos; no orden de máximo/mínimo. strategies/R20SpyCashInventoryRecovery/__init__.py: gap cash e inventario con objetivo en apertura; no el mismo predicado temporal y no una transferencia a horarios BTC.
- H, strategies/BtcResearchR12WickBase1m/__init__.py: sumas de geometría de ocho velas y desplazamiento pequeño. Las sumas no codifican el orden intradiario de los bloques extremos.
- I, strategies/BtcResearchR12ParticipationBase1m/__init__.py: impulso S y devolución B con fase de volumen y baselines horarios. O no exige impulso ATR, retorno porcentual de dos barras ni secuencia de volumen.
- E usa excursiones de cierres maduros y recuperación de mitad del trayecto; F variación/bipower; G AR de retornos; M etiquetas maduras por geometría; N composición de máquinas congeladas. O pregunta por trayectoria dentro del día con control que mantiene el mismo signo de cuerpo.

No se encontró equivalente económico de este predicado en las fuentes revisadas. No se afirma novedad universal, independencia estadística ni que los antecedentes negativos refuten familias completas. El histórico se reutiliza intensamente.

## Reloj, datos y señal exacta

Ruta BTC-USDT 1m para observación/ejecución; datos BTC-USDT 4h. Warmup240 barras4h. Sólo se considera entrada cuando T es múltiplo exacto de 24h UTC. Es un reloj de agregación de datos de BTC continuo 24/7, no un calendario de mercado ni exclusión de fines de semana.

En T tomar exactamente quince OHLC4h cerrados, consecutivos y alineados: última apertura T−4h y último cierre igual al precio BTC actual. Las seis últimas barras forman íntegramente el día [T−24h,T), con aperturas T−24h+4h*j para j=0..5. Apertura diaria O=Open de la primera; cierre diario C=Close de la sexta; H=máximo de High; L=mínimo de Low.

Admisibilidad común:
1. Precios OHLC finitos, positivos y coherentes; reloj exacto y sin huecos.
2. Si C=O, día doji: no entrar en ninguna política. No se agrega umbral de tamaño del cuerpo.
3. H debe aparecer en exactamente un bloque y L en exactamente uno. Empates de cualquier extremo rechazan ambas políticas; no desempatar escogiendo primera/última aparición.
4. Los dos bloques extremos deben ser distintos. Si ambos extremos caen en la misma4h, rechazar ambas políticas porque su orden interno no está identificado.
5. Volumen no interviene en ninguna señal ni comparación: cero o NaN en la columna volumen no selecciona una política si los OHLC son válidos. No se interpreta como flujo ni se imputa un dato usado por la señal.

D=+1 si C>O; D=−1 si C<O. BODY admite todo día válido y opera D. REPAIR admite sólo (D=+1 y índiceH<índiceL) o (D=−1 e índiceL<índiceH), y también opera D. No invierte retrospectivamente el signo ni escoge el mejor lado o año. Se registra label repair/body_only con los índices observados.

Cada día es un evento nuevo, aun si repite dirección o label del día anterior. No se exige cruce de estado. Oportunidad consumida si ocupado o con entrada pendiente, sin cola, sin reversión y sin reentrada en el mismo cierre de una salida. Todas las decisiones usan el día ya cerrado; no operar retroactivamente en sus extremos.

## Protección, costos y medición comunes

ATR14 simple de las quince OHLC4h actuales, incluyendo barras del día ya cerrado. Stop inicial2ATR4h congelado al decidir y colocado desde fill real; TP2R=4ATR4h; salida máxima48h desde opened_at en cierres4h. La entrada es diaria pero la protección conserva la unidad4h común, elegida antes de resultados. No se usa ATR diario ni se cambia plazo por política. Protecciones intrabar según motorM1. Target y stop pueden salir del rango del día de señal: se prueba persistencia posterior, no un objetivo al extremo diario.

Sizing helperR10 fee-aware con objetivo2% por trade, margen90%, floor8; una posición BTC sin pirámides. Límite agregado6% y isolated3x fijos. Funding/gaps pueden superar la pérdida prevista, que no es garantía de riesgo máximo.

BTC-USDT Binance Perpetual Futures, [2020-10-15,2026-01-01) UTC; desarrollo observado, no OOS nuevo. Capital virtual10000. Fee0.00045 por lado, taker con descuento según supuesto confirmado por usuario; fundingBTC histórico ON, aplicado y verificado, snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 con marcas proxy declaradas. Slippage modelado0. Sin estrés, variantes de riesgo/leverage/capital, nuevas pruebas económicas2026, imports, ML/HMM, research_scripts, instalaciones, reinicios, configuración global, live/paper oPi.

Observador R11 congelado: wallet+PnL abierto cadaM1 y fill; fronteras00:00UTC después del funding y antes de decisiones según convención por fase. No es agrupación estricta de eventos por mes. DD M1+ejecuciones no identifica todos los extremos intraminuto. Meses calendario inactivos se incluyen en la mediana. No se alteran fuentes de resultados previos.

## Presupuesto, puertas y cierre

Exactamente dos corridas económicas nuevas, una por política. Hasta dos reemplazos exclusivamente por errores técnicos documentados, no por rentabilidad. Máximo dos motores globales y un análisis propio simultáneo. La economía O espera N terminal y los slots libres; preparación no ocupa motores ni jobs. No barrer resolución de bloques, empates, tamaño del cuerpo, extremos, umbrales o protección después del resultado.

Gatesr9 intactos: CAGR neto base>=30%, PF>=1.2, DD<=25% (objetivo20%), >=65% de meses completos activos positivos, >=80% de trimestres completos positivos, mediana de retornos de meses calendario completos>0 incluyendo inactivos, neto aritmético retirando los dos mejores meses>0. N>=100 es suficiencia operativa preliminar, no potencia ni confianza por conteo. Aspiraciones40–50%+ yM70 conservadas. Falla económica=>NO_CUMPLE; economía favorable con muestra/medición insuficiente=>INCONCLUSA. Cumplir base no autoriza operar ni estrés automático; estrés requiere candidata y acuerdo conjunto.

Antes de economía: AST y checks de seis barras/día cerrado, prefijos/futuro/gaps, signo espejo, doji, empates, extremos en mismo bloque, orden cambiado conservando OHLC diario, admisibilidad compartida y sizing heredado. Revisión separada, readback/hash y manifiesto de formularios reales antes de ejecutar. No se crean resultados ficticios durante preparación.

Después: auditoría snapshots completos bruto−fees+funding=PNLsum=equityfinal−10000 con tolerancia1e−6USDT. Verificar2.741.760 marcasM1,63intervalos/62meses/20Q y telescopía mensual. Guardar todos los resultados y fallos con reportesMCP/Hub inmutable, archivos primero e índice último. Si falla, cerrar presupuesto y vecinos locales; continuar otra pregunta material dentro del objetivo autónomo sin rebajar metas.
