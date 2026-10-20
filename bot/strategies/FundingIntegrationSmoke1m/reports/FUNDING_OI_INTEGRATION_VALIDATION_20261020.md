# Integración funding/OI — validación 2026-10-20

## Alcance y estado
Implementación en feature/funding-integration, desde el checkpoint de exploración 0dfb91d5.
BTC-USDT Binance USD-M. Sin ML. Funding y OI desactivados por defecto.
Datos/estrategias/backtests de esta validación se consumieron por MCP; código y tests del framework se trabajaron localmente con autorización.
Los adaptadores live se probaron con respuestas simuladas; no hubo cuentas, sesiones ni órdenes reales.

## Circuito real de funding
- [Control sin funding](http://localhost:9200/#/backtest/4ccfc043-032f-45fd-b968-5f1521be2700).
- [Diagnóstico con funding](http://localhost:9200/#/backtest/5f570095-5625-4a84-bfee-112194a75b8e).
- [Import Data dentro del dashboard](http://localhost:9200/#/candles/).
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
- Suite general final: 2203 tests pasaron, 77 omitidos por condiciones del entorno; incluye los tests lentos.
- Conjunto específico previo: 237 pasaron, 1 omitido; revisión final de live: 68 pasaron. La suite general final incluye las nuevas regresiones.
- UI: 10 tests pasaron con Chromium en Windows, además de lectura contra los endpoints reales para sesiones con/sin funding y para OI; escritorio y móvil sin overflow ni errores JS.
- Cancelación, timeout y limpieza de procesos: 92 tests pasaron tras habilitar init:true en el contenedor local; no se modificaron aserciones para ignorar procesos.
- Pyrefly 1.4.0 instalado en el contenedor local con autorización expresa del usuario. Indicadores, Strategy, estrategias de test, importador OI, jobs, API y MCP: 0 errores; 12 supresiones preexistentes en indicadores.

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
El servidor anuncia 112 herramientas, incluidas once de funding/OI y progreso de importación. Si un cliente conserva el catálogo anterior, hay que reconectar su conexión MCP; no cambia el token por esta feature.
Snapshots y journals permanecen en el storage local ignorado por Git; la base local y la Pi no se copiaron ni se mezclaron.


## Ampliación histórica y pantalla Import Data

- Pantalla principal integrada en el dashboard: [Import Data](http://localhost:9200/#/candles/), con pestañas Candles, Funding y Open Interest. El formulario nativo de candles y su estado se conservan; se verificaron navegación SPA, escritorio/móvil y ausencia de errores JS. La URL antigua sigue disponible por compatibilidad.
- Fuente OI histórica: archivos diarios oficiales de Binance USD-M BTCUSDT, primer archivo listado 2020-09-01. Cada ZIP se verifica contra su CHECKSUM SHA-256; manifest y versiones permanecen locales.
- Dataset de calibración: `6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf`, [2020-09-01,2026-01-01), 560390 observaciones de 561024 esperadas; faltan 634 (0.1130%), en 156 intervalos. Mayor separación entre muestras 37800000 ms (10.5 h). 1948 ZIPs verificados; ningún día de archivo ausente; 75255 filas duplicadas idénticas fueron contabilizadas y normalizadas.
- Calidad `incomplete` explícita: no se inventan muestras para alcanzar cobertura completa. Consumir este archivo requiere `allow_missing_observations=True`; una muestra vencida o ausente retorna None.
- El archivo original de septiembre de 2020 tiene LastModified de marzo de 2026. Esta importación no certifica disponibilidad original punto a punto; `allow_archive_assumptions=True` acepta un replay retrospectivo con etiqueta +6 minutos. No se usa la fecha de descarga de hoy como si fuera publicación original.
- No se verificó una fuente gratuita para enero–agosto de 2020. Tardis documenta OI normalizado desde mayo de 2020, con acceso completo sujeto a autorización comercial; Coin Metrics respondió 403 para BTC Binance en su API community. No se compraron datos ni se mezclaron series de proveedores.
- Importaciones extensas usan jobs persistidos y progreso consultable por MCP/UI. La web descubre trabajos iniciados por MCP. Se probaron exclusión entre procesos, interrupción por reinicio, reutilización de ZIPs verificados y errores sin sustituir el dataset anterior.
- La serie tiene resolución nativa de 5m y se vincula por timestamps de disponibilidad al replay de candles de 1m. No se interpola a 1m. Funding conserva eventos de liquidación independientes del timeframe de la estrategia.

### Resultado de la extensión a 2026 y diagnóstico histórico

- Actualización terminada por MCP: `e302d68e8cd3c1f68a602adcc8f355a254bbb4c3575ab8b9f20e1980a06c6093`, [2020-09-01,2026-10-20), 644486 observaciones de 645120 esperadas. Permanecen los mismos 634 faltantes y 156 intervalos; sin nuevos huecos en 2026. 2211 ZIPs únicos verificados más REST para la cola [2026-09-21,2026-10-20). La versión de calibración anterior queda intacta.
- [Observador histórico de enero de 2021](http://localhost:9200/#/backtest/343bd1b4-a212-407e-84ee-75113006b3f5): [2021-01-01,2021-01-03), terminado sin excepción, cero órdenes/trades. La estrategia confirmó al menos una muestra positiva de OI con timestamp no futuro. Resultado open_interest.applied=true, allow_missing_observations=true y dataset de calibración original, aunque ya existe una versión nueva.
- UI real sobre /#/candles/: muestra el archivo histórico, sus huecos, ZIPs, duplicados y supuesto temporal. Descubre la actualización creada por MCP sin sembrar su ID en el navegador. Escritorio y móvil 390px sin overflow ni errores JS; cero escrituras de sesiones o solicitudes de trading durante esta QA.

### Cierre de validación

- Suite general: 2203 passed, 77 skipped; tras los ajustes finales de consentimiento, descubrimiento y caché, 85 tests específicos de OI/jobs/API pasaron. UI: 10/10. Pyrefly: 0 errores (12 supresiones preexistentes en indicadores).
- Lectura real autenticada vía MCP tras reiniciar: cinco datasets OI visibles; listado en frío 10.812 s y repetición 0.098 s. Caché acotado a 200 resúmenes, invalidado por cambios/eliminación del archivo; las lecturas explícitas siempre verifican checksum. No se retienen observaciones completas en caché.
- Backend anuncia 112 herramientas. Servicio local actualizado, sin sesiones live/paper ni backtests activos al reiniciar. No se conectó una cuenta real ni se operó en la Pi.
