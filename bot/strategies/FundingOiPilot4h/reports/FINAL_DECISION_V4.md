# Decisión final V4 — SIN_CANDIDATA

Fecha local: 20 de octubre de 2026. Cierre económico de las seis configuraciones. No se promueve ninguna estrategia.

## Resultado

Se investigaron tres mecanismos nuevos en BTC-USDT de una hora: RSI2 extremo dentro de una tendencia, reversión de shocks de precio y volumen, y normalización de funding con confirmación de precio. Cada uno tuvo una variante con filtro OI y otra sin él. Un subagente se dedicó a cada sector; trabajaron con hasta dos backtests propios y un límite global de dos motores.

El período continuo de screening fue del 1 de septiembre de 2020 al 1 de enero de 2024. Cada sesión comenzó con 10.000 USDT y registró 29.208 decisiones. Estos retornos corresponden al período completo de 40 meses, no a un año.

| Variante | Operaciones | Neto del período | PF | Drawdown | Años positivos 2021–2023 |
|---|---:|---:|---:|---:|---:|
| [ResearchV4OscillatorP1h](http://localhost:9200/#/backtest/29dd9e7e-c785-4763-abd3-2aff1e649661) | 774 | -8.61% | 0.960 | -26.86% | 1/3 |
| [ResearchV4OscillatorOi1h](http://localhost:9200/#/backtest/a1070e6a-ef44-4f9e-8c9f-34be95ca8f11) | 464 | -27.29% | 0.796 | -33.67% | 0/3 |
| [ResearchV4ShockPV1h](http://localhost:9200/#/backtest/02499a0c-1bc8-45ad-8f3a-bf4df11c404b) | 461 | -65.90% | 0.528 | -68.23% | 0/3 |
| [ResearchV4ShockPVOi1h](http://localhost:9200/#/backtest/2980adc0-9379-4f04-bb2a-0a6b931c1af0) | 279 | -51.81% | 0.475 | -53.09% | 0/3 |
| [ResearchV4FundingFP1h](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068) | 26 | -6.93% | 0.590 | -12.71% | 0/3 |
| [ResearchV4FundingFPOi1h](http://localhost:9200/#/backtest/786b270b-f497-4f48-b254-648ab7ea63af) | 12 | -7.66% | 0.268 | -8.55% | 0/3 |

Todas fallan neto positivo y PF ≥ 1,2. Oscilador y shocks también superan el máximo de drawdown del 25%. Las variantes funding tienen 26 y 12 operaciones, por debajo de las 30 mínimas. Ninguna alcanza dos años positivos de los tres años completos 2021–2023; 2020 parcial queda excluido. Los criterios se mantuvieron sin cambios.

La shortlist vacía está fijada en FROZEN_SHORTLIST_V4.md. Se consumieron seis de los 40 slots económicos y tres de los seis técnicos. Los 34 slots de confirmación, replay, costes, vecinos y retraso OI se omiten conforme al protocolo. No se reasignan a ajustes para rescatar resultados.

No hubo confirmación económica V4 de 2024–2025. No existe una curva de selector V4 para esos años y no se fabrica una rentabilidad de 0% por no haber ejecutado esa fase. 2026 continúa cerrado.

## Qué aprendimos

El oscilador sin OI obtuvo 5.567,52 USDT brutos por movimientos de precio, pero pagó 6.274,27 en comisiones y 153,99 en funding. Su resultado neto fue −860,73 USDT. La actividad no aportó una ventaja suficiente para cubrir el coste nominal. Con OI quedaron menos operaciones y peor rentabilidad.

Las dos variantes de shocks tuvieron pérdidas incluso antes de comisiones y funding. El problema observado incluye la dirección y evolución posterior de la señal; no se explica sólo por fricción.

Funding produjo 27 setups después de la confirmación de precio. Sin OI se ejecutaron 26 y uno quedó bloqueado por posición abierta. Con OI se ejecutaron 12 y se rechazaron 15 por OI no creciente. El filtro redujo exposición y drawdown, pero no creó rentabilidad ni una muestra suficiente. Un drawdown menor por operar poco no permite promoción.

Estas conclusiones rechazan las reglas nominales estudiadas. No demuestran que todos los osciladores, shocks, funding u OI carezcan de utilidad.

## Validación y trazabilidad

Las 14 fuentes compilaron y pasaron 248 comprobaciones deterministas: 61 comunes, 87 de oscilador, 48 de shocks y 52 de funding. Las revisiones cruzadas se realizaron antes de los screenings. La única corrección productiva previa fue rechazar medias no finitas por desborde numérico en funding; no cambió parámetros económicos.

Se completaron tres smokes de siete días, con 168 decisiones cada uno. El smoke funding no operó; no se le atribuye cobertura de fills o cierres. Los otros dos ejercieron callbacks reales de cierre, incluido el cierre final forzado.

Las seis sesiones económicas concilian precio bruto − comisiones + funding = PNL y saldo final. El error máximo es 1.000444171950221e-11 USDT, inferior a la tolerancia de 0,000001. Las curvas tienen cobertura diaria completa y 40 meses; el drawdown del motor gobierna los filtros.

Los subagentes recorrieron los logs completos. Se verificaron 2.016 planes de entrada y sus cierres, contando por configuración. Esta suma no representa operaciones independientes de una cartera combinada. Las seis sesiones económicas no necesitaron cierre forzado final. Oscilador ejerció salidas RSI y stops; shocks ejerció stops, objetivos y máximo de seis horas; funding ejerció salidas SMA24 y stops. Las ramas de calendario y máximo de 72 horas de funding quedaron cubiertas por comprobaciones deterministas, sin fills reales que acrediten esas ramas.

En cada variante funding se verificaron los 3.651 eventos y sus 7.302 bloques canónicos, con 3.651 hashes correctos, sin discrepancias del timestamp público. El recálculo independiente de pares normalizables, sigma cero y confirmación de precio coincidió. Las auditorías persistidas guardan todos los contadores, planes y cierres, más ventanas seleccionadas de inicio, medio, final y entradas. Las ventanas restantes permanecen en los logs originales de cada sesión.

Al cierre, las 14 fuentes coinciden exactamente con el snapshot congelado. La dependencia ResearchV2Core4h conserva su fuente. El listado devuelve nueve sesiones V4 únicas y terminadas: seis económicas y tres técnicas. No quedan motores V4 activos. Los timeouts se resolvieron leyendo el mismo ID, sin duplicar arranques.

## Límites y cierre

El nominal usa fee 0,00045, slippage cero, funding histórico y riesgo previsto del 2% incluyendo ambos fees, con tope nocional de una vez el capital. Stops, gaps y costes reales pueden exceder ese riesgo previsto. No se acredita robustez económica a slippage o fees duplicadas porque ninguna variante pasó el screening.

OI procede de un archivo retrospectivo, con disponibilidad asumida de etiqueta + seis minutos y freshness de diez minutos; no está certificado point-in-time. Funding de este período incluye marcas proxy. Los datos ya observados en ciclos anteriores no constituyen una prueba independiente. Las sensibilidades de funding con cantidades fijas son descriptivas y no sustituyen un replay.

V4 no modificó el framework ni las reglas V1–V3. No hubo instalaciones, reinicios, ML, live/paper, órdenes reales, Pi, cambios de cuentas, commits o push. La validación técnica demuestra consistencia de implementación; no rentabilidad futura.

Con este resultado se agotan las tres líneas nuevas previstas para el ciclo final V4. Se cierra este conjunto de hipótesis y se conserva la evidencia parcial de V3 por separado. No se alcanzó una candidata aprobada para la meta orientativa de 20–30% anual.

## Evidencia principal

- RESEARCH_PROTOCOL_V4_20261020.md y las tres propuestas sectoriales.
- REGISTRY_V4.json y V4_FINAL_METRICS.json: configuración, datasets, fuentes, sesiones, métricas y estado.
- V4_IMPLEMENTATION_SOURCE_FINAL_20261020.md y V4_STATIC_VERIFICATION_FINAL.json.
- V4_FINAL_SOURCE_AND_SESSION_VERIFICATION.json.
- V4_TECHNICAL_GATE.md y auditorías de los tres smokes.
- WALK_FORWARD_EXPLORATION_V4.md y las cinco auditorías centrales de las seis sesiones económicas.
- V4_OSCILLATOR_SCREEN_REPORT.md, V4_SHOCK_SCREEN_RESULT_20261020.md y V4_FUNDING_SCREEN_FINAL_REPORT.md.
- V4_FUNDING_FINAL_COUNTERS.json y las auditorías de logs por sesión.
- FROZEN_SHORTLIST_V4.md y WALK_FORWARD_CONFIRMATION_AND_STRESS_V4.md.
