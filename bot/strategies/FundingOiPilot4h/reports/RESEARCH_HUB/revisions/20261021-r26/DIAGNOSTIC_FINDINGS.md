# K1001: qué sabemos antes de estudiar una división

Fecha local: 2026-10-21. Diagnóstico de la cuenta BTC-USDT ya ejecutada; sin nuevas corridas de estrategias, velas, importaciones o derivados. El objetivo económico sigue sin cumplirse y K1001 conserva su veredicto previo.

[Cuenta BTC individual K1001](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4). Histórico UTC [2020-10-15,2026-01-01), ampliamente observado. Capital inicial 10.000 USDT, perfil histórico 2% por operación /6% agregado /3x aislado. Taker .00045 por lado, funding histórico aplicado con proxies declarados; slippage modelado cero. No son resultados futuros del reparto 1%+1% o de tres cuotas de 2/3%.

**Pregunta 1. ¿De dónde viene la ganancia?**

| Componente | Operaciones | Neto USDT | PF de sus trades | Media neta en R | Duración media |
|---|---:|---:|---:|---:|---:|
| Long de tendencia | 31 | 10650.42 | 2.88 | 1.270 | 170.6 h |
| Short principal | 116 | 4686.30 | 1.25 | 0.095 | 20.8 h |
| Suplemento short | 45 | 9191.97 | 2.99 | 0.522 | 37.4 h |

Los tres componentes aportaron ganancias dentro del libro coordinado. Los dos shorts juntos aportaron 13.878,27 USDT frente a 10.650,42 del long. No es correcto empezar suponiendo que sólo los longs funcionan. Tampoco son tres cuentas independientes: compartieron selección, prioridad, capital y una posición.

R es aquí neto del trade dividido por cantidad×distancia del stop inicial. Su numerador incluye comisiones y funding; el denominador es riesgo de precio, sin comisiones ni reserva. Se guardan por separado los múltiplos sobre riesgo de sizing y presupuesto. R no es retorno de cuenta ni garantía de pérdida máxima.

**Pregunta 2. ¿Por qué bajó la rentabilidad en 2024–2025?**

| Año de cierre | Operaciones | Media bruta R | Comisiones medias R | Funding medio R | Media neta R |
|---|---:|---:|---:|---:|---:|
| 2021 | 40 | 0.516 | 0.025 | -0.040 | 0.451 |
| 2022 | 31 | 0.515 | 0.035 | 0.001 | 0.481 |
| 2023 | 34 | 0.769 | 0.053 | -0.001 | 0.715 |
| 2024 | 42 | 0.198 | 0.037 | -0.000 | 0.160 |
| 2025 | 34 | 0.286 | 0.053 | -0.001 | 0.232 |

La frecuencia ejecutada no cayó en 2024: 42 operaciones frente a 31–40 en los tres años anteriores. En 2025 hubo 34, las mismas que en 2023. Lo que cayó fue el resultado observado por unidad de riesgo: media neta 0,715R en 2023 frente a 0,160R y 0,232R en 2024–2025. La media bruta también cayó. La tasa de comisión no cambió y el funding neto anual fue pequeño en esos dos últimos años; por tanto no es una explicación suficiente atribuir la debilidad a los costos.

Esto describe las operaciones que el libro ejecutó. No demuestra cuántas señales hubo en el mercado, si se perdió una tendencia por ocupación, ni separa todavía calidad de entrada de gestión.

| Año | Retorno del libro | Aporte long | Aporte short principal | Aporte suplemento |
|---|---:|---:|---:|---:|
| 2021 | 37.75% | 33.94 pp | -3.86 pp | 7.67 pp |
| 2022 | 30.14% | -3.31 pp | 13.72 pp | 19.73 pp |
| 2023 | 46.39% | 27.40 pp | 8.94 pp | 10.05 pp |
| 2024 | 11.41% | 6.28 pp | 2.84 pp | 2.29 pp |
| 2025 | 13.97% | -0.09 pp | 3.26 pp | 10.79 pp |

Los aportes son puntos porcentuales del retorno de la cuenta común al inicio de cada año; suman su retorno. No son rentabilidades de cuentas independientes. En 2024 se debilitaron particularmente long y suplemento respecto de 2023. En 2025 el long quedó aproximadamente neutro y el suplemento explicó la mayor parte de la ganancia del libro.

**Pregunta 3. ¿Qué tipo de ganancia y fragilidad tiene cada componente?**

El long tiene una distribución de captura de tendencias: 13 trades ganadores de 31, ganadoras medias +4,04R y perdedoras medias −0,73R; duración media cercana a siete días. Su mediana de trade neto es negativa, aunque su media y su aporte total sean positivos. Al excluir sus tres mejores trades, su contribución histórica quedaría en −116,08 USDT. Esa exclusión es una resta descriptiva de dólares históricos con tamaños congelados, no una simulación de la cuenta sin esas operaciones. La concentración es un rasgo a investigar, no una regla nueva de rechazo ni permiso para eliminar retrospectivamente ganadores. No se deben cortar las tendencias grandes para intentar mejorar la tasa de acierto.

El short principal ganó 65 de 116 trades; su media neta fue +0,095R y su PF 1,25. Su objetivo real estaba entre 0,541R y 1,484R, con media 1,007R: target 1,5ATR no significa 1,5R. Su ventaja observada por operación es menor y deja menos margen frente a degradaciones, aunque gana en el conjunto. No se infiere que cambiar el target la mejore.

El suplemento ganó 28 de 45 trades, con media +0,522R y PF 2,99. Su target nominal es 2R, pero 24 de sus 45 cierres fueron por tiempo, 14 tocaron TP LIMIT y 7 salieron por stop. Los timeouts aportaron en conjunto +1.332,38 USDT, con 14 ganadores y 10 perdedores; no son sólo pérdidas ni sólo tomas de ganancia. Esto impide describirlo simplemente como una regla binaria de ganar 2R o perder 1R.

En el short principal hubo 64 TP LIMIT,45 stops y7 timeouts. En el long hubo30 cierres STOP inicial/trailing y un MARKET con etiqueta stop-loss. Se revisó el framework: liquidate() puede etiquetar MARKET como take-profit o stop-loss según PnL abierto; por eso no se clasificó la causa únicamente por submitted_via. La conversión long MARKET se conserva como categoría propia, sin llamarla timeout. No se cambió el motor.

CORE_SHORT requiere EMA120 de 4h ascendente. Es un short admitido dentro de esa referencia lenta local; no demuestra ser una especialista permanente en grandes tendencias bajistas. Las cohortes de pocos trades no certifican estabilidad estadística.

**Pregunta 4. ¿Cómo se distribuyen los aportes entre meses?**

| Contribución observada | Meses activos positivos | Meses calendario positivos | Trimestres positivos |
|---|---:|---:|---:|
| Long de tendencia | 13/28 (46.43%) | 13/62 | 8/20 |
| Short principal | 33/51 (64.71%) | 33/62 | 12/20 |
| Suplemento short | 25/36 (69.44%) | 25/62 | 16/20 |
| Dos shorts combinados | 40/58 (68.97%) | 40/62 | 15/20 |

El libro completo sigue en37/58 meses activos positivos y15/20 trimestres. Las cifras anteriores son contribuciones MTM de las operaciones efectivamente seleccionadas por K1001. Los shorts tuvieron40 meses positivos en esa atribución, pero no se puede afirmar que quitar el long produzca automáticamente una cuenta short con esa trayectoria: liberaría entradas y cambiaría tamaños/capital.

Se recuperó una atribución MTM mensual legítima sin precios nuevos: existe una única posición, se conocen los flujos de wallet y las fronteras de equity R11; el PnL abierto residual se asigna al único origen expuesto. Ninguna apertura/cierre coincide con una frontera mensual. Las53 fronteras planas reconcilian equity y wallet con error máximo5,82e−11 USDT. La suma de componentes en las fronteras abiertas es una identidad por construcción del residual, no una verificación independiente del precio de marca. Los controles independientes son las53 fronteras planas, la fase de cashflows y los ledgers terminales; los63 intervalos suman el libro y terminan en sus ledgers netos. La revisión independiente y el código quedan guardados.

Esto supera una limitación de la viabilidad preliminar; no se borra aquella revisión. La atribución es posible en este libro de posición única y no generaliza a varias posiciones con marcas desconocidas. No acredita CAGR, DD ni regularidad standalone.

**Pregunta 5. ¿La coordinación está bloqueando oportunidades valiosas?**

Se conoce el orden long→short principal→suplemento, los313 planes seleccionados,192 fills,121 cancelaciones y82 eventos del suplemento. El long estuvo expuesto aproximadamente11,57% del tiempo total, el short principal5,27% y el suplemento3,69%; el libro tuvo posición alrededor del20,53% del histórico.

Esto no responde si la ocupación perjudicó: las señales pueden concentrarse en ese20,53%, y las órdenes pendientes también ocupan recursos. Los registros no guardan todos los candidatos, sus latches y causas de descarte en cada cierre de4h. No se interpreta82−45 como37 operaciones perdidas ni el tiempo plano como oportunidad desaprovechada. Sin instrumentación posterior no sabemos el resultado de liberar componentes.

**Pregunta 6. ¿Qué merece estudiarse después, y qué no?**

La prioridad razonada es medir si las reglas originales generan candidatos adicionales mientras otra rama ocupa el libro, antes de cambiar entradas/salidas o asumir que una partición mejora las ganancias. Esa medición necesitará una instrumentación nueva que preserve exactamente la operativa original y registre lo que hoy falta; no debe presentarse como nueva validación económica de K1001. Este diagnóstico todavía no implementa ni ejecuta esa medición.

La pregunta creativa conservada es distinguir calidad de señal y forma de capturar el movimiento: un runner concentrado y una regla de cobro corto no deben juzgarse sólo por tasa de acierto o aporte en dólares. Primero describimos esas diferencias; no se decide ahora copiar trailing, ampliar targets o invertir longs para crear shorts.

No conviene descartar el short principal sólo por ser el menor aporte, promover el suplemento por PF alto, eliminar años malos, imponer un filtro de régimen retrospectivo o sumar curvas. Debemos separar lo observado de lo contrafactual.

**Integridad y alcance.**

Se unieron192 trades a192 aperturas/cierres reales sin ambigüedad, con conteos31/116/45 y ledgers conciliados. Se recuperaron los1151 pagos de funding; los27 trades cuyo snapshot omitía el campo no tenían pagos vinculados en el ledger completo, de modo que sus ceros se verificaron, no se supusieron. No se inventó stop inicial desde el precio de salida; la geometría salió del log de apertura.

Hubo tres intentos de análisis de registros: V1 falló por URL opcional ausente en snapshot; V2 terminó correctamente pero el lector truncó sus archivos grandes al límite efectivo64K; V3 cambió únicamente el transporte a seis partes de32 y se recuperaron todas. Los resultados parciales truncados no se utilizaron. Se conservaron código, intentos y correcciones. Ninguno fue una nueva corrida de estrategia.

Fuentes duraderas del diagnóstico bajo strategies/FundingOiPilot4h/reports/: K1001_DEEP_DIAGNOSTIC_PROTOCOL_20261021.md; CODE/V2/V3 y JOIN_CODE/V2/V3; K1001_EXISTING_LOG_IDENTITY_MAP_20261021.json; K1001_DEEP_DIAGNOSTIC_RESULT_20261021.json; K1001_MONTHLY_MTM_ATTRIBUTION_20261021.json; K1001_DEEP_DIAGNOSTIC_RECEIPT_20261021.json; K1001_MTM_ORIGIN_METHOD_CRITIQUE_20261021.md; K1001_MTM_ORIGIN_PROTOCOL_AND_CODE_20261021.md. Se conserva P como referencia histórica.

El acuerdo vigente es diagnóstico primero y bloque creativo permanente. BTCUSDT exclusivo; BTCUSDC diferido. Para futuras dos operativas, 1% cada una del mismo capital total BTC; tres, 2/3% cada una; presupuesto BTC total2%, límite global6%,3x aislado y sin redistribución automática del cupo inactivo. No se altera el riesgo histórico ni se relajan objetivos para aprobar derivados. La simultaneidad exacta requiere además resolver la contabilidad y restricciones nativas de Jesse, documentadas por separado. Sin estrés, 2026 nuevo, paper/live o cambios globales.
