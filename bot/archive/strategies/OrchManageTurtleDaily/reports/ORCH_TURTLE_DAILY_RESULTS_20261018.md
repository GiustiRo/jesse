# Turtle diario simplificado — resultado y atribución
Dashboard: http://localhost:9200/#/backtest/a4a5837e-ed47-4179-82a1-2612fd899d14

## Hipótesis y configuración
Protocolo ORCH_TURTLE_DAILY_PROTOCOL_20261018.md guardado antes del run. Una única receta: cierre rompe canal previo55d, MARKET posterior a confirmación, stop inicial2ATR20 desde fill real, protección ratchet canal10d conocido para el día siguiente. Sin EMA/ADX/RSI/TP/BE/piramidado.
BTC y PAXG, ambos sentidos,1D. Cuenta10kUSDT,5xaislado,riesgo1%poractivo/8%global,gross4.4x con2.2xtechoindividual,margen90%,fee0.00045porlado. Normal replay,warmup40 quecrecehasta56cierres antes de operar. Ventana2020-10-15→2025-12-31exclusivo;2026reservado.
La familia tendencial ya fue explorada: se evalúan simplificación e horizonte distinto, no una ventaja independiente. PAXGSpot es proxy para futuros y no valida shorts/funding nativos.

## Resultado del motor
64 trades:41long y23short. Neto+2321.382480USDT, saldo12321.382480, CAGR4.085133%, DD−8.892327%, Sharpe0.693056, fees140.124184USDT.0posiciones terminales.
La aserción de retención al1nov2020 pasó; primera entrada observada6nov2020 00:00UTC. Ese cash inicial se conserva dentro del período, no se recorta la ventana.
Median holding14.72d. Las dos mayores ganancias suman48.83%delneto y22.72%delgrossprofit: concentración relevante con muestra pequeña.

## Atribución por activo y sentido
| Componente | Trades | NetoUSDT | FeesUSDT | Ganadores | Holding medio |
|---|---:|---:|---:|---:|---:|
| BTC long |23|+1537.44|29.34|9|19.33d|
| BTC short |13|−75.50|12.57|5|15.22d|
| PAXG long |18|+1214.75|64.93|11|22.49d|
| PAXG short |10|−355.31|33.28|2|14.45d|

Longs aportan+2752.19USDT; shorts−430.81USDT. Ambos sentidos se ejecutaron, pero los shorts no aportan una expectativa útil en este control. No seleccionar long-only post hoc sin nueva hipótesis y comparación predeclarada.

## Años por fecha de cierre, NO retornos MTM
2020−66.68;2021+136.03;2022−220.80;2023+783.46;2024+969.20;2025+720.17USDT. Períodos fronterizos2020/25sonparciales; trades abiertos cruzando año pertenecen aquí al cierre, por eso NO es una tabla de rendimiento anual de cartera.

## Costes y validación
Análisis MCPb7955ace718c40e48396a74b6f1581bc verificó PnL y fees por trade y la reconciliación total. Añadir10bps por operación completa a fills/cantidades fijos deja neto+2165.688942USDT. Es diagnóstico de costes, NO nuevoCAGR/DD ni modelo de spread/gaps/funding.
Todas las ejecuciones conservan fuente exacta de la receta. No se instalaron paquetes, importaron datos ni modificaron framework/configglobal/live.

## Decisión
No promover como solución de fase2: retorno modesto al riesgo estudiado,64trades y ambas patas short negativas. No aumentar riesgo para aparentar objetivo, ni barrer55/10/2ATR o añadir filtros después de ver resultados.
El calendario MTM V4 se añade al cierre siguiente; no usar muestras diarias del motor como sustituto. Objetivos65–70%mesesactivos/80%trimestres yDD<=25%siguen vigentes. Referencia y2026intactos.

## Cierre con auditor V4 del orquestador
El auditor por ejecuciones y saldo terminó correctamente; no se repite el análisis.
- Meses activos positivos:24/57=42.1053%.
- Meses positivos sobre calendario completo de la ventana:24/63=38.0952%.
- Trimestres positivos incluidos bordes:12/21=57.1429%.
- Control de meses completos:24/56activos=42.8571%;24/61calendario=39.3443%.
- Control de trimestres completos:11/19=57.8947%.
- Peor mes:−2.06154%; drawdown de cierres diariosUTC:−8.87986%.
Retornos anuales MTM (distintos de PnL por fecha de cierre):2020parcial+3.055%,2021−2.291%,2022−0.877%,2023+6.522%,2024+9.116%,2025parcial+6.208%.
RECHAZO DEFINITIVO como solución de regularidad: no cumple65–70%/80%, sin escalar riesgo ni retirar shorts retrospectivamente. Fuente conservada exacta; no nuevas variantes.
