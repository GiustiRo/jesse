# Incertidumbre de regularidad y selección de modelos
Fecha: 18 de octubre de 2026. Análisis descriptivo posterior a investigación; no modifica criterios de aceptación.
Dashboard referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
Dashboard FixedR5: http://localhost:9200/#/backtest/efc9d485-56ea-49fb-95ed-0f93aa690e71
Dashboard parcial: http://localhost:9200/#/backtest/0c6cfad7-c5da-465d-a45e-7009d284a1ec

## Método y alcance
Job MCP 7bf485bc8ffb45d684079723fe98191e terminó correctamente. Se embebió INLINE la versión V4 de 15.520 bytes leída por MCP, sin modificar el módulo compartido. Pasaron self_test, validación de fills, comisiones y saldo terminal. Precios diarios UTC reconstruidos con anclas de fills MARKET; el benchmark histórico sirve exclusivamente para cotizaciones, nunca para interpretar el rendimiento previo al arreglo contable.
Ventana común fija: 2020-10-15 a 2025-12-31 exclusivo. Por ello octubre de 2020 y diciembre de 2025 son meses parciales; 2020Q4 y 2025Q4 son trimestres parciales. Los principales denominadores originales (63 meses, 61 activos, 21 trimestres) permanecen intactos. El control de períodos completos es adicional, no una sustitución retrospectiva.

## Proporciones principales e intervalos Wilson nominales del 95%
| Variante | Meses activos positivos | IC95 Wilson | Trimestres positivos | IC95 Wilson |
|---|---:|---:|---:|---:|
| Referencia | 33/61 = 54,10% | 41,72–65,99% | 15/21 = 71,43% | 50,04–86,19% |
| FixedR5 | 39/61 = 63,93% | 51,39–74,83% | 16/21 = 76,19% | 54,91–89,37% |
| Parcial 50% a2R | 35/61 = 57,38% | 44,90–68,98% | 14/21 = 66,67% | 45,37–82,81% |

Sobre los 63 meses de calendario: referencia 33/63 = 52,38%; FixedR5 39/63 = 61,90%; parcial 35/63 = 55,56%. Las tres tienen 61/63 meses activos y exactamente dos meses cero.

Los intervalos usan un modelo binomial nominal con observaciones independientes y probabilidad estable. En estrategias financieras esas premisas no están garantizadas: hay posiciones que cruzan meses, regímenes comunes y selección del modelo sobre la misma muestra. Los intervalos indican incertidumbre de muestreo bajo ese modelo; no son garantía futura ni probabilidad de que la estrategia cumpla el objetivo. No se añade como criterio que el límite inferior del IC deba superar 65% u80%.

## Control de períodos completos
| Variante | Meses completos, todo calendario | Meses completos activos | Trimestres completos |
|---|---:|---:|---:|
| Referencia | 33/61 = 54,10% | 33/59 = 55,93% | 14/19 = 73,68% |
| FixedR5 | 38/61 = 62,30% | 38/59 = 64,41% | 14/19 = 73,68% |
| Parcial | 35/61 = 57,38% | 35/59 = 59,32% | 13/19 = 68,42% |

La ventaja trimestral agregada de FixedR5 desaparece al excluir ambos bordes: tiene los mismos 14 trimestres completos positivos que la referencia. Esto no invalida la tabla principal; muestra sensibilidad a extremos de la ventana y evita sobreinterpretar una diferencia de un trimestre.
IC95 Wilson para14/19: 51,21–88,19%; para13/19:46,01–84,64%. La muestra trimestral es pequeña.

## Comparación pareada de signos mensuales
Se comparan exactamente los mismos 63 meses; cero cuenta como no positivo, con independencia de la actividad de cada variante. McNemar exacto bilateral equivale a un binomial condicionado al número de meses discordantes.

| Cambio | No positivo → positivo | Positivo → no positivo | Cambio neto de meses positivos | p nominal bilateral |
|---|---:|---:|---:|---:|
| Referencia → FixedR5 | 10 | 4 | +6 | 0,179565 |
| Referencia → parcial | 3 | 1 | +2 | 0,625000 |
| FixedR5 → parcial | 5 | 9 | −4 | 0,423950 |

La diferencia de proporción calendario de FixedR5 frente a referencia es +9,52 puntos porcentuales; la del parcial +3,17. La diferencia media aritmética de retorno mensual es −0,588 puntos porcentuales y −0,446, respectivamente: ganar más meses puede reducir la magnitud de los mejores meses.
No se detecta evidencia nominal fuerte de cambio de signos con esta muestra; eso no demuestra equivalencia. La prueba tampoco corrige dependencia temporal ni la búsqueda adaptativa de modelos.

Correlaciones descriptivas lag1 de signos: referencia0,028, FixedR5−0,062, parcial0,081. De retornos: −0,073/−0,121/0,028. Valores pequeños en esta muestra NO prueban independencia ni estacionariedad.

## Selección de al menos13 pruebas
Esta ronda contiene al menos13 pruebas de desarrollo, además de las exploraciones previas. Muchas hipótesis fueron elegidas después de observar resultados; las estrategias y períodos comparten datos. El mejor resultado observado está sujeto a sesgo de selección.
Como recordatorio ilustrativo, multiplicar las p nominales por13 deja todas en1. No constituye una corrección exhaustiva: el número de decisiones adaptativas y ensayos previos es mayor, y no hubo un protocolo confirmatorio único anterior a toda la búsqueda.
No presentar estos resultados como OOS. Mantener2026 reservado y evaluar una única candidata completamente congelada cuando corresponda; no repetir el lockbox hasta aprobar.

## Hacer medible la meta sin fomentar exclusiones artificiales
Conservar el objetivo acordado65–70% de meses activos positivos y80% de trimestres. Para interpretarlo:
- Mostrar siempre juntos numerador, meses activos, todos los meses de la ventana fija, meses cero y cobertura de actividad.
- Mantener la definición actual de activo: cualquier intervalo real de posición superpuesto al mes según timestamps. No borrar meses perdedores después de verlos ni cambiar la ventana para mejorar el cociente.
- Informar períodos completos como control adicional, conservando principales denominadores originales.
- Mantener retornos de cartera MTM: una pérdida abierta cuenta en el mes correspondiente, y realizar una ganancia no crea beneficio adicional por sí solo.
- No aceptar una estrategia sólo por un cociente favorable si su actividad se colapsa o si la mejora se limita a no operar; evaluar también economía, exposición, drawdown, costes y aporte incremental. Esto es interpretación del objetivo, no un umbral nuevo de actividad.
- No añadir operaciones diminutas artificiales para convertir un mes en activo. Las reglas deben tener una hipótesis económica anterior al resultado.

En estos tres controles la cobertura es idéntica61/63: sus diferencias de signo no provienen de excluir meses inactivos. Una regla legítima que reduzca exposición puede mejorar riesgo, pero su rendimiento de todos los meses debe permanecer visible.

## Conclusión
Ninguna de las tres cumple los objetivos originales. FixedR5 se acerca en estimaciones puntuales, pero su vecino3R es débil, el beneficio trimestral depende de bordes y la incertidumbre es amplia. El parcial reduce drawdown pero no resuelve regularidad.
Se mantiene la referencia; no se modifican reglas, fuentes, riesgos, comisiones ni2026. Los resultados estadísticos no crean una nueva condición de aceptación ni justifican descartar alternativas sólo por p>0,05.
