# Decisión final V1 — SIN_CANDIDATA
Fecha: 2026-10-20. Ciclo cerrado conforme al protocolo. No se promueve ninguna estrategia.

## Resultado económico
Se completaron las 96 sesiones previstas de exploración: 12 configuraciones, cuatro cortes cronológicos y una sesión de train/evaluación por corte. Todas terminaron. Los entrenamientos comienzan en septiembre de 2020 y las evaluaciones cubren los cuatro semestres de 2022–2023.

Ninguna configuración cumplió simultáneamente los criterios de train: al menos 30 trades, neto positivo, PF ≥ 1,2 y drawdown absoluto ≤ 25%. Las cuatro decisiones fueron SIN_CANDIDATA y se guardaron antes de iniciar la evaluación correspondiente. Ningún resultado posterior modificó esas decisiones.

El selector permaneció plano durante los 24 meses: cero trades, retorno del índice convencional 0%, DD 0% por ausencia de exposición y PF indefinido. Ese resultado no supera los criterios económicos ni acredita la meta orientativa de 20–30% anual.

## Hallazgos de las ablaciones
H1+OI redujo el DD de evaluación frente al control de precio en los cuatro semestres, pero su PF agregado fue 1,042 y falló todos los entrenamientos. Añadir funding a esa variante redujo el PF agregado a 1,016.

H3+OI ganó 40,19% en enero–junio de 2023, pero perdió los otros tres semestres y su PF agregado fue 1,018. Al retirar su mejor semestre, la suma nominal de los otros tres netos queda en −33,38 puntos porcentuales. Esta suma describe sesiones independientes con capital reiniciado; no representa la rentabilidad de una cuenta continua.

Las tres configuraciones con suma nominal positiva cambian de signo al retirar su mejor semestre. Las señales de funding en H2/H3 también produjeron muestras pequeñas: 2 y 0 trades de evaluación para H2 con funding y combinada; 28 y 15 para H3. Un DD bajo por operar poco no demuestra robustez.

Estos resultados rechazan las reglas V1 bajo sus criterios. No demuestran que toda información de funding u OI carezca de utilidad.

## Cierre técnico
El servicio local de investigación se reinició con autorización del usuario. Se verificaron el puerto 9200, el directorio /src/bot y la ausencia de backtests y sesiones live/paper activas antes de actuar. Las lecturas autenticadas por MCP posteriores fueron exitosas. Postgres, Pi y cuentas no se intervinieron.

El slippage adverso optativo quedó implementado y probado: 279 tests aprobados y Pyrefly sin errores. El [smoke efectivo de 5 bps](http://localhost:9200/#/backtest/65ed1148-59cb-477e-9143-75fee5de93f9) verificó cinco fills ajustados en tres trades, con error contable cero. Esto valida la implementación técnica; no prueba robustez económica de las estrategias.

La auditoría OI identificó 560.390 muestras, 634 ausencias en 156 intervalos y 473 ceros. Se preservaron el dataset, la exclusión de ceros y los límites de disponibilidad y stale. El archivo sigue siendo retrospectivo y no está certificado point-in-time.

Los 96 backtests conciliaron precio bruto − fees + funding = PnL y saldo final. El error máximo observado fue 5,093 × 10⁻¹¹ USDT. Sus contadores persistidos concilian barras, causas y entradas; los cierres forzados posteriores al resumen se registran aparte.

Código común, subclases, configuraciones, datasets, hashes, 12 snapshots de framework, duraciones y dashboard_url reales quedaron preservados. Los cinco archivos de integración conservaron los hashes de fase 0. Los cambios preexistentes no se revirtieron.

Los timeouts de arranque se resolvieron consultando las mismas sesiones, sin duplicar runs. Una página de logs insuficiente se amplió sólo para lectura. Los incidentes están en registry.json y el freeze.

## Fases no ejecutadas
La shortlist está vacía conforme a la regla predefinida. No se ejecutan la confirmación de 2024–2025 ni las 48 sesiones de robustez, y sus slots no se reasignan a tuning posterior. Se utilizaron 96 de las 160 sesiones económicas máximas, más siete intentos técnicos registrados.

No se afirma supervivencia de una candidata a fees duplicadas, slippage, retraso OI, vecinos, máscara común, proxy de marcas o bootstrap. El nominal usa fee 0,00045, slippage cero y funding activo con marcas históricas proxy; los importes de financiación no son exactos certificados. No se simulan latencia ni liquidez real.

No hubo nuevas consultas económicas de 2024–2025 para estas configuraciones ni consultas/backtests de 2026. Tampoco ML, live/paper, órdenes, Pi, commit o push. El backend local queda disponible y no hay backtests activos.

## Evidencia dentro del proyecto Jesse
- RESEARCH_DATA_AND_EXECUTION_FREEZE.md: cierre de fase 0 y límites.
- RESEARCH_PROTOCOL_V1.md: reglas, selección, fricción y presupuesto prerregistrados.
- RESEARCH_V1_IMPLEMENTATION_FINAL.md y registry.json: fuentes, hashes, configuraciones, ventanas e incidentes.
- WALK_FORWARD_EXPLORATION_V1.md: tablas, concentración, las 96 sesiones y sus duraciones.
- Los ocho WALK_FORWARD_*_RESULTS.md: meses, costes, exposición, long/short y selección previa por etapa.
- WALK_FORWARD_COMPARISON_V1.json: comparación MCP de las 48 evaluaciones.
- AUDIT_<strategy>.json: contadores completos por sesión, mes y dirección.
- FROZEN_SHORTLIST_V1.md: shortlist vacía.
- WALK_FORWARD_CONFIRMATION_AND_STRESS_V1.md: fases no ejecutadas y motivo.

## Condición de un eventual ciclo siguiente
V1 se rechaza bajo sus reglas. Un ciclo V2 deberá declarar una hipótesis distinta, sus criterios y presupuesto antes de ejecutar. Los años 2022–2023 ya son desarrollo observado; la reserva interna de 2024–2025 no ofrece independencia absoluta frente a investigaciones antiguas del workspace.

2026 permanece cerrado para esta línea hasta una autorización específica posterior a una candidata inmutable. No se relajan los criterios de V1 para promover retrospectivamente un semestre ganador.
