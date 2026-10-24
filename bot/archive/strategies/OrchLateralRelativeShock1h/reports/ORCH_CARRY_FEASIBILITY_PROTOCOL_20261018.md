# Propuesta documental: funding/carry BTC y ETH

Estado: DISEÑO, sin scripts, descargas, nuevos backtests ni modificaciones de framework. Fuentes primarias verificadas18oct2026. La nueva fuente informativa sería el pago de financiación y la base entre mercados; no otra combinación de OHLC. No existe evidencia de rentabilidad ni promesa de20–30% anual.

## Fuentes oficiales y límite de disponibilidad

La [API USD-M de Binance](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data) documenta:

|Necesidad|Interfaz pública|
|---|---|
|Funding realizado|/fapi/v1/fundingRate: fundingTime,fundingRate,markPrice; fechas inclusivas,paginación ascendente,hasta1000registros|
|Intervalos/caps ajustados|/fapi/v1/fundingInfo; no documenta una serie temporal completa de cambios|
|Referencias históricas|/fapi/v1/markPriceKlines,/fapi/v1/indexPriceKlines,/fapi/v1/premiumIndexKlines, con fechas e intervalos|
|Basis empaquetado|/futures/data/basis; sólo últimos30días|

La existencia de parámetros históricos no prueba cobertura íntegraBTC/ETH2020–2025: debe verificarse tras autorización. No sustituir seis años de basis por sus30días recientes. La alternativa a evaluar es reconstruirlo de precios sincronizados Spot/perpetual; mark/index no son precios ejecutables.

[Binance Public Data](https://github.com/binance/binance-public-data) describe archivos diarios/mensuales y checksums; los timestamps de archivosSpot desde2025 son microsegundos. Su README no documenta cobertura de funding, por lo que no se presume. Versionar hash/fecha de descarga; normalizar unidades sin mezclarSpot2025 con milisegundos.

La [explicación oficial de funding](https://www.binance.com/en/support/faq/detail/360033525031) define pagos según nominal al mark: funding positivo paga de long a short; negativo invierte ese flujo. Los intervalos pueden cambiar y hay desviación temporal alrededor del settlement; el débito puede afectar el margen de liquidación. Usar eventos reales, no rejilla8h fija ni condiciones actuales aplicadas retrospectivamente.

## Qué permite hoy el MCP

Las herramientas visibles importan/leen OHLCV y ejecutan estrategias; no hay herramienta nativa visible para funding/basis histórico ni un ledgerSpot+perpetual con funding. No se probará carry mediante una curvaOHLC a la que luego se añada un ingreso fijo. run_analysis sólo admite snapshots, no descargar datos externos ni leerCSV externos para eludir el opt-in.

Un backtest con10000 por cada exchange tampoco representa10000 compartidos: duplicaría capital. La investigación requiere contabilidad explícita de efectivoSpot, tenenciaSpot, collateralFutures, PnLrealizado/no realizado, pagos de funding, transferencias y costes. No se ha implementado ese ledger ni inspeccionado/cambiado framework para crearlo.

## Primera hipótesis económica propuesta, aún no implementada

Carry positivo del MISMO activo: comprarSpot y vender igual cantidad base de perpetual linealUSDT. Esto difiere del hedgeβBTC/ETH descartado. No asumir neutralidad perfecta: precios divergen, ejecuciones se descalzan y las cuentas/márgenes son separados.

Primera versión evitaría el carry inverso: venderSpot prestado exigiría disponibilidad y coste histórico de préstamo, ausentes. BTC y ETH se investigarían ambos, con presupuesto ex ante idéntico, sin elegir luego el activo ganador. Ventana económica común2020-10-15→2025-12-31exclusivo;2026 excluido desde adquisición/modelado.

Regla preliminar reproducible: al cierre diario, usar sólo funding ya liquidado con retraso conservador1h; sumar7días naturales anteriores y proyectar30días sólo como previsión, nunca ingreso garantizado. Entrar en carry positivo si esa proyección cubre al menos dos roundtrips de ambos mercados más reserva de spread/impacto. Mantener como máximo30días; salir antes si la suma pasada7días deja de ser positiva, por pérdida conjunta presupuestada o por margen insuficiente. No optimizar7/30 sobre esta misma muestra.

El funding del siguiente settlement es FUTURO al decidir. Su valor realizado sólo sirve como cashflow cuando el evento ocurre y la posición cumple la elegibilidad, jamás como señal conocida de antemano. No usar el campo actualestimated/lastFundingRate como archivo histórico point-in-time. Premiumhistórico puede ayudar a investigar previsiones, pero replicar fórmulas/caps históricos es un proyecto aparte; primera versión usaría únicamente pagos pasados.

## Capital, costes y riesgos que debe resolver el ledger

Propuesta de estudio prudente: no apalancarSpot; dejar20% de capital como efectivo y reservar collateralFutures económico de100% del nominalshort. Así, con N deSpot yN decolateral, Ntotal<=40%capital y exposición brutaSpot+Perp<=80%. Son supuestos de diseño, no configuración nativa de Jesse ya verificada. Configurar5xaislado NO equivale a haber añadido ese collateral: deben modelarse el margen real, mantenimiento, liquidación al mark y posibilidad efectiva de transferir. No atribuir automáticamente ganancias no realizadasSpot al margenFutures.

Riesgo inicial conjunto previsto<=1%capital,<=0.5%por activo y<=8%global, incluyendo spreadadverso/fees y cierre; no usar estos límites como garantía contra gaps/liquidación. Stops de precio independientes en ambas piernas pueden destruir el hedge: deben cerrarse ambas ante evento de margen o basketstop, con latencia explícita y cotizaciones actuales. Si no se puede demostrar esa contabilidad, se rechaza la simulación.

Mantener0.00045porlado enFutures como acuerdo. La tarifaSpot no puede inferirse de la de perpetual; estudiar0.001porlado como supuesto conservador provisional, sin afirmar que sea la tarifa real de la cuenta. Con esos supuestos el coste inicial+final de ambos mercados es2*(.001+.00045)*N=.0029N, antes de spread/impacto. La rentabilidad debe dividirse por TODO capital comprometido/reservado, no sólo el margen inicial deFutures.

PnLbasket=q*(Spotfinal−Spotinicial)+q*(Perpinicial−Perpfinal)+fundingcobrado−fees−impacto−otroscostes. Basis se marca a mercado, no se supone convergencia de un perpetual en fecha fija. Funding puede cambiar de signo; congelar nominal/futurosingresos no elimina pérdidas de basis, colateral o exchange. No incluir rendimiento de cash/Spot ni préstamos gratis por defecto. Los contratos con vencimiento serían otra hipótesis: historial de contratos/expiraciones/rolls debe verificarse; no reemplazarlos con perpetuals.

La referencia ya usaBTCperpetual enBinanceone-way. Una pata carry no sería simultáneamente independiente: requeriría neteo/alternancia o asignación de cuentas permitida por el usuario. No sumar curvas para certificar una cartera ejecutable.

## Entregables y criterios antes de pedir más complejidad

EtapaA propuesta: descargar sólo datos públicos2020–2025, manifest/hashes, huecos/duplicados/eventtimes/unidades y cobertura por activo; mostrar montos de funding realizados de un nominal constante sólo como descripción, sin convertirlos en estrategia. Validar límites inclusivos y evitar duplicar eventos al paginar.

EtapaB, sólo si los datos son completos y hay presupuesto neto plausible: ledger independiente de dos mercados con balances separados y pruebas contables; simulación causal de la regla fijada, feesSpot/Futures separados, spread/impacto y marginstress. La primera etapa no autoriza automáticamente tocar framework ni desarrollar live.

Rechazar o declarar inconcluso ante cobertura no verificable, forward-lookingfunding, insolvencia de una cuenta pese a equity agregada positiva, coste que elimina margen, exposición huérfana no acotada o dependencia de unos pocos episodios. Mantener objetivos de regularidad yDD del proyecto; rentabilidad insuficiente no se arregla subiendo leverage. Si promete, controles de retardos/costes/intervalos/períodos antes de integrar y antes de2026.

## Autorización pendiente para scripts, no para este documento

bot/AGENTS.md y jesse://research_scripts dicen que una solicitud genérica de investigar no consiente crear/ejecutar scripts. Sería necesario pedir autorización específica para un descargador público y/o el módulo research/ledger. Alcance concreto sugerido: scripts bajo research_scripts/ víaMCP, allowlist de endpoints públicosBinance, fechas2020–2025, sin claves/.env/cuentas reales, sin instalaciones, órdenes, live/Pi ni cambios del framework. No se ha creado ningún script ni iniciado descarga de funding/basis.

Recomendación: pedir primero el opt-in limitado de EtapaA, no prometer un nuevo sistemacarry validado. Datos y contabilidad determinarán siEtapaB merece el trabajo.


## Dependencias todavía no verificadas

Faltan cobertura histórica realSpot/mark/index/premium, spreads bid/ask y profundidad, niveles históricos de mantenimiento/liquidación, restricciones por símbolo y transferencias entre wallets. Las reglas o tarifas actuales no bastan para demostrar retrospectivamente la cuenta de2020. Si un funding antiguo carece de mark asociado, la falta se identifica; no sustituirlo por el precio de una vela futura. No se leerán claves para consultar datos privados.

Como presupuesto de diseño paraEtapaB, cada activo usaríaN<=20% del capital total ystop de basket a pérdidaMTMneta0.5% del capital total; ambos juntos1%. Es una regla de cierre prevista, no garantía de pérdida máxima. Antes de implementarla hay que demostrar que las cuentas sobreviven hasta ese cierre bajo estrés al mark y que la liquidación/transferencia es ejecutable. Si no se puede, el estudio queda incompleto aunque la sumaSpot+Futures parezca estable.
