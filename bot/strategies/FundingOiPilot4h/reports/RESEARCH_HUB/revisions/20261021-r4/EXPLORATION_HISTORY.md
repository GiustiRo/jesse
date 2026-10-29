# Historial de exploraciones ejecutadas y control de repetición

Revisión 20261021-r4; 2026-10-21T14:23:19Z. Esta revisión corrige el inventario inicial del Hub. El historial incluye propuestas, experimentos posteriores, controles, reusos, equivalencias, errores, retiradas sin ejecución y cierres. Leer sólo los handoffs no basta.

## Alcance comprobado y límites
Se listó por MCP la raíz strategies/ sin truncar (574 entradas, incluidas carpetas auxiliares y __init__.py; NO son574estrategias económicas ni574experimentos).
Se inventariaron colecciones de reportes y se leyeron los cierres de las14familias siguientes. El registro conserva47referencias de evidencia. MultiAssetRetestBtcShort4h contiene521entradas en el listado recursivo y ResearchSpyReference4h128; son archivos/directorios, no conteos de sesiones.
La revisión de cierre no vuelve a auditar todos los fills, fuentes o jobs de cada experimento. Antes de una propuesta concreta, bajar de esta familia al protocolo, matriz y fuente exactos. No se afirma conciliación global porID de todas las sesiones del servidor. El inventario recursivo deFundingOiPilot4h truncó a1000entradas y no se usa como censo exhaustivo; sus decisionesV1–V6 y conteos conciliados permanecen como fuente de ese bloque.
El JSON asociado organiza evidencia por pregunta y resultado. Los47reportes incluyen cierres y diagnósticos superpuestos: NO sumar sus conteos como total nuevo ni considerarlos observaciones independientes.

## Secuencia y resultados
### PHASE2 — Fase 2: ejecución, componentes, costes y capacidad
**Probado:** Entradas breakout/retest, shorts BTC, esquinas RSI/target, vencimientos24/48/72h, atribución BTC long/short frente a3activos, reglas dependientes de fee/fijas, cuota individual y capacidad compartida, permutaciones del formulario.

**Resultado registrado:** Los controles comparables y de capacidad ya existen. Más retorno con más exposición no resolvió regularidad. Acortar shorts no fue adoptado; falló una esquina de sensibilidad. Permutar formulario no cambió prioridad interna del motor.

**Para evitar repetición:** No proponer otra vez comparar BTC solo vs3activos, liberar capacidad, short24/48h o cambiar orden del formulario sin leer estos controles. Una verdadera prioridad interna distinta no queda probada por los runs del formulario.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_COMPARABLE_ATTRIBUTION_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_SHARED_CAPACITY_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_SHORT_SENSITIVITY_AND_TEMPORAL_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_SHORT_EXPIRY_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_FIXED_FEE_RULES_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_ROUTE_ORDER_RESULTS_20261018.md

### ORCH — Orquestación rondas1–5 y cartera por funciones
**Probado:** Asignación con reloj común/riesgo igual, reversión de rango, short mínimoR/reclaim, salida completa3R/5R, parcial50%a2R, guardas mensuales, short diario, reversión rápida, canal de baja volatilidad, Turtle diario, rotación mensual, una entrada short por episodio, calendario SPY4/4, shock relativo BTC/ETH; PAXG contextual y SPY con mayor participación.

**Resultado registrado:** 18 backtests económicos de la orquestación, no total global. Ninguna variante promovida. La combinación por funciones tampoco sustituyó referencia. Se retiró un expiry24h porque ya existía, y un rechazo de subasta por duplicación; retiradas no equivalen a backtests negativos.

**Para evitar repetición:** No reiniciar estas familias con otro nombre o rejilla de umbrales. Conservar parcial como comparador de menorDD y distinguir hipótesis retirada, fallo técnico y rechazo económico.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_RESEARCH_LEDGER_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND1_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND2_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND3_REJECTIONS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND4_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND5_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/PORTFOLIO_ROLES_RESULTS_20261018.md

### BTC_ANGLES — Ángulos BTC y observador predictivo
**Probado:** Volumen, estructura short, aceptación/reclaim del retest, relojes por eventos y falta de progreso; observador causal1D/4h+pivots con first-touch24h y estimador congelado.

**Resultado registrado:** Las variantes BTC del cierre no se aceptaron. El observador estructural empeoró Brier/logloss globales, por año y cohorte; recipe archivado. Los scores predictivos no son PnL de trading.

**Para evitar repetición:** No llamar novedoso a añadir volumen, pivots o falta de progreso sin comparar receta exacta. No recuperar el observador variando horizonte/ventana/shrink después de su fallo.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md
- strategies/FreshStructureProbability/reports/INDEPENDENT_OBSERVER_NEGATIVE_RESULT_20261018.md

### FRESH — Diagnósticos independientes de cartera y viabilidad de datos
**Probado:** Eficiencia por nocional y capital-tiempo, mayor participación SPY/PAXG; evaluación documental de métodos de autor, flujo real, GEX y carry.

**Resultado registrado:** Más participación deterioró eficiencia en los contrastes observados. La propuesta SPYMR se retiró por duplicación/evidencia previa. Viabilidad de fuentes es investigación documental, no estrategia ejecutada ni rentabilidad acreditada.

**Para evitar repetición:** No tratar documentos de viabilidad como runs o ideas aún pendientes de ejecutar. Volumen0 del proxySPY no acredita flujo del instrumento nativo; un requisito de datos no equivale a una ventaja validada.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_RESEARCH_LEDGER_20261018.md
- strategies/FreshPortfolioResearch/reports/FRESH_PORTFOLIO_DIAGNOSIS_AND_DESIGN_20261018.md
- strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md

### SPY_PAXG_INITIAL — SPY/PAXG: etapa independiente inicial y calendario PAXG
**Probado:** SPY apertura/drive/beta lenta y control; PAXG shocks en ambos sentidos, retest, fin de semana vs hábil, vecinos0.75/1/1.25ATR, controles targetMARKET y cuenta compartida.

**Resultado registrado:** 17 backtests de esa etapa:5SPY+12líneaPAXG. La integración PAXG0.75 mejoró modestamente CAGR/DD pero no regularidad; no sustituyó referencia. Las cinco pruebasSPY de este bloque no promovieron candidata.

**Para evitar repetición:** No volver a descubrir calendario de fin de semana, shocks o beta lenta como pruebas vírgenes. La etapa posterior de atribución/estructurasSPY sí produjo candidatas de desarrollo: este rechazo inicial no es el veredicto final de todaSPY.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/SPY_PAXG_RESEARCH_RESULTS_20261018.md
- strategies/ResearchPortfolioPaxgWeekend075/reports/PAXG_SHARED_ACCOUNT_RESULTS_20261018.md

### R20_R40 — SPY/PAXG: R20 y R40
**Probado:** R20: diez recetas por activo de eventos/regímenes. R40: diez por activo de ciclos/estado, estacionalidad, espectro, mechas, tendencia adaptativa, recuperación, CUSUM, relación beta, ocupación, entropía ordinal, segmentos, rachas y subastas.

**Resultado registrado:** R20:20runs completos, cuatroSPY positivos/cuatro negativos/dos sin trades; diezPAXG negativos. R40:20completos,18negativos/dos sin exposición. Sin sustituciones robustas. No son40mecanismos independientes.

**Para evitar repetición:** Cruzar predicados y fuentes con matrices antes de sugerir Kalman, ciclos, filtros adaptativos, estacionalidad o nuevas etiquetas para reglas equivalentes. Negatividad de receta no refuta toda familia.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/R20_SPY_PAXG_RESEARCH_RESULTS_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/R40_SPY_PAXG_RESEARCH_RESULTS_20261018.md

### ATTR_R60 — Atribución señal/ejecución/gestión y R60
**Probado:** 34runs:17por activo, C0/Cq, quitarBE/trailing, stopinicial, vencimiento72h, entradaMARKET, cinco seeds de reloj con/sin régimen. R60:20contrastes adicionales de contexto y selección.

**Resultado registrado:** PAXGMARKET conservó una ventaja local frente a retest con más exposición/DD. SPYMARKET simple empeoró; cuatro variantesSPYR60 reprodujeron referencia y máximo incremento fue0.364237USDT en ventana completa. Posteriormente se usaron candidatas en carterasB/C.

**Para evitar repetición:** No inferir alpha por exposición adicional ni contabilizar identidades económicas como evidencia independiente. Una entradaSPYMARKET posterior por ordinal de episodio no equivale al controlMARKETsimple de esta etapa.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/ATTRIBUTION_SPY_PAXG_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/R60_SPY_PAXG_RESULTS_20261019.md

### SPY_LATE — SPY estructural BR/PB y última ronda RESET/MECH
**Probado:** Doce nuevosBR/PB (seis cada familia) y doceRESET/MECH. Ordinal de ruptura, primer contacto/reclaim, entrada por anclas y resets; sólo segunda oportunidad vs posteriores y repricingMARKET.

**Resultado registrado:** BR02 fue pista de eficiencia. PB no demostró mejora robusta. Última ronda retuvo MECH01 (segunda oportunidad) como prioritaria de desarrollo y MECH05 como alternativa de mayor neto. Diagnóstico conjunto posthoc: MECH01 conserva105.62USDT sin3mejores y+10bpsRT, con sólo12trades originales; MECH05/06 fallan ese diagnóstico conjunto. No promoción.

**Para evitar repetición:** No recomendar simplemente estudiar breakout/pullbackSPY o reiniciar desdeBR02. Las continuacionesRESET/MECH ya existen y alimentaron las versionesSPYSecond/Market deB/C. No sumar12estructurales+6PB como18:PB es parte de los12.

**Evidencia:**
- strategies/ResearchSpyReference4h/reports/SPY_STRUCT_R1_RESULTS_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_RESULTS_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_RESET_FINAL_REPORT_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_COMBINED_STRESS_20261019.md
- strategies/SpyStructR1PB01/reports/SPY_STRUCT_R1_PB_FINAL_REPORT_20261019.md

### BTC_R1_R3 — BTC: R1, X03, validaciónR2 y ejecuciónR3
**Probado:** R1: nueve hipótesis enB/C (18fulls); suplementoX03, vecinos/timing/costes y control de reglas deBE PAXG. R2 validación:14sesiones; R3:8nuevas y8referencias reutilizadas.

**Resultado registrado:** X03 tuvo aporte nominal pero no robustez de regularidad a costes/timing; retraso4h eliminó ventaja. R3 retuvoN204 congelada tras controles de ejecución/fee/BE; sin promoción.

**Para evitar repetición:** No volver a ejecutar vecinosX03 ni BE fijo como supuesta novedad. N204 es una evolución ya identificada, no candidata sin historia.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/X03_R2_VALIDATION_FINAL_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_RESULTS_20261019.md

### BTC_R4_R7 — BTC: N204/T403/N503/P604, rondasR4–R7
**Probado:** R4:12hipótesis entradas/salidas/experimentales. R5:10hipótesis/20runsB/C desdeN204/T403. R6:10hipótesis/20runs de filtros y convivencia suplemento/original. R7:14runs nominales de gestión y controles.

**Resultado registrado:** R4 todas redujeron neto. R5 retuvoN503/C504 como mejoras nominales sin cumplir todo. R6/R7 ninguna pasó todas las puertas; P604 fue mejora nominal pequeña. Algunas salidas rentables reprodujeron mecanismos previos, no evidencia independiente.

**Para evitar repetición:** Comparar hipótesis con matricesR4–R7 y atribución de ocupación/capital. No volver a proponer timeout, presión/volumen o reglas de salida sin identificar la receta previa más cercana y diferencia material.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/N204_R4_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/N204_T403_R5_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_FINAL_RESULTS_20261019.md

### BTC_R8_R10 — BTC: Y902, K1001 y K1005, rondasR8–R10
**Probado:** R8:13recetas/26runs; contextuales, experimentales y creativas. R9:20runs de fee/vecinosY902 y variantesK. R10:8runs nuevos parafee/vecinosK1001, incertidumbre y concentración incremental.

**Resultado registrado:** R8 detectó identidadesV801=N503,V803/V805=N204 y retuvoY902. R9 retuvoK1001/K1005. R10K1001 pasó diagnósticos operativos, pero cinco entradas modificadas y concentración enjulio2024; todosICprimarios incluyeron0. Sin validación prospectiva ni promoción.

**Para evitar repetición:** No presentar cinco entradas modificadas como evidencia de muchas operaciones nuevas ni bootstrap/vecinos como OOS. La cartera histórica ya se investigó extensamente; conservar comparadores al mismofee y riesgo.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R9_FINAL_RESEARCH_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R10_K1001_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_TODAY_PROGRESS_ALL_METRICS_20261019.md

### CAPITAL — Gestión de capital y escalado R11–R13
**Probado:** R11:24nuevas+4anclas; R12:28nuevas+12anclas; R13:4nuevas50k+4anclas10k. Combinaciones de riesgo/margen, leverage y tamaño de cuenta.

**Resultado registrado:** La asignación y el riesgo ya fueron estudiados: se eligió perfil de investigación2%portrade/6%agregado/3x. Las curvas de mayor riesgo no acreditan mejor señal. Escalado50k fue ejecutado, no sólo multiplicado algebraicamente.

**Para evitar repetición:** No recomendar definir riesgo/asignación desde cero ni volver a probar10k/50k o3x/5x sin pregunta diferencial. Mantener riesgo común cuando se comparen reglas.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R11_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R13_50K_RESULTS_20261019.md

### OOS_LATER — 2026: K1001, candidatas archivadas y diagnóstico
**Probado:** K1001B/Cnominal/estrés corregidas existentes; comparación ampliada posterior deN204,N503,P604,C504,K1005:20nuevas+4K1001reutilizadas. Diagnóstico de pérdidas y componentes posterior, sin nuevo backtest.

**Resultado registrado:** Ninguna de las cinco candidatas pasó las puertasOOS. K1001Bfalló;Cpasó mínimos con concentraciónSPY. Comparación ampliada autorizada y exploratoria después de observarK1001, no nueva selección confirmatoria ciega. DiagnósticoBTC: ocho longs perdedores y deterioro suplemento; no toda pata corta falló.

**Para evitar repetición:** No volver a presentar candidatas archivadas como no evaluadas2026 ni tratar el año como virgen de toda la trayectoria. Conservar apertura previa y sus protocolos; ello no autoriza nuevas consultas/runs2026. Proxies y runs invalidados siguen explícitos.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/OOS_2026_ARCHIVED_CANDIDATES_PROTOCOL_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/OOS_2026_ARCHIVED_CANDIDATES_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/K1001_OOS_2026_DIAGNOSTICO_20261020.md

### R14_V1_V6 — R14 y la investigación posterior funding/OI V1–V6
**Probado:** R14: quitar suplemento, eficiencia12 y EMA120conpendiente;12nuevas/4anclas. Después: preflight causal/contable, piloto, V1–V6 con precio/funding/OI,screening,selección,confirmación y estrés.

**Resultado registrado:** R14sin variante elegible. V1–V6:209económicas únicas/233slots/24reusos/23intentos técnicos aparte. CHANNEL_P parcial; CROSS_Pscreeneligible sin confirmación posterior. Ninguna candidata aprobada. No extrapolar ese cierre a toda la investigación anterior.

**Para evitar repetición:** R14ya sigue al diagnóstico2026; no presentarlo como siguiente experimento pendiente. El plan de funding deR14 fue continuado: no detenerse en su estado antiguo de 'planificado'. Cualquier interpretación nueva conserva reglas y veredictos originales.

**Evidencia:**
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_RESULTS_20261020.md
- strategies/FundingOiPilot4h/reports/RESEARCH_CONSOLIDATED_DECISION_20261020.md

## Qué cambia respecto del roadmap inicial
La investigación de asignación, exposición, tendencia, estructura, ejecución, carteras y validación histórica ya se realizó en numerosas rondas. No corresponde presentar esos temas genéricos como etapas inéditas.
N204, Y902, K1001, PAXGMARKET y SPYSecond/Market ya tienen historia y funciones concretas; 'definir referencias' significa seleccionar/reconciliar las existentes para una pregunta específica, no diseñarlas otra vez.
Cambiar el objetivo desde regularidad mensual/trimestral hacia20–30%anual puede motivar una lectura posterior de resultados existentes. Registrar ese cambio como interpretación nueva; no alterar los veredictos ni presentar criterios nuevos como prerregistrados entonces. Primero reutilizar evidencia compatible; un nuevo criterio no exige automáticamente nuevos motores.

## Comprobación obligatoria antes de otra prueba
Toda propuesta debe registrar:
1. Pregunta concreta y recetas/experimentos previos más cercanos, con evidencia.
2. Mismo/diferente instrumento, feed, reloj de señal, entradas, salidas, filtros, sizing, riesgo, costos, ventana y motor. Comparar comportamiento, no nombre de clase.
3. Qué ya respondió la evidencia y con qué limitación. Una receta negativa no refuta toda una familia.
4. Diferencia material propuesta y qué información nueva produciría. Una nueva etiqueta, pequeño umbral o combinación de descartes no acredita novedad por sí misma.
5. ¿Puede contestarse con resultados/snapshots existentes? Si sí, priorizar lectura o análisis compatible antes de otro motor.
6. Si ya existe equivalencia económica, reutilizar la sesión como control; si hay duda, comprobar fuente/config/eventos antes de asumir duplicación o independencia.
7. Decisión previa: reutilizar, analizar lo existente, retirar por duplicación o justificar un nuevo experimento. Sólo entonces prerregistrar presupuesto y gates.

Esto es una regla documental para agentes; el panel no implementa un detector automático de duplicados ni bloquea técnicamente runs.

## Pendientes históricos no son pendientes actuales
Un cierre deR8que propongaR9, deSPYBRque propongaRESET, o deR14que planifiquefunding no demuestra que falte esa etapa: se deben leer sus continuaciones.
El control de prioridad interna del motor figura como pendiente en su informe original; las permutaciones de formulario no lo resolvieron. Antes de recomendarlo hoy, verificar si otro trabajo posterior lo cubrió y si condiciona la decisión actual.
CROSS_P sigue sin confirmación posterior en el cierreV1–V6; eso no le otorga prioridad automática.
La transferencia de proxies a instrumentos nativos y la validación prospectiva necesitan alcance propio; no repetir desarrollo histórico para llamarloOOS.
2026 ya fue observado enK1001y en comparación ampliada deN204/N503/P604/C504/K1005, además de diagnósticos posteriores. La ampliación fue exploratoria trasK1001. Se conserva su protocolo; esto no autoriza nuevas consultas de2026ni lo vuelve una reserva virgen para nuevas reglas.

## Próximo paso correcto
Cerrar para una pregunta concreta la comparación contra los antecedentes exactos. Elegir después entre: evidencia suficiente para una decisión, reanálisis de resultados existentes, limitación de datos/ejecución o un experimento distinto y justificado. La exploración BTC genérica de tendencia/exposición queda retirada como prioridad automática.
Sin nuevos backtests, análisis económicos, importaciones, estrategias, instalaciones, reinicios o acceso aPi en esta revisión documental.
