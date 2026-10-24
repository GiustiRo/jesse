# K1001 — Diagnóstico autorizado y posible especialización BTC
Fecha local:2026-10-21. Estado: acuerdo de dirección y propuesta de investigación; no protocolo económico ejecutable ni autorización operativa.

El usuario aprueba entender K1001 y mantener siempre un bloque creativo, incluso derivado de K1001. Plantea segmentar en2–3 estrategias BTC (long/short o tendencia/rango), evaluarlas individualmente y eventualmente operarlas en paralelo, posiblemente BTCUSDT/BTCUSDC por restricción one-way. BTCx2–PAXG–SPY es horizonte futuro, no asignación o arquitectura aprobada.

Se supera la restricción previa de no estudiar componentes de K1001 en lo que permite este diagnóstico y propuestas explícitas. No se modifica el resultado de la receta congelada ni se autorizan variantes de riesgo, barridos, nuevos contratos/datasets, economía2026, cartera actual o live/paper. Cada experimento posterior exige pregunta, comparación, presupuesto y protocolo antes de ejecutar. Autonomía investigadora vigente; no volver a pedir permisos rutinarios ya concedidos.

## Hechos contrastados
Cuenta BTC K1001 de tandaP: sesión94ec00b5-7541-4e9a-b685-a98160e1abd4, http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4 . FuenteP_FINAL y R16LegacyBase leídas. Atribución de trades realmente ejecutados dentro del libro único:
- LONG_RUNNER dirección+1:31 cierres, PNL+10650.419092195123USDT.
- CORE_SHORT dirección−1:116 cierres, PNL+4686.29849188876USDT.
- SUPPLEMENT dirección−1:45 cierres, PNL+9191.971406577974USDT.
Sumas reconcilian192/+24528.688990661857; el ledger financiero original usa flotantes sin redondeo. No son resultados de tres cuentas standalone. Las reglas comparten capital/ocupación/prioridad (long,short,suplemento); setups tienen consumo/estado y órdenes pendientes. Separar cambia la selección de entradas, disponibilidad y compounding; filtrar el ledger por origen no simula independencia.
CORE_SHORT requiere EMA120 ascendente, entre otras condiciones. Ser short no acredita especialización en grandes tendencias bajistas ni cobertura de crisis. El bloque long tiene31 trades, sin certificar confianza por superar un conteo arbitrario.

## Análisis crítico
La especialización es hipótesis válida si corresponde a comportamientos/gestiones distintos y mejora evidencia individual o aporte conjunto posterior. No necesita ser inversión espejo de longs, ni las piezas deben estar siempre activas. Añadir un segundo ticker no crea un segundo activo económico; ambas rutas concentran BTC.
Si dos futuros equivalentes tienen long yshort de la misma cantidadBTC simultáneamente, su sensibilidad al movimiento común se compensa aproximadamente durante el solapamiento; quedan diferencias de precio/funding/costos y riesgo de cada posición. El beneficio eventual debe provenir de selección temporal/tamaños/gestiones, no de tener dos nombres. No contabilizar riesgo agregado como cero por netear direcciones y no sumar CAGRs de cuentas capitalizadas por separado.
La primera división diagnóstica debe seguir los3orígenes existentes. No decidir de antemano long/short versus trend/range ni quitar componentes sólo por atribución posterior favorable. Estudiar standalone será un nuevo contrafactual con reglas congeladas, todos los eventos admisibles y capital/costos/riesgo comparables; no un recorte de trades ya elegidos.

## Contratos y adaptación futura
Binance one-way permite una dirección por contrato; hedge permite long+short en mismo contrato: https://www.binance.com/en-IN/support/faq/detail/360041513552 . Esto distingue capacidad del exchange de capacidad del fork.
Revisión readonly local: jesse_live/funding.py validate_live_features restringe funding/OI live a BTC-USDT; jesse_live/binance.py account_balance_usdt lee USDT; jesse_live/reconciliation.py exige one-way parafunding/OI. Por ello no se acredita soporte multicontratoUSDChedge con sólo renombrar ruta. No se cambió código, cuenta, posición o sesión.
Fuente oficial histórica lanzamientoBTCUSDC enero2024: https://www.binance.com/en/square/post/1979323341321 . No extrapolar ejecución contractualUSDC hasta2020. UsarUSDT para generar señalesUSDC es hipótesis de transferencia, no backtestUSDC: se requerirán precios/fills/funding/margen/moneda de liquidación del instrumento ejecutado cuando corresponda. ContratoUSDT actual y costosbase no se cambian.
Comisiones se producen por ejecución yfunding por posición alsettlement, no compensación asegurada entre contratos: https://www.binance.com/en/support/faq/detail/98488a516eb84e3eb34605683dffd554 . No se inicia estrés ni se supone funding idéntico o siemprecoste.

## Orden de trabajo
1. Inventariar registros existentes, revisar fortalezas/debilidades por origen y tiempo, separando atribución realizada y MTM mensual. No fabricar señales ausentes ni atribuciónM1 a partir de cierres.
2. Diagnóstico de menor desempeño2024–25: oportunidades, selección, ejecución, gestión y costos. Primero medición; no elegir filtros retrospectivos.
3. Proponer comparación acotada de componentes standalone originales si el diagnóstico la justifica; preservarK1001original como control.
4. Diseñar especialización/idea creativa material con evidencia y protocolo propio, sin obligarla a copiar/invertirK1001.
5. Sólo después evaluar convivencia y arquitectura de ejecución, incluyendo capital/riesgo agregado y comparación con coordinador de órdenes. BTCx2/PAXG/SPY siguen futuro eventual.

Ninguna candidata nueva, derivados implementados, backtests, imports, cambios framework/globales o live/paper por esta propuesta. Ownerreversion_history recibió subtarea documental de viabilidad de registros, sin run_analysis ni motores hasta revisión de protocolo porroot. Se mantiene bloque creativo y autonomía.
