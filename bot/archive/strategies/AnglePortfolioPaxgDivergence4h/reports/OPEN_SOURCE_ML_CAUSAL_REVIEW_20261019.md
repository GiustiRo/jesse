# Investigación crítica: Pine ML, aprendizaje online y estados

19/10/2026. Lectura de fuentes primarias públicas y protocolos locales; sin instalar, descargar datasets, crear scripts, importar modelos o ejecutar análisis/backtests. No se consultaron precios ni resultados de 2026. La reapertura humana de funding pertenece a otra línea; no se mezcla aquí.

## Recomendación concreta

Priorizar **un único observador causal multiescala con evaluación prequential retrasada**, ya diseñado por allocation, aprovechando el contrato de evaluación de River como referencia de ingeniería. No portar ahora el clasificador Pine ni introducir un HMM. Esta recomendación no pide otra familia de reglas ni una segunda implementación competidora: primero comprobar si nuestra representación añade información frente a su benchmark incondicional.

El protocolo local leído es strategies/OrchManageTurtleDaily/reports/ANGLE_CAUSAL_MULTISCALE_OBSERVER_PROTOCOL_20261018.md. Ya especifica estados U/D/M de pivots diarios y 4h confirmados, fallback unknown, tres resultados de primera barrera en 24h, ventana180d y contracción20. Mantener esos valores sin optimización. No es continuación del intento anterior de cuatro signos y gate mean−SE, ni promete beneficio.

## 1. Pine Lorentzian/kNN: código real accesible, no señales listas para copiar

Se consultó la [publicación original de jdehorty](https://www.tradingview.com/script/WhBzgfDu-Machine-Learning-Lorentzian-Classification/) y el [repositorio de puertos mantenido por AI Edge](https://github.com/artificial-intelligence-edge/lorentzian-classification). Este último ofrece una referencia Pine y puertos; no verifiqué que su snapshot sea idéntico a la revisión actualmente cargada en TradingView. Paridad entre puertos tampoco prueba rentabilidad.

**Auditoría del fichero Pine inspeccionado:** distancia = suma log(1+|diferencia de feature|), no geometría física que identifique eventos macro. La etiqueta compara precio actual con cuatro barras anteriores: una subida100→104 produce short(−1), guardado junto a features actuales. No equivale a asociar el feature anterior con un outcome forward maduro; tampoco demuestra por sí solo fuga de precio futuro. El ANN usa d>=lastDistance y i%4!=0, no un top-k estándar ordenado por menor distancia; conserva votos entre barras. Su suma de votos no es probabilidad calibrada. La selección depende además de last_bar_index: requerir invariancia por prefijos antes de usarla como predictor histórico. Son diferencias auditables, no una acusación de que todo kNN falla. [Código Pine v6](https://raw.githubusercontent.com/artificial-intelligence-edge/lorentzian-classification/main/ports/pinescript/lorentzian-classification-v2.pine).

La referencia está marcada MPL-2.0, mientras los puertos del repositorio se ofrecen MIT con excepción explícita para Pine y sus bibliotecas. Conservar procedencia y avisos si se reutilizara código; no tratar la cabecera MIT general como permiso para borrar MPL de esos ficheros. La [FAQ oficial de Mozilla](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) explica el copyleft por archivo y las obligaciones al distribuir modificaciones. No se copió código al proyecto.

**Latencia y repaint:** las condiciones intrabar basadas en HLC pueden variar hasta el cierre. TradingView documenta que confirmar la barra introduce una latencia real y que pivots dibujados hacia atrás no estaban disponibles en su extremo. La prueba propia debe usar sólo cierres confirmados y timestamps de disponibilidad, no imitar la posición visual de una flecha. [Documentación oficial](https://www.tradingview.com/pine-script-docs/concepts/repainting/). El nombre non-repainting o un screenshot no certifican causalidad de features, labels y ejecución.

También se leyó la biblioteca referenciada del repositorio. Su cálculo ilustrativo de performance usa una unidad y precios sintéticos o close según opción; no modela nuestra cuenta, fees, STOP, capital o margen. Además el snapshot inspeccionado exporta analyzePerformance, mientras el indicador llama ml.backtest: exige verificar versiones de bibliotecas remotas antes de alegar reproducción ejecutable. No se compiló y no se concluye que la biblioteca realmente publicada en TradingView sea incompatible. [MLExtensions inspeccionada](https://raw.githubusercontent.com/artificial-intelligence-edge/lorentzian-classification/main/ports/pinescript/libraries/MLExtensions.pine).

Qué aprovechar: separación explícita de features, distancia, memoria y filtros; auditoría de paridad y contratos de disponibilidad. Qué descartar ahora: importar sus señales, su tabla de acierto o el stack de filtros como una ventaja verificada. Si más adelante se estudia kNN, deberá ser una receta nueva, con features guardados al origen y labels que sólo se incorporan cuando maduran; eso ya no sería una réplica literal de este Pine.

## 2. River: aprovechar el proceso de evaluación antes que otro algoritmo

River documenta predicción seguida de evaluación y aprendizaje; progressive_val_score permite retrasar la revelación de la etiqueta mediante moment/delay. El valor por defecto no introduce retraso: no sería correcto usarlo sin adaptación para un outcome24h. Debe puntuarse la distribución emitida y archivada antes de ese horizonte, no una predicción recalculada tras aprender el resultado. [API oficial](https://riverml.xyz/latest/api/evaluate/progressive-val-score/) y [código del evaluador](https://github.com/online-ml/river/blob/main/river/evaluate/progressive_validation.py).

La biblioteca también implementa regresión softmax online con predict_proba_one/learn_one. Eso ofrece una alternativa multiclase conocida, pero sus probabilidades no quedan empíricamente calibradas por elegir esa clase; habría que medirlo en nuestro flujo. No propongo añadirla al primer prototipo: crearía otro modelo e hiperparámetros antes de demostrar valor en la representación simple. [SoftmaxRegression](https://riverml.xyz/latest/api/linear-model/SoftmaxRegression/).

Su licencia es [BSD-3-Clause](https://github.com/online-ml/river/blob/main/LICENSE). No se verificó disponibilidad en el entorno ni se solicita instalarlo. Podemos aplicar el contrato conceptual de evaluación sin copiar o incorporar el paquete.

Aplicación exacta al observador: guardar estado y vector emitido en T; mantener episodios hasta T+24h; puntuar sus vectores originales; recién entonces aprender. Normalización, estados y entrenamiento no ven observaciones posteriores a su fecha. El prior y benchmark usan el mismo universo; unknown, censura y ambigüedad se conservan conforme al protocolo. La estructura de dependencia temporal sigue existiendo: online no significa independiente ni OOS limpio.

## 3. HMM: útil como hipótesis de régimen, mayor riesgo de evaluación engañosa

hmmlearn documenta decodificación Viterbi/MAP sobre secuencias. Su implementación de posteriors combina forward y backward. Por tanto, asignar estados históricos obtenidos sobre toda2020–2025 y tratarlos como señales conocidas entonces usaría información posterior. Un modelo ajustado sólo con pasado y filtro forward es otro contrato; alternativamente el último posterior de un prefijo sólo ve ese prefijo. No hay permiso para suavizar retrospectivamente la historia y llamar a eso detección en vivo. [Código oficial](https://github.com/hmmlearn/hmmlearn/blob/main/src/hmmlearn/base.py) y [API](https://hmmlearn.readthedocs.io/en/stable/api.html).

El estado latente no es por naturaleza bullish/bearish: interpretar emisiones, reestimar parámetros y alinear etiquetas añade decisiones. Número de estados, forma de emisión, ventana, reinicios y transición son grados de libertad que no necesitamos para la primera prueba. Descartar **esta integración ahora**, no la familia universalmente. La [licencia del proyecto](https://raw.githubusercontent.com/hmmlearn/hmmlearn/main/LICENSE.txt) exige conservar avisos; no se incorporó su código.

## Comparación con el observador propio

| Familia | Qué añade | Problema principal ahora | Decisión |
|---|---|---|---|
| Pine/kNN abierto | Similitud entre features y memoria de vecinos | Semántica de labels, ANN particular, versiones y publicidad frente a ejecución | No portar señales |
| Online/prequential | Disciplina para predecir, puntuar y aprender con retraso | No crea edge; el delay y los targets deben coincidir con nuestro reloj | Adoptar el contrato metodológico |
| HMM | Estados latentes y persistencia | Suavizado futuro, ajuste e interpretación añaden complejidad | Posponer |
| Observador ya propuesto | Representación causal pequeña, benchmark emparejado y targets de barrera | Aún no sabemos si añade información y falta persistencia auditada | Primer y único prototipo recomendado |

Antes de autorizar su ejecución, cerrar almacenamiento auditable de cada pronóstico y label. El prototipo no opera ni cambia la cartera. Mantener la comparación Brier/logloss, cobertura y calibración sobre fechas idénticas; incluir unknown y startup, bounds de ambiguos y cohorte diaria predeclarada sin solapamiento. La hora00UTC no se selecciona por ser la mejor.

Si el observador no mejora la información frente al incondicional de forma estable, archivarlo sin mover pivots, escalas, barreras o smoothing. Si mejora, sólo habilita revisar una política económica posterior y sus costes; no convertir argmax en órdenes ni inferir65/80 o un70% de winrate. La búsqueda acumulada sobre2020–2025 sigue siendo desarrollo. No se abre2026.

## Estado del trabajo

Se inspeccionaron fuentes primarias de las tres familias y código/licencia de una implementación Pine real, sin ejecutar ni copiarla. No se descargaron datasets de ejemplo de esos repositorios. El único cambio de proyecto de esta revisión es este informe; el patch diagnóstico PAXG se realizó por encargo root separado y sin modificar alpha. No hay instalación, fuente ML, script, draft o run nuevo autorizado por este documento.
