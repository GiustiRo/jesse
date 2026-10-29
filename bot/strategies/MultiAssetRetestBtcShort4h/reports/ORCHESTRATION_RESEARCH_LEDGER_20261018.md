# Orquestación autónoma — registro de investigación

## Actualización vigente — traspaso final de las tres líneas frescas

Estado consolidado al18octubre2026local: tres agentes frescos COMPLETED, sin jobs pendientes propios. Leer primero strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_RESEARCH_HANDOFF_20261018.md. Este handoff sustituye los estados históricos pendientes/en ejecución/blocked como resumen actual, sin borrar la historia.

FreshStructureProbability: fullrun a3d3904dcb764db4b987fa0be7883d7d y auditoría ec58a9386a9f4151b3c1ac8764d28548 succeeded.11418forecasts;11411válidos/2ambiguos/5censurados;24controlesPASS. Pivots y combinado empeoran Brier/logloss globales, cada año y cohorte00UTC. ARCHIVAR recipe1D/4h+pivots/firsttouch24h/180d/shrink20, no retocar para rescate. Informe strategies/FreshStructureProbability/reports/INDEPENDENT_OBSERVER_NEGATIVE_RESULT_20261018.md. No tradingPnL ni2026.

FreshAuthorMethods: informe documental final strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md. Priorizar viabilidad de flujo real BTCperp propio; GEX opcional y estimado. Cobertura/asof/licencia/coste pendientes, sin descarga/compra. SPYCFDvol0/PAXGproxy no soportan inferencias microestructurales de otros instrumentos.

FreshPortfolioResearch: informe final strategies/FreshPortfolioResearch/reports/FRESH_PORTFOLIO_DIAGNOSIS_AND_DESIGN_20261018.md. Más participación deteriora eficienciaSPY/PAXG. IdeaSPYMR retirada antes de run por duplicación y evidencia previa negativa antes de comisiones. No nueva estrategia pendiente de ejecución.

Tanda por funciones10/01/11 cerrada y rechazada: primaria25.78%CAGR/DD−26.93%,38/63mesesactivospositivos60.32%/16/21q76.19%; referencia intacta28.83%CAGR/DD−14.89%,33/61activos/15/21q. Detalle PORTFOLIO_ROLES_RESULTS_20261018.md. Objetivo65–70%meses/80%q no conseguido, riesgo máximo3%/8%,fee.00045lado y2026reservado. No reiniciar conteo histórico ni tratar2020–25comoOOSlimpio. Próxima tarea: decisión de investigación fundada, no repetir modelos archivados ni esperar jobs ya terminados.


Inicio: 18 de octubre de 2026. Objetivo activo, no conseguido.

## Encargo y límites
El usuario autoriza coordinar subagentes y explorar nuevas estrategias, combinaciones, timeframes y gestión. No se garantiza que exista una ventaja robusta que alcance todas las métricas. No se rebajan criterios después de ver resultados.

Referencia inmutable: [MultiAssetRetestBtcShort4h](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Desarrollo: 2020–2025; ventana común 2020-10-15 a 2025-12-31 exclusivo. 2026 permanece cerrado hasta congelar reglas y selección.
Objetivos de desarrollo: mínimo65% de meses activos positivos (aspiración70%), mínimo80% de trimestres positivos, DD no peor que−25% y rentabilidad útil resistente a costes. Reportar también todos los meses y períodos completos para evitar mejorar porcentajes simplemente excluyendo inactividad.
Conservar criterios finales documentados: PF>=1.2, DD no peor que−25% y muestra aproximada mínima20 trades en evaluación reservada. No usar2026 para escoger variantes ni hacer reintentos adaptativos sobre un lockbox ya leído.
Límites de investigación inicial: riesgo por trade como máximo3%, agregado planificado8%,5xaislado y techo bruto4.4x. Nuevas lógicas pueden partir de1%. Fee por lado.00045 para TODAS las órdenes, incluidasLIMIT. Variar riesgo dentro de límites no convierte más exposición en evidencia de mejor ventaja.
No live/paper, Pi, fondos, claves, instalaciones ni reinicios. Las autorizaciones previas del framework cubren dos correcciones concretas; nuevas extensiones necesitan autorización aparte.

## Equipo y propiedad
- orch_allocation: estrategias/reportes OrchAlloc, OrchManageFixedR, OrchManageScaleOut y nueva reversión rápida propia.
- orch_lateral: exclusivamente OrchLateral.
- orch_shorts: OrchShort y OrchManageMonthly.
- Root: coordinación, cola de máximo dos backtests simultáneos, auditoría MTM unificada, comparaciones, aceptación y registro central.
No editar fuentes de otros agentes ni la referencia. Cada protocolo precede al run y cada resultado, incluso malo, queda registrado. Hasta dos hipótesis por línea en primera ronda, sin barridos masivos de parámetros.

## Ronda1
| Línea | Hipótesis | Estrategia | Estado final |
|---|---|---|---|
|Asignación A|Techo nocional inverso a volatilidad de20retornos sobre21cierres observados comunes, mismo relojUTC|OrchAllocCommonClock4h|Finalizada, descartada como solución de regularidad|
|Asignación B|Presupuesto de riesgo8%/3poractivo en lugar de techo nocional individual|OrchAllocEqualRisk4h|Finalizada, descartada como solución de regularidad|
|Lateral A|Fallo simétrico de ruptura de rango20 en contexto oscilante ER<=.25, MARKET, target centro,1%riesgo|OrchLateralFailedRange4h|Finalizada, descartada como solución de regularidad|
|Short A|Recompensa neta planificada al menos igual a pérdida neta, sin cambiar target1.5ATR|OrchShortRewardRisk4h|Finalizada, descartada como solución de regularidad|
|Short B|Invalidación futura por cierre que recupera máximo de vela de señal, stop/target originales|OrchShortReclaimExit4h|Finalizada, descartada como solución de regularidad|

[Asignación A](http://localhost:9200/#/backtest/9bbd9545-2154-4842-8902-8c926c7a4a56)
[Asignación B](http://localhost:9200/#/backtest/72996434-7c02-4589-9400-42a23229ae02)
[Lateral A](http://localhost:9200/#/backtest/acae5bd3-7f00-439d-991b-7eabbf86b903)
[Short A](http://localhost:9200/#/backtest/1f0b9301-0754-4044-ab29-9c9d9c979696)
[Short B](http://localhost:9200/#/backtest/2168b24e-632b-4dca-be9c-48677c7b5a58)

## Reglas de interpretación
La selección adaptativa sobre2020–25 es desarrollo, no OOS limpio. Anotar cuántas hipótesis se prueban; no ignorar descartes.
Auditor v4: cierres UTC MTM y contabilización individual de salidas parciales ejecutadas; comisiones y wallet reconciliadas. Una entrada, múltiples salidas; no piramidado ni terminal abierto. Paridad v3 comprobada y caso real de parciales reconciliado. Ver ORCHESTRATION_ROUND2_RESULTS_20261018.md. No declarar cumplimiento por PnL realizado mensual ni últimas muestras00:01.
Primer filtro: rentabilidad neta, exposición/DD y muestra. Una estrategia lateral pequeña puede servir como componente, pero deberá demostrar mejora de la cuenta combinada con interacciones reales; sumar curvas no constituye backtest de cartera.
Después: vecinos de parámetros, tramos temporales congelados, costes con umbrales de señal fijos, concentración y adversidad de ejecución. Congelar candidato y criterios antes de abrir2026.
Cambiar orden del formulario no cambia prioridad interna en timestamp replay: el motor ordena por exchange/símbolo. Este control sigue pendiente y no se simula lo contrario.
No usar MC de rutas independientes para certificar dependencia conjunta. Fuentes PAXGSpot/SPXCFDBID y fillsLIMIT tienen límites antes de promoción.

## Ronda2: finalizada
Seis pruebas económicas: salida completa3R, salida completa5R,50%a2R+runner, guardas mensuales2/1y4/2, corto con régimen diario. Ninguna cumple la tarjeta de aceptación. Detalles y links en ORCHESTRATION_ROUND2_RESULTS_20261018.md. No barrer thresholds después del fallo. La salida parcial queda como comparación de menor DD, no candidata aceptada.

## Ronda3: diseños acotados
- Reversión rápida BTC4h: revisión reconoce solapamiento con premisa de sleeve fallido; MARKET y salida media rápida dinámica son diferencias de implementación relevantes, no evidencia independiente. Un recipe, sin rejilla de RSI tras fallo. Fuente pendiente de revisión antes de run.
- Ruptura BTC1h tras volatilidad realizada72h baja frente720h: simplificación de compresión-expansión, reconoce SqueezeRelease5m ya descartada. Sin bandas ni stack macro. Una prueba predeclarada, no reajustar ratio tras fallo. Fuente pendiente de revisión.
- Valor relativo BTC/ETH1h: fuente y smoke técnico revisados; una cesta tuvo48min de salida huérfana, ejecución no atómica. Histórico ETH importándose. Borrador full con benchmarks guardado pero sin ejecutar: [Pares full](http://localhost:9200/#/backtest/62b9f852-8b48-4b4c-b59b-537e9e687a64). Smoke17días no es resultado económico representativo. Mantener2026fuera incluso cuando importación almacene esos datos.
- Se retiró sin ejecutar el rechazo de subasta alcista por ser casi duplicado del fallo de rango ya probado. Este descarte de idea también cuenta en el historial de selección.

Total de backtests económicos completos en esta orquestación:18. Se añade un smoke técnico breve y un full detenido por falta de datos, excluidos de comparaciones económicas. No se inventa una muestra limpia después de iterar. Objetivo sigue activo y no alcanzado.

## Actualización tras ronda3
FastMR y QuietChannel finalizaron y se rechazaron por rentabilidad neta no positiva; QuietChannel además supera DD25%. Ver ORCHESTRATION_ROUND3_REJECTIONS_20261018.md. OvernightSPY se retiró antes de simular por costes/fuente; no se inventa rendimiento propio.
La revisión de regularidad informa Wilson nominal y comparación pareada, no confirmatorios. FixedR5 y referencia empatan14/19trimestres completos; no seleccionar bordes favorables. V4 ahora informa conteos completos además de los originales.
Rotación mensual pasa a implementación para revisión:3meses relativo+absoluto,stop10%,riesgomáximo3%,capnocional1x que implica~0.294xreal. Observaciones16UTC verificadasporM1 y estrictamente conocidas antesdecidir; deudasdesalida propias; startupcashcontado. No ejecutado aún.
Diseño adicional pendiente: simplificación trend daily BTC/PAXG55d/10d con ambasdirecciones y riesgo1%cadauno; reconocefamilia tendencia ya vista, sin alegar independenciani lanzar rejilla. No implementar sin revisión.

## Actualización tras ronda4
Turtle y rotación mensual finalizaron y se rechazaron. Resultados y diagnóstico de contador terminal en ORCHESTRATION_ROUND4_RESULTS_20261018.md. V4 acepta sólo cierre terminal sintético plenamente reconciliado; no altera métricas guardadas ni framework. Próximo control de salida corta24h con señales fijas y fuente pendiente de review; pares continúa esperando cobertura2025. Total15pruebas económicas; objetivo activo sin candidata aceptada.

## Reutilización y error localizado
La propuesta de expiryshort24h se retiró antes de implementar: ya existían MultiAssetShortExpiry24h/48h con corridas y MTMv3 válidos. No se repite ni se añade a15pruebas nuevas. El mapa global abarca muchas más exploraciones anteriores;15no es número total de hipótesis vistas.
MCP read_strategy(BtcTrendMaster) devuelve HTTP500 específico de ese legado; se abandona esa lectura opcional sin accesos alternativos. APIde resultados eimportación verificadas respondiendo; ETH70.7% a2024-12-27 en última comprobación de root. No reinicios/ediciones de framework. Seguimiento independiente de la importación continúa porMCP.

## Actualización tras ronda5
OneFill y SPYcalendario, más fullBTC/ETH, terminados: total18económicos adicionales. Ninguno cumple la aceptación; OneFill deja33/61meses y15/21quarters sinmejora. SPY ypares pierden inclusoenprecioantesdefees sobremismosfills. Ver ORCHESTRATION_ROUND5_RESULTS_20261018.md. La búsqueda global esmuchomayor que18 y sigue siendo desarrollo. Protocolos nuevos enestudio: eventosFedexante, financiación/basis(datos/contabilidad faltantes; optinresearch pendiente sihicierafalta). Sin nuevasestrategias lanzadas tras esos cierres porahora. ImportETHpuedealmacenar2026sin evaluar rendimientos; mantener seguimiento hastaterminal. Referencia ylockboxintactos.

## Punto de autorización pendiente
ETH importación completada (3.248.443M1,2020-08-15→2026-10-18),2026sólo almacenado. Auditoría pares V4 fbb1facc83304c62857321ebe9a914c1 pasó,10/63meses y1/21quarters positivos; descartada. Propuestas pre-FOMC/cycle archivadas SINrun por evidencia primaria de debilitamiento/inversión previa; no añadir al contador18.
Se solicitó mediante pregunta alusuario opt-in ESPECÍFICO para crear/ejecutar porMCP un descargador de datos públicosfunding/preciosBTC/ETH2020–2025. Mientras no responda, no crear scripts ni iniciar descarga deesa línea. Alcancepropuesto sóloauditoría de datos; no sistema carry, fondos, live/Pi ni framework. Diseño concreto: strategies/OrchLateralRelativeShock1h/reports/ORCH_CARRY_FEASIBILITY_PROTOCOL_20261018.md. Actualizadoinforme canónico: strategies/MultiAssetBreakout4h/reports/PHASE2_PROGRESS_20261018.md. Objetivo sigue activo, no logrado; ningúnbacktest/análisis/importactivo.

## Análisis independiente mientras se espera opt-in
Se calculó sólo con snapshots existentes el ingreso NETO perfectamente regular que requeriría un complemento con asignación10/25/50%para65/80 y70/80. Con25%de capital exige1.9415%/mes sobre ese bloque para65/80;con50%,0.6472%. Escenario algebraico mensual rebalanceado, NOcartera ejecutable ni fundingobservado, sin pesos recomendados o nuevos criterios de entrada. Todo complemento continuo hace activos63meses; control19quarterscompletos incluido. Fuente: ORCH_COMPLEMENT_INCOME_HURDLES_20261018.md; jobs04a4596f4bca4c318faf20aac39d77d7 y8318816be5d1407294abcc671d7ef45a succeeded.18backtests sin cambio. Autorización del nuevo descargador sigue pendiente; ningún script creado ni descarga nueva. Objetivo activo y no conseguido.


## Cierre de verificación y bloqueo pendiente de autorización
Comprobación final: los tres subagentes terminaron; importación ETH finalizada; últimas20tareas de análisis succeeded; ninguna sesión de backtest running. La referencia y2026 siguen reservados. No se creó ni ejecutó el nuevo descargador. Tras tres turnos consecutivos con la misma autorización específica pendiente y sin trabajo independiente restante en esta rama aprobada, el objetivo se marca blocked, no logrado ni pausado. La continuación requiere respuesta humana al opt-in de auditoría pública de funding/preciosBTC/ETH2020–2025; los mensajes automáticos de continuación no constituyen consentimiento.
