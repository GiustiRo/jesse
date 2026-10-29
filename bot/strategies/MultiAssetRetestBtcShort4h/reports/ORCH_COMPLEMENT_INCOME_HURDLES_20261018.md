# Umbral económico de un complemento: escenario algebraico
Fecha2026-10-18. Análisis de snapshots existentes; sin nuevas estrategias, descargas ni datos2026. La autorización específica para el descargador de funding continúa pendiente.

## Pregunta y método
¿Cuánto tendría que rendir una fuente complementaria perfectamente regular, reservándole parte del capital, para mejorar los signos de la referencia hasta65%–70%de meses activos y80%de trimestres positivos?

Se reconstruyeron los63retornos mensuales de la referencia mediante auditorV4, con autocontroles y reconciliación. Para cada peso prefijado w en10%,25%,50%, se calculó:
R_mes=(1-w)*R_referencia_mes+w*((1+c)^f_mes-1).
c es un retorno mensual NETO hipotético sobre el capital asignado al complemento, no sobre toda la cuenta; f corrige el primer y último mes parcial según días realmente observados. Se supone rebalanceo mensual sin coste entre dos bloques matemáticos independientes.

Para w>0 y c>0 todos63meses serían activos: NO se mantiene artificialmente61como denominador. El mínimo65%requiere41/63positivos y70%requiere45/63;80%trimestral requiere17/21. Se resolvió el mínimo c por búsqueda monótona, sin convertirlo en umbral de entrada de una estrategia.

## Resultados
|Capital del complemento|Neto mensual fuente para65%meses +80%quarters|Equivalente anual fuente|Neto mensual fuente para70%meses +80%quarters|Equivalente anual fuente|
|---|---:|---:|---:|---:|
|10%|5,8245%|97,26%|9,8208%|207,76%|
|25%|1,9415%|25,95%|3,2736%|47,19%|
|50%|0,6472%|8,05%|1,0912%|13,91%|

Los porcentajes anuales son (1+c)^12-1 del complemento hipotético, NO CAGR de la cartera ni rendimiento observado de funding. El caso65%produce41/63meses y17/21trimestres;el caso70%produce45/63y18/21. En todos estos escenarios quedan16/19trimestres completos positivos;meses completos41/61o45/61. El control de80%en trimestres completos no eleva los umbrales obtenidos.

## Interpretación y límites
Una asignación pequeña a un ingreso modesto no asegura alcanzar los objetivos. Con25%de capital, el caso regular65/80exigiría1,94%NETO cada mes sobre ese bloque. Con50%el umbral baja, pero se retira la mitad del capital de la referencia y cambian retorno y riesgos conjuntos.

Esto es un escenario contable idealizado, no un backtest, frontera realizable, cota formal ni propuesta de pesos. Un complemento irregular o anticíclico podría producir otros resultados; no se demuestra imposibilidad general. No se modelan ejecución, tamaños discretos, one-way/netteo, margen/collateral separado, fundingvariable, solvencia ni drawdown intramensual. No se declara cumplido ningún objetivo.

La adquisición propuesta de funding sigue siendo estudio de viabilidad. No presupone que carry genere esos ingresos; primero habría que verificar cobertura, cashflows y coste sobre TODO capital reservado. La distribución de retornos de desarrollo ya fue observada: no usar sus fechas negativas o estos umbrales retrospectivos como filtro de trading.

## Evidencia
Análisis MCP04a4596f4bca4c318faf20aac39d77d7 y control de períodos completos8318816be5d1407294abcc671d7ef45a, ambos succeeded. Inputs: benchmark de precios2e943276-7815-4280-96c8-d634d2dab817 (no reutilizar su resultado económico),fadeb6f5562e-2144-4a54-9d27-108155680338,reject5c8e7296-fdc3-46a6-8663-ff00ff0b1d20,sleeves262fb59f-2b20-4247-aa9a-e7823cc3c930,y[referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Sólo la referencia aporta retornos del sistema; los otros snapshots identifican la escala inmutable de precios. V4autopruebas ycontabilidadterminal pasaron. El recuento permanece18backtests adicionales; estas son dos comprobaciones analíticas, no nuevas pruebas de estrategias.
