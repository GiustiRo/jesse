# K1001: bloque creativo posterior, selección adversa de la ejecución pendiente

Estado: UNA pregunta documental para discusión posterior a los dos escenarios. No es protocolo económico ni autorización de estrategias, jobs, precios, cambios de TTL o nuevas corridas. Se elige una sola pregunta porque una segunda sobre devolver excursiones favorables ya está cubierta por el diagnóstico y el Rtrace previsto; renombrarla como novedad repetiría trabajo.

## Pregunta económica

¿Parte de la debilidad de2024–2025 reside en que el mecanismo de orden pendiente selecciona las oportunidades que efectivamente llenan, en lugar de que haya empeorado por igual toda señal original?

Una señal y su fill son objetos distintos. El long compra un retesteo mediante LIMIT; los dos shorts venden una ruptura mediante STOP. El precio puede alcanzar la orden porque la tesis se confirma, porque revierte el movimiento que originó la señal, o porque llega tarde una ruptura ya degradada. La ejecución no es necesariamente una muestra aleatoria de las señales. La antigüedad señal→fill y el gap requested_entry→actual_entry son marcas observables de esa selección, sin ser por sí mismos medidas de liquidez u orderflow.

Hipótesis falsable, todavía sin receta: la caída del payoff bruto/neto normalizado se concentra en una forma observable de ejecución dentro de cada origen y año, y no aparece sólo al mezclar long LIMIT con short STOP. Su rival es que el menor payoff refleje el mercado posterior a la entrada, mezcla de años, régimen de volatilidad, tamaños o simple variación de muestra, sin relación reproducible con la ejecución pendiente.

## Qué evidencia actual favorece o debilita investigarla

El diagnóstico mostró que2024 tuvo42 fills y2025 tuvo34: no fue simplemente falta de operaciones respecto a2021–2023. Cayeron las medias R bruta y neta. Existen313 planes,192 fills y121 cancelaciones, de modo que hay selección real entre plan y ejecución. Los trades enlazados incluyen signal_at, requested_entry, actual_entry y opened_at. La espera media observada fue aproximadamente34min en long,61min en core y47min en suplemento: esos promedios justifican preguntar por el proceso, pero NO demuestran una relación con resultados ni comparabilidad entre tipos de orden.

La evidencia también limita la idea. No están registrados todos los candidatos descartados por ocupación, y los no-fills no tienen payoff contrafactual. La antigüedad depende de la trayectoria de precio y no es una variable asignada aleatoriamente. Un fill inmediato puede ser bueno o malo; un fill lento también. Las muestras por origen/año son pequeñas, sobre todo los31 longs y45 suplementos. Los tres grandes long explican gran parte del neto, pero eso no permite afirmar que entraron demasiado tarde ni cambiar su trailing.

## Evidencia mínima que resolvería algo, sin convertirla ahora en análisis autorizado

Primero conservar los resultados completos de ambos escenarios y sus registros reales. Si root decide profundizar, los metadatos ya existentes permiten una descripción continua de espera, diferencia requested/actual normalizada por distancia inicial y net/gross R dentro de cada origen, con tablas por año y casos individuales auditables. No seleccionar cortes de minutos buscando el mejor PnL, ni convertir de inmediato una correlación ex post en filtro. Distinguir gaps de STOP de mejora de LIMIT según lado; no llamar a ambos slippage y no imputar comisión adicional no modelada.

Antes de dar cualquier explicación causal haría falta saber qué mecanismo de ejecución se está aislando. El ledger de fills por sí solo NO identifica el rendimiento de órdenes canceladas o entradas a mercado alternativas. Si sólo aparece una correlación frágil, desaparece dentro de origen/año, o depende de uno de los tres grandes long, la pregunta no justifica otra corrida.

## Qué decisión podría cambiar

Una respuesta negativa o no identificable preservaría las órdenes y TTL originales y evitaría gastar motores en modificar ejecución. Una asociación estable y económicamente interpretada sólo justificaría debatir un contraste FUTURO expresamente acotado de política de entrada, conservando señal, riesgo, costos y gestión; todavía no define ni autoriza tal contraste. Dado el cierre deP y vecinos, haría falta una nueva revisión de alcance antes de cualquier receta. No basta que el resultado de los escenarios decepcione para abrirla.

No se propone cambiar TTL4h, entrar a mercado, seleccionar fills rápidos, reducir stops, retirar costos o aumentar cuota. Tampoco se promete que una variante mejore: cambiar la orden puede cambiar quién llena, el precio, el riesgo efectivo y la selección posterior.

## Control de repetición acotado

Fuentes leídas: K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md; K1001_DEEP_DIAGNOSTIC_RESULT_20261021.json y JOIN_CODE_V3; K1001_OCCUPANCY_MEASUREMENT_PROPOSAL_20261021.md y anexo SOURCES; BTC_DISCOVERY_P_PROTOCOL_20261021.md y FINAL; card BTC_R14 de Hub r6; revisión r8 y Hub r26.

- R14: quitar suplemento o filtrar long por eficiencia/EMA120 no mide la selección de fills condicionada a la misma señal y política pendiente. Sus negativos se preservan; no se reabren esos filtros.
- P ya audita TTL, fills del minuto de expiry, cancelación y rearmado: esta pregunta NO pretende descubrir un error de broker ni corregir su reloj. El cierreP excluye rescates de ejecución/gestión por PnL; este documento no lo deja sin efecto.
- Propuesta de ocupación HOLD estudia candidatos bajo recursos/prioridad y no-fills del libro. Aquí la variable económica es la selección de EJECUCIONES frente a señales/planes, no el porcentaje de tiempo ocupado. No se reactiva aquel motor ni se supone conocer el universo censurado.
- Diagnóstico existente ya calcula espera señal→fill descriptiva; la pregunta adicional sería su relación con deterioro de payoff, con explicaciones rivales explícitas. No vender el promedio ya calculado como nueva investigación.
- Rtrace previsto describe excursiones durante trades reales. No se propone de nuevo cambiar captura/trailing a partir de extremos observados.
- Las dos cuentas de cuota1% cambian grupo habilitado y capital; no son experimento de antigüedad de orden. No atribuir sus diferencias causalmente a esta hipótesis.

No se afirma ausencia global de antecedentes de ejecución ni novedad algorítmica. Antes de convertir la pregunta en un experimento, habría que revisar las fuentes y cierres exactos de cualquier política de entrada comparable hallada; el inventario documental presente sólo permite mantenerla como pregunta posterior.

Conclusión: conservar una pregunta económica concreta sobre selección adversa de fills. El diagnóstico la hace plausible pero no la resuelve; los registros actuales pueden debilitarla y ahorrar una prueba. No hay segunda propuesta artificial ni autorización experimental.
