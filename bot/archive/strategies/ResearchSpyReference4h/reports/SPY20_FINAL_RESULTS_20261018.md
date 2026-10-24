# SPY20: diez exploraciones completadas

Fecha local: 18 de octubre de 2026. **Los diez fulls primarios terminaron. Ninguna estrategia se promueve como mejora operativa.** SPY20-02 deja una pista frágil de continuación de gaps; SPY20-03 deja una pregunta de recuperación de inventario con muestra insuficiente. No hubo sustituciones, cambios de umbral ni rescates después de observar resultados.

Esta tanda añade diez experimentos SPY al historial amplio de selección, incluidos los cinco SPY y los demás experimentos de la etapa anterior. No son diez mecanismos independientes ni una muestra OOS nueva.

## Contrato, fuentes y predeclaración

Se leyeron el handoff actualizado, el consolidado de los 17 fulls previos, el inventario global y fuentes de las familias relacionadas antes de diseñar. Matriz SPY20_MATRIX_PROTOCOL_20261018.md y aclaraciones SPY20_FREEZE_ADDENDUM_20261018.md guardadas antes de resultados. Root revisó motor común y las diez señales antes del primer lanzamiento. Código de cada clase R20Spy... y snapshot de notas conservados antes de correr.

Desarrollo: 2020-10-15 a 2025-12-31 exclusiva. Capital 10.000 USDT, riesgo inicial 1%, fee 0,00045 por lado incluidas LIMIT, 5x aislado y techo bruto 4,4x. Reserva de 10 bps exclusivamente para sizing. Proxy de precio SPX CFD BID/10 aceptado para desarrollar operativa de SPY Binance perpetual. Sin volumen ficticio ni funding. BTC, referencia de cartera y 2026 intactos. No scripts, framework, instalaciones, reinicios ni live/paper.

Cada señal emplea el reloj y horizonte que fijó su protocolo. Ruta 30m y M1 auxiliar; SPY20-08/09 añaden únicamente precios auxiliares PAXG, sin operar PAXG o BTC. Los resultados no son recomendaciones de exposición ni una cartera sumada.

## Todos los resultados

Neto y recargo en USDT. DD corresponde al motor; su frecuencia difiere del DD diario MTM de abajo. El recargo +5 bps RT aplica 2,5 bps a cada lado sobre los mismos fills, manteniendo cantidades y decisiones.

| Experimento | Receta | N | Neto | Fees | PF | DD motor % | Neto con +5 bps RT |
|---|---|---:|---:|---:|---:|---:|---:|
| [SPY20-01](http://localhost:9200/#/backtest/3e887db0-3e26-4405-a62f-100a1f466432) | CashGapFade | 36 | -197.16 | 129.27 | 0.796 | -3.281 | -268.98 |
| [SPY20-02](http://localhost:9200/#/backtest/32a9b1f5-ea19-43ff-bd30-17a4a9fb4379) | AcceptedGap | 36 | 174.97 | 128.95 | 1.235 | -2.499 | 103.33 |
| [SPY20-03](http://localhost:9200/#/backtest/fc9e0fb9-3be4-4d79-9ea6-cd5289ba62f5) | CashInventoryRecovery | 25 | 136.99 | 91.90 | 1.329 | -2.280 | 85.93 |
| [SPY20-04](http://localhost:9200/#/backtest/f9055a4a-00ae-4a77-b153-c9bc811ae2eb) | CrashRecovery | 0 | Sin operaciones | — | — | — | — |
| [SPY20-05](http://localhost:9200/#/backtest/3e5679ee-7c30-4629-a4ac-099c272b1e2d) | DownsideCascade | 16 | -59.15 | 42.60 | 0.875 | -3.801 | -82.82 |
| [SPY20-06](http://localhost:9200/#/backtest/2624be2b-8db2-4400-9858-4bfd67aeabce) | PostShockReentry | 2 | 122.69 | 5.37 | Sin pérdidas observadas | -0.809 | 119.71 |
| [SPY20-07](http://localhost:9200/#/backtest/9f03cc46-9c01-4856-9a1a-5bab7387f2da) | DayNightDisagreement | 12 | 77.13 | 51.78 | 1.161 | -3.212 | 48.36 |
| [SPY20-08](http://localhost:9200/#/backtest/f4252286-205b-4fa0-8111-c36f00d4e9a3) | JointLiquidation | 10 | -21.71 | 26.04 | 0.920 | -2.987 | -36.18 |
| [SPY20-09](http://localhost:9200/#/backtest/f2461e76-9adc-4adb-9677-8e8ef4791a6d) | SafeHavenUnwind | 23 | -213.65 | 87.27 | 0.657 | -4.090 | -262.13 |
| [SPY20-10](http://localhost:9200/#/backtest/cb0d1d11-8695-44d9-8a2f-20a7f1cf3183) | FailedCrashBounce | 0 | Sin operaciones | — | — | — | — |

El [retest SPY aislado al 1%](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2), reutilizado como comparación contextual, tiene 31 trades, +751,35 USDT, PF1,493 y DD motor−5,213%. Sus +5/+10 bps RT dejan +592,19/+433,04 USDT. Los tamaños y capital-tiempo difieren; no es una prueba causal del trigger de cada primaria.

## Interpretación crítica

**02: continuación del gap aceptado.** Con 36 trades, PF1,235, DD−2,499% y neto+174,97, pasa apenas el cribado descriptivo. Conserva +103,33/+31,69 USDT con otros5/10bpsRT. Sin su mayor ganador de303,05 queda−128,08. MTM2024 y2025 son negativos (−0,274% y−0,329%). El lado largo pierde70,86 y el corto gana245,83; esto es diagnóstico, no autorización para retirar longs. Comparado con el retest, aporta menor retorno y menor DD, sin mejora dominante demostrada. Una entrada informativa de gap puede ser una pregunta de complemento distinta del retest, pero su concentración y temporalidad impiden recomendar integración ahora.

**03: recuperación de inventario cash.** Sus25trades ganan136,99 y conservan85,93/34,88 con5/10bpsRT extra. Sin el mayor ganador todavía deja61,20, pero sin los tres mayores queda−56,91. MTM2022−1,522%,2024−0,661% y2025+2,153% muestran dependencia de época. Es una hipótesis de liquidez al cierre con condición nocturna, distinta del RSI3 previo; no alcanza la muestra predeclarada. Puede merecer una comparación futura predeclarada si root encuentra una mejora incremental defendible, sin bajar umbral para fabricar30trades.

**04 y10: receta sin exposición.** Las dos reglas completas de crash/recuperación y crash/rebote fallido generan cero operaciones. Su condición extrema —caída10% desde un máximo reciente en cinco sesiones, con confirmación posterior— era previsible que produjera muy poca muestra desde octubre2020. Se mantuvo intacta. No existe evidencia económica para evaluarlas y no corresponde llamar esto rentabilidad0%, DD0% o ausencia de efecto. Los snapshots no exportan vars ni contadores de episodios: cero entradas no permite distinguir si nunca se activó el subestado de crash o si faltó su confirmación posterior. No se inventan esos estados ni se crean sustituciones automáticas.

**05,08 y09:** las recetas terminan negativas, con muestras16/10/23. 05 y09 pierden también antes de fees; 08 apenas gana4,33 por precio y paga26,04 de fees. Las cohortes favorables de2022 no rescatan los períodos posteriores. No modificar disparadores, contexto PAXG o dirección para salvarlas.

**06:** dos trades positivos no validan una regla. Su ganancia122,69 y bajo DD sólo describen esos dos eventos. Cuatro meses MTM positivos durante sus tenencias no son cuatro observaciones independientes. No usar winrate100% o PF sin pérdidas para promoverla.

**07:** gana77,13 en doce trades, PF1,161; sin el mayor ganador pierde71,29. Los años MTM2024/2025 son negativos, mientras la ganancia se concentra en2021. No demuestra una prima estable por desacuerdo entre participantes nocturnos y cash.

**01:** pierde197,16 y también es negativa antes de fees. Se archiva la receta de fade de gap. El contraste01/02 son políticas alternativas con conjuntos de eventos diferentes, no una identificación causal de inventario versus información.

## MTM diario UTC y períodos completos

Root reconstruyó equity al cierre diario UTC desde fills y precios observados anclados, conciliando fees, wallet y terminal. No se usa PnL del mes de cierre ni las muestras Portfolio00:01 como cierre del día.

| Modelo | Meses positivos / activos completos | Positivos /61 meses completos | Trimestres positivos /19 completos | DD diario MTM |
|---|---:|---:|---:|---:|
| Referencia aislada |15/33|15/61|9/19|−5,218%|
|01|14/28|14/61|7/19|−3,279%|
|02|15/28|15/61|9/19|−2,526%|
|03|12/21|12/61|8/19|−2,284%|
|05|8/14|8/61|4/19|−3,799%|
|06|4/4|4/61|2/19|−0,804%|
|07|4/9|4/61|2/19|−3,204%|
|08|7/11|7/61|3/19|−2,983%|
|09|8/19|8/61|4/19|−4,094%|

04/10 no tienen fills ni métricas suficientes para estos ratios. Bordes parciales, todos los meses y años completos están en los informes root R20_MTM_SPY_BATCH1_20261018.md y R20_MTM_SPY_BATCH2_20261018.md, bajo reports de MultiAssetRetestBtcShort4h. Jobs272eb9c53aca4bb5aae4e3b08c1a1b6b y266bb0fcee334fb28b5e9ed5b7d278b6: succeeded.

No se exige regularidad de cartera a cada señal. A la inversa, algunos meses activos positivos o correlación baja no bastan para recomendar una cartera. La evidencia actual no demuestra mejora compartida de02/03 frente a mantener el retest.

## Datos, observabilidad y ejecución

Cada sesión de features exige13velas30m y30M1 disponibles consecutivas por vela. Festivos, cierres tempranos y huecos permanecen ausentes. El cierre anterior usado como nocturno requiere el día hábil civil anterior; se excluyen fechas que no cumplen, sin afirmar un calendario NYSE completo. Esta selección puede cambiar la distribución de eventos. La existencia de timestamps consecutivos tampoco certifica que el proveedor no haya rellenado datos aguas arriba.

ATR diario: media simple de14true ranges previos sobre sesiones observadas, no Wilder4h. Los64fixings PAXG de08/09 están sincronizados y su normalizador excluye los tres intervalos del evento. No equivale a observar flujo, inventario, oro justo ni causalidad macro.

No se extrapola rendimiento de SPY CFD a fills perpetual certificados; la aceptación del proxy permite investigar la regla de precio. No se impuso conseguir fuentes nuevas o implementar funding para esta tanda.

Horizontes nominales se miden desde fill; las deudas de salida esperan quote fresca. Duraciones máximas observadas:01=81,5h frente48;02=105,5 frente72;03=75,5 frente48;05/07/08=147,5 frente120;06=267,5 frente240;09=123,5 frente120. No se fingen salidas en cierres sin cotización. Stops y targets permanecen activos24/7, y los límites son riesgos planificados, no garantía frente a gaps reales.

## Auditoría y continuidad

Diez backtests terminales finished, ocho con operaciones y dos sin ellas. Seis análisis de snapshots completos terminaron succeeded; conciliaron las sumas de precio, fees0,00045porlado y métricas donde existen, y verificaron relojes de entrada10:00/16:00NY y techo de nocional inicial. No hubo error de estrategia ni cambio de reglas tras resultados.

Archivos persistentes en esta carpeta:
- SPY20_MATRIX_PROTOCOL_20261018.md y SPY20_FREEZE_ADDENDUM_20261018.md: recetas previas.
- SPY20_IMPLEMENTATION_REVIEW_20261018.md: motor y señales revisados.
- SPY20_SESSION_REGISTRY_20261018.md: diez IDs y enlaces.
- SPY20_AUDIT_*.md y SPY20_RESULTS_DATA_20261018.md: todos los números, incluidas pérdidas y ceros.
- SPY20_ANALYSIS_SOURCE_20261018.md: análisis reproducible y jobs.

Se conservan02/03 como preguntas de investigación con debilidades explícitas, no como candidatas aceptadas. Una futura comparación incremental necesitaría protocolo previo, tamaños coherentes y cuenta compartida real. No sumar curvas, optimizar direcciones o abrir2026 para encontrar una aprobación. Hasta esa evidencia, la referencia permanece y esta tanda SPY termina sin promoción.
