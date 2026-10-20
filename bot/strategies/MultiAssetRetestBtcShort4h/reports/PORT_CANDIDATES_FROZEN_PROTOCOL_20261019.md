# Portfolio de candidatas — protocolo previo — 2026-10-19

Pregunta: ¿las mejoras aisladas PAXG MARKET y SPY MECH01/MECH05 mejoran una cuenta compartida con BTC original? Exactamente cuatro backtests, sin optimización ni ampliación adaptativa.

| ID | BTC | PAXG | SPY |
|---|---|---|---|
| CONTROL | Original long y short | Cq retest fresco | Cq retest fresco |
| A | Igual | MARKET central congelada | Igual al control |
| B | Igual | MARKET central | MECH01 sólo segunda oportunidad |
| C | Igual | MARKET central | MECH05 posteriores con MARKET |

Clases copiadas e inmutables para esta ronda: PortCompareBtc4h, PortComparePaxgRetest4h, PortComparePaxgMarket4h, PortCompareSpyRetest4h, PortCompareSpySecond4h, PortCompareSpyMarket4h. Mismo ledger compartido phase2_reservations y _committed/_capital/_volatility_share en todas. SóloBTC tiene shorts activos por su guard de símbolo. El orden de rutas siempre BTC/PAXG/SPY; M1 auxiliares de los tres. No sumar curvas individuales.

## Riesgo y control justo

10.000USDT COMPARTIDOS por cartera, no por activo. Riesgo1% por trade,8% agregado planificado, techo nocional4.4x, isolated5x, sin piramidado, fees.00045 por lado para todos los tipos. Reserva.001 sólo sizing, no fricción simulada. Pesos ex ante inversos a ATR relativo de todos los activos, incluso inactivos, heredados del código común; pendientes reservan riesgo/nocional.

La referencia histórica original de cartera usaba3% por trade y no es el control numérico de esta comparación. Se normalizan las cuatro a1%, siguiendo la investigación reciente y sin subir exposición. BTC preserva exactamente reglas de entrada/salidas/indicadores, cambiando sólo TRADE_RISK3%→1% en la copia. PAXG/SPY control son las referencias Cq frescas de atribución; por ello no llamar a CONTROL réplica exacta de la cartera antigua de3%.

Misma ventana2020-10-15→2025-12-31 exclusiva, último día30/12;2026 reservado. Warmup240, normal engine fast/debugfalse. SPY historia UTC Mon–Fri00–20 y entrybaropen00–16, gestión original siempre; BTC/PAXG sin calendario. Señales/gestión/quote guards preservadas por copia. No funding, fuentes nuevas, frameworks/config global, instalaciones, reinicios o live/paper/Pi/research_scripts.

## Instrumentación pasiva

Se añaden _record_capacity y terminate a las seis copias: counters en vars, una línea JSON PORT_CAPACITY por ruta vía jh.debug al terminar. Mide sólo planes que llegaron a sizing estando flat y sin pending. Cuenta recortes por riesgo agregado, nocional/peso y margen, intentos por debajo de objetivo, capacidad nula y rechazo por redondeo de lote. Las categorías se solapan y no se suman como total de trades omitidos.

No ejecuta decisiones, no altera quantities, no reevalúa señales ocupadas y no afirma que un plan rechazado hubiera llenado. Este límite es material: no hay contrafactual de todas las oportunidades. Validar que al quitar diagnóstico/imports/clase/riesgo BTC la fuente retorna exactamente la base antes de correr.

## Auditoría y lectura de resultados

Dos backtests simultáneos: CONTROL/A, luego B/C. Configuración por draft, sin tocar configuración global. Snapshots íntegros de las tres fuentes en cada sesión, readback previo, título PORT CANDIDATES CONTROL/A/B/C.

Comparaciones A−CONTROL (cambio PAXG), B−A y C−A (cambio SPY sobre PAXG MARKET), B vs C. El tamaño/ocupación y capital compartido son endógenos; BTC puede cambiar sus fills/PNL sin cambiar sus reglas. Separar contribuciones por activo y BTC long/short; no atribuir exclusivamente todo incremento a la pata editada.

Métricas N/neto/fees/PF/Sharpe/CAGR/DDmotor; fills/qty/fee/PNL/wallet/terminales; exposición temporal/nocional-tiempo, costes estáticos5/10bpsRT, concentración exbest/ex3 y diagnóstico conjunto como sensibilidad. Auditar MTM diarioUTC, meses activos/totales/completos, Q completos, correlación y co-pérdidas de contribuciones mensuales, peores meses/Q y drawdowns. Identificar participación en periodos malos y contadores de límites. No llamar cohortes por cierre rentabilidad de calendario.

Criterios históricos de cartera siguen:>=65%meses ACTIVOS positivos (aspiración70%),>=80%Q positivos y DD no peor que−25%, rentabilidad resistente a fricción. Mostrar denominadores completos (61meses/19Q) y fronteras parciales aparte, sin rebajar criterios. Ninguna selección automática por máximo de neto. No OOS limpio tras reutilizar2020–2025.

Referencias aisladas se usan sólo para atribución y selección fijada: PAXG M8b43d9d2..., SPY MECH01527a0334.../MECH059205534b... y Cq0fc6e1f7.../58877a96.... No reruns aislados ni nueva exploración BTC. Fuentes originales preservadas.
