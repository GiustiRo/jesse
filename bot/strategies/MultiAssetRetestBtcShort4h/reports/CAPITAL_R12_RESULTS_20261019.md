# R12 — Combinaciones de riesgo y apalancamiento
Estudio concluido el 2026-10-19: 28 corridas nuevas y 12 anclas previas, 40 configuraciones comparadas. Investigación autorizada por el usuario. K1001 sigue candidata provisional; N204 conserva su función de referencia.

## Qué cambia para una cartera de 10.000 USDT
En las fuentes multiactivo verificadas, el perfil original es riesgo objetivo 1% por operación y límite agregado 8%, no 1% de margen. No se inspeccionó la configuración live; la decisión antigua de DOCS sobre 2% de BTC no cambia las constantes verificadas de este estudio.

|Perfil|Presupuesto inicial por operación al stop|Límite agregado de admisión|Tres entradas nuevas al objetivo, aproximadamente|
|---|---:|---:|---:|
|Original 1% / 8%|100 USDT|800 USDT|300 USDT|
|Intermedio 2% / 6%|200 USDT|600 USDT|600 USDT|
|Mayor exposición 3% / 9%|300 USDT|900 USDT|900 USDT|

Son objetivos estimados, no pérdidas máximas garantizadas ante gaps o slippage. El agregado se mide desde mark a stop, con costes y reservas pendientes; puede variar después. El stop técnico no se aleja: se cambia la cantidad, sujeta a margen, cap nominal y cuota por activo.
Ejemplo sin costes: stop a 2% del precio y presupuesto de pérdida de 200 USDT requieren nominal aproximado de 10.000 USDT; a 3x el margen inicial sería unos 3.333 USDT. No significa invertir sólo 200 USDT ni multiplicar nuevamente 2% por 3. Tres activos comparten el presupuesto de la misma cuenta.
Los porcentajes se recalculan sobre max(0,min(wallet,equity)): al bajar la cuenta a 9.000, 2% son 180; al subir a 11.000, 220, antes de límites de capacidad. Las ganancias flotantes no agrandan la base y las pérdidas flotantes la reducen.
No se aplicó un cambio operativo. Son perfiles candidatos de investigación, no una nueva asignación live elegida automáticamente.

## Hallazgos principales
- K1001 mejora retorno nominal y DD frente a N204 en las cuatro combinaciones nuevas y ambas carteras. Con fee estresado conserva más retorno, pero no siempre menor DD: por ejemplo 2%/6% B, K1001 -14.59% vs N204 -14.03%.
- A 3x, el perfil K1001 2%/6% produce 33.85–34.66% anual compuesto con DD 13.34–13.82%; bajo fee estresado conserva 26.50–26.92% con DD 14.54–14.59%.
- A 3x, el perfil K1001 3%/9% produce 38.87–39.53% anual con DD 14.71–15.67%; en estrés conserva 31.50–31.90% con DD 15.86–16.32%.
- El perfil 3%/9% a 3x mejora Calmar frente al 2%/6% a 3x en B/C, nominal y estrés. No tiene el menor DD ni el mayor Sharpe nominal. El perfil 2%/6% a 1x tiene mayor Sharpe nominal entre estas configuraciones en B/C, pero sólo se probó nominalmente a 1x.
- En C, 2%/6% a 3x mejora retorno y DD frente a 3%/9% a 1x; sucede también en B. No es necesario aumentar el porcentaje por trade para mejorar esa combinación.
- Los nuevos perfiles a 3x mejoran retorno, Calmar y PF frente al original a 3x bajo el mismo fee. Eso no elimina el coste de mayor DD absoluto. El original 1% a 1x sigue ofreciendo una alternativa de menor caída.
- No mejora toda medida de regularidad: por ejemplo K1001 B 2%/6% a 3x tiene 46/61 meses positivos nominales vs 43/61 del original, pero en estrés 38/61 vs 40/61. C tiene 44/61 vs 44/61 nominal y 40/61 vs 41/61 en estrés.
- En todos los grupos, cambiar perfil de riesgo a igual fee/leverage conserva las entradas y salidas. La comisión mayor sí cambia registros frente al ancla nominal; no equivale a restar un coste fijo sobre fills idénticos.

## Diseño reproducible y límites de la comparación
Matriz congelada antes de los resultados: 16 nominales = 2%/6% y 3%/9% × 1x/3x × K1001/N204 × B/C; fee 0.00045 por lado. 12 estrés = 1%/8%, 2%/6%, 3%/9% × 3x × K1001/N204 × B/C; fee 0.00095 por lado. Se ensayaron todos los perfiles previstos bajo estrés, sin selección adaptativa.
Ventana 2020-10-15 inclusiva a 2025-12-31 exclusiva. Capital inicial compartido 10.000 USDT; Binance Perpetual Futures; BTC/PAXG/SPY 4h y tres feeds 1m; warmup 240; fast_mode false; debug true; benchmark false. Orden BTC/PAXG/SPY, B=SPY Second y C=SPY Market, horarios heredados.
Fuentes clonadas sólo cambian clase/comentario y constantes de riesgo. Cap nominal 4.4, pesos inversos ATR, margen disponible ×0.90 y reserva de sizing 0.001 idénticos. Stops, objetivos y relojes iguales. Los perfiles cambian simultáneamente presupuesto por operación y agregado: no se aísla causalmente sólo el primer porcentaje.
A 1x puede no alcanzarse el riesgo objetivo por falta de margen. A 3x también pueden limitar nominal y cuotas. No se corrieron perfiles 2%/3% a 5x: la meseta 3x–5x de R11 correspondía a riesgo 1% y no se extrapola sin pruebas.
Estrés ejecutado en el motor: mayor fee cambia sizing y reglas dependientes de fee, incluyendo protección de PAXG. No representa slippage, liquidez ni funding. No hay prueba estresada propia para los perfiles nuevos a 1x.
2026 continúa cerrado, incluso inspección. Se reutiliza histórico de desarrollo explorado; no es OOS ni prueba de ausencia de sobreajuste.

## Todas las métricas comparables
CAGR y retorno en %; DD diario negativo. Underwater = días según motor. Meses positivos sobre 61 meses completos, con meses sin operaciones incluidos; 2020-10 y 2025-12 se excluyen de ese denominador.

### K1001B

|Perfil / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[Original 1%/8% · 1x](http://localhost:9200/#/backtest/141760eb-4fbc-4832-915c-87cb417931d6)|13074.77|130.75|17.40|-7.38|2.359|1.754|2.101|242|1462.53|278|45/61|
|[Original 1%/8% · 3x](http://localhost:9200/#/backtest/065ff012-e01f-47fc-a043-b21404d65bbd)|13616.90|136.17|17.92|-8.82|2.031|1.656|1.976|242|1767.99|291|43/61|
|[Original 1%/8% · 5x](http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a)|13619.21|136.19|17.92|-8.82|2.031|1.656|1.976|242|1767.92|291|43/61|
|[1%/8% · 3x · fee95](http://localhost:9200/#/backtest/6e33a5ce-4830-47fc-aa83-a6b1f7be76d5)|9697.62|96.98|13.89|-9.30|1.494|1.374|1.748|242|3218.87|292|40/61|
|[2%/6% · 1x](http://localhost:9200/#/backtest/3405bf14-a0af-408a-814b-c6072c6da785)|24942.19|249.42|27.12|-13.90|1.951|1.764|2.169|242|2508.35|215|43/61|
|[2%/6% · 3x](http://localhost:9200/#/backtest/b9f0cccc-8de0-4076-a7fa-eb9ae8e1be38)|35727.07|357.27|33.85|-13.34|2.537|1.743|2.058|242|4379.33|278|46/61|
|[2%/6% · 3x · fee95](http://localhost:9200/#/backtest/bb6e80f2-36f1-4c8f-8c8c-cac840794b8c)|24064.34|240.64|26.50|-14.59|1.817|1.442|1.786|242|7794.13|291|38/61|
|[3%/9% · 1x](http://localhost:9200/#/backtest/ba7fe481-0248-4be6-936d-dc5bcc74c096)|29016.75|290.17|29.84|-15.72|1.898|1.751|2.163|242|2886.99|215|43/61|
|[3%/9% · 3x](http://localhost:9200/#/backtest/6275ee04-32ec-42b8-811f-b7d7f2b8a735)|45392.03|453.92|38.87|-14.71|2.643|1.738|2.090|242|5351.59|278|44/61|
|[3%/9% · 3x · fee95](http://localhost:9200/#/backtest/b76983f3-2ce8-4b3c-8261-1af29fdfa937)|31695.23|316.95|31.50|-15.86|1.987|1.461|1.823|242|9788.03|291|39/61|

### K1001B: efecto de fee mayor a 3x

|Perfil|CAGR nominal|CAGR estrés|Delta puntos anuales|DD nominal|DD estrés|Calmar nominal / estrés|
|---|---:|---:|---:|---:|---:|---:|
|1%/8%|17.92|13.89|-4.03|-8.82|-9.30|2.031 / 1.494|
|2%/6%|33.85|26.50|-7.35|-13.34|-14.59|2.537 / 1.817|
|3%/9%|38.87|31.50|-7.36|-14.71|-15.86|2.643 / 1.987|

### K1001B: retornos por año

2020* comienza el 15 de octubre y 2025* termina el 30 de diciembre; ambos parciales. Retornos de equity diaria, no cohortes de trades cerrados.

|Perfil|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|Original 1%/8% · 1x|3.74%|21.11%|12.19%|19.34%|14.10%|20.22%|
|Original 1%/8% · 3x|3.74%|20.89%|12.03%|21.41%|17.06%|18.28%|
|Original 1%/8% · 5x|3.74%|20.89%|12.03%|21.40%|17.06%|18.29%|
|1%/8% · 3x · fee95|3.30%|18.77%|10.02%|18.00%|13.54%|8.92%|
|2%/6% · 1x|5.45%|39.46%|18.25%|25.49%|25.52%|27.57%|
|2%/6% · 3x|7.33%|49.38%|17.41%|32.86%|33.83%|36.61%|
|2%/6% · 3x · fee95|6.34%|43.78%|14.86%|29.38%|27.59%|17.50%|
|3%/9% · 1x|5.85%|52.22%|21.05%|24.47%|27.53%|26.03%|
|3%/9% · 3x|9.29%|63.81%|17.05%|31.37%|35.70%|48.28%|
|3%/9% · 3x · fee95|8.19%|60.10%|14.24%|27.69%|30.60%|26.35%|

### K1001B: concentración mensual y reparto por activo

Restar el mejor mes es una sensibilidad aritmética; no una simulación sin ese mes. Exposición de referencia: suma de nominal de entrada × duración, dividida por (capital inicial × duración del estudio); no nominal mark/equity ni riesgo al stop.

|Perfil|Peor mes %|Mejor mes %|Neto observado sin mejor mes|BTC neto|PAXG neto|SPY neto|Exposición referencia|
|---|---:|---:|---:|---:|---:|---:|---:|
|L1|-3.95|13.09|11229.50|10155.68|1503.38|1415.70|0.3395|
|L3|-3.96|14.17|11625.61|9735.07|2018.68|1863.15|0.4336|
|L5|-3.96|14.17|11627.92|9737.23|2018.72|1863.25|0.4336|
|R1A8_L3_F95|-4.02|13.72|7845.58|7832.19|492.13|1373.30|0.3646|
|R2A6_L1|-6.72|18.62|21363.97|19883.35|3230.74|1828.10|0.5584|
|R2A6_L3|-6.41|22.55|31481.68|23609.71|6673.25|5444.11|1.1921|
|R2A6_L3_F95|-6.54|23.35|19963.84|18775.17|1493.20|3795.97|0.9659|
|R3A9_L1|-6.74|23.74|24408.74|23734.69|3271.58|2010.48|0.6362|
|R3A9_L3|-6.38|23.67|40121.79|29242.37|9386.37|6763.30|1.5007|
|R3A9_L3_F95|-6.61|23.54|27104.10|23972.49|2554.47|5168.26|1.2674|

### K1001C

|Perfil / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[Original 1%/8% · 1x](http://localhost:9200/#/backtest/73f15cb2-09a1-4323-8c63-52cd27c55f8e)|13560.86|135.61|17.87|-7.27|2.458|1.797|2.139|249|1496.64|215|44/61|
|[Original 1%/8% · 3x](http://localhost:9200/#/backtest/71788184-6546-427f-b95a-cc84c09783aa)|13853.51|138.54|18.15|-8.78|2.067|1.645|1.953|249|1873.45|219|44/61|
|[Original 1%/8% · 5x](http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c)|13854.33|138.54|18.15|-8.78|2.067|1.646|1.953|249|1873.23|219|44/61|
|[1%/8% · 3x · fee95](http://localhost:9200/#/backtest/060c9265-5529-42e1-90c6-1136b55d5c92)|9756.42|97.56|13.95|-9.29|1.502|1.356|1.724|249|3388.81|219|41/61|
|[2%/6% · 1x](http://localhost:9200/#/backtest/59a2a153-3875-4e49-810b-c075d8b44f18)|26361.50|263.61|28.10|-12.86|2.184|1.832|2.235|249|2577.47|173|43/61|
|[2%/6% · 3x](http://localhost:9200/#/backtest/3ec33cac-3ea6-43c7-9cfe-4d315930fee2)|37184.83|371.85|34.66|-13.82|2.508|1.755|2.056|249|4666.53|215|44/61|
|[2%/6% · 3x · fee95](http://localhost:9200/#/backtest/ac57b4d3-cfeb-4add-88cb-19358d701db1)|24652.00|246.52|26.92|-14.54|1.851|1.443|1.775|249|8217.90|223|40/61|
|[3%/9% · 1x](http://localhost:9200/#/backtest/c7294fba-ec55-4911-bf33-ce9de2efc60e)|30710.61|307.11|30.90|-14.70|2.102|1.820|2.229|249|2966.78|211|43/61|
|[3%/9% · 3x](http://localhost:9200/#/backtest/d4a39027-b4d0-4c0c-8396-d9222c3af8ef)|46797.80|467.98|39.53|-15.67|2.523|1.734|2.083|249|5684.11|261|43/61|
|[3%/9% · 3x · fee95](http://localhost:9200/#/backtest/1ee8889e-4415-4f9f-98e9-d7c5334d258f)|32348.16|323.48|31.90|-16.32|1.954|1.453|1.812|249|10323.92|264|40/61|

### K1001C: efecto de fee mayor a 3x

|Perfil|CAGR nominal|CAGR estrés|Delta puntos anuales|DD nominal|DD estrés|Calmar nominal / estrés|
|---|---:|---:|---:|---:|---:|---:|
|1%/8%|18.15|13.95|-4.19|-8.78|-9.29|2.067 / 1.502|
|2%/6%|34.66|26.92|-7.74|-13.82|-14.54|2.508 / 1.851|
|3%/9%|39.53|31.90|-7.64|-15.67|-16.32|2.523 / 1.954|

### K1001C: retornos por año

2020* comienza el 15 de octubre y 2025* termina el 30 de diciembre; ambos parciales. Retornos de equity diaria, no cohortes de trades cerrados.

|Perfil|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|Original 1%/8% · 1x|3.65%|20.36%|12.49%|23.26%|12.93%|20.61%|
|Original 1%/8% · 3x|3.66%|18.70%|12.38%|25.95%|16.50%|17.57%|
|Original 1%/8% · 5x|3.66%|18.70%|12.38%|25.96%|16.50%|17.56%|
|1%/8% · 3x · fee95|3.21%|16.65%|10.26%|21.74%|13.00%|8.19%|
|2%/6% · 1x|5.26%|40.30%|19.54%|29.00%|24.73%|28.02%|
|2%/6% · 3x|7.14%|45.54%|18.10%|42.07%|32.47%|36.13%|
|2%/6% · 3x · fee95|6.19%|39.63%|15.38%|37.33%|26.26%|16.81%|
|3%/9% · 1x|5.60%|53.24%|22.55%|27.86%|27.00%|26.42%|
|3%/9% · 3x|9.05%|58.53%|18.03%|40.50%|34.09%|47.75%|
|3%/9% · 3x · fee95|7.93%|54.68%|15.01%|36.14%|28.85%|25.73%|

### K1001C: concentración mensual y reparto por activo

Restar el mejor mes es una sensibilidad aritmética; no una simulación sin ese mes. Exposición de referencia: nominal de entrada × duración / capital inicial × duración del estudio; no nominal mark/equity ni riesgo al stop.

|Perfil|Peor mes %|Mejor mes %|Neto observado sin mejor mes|BTC neto|PAXG neto|SPY neto|Exposición referencia|
|---|---:|---:|---:|---:|---:|---:|---:|
|L1|-3.94|13.11|11721.37|10094.64|1787.04|1679.18|0.3821|
|L3|-4.69|14.17|11893.66|9676.71|2079.85|2096.96|0.4917|
|L5|-4.69|14.17|11894.47|9677.25|2079.95|2097.12|0.4917|
|R1A8_L3_F95|-4.76|13.73|7933.95|7758.78|523.34|1474.30|0.4112|
|R2A6_L1|-6.38|17.99|22655.53|20270.98|3783.79|2306.73|0.6224|
|R2A6_L3|-7.87|22.55|32951.45|23376.87|7561.02|6246.94|1.3759|
|R2A6_L3_F95|-8.40|23.36|20655.57|18410.93|1984.97|4256.10|1.1038|
|R3A9_L1|-6.40|23.26|25911.11|24269.18|3869.09|2572.34|0.7074|
|R3A9_L3|-7.51|22.55|41384.16|28925.06|10481.96|7390.79|1.7127|
|R3A9_L3_F95|-7.96|23.21|27737.52|23514.63|3370.92|5462.62|1.4432|

### N204B

|Perfil / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[Original 1%/8% · 1x](http://localhost:9200/#/backtest/d28543bd-a2cf-4700-a115-72af4744e582)|12152.57|121.53|16.48|-8.20|2.009|1.637|1.888|273|1583.98|291|44/61|
|[Original 1%/8% · 3x](http://localhost:9200/#/backtest/55a97e97-a6b2-498b-a01e-d3a6c55cdb8e)|13055.77|130.56|17.38|-8.78|1.980|1.582|1.822|273|1913.03|291|44/61|
|[Original 1%/8% · 5x](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142)|13056.61|130.57|17.38|-8.78|1.980|1.583|1.822|273|1912.86|291|44/61|
|[1%/8% · 3x · fee95](http://localhost:9200/#/backtest/d0939481-e9db-4dd1-b53f-82d1e745b54a)|8979.66|89.80|13.08|-9.29|1.407|1.279|1.611|273|3463.31|328|41/61|
|[2%/6% · 1x](http://localhost:9200/#/backtest/5f31bbbe-872c-49d7-9d63-c992771c9f7b)|22947.45|229.47|25.70|-15.09|1.703|1.643|1.925|273|2715.69|215|43/61|
|[2%/6% · 3x](http://localhost:9200/#/backtest/c7c06f37-6fc6-41b5-8b64-9314e34461ab)|33646.45|336.46|32.66|-13.38|2.442|1.667|1.883|273|4638.39|287|43/61|
|[2%/6% · 3x · fee95](http://localhost:9200/#/backtest/114d7db9-f127-4a64-863c-f4d7fd0f3e3b)|22034.26|220.34|25.02|-14.03|1.783|1.353|1.642|273|8202.34|292|42/61|
|[3%/9% · 1x](http://localhost:9200/#/backtest/3afd86a4-ef01-40e9-a749-7ca3e43155cb)|25991.37|259.91|27.84|-16.83|1.654|1.611|1.904|273|3076.10|313|41/61|
|[3%/9% · 3x](http://localhost:9200/#/backtest/96ac79af-34c5-438c-8470-303d6f7cbf56)|42095.36|420.95|37.24|-15.63|2.383|1.654|1.900|273|5605.46|278|42/61|
|[3%/9% · 3x · fee95](http://localhost:9200/#/backtest/40c9f1d1-891c-4bca-9a22-a77a2ff4fda8)|28422.15|284.22|29.46|-16.15|1.824|1.363|1.665|273|10133.14|292|41/61|

### N204B: efecto de fee mayor a 3x

|Perfil|CAGR nominal|CAGR estrés|Delta puntos anuales|DD nominal|DD estrés|Calmar nominal / estrés|
|---|---:|---:|---:|---:|---:|---:|
|1%/8%|17.38|13.08|-4.30|-8.78|-9.29|1.980 / 1.407|
|2%/6%|32.66|25.02|-7.64|-13.38|-14.03|2.442 / 1.783|
|3%/9%|37.24|29.46|-7.78|-15.63|-16.15|2.383 / 1.824|

### N204B: retornos por año

2020* comienza el 15 de octubre y 2025* termina el 30 de diciembre; ambos parciales. Retornos de equity diaria, no cohortes de trades cerrados.

|Perfil|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|Original 1%/8% · 1x|4.07%|21.14%|9.39%|17.57%|13.57%|20.30%|
|Original 1%/8% · 3x|4.07%|20.96%|10.83%|19.57%|16.69%|18.43%|
|Original 1%/8% · 5x|4.07%|20.95%|10.83%|19.57%|16.69%|18.44%|
|1%/8% · 3x · fee95|3.57%|18.62%|8.49%|15.73%|13.10%|8.78%|
|2%/6% · 1x|6.06%|41.38%|12.28%|21.64%|26.09%|27.58%|
|2%/6% · 3x|7.97%|51.36%|13.56%|28.76%|34.74%|35.56%|
|2%/6% · 3x · fee95|6.98%|45.64%|10.59%|24.65%|28.23%|16.33%|
|3%/9% · 1x|6.11%|53.55%|13.46%|20.34%|28.77%|25.64%|
|3%/9% · 3x|10.26%|65.66%|11.83%|27.00%|37.40%|46.16%|
|3%/9% · 3x · fee95|9.12%|61.45%|8.46%|22.66%|32.06%|24.14%|

### N204B: concentración mensual y reparto por activo

Restar el mejor mes es una sensibilidad aritmética; no una simulación sin ese mes. Exposición de referencia: nominal de entrada × duración / capital inicial × duración del estudio; no nominal mark/equity ni riesgo al stop.

|Perfil|Peor mes %|Mejor mes %|Neto observado sin mejor mes|BTC neto|PAXG neto|SPY neto|Exposición referencia|
|---|---:|---:|---:|---:|---:|---:|---:|
|L1|-3.82|13.76|10255.16|9352.10|1421.54|1378.92|0.3398|
|L3|-3.84|14.83|10986.50|9265.26|1958.57|1831.95|0.4370|
|L5|-3.84|14.83|10987.35|9266.17|1958.51|1831.93|0.4370|
|R1A8_L3_F95|-3.92|14.28|7075.77|7178.14|459.64|1341.88|0.3654|
|R2A6_L1|-6.71|18.70|19573.15|18210.67|2974.17|1762.61|0.5546|
|R2A6_L3|-6.11|23.41|29301.83|21996.98|6366.29|5283.17|1.1785|
|R2A6_L3_F95|-6.37|24.14|17874.93|17027.13|1346.44|3660.69|0.9485|
|R3A9_L1|-6.74|23.68|21716.91|21157.24|2928.76|1905.37|0.6211|
|R3A9_L3|-6.16|23.77|36986.01|26689.95|8905.21|6500.20|1.4672|
|R3A9_L3_F95|-6.48|23.99|23838.91|21197.30|2307.06|4917.80|1.2247|

### N204C

|Perfil / sesión|Neto USDT|Retorno %|CAGR %|DD %|Calmar|Sharpe|PF|Trades|Fees USDT|Underwater días|Meses +/61|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[Original 1%/8% · 1x](http://localhost:9200/#/backtest/9c2f2137-2406-4cc2-bf15-d91b486e1950)|12307.77|123.08|16.64|-8.18|2.033|1.658|1.903|280|1596.90|219|45/61|
|[Original 1%/8% · 3x](http://localhost:9200/#/backtest/163e3a1b-6d27-4260-8af6-b343ccb0c8e5)|13239.62|132.40|17.56|-9.06|1.938|1.569|1.805|280|2012.64|219|45/61|
|[Original 1%/8% · 5x](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794)|13239.44|132.39|17.56|-9.06|1.938|1.570|1.805|280|2012.42|219|45/61|
|[1%/8% · 3x · fee95](http://localhost:9200/#/backtest/f07e991a-b0f7-4732-9429-588a363db730)|8985.74|89.86|13.08|-9.30|1.407|1.258|1.592|280|3622.80|220|41/61|
|[2%/6% · 1x](http://localhost:9200/#/backtest/3facca20-4692-4e98-a5b0-d74aa19db442)|23752.54|237.53|26.28|-14.06|1.869|1.693|1.962|280|2752.53|215|42/61|
|[2%/6% · 3x](http://localhost:9200/#/backtest/436b001f-2868-44cc-890e-77d62e7a6397)|35025.68|350.26|33.46|-15.00|2.231|1.679|1.888|280|4913.48|220|43/61|
|[2%/6% · 3x · fee95](http://localhost:9200/#/backtest/3dbe6a72-a7e8-40d6-b773-e3c2434567f0)|22494.18|224.94|25.36|-15.66|1.619|1.353|1.637|280|8581.17|228|42/61|
|[3%/9% · 1x](http://localhost:9200/#/backtest/e9b7245c-5c62-4095-94ee-4a6dc8121298)|27028.24|270.28|28.54|-15.84|1.802|1.664|1.943|280|3122.26|289|41/61|
|[3%/9% · 3x](http://localhost:9200/#/backtest/31673d52-b6c6-4d93-9b33-8ad637d55345)|43283.89|432.84|37.84|-16.83|2.247|1.650|1.900|280|5908.33|229|41/61|
|[3%/9% · 3x · fee95](http://localhost:9200/#/backtest/19ceeb99-958e-4dd9-94ad-7e8f0166e447)|28957.54|289.58|29.80|-17.46|1.707|1.356|1.660|280|10615.73|283|40/61|

### N204C: efecto de fee mayor a 3x

|Perfil|CAGR nominal|CAGR estrés|Delta puntos anuales|DD nominal|DD estrés|Calmar nominal / estrés|
|---|---:|---:|---:|---:|---:|---:|
|1%/8%|17.56|13.08|-4.47|-9.06|-9.30|1.938 / 1.407|
|2%/6%|33.46|25.36|-8.09|-15.00|-15.66|2.231 / 1.619|
|3%/9%|37.84|29.80|-8.04|-16.83|-17.46|2.247 / 1.707|

### N204C: retornos por año

2020* comienza el 15 de octubre y 2025* termina el 30 de diciembre; ambos parciales. Retornos de equity diaria, no cohortes de trades cerrados.

|Perfil|2020*|2021|2022|2023|2024|2025*|
|---|---:|---:|---:|---:|---:|---:|
|Original 1%/8% · 1x|3.98%|20.38%|9.68%|19.69%|12.57%|20.60%|
|Original 1%/8% · 3x|3.99%|18.72%|11.16%|23.93%|16.15%|17.65%|
|Original 1%/8% · 5x|3.98%|18.71%|11.16%|23.93%|16.15%|17.66%|
|1%/8% · 3x · fee95|3.49%|16.45%|8.72%|19.33%|12.43%|8.00%|
|2%/6% · 1x|5.84%|42.20%|13.53%|23.13%|25.34%|27.99%|
|2%/6% · 3x|7.81%|47.52%|14.23%|37.46%|33.45%|35.12%|
|2%/6% · 3x · fee95|6.79%|41.36%|11.08%|32.12%|26.82%|15.65%|
|3%/9% · 1x|5.84%|54.77%|14.85%|21.76%|28.25%|26.04%|
|3%/9% · 3x|9.99%|60.33%|12.72%|35.60%|35.74%|45.64%|
|3%/9% · 3x · fee95|8.89%|56.04%|9.19%|30.56%|30.22%|23.52%|

### N204C: concentración mensual y reparto por activo

Restar el mejor mes es una sensibilidad aritmética; no una simulación sin ese mes. Exposición de referencia: nominal de entrada × duración / capital inicial × duración del estudio; no nominal mark/equity ni riesgo al stop.

|Perfil|Peor mes %|Mejor mes %|Neto observado sin mejor mes|BTC neto|PAXG neto|SPY neto|Exposición referencia|
|---|---:|---:|---:|---:|---:|---:|---:|
|L1|-3.80|13.75|10419.67|9038.23|1666.38|1603.16|0.3770|
|L3|-4.69|14.81|11206.64|9189.39|2014.75|2035.48|0.4927|
|L5|-4.69|14.82|11206.48|9189.42|2014.59|2035.43|0.4927|
|R1A8_L3_F95|-4.74|14.30|7112.60|7079.37|488.33|1418.03|0.4096|
|R2A6_L1|-5.90|17.99|20294.40|18149.38|3440.56|2162.61|0.6082|
|R2A6_L3|-7.86|23.41|30773.57|21831.15|7220.74|5973.78|1.3530|
|R2A6_L3_F95|-8.39|24.14|18445.79|16664.49|1812.60|4017.09|1.0757|
|R3A9_L1|-5.90|23.20|22645.29|21226.34|3434.27|2367.62|0.6802|
|R3A9_L3|-7.52|23.40|38050.47|26371.29|9932.05|6980.54|1.6631|
|R3A9_L3_F95|-7.95|23.99|24507.42|20800.51|3078.12|5078.91|1.3856|

## Interpretación temporal
No hay mejora uniforme por año al subir del 2% al 3%: en K1001 B a 3x, 2022 baja de 17.41% a 17.05% y 2023 de 32.86% a 31.37%; en C, 2022 baja de 18.10% a 18.03% y 2023 de 42.07% a 40.50%. Aumenta especialmente el rendimiento de 2021 y 2025 parcial. La capitalización también concentra más PnL nominal en los últimos años.
Todos los perfiles quedan con neto observado positivo tras restar su mejor mes. Es robustez descriptiva de concentración, no evidencia estadística independiente ni prueba contra selección histórica.
A 3x, los dos perfiles nuevos pasan las puertas descriptivas de neto positivo, PF>=1.2 y DD no peor que -25% en B/C y fee nominal/estresado. Esos umbrales son los previos del proyecto; no constituyen promoción OOS. Todas las 40 configuraciones analizadas pasan esas puertas, por lo que no bastan para elegir entre ellas.

## Auditoría
28 nuevas sesiones terminadas; overrides de leverage, fee y fechas comprobados individualmente. Diez clones leídos de vuelta e inversión exacta de cambios contra las fuentes originales. Sólo riesgo/clase/comentario cambian.
Cuatro análisis con diez snapshots completos cada uno: 10440 registros de trades entre configuraciones repetidas, no muestras independientes. PnL de trades reconciliado con motor a 0.01 USDT; equity terminal igual a wallet terminal en las 40 configuraciones. Identidad única de entradas; cero diferencias de entradas y de tiempos/precios de salida al comparar perfiles con original a igual fee y leverage.
En K1001 B/C el cambio de fee produce una entrada retirada y una nueva, y cuatro salidas distintas entre entradas comunes respecto del ancla nominal L5, consistentemente en los tres perfiles de riesgo. Son registros, no casos independientes. La comparación igual-fee confirma que el cambio de capital no agrega esas discordancias.
Curvas con 1904 puntos y mediana 86400 segundos; DD de curva coincide con motor salvo redondeo. No se mide DD intraminuto. Campos total_open_trades/open_pl del motor pueden ser anteriores a liquidación final y no deben sumarse nuevamente al neto reconciliado.
B/C comparten muestra y operaciones; no se suman como evidencia independiente. No se calcularon intervalos ni significancia ajustada por búsquedas anteriores.
Configuración global verificada al final: 5x y fee0.00045, sin cambios. No se modificó live/paper ni se ejecutó 2026. El proxy SPY/SPX y su calendario heredado siguen sin certificar paridad con un instrumento nativo.

## Candidatos para continuar, sin cambio operativo
- Opción defensiva ya conocida: original 1% a 1x; menor DD a costa de menor retorno.
- Paso intermedio: 2%/6%. A 1x encaja en 27–28% anual nominal y tiene el mayor Sharpe nominal entre estos casos; requiere su propio estrés antes de preferirla. A 3x tiene validación de fee propia y mayor retorno, con mayor DD en C pero menor en B que su versión 1x.
- Más exposición: 3%/9% a 3x. Mayor CAGR y Calmar que 2%/6% a 3x, nominal y estrés, con DD más alto. No es automáticamente la mejor opción si se prioriza reducir caídas.
Para una transición prudente de presupuesto, el perfil 2% permite explicar y controlar el paso de 100 a 200 USDT iniciales por operación. El perfil 3% queda separado como alternativa de mayor exposición; no se elige por defecto para operar.
Antes de una decisión operativa, congelar política y criterio de aceptación y obtener validación nueva. El siguiente estudio no debería seguir multiplicando combinaciones sobre el mismo histórico; podría completar estrés propio de 2% a 1x o preparar una comparación confirmatoria. 2026 sigue reservado y no se abre sin autorización explícita.

## Evidencia persistente en el proyecto Jesse
- CAPITAL_R12_PROTOCOL_20261019.md: hipótesis, matriz y criterios previos.
- CAPITAL_R12_SOURCE_QA_20261019.md: diez fuentes completas y auditoría.
- CAPITAL_R12_SESSION_REGISTRY_20261019.md: 28 sesiones, 12 anclas, auditoría de configuración y cuatro jobs.
- CAPITAL_R12_ANALYSIS_SOURCE_20261019.md: código reproducible de análisis.
- CAPITAL_R12_K1001B_DATA_20261019.md, CAPITAL_R12_K1001C_DATA_20261019.md, CAPITAL_R12_N204B_DATA_20261019.md, CAPITAL_R12_N204C_DATA_20261019.md: métricas completas del motor, anuales, atribución y todos los meses.
Gráficos PNG temporales en los cuatro jobs de análisis; los datos anteriores permanecen guardados aunque esos workspaces expiren.
