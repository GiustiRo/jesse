# Observador causal BTC de estructura multiescala — protocolo experimental
Fecha: 2026-10-18. Estado: DISEÑO SOLAMENTE. No fuente, draft, backtest, análisis/job, framework, script ni dato externo nuevos. Propiedad propuesta AngleBtcStructureObserver1m, aún sin crear. Esta línea es paralela a la investigación principal de cartera, no sustituye la referencia ni consume capital.

## Pregunta y diferencia respecto del intento anterior

¿Una descripción causal pequeña de la estructura diaria y4h mejora probabilidades de primera barrera en las próximas24h frente a ignorar el estado, sobre las mismas fechas?

Se leyó por MCP AngleBtcProbability4h y el inventario/resultado central. El experimento anterior usaba cuatro estados por signos de dos retornos4h, labels de payoff monetario long/short de una sola barra, stop3ATR, ventana1.080 y gate heurístico mean−1SE. Con datos válidos no superó el gate y produjo cero trades. No se afloja aquel gate ni se presenta esta línea como continuación exitosa.

Aquí cambian materialmente representación (pivots1D+4h confirmados), horizonte24h y objetivo (probabilidad de tres eventos de primera barrera, no expectativa monetaria ni decisión). El benchmark incondicional recibe exactamente las mismas observaciones admisibles y se compara con proper scoring rules prequentiales. La evaluación no genera operaciones y no puede declarar CAGR, winrate de trading ni cumplimiento65/80. Sigue siendo desarrollo adaptativo2020–2025; no reinicia historial de selección.

## Datos y reloj causal

Sólo BTC Binance histórico existente. Trading route técnica1m sin órdenes, auxiliar4h; las llamadas de estrategia procesan cada M1 cerrada y sólo calculan un nuevo pronóstico al cierre4h UTC. get_candles4h se filtra por apertura+4h≤timestamp actual. Confirmar paridad del cierre4h con la M1 que termina en ese mismo instante. Datos inválidos/faltantes generan motivo explícito de ausencia, no imputación.

Construir velas1D UTC exclusivamente con seis bloques4h cerrados de aperturas00,04,08,12,16,20 de una misma fecha, contiguos y finitos: open primero, close último, high máximo, low mínimo y volumen agregado sólo como campo contable, sin feature de volumen. Una fecha incompleta no es una vela diaria negociable ni desplaza el reloj de los días siguientes. No usar la vela diaria en formación ni ampliar warmup a240D.

Las240 barras4h del warmup original permiten unos40 días de estructura previa. Se pueden inicializar pivots con esa historia ya conocida, pero NO entrenar con labels de warmup ni emitir pronósticos retrospectivos puntuados. Si todavía faltan pivots, emitir el benchmark incondicional en ambas salidas con flag structure_unknown; no omitir la fecha del score global. No obtener resultados2026 ni agregar otra fuente.

## Pivots y tres estados, fijados antes de implementar

En cada escala, una barra candidata j es pivot high si su high es estrictamente mayor que los highs de las dos barras anteriores y las dos siguientes; pivot low análogo estricto. Se publica sólo al cerrar j+2. Exigir que las cinco barras sean contiguas en el reloj de esa escala. Empates no son pivots. Si una misma candidata cumple high y low, descartar ambas marcas por ambigüedad de secuencia, sin escoger según precio posterior.

Guardar tiempo de extremo Y tiempo de confirmación. Nunca insertar un pivot nuevo como información disponible en la fecha del extremo ni repintar estados/pronósticos previos. Mantener por escala los dos últimos highs y dos últimos lows confirmados:
- up: ambos highs y ambos lows crecientes;
- down: ambos highs y ambos lows decrecientes;
- range: las restantes configuraciones con dos pivots de cada tipo disponibles.
Si faltan esos cuatro pivots en alguna escala, structure_unknown, distinto de range: emitir exactamente p0 como predicción del observador y mantener el episodio en scores globales. Informar por separado coverage de estados conocidos.

Estados finales únicamente tres: U si1D y4h son up; D si ambas down; M si ambas escalas están disponibles y no cumplen los dos acuerdos anteriores. No usar nueve cruces, distanciasFibonacci, amplitud de ondas,30 features ni filtros adicionales. Las estructuras se invalidan/reclasifican objetivamente al confirmarse pivots que dejan de cumplir su relación; no se reetiqueta el pasado.

La inspiración Elliott se limita a describir secuencias de máximos/mínimos y distinguir continuidad de estructura mixta. No se identifica una cuenta verdadera de cinco/tres ondas ni se atribuye causalidad a Elliott. Un eventual desarrollo distinto necesitaría protocolo propio; no se añade después de ver este resultado.

## Episodios y labels de primera barrera

En cada cierre4h T con quote y ATR válidos, congelar estado conocido o flag unknown, referencia x=closeBTC(T), ATR14 sobre4h cerradas, barreras U=x+ATR y L=x−ATR, deadline=T+24h, y ambas distribuciones pronosticadas antes de observar minutos posteriores. Rechazar ATR no positivo/no finito o L≤0. Ningún stop/riesgo de trading interviene.

Procesar incrementalmente las M1 del intervalo de aperturas[T,T+24h), conocidas al cerrarse cada minuto. Como hay un episodio cada4h, se solapan hasta seis horizontes activos. No intentar recuperar1.440 minutos desde un buffer corto al llegar el deadline; cada episodio conserva sólo primer evento, flags de cobertura y el próximo minuto esperado.

Regla de orden dentro de una M1:
1. Si su open≥U, primera barrera up; si open≤L, down: la apertura observada resuelve el orden incluso con ambas mechas.
2. Si la apertura está estrictamente entre barreras, high≥U y low≤L en la misma M1 constituye ambigüedad intraminuto: no elegir dirección, no usar el close para inventar cuál barrera fue primero.
3. Si sólo toca una, ésa es la primera. Tras resolver, no reemplazarla por un evento posterior.
4. Si no toca ninguna durante el horizonte íntegro, label none. Tocar exactamente el nivel cuenta como toque.

Todos los episodios, incluso resueltos pronto, maduran y entran a aprendizaje únicamente en T+24h. Se continúa verificando cobertura después del primer toque: faltantes/invalidación de cualquier M1 del horizonte excluyen el episodio del conjunto común, incluso si ya parecía resuelto. Esto evita poblaciones con exigencia de datos distinta según el outcome.

Ambiguos y datos inválidos se conservan como conteos/motivos fuera de las tres clases, sin entrenar ni puntuar una etiqueta inventada. Informar sus tasas por estado/unknown y año y volumen de pronósticos no puntuables: la ambigüedad NO es missing-at-random y la comparación principal queda condicionada a labels observables, sin reclamar una población imparcial. No cambiar las reglas de ambigüedad tras observar su frecuencia.

Para ambiguos con cobertura íntegra, guardar los dos losses posibles (up/down) de cada vector emitido, sin entrenarlos. Presentar bounds descriptivos de la diferencia pareada de score: para cada ambiguo calcular Δup y Δdown (observador menos baseline), sumar sus mínimos/máximos a los deltas conocidos y dividir por el número total de episodios íntegros, incluidos ambiguos. Así el intervalo limita optimista/pesimista el score diferencial bajo cualquier orden intraminuto compatible, no inventa etiquetas ni resuelve pérdidas de cobertura. Hacerlo para Brier y logloss; el label none no es compatible con ambos niveles tocados.

Al terminar, episodios sin24h completas se etiquetan right-censored y no se entrenan ni puntúan. No acortar el horizonte ni usar el cierre terminal como outcome none.

## Aprendizaje y comparación prequential, sin gate

Ventana fija de180 días civiles anteriores por fecha de origen del episodio, no las últimas1.080 filas válidas que estirarían el período cuando faltan datos. Las1.080 posiciones de pronóstico4h equivalen al techo nominal de180d; el horizonte pendiente y los descartes reducen la muestra madura real. No cambiar ventana según resultados.

En cada instante T:
1. Procesar la M1 que acaba de cerrar y madurar episodios con deadline≤T; sus labels son ya conocidos.
2. Puntuar sus vectores GUARDADOS cuando se emitieron; nunca recalcular esa predicción con el label recién llegado.
3. Actualizar conteos sólo con los labels maduros admisibles y retirar del entrenamiento orígenes anteriores a T−180d.
4. Actualizar estructura sólo con barras cerradas y emitir el nuevo pronóstico para un episodio futuro.

Benchmark incondicional: p0,k=(N_k+1)/(N+3), prior Dirichlet(1,1,1), aprende de todos los episodios maduros válidos, incluidos unknown. La parte condicional usa los mismos labels globales para su prior p0 y sólo agrega a sus conteos por estado cuando ese estado era conocido al emitir. Un episodio unknown nunca se reclasifica con pivots posteriores.
Modelo de estado: ps,k=(N_s,k+20×p0,k)/(N_s+20). Las20 pseudoobservaciones predeclaradas contraen al benchmark, evitando una distribución extrema con pocos casos. N_s=0 implica exactamente el benchmark. No interpretar esta suavización empírica como certeza bayesiana bajo independencia.

Desde el primer cierre4h con quote/ATR válidos se conservan scores, incluso arranque con prior uniforme y estructura unknown; no suprimir pérdidas iniciales. En unknown el observador devuelve p0 exactamente, por lo que su delta de score es cero, sin ocultar esas fechas del denominador global. Presentar además conteos por tamaño de entrenamiento de forma descriptiva, sin escoger un punto de corte ganador. No n_min para emitir, no mean−SE gate, no elección long/short ni Kelly, y no buscar otro pseudo-count después.

La implementación debe guardar/loguear por episodio: origen, estado y timestamps de confirmación utilizados, x/ATR/barreras/deadline, p0/ps emitidos, conteos maduros disponibles, resultado y motivo de exclusión. El mecanismo exacto de persistencia por herramientas MCP debe revisarse antes de ejecutar: no confiar en vars que no queden archivadas ni crear scripts para suplirlo. No se implementa hasta que root apruebe diseño y almacenamiento auditable.

## Métricas y lectura crítica

Comparación pareada exactamente sobre los mismos episodios maduros:
- Brier multiclase=sum_k(p_k−1[y=k])², menor mejor; logloss=−log(p_y), menor mejor. La suavización mantiene probabilidades positivas; no redondearlas antes de puntuar.
- Diferencia de score condicional menos incondicional, global/por año/por estado y número de observaciones, no sólo el estado o año ganador.
- Calibración one-vs-rest por cada clase en cinco bins fijos[0,.2,.4,.6,.8,1], con conteos y frecuencia observada; no alegar calibración con celdas minúsculas.
- Cobertura de estructura, datos y labels, flags unknown con baseline emitido, ausencias por quote/ATR, ambigüedad, censura final, distribución de clases y concentración de mejora en pocos episodios. Score global incluye unknown; score de sólo estados conocidos se etiqueta como análisis de coverage, no sustituto del global.
- Cohorte descriptiva predeclarada de episodios00UTC cada día: sus horizontes24h no se solapan entre sí. Se evalúa el mismo pronosticador, no se reentrena otra receta ni se escoge la mejor hora. Sirve para advertir cuánto depende el resumen global de solapamiento, no como OOS independiente.

Los seis horizontes superpuestos y estados persistentes hacen falsas las inferencias de N ensayos independientes; no usar errores binomiales IID ni interpretar una diferencia mínima de loss como demostración. La selección acumulada del proyecto persiste. Una mejora debe aparecer de forma consistente frente al benchmark en ambas scoring rules y no estar sostenida sólo por un año o un puñado de casos; estos son criterios de revisión del observador, no sustitutos del objetivo económico.

Si no añade información predictiva, archivar este recipe sin rejilla de pivots/escalas/barreras/horizontes. Si parece prometedor, primero revisión de causalidad/coverage/estabilidad y protocolo posterior de uso económico; probabilidades mejores NO demuestran esperanza después de fees9bpsRT, ejecución, gaps, funding o exposición. No convertir de inmediato argmax en trading ni abrir2026.

## Presupuesto y relación con la fase principal

Un observador, una representación y un benchmark incondicional calculados simultáneamente: no dos estrategias elegidas por desempeño, sin riesgo ni operaciones. Primero revisión de root y almacenamiento; después, si se autoriza, una ejecución de desarrollo. No existe autorización de job/run en este protocolo.

La cartera principal mantiene sus objetivos de regularidad/riesgo y su investigación separada PAXG/SPY. Este observador no añade entradas BTC a esa cartera ni usa sus meses negativos como etiquetas favorables.2026continúa reservado.


## Aclaraciones de review anteriores a implementación
Root confirmó el alcance observacional y fijó explícitamente incluir structure_unknown con fallback incondicional en ambas predicciones y en el score global. Los pivots pertenecen al tiempo de confirmación y los snapshots históricos son inmutables. Ventana180d/shrink20 siguen congelados. Se añadieron bounds descriptivos up/down para labels ambiguos completos, sin entrenarlos ni afirmar que faltan al azar. No código/run mientras se cierra la comparación principal2×2. No se afirma edge ni se habilita trading.


## Implementación provisional autorizada por opt-in ML específico
El usuario pidió explícitamente investigación ML/open source en paralelo; root autorizó UN script MCP: research_scripts/portfolio_roles/causal_multiscale_observer.py. Esto no habilita descargadores funding/VIX/COT, scripts generales, datos externos, instalaciones, red, lectura de secretos ni cambios de framework.

Se leyó jesse://research_scripts. Se escribió y releyó únicamente el prototipo provisional: núcleo causal puro, exportación futura CSV/JSON y modos --self-test / --describe-api. NO se ejecutó. El adaptador DB está deliberadamente AUSENTE hasta confirmar por --describe-api la firma/doc pública del host. Ese modo usa inspect.signature y __doc__, sin inspeccionar implementación ni consultar datos. Root debe revisar todo y ejecutar por MCP ese modo; este agente no lanza jobs.

El núcleo agrega4h desde M1 completos y1D desde seis4h completos, causalmente disponibles sólo al cierre. Define ATR14 Wilder con semilla media de los primeros14 true ranges (primero high-low), explícita y no ajustada a resultados; esta convención técnica debe aceptarse antes de ejecutar con datos. Los self-tests sintéticos cubren confirmación/ties/outside-pivots, estados conocidos/unknown, maduración24h, prioridad de apertura/ambigüedad, ausencia de minutos, censura, expiración temporal, agregación contigua, features invariantes de prefijo y scores pareados. Sus resultados están pendientes de ejecución autorizada, no se afirma PASS.

El adaptador y manifest deben fijar consultas exclusivamente previas al fin exclusivo2025-12-31 y warmup40d; nunca solicitar2026. El prototipo carece todavía de modo full/DB, de modo que el trabajo no se presenta como terminado ni validado. La persistencia acordada son CSV/JSON bajo research_scripts/portfolio_roles/output/ en un subdirectorio nuevo por corrida; ningún pickle/modelo live. El archivo está en el host Jesse y sólo se accedió mediante MCP.
