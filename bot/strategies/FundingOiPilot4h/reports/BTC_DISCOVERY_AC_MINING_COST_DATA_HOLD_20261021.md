# AC — Coste de producción minera: HOLD documental

Fecha: 2026-10-21.
Estado: HOLD por viabilidad de representación. No es un protocolo ejecutable, una estrategia rechazada por rentabilidad ni una candidata.
Alcance: una pregunta económica; cero clases, jobs, drafts, análisis, nuevas velas, importaciones o datasets. No se consultaron resultados de AA.

## Pregunta y motivación

¿La distancia entre el precio de BTC y un coste de producción minera medido de forma independiente contiene información incremental para su rendimiento posterior, o esa distancia sólo refleja la adaptación tardía de los mineros al precio?

La fuente económica sería el beneficio operativo de productores y su ajuste de capacidad; no una transformación adicional de OHLCV. Una eventual restricción de caja podría influir sobre sus ventas, pero el coste por sí solo no demuestra ventas forzadas ni dirección. No se presupone un piso de precio, causalidad ni una oportunidad a 24 horas.

Esta pregunta sería material sólo con una medición externa identificable y disponible en cada fecha. No corresponde elegir ahora umbrales, ventanas o gestión con variables que el contrato no proporciona.

## Literatura primaria y objeción principal

[Adam Hayes, Bitcoin price and its marginal cost of production: support for a fundamental value](https://arxiv.org/pdf/1805.07610). Lectura del modelo, datos, análisis y conclusión. El modelo relaciona precio con costes eléctricos, eficiencia del hardware, dificultad y recompensa. Su aplicación usa supuestos sobre electricidad y datos de eficiencia, y estudia fechas de cambio de dificultad. Es una motivación de valoración histórica, no una validación de nuestra operativa ni de una señal de 24 horas.

[John E. Marthinsen y Steven R. Gordon, The Price and Cost of Bitcoin](https://arxiv.org/pdf/2204.13102), [publicación original](https://doi.org/10.1016/j.qref.2022.04.003). Lectura del resumen y secciones económicas sobre costes, entrada/salida minera y ajuste de beneficios. Su explicación invierte la dirección económica: el precio altera incentivos y capacidad, que luego modifican costes. También separa monedas producidas de monedas efectivamente ofrecidas al mercado. Este contraargumento impide adoptar un piso de coste como hecho.

Las dos fuentes son originales. Se conservan enlaces y paráfrasis breves; no se adjuntan papers ni citas textuales. Las tablas bibliográficas de la segunda no se usan como comprobación directa de los trabajos allí citados.

## Qué falta y por qué no se puede reemplazar

La documentación y los contratos consultados acreditan OHLCV de BTC y el ledger de funding existente. No acreditan una serie histórica de coste minero utilizable as of. La revisión no constituye un censo de todos los ficheros o bases del sistema.

Una medición defendible tendría que especificar, según el modelo escogido, dificultad y recompensa vigentes, eficiencia de equipos, electricidad y cobertura de costes. Cada dato requiere fecha de conocimiento, unidad y procedencia; las revisiones retrospectivas no pueden entrar antes de publicarse. La rentabilidad minera es heterogénea: una media mundial supuesta no equivale al coste marginal observado. Si se afirma presión de venta minera, haría falta evidencia separada sobre existencias y ventas atribuibles; no basta la emisión.

El volumen negociado en un perpetual no mide energía, hash rate, equipos ni BTC vendidos por productores. El funding es un pago entre posiciones del derivado, no coste eléctrico o beneficio de minería. ATR, VWAP, medias de precio y retornos tampoco identifican esos inputs. No se fabricará un coste minero usando estas variables, ni se ajustará retrospectivamente una constante eléctrica para que el precio se acerque a ella.

Incluso con inputs válidos, un ajuste de precio/coste podría ser endógeno o lento. Una relación en niveles no acredita expectativa operable después de comisiones y funding, y menos aún regularidad mensual.

## Deduplicación y alcance de la revisión

Se consultaron por MCP:

- `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r24/revision.json`: estado de investigación al iniciar AC. Ningún resultado AA fue usado.
- `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md`: historial y cierres registrados; búsqueda textual de minería, hash, energía y producción sin equivalente identificado en ese documento.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Z_DOCUMENTAL_DEDUP_NO_EXPERIMENT_20261021.md`: carry/funding ya cubierto y no equivalente al coste físico de producir BTC.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_AB_DISPOSITION_DATA_HOLD_PROPOSAL_20261021.md`: coste de adquisición de tenedores y supervivencia de cohortes. AC se refiere a producción; comparte la exigencia de no inventar inputs económicos ausentes.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_AA_PROTOCOL_20261021.md`: interacción retorno-volumen del derivado; no representa producción. Sólo se leyó el protocolo, sin resultados.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_X_PROPOSAL_HOLD_20261021.md`: integridad del proxy y calendario, problema distinto.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Y_PROTOCOL_20261021.md`: asociación rezagada volumen-amplitud, no energía ni oferta minera.
- `strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md`: límites de atribución de mecanismos económicos a proxies del mercado ejecutado.

El inventario MCP de nombres de estrategias devolvió 645 entradas y no estaba truncado. La búsqueda nominal de minería, hash, dificultad, energía, producción y halving no identificó un mecanismo equivalente; los nombres de coste encontrados correspondían a costes de ejecución. Un nombre no prueba el contenido y esta búsqueda no permite afirmar novedad universal. El listado general de reportes sí estaba truncado y no se trata como censo. La conclusión HOLD no depende de demostrar ausencia global.

No se rescatan vecinos cerrados de R/S/T/U/V, ocupación M1, calendario X, carry Z, disposición AB, Y o AA. No se propone reconvertir una regla legacy de VWAP en valoración minera.

## Falsación y decisión

Antes de cualquier comparación económica, la condición necesaria sería disponer de una medición histórica independiente y causal del coste. Si sólo se reconstruye desde precio/volumen, se falsea la representación propuesta y AC no pasa a motor.

Con datos apropiados, una pregunta posterior podría enfrentar información minera incremental con un control de precio bajo idéntica admisión y ejecución. Serían resultados adversos que la supuesta información desapareciera al controlar la historia de precio, que los costes reaccionaran después del movimiento, o que no aportara expectativa realizada tras costes. Esa comparación no queda autorizada ni parametrizada aquí.

Decisión actual: HOLD. No hay contraste mínimo honesto ejecutable exclusivamente con los recursos documentados. No se importan datos ni se solicita ampliar alcance para salvar esta idea. No se consume presupuesto económico o técnico. El contrato, el riesgo y los gates r9 permanecen intactos; no se modifica la gestión para acomodar una hipótesis de largo plazo.
