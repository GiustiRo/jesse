# BTC perp individual: viabilidad documental de funding — 2026-10-18

Estado: documentación primaria oficial y diseño de auditoría, SIN descargar datasets, consultar tasas/precios reales, crear scripts/integraciones, instalar paquetes o ejecutar simulaciones. No se abrió rendimiento/precios2026. La documentación vigente puede contener cambios normativos/técnicos fechados2026; eso no abre el lockbox.

Este informe estudia UN activo BTC perp, principalmente BinanceBTCUSDT. No propone cestaBTC/ETH, carrySpot+perp, arbitraje entre exchanges o panorama global de posicionamiento. El antiguo diseño carry del mismo directorio es otra línea histórica.

## Una recomendación

Priorizar una auditoría futura, acotada y monocontrato de financiación REALIZADA BinanceBTCUSDT2020–2025 como coste/cashflow del instrumento, antes de utilizar funding como señal de trading. Esto añade información económica que las velas de precio no contienen y aborda una omisión de realismo más directamente que otro filtro OHLC. No demuestra una ventaja predictiva ni que podamos alcanzar65/80.

La aprobación actual sólo cubre esta documentación: ninguna adquisición o integración se inició. Si después se autoriza esa auditoría, su primera decisión debe ser cobertura/semántica/licencia, no buscar la variante con más rendimiento. Bybit sería contraste externo posterior de robustez sobre tramos comunes, no reemplazo de tasas Binance para cobrar su financiación.

## Cobertura documentada y límites: posibilidad no equivale a dataset validado

| Fuente/contrato | Interfaz oficial y retención declarada | Consecuencia para2020–2025 |
|---|---|---|
| BinanceUSD-MBTCUSDT | GET/fapi/v1/fundingRate: fechas inclusivas, orden ascendente, hasta1000registros; fundingTime, fundingRate y markPrice asociado al cargo. Límite compartido500/5min/IP con fundingInfo. No documenta aquí una retención corta ni garantiza todos los años. | Contrato existía en2019, pero continuidad/completitud2020–25 NO verificadas sin datos. Mejor candidato por coincidir con nuestro instrumento simulado. [APIoficial](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data), [existencia2019](https://www.binance.com/en/blog/all/421499824684900356). |
| BybitBTCUSDTlinear / BTCUSDinverse | GET/v5/market/funding/history: startTime+endTime, máximo200; sólo startTime produce error. Devuelve tasas ya liquidadas. La página no certifica fecha inicial ni completitud multianual. | Cobertura exacta2020–25 y contrato concreto pendientes. Linear e inverse no son intercambiables. [Documentación](https://bybit-exchange.github.io/docs/v5/market/history-fund-rate). |
| OKXBTC-USDT-SWAP / BTC-USD-SWAP | RESTfunding-rate-history sólo hasta3meses, máximo400, before/after. Portal oficial anuncia archivosfunding desdeMarzo2022. | RESTactual no recupera2020–25 completo; archivo anunciado tampoco cubre2020–21. No rellenar esos años con otro exchange. [REST](https://app.okx.com/docs-v5/en/#public-data-rest-api-get-funding-rate-history), [archivo anunciado](https://www.okx.com/historical-data). |
| KrakenBTCperp: identificar contrato exacto | RESThistorical-funding-rates por símbolo, tasas ordenadas por timestamp; campos fundingRate y relativeFundingRate. Soporte ofrece exportaciónCSV por mercado desde inception; no abrí el archivo. | No se validó qué históricoBTC existe, sus fechas ni continuidad entre inverse/linear/cambios de símbolo. La existencia de un export no acredita cobertura de nuestro contratoBinance. [REST](https://docs.kraken.com/api-reference/historical-funding-rates/historical-funding-rates), [export oficial](https://support.kraken.com/articles/export-historical-funding-rates). |
| CoinbaseInternationalBTC-PERP | Endpointinstrument/funding, result_limit≤100 y offset; funding_ratefinal,mark_price,event_time. Exchange lanzóBTCperp enMay2023. | No puede aportar historiaINTX2020–22. Submuestra2023–25 sólo si luego se valida retención/semántica. No sustituir por CoinbaseSpot o futurosUS. [API](https://docs.cdp.coinbase.com/api-reference/international-exchange-api/rest-api/instruments/get-historical-funding-rate), [lanzamiento](https://www.coinbase.com/en-in/blog/introducing-coinbase-international-exchange). |

No se hicieron solicitudes a endpoints de DATOS, ni comprobaciones de primera/última fila, huecos o valores. Las fechas de existencia de contrato no prueban retención de su API; los ejemplos de documentación no prueban cobertura. No certifico disponibilidad de2020completo en ninguna fuente sólo por aceptar startTime.

Las interfaces citadas son públicas/documentadas y no encontré precio de suscripción en esas páginas. Eso no garantiza acceso desde toda región/IP, servicio perpetuo, ausencia de límites ni una licencia de redistribución/producción.

## Uso1: coste real del instrumento

Para un contrato linealUSDT y posiciónBTC firmada q (longpositivo), cashflow de una liquidación elegible = −q*markPrice_settlement*rate_realizada, enUSDT. Esta es una especificación contable, no una expectativa de beneficio. La financiación puede ser ingreso o gasto; debe asignarse al lado/posición realmente abierta y al evento correspondiente.

Binance describe intercambio entre longs/shorts, cargo sobre nominal marcado y participación de posiciones abiertas en el instante de financiación. Advierte desviación de15segundos y posibles cambios de intervalo; no fijar tres cargos diarios para todos los años. [Mecánicaoficial](https://www.binance.com/en/support/faq/detail/360033525031). Bybit advierte incertidumbre de inclusión al abrir/cerrar dentro de5segundos alrededor del cargo y posible deducción de margen. [MecánicaBybit](https://www.bybit.com/en/help-center/article/Funding-fee-calculation?category=cd60af6303161fd598).

Requisitos futuros:
- Identificar funding events reales y la cantidad vigente en cada uno, incluidas variaciones/parciales si existieran. No cargar toda la financiación al mes de cierre del trade.
- Usar mark_price aplicable, no sustituir sin aviso por OHLC de último trade o por entry_price.
- Resolver el orden de entradas/salidas/cargos en fronteras temporales. Con replayM1, documentar y acotar cargos de operaciones demasiado cercanas a la liquidación; no escoger la convención favorable.
- Incorporar cashflows en wallet/margen/equity durante el replay si se pretende recalcular una cartera ejecutable. Pueden cambiar tamaños, órdenes rechazadas y liquidación.
- Un overlay de cargos sobre fills congelados es diagnóstico aritmético; NO nuevoCAGR/DD, ni una cuenta realmente simulada con financiación, ni prueba de impacto cero en sizing.
- COIN-M/inverse y USDC tienen otras unidades/monedas/valoración: no aplicar mecánicamente la fórmulaUSDT.

Esto mantiene la comisión0.00045porlado: trading fee y funding son conceptos distintos, no reemplazos. No aumenta el riesgo ni autoriza tocar framework. El inventario de herramientasMCP no expone una herramienta nativa cuyo nombre modele funding/basis; la futura integración necesitaría una revisión de soporte separada, no un atajo dentro de Strategy.

## Uso2: señal de presión relativa, no observación de posicionamiento global

Hipótesis potencial: la prima de perp, financiación y sus límites reflejan condiciones distintas de sólo OHLC del último trade. Puede servir como feature causal de coste/crowding local. Pero funding incluye fórmulas, interés, clamps y cambios de metodología; no identifica cuántos compradores netos hay, ni demuestra liquidaciones, flujos o dirección futura. Cada contrato tiene contraparte long/short: fundingpositivo no significa por sí mismo un exceso de cuentaslong medido.

No existe aquí evidencia de que debamos continuar o revertir una tasa extrema. No elegir el signo o umbral tras ver qué rescata los meses conocidos. Un predictor necesitaría protocolo nuevo después del control de datos, una comparación neta conOHLCbase y robustez a retrasos/costes; muchos regímenes y mercados compartidos no son muestras independientes.

### Esquema de normalización as-of exigible

Guardar por fila: exchange, instrument_id y versión, moneda de margen/liquidación, lineal/inverso, unidad original, rate_kind(realizada/prevista), event_time/finalization_time, effective_period_start/end, settlement_time, publication_time(si existe), first_observed_at(si se capturó), retrieved_at y procedencia. UTCmilisegundos normalizados; conservar campos originales.

No confundir estos tiempos:
- BinancefundingTime y BybitfundingRateTimestamp marcan la liquidación histórica; el historial liquidado NO archiva todo lo que la pantalla pronosticaba antes.
- OKX distingue fundingRate previsto de realizedRate real y methodcurrent_period/next_period. El histórico de previsiones no es automáticamente una seriepoint-in-time con timestamps de publicación. [Camposoficiales](https://app.okx.com/docs-v5/en/#public-data-rest-api-get-funding-rate-history).
- Coinbaseevent_time es cuando quedó determinada la tasa final, no necesariamente el momento exacto en que un cliente la recibió. Su especificación debe validar unidades antes de comparar el escalar con otras venues. [Definición](https://docs.cdp.coinbase.com/api-reference/international-exchange-api/rest-api/instruments/get-historical-funding-rate).
- Kraken documenta una metodología previa a29Sep2022 con tasa fijada para el período siguiente, acumulación continua ybooking4h; ese día cambió a1h. No modelarlo como simple foto de posición en un settlementBinance. [Método previo](https://support.mtf.kraken.com/hc/en-us/articles/7009378818333-Inverse-Perpetual-Contracts-Funding-Rate-Method-Prior-to-September-29-2022). Distinguir absolute fundingRate/relativeFundingRate y especificación de contrato. [Contrato](https://support.kraken.com/articles/360022835911-inverse-crypto-collateral-perpetual-contract-specifications-derivatives).

Para costes se necesita la tasa real efectivamente aplicable al intervalo/settlement. Para señales sólo datos disponibles antes de decidir: no colocar r_realizada_t al inicio de su ventana porque hoy sabemos el resultado. Si publication_time histórico no existe, cualquier lag conservador es una ASUNCIÓN explícita, no disponibilidad demostrada; no etiquetar como “exacto asof”. Una futura prueba sólo con tasas liquidadas rezagadas puede reducir fuga, pero no reconstruye previsiones perdidas ni sus revisiones.

Normalización de comparación: expresar fracción por unidad de período y, sólo como descripción, equivalente por hora con duración real. No anualizar automáticamente como ingreso garantizado ni multiplicar una tasa8h por365. Para cashflow usar contrato/moneda/posición y mecanismo real, no esa escala de display.

## Open interest y composite: no son prerrequisito del primer paso

La auditoría de costeBinanceBTCUSDT no necesitaOI ni un índice de exchanges. Para “crowdingglobal” sí faltarían universo causal, cobertura, pesos contemporáneos, unidades/contracts,collateral/precios históricos, timestamps de publicación y reglas para venues que aún no existían.

BinanceopenInterestHist declara sólo el último mes; no es historial2020–25 por paginar más. BybitOI ofrece fechas/cursor y unidades distintas (inverseUSD/linearBTC); no valida por sí solo publicación histórica ni comparabilidad. [Binance](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data), [Bybit](https://bybit-exchange.github.io/docs/v5/market/open-interest).

No ponderar funding2020 conOIactual, no rellenar Coinbaseantes2023 con cero, no sumar nominales dobles y no llamar una media de dos venues “mercado global”. La ausencia deOI completo no bloquea estudiar financiación del contrato propio; bloquea afirmar una medición global que no poseemos.

## Acceso y licencias verificadas

Los términos actuales del repositoriooficialBinanceVision, versión1.0actualizada26Aug2026, indican acceso sin cargo a sus datasets bajoCCBY-NC-SA4.0, investigación personal no productiva y restricciones comerciales/producción; declaran que los datos ya descargados se rigen por los términos vigentes en su descarga. [Textooficial](https://github.com/binance/binance-public-data/blob/master/TERMS_AND_CONDITIONS.md).

Esto es información documental, no una interpretación jurídica ni conclusión sobre todos los endpointsREST. No asumir que licencia de código=licencia de dataset, ni que público/gratis=uso comercial irrestricto. Alcance de términos/API, jurisdicción y futura producción requieren confirmación antes de esa adquisición/uso concreto. No modifiqué ni cuestioné retrospectivamente la licencia de archivos existentes.

Para las otras fuentes no verifiqué una licencia expresa de redistribución/producción en las páginas consultadas; queda desconocida, no “permitida”. Kraken ofrece el export y OKX el portal, pero no abrí datasets ni acepté condiciones de descarga.

## Criterio de continuar o retirar la línea

La recomendación única sigue siendo contabilidadmonocontratoBinance primero. Merece prioridad como mejora de realismo frente a otro filtroOHLC porque constituye un cashflow del mismo instrumento, NO porque prometa alpha.

Antes de un posterior estudio predictivo: exigir cobertura del tramo2020–25 declarado, eventos/monedas/unidades deduplicados, huecos e intervalos explicados, markprices válidos y semántica/asof documentada. Si no puede reconstruirse el coste con precisión suficiente, informar incertidumbre o cotas; no presentar resultadosnetos completos ni fabricar financiación. Si faltan archivos históricos de forecasts/publicación, retirar cualquier estrategia que los requiera en vez de usar el realizado futuro.

Ni Bybit/OKX/Kraken/Coinbase se añaden al bot en este informe ni se inicia un composite. No hay promesa deedge,rentabilidad,65/80ni recomendación de operar. No se cambia SPYsource ni otra estrategia, ni se solicita ahora editar framework.
