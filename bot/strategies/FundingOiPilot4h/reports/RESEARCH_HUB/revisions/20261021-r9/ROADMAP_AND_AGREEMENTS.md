# Acuerdos vigentes BTC y roadmap amplio — r9
Fecha: 2026-10-21. Consolida la aceptación del usuario de r8 y los refinamientos posteriores. Documento de dirección y objetivos; no es prerregistro de un experimento ni ejecución.

## Qué queda acordado
- Foco exclusivo actual BTC-USDT individual. Evaluar operativas individuales antes de combinar. PAXG/SPY y cartera son fases futuras eventuales.
- Riesgo fijo de investigación: 2% objetivo por operación / 6% límite agregado de admisión / 3x aislado. Sin variantes de riesgo, apalancamiento o capital para rescatar resultados. Igual riesgo por trade entre activos es intención futura, no distribución de capital fijada.
- Objetivo mínimo: CAGR neto base de 30%; aspiración 40–50% o superior, sin techo. No significa 30% cada año.
- DD objetivo hasta 20%, techo de evaluación 25%; PF neto de trades cerrados ≥1,20.
- ≥65% de meses activos positivos, aspiración ≥70%; ≥80% de trimestres positivos. Mostrar también todos los meses calendario, ceros, negativos y períodos completos; no confundir meses activos con meses de PnL no nulo.
- Mediana de retornos de meses calendario completos positiva, incluyendo inactivos; reportar su magnitud. No es otra denominación para el 65% ni evidencia independiente.
- Resultado aritmético sobre trayectoria fija positivo al excluir los dos mejores meses del período completo. Informar exclusiones por año como diagnóstico. No presentar esta resta como replay o curva contrafactual con capital recalculado.
- Resultados mensuales basados en equity MTM, no en agrupar sólo trades por fecha de cierre. Costos y exposición abierta explícitos. Los detalles de cortes, frecuencia de mark y fronteras se fijarán en cada protocolo.

## Costos: qué incluye neto y cuándo estresar
El usuario confirma comisión taker con descuento como supuesto base. Referencia histórica 0,00045 por lado = 0,045%; el protocolo de cada estudio debe expresar la tarifa y descuento aplicables asumidos, sin afirmar que se verificó aquí la condición de una cuenta real.

Las futuras pruebas BTC deben incorporar funding activado y aplicación verificada en resultados. La integración existente es optativa y está desactivada por defecto: capacidad implementada no significa que se aplicara a cada sesión. Resultados anteriores con funding OFF conservan ese alcance. No sustituir silenciosamente datasets ni tratar datos faltantes como pagos cero.

Etiqueta acordada: «neto de comisiones taker con descuento y funding modelados». La fase inicial no modelará slippage por acuerdo del usuario; esa exclusión debe aparecer junto al resultado. No llamarlo neto de todos los costos reales.

Se difiere el estrés de comisiones, slippage y otros supuestos de ejecución hasta disponer de candidatas preliminares; se definirá y acordará antes de ejecutarlo. Esto modifica el orden de evaluación de r8: positivo bajo estrés sigue siendo una condición de validación posterior, no una puerta que obligue a estresar cada idea durante descubrimiento.

La mención del usuario de 2% de capital por slippage fue un ejemplo, no una medición, un presupuesto anual ni un techo comprobado. No descontar un 2% arbitrario ni prometer que el objetivo lo absorbe.

## Datos y método
Conservar el histórico amplio 2020–2025 ya examinado y usar la evidencia 2026 disponible. La ventana exacta, cobertura y extremos parciales de cada fuente deben declararse. No hay espera obligatoria de 12 meses futuros.

2026 conocido conserva sus fallos y exposición: para recetas congeladas antes de abrirlo, guardar evaluación original; reglas seleccionadas/modificadas después no obtienen confirmación ciega en ese mismo tramo. Este acuerdo no inicia ni autoriza automáticamente nuevas consultas de velas o corridas 2026.

Base para reglas fijas: evaluación continua con trayectoria de capital, desgloses anuales/mensuales y ventanas móviles de 12 meses. Las ventanas solapadas son descriptivas y dependientes. Walk-forward sólo si corresponde un procedimiento de selección/estimación con pasado disponible; se diseña antes de buscar, con selección, bloques y manejo de posiciones prefijados. No optimizar automáticamente al final ni presentar reconstrucción retrospectiva como eliminación del sobreajuste. Consultar V1–V6 antes de repetir.

## Roadmap: hacia dónde vamos
| Etapa | Trabajo | Por qué | Condición de salida |
|---|---|---|---|
| 1. Ubicar BTC hoy | Matriz de evidencia individual existente: cumple, no cumple, falta, no comparable. Revisar historial posterior a handoffs. | Aprovechar lo hecho y localizar la brecha real. | Diagnóstico con fuentes y sin confundir atribución de cartera con cuenta BTC aislada. |
| 2. Preparar la siguiente investigación | Elegir una pregunta material, referencia, hipótesis, reglas, datos y costos base. Congelar protocolo, presupuesto y método temporal antes de ejecutar. | Evitar repetir variantes o cambiar condiciones según los resultados. | Propuesta concreta revisada con el usuario; viabilidad técnica y alcance de ejecución definidos. |
| 3. Explorar BTC de forma acotada | Si se acuerda el protocolo, investigar estrategias con riesgo fijo, tarifa taker con descuento y funding verificado. Sin batería de estrés ni variantes de riesgo. | Concentrar esfuerzo en encontrar utilidad económica individual. | Candidatas preliminares que cumplen el objetivo base, o cierre sin candidata con aprendizaje y presupuesto respetados. |
| 4. Revisar candidatas | Examinar meses/años, concentración, causalidad, costos contabilizados, muestra y sensibilidad temporal. Verificar integridad antes de interpretar. | Separar una curva atractiva de evidencia defendible. | Lista corta y motivos; muestra insuficiente no se convierte en aprobación automática. |
| 5. Validar resistencia | Definir juntos estrés de costos/ejecución y robustez pertinente; ejecutar sólo el protocolo acordado, conservando resultados desfavorables. | Saber si la utilidad sobrevive a supuestos adversos. | Sobrevive con límites explícitos, queda inconclusa o se descarta; sin aumento de riesgo ni rescate automático. |
| 6. Comprobar operabilidad BTC | Si existe candidata validada, proponer seguimiento controlado y verificar que reglas, datos, órdenes y contabilidad puedan reproducirse. | El backtest no demuestra ejecución real. | Plan técnico y decisión específica antes de paper/live. No hay espera de 12 meses prefijada ni autorización para operar. |
| 7. Otras operativas individuales | Retomar PAXG y SPY cuando se decida, partiendo de sus antecedentes, instrumentos y costos propios. | Construir piezas evaluables por sí mismas. | Evidencia individual con sus límites; no exigir simetría long/short por defecto ni asumir rentabilidad por tendencia macro. |
| 8. Combinación eventual | Estudiar capital, simultaneidad y aporte marginal cuando haya piezas defendibles. Considerar también diversificadores de retorno modesto. | Comprobar qué mejora realmente al operar juntas. | Decisión conjunta posterior, con riesgo y ejecución explícitos; no suma automática de curvas. |

Las etapas 7–8 son horizonte futuro; no distraen el trabajo BTC actual. Si BTC alcanza antes una fase operativa defendible, no necesita esperar a completar los otros activos; cualquier operación real requiere autorización específica.

## Cómo se avanza sin quedarse atrapados
Un objetivo exigente no garantiza que aparezca una candidata. Cada tanda futura tendrá presupuesto y criterios de cierre: ni búsqueda interminable ni rebajar puertas para aprobar. Si falla, registrar qué hipótesis pierde respaldo y proponer una dirección materialmente diferente basada en evidencia. No seguir añadiendo filtros hasta que el histórico encaje.

La aceptación de estos objetivos define dirección, no constituye un protocolo prerregistrado. Los cortes nuevos no cambian los veredictos históricos. Las siguientes ejecuciones requieren especificación concreta; esta entrega sólo publica acuerdos y roadmap. No se hicieron backtests, replays, análisis jobs, imports, cambios de estrategias/configuración ni live/paper.

## Continuidad y precedencia
Esta r9 reemplaza el estado «cifras propuestas» de r8 por objetivos aceptados por el usuario y difiere el estrés hasta candidatas. R7 no aprobada permanece superada; su cartera de ocho libros y espera de doce meses no rigen. R5/r6 conservan evidencia y conclusiones originales. R4 conserva el mapa de exploraciones para evitar repeticiones. AGREEMENTS.json es el resumen estructurado vigente.
