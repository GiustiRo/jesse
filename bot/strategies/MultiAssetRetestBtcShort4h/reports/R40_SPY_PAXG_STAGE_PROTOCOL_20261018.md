# R40: segunda tanda de veinte escenarios nuevos

El usuario autoriza otros veinte escenarios exploratorios después de R20, con nuevos indicadores, lecturas de precio, combinaciones de timeframes y enfoques distintos. Reparto: diez SPY y diez PAXG. Se conservan los especialistas existentes y los límites de concurrencia. Leer R20_SPY_PAXG_RESEARCH_RESULTS_20261018.md y PHASE2_RESEARCH_HANDOFF_R20_20261018.md antes de diseñar.

## Registro antes de resultados

IDs SPY40-01..10 y PAXG40-01..10, clases R40Spy... y R40Paxg... autocontenidas. Cada especialista guardará matriz de diez recetas antes de escribir y lanzar. Root revisará matriz y código antes de ejecución.

Cada fila debe expresar: mecanismo que se intenta detectar; qué información añade frente a familias anteriores; TF de señal y contexto; reglas exactas, causalidad de denominadores y estados; entry, stop, salida, horizonte, consumo y rearmado; frecuencia esperable cualitativa y razones para esperar una muestra evaluable; solapamiento conceptual y contraste relevante. Frecuencia prevista no es una medición de oportunidades ni una promesa de N.

No contar como nuevas exploraciones diez umbrales, inversiones de lado, cambios de horario o indicadores equivalentes para rescatar pérdidas. Las hipótesis pueden compartir familias, sin afirmar independencia. Nuevos indicadores deben aportar una transformación o lectura que se explique; un nombre nuevo no demuestra información adicional. Evitar condiciones extremas que previsiblemente no produzcan exposición en el rango disponible. No explorar velas o resultados de 2026.

## Contrato invariable

Históricos existentes aceptados: SPX CFD BID/10 para SPY y spot PAXG para investigar reglas de precio destinadas a perpetual. Sin funding, volumen ficticio, fuentes nuevas ni BTC. Desarrollo 2020-10-15 a 2025-12-31 exclusiva; 2026 reservado. No scripts de investigación, instalaciones, framework, reinicios o live/paper.

Capital aislado10.000USDT, riesgo planificado1% por operación, comisión0,00045 por lado incluidas LIMIT,5x aislado, nocional bruto4,4x, sin piramidado. Reserva de sizing10bps no es slippage aplicado. Comparadores aislados existentes y referencia permanecen, no hace falta rerun sin causa. No cambiar parámetros tras observar resultados.

Hasta2backtests por especialista/4globales y1análisis por especialista/2globales. Operaciones de proyecto y reportes solo Jesse MCP. Corregir errores técnicos según herramientas; no usar shell, filesystem, SQL o red como bypass del MCP.

## Cribado y validación

Mismos criterios descriptivos: neto positivo, PF≥1,2, unas30operaciones yDD no peor que−25%. Menor muestra es inconclusa, no ausencia de efecto. Preservar pérdidas y ceros; no relajar filtros para generar N. Evaluar fees y recargos estáticos5/10bpsRT, concentración, temporalidad, capital-tiempo y aportación frente a referencia. Los recargos de todos los fills se distinguen de nuevas simulaciones.

Los objetivos de regularidad corresponden al portfolio. Si se informa regularidad, usar MTM con fills y precios a cierre UTC, no cohortes de cierre ni Portfolio00:01. No sumar curvas aisladas para representar cuenta compartida. Una candidata defendible exige protocolo adicional antes de sensibilidades o integración; esos controles no rellenan el cupo de veinte escenarios.

R40 añade selección a toda la investigación anterior. Ninguna nueva subdivisión de2020–2025 es OOS limpio. No garantizar que otra tanda producirá una mejora ni elegir una curva porque sea la mejor de veinte. Si no hay candidata, documentar el objetivo pendiente y conservar referencias; no avanzar a otra fase por haber completado ejecuciones.
