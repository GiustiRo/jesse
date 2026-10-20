# R11 — Gestión de capital de K1001 y N204
Fecha: 2026-10-19. Estudio concluido: 24 corridas nuevas y cuatro anclas5x; 28 configuraciones comparadas.
Hipótesis y matrices se fijaron antes de sus resultados. K1001 sigue ganadora provisional de investigación; N204 referencia congelada. 2026 continúa cerrado.

## Hallazgos
- Con el sizing original, 3x/4x/5x forman una meseta práctica: sus diferencias de neto son de pocos USDT sobre cuentas iniciales10000. No hay un beneficio histórico material por disponer de5x frente a3x bajo estas reglas.
- K1001 a1x retiene el96.00% del beneficio del ancla enB y97.88% enC; reduce la magnitud del drawdown16.41% y17.20%, respectivamente. Es un compromiso conservador atractivo en esta muestra. No gana todos los años ni tiene el menor DD absoluto entre todas las políticas.
- Riesgo5/15 a5x aumenta CAGR K1001 hasta39.72–39.94%, con DD16.50–17.41%. Mejora retorno y Calmar frente a5x original, pero el Sharpe prácticamente no mejora enC y queda por debajo de1x enB/C. No mejora consistentemente la regularidad mensual.
- Margen5/15 a5x, conservando las protecciones de riesgo1/8, reduce CAGR K1001 a10.42–10.47% y DD a6.29%. Es la política menos agresiva probada por DD histórico, pero resigna mucho retorno frente a1x.
- K1001 supera a N204 en retorno/CAGR, Sharpe y PF en las siete políticas equivalentes y ambas carteras. El DD no es estrictamente mejor en todos los casos: por ejemploB5x original K1001−8.8231% vsN204−8.7768%. No se declara dominancia universal.
- Las 28 configuraciones conservan las mismas entradas y salidas que su propia ancla5x. No hay nuevas/retiradas entradas ni cambios de tiempo/precio de salida: el cambio observado es de cantidades y composición del capital entre activos.

## Contrato reproducible
2020-10-15 inclusiva →2025-12-31 exclusiva; histórico de desarrollo reutilizado, no OOS. Capital compartido10000 USDT; BTC/PAXG/SPY4h, tres feeds1m; isolated, fee0.00045 por lado; warmup240; fast_modefalse; debugtrue. B=SPY Second, C=SPY Market. Orden BTC/PAXG/SPY congelado. Todas las fuentes originales se preservaron.
A: sólo cambia leverage1/2/3/4 vs ancla5; riesgo objetivo1%/agregado8%, capnominal4.4, pesos inversos ATR, margen disponible×0.90, reservas pendientes y reserva sizing0.001 exactos.
B R5A15: riesgo objetivo5%/agregado15% en las tres rutas, mismos límites nominales y de margen. Puede no alcanzar5% por restricciones; no es multiplicar PnL por cinco.
B M5A15: añadir límites de margen5% por orden y15% agregado, medidos como nominal/leverage, incluyendo posiciones valoradas al mark y pendientes; conservar riesgo1/8. Límite de admisión, sin rebalanceo forzado posterior.
Capital base conservador=max(0,min(wallet,equity)). Riesgo agregado desde mark a stop más costes, distinto de suma de pérdidas futuras garantizadas. Stops técnicos, objetivos, relojes, señales y calendario iguales.
5% de margen con5x produce nominal máximo25% de cuenta; con stop2%, riesgo aproximado0.5% más costes. 5% de riesgo al stop tiene otra escala. Esta aritmética ilustra la diferencia; el riesgo efectivo no se certificó trade a trade.
La cuota nominal4.4 se retuvo enA para aislar el margen del motor; con leverage menor no significa poder alcanzar4.4x. La prioridad de rutas puede afectar distribución cuando falta margen.

## Resultados completos
Retorno y CAGR en%; DD negativo; PF de PnL neto por trade; Calmar y Sharpe del motor. Underwater en días según motor. Meses positivos sobre61meses calendario completos; se excluyen2020-10 y2025-12 de ese denominador, no los meses sin operaciones.

### K1001B

|Política / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[1x · riesgo1/8](http://localhost:9200/#/backtest/141760eb-4fbc-4832-915c-87cb417931d6)|13074.77|130.75|17.40|-7.38|2.359|1.754|2.101|242|1462.53|278|45/61|
|[2x · riesgo1/8](http://localhost:9200/#/backtest/1f451972-2da0-4a2c-97be-d532351a59ff)|13422.04|134.22|17.73|-8.85|2.003|1.650|1.966|242|1748.11|291|43/61|
|[3x · riesgo1/8](http://localhost:9200/#/backtest/065ff012-e01f-47fc-a043-b21404d65bbd)|13616.90|136.17|17.92|-8.82|2.031|1.656|1.976|242|1767.99|291|43/61|
|[4x · riesgo1/8](http://localhost:9200/#/backtest/0b85e584-e4b2-469f-ae2b-12d60d1c2d82)|13616.89|136.17|17.92|-8.82|2.031|1.656|1.976|242|1767.99|291|43/61|
|[5x · riesgo1/8](http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a)|13619.21|136.19|17.92|-8.82|2.031|1.656|1.976|242|1767.92|291|43/61|
|[5x · margen5/15 + riesgo1/8](http://localhost:9200/#/backtest/b1d19022-bae3-4af1-b013-56b79bb5641c)|6763.22|67.63|10.42|-6.29|1.656|1.559|1.944|242|721.43|193|45/61|
|[5x · riesgo5/15](http://localhost:9200/#/backtest/4d1a9bce-c19c-409f-8e70-2f19feebc98a)|47187.72|471.88|39.72|-16.50|2.408|1.672|2.080|242|5571.11|244|43/61|

Frontera retorno/DD con desigualdades exactas del protocolo: L1, L5, M5A15, R5A15. La clasificación exacta puede distinguir centavos o diferencias ínfimas de DD; no convertirla en una recomendación ni tratar3/4/5como evidencia diferente.

### K1001C

|Política / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[1x · riesgo1/8](http://localhost:9200/#/backtest/73f15cb2-09a1-4323-8c63-52cd27c55f8e)|13560.86|135.61|17.87|-7.27|2.458|1.797|2.139|249|1496.64|215|44/61|
|[2x · riesgo1/8](http://localhost:9200/#/backtest/618e93e7-cf95-4e19-8791-b648f77630ce)|13615.82|136.16|17.92|-8.76|2.046|1.641|1.948|249|1835.67|219|45/61|
|[3x · riesgo1/8](http://localhost:9200/#/backtest/71788184-6546-427f-b95a-cc84c09783aa)|13853.51|138.54|18.15|-8.78|2.067|1.645|1.953|249|1873.45|219|44/61|
|[4x · riesgo1/8](http://localhost:9200/#/backtest/79933290-0b34-4858-8b56-d06dd4390564)|13854.28|138.54|18.15|-8.78|2.067|1.646|1.953|249|1873.24|219|44/61|
|[5x · riesgo1/8](http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c)|13854.33|138.54|18.15|-8.78|2.067|1.646|1.953|249|1873.23|219|44/61|
|[5x · margen5/15 + riesgo1/8](http://localhost:9200/#/backtest/8e369187-59bc-4c4d-82bc-ce9f9f63f1f0)|6806.61|68.07|10.47|-6.29|1.664|1.557|1.936|249|742.32|178|45/61|
|[5x · riesgo5/15](http://localhost:9200/#/backtest/8d7d5fdb-85bf-4b17-88d0-e04add0b56d2)|47670.36|476.70|39.94|-17.41|2.294|1.649|2.043|249|5948.62|223|43/61|

Frontera retorno/DD con desigualdades exactas del protocolo: L1, L2, L4, L5, M5A15, R5A15. La clasificación exacta puede distinguir centavos o diferencias ínfimas de DD; no convertirla en una recomendación ni tratar3/4/5como evidencia diferente.

### N204B

|Política / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[1x · riesgo1/8](http://localhost:9200/#/backtest/d28543bd-a2cf-4700-a115-72af4744e582)|12152.57|121.53|16.48|-8.20|2.009|1.637|1.888|273|1583.98|291|44/61|
|[2x · riesgo1/8](http://localhost:9200/#/backtest/7a74ebeb-4af0-4ba4-9914-9e8b93154f61)|12855.35|128.55|17.18|-8.80|1.953|1.575|1.812|273|1891.79|292|44/61|
|[3x · riesgo1/8](http://localhost:9200/#/backtest/55a97e97-a6b2-498b-a01e-d3a6c55cdb8e)|13055.77|130.56|17.38|-8.78|1.980|1.582|1.822|273|1913.03|291|44/61|
|[4x · riesgo1/8](http://localhost:9200/#/backtest/ea844ce6-381d-4c53-a44e-156c2f1a6c3e)|13057.53|130.58|17.38|-8.78|1.980|1.582|1.822|273|1912.96|291|44/61|
|[5x · riesgo1/8](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142)|13056.61|130.57|17.38|-8.78|1.980|1.583|1.822|273|1912.86|291|44/61|
|[5x · margen5/15 + riesgo1/8](http://localhost:9200/#/backtest/bcad9d8e-a126-4eb9-8c39-cd813b29b747)|6334.29|63.34|9.87|-6.31|1.563|1.446|1.751|273|800.36|220|43/61|
|[5x · riesgo5/15](http://localhost:9200/#/backtest/dc5ea1ff-d857-4ba1-94c9-0182553b66f4)|43489.01|434.89|37.94|-17.04|2.227|1.593|1.899|273|5775.06|278|40/61|

Frontera retorno/DD con desigualdades exactas del protocolo: L1, L4, M5A15, R5A15. La clasificación exacta puede distinguir centavos o diferencias ínfimas de DD; no convertirla en una recomendación ni tratar3/4/5como evidencia diferente.

### N204C

|Política / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[1x · riesgo1/8](http://localhost:9200/#/backtest/9c2f2137-2406-4cc2-bf15-d91b486e1950)|12307.77|123.08|16.64|-8.18|2.033|1.658|1.903|280|1596.90|219|45/61|
|[2x · riesgo1/8](http://localhost:9200/#/backtest/26845405-c0ec-4d98-85f1-4134589de8cf)|13011.72|130.12|17.33|-9.47|1.831|1.563|1.800|280|1974.53|220|45/61|
|[3x · riesgo1/8](http://localhost:9200/#/backtest/163e3a1b-6d27-4260-8af6-b343ccb0c8e5)|13239.62|132.40|17.56|-9.06|1.938|1.569|1.805|280|2012.64|219|45/61|
|[4x · riesgo1/8](http://localhost:9200/#/backtest/fc07e888-ebef-45a5-9798-e96fcbec550e)|13237.65|132.38|17.55|-9.06|1.938|1.569|1.805|280|2012.50|219|45/61|
|[5x · riesgo1/8](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794)|13239.44|132.39|17.56|-9.06|1.938|1.570|1.805|280|2012.42|219|45/61|
|[5x · margen5/15 + riesgo1/8](http://localhost:9200/#/backtest/12b18fcc-1835-449f-a5a5-2e9ebef14aaf)|6350.89|63.51|9.89|-6.48|1.527|1.442|1.744|280|820.51|220|42/61|
|[5x · riesgo5/15](http://localhost:9200/#/backtest/47226654-c3b2-443b-bed7-d809580a040c)|43833.92|438.34|38.11|-18.57|2.052|1.570|1.874|280|6120.46|229|39/61|

Frontera retorno/DD con desigualdades exactas del protocolo: L1, L3, M5A15, R5A15. La clasificación exacta puede distinguir centavos o diferencias ínfimas de DD; no convertirla en una recomendación ni tratar3/4/5como evidencia diferente.

## Comportamiento por año
Retornos compuestos desde equity diaria. 2020* comienza15octubre y2025* termina30diciembre (finish exclusivo31diciembre): ambos parciales. No son cohortes de trades cerrados.

### K1001B

|Política|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|L1|3.74%|21.11%|12.19%|19.34%|14.10%|20.22%|
|L2|3.74%|20.90%|12.03%|20.89%|16.58%|18.28%|
|L3|3.74%|20.89%|12.03%|21.41%|17.06%|18.28%|
|L4|3.74%|20.89%|12.03%|21.41%|17.06%|18.28%|
|L5|3.74%|20.89%|12.03%|21.40%|17.06%|18.29%|
|M5A15|3.80%|20.20%|7.30%|7.61%|9.23%|6.52%|
|R5A15|8.26%|60.62%|16.20%|33.09%|37.58%|54.57%|

### K1001C

|Política|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|L1|3.65%|20.36%|12.49%|23.26%|12.93%|20.61%|
|L2|3.66%|18.23%|12.37%|25.36%|16.07%|17.87%|
|L3|3.66%|18.70%|12.38%|25.95%|16.50%|17.57%|
|L4|3.66%|18.70%|12.38%|25.96%|16.50%|17.56%|
|L5|3.66%|18.70%|12.38%|25.96%|16.50%|17.56%|
|M5A15|3.74%|19.67%|7.45%|8.49%|9.21%|6.35%|
|R5A15|7.96%|54.12%|17.15%|42.56%|36.01%|52.59%|

### N204B

|Política|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|L1|4.07%|21.14%|9.39%|17.57%|13.57%|20.30%|
|L2|4.07%|20.96%|10.83%|19.06%|16.19%|18.42%|
|L3|4.07%|20.96%|10.83%|19.57%|16.69%|18.43%|
|L4|4.07%|20.96%|10.83%|19.57%|16.69%|18.44%|
|L5|4.07%|20.95%|10.83%|19.57%|16.69%|18.44%|
|M5A15|4.14%|20.82%|4.90%|6.39%|9.39%|6.34%|
|R5A15|9.89%|62.08%|9.70%|28.67%|39.41%|52.61%|

### N204C

|Política|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|L1|3.98%|20.38%|9.68%|19.69%|12.57%|20.60%|
|L2|3.99%|18.26%|11.18%|23.36%|15.64%|17.98%|
|L3|3.99%|18.72%|11.16%|23.93%|16.15%|17.65%|
|L4|3.98%|18.71%|11.16%|23.93%|16.15%|17.65%|
|L5|3.98%|18.71%|11.16%|23.93%|16.15%|17.66%|
|M5A15|4.05%|20.25%|5.05%|7.23%|9.24%|6.20%|
|R5A15|9.55%|55.62%|10.59%|37.60%|37.69%|50.70%|

## Concentración y reparto de capital
K1001 es rentable en todos los años observados bajo las políticas probadas. A1x supera al ancla en2021/2022/2025*, pero queda por debajo en2023/2024 en ambasB/C: no hay mejora uniforme.
R5A15 aumenta ganancias en varios años. La mayor contribución USDT de2025* también refleja capitalización; no demuestra por sí sola dependencia de una anomalía. Eliminar aritméticamente el mejor mes observado deja neto positivo en todas las28configuraciones; no es un replay de la estrategia ni prueba contra sobreajuste.

### K1001B: extremos mensuales y sensibilidad al mejor mes

|Política|Peor mes %|Mejor mes %|Neto observado sin mejor mes USDT|2025* / neto total USDT %|
|---|---:|---:|---:|---:|
|L1|-3.95|13.09|11229.50|29.68|
|L2|-3.96|14.03|11450.44|26.97|
|L3|-3.96|14.17|11625.61|26.80|
|L4|-3.96|14.17|11625.60|26.80|
|L5|-3.96|14.17|11627.92|26.81|
|M5A15|-3.65|9.16|5723.00|15.17|
|R5A15|-6.39|23.83|41977.71|42.79|

### K1001B: atribución y exposición de referencia

|Política|BTC neto|PAXG neto|SPY neto|Turnover entrada / capital inicial|Nominal entrada ponderado por tiempo / capital inicial|
|---|---:|---:|---:|---:|---:|
|L1|10155.68|1503.38|1415.70|162.34|0.3395|
|L2|9690.91|1928.15|1802.98|194.05|0.4218|
|L3|9735.07|2018.68|1863.15|196.25|0.4336|
|L4|9735.07|2018.68|1863.15|196.25|0.4336|
|L5|9737.23|2018.72|1863.25|196.24|0.4336|
|M5A15|5667.62|694.80|400.79|80.06|0.1454|
|R5A15|27666.28|12501.84|7019.59|617.88|1.6221|

### K1001C: extremos mensuales y sensibilidad al mejor mes

|Política|Peor mes %|Mejor mes %|Neto observado sin mejor mes USDT|2025* / neto total USDT %|
|---|---:|---:|---:|---:|
|L1|-3.94|13.11|11721.37|29.69|
|L2|-5.11|14.02|11684.73|26.30|
|L3|-4.69|14.17|11893.66|25.73|
|L4|-4.69|14.17|11894.43|25.72|
|L5|-4.69|14.17|11894.47|25.72|
|M5A15|-3.66|8.92|5746.97|14.73|
|R5A15|-7.93|23.45|42337.96|41.70|

### K1001C: atribución y exposición de referencia

|Política|BTC neto|PAXG neto|SPY neto|Turnover entrada / capital inicial|Nominal entrada ponderado por tiempo / capital inicial|
|---|---:|---:|---:|---:|---:|
|L1|10094.64|1787.04|1679.18|166.10|0.3821|
|L2|9546.78|2040.41|2028.63|203.75|0.4769|
|L3|9676.71|2079.85|2096.96|207.95|0.4917|
|L4|9677.25|2079.96|2097.07|207.92|0.4917|
|L5|9677.25|2079.95|2097.12|207.92|0.4917|
|M5A15|5665.24|700.04|441.33|82.38|0.1570|
|R5A15|27255.41|12957.34|7457.61|659.76|1.8279|

### N204B: extremos mensuales y sensibilidad al mejor mes

|Política|Peor mes %|Mejor mes %|Neto observado sin mejor mes USDT|2025* / neto total USDT %|
|---|---:|---:|---:|---:|
|L1|-3.82|13.76|10255.16|30.76|
|L2|-3.84|14.69|10805.73|27.65|
|L3|-3.84|14.83|10986.50|27.48|
|L4|-3.84|14.83|10988.26|27.49|
|L5|-3.84|14.83|10987.35|27.49|
|M5A15|-3.41|9.22|5301.24|15.38|
|R5A15|-6.18|24.29|38462.21|42.40|

### N204B: atribución y exposición de referencia

|Política|BTC neto|PAXG neto|SPY neto|Turnover entrada / capital inicial|Nominal entrada ponderado por tiempo / capital inicial|
|---|---:|---:|---:|---:|---:|
|L1|9352.10|1421.54|1378.92|175.82|0.3398|
|L2|9213.64|1869.07|1772.63|210.00|0.4254|
|L3|9265.26|1958.57|1831.95|212.35|0.4370|
|L4|9266.94|1958.58|1832.01|212.35|0.4370|
|L5|9266.17|1958.51|1831.93|212.33|0.4370|
|M5A15|5266.13|671.96|396.21|88.82|0.1490|
|R5A15|24945.69|11825.57|6717.75|640.50|1.5735|

### N204C: extremos mensuales y sensibilidad al mejor mes

|Política|Peor mes %|Mejor mes %|Neto observado sin mejor mes USDT|2025* / neto total USDT %|
|---|---:|---:|---:|---:|
|L1|-3.80|13.75|10419.67|30.96|
|L2|-5.12|14.68|11004.41|26.95|
|L3|-4.69|14.81|11206.64|26.33|
|L4|-4.69|14.82|11204.68|26.34|
|L5|-4.69|14.82|11206.48|26.35|
|M5A15|-3.43|8.99|5318.03|15.03|
|R5A15|-7.93|24.29|38722.72|41.32|

### N204C: atribución y exposición de referencia

|Política|BTC neto|PAXG neto|SPY neto|Turnover entrada / capital inicial|Nominal entrada ponderado por tiempo / capital inicial|
|---|---:|---:|---:|---:|---:|
|L1|9038.23|1666.38|1603.16|177.21|0.3770|
|L2|9065.75|1976.25|1969.73|219.17|0.4783|
|L3|9189.39|2014.75|2035.48|223.40|0.4927|
|L4|9187.73|2014.57|2035.34|223.39|0.4927|
|L5|9189.42|2014.59|2035.43|223.38|0.4927|
|M5A15|5242.61|675.98|432.30|91.05|0.1602|
|R5A15|24596.59|12231.74|7005.59|678.82|1.7630|

La exposición de referencia suma nominal de entrada×duración de cada trade, dividida por duración total×capital inicial; no mide nominal al mark/equity corriente, margen efectivo del exchange ni riesgo al stop. El turnover también usa capital inicial; ambos suben por capitalización. Las cuotas de cada activo y las restricciones de margen hacen que la cartera no sea un mero múltiplo de la original.

## Verificación y límites
24backtests nuevos terminados;4anclas previas terminadas. Configuración ejecutada validada por sesión: leverage solicitado, fee, fechas. Fuentes originales iguales a snapshots antes deA; diez clonesB creados y leídos de vuelta, y auditoría inversa byte por byte limitó cambios a sizing/clase/comentario.
Cuatro análisis finales con7snapshots completos cada uno,7308registros de trades entre políticas (repeticiones, no muestras independientes). Neto de trades/motor reconciliado dentro0.01USDT en las28configuraciones. Identidades de entradas únicas; cero discordancias de entradas y salidas vsancla dentro de cada grupo. Brecha terminal equity/wallet cero en las28; DD calculado de curva coincide con motor salvo redondeo flotante.
Equity1904puntos con mediana86400s. DD y resultados calendario observados tienen resolución diaria; no certifican máxima caída intraminuto. Los campos del motor total_open_trades/open_pl pueden reflejar historia previa aterminate y no deben sumarse de nuevo al neto/curva terminal reconciliados.
B/C comparten precios y gran parte de operaciones: no son muestras independientes. Variantes elegidas sobre un histórico ya explorado; sin prueba estadística de ausencia de sobreajuste. No se estimaron intervalos ni significancias nuevas.
Reserva sizing0.001 no es slippage simulado. Sin funding, liquidez, gaps/fills adversos ni pruebas nuevas de comisiones mayores para estas políticas; no heredan automáticamente los controles de costes previos de K1001 al cambiar sizing. SPY es proxy SPX CFD con calendario heredado, no instrumento nativo certificado.
Las conclusiones son de investigación. No se cambió configuración global (continúa5x/fee0.00045), fuentes originales ni operativa live/paper. 2026 ni se inspeccionó ni se ejecutó.

## Línea siguiente propuesta, no ejecutada
Mantener1x/riesgo1/8 como candidato conservador y3x/riesgo1/8 como réplica económica del histórico5x. El escenario5/15sirve como extremo agresivo. Una fase futura acotada podría probar2%/6% y3%/9% a3x, K1001/N204×B/C (8corridas), fijando antes costes estresados y criterio de selección. No se añaden esas corridas retrospectivamente aesta fase.
Antes de aplicar un cambio de capital: congelar una política, validar sus propios costes/ejecución y obtener evidencia nueva. 2026 sigue cerrado por decisión vigente; abrirlo exigiría autorización explícita y no usarlo después para ajustar parámetros.

## Archivos persistentes en el proyecto Jesse
- CAPITAL_R11_PROTOCOL_20261019.md y CAPITAL_R11_B_PROTOCOL_20261019.md: hipótesis y matrices previas.
- CAPITAL_R11_SESSION_REGISTRY_20261019.md:24sesiones, auditoría config,4análisis finales.
- CAPITAL_R11_B_SOURCE_QA_20261019.md y CAPITAL_R11_B_DIFF_AUDIT_20261019.md:fuentes y cambios.
- CAPITAL_R11_ANALYSIS_SOURCE_20261019.md:código reproducible de análisis.
- CAPITAL_R11_K1001B_DATA_20261019.md, CAPITAL_R11_K1001C_DATA_20261019.md, CAPITAL_R11_N204B_DATA_20261019.md, CAPITAL_R11_N204C_DATA_20261019.md: métricas motor completas, anuales, aportes por activo y todos los meses.
Los gráficos PNG están en los jobs temporales de análisis; no sustituyen los datos persistentes ni se garantiza su conservación tras24h.
