# PAXG 0,75 en cuenta compartida: resultado final

Fecha local: 18 de octubre de 2026. Los dos backtests y sus auditorías terminaron. El tratamiento mejora modestamente rentabilidad y drawdown frente al control con el mismo riesgo PAXG, pero no mejora el número de meses o trimestres positivos. No alcanza la meta de regularidad y no se acepta como reemplazo de la referencia.

## Comparación implementada

El protocolo PAXG_SHARED_ACCOUNT_PROTOCOL_20261018.md se guardó antes de los resultados. Root revisó ambas clases completas antes de ejecutar.

C mantiene las reglas originales en las tres rutas 4h, con riesgo PAXG del 1% y BTC/SPY del 3%. T mantiene BTC/SPY y sustituye PAXG por la política de fin de semana 0,75 a 1h, también al 1%. En ambos, el share ATR de TODOS los símbolos usa únicamente velas 4h completas y el calendario propio de cada ruta. Se conservan ledger, reservas de órdenes pendientes, riesgo agregado del 8%, techo bruto de 4,4x y techo individual por share ATR.

Las cuentas comparten 10.000 USDT, 5x aislado, fee de 0,00045 por lado incluso LIMIT y ventana 2020-10-15 a 2025-12-31 exclusiva. La reserva de 10 bps sólo afecta sizing. No se modificó la referencia, el framework, fuentes ni 2026.

C no es una réplica exacta de la referencia: PAXG baja del 3% al 1% y el reloj común de asignación se hace explícito. T contra C es la comparación primaria. La selección previa del umbral 0,75 es adaptativa; no se convierte en una validación independiente al usar cuenta compartida.

| Resultado | [Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) | [C: retest PAXG 1%](http://localhost:9200/#/backtest/148f089d-2a06-48e0-b3eb-cd45a9f69eb2) | [T: fin de semana PAXG 0,75 al 1%](http://localhost:9200/#/backtest/08975619-224b-415a-9c40-bde9ded32d69) |
|---|---:|---:|---:|
| Trades | 220 | 222 | 247 |
| Neto USD | 27.461,46 | 24.807,07 | 25.563,78 |
| Fees USD | 4.595,62 | 3.958,75 | 4.419,76 |
| CAGR motor | 28,829% | 27,026% | 27,551% |
| DD motor | −14,891% | −13,523% | −12,359% |
| Sharpe motor | 1,316 | 1,394 | 1,472 |
| DD de cierres diarios auditado | Ver auditoría de referencia | −13,510% | −12,359% |

T frente a C suma 756,71 USD netos y 0,525 puntos porcentuales de CAGR, con mejora de 1,163 puntos en DD del motor. Frente a la referencia original conserva menor CAGR; ese contexto no se oculta.

## Regularidad MTM: el objetivo no se alcanza

Root ejecutó el auditor V4 unificado, job 63531bd31d1a47d28c3f3702a8d8b6a9, terminado succeeded. Utiliza snapshots completos, fills y anclas de precios, sin atribuir rentabilidad al mes de cierre de trades ni usar muestras a las 00:01 como cierre UTC.

| Regularidad | Referencia | C | T |
|---|---:|---:|---:|
| Meses activos positivos | 33/61 = 54,10% | 35/61 = 57,38% | 35/61 = 57,38% |
| Todos los meses positivos | 33/63 = 52,38% | 35/63 = 55,56% | 35/63 = 55,56% |
| Trimestres positivos | 15/21 = 71,43% | 14/21 = 66,67% | 14/21 = 66,67% |
| Meses completos activos positivos | Ver informe de referencia | 35/59 = 59,32% | 35/60 = 58,33% |
| Meses completos de calendario positivos | Ver informe de referencia | 35/61 = 57,38% | 35/61 = 57,38% |
| Trimestres completos positivos | 14/19 = 73,68% | 13/19 = 68,42% | 13/19 = 68,42% |

T rescata tres meses negativos de C y deteriora cuatro positivos; cambios de meses planos compensan el conteo total. No basta enumerar meses rescatados sin los deteriorados.

Ni C ni T alcanzan el mínimo del 65% de meses activos positivos y 80% de trimestres positivos. Respecto de la referencia, la pequeña mejora mensual acompaña menor proporción de trimestres positivos. El menor drawdown no autoriza rebajar la tarjeta de aceptación.

## Atribución: la ganancia incremental no es simplemente PAXG

| Contribución de trades USD | C | T | T − C |
|---|---:|---:|---:|
| BTC long | 13.985,69 | 14.419,13 | +433,44 |
| BTC short | 5.520,20 | 5.886,21 | +366,01 |
| SPY long | 3.617,57 | 3.705,37 | +87,80 |
| PAXG, todos los sentidos | 1.683,61 | 1.553,07 | −130,54 |
| Cuenta | 24.807,07 | 25.563,78 | +756,71 |

PAXG realizado aporta algo menos en T. La mejora de cuenta aparece por tamaños y trayectoria endógena de BTC/SPY bajo capital compartido, con las mismas reglas y eventos ejecutados. No se presenta la diferencia de cuentas como alpha aislada de PAXG ni como suma de curvas independientes.

La ocupación PAXG cae de 6.100,47 a 659,80 horas, pero su turnover aumenta: fees PAXG de 625,79 a 941,00 USD. T ejecuta los 60 eventos PAXG observados en el backtest aislado. Tiene 18 longs con −258,78 USD y 42 shorts con +1.811,85 USD; no se retira el lado long retrospectivamente.

Root calculó fricción adicional contable sobre TODOS los fills, sin cambiar sizing ni decisiones: con 5 bps extra por ida y vuelta, T conserva +500,59 USD frente a C; con 10 bps, +244,48 USD. Esta sensibilidad no simula ejecución nativa ni decisiones reoptimizadas. El archivo numérico de este agente conserva además la aproximación sobre nocional de entrada, con diferencias pequeñas por el precio de salida; no son el mismo convenio de aplicación de costes.

## Auditoría y alcance

El análisis fd5b1bdce0594f599ea9004d4fc8806b terminó succeeded / exit 0. Incluye todos los trades de referencia, C, T y PAXG aislado. Las cantidades, fees, PnL y wallet concilian; diferencias máximas de PnL inferiores a 1,4e−11 USD y de wallet inferiores a 3e−11. No hay cierre sintético terminal en C o T.

C y T tienen exactamente los mismos 156 eventos BTC y 31 SPY en timestamp, sentido y fecha de salida. Sus precios coinciden dentro de precisión numérica; cantidades varían por capital. T conserva los 60 eventos PAXG aislados, con diferencia máxima de precio 4,55e−13. Esto verifica coincidencia de eventos ejecutados observados, no el universo de oportunidades ni disponibilidad perfecta de capital en cualquier escenario.

PAXG T entra siempre domingo 16:00 de Nueva York y nunca mantiene más de 24 horas. Sus salidas son 37 targets LIMIT, 8 stops y 15 salidas MARKET exactamente a 24 horas. El código mantiene gestión continua y reservas compartidas; no se dejó una estrategia aislada sin adaptar su contabilidad.

La comprobación fuente confirma share ATR común en 4h completas, ledger original y dispatch PAXG. Los resultados guardados no contienen todos los estados del ledger o velas para reconstruir cada decisión de sizing. No se presenta la auditoría de fills como prueba independiente de todos los límites intrabar o del proceso de generación de datos.

Los resultados numéricos completos se guardan en PAXG_SHARED_ACCOUNT_AUDIT_20261018.md. La auditoría MTM de root concilia también wallet y fees.

## Decisión y cierre de etapa

No aceptar T como reemplazo de la referencia ni abrir 2026. Se conserva la política PAXG de fin de semana como hallazgo exploratorio que superó controles aislados, pero su integración comprobada no resuelve la regularidad requerida. No se aumentará el riesgo PAXG, cambiará el umbral ni buscarán nuevas salidas para rescatar esta comparación.

El uso del spot como proxy para desarrollar precio fue aceptado y permitió avanzar. Una ventaja vinculada a dislocaciones específicas del token aún necesita corroboración con precio propio del perpetual y verificación de la política histórica del mercado primario antes de una promoción operativa.

Conteo final de esta etapa: once full nuevos ejecutados por este agente, más el estrés de 1 ATR de root = doce de la línea PAXG. Con cinco de SPY coordinados por el otro agente, root informa diecisiete backtests nuevos en la etapa global. Los anteriores descartes siguen formando parte del historial de selección.

Ambos backtests están finished y los análisis propios succeeded. No quedan trabajos propios activos. Las clases y todos los protocolos, auditorías y resultados quedan persistidos para revisión. Se congela esta etapa sin más tuning.
