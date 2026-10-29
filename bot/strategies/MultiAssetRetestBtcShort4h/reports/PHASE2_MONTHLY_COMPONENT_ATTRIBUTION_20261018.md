# Qué meses mejora y empeora añadir PAXG y SPY

Comparación entre [BTC long + short con contexto fijo](http://localhost:9200/#/backtest/4623d369-05e7-4714-8f3b-5c10b1726663) y la [referencia de tres activos](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Misma lógica, costes, período y techos individuales de exposición; capital compartido y tamaños recalculados en cada simulación. Son datos de desarrollo, sin evaluar 2026.

Al incorporar las entradas long de PAXG y SPY:
- Siete meses negativos de BTC pasan a positivos.
- Nueve meses positivos de BTC pasan a negativos.
- También cambia la actividad de meses antes planos. El total de meses positivos pasa de 34 a 33 sobre los mismos 63 meses; no se obtiene ese cambio únicamente restando las dos categorías anteriores.
- En los nueve meses que pasan a negativos, la contribución conjunta MTM de PAXG/SPY es negativa, mientras BTC sigue contribuyendo positivamente en la referencia.
- En los siete meses rescatados, PAXG/SPY contribuyen positivamente y BTC negativamente en la referencia.

Esto confirma una aportación bidireccional: los activos adicionales compensan algunas pérdidas de BTC, pero también generan pérdidas en otros meses que BTC habría cerrado en positivo. Tener correlación baja y beneficio neto positivo no garantiza aumentar la proporción de meses positivos.

Ejemplos de contribuciones dentro de la cuenta de referencia:
| Mes | BTC | PAXG | SPY | Portafolio |
|---|---:|---:|---:|---:|
| Mayo 2021 | +1,930% | −2,576% | 0% | −0,646% |
| Noviembre 2021 | −2,102% | +1,753% | +1,552% | +1,204% |
| Enero 2025 | −2,399% | +12,012% | +0,157% | +9,770% |

Las contribuciones se dividen por la equity global al comienzo del mes. No son retornos de cuentas individuales ni un modelo que mantenga cantidades fijas. Las fechas se incluyen para auditar, no para construir filtros estacionales retrospectivos.

Análisis MCP: 434a696e8f7b4f289c6b0d4e1170641e, terminado correctamente. Auditor MTM v3, reconciliación de saldos, precios diarios anclados a ejecuciones; sin velas negociables inventadas. El artefacto temporal changed_months.json contiene las 16 transiciones y contribuciones completas.
Decisión: investigar la combinación y utilización del capital además de la lógica short. No excluir activos por quitar retrospectivamente sus mejores o peores trades ni escoger meses conocidos.
