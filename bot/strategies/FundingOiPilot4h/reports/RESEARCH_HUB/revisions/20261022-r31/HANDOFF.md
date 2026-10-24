# Continuidad r31

Cerrado diagnóstico long y suplemento con203filas previas: menor acierto/ganadoras y pérdidas algo mayores en2024–25; costos no explican caída. No atribución causal a trailing ni candidato.51IDs económicos sin cambio.

Pasar a formular una nueva pregunta experimental por comportamiento/entrada/régimen observable causal, deduplicar y fijar comparación pequeña antes de variantes. Segmentación no fijada porlong/short ni número2/3.

# Cierre del bloque diagnóstico: long y suplemento K1001
Fecha local:2026-10-22. Estado: diagnóstico cerrado para orientar investigación posterior; objetivo económico no cumplido, sin candidata. Nuevo pedido humano: estudiar long/suplemento y cerrar este bloque, después investigar variantes; segmentación abierta por mecanismo, entrada o régimen, no obligatoriamenteLong/Short.

## Referencias y qué se analizó
[LONG_ONLY](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c) y [SHORT_BOOK](http://localhost:9200/#/backtest/aa79608f-70fd-42aa-8047-ed6bc31133c2) son cuentas alternativas ya auditadas,10k cada una, cuota activa1% del capital total y resto ocioso. SHORT_BOOK incluye dos orígenes; SUPPLEMENT no tiene cuenta standalone nueva. No sumar curvas ni atribuirle CAGR independiente al suplemento.

[Control K1001 original](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4) permanece2%histórico y31/116/45 operaciones. Cuentas de cuota31/124/48;48suplemento no45. Nuevo análisis usa203registros auditados suministrados en código:31long,124core,48suplemento. Sin nuevas velas/backtests/precios. Año de APERTURA:2020parcial separado;2021–23 y2024–25 son grupos descriptivos publicados previamente, no descubrimiento de régimen o cambio estructural.2020incluye4long/8core/1suplemento y está en ALL.

Rnet=PNL trasfee/funding dividido porqty×distancia inicial. No incluye fees/reserva en denominador; no es retorno de cuenta ni presupuestoriesgo. MáximosM1+fills observados mientras estuvo abierta cada operación, censurados por su propia salida, no MFEintraminuto ni precios ejecutables.

## Long: menos aciertos, menor ganadora y pérdida algo mayor
|Métrica por trade|2021–23|2024–25|
|---|---:|---:|
|N|13|14|
|Ganadores|6/13=46.15%|4/14=28.57%|
|Ganadora media netaR|5.8408|2.8392|
|Perdedora media netaR|−0.5940|−0.7966|
|Media brutaR|2.5921|0.3296|
|Comisión mediaR, resta|0.02965|0.03731|
|Funding medioR, suma|−0.18656|−0.05016|
|Media netaR|2.3759|0.2422|
|Máximo favorable observado, mediaR|4.7449|2.1048|
|Giveback observado, mediaR|2.1528|1.7752|

La caída neta−2.13374R/trade se descompone aritméticamente en bruto−2.26248, cambiofee−0.00766 yfunding+0.13640. El funding MEJORÓ; no explica el deterioro. No confundir incremento de feeR con aumento de tarifa nominal: tarifa.00045 constante, distinta geometría/tiempo/precio produce otro costoR.

El giveback medio y mediano no aumentó; la trayectoria favorable observada sí se redujo. Esto contradice una explicación exclusiva de “está devolviendo cada vez más beneficio”, pero no identifica causalmente entrada o salida ni prueba una regla mejor. Duración mediana186.4→86.27h, muestras pequeñas y salida condicionante.

En ALL31 el long mantiene media1.270R y mediana−.0679R;13ganadores/18perdedores. Sus3mayoresR aportan30.7961de39.3697R totales; el resto suma+8.5735R. Esto no contradice la resta histórica−116.08USDT del libro original sin sus3mejores dólares: son otros pesos, capitalización/escenario y selección porR frente aUSDT. Ninguna resta recalcula una cuenta alternativa ni autoriza quitar trades. Se conserva el rasgo de concentración y la necesidad de capturar algunas tendencias grandes.

[Entrada MARKET ya ejecutada](http://localhost:9200/#/backtest/1e016570-d981-47d1-b6d8-38fcde982084): CAGR8.2325% frente6.7079%,DD6.2330% frente8.4730%,M15/33frente13/28,mediana0ambas. Más fills y mejor retorno/DD no resolvieron regularidad/objetivo. No convertirla en candidata ni repetir este contraste como investigación nueva.

## Suplemento: cambia la mezcla de resultados
|Métrica por trade|2021–23|2024–25|
|---|---:|---:|
|N|24|23|
|Ganadores|17/24=70.83%|13/23=56.52%|
|Ganadora media netaR|1.3347|1.0188|
|Perdedora media netaR|−0.4835|−0.7170|
|Media brutaR|0.83915|0.29149|
|Comisión mediaR, resta|0.04329|0.04177|
|Funding medioR, suma|+0.00851|+0.01437|
|Media netaR|0.80436|0.26409|
|Cierres LIMIT objetivo2R|10/24|5/23|
|Cierres STOP|2/24|5/23|
|Cierres MARKET|12/24|13/23|
|Media neta de cierres MARKET,R|+0.16240|+0.11677|

La caída neta−0.54027R/trade se descompone en bruto−0.54766,fee+0.00153 yfunding+0.00587. Costos no explican la caída; fees/funding medios ayudaron levemente. Menos TP y más STOP describen el resultado, no etiquetas utilizables antes de entrar.

En ALL48hay15LIMIT,8STOP,25MARKET. MARKET aporta media+.13867R y15ganadores/10perdedores: no es sinónimo de trade malo. En la fuente el suplemento usa horizonte48h evaluado cada4h; duración no es48h exactas (MARKET media50.78h). Aquí clasificamos por tipo nativo, sin deducir causa sólo desde submitted_via. El long también tiene un MARKET distinto; no llamarlo timeout por ese tipo.

Máximo observado mediano1.4191→.5830R; giveback mediano.1916→.4771R. Con MEDIAS puede escribirse bruto=max−giveback por identidad por fila: cambio máximo−.39492R y giveback+.15274R producen cambio bruto−.54766R. Esta igualdad es algebraica, no dos efectos causales identificados ni prueba de que capturar el máximo fuese posible. No restar medianas para fabricar esa descomposición. El suplemento tiene mezcla de caminos débilmente favorables y fallos, no simple apuesta binaria2R/−1R.

## Qué queda resuelto y qué no
Resuelto: deterioro no uniforme; core conserva medias/maxobservados similares oalgo mayores en estos grupos. Long y suplemento pierden fuerza por características observadas diferentes; no agrupar todos los shorts ni explicar todo por costos, frecuencia o trailing. Independizar long no añadió fills frente al original; SHORT_BOOK sí cambia selección, sin convertir14entradas nuevas netonegativas en licencia de eliminarlas.

No resuelto: causa económica de la menor continuación, clasificación causal anticipable de mercado, efecto de una salida alternativa, contrafactual de candidatos no guardados y comportamiento simultáneo de varias ramas. No es necesario resolver todo para cerrar diagnóstico. Estas incógnitas pasan a hipótesis experimentales futuras, no a afirmaciones que pretendan estar demostradas hoy.

No se ha demostrado que segmentar mejore, ni que exista una cantidad óptima de bloques. Regímenes deben definirse con información disponible al decidir, nunca por PnL futuro o año retrospectivo. Las muestras pequeñas limitan extrapolación y este histórico fue reutilizado/adaptativo, no OOS.

## Puente hacia nuevas pruebas
Unidad de investigación = comportamiento explotable y reglas causales, no lado obligatorio. Taxonomía abierta: continuación de movimiento, fallo/reversión, respuesta a expansión/compresión o forma de entrada pueden generar especialistas si lo acredita evidencia posterior. Son categorías de preguntas, no cuatro recetas ya aprobadas ni promesa de edge.

Siguiente secuencia:
1. Elegir una pregunta sobre contexto de entrada/continuación que distinga una explicación de otra, contrastada con antecedentes; no asumir “trailing malo”. Para suplemento estudiar qué condiciones disponibles anticipan persistencia del fallo frente a recuperación, sin etiquetar con cierreTP/STOP.
2. Diseñar comparación pequeña con referencia reutilizada cuando equivalente, reglas completas, mismo riesgo/costos y presupuesto previo. Una variante puede ser válida si responde una diferencia material; no hay veto general a investigar variantes, pero no seguir vecinos de una comparación cerrada por inercia.
3. Probar y medir cada especialista; conservar fallos y creatividad con mecanismo específico. Sólo después discutir convivencia y reparto/arquitectura. No trasladar automáticamente30%CAGR a cada cuota como promesa, cambiar denominadores o relajar puertas para rescatar aprobación.

Nueva fase no exige que todas las hipótesis deriven deK1001. Se conserva su referencia y lo aprendido; estrategias nuevas pueden superar esta familia. No se ejecutó aún nueva variante dentro de este cierre.

## Integridad, autorización y conservación
Protocolo y código guardados antes del único analysisjob56dc8aa026ff4e2aa588430afb749a39;PASSprimerintento,203filas,closure.json41761caracteres completo. Identidades porfila tolerancia1e−10. Root recomputó84medias y conteos y la fórmula explícitapWin*meanWin+pLoss*meanLoss enJavaScript sobre mismosinputs, error máximo2.84e−14; no segunda fuente independiente. El campo Pythonmean_identity_error sólo verifica suma completa vs particionada, alcance aclarado en recibo. No error técnico ni rerun.

51IDs económicos desde r9 siguen51; cero motores nuevos en este cierre. Costos base taker descontado.00045/funding históricoON; slippage0,reserva.001sólodesizing. BTCtotal2% compartido en eventuales cuotas iguales, sin redistribución automática,6%global/3xaislado. No fijar dos o tres especialistas antes de resultados. No nuevosdatos/2026/USDC/estrés/riskgrids/live/paper/Pi/configglobal/install. No cambiaron fuentes de estrategias.

Fuentes: K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md; K1001_QUOTA_SCENARIOS_RESULTS_20261021.json; K1001_QUOTA_SCENARIOS_PERIOD_AND_FUNNEL_20261021.json; K1001_LONG_MARKET_FINAL_20261021.md; K1001_WEAKNESS_AND_SPOT_PERP_DOCUMENTARY_REVIEW_20261021.md. Nuevo protocolo/código/recibo K1001_LONG_SUPPLEMENT_CLOSURE_*_20261022 y revisión crítica asociada. Guardados dentro del proyectoJesse de la máquina que ejecutaJesse, no en workspace del asistente.


## Auditoría independiente acotada

# K1001 long y suplemento — crítica independiente de cierre
Fecha local2026-10-22. Revisión acotada del protocolo y código completos K1001_LONG_SUPPLEMENT_CLOSURE_PROTOCOL_20261022.md y K1001_LONG_SUPPLEMENT_CLOSURE_CODE_20261022.md; hallazgos comunicados por root del job56dc8aa026ff4e2aa588430afb749a39PASS. No consulté directamente el artefacto del job ni ejecuté otro análisis.

## Veredicto
Conforme para cerrar el diagnóstico descriptivo antes de variantes, con las precisiones siguientes. Los resultados justifican afirmar que las ejecuciones long y suplemento tuvieron menor ventaja realizada en2024–25: menos aciertos, ganadoras menores y pérdidas medias mayores. No identifican por sí solos causa de mercado, señal inferior, régimen estable, mala salida ni una intervención rentable.

## Long
La media brutaR cae2.5921→.3296 y la neta2.3759→.2422. El funding menos negativo−.18656→−.05016R amortigua la caída, no la causa. Acierto46.15→28.57%, ganadora media5.8408→2.8392R y perdedora−.5940→−.7966R describen conjuntamente el deterioro. No tratar esas diferencias como efectos causales separados o aditivos sin una convención de descomposición.

El máximo favorable medio observado baja4.7449→2.1048R y el giveback medio2.15276→1.77517R. No respalda un aumento del giveback absoluto medio como explicación única. Tampoco demuestra que el trailing sea óptimo o irrelevante: máximo y duración están censurados por la propia salida, sólo cubren marcasM1+fills y no son precios ejecutables. La identidad maxR−givebackR=grossR es algebraica, no una salida contrafactual.

Top3long30.7961R de39.3697R y resto+8.57355R indican concentración con un resto positivo bajo esta normalización, no que el resto sostenga el objetivo. El antiguo resto−116.08USDT correspondía a otra cuenta/pesos2%; no es contradicción. Explicar ambas unidades y selección de cuenta si se mencionan juntas; mejor no mezclar tablas.

## Suplemento
Menor acierto70.83→56.52%, ganadoras1.3347→1.0188R y pérdidas−.4835→−.7170R sostienen una degradación observada más amplia que “unos timeouts malos”. TP10/24→5/23 y STOP2/24→5/23 describen mezcla de desenlaces bajo la regla existente, no probabilidades de regímenes causales.

Los MARKET12→13 tienen media neta positiva+.16240→+.11677R; no habilitan retirar la salida por plazo ni concluir que todos los cierres por tiempo pierden. Tipo nativoMARKET es modo de ejecución, no causa universal. Etiquetar timeout sólo cuando la causa/edad original ya auditada lo sostenga, conservando posibles conversiones o cierres terminales separados. Ningún grupo por salida está disponible en el momento de entrar: no usarlo como filtro retrospectivo.

## Alcance de muestra y comprobaciones
El código incorpora203filas únicas:31LONG_RUNNER,48SUPPLEMENT y124CORE_SHORT, de dos escenarios alternativos. EnSUPPLEMENT48=1apertura2020parcial+24en2021–23+23en2024–25. No confundir con45suplementos del libroKoriginal; origen y reglas comunes no implican idéntico conjunto ejecutado.

Cohortes son por año de apertura; un cierre posterior sigue perteneciendo a su cohorte. No representan retornos anualesMTM. NormalizaciónR usa riesgo de precio, no retorno del capital ni presupuesto completo con costos. Las cuentas no se suman, core es referencia descriptiva y Npequeño/dependencia temporal impiden atribuir estabilidad por conteo.

Las identidades gross−fees+funding=net y max−giveback=gross están comprobadas por fila. El campomean_identity_error sólo compara suma completa con la misma suma reagrupada en win/loss/zero; no constituye comprobación independiente de pWin*meanWin+pLoss*meanLoss. No invalida las medias publicadas ni exige otra corrida; describirlo como consistencia aritmética. El código separa ceros y grupos vacíos, sin convertir ausencias en ventajas.

## Plan de cierre recomendado
Cerrar explícitamente las preguntas de acierto/payoff/costos/concentración/tipos de salida como respondidas descriptivamente, preservando incertidumbre sobre la causa. Registrar que no hay evidencia suficiente para prescribir trailing,TP,TTL,filtros o ampliación de exposición.

La siguiente decisión metodológica debe evaluar una única pregunta de comportamiento, entrada o régimen observable causal que no esté ya respondida o descartada por antecedentes. No imponer desde ahora dos/tres operativas ni una divisiónLong/Short; esos lados fueron herramientas de diagnóstico. Cualquier segmentación futura se define con información anterior a la decisión, nunca con ganador/perdedor,máximo futuro,tipo de salida o año elegido por resultado. Si no se identifica una pregunta material, conservar cierre y no forzar un motor.

Resultado de esta revisión: crítica documental y este reporteMCP; cero nuevos jobs,precios,estrategias,backtests o cambios de configuración/riesgo.


## Continuidad operativa de agentes

No confundir cierre de diagnóstico con objetivo económico cumplido. No hay motores activos ni nuevas estrategias en esta tanda. No pedir permiso rutinario para formular/deduplicar la próxima hipótesis dentro de autonomía ya concedida. El pedido actual prioriza cierre antes de nuevas pruebas; ese cierre ya quedó realizado. No repetir las respuestas de confirmación al usuario ni presentar un plan como si fuese ejecución. Fuentesyresultados económicos conservados. Próxima tarea: concretar pregunta de investigación y comparación, no reabrir por inerciaMARKET/TTL/trailing. Una variante posterior con nueva justificación material no está vetada por su nombre; respetar presupuestos y evidencia de protocolos previos.
