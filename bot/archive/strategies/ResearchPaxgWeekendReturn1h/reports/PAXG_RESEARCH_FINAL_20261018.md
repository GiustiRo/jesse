# PAXG: investigación independiente y sensibilidad

> Cierre posterior de cuenta compartida: leer strategies/ResearchPortfolioPaxgWeekend075/reports/PAXG_SHARED_ACCOUNT_RESULTS_20261018.md. El total vigente es once full de este agente y doce de la línea PAXG contando el estrés de root. T mejora modestamente CAGR/DD frente al control con riesgo PAXG del 1%, pero ambos tienen 35/61 meses activos positivos y 14/21 trimestres: no cumplen la meta. No se acepta reemplazo de referencia ni se abre 2026. Esta etapa queda congelada; los resultados históricos siguientes se conservan.


> Actualización posterior: la continuación de dos controles adicionales está terminada y se documenta en PAXG_EVENT075_FALSIFICATION_RESULTS_20261018.md. El 0,75 conserva expectativa frente a control hábil del mismo umbral y target MARKET. El total vigente es nueve full de este agente y diez de la línea PAXG incluyendo el estrés de 1 ATR de root. La primaria 1 ATR no cambia; no se ejecutó integración ni se abrió 2026. El cuerpo siguiente conserva el cierre histórico de los primeros siete runs.

Fecha local: 18 de octubre de 2026. Este agente completó siete backtests económicos nuevos. Apareció un contraste interesante de fin de semana, pero no hay una nueva estrategia robusta aceptada. La referencia y 2026 permanecen intactos.

## Diseño y trazabilidad

Se aceptó desarrollar reglas de precio sobre el PAXG spot ya disponible para investigar su posible uso posterior en Binance perpetual. Funding quedó fuera de esta etapa. No se crearon scripts de investigación, datasets, instalaciones, cambios del framework ni sesiones live o paper.

Todos los runs usan 2020-10-15 a 2025-12-31 exclusiva, 10.000 USDT, riesgo fijo del 1%, fee de 0,00045 por lado incluso LIMIT, 5x aislado y techo bruto de 4,4x. Los 10 bps de reserva sólo afectan sizing; no son slippage simulado. La muestra 2020–2025 tiene selección acumulada y no es OOS limpio.

Los protocolos se guardaron antes de sus resultados:

- Ronda inicial: ResearchPaxgShockContinue4h/reports/PAXG_INDEPENDENT_PROTOCOL_20261018.md.
- Calendario: PAXG_WEEKEND_PROTOCOL_20261018.md, en esta carpeta.
- Sensibilidad: PAXG_WEEKEND_ROBUSTNESS_PROTOCOL_20261018.md, en esta carpeta.

## Siete resultados completos

| Prueba y dashboard | Trades | Neto USD | Antes de fees USD | PF neto | CAGR motor | DD motor |
|---|---:|---:|---:|---:|---:|---:|
| [Shock: continuación](http://localhost:9200/#/backtest/73464795-1e47-4f0a-9239-fd8901775dc2) | 235 | −2.140,19 | −507,83 | 0,7705 | −4,514% | −30,658% |
| [Shock: reversión](http://localhost:9200/#/backtest/aca7b3b8-3781-4986-8ed6-0ede625ba31c) | 245 | −2.398,95 | −785,75 | 0,7427 | −5,125% | −26,465% |
| [Retest: control aislado](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c) | 35 | 546,11 | 792,72 | 1,3083 | 1,025% | −6,919% |
| [Fin de semana: primaria 1 ATR](http://localhost:9200/#/backtest/2da06c02-d246-43a0-b265-8837aa9c4be5) | 37 | 400,22 | 659,35 | 1,5073 | 0,756% | −2,062% |
| [Control hábil: 1 ATR](http://localhost:9200/#/backtest/3855e023-3d66-4aff-8a13-fbb3110a3255) | 162 | −1.245,28 | −119,12 | 0,7135 | −2,519% | −13,039% |
| [Vecino: 0,75 ATR](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c) | 60 | 764,04 | 1.178,35 | 1,7318 | 1,422% | −2,991% |
| [Vecino: 1,25 ATR](http://localhost:9200/#/backtest/dd08508d-0124-44a7-99e8-4d2806e18790) | 24 | 80,21 | 246,57 | 1,1250 | 0,153% | −1,934% |

El retest es una copia de la referencia con sólo nombre de clase y riesgo del 1% cambiados, ejecutada aislada en PAXG. No replica su contribución original de cartera: tamaños y capital compartido difieren. No se suman curvas.

Los shocks compararon continuar o revertir un desplazamiento 4h de al menos 1,5 ATR previo, con stop fijo de 2 ATR y salida a 48 horas, sin filtros macro, target ni trailing. Ambos pierden antes de fees y en ambos sentidos. Se archivan sin ajustar umbral, horizonte o dirección.

## Qué aporta el calendario y qué todavía falla

El mecanismo distinto se motivó en la política publicada por Paxos: mercado primario abierto de domingo 18:00 a viernes 17:00 de Nueva York, con pausa diaria de 17:00 a 18:00, mientras el secundario continúa. Fuentes revisadas por root: [determinación de precio PAXG](https://support.paxos.com/articles/7818174259-pax-gold-price-determination) y [guía PAXG](https://docs.paxos.com/guides/stablecoin/paxg).

La receta primaria compara el precio propio de PAXG del viernes a las 16:00 con el domingo a las 16:00. Si el cambio alcanza un ATR 4h fijado al ancla, opera en sentido contrario con target en esa ancla, stop a dos ATR y máximo 24 horas. El control hábil compara lunes y miércoles a la misma hora. No se afirma observar valor justo del oro ni operaciones de creación o redención.

La primaria supera los gates iniciales predeclarados y contrasta con un control hábil negativo incluso antes de fees. Su neto por nocional es 13,885 bps frente a −9,952 bps. El contraste favorece investigar el calendario bajo esta receta; días y muestras diferentes impiden llamarlo identificación causal.

La debilidad principal permanece: 337,42 USD, el 84,3% del neto primario, corresponde a trades cerrados en 2022. El agregado de cohortes 2023–2025 es −34,82 USD. Son cohortes de cierre, no retornos anuales MTM.

| EVENT_ATR | Neto con 5 bps extra RT | Neto con 10 bps extra RT | Neto de cohortes 2023–2025 | Neto sin top 3 ganadores |
|---|---:|---:|---:|---:|
| 0,75 | 533,60 | 303,17 | 310,76 | 461,72 |
| 1,00 primaria | 256,10 | 111,97 | −34,82 | 102,92 |
| 1,25 | −12,27 | −104,75 | 45,36 | −212,78 |

Costes extra y eliminación de top 3 son sensibilidades estáticas sobre mismos fills; no simulaciones de una nueva cartera. Los tres umbrales tienen neto agregado positivo, pero el vecino alto falla PF, muestra y el estrés de 5 bps. El vecino bajo es mejor, con cohortes anuales positivas, aunque 2025 aporta sólo 9,89 USD. No se reemplaza la primaria por el mejor vecino después de observar resultados. La rentabilidad temporal de la primaria sigue débil.

Los longs del calendario pierden en los tres umbrales: −57,22 / −87,02 / −29,60 USD. Los shorts aportan +821,26 / +487,25 / +109,80 USD. Se conserva la simetría original; estos resultados no autorizan una selección retrospectiva de shorts.

Exposición temporal: 1,445% / 1,006% / 0,641%. La baja actividad impide asumir que esta señal resolverá la regularidad de cartera. Su función, si se validara, sería un complemento pequeño; todavía no se ejecutó una integración.

## Validación realizada

Los análisis completos terminaron succeeded / exit 0:

- aa21b5ab23ab40449bd367ed22386bfc: shocks y control de retest.
- f6e032d499ae4fa1a354d3f9471d6fb7: calendario y control hábil.
- 1ceab28985404f65ab73a7bb72fd9925: primaria y dos vecinos.

En los siete runs concilian cantidades, fees por todos los fills, PnL y wallet. No hay posiciones superpuestas. Las salidas MARKET por tiempo son exactamente 48 horas en shocks y 24 horas en calendario, salvo cierres sintéticos al final de muestra en los dos shocks, plenamente reconciliados con open_pl. Los siete runs están finished y este agente no deja trabajos propios activos.

Las entradas del calendario y sus vecinos son todas domingo 16:00 de Nueva York, y las del control miércoles 16:00. El código comprueba M1 fresca y paridad con 1h, guarda ATR de 4h completas al ancla y utiliza ZoneInfo para DST. El análisis de resultados no reproduce independientemente todas las oportunidades: los snapshots no incluyen velas ni estado de anclas. No se certifica cobertura de oportunidades, ausencia de rellenos del proveedor ni paridad de ejecución perpetual.

Root ejecutó el auditor MTM V4 para primaria y control: primaria 18/30 meses activos positivos y 18/63 calendario, 12/21 trimestres; completos 18/30 activos, 18/61 calendario y 11/19 trimestres. DD diario −2,102%. Control hábil 26/63 meses activos/calendario y 7/21 trimestres; DD diario −13,039%. Son descripciones de la señal y no criterios individuales de la meta de cartera. Fuente: job c761869862e74de89d19eca1c4114aee, confirmado por root.

Las curvas del motor tienen 1.902 muestras a las 00:01 UTC; no se usan como cierres mensuales. Los reportes numéricos persistentes conservan todos los resultados y nombres de sesiones.

## Estado de la línea

No promover aún. El calendario merece conservarse como hallazgo de desarrollo, con sensibilidad económica desigual y primaria débil en 2023–2025. No abrir 2026, aumentar riesgo, escoger el mejor vecino ni integrar antes de valorar ejecución y transferencia.

Root completó por separado el [estrés de target mediante MARKET al cierre horario posterior al toque](http://localhost:9200/#/backtest/cb5bdb97-ba8a-4997-a009-673d76b4a156), conservando entrada y stop. Root informó 37 trades, neto +321,19 USD, PF 1,409 y DD del motor −2,332%. Ese trabajo es el octavo backtest global de esta línea; no se cuenta entre los siete de este agente. La auditoría final de ejecución, comparación de entradas y MTM corresponde a root. El resultado reduce la preocupación por el target pasivo bajo este estrés concreto, pero no remedia la fragilidad temporal ni acredita fills nativos.

Aunque los gráficos generales de spot y perpetual sean próximos, una ventaja basada precisamente en dislocaciones del token puede desaparecer en el contrato. Si supera los controles, la siguiente validación deberá corroborar ese comportamiento con precio propio del perpetual y verificar la política histórica del mercado primario. Esta observación acota el alcance del hallazgo y no invalida usar el proxy para investigar.

Archivos persistentes de esta carpeta: protocolos, PAXG_WEEKEND_RESULTS_20261018.md, PAXG_WEEKEND_AUDIT_20261018.md y PAXG_WEEKEND_NEIGHBOURS_AUDIT_20261018.md. Los dos shocks descartados y el control inicial se documentan bajo ResearchPaxgShockContinue4h/reports/. No se ocultaron intentos negativos.
