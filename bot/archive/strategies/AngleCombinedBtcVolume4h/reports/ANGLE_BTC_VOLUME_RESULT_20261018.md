# Resultado: filtro de volumen BTC en la combinada
Fecha: 2026-10-18. Estado: RECETA DESCARTADA. No se abre rejilla de medianas, períodos ni horarios.

[Dashboard de la corrida](http://localhost:9200/#/backtest/fabf8e7d-438b-4690-a7af-92544858b435).

## Cambio e invariantes
La clase AngleCombinedBtcVolume4h es clon completo de la referencia combinada. Sólo BTC requiere volumen de la vela de señal ≥ mediana de las 28 fechas UTC exactamente anteriores del mismo bloque 4h, antes de resolver long/short. PAXG/SPY y restantes reglas de riesgo, señales, ejecución y fees permanecen intactos. Root verificó identidad textual de todo el resto.

Protocolo previo: ANGLE_BTC_VOLUME_PROTOCOL_20261018.md. Ventana común 2020-10-15→2025-12-31 exclusiva, fee 0,00045 por lado, mismos capital y límites. 2026 sigue reservado; no se usan datos externos.

## Resultado comunicado por root y auditado
Auditoría V4 de cartera: job b3de8216d2f64b1ea409501db66a1ac5, succeeded. Se reconciliaron fills y wallet antes de interpretar regularidad. No se repitió una auditoría desde este agente.

| Medida | Filtro volumen |
|---|---:|
| CAGR | 25,91246% |
| Drawdown diario MTM | −14,4868% |
| Operaciones | 201: 94 long, 107 short |
| Beneficio neto | 23.245,13 |
| Comisiones | 3.977,69 |
| Meses activos positivos | 32/61 = 52,4590% |
| Todos los meses positivos | 32/63 = 50,7937% |
| Trimestres positivos | 14/21 = 66,6667% |
| Meses activos completos positivos | 32/59 = 54,2373% |
| Trimestres completos positivos | 13/19 = 68,4211% |

Referencia: [combinada original](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb), CAGR 28,8294%, meses activos 33/61, trimestres 15/21. El filtro rescata cuatro signos mensuales y estropea cinco. No es una mejora de regularidad.

BTC short: neto 3.572,18 y profit factor 1,2909 frente a 5.287,02 y 1,3602 de referencia. La participación por volumen no refinó satisfactoriamente esa pata. No se interpreta este resultado como prueba universal de inutilidad del volumen.

## Límites y decisión
Los contadores existían en vars y se emitían vía debugging anual/final, pero debug_mode=False puede impedir su archivo. No se inventan cantidades de bloqueos, valores de medianas ni detalle por años ausente de la evidencia recibida. No son trades contrafactuales.

Los componentes comparten capital: conservar reglas PAXG/SPY no asegura idénticos fills cuando se bloquea BTC. La comparación válida es la cartera efectiva auditada, no una suma de curvas.

Receta rechazada por menor regularidad y menor CAGR, sin cambiar objetivos ni seleccionar otro umbral tras observarla. El ligero descenso del drawdown no compensa el incumplimiento del objetivo. Ésta es otra observación de desarrollo dentro de una búsqueda extensa, no OOS.
