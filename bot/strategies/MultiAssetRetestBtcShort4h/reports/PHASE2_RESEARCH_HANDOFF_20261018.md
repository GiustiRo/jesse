# Handoff de investigación Fase 2 — estado para el siguiente agente

Fecha local: 18 de octubre de 2026, America/Montevideo. Algunos jobs muestran 19 de octubre UTC; no son investigaciones de otro día local.
Estado: las tres líneas de agentes frescos finalizaron. Objetivo NO alcanzado. Referencia conservada; ningún reemplazo aceptado. Este documento consolida el estado más reciente y prevalece como resumen sobre los encabezados históricos que digan «pendiente», «en ejecución» o «blocked». No es autorización para operar.

## 1. Encargo humano y modo de trabajo

El usuario autorizó investigación autónoma coordinada con subagentes: estrategias distintas por activo, estructuras de precio, nuevos indicadores/timeframes, gestión, modelos propios/ML y revisión crítica de metodologías documentadas por sus autores. Prefiere hipótesis nuevas y fundadas a repetir ajustes de indicadores. No exige el mismo sistema para BTC, PAXG y SPY: lo importante es su contribución a una cuenta compartida.

Pidió sustituir a los agentes anteriores por tres nuevos sin historial conversacional heredado, con libertad para cuestionar y descartar propuestas. Los tres ya entregaron. Sus conclusiones no son autoridad incuestionable: están acompañadas de protocolos, artefactos y evidencia. Evitar repetir por desconocimiento experimentos ya fallidos.

Último pedido humano: preparar este documento para que otro agente continúe. No se ha pedido ejecutar nuevas corridas durante el traspaso.

## 2. Objetivos, decisiones vigentes y límites

- Desarrollo/calibración: 2020–2025. Ventana común usada: inicio 2020-10-15 UTC, fin exclusivo 2025-12-31 00:00 UTC. Ese fin EXCLUYE el 31 de diciembre; no describirlo como todo el año civil 2025.
- 2026 reservado para evaluación final después de congelar selección/reglas. Puede existir almacenado en DB por importaciones, pero NO consultar precios ni rendimientos de 2026 para esta investigación.
- Objetivo de regularidad: al menos 65% de meses activos positivos, aspiración 70%; al menos 80% de trimestres positivos. Informar también todos los meses, conteos y períodos completos.
- Drawdown no peor que −25% y rentabilidad útil resistente a fricción. No rebajar criterios después de ver resultados. DOCS conserva una meta anual 20–30% negociable; no transformar CAGR elevado en sustituto de regularidad/riesgo.
- Criterios reservados documentados: PF ≥1.2, DD no peor que −25% y muestra aproximada mínima de 20 trades; congelar protocolo final antes de abrir 2026. No hacer reintentos adaptativos sobre un lockbox ya observado.
- Configuración de comparación: riesgo máximo 3% por trade, 8% agregado planificado, 5x isolated, techo bruto 4.4x, sin piramidado. Una nueva hipótesis puede usar menos riesgo, pero debe declararlo; no aumentar exposición para «rescatar» una señal.
- Comisión 0.00045 POR LADO para TODAS las órdenes, también LIMIT: aproximadamente 9bps ida/vuelta. STOP/LIMIT son condiciones de ejecución; no cambiamos la tarifa por usar LIMIT.
- Reserva adicional de ejecución en sizing NO significa slippage real aplicado. Funding, spread, impacto y latencia siguen siendo limitaciones materiales.
- Long y short deben evaluarse por expectativa neta/payoff, no por imponer winrate≥51%. El usuario quiere ambos sentidos con contribución válida.
- DOCS.md contiene decisiones antiguas «sólo BTC» y «2%» superadas por autorización humana multi-activo y 3%/8%. No revertir inadvertidamente.

## 3. Operación y permisos

Leer DOCS.md, AGENTS.md y bot/AGENTS.md antes de actuar; escanear frontmatter de habilidades del repo y leer las pertinentes. Investigación local vía MCP jesse-local, dashboard http://localhost:9200. No usar Pi ni sesiones live/paper.

Todos los archivos de estrategias/reportes/datos del proyecto por Jesse MCP. Reportes con save_strategy_report. No shell/FS/SQL/red para sortear herramientas. Si MCP falla o tiene timeout, comprobar estado al reconectar antes de repetir y no usar fallback. Los procesos pueden haber continuado tras timeout o fallo del agente.

Research scripts son opt-in: autorización humana explícita de investigación ML cubrió el observador y sus controles por MCP; no equivale a autorización genérica de scripts/descargadores. Para analizar sesiones usar run_analysis con snapshots, no nuevos scripts. Leer scripts enteros antes de ejecutarlos.

No compras, instalaciones, contratos de datos, credenciales, fondos, cambios de framework ni reinicios por autonomía genérica. Las excepciones históricas autorizadas del framework cubrieron dos bugs concretos (equity y reservas), no futuras extensiones. Revisión documental de funding/GEX/footprint está autorizada; NO se ejecutaron nuevos descargadores de esas fuentes y no existe consentimiento de compra.

Máximo dos backtests simultáneos, coordinar root; máximo dos analysis/research jobs según límites del servicio. Cada hipótesis tiene protocolo anterior al resultado, registro de fallos y comparación con capital compartido. No barridos masivos ni esconder variantes fallidas.

Cuando se mencione una sesión al usuario, incluir su dashboard_url. Al editar notas, conservar title, description y strategy_codes: omitir el snapshot puede borrarlo.

## 4. Referencia inmutable

Estrategia: MultiAssetRetestBtcShort4h.
[Dashboard de referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Sesión: 2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb.
Rutas BTC-USDT, PAXG-USDT y SPY-USDT 4h, auxiliares M1, simulación normal con motor corregido.

| Métrica | Referencia |
|---|---:|
| CAGR |28.8294%|
| DD motor |−14.8905%|
| Sharpe |1.3164|
| Neto / fees USD |27461.46 / 4595.62|
| Trades |220|
| Longs |97 =31 BTC +35 PAXG +31 SPY|
| Shorts |123 BTC|
| Meses positivos / activos |33/61 =54.10%|
| Meses positivos / todos |33/63 =52.38%|
| Trimestres positivos |15/21 =71.43%|
| Meses completos positivos / activos |33/59 =55.93%|
| Trimestres completos positivos |14/19 =73.68%|

Contribución neta de trades: BTC long13881.76USD; BTC short5287.02; PAXG4632.27; SPY3660.42. No confundir esto con MTM mensual.
Long winrate44.33%, short55.28%; long gana por tamaño de ganancias, no por mayoría de aciertos.

Lógica resumida: longs retest de ruptura Donchian26 con EMA20/80, ADX26 y RSI; stop2ATR, trailing4.2ATR, BE2.25R. BTC short continuación tras selloff/rebote en régimen macro, STOP de activación, target1.5ATR y tiempo máximo72h. Leer fuente real antes de reproducir; este resumen no sustituye código.

No modificar la referencia ni sus resultados; nuevas ideas en estrategias nuevas.

## 5. Datos, ejecución y evaluación: restricciones que importan

SPY procede de HistData SPX CFD BID dividido por10, con volumen cero y huecos; NO es tape de SPY/ES ni precio ejecutable demostrado del SPY-USDT24/7. La elección inicial Dukascopy no fue la fuente finalmente disponible. No usar indicadores de volumen, footprint o volume profile auténtico sobre ese archivo. Calendario/filtro de sesiones y cotización M1 fresca son necesarios; paridad con instrumento tokenizado sigue sin certificarse.

PAXG procede de Spot, usado como proxy en simulación perpetual. No equiparar sus trades a flujo COMEX/GLD ni asumir contratos/funding históricos idénticos.

Hay datos BTC disponibles mediante research.get_candles, pero un reloj completo devuelto no demuestra que el proveedor nunca rellenó huecos. Auditar procedencia cuando importe.

Equity: auditor V4 reconstruye MTM al cierre diario UTC desde fills, salidas parciales y comisiones, con anclas de precio. No calcular regularidad por mes de cierre de trades ni usar muestra equivocada00:01. DD del motor y de cierres diarios difieren por muestreo. Contador de posición abierta preterminación puede reconciliarse con cierre de frontera; eso no demuestra liquidez real en ese cierre.

En run_analysis los snapshots incluyen métricas, trades, equity e hiperparámetros, NO logs/vars/charts/strategy_codes. No fingir que se exportaron predicciones si no hay artefactos reales. No pegar arrays externos en analysis para sortear su contrato.

Monte Carlo es validación transversal, no nueva fuente de alpha. Shuffle de trades sólo informa secuencia/path risk; velas remuestreadas dependen del modelo de bootstrap. Ninguno certifica por sí solo costes, causalidad, ausencia de selección múltiple o dependencia conjunta multi-activo. No afirmar que estar bajo la mediana «prueba» ausencia de sobreajuste.

## 6. Historia de exploraciones: evitar repetirla

Historial GLOBAL ampliamente adaptativo sobre2020–25; no OOS limpio. Los siguientes conteos son subconjuntos, no el total global:
- 18 backtests económicos de orquestación anteriores (asignación, riesgo, exits fijos/parciales, guardas mensuales, lateral/fallo de rango, shorts, MR, compresión, Turtle, rotación, calendario y pares BTC/ETH). Ninguno aceptado.
- Tanda posterior BTC:8 configuraciones combinadas (7 candidatas +1 control) y un laboratorio probabilístico sin trades. Volumen, estructura confirmada, aceptación, reclaim, reloj de evento, salida por falta de progreso, suplemento semanal y control de días. Ninguna cumplió objetivos.
- Tanda por funciones PAXG/SPY:3 configuraciones económicas fijas, concluida y rechazada.
- Agentes frescos: diagnósticos de sesiones +un estudio probabilístico observacional; NO nuevos backtests de trading.

Consultar el registro central y reportes de cada tanda en lugar de repetir todas las métricas aquí. Que una fila histórica diga «pendiente» no implica trabajo actual: leer secciones posteriores y este handoff.

Diagnóstico previo:28 meses negativos,13 con BTC no negativo y otras patas negativas,8 caso contrario,7 ambos;4 sin exposiciónBTC. Alta concentración de beneficio long en pocos runners. No prueba imposibilidad de la meta, pero desacredita asumir que arreglar sólo shortsBTC resuelve toda regularidad.

Errores del handoff original ya detectados: Fase1 tuvo45long/0short, no35/10; óptimo58%CAGR dependía de5%riesgo y parámetros en bordes;2024–25 ya participó en selección y no era OOSlimpio. No reutilizar aquellas afirmaciones.

## 7. Última tanda de cartera por funciones: terminada, NO aceptada

Protocolo previo: PORTFOLIO_ROLES_STAGE_PROTOCOL_20261018.md.
Resultados: PORTFOLIO_ROLES_RESULTS_20261018.md, ambos bajo reports de MultiAssetRetestBtcShort4h.
Diseño2×2: BTCbaseline intacto en reglas;10 cambia PAXG;01 cambia SPY;11 combina ambos y es primaria predeclarada. Cuenta compartida cambia tamaños y oportunidades; no sumar curvas individuales.

| Configuración | CAGR | DD motor | Meses positivos/activos | Q positivos |
|---|---:|---:|---:|---:|
| Referencia |28.83%|−14.89%|33/61|15/21|
| PAXG divergencia7d (10) |26.04%|−16.09%|32/63|15/21|
| SPY participación cooldown168h (01) |30.14%|−17.73%|37/63|13/21|
| Combinada primaria (11) |25.78%|−26.93%|38/63|16/21|

La combinada alcanza60.32%meses/76.19%q; completos38/61meses62.30% y14/19q73.68%. No pasa criterios y empeora DD. Peor mes−10.27%,peorq−11.60%,2022−7.36%. No retocar cooldown/ventana/riesgo para rescatar.

Sesiones:
- [PAXG contextual](http://localhost:9200/#/backtest/af7161bf-00cd-49a9-b3aa-385fd301396d), AnglePortfolioPaxgDivergence4h.
- [SPY participación](http://localhost:9200/#/backtest/3315ba00-2a40-4e8c-9b5a-690e1b4e5006), PortfolioSpyPersistent4h.
- [Combinada primaria](http://localhost:9200/#/backtest/2ca17713-06a5-42ea-8956-6de60653e2a5), PortfolioRolesCombined4h.

Auditoría MCP722aa973845c4c89b6acfe9eff63ce0e succeeded. Fills/horarios/deudas/cooldown y terminal conciliados. Artefactos temporales de analysis pueden caducar: los reportes persisten; recrear desde snapshots si hace falta, no depender de memoria de otro agente.

## 8. Tres agentes nuevos: resultados finales

### A. FreshStructureProbability — ARCHIVAR el modelo probado

Informe: strategies/FreshStructureProbability/reports/INDEPENDENT_OBSERVER_NEGATIVE_RESULT_20261018.md.
Protocolo anterior a scores: INDEPENDENT_PREQUENTIAL_PROTOCOL_20261018.md, misma carpeta.

BTC1M→4h y1D completos. Pivots estrictos2izq/2der confirmados, estados tendenciaU/D/mixto, primer toque±ATR14 conocido al origen en24h. Entrenamiento sólo al madurar24h incluso si toca antes. Ventana180d, shrink20 fijos. Cuatro modelos: climatología, tendencia diaria simple, pivots y combinado.

11418 pronósticos:11411válidos,2ambiguos,5censurados.1903medianoches válidas.24controles sintéticosPASS. Unknown debía caer a benchmark; en datos observados estructura conocida100%. No inferenciaIID ni PnL.

| Modelo | Brier | Logloss |
|---|---:|---:|
| Climatología |0.628630|1.034203|
| Tendencia diaria |0.630654|1.037788|
| Pivots |0.631770|1.039421|
| Combinado |0.634620|1.044082|

Menor es mejor. Pivots−base ΔBrier+0.003139258/ΔLL+0.005217032; combinado−tendencia+0.003966410/+0.006294837. Deterioran globalmente, CADA año2020–25, todos estados agregados y cohorte00UTC. Bounds de ambiguos conservan signo. No seleccionar intersecciones año×estado favorables.

Decisión: NO promover a trading ni variar ventanas/pivots/shrink para rescatar. Rechaza esta representación/estimador/horizonte, no toda estructura de precio ni todo ML. Disponibilidad temporal no equivale a causalidad económica.

Fullrun a3d3904dcb764db4b987fa0be7883d7d succeeded; auditoría ec58a9386a9f4151b3c1ac8764d28548 succeeded. Root verificó ambos estados terminales.
Auditoría reproduce11418vectores/soportes/scores con etiquetas maduras y confirmaciones≤origen; reutiliza estimador/scoring, no segunda implementación estadística independiente.
Datos hasta2025-12-30 23:59UTC; no2026. Cinco orígenes finales censurados, no tratados como none.

Artefactos persistentes:
- research_scripts/fresh_structure_probability/observer_evaluation_v1.py
- research_scripts/fresh_structure_probability/output_v1/forecasts.jsonl
- research_scripts/fresh_structure_probability/output_v1/summary.json
- research_scripts/fresh_structure_probability/output_v1/manifest.json
- research_scripts/fresh_structure_probability/output_v1/artifact_audit.json
- research_scripts/fresh_structure_probability/calibration.csv
- research_scripts/fresh_structure_probability/audit_api_controls.json
- research_scripts/fresh_structure_probability/adapter_controls.json

Prototipo previo research_scripts/portfolio_roles/causal_multiscale_observer.py quedó inalterado. El código ejecutado es el adapter nuevo. API pública comprobada research.get_candles(...warmup_candles_num=0...) devuelve(None, ndarrayN×6); primera parteNone hizo fallar primer probe de assertion, no falloMCP. Hubo fallo de capacidad del modelo del agente después del fullrun, resuelto retomando artefactos sin repetir run ni cambiar modelo.

### B. FreshAuthorMethods — documental final, datos pendientes

Informe: strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md.

Usuario aportó vídeo https://www.youtube.com/watch?v=1IuNNXIUnvE y resumen de Creamer: contextoGEX→zonas→confirmaciónfootprint→riesgo. No se pudo visionar vídeo; atribuir resumen al humano. Categoría oficial verificada previamente: ganador July2026MonthlyMicroDayTrading, no adjudicar campeonato anual general ni usar prestigio como evidencia de edge.

Conclusión prioritaria: investigar viabilidad de trades agresores del MISMO BTCperp/venue para hipótesis de agresión sin avance y recuperación. GEX opcional, no prerrequisito.
- Footprint requiere trades porprecio/tamaño/lado; OHLCVno lo reconstruye.
- OFI del libro incluye cambios/cancelaciones; no es tradedelta.
- Absorción es hipótesis, no observación automática de iceberg.
- GEX desdeOI depende de supuestos; no es inventario dealer observado. PaperCboe usa datos propietarios de participantes.
- SPYCFDvol0 yPAXGspot no validan microestructura de otra ejecución.
- Fuentes anuncian históricos, pero cobertura real por símbolo/día2020–25 no auditada. RESTBinanceactual y archivos históricos son vías diferentes; no confundir endpoint con historia completa.
- Tardis/Cboe implican revisar coste/licencia/latencia; ninguna compra ni descarga realizada. Ver condiciones actuales en fuentes antes de inferir precio/disponibilidad.
- Carry spot/perp es mecanismo distinto, requiere2patas/fundingasof/financiación/contabilidad; sólo documental, no implementación autorizada. Crabel/ruptura probablemente duplica familias anteriores y no se prioriza.

Próximo gate: inventario real de datos, timestamps de publicación/evento/recepción, gaps/correcciones, instrumento/calendario, licencia y coste. Después protocolo trigger/contexto/ambos frente precio/volatilidad simple y fricción realista. No programar una estrategia con datos ficticios.

### C. FreshPortfolioResearch — diagnóstico final, sin nueva estrategia

Informe: strategies/FreshPortfolioResearch/reports/FRESH_PORTFOLIO_DIAGNOSIS_AND_DESIGN_20261018.md.

Análisis independientes5e4cf8e7d9fe49309d42c75246de9b9a y398f14c4d76e422b953bb9fd63591020 succeeded.
Neto enbps sobre suma nocionalentrada referencia→11:
- SPY24.324→5.552.
- PAXG31.705→9.088.
- BTClong296.583→325.764.
- BTCshort31.791→29.409.

No son retornos de cartera ni estrés dinámico; tamaños endógenos compartidos importan. Mayor actividad SPY triplica exposición temporal y reduce neto. Fricción extra pequeña puede consumir beneficio observado; no asumir que bajar costes resuelve ausencia de señal.

El agente propuso SPYrecuperación diaria, detectó solapamiento con MRprevia y RETIRÓ ejecución automática. Evidencia anterior [MultiAssetSleeves4h](http://localhost:9200/#/backtest/262fb59f-2b20-4247-aa9a-e7823cc3c930):86tradesSPY,neto−5148.18USD,fees2834.83,antesfees−2313.35. No era sólo comisión. Diseño diario sigue provisional, no congelado, sin código ni run.

Conclusión: falta demostrar una fuente de expectativa neta de horizonte corto complementaria. Baja correlación o más participación no bastan. No recortar runnersBTC sin motivo económico, ni lanzar otra MR con nombre nuevo.

## 9. Funding y fuentes externas: decisión actual

El usuario inicialmente rechazó descargadores fundingBTC/ETH, después reabrió discusión y permitió exploración documental paralela. No interpretar eso como descarga/compras ya consentidas.
Informe: strategies/OrchLateralRelativeShock1h/reports/BTC_SINGLE_PERP_FUNDING_FEASIBILITY_20261018.md.
Prioridad si se aborda: coste real específico del BTCperpBinance, no predictor «global» por una sola venue. Diferenciar tasa realizada posterior y expectativa disponible antes. Cobertura2020–25 no auditada. No usar2026 ni ampliar aETHporinercia.
VIX/CFTC se descartaron por el usuario como dependencia operativa de esta etapa. No reabrirlos sin razón explícita.

## 10. Correcciones previas del framework

Hubo autorización humana explícita para:
1. Persistencia de curva numérica de equity en backtests normales.
2. Liberación correcta de reserva al ejecutar órdenes con precio distinto del solicitado: reserva por precio enviado, ejecución real parafee/PnL.
Corregidas y verificadas en etapa previa; se informaron148tests entonces. Eso es evidencia histórica, NOtest suite ejecutada ahora ni permiso para tocarframeworknuevo. Rama live real excluida de esas tareas; simulaciones compartidas, incluidoMC, pueden verse afectadas por contabilidad corregida. Comparar sólo resultados de motor corregido y no mezclar cifras antiguas.

## 11. Qué debe hacer el siguiente agente

1. Leer este documento y los tres informes finales. Verificar estados existentes antes de ejecutar; los tres agentes frescos terminaron y no tienen jobs pendientes propios.
2. Mantener baseline/lockbox y archivo de resultados negativos. No repetir modelo pivots1D/4h ni MRSPY por defecto.
3. Elegir con criterio una continuación concreta:
   - viabilidad histórica de flujo BTCperp propio con datos reales accesibles, empezando inventario/documentación y condiciones; cualquier compra/integración nueva requiere decisión humana;
   - o hipótesis de payoff distinto compatible con velas y con evidencia/mechanismo claramente diferenciados de las familias previas.
   No existe ahora una nueva estrategia pendiente de fullrun ni receta aceptada que sólo necesite optimización.
4. Antes de ejecutar: hipótesis, mecanismo, benchmark/ablación, reloj causal, costes, muestra, criterios de descarte y límite de variantes. Diseñar señal/ejecución para instrumento realmente disponible.
5. Evaluar incremental y luego cartera real compartida. No sumar curvas ni seleccionar mejoresmeses de cada pata. Registrar todos los intentos y reconocer selección adaptativa.
6. Validar robustez si aparece señal prometedora: costes/latencia/vecinos/temporalidad/concentración yMCcondependencias pertinentes. No abrir2026hasta congelar candidato.
7. Actualizar registro central y comunicar hallazgos con honestidad. Libertad de proponer cambios de rumbo; ninguna garantía de que exista estrategia robusta que alcance todas las metas.

## 12. Mapa de lectura y persistencia

Todos los siguientes paths son relativos al proyecto que ejecuta Jesse; los reportes se guardaron por MCP. No asumir acceso a estos paths en el filesystem del asistente si se usa otrohost/Docker.

Prioridad:
1. Este PHASE2_RESEARCH_HANDOFF_20261018.md.
2. FreshStructureProbability/reports/INDEPENDENT_OBSERVER_NEGATIVE_RESULT_20261018.md.
3. FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md.
4. FreshPortfolioResearch/reports/FRESH_PORTFOLIO_DIAGNOSIS_AND_DESIGN_20261018.md.
Los3últimos están bajo strategies/.

Historia central:
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_RESEARCH_LEDGER_20261018.md
- strategies/MultiAssetBreakout4h/reports/PHASE2_PROGRESS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PORTFOLIO_ROLES_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_PORTFOLIO_DIAGNOSIS_20261018.md
- Reportes ORCHESTRATION_ROUND*_RESULTS/REJECTIONS bajo reports de referencia.
- strategies/PortfolioSpyPersistent4h/reports/AUTHOR_METHODS_GEX_FOOTPRINT_ROADMAP_20261018.md (revisión anterior, reemplazada como prioridad por informe fresco).
- strategies/AnglePortfolioPaxgDivergence4h/reports/OPEN_SOURCE_ML_CAUSAL_REVIEW_20261019.md (fechaUTC del filename; no evaluación2026).
- bot/docs/multi-asset-pivot-handoff.md es plan histórico original, no estado actual.

Scripts/artefactosML persistentes detallados arriba. Analysis temporales pueden caducar; reconstruir usando snapshots completos si se necesita. No depender del store de functions ni memoria de chat previo para continuar.

## 13. Estado al entregar

Tres agentes frescos completed. FullrunML y auditoría de artefactos confirmados succeeded por root; informes finales guardados. Ninguna nueva candidata aceptada, ni obligación de repetir corridas. Referencia y2026 intactos. No operaciones, compras o nuevas fuentes integradas. Trabajo que queda: nueva decisión de investigación fundada, no reparación pendiente de la última tanda.
