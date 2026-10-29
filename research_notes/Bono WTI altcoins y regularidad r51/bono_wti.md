# Bono largo US (TLT/ZB) y WTI: reglas sistematicas solo-precio (estado 2026)

NOTA DE ENTREGA: la sesion estaba en plan mode, asi que estas notas se guardaron aqui (fichero de plan) y NO en la ruta pedida
(...\scratchpad\research_notes\Bono WTI altcoins y regularidad r51\bono_wti.md). Copiar a esa ruta al salir de plan mode.
Los puntos marcados [conocimiento previo, no verificado en esta sesion] vienen de la literatura conocida pero no se revisaron con una fuente web en esta sesion. Tratarlos como pistas, no como citas.

## 1. Time-series momentum (TSMOM) en bonos y crudo: lookbacks, long/short, CTAs en bonos 2020-2025

### Takeaway
Las lookbacks largas (combinacion 1/3/12m, con mas peso en 3-12m) son las que mejor funcionan de forma generica. El Sharpe esperable por activo individual es bajo, alrededor de 0.3-0.4 bruto. Para el bono, el regimen 2022-2025 fue malo para trend fuera de 2022: un 2022 historico, el whipsaw de 2023 (SVB), un 2024 con perdidas en bonos en la segunda mitad y reversiones lentas en 2024-25. El crudo fue contribuidor importante de los CTAs en 2026.

### Cited Findings
- Hurst-Ooi-Pedersen (2013, "Demystifying Managed Futures"), con 24 commodities y otras clases, 1985-2012. El Sharpe bruto medio por activo fue 0.29 (1m), 0.36 (3m) y 0.38 (12m), y las lookbacks largas superan a las cortas. Sin costes de roll ni de rebalanceo. — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/intrinsic-momentum-diversified-across-futures/)
- Hurst-Ooi-Pedersen (2017, "A Century of Evidence"), 67 activos, 1880-2016. La combinacion 1/3/12m da un Sharpe medio de cartera de ~0.4 neto de comisiones 2/20. Ese Sharpe es de cartera diversificada, no de un activo. — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/trend-following-with-intrinsic-momentum-over-the-very-long-run)
- Geczy-Samonov (2019), commodities 1877-2017. TSMOM long/short sobre el retorno en exceso de 12m da un Sharpe mensual bruto de 0.18 y un MaxDD de -59%. — [CXO Advisory](https://www.cxoadvisory.com/commodity-futures/commodity-futures-strategies-over-the-very-long-run)
- Baltas-Kosowski (2012) sustituyen la senal binaria (signo del retorno de 12m) por una senal continua de "fuerza de tendencia" en [-1,+1] y usan el estimador de volatilidad Yang-Zhang. Ambas cosas reducen la rotacion y mejoran el resultado neto de costes. Tambien encuentran que distintas frecuencias de TSMOM capturan fenomenos distintos. — [QuantConnect tutorial](https://www.quantconnect.com/tutorials/strategy-library/improved-momentum-strategy-on-commodities-futures); [NBIM discussion note](https://www.nbim.no/globalassets/documents/news/2014/discussionnote_time_series_momentum_latest.pdf)
- Marzo 2023 (SVB): JPMorgan estimo que los CTAs perdieron ~7% entre el 8 y el 13 de marzo, sobre todo por cortos en futuros de bonos (y el yen). El SG CTA cayo un 4% en un dia, su peor dia registrado, despues de que 2022 fuera su mejor ano. — [Reuters via Kitco](https://www.kitco.com/news/off-the-wire/2023-03-16/trend-following-hedge-funds-whiplashed-wild-bond-trade)
- 2023 fue "el ano del whipsaw": el SG Trend tuvo perdidas moderadas, los gestores muy cargados en renta fija lo pasaron peor y los que anadieron commodities lo hicieron mejor. — [Top Traders Unplugged](https://www.toptradersunplugged.com/?p=14211)
- En 2024 el indice SG de trend acabo en ~+2%: las ganancias se evaporaron por la volatilidad en bonos y las reversiones en acciones, energia y metales. — [Bloomberg via Advisor Perspectives](https://www.advisorperspectives.com/articles/2025/01/03/fast-money-quants-big-year-bust-wild-cross-asset-ride)
- El bono a 30 anos cayo ~13% entre septiembre de 2024 y mediados de enero de 2025 y despues reboto, pero la mayoria de modelos siguio corta en bonos hasta marzo de 2025. Es un ejemplo del retraso de las tendencias largas en giros de tipos. — [RCM Alternatives](https://www.rcmalternatives.com/2025/04/paging-mr-following-mr-trend-following/)
- En el Q2 2025 la renta fija global resto un -2.0% al KFA MLM Index (KMLM), que paso de un 69% a un 128% neto corto en renta fija. En el mismo trimestre Goldman MF gano con steepeners cortos de largo plazo, asi que el signo depende de la implementacion. — [KraneShares](https://kraneshares.com/kmlm-signal-vs-noise-navigating-todays-trend-following-landscape-q2-review/); [GS AM](https://am.gs.com/public-assets/documents/cc866971-2126-11f0-9561-47215d2d5018?view=true)
- En 2026 las commodities fueron el mayor contribuidor en el Q1 (Goldman), y el complejo del petroleo fue el mayor contribuidor YTD hasta julio (WisdomTree). — [GS AM](https://am.gs.com/public-assets/documents/641dc743-48cb-11f1-9232-0fc76e371c0a?view=true); [WisdomTree](https://www.wisdomtree.com/us/insights/blog/when-markets-zigzag-trend-followers-can-shine/pdf)
- Un backtest de RCM atribuye al mercado de bonos aproximadamente el doble del rendimiento historico de trend que cualquier otro sector. Gran parte de ese rendimiento es la deriva alcista de 1981-2020, que no se repite. — [RCM Alternatives](https://www.rcmalternatives.com/?p=1889)

### Inferences
- Defaults: senal = media de signos (o senal continua) de los retornos en exceso de 1, 3 y 12m (≈21/63/252 dias), con volatility targeting ex-ante (vol EWMA de ~60 dias de centro de masa, como en MOP) y rebalanceo semanal o mensual. Para el bono conviene una version long/short. Un sistema solo largo como el ensemble Donchian actual capturo justo la parte mala: estuvo largo en los rebotes falsos de 2023-24 y no pudo ponerse corto en 2022. Eso explica por si solo un Sharpe de -1.29 en 2021-25.
- Sharpe realista para un activo aislado: 0.2-0.4 bruto a largo plazo. En 2021-25 el bono long/short probablemente estuvo en positivo por 2022 y en negativo en 2023-24 [inferencia, no verificado con datos].
- El bono es el activo donde la deriva historica (1981-2020) infla los backtests de "long-only trend". El periodo desde 2002 en TLT incluye esa deriva: hay que exigir que la regla funcione en el subperiodo 2021-25 y en version long/short.

### Gaps
- No se encontraron cifras de TSMOM especificas por activo para ZB/TLT ni para WTI aislados. Las cifras de HOP y MOP son medias de muchos activos.
- No se verifico el paper de AQR "trend in rates" ni la cifra anual exacta del SG Trend para 2023 y 2025.
- Moskowitz-Ooi-Pedersen (2012, JFE): Sharpe ~1.2 de la cartera diversificada TSMOM-12m de 58 futuros entre 1985 y 2009; TSMOM rentable para el 100% de los contratos a horizonte de 12m; reversion parcial pasado el ano [conocimiento previo, no verificado en esta sesion].

## 2. Proxies solo-precio de carry/term structure (crudo) y de nivel/pendiente (bono)

### Takeaway
El carry predice retornos en commodities, pero se mide con la curva de futuros. Sin curva, los proxies solo-precio (spot frente a media movil, momentum) son, en lo esencial, momentum renombrado. Para el bono, un proxy de nivel de yield a partir del precio de TLT es en la practica una senal de reversion o value de muy baja frecuencia. Ninguno de los dos tiene evidencia OOS especifica.

### Cited Findings
- Koijen-Moskowitz-Pedersen-Vrugt ("Carry", NBER w19325): el carry, medible ex ante, predice retornos en sentido cross-section y time-series en varias clases, commodities incluidas. — [NBER](https://www.nber.org/papers/w19325)
- En commodities el carry es esencialmente el roll yield implicito en la curva, positivo en backwardation, y la convenience yield predice retornos. — [Chicago Booth Review](https://www.chicagobooth.edu/review/carry-trading-not-just-for-currencies)
- Gorton et al. (2013) documentan una relacion cross-section significativa entre convenience yield (inventarios bajos) y retornos futuros. — [Essex WP (citandolo)](https://repository.essex.ac.uk/34736/1/Convenience%20yield%20risk.pdf)

### Inferences
- Un proxy "spot > MA(N)" no mide el roll yield. La backwardation del WTI esta correlacionada con precio alto y en subida (inventarios bajos), asi que el proxy captura algo, pero sobre todo es TSMOM. No conviene contarlo como un factor independiente en el pre-registro.
- Proxy de "USO frente a spot": la diferencia acumulada de rentabilidad entre USO (que rola futuros) y el spot (o el CFD de Dukascopy, si este aplica ajustes de rollover) recupera el roll yield realizado pasado. Es un proxy creible del carry realizado reciente: si USO rinde menos que el spot, la curva esta en contango. Es el unico proxy solo-precio con fundamento mecanico, pero hay que verificar como construye Dukascopy su serie de WTI (rolada o con ajuste de swap) [inferencia, no verificado].
- CLUSDT en Binance: el funding del perp frente al indice puede actuar como un "carry" propio del instrumento (ver seccion 6).
- Para el bono, el carry de ZB es aproximadamente la pendiente (yield a 30 anos menos tipo corto) mas el roll-down. Con solo el precio de TLT no se puede observar la pendiente, porque haria falta el tipo corto (SHY/BIL), que no es "solo precio" del activo. El ratio TLT/SHY seria un proxy de pendiente, pero queda fuera del supuesto de datos.

### Gaps
- No se encontro evidencia publicada que valide "precio frente a media movil" como proxy de backwardation del crudo.
- No se encontro el paper de Szymanowska-de Roon-Nijman-van den Goorbergh (2014, JF, spot vs term premia) en esta sesion [conocimiento previo: la prima de basis/carry es la principal en commodities].

## 3. Efectos de calendario y eventos: supervivencia post-publicacion

### Takeaway
Del lado del bono, el efecto de fin de mes en Treasuries (Hartley-Schwarz) y el ciclo de subastas (Lou-Yan-Zhang) tienen base estructural, los flujos de dealers e indices. El pre-FOMC drift desaparecio tras su publicacion. En el crudo, la estacionalidad mensual no tiene un test OOS convincente, y el efecto del EIA es intradia y no accionable con datos diarios.

### Cited Findings
- Lou-Yan-Zhang (RFS 2013): los precios secundarios de los Treasuries caen significativamente los dias previos a una subasta y se recuperan poco despues, aunque el calendario es publico. Lo atribuyen a la capacidad de riesgo limitada de los dealers. Coste oculto estimado: 9-18 pb del tamano de la subasta. — [LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/46329); [working paper](https://ifr.hkust.edu.hk/uploads/upload/files/20250212/f5cba4b7e2aa3ada8477ad2fc38fab02.pdf)
- Collin-Dufresne, en su discusion del paper, senala que el efecto aparece entre vencimientos, crece con el tamano de la emision y se derrama hacia acciones (10 dias despues frente a 10 dias antes de la subasta). — [EPFL discussion slides](https://www.epfl.ch/labs/sfi-pcd/wp-content/uploads/2021/07/Discussion-of-Anticipated-and-Repeated-Shocks-in-Liquid-Markets-2011.pdf)
- Hartley-Schwarz ("Predictable End-of-Month Treasury Returns", 2019): retornos en exceso positivos y muy significativos en los ultimos dias de cada mes en Treasuries con cupon, en 1990-2018. Los atribuyen a window dressing y rebalanceo, incluidas compras de aseguradoras en fechas de rebalanceo de benchmarks. — [Wharton Rodney White Center WP](https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2019/12/17-19.Schwarz.pdf)
- La extension de duracion de los indices a fin de mes es un flujo conocido y anunciado por los bancos (p. ej., Citi estima la extension mensual del indice). — [MNI Markets](https://www.mnimarkets.com/articles/citi-flag-slightly-larger-than-normal-egb-extension-small-gilt-contraction)
- Pre-FOMC drift: Kurov-Wolfe-Gilbert (FRL 2021) amplian la muestra de Lucca-Moench (1994-2011) hasta 2019. El drift desaparecio esencialmente despues de 2015, con y sin rueda de prensa. — [Skidmore PDF](https://www.skidmore.edu/economics/documents/KurovWolfeGilbert-TheDisappearingPre-FOMC-Announce-Drift-200914.pdf); [IDEAS](https://ideas.repec.org/a/eee/finlet/v40y2021ics1544612320315956.html)
- EIA del miercoles (10:30 ET): las sorpresas de inventario tienen un impacto negativo inmediato en los retornos del crudo. En los dias de EIA, la tercera media hora predice la ultima media hora (momentum intradia), pero no en otros dias. — [Energy Journal, Wen-Indriawan-Lien-Xu 2023 (IDEAS)](https://ideas.repec.org/a/aen/journl/ej44-5-xu.html); [Adelaide](https://digital.library.adelaide.edu.au/items/13d367dd-06b2-4eca-8d21-4dfeb46c4f55)
- Rousse-Sevi: hay desequilibrio de ordenes en las 2 horas previas al EIA (caida de ~-0.25% antes de sorpresas positivas) y sobrerreaccion asimetrica que se revierte parcialmente en las horas siguientes. — [IAEE exec summary](https://iaee.org/ej/ejexec/EJ40-2_Rousse_ExecSum.pdf)
- Estacionalidad del WTI (1986-2020): las subidas mas consistentes son de marzo a mayo y las caidas de noviembre a diciembre. La volatilidad mensual (6.7-14.2%) es enorme frente a las medias, y no es un test OOS. — [CXO Advisory](https://www.cxoadvisory.com/calendar-effects/any-seasonality-for-oil-prices/)
- Quayyoum et al. (2019) encuentran retornos negativos en noviembre y diciembre en Brent y WTI (1987-2016), dentro de la muestra. — [Cardiff Met](https://pure.cardiffmet.ac.uk/en/publications/seasonality-in-crude-oil-returns/)
- Advertencia metodologica: muchas "predictibilidades" del petroleo usan medias mensuales de precios diarios, lo que infla los t-stats. Con datos de fin de mes no hay evidencia convincente ni dentro ni fuera de la muestra. — [EFMA 2020 paper](https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2021-Leeds/papers/EFMA%202020_stage-1301_question-Full%20Paper_id-473.pdf); [HAL](https://hal-rennes-sb.archives-ouvertes.fr/hal-03519860v1)
- Hay un paper de 2026 (arXiv 2609.12227) con reglas estacionales OOS sobre 15 commodities, WTI incluido. No se pudieron ver sus resultados para el crudo. — [arXiv](https://arxiv.org/pdf/2609.12227)

### Inferences
- Defaults para el bono, a pre-registrar:
  - Fin de mes: largo TLT/TMF desde el cierre del dia T-3 o T-4 hasta el ultimo dia habil del mes.
  - Ciclo de subastas: neutral o corto ~3-5 dias antes de las subastas de 10y/30y (calendario del Tesoro, normalmente las semanas de refunding y reaperturas mensuales) y largo desde el dia de la subasta hasta ~3 dias despues.
  - Conviene tratarlos como un solo "sleeve de flujos" para reducir el multiple testing.
  - Sharpe esperable por regla, si el efecto persiste: bajo (~0.3-0.5), con muy poca exposicion temporal. Los costes de TMFUSDT (spread con <1M/dia) pueden comerse todo el efecto (pocos pb por evento).
- El pre-FOMC drift no debe usarse: esta muerto post-publicacion.
- Para WTI con datos diarios no hay un efecto de calendario con evidencia OOS solida. La estacionalidad de marzo a mayo frente a noviembre y diciembre es, como mucho, un filtro debil y probablemente fruto de data mining.

### Gaps
- No se encontro evidencia OOS post-2019 del efecto de fin de mes de Hartley-Schwarz ni post-2013 del de Lou-Yan-Zhang. No se pudo leer el PDF de Hartley-Schwarz (estaba comprimido), asi que no hay magnitudes en pb.
- No se cubrieron con fuentes las reuniones de la OPEP, el pre-holiday en bonos ni el turn-of-month en commodities.

## 4. Reversion a la media de corto plazo y regimen de volatilidad (bonos y crudo)

### Takeaway
En esta sesion no se encontro evidencia OOS solida de reglas de reversion diaria en bonos o crudo. Lo unico documentado es microestructura intradia alrededor del EIA (momentum en el dia del anuncio y reversion parcial de la sobrerreaccion en horas).

### Cited Findings
- Sobrerreaccion asimetrica del crudo a las noticias de inventario, parcialmente revertida en las horas siguientes. — [IAEE exec summary](https://iaee.org/ej/ejexec/EJ40-2_Rousse_ExecSum.pdf)
- Momentum intradia el dia del EIA (la media hora 3 predice la ultima). — [IDEAS](https://ideas.repec.org/a/aen/journl/ej44-5-xu.html)
- Volatility scaling o una senal continua reducen la rotacion y mejoran el resultado neto en TSMOM. — [QuantConnect / Baltas-Kosowski](https://www.quantconnect.com/tutorials/strategy-library/improved-momentum-strategy-on-commodities-futures)

### Inferences
- El regimen de volatilidad debe usarse para el sizing (vol target) y no como senal direccional.
- Con <1M/dia en TMFUSDT, cualquier regla de reversion de alta rotacion es inviable en costes.

### Gaps
- No se encontraron estudios OOS de reversion de corto plazo (1-5 dias) en futuros de Treasury o WTI con datos diarios.

## 5. Bono como diversificador de crisis: cambio de regimen de la correlacion acciones-bonos

### Takeaway
La correlacion acciones-bonos paso a ser positiva alrededor de marzo de 2022, tras unos 20 anos de regimen negativo, impulsada por la inflacion. Esto erosiona el papel del bono largo como cobertura y justifica condicionar la exposicion larga a bonos a que la correlacion rodante sea negativa.

### Cited Findings
- El cambio de correlacion negativa a positiva se fecha en marzo de 2022 y cierra un regimen negativo de mas de 20 anos. — [Franklin Templeton/Brandywine](https://www.franklintempleton.com/articles/2023/brandywine-global/deconstructing-the-dynamic-duo-of-stocks-and-bonds)
- Man Group: la correlacion fue positiva en el muy largo plazo y negativa durante los ~20 anos previos, y volvio a ser positiva en 2022, sobre todo por la inflacion. — [Man Institute](https://www.man.com/insights/regifting-2022)
- AQR (Brixton, Brooks, Hecht, Ilmanen, Maloney, McQuinn): pasar de una correlacion de -0.5 a +0.5 sube la volatilidad de un 60/40 en ~20%, y la correlacion de 1926-1999 fue de ~+0.18. La correlacion depende del regimen macro (inflacion frente a crecimiento). — [WealthManagement (resumen)](https://www.wealthmanagement.com/equities/implications-regime-shifting-stock-and-bond-correlations)
- Un estudio Markov-switching de 2025 concluye que la cobertura con Treasuries depende del regimen y falla en caidas impulsadas por inflacion, con 2022 como cambio de regimen. — [reference-global](https://reference-global.com/article/10.32676/n.11.1.7)

### Inferences
- Regla condicional propuesta, a pre-registrar:
  - Calcular la correlacion rodante de 63 o 126 dias entre los retornos diarios de SPX y TLT.
  - Si es negativa, permitir largo bono por trend (o un largo "crisis" cuando SPX esta por debajo de su MA de 200 dias).
  - Si es positiva, solo corto bono por trend o plano.
  - Riesgo: la senal de correlacion es lenta y tiene pocos cambios de regimen independientes (unos 2-3 desde 1990), asi que la potencia estadistica es minima. Hay que tratarla como un prior economico y no como algo optimizable.
- En el sistema del equipo, el bono "aporta cero correlacion" justo porque el regimen positivo elimina el efecto cobertura frente a crypto y equity.

### Gaps
- No se encontro ningun paper que pruebe trend en bonos condicionado a la correlacion acciones-bonos con evidencia OOS.

## 6. Practico: decay de TMF/TBT y perps TradFi de Binance (CLUSDT, TMFUSDT)

### Takeaway
TMFUSDT y TBTUSDT se listaron el 27-07-2026 y son perps sobre ETFs apalancados con rebalanceo diario. Su exposicion al bono es dependiente de la trayectoria (volatility decay) y su liquidez es escasa. CLUSDT (desde el 01-04-2026) es mucho mas liquido: el crudo es el producto estrella de los perps TradFi. Hay que modelar el funding (cada 8h, tope ±2%) y el indice congelado en fines de semana y festivos.

### Cited Findings
- TMFUSDT, TBTUSDT y BITOUSDT se listaron el 27-07-2026 (13:30-13:40 UTC) como USDⓈ-M perpetuos: 24h, apalancamiento de hasta 25x, funding cada 8h con tope de ±2.00%, componente de tipo de interes del funding en 0%, sin cambio automatico del intervalo a 1h, orden minima de 0.01 y nocional minimo de 5 USDT. TMFUSDT replica el Direxion Daily 20+ Yr Treasury Bull 3X. — [CoinGape](https://coingape.com/binance-launches-tradfi-perp-futures-tied-to-us-treasury-bonds-proshares-bitcoin-etf/)
- Discrepancia: CoinGape describe el subyacente de TBTUSDT como "ETF Shares UltraShort 20+ Year Treasury (NYSE: UPR)". El ProShares UltraShort 20+ Yr historico tiene el ticker TBT. Verificar en el anuncio oficial de Binance que ETF y que ticker usa el indice. — [CoinGape](https://coingape.com/binance-launches-tradfi-perp-futures-tied-to-us-treasury-bonds-proshares-bitcoin-etf/)
- Perps de petroleo en Binance desde el 01-04-2026, con apalancamiento de hasta 100x segun la cobertura de lanzamiento. Volumen de petroleo combinado mes a la fecha de $42.5B (56% HIP-3/Hyperliquid y 44% Binance). Binance tuvo el 49.3% del volumen de petroleo desde el 9 de abril (pico del 54% el 17 de abril). La demanda se ligo a tensiones en Oriente Medio y aranceles, con trading de fin de semana. — [CoinDesk Research](https://www.coindesk.com/research/oil-etfs-and-the-tradfi-perp-land-grab); [BitMEX Q1 2026 report](https://www.bitmex.com/blog/2026q1-derivatives-report)
- Fines de semana: segun BitMEX (fuente competidora y no oficial), Binance congela el indice en el ultimo precio spot conocido al cierre del mercado, el mark price pasa a una EWMA suavizada y en commodities hay un limite de desviacion de ±3% entre el mark y el indice congelado. — [BitMEX Q1 2026 report](https://www.bitmex.com/blog/2026q1-derivatives-report)
- Richard Teng (abril de 2026): los perps TradFi de Binance suponen ~4.9% del volumen de los principales futuros TradFi. A junio de 2026 habia 69 contratos TradFi, la mayoria con mas de $1M/dia. — [OneKey blog](https://onekey.so/blog/ecosystem/richard-teng-binance-tradfi-perpetual-contracts-are-expanding-fast-now-49-of-major-tradfi-futures-volume-20260416173250/); [OneKey](https://onekey.so/blog/ecosystem/tradfi-summer-binance-69-tradfi-20260603165259/)
- TMF cayo ~73% en 2022. Su drawdown desde 2009 hasta agosto de 2025 fue de -92.6%, frente a -48.4% de TLT. Sus retornos mensuales siguen a 3x TLT con fuerte no linealidad por decay, y la propia Direxion lo define como instrumento tactico de corto plazo. — [BNN Bloomberg](https://www.bnnbloomberg.ca/triple-leveraged-bond-etf-attracts-billions-despite-losing-22-this-year-1.1960370); [Seeking Alpha](https://seekingalpha.com/article/4813847-tmf-bond-leveraged-etf-for-active-traders); [Seeking Alpha](https://seekingalpha.com/article/4037686-tmf-will-tend-underperform-tlt-long-term)
- El UBT (2x) perdio menos que TMF en 2022 por tener menos volatility drag. — [bestetf / comparativas](https://www.bestetf.net/compare/UVIX-vs-TMF/)

### Inferences
- Decay: el retorno log de un ETF apalancado L ≈ L·r - (L²-L)/2·σ²·t, menos comisiones y la financiacion, que es aproximadamente (L-1)·el tipo corto. Con una vol de TLT de ~15-18% anual, TMF (L=3) pierde unos 3·σ² ≈ 7-10%/ano frente a 3xTLT por varianza, mas el coste de financiacion de 2x el tipo corto (~8% con tipos al 4%). TBT (L=-2) pierde 3·σ² ≈ 7-10%/ano mas la financiacion. [formula estandar; inferencia]
- Para trading con holding de dias o semanas, el decay es pequeno. En holdings de meses (TSMOM 12m) es material, y ademas asimetrico: los dos lados pierden en mercado lateral. Recomendacion: computar la senal sobre TLT o el CFD, ejecutar en TMFUSDT (largo) o TBTUSDT (corto) con holding corto o rebalanceo frecuente, dimensionar por la beta efectiva (3x o -2x) y descontar el decay mas el funding en el backtest.
- No hay datos historicos de TMFUSDT ni TBTUSDT (listados en julio de 2026). El backtest tiene que sintetizar el precio del perp como el ETF mas el funding estimado, con slippage alto. Con <1M/dia, el tamano de posicion debe ser una fraccion pequena del ADV (p. ej. <1-2%).
- Fuera del horario de NYSE los perps de ETF cotizan contra un indice congelado: los gaps de lunes y los movimientos de fin de semana del perp son un riesgo de basis. Hay que usar senales con datos de cierre de NYSE y ejecutar en horas de mercado.
- CLUSDT: el apalancamiento alto y la demanda retail en eventos geopoliticos pueden producir funding sesgado (premium). Hay que medir el funding historico de CLUSDT (abril a octubre de 2026) antes de dimensionar el lado corto.

### Gaps
- No se encontro la documentacion oficial de Binance sobre el indice de CLUSDT (que contrato o que fuentes), su funding historico, su volumen diario especifico ni el funcionamiento oficial en fines de semana. Lo de BitMEX es de segunda mano.
- No hay datos de volumen ni de OI de TMFUSDT o TBTUSDT. El "<1M/dia" lo aporta el equipo.

## 7. Parametros por defecto y Sharpe esperable (sintesis)

### Takeaway
Ninguna idea aislada promete un Sharpe mayor de ~0.5 neto en un solo activo. Lo mas defendible es TSMOM long/short multi-horizonte, que funciona mejor en el crudo que en el bono en el regimen actual. Para el bono, los efectos de flujo (fin de mes y subastas) tienen fundamento estructural pero sin OOS reciente verificado.

### Cited Findings
- TSMOM 1/3/12m: Sharpe bruto por activo de 0.29-0.38. — [CXO/HOP 2013](https://www.cxoadvisory.com/momentum-investing/intrinsic-momentum-diversified-across-futures/)
- TSMOM 12m en commodities long/short: Sharpe mensual de 0.18 y MaxDD de -59% (1877-2017). — [CXO/Geczy-Samonov](https://www.cxoadvisory.com/commodity-futures/commodity-futures-strategies-over-the-very-long-run)
- El pre-FOMC drift desaparecio despues de 2015. — [Kurov-Wolfe-Gilbert](https://ideas.repec.org/a/eee/finlet/v40y2021ics1544612320315956.html)

### Inferences
Tabla de defaults y Sharpe esperable [inferencias del autor de las notas, a partir de lo anterior]:

| Idea | Activo | Defaults | Sharpe neto esperable | Estado de la evidencia |
|---|---|---|---|---|
| TSMOM multi-horizonte L/S | WTI | signo de los retornos de 21/63/252d (o senal continua BK); vol target; rebalanceo semanal | 0.2-0.4 | Robusta en general; 2026 favorable |
| TSMOM multi-horizonte L/S | Bono | igual; L/S obligatorio | 0-0.3 (2021-25 incierto) | Robusta historicamente, con whipsaw en 2023-25 |
| Trend condicionado a la correlacion acciones-bonos | Bono | correlacion SPX-TLT a 126d; largo solo si es negativa | desconocido | Prior economico, sin OOS |
| Fin de mes en Treasuries | Bono | largo de T-3 a T0 del mes | 0.3-0.5 por exposicion; neto dudoso con TMFUSDT | Base estructural; OOS post-2018 no verificado |
| Ciclo de subastas 10y/30y | Bono | corto o plano de T-5 a T-1; largo de T0 a T+3 | bajo | RFS 2013; OOS no verificado |
| Pre-FOMC | Bono | — | ~0 | Muerto post-2015; descartar |
| Estacionalidad (mar-may largo, nov-dic corto) | WTI | mensual | ~0-0.2 | In-sample; probable data mining |
| EIA intradia | WTI | requiere datos de 30 minutos | n/a con diarios | Solo intradia |
| Proxy de carry USO frente a spot | WTI | diferencia de rentabilidad a 63d; largo si USO rinde mas (backwardation) | desconocido | Mecanicamente creible; sin test |

### Gaps
- Faltan Sharpe OOS publicados post-2015 especificos para bono o WTI aislados en cualquiera de estas reglas.
