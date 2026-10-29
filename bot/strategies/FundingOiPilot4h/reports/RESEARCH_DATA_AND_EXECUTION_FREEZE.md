# Research data and execution freeze — 2026-10-20
Estado actualizado: **APTO CON LÍMITES para investigación histórica V1**, tras autorización del usuario y cierre MCP de ejecución e instrumentación. El cuerpo original conserva la evidencia y el bloqueo previo, resuelto por el addendum final. Datos auditados con límites; implementación de slippage probada en proceso nuevo, pendiente de activación y prueba completa por MCP. No se lanzó exploración económica V1.

## Alcance y evidencia leída
Continuación desde fase 0 del RESEARCH_WALK_FORWARD_HANDOFF_20261020.md. Leídos por MCP los seis informes de preflight, prerregistro/selección/resultados funding y prerregistro/resultados OI. No se reentrenó legacy ni se repitieron los cuatro pilotos finales.
BTC-USDT, Binance Perpetual Futures; [2020-09-01,2026-01-01), datos hasta 2025. Capital 10000 USDT, isolated3x, fee nominal .00045. Sin cuentas, Pi, ML, live/paper, scripts de research, cambios globales, commit o push.

Framework 3.4.0; HEAD 55c77098acfcc79de6a611712f4d066c4bb11f65, árbol modificado. Python de pruebas 3.11.17; jesse-rust 1.3.1. Los cambios preexistentes project_files.py, session_analysis.py y test_mcp_session_results.py se preservaron.

## Datasets congelados
Funding: 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571.
OI: 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
No se importó ni reemplazó ningún dataset.
Funding decimal, final liquidado, disponibilidad +1m modelada. Marcas proxy históricas explícitas.
OI archivo retrospectivo, label+6m asumido, stale máximo10m desde disponibilidad; no certifica publicación/revisiones históricas. Los ceros se preservan como datos, se excluyen de señales/referencias; sin interpolación, relleno o ampliación de stale.

## Acceso MCP y auditoría OI
get_session_funding funciona: offset0/limit2 y offset2/limit2 entregaron filas distintas, total91, next_offset2/4 y status applied. Se resolvió el problema de normalización que estaba pendiente en el handoff.
get_open_interest_dataset permite observaciones y disponibilidad paginadas. Para evitar más de1100 páginas se usó un observador sin órdenes, leyendo exclusivamente Strategy.open_interest/timestamp; cada muestra5m pasa por al menos una decisión5m bajo lag6m y stale10m.
Primera auditoría: [sesión](http://localhost:9200/#/backtest/7770abfd-57c0-4004-ac81-fc1e5a87693a), 46.83s. Dos líneas largas fueron truncadas por el lector MCP a2000 caracteres, no por el proveedor. Reintento técnico con mismos cálculos/datos y líneas acotadas: [sesión](http://localhost:9200/#/backtest/0dccc27a-f17c-4b55-8958-9881e40b11bb),45.10s. No corrección económica.
El último label2025-12-31 23:55 sólo estaría disponible2026-01-01 00:01. Se añadió exclusivamente al conteo de cobertura usando la página MCP raw offset560387/limit3; nunca se usó para decisiones anteriores al fin.

Resultado reconciliado: 560390 de561024 muestras esperadas (99.886992%),634ausentes en156intervalos;473ceros en264runs de ceros contiguos. Mayor salto entre observaciones37800000ms. No falta ningún archivo diario completo, pero sí observaciones intradiarias.
Archivo duradero con los64meses y TODOS los intervalos y sus timestamps UTC [inicio,fin), conteos, runs de ceros y reconciliación de cola:
strategies/ResearchDataAudit5m/reports/PHASE0_OI_AUDIT_20261020.json.
Los intervalos determinan los días afectados; no se eliminó ningún mes.

### Disponibilidad en decisiones4h
11688decisiones en (inicio,fin], correspondientes a barras cerradas dentro del período; el punto fin sólo consume datos anteriores y no permite nuevas entradas en V1.
Partición con prioridad exclusiva: ausente0; stale10; cero actual10; inicialización6; referencia inválida19; gate OI no creciente5588; OI creciente6055. Suma11688.
Referencia de24h construida con seis decisiones4h previas. Inicialización es del observador, no un hueco del proveedor. Referencia inválida incluye cero/None observado24h antes, no otro conteo de muestras crudas faltantes.
Los conteos son por barra, sin condicionar a una oportunidad de precio, y no equivalen a trades bloqueados. Entradas del observador:0. Para las estrategias V1 se exige además persistir por oportunidad: precio, funding ausente/varianza nula/extremo, OI ausente/stale/cero/inicialización/referencia inválida/gate económico y entradas, junto con denominadores y causas simultáneas. Esa instrumentación debe verificarse antes del primer lote; no atribuirla retroactivamente a pilotos.

| Mes UTC | OI filas | Ausentes5m | Ceros5m | Decisiones4h | Stale | Cero actual | Inicialización | Ref inválida | No creciente | Creciente |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2020-09 | 8636 | 4 | 0 | 180 | 0 | 0 | 6 | 0 | 81 | 93 |
| 2020-10 | 8918 | 10 | 0 | 186 | 0 | 0 | 0 | 0 | 66 | 120 |
| 2020-11 | 8621 | 19 | 0 | 180 | 2 | 0 | 0 | 2 | 95 | 81 |
| 2020-12 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 79 | 107 |
| 2021-01 | 8911 | 17 | 0 | 186 | 0 | 0 | 0 | 0 | 89 | 97 |
| 2021-02 | 7948 | 116 | 0 | 168 | 2 | 0 | 0 | 2 | 91 | 73 |
| 2021-03 | 8921 | 7 | 0 | 186 | 0 | 0 | 0 | 0 | 85 | 101 |
| 2021-04 | 8607 | 33 | 0 | 180 | 1 | 0 | 0 | 1 | 86 | 92 |
| 2021-05 | 8916 | 12 | 10 | 186 | 0 | 0 | 0 | 0 | 64 | 122 |
| 2021-06 | 8456 | 184 | 0 | 180 | 2 | 0 | 0 | 2 | 67 | 109 |
| 2021-07 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 83 | 103 |
| 2021-08 | 8927 | 1 | 0 | 186 | 0 | 0 | 0 | 0 | 85 | 101 |
| 2021-09 | 8609 | 31 | 0 | 180 | 0 | 0 | 0 | 0 | 85 | 95 |
| 2021-10 | 8906 | 22 | 0 | 186 | 0 | 0 | 0 | 0 | 84 | 102 |
| 2021-11 | 8602 | 38 | 0 | 180 | 0 | 0 | 0 | 0 | 88 | 92 |
| 2021-12 | 8921 | 7 | 0 | 186 | 0 | 0 | 0 | 0 | 70 | 116 |
| 2022-01 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 85 | 101 |
| 2022-02 | 8064 | 0 | 0 | 168 | 0 | 0 | 0 | 0 | 93 | 75 |
| 2022-03 | 8928 | 0 | 117 | 186 | 0 | 3 | 0 | 3 | 86 | 94 |
| 2022-04 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 72 | 108 |
| 2022-05 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 91 | 95 |
| 2022-06 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 84 | 96 |
| 2022-07 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 75 | 111 |
| 2022-08 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 91 | 95 |
| 2022-09 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 71 | 109 |
| 2022-10 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 97 | 89 |
| 2022-11 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 104 | 76 |
| 2022-12 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 92 | 94 |
| 2023-01 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 88 | 98 |
| 2023-02 | 8064 | 0 | 0 | 168 | 0 | 0 | 0 | 0 | 79 | 89 |
| 2023-03 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 86 | 100 |
| 2023-04 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 99 | 81 |
| 2023-05 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 88 | 98 |
| 2023-06 | 8640 | 0 | 4 | 180 | 0 | 0 | 0 | 0 | 88 | 92 |
| 2023-07 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 88 | 98 |
| 2023-08 | 8928 | 0 | 1 | 186 | 0 | 0 | 0 | 0 | 102 | 84 |
| 2023-09 | 8637 | 3 | 0 | 180 | 0 | 0 | 0 | 0 | 93 | 87 |
| 2023-10 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 93 | 93 |
| 2023-11 | 8640 | 0 | 11 | 180 | 0 | 0 | 0 | 0 | 74 | 106 |
| 2023-12 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 100 | 86 |
| 2024-01 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 88 | 98 |
| 2024-02 | 8227 | 125 | 0 | 174 | 3 | 0 | 0 | 3 | 76 | 92 |
| 2024-03 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 77 | 109 |
| 2024-04 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 88 | 92 |
| 2024-05 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 89 | 97 |
| 2024-06 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 79 | 101 |
| 2024-07 | 8928 | 0 | 299 | 186 | 0 | 6 | 0 | 5 | 93 | 82 |
| 2024-08 | 8928 | 0 | 6 | 186 | 0 | 0 | 0 | 0 | 85 | 101 |
| 2024-09 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 79 | 101 |
| 2024-10 | 8926 | 2 | 0 | 186 | 0 | 0 | 0 | 0 | 86 | 100 |
| 2024-11 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 101 | 79 |
| 2024-12 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 87 | 99 |
| 2025-01 | 8928 | 0 | 5 | 186 | 0 | 0 | 0 | 0 | 112 | 74 |
| 2025-02 | 8064 | 0 | 0 | 168 | 0 | 0 | 0 | 0 | 88 | 80 |
| 2025-03 | 8928 | 0 | 1 | 186 | 0 | 0 | 0 | 0 | 105 | 81 |
| 2025-04 | 8640 | 0 | 9 | 180 | 0 | 1 | 0 | 1 | 84 | 94 |
| 2025-05 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 100 | 86 |
| 2025-06 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 96 | 84 |
| 2025-07 | 8928 | 0 | 10 | 186 | 0 | 0 | 0 | 0 | 94 | 92 |
| 2025-08 | 8925 | 3 | 0 | 186 | 0 | 0 | 0 | 0 | 109 | 77 |
| 2025-09 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 99 | 81 |
| 2025-10 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 81 | 105 |
| 2025-11 | 8640 | 0 | 0 | 180 | 0 | 0 | 0 | 0 | 83 | 97 |
| 2025-12 | 8928 | 0 | 0 | 186 | 0 | 0 | 0 | 0 | 92 | 94 |

## Causalidad
[Observer de prefijos/mutación futura](http://localhost:9200/#/backtest/cf8d315d-79aa-4d6e-9a0e-fe88566c147f): finished,.94s,0trades;10assertions sintéticas y12barras4h reales. Fuente completa guardada en registry.json.
Se comparó prefijo contra serie extendida y futuro mutado para rango UTC de velas cerradas, z-score31eventos (30referencia, ddof0, ptp>0) y selección OI por available_at. Bordes: publicación, stale inclusivo10m y cero distinto de ausencia. Además assertions runtime de timestamps en ambas auditorías.
Límite: prueba de las funciones concretas de ResearchFeatureAudit4h y del acceso runtime, no certificado universal del motor ni de transformaciones aún no implementadas. H2/H3, su composición temporal y cualquier nuevo timeframe necesitan sus propios checks antes de ejecutar. Los tests existentes OI/funding también se ejecutaron.

## Balance, riesgo y conciliación independiente
[Snapshot piloto C2022](http://localhost:9200/#/backtest/e520a85a-2da4-4c7e-bca0-876eaf0aed6b), reanalizado sin repetir backtest.
Análisis MCP5d48099bcd244484960e325ea9ab2e51:
59trades,91movimientos ledger. Precio bruto1434.703369090778; fees534.7920857039071; funding−7.640323778212991; saldo final10892.27095960866, diferencia con métrica7.275957614183426e-12USDT.
Error máximo por trade0; error máximo de qty reconstruida0.
14trades omiten el campo funding; se comprobó que no tienen movimientos vinculados antes de interpretar0.
Verificados PNL=precio bruto−fees+funding, cashflow=−qty firmada×marca×rate y vinculación temporal por trade.
Fuente de capital: Strategy.available_margin → FuturesExchange.available_margin, saldo wallet menos compromisos; con una ruta plana es saldo realizado. Funding aplica una sola vez al wallet y cambia sizing posterior. El qty del piloto se reconstruyó desde ese saldo, stop2%, ambas fees y floor8decimales; riesgo al stop+fees<=2%. No se multiplica riesgo por3x.
Todos los cargos del ejemplo son proxy; tolerancia contable1e-6USDT no implica exactitud de marca. Primer análisis de conciliación a2cd71669aaf4fbbaaf97d3f10b6c2a7 falló al suponer campo funding presente en todos los trades; se corrigió el análisis, sin tocar resultados. Inspección previa de schema68ab7b98703c4fac863d765b8ed4a70a.

## Ejecución: código preparado, runtime pendiente
Antes no había un parámetro explícito de slippage. Se agregó exchange.slippage_bps optativo, default0, sólo futures/backtest.
MARKET y STOP: precio fill=referencia×(1+s×bps/10000), s=+1buy/−1sell. Se aplica DESPUÉS del trigger/gap y ANTES de fees, wallet y callbacks. LIMIT conserva su precio. Se preserva submitted_price para liberar correctamente la reserva de margen; se exporta precio de referencia/bps, sin exportar vars arbitrarias. Reejecutar una orden terminada no vuelve a aplicar slippage.
Validación finita0<=bps<10000; spot y otros modos con bps>0 se rechazan. 10000 es el borde algebraico de precio de venta no positivo, no un coste elegido para investigación.
Es un estrés determinista de fills; no simula profundidad, queueing, rechazo, latencia, spread real ni liquidez del exchange. No acredita costes reales ni todas las liquidaciones aisladas. Funding/slippage siguen fuera del presupuesto de stop+fees.
Cambios framework: jesse/config.py; jesse/services/backtest_slippage.py; jesse/services/order_service.py; jesse/models/Order.py; jesse/mcp/tools/services/session_config.py. Tests nuevos tests/test_backtest_slippage.py y ampliación tests/test_broker.py.
279tests aprobados en dos lotes:241de estrategia/broker/config/funding/OI/MCP y38de gaps/órdenes/conflictos/isolated. Un warning de dependencia Starlette/AnyIO. Pyrefly0errores en los cinco módulos cambiados; git diff --check sin errores.
[Smoke MCP pedido5bps](http://localhost:9200/#/backtest/1037c215-a3f9-4bff-9a44-7215e2f09a34): finished,.87s,3trades, pero form.config.exchange perdió slippage_bps al arrancar y las órdenes no tienen slippage. **Aplicado0bps**, no un ensayo5bps exitoso.
Diagnóstico: el proceso MCP sigue con _exchange_config anterior que descarta el campo. No se reiteró ciegamente, ni se usó CLI para lanzar research, ni se cambió configuración global. Los tests corren en intérprete nuevo y por eso no sustituyen la prueba MCP.

## Trazabilidad de código compartido
SHA256 del código de integración preparado (no afirmar que el daemon cargó estos hashes):
- jesse/config.py CAC6823F826FA7C919AB6D6C7136BAA971DA5BFCFD688B2D1303BE36C19897C2
- jesse/models/Order.py 8AD3105AA124F55B9DF8303694A1D30EA52EDF61813E24FD30FDA03DBC4FC5D5
- jesse/services/order_service.py F0D9F3B9FE6B5AEB8139609D0A13A271370C32DB21811397B62F47C3B30C91E8
- jesse/services/backtest_slippage.py D7262338FF4C278B7A32767E8C0B9DC7FE8293CD90F478D20E703D94458C0C5B
- jesse/mcp/tools/services/session_config.py E9F24AA96C6A3708724E8384EEED5D0EB92BF803C3AC6F7C96C3C38DA213DF61
Fuentes completas de observadores e intentos en strategies/FundingOiPilot4h/reports/registry.json. El protocolo V1 especifica hipótesis pero ninguna tiene aún implementación promovida ni sesiones económicas V1.

## Condiciones para cerrar fase0 y continuar
1. Autorizar y realizar renovación controlada del proceso local/MCP; no Pi ni reinicio de Postgres. No reiniciar a ciegas. Al guardar este informe get_backtest_sessions(status_filter=running) devolvió0.
2. Después de reconectar, inspeccionar el smoke anterior antes de crear un nuevo intento. Repetir misma ventana con5bps, verificar campo preservado, provenance y fórmula en cada orden, fees/ledger/saldo y sizing. Guardar intento y duración.
3. Implementar instrumentación por oportunidad y nuevas transformaciones V1 con prefijos/mutación futura; capturar código completo del padre y cada subclase antes de su primer resultado.
4. Sólo entonces marcar APTO CON LÍMITES y comenzar train E1 del protocolo. Sin promoción,2026 ni ajustes económicos para rescatar resultados.


## Addendum — cierre de fase0 tras autorización del usuario
Servicio local jesse-research-jesse-1 (puerto9200,working directory/src/bot) renovado con autorización directa. Antes:0backtests activos y0sesiones live/paper; Postgres y Pi sin intervención. Reinicio finalizado2026-10-20T20:37:38.296077189Z; lectura autenticada get_backtest_sessions exitosa después.
[Smoke5bps efectivo](http://localhost:9200/#/backtest/65ed1148-59cb-477e-9143-75fee5de93f9): finished,.81s,3trades,5fills MARKET/STOP con5bps aplicados y límites sin ajuste. Análisis41aaaa8e78b24a98a4a1e995f11f8c01: error máximo0,fees/funding/sizing conciliados,saldo9956.382901370425USDT,3eventos funding. No es búsqueda económica.
[Instrumentación inicial](http://localhost:9200/#/backtest/37919fca-4d03-40a7-b89d-8086e9004a38): finished,.76s. [Instrumentación final](http://localhost:9200/#/backtest/7166595f-90de-4db4-bd1c-75a4e51b17bd): finished,1.16s. Conservación:54barras;4oportunidades=3entradas+1rechazoOI;3cierres. Self-checks reales de H1/H2/H3,funding actual/anterior,OI24h y retraso conservador: passed. Campos available_at/settled_at y causas simultáneas de calidad registrados; código antes de resultados en RESEARCH_V1_IMPLEMENTATION_FINAL.md y registry.json.
La última llamada run_backtest devolvió timeout10s,pero consultar la MISMA sesión mostró running y luego finished; no se repitió la mutación. Se mantiene un solo backtest activo para aislar demoras.
Core SHA256 4512d21d8bab7bd33389db6e32315cf4ffaf50955cfa6e03f48d25082c1c2546. Cada subclase nominal/ventana tiene fuente completa y SHA256 en registry antes de su ejecución. No se validan por anticipado todas las posibles transformaciones; sólo las implementadas en este core. No hay simulación de latencia ni point-in-time certificado del archivoOI.
Fase0 cerrada con esos límites; se habilita investigación cronológica E1–E4 conforme al protocolo congelado. Ninguna autorización de live/paper/2026.


## Cierre del cicloV1
96sesiones económicas de exploración completadas,ninguna candidata elegible en cuatro trains. Detalle y límites en FINAL_DECISION_V1.md y WALK_FORWARD_EXPLORATION_V1.md. Se conservaron12snapshots FRAMEWORK_*.py del código utilizado,con hashes originales idénticos a los contenidos UTF8 archivados. No se abrió confirmación2024–2025 ni2026. Los contadores completos de las96sesiones se validaron y archivaron por MCP.
