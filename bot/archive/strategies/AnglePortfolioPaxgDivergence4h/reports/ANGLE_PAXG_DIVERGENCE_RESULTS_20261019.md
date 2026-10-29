# Resultado individual: divergencia contextual PAXG, celda 10

[Backtest completo en el dashboard](http://localhost:9200/#/backtest/af7161bf-00cd-49a9-b3aa-385fd301396d).

## Decisión individual

La sustitución de PAXG por long/cash contextual no mejora la cartera de referencia: baja CAGR, empeora drawdown y reduce meses positivos. Se descarta esta receta individual sin ajustar horizonte, stop, riesgo ni añadir fallback. La celda combinada 11 tiene una prueba predeclarada propia; este informe no anticipa su resultado.

Desarrollo adaptativo 2020-10-15 a 2025-12-31, fin exclusivo, modo normal. 2026 permanece reservado. Protocolo previo: ANGLE_PAXG_ROLE_PROPOSAL_20261018.md, en esta misma carpeta. Root autorizó y lanzó esta prueba después de revisión de fuente e independiente; no hubo nuevas corridas ni trabajos durante esta auditoría.

## Receta y alcance

Clon de MultiAssetRetestBtcShort4h; sólo se reemplaza PAXG. Las reglas BTC long/short y SPY long se conservan, pero capital compartido altera cantidades y oportunidades. No se afirma que sus resultados debieran ser idénticos.

PAXG entra MARKET cuando aparece la transición BTC 7d negativo / SPY 7d negativo / PAXG 7d positivo. Extremos exactos comunes a las 12 UTC; actualización hábil a las 16 UTC, memoria de snapshots con prueba M1 fresca y paridad 4h. Sin imputación ni eventos en fin de semana. Stop fijo 2 ATR14 anclado al fill; salida por nueva observación válida de contexto falso. El evento se consume aunque no sea operable; faltantes no resetean estado.

Riesgo original máximo 3% por operación / 8% agregado, cuota inversa ATR de tres rutas, gross 4,4x, aislado 5x. Fee aplicada 0,00045 por lado para todo tipo de orden. La reserva de sizing no es fricción adicional aplicada.

PAXG es proxy Binance Spot en una ruta Perp simulada. No es COMEX nativo; no se demuestra causalidad macro, protección de cartera, financiación ni liquidez final del instrumento.

## Resultado económico y calendario

| Medida | Celda PAXG 10 | Referencia |
|---|---:|---:|
| CAGR | 26,041647% | 28,829387% |
| DD de la sesión | −16,094290% | −14,890506% |
| Neto USDT | 23.423,356695 | 27.461,463375 |
| Meses activos positivos | 32/63 = 50,79365% | 33/61 = 54,09836% |
| Todos los meses positivos | 32/63 = 50,79365% | 33/63 = 52,38095% |
| Trimestres positivos | 15/21 = 71,42857% | 15/21 = 71,42857% |

Sharpe 1,256422; fees totales 5.418,029034 USDT; 260 trades = 135 longs + 125 shorts. Meses completos: 32/61 positivos, activos y calendario; trimestres completos: 13/19. Rescata seis meses negativos de referencia y perjudica siete antes positivos. En 2022 la cuenta pierde 2,74364%; 2024 gana 10,18994%. Los objetivos de regularidad 65–70% / 80% no se cumplen.

Auditoría MTM V4 individual de root: af6bb6056f5a43fc953224c729a4f9f0, succeeded; fills, fees, wallet y calendario conciliados, sin cierre sintético terminal. No se inicia auditoría duplicada. Los conteos de calendario y atribución MTM de esta sección proceden de esa auditoría; no de equity realizada de cierres.

Atribución neta USDT: BTC long 31 trades +13.079,463405; BTC short 125 trades +4.657,939095; SPY long 31 trades +3.210,672369; PAXG long 73 trades +2.475,281827. No sumar patas independientes como prueba contrafactual: pertenecen a la misma cuenta.

## Economía de PAXG

73 trades, neto +2.475,281827 USDT, fees 2.450,978145, PF 1,222690. El movimiento de precio antes de fees aporta +4.926,259971; aproximadamente el 49,75% se consume en comisiones. Exposición acumulada 4.324,7833 horas de posición; es duración observada de esta pata, no una atribución causal.

El mejor trade aporta +2.349,123770 USDT, aproximadamente el 94,90% del neto PAXG. La receta no resuelve la concentración que motivaba parte del diagnóstico. Esto no invalida por sí solo un perfil tendencial ni autoriza excluir ganadores o perdedores.

## Auditoría de snapshots, eventos y ejecución

Lectura MCP de los 7.760 registros de logs disponibles, en 16 páginas, más las 260 operaciones completas paginadas. No se crearon jobs, scripts ni archivos auxiliares.

Primer callback PAXG: 2020-10-15 04:00 UTC. Primer contexto válido: 2020-10-22 16:00 UTC. Primer evento y fill: 2021-03-23 16:00 UTC. Último contexto válido: 2025-12-30 16:00 UTC. El startup cash está incluido en el calendario; no se eliminan meses sin actividad.

Contadores FINAL, explícitamente preterminales:
- 11.412 callbacks; 1.359 intentos de captura, 1.282 capturas y 77 capturas ausentes.
- 1.358 intentos de actualización: 77 sin snapshot actual, 58 sin previo, 21 sin quote de decisión y 0 sin 4h; 1.202 actualizaciones válidas.
- 135 actualizaciones con contexto activo; 73 eventos; 0 eventos con posición o pending; 0 rechazos de riesgo; 73 planes y 73 fills.
- 57 solicitudes de salida por contexto y 57 salidas de contexto; 0 deudas diferidas por quote; 73 cierres.

Las etiquetas CUMULATIVE_THROUGH_YEAR_END son acumulados, no estadísticas anuales. La muestra bounded_context_samples del log final aparece cortada por el proveedor al superar su límite de línea: no se reconstruyen precios ausentes ni se afirma haber inspeccionado todos los snapshots brutos. Los registros EVENT y FALSE_TO_EXIT_DEBT completos permiten comprobar todos los eventos y deudas; la prueba de paridad M1/4h se ejecutó en la fuente revisada y no produjo excepción.

Se verificaron los 73 EVENT: BTC y SPY negativos, PAXG positivo, allowed verdadero, open/pending falsos. Cada decisión es hábil a las 16 UTC; T = decisión−4h y el previo dista exactamente siete días. Se verificaron las 57 deudas: contexto falso, posición abierta y allowed falso. Cero anomalías en esas comprobaciones.

Todos los eventos tienen BUY MARKET ejecutado en el mismo timestamp. Todos los nacimientos de deuda tienen SELL MARKET ejecutado en el mismo timestamp; no hubo liquidación discrecional con quote antigua ni deuda pendiente observada en esta corrida. Las operaciones registran 73 entradas MARKET y 57 salidas MARKET + 16 STOP. Para cada PAXG entry, created_at = executed_at = opened_at; para cada exit, executed_at = closed_at. Todas las salidas MARKET también tienen created_at = executed_at. El contador closed=73 concuerda y no hay residual ni terminal que reinterpretar.

Ejemplo causal inicial: decisión 2021-03-23 16 UTC, extremos 2021-03-23 y 2021-03-16 a las 12 UTC; retornos BTC −2,171923%, PAXG +0,137022%, SPY −1,134980%. Se abre en esa decisión. El 24 de marzo a las 16 UTC, una nueva observación con BTC positivo y PAXG negativo genera deuda y cierre MARKET inmediato. No se usa la dirección posterior del trade para definir el episodio.

## Conclusión y límite

El mecanismo produjo episodios reales con ejecución coherente y neto PAXG positivo, pero añade rotación/costes y no mejora la cuenta. El fallo de esta receta no demuestra que toda divergencia contextual carezca de valor; tampoco justifica rescatarla con una búsqueda de horizontes después de observar estos resultados. No hay cambios de alpha, nuevas fuentes, corridas o rebaja de objetivos. La combinación predeclarada se evalúa separadamente por root.
