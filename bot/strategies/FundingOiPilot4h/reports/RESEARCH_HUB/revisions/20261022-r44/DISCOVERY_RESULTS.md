# R44 cerrada — primera ruptura del rango inicial BTC
Objetivo r9 no alcanzado; autonomía global activa. Dos cuentas alternativas BTC-USDT, no libro conjunto ni muestras independientes. Histórico UTC[2020-10-15,2026-01-01), ya observado/adaptativo, no OOS. Sin economía nueva2026.

| Ciclo | Operaciones | Neto USDT | CAGR | PF neto | DD M1+fills | Meses activos positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|---:|---:|
| [00UTC](http://localhost:9200/#/backtest/026a408a-24e4-4174-adc7-416a7b577c9a) | 1809 | −4894.80 | −12.09% | .905 | 58.04% | 23/62 | 5/20 |
| [12UTC](http://localhost:9200/#/backtest/8056c4d9-dec4-4b84-b587-269dc6143c8e) | 1521 | −6225.81 | −17.04% | .804 | 62.56% | 20/62 | 4/20 |

Ambas fallan todas las puertas económicas salvo N>=100, que sólo acredita suficiencia operativa preliminar. Mediana calendario −1.1092%/−1.7705%; neto aritmético sin dos mejores meses −6661.93/−6954.88. Todos los años completos2021–25 pierden en ambas. 51ventanas12m por cuenta: extremos00 −32.67%/+9.36%;12 −24.94%/+2.90%.

## Qué aprendimos
Ambas fases tuvieron1904 rangos válidos, cero fallos4h/M1, cero oportunidades omitidas por ocupación o sizing. Eventos1809/1521 y ciclos sin ruptura95/383. Fase12 conserva parcial inicial omitido y último parcial con cierre terminal; fase00 termina flat. El problema no es escasez de operaciones ni cuota sin poder entrar.
Bruto sobre las cantidades realmente ejecutadas:00 +1726.96, fees6472.55, funding−149.21;12 bruto−2251.01, fees3856.47, funding−118.33. Esta descomposición no simula una cuenta sin costos ni prueba ventaja explotable sin fees. El funding no explica la pérdida principal.
Mayor neto relativo00 no implica candidata: CAGR, PF, DD y regularidad fallan. No seleccionar longs00 por su neto+172.34 frente a shorts−5067.13; no retirar lados ni cambiar fases/8h/stop/primera ruptura/cortes/duración tras verPnL.

## Controles y límites
154 resultados sintéticos PASS primer intento antes de motores; fuentes reales suministradas y cotejadas, sin importar proyecto ni consultar mercado en analysis. Fuente base tuvo una corrección defensiva de orden de timestamps antes de motores, inicial preservada; sin cambio económico.
Snapshot nativo PASS primer intento,3330trades y4756pagos funding conciliados. Cuota1% del mismo wallet10k, legacy .5capital/.5margin, lote.001, fee.00045 y reserva.001 sólo sizing: errorqty0, máximobudgeterror4.2e−13. BTCtotalfuturo2%/6%global/3xaislado intactos, cuota ociosa sinredistribución. Funding dataset verificado9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571, slippage0.
Rangos reconstruidos de dos OHLC4h expuestos, eventos/relojes/primera ruptura por fuente+sintéticos+contadores/extremos runtime. No replay independiente de cada quoteM1 real. Máxima duración15h59m; min tiempo restante00 13m y12 1m, sin eliminar entradas tardías. Salidas827STOP,2502deadline,1terminal; posicionesfinales0.
Una comprobación root adicional falló porque asumía órdenes STOP canceladas presentes en cada trade snapshot; éste sólo las ofrece cuando ejecutadas. Sin reruns. Se documentó omisión y se conciliaron3330STOPsubmit/2503cancel desde logs nativos completos con precios de texto a2decimales, además de exactitud de STOP ejecutados. No afirmar ledger completo de órdenes del exchange.
Raw completo152páginas/75743líneas y13páginasfunding;31archivos durables30.98Mchars con readback exacto, índice BTC_R44_A_DURABLE_INDEX_20261022.json. Fuentes/formas finales exactas;0motoresactivos. Sin cambiosframework/configglobal, instalaciones, restart, nuevosdatos/activos, cartera, estrés o live/paper.

## Decisión y continuidad
Cerrar ambas recetas, sin vecinos de rescate.70IDs económicos completos desde r9, observadorR42 separado; no independencia estadística. Objetivo global activo y sin candidata.
Revisión creativa paralela descartó repeticiones de orden de extremos/recuperación; patrón de tres barras no recibió motor por fundamento/materialidad insuficientes. No inventar mecanismo de órdenes a partir de OHLC.
Siguiente trabajo: otra pregunta material contrastada con historial; reconocer que nueva etiqueta no acredita información nueva. No repetir R44 ni relanzar sus handles terminados.
