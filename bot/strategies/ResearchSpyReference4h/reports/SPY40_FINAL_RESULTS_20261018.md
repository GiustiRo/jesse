# SPY40 — diez exploraciones primarias completadas

No se identifica una mejora aceptable de SPY. Las ocho recetas con operaciones pierden después de comisión base; dos no producen exposición. Ninguna merece promoción ni integración de cartera a partir de esta tanda. Un resultado negativo de una receta no invalida toda la familia económica. Se terminaron las diez fuentes fijadas, sin rescates, cambios de parámetros ni sustituciones por falta de muestra.

## Resultados comparables

| ID | Lectura de precio | N | Neto USDT | PF | DD motor % | +5 bps RT | +10 bps RT | Decisión |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| [SPY40-01](http://localhost:9200/#/backtest/3441ac21-d65a-48f4-9f2d-4a025b474c1c) | Ciclo causal 2h | 0 | — | — | — | — | — | Sin operaciones; inconclusa |
| [SPY40-02](http://localhost:9200/#/backtest/47206fe5-b8e0-4650-a7dc-23d0f7949e24) | Componente discontinuo | 58 | -263.42 | 0.80 | -5.30 | -375.09 | -486.77 | Descartar esta receta |
| [SPY40-03](http://localhost:9200/#/backtest/817894dd-a064-4a38-be9c-990c7831e599) | Ocupación y giro final | 15 | -146.58 | 0.59 | -2.56 | -177.44 | -208.30 | Negativa, N escaso |
| [SPY40-04](http://localhost:9200/#/backtest/7e15fa8f-eb4f-4029-af1a-6bae22f1803d) | Entropía ordinal | 189 | -877.35 | 0.79 | -9.85 | -1214.93 | -1552.52 | Descartar esta receta |
| [SPY40-05](http://localhost:9200/#/backtest/a99c090e-fa7d-4ec9-a51d-df265a0373fd) | Respuesta gap/cash OLS | 179 | -1185.05 | 0.60 | -13.05 | -1478.08 | -1771.12 | Descartar esta receta |
| [SPY40-06](http://localhost:9200/#/backtest/c3d874cb-ced8-4c68-8605-73335aae3a6e) | Información cierre/rango | 35 | -660.15 | 0.30 | -6.63 | -727.82 | -795.50 | Descartar esta receta |
| [SPY40-07](http://localhost:9200/#/backtest/fcd709dc-c844-4d40-8e9a-35497ac3681f) | Respuesta por duración de racha | 68 | -453.03 | 0.58 | -5.28 | -575.49 | -697.96 | Descartar esta receta |
| [SPY40-08](http://localhost:9200/#/backtest/79ce393c-4c56-46ae-a1b0-9410a5da2fc8) | Reparación semanal | 0 | — | — | — | — | — | Sin operaciones; inconclusa |
| [SPY40-09](http://localhost:9200/#/backtest/816a9466-705c-4149-a705-b466911dca5f) | Densidad de cierres | 249 | -218.75 | 0.95 | -9.49 | -680.27 | -1141.79 | No supera costes base |
| [SPY40-10](http://localhost:9200/#/backtest/9446bc74-046a-42fb-a65b-531828ea8758) | Presión repetida de barrera | 11 | -33.08 | 0.84 | -1.54 | -52.59 | -72.11 | Negativa, N escaso |

Capital inicial 10 000; riesgo máximo presupuestado por operación 1% incluyendo comisión y reserva; fee 0.00045 por lado en todas las órdenes, isolated 5x, gross máximo 4.4. Ventana 2020-10-15 → 2025-12-31 exclusiva. PF calculado sobre PnL neto por trade. DD de esta tabla es el sampling del motor. No se realizará MTM nuevo: ninguna receta es candidata y no se informa regularidad mensual. Stress añade 5 o 10 bps por roundtrip sobre los mismos fills y tamaños; no simula cambios de ejecución, impacto ni nuevo sizing. Los guiones de cero operaciones indican métricas económicas ausentes, no riesgo cero demostrado. N es operaciones/trades cerrados; no oportunidades independientes. Los fills de entrada y salida son otra métrica.

La [referencia aislada al mismo riesgo](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2) (31 operaciones, neto +751.35, PF 1.493, DD motor −5.213%) no se modifica. Es comparación descriptiva histórica: no certifica alpha, OOS limpio ni equivalencia de exposición. El contraste por receta quedó fijado en la matriz; no se añadieron controles nuevos al no aparecer candidata. Los gates neto positivo, PF≥1.2, N≥30, DD no peor que −25% son cribado descriptivo, no significación estadística.

## Qué información nueva se puso a prueba

01 transforma el precio en fase/amplitud causal de bloques 2h. 02 diferencia variación cuadrática y bipotencia de trece intervalos intradía, partición que suma exactamente el retorno cash. 03 diferencia tiempo de ocupación sobre apertura de la posición final. 04 usa el orden relativo de triples y su entropía frente a historia previa. 05 estima por separado respuesta posterior al gap y al tramo cash con labels ya maduros. 06 contrasta dispersión cierre a cierre, con nocturno, y rango intrabar sin nocturno. 07 condiciona respuesta posterior por signo y duración de racha con shrinkage fijo. 08 examina rechazo semanal con extremo temprano y reparación hacia apertura semanal. 09 construye densidad de cierres con bins de ancho causal congelado. 10 exige dos pruebas de barrera y presión creciente antes de un breakout posterior. Son diez exploraciones diferenciadas, con parentescos explícitos con familias previas; no diez mecanismos estadísticamente independientes.

## Diagnóstico económico

02, 03, 04, 05, 06 y 07 ya presentan PnL de precio negativo antes de comisión. El problema de esas implementaciones excede fricción. 09 obtiene +611.98 de precio bruto, pero paga 830.74 y termina −218.75; es evidencia contra la receta con costes aceptados. 10 obtiene apenas +2.05 bruto, paga 35.13 y pierde −33.08 con once observaciones. Aumentar riesgo no altera esa ausencia de margen económico.

En 09 los largos suman +554.35 y los cortos −773.10, corte observado después del resultado. No se convierte en una nueva receta long-only, ni se presume mejora de cartera. El coste de seleccionar ese lado tras ver diez recetas y el historial acumulado requiere una validación nueva y coordinada; no se usa 2026. En otras recetas también hay lados parciales positivos; se conserva el resultado bilateral primario.

03 (15 trades) y 10 (11) son negativas con muestra escasa; no hay potencia para una conclusión general sobre su mecanismo. 01 y 08 tienen cero fills: los snapshots no conservan vars, contadores ni estados intermedios. No se puede afirmar que nunca hubo ciclo, semana válida o condición de mercado; tampoco medir qué gate bloqueó el evento. Root hizo un diagnóstico sintético separado de bandpass: valores finitos y campos correctos, pero amplitud normalizada sensible a nivel/historia. Esa prueba técnica no contiene datos reales y no explica por sí sola los cero fills. 01 queda congelada y la evidencia económica es simplemente sin exposición. Fuente, resultados y límites del diagnóstico separado: strategies/MultiAssetRetestBtcShort4h/reports/R40_BANDPASS_SYNTHETIC_DIAGNOSTIC_20261018.md.

Las curvas completas del motor se inspeccionaron en cinco auditorías. Ninguna ganancia temporal se confunde con rentabilidad persistente. Las cohortes por año de cierre disponibles en los datos son diagnósticos de trades y no retornos MTM anuales. Una operación que cruza varios meses sigue siendo una sola operación. No se agregan análisis de calendario para buscar porcentajes favorables tras los resultados negativos. No se fuerza regularidad a cada señal.

## Construcción causal y límites

Cada sesión D requiere trece barras 30m desde 09:30 hasta 16:00 NY con DST, y cada barra requiere treinta M1 contiguas y cierre fresh. Los bloques 2h usan cuatro barras completas independientes desde 09:30, 11:30 y 13:30; la media hora final sólo integra D. A es la media de catorce TR de sesiones observadas previas, excluyendo la actual. Se retienen 300 bloques y 400 días; 01 exige 100 bloques y conserva veinte snapshots previos de amplitud. No se imputa calendario ausente ni se representan sesiones parciales como días completos.

Las ventanas son observaciones completas, no una prueba de cobertura de todos los días NYSE. Timestamps M1 completos no certifican que el proveedor no haya rellenado precios ni la exactitud de su calendario. Holiday gaps y early closes pueden cambiar elegibilidad y horas entre observaciones. Guardia civil Mon←Fri/resto día previo evita llamar gap ordinario a una ausencia multidiaria en features que lo exigen. PK frente a CC mezcla deliberadamente intrabar y nocturno; el salto BV/RV con trece intervalos es heurístico, no test asintótico formal.

Los modelos 05/07 excluyen orígenes sin label posterior y sólo usan target≤decisión; el límite 120h alinea labels con failsafe. Features y estados se actualizan en before aun con posición, sin replay. Stop 2A medido desde fill efectivo, salida de fase o primer D posterior cuando procede y deuda de expiración hasta quote fresh. La hora contractual es expiración, no garantía de fill exacto: en esta muestra hubo holds por encima de 72/120h por ausencia de quote. Stops permanecen activos; toda afirmación de microestructura, liquidez o flujo sería injustificada con OHLC.

Warmup 240 velas del motor no equivale a historia diaria suficiente: estrategias con labels 120/252 requieren períodos adicionales en cash. Primer fill de 05 fue 2021-12-01 y de 07 2022-04-12; esas fechas no prueban cuándo terminaron todos los gates. El mayor gross observado en las ocho estrategias con fills quedó bajo 0.70x; 5x es configuración de margen, no exposición real. Las ausencias y períodos en cash forman parte del resultado, no se extrapola retorno a 1x incompatible con el riesgo fijado.

Los proxies aceptados sirven para investigación de precio: SPX CFD BID/10 para SPY. Funding y derivados fuera de alcance. Ningún resultado valida spreads/lot sizes/horario/ejecución de Binance perpetual ni su transporte 24/7. La ventana 2020–2025 está reutilizada extensamente y no se denomina OOS limpio. Se añade esta selección de diez a la cronología acumulada; no se reporta sólo el menos malo.

## Trazabilidad

Matriz SPY40_MATRIX_PROTOCOL_20261018.md, SPY40_FREEZE_ADDENDUM_20261018.md, SPY40_IMPLEMENTATION_CLARIFICATIONS_20261018.md guardadas antes de resultados. Implementación completa en SPY40_IMPLEMENTATION_REVIEW_20261018.md: motor común y diez bloques autocontenidos, readback exacto 10/10 revisado por root antes del primer lanzamiento. Fuentes R40Spy* preservadas en las notas de cada dashboard y en strategies/<clase>/__init__.py. Registro SPY40_SESSION_REGISTRY_20261018.md. Sólo herramientas Jesse MCP; debug_mode=false; configuración global intacta.

Auditorías completas succeeded (fuente en SPY40_ANALYSIS_SOURCE_20261018.md):

- Par 1: 803b4e9b71814d7ead7ad52460db9e7f; SPY40_AUDIT_BATCH1_20261018.md; artefactos results.json y equity_engine.png.
- Par 2: 0bad9bcf93c64493b90f217c828bd256; SPY40_AUDIT_BATCH2_20261018.md; artefactos results.json y equity_engine.png.
- Par 3: bd94d7bf995a4afa9df061908cfdac00; SPY40_AUDIT_BATCH3_20261018.md; artefactos results.json y equity_engine.png.
- Par 4: 4aee4d320ebe4536841c70c9c9a26b29; SPY40_AUDIT_BATCH4_20261018.md; artefactos results.json y equity_engine.png.
- Par 5: 0a9d9f3a20a7475ea9f1bdb98dbee0e8; SPY40_AUDIT_BATCH5_20261018.md; artefactos results.json y equity_engine.png.

## Implicación para la siguiente decisión

La transformación de precio añadió preguntas distintas y produjo evidencia suficiente para cerrar esta tanda sin promoción. Más indicadores sobre los mismos precios no constituyen por sí solos información nueva. Antes de buscar parámetros vecinos harían falta una hipótesis que prediga por qué cambia el payoff neto, un contraste que la separe de beta/lado/calendario, costes de transporte observables y una evaluación futura que incorpore toda la selección previa. No se ejecuta ninguna receta derivada automáticamente.
