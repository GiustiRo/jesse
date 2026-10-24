# AB — viabilidad documental HOLD: disposición y coste de tenencia

Fecha2026-10-21. Estado HOLD por representación/datos; no es receta económica ni prueba negativa. Cero código, jobs, drafts, velas, importaciones o datasets nuevos. No depende de resultadosY. AA mantiene separada la única pregunta sugerida como posible experimento.

La hipótesis económica sería que ganancias/pérdidas no realizadas de los tenedores modifican su propensión a vender, y que el precio conserve información incremental respecto del retorno pasado. Es distinta conceptualmente de un VWAP arbitrario; para representarla hace falta una distribución defendible de coste y supervivencia de posiciones. OHLCV de un perpetuo no identifica compradores, última adquisición o unidades que siguen en manos de una cohorte.

## Fuentes primarias leídas

[Grinblatt y Han, Prospect Theory, Mental Accounting, and Momentum, versión agosto2004, paper posteriorJFE2005](https://www.anderson.ucla.edu/documents/areas/fac/finance/prospect_momentum.pdf). Lectura de resumen y sección2.1/ecuación4, pp8–10 delPDF. Su proxy de precio de referencia pondera precios pasados por turnover y supervivencia posterior. El peso representa probabilidad de compra previa sin negociación posterior, bajo sus supuestos; usa volumen relativo a acciones existentes y una larga historia. Extracto breve: “weekly trading volume divided” (la definición completa continúa con acciones existentes). No se presenta como modelo de BTC ya validado. No se copia la fórmula sustituyendo turnover por volumen normalizado local.

[Schatzmann y Haslhofer, Exploring investor behavior in Bitcoin: a study of the disposition effect, arXiv2010.12415v2,2023](https://arxiv.org/abs/2010.12415). Se leyó el abstract primario y metadatos; no se afirma lectura completa delPDF. Estudia transacciones destinadas a exchanges como proxies de ventas. El abstract declara variación temporal de la presencia del efecto. No es evidencia de estrategia rentable con nuestro OHLCV y no identifica posiciones de BinancePerpetual.

## Motivo de HOLD y deduplicación

El inventario permitido actual acredita OHLCV BTC y tasas finales de funding, no historial de coste de tenedores, identidad de unidades, flujos on-chain o una tasa de renovación de una cohorte del contrato. Incluso una serie de OI total no identifica edades o precios de entrada individuales. El volumen negociado puede cambiar muchas veces la misma exposición; dividirlo por suma o máximo no produce una probabilidad de supervivencia.

N204ExploreR501 ya usa VWAP HLC3 por cohortes OHLCV de presión positiva/negativa como filtro, y V5VWAP usa media/varianza móvil ponderada. Añadir decaimiento o llamar sobrehang a otro centro ponderado con datos iguales no soluciona la brecha económica y se parecería a una reformulación de esos antecedentes. Fuentes completas N204ExploreR501 leídas; protocoloV5y cierresr4/R5consultados. No se afirma haber deduplicado exhaustivamente cualquier modelo de coste de tenencia del servidor.

Decisión: HOLD; no construir un proxy de inventario sin denominador/semántica defendibles. No pedir adquisiciones, descargar cohortes, sustituir por precio o calibrar una tasa de renovación para fabricar una prueba. La necesidad de datos queda documentada y no autoriza ampliación del alcance. El contrato10k/2%/6%/3x/costesfunding/2020–25permanece; este documento consume cero presupuesto económico.
