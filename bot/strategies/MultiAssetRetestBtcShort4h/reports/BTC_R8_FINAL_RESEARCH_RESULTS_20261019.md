# BTC R8 — resultado final y candidata Y902 retenida

## Decisión y alcance

Se completaron13recetas en26backtests nominales:5contextuales,5experimentales y3del agente creativo adicional solicitado. Se conserva N204 como referencia operativa y Y902 como candidata de investigación prometedora. Ninguna receta cumple simultáneamente todas las puertas congeladas en B y C; por eso no se activan las6verificaciones condicionales ni se elige un ganador alternativo. Esto no equivale a descartar Y902 ni demuestra sobreajuste.

2026 permaneció cerrado incluso a inspección. Misma muestra de desarrollo2020-10-15 inclusiva→2025-12-31 exclusiva, cuatro años calendario completos2021–24 y2025parcial; no validación fuera de muestra. B/C son configuraciones relacionadas de SPY, no dos muestras independientes. Neto de cartera BTC/PAXG/SPY con capital compartido10000USDT y riesgo1% por operación/8% agregado; aislado5x, capnocional4.4 yfee.00045porlado. Reserva.001es dimensionamiento, no slippage ejecutado. No se añadió funding. Se mantuvieron PAXG original y las variantes SPY BSecond/CMarket.

## Resultados nominales

N204 referencia: B13056.614915 y C13239.442380USDT. N503 semilla de la familia creativa: B13328.711713 y C13536.902513USDT. Cada enlace lleva al registro de backtest devuelto por Jesse.

|Receta|Neto B USDT|Neto C USDT|Δ N204 B/C|Conclusión|
|---|---:|---:|---|---|
|V801|[13328.71](http://localhost:9200/#/backtest/b0c5ce4f-ed64-4b07-bdca-f708aae2d445)|[13536.90](http://localhost:9200/#/backtest/5de86562-4ba7-4f2f-b9fb-f647ed2a8b70)|272.10 / 297.46|Identidad económica con N503; no nueva observación independiente. C falla calendario bajo +5.|
|V802|[12838.90](http://localhost:9200/#/backtest/876feccb-b93c-4fb0-a6ea-3a4b58c642c7)|[13013.55](http://localhost:9200/#/backtest/8e889155-eabc-4187-acc5-748f98dc5378)|-217.71 / -225.89|Menor neto; cambios demasiado escasos.|
|V803|[13056.61](http://localhost:9200/#/backtest/e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531)|[13239.44](http://localhost:9200/#/backtest/1d818489-9707-43ab-8106-98cacdbf0a56)|0.00 / 0.00|Identidad económica con N204.|
|V804|[13123.60](http://localhost:9200/#/backtest/b481d1da-f0b2-4c9c-b663-b4a4a8c44896)|[13307.81](http://localhost:9200/#/backtest/b042558a-4ea4-41f1-a2de-7d51d8d53b56)|66.99 / 68.37|Pequeña mejora nominal; falla calendario, distribución y omisión del mejor mes.|
|V805|[13056.61](http://localhost:9200/#/backtest/0af9be29-c28a-490b-a7d7-6a481660a950)|[13239.44](http://localhost:9200/#/backtest/ec8d524e-d8c0-4b55-8dbe-da6ae8051918)|0.00 / 0.00|Identidad económica con N204.|
|X801|[4947.13](http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f)|[5129.70](http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660)|-8109.48 / -8109.74|Ancla en vela de máximo volumen; menor neto.|
|X802|[7971.10](http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3)|[8181.46](http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e)|-5085.51 / -5057.98|Ruptura de compresión común de seis velas; menor neto.|
|X803|[8013.23](http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf)|[8180.37](http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757)|-5043.39 / -5059.08|Readmisión y pérdida del punto medio de vela bajista; menor neto.|
|X804|[5040.50](http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9)|[5213.66](http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d)|-8016.11 / -8025.78|Cambio de presión de volumen/retornos; menor neto.|
|X805|[3846.19](http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8)|[3967.02](http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41)|-9210.43 / -9272.42|Reloj de volumen M1; sobreoperación y menor neto.|
|Y901|[11046.64](http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2)|[11228.81](http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c)|-2009.97 / -2010.63|Retesteo LIMIT; menor neto.|
|Y902|[13446.23](http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c)|[13680.35](http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff)|389.62 / 440.91|Candidata prometedora retenida; B falla únicamente concentración nominal del mejor mes.|
|Y903|[10679.17](http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33)|[10898.84](http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff)|-2377.44 / -2340.60|Invalidación adversa; menor neto pese a recortar algunas salidas.|

V801 reproduce económicamente N503; V803 y V805 reproducen N204 (tolerancia1e-7, tiempos/tipos exactos). Son comprobaciones de equivalencia en esta muestra, no tres mejoras independientes. Las fuentes originales no cambian; la ocupación sí puede cambiar ejecuciones: X805 retiene30de31largos originales, no31. Todos los experimentos deben evaluarse por cartera y coste de oportunidad, no sólo por rendimiento aislado de su suplemento.

## Y902: qué aporta y qué queda incierto

Usa el mismo evento N503 pero solicita un SELL STOP en el mínimo de la vela de señal, válido sólo durante la siguiente4h. Distancia técnica congelada desde la señal, SL1R/TP2R desde fill y48h desde fill real; misma fórmula de sizing evaluada en el precio candidato, prioridad original y cancelación existentes. No hay reintentos de la misma señal. Se ejecutaron46suplementos frente a67N503. Los logs completos identifican45STOP y1MARKET por cartera; tipo STOP no significa corto original. El motor puede seleccionar MARKET cuando su regla de proximidad lo determina.

Mejora frente a N204: +389.619610/+440.906791USDT; frente a N503: +117.522813/+143.446658. Bajo overlay de10bps adicionales por round trip, mejora frente a N204 +546.100683/+591.583164. Son costes estáticos sobre fills/cantidades fijados, no un backtest con comisión elevada ni una prueba de liquidez real.

Bajo +5bpsRT:
- B:41de63meses calendario positivos (41/62activos), igual número calendario que N204.
- C:42de63positivos (42/62activos), un mes más que N204.
- Trimestres17/21en ambas, igual a N204B y uno menos que N204C.
- Sólo meses completos: B41/61calendario y C42/61, sobre60activos en Y902.
- Mejora MTM en4de5bloques2021–25 frente a N204;2025no es año completo.

Hay un coste: DDmotor−9.6941%/−9.6301%, frente a−8.7768%/−9.0579%N204. No mejora todas las dimensiones.

Enero2022 aporta +409.380189/+400.581645USDT de ventaja incremental. Al descontarlo aritméticamente, el resto suma−19.760578/+40.325146 frente a N204. Es el único fallo de B bajo el contrato de selección; C cumple todas las condiciones. Los−19.76no son una pérdida de un escenario de2022. La cercanía al cero, el mejor neto bajo costes y4/5bloques favorables justifican retener la candidata. La concentración justifica prudencia antes de sustituir la referencia; no diagnostica por sí sola sobreajuste.

## Consulta posterior: regularidad quitando enero2022 de ambas

Se realizó un análisis descriptivo adicional a petición del usuario, sin nuevos backtests, sin ajustar fuentes ni puertas y sin abrir2026. Entre los62meses calendario restantes:
- Nominal: B41/62positivos en ambas; C42/62en ambas.
- +5bpsRT: B N20441/62 frente aY90240/62; C41/62en ambas.
- +10bpsRT: B38/62en ambas; C39/62en ambas.

Y902 tiene un mes plano/inactivo; sus porcentajes sobre meses activos usan61, frente a62N204. El denominador activo puede elevar su porcentaje sin agregar un mes ganador. Sólo meses completos (60calendario tras retirar enero) da la misma conclusión relativa. No es un replay de capital sin enero ni una validación fuera de muestra.

Bajo +5 estático, la ventaja monetaria restante es +54.33/+111.64USDT; bajo+10,+128.43/+182.95. La casi igualdad nominal restante no agota la comparación, pero tampoco prueba mejora uniforme de regularidad. Detalle y código: BTC_R8_Y902_WITHOUT_JAN2022_MONTHLY_REGULARITY_20261019.md, job3025c86117854b62ac3e9b8f5581e7d6.

## Validación y trazabilidad

26formularios y78snapshots finales coherentes;37fuentes exactas (bases y rondas preservadas);13auditorías financieras de pares con4anclas inmutables, conciliando fills/qty/fees/PNL/wallet/terminal/MTM. Todos los targets pasan. Metadatos de Y901/Y902/Y903 conciliados contra logs MCP paginados completos:33/46/70suplementos por cartera. Y903modifica29salidas del suplemento emparejadas contra N503; se conservó el diagnóstico de toda la cartera separado para evitar atribuir cambios ajenos al mecanismo.

QA:102contextual,184experimental,201creativa final; hay200checks creativos previos a añadir telemetría. Estas comprobaciones se solapan y no son observaciones estadísticas independientes. Revisión independiente final310comprobacionesPASS, incluyendo puertas de26filas y trazabilidad Y903. Fuentes económicas congeladas; cambios de fixtures QA anteriores a las corridas no se presentan como backtests. La telemetría creativa se refrescó en los mismos6drafts antes de sus corridas mediante snapshots nuevos.

Hubo una respuesta MCP noJSON en el tramo previo y se suspendieron herramientas; al recuperar, se comprobaron estados existentes y se continuó el draft sin duplicar corridas. Límites lógicos de capacidad de análisis se gestionaron esperando trabajos existentes. No hubo purgas, borrados, reinicios ni cambios en framework o live/paper. Figuras PNG no se descargaron por el fallo de integridad conocido; artefactos textuales y cálculos sí se verificaron.

## Continuidad propuesta

Retener N204 y Y902 con sus fuentes actuales. La próxima fase útil es validar causalmente el cambio de ejecución Y902: qué entradas pierde/gana, cuánto depende la mejora de selección frente a precio y cuánto cambia la disponibilidad del corto original y el capital compartido. Diseñar cualquier validación de fee endógeno/bloques antes de correrla, sin afinar la receta para rescatar el margen de−19.76 ni abrir2026. No se ejecutó esa fase en esta ronda.

## Índice de evidencia

- BTC_R8_FROZEN_PROTOCOL_20261019.md y BTC_R8_CREATIVE_Y_FROZEN_ADDENDUM_20261019.md: hipótesis/gates/budget previos.
- BTC_R8_RESULTS_MATRIX_20261019.md: matriz26filas completa, elegibilidad y URLs.
- BTC_R8_FINAL_MANIFEST_20261019.md:26sesiones/78snapshots/37fuentes/13jobs y conciliaciones.
- BTC_R8_AUDIT_<receta>_20261019.md:13auditorías financieras.
- BTC_R8_Y901/902/903_SLEEVE_IDENTIFICATION_20261019.md: conciliación completa.
- BTC_R8_Y903_EXIT_ATTRIBUTION_CLARIFICATION_20261019.md y BTC_R8_Y903_SUPPLEMENT_EXIT_TRACE_20261019.md: atribución conservadora antes de resultados y29pares después.
- BTC_R8_FINAL_SELECTION_AND_METADATA_SOURCE_20261019.md: helpers finales.
- ../BTCExploreR801/reports/BTC_R8_INDEPENDENT_FINAL_GATE_REVIEW_20261019.md: dictamen independiente.
- ../BTCNovelR901/reports/BTC_R8_Y_FAMILY_RESULTS_20261019.md: informe del agente creativo.
