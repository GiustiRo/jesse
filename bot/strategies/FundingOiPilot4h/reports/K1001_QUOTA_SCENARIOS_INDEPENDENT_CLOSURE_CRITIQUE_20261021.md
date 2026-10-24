# K1001 cuota1% — Crítica independiente del cierre

Fecha: 2026-10-21. Dictamen: CONFORME con el cierre sin candidata; precisiones de interpretación no bloqueantes. Sólo lectura de evidencia y este informe, sin jobs, motores, velas nuevas o cambios de fuentes.

## Evidencia contrastada y alcance

Leí FINAL completo y los dos summaries nativos terminados:
- [LONG_ONLY](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c).
- [SHORT_BOOK](http://localhost:9200/#/backtest/aa79608f-70fd-42aa-8047-ed6bc31133c2).

Corroboré31/172trades, CAGR6.7079%/5.9247%, netos4030.903490/3501.965680USDT, capitales finales14030.903490/13501.965680, funding aplicado del dataset congelado y posiciones finales0. Los formularios conservan10000 totales,3x,fee.00045,warmup240,ruta1m/data4h y ventana aprobada. Las fees nativas son117.601939 y737.473274USDT; funding neto−421.329064 y+187.187383, con658/520pagos.

Leí directamente los resúmenes terminales R11 y R16 por MCP. Corroboran DD M1+fills8.4730%/8.6080%, M13/28 y38/58, Q8/20 y16/20, mediana0/.519105%, y neto sin dos mejores meses1397.792214/2735.482375. El DD diario del summary nativo es otro muestreo; no sustituye al R11 usado en gates.

La cola nativa reproduce el recorte de K1001_QUOTA_STATS short después de su prefijo válido. No se interpretó como JSON completo. LONG_ONLY conserva su resumen propio íntegro. Leí completos AUDIT_CODE_V2 y JOIN_AUDIT_CODE_V2, y el comienzo del JSON de resultados para comprobar esquema. No rehice la auditoría fila a fila de203 trades o1178pagos ni afirmo haber releído el JSON1.1MB completo. Los matches comunes/nuevos y distribuciones de traza proceden de la auditoría root preservada; aquí reviso su lógica y alcance frente a fuentes/código y comprobaciones nativas puntuales.

## Capital, PF y comparación con el original

El denominador correcto es10000 de cuenta total por escenario, con riesgo objetivo1% y mitad del margen disponible; la otra cuota queda inactiva. No son dos subcuentas5000 ni una cuenta conjunta simulada. El cierre lo expresa correctamente.

La diferencia respecto de Koriginal no identifica un efecto causal de liberar ocupación: cambian grupo, tamaño, capitalización y oportunidades de su propia trayectoria. Tampoco un menor DD absoluto acredita mejor coordinación cuando el presupuesto de riesgo es menor. No sumar CAGR, netos o curvas ni escalar a2% para fabricar aprobación.

Para un trade i con distancia inicial D_i y cantidad q_i, peso monetario w_i=q_i*D_i y Rnet_i=PnL_i/w_i. Entonces:
PF_USDT = suma(w_i*Rnet_i de ganadores) / suma(w_i*abs(Rnet_i) de perdedores).

Conservar los mismos Rnet_i no conserva PF_USDT si cambian los pesos relativos w_i. Por eso PF long3.5520 no acredita mejor señal que su atribución anterior. Un PF de R sin ponderación sería otra estadística descriptiva, no sustituto del PF de cuenta ni una nueva regla de aprobación. El cierre evita bien ese sobreclaim.

## Precisiones de lenguaje

1. La coincidencia de31 fills long y sus salidas acredita que separarlos NO produjo ejecuciones long adicionales en esta ventana y bajo este contrato. Recomiendo mantener esa formulación estrecha. No prueba inexistencia de candidatos raw bloqueados o de órdenes que nunca habrían llenado; la instrumentación de ese universo quedó HOLD.
2. “Función distinta” debe entenderse como perfiles observados de frecuencia/payoff/regularidad de estos escenarios. No demuestra independencia, diversificación o mejora de una futura cuenta compartida.
3. Los158shorts comunes/14nuevos/3ausentes describen una trayectoria alternativa. El neto de los14nuevos no es un incremento causal de cartera ni autoriza quitarlos, como ya declara FINAL.

No son objeciones al dictamen; evitan extenderlo más allá de lo medido.

## Trace y suficiencia de evidencia

La fuente congelada usa open0, pre conT>opened_at y exitfill antes de que parent borre el plan o emitaFINAL. La auditoría verifica identidad, geometría, bounds, marks=2+M1 y unión con órdenes nativas de cierre. Eso acredita consistencia del algoritmo y del registro recuperado, no reobservación independiente de cada marca M1.

El recorte short se maneja de forma transparente: cohortes de cierre derivadas y campos terminales inferidos se etiquetan como tales. La ausencia de errores se apoya en recuperar logs completos y en la fuente que emite el primer error, no en un trace_errors nativo que no se pudo leer. No hace falta otro motor para recuperar telemetría redundante. Conservar esta limitación incluso si todas las cuentas concilian.

En el JSON, sources.*.observed_max_R contiene la MEDIANA de los máximos por trade según JOIN_AUDIT_CODE_V2, no el máximo global. La prosa FINAL ya usa medianas correctamente. Para futuras lecturas conviene describir ese campo sin ambigüedad; no cambiar resultados ni reinterpretarlo como extremo de la muestra.

Que perdedores long tengan una mediana de máximo observado favorable no prueba una salida alternativa ejecutable: son grupos definidos después del resultado y máximos seleccionados retrospectivamente. El trailing decide4h mientras el observador muestreaM1; el cierre original censura lo posterior. No identificar mala captura, falta de follow-through o target óptimo únicamente a partir de esa comparación.

## Veredicto

LONG_ONLY falla retorno, regularidad/mediana y muestra preliminar. SHORT_BOOK pasa las puertas numéricas restantes pero falla CAGR30%; estar por encima de65% en38/58meses y80% en16/20trimestres no acredita potencia ni estabilidad fuera de este desarrollo. Mantener ambas como NO_CUMPLE es correcto, sin relajar gates por cuota1%.

La separación medida no alcanzó el objetivo. No hay fundamento en este cierre para retirar core, subir riesgo, escoger años o mover trailing/targets. Una combinación conjunta sigue sin medir; tampoco puede declararse que nunca funcionaría. Las siguientes preguntas deben conservar esas distinciones y cambiar una decisión real de investigación, sin usar esta descripción como optimización retrospectiva.

Referencias en strategies/FundingOiPilot4h/reports/: K1001_QUOTA_SCENARIOS_FINAL_20261021.md; RESULTS; PRE_ENGINE_MANIFEST; IMPLEMENTED_SOURCES; AUDIT_CODE_V2; JOIN_AUDIT_CODE_V2; RAW_RECEIPT y ANALYSIS_RECEIPT originales. Se preservan los intentos de transporte/parsing separados de los dos motores económicos terminados.
