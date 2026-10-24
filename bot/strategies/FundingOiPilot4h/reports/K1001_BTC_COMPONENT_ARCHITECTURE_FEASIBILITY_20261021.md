# K1001 — Viabilidad arquitectónica preliminar de componentes BTC

Fecha: 2026-10-21. Sólo lectura documental/framework y escritura de este informe. El steering humano más reciente prioriza entender K1001 antes de investigar o probar: este pendiente técnico no autoriza implementación, protocolo económico, clases, jobs, drafts ni tests.

## Dictamen breve

Una única cuenta nativa Jesse no admite dos posiciones independientes long/short del mismo BTC-USDT en el mismo exchange. Un coordinador de posición neta con atribución por componente es viable en principio como estrategia nueva; su paridad de ejecución, callbacks y contabilidad aún no está demostrada. Un libro hedge virtual sería un modelo adicional, no un resultado nativo de hedge ni dos cuentas reales.

La autorización nueva define 2% de riesgo BTC total: dos componentes con 1% cada uno, o tres con 2/3% cada uno, sobre equity común. El cupo ocioso de un componente no se transfiere por defecto. Global 6% / aislado 3x y funding histórico ON; USDC diferido. Esto supera el antiguo 2% por trade para este alcance. No se propone variar riesgo.

## Evidencia de framework, sólo lectura

- `jesse/routes/__init__.py:27–41`: rechaza duplicar (exchange, symbol), aunque difieran estrategia o timeframe.
- `jesse/store/state_positions.py:15–16`: una Position por clave exchange-symbol.
- `jesse/strategies/Strategy.py:475–476`: ruta toma esa posición y su Broker. Líneas 1150–1175: entrada estándar sólo flat; long y short simultáneamente verdaderos generan conflicto.
- `jesse/strategies/Strategy.py:1252–1270`: cierre nativo llama cancelación de órdenes del símbolo antes del callback del usuario. Un cierre de componente no puede delegarse ingenuamente al padre como si los hermanos no existieran.
- `jesse/services/broker.py`: permite compras/ventas y reducciones sobre la misma posición; no crea subposiciones. Las reducciones nativas no representan por sí solas el cierre de una pata virtual opuesta.
- `jesse/services/position_service.py:176–216`: fills aumentan, reducen, cierran o invierten una posición neta. El callback se clasifica por el cambio de esa posición, no por identidad de componente.
- `jesse/modes/backtest_mode.py`: el simulador procesa órdenes activas y gaps intraminuto antes de la decisión de la estrategia; puede cancelar/recrear órdenes desde callbacks. Varias órdenes en M1 se ordenan con una heurística OHLC, no ticks observados. Funding se liquida por reloj del motor sobre la exposición nativa.
- MCP `jesse://strategy`, `jesse://backtest_management`, `jesse://funding`, `jesse://position_risk` y `jesse://session_analysis` consultados. La simplificación de flujo en docs no sustituye el source actual de cancelación y reevaluación.

No se leyó ninguna estrategia del proyecto bot por filesystem; no se tocaron framework, adapter, configuración, datos, estado o secretos.

## Qué se puede acreditar y qué no

| Diseño | Alcance acreditable | Límite |
|---|---|---|
| Standalone nativos separados | Reglas y ejecución de cada componente con su cupo fijo y costes, una cuenta por sesión | No acreditan equity común, simultaneidad, margen compartido ni tamaños posteriores conjuntos. |
| Coordinador neto, una ruta | Una posición física, fills y funding nativos; ledger interno atribuye decisiones, reservas y PnL por componente | Requiere desarrollo y paridad técnica futura; las métricas nativas agrupan episodios netos, no trades de cada sleeve. |
| Hedge virtual dentro de estrategia | Hipótesis matemática de patas simultáneas con equity común y ledger explícito | No hay dos posiciones nativas. Sus fills, stops, margen bruto, fees y liquidación necesitan reglas propias verificadas; no llamarlo hedge nativo. |
| Suma de curvas standalone | Descripción de resultados aislados | No sirve como simulación conjunta ni como compounding sobre equity común. Se descarta. |

No se recomienda engañar claves usando exchanges o símbolos ficticios, clonar datos ni introducir USDC para eludir la restricción.

Un coordinador tendría que separar estado/señal de cada componente, riesgo reservado, planes pendientes, fills atribuidos y protección de la posición neta. Un cierre neto no puede borrar silenciosamente órdenes de otro componente. El margen nativo neto no demuestra capacidad de margen de dos patas brutas opuestas. Las compensaciones pueden ahorrar turnover/fees; no se puede otorgar ese ahorro al libro independiente por conveniencia ni cobrar a ambas cuentas el mismo ledger sin demostrar equivalencia.

La equity común debe actualizarse cronológicamente con wallet, PnL abierto y costes de las operaciones realmente representadas. La fórmula lineal de funding puede permitir atribución algebraica por cantidades firmadas con el mismo mark/rate, pero eso no demuestra equivalencia de margen, fees, tamaños, stops o liquidación entre hedge y neteo. No hay una curva conjunta demostrada actualmente.

## Análisis y trazas

El snapshot de backtest admitido por `run_analysis` contiene summary, metrics, trades/orders, equity_curve e hyperparameters. La documentación no incluye logs ni velas como inputs. Por ello no se presupone que un trace escrito en logs sea legible dentro de analysis. Tampoco está acreditado que cualquier metadato personalizado sobreviva en los orders exportados.

Se puede consultar logs por MCP para diagnóstico y analizar snapshots completos existentes mediante inputs autorizados. Una futura vía de trace necesitaría verificar el formato exportado y su integridad; no inventar un campo, pegar arrays de resultados en código, leer archivos del proyecto/velas desde analysis ni ejecutar un segundo motor dentro del análisis. No se realizó ese desarrollo.

## Próximo estado

Pendiente técnico, subordinado a comprender primero K1001 y sus componentes exactos. No se selecciona ahora arquitectura final ni se inicia comparación. La opción nativa más defendible para una futura cuenta operativa es posición neta; la independencia simultánea opuesta conserva una limitación explícita del framework actual. No hay permiso implícito para modificarlo.
