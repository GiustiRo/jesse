# Metodología y formato — v1

Orden obligatorio: hipótesis → prerregistro → verificación técnica → exploración acotada → validación/estrés → revisión crítica → decisión razonada.

## Doble evaluación
Objetivo orientativo: 20–30% anual por operativa y por cartera. Mostrar rendimientos por año, semestre y períodos adversos con ventanas explícitas; las cohortes de cierre no equivalen a retorno MTM. Una pieza inferior puede continuar si aporta al conjunto bajo límites de riesgo. No sumar curvas aisladas con capital propio para inventar cartera compartida.
Medir correlación de rendimientos alineados y pérdidas simultáneas, incluyendo períodos sin exposición, moneda, frecuencia, cobertura y tamaño de muestra. Comparar con/sin cada pieza bajo capital, riesgo y fricción comparables. Separar retorno de exposición/beta y ventaja de reglas activas.
Muestra insuficiente es estado de evidencia; puede coexistir con incumplimiento de un gate histórico sin demostrar imposibilidad económica.

## Registro
index.json: format_version=1, current y revisions[{id,path}].
Cada revisión: id, updated_at_utc ISO8601 UTC, objetivos, decisiones, referencias reemplazadas, roadmap, documentos y catálogo de fichas.
Cada ficha: id, asset, family, execution, evidence, objective, hypothesis, origin, method, protocol, budget, versions, periods, results, limitations, audit, decision, references y sessions.
results=null significa sin evaluar; no 0. Resultados porcentuales identifican unidad, ventana, CAGR, neto, DD (motor/diario), PF, N, años/semestres, costes, exposición y estrés donde existan. Datos detallados originales se leen con los botones de evidencia. En carteras incluir correlación, pérdidas simultáneas y comparador.
Los protocolos históricos permanecen en sus archivos. Un protocol=null en una ficha histórica significa que el panel no ha transcrito ni certificado su estructura; no invalida el prerregistro original.

## Protocolos futuros
protocol requiere strings no vacíos: hypothesis, refutation, rules, references, data, costs, risk, windows, selection, code_version, data_version.
budget y criteria: objetos no vacíos con valores numéricos finitos; definir criterios propios antes del primer run (por ejemplo N mínimo, DD máximo, retorno mínimo, gates de estrés, reglas de suficiencia), sin heredar números arbitrarios del panel.
registered_at_utc obligatorio; first_run_at_utc cuando exista debe ser posterior. Referenciar evidencia temporal de congelación y timestamp de sesión. El panel sólo acredita estructura declarada.
Los presupuestos incluyen todos los intentos y reglas de cierre. Registrar variantes, fallos y reusos. Agotar una muestra pequeña no habilita ampliar el presupuesto retrospectivamente.

## Publicación
1. Elegir id nuevo. No modificar evidencia cerrada.
2. Escribir documentos, fichas y manifiesto bajo revisions/<id>/ mediante MCP; conservar originales por referencia.
3. Releer por MCP, verificar JSON, paths, fechas, identidad, conteos y enlaces. Las páginas se recorren hasta has_more=false; línea truncada invalida lectura.
4. Agregar nueva revisión al índice y cambiar current al final en una escritura completa. No hay transacción multiarchivo ni bloqueo multiagente: un responsable publica y relee el índice para detectar conflictos.
5. Si una llamada vence, leer el archivo antes de reintentar. Una corrección de una revisión publicada genera otra revisión, con motivo y referencias reemplazadas.

El panel tiene lectura autenticada, refresco al entrar/manual/cada30s visible. Señala errores, ausencias y antigüedad documental >7d; ese umbral sólo pide revisar vigencia. No monitoriza el motor ni ejecuta escrituras o experimentos.
