# Investigación independiente SPY / PAXG — protocolo de etapa

## Mandato humano actualizado
18 octubre 2026 America/Montevideo. Prioridad invertida: investigar SPY y PAXG con operativas independientes antes de volver a BTC. Dos agentes, uno por activo. El usuario acepta los históricos actuales (SPX CFD BID /10 para SPY; spot PAXG) como proxies de acción de precio para desarrollar estrategias destinadas a Binance perpetual. Correspondencia proxy/contrato es hipótesis de trabajo, no paridad de fills demostrada. Funding fuera de esta etapa, motor sin implementar esa contabilidad. No nuevas fuentes necesarias, ni compras, instalaciones, framework, reinicios, live/paper o Pi.

## Diseño y límites
Referencia MultiAssetRetestBtcShort4h y sus resultados intactos. BTC congelado. Desarrollo 2020-10-15 a 2025-12-31 exclusivo. 2026 cerrado. Todo 2020–25 es investigación adaptativa; nuevos bloques temporales no recuperan independencia estadística. Precio únicamente donde volumen no es genuino; sin footprint/GEX sintéticos.

Cada línea revisará historia y predeclarará hasta dos hipótesis con mecanismo propio, distinguiéndolas de MR/calendario/participación/divergencia/rotación/turtle ya probados. Máximo cuatro full económicos por activo en ronda inicial, incluidos controles; una candidata prometedora puede justificar ampliación de robustez documentada antes de nuevos resultados. No barridos ni cambios ad hoc para rescatar fallos. Dos slots backtest por agente, hasta cuatro globales por nueva autorización humana; respetar límites reales del servicio. Un analysis por agente, dos globales. No scripts nuevos: usar estrategias/MCP y run_analysis de snapshots completos.

Comparación aislada: capital10000USDT, riesgo nominal1% por operación, comisión0.00045 por lado incl LIMIT, 5x isolated, nocional bruto máximo4.4x, sin piramidado. Riesgo1% sirve para comparar señales sin rescatar con exposición. Integración posterior conserva límites humanos3%trade/8%agregado y usa cuenta compartida real, no suma de curvas. Protocolo de integración se fija después de evidencia aislada y antes de su resultado.

## Criterios de avance
Regularidad es objetivo de CARTERA, no requisito de cada señal. Prioridad: expectativa neta y mecanismo defendible, muestra y concentración visibles, estabilidad por tramos y resistencia a fricción. Baseline aislado o control equivalente a mismo riesgo, para distinguir alpha de exposición. Una mejor cifra total sola no basta. Net<=0 o dependencia de un umbral/días excepcionales implica descarte o evidencia insuficiente; no selección retrospectiva de años/estados.

Si hay promesa: controles de implementación/causalidad/horarios/quotes frescas, costes incrementales sobre fills identificados claramente como estáticos, vecinos limitados predeclarados y backtest dinámico si el motor permite sin alterar config guardada. MTM mensual, períodos completos/todos/activos y DD con frecuencia explícita; años, direcciones, turnover, exposición, ganadores concentrados, pérdida mensual y recuperación. No asignar PnL mensual por fecha de cierre. Sin afirmar que bootstrap certifica ausencia de sobreajuste.

Metas de cartera conservadas como evaluación:65%mesesactivospositivos aspiración70%,80%trimestres,DD no peor−25%,rentabilidad útil resistente a costes (meta20–30%anual negociable). PF>=1.2/DD>=−25% y aproximadamente20trades son criterios reservados históricos mínimos, no certificación estadística. No abrir2026 durante esta etapa; antes habrá que congelar selección/reglas/protocolo final.

## Entregables
Protocolos previos por activo; estrategias nuevas ResearchSpy*/ResearchPaxg*; sesiones con dashboard_url; resultados completos positivos y negativos, artefactos análisis y reportes persistentes; recomendación fundada continuar/descartar/inconcluso. Root revisa código y evidencia y coordina integración/robustez. No promesa de cumplir las metas.