# Buscá con presupuesto, validá con datos frescos

Mi respuesta corta es que **sí conviene seguir buscando antes de validar, pero no "hasta que algo funcione"**. Lo que conviene es una búsqueda con presupuesto cerrado, una agenda escrita de antemano y una sola confirmación sobre datos que nadie miró. Inflar N, el número de pruebas, cuesta menos de lo que parece. La vara del Deflated Sharpe crece de forma logarítmica: pasar de 81 a 200 pruebas sobre 5 años sube el Sharpe exigido de ~1,83 a ~1,98. Lo que sale caro es otra cosa. Son las pruebas que no se registran, las decisiones tomadas después de ver resultados (como el mapeo de clases de C0) y las miradas repetidas a los datos reservados. Todo eso infla el N real sin que el registro se entere y, además, arruina el único dato limpio que queda. La literatura coincide en tres puntos. Primero, los Sharpe de backtest caen entre **26% y 73%** al pasar a fuera de muestra. Segundo, trend following es la familia que mejor generaliza entre activos y décadas, y la reversión de corto plazo fuera de índices de acciones no tiene respaldo serio. Tercero, el único fuera de muestra realmente limpio es el trading en vivo o en papel. Tus propios datos dicen lo mismo: el núcleo de tendencia generalizó y la reversión colapsó. Mi recomendación para cerrar el hito es acotar unas 30-40 pruebas nuevas, todas de familias con respaldo (refinamientos de tendencia, carry de funding, momentum transversal). Pasan a confirmación solo si cumplen compuertas de salida preregistradas. Esa confirmación se hace una única vez, sobre una canasta de activos nunca cargados y sobre 2026 solo para motores que no lo tocaron. Después vienen 6-12 meses de paper trading con reglas de corte. Y conviene recalibrar las metas r9 de regularidad, porque hoy exigen un Sharpe sostenido de ~2, que la evidencia no respalda.

## Tres conceptos: N, DSR y PBO

**N** es la cantidad de pruebas independientes que hiciste antes de quedarte con una estrategia. Cuenta cada variante, cada parámetro, cada universo de activos y cada período que probaste, aunque lo hayas descartado. Si las variantes son muy parecidas entre sí (vecinos de parámetros de una misma regla), el **N efectivo** es menor que el nominal. **DSR (Deflated Sharpe Ratio)** es la probabilidad de que el Sharpe verdadero de tu estrategia sea mayor que cero, una vez descontado que elegiste la mejor de N pruebas. También corrige por colas gruesas y por lo corta que es la muestra. Un DSR de 0,95 quiere decir "95% de confianza de que no es pura suerte de selección". **PBO (Probability of Backtest Overfitting)** responde otra pregunta: si tu *procedimiento* de elección generaliza. Parte la historia en mitades de todas las formas posibles (eso es CSCV), elige el mejor en una mitad y mira si en la otra queda por debajo de la mediana. Un PBO cercano a 0,5 indica que tu método de selección no le gana a elegir al azar ([Bailey, Borwein, López de Prado y Zhu 2017](https://escholarship.org/content/qt4w1110bb/qt4w1110bb.pdf)).

## Inflar N cuesta poco en la fórmula y mucho en el proceso

La vara del DSR es el Sharpe máximo esperado de N estrategias sin ninguna ventaja. Ese máximo crece aproximadamente como la raíz de 2·ln N, o sea muy despacio ([Bailey y López de Prado 2014](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf)). La tabla sale de las notas de investigación, que calcularon la Ec. 1 del paper y reprodujeron su valor de referencia publicado:

| N | Sharpe de "pura suerte" (5 años) | Sharpe exigido para DSR ≥ 0,95 (5 años) | Sharpe exigido (13 años) |
|---|---|---|---|
| 10 | 0,70 | 1,44 | ~0,95 |
| 50 | 1,02 | 1,76 | 1,09 |
| 80 | 1,10 | 1,83 | 1,14 |
| 200 | 1,24 | 1,98 | 1,22 |
| 1000 | 1,46 | 2,19 | 1,36 |

En tu caso, el portafolio C0+C6 tiene **Sharpe 1,81 y DSR 0,96 con N=81**, justo en el borde. Con unas 120-150 pruebas más, contadas honestamente y sin correlación, probablemente quedaría por debajo de 0,95 (es una extrapolación de la tabla). Igual, esa no es la cuenta que más importa, por tres motivos.

El primero es que **la vara depende más de la longitud de la muestra que de N**. Pasar de 5 a 13 años divide todas las exigencias por 1,6, y eso pesa mucho más que evitar 100 pruebas extra. El teorema de longitud mínima de backtest dice algo parecido: con 5 años de datos, **no más de unas 45 configuraciones independientes** antes de que el ruido solo produzca un Sharpe de 1 en muestra ([Bailey et al. 2014](https://carmamaths.org/jon/backtest.pdf)). Con N=81 sobre la ventana 2020-25 ya estás pasado de ese presupuesto. La salida natural es evaluar los motores de tendencia sobre tu historia 2011+ (y 2017+ en crypto), no solo sobre 2020-25.

El segundo es que la vara también es proporcional a la dispersión de Sharpe entre tus pruebas. Si las pruebas mezclan familias estructuralmente distintas, la dispersión real supera la del ruido puro y la vara sube. Hay que usar la varianza observada en el registro.

El tercero, y el más grave: **el N que importa es el que no está en el registro**. Simmons, Nelson y Simonsohn mostraron que cuatro decisiones analíticas comunes alcanzan para llevar un 5% nominal de falsos positivos a más de 60%. El "jardín de senderos que se bifurcan" de Gelman y Loken agrega que la multiplicidad existe aunque hayas corrido un solo análisis, si ese análisis habría sido otro con otros datos ([Wikipedia: Forking paths](https://en.wikipedia.org/wiki/Forking_paths_problem)). El mapeo de clases de C0, elegido después de ver resultados previos, es exactamente un sendero bifurcado no contado. Por eso el 0,96 es optimista.

### El Sharpe del ganador está inflado aunque pase el DSR

Pasar el DSR responde "¿es mayor que cero?", no "¿cuánto voy a ganar?". La evidencia empírica sobre esa caída es contundente:

- **McLean y Pontiff** encuentran que 97 predictores académicos rinden **26% menos** fuera de muestra y **58% menos** tras su publicación ([McLean y Pontiff 2016](https://counterpointfunds.com/wp-content/uploads/2017/07/PredictabilityMcleanPontiff.pdf)).
- En 215 índices de primas alternativas de bancos, el Sharpe mediano pasó de **1,20 en backtest a 0,31 en vivo**, una caída de 73%. Las estrategias más complejas sufrieron recortes 30% mayores ([Suhonen, Lennkh y Perez vía Alpha Architect](https://alphaarchitect.com/looking-at-alternatives-avoid-complexity-and-magical-backtests/)).
- En 888 algoritmos de Quantopian, el Sharpe de backtest explicó **menos del 2,5%** de la varianza del Sharpe fuera de muestra. Cuanto más se había backtesteado una estrategia, mayor era la brecha. La volatilidad y el drawdown predecían mejor que el Sharpe ([Wiecki et al. vía Quantpedia](https://quantpedia.com/quantopians-academic-paper-about-in-vs-out-of-sample-performance-of-trading-alg/)).

Harvey y Liu formalizan esto como un "recorte" que no es lineal. Los Sharpe marginales pierden más de la mitad, y a veces todo. Los fuertes (más de 1 anual) pierden como máximo ~25% en su configuración ([Harvey y Liu 2015](https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF)). Su regla de **t > 3** para un factor nuevo ([Harvey, Liu y Zhu, NBER w20592](https://www.nber.org/papers/w20592)) equivale a un Sharpe anual de ~1,35-1,5 con 5 años de datos y de ~0,85-0,9 con 13 años. Chen (2022) discute ese pesimismo para factores de acciones ([arXiv 2206.15365](https://arxiv.org/pdf/2206.15365)), pero el argumento se aplica menos a una búsqueda privada que nadie replica.

Hay además una buena noticia en tus propios números. Al sumar los activos de validación, el Sharpe bajó de 1,81 a 1,57, una caída de solo ~13%. Es la firma de un núcleo que generaliza, no de un artefacto de selección. Lo que no generalizó fueron las mangas de reversión.

## La tendencia generaliza, la reversión corta no

Trend following es la familia con más evidencia fuera de muestra que existe:

- **Moskowitz, Ooi y Pedersen** documentan momentum de serie temporal significativo en **cada uno de los 58 futuros líquidos** que estudian, entre 1985 y 2009 ([SSRN](https://papers.ssrn.com/abstract=2089463)).
- Hurst, Ooi y Pedersen lo extienden a **67 mercados desde 1880**, con retornos positivos y baja correlación con activos tradicionales en todas las décadas ([AQR](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing)). Neto de comisiones 2/20, el Sharpe promedio ronda **0,4** ([CXO](https://www.cxoadvisory.com/momentum-investing/trend-following-with-intrinsic-momentum-over-the-very-long-run)).
- La mala racha de 2010-2018 vino de que hubo pocos movimientos grandes, no de que el mecanismo se rompiera ([Babu et al. vía Alpha Architect](https://alphaarchitect.com/2020/04/trend-following-reality-you-need-trends-to-trend-follow/)).
- Baltas y Kosowski atribuyen el bajo rendimiento posterior a 2008 a correlaciones más altas entre activos. Muestran que una señal continua más un estimador de volatilidad por rango reducen la rotación más de un tercio sin perder rendimiento ([Imperial/SSRN](https://spiral.imperial.ac.uk/bitstream/10044/1/41472/4/SSRN-id2140091.pdf)).

Tu resultado de **10 de 13 combinaciones motor×activo con Sharpe positivo** en plata, cobre, Nasdaq, EWJ y EWY es justamente lo que esa literatura predice. En crypto la evidencia también es sólida. Liu y Tsyvinski encuentran momentum de serie temporal fuerte en BTC a horizontes diarios y semanales ([NBER w24877](https://www.nber.org/system/files/working_papers/w24877/w24877.pdf)). Un ensamble de canales de Donchian sobre las top-20 monedas líquidas reporta Sharpe superior a 1,5 neto, aunque lo publica una firma interesada y no tiene réplica independiente ([Zarattini, Pagani y Barbon 2025](https://ideas.repec.org/p/chf/rpseri/rp2580.html)).

La reversión de corto plazo (RSI(2), IBS) está en la vereda opuesta. Su base es casi toda de backtests de practicantes sobre acciones y ETFs de EE.UU. ([LuxAlgo](https://www.luxalgo.com/library/concept/rsi-2/); [Pandey y Joshi 2023](https://arxiv.org/abs/2306.12434v1)). Las notas no encontraron ningún estudio revisado por pares que la muestre en commodities o crypto. En crypto, la reversión diaria es propia de monedas ilíquidas, mientras que las grandes muestran *momentum* diario ([Zaremba et al. 2021](https://ideas.repec.org/a/eee/finana/v78y2021ics1057521921002349.html)). Tu 2 de 10 con 7 colapsos no es mala suerte: es lo esperable. Tus otros dos fracasos también encajan con la literatura:

- **Funding y open interest como señal de entrada.** No aportaron ventaja, y eso cuadra con Schmeling, Schrimpf y Todorov: el basis alto refleja demanda apalancada que persigue tendencias, o sea la misma información que el precio. El funding sirve para *cosechar* carry, no para *timing* ([BIS WP 1087](https://www.bis.org/publ/work1087.pdf)).
- **Shorts como manga independiente.** La deriva alcista de crypto y el funding que pagan los largos explican buena parte de por qué perdieron.

### Carry y gestión de volatilidad: diversificadores con letra chica

El carry es una prima transversal a las clases de activos. Rinde ~0,7 de Sharpe bruto dentro de cada clase y ~1,1 diversificado. Sus peores caídas (2008-09) coinciden con los mejores momentos de la tendencia ([Koijen et al. vía CXO](https://www.cxoadvisory.com/big-ideas/unified-carry-trade-theory/)), lo que lo vuelve el complemento natural para los años sin tendencia.

En perpetuos, el carry solo existe como funding. El carry de crypto llegó a **40-60% anual**, pero con riesgo de colapso por liquidaciones ([BIS](https://www.bis.org/publ/work1087.pdf)).

Sobre volatilidad, hay que separar dos cosas:

- **Targeting fijo de volatilidad.** Reduce las colas en todas las clases de activos, pero solo mejora el Sharpe en acciones y crédito ([Harvey et al. 2018](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf)).
- **Escalado ajustado por regresión, al estilo Moreira-Muir.** Falla en tiempo real en **72 de 103** estrategias ([Cederburg et al. 2020](https://www.lehigh.edu/~xuy219/research/COWY.pdf)).

Conclusión: conviene un target fijo e inverso a la volatilidad, sin parámetros ajustados.

## Los datos limpios se gastan, y 10 meses dicen poco

Arnott, Harvey y Markowitz lo plantean sin vueltas. El fuera de muestra "no es realmente fuera de muestra" cuando el investigador vivió ese período. Y si un modelo falla, se corrige por la razón observada y se vuelve a probar sobre los mismos datos, "ya no es un test fuera de muestra, es sobreajuste" ([AHM 2019](https://papers.ssrn.com/abstract=3275654)). El trabajo de Dwork y coautores sobre el "holdout reutilizable" muestra lo mismo desde la estadística general: cada consulta adaptativa al hold-out consume su validez ([listado bibliográfico](https://www.cs.toronto.edu/~toni/publications.html)).

Aplicado a tu programa, cada fuente de datos queda en un estado distinto:

- **Los cinco activos de validación ya son datos de exploración.** Cualquier candidato diseñado sabiendo que ahí fallaron las mangas de reversión no puede "validarse" otra vez en ellos.
- **2026 es, como mucho, un hold-out semiciego.** Lo vieron en vivo, y algunas estrategias viejas se probaron sobre él.
- **Los activos del mismo período no son independientes en el tiempo.** Un patrón minado puede "funcionar" en otros mercados correlacionados durante las mismas fechas ([AHM 2019](https://papers.ssrn.com/abstract=3275654)). Una canasta nueva confirma mejor si incluye clases y regiones poco correlacionadas.

El poder estadístico es el costo escondido. Con ~10 meses, el error estándar del Sharpe anual ronda 1,1, según la aproximación de [Lo 2002](https://ideas.repec.org/a/taf/ufajxx/v58y2002i4p36-52.html) calculada en las notas:

| Sharpe verdadero | Prob. de detectar ventaja en 10 meses | Prob. de ver Sharpe negativo en 10 meses |
|---|---|---|
| 0,5 | 12% | 32% |
| 1,0 | 23% | 18% |
| 1,5 | 39% | 9% |
| 2,0 | 57% | 3% |

Con un Sharpe real de 1, hay **casi una chance en cinco de ver 2026 en negativo**, y solo un 23% de que 2026 "pruebe" algo. 2026 sirve como prueba de "no está roto", no como prueba de ventaja. Según el track record mínimo de López de Prado, un Sharpe observado de 1,0 necesita **~2,7 años** de datos diarios para ser significativo, y un 1,5 necesita ~1,2 años ([slides MinTRL](http://boston.qwafafew.org/wp-content/uploads/sites/4/2017/01/Lopez_de_Prado_Sharpe.pdf)). La forma de recuperar poder es agrupar. Carver estima que distinguir dos reglas lleva ~45 años en un solo instrumento y ~11 años agrupando un portafolio ([hilo sobre *Systematic Trading*](https://threadreaderapp.com/thread/1234306875379683328.html)). Por eso una canasta nueva de varios activos más 2026 confirma mucho más que cualquiera de las dos cosas por separado.

Walk-forward, CPCV y PBO validan el *procedimiento de selección* dentro de la exploración. No reemplazan la confirmación final ([LuxAlgo](https://www.luxalgo.com/library/concept/probability-of-backtest-overfitting/)). El paper trading es el único fuera de muestra inmune al conocimiento previo. No hay una duración estándar. La práctica razonable combina:

- seguimiento CUSUM, que viene del monitoreo de gestores ([Morgan Stanley IM](https://www.morganstanley.com/im/en-la/intermediary-investor/insights/articles/when-good-managers-stumble.html));
- bandas de drawdown simuladas por Monte Carlo y fijadas antes de arrancar;
- escalado gradual del capital en lugar de un interruptor binario ([LuxAlgo](https://www.luxalgo.com/library/concept/live-decay-tracking/)).

## Mi opinión: de acuerdo con buscar, en desacuerdo con "hasta que funcione"

Coincido en que cortar ahora sería prematuro. El núcleo de tendencia está bien sostenido por la literatura y por tus datos. Quedan diversificadores con buen respaldo sin probar, y el costo de 30-40 pruebas más en N es chico si se registran (+0,05-0,1 de Sharpe en la vara). Tampoco hace falta un hold-out "virgen" para explorar: la exploración puede usar todo lo ya gastado sin límite de miradas, siempre que queden anotadas.

Discrepo con la regla de parada "seguir hasta encontrar una operativa funcional", por tres razones.

La primera es que "hasta que funcione" es la parada opcional que describen Simmons et al.: el criterio de corte depende del resultado, y eso sesga al ganador. Es el bucle que López de Prado señala como la causa típica de fracaso: backtestear, ajustar y repetir hasta que aparezca un backtest lindo ([GARP](https://www.garp.org/hubfs/Whitepapers/a1Z1W0000054x6lUAA.pdf)). AHM preguntan explícitamente si el investigador recorrió toda la agenda o "cortó apenas encontró un buen modelo".

La segunda es que **"funcional" hoy significa cumplir r9, y r9 es casi inalcanzable para un libro de tendencia**. Bajo normalidad (cálculo propio), el 80% de trimestres positivos exige un Sharpe de ~1,7. La asimetría positiva de la tendencia, con muchas pérdidas chicas y pocas ganancias grandes, empuja esa exigencia a ~2, como ya estimaron ustedes. Tu 56% de meses positivos con Sharpe 1,81, contra ~74% bajo normalidad, es la huella de esa asimetría. Ningún hallazgo honesto va a cumplir Q80 de forma sostenida. Buscar hasta cumplirlo garantiza seleccionar ruido.

La tercera es que cada ronda más agranda la tentación de mirar 2026 y de reciclar activos gastados. Esa es la pérdida que no se recupera.

### Proceso concreto para cerrar el hito

| Etapa | Qué hacer | Compuerta para avanzar |
|---|---|---|
| 0. Recalibrar metas | Pasar r9 de regularidad a metas de seguimiento, no de aprobación. Fijar metas compatibles con Sharpe ~1: maxDD ≤ 20% a ~15-17% de vol, DSR ≥ 0,95, y meses/trimestres positivos como métrica informativa. Mantener CAGR como resultado, no como objetivo de ajuste. | Escrito y commiteado antes de cualquier prueba nueva. |
| 1. Agenda cerrada | Preregistrar 3-4 familias, sus grillas y el universo de activos. Presupuesto de **30-40 pruebas** (N acumulado ≈ 110-120). Registrar la serie diaria de retornos de *cada* prueba. Contar retroactivamente las bifurcaciones conocidas, como las alternativas de mapeo de C0. | Agenda congelada con hash. |
| 2. Exploración | Usar libremente la ventana 2020-25, la historia 2011+ (2017+ en crypto) y los cinco activos ya gastados. Preferir ensambles de parámetros y de activos antes que óptimos puntuales. | Sin límite de miradas, pero todas registradas. |
| 3. Compuerta de salida | Calcular el N efectivo agrupando las series de retornos por correlación. Exigir DSR ≥ 0,95 con la varianza de Sharpe observada; PBO < 0,3 sobre la familia; eficiencia walk-forward anclada ≥ 0,5 en 2011+; meseta de parámetros (±20-50% conserva ~70% del Sharpe); resultado positivo agrupado en la mayoría de las clases. Todo neto de costos y funding. | Si nada pasa, el hito cierra con el núcleo de tendencia actual como candidato. |
| 4. Confirmación única | Un solo test, con código congelado y regla preregistrada, sobre (a) una canasta de activos **nunca cargados**, y (b) 2026, solo para motores que nunca lo tocaron (R1/R2/R3 sí califican, las estrategias viejas no). Aprueba con Sharpe agrupado > 0 y p unilateral < 0,10 en la canasta, más Sharpe 2026 ≥ −0,5 con drawdown dentro de la banda simulada del 95%. | Si falla, el candidato se retira. Las variantes vuelven a la etapa 2 y necesitan otros datos frescos. |
| 5. Incubación | 6-12 meses de paper trading o capital chico. Reglas de corte preregistradas: drawdown por encima del percentil 95-99 del bootstrap, alarma CUSUM, Sharpe móvil de 12 meses debajo del percentil 5 simulado. Escalado 25% → 50% → 100%. Sin retoques: cualquier cambio reinicia la incubación. | Posterior P(Sharpe > 0) ≥ 0,9 y ninguna regla de corte disparada. |

Los umbrales concretos de PBO, walk-forward, meseta y prueba de no-colapso son síntesis de las notas a partir de la matemática de poder citada, no estándares publicados. La única regla publicada para PBO es el 0,05 del paper original. Tienen que quedar preregistrados como decisión propia del programa.

En cuanto a datos frescos, la canasta nueva puede combinar dos fuentes. Una es activos negociables en Binance que nunca se cargaron, como altcoins líquidas: sirven para la manga de crypto, pero correlacionan fuerte con BTC, así que valen menos como evidencia independiente. La otra, y esto es lo más valioso, son mercados que **no hace falta poder operar**: futuros o ETFs de otras clases y regiones (granos, bonos no estadounidenses, divisas, otros índices). Lo que la confirmación pone a prueba es que la *familia* generalice, no que el activo sea negociable. Los CSV de EWJ y EWY que hay en el árbol de trabajo ya no califican, porque se usaron en F3.

### Expectativas realistas

Con 7 mercados, dos pares muy correlacionados (BTC/ETH y S&P/Nasdaq) y una ventana 2021-25 favorable a la tendencia, lo razonable es esperar un **Sharpe de largo plazo de ~0,6-1,0**, no 1,8. Ese rango sale de dos referencias: el recorte empírico de 25-75% y la observación de Carver de que los Sharpe realistas "rara vez superan 1,0" ([CXO](https://www.cxoadvisory.com/big-ideas/a-few-notes-on-systematic-trading)). A 17% de vol, eso implica un CAGR de un dígito alto o de 10-15%, no 34%. La regularidad sería de **~55-60% de meses y ~65-75% de trimestres positivos** (cálculo propio bajo normalidad, ajustado a la baja por asimetría), con drawdowns mayores a 10% cada uno o dos años, como el SG Trend Index desde 2000 ([Cambridge Associates](https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/)). Si el sistema en vivo entrega eso, está funcionando bien.

### Qué familias explorar, en orden

1. **Refinamientos del núcleo de tendencia.** Mezclar momentum de serie temporal 1/3/12 meses con el ensamble Donchian, usar señal continua, volatilidad por rango OHLC y un tope de exposición que baje cuando suben las correlaciones ([Baltas y Kosowski](https://spiral.imperial.ac.uk/bitstream/10044/1/41472/4/SSRN-id2140091.pdf)). Agregar amplitud a la manga crypto con más perpetuos líquidos de peso chico ([Zarattini et al.](https://ideas.repec.org/p/chf/rpseri/rp2580.html)). Es la apuesta de mayor probabilidad y ataca los modos de falla documentados de la tendencia.
2. **Carry de funding en crypto.** Es la prima no direccional mejor documentada, gana en mercados laterales y diversifica justo cuando la tendencia sufre ([BIS](https://www.bis.org/publ/work1087.pdf)). Tiene riesgo de cola por liquidaciones. Que el funding de los perpetuos TradFi de Binance tenga prima no está documentado.
3. **Momentum transversal** entre los 7-12 activos, en versión de inclinación larga para esquivar la debilidad de los shorts. Crypto tiene un factor momentum documentado, aunque transitorio ([Liu, Tsyvinski y Wu](https://papers.ssrn.com/abstract=3379131)).
4. **Reversión de largo plazo como proxy de "value"** (z-score de 3-5 años). Está correlacionada negativamente con momentum en todas las clases ([Asness, Moskowitz y Pedersen](https://www.johnhcochrane.com/s/Value-and-Momentum-Everywhere.pdf)), pero en un universo chico su Sharpe va a ser bajo y ruidoso.
5. **Paridad de riesgo inversa a la volatilidad entre mangas**, como capa de construcción y no como familia de señales.

Hay que despriorizar la reversión de corto plazo fuera de índices de acciones (como mucho, una manga chica en S&P/Nasdaq que tendría que pasar por la confirmación igual que el resto), el timing direccional por funding u OI, y los shorts como manga independiente.

## Conclusión

La pregunta "¿cuánto me penaliza inflar N?" está mal planteada. La penalización explícita es logarítmica y manejable. La que no se ve es la que mata: decisiones post hoc no contadas, metas que solo un Sharpe de 2 cumple, y datos de confirmación que se gastan de a poco mirándolos. El activo más escaso del programa no es el margen del DSR, sino los datos que nadie vio. Cada ronda de "seguir buscando" tiene que comprarse con presupuesto explícito y pagarse con una única mirada a datos frescos.

Mi veredicto: el hito no se cierra cuando aparezca una estrategia que cumpla r9. Se cierra cuando un candidato definido de antemano pasa o falla una confirmación única y después sobrevive la incubación. El candidato con mejores chances ya lo tenés: el núcleo de tendencia, que generalizó donde lo esperaba la literatura. El trabajo que queda es diversificarlo con carry y momentum transversal, y aceptar que un Sharpe vivo de ~0,8 con 60% de meses positivos sería un éxito.
