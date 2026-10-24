# Atribución PAXG: entrada, gestión y exposición direccional

Fecha de registro: 19 de octubre de 2026, America/Montevideo. Estado: protocolo definitivo de alcance previo a código y resultados, según revisión de root. Se requiere revisión del código antes del primer run y paridad de C0 antes de los restantes.

## Pregunta y presupuesto

Se investiga qué aporta la selección de entrada de la referencia PAXG frente a su régimen y su gestión de runners. No se ensayan diecisiete ideas de alpha ni se intenta rescatar R20/R40. La referencia relevante es el retest aislado de PAXG al 1%, no la pauta de fin de semana.

El diseño inicial era32 fulls totales; se añadió ex ante Cq por activo para resolver una diferencia real de frescura de quote entre LIMIT y MARKET. Presupuesto definitivo **34 fulls,17 por activo**. Este protocolo cubre17 PAXG. No hay controles adicionales automáticos fuera de estas filas, no barridos y no elección de seed ganadora. Root revisará código común/diferencias antes de ejecutar; C0 es un gate técnico de reproducción, no una candidata.

Desarrollo2020-10-15 a2025-12-31 exclusiva. Capital10.000USDT, riesgo planificado1%, fee0,00045 por lado en TODAS las órdenes,5x isolated, cap bruto4,4x, sin piramidado, reserva10bps sólo para sizing, warmup240, modo normal. Ruta única PAXG-USDT4h con data PAXG1m. Mismo proxy spot aceptado; sin funding, BTC ni2026. Sólo Jesse MCP, sin scripts, instalaciones, framework, live/paper. Máximo dos backtests y un análisis propios simultáneos; coordinación global con root.

Todas las filas son **long-only** porque la pata PAXG de referencia lo es. Esto es atribución de esa política existente, no quitar shorts perdedores de los experimentos anteriores.

## Fuente y hallazgo de equidad

Fuente inmutable: snapshot del [benchmark aislado](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c), ResearchPaxgRetestControl4h. Se leyó completo y se comprobó igualdad exacta con su código actual; referencia MultiAssetRetestBtcShort4h también leída. Sus únicas diferencias de copia aislada son clase y riesgo1% frente3%; no se modifica ninguna.

La base PAXG no exige M1 exacta al armar LIMIT ni condiciona actualización de trailing a una M1 fresca. Añadir el guard a C0 alteraría su comportamiento y rompería reproducción. Por eso C0 conserva ambas políticas originales; E1/E2/E3 preservan la entrada y las partes no ablacionadas de la gestión. Cq añade M1 exacta **sólo en entrada**, y M/R/U comparten ese guard. Ninguna actualización de trailing se suspende por falta de M1 fresca. E4 añade guard sólo para su nueva liquidación temporal; su stop permanece activo.

Guard de entrada nuevo: último timestamp M1 propio exactamente T−60.000ms, precio finito positivo y paridad con cierre de ruta (rel_tol1e−10,abs_tol1e−8). No inventar quotes, no sustituir por cierre de otra hora. Cq continúa siendo LIMIT a nivel Donchian, con vencimiento original de una4h; el guard de armado no certifica liquidez ni todas las quotes de su posterior fill intrabar.

C0→Cq mide el guard; Cq→M compara políticas de ejecución con la misma decisión elegible por frescura. Aun así no es únicamente una diferencia de comisión o precio: LIMIT puede no llenar, llena en otro momento y ocupa reserva; MARKET entra inmediatamente. Ocupación, muestras y capital posterior cambian endógenamente.

## Matriz de17 configuraciones

| ID | Clase nueva | Propósito | Cambio único o paquete explícito | Contraste |
|---|---|---|---|---|
| C0 | AttrPaxgC0Retest4h | Réplica aislada 1% | Clase únicamente; comportamiento idéntico al snapshot93a161 | Paridad contra benchmark antes de cualquier otra corrida |
| Cq | AttrPaxgCqFreshRetest4h | Control de quote fresca al armar LIMIT | Añade sólo guard M1 exacta/paridad en entrada | C0→Cq identifica efecto de guard de entrada |
| E1 | AttrPaxgE1NoBe4h | Ablación de breakeven | Quita sólo BE; conserva trailing4,2 ATR y tightening5R/8R | C0→E1, política de gestión completa |
| E2 | AttrPaxgE2NoTrail4h | Ablación de trailing | Quita trailing/tightening; conserva BE2,25R y stop inicial | C0→E2, efecto conjunto de dejar correr/ocupación |
| E3 | AttrPaxgE3InitialStop4h | Sin BE ni trailing | Sólo stop inicial2ATR hasta cierre de frontera del motor | C0→E3; alta duración posible, no forzar N |
| E4 | AttrPaxgE4InitialStop72h4h | Stop inicial y expiración | E3 más72h desde fill real; exit debt y M1 propia fresca | E3→E4, duración/ocupación, plazo no garantía de fill |
| M | AttrPaxgMMarketSignal4h | Sustituye LIMIT retest por MARKET | Mismos filtros que Cq; MARKET al cierre, riesgo recalculado al precio | Cq→M, política de ejecución/precio/selección de fill |
| R01 | AttrPaxgRegimeSeed1014h | Reloj hash dentro de régimen | Seed101, sin ruptura/retest Donchian | Familia R conjunta, no escoger seed |
| R02 | AttrPaxgRegimeSeed2024h | Reloj hash dentro de régimen | Seed202, sin ruptura/retest Donchian | Familia R conjunta, no escoger seed |
| R03 | AttrPaxgRegimeSeed3034h | Reloj hash dentro de régimen | Seed303, sin ruptura/retest Donchian | Familia R conjunta, no escoger seed |
| R04 | AttrPaxgRegimeSeed4044h | Reloj hash dentro de régimen | Seed404, sin ruptura/retest Donchian | Familia R conjunta, no escoger seed |
| R05 | AttrPaxgRegimeSeed5054h | Reloj hash dentro de régimen | Seed505, sin ruptura/retest Donchian | Familia R conjunta, no escoger seed |
| U01 | AttrPaxgUnconditionalSeed1014h | Reloj hash sin régimen | Mismo reloj/seed101, sólo calendario/history/ATR/riesgo | Familia U y pareja R/U por seed |
| U02 | AttrPaxgUnconditionalSeed2024h | Reloj hash sin régimen | Mismo reloj/seed202, sólo calendario/history/ATR/riesgo | Familia U y pareja R/U por seed |
| U03 | AttrPaxgUnconditionalSeed3034h | Reloj hash sin régimen | Mismo reloj/seed303, sólo calendario/history/ATR/riesgo | Familia U y pareja R/U por seed |
| U04 | AttrPaxgUnconditionalSeed4044h | Reloj hash sin régimen | Mismo reloj/seed404, sólo calendario/history/ATR/riesgo | Familia U y pareja R/U por seed |
| U05 | AttrPaxgUnconditionalSeed5054h | Reloj hash sin régimen | Mismo reloj/seed505, sólo calendario/history/ATR/riesgo | Familia U y pareja R/U por seed |

Orden fijo: C0, luego Cq/E1/E2/E3/E4/M y familias R01..05, U01..05. Se pueden ocupar dos slots respetando ese orden de lanzamiento; no se decide la cola por rendimiento.

## C0: reproducción obligatoria

C0 copia completa y autocontenida del snapshot93a161 cambiando únicamente nombre de clase. No añade guard, before, cálculo de señales o gestión. Configuración, defaults, calendario, precisión, reservas y órdenes iguales. Se espera35 operaciones, neto546,110572353739 y fees246,608881054834, además de sus timestamps/direcciones/cantidades/órdenes.

Tras el run, comparar snapshots completos: secuencia de entradas/salidas ejecutadas, tipos y timestamps, precios, cantidades, fees, PnL y wallet, además de métricas/curva cuando el contrato lo permita. Igualdad exacta para identidades/eventos discretos; tolerancia1e−8 USDT/precio/cantidad para floats de la misma cuenta, sin relajar para aceptar diferencias económicas. Renombrar clase/IDs de órdenes/sesión no cuenta como discrepancia económica.

Si falla paridad, detener cola y diagnosticar por MCP fuente/configuración/estado de datos/motor antes de cualquier otra fila. No ajustar reglas para imitar estadísticas ni borrar el fallo. Sin fallback de shell/FS/SQL/red.

## Gestión: alcance preciso de E1–E4

La base abre stop inicial a entry_fill−2ATR conocido al plan; guarda best_close desde fill y lo actualiza con cierres4h completos cuando ATR es válido. El trailing es best_close−4,2ATR contemporáneo, multiplicado por0,78 a partir de5R y0,62 a partir de8R. BE se activa con best_close≥entry+2,25R, a entry×(1+2,5fee). La ratchet sólo eleva stop y exige stop<precio. R se refiere a distancia inicial, no a una vela futura.

- E1 elimina únicamente la rama BE. Conserva trailing, tightening, ATR válido, best_close, horarios, condición de ratchet y demás comportamiento.
- E2 elimina trailing y sus dos tightening. Conserva stop inicial y activa únicamente BE con el mismo best_close,2,25R y precio fee-adjusted. Conserva la condición de ATR válido antes de actualizar best_close/gestión, para no introducir otro cambio de reloj.
- E3 mantiene el stop inicial sin ratchet ni TP ni expiración. Puede quedar muchos meses/años y cerrar en frontera por el motor. Eso no es un fallo técnico por sí mismo, ni se obliga a alcanzar cierto N.
- E4 conserva E3 y añade deadline opened_at+72h usando fill real. Comprueba liquidación en decisiones4h; la primera decisión posterior puede llegar hasta casi cuatro horas después de72h, y una quote inválida puede demorar más. Latch de deuda hasta M1 propia válida/paridad, sin retirar stop inicial. No se adelanta artificialmente fill a la hora72.

Cambiar gestión modifica duración, disponibilidad y siguientes entradas. C0/E se interpretan como políticas completas con entradas iniciales definidas por la misma receta; no como una comparación pareada de35 trades idénticos. Se describirá el subconjunto de entradas efectivamente comunes sin generalizarlo al universo.

## M: mismo evento, otra política de ejecución

M conserva todos los filtros de Cq, incluido breakout del canal previo26, entry_boundary<close≤entry_boundary+ATR, close>EMA80, EMA20>EMA80>EMA80[-5], ADX14≥26, RSI14 entre52 y76, rango high−low≤3ATR y soporte de al menos100 velas. La validación original de distancia respecto al boundary se conserva para no modificar elegibilidad.

Después de aprobar esos filtros, entry de plan pasa a close para MARKET. Stop inicial conserva distancia2ATR pero se ancla a fill real. Sizing1%, fees de entrada/stop, nocional/reserva y ledger se recalculan con el precio MARKET. No conservar cantidad LIMIT para forzar coincidencia de exposición. Stop/BE/trailing originales intactos; sin timeout adicional.

## R/U: relojes deterministas emparejados, no hipótesis IID

Semillas fijas101,202,303,404,505. Para cada símbolo y vela, key ASCII exactamente:

`ATTR1|{symbol}|{seed}|{closed_candle_open_time}`

SHA256 de la key; tomar primeros8 bytes como entero big-endian; activar si entero%48==0. No Python hash, no nombre de clase/modo en la key, no futuro, no seed elegida por resultado. Se obtiene aproximadamente probabilidad1/48 bajo una salida de hash uniforme; no se afirma independencia de retornos o de eventos de mercado.

Calcular bit en before en TODAS las velas, aun ocupado o con orden pendiente. Sólo la oportunidad de esa vela puede entrar si la cuenta está libre y demás gates válidos; no conservar deuda de entrada, no desplazar un bit perdido a otra vela. La entrada es MARKET long. Los estados de gestión conservan el código de la base.

R requiere régimen de la base sin Donchian/retest ni la condición close≤boundary+ATR: close>EMA80, EMA20>EMA80>EMA80[-5], ADX14≥26,52≤RSI14≤76 y high−low≤3ATR. También historia≥100, ATR positivo finito, calendario, quote fresca y sizing válido.

U elimina esos filtros direccionales/de rango: únicamente calendario, historia≥100, ATR positivo finito, quote propia fresca/paridad y sizing válido. No exigir finitud de indicadores que U no utiliza. Ledger y share de exposición originales permanecen; aislado significa share1 cuando el soporte/ATR son válidos.

R y U comparten exactamente bit por seed/symbol/bar. Un fill R y uno U no tienen por qué coincidir: estar ocupado o sin margen es endógeno. Comparar por seed no equivale a emparejar todos los resultados. No reequilibrar después la tasa de reloj, holding, años o exposición para igualarlos artificialmente.

## Lectura de resultados y límites de identificación

Registrar las17 sesiones y todos los fallos. Por cuenta: N, neto, fees, antes de fees sobre mismos fills, PF/DD, duración media/mediana/máxima, exposición temporal sobre ventana completa, turnover y neto en bps por nocional de entrada, costes extra5/10bpsRT estáticos sobre todos los fills, años/cohortes, concentración y terminal. Diferenciar tiempo con posición, margen/nocional y capital-tiempo; una proxy basada en nocional de entrada no es exposición MTM exacta.

Las cinco semillas se reportan TODAS, con rango/mediana y comparación emparejada de políticas por seed. No seleccionar mejor seed, no construir p-values IID ni presentar cinco caminos como test formal de ausencia de alpha. Sesgo de ocupación y número desigual de operaciones permanecen explícitos.

Entradas comunes defendibles se identifican por símbolo/dirección/timestamp ejecutado y sus diferencias de precios/tamaños; fills LIMIT de otro momento no se fuerzan a coincidir con MARKET por proximidad temporal. No afirmar que snapshots de trades revelan todas las oportunidades, estados rechazados o cotizaciones faltantes.

Regularidad y retorno de calendario requieren MTM a cierre UTC coordinado por root, no año/mes de cierre de trades ni Portfolio00:01. E3 puede contener grandes cierres sintéticos de frontera: conciliar terminal y señalar que no certifica liquidez real. No sumar curvas aisladas como cartera.

No hay gates de promoción automática en esta etapa de atribución. Rentabilidad de un control aleatorio o mejora al quitar una gestión genera una pregunta interpretativa bajo desarrollo seleccionado, no una estrategia aprobada ni permiso para2026.

## Código y revisión antes de ejecución

Diecisiete clases AttrPaxg... autocontenidas generadas desde el snapshot completo, sin imports de otra estrategia ni módulos comunes externos. C0 sólo renombre; para revisión se muestra fuente base una vez y diferencias completas por clase. Readback íntegro y comparación mecánica antes del primer run. Toda constante/umbral tiene origen en base o contrato anterior.

Primero root revisa código; después C0 y auditoría de paridad; sólo si pasa se lanza la cola restante. No hay código ni corridas de esta tanda al guardar este protocolo.

## Adenda de revisión de código, anterior a resultados

Root verificó C0 actual exacto al snapshot salvo nombre y autorizó únicamente su ejecución y gate de paridad. Antes del resto16 se sustituye el helper de quote de Cq/E4/M/R/U por búsqueda exacta de T−60.000ms mediante np.searchsorted sobre timestamps M1, verificando índice dentro del array y timestamp idéntico. Esto evita asumir que c[-1] es la M1 correcta si la API expone otra vela en el borde. Close positivo/finito y paridad con self.price se conservan. C0/E1/E2/E3 permanecen intactos.

Análisis adicional predeclarado: sum(entry_notional×holding_hours)/(10.000×window_hours) como aproximación de exposición nocional-tiempo a PRECIO DE ENTRADA, no MTM. Pares de fills realmente comunes también comparan PnL/entry_notional; no es causalidad pura por ocupación y capital endógenos.

## Diagnóstico secundario aprobado antes de resultados M

Además del pareado primario por timestamp de fill, se permite vincular símbolo/dirección y EXACTO created_at de la orden de entrada ejecutada cuando sea inequívoco uno a uno. Se excluyen explícitamente claves ambiguas y trades con múltiples órdenes de entrada; se informa cuántos. Medir diferencia de precio, retraso created_at→opened_at y PnL/entry_notional. Es una intersección seleccionada de decisiones que terminaron llenando en ambas políticas, no el universo de oportunidades ni un efecto causal puro. No se aproximan fechas por proximidad ni se añaden fulls.
