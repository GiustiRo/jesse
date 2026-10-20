# Diseño previo: SPY y cambio de mes
Fecha: 18 de octubre de2026. Solo fundamento y diseño. No se creó fuente ni draft, no se lanzó backtest ni se importaron datos.

## Antecedentes primarios anteriores a la muestra
[Lakonishok y Smidt,1988, Are Seasonal Anomalies Real?](https://academic.oup.com/rfs/article-abstract/1/4/403/1566965) estudia90años de DJIA y documenta patrones persistentes alrededor del cambio de mes, entre otras estacionalidades.

[McConnell y Xu,2008, Equity Returns at the Turn of the Month — PDF del autor](https://business.purdue.edu/faculty/mcconnell/publications/Equity-Returns-at-the-Turn-of-the-Month.pdf) examina1926–2005 y comprueba persistencia en1987–2005. La ventana publicada abarca el último día bursátil y los tres primeros del siguiente mes, no cuatro días de calendario a cada lado. Para1987–2005 el índice CRSP ponderado por valor registra aproximadamente15bps diarios en esas cuatro sesiones. No es una predicción de SPYCFD2020–25. El trabajo no atribuye el patrón a compras de fin de mes medidas por volumen o flujos netos de fondos; no debe presentarse una explicación de cobros/aportes como hecho establecido.

[Etula, Rinne, Suominen y Vaittinen,2020, Dash for Cash](https://academic.oup.com/rfs/article/33/1/75/5494694) vincula necesidades institucionales de liquidez, liquidación de operaciones y presión de precios alrededor del fin de mes. Apoya investigar un mecanismo de calendario/financiación de liquidez, pero no prueba que una ventana uniforme4/4calendario sea óptima ni que sobreviva en un CFD.
Todos estos trabajos existían antes de la muestra de desarrollo; nuestra selección actual sigue siendo adaptativa y no convierte2020–25enOOS.

## Novedad respecto del inventario local
No se encontró una estrategia local de turn-of-month pasivo en SPY. La rotación mensual elige un ganador por momentum de3meses; las guardas mensuales gestionan giveback; la propuesta overnight se retiró sin simular. Ninguna es esta exposición predecible por fechas. No se afirma novedad mundial.

## Diferencia metodológica que debe aprobar el orquestador
La literatura clásica usa días bursátiles y retornos entre cierres. Una réplica precisa necesita un calendario bursátil conocido exante y convención de entrada antes del retorno del último día. No se puede usar el último día CON COTIZACIÓN observado retrospectivamente como si fuera conocido al decidir.
El proyecto no tiene un calendario NYSE validado y no debemos inferir festivos futuros de huecos del archivo. A las16UTC tampoco estamos en el cierre regular16NY.
Por ello, la receta operable propuesta es una ADAPTACIÓN DE CALENDARIO Y RELOJ, no una réplica exacta: cuatro últimos días de calendario más cuatro primeros, observaciones y ejecución al callback16UTC cuando exista la cotizaciónM1propia fresca. Cuatro es fijo antes del test, tomado como bloque de exposición aproximado al cambio de mes, sin respaldo de que sea el óptimo de la literatura. Si se exige réplica exacta, posponer hasta disponer de calendario exante; no disfrazar4/4como la regla publicada.

## Receta única para posible revisión
- Una rutaSPY-USDT4h, Binance Perpetual Futures, proxy SPXCFDBID/10; long solamente. Una rutaM1legítima puede verificar la frescura, siguiendo el patrón ya auditado de rotación.
- Bloque de entrada: últimos cuatro días de calendario del mes. En el primer callback hábil16UTC con M1propia cerrada exactamente en ese momento, entrar MARKET. Si no hay ninguna cotización fresca en ese bloque, omitir ese turno; no simular una entrada pasada.
- Mantener la posición hasta el primer callback propio16UTC con cotización fresca después del cuarto día de calendario del mes siguiente. Los días sin cotización difieren la salida; no inventar cierres ni festivosNYSE.
- Una sola entrada por turno de mes. Un stop consumido deja cash hasta el siguiente turno; no reentrar repetidamente en la misma ventana.
- Stop protector fijo3% bajo el fill real. Sin TP, trailing, filtro de precio, indicador de volumen ni condición por meses que perdieron.
- Horarios con API pública de Jesse: ventana de decisiónUTC16 mediante la vela4h que abre12, díasMon–Fri explícitos; gestión protectora nunca suspendida. El calendario del día de mes es una condición exante, no una selección retrospectiva de cotizaciones.
- Capital10k, riesgo máximo3%portrade/8%agregado,5xaislado,capnocional1x,margen90%,fees0.00045porlado y reserva0.001de sizing. Con distancia3%, el tamaño esaproximadamente0.94x, no3%sinfeesni1xautomático.
- Fuente y señales2020-10-15→2025-12-31exclusivo,normalreplay,warmup240.2026reservado. Cash con rendimiento0; sin nuevas descargas, instalaciones, framework ni forecastmacrorevisado.

## Costes, muestra y contabilidad
En torno a12entradas/salidas anuales,9bpsRTimplican aproximadamente1.08%anual de coste por unidad de nocional constante, antes de otros costes. Es un hurdle diferente de pagar9bps todos los días; no justifica aplicar a SPYCFD el promedio histórico del paper.
El proxyBID omite spread/impacto/funding y no equivale a ETF con dividendos. La ausencia de quotes en un festivo histórico tampoco garantiza que el feed24/7final omita ese día: adaptaciónlive pendiente.
Cada turno cruza dos meses. Rentabilidad por trade o turno NO equivale a meses positivos de cartera. V4debe marcar la posición abierta al cierre de cada mes; mostrar activos, todos los meses, períodos completos, cash inicial/final y fechas diferidas. No mover PnL entre meses para conseguir65%.
Muestra máximaaproximada60turnos en cincoaños; intervalos de incertidumbre amplios y exposición potencial a pocos shocks. Un resultado prometedor necesita costes y atribución temporal, no una rejilla de fechas.

## Falsación y estado
Hay fundamento suficiente para una hipótesis de calendario distinta, pero NO para asegurar causalidad de aportes ni para llamar a4/4una réplica exacta.
El orquestador debe decidir si acepta esta adaptación explícita o prefiere una réplica futura con calendario validado. No hay permiso de ejecución en este documento.
Si el único componente no genera esperanza neta útil, descartar sin combinar ni afinar días/weekday/mes. Si sobrevive, medir cartera real antes de promocionar. Objetivos65–70%mesesactivos/80%trimestres/DD<=25%y2026sellado permanecen.
