# R36 A — crítica interpretativa independiente

Ambas políticas quedan NO_CUMPLE. Se leyeron completos BTC_R36_A_RESULTS_20261022.json (2.358 líneas, dos páginas unidas y parseadas) y BTC_R36_UNIVERSE_CHECK_20261022.json. Esta revisión acepta la auditoría contable y nativa root de 543 trades y 1.274 pagos; no la repite por fill ni inicia jobs.

| Política | N | Neto USD | CAGR | PF neto USD | DD M1 y fills | Meses positivos | Trimestres positivos |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Lunes: revierte sábado→lunes | 272 | −3.581,95458 | −8,15008% | 0,65703 | 38,46105% | 23/62 | 5/20 |
| Jueves: revierte martes→jueves | 271 | −239,28440 | −0,46321% | 0,96949 | 14,79581% | 34/62 | 10/20 |

La cadencia se consiguió: los 272 y 271 slots esperados produjeron todos sus eventos, planes y fills, con cero retornos iguales a cero, datos inválidos y ocupaciones. La diferencia de una oportunidad es la frontera histórica prefijada; no se igualan denominadores borrando trades ni se consideran semanas independientes. A diferencia de R34 A, aquí la limitación no es escasez o acceso: hay actividad recurrente, pero no ventaja neta.

La hipótesis comparativa tampoco se sostuvo: la política de fin de semana tiene menor CAGR, mayor DD y menos meses calendario positivos que el control. Ambos brazos activos en los 62 meses permiten comparar sus números de meses positivos sin cambio de denominador. Se comparan políticas completas con distintos días y retornos de formación; esto no identifica una causa de liquidez, flujo institucional o cierre de mercado.

La pérdida del lunes no es sólo una comisión que borra un pequeño margen: bruto −2.753,45154 menos fees 852,43583 más funding 23,93279 da neto −3.581,95458 USD. Sus dos lados sumaron pérdidas y cada año completo 2021–2025 fue negativo. El jueves tuvo bruto +409,99793, pero fees 705,65263 menos el crédito funding 56,37030 lo dejan en −239,28440. La contabilidad usa los costes base acordados, no estrés. Un bruto positivo del control no acredita una estrategia operable.

La mediana mensual positiva del jueves (+0,09803%) coexiste con pérdida neta global, PF inferior a1 y neto sin los dos mejores meses de −889,80871 USD. Es una demostración concreta de por qué regularidad y rentabilidad deben exigirse juntas. El lunes también falla la mediana (−0,59147%) y queda en −4.104,88499 USD sin los dos mejores meses. Ninguno cumple los objetivos r9; superar N100 sólo satisface el mínimo operativo, no prueba potencia ni independencia.

Las salidas auditadas fueron lunes116 STOP/156 MARKET a24h y jueves52 STOP/219 MARKET; no hubo TP ni terminal. El stop y reloj funcionaron conforme al protocolo. Esa diferencia de stops describe estas trayectorias; no autoriza invertir el signo, cambiar la gestión o seleccionar el lado corto del jueves por su contribución positiva.

Se cierra esta comparación y sus recetas, sin seguir el retorno en vez de revertirlo, mover días, ampliar formación/tenencia o rescatar parámetros. El resultado reduce una incertidumbre real: una oportunidad semanal disponible puede ser recurrente y aun destruir capital con reglas disciplinadas. No refuta toda estrategia semanal, ni propone otra variante desde este PnL. Son cuentas alternativas sobre desarrollo histórico observado, no cartera ni OOS.

Fuentes de verdad: ambos JSON mencionados, en strategies/FundingOiPilot4h/reports/. Sin nuevos precios, motores, jobs o modificaciones de fuentes en esta revisión.
