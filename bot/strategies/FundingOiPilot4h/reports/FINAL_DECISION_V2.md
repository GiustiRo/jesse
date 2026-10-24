# Decisión final V2 — SIN_CANDIDATA
Fecha: 2026-10-20. Investigación cerrada conforme al protocolo. No se promueve ninguna estrategia.

## Qué se completó
Se ejecutaron las 16 sesiones ATR previstas y se reutilizaron 16 controles fijos V1 previamente verificados: 32 slots nominales, cuatro configuraciones y cuatro folds con train/evaluación. Todas las sesiones terminaron. Los cuatro smokes técnicos previos quedan separados.

El trabajo se distribuyó entre tres subagentes: ATR sin OI, ATR con OI y auditoría independiente. Inicialmente cada rama pudo gestionar dos backtests simultáneos. Tras errores de respuesta de la API/MCP se redujo a uno por rama, dos en total. Los timeouts se resolvieron leyendo los mismos IDs; no hubo duplicados, cambios de reglas ni reinicios.

## Decisión económica
Las cuatro selecciones E1–E4 fueron SIN_CANDIDATA. Ningún entrenamiento cumplió simultáneamente:
- al menos 30 trades;
- neto positivo;
- PF ≥ 1,2;
- drawdown absoluto ≤ 25%.

La selección de cada fold se guardó antes de solicitar cualquiera de sus dos evaluaciones ATR. La auditoría independiente verificó los ocho timestamps y los reportes previos. Los controles fijos y sus evaluaciones ya eran conocidos de V1; no se presentan como una muestra nueva.

La shortlist queda vacía porque ninguna configuración fue seleccionada al menos una vez. El selector permaneció plano durante los 24 meses de 2022–2023: cero trades, índice convencional de 10.000 constante, retorno 0%, DD 0% por ausencia de exposición y PF indefinido. No se acreditó la meta orientativa de rentabilidad anual.

## Qué mejoró en la exploración
La comparación diagnóstica de las cuatro evaluaciones muestra:

| Variante | Trades únicos | PF agregado | Semestres positivos |
|---|---:|---:|---:|
| Fija sin OI | 342 | 0,975 | 1/4 |
| ATR sin OI | 332 | 1,093 | 3/4 |
| Fija con OI | 228 | 1,042 | 2/4 |
| ATR con OI | 223 | 1,172 | 4/4 |

ATR redujo DD y turnover frente al control fijo correspondiente en los cuatro semestres, tanto con OI como sin él. Mejoró el neto en tres de cuatro; rindió menos en enero–junio de 2023. La intervención cambia protección, tamaño, ocupación y entradas posteriores, de modo que no identifica un efecto aislado del stop entre operaciones idénticas.

ATR con OI obtuvo +10,81%, +3,08%, +7,96% y +2,88% por semestre. Son retornos de cuatro sesiones independientes, cada una reiniciada con 10.000 USDT; no se suman ni anualizan como rentabilidad de una cuenta continua.
Su PF agregado fue 1,17171 y el peor DD de evaluación fue −10,94%. La suma nominal de sus netos fue +2.474,37 USDT y siguió positiva, +1.392,89, al retirar el mejor semestre. Es una atribución descriptiva sobre sesiones con capital reiniciado.

Esto representa una mejora exploratoria respecto a V1, pero no permite promoción retrospectiva. ATR con OI tuvo en los entrenamientos:
- E1: neto −0,20%, PF 0,999 y DD −29,08%;
- E2: neto +10,59%, PF 1,059 y DD −30,65%;
- E3: neto +14,01%, PF 1,063 y DD −30,65%;
- E4: neto +23,08%, PF 1,087 y DD −30,65%.

Sus cuatro semestres positivos convivieron con 11 meses negativos y una racha de tres meses negativos. El peor mes fue −5,89%, ligeramente peor que el control fijo con OI (−5,78%). No todas las métricas mejoran. Su PF agregado tampoco alcanza 1,2; no se redondea para aprobar.

## Integridad y límites
La conciliación de las 32 sesiones nominales verificó precio bruto − fees + funding = PNL y saldo final. El error máximo fue 5,093 × 10⁻¹¹ USDT, frente a tolerancia de 10⁻⁶. Las 16 auditorías ATR conservan contadores mensuales, entradas, salidas y cierres forzados posteriores al resumen. Algunos indicadores open_trades/open_pl son previos a ese cierre; el ledger, trades y saldo finales conciliaron, sin inferir una posición residual activa.

Código, parámetros, datasets y configuración permanecieron congelados. Se preservaron fuentes, hashes, fechas, dashboard_url reales, duraciones y respuestas de error en el registry y los progresos de rama. Los 16 backtests nuevos aparecen una sola vez en el listado MCP y no queda ninguno activo. Su suma de duración de motor fue 216,11 segundos; no es el tiempo de pared de orquestación.

El nominal usa slippage cero; funding conserva marcas proxy y OI es un archivo retrospectivo sin certificación point-in-time. Las ventanas 2022–2023 son desarrollo observado. Las curvas mensuales tienen resolución diaria aproximada, y las sesiones con capital reiniciado no sustituyen un replay continuo. La validación técnica previa no demuestra supervivencia económica a fricción.

## Fases no ejecutadas
Con shortlist vacía no se ejecutaron las ocho sesiones de confirmación de 2024–2025 ni las 24 de robustez. Se consumieron 32 de los 64 slots nominales V2, contando las 16 reutilizaciones; los restantes no se reasignan a tuning.

No se afirma que una candidata sobreviva fees duplicadas, slippage, vecinos, retraso OI o cambios de proxy. Tampoco se abrió 2026. No hubo ML, RST, live/paper, órdenes, Pi, cambios globales, instalaciones, reinicio, commit o push.

## Continuidad
V2 queda cerrada. La escala por volatilidad y OI dejan una hipótesis exploratoria más consistente que el esquema fijo, pero no una estrategia aprobada. Un ciclo siguiente debe definir una pregunta distinta y un presupuesto antes de probarla, declarando todos estos datos como observados. No corresponde ajustar direcciones, ventanas o criterios hasta que esta misma variante pase.

La reserva interna 2024–2025 no se abrió en V2, aunque otras investigaciones antiguas ya usaron esos años. 2026 sigue cerrado y requeriría una autorización específica para un examen posterior con candidata y reglas inmutables. Este cierre no autoriza operar.

## Evidencia guardada dentro del proyecto Jesse
- WALK_FORWARD_EXPLORATION_V2.md: tablas, meses, las 32 sesiones y límites.
- REGISTRY_V2.json: fuentes, hashes, configuración, datasets, sesiones, selecciones, incidentes y estado final.
- WALK_FORWARD_E1_SELECTION_V2.md a WALK_FORWARD_E4_SELECTION_V2.md y V2_AUDIT_CHRONOLOGY.json: decisiones previas verificadas.
- Los ocho WALK_FORWARD_*_RESULTS_V2.md y auditorías por sesión/etapa.
- V2_FINAL_COMPARISON.json y V2_INDEPENDENT_AUDIT_20261020.md: agregados y auditoría independiente.
- FROZEN_SHORTLIST_V2.md: lista vacía.
- WALK_FORWARD_CONFIRMATION_AND_STRESS_V2.md: fases no ejecutadas y motivo.
- V2_BRANCH_P_PROGRESS.json y V2_BRANCH_POI_PROGRESS.json: trazabilidad de los subagentes.
