# Integración funding/OI — validación 2026-10-20

## Alcance y estado
Implementación en feature/funding-integration, desde el checkpoint de exploración 0dfb91d5.
BTC-USDT Binance USD-M. Sin ML. Funding y OI desactivados por defecto.
Datos/estrategias/backtests de esta validación se consumieron por MCP; código y tests del framework se trabajaron localmente con autorización.
Los adaptadores live se probaron con respuestas simuladas; no hubo cuentas, sesiones ni órdenes reales.

## Circuito real de funding
- [Control sin funding](http://localhost:9200/#/backtest/4ccfc043-032f-45fd-b968-5f1521be2700).
- [Diagnóstico con funding](http://localhost:9200/#/backtest/5f570095-5625-4a84-bfee-112194a75b8e).
- [Panel Funding & OI](http://localhost:9200/funding/index.html?session_id=5f570095-5625-4a84-bfee-112194a75b8e).
- Ventana: 2025-12-01 inclusive → 2025-12-03 exclusiva, UTC.
- Capital 10.000 USDT; isolated 3x; fee 0,00045; cantidad fija 0,01 BTC; entrada una vez y cierre al día.
- Son diagnósticos de infraestructura, no candidatas de inversión ni evidencia de una ventaja económica.

| Comprobación | Resultado |
|---|---:|
| Pagos/cobros con posición | 3 |
| Funding neto, USDT | -0.03119174812650414 |
| Diferencia de PnL con/sin funding | -0.031191748126502716 |
| Diferencia de saldo final | -0.03119174812673009 |
| Comisiones de cada ejecución | 0.7947828 |
| Precios y timestamps de fills, cantidad y comisiones | Idénticos |
| Marks aproximados utilizados en estos pagos | 0 |
| Eventos de funding recorridos en la ventana | 6 |

El neto sin funding es -42,1467828 USDT; con funding -42,17797454812647 USDT. La diferencia coincide con el ledger y con el campo funding del trade, con tolerancia numérica 1e-8.
El motor publica funding.applied, scope, exclusiones, política de límites y versión utilizada; una configuración solicitada sin resultados no se presenta como aplicada.

## Datos reales, procedencia y actualizaciones
Todo el contenido siguiente vino de endpoints públicos oficiales de Binance mediante las herramientas MCP nuevas.

| Dataset | Ventana UTC | Registros | ID |
|---|---|---:|---|
| Funding calibración, preservado por el diagnóstico | 2020-01-01 → 2026-01-01 | 6576 | 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 |
| Funding actualizado | 2020-01-01 → 2026-10-20 | 7452 | 22844a59690b907ffe4f7b039592907ab4181241f08fb57abbdff3935cc2d1e8 |
| OI reciente, preservado por el observador | 2026-10-10 → 2026-10-19 | 2592 | 20ef231937c1563e384f305c80f57569f07af034e03bf414073fa916768a339b |
| OI actualizado | 2026-10-10 → 2026-10-20 | 2880 | 76ecc04c53393d03dfaed5de184821e8513a64835e64a82d432272bbf87eef92 |

- Funding completo bajo el control explícito de máximo ocho horas más jitter de un segundo.
- Binance devuelve markPrice vacío en 4198 registros antiguos. Se autorizó explícitamente allow_mark_price_proxy=true para la importación; esos marks se aproximan con la apertura horaria de markPriceKlines. Se conservan tasa real, fuente de precio y contador de aproximaciones.
- El dataset completo contiene 4198 proxies, pero los tres pagos del diagnóstico de diciembre de 2025 usan marks de liquidación exactos de la API.
- Actualizar crea versiones nuevas y no cambia la selección ni el contenido de sesiones anteriores.
- OI: cobertura completa de las ventanas recientes finales; fuente REST limita el historial al mes reciente. No afirmar disponibilidad causal de 2020–2025.
- Una importación intermedia de OI truncada a 500 registros quedó preservada con ID 88aa5ce4d1916b65efd7cc33200b634398ffbdb94db5ce3a9adbdd7b4aac6d93. Ahora se identifica como incompleta, con 2092 observaciones faltantes; la UI impide seleccionarla para consumo.
- Se corrigió el paginado de OI por ventanas de hasta 500 intervalos y se agregó una regresión de la respuesta real truncada. No se inventan ceros ni interpolaciones.

## Observador OI real
[Sesión del observador](http://localhost:9200/#/backtest/b82ac782-7bdf-4444-a018-aacb654795ca), ventana 2026-10-10 → 2026-10-12.
No emite órdenes. Sus assertions confirman que una muestra positiva de OI llega a la estrategia y que su timestamp no es futuro.
Resultado terminado sin excepciones; metrics.open_interest.applied=true y funding desactivado.
El motor aplica un retraso explícito de seis minutos sobre la etiqueta del período; el timestamp de publicación original no está disponible.
La importación de 2026 y este observador son diagnósticos técnicos, no una búsqueda de reglas ni un nuevo test de rentabilidad OOS.

## Validación
- Suite general final: 2168 tests pasaron, 77 omitidos por condiciones del entorno; incluye los tests lentos.
- Conjunto específico previo: 237 pasaron, 1 omitido; revisión final de live: 68 pasaron. La suite general final incluye las nuevas regresiones.
- UI: 7 tests pasaron con Chromium en Windows, además de lectura contra los endpoints reales para sesiones con/sin funding y para OI; escritorio y móvil sin overflow ni errores JS.
- Cancelación, timeout y limpieza de procesos: 92 tests pasaron tras habilitar init:true en el contenedor local; no se modificaron aserciones para ignorar procesos.
- Pyrefly: pendiente de autorización para instalar la herramienta ausente en el contenedor; no se instaló ninguna dependencia hasta este punto.

## Live
HTTP: premiumIndex, fundingRate, income y openInterest; positionRisk y estado de órdenes para reconciliación.
- Datos públicos cada 30 s; income cada 60 s; datos vencidos o inconsistentes bloquean entradas.
- Wallet real no se debita dos veces. Ledger durable por tranId, cashflow decimal y alcance de cuenta, sin atribución ficticia a trades.
- Reconciliación con el motor nativo de fills parciales/completos, VWAP y carreras de cancelación; salidas reduceOnly conservadas.
- Regresiones finales: entrada y salida con igual milisegundo se ordenan por restricciones de posición/reduceOnly; si el orden es ambiguo se bloquea antes de modificar estado. No se infiere cronología de UUIDs. La resta de lotes decimales no genera posiciones fantasma.
- El panel exige una sesión terminada y el dataset seleccionado coincidente antes de afirmar aplicación; métricas viejas tras un fallo de cola o cambio de dataset no prueban uso actual.
- Inicio exige one-way, BTC sin posiciones ni órdenes preexistentes; no adopta exposición externa.
- Funding/OI habilitados no permiten un wallet ficticio cuando el saldo real falta o es inválido.
- Paper con estas funciones se rechaza antes de conectar. No es válido usar pagos reales de una cuenta para una posición simulada.
- No se validaron credenciales, conectividad autenticada ni ejecución de una cuenta real. Esa comprobación operativa requiere una autorización separada y no equivale a validación de rentabilidad.

## Guía
La referencia del framework es jesse://funding (jesse/mcp/resources/funding.md). Incluye las diez herramientas MCP, los campos form.config, las APIs de Strategy y las aproximaciones del replay.
El servidor anuncia 111 herramientas, incluidas las diez nuevas. Si un cliente conserva el catálogo anterior, hay que reconectar su conexión MCP; no cambia el token por esta feature.
Snapshots y journals permanecen en el storage local ignorado por Git; la base local y la Pi no se copiaron ni se mezclaron.
