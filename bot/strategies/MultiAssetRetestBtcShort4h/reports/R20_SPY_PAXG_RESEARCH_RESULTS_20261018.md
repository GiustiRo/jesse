# R20 SPY/PAXG: resultados de las veinte exploraciones

Fecha local: 18 de octubre de 2026; algunas ejecuciones finalizaron el 19 de octubre UTC.

**Los veinte backtests terminaron. Esta tanda no demuestra una mejora robusta de ambos activos.** SPY obtuvo cuatro resultados positivos, cuatro negativos y dos recetas sin operaciones. Las diez recetas nuevas de PAXG terminaron negativas. No se acepta ninguna sustitución de la referencia ni se avanza a implementación operativa. El objetivo económico continúa pendiente.

## Contrato y trazabilidad

Se fijaron diez hipótesis por activo antes de observar resultados. Root revisó el motor y las diez señales de cada especialista antes del primer lanzamiento. Las clases son autocontenidas para que el snapshot de cada sesión conserve toda su implementación. Root verificó igualdad exacta entre las veinte fuentes revisadas y sus veinte snapshots.

Todas las sesiones usan desarrollo desde 2020-10-15 hasta 2025-12-31 **exclusiva**, capital aislado de 10.000 USDT, riesgo planificado del 1% por operación, comisión de 0,00045 por lado para todas las órdenes, apalancamiento aislado 5x y techo nocional bruto de 4,4x. La reserva de 10 bps para dimensionar posiciones no simula slippage. Root comprobó formularios, estados terminales y ausencia de errores en las veinte sesiones.

Se usaron los proxies de precio aceptados: SPX CFD BID/10 para SPY y spot PAXG. No se incorporaron funding, volumen supuesto o datos nuevos. BTC y 2026 permanecieron fuera de la tanda. No hubo scripts de investigación, cambios de framework, instalaciones, reinicios ni sesiones live/paper. Se respetaron los límites de cuatro backtests y dos análisis simultáneos.

Estas son veinte pruebas adicionales sobre desarrollo ya utilizado, después de los diecisiete fulls de la etapa anterior y más exploraciones históricas. Sus mecanismos no son independientes; varias reglas comparten reversión, momentum o contexto entre activos. No se presenta ningún resultado como OOS limpio.

## Los veinte resultados

Neto después de comisiones. Las cuentas son aisladas: no sumar estas ganancias o curvas para representar una cartera. PF usa ganancias y pérdidas netas de operaciones. DD corresponde al motor; cero operaciones no implica un retorno o drawdown demostrados de cero.

|Experimento y sesión|Operaciones|NetoUSDT|FeesUSDT|PF|DDmotor%|
|---|---:|---:|---:|---:|---:|
|[PAXG20-01 R20PaxgARResponse4h](http://localhost:9200/#/backtest/51a0c817-4c43-4940-ab0e-4bfec6b3a52c)|393|-1909.52|1890.23|0.786|-26.640|
|[PAXG20-02 R20PaxgPathAnalogue4h](http://localhost:9200/#/backtest/a758809e-9d05-4e7e-a5b9-333751a19395)|1082|-4546.37|4816.61|0.737|-52.978|
|[PAXG20-03 R20PaxgSpyDelayed1h](http://localhost:9200/#/backtest/f72b8359-4531-42ff-8cc0-5b61a6f23320)|17|-132.62|108.69|0.677|-1.991|
|[PAXG20-04 R20PaxgDirectionalOvershoot1h](http://localhost:9200/#/backtest/b8ee439b-4d96-46c3-8948-fca6eb59f5eb)|928|-7464.85|5503.71|0.664|-74.729|
|[PAXG20-05 R20PaxgRoundBarrier1h](http://localhost:9200/#/backtest/43ec28da-525d-46d6-8c65-c641f32aa1d7)|766|-8329.60|6069.89|0.548|-83.416|
|[PAXG20-06 R20PaxgBreakevenRevisit4h](http://localhost:9200/#/backtest/351eb0d1-160b-4079-a4d6-7aa50fec5ed4)|18|-102.68|138.83|0.835|-2.211|
|[PAXG20-07 R20PaxgStaircase4h](http://localhost:9200/#/backtest/ffc75a3c-81cb-43cd-8b2f-65fb2201d19b)|27|-526.00|166.31|0.259|-6.113|
|[PAXG20-08 R20PaxgSemivariance4h](http://localhost:9200/#/backtest/842e4385-1c19-4f61-b5d5-acd8f96c9ce9)|3|-132.57|13.60|0.000|-1.326|
|[PAXG20-09 R20PaxgTrendExhaustion4h](http://localhost:9200/#/backtest/f081dc32-7dc3-4f28-9a60-77275d6c155c)|108|-2022.43|705.54|0.526|-22.128|
|[PAXG20-10 R20PaxgMonthEndRebalance1h](http://localhost:9200/#/backtest/105bd7cf-90dd-454a-b2f8-8942dad5e30f)|20|-425.29|133.19|0.595|-7.984|
|[SPY20-01 R20SpyCashGapFade](http://localhost:9200/#/backtest/3e887db0-3e26-4405-a62f-100a1f466432)|36|-197.16|129.27|0.796|-3.281|
|[SPY20-02 R20SpyAcceptedGap](http://localhost:9200/#/backtest/32a9b1f5-ea19-43ff-bd30-17a4a9fb4379)|36|174.97|128.95|1.235|-2.499|
|[SPY20-03 R20SpyCashInventoryRecovery](http://localhost:9200/#/backtest/fc9e0fb9-3be4-4d79-9ea6-cd5289ba62f5)|25|136.99|91.90|1.329|-2.280|
|[SPY20-04 R20SpyCrashRecovery](http://localhost:9200/#/backtest/f9055a4a-00ae-4a77-b153-c9bc811ae2eb)|0|Sin operaciones|—|—|—|
|[SPY20-05 R20SpyDownsideCascade](http://localhost:9200/#/backtest/3e5679ee-7c30-4629-a4ac-099c272b1e2d)|16|-59.15|42.60|0.875|-3.801|
|[SPY20-06 R20SpyPostShockReentry](http://localhost:9200/#/backtest/2624be2b-8db2-4400-9858-4bfd67aeabce)|2|122.69|5.37|Sin pérdidas observadas|-0.809|
|[SPY20-07 R20SpyDayNightDisagreement](http://localhost:9200/#/backtest/9f03cc46-9c01-4856-9a1a-5bab7387f2da)|12|77.13|51.78|1.161|-3.212|
|[SPY20-08 R20SpyJointLiquidation](http://localhost:9200/#/backtest/f4252286-205b-4fa0-8111-c36f00d4e9a3)|10|-21.71|26.04|0.920|-2.987|
|[SPY20-09 R20SpySafeHavenUnwind](http://localhost:9200/#/backtest/f2461e76-9adc-4adb-9677-8e8ef4791a6d)|23|-213.65|87.27|0.657|-4.090|
|[SPY20-10 R20SpyFailedCrashBounce](http://localhost:9200/#/backtest/cb0d1d11-8695-44d9-8a2f-20a7f1cf3183)|0|Sin operaciones|—|—|—|


## Comparadores conservados

|Política aislada1%|N|NetoUSDT|PF|DDmotor%|
|---|---:|---:|---:|---:|
|[SPY retest](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2)|31|751.35|1.493|−5.213|
|[PAXG retest](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c)|35|546.11|1.308|−6.919|
|[PAXG fin de semana0,75](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c)|60|764.04|1.732|−2.991|


La regla de fin de semana sigue siendo una hipótesis experimental anterior, no una sustitución aceptada: su prueba previa con cuenta compartida no mejoró la regularidad. La [referencia original](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) permanece congelada. Esta tanda no hizo nuevas pruebas de cartera.

## Interpretación

**SPY02, continuación del gap aceptado**, pasa apenas el cribado descriptivo con 36 operaciones y PF 1,235. Conserva 103,33 / 31,69 USDT al añadir 5 / 10 bps de coste RT sobre los mismos fills. Sin su mayor ganador de 303,05 USDT pierde 128,08. Sus retornos MTM de 2024 y 2025 son negativos: −0,274% y −0,329%. Retirar retrospectivamente los largos perdedores no constituye validación. Su menor retorno y menor DD frente al retest no demuestran una mejora dominante.

**SPY03, recuperación tras la sesión cash**, gana 136,99 USDT en 25 operaciones y conserva 85,93 / 34,88 con esos recargos. Sin el mayor ganador queda +61,20; sin los tres mayores, −56,91. Tiene muestra insuficiente según el protocolo y años MTM débiles. SPY06 solo reúne dos operaciones positivas; SPY07 tiene doce y PF 1,161. Ninguna se promueve por mostrar un total positivo.

SPY04 y SPY10 no generaron exposición. Los snapshots no exportan estados internos: cero entradas no permite inferir si jamás ocurrió el subestado de crash o faltó su confirmación posterior. No se relajaron sus condiciones para fabricar operaciones.

**PAXG no deja supervivientes.** Cinco reglas tienen menos de treinta operaciones: 03, 06, 07, 08 y 10. Sus muestras son insuficientes, además de terminar negativas. Las otras cinco ofrecen evidencia económica más clara contra sus recetas concretas; esto no refuta toda la familia de ideas. El modelo de análogos gana 270,24 USDT antes de comisiones y paga 4.816,61: su ventaja bruta equivale a unos 0,505 bps por nocional de entrada, frente a aproximadamente 9 bps de comisión RT. Reducir hipotéticamente los costes o retirar un lado no valida la regla probada.

El cribado previo exigía neto positivo, PF ≥ 1,2, unas treinta operaciones y DD no peor que −25%. Pasarlo solo autoriza investigar más. La concentración y fragilidad temporal impiden tratar SPY02 como una mejora aceptable. No hubo una superviviente defendible que justificara sensibilidades dinámicas o integración compartida adicionales.

## Verificación y límites

Los análisis de snapshots completos concilian órdenes ejecutadas, cantidades, comisiones, PnL y wallet, y documentan solapamientos y liquidaciones terminales. Los recargos de 5 / 10 bps RT aplican 2,5 / 5 bps a cada lado sobre todos los fills, conservando decisiones y cantidades. Son análisis estáticos, no backtests con nuevo dimensionamiento.

Root reconstruyó MTM al cierre diario UTC de las ocho reglas SPY con operaciones, conciliando balances terminales. Se recuperaron precios de benchmarks mediante múltiples anclas de órdenes, con error relativo inferior a 2,3e−15. La curva Portfolio de las 00:01 no se usa como cierre del día. Se conservan meses y trimestres completos, bordes parciales, años y DD diario en los dos informes MTM. Los objetivos de regularidad corresponden a cartera. No se publica regularidad MTM de las nuevas reglas PAXG: sus cohortes por año de cierre están expresamente etiquetadas como tales.

Las features SPY requieren sesiones observadas completas y cotizaciones M1 frescas. Festivos y cierres tempranos ausentes no se rellenan. Timestamps consecutivos tampoco certifican ausencia de relleno previo del proveedor. El ATR diario usa catorce sesiones observadas; no equivale al ATR Wilder de 4h. Las salidas temporales esperan cotización fresca cuando hay huecos.

Las reglas PAXG con SPY usan retornos logarítmicos comparables y fixings emparejados. Las etiquetas de seis barras del modelo de análogos están maduras antes de predecir; la separación de patrones no vuelve independientes sus etiquetas. Estos controles permiten estudiar la acción del precio, sin certificar ejecución futura en Binance.

## Continuidad de la investigación

El requisito de mejorar ambos activos sigue pendiente. Mantenemos las referencias y 2026 cerrado. No se abre otra fase ni se declara éxito por completar veinte pruebas.

SPY02 y SPY03 quedan como preguntas específicas sobre información de gaps e inventario al cierre, con debilidades explícitas. Antes de ampliar su búsqueda, una comparación futura deberá fijar un control interpretable, presupuesto de pruebas, criterio de abandono y medida de aporte incremental. No seleccionar años o direcciones favorables, ni rebajar filtros para conseguir más muestra. Una ganancia nueva sobre 2020–2025 seguirá siendo un descubrimiento seleccionado.

Las diez recetas PAXG se archivan con sus resultados. Su fracaso no autoriza a dar por robusta la regla anterior de fin de semana. Las siguientes investigaciones deben formular una hipótesis refutable y explicar qué evidencia nueva aportarán frente al inventario ya explorado; continuar hasta encontrar cualquier curva positiva aumentaría el riesgo de sobreajuste.

## Informes persistentes en el proyecto Jesse

- strategies/MultiAssetRetestBtcShort4h/reports/R20_SPY_PAXG_STAGE_PROTOCOL_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/R20_MTM_SPY_BATCH1_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/R20_MTM_SPY_BATCH2_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY20_MATRIX_PROTOCOL_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY20_FREEZE_ADDENDUM_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY20_IMPLEMENTATION_REVIEW_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY20_FINAL_RESULTS_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY20_METHODOLOGICAL_REVIEW_20261018.md
- strategies/ResearchPaxgWeekendReturn1h/reports/R20_PAXG_TEN_EXPERIMENTS_PROTOCOL_20261018.md
- strategies/ResearchPaxgWeekendReturn1h/reports/R20_PAXG_IMPLEMENTATION_REVIEW_20261018.md
- strategies/R20PaxgARResponse4h/reports/R20_PAXG_BATCH1_AUDIT_20261018.md

- strategies/R20PaxgARResponse4h/reports/R20_PAXG_FINAL_20261018.md
- strategies/R20PaxgARResponse4h/reports/R20_PAXG_BATCH2_AUDIT_20261018.md
- strategies/R20PaxgARResponse4h/reports/R20_PAXG_ANALYSIS_SOURCE_20261018.md

Cierre PAXG leído por root: 3.362 operaciones primarias y 95 de comparación auditadas. Último job a703e1e367cf4d868defe61e9dc17a7c succeeded. Los DD superiores al 25% son cuatro: PAXG01,02,04,05. Todos los trabajos de R20 terminaron. La autorización posterior para veinte escenarios más se registra separadamente como R40; no cambia el veredicto anterior.
