# V6 NR7 — smoke técnico aprobado

Dashboard: http://localhost:9200/#/backtest/3dc0cf2e-e35a-4d54-aef0-bd644138c259

Sesión 3dc0cf2e-e35a-4d54-aef0-bd644138c259, ResearchV6Nr7Smoke4h, BTC-USDT Binance Perpetual Futures, 4h, [2020-09-01,2020-09-08). Nominal exacto REGISTRY_V6, balance10.000,isolated3x/cap1x,risk2%stop+fees,funding históricoON,fee0.00045/slip0,OI histórico; debug/fast solicitados y exports/benchmark desactivados. Fast efectivo false por funding.

## Resultado técnico

El motor terminó sin error. Se ejecutaron89 comprobaciones NR7 y67 comunes, todas aprobadas. Se recorrieron28 líneas completas de logs, máximo1080caracteres, y el único trade completo. La auditoría de ejecución agregó35 verificaciones conformes.

42decisiones, una entrada short y un cierre final forzado. El resumen before_terminate reporta cero cierres porque el único cierre ocurrió después; trade, V6_CLOSE y saldo terminal lo incluyen. No se infiere una posición residual activa a partir del total_open_trades1/open_pl precierre.

NR7: siete rangos previos, setup205.28 menor estricto que mínimo previo235.37. Cierre10409.93<low del setup10430.49; la entrada MARKET se ejecutó enT, no retroactivamente al nivel roto. La ventana8OHLC y ATR actual15OHLC/14TR tienen relojes exactos y offset0.

ATR337.6042857143; distancia2ATR675.2085714286, stop11085.1385714286 y TP8384.3042857143 desde fill10409.93, RR3. Cantidad0.29202138, plan de stop+fees199.99999763USDT<=200 y cap nocional respetado. La cuota UTC y metadata temporal coinciden.

Se procesaron21settlements, con ocho cashflows efectivos y funding+2.3881036024USDT. Se verificó identidad por trade bruto−fees+funding=PNL; la conciliación completa de ledger/órdenes/equity corresponde a root mediante snapshot.

## Métricas descriptivas, no selección

N1, neto0.087586%, DD-0.651494%, Sharpe0.696235, saldo final10008.75857614USDT. PF no definido por ausencia de pérdidas. Estas métricas semanales no seleccionan parámetros ni acreditan edge, muestra o meta anual.

No hubo fallo técnico, reintento de arranque ni cambio de fuentes. Draft, configuración leída de vuelta y start_requested se persistieron antes del único start; run respondióstarted.

## Cobertura y siguiente paso

Hubo fill short y callback real de cierre forzado. Stop/TP, hold96h y calendario semestral no llegaron a ejecutarse en este smoke; sus niveles o ramas deterministas no equivalen a fills reales. No hubo entrada long ni gateOI económico porque el smoke heredaP. No atribuir cobertura no observada.

AUDIT_ResearchV6Nr7Smoke4h.json conserva logs/trade completos,35checks y limitaciones. V6_NR7_PROGRESS.json preserva fuentes y respuestas de sesión. Token motor liberado. Esperar GO de root antes de cualquier SCREEN; no se iniciaron jobs de análisis ni otras sesiones y2026 permanece cerrado.
