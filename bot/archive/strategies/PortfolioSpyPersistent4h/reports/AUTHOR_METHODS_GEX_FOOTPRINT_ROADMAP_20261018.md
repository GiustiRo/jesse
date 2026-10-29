# Roadmap documental: Creamer, GEX, footprint y metodologías de autor

Fecha: 18 de octubre de2026. Sólo documentación y diseño. Sin datasets, compras, instalaciones, scripts, integraciones, nuevas corridas o cambios de estrategia. No se reabrió la adquisición de funding.2026 de rendimiento del proyecto permanece sellado.

## Evidencia y atribución correcta

El [vídeo solicitado](https://www.youtube.com/watch?v=1IuNNXIUnvE) no resultó accesible mediante la herramienta web. NO afirmo haberlo visto ni disponer de transcripción. La descripción metodológica siguiente procede del resumen humano transmitido por root: Nasdaq futures; preparación GEX positiva para rotación/reversión y negativa para expansión/continuación; Call/PutWalls/HVL como zonas; confirmación footprint/orderflow de aceptación o rechazo;1–2trades en los primeros90min. No son reglas completas verificadas ni parámetros automáticamente transportables.

Los [resultados oficiales](https://www.worldcupchampionships.com/world-cup-trading-championship-standings) sí muestran a Christopher Creamer primero en **July2026 Monthly Micro Day Trading Championship**,100.2%, estadoFinal. Es una categoría mensual micro; no implica campeón anual general ni demuestra rentabilidad duradera, representatividad de su operativa, riesgo aceptable para nuestra cuenta o reproducibilidad de cada componente enseñado.

La última combinada del proyecto sigue rechazada según auditoría de root:38/63meses positivos,16/21trimestres yDD26.93%. Este roadmap no declara objetivos alcanzados ni utiliza prestigio competitivo como evidencia sustituta.

## Qué mecanismo merece estudiar

La arquitectura contexto→localización→confirmación→riesgo es más útil que copiar niveles o indicadores:
1. Contexto: una estimación de gamma puede plantear una hipótesis sobre amortiguación/amplificación de movimientos por cobertura, condicionada a posiciones y comportamiento de dealers.
2. Localización: fijar antes del evento zonas calculadas con datos disponibles entonces; una pared no es orden de compra/venta.
3. Confirmación: observar la respuesta al llegar a la zona y una transición posterior, no inferir el orden de eventos desde una sola vela.
4. Riesgo: invalidación estructural observable, tamaño por pérdida monetaria y costes; límites de sesión/actividad como disciplina, no obligación de operar.

Gamma positiva podría ser compatible con ventas de cobertura al subir y compras al bajar; negativa con refuerzo del movimiento. Eso es un mecanismo condicional de cobertura, no una predicción infalible ni una dirección. El estudio de Amaya/Garcia-Ares/Pearson/Vasquez usa SPX/SPXW y reconstruye posiciones con registros que identifican capacidad y lado de participantes. Estima un impacto típico amortiguador y episodios de amplificación de magnitud limitada frente a otros movimientos; no demuestra que toda ruptura de una gammawall sea negociable. [Paper alojado por Cboe](https://cdn.cboe.com/resources/education/research_publications/gammasqueezes.pdf).

No trasladar sus conclusiones SPX directamente a MNQ, Bitcoin o PAXG. Su cobertura de datos tampoco prueba que hoy tengamos una serie minorista equivalente y disponible2020–2025.

## Footprint real, OFI y proxies: objetos diferentes

Un footprint requiere volumen ejecutado por nivel de precio y clasificación de agresor/lado (o trades sincronizados con mejoresbid/ask para clasificar). Sierra distingue bid/ask traded volume, delta y comparaciones diagonales; NumbersBars no necesita por sí mismo profundidadL2 completa. [Documentación técnica Sierra](https://www.sierrachart.com/index.php?page=doc/NumbersBars.php).

El order-flow imbalance de Cont/Kukanov/Stoikov incluye eventos de órdenes límite, cancelaciones y operaciones en mejoresbid/ask; no equivale al delta de trades de una footprint. Su evidencia de impacto a corto horizonte en50accionesUS no prueba una estrategia rentable transferida a tres activos tras9bps de comisionesRT. [Artículo de los autores](https://arxiv.org/abs/1011.6402).

Una candidata a absorción sería agresión importante sin progreso equivalente y luego un cambio confirmado de flujo/precio. No observa automáticamente un iceberg, inventario institucional ni manipulación. Para afirmar reposición de liquidez harían falta quotes/profundidad/eventos adecuados; incluso éstos no revelan toda liquidez oculta.

Con OHLCV no podemos reconstruir quién agredió cada precio, cancelaciones o secuencia interna. Dividir volumen según color de vela, tick-count, RSI o posición del cierre produce un proxy. La ocupación M1 de rango que ya probamos sigue siendo una variable de precio; no se renombra footprint para presentarla como información nueva.

## GEX estimado no es inventario dealer observado

Una exposición nocional aproximada por un movimiento de1% suele adoptar la forma Σ(n_dealer*gamma*multiplier*S²*0.01), con unidades y convención de signo declaradas. La parte difícil es n_dealer: el OI agregado no identifica automáticamente a su dueño ni si el dealer está long/short.

Longcalls y longputs tienen gamma positiva; asignar signos opuestos sólo por ser call/put es una convención de estimación, no inventario observado. CallWall/PutWall/HVL necesitan definiciones reproducibles y versionadas; vendors pueden usar convenciones distintas. Las posiciones inferidas con capacidad/lado de operaciones tampoco equivalen a inventario global completo de todos los dealers.

Hay que conservar cadena de opciones, strikes, expiries, multiplicadores, OI conocido, IV/modelo/Greeks, tipo de opción, precio subyacente, timestamps y correcciones. Un OI publicado al día siguiente no se usa intradía el día anterior. Greeks históricos entregadosT+1 no demuestran disponibilidad del producto intradía; recomputarlos con cotizaciones causales sería otro procedimiento explícito. [Producto oficial Cboe conGreeks,T+1 e inicio anunciado2019](https://datashop.cboe.com/us-options-trade-by-trade-greeks). Ese producto es propietario y no es una descarga gratuita ni un inventario dealer.

## Matriz de viabilidad por activo

| Activo / datos presentes | Datos reales para trigger | Datos para contexto GEX | Viabilidad histórica2020–25 / decisión |
|---|---|---|---|
| BTC perp: M1 OHLCV de Binance | Trades con precio/tamaño/agresor, reloj ordenado y correcciones; quotes si se clasifica porbid/ask; L1/L2 si se estudian cancelaciones/reposición/OFI. Sólo describen la venue observada. | OpcionesBTC de venue identificada, cadena/OI/Greeks/IV asof y supuesto de dealer explícito. Funding no es GEX. | La historia de esas capas no se auditó. OHLCV actual no contiene footprint. Primero viabilidad de trades/quotes por contrato; GEX no es requisito para un trigger de microestructura independiente. |
| PAXG: M1 OHLCVSpotproxy | Trades agresores propiosPAXG para flujo del token. GCfutures sería un mercado externo con contratos, rolls, calendario y transmisión por validar. | Opciones sobre instrumento de oro identificado (por ejemploGC/GLD si se obtuvieran), no opcionesPAXG supuestas. Mapeo de subyacente/basis/moneda necesario. | No hay datos verificados de estas capas. El volumenPAXG no representa todo el oroOTC/CME. Prioridad baja para “GEX de oro” hasta demostrar vínculo económico con el token ejecutado. |
| SPY-USDT actual: SPXCFDBID/10, volumen0 y huecos | Trades/quotes de ES o del ETFSPY negociado; SPX cashindex no tiene una footprint de trades propia. ETF requiere tratar fragmentación/quotes/auctions; ES requiere contrato/roll. | Cadena históricaSPX/SPY u opciones del futuro elegido, con OI/publicación y estimación de posiciones. No confundir todos esos productos. | La fuente actual NO soporta footprint, profile de volumen real ni GEX. Hay productos históricos oficiales, pero cobertura completa, licencia, coste y disponibilidadasof no están verificados. Mejor correspondencia conceptual GEXíndices, mayor necesidad de datos nuevos. |

La nueva hipótesis debe elegir instrumento de señal y de ejecución. ES/SPY/SPX/CFD, GC/GLD/PAXG y BTCSpot/perp/opciones no se sustituyen por factor10 o correlación verbal. La transferencia requiere sincronización, basis, horarios y ejecución conservadora.

No inventarRTHNYSE a partir delCFD actual. Los primeros90min del resumen no son aplicables a BTC24/7 ni al históricoSPY con su sesiónUTC heredada sin un nuevo diseño de calendario y DST. Tampoco trasladar un umbral absoluto de contratosMNQ a BTC o PAXG.

## Diseño incremental de hipótesis, todavía sin parámetros de prueba

Primer candidato conceptual para índices, SI datos fiables existen: contexto de gamma positiva estimada conocida antes del evento; llegada a una zona previamente congelada; agresión que no consigue continuación; después un cambio de dominancia y recuperación confirmada en un intervalo posterior. Riesgo más allá de la invalidación estructural con colchón de coste y sin perseguir un stop microscópico. El contexto negativo se trataría como hipótesis distinta de aceptación/continuación, no se mezcla para rescatar retrospectivamente.

Para BTC podría estudiarse primero agresión/progreso y recuperación con trades reales del propio perp, sin atribuirlo a dealers de opciones ausentes. Para PAXG puede convenir otra metodología completamente distinta; no existe obligación de forzar footprint/GEX en los tres.

Antes de programar deben fijarse zona, reloj, definición de aceptación/rechazo, normalización de participación usando sólo pasado, expiración y costes. No se fijan aquí umbrales a partir de trades ganadores ni se presenta una réplica exacta del criterio discrecional del autor.

Validación futura por capas:
- Controles de datos y causalidad sin PnL: secuencia, eventos duplicados, huecos, unidades, cotizaciones y disponibilidad.
- Una hipótesis y trigger preregistrados; mantener ejecución/riesgo iguales al comparar trigger solo, contexto solo y ambos. El diseño de ablación no autoriza tres corridas ahora.
- Spread, fees, latencia, fills y funding cuando corresponda. El motor actualM1 y accesoStrategy deben soportar la información requerida sin inventar datos ni eludir restriccionesIO. Si no lo permiten, detener para diseño/aprobación del soporte necesario, no modificar framework por iniciativa.
- Evaluar la cuenta compartida, MTM de todos los meses/trimestres, exposición, concentración, adversidad y muestras; no sumar independientes. No confundir mejorwinrate con expectativa.
- Congelar selección antes de2026. Todo2020–2025 sigue siendo desarrollo muy observado; un walk-forward hecho ahora no vuelve virgen su selección.

El límite de1–2trades/sesión del resumen puede convertirse en una política de riesgo/operativa, pero no certifica edge. “Eliminar operaciones malas” sólo puede significar reglas causales y adherencia medible, nunca eliminar trades porque luego perdieron.

## Tres metodologías adicionales documentadas por autores

1. **LarryWilliams: expansión de volatilidad/rango.** Su propio texto describe entrar al expandirse el rango respecto a una referencia de apertura/cierre y reconoce que la técnica funcionó peor posteriormente. [Fuente del autor](https://www.ireallytrade.com/innovation/). Requiere OHLC y definición de sesión; posible como familia de contexto/trigger, pero solapa las rupturas/compresión ya probadas. No es una nueva prueba autorizada ni una razón para otra rejilla de períodos. No importamos su retorno competitivo como retorno esperado.

2. **LindaBradfordRaschke: HolyGrail, pullback dentro de tendencia fuerte.** Entrevista primaria alojada por la autora documentaADX14>30 creciente, retroceso aEMA20, confirmaciónSTOP sobre barra previa y protección en swing. [Documento original1997, páginas2–3](https://lindaraschke.net/wp-content/uploads/2026/01/august1997.pdf). Es metodología concreta, no prueba empírica contemporánea. Solapa tendencia/pullback/ADX de nuestro inventario; queda catálogo/contraste antes de decidir si existe una diferencia material. No le atribuyo un título competitivo no verificado ni adoptamos sus afirmaciones probabilísticas como evidencia del proyecto.

3. **KevinDavey: desarrollo sistemático y cartera robusta.** Su documentación exige reglas claras, costes, walk-forward, control de sobreajuste, diversificación e incubación; también advierte que reiterar ajustes contamina los resultados. [Fuente del autor](https://kjtradingsystems.com/). Es proceso de investigación, no una entrada alpha. Adaptación inmediata: registrar hipótesis negativas, separar aprendizaje y aceptación y no declarar OOSlimpio sobre años ya observados. Nuestro remuestreo debe respetar dependencia/calendario; no copiar un shuffle de trades como certificación conjunta.

Son fuentes de los autores, algunas con productos comerciales. Eso acredita procedencia de la descripción, no eficacia, independencia ni necesidad de comprar. No se abre ninguna prueba por autoridad o por resultados de concursos.

## Bloque listo para el registro central

Añadir línea “metodologías de autor por activo”, empezando con Creamer y separación contexto→zona→confirmación→riesgo. Estado documental, sin adquisiciones ni pruebas. Verificado: primeroJuly2026MonthlyMicro, no campeón anual general; vídeo no visionado, resumen humano atribuido.

FaseA: matriz por activo de datos, fuente/licencia, contrato, cobertura2020–25 y disponibilidadasof; diferenciar footprint real/OFI/proxies y GEXestimado/inventario.
FaseB: controles de reconstrucción causal sin rendimiento.
FaseC: una hipótesis mecanística y trigger explícitos, revisión y ablación de capas con ejecución/costes iguales; sólo después autorización de corridas.
FaseD: cartera compartida, robustez y congelación;2026cerrado hasta cumplir ese proceso. Objetivos originales intactos; última cartera sigue rechazada.

SPYactual no soportaGEX/footprint; BTCnecesita trades/quotes para microestructura y opciones si se añadeGEX; PAXGexige validar su mercado propio o transmisión desde oro externo. No forzar el mismo sistema en los tres. Catálogo adicional Williams/Raschke/Davey con chequeo de duplicación antes de investigar. No se autoriza comprar, instalar, descargar o editar framework por incorporar este roadmap.
