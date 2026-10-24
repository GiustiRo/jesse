# R36 — reversión semanal de48h: cierre

Las dos políticas pierden dinero después de costos base. La reversión del fin de semana es peor que el comparador entre semana. No hay candidata ni preferencia relativa para WEEKEND.

|Política|Operaciones|Neto USDT|CAGR neto|PF neto|DD M1 y fills|Meses positivos|Trimestres positivos|
|---|---:|---:|---:|---:|---:|---:|---:|
|[MONDAY](http://localhost:9200/#/backtest/cd719c96-0852-4280-9d2c-ae3199041e93)|272|-3581.95|-8.150%|0.657|38.461%|23/62|5/20|
|[THURSDAY](http://localhost:9200/#/backtest/87e47587-dc20-4e9e-8bb9-9f3ce7bed59b)|271|-239.28|-0.463%|0.969|14.796%|34/62|10/20|

MONDAY opera contra el movimiento sábado00→lunes00UTC, con entrada lunes00. THURSDAY revierte martes00→jueves00UTC. Ambos usan48h ya cerradas, MARKET, SL2ATR actual,24hsinTP y cuota1% sobre el mismo capital total10000, resto ocioso. No hay búsqueda de días ni umbral de movimiento elegido por resultado.

El calendario se cumplió exactamente:272slots lunes y271jueves, todos con retorno distinto de cero y todos ejecutados. La diferencia de un slot proviene de START/FINISH jueves00 exclusivos. Sin huecos, invalidación, bloqueo por ocupación o problema de sizing. La recurrencia semanal existió y no produjo la ventaja buscada.

MONDAY pierde incluso antes de costos: bruto−2753.45−fees852.44+funding23.93=neto−3581.95USDT. THURSDAY tiene bruto+410.00, insuficiente para fees705.65, aunque funding aporte+56.37; neto−239.28. No corresponde culpar al funding: contribuyó positivamente en ambas. No se omiten costos conocidos ni se cambia tarifa para fabricar rentabilidad.

Las62 mensualidades completas fueron activas en cada cuenta. Mediana calendario MONDAY−0.59147% y THURSDAY+0.09803%; la segunda no basta para compensar retorno/PF/regularidad insuficientes. Neto aritmético sin los dos mejores meses:−4104.88 y−889.81USDT. MONDAY incumple también el techoDD25%. Ambas sólo acreditanN100 como mínimo operativo, no confianza estadística.

Auditoría completa de543trades y1274pagos: gross−fees+funding=PNL=saldo−10000, órdenes MARKET de entrada, cantidades/riesgo/lote, stops exactos y salida a24h. Salidas MONDAY116STOP y156MARKET; THURSDAY52STOP y219MARKET. SinLIMIT ni posición terminal residual. Fronteras mensuales postfunding y observación M1+fills verificadas; DD no es máximo intraminuto.

Dos motores y cero reruns/reemplazos. Check supplied-sourceb8b68d9ed1724c828787f35c91eec622 PASS94 al primer intento; auditoría de snapshotsd7043b31340043cebaed88f7732580be PASS al primer intento. Padres R10/R11/R16/R32 intactos. Recibos durables:BTC_R36_A_RESULTS_20261022.json, BTC_R36_A_DURABLE_INDEX_20261022.json yBTC_R36_UNIVERSE_CHECK_20261022.json. Revisión interpretativa independiente completa en BTC_R36_A_INDEPENDENT_INTERPRETATIVE_REVIEW_20261022.md; leyó ambos JSON durables completos y no repitió la auditoría por fill.

Ventana BTC-USDT Binance Perpetual Futures[2020-10-15,2026-01-01), historia observada/adaptativa, sin OOS nuevo o economía2026. Fee taker con descuento.00045porlado y funding histórico aplicado;3xaislado, reserva.001 sólo sizing, slippage modelado0. No suma de cuentas, cartera, estrés o variación de riesgo.

El contraste describe políticas completas con distintos días y trayectorias; no identifica una causa de liquidez ni prueba que todo movimiento del fin de semana revierta o continúe. Las pérdidas tampoco acreditan rentabilidad de invertir la dirección: stops, vencimiento, costos y funding impiden negar algebraicamente el PnL. Cambiar signo, día, ventana o plazo tras este resultado violaría el cierre previamente fijado.

Decisión: NO_CUMPLE en ambas cuentas. Cerrar esta comparación y conservar su evidencia, sin convertir la frecuencia en argumento para promoción.
