# X03 R3 — revisión independiente de resultados

Lectura independiente de protocolo, fuente y QA, paridad nominal, diagnóstico mensual final, auditorías FIXED_STRESS_B/C, resultados de ejecución fixedBE y artefactos de contrastes/divergencias. No se ejecutaron nuevos jobs o backtests desde este rol.

No se encontraron objeciones materiales a los números ni a la disposición propuesta. La revisión de un eventual informe principal se hará contra estas mismas distinciones.

## Contrafactual fixedBE y preselección BTC

La intervención mantiene positivas las diferencias N204−X03 al fee motor .00070 en ambas carteras:

| Política PAXG | Δ N204−X03 B | Δ N204−X03 C |
|---|---:|---:|
| Original, dependiente del fee real | 923.163802 | 988.068271 |
| Ancla BE nominal fija | 955.663691 | 1062.542234 |
| Interacción fixed menos original | 32.499889 | 74.473963 |

Las cuatro paridades nominales pasaron con diferencia máxima de PNL cero; DD motor se mantiene dentro de 25%. Así se satisface la condición congelada para preseleccionar N204 como BTC de investigación para un eventual examen reservado, conservando PAXG original. No autoriza abrir 2026, promover la cartera ni elegir fixedBE por beneficio.

N204 con PAXG original y fee alto tiene 39/61 y 39/63 meses positivos: 63.934426% y 61.904762%, ambos fallan 65%. El contrafactual fijo tiene 40/61=65.573770% y 40/63=63.492063%: pasa sólo completos y falla incluyendo fronteras. Sus Q sí pasan: B16/19 y17/21; C17/19 y18/21. No cumple el objetivo conjunto tampoco bajo fixedBE; no se selecciona el denominador favorable.

FixedBE gana en estos caminos del simulador, pero esa observación no permite adoptarlo. Se intervino una sola política y se retuvieron los costes reales y los canales de sizing/gestión restantes. Las cantidades y el capital posteriores son mediadores del efecto total. La interacción pequeña de la ventaja BTC no es una estimación de alpha causal ni una validación independiente.

## Mensual: bruto fijo, neto base y overlay

La versión final de X03_R3_MONTHLY_REFERENCES_20261019.md distingue correctamente:

1. Bruto fijo: ΔMTM neto mensual más fees ejecutados en ese mes.
2. Neto base: después del fee propio de la sesión.
3. Overlay: base menos otros +5/+10 bps RT sobre fills fijos.

Los resúmenes publicados concilian bruto−fees=neto en las ocho sesiones, con residuos numéricos como máximo del orden de 1e-12 USDT. La asignación de midnight al borde derecho previo, los meses parciales y la distinción MTM frente a PNL por cierre son coherentes. Los 504 registros son salidas repetidas de ocho carteras sobre el mismo calendario, no 504 observaciones independientes.

N204 con fee alto y gestión original tiene, en ambas B/C, 20 meses brutos negativos y 43 positivos. Cuatro positivos brutos son absorbidos por el fee propio: quedan 39 netos positivos y 24 netos negativos. Los cuatro meses son:

- B: 2023-11, 2024-07, 2025-01, 2025-07.
- C: 2020-11, 2024-07, 2025-01, 2025-07.

Añadir otros +5 bps RT a esas mismas runs convierte dos meses positivos B y uno C en no positivos: quedan 37 y38, respectivamente; con otros +10 quedan36 en ambas. Ese overlay adicional no representa la diferencia previa de fee nominal→alto.

La deducción directa de fees de cada mes no es necesaria para clasificar negativos los 20 meses ya brutos negativos. Pero el bruto conserva posiciones y decisiones dependientes de comisiones; no se debe concluir que la comisión no influyó causalmente en ellos ni que son alpha de precio puro. Tampoco los negativos base son pérdidas anteriores a toda comisión o pérdidas de operativa real.

En nominal, N204 rescata dos meses y pierde otros dos frente a X03, conservando el número de meses positivos. Mejora neto, mientras la suma monetaria de meses negativos es más negativa. La mejora de retorno no equivale a una mejora general de frecuencia ni de severidad de pérdidas mensuales.

Las clases de beneficios pequeños están ligadas al coste propio de cada mes y son disjuntas; no se inventó un corte para aprobar. Los presupuestos son fricción hipotética y no slippage observado.

## Divergencias de ejecución

La primera ejecución PAXG divergente observada corresponde a una entrada del 27-dic-2020: el stop dinámico ejecuta el 6-ene-2021 y el fijo el 8-ene-2021. La ganancia neta pequeña del primero se vuelve pérdida con el fijo. Esto conserva evidencia adversa.

Enero de 2025 es el episodio económico grande, no el primero: fixedBE prolonga un runner y desplaza una reentrada. PAXG pasa de39 a38 trades; BTC conserva223 timestamps de entrada/salida y SPY12/19, con cantidades que pueden cambiar por capital.

Los snapshots sólo permiten ver extremos de órdenes; no contienen la historia completa de modificaciones. Por tanto, la primera instrucción STOP diferente o el primer estado interno divergente siguen siendo desconocidos. Un created_at retenido al modificar una orden no identifica el instante de la modificación. Cambios mínimos de exit_price VWAP por redondeo al variar cantidad no deben confundirse con fills a otro precio cuando las órdenes ejecutadas conservan precio/timing.

## Alcance del dictamen

R3 explica una sensibilidad de implementación y distingue pérdidas mensuales brutas, fees propios y costes adicionales. No crea un OOS ni elimina la selección histórica. B/C, nominal/stress y fixed/original comparten muestra; no se suman como pruebas independientes.

La disposición coherente es mantener PAXG original como tratamiento oficial, conservar X03 como referencia y preseleccionar N204 BTC sólo según la regla de investigación ya congelada. Deben quedar explícitos el fallo mensual bajo ambas políticas, la ausencia de promoción y el cierre de 2026. Sin más recetas, búsquedas, runs o cambios de umbral.
