# PAXG: diagnóstico y protocolo de divergencia contextual

18/10/2026. Protocolo aprobado e implementado para revisión de fuente: sin borradores, backtests ni trabajos de análisis nuevos. Se usan las velas disponibles de BTC, PAXG y SPY. No se retoman COT, VIX, funding ni descargas. La referencia y 2026 permanecen intactos.

## Diagnóstico y relación con el inventario

La referencia tiene 35 longs PAXG y aproximadamente 4.632,27 USDT de beneficio neto. El mejor trade representa el 90,04% del neto; los tres mejores, el 200,13% del neto y el 66,67% de la suma de ganadores. Es concentración compatible con seguimiento de tendencias, no prueba de sobreajuste ni permiso para eliminar operaciones.

Durante los 28 meses negativos de cartera, PAXG aporta −6.538,96 USDT MTM; durante los trimestres negativos, −2.496,60. Es contabilidad condicionada al signo conocido al final. No usaremos esas fechas para construir un filtro retrospectivo. Su rol actual replica breakout/retest tendencial: no define protección contemporánea frente a BTC y SPY.

Se releían por MCP Sleeves, Blend, Relative, RetestHedge, RiskOff, TurtleDaily, AllocEqualRisk y RotateMonthlyMomentum, además del diagnóstico y la atribución centrales. No se propone repetir MR, shorts PAXG, Donchian, Turtle o un cambio de pesos.

RiskOff ya observaba debilidad de BTC/SPY y resiliencia de PAXG para habilitar shorts BTC/SPY. Esta propuesta comparte esa premisa, pero controla directamente PAXG long/cash, sin breakout ni ranking mensual. El cambio de rol es material; no demuestra una ventaja independiente. Si root considera insuficiente esa diferencia, puede retirarla antes de implementar.

## Una receta predeclarada

Clonar la referencia y reemplazar sólo la política PAXG. BTC long/short y SPY long conservan sus reglas. PAXG tiene una posición long o cash; no conserva el breakout antiguo como fallback.

Para cada activo, calcular R = P(T) / P(T−7 días) − 1. Son siete días calendarios exactos, fijados antes de resultados en sustitución del borrador de 20 observaciones comunes. No se probarán horizontes vecinos.

El contexto está activo si R_BTC < 0, R_SPY < 0 y R_PAXG > 0. No hay umbral adicional de magnitud, correlación, ranking, ADX, RSI, EMA o canal. La oportunidad hipotética es una divergencia positiva observada de PAXG mientras ambos activos de riesgo caen en el mismo horizonte. No mide flujos hacia oro ni constituye una cobertura demostrada.

Entrar MARKET en la transición de falso a verdadero si PAXG está flat y hay riesgo/margen disponible. El evento se consume en la decisión aunque no produzca orden o fill. No se guarda para entrar después ni se reentra tras un STOP mientras el contexto siga verdadero. El primer contexto válido puede compararse con el estado inicial falso, sin retrooperar el tramo de memoria.

Conservar el riesgo PAXG máximo original del 3%, el agregado del 8%, el techo bruto de 4,4x, 5x aislado, la cuota inversa ATR de las tres rutas, margen del 90%, fees, reserva y precisión originales. Esto sustituye la sugerencia inicial del 1% para no confundir una mejora con menor riesgo.

Stop protector fijo de 2 ATR14 PAXG 4h, conocido al planear y anclado al fill. Se conserva la distancia inicial original, en lugar de los 3 ATR del borrador. Sin target, breakeven, trailing o nueva caducidad. La nueva política cambia entrada y salida de contexto; no es una prueba aislada de un único filtro.

Salir MARKET sólo cuando una nueva actualización válida muestre contexto falso, usando cotización propia fresca. El STOP permanece activo siempre, incluso en fin de semana. Si no puede actualizarse el contexto, esperar una actualización real para la salida discrecional: ausencia de datos no significa falso ni una nueva oportunidad.

## Reloj causal común

Decidir el contexto sólo en PAXG a las 16:00 UTC de lunes a viernes. Fijar T = hora de decisión menos cuatro horas: las 12:00 UTC de ese día. Usar exactamente T y T−7 días en los tres activos. El bloque de retraso deja completados todos los callbacks de las 12:00 antes de decidir, sin depender del orden de rutas a las 16:00.

Cada extremo exige una vela 4h que cierre exactamente allí y una M1 propia con open + 60.000 ms igual a ese extremo. El cierre M1 debe coincidir con el cierre 4h; los tres activos comparten los mismos timestamps. No usar nearest, interpolación ni forward fill.

Para emitir una actualización a las 16:00, SPY también debe tener M1 fresca en esa decisión y PAXG debe tener precio propio fresco para ejecutar. Si un extremo falta por festivo/gap, o falta SPY actual, omitir toda la actualización. No buscar un T antiguo, imputar retorno cero o cambiar el estado por ausencia. No se generan señales nuevas en fin de semana.

Acumular snapshots verificados desde el inicio del run. Hasta disponer del par exacto separado siete días, PAXG permanece cash. Ese startup cuenta en los 63 meses y limita la comparación inicial. Registrar las fechas reales sin inventar el primer contexto o fill.

El precio T tiene cuatro horas de retraso al decidir. No se presenta como respuesta instantánea a un shock de las 16:00. No liquidar otra ruta ni usar una quote SPY antigua como señal nueva.

## Complementariedad, muestra y costes

La pregunta principal es si el nuevo rol mejora la cuenta compartida, no si PAXG aislado alcanza 65/80. Sus posiciones alterarán capital, cantidades y oportunidades de las demás patas. No sumar curvas independientes ni interpretar diferencias en dólares como un contrafactual exacto.

Medir contribución PAXG, exposición, fees, concentración, efecto en BTC/SPY y calendario MTM. Informar meses rescatados/perjudicados, los 63 meses y 21 trimestres, y períodos completos. Una mejora del denominador activo por pasar a cash no basta. La pérdida de una gran tendencia es un coste de oportunidad que no puede reponerse retrospectivamente.

No se estimó la muestra mediante un job nuevo. Las condiciones conjuntas y los extremos exactos pueden dejar pocos episodios. Una muestra escasa no demuestra estabilidad ni autoriza acortar el horizonte para fabricar operaciones.

PAXG es un proxy de precio Binance Spot usado en una ruta Perp de simulación. No es oro/COMEX nativo ni un instrumento final validado. Liquidez, spread, base USDT, negociación 24/7 y financiación siguen pendientes. La fee de 0,00045 por lado para todo tipo de orden y la reserva de sizing no acreditan slippage realista.

## Descarte antes de resultados

- Un fallo de reloj, memoria o ausencia total de snapshots verificables es técnico, no una conclusión económica.
- Si no aporta contribución útil o mejora conjunta, descartar esta receta sin rejilla de horizonte, ATR, stop o riesgo.
- Si sólo mejora meses activos al aumentar cash, sin mejorar calendario completo y trimestres, no promover.
- Si recorta la gran tendencia y no compensa la cartera, aceptar el fallo; no añadir después un fallback tendencial.
- Una pata negativa podría ser útil sólo si mejora la cuenta real; no imponer signo positivo a cada cobertura, ni llamarla cobertura antes de comprobarlo.
- Con pocos episodios, declarar muestra limitada y conservar los umbrales.

Ventana común: 2020-10-15 a 2025-12-31, fin exclusivo, modo normal. Se mantienen 65–70% de meses activos positivos, 80% de trimestres y DD no peor que −25%. Desarrollo adaptativo ya observado; 2026 sellado. Root autorizó implementar esta receta para revisión. No hay autorización para borradores o corridas; ese siguiente paso permanece pendiente.


## Implementación para revisión, antes de cualquier ejecución

Fuente: strategies/AnglePortfolioPaxgDivergence4h/__init__.py. Guardada por MCP y releída exactamente. Se comprobó identidad textual de 16 métodos originales; los tres despachos PAXG preservan íntegro el cuerpo original para BTC/SPY. Retirar helpers, constantes, imports y despachos nuevos devuelve la fuente baseline completa, ignorando sólo un salto de línea final.

No se presupone memoria M1 de siete días: before PAXG captura únicamente quotes M1 frescas de los tres activos a las 12:00 y las guarda en su propia memoria durante al menos ocho días. No consulta en ese callback el cierre 4h de SPY todavía pendiente. A las 16:00 valida los cierres 4h exactos de T y T−7d contra aquellos registros; SPY y PAXG actuales deben ser frescos. Los futuros drafts necesitan data_routes M1 existentes de los tres símbolos, sin nuevas importaciones.

La transición se procesa en before aunque exista posición o entrada pendiente. Además del pulso de timestamp, se congela su admisibilidad en ese instante: un evento recibido con posición/pending no puede rearmarse si el estado se libera después en el mismo callback. La ausencia de datos no cambia el contexto anterior. Una salida pendiente sólo nace de un falso válido y se conserva hasta un cierre con quote propia; el stop no se suspende. No hay trailing PAXG.

Telemetría acotada: contadores acumulados, primer/último callback y contexto, más hasta ocho muestras con timestamps de decisión y ambos extremos, precios, retornos y estado. Logs acumulados hasta cada cierre de año y before_terminate con etiqueta counts_preterminal; no listas por minuto ni totales terminales inventados. Contadores de ocupación/eventos son diagnósticos, no poblaciones independientes que deban sumarse sin revisar su definición.

No se creó draft ni se ejecutó nada. Root y revisión independiente examinarán fuente/protocolo antes de decidir prueba técnica/económica. BTC/SPY conservan sus reglas y prioridad, no necesariamente sus cantidades o resultados posteriores.


### Ampliación diagnóstica previa a la primera corrida

Tras revisión independiente aprobada, root pidió auditar cada entrada potencial real: se añade un log EVENT por transición, y FALSE_TO_EXIT_DEBT al nacer una deuda de salida, con timestamp de decisión, ambos extremos, retornos y flags allowed/open/pending. No se limita a las primeras ocho muestras, que podrían corresponder sólo a contextos falsos. La etiqueta de cierre de año pasa a CUMULATIVE_THROUGH_YEAR_END para no presentar contadores acumulados como anuales.

Sólo cambian logs y etiquetas. La reversión textual de esos añadidos devuelve exactamente la fuente anterior; readback confirmado. Sin cambio de reglas, ejecución, ventanas, sizing o estado; sin drafts ni runs creados por esta ampliación.
