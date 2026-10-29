# Exploración BTC sobre la combinada — 18/10/2026

Estado: ninguna candidata aceptada. La referencia y los objetivos permanecen intactos. Recuperación del retest y reloj por eventos terminaron y se descartaron. La prueba de gestión long BTC por falta de progreso también terminó y fue auditada sin inconsistencias: no mejora la regularidad y reduce mucho la rentabilidad.

## Alcance vigente

El usuario descartó funding, VIX y COT y sus descargadores. No quedan solicitudes de autorización pendientes para esas líneas. Autorizó seguir con BTC, velas, volumen y estructura, conservando PAXG/SPY, y dedicar una línea a investigación experimental.

Desarrollo: 2020-10-15 a 2025-12-31 exclusivo. El histórico 2020–2025 ya se ha usado ampliamente; no es OOS limpio. 2026 permanece reservado. Cuenta compartida de 10.000 USDT, 5x aislado, fee 0,00045 por lado en TODAS las órdenes. Riesgo máximo planificado 3% por trade / 8% agregado y techo bruto 4,4x. Funding y slippage efectivo siguen fuera; la reserva de sizing no los simula.

Objetivos: 65–70% de meses activos positivos, 80% de trimestres positivos, drawdown no peor que −25% y rentabilidad útil resistente a costes. También se muestran todos los meses y períodos completos.

## Resultados de la primera tanda

| Variante | CAGR | DD motor | Meses activos positivos | Todos los meses positivos | Trimestres positivos | Decisión |
|---|---:|---:|---:|---:|---:|---|
| [Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) | 28,83% | −14,89% | 33/61 (54,10%) | 33/63 (52,38%) | 15/21 (71,43%) | Referencia intacta |
| [Volumen BTC](http://localhost:9200/#/backtest/fabf8e7d-438b-4690-a7af-92544858b435) | 25,91% | −14,49% | 32/61 (52,46%) | 32/63 (50,79%) | 14/21 (66,67%) | Descartada |
| [Estructura short BTC](http://localhost:9200/#/backtest/e632b3d1-9998-4c25-85c9-0b96bc1c4792) | 22,07% | −14,95% | 30/57 (52,63%) | 30/63 (47,62%) | 14/21 (66,67%) | Descartada |
| [Permanencia intrabar](http://localhost:9200/#/backtest/b1c63c4c-ddc9-40d9-b289-d01915073041) | 25,97% | −13,72% | 34/60 (56,67%) | 34/63 (53,97%) | 15/21 (71,43%) | Comparación útil; no aceptada |
| [Recuperación del retest](http://localhost:9200/#/backtest/7068c1f7-f9d2-4d10-a8df-95e760a19c8b) | 26,91% | −15,01% | 32/61 (52,46%) | 32/63 (50,79%) | 15/21 (71,43%) | Descartada |
| [Reloj por eventos](http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967) | 17,60% | −15,67% | 28/58 (48,28%) | 28/63 (44,44%) | 11/21 (52,38%) | Descartada |
| [Falta de progreso long](http://localhost:9200/#/backtest/c6e326d6-5e63-4489-be8d-741d0f83f43a) | 11,86% | −18,27% | 33/61 (54,10%) | 33/63 (52,38%) | 14/21 (66,67%) | Descartada |

En períodos completos: referencia 33/59 meses activos y 14/19 trimestres; volumen 32/59 y 13/19; estructura 30/55 y 13/19; permanencia 34/58 y 14/19. Los 61 meses completos se conservan como denominador calendario, además del denominador activo.

El auditor V4 reconcilió órdenes ejecutadas, fees, wallet y MTM UTC. Sus self-tests pasaron; escalas de las fuentes verificadas con múltiples fills MARKET independientes a medianoche. Jobs b3de8216d2f64b1ea409501db66a1ac5 y 46be126036194c67857c0f30fdce3982 finalizaron succeeded. Los controles antiguos se usan sólo como anclas de precio de la misma serie, no para reciclar rendimiento de un motor anterior.

## Qué cambió y qué aprendimos

- Volumen: requiere volumen BTC 4h >= mediana de las 28 fechas anteriores del mismo bloque UTC. No modifica PAXG/SPY ni posiciones abiertas. Shorts: 107, neto 3.572,18, PF 1,29 frente a 123 / 5.287,02 / 1,36 de referencia. Rescata cuatro meses y estropea cinco. No se abre una rejilla de volumen.
- Estructura: reemplaza sólo RSI3<=20 del short por H1–L1–H2 confirmado, máximo menor y primera pérdida del soporte; dos barras a cada lado y memoria 60. Shorts: 17, neto −904,96, fees 160,90, PF 0,60; pierde también antes de fees sobre esos fills. Rescata cuatro meses y estropea siete. No se cambia pivots/memoria tras el fallo.
- Permanencia: conserva el short original, pero exige 120/240 cierres M1 en el tercio inferior de la vela señal. Logs: 327 candidatos, 327 ventanas M1 completas y con paridad 4h, 300 rechazados, 27 admitidos, 21 shorts ejecutados. Shorts: neto 2.138,67, fees 258,96, PF 2,28 y WR 66,67%; muestra pequeña. Mejora un mes positivo neto (rescata cinco y estropea cuatro) y el DD, pero no los trimestres; 2022 pasa de +2,67% a −5,06% y el peor trimestre empeora de −4,24% a −6,02%. No sustituye la referencia ni se ajusta el umbral.

Las reglas long y de otros activos permanecen iguales; sus cantidades y PnL pueden cambiar por el capital y la ocupación compartidos. No se suman curvas independientes.

## Laboratorio probabilístico cerrado

[Primera corrida](http://localhost:9200/#/backtest/8fb36f9a-ead7-41cd-9341-bc95de116f5a): cuatro estados por signos de dos retornos 4h, aprendizaje causal de etiquetas M1 de una política de una barra, shrinkage y gate heurístico de expectativa neta. No añade información externa ni demuestra una teoría nueva. Usa 1% de riesgo.

[Repetición técnica con debug](http://localhost:9200/#/backtest/ab8e72a8-f81f-41d8-8d95-8681d27e1b9c), sin cambiar política: 11.297 etiquetas válidas, cero ausencias, ventana 1.080 y conteos [264,272,273,271]. Las 10.218 decisiones evaluables no superaron el gate. Cero señales long/short y cero trades. El saldo de diagnóstico termina en 10.000; el motor no guardó métricas ni curva: no fabricar CAGR/Sharpe/DD. El guard de stop descartó 120 contextos; no sumar ese contador a skip_window como poblaciones independientes.

La abstención no fue un fallo total de datos ni entrenamiento incompleto. No se relajan umbrales ni se ejecuta un control incondicional para rescatar el resultado. El margen de una SE es una heurística, no significancia ni garantía bajo dependencia.

## Nueva ejecución: control técnico verificado

[Control BTC 1m](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1) conserva decisiones, trailing y gestión 4h, órdenes originales y los otros activos. El auxiliar BTC 4h excluye velas en formación y la cancelación conserva cuatro horas de vigencia.

Comparación del job 3e58c073425c45a5ba8ef163147f54d7, succeeded: 220 trades, 440 órdenes registradas asociadas a esos trades y 1.904 puntos Portfolio equivalentes. Campos económicos, cantidades, precios, tiempos, fees y wallet coinciden; 45 métricas coinciden con tolerancia numérica. Diferencia máxima de curva 3,64e−12. Se excluyen sólo IDs aleatorios y nombre de estrategia. No prueba identidad de cada orden sin fill que no está en el snapshot.

Sólo después de esta equivalencia se autorizó preparar una variante de ejecución: armar el setup long BTC original, observar toque real en M1 y recuperar el nivel en una M1 estrictamente posterior, antes de cuatro horas. Entrada MARKET al precio real de confirmación, más cara explícitamente. Reservas y techos originales congelados; revalidación de riesgo/notional/margen al ejecutar. Shorts, PAXG/SPY y gestión 4h se conservan. Fuente revisada por dos agentes, contrato de tamaño cero corregido antes de ejecutar, sin cambios de alpha. La corrida terminó: 219 trades, 96 longs y 123 shorts, neto 24.643,53 y fees 4.213,33. Calendario: 32/61 meses activos y 15/21 trimestres; completos 32/59 activos y 14/19 trimestres. Rescata cero meses y estropea uno frente a referencia. Los 30 longs BTC fueron MARKET; 29 comparten setup con fills de referencia y uno corresponde a un setup sin fill de referencia. En los comunes, mediana +4,79 bps de precio, un minuto de demora y ratio de cantidad 0,9165; selección y capital posterior también cambian. Auditoría 8ea448f4be70443cb2614e988c970bf9 succeeded. Receta descartada sin cambiar la latencia.

La reserva interna no reserva margen real del broker mientras no existe orden; el tope de cartera y revalidación se comprobaron sobre la simulación conjunta. Corrección de explicación: exigir una M1 posterior es una confirmación adicional de persistencia predeclarada, no una necesidad matemática para ordenar mínimo y cierre. El cierre es el último precio de la vela; esta aclaración no cambia la regla ejecutada ni autoriza probar otra latencia tras ver el resultado.

## Conteo y continuidad

A las 18 pruebas económicas anteriores se añaden seis variantes combinadas y una receta probabilística sin operaciones. El repeat debug y el control de reloj son verificaciones técnicas, no dos hipótesis de alpha adicionales. La búsqueda global previa es mucho mayor y no se reinicia la selección. No hubo scripts nuevos, descargas, cambios de framework, instalaciones, fondos, live/paper o Pi.


## Reloj de eventos BTC — receta descartada

[Combinada por eventos](http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967): terminada, 266,17 s, 185 trades (96 longs y 89 shorts). CAGR 17,5996%, DD −15,6699%, Sharpe 0,9103, neto 13.284,891739 USDT, fees 3.097,647678. Sustituye RSI short por fases alternantes de una ATR4h congelada desde extremos de cierres M1; cambia cadencia y adapta STOP al low de M1. Es una política conjunta; no aísla el aporte del reloj. Longs y PAXG/SPY conservan reglas, no necesariamente tamaños/fills.

Auditor V4 cabb99082ffd47ec99028fcd2d1c8d6d succeeded, self-tests y reconciliación de fills/fees/wallet aprobados. Meses activos 28/58 =48,28%; todos 28/63 =44,44%; trimestres 11/21 =52,38%. Periodos completos:28/56 activos,28/61 todos,10/19 trimestres. Rescata2 meses y estropea7 frente a referencia. Peor mes −6,3219%; peor trimestre −8,9991%. Año2022 −8,9323%.

ShortsBTC:89, neto −3.848,835196, fees831,283090, PF0,671347, winrate41,57%; precio antes de fees también pierde −3.017,552106. LongBTC30 neto11.091,505475; SPY31 neto2.874,645447; PAXG35 neto3.167,576013. No confundir menores cantidades de los otros activos con cambios de sus reglas: cuenta compartida y trayectoria de capital.

Cobertura exacta del full:2.740.320 callbacks M1, desde2020-10-15T00:01Z hasta2025-12-31T00:00Z; inicialización neutral primera frontera4h,2020-10-15T04:00Z. DOWN2009 =open316 +pending1 +prioridadlong0 +rechazados1582 +planes110. Armed110, fills89, UP2008. Sin guard failures. El smoke técnico Q1-2021 tuvo125.340 callbacks; su menor cobertura efectiva no tiene una causa verificada, no se inventa. La corrida común completa sí coincide con todos los minutos esperados.

No se ajustan amplitud, ATR, STOP, inicialización, timeout ni años para rescatar esta receta. No demuestra que toda representación por eventos carezca de utilidad. El objetivo económico sigue sin lograrse y 2026 permanece cerrado.

## Gestión por falta de progreso — receta descartada

[Full terminado](http://localhost:9200/#/backtest/c6e326d6-5e63-4489-be8d-741d0f83f43a), 277,2 s, sin error: 241 trades, 111 longs y 130 shorts. CAGR 11,861636%, DD −18,265016%, Sharpe 0,738878, neto 7.939,441908 USDT y fees 2.426,185507.

Clon de referencia, sin mezclar experimentos. Sólo long BTC: en el primer cierre 4h con edad real ≥24 h, cerrar MARKET si ningún cierre estrictamente posterior al fill alcanzó entry+1R inicial, congelada con el stop original. Revisión efectiva entre 24 y 28 h; el milestone puede alcanzarse hasta esa revisión. Si pasa, conserva el trailing original. Fuente revisada por root y agente independiente: 17 métodos originales idénticos; sólo cambian hooks de gestión y se añaden helpers/counters.

V4 job 55d0ba2d94654a4394feedbe850bd4d9 succeeded; self-tests, fills, fees, wallet y MTM reconciliados. 33/61 meses activos positivos (54,10%), 33/63 todos y 14/21 trimestres. Completos: 33/59 activos, 33/61 todos y 14/19 trimestres. Rescata dos meses y estropea dos, sin avance neto de regularidad. Peor mes −6,79269%; peor trimestre −8,30382%. Años: 2020 parcial −3,33427%; 2021 −5,24177%; 2022 +6,31889%; 2023 +8,59928%; 2024 +34,3312%; 2025 +26,27145%.

Long BTC: 45 trades, neto 1.722,628222, fees 303,76636 y PF 1,608713; referencia 31 trades y neto 13.881,758924. Short BTC: 130, neto 2.155,808727, fees 807,98926 y PF 1,250446. SPY: 31, neto 2.001,440573; PAXG: 35, neto 2.059,564387. Reentradas y capital compartido alteran exposición posterior: la diferencia no se atribuye sólo a una salida aislada.

Auditoría independiente de logs y órdenes: 39 revisiones únicas emparejadas con 45 longs BTC. Edades entre 24,000 y 27,9833 h; cada revisión coincide con la primera frontera 4h elegible tras fill+24h. Los 34 fallos cerraron íntegramente MARKET exactamente en la revisión; los cinco pases tenían milestone posterior al fill y anterior o igual a la revisión. Seis posiciones cerraron antes de revisión. Best-close concuerda con cada clasificación. Counters finales: 45 fills y 45 cierres =6 previos +34 fallos +5 pases; sin posición terminal. Cero inconsistencias. Neto de cohortes descriptivas: fallos −326,54; pases +3.398,90; previos −1.349,73. No son contrafactuales ni base para retocar la regla.

Receta descartada sin cambiar plazo o R. No demuestra que toda gestión temporal falle. La referencia y 2026 permanecen intactos. Ninguna candidata nueva cumple los objetivos; no se rebajan criterios.

## Cierre de la tanda

Seis variantes combinadas y una receta probabilística se añaden a las 18 pruebas económicas previas de la orquestación, sin reiniciar el historial global de selección. Repetición debug, control de reloj y smoke son verificaciones técnicas, no nuevas hipótesis de alpha. Resultados negativos conservados; ninguna receta se promovió a producción ni se evaluó en 2026. No se hicieron descargas, scripts nuevos, cambios de framework, instalaciones, reinicios ni operaciones live/paper.

Lo aprendido: seleccionar menos shorts no garantiza más regularidad conjunta; cambiar a eventos con estos niveles destruye la contribución short; exigir progreso rápido con esta regla recorta la principal contribución long. Estas conclusiones se limitan a las recetas ejecutadas y a este histórico de desarrollo, ampliamente reutilizado. No certifican imposibilidad de mejorar BTC ni justifican una nueva rejilla de umbrales.

## Experimento adicional terminado: calendario semanal BTC

Candidata: añadir long BTC sábado 00:00 UTC hasta lunes 00:00 UTC, sólo si está flat y no hay plan original long ni short. Control descriptivo no seleccionable: martes 00:00 → jueves 00:00 UTC. Antes de código o rendimiento se fija régimen común EMA20 > EMA80 > EMA80[-5] y close > EMA80, ATR14, stop 2ATR, riesgo máximo 1%, duración 48h y caps de cartera originales. Planes originales conservan reglas y prioridad en la decisión, pero la nueva posición puede bloquear señales posteriores y modificar capital: no se afirma que sus fills permanezcan intactos.

Ambas fuentes fueron revisadas por root y un agente independiente antes de ejecutar; 16 métodos originales idénticos y clones que sólo difieren en clase, descripción y día. Las dos corridas terminaron sin error. El control debe separar mejor exposición bull de posible efecto de calendario; es contraste descriptivo bajo estados de cuenta endógenos, no inferencia causal. Un control mejor no se promoverá como ganador ni habilitará probar más días. El borrador del agente sugería miércoles–viernes; root fijó martes–jueves antes de código/datos/rendimiento, sin selección estadística. No se barren ventanas.

### Resultados de calendario y decisión

| Configuración | CAGR | DD motor | Meses activos positivos | Todos los meses | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| [Candidata sábado–lunes](http://localhost:9200/#/backtest/b3157b7b-1745-4e0a-8314-77205763f58c) | 23,25% | −14,72% | 34/61 (55,74%) | 34/63 (53,97%) | 14/21 (66,67%) |
| [Control martes–jueves](http://localhost:9200/#/backtest/dd37b90d-f28b-460d-9354-81122f7a4b0b) | 30,63% | −16,49% | 33/62 (53,23%) | 33/63 (52,38%) | 14/21 (66,67%) |

Periodos completos: candidata 34/59 activos y 13/19 trimestres; control 32/60 activos y 13/19 trimestres. Candidata rescata tres meses y estropea dos; control rescata cuatro y estropea cuatro. Candidata: 295 trades, neto 19.745,835839 y fees 3.981,314336. Control: 298 trades, neto 30.272,040985 y fees 5.360,317581.

Leg nuevo candidato: 81 trades, neto +747,794704, fees 376,496926, 42 ganadores, 3.748,4833 horas de exposición; 71 salidas MARKET y diez STOP. Control: 95, neto +283,291325, fees 733,861167, 39 ganadores y 3.400,6 horas; 50 MARKET y 45 STOP. No son patas independientes ejecutables fuera de la cuenta observada. El resultado de toda la cuenta depende además del bloqueo de entradas y capital posterior, no sólo del PnL nuevo.

Auditoría final 6767173c23d84f06bb9f7af287b9ab6f succeeded: V4, fills, fees, wallet, calendario y tipos/timestamps de entradas y salidas reconciliados. Contadores de fills/cierres coinciden con 81 y 95; no retrasos, quotes ausentes ni cierres terminales BTC observados. Las entradas del suplemento son MARKET en su slot exacto, created=executed=opened; MARKET de salida a deadline, STOP antes o igual. La primera auditoría a4c07e227e9c4d8183029236090532e5 falló por una suposición del analista: MARKET por sí solo no distingue el suplemento, pues también hay cuatro entradas MARKET originales fuera del slot por sesión. Se corrigió el clasificador para exigir tipo+slot y reconciliar los contadores independientes; no se cambió ni repitió estrategia para arreglar rendimiento.

Los contadores occupied/pending/baseline_priority/evaluated no son una partición aditiva de slots; no inferir señales futuras bloqueadas a partir de su suma. Evaluated sí coincide con rechazos de régimen/riesgo y planes. Counters son preterminales; en estas corridas todos los suplementos ya estaban cerrados antes de terminar. La posibilidad de cierre terminal del control fue un riesgo predeclarado, no un suceso ocurrido.

Se descarta la candidata. El mayor CAGR del control no mejora regularidad ni DD y no se promueve como ganador, tal como se fijó antes de resultados. No se prueban otros días. Total añadido a las 18 pruebas económicas previas: ocho configuraciones combinadas (siete candidatas y un control) y una receta probabilística; controles técnicos aparte. Ninguna candidata aprobada.

## Cambio de dirección solicitado por el usuario

El usuario cuestiona estancamiento. Se cierra esta tanda y no se abren más variantes locales. Diagnóstico guardado en strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_PORTFOLIO_DIAGNOSIS_20261018.md: 13 de 28 meses negativos tienen contribución BTC no negativa y PAXG/SPY conjunta negativa; ocho el caso contrario y siete ambos negativos. Tres mejores longs BTC representan 82,4% del neto de esa pata. No es una prueba de imposibilidad ni motivo para eliminar activos retrospectivamente.

Se recomienda estudiar complementariedad de las tres patas con velas ya disponibles, objetivos y riesgo iguales y 2026 reservado. El usuario AUTORIZÓ ampliar el alcance a BTC/PAXG/SPY como cartera. Se prepara el diseño fijo de roles descrito en PORTFOLIO_ROLES_STAGE_PROTOCOL_20261018.md. Funding/VIX/COT siguen descartados.
