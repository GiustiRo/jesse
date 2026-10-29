# HANDOFF — Research BTC con funding/OI y walk-forward
Fecha: 2026-10-20. Estado: PLAN DE CONTINUACIÓN; no se ejecutó research profundo en esta entrega.
Solicitante: usuario del workspace. Pide plan escrito para que otro agente continúe.
Ruta del repositorio framework: C:/dev/trading/regime-trade/jesse
Proyecto Jesse: bot/; rama observada feature/funding-integration.

## 1. Decisión y alcance
Estamos preparados para comenzar investigación histórica más profunda, con una fase inicial corta de cierre de calidad y trazabilidad. No estamos listos para afirmar ventaja, desplegar ni operar.
Objetivo: encontrar reglas simples, sin ML, inspiradas en mecanismos y features causales del bot legacy; medir por separado qué aportan funding y open interest y evaluar estabilidad en distintos regímenes mediante walk-forward cronológico.
La disponibilidad de una feature exige probar su integración y su aporte mediante ablación; NO obliga a incluirla en toda estrategia final.
Universo inicial exclusivamente BTC-USDT, Binance Perpetual Futures. PAXG/SPY y otras bolsas fuera de este bloque. Sin chunks aleatorios.
Capital de referencia 10.000 USDT. Riesgo por operación: presupuesto 2% para pérdida al stop + fees de entrada/salida; funding y slippage adicionales se reportan. Sin piramidar. Isolated3x para continuidad con piloto; no confundir con decisión futura de live5x.
Prioridad rentabilidad y estabilidad, no frecuencia. DOCS.md registra objetivo orientativo20–30% anual, negociable. No existe en este handoff un umbral mensual numérico aprobado: reportar meses completos sin inventarlo.

## 2. Instrucciones de operación para el próximo agente
1. Leer DOCS.md y los AGENTS aplicables; escanear frontmatter de .claude/skills/*/SKILL.md. Leer backtest-expert y jesse-strategy-tests si escribe tests de framework.
2. Leer este handoff y los informes enumerados en sección3 mediante MCP. No reauditar todo el legacy ni repetir pilotos ya terminados.
3. Estrategias, datasets, sesiones, análisis y reportes por Jesse MCP local, localhost9200. Usar run_analysis para comparar snapshots; NO research_scripts sin consentimiento específico. Las autorizaciones anteriores de código local fueron para integración/framework/tests, no para saltarse MCP de research.
4. Ante timeout de una mutación no repetir a ciegas: comprobar estado cuando MCP vuelva a responder. Un timeout de arranque ya dejó una sesión terminada correctamente. Si MCP no responde, detener el trabajo dependiente y explicar el error; no sustituirlo por CLI o acceso directo a la base.
5. Cada sesión reportada debe incluir dashboard_url real devuelto por herramienta. Configurar por sesión en form.config; no cambiar ajustes globales para una prueba.
6. No leer/imprimir .env, credenciales ni operar Pi/cuentas. Sin live/paper ni despliegue. No instalar plugin comercial ni LICENSE_API_TOKEN.
7. No crear otro chat ni enviar mensajes a otros chats: el usuario sólo pidió documento de continuación.
8. No hay orden nueva de commit/push en esta entrega. Preservar cambios existentes y no revertir archivos ajenos. Antes de editar, revisar git status.

## 3. Evidencia existente que debe leerse
Informes en proyecto Jesse, rutas retornadas por MCP:
- strategies/FundingIntegrationSmoke1m/reports/LEGACY_PREFLIGHT_AND_FUNDING_WALK_FORWARD_PILOT_20261020.md
- strategies/FundingWfPilotBase4h/reports/FUNDING_WF_PILOT_PREREG_20261020.md
- strategies/FundingWfPilotBase4h/reports/FUNDING_WF_PILOT_SELECTION_20261020.md
- strategies/FundingWfPilotBase4h/reports/FUNDING_WF_PILOT_RESULTS_20261020.md
- strategies/FundingOiPilot4h/reports/OI_PILOT_PREREG_20261020.md
- strategies/FundingOiPilot4h/reports/OI_PILOT_RESULTS_20261020.md

Legacy readonly: C:/dev/trading/regime-trade (carpeta padre).
Hallazgos ya verificados:
- Modelo promovido LightGBM de12 features:5 funding,3OI,4precio/rango/régimen. No demuestra alpha aislada de funding ni autoriza ML ahora.
- oi_price_divergence usa cierre final del día corriente en barras anteriores: anticipación localizada. No copiar esa implementación; no implica que todas las features OI sean inválidas.
- Motor legacy divide funding decimal por100 y cobra según calendario desde entrada: resultados de costes no comparables a Jesse.
- Sus reportes incluyen períodos de2026: no usar agregados legacy como validación nueva pre2026.
- No reejecutar/reentrenar legacy para tomar decisiones de este bloque; extraer hipótesis documentadas y reconstruir cálculo causal.

Piloto:
A=FundingWfPilotBase4h; B=FundingWfPilotFiltered4h.
C=FundingOiPilot4h; D=FundingOiCombinedPilot4h.
A usa ruptura del máximo/mínimo del día UTC anterior, decisión4h; stop2%,target4%,hold24h.
B bloquea funding final extremo y desfavorable, zscore del último respecto a30eventos anteriores, umbral2, ptp>0 y desviación finita.
C exige OI disponible mayor al valor observado en la decisión4h de24h antes; D combina B+C.
Funding contable ON en las cuatro, incluyendo A/C; no confundir coste con señal.
Ninguna A/B pasó selección de desarrollo. Las comparaciones C/D son exploratorias, con ventanas ya vistas.

| Variante | Neto ene-jun2022 | DD2022 | Trades2022 | Neto ene-jun2023 | DD2023 | Trades2023 |
|---|---:|---:|---:|---:|---:|---:|
| A | -10,94% | -20,77% | 93 | +20,32% | -17,38% | 85 |
| B | -6,23% | -17,32% | 91 | +19,80% | -17,38% | 82 |
| C | +8,92% | -8,44% | 59 | +11,94% | -12,37% | 56 |
| D | +11,40% | -8,23% | 58 | +7,30% | -15,29% | 54 |

Interpretación: OI redujo exposición y DD de C frente a A en ambos semestres, pero sacrificó retorno2023. Funding combinado no domina OI solo. No promover ni extrapolar los pilotos.
Sesiones finales2022: C http://localhost:9200/#/backtest/e520a85a-2da4-4c7e-bca0-876eaf0aed6b ; D http://localhost:9200/#/backtest/b55b776b-1c7b-4d46-9e02-d0289abb626a
Sesiones finales2023: C http://localhost:9200/#/backtest/3b1e599e-c393-4305-8c18-a1d603f9e638 ; D http://localhost:9200/#/backtest/ea8fc49b-0e12-4886-82eb-7ad1a6b105e7
Análisis reconciliación funding inicial a360d6fbd8c04c2ab37a060969136100 y comparativa A/B/C/D d03d03ccb6884b43a1ccd1087d80a24c. Workspaces temporales caducan: informes guardados son referencia duradera.

## 4. Datos y supuestos congelables
Período común: [2020-09-01,2026-01-01), último dato2025. Execution candles1m; señales iniciales4h. Funding eventos, OI5m, no se convierten en falsas series1m.
Dataset funding calibración:
9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571
Dataset OI calibración:
6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf
No sustituir automáticamente por versiones nuevas. Registrar hash de código y versión/framework/config en cada prueba. Si se revisa dataset, conservar ambos y no elegir el que más gana.
Funding decimal; final liquidado no es estimación de próximo pago. Publicación histórica modelada +1m; marca antigua proxy horario explícito. Todos los cargos de las ventanas piloto usaron proxy, no importes exactos certificados.
OI archivo retrospectivo, label+6m asumido, stale máximo10m desde disponibilidad. No point-in-time certificado; ampliar el retraso por sensibilidad no subsana revisiones retrospectivas.
OI total560390/561024 muestras esperadas,634ausentes,156huecos. Ceros presentes son distintos de ausencia; no considerar una caída a cero como señal económica.
Nunca rellenar huecos con0/interpolación ni prolongar stale para rescatar resultados. Si la feature es requisito de entrada y falta, no entrar; mantener gestión de posiciones/salidas.
Primer24h del filtro OI piloto tiene inicialización explícita; nunca confundirla con falta del proveedor.
No usar enero-agosto2020 para estrategias que exigen OI.

## 5. Fase0 — cierre corto antes de volumen de research
Entregable: RESEARCH_DATA_AND_EXECUTION_FREEZE.md por MCP, con estado apto/inconcluso y límites.
- Confirmar que el MCP renovado permite leer funding paginado; fix de normalización existe pero daemon anterior seguía cargando versión vieja. No reiniciar backend o MCP de forma ciega.
- Código corregido en jesse/mcp/tools/services/project_files.py y session_analysis.py; tests en tests/test_mcp_session_results.py.123tests y Pyrefly0errores pasaron en proceso nuevo;45tests OI pasaron. Esos tres archivos estaban modificados sin commit al redactar.
- Auditar por mes cobertura OI5m, ceros, días/intervalos afectados y disponibilidad a4h; si MCP no expone inspección suficiente, registrar la capacidad faltante. No leer storage por fuera de MCP para eludirla.
- Persistir contadores separados: dato ausente, stale, cero actual, referencia inválida, inicialización, gate económico y entradas. El piloto blocked_missing agrupa causas, debe desglosarse antes de resultados masivos. Guardar también parámetros/procedencia de cada feature.
- Verificar independencia del futuro mediante prueba de prefijos/mutación futura y timestamps, incluyendo cada nueva transformación, rolling statistics y multi-timeframe; conservar tests, sin red/cuentas. Hoy pasaron lookup retardado/stale y assertions runtime; no afirmar que todas las transformaciones futuras ya estén validadas.
- Revisar fuente de balance/sizing y conciliar por trade: precio bruto-fees+funding=PNL; ledger vinculado y balance final coherentes.
- Determinar soporte real de slippage adverso en backtest. Si falta, resolver integración acotada y tests antes de afirmar validación de ejecución. Un haircut posterior en run_analysis sólo es aproximación de costes, no simula fills, stops ni compounding.
- Un solo backtest activo inicialmente para aislar demoras MCP; subir a2sólo si respuesta estable. Registrar excepciones y duración.
- No preimportar velas por rutina: ejecutar y sólo resolver cobertura si el motor detecta faltantes.
No se requiere cobertura perfecta para investigar, pero sí política explícita, cuantificación y sensibilidad; no eliminar meses adversos por tener huecos.

## 6. Fase1 — protocolo de hipótesis, máximo12 configuraciones
Entregable antes de correr: RESEARCH_PROTOCOL_V1.md, registry de configuraciones/parentesco, hashes, selección y fricción.
Trabajar tres mecanismos como máximo, inspirados en legacy:
H1 continuación de precio evitando funding congestionado/desfavorable.
H2 reversión tras extremo de funding con confirmación de precio ya cerrado.
H3 cambio/normalización de funding tras un extremo con confirmación de régimen por precio.
Son hipótesis para especificar y falsar, no hallazgos demostrados del modelo. No asignar dirección a una feature por su importancia ML.
El siguiente agente debe definir algebraicamente cada entrada, ventana, salida y falta de dato antes de ver su primer resultado. Mantener4h al inicio y salidas/sizing comunes del piloto para aislar el mecanismo. Umbrales30eventos/2z y OI24h pueden ser puntos iniciales documentados, informados por legacy/piloto, no estimaciones independientes.
Cada mecanismo incluye ablaciones equivalentes: P (precio), P+F, P+OI, P+F+OI. Máximo3x4=12 configuraciones únicas; si P/OI se repiten exactamente reutilizar sesiones/hashes, no fabricar variantes distintas.
OI inicial creciente24h: prueba de confirmación de participación, no predicción automática long/short. Nuevas transformaciones OI o cambios de timeframe consumen presupuesto de configuración, no se agregan gratis.
Sin grids enormes ni thresholds ajustados fold a fold. No usar el rendimiento2026 para elegir mecanismos. No descartar shorts por intuición ni imponer50/50.

## 7. Fase2 — walk-forward de exploración 2022–2023
Entrenamiento expansivo, comienzo2020-09-01; evaluación siguiente semestre, fin exclusivo:
| Fold | Entrenamiento [inicio,fin) | Evaluación [inicio,fin) |
|---|---|---|
| E1 | 2020-09-01 → 2022-01-01 | 2022-01-01 → 2022-07-01 |
| E2 | 2020-09-01 → 2022-07-01 | 2022-07-01 → 2023-01-01 |
| E3 | 2020-09-01 → 2023-01-01 | 2023-01-01 → 2023-07-01 |
| E4 | 2020-09-01 → 2023-07-01 | 2023-07-01 → 2024-01-01 |
Estas ventanas, especialmente E1/E3, ya tienen exposición exploratoria. Etiquetar resultados como research.
Ejecutar cada configuración congelada en train y evaluación para comparar familias, máximo12x4x2=96sesiones económicas nominales; reutilizar exactamente equivalentes verificando código/config/datos.
En cada fold guardar selección basada sólo en train ANTES de ejecutar/consultar su siguiente evaluación.
Filtro train propuesto a congelar en protocolo: >=30trades, neto>0, PF>=1.2, absDD<=25%. Son gates de investigación, no prueba estadística de edge.
Orden entre elegibles: menor absDD; luego mayorPF; luego menor turnover; empate restante favorece configuración más simple y luego IDestable. No seleccionar por evaluación. Si ninguna pasa: SIN_CANDIDATA y posición plana en evaluación del selector.
Evaluar todas las ablaciones permite aprendizaje, pero sólo el registro de la candidata elegida corresponde al selector walk-forward. No presentar ganadora posterior de un semestre como si se hubiera elegido antes.
Al finalizar E1–E4, escoger máximo2configuraciones finalistas para fase3; esta elección usa desarrollo y debe registrarse. Congelar también el algoritmo de selección, desempates, política de datos, número de intentos y pruebas de estrés. Si no hay evidencia suficiente, concluir sin candidata, no abrir fase3 por obligación.
No ajustar continuamente después de cada semestre para luego sumar todos como prueba independiente. Una modificación es nueva versión y sus pruebas quedan dentro de desarrollo.

## 8. Fase3 — confirmación cronológica 2024–2025
| Fold | Entrenamiento [inicio,fin) | Evaluación [inicio,fin) |
|---|---|---|
| C1 | 2020-09-01 → 2024-01-01 | 2024-01-01 → 2024-07-01 |
| C2 | 2020-09-01 → 2024-07-01 | 2024-07-01 → 2025-01-01 |
| C3 | 2020-09-01 → 2025-01-01 | 2025-01-01 → 2025-07-01 |
| C4 | 2020-09-01 → 2025-07-01 | 2025-07-01 → 2026-01-01 |
Máximo2 finalistas,4folds,train+evaluación=16sesiones nominales. Aplicar algoritmo congelado usando exclusivamente pasado en cada corte; puede cambiar candidato automáticamente según train, no por intervención humana tras ver evaluación.
No inspeccionar métricas2024–2025 de estas nuevas configuraciones antes de congelar shortlist/protocolo. Es reserva interna de este ciclo; estrategias anteriores ya usaron esos años, no es independencia absoluta.
Pasado evaluado en C1 puede incorporarse al train C2 por calendario; no permite cambiar meta-reglas.
Si se cambian reglas después de ver confirmación, esa confirmación pasa a desarrollo de la nueva versión; no llamarla holdout nuevo.
Cada sesión de train/evaluación empieza plana con10000 y warmup declarado sin operar. Historia anterior sirve para features, nunca incluye eventos posteriores al instante de decisión.
Posiciones abiertas se cierran al borde del fold con costes documentados. Máxima duración24h; no atribuir a train trades cuyo resultado pertenece a evaluación.
No hay etiquetas ML a purgar. Si se incorporan señales/eventos con resultado futuro, truncar su evaluación en train en el corte; para reglas con holding mayor, explicitar cierre o separación temporal antes de ejecutar.
Una curva con folds reseteados no representa una cuenta continua. Reportar tabla de retornos/DD por fold y selector con meses planos; no sumar balances, fees en USDT ni trades repetidos de train.
Si se construye índice rebajando/rebasando retornos, declarar convención de reinversión y costes de cambios; validación de capital continuo real requiere un replay que transporte capital y posiciones sin resets. No afirmar ese replay si sólo se usaron sesiones independientes.

## 9. Fase4 — robustez previamente declarada, hasta48sesiones
Presupuesto total de ciclo máximo160sesiones económicas:96exploración+16confirmación+48robustez. Retries técnicos sólo con misma lógica/datos y motivo registrado; también se registran intentos cancelados/no concluidos. No ampliar presupuesto automáticamente.
Definir dentro de48 antes de fase3:
- Fee nominal0.00045 y estrés0.0009; costes de funding siempre activos.
- Slippage adverso/latencia de entrada con soporte real del motor; valores y número de ejecuciones fijados según resolución y mercado antes de ver resultados, no buscando mínimo coste que salva candidata. Si sólo fee duplicado disponible, denominarlo estrés de fees y dejar ejecución pendiente.
- Vecindad pequeña de ventanas de señal/stop/target, sin seleccionar vecino ganador: objetivo comprobar degradación suave. Stop/TP secundarios sólo en finalistas; no mezclar búsqueda de alfa con tuning de riesgo.
- Sensibilidad OI a retraso más conservador y exclusión de ceros/huecos; comparar misma máscara de disponibilidad entre ablaciones como diagnóstico separado del caso operativo, para distinguir efecto señal de efecto datos faltantes.
- Sensibilidad de costes al proxy de marca funding; no afirmar exactitud por cobertura.
- Bootstrap por bloques/Monte Carlo como complemento si herramientas MCP soportan dependencias/calendario; no mezclar trades aleatorios para descubrir reglas ni usar random chunks temporales como walk-forward.
- Desgloses long/short, mes, año, exposición, trades/bloqueos, duraciones, funding, fees y precio bruto.
Los costes extra y recortes posteriores no reproducen fills ni liquidación; explicitar límites.
Si repetir fases o otra familia excede160, cerrar informe y proponer cicloV2 con límites nuevos.

## 10. Criterios de salida propuestos para congelar
Gate económico de confirmación: neto agregado del índice del selector>0, PF de trades únicos seleccionados>=1.2, DD del índice<=25%, >=100trades seleccionados en total y mayoría de semestres de confirmación positivos. Si hay menos100: evidencia insuficiente, no aprobar por ser positivo. Los100 no certifican significancia estadística.
Neto positivo bajo estrés de fees y ejecución declarada; todos los límites anteriores se reportan también bajo estrés. No exigir que cada fold aislado superePF1.2 si el protocolo sólo exige agregado, ni relajar gates tras resultados.
Estabilidad: reportar concentración por mejor semestre/trade; quitar mejor semestre y señalar si se invierte signo. Sin umbral de concentración inventado después de resultados.
Valor de una feature: mejora repetida de retorno/riesgo o robustez frente a ablación comparable, con exposición/turnover y disponibilidad explicados; no alcanza un mejor fold. Si no aporta, la final puede omitirla.
Objetivo orientativo anual20–30% se evalúa sólo con una convención válida de capital/tiempo; no anualizar mejor semestre como expectativa. Mostrar meses negativos, mediana, peor mes y rachas; no prometer cuota mensual.
Una candidata que pasa esto sigue siendo candidata histórica: integración live tiene límites propios y no se autorizan órdenes.

## 11. 2026 y evidencia final
No ejecutar ni consultar2026 durante este plan. Fecha máxima de todas las sesiones2026-01-01 exclusiva.
2026 ya fue observado con K1001/referencias y condicionó decisiones generales de research; no vuelve a ser muestra virgen por empezar estrategia desde cero. Mantenerlo sin nuevas consultas reduce contaminación adicional, no borra la existente.
Después de congelar estrategia y protocolo y revisar resultados2020–2025, proponer un único examen2026 con versión inmutable, limitaciones de exposición y sin retuning. La autorización histórica para K1001 no se extiende automáticamente a cualquier estrategia nueva.
Fracaso final => rechazar o nueva versión declarando2026 observado para ella, no iterar hasta positivo. Evidencia realmente nueva vendrá de fechas futuras/prospectivas; paper con funding/OI está actualmente rechazado por diseño y necesitaría implementación específica, no iniciar por rutina.
Nada de este plan autoriza live con fondos.

## 12. Registro y entregables
Guardar por MCP reportes y registry duraderos (estrategia/carpeta de research identificable):
- RESEARCH_DATA_AND_EXECUTION_FREEZE.md
- RESEARCH_PROTOCOL_V1.md y registry.json (cada intento, código completo o hash+ubicación inmutable, parámetros, datasets, costes, fold, etapa, sesión/dashboard_url, timestamps, decisión previa).
- WALK_FORWARD_EXPLORATION_V1.md
- FROZEN_SHORTLIST_V1.md antes de2024–2025
- WALK_FORWARD_CONFIRMATION_AND_STRESS_V1.md con meses y descomposición.
- FINAL_DECISION_V1.md: candidata, descartada o inconclusa, sin forzar éxito.
Snapshots analysis expiran; copiar conclusiones/tablas/procedencia a informes mediante save_strategy_report. Nunca inspeccionar reportes localmente para eludir MCP.
Cambios de código compartido deben preservarse en cada sesión/reporte: MCP puede capturar sólo subclase; guardar también padre o hash+contenido para reproducción.

## 13. Estado de trabajo para retomar
Últimas4sesiones OI finales están finished; no repetirlas. Pilotos concluidos y contabilidad conciliada.
Rama feature/funding-integration. Al escribir se observaron:
M jesse/mcp/tools/services/project_files.py
M jesse/mcp/tools/services/session_analysis.py
M tests/test_mcp_session_results.py
Directorios/reportes nuevos sin commit: FundingWfPilotBase4h, FundingWfPilotFiltered4h, FundingOiPilot4h, FundingOiCombinedPilot4h y reporte legacy en FundingIntegrationSmoke1m.
No hay bloqueo económico que impida investigar; sí deben resolverse/registrarse límites fase0 antes de volumen grande. No reiniciar servicios ni introducir scripts de research como atajo.

## 14. Instrucción de inicio para el agente sucesor
Continuar desde fase0 de este documento, sin ejecutar2026, ML, cuentas ni Pi. Entregar primero freeze de datos/ejecución y protocoloV1 con12configuraciones como máximo y selección reproducible. Después avanzar cronológicamente hasta una conclusión registrada, incluyendo SIN_CANDIDATA si corresponde. No pedir al usuario que reconstruya lo ya documentado. Este handoff planifica trabajo futuro; no afirma que ya se hayan corrido los ocho folds completos.
