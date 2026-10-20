# Resultado: BTC long touch-and-reclaim en la combinada
Fecha: 2026-10-18. Estado: RECETA DESCARTADA; no ajustar la latencia, umbrales ni probar same-minute tras observar el resultado.

[Dashboard de reclaim](http://localhost:9200/#/backtest/7068c1f7-f9d2-4d10-a8df-95e760a19c8b).
[Control de reloj equivalente](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1).
[Referencia original](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

## Qué se probó
Mismo setup 4h y resto de la combinada. Sólo BTC long espera toque M1 posterior al setup y cierre por encima del boundary en una M1 estrictamente posterior al toque, antes de caducidad 4h. Compra MARKET a ese cierre; qty/riesgo/nocional/distancia tienen techos congelados del setup y se revalida capital/margen actual. El control técnico previo reprodujo la referencia y aisló el adaptador de reloj.

PAXG/SPY y shorts conservan reglas, pero la trayectoria de capital compartido cambia sus cantidades y eventualmente fills. Por tanto el efecto de la variante no se reduce a diferencias de precio de entrada BTC.

## Resultado auditado comunicado por root

Auditoría cartera MTM V4: job 8ea448f4be70443cb2614e988c970bf9, succeeded. Root verificó fills/wallet y dejó los siguientes resultados; este agente no repitió la corrida ni el análisis.

| Medida | Reclaim |
|---|---:|
| CAGR | 26,91146% |
| Drawdown diario MTM | −15,00885% |
| Trades | 219: 96 long y 123 short |
| Beneficio neto | 24.643,53 |
| Comisiones | 4.213,33 |
| Meses activos positivos | 32/61 = 52,4590% |
| Todos los meses positivos | 32/63 = 50,7937% |
| Trimestres positivos | 15/21 = 71,4286% |
| Meses activos completos positivos | 32/59 = 54,2373% |
| Trimestres completos positivos | 14/19 = 73,6842% |

Frente a referencia: no rescata ningún mes de signo negativo y estropea uno positivo. La referencia obtenía 33/61 meses activos positivos y 15/21 trimestres; CAGR 28,8294%. La variante no mejora regularidad ni economía de la cuenta.

BTC long: 30 operaciones, neto 12.185,92 y profit factor 3,36794. BTC short: 123 operaciones, neto 4.821,48. No se interpreta mantener el número de shorts como identidad de cantidades/resultados: comparten capital.

## Ejecución efectiva y límites de atribución
Las 30 entradas BTC long fueron MARKET. Se identifican 29 setups comunes con la referencia y uno nuevo. En los pares comunes, root comunicó diferencia mediana de precio +4,7904 bps y retraso mediano de un minuto respecto del fill original; ratio mediano de cantidad 0,9165.

La cantidad menor no se atribuye exclusivamente a pagar más caro: los techos de nocional/riesgo y la trayectoria de capital modificada también intervienen. El nuevo setup no implica un nuevo filtro de señal; la disponibilidad/ocupación y capital pueden alterar la secuencia efectiva.

## Corrección de explicación, preservando la evidencia
La justificación inicial de exigir otro minuto como condición necesaria para evitar inferir el orden low/close era excesiva. En una vela ya cerrada, low≤boundary y close>boundary sí implican alcanzar el nivel antes del cierre. Otra M1 representa una confirmación adicional de persistencia y su coste de latencia, predeclarados; no es un requisito matemático anti-lookahead.

Se corrigieron únicamente dos líneas de comentario en la fuente actual y el razonamiento del protocolo. La fuente ejecutable, señales, umbrales y caducidad estricta son idénticos; el snapshot del run conserva la versión original por procedencia. No se corre same-minute después de conocer el fallo.

## Decisión
Descartar la receta singular por menor regularidad y CAGR, con drawdown ligeramente peor, sin una rejilla posterior de latencias ni cambio de objetivos. La buena rentabilidad aislada del long BTC no satisface por sí sola el objetivo de la cartera. Todos los resultados siguen siendo desarrollo 2020–2025; 2026 continúa sellado. No hubo datos externos, scripts nuevos ni modificación de framework.
