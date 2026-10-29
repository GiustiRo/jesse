# Handoff Fase 2 después de R60

Fecha local: 19 de octubre de 2026.

## Estado completado

El usuario autorizó diez exploraciones por símbolo en paralelo. Se completaron exactamente veinte backtests nuevos: diez SPY y diez PAXG. Se reutilizaron dos especialistas, con un máximo de dos backtests por especialista y cuatro globales; un análisis por especialista y dos globales.

No se repitieron las referencias como nuevos fulls. No hubo optimización adaptativa ni cambios de fuentes después de resultados. Los veinte snapshots de código, formularios y conjuntos de hiperparámetros registrados fueron verificados por root. Todos coinciden con la matriz; DNA vacío. Los veinte resultados MTM a cierre diario UTC concilian con fills, cantidades, fees y wallet. Todos los trabajos terminaron, sin ejecuciones pendientes.

Informe central: R60_SPY_PAXG_RESULTS_20261019.md.
Protocolo previo: R60_SPY_PAXG_FROZEN_PROTOCOL_20261019.md.
Auditoría: R60_ROOT_IMPLEMENTATION_REVIEW_20261019.md.
Calendario reproducible: R60_MTM_SOURCE_20261019.md y R60_MTM_RESULTS_20261019.md.

## PAXG: comparación local favorable y dependencia temporal

Se probaron cinco contextos, cada uno retest y MARKET: Donchian 24, Donchian 28, ADX mínimo 24, ADX mínimo 28 y EMA rápida 24. Cada contexto cambia una sola pieza respecto al centro; salidas y riesgo permanecen iguales.

MARKET supera al retest en los cinco pares. Las diferencias de neto son 425,66; 409,32; 143,48; 341,47 y 415,41 USDT, respectivamente. Las cinco diferencias siguen positivas con 10 bps RT adicionales, y las cinco MARKET conservan beneficio con ese recargo. Aumentan también tiempo expuesto y drawdown en todos los pares.

Con las dos referencias hay doce trayectorias de fills y doce curvas distintas. Comparten la misma historia y muchos episodios: no son doce muestras independientes.

En TODOS los pares, la diferencia M−retest por cohortes de año de cierre es negativa en 2021, 2022 y 2023 y positiva en 2024 y 2025. Las cohortes no son rentabilidad MTM anual. Las diez variantes quedan negativas sin sus tres operaciones de mayor PnL; MARKET ADX24/ADX28 también sin su mejor operación.

Mantener como candidata fija el [MARKET central](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae), no sustituir automáticamente por Donchian24 por ser el mayor neto de la tanda. El centro tiene N38, neto 962,13, PF1,57, Sharpe0,377, DD motor −7,65%, CAGR1,78%, 17/61 meses y 10/19 trimestres completos positivos. No está integrado o validado para operar.

En orígenes exactos compartidos, MARKET paga más caro y su PnL normalizado es peor. El mejor resultado global mezcla selección de fills, gestión anclada al precio de entrada, capital y ocupación posteriores; no demuestra mejor precio de ejecución ni un efecto causal puro.

## SPY: referencia conservada

Las diez perturbaciones fueron g mínimo 0,10/0,25; g máximo 0,50/0,75; Donchian24/28; ADX24/28; EMA rápida16/24. g=(close−máxima Donchian previa)/ATR. No se combinaron parámetros.

La [referencia Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) mantiene N31, neto751,35, fees286,48, Sharpe0,458 y DD motor −5,21%. Tiene 15/61 meses y 9/19 trimestres completos positivos.

Cq, máximo0,75ATR, Donchian24, Donchian28 y EMA16 comparten exactamente trades, campos económicos y curva numérica. Es estabilidad local, no cinco confirmaciones independientes. Los valores efectivos de hiperparámetros se comprobaron; las variantes sí aplicaron sus cambios. Los snapshots no cubren todo arming sin fill.

EMA24 añade sólo 0,364237 USDT y conserva los mismos recuentos de calendario y DD diario. No se escoge ese máximo. Los filtros mínimos de ruptura y los umbrales ADX24/28 reducen el neto; varias alternativas también empeoran DD. Ninguna mejora material justifica sustituir la referencia. Las diez quedan negativas sin sus tres operaciones de mayor PnL.

## Condiciones persistentes

- Ventana 2020-10-15 a 2025-12-31 exclusiva. 2026 permanece cerrado.
- Capital aislado de 10.000 USDT, riesgo planificado 1%, fee0,00045 por lado en todos los tipos, isolated5x, cap4,4 y sin piramidado. Reserva0,001 sólo sizing.
- Una ruta4h y data routeM1 del mismo activo, warmup240, fast/debug false.
- SPY conserva exactamente UTC Mon–Fri00–20 para historia y barras abiertas00–16 para entradas. PAXG sin ventana. No filtrar gestión con nuevo calendario o quote guard.
- Proxies aceptados SPX CFD BID/10 y spot PAXG para desarrollar acción de precio. Funding y nuevas fuentes fuera de este estudio.
- Sin instalaciones, scripts de investigación, cambios de framework/config global, reinicios, live/paper/Pi o nuevas rutas BTC.
- Todo el proyecto por MCP; fuentes autocontenidas y snapshots completos. Enlazar dashboard_url y guardar informes con save_strategy_report. No usar resultados truncados ni FS/SQL/red como fallback.
- Mantener cronología R20/R40/atribución/R60, incluidos negativos e identidades. Estos veinte son sensibilidad y selección de evento, no veinte descubrimientos independientes.

## Continuidad, sin nuevas ejecuciones comprometidas

PAXG: conservar la candidata central fija y evaluar la dependencia temporal. Estabilidad entre vecinos reduce una preocupación concreta de fragilidad de parámetro; no elimina selección histórica ni sustituye validación fuera de muestra. No abrir 2026 para clasificar vecinos.

SPY: esta tanda no respalda seguir moviendo números cercanos para superar marginalmente una tabla. Una siguiente hipótesis podría distinguir primera ruptura/retest reciente de reentradas tardías en un tramo maduro, o confirmar el retroceso mediante estructura de precio. Su contrato se debe fijar antes de ejecutar, separando señal y ejecución. No se implementó ni probó esa hipótesis aquí.

El usuario quiere mejorar SPY antes de volver a BTC. Conservar ese foco y reconocer que aún no se ha demostrado una mejora robusta para ambos activos. No aumentar riesgo ni combinar vecinos ganadores para declarar éxito. La ronda de veinte está cerrada.

## Informes de especialistas

SPY: strategies/ResearchSpyReference4h/reports/R60_SPY_FINAL_REPORT_20261019.md y R60_SPY_EXACT_RESULTS_20261019.md. Auditorías por lote y pares íntegros en esa carpeta.

PAXG: strategies/R60PaxgN24Retest4h/reports/R60_PAXG_FINAL_REPORT_20261019.md y R60_PAXG_EXACT_TABLE_20261019.md. Auditorías A/B y manifiesto de diez sesiones en esa carpeta.

Métricas exactas, URLs, fuentes y veinte resultados MTM están preservados dentro del proyecto Jesse en la máquina que lo ejecuta.
