# Resultado completo: descartar la hipótesis de overshoot relativo

[Backtest completo BTC/ETH](http://localhost:9200/#/backtest/62b9f852-8b48-4b4c-b59b-537e9e687a64). Estado finished sin excepciones ni cambios de parámetros tras el protocolo y smoke. Ventana2020-10-15→2025-12-31exclusivo, normal, benchmark=True, warmup240;10000USDT,5xaislado,fee0.00045porlado. Riesgo inicial máximo1%basket/0.5%porleg. Fuente verificada idéntica a la revisada antes del run. 2026 no evaluado.

## Resultado económico de la cesta, no de piernas aisladas
|Medida|Resultado|
|---|---:|
|Baskets completos|1247|
|Piernas cerradas|2494|
|Neto|−3403.1719USDT|
|Comisiones|2947.4336USDT|
|Saldo final|6596.8281USDT|
|CAGR motor|−7.6689%|
|Drawdown motor|−34.3718%|
|Winrate de basket neto|36.3272%|
|Winrate de piernas individuales|44.7875%|

El PnL de precio a cantidades y fills realizados, antes de restar comisiones pagadas, es−455.7382USDT. No es un backtestfee0: sólo indica que la pérdida no se explica exclusivamente por comisiones. Las dos direcciones de basket pierden: BTClong+ETHshort−1573.4464;BTCshort+ETHlong−1829.7255. No se exige signo positivo a una pierna de cobertura individual.

PnL de baskets por año de cierre (NO retornos anualesMTM):2020parcial−197.3331;2021−610.3368;2022−746.0941;2023−922.7507;2024−477.4752;2025−449.1820. Todos negativos. No usar estos años para crear filtros retrospectivos.

## Costes diagnósticos sobre iguales fills y cantidades
Neto con coste adicional0.0005porlado(+0.10%poroperacióncompleta de cada leg):−6678.0981USDT. Con0.00125porlado(+0.25%):−11590.4875. Es aritmética de fills fijos; no nueva simulación, no CAGR/DDestresados ni cambios de tamaños/capital posteriores.

## Auditoría de ejecución y temporalidad
Análisis MCP7dfd3225695c40f5a1012a0233005c79 succeeded, input snapshot íntegro3962420bytes. Cadaopened_at contiene exactamente dos registros BTC/ETH con lados opuestos. Cada leg tiene una entradaMARKET y una salidaEXECUTED completa; no parciales/piramidado ni duplicados de entrada. Identidad precioPnL−fee y suma de baskets/neto reconciliadas. Cantidad relativa de notionalsETH/BTC observada0.25823–1.19077; no es una verificación independiente de β ni certificado de neutralidad.

191baskets (15.317%) tienen separación entre cierres de sus piernas. Máximo3540s(59min), suma326400s(90.6667h). No sumar esa duración como exposición monetaria: aquí no se reconstruyeron marks de la pierna sobreviviente. Hold máximo12h. La ejecución es secuencial y el riesgo huérfano es real dentro del modelo, aunque ambas entradas compartan timestamp.

## Contador de posiciones terminales: precisión importante
metrics.total_open_trades informa2 yopen_pl0.83463. La inspección read-only de Strategy._terminate muestra que incrementa ese contador ANTES de forzar el cierre al terminar. Las últimas dos piernas sí tienen MARKETreduce_onlyEXECUTED,closed_at=finish_date yPNL/fees registrados. Hay1247baskets íntegros; dos piernas fueron LIQUIDADAS POR FIN DEL BACKTEST, no naturalmente cerradas por la señal. No se cambió el snapshot ni se puso el contador a cero.

Por ese contador preterminación, el guard conservador actual de auditorMTMv4 rechazaría esta sesión aunque los registros cerrados permitan reconciliarla. No se presentan porcentajes mensualesMTM improvisados; ROOT decidirá si ampliar ese contrato con evidencia de fills terminales. La conclusión de descarte ya es inequívoca por neto yDD, sin necesitar un ajuste de auditor para rescatar resultados.

## Conclusión y límites
Descartar esta formulación. OLS de retornos con α/β congeladas sólo define exposición y una referencia causal; no demuestra cointegración, estacionariedad del spread acumulado ni recuperación. Es una hipótesis de overshoot transitorio que no superó la primera falsación económica. Recuperar residualcero tampoco garantiza PnLcash positivo por derivaα, beta y aproximaciónlog→cash.

No proceder a buscar un ganador1hvs2h, aumentar riesgo, cambiar umbrales ni introducir ejecución1m para rescatar esta pérdida. La ejecución1m/data1h queda como posible control técnico de otra hipótesis que primero demuestre ventaja. Sin funding/spread/impacto/rechazos reales modelados; esos costes adicionales no aportarían validación al resultado actual.

StandaloneBTC/ETH: la referencia ya operaBTC en Binanceone-way; sumar curvas o duplicar rutaBTC no sería integración ejecutable. La referencia y2026 siguen intactos. No cambios de framework, reinicios, instalaciones ni live/Pi. La importación ETH continúa almacenando datos posteriores mientras se completa; no se usa su rendimiento2026.

## Adenda: auditoría MTM V4 de ROOT completada

Job fbb1facc83304c62857321ebe9a914c1 succeeded. Auditor con diagnóstico terminal: ambas piernas forzadas, precioPnLpreclose ywallet reconciliados sin alterar métricas del snapshot. Escalas de precios verificadas con104anclasBTC y102ETH, timestamps distintos, errores relativos~1e−15.

10/63meses activos/calendario positivos=15.873%;1/21trimestres=4.762%. Excluyendo períodos parciales de borde:9/61meses=14.754%,1/19trimestres=5.263%. Peor mes−2.66866%;peor trimestre−4.83889%;DDdailyclose−34.3730%. Retornos anualesMTM2020parcial−1.9733%,2021−6.2262%,2022−8.1165%,2023−10.9250%,2024−6.3465%,2025parcial−6.3750%.

Correlación de contribucionesMTM entre piernas−0.7603: refleja exposición opuesta, no demuestra una fuente rentable. Confirma descarte; ninguna búsqueda de parámetros ni validación2026 procede para esta formulación.

Importación ETH finalizada:03565c0b-635f-4d7d-8055-61237d918b5a,3248443velasobservadasM1,2020-08-15→2026-10-18;filasexistentes retenidas. La evaluación anterior sólo usó2020–2025.
