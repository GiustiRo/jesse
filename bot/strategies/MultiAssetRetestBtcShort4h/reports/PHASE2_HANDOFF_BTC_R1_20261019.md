# Phase 2 — handoff BTC R1 — 2026-10-19

## Decisión

Ronda terminada: tres agentes nuevos, nueve hipótesis distintas evaluadas por separado y 18 full backtests finalizados sin errores. Se ejecutaron pares B/C simultáneos, con cuatro backtests y dos análisis como máximos globales. No quedan trabajos pendientes ni hay otra ronda automática autorizada.

**BtcExploreR103 queda como candidato congelado de investigación.** Mejora neto y CAGR en ambas carteras y alcanza 65% de meses activos y 80% de trimestres positivos con comisión base, incluyendo parciales. Su regularidad falla con +5 bps RT de coste adicional. No se promueve ni se declara robustamente validado. B/C comparten muestra y mecanismo BTC; no constituyen validaciones independientes.

Leer primero BTC_R1_RESULTS_20261019.md y BTC_R1_COST_CALENDAR_20261019.md, bajo strategies/MultiAssetRetestBtcShort4h/reports/ dentro del proyecto Jesse. Después, protocolo congelado, revisión de fuentes, registro de sesiones y tres auditorías exactas.

## Contrato preservado

- Datos: 2020-10-15→2025-12-31 **exclusivo**, último día 2025-12-30. **2026 sigue cerrado**. Muestra 2020–2025 intensamente reutilizada de desarrollo.
- OHLCV existentes; proxies PAXG/SPY aceptados. Sin nuevos datos, funding o derivados.
- Cuenta compartida 10000 USDT; riesgo 1% por trade y 8% agregado; isolated 5x; cap nocional 4.4; fee .00045 por lado en todos los tipos; reserve .001 sólo para sizing; sin pyramiding.
- BTC/PAXG/SPY en ese orden, 4h y tres datos M1; warmup 240, debug=true, fast=false, export_chart=true. Los logs requieren debug=true.
- Originales PortCompareBtc4h, PortComparePaxgMarket4h, PortCompareSpySecond4h y PortCompareSpyMarket4h releídos por root y byte-idénticos a las versiones iniciales. Sin cambios de default, producción, live, paper, framework o configuración global.

No comparar con la antigua cartera de riesgo 3%.

## Referencias y candidato

| Sesión | Neto USDT | CAGR | DD motor | Meses completos positivos/activos | Meses con parciales | Q completos | Q con parciales |
|---|---:|---:|---:|---:|---:|---:|---:|
| [B control](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f) | 9234.194391 | 13.366850% | −7.496635% | 37/57 | 37/59 | 16/19 | 17/21 |
| [X03 B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127) | 11964.238131 | 16.289896% | −8.253965% | 41/61 | 41/63 | 16/19 | 17/21 |
| [C control](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835) | 9407.826226 | 13.562427% | −8.168013% | 38/57 | 38/59 | 16/19 | 17/21 |
| [X03 C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c) | 12135.876834 | 16.463647% | −9.009386% | 42/61 | 42/63 | 16/19 | 17/21 |

Hay 61 meses calendario completos y 63 incluyendo fronteras. X03 tiene todos activos; los controles no. B pasa nominalmente por un margen estrecho: 41/63=65.0794%. El objetivo aspiracional de 70% de meses y 20–30% CAGR no se alcanza.

B usa SPY PortCompareSpySecond4h; C usa PortCompareSpyMarket4h. PAXG usa PortComparePaxgMarket4h. En los candidatos sólo BTC cambia a BtcExploreR103.

## Mecanismo congelado de X03

Mantiene los planes originales y runners long con prioridad. Añade shorts tras discrepancia entre retorno positivo de 12 barras y suma negativa de volumen ponderado por ubicación del cierre en el rango. Es un proxy OHLCV, no flujo agresor observado. Luego exige pérdida de VWAP12_s, congelada al origen, en una vela posterior bajista.

Entrada MARKET; stop max(high_s, high_t)+.25ATR, con distancia 1..3ATR; target 2R; timeout 48h. Primer false→true del setup completo; estado avanza incluso ocupado o con órdenes pendientes. Sin cola de señales antiguas. Reglas exactas en fuente, protocolo y QA; no ajustar 12/2R/48h al resultado.

79 shorts suplementarios MARKET + 113 originales STOP = 192 frente a 125 base: **67 trades netos más**, no 79. Se retienen 112 entradas short base, se desplazan 13 y aparece una original distinta; 80 entradas nuevas = 79 suplementos + una original. Los 31 long BTC conservan todos sus horarios de entrada y salida. Cantidades y PNL son endógenos al capital.

Suplemento neto B/C: 2107.76/2087.17 USDT; con +10 bps, 1590.19/1571.17. Excluyendo sus tres mejores trades y añadiendo +10 bps queda 578.67/544.93. Cerca del 80% del neto procede de 2022 y 2025; 2024 y el parcial de 2020 pierden. Más actividad, exposición y fees; DD y PF empeoran, neto y Sharpe mejoran.

## Fricción decisiva

Overlay estático aplicado por cada fill, con precios, cantidades y timestamps congelados; MTM y retornos calendario recalculados. No son backtests nuevos ni modelo de resizing, latencia, gaps o funding.

- +5 bps RT: ambos X03 quedan 40/61 meses completos y 15/19 Q; incluyendo parciales, 40/63=63.4921% y 16/21=76.1905%. Fallan el objetivo conjunto.
- +10 bps RT: X03 B neto 9878.122876, meses 37/61 y 37/63, Q 14/19 y 15/21. X03 C neto 9942.012024, meses 38/61 y 38/63, Q 15/19 y 16/21.
- Controles con +10 bps: 7720.949024 B y 7792.529096 C. La ventaja neta de +2157.17/+2149.48 persiste; la regularidad objetivo no.

DD diario al cierre de X03: −8.313517%/−9.068338%, diferente del DD del motor. Peor Q nominal −3.9043%/−4.7159%, peor que referencias.

## Otras ocho recetas

- Entry E01: volumen direccional 24h; neto y regularidad inferiores.
- Entry E02: caída sin vela dominante; quedan 62 shorts con bruto y neto negativos.
- Entry E03: target sobre mínimo previo de cinco días; DD menor, pero neto inferior y regularidad con parciales falla. Sus 44 shorts tienen bruto negativo.
- Payoff P01: stop EMA20 descendente; mejora meses y DD, pero Q 15/19 B y 14/19 C.
- Payoff P02: equilibrio con fee tras medio target; neto y DD empeoran.
- Payoff P03: salida RSI3>=50; neto short cercano a cero y negativo bajo coste extra.
- Explore X01: rechazo y recuperación de shock vendedor; cero eventos elegibles completos contados y cero suplementos. No hay diagnóstico de causas de rechazo; no relajar reglas.
- Explore X02: semivarianza bajista persistente; sustituye shorts originales por 96 nuevos con bruto y neto negativos.

No repetir estas recetas como nuevas, seleccionar umbrales alternativos ni combinarlas con X03 para rescatar métricas en esta ronda.

## QA y evidencia

Root verificó 18 formularios y 54 snapshots. Las 18 auditorías conciliaron fills, cantidades, fees, PNL, wallet, terminal y MTM diario. QA sintética: 128 checks Explore + 101 Payoff; auditorías de órdenes ejecutadas Payoff sin violaciones detectadas. Los stubs no recalculan indicadores históricos y los snapshots no contienen modificaciones/cancelaciones completas.

Sólo las tres copias Entry corrigieron un comentario de logging después de sus corridas. No cambió executable; root verificó reversión exacta a bytes congelados. Snapshots originales intactos.

Contadores: no intentos con capacidad cero, lot rounding cero, margen o riesgo agregado limitantes; sí recortes por room nocional/cuota de volatilidad. Se cuentan planes que llegan a sizing, no señales ocupadas. events_occupied describe estado en before, no rechazos: el motor puede cerrar y entrar de nuevo con una señal fresca en la misma barra. Cierres terminales conciliados; open1 preterminación no indica residual ni demuestra liquidez al precio final.

Auditorías principales: ad66331f9c894766a156a4b6cd75d216; 831bac3de3cb4ff1953bd28756787b33; 46f434f9e40d46289f61102144344722. Calendario de costes: b103dc4be3a245e4a4c0f1b135b9a91b. Código reproducible inline en BTC_R1_AUDITOR_SOURCE_20261019.md y BTC_R1_COST_CALENDAR_SOURCE_20261019.md. Resultados exactos y 18 enlaces en registro.

## Continuación

Priorizar validación temporal y de ejecución de X03 con reglas y criterios congelados, antes de otra búsqueda amplia. Los vecinos sirven para sensibilidad, sin escoger el mejor. Los datos 2020–2025 siguen siendo desarrollo. Cualquier apertura de periodo reservado requiere acordarla antes de consultar resultados; 2026 no se abrió. No activar operativa real.
