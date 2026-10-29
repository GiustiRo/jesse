# BTC primero: alcance acordado y objetivo propuesto
2026-10-21. Revisión r8. Integración del feedback del usuario; definición documental, sin ejecución.

## Decisiones de alcance incorporadas
- Foco actual exclusivo: BTC-USDT. Primero evaluar cada operativa individual; PAXG, SPY y la combinación quedan para fases futuras eventuales, sin investigación activa adicional.
- Mantener estrategias independientes. No imponer simetría long/short ni justificar una dirección sólo por la tendencia macro: cada regla necesitaría evidencia propia.
- Reservar para una fase eventual la combinación, su mejora marginal y los diversificadores de retorno individual modesto. La intención del usuario es aplicar el mismo riesgo por operación a los tres activos cuando llegue esa fase. Esto no fija hoy capitales, pesos ni ejecución conjunta.
- Perfil de investigación sin cambios: 2% objetivo por operación, límite agregado de admisión de 6%, 3x aislado. Igual riesgo por trade no equivale a igual volatilidad, riesgo de cola ni contribución a pérdidas. Se acepta diferir esa evaluación conjunta; no se declara resuelto el riesgo de dependencia.
- Conservar la evaluación histórica extensa 2020–2025 y aprovechar la evidencia 2026 disponible. La propuesta de esperar 12 meses futuros no se adopta como paso actual.
- No iniciar nuevos backtests, replays, análisis jobs, optimizaciones, exploraciones, importaciones, captación prospectiva, cambios de código/configuración, paper/live o acceso a la Pi con esta entrega.

## Qué sustituye
R7 fue un borrador para debate y nunca se aprobó. Su prioridad cartera, cuatro libros principales más cuatro de estrés y ventana prospectiva de 12 meses dejan de ser la propuesta vigente. Se conserva intacto para trazabilidad. No hay candidata promovida; r5/r6 conserva sus resultados y veredictos históricos. Los umbrales propuestos aquí no se aplican retroactivamente para cambiar aprobaciones o descartes cerrados.

## Propuesta de objetivo individual BTC — pendiente de acuerdo
El retorno se calcula sobre la equity de una cuenta BTC aislada, con posiciones abiertas valoradas y costos declarados. No estimar este retorno restando PAXG/SPY de una cartera compartida ni atribuir a BTC el CAGR de la cartera.

| Dimensión | Propuesta | Significado |
|---|---|---|
| Rentabilidad | Mínimo objetivo de CAGR neto 30%; aspiración 40–50% o superior | Criterio de ambición del proyecto, no rentabilidad demostrada ni clasificación universal de retorno medio/alto. No exige 30% cada año. |
| Riesgo | Buscar DD de equity ≤20%; techo de evaluación 25% | Meta y límite distintos; no cambiar sizing para fabricar retorno. |
| Calidad económica | PF neto ≥1,20 y neto positivo bajo estrés de costos prefijado | Sobre operaciones cerradas, con exposición abierta y supuestos informados. Estrés numérico pendiente de protocolo. |
| Regularidad mensual | Recuperar ≥65% de meses activos positivos, aspiración ≥70% | Es el criterio histórico verificado; informar también meses calendario, ceros, negativos y meses completos. |
| Regularidad trimestral | Recuperar objetivo de ≥80% de trimestres positivos | Antecedente histórico; transferencia a BTC individual pendiente de acuerdo, no herencia automática de un test de cartera. |
| Mediana mensual | Informar mediana de retornos de todos los meses completos, incluidos ceros | Propuesta adicional: exigir que sea positiva. No fija un mínimo mensual en porcentaje ni equivale al 65%. |
| Concentración | Propuesta adicional: que el resultado aritmético neto siga positivo al excluir los dos mejores meses del período completo | Diagnóstico sobre la trayectoria fija; no es replay ni rentabilidad contrafactual con capital recalculado. Reportar además la exclusión de uno/dos mejores meses en cada año, sin ocultar años negativos. |

Los números nuevos son preferencias para debatir, no umbrales estimados con potencia estadística ni evidencia de que exista una estrategia que los cumpla. No seleccionar valores tras ver qué candidata supera cada corte. Una estrategia positiva que no alcance el objetivo puede ser informativa, sin promoverse automáticamente. No se exige un mínimo positivo todos los meses.

La regularidad se calcula con cambios de equity MTM entre límites mensuales, ajustados por flujos externos si existieran, no agrupando sólo trades por fecha de cierre. El protocolo final debe fijar horario de corte, definición de mes activo, costos/funding y frecuencia del mark. Mes activo no se deduce simplemente de PnL distinto de cero: puede haber actividad o exposición con resultado cero. No excluir meses difíciles, sin operaciones o de baja actividad según convenga. Separar períodos completos de fronteras parciales.

## El 65% y la mediana son diferentes
La frecuencia indica cuántos meses ganan; la mediana indica el retorno central al ordenar los meses.
Ejemplo hipotético de 20 meses: 13 meses de +0,1%, seis de −2% y uno de +30%. Hay 65% de meses positivos y mediana +0,1%, pero un solo mes explica la ganancia. Sin ese mes, el resultado compuesto es negativo. El ejemplo es pedagógico, no resultado de nuestras estrategias.

Por eso conviene conservar la frecuencia, añadir magnitud y revisar concentración y pérdidas. Sobre la misma muestra, una frecuencia positiva superior al 50% normalmente ya implica mediana positiva; informar ambas no son dos confirmaciones independientes. Si una usa meses activos y la otra todos los meses, ni siquiera comparten denominador. No convertir 65% positivo en 65% por encima de un retorno mínimo sin otro acuerdo.

## Historia y 2026: uso permitido e interpretación
2020–2025 sigue siendo la base histórica extensa, ya reutilizada para desarrollo. La ventana heredada es 2020-10-15 inclusiva a 2025-12-31 exclusiva; los extremos son parciales y no se presentan como cinco años calendario completos.

Se conservan y consultan los resultados 2026 ya disponibles, con sus fallos. La aceptación del usuario de utilizar 2026 no convierte esa información en un lockbox nuevo ni autoriza aquí una nueva consulta de velas, prueba o búsqueda. Antes de cualquier futura ejecución habrá que delimitar su pregunta, costo y ventana.

Para recetas congeladas antes de abrirlo, conservar su evaluación original y sus criterios. Si se ajustan reglas o se elige una candidata después de conocer 2026, la evaluación posterior sobre ese mismo tramo es desarrollo/revalidación retrospectiva de esa selección, no OOS limpio. Se puede usar como diagnóstico sin ocultar esta limitación. Tampoco extrapolar su retorno parcial a una renta anual prometida.

## Backtest continuo, ventanas móviles y walk-forward
No son tres alternativas equivalentes.
1. Backtest continuo: evalúa una receta y una trayectoria de capital sin reiniciar cada año. Es la base recomendada para medir retorno, drawdown, costos y regularidad de una estrategia fija.
2. Ventanas móviles de 12 meses: resumen intervalos de esa misma curva, por ejemplo enero–diciembre y febrero–enero. No recalibran parámetros, no exigen esperar un año futuro y las ventanas solapadas no son muestras independientes.
3. Validación walk-forward: fija por adelantado un procedimiento que usa sólo el pasado para seleccionar/estimar reglas y evalúa el siguiente bloque. Si existe recalibración periódica, su frecuencia, criterio, universo, warmup y manejo de posiciones también forman parte de la estrategia. No es una optimización que se añade al final para mejorar una curva desfavorable.

Recomendación metodológica, aún sin ejecución: mantener la evaluación continua de reglas fijas y sus desgloses temporales. Si una futura línea requiere aprender o seleccionar parámetros, diseñar su validación walk-forward antes de buscar y seleccionar, con bloques de evaluación no solapados, causalidad y tratamiento de fronteras explícitos. No adoptar recalibración periódica automáticamente para una estrategia que se desea fija.

Un walk-forward reconstruido después de haber visto todos los años sigue aportando diagnóstico temporal, pero no borra la selección histórica ni recupera un OOS virgen. V1–V6 ya tuvieron investigación walk-forward: consultar sus protocolos y conclusiones antes de plantear otra ronda con distinto nombre. Este documento no fija una división de ventanas nueva ni promete dos baterías de backtests.

## Acción documental siguiente
Acordar los criterios propuestos y contrastar la evidencia BTC individual ya guardada contra ellos, con una matriz que distinga: acreditado / no cumple / falta dato / no comparable. Reutilizar informes antes de calcular o ejecutar otra cosa. No asumir que las referencias K1001/N204 de cartera son cuentas BTC aisladas comparables.

Registrar las brechas que realmente queden. Sólo después proponer un protocolo acotado para resolverlas. No repetir R14, V1–V6 ni otras exploraciones cerradas sin una diferencia material y nueva autorización. Mantener PAXG/SPY/cartera fuera del trabajo actual.

## Fuentes contrastadas
- PHASE2_RESEARCH_HANDOFF_20261018.md, líneas 18–20: ≥65% de meses activos, aspiración 70%, ≥80% trimestres, DD25 y meta anterior negociable.
- N503_R6_FROZEN_PROTOCOL_20261019.md, sección de elegibilidad: M65/Q80 bajo costos/denominadores específicos; no eran medianas ni puertas universales de BTC.
- BTC_R8_FROZEN_PROTOCOL_20261019.md, secciones de auditoría/selección: meses positivos sin redondeo y concentración.
- BTC_R8_Y902_WITHOUT_JAN2022_MONTHLY_REGULARITY_20261019.md: ejemplo histórico del efecto de denominadores y exclusión aritmética, no replay.
- RESEARCH_HUB r4/EXPLORATION_HISTORY.md y r6/VALIDATION_R5_RESULTS.md: antecedentes, límites de comparabilidad y exposición a 2026.
- [QuantConnect, walk-forward optimization](https://www.quantconnect.com/docs/v2/writing-algorithms/optimization/walk-forward-optimization): selección temporal y recalibración.
- [Bailey et al., The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf): reutilización y selección múltiple no desaparecen al cambiar el nombre de la evaluación.
