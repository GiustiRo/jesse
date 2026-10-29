# Propuesta Y: orientación temporal de la asociación entre volumen y amplitud

Fecha: 2026-10-21. Estado: propuesta documental pendiente de revisión root. No es autorización para fuentes, análisis, borradores ni economía. X conserva su nombre y su HOLD de calendario del proxy; no se sobrescribe. Y usa exclusivamente BTC y recursos ya empleados en esta investigación. No consulté resultados económicos de W para diseñarla.

## Pregunta y motivación económica

¿Distinguir si la actividad de negociación tiende a aparecer antes o después de la amplitud del movimiento ayuda a predecir la continuación o reversión de la dirección BTC actual, frente a conservar sólo la dirección actual y la asociación temporal simétrica?

La hipótesis económica exploratoria es una diferencia entre atención/participación que antecede al reajuste y actividad que llega como respuesta al movimiento. En el primer caso podría persistir la dirección reciente; en el segundo, la actividad podría reflejar una respuesta tardía y tener menor persistencia. Esa explicación es plausible, pero no está acreditada: volumen agregado no identifica agentes, órdenes agresoras, información privada, liquidaciones ni impacto causal. La estadística tampoco identifica el comienzo de un episodio económico.

La debilidad central se declara antes de ejecutar: ambas variables propuestas son no direccionales. Volumen y magnitud del retorno pueden ayudar a anticipar volatilidad sin aportar nada a la media del retorno. Para producir una señal de trading se necesita que su orientación temporal modifique la persistencia de la dirección del retorno actual. Esa es la interacción sustancial que se intentaría falsar; una fórmula distinta por sí sola no justifica un motor.

No se propone Y porque W o V perdieran. La necesidad representacional es que productos contemporáneos de volumen y retorno, umbrales de volumen o un reloj de volumen no separan el orden de aparición de ambas variables. Que esta separación exista algebraicamente no implica que sea económicamente útil.

## Observable causal y propiedad exacta

En cada cierre 4h, tomar 26 cierres BTC consecutivos y sus últimos 25 volúmenes de barra, todos ya cerrados. Para j=1..25:

- r_j = log(C_j) − log(C_(j−1)).
- a_j = abs(r_j).
- v_j = log(V_j), con V_j estrictamente positivo.
- A_j = (a_j − media25(a))/std25(a, ddof=0).
- Z_j = (v_j − media25(v))/std25(v, ddof=0).

Las dos medias y desviaciones se calculan sobre las mismas 25 observaciones emparejadas de CADA origen. Para entrenar el origen i se recalculan únicamente con sus propias 25 parejas terminadas en i; nunca con el banco completo, la ventana actual o un z-score global del entrenamiento. La característica actual usa su propia ventana terminada en391. No centrar las dos direcciones con ventanas de 24 puntos distintas. Las medias pueden incluir el cierre actual porque la característica se decide después de cerrarlo; no se dice que fueran conocidas antes de esa barra.

Definir con exactamente 24 pares conocidos:

F = media24(Z_j * A_(j+1)).
R = media24(A_j * Z_(j+1)).
S = F + R.
D = F − R.

F describe asociación entre volumen de una barra y amplitud de la siguiente. R describe amplitud de una barra y volumen de la siguiente. No son dos efectos causales estimados ni coeficientes de Granger. S conserva la parte simétrica; D describe orientación temporal de esa asociación en la ventana.

Al invertir conjuntamente el orden de las 25 parejas (a_j,v_j), sus marginales, medias, desviaciones y asociación contemporánea se conservan. Con esos mismos centros y escalas, F y R intercambian papeles: S queda igual y D cambia de signo, salvo error flotante. Es una propiedad exacta de esa ventana emparejada finita. No se afirma identidad entre ventanas rolling sucesivas, que tienen otros extremos/medias; tampoco equivalencia con invertir OHLC crudos o con invertir sólo una variable.

El uso de 24 pares equivale a un lag de una barra4h en una referencia de 25 observaciones. Fundamento previo de diseño: 24 observaciones anteriores cubren cuatro días de barras4h y se agrega la observación actual, de modo que ambas orientaciones tienen exactamente24pares y las mismas marginales. Los26cierres necesarios abarcan100horas de precio; no afirmar que cuatro días sean un ciclo económico demostrado. Es una convención finita para contrastar una propiedad temporal, no una ventana identificada por frecuencias observadas. Es un único horizonte de asociación elegido para revisión, no una búsqueda de retardos, escalas o transformaciones. No imponer umbral mínimo a abs(D) o abs(S), percentiles, banda de ruido o epsilon económico. Signos cero exactos o varianza no positiva producen invalidez común; no se convierten en una categoría favorable. La fragilidad de signos cercanos a cero se acepta como limitación sin buscar un cutoff después.

## Un solo contraste, con el contrato fijado para revisión

El tratamiento tendría estado (s,q,d), donde s=sign(r_25), q=sign(S) y d=sign(D). Ocho celdas posibles. El control tendría estado (s,q), cuatro celdas: conserva la dirección actual y el signo de la asociación simétrica, sin distinguir la orientación de precedencia. Controlar sign(S) es grosero: no iguala su magnitud, las escalas originales de amplitud/volumen ni toda diferencia de régimen. Un resultado no se atribuiría a orientación temporal pura. La autocorrelación de ambas variables, tendencias intraventana, horario, heterocedasticidad y ruido de muestra finita pueden explicar D.

Ambos aprenderían medias simples del MISMO label bruto de precio BTC24h:

y_i = log(C_(i+6)/C_i).

El tratamiento usa la media de su celda actual (s,q,d). El control usa la media del grupo actual (s,q). No se utiliza D para imponer retrospectivamente una dirección ganadora ni se ofrece un tercer modelo. S tampoco se sustituye por asociación contemporánea o por GLOBAL después de resultados.

Banco: exactamente los 360 orígenes relativos con edades 6..365 barras4h, sin completar hasta 360 válidos. Se conserva el número360 de M/R/S para no elegir una historia por frecuencia de las ocho celdas: son60días de orígenes4h, no60días de observaciones independientes. No se usa replay1000 ni un banco de eventos que deba inicializarse: cadaT recomputa causalmente el problema desde las392filas cerradas, con la propia normalización de cada origen. No se observó ninguna frecuencia para justificar25/360/20. Hacen falta 392 OHLCV4h cerradas: current index391; orígenes i=26..385 inclusive; targets i+6=32..391; la primera característica utiliza cierres1..26. Así cada origen tiene 25 retornos y volúmenes emparejados, y su label ha madurado antes de decidir. El label del origen actual nunca se usa. No son 360 observaciones independientes; ventanas de features y labels se solapan intensamente.

Admisibilidad compartida: ventanas 4h consecutivas/asof exactas, OHLC finitos/positivos y consistentes; característica actual válida y s/q/d no cero; al menos 20 orígenes válidos de la celda actual (s,q,d) para AMBAS políticas, medias finitas. No dejar operar al control si la celda adicional carece de soporte. Los orígenes con volumen no positivo/no finito, desviaciones degeneradas o aritmética inválida se excluyen de los dos estimadores, sin ampliar ventana ni buscar otra transformación. No añadir regularización, shrinkage, SE, prioridad, red neuronal, kNN, OLS o selector de modelos.

Forecast >0,0019 implica long; forecast <−0,0019 implica short; banda e igualdades cash. Son medias de retorno de precio bruto, no payoffs con stop, fees o funding. El hurdle heredado es una regla de señal, no un cargo adicional. La dirección actual s forma parte del estado, pero no impone por sí misma seguirla: el resultado aprendido causalmente puede ser continuación, reversión o abstención. No se cambiará el signo de entrada después de ver PnL.

Se observaría cada nueva frontera4h, incluso ocupado. No cola, reversión, pirámides o replay; sin nueva entrada en el timestamp de una salida real. Cada política conserva su ocupación y capital propios, por lo que comparar libros no estima un efecto sobre una lista fija de trades.

La tabla de medias y el mínimo20 son herramientas ya usadas en M/Angle/W, no una innovación ni evidencia adicional de capacidad. Y sólo podría justificarse por la pregunta económica sobre orientación de la asociación precio/volumen. No repetir un mismo learning gate bajo nombres nuevos para sumar intentos si la revisión considera que esa motivación es insuficiente.

## Ejecución y evaluación que no cambiarían

Sólo BTC-USDT, Binance Perpetual Futures. Ruta de ejecución1m y auxiliar BTC4h; sin ETH, SPY u otros datos. Warmup4004h por lookback392, con cash inicial incluido y sin replay económico. No se inspeccionaron velas para elegir estas cifras; están pendientes de aprobación root, no de ajuste por resultados.

Ventana UTC [2020-10-15,2026-01-01), 10.000 USDT, riesgo objetivo2% por operación y6% agregado, aislado3x. Fee0,00045 por lado, taker con descuento; funding BTC histórico ON con dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 y proxies declaradas; slippage aplicado0. No estrés ni variantes de exposición.

Gestión R12AR congelada: entrada MARKET BTC fresco en la frontera4h, stop2ATR14simple actual de cuatro horas, sin TP, timeout24h desde fill real en el primer callback4h elegible. Sizing R10 fee-aware, margen90%, floor8; observer R11 M1 y cierre terminal intactos. El volumen sólo informa señal: no altera tamaño, stop, riesgo o plazo. Forecast bruto y ledger con fees/funding son objetos distintos.

Gates r9 sin cambios: CAGR neto>=30%, PF>=1,2, DD<=25% con objetivo20, al menos65% de meses activos completos positivos,80% de trimestres completos positivos, mediana calendario>0 incluyendo inactivos, neto sin dos mejores meses>0 y N>=100 sólo preliminar. Superar el control sin cumplirlos no promueve candidata; un conteo alto no acredita potencia o independencia.

## Falsación y razones para retirar la idea

- Si el tratamiento no cumple los gates, se rechaza esta receta aunque alguna celda o año parezca bueno. No seleccionar lados, fases UTC, subperíodos o signos de D después.
- Para sostener utilidad incremental debe mejorar el retorno del libro frente al control bajo la misma ventana/capital/costos; una diferencia de nombres o un conjunto de trades equivalente no aporta evidencia nueva. Esto no es prueba de significancia o causalidad.
- La narrativa de participación anticipatoria tendría apoyo sólo si la persistencia orientada s*y es mayor con D positivo que con D negativo dentro de comparaciones de s/q con soporte. Si no aparece esa relación o resulta opuesta, la interpretación se considera no sostenida. No invertir la historia económica para llamar anticipación al resultado que convenga. Este diagnóstico describe el mecanismo; no se convierte en otro selector de estrategias ni en un nuevo gate de p-values.
- D puede contener principalmente clustering de volatilidad, fase diaria, efectos de extremos y cambios de régimen. Si no añade información direccional, no rescatarla convirtiendo el target a amplitud, cambiando lag o ajustando umbrales: sería otra pregunta y el presente contraste queda cerrado.
- Si las ocho celdas no tienen soporte o no producen actividad suficiente, no rebajar20 ni ampliar360 por PnL. No se ha medido frecuencia, cobertura o número de operaciones; no se promete suficiencia.
- La comparación de políticas mezcla señal, ocupación y trayectoria de capital. La lectura por celda no aísla efecto puro de D frente a toda la historia OHLCV, sólo frente al control definido.
- La normalización y los signos son convenciones de esta formulación. No se ha demostrado que la media de25 o el lag4h representen un proceso económico estable. Si root no considera convincente esa conexión con dirección posterior, retirar antes de implementar, sin gastar un motor.

## Deduplicación estricta

| Fuente o familia leída | Qué ya hace y diferencia material propuesta |
|---|---|
| BTCExploreR804, cierre R8 | Suma V*ΔC en dos mitades de seis barras y exige cambio de presión contemporánea. Usa retornos firmados. No compara V_j con abs(r_(j+1)) frente a abs(r_j) con V_(j+1). No se retoca su setup o gestión. |
| N204/K1001, R1/R4/R5/R6/R8/P | Presión por localización del cierre, cohortes VWAP, eficiencia, prioridad/ocupación. Y no añade un filtro a esos libros ni rescata suplementos. |
| BTCExploreR801 | Ancla en barra de máximo volumen y pérdida de coste; no asociación cruzada temporal. |
| C: absorción | Volumen grande/cuerpo pequeño seguido de escape. Dos fases de un patrón concreto, no componente antisimétrica de covariaciones de amplitud/volumen. C conserva su cierre. |
| I: participación | Impulso bajo volumen seguido de reparación a volumen normal con medianas por fase UTC. Es antecedente económico cercano de orden de participación; no es un concepto universalmente nuevo. Y no mueve sus umbrales o plazo ni selecciona otro volumen del mismo patrón. |
| AngleCombinedBtcVolume4h | Volumen actual frente a mediana previa del mismo bloque UTC; no precedencia cruzada. No se reabre su gate. |
| AngleCombinedBtcAcceptance4h | Ocupación M1 de tercio inferior. Esa idea se descartó explícitamente como repetida antes de X; no se usa aquí. |
| D, X805 y U | Frontera de buckets/cohortes definida por volumen, o reloj BTC/ETH. No estiman F−R, y Y no cambia fronteras ni ramas legacy. |
| V4 shock_features.py | Retorno grande y volumen alto simultáneos, con ATR previo; no orden de covariaciones. |
| V5 vwap_features.py | HLC3/volumen, dispersión y reentrada hacia media ponderada. No correlaciones a lag±1. |
| F: jump_state | RV/BV de retornos horarios y orientación neta, sin volumen. No se cambia su umbral ni dirección. |
| H/O/M | Geometría OHLC, orden de extremos o avance/TR; Y usa otro observable y no altera sus bins, resolución o protección. |
| R/S | Similitud de vectores de retorno y cambio a target fee-only. Y no cambia K, distancia, labels o modelo para rescatar esos resultados. |
| T | Retorno por fase UTC. Y no selecciona horas; se reconoce que D podría confundirse con estacionalidad no controlada. |
| V | Dinámica recursiva de retornos BTC/ETH, lag y seis pasos. Y no modifica ese VAR ni cambia su activo exógeno. |
| W, sólo protocolo | Pasajes a barreras y comparación de duraciones; Y no cambia barreras, tipo, reloj o banco de eventos de W. Comparte el estimador de celdas, no se presenta como algoritmo nuevo. |

Se leyeron Hub r22, historial R4, cierres C/H/I/M/O/U/V y cierres legacy R1/R4/R5/R6/R8. R/S/J/Q ya se leyeron íntegros en esta misma investigación y se conservan sus restricciones. El inventario MCP de estrategias volvió a listarse sin truncar; no apareció un nombre de inversión temporal/covariación que por sí solo resolviera la pregunta. La búsqueda de fuentes fue dirigida: no se afirma ausencia global de otro equivalente dentro de las numerosas estrategias existentes.

No vi un resultado económico que responda exactamente si D añade información direccional al control (s,S). Los resultados anteriores tampoco prueban que vaya a funcionar. No se suman curvas, se reutilizan aportes de cartera o se reinterpreta un fallo como apoyo.

## Evidencia leída y hashes

- strategies/BTCExploreR804/__init__.py — SHA256 86bcb4297fed564346c949b7f02886a062134b20a75db32d35c657b6184c6692
- strategies/BTCExploreR801/__init__.py — SHA256 3ce523dd958a8dbee3e1f96cca92b24a89d19b619343a67e1ab2b7a678a29861
- strategies/BtcContextR802/__init__.py — SHA256 f781b13d8e5ef3726f10b3b1665b1c6b3623a504650a05e09bc7ba11c50ab795
- strategies/BtcResearchR11Base1m/__init__.py — SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- strategies/BtcResearchR11ClockBase1m/__init__.py — SHA256 26440c3d83c60fcc96bd7066740dffcd7024778814e1be2f224af71e2ef6cdf5
- strategies/BtcResearchR12ParticipationBase1m/__init__.py — SHA256 3928d2b3fd4ba9ffab43b89e134e982fb65e941cccaba9ba38e3c845bf9acfba
- strategies/BtcResearchR16LegacyBase1m/__init__.py — SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542
- strategies/AngleCombinedBtcAcceptance4h/__init__.py — SHA256 8e41a80a82180a8ad2193b6105bbd2173008e76e89ac4318e9cf774511148ae4
- strategies/AngleCombinedBtcVolume4h/__init__.py — SHA256 4672a72f60a506c7dec8fdb018849bca1072a6d2ea0289820b46c2cc804c116a
- strategies/BtcResearchR12JumpBase1m/__init__.py — SHA256 631377b49a213511ca5d08f63e50cf08aa38e18fcec303479b89e3a9fc0b81a6

- strategies/ResearchV4Base1h/shock_features.py — SHA256 0ebf34769d0ad821e19773dfe5f6494398a0727ec5d1a93fc42c84472650a43b
- strategies/ResearchV5Base1h/vwap_features.py — SHA256 d6652607f3a667bcadaf10d2d64eed2af42864784f05c00123f1f429d5345bde
- strategies/ResearchV4Base1h/oscillator_features.py — SHA256 20aa757e423d6105c3276b92ad16ac154f51edae040243551de5662249521c72

Cierres legacy:
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/N204_R4_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/N204_T403_R5_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FINAL_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md

## Decisión pendiente

Root debe decidir si la justificación económica y la diferencia frente a I/X804 son suficientes. Si no, retirar documentalmente sin implementar. Si aprueba, hará falta un protocolo posterior revisado, fuentes separadas, checks supplied-source y manifiesto antes de cualquier motor. Presupuesto propuesto, aún no consumido ni autorizado: dos economías, tratamiento/control, y hasta dos reemplazos sólo técnicos. Ningún vecino posterior de25/360/20, lag, transformación log, umbrales, orientación, horizonte, target, riesgo o gestión.

Esta propuesta no demuestra necesidad de otro motor por haber definido una variable distinta. Es creatividad causal en sentido de datos asof, no causalidad económica. Estado: documental,0clases/0jobs/0drafts/0economías/0velas inspeccionadas, sin datasets nuevos, scripts, instalaciones, framework, global config, reinicios, live/paper/Pi o nuevos2026.
