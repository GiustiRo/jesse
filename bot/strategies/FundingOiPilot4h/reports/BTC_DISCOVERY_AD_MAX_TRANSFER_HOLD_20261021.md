# AD — Preferencia por pagos extremos (MAX): HOLD de materialidad

Fecha: 2026-10-21. Investigación documental anterior a cualquier resultado AA.
Decisión: HOLD; no recomendar motores para esta traslación temporal a BTC. El dato es operacionalizable, pero todavía no hay un contraste que represente de forma suficientemente distinta la hipótesis económica. No se implementó ni parametrizó una receta.

## Pregunta económica y viabilidad del dato

La pregunta considerada es si la posibilidad reciente de una ganancia excepcional atrae demanda especulativa y modifica el rendimiento posterior. En la literatura MAX se mide mediante el mayor retorno diario del período pasado. Los cierres BTC existentes permiten calcular esa estadística causalmente, sin nuevas fuentes; no se necesita inferir órdenes, propiedad de monedas o costes mineros.

Una pregunta temporal preliminar sería: dentro de BTC, ¿un máximo positivo pasado aporta información sobre el rendimiento futuro después de distinguirlo del retorno acumulado y la volatilidad del mismo período? Un control conceptual conservaría esas últimas variables y omitiría MAX, con idénticos orígenes, datos, validez y ejecución. Una asociación incremental nula sería una falsación de esa pregunta estadística.

Ese contraste NO identifica demanda de lotería. MAX también resume volatilidad, shocks de información y movimientos de tendencia. Añadirlo a una regresión no demuestra que inversores hayan sobreponderado probabilidades pequeñas. No se propone una nueva OLS sólo porque AA emplee otra interacción.

## Fuentes primarias y límites de transferencia

[Bali, Cakici y Whitelaw (2011), Maxing out: Stocks as lotteries and the cross-section of expected returns](https://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf). Se leyeron resumen, introducción y definición empírica. Su hipótesis vincula preferencias por pagos tipo lotería y extremos positivos pasados con precios relativos. La evidencia principal es transversal entre acciones; no estima una regla temporal BTC.

[Ozdamar, Akdeniz y Sensoy (2021), Lottery-like preferences and the MAX effect in the cryptocurrency market](https://link.springer.com/article/10.1186/s40854-021-00291-9). Se leyeron resumen, motivación y diseño transversal. Reportan una relación positiva entre MAX del mes previo y retornos posteriores entre criptomonedas, distinta de la relación negativa del trabajo bursátil. No es una prueba de continuación temporal en BTC ni de una señal a 24 horas.

[Grobys y Junttila (2021), Speculation and lottery-like demand in cryptocurrency markets](https://doi.org/10.1016/j.intfin.2021.101289), [resumen original de autores en SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551948). El resumen editorial/autor describe ordenación entre criptomonedas por extremos diarios pasados y una diferencia favorable a la cartera de menor MAX respecto a mayor MAX. Sirve como advertencia contra imponer un signo único. No se obtuvo lectura completa del PDF: editor devolvió 403 y repositorios devolvieron restricción/bloqueo. El buscador sí devolvió un extracto primario de la [tabla A7 del PDF depositado en la universidad](https://osuva.uwasa.fi/server/api/core/bitstreams/a78c09ee-7f77-4f1a-bd23-1ec8a7f4dbc4/content): su variante que incluye BTC conserva un diferencial mayor-MAX menos menor-MAX negativo. Esa cartera de veinte monedas tampoco constituye evidencia temporal sobre BTC aislado. No se infiere de ese apéndice la composición completa del diseño principal.

Son fuentes primarias; no se copiaron papers ni citas textuales. La discrepancia entre diseños y signos no autoriza probar ambas direcciones, varios plazos o universos y elegir después.

## Deduplicación antes de cualquier motor

Se leyeron completas por MCP las fuentes:

- `strategies/BtcResearchR12JumpBase1m/__init__.py` — SHA256 `631377b49a213511ca5d08f63e50cf08aa38e18fcec303479b89e3a9fc0b81a6`.
- `strategies/BtcResearchR13Semivariance1m/__init__.py` — SHA256 `0e97f8bf81ace3d8874f4c7740a35deadfcd278874992ce4d1c0fb15506b586a`.
- `strategies/BtcResearchR18AnalogueBase1m/__init__.py` — SHA256 `e8fc9ba9710cef644a41e32608b3132d38d6aca55f5027f259b1c147404e9e2e`.
- `strategies/BtcResearchR13RoundBase1m/__init__.py` — SHA256 `4b6bff9fb5739ddc4aedad4636c1fca1438976f0da0f3d11b0bfcba4b61fbef8`.

También se leyeron completos:
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_F_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_K_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_R_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_L_FINAL_20261021.md`.

F representa desplazamiento de 24 horas concentrado según RV/BV y ya enfrentó seguimiento/reversión del mismo evento. K representa dominancia de semivarianza con desplazamiento neto pequeño. R representa seis retornos ordenados normalizados y similitud coseno frente a media global; su cierre impide rescatar ajustando dimensión, horizonte, lookback o signo.

MAX no es algebraicamente igual a esas tres representaciones. Sin embargo, reemplazar RV/BV por el mayor retorno, ampliar el lookback de R o cambiar una suma cuadrática de K por un máximo no basta para acreditar una pregunta económica nueva. La propuesta temporal considerada perdería el canal transversal de preferencia y selección de activos que sustenta la literatura. Dentro del contrato BTC único, no se identificó aquí una comparación que aislase ese canal; una nueva feature no salva esa ausencia.

Antes de MAX se consideraron niveles nominales redondos y se descartaron por duplicación de L. [Osler, Currency Orders and Exchange-Rate Dynamics](https://www.newyorkfed.org/research/staff_reports/sr125.html) aporta la motivación de órdenes agrupadas alrededor de números redondos en divisas. L ya compara rechazos confirmados en grillas BTC 1000n y 1000n+500, con consumo y rearme. No se propone continuación, otro espaciado, buffer o plazo para reabrirla.

La consulta de inventario nominal y del historial `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md` es acotada: no demuestra ausencia universal. Se revisaron además las familias BTCNovelR901/902/903 y BtcContextR801–805; sus contextos y cambios de ejecución no aportan el mecanismo transversal de MAX. No se consultaron resultados AA ni se ajustó la idea a Y.

## Decisión y límites

AD queda HOLD por materialidad de la adaptación, no por datos faltantes ni por un backtest negativo. La estadística MAX es calculable; falta justificar por qué una versión temporal BTC, con control de tendencia/volatilidad, sería una prueba económica distinta de otra medida de shock. La etiqueta lotería no acredita esa diferencia.

No se congelan ventanas, horizonte, signo, estimador, filtros o umbrales y no se reclama que la literatura cubra los gates r9. No se autoriza probar versiones hasta encontrar una positiva. Una futura revisión tendría que resolver esta objeción conceptual antes de código, sin cambiar riesgo, gestión o datos para producir artificialmente una pregunta nueva.

Cero clases, jobs, drafts, análisis, velas observadas, importaciones y datasets nuevos. No se ocuparon slots ni presupuesto. Contrato 2%/6%/3x y costes vigentes intactos. No se modificaron padres, framework, configuración global ni Hub.
