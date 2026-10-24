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
