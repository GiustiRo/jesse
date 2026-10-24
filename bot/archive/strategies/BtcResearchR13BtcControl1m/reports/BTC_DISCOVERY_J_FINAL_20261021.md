# Tanda J cerrada: confirmación ETH frente a control BTC

Las dos políticas pierden y no cumplen los objetivos. ETH se usó sólo como información: todas las posiciones, comisiones y funding fueron BTC. La reducción de actividad mejoró el resultado relativo del tratamiento, sin generar rentabilidad ni acreditar causalidad ETH→BTC.

## Reglas y contrato

La dirección se definió con seis retornos BTC previos. BTC actual debía moverse dentro de una desviación previa; ETH_CONFIRM agregaba un shock ETH de al menos dos desviaciones en esa dirección. El control mantenía el mismo patrón BTC. Entradas horarias; stop2ATR14simple1h, TP2R y vencimiento6h. El umbralBTC1sigma fue declarado antes de ejecutar, diferente del .25sigma del antecedentePAXG. No hubo OLS residual, hedge ni estrategia ETH.

Ventana [2020-10-15,2026-01-01), desarrollo reutilizado, BTC-USDT Binance Perpetual Futures. Capital10k, riesgo2%/6%/3x, fee.00045porlado, funding histórico aplicado con proxies declarados, slippage0. Sin estrés, nueva economía2026 ni importaciones. Motor validó cobertura BTC/ETH sin ventanas inválidas.

| Política | CAGR neto | DD M1 y ejecuciones | PF | Meses activos positivos | Trimestres positivos | N |
|---|---:|---:|---:|---:|---:|---:|
| [BtcResearchR13EthConfirm1m](http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a) | -8.90% | 44.24% | 0.708 | 24/61 | 4/20 | 225 |
| [BtcResearchR13BtcControl1m](http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0) | -81.57% | 99.99% | 0.884 | 9/62 | 1/20 | 6808 |

Dashboard: http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a

BtcResearchR13EthConfirm1m: neto-3849.06USDT; bruto de precio-1318.34, fees2375.58, funding-155.13; saldo final6150.94; Sharpe-0.8971. Mediana mensual calendario-0.9073%; neto sin dos mejores meses-4697.44USDT.

Dashboard: http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0

BtcResearchR13BtcControl1m: neto-9998.53USDT; bruto de precio2107.80, fees11874.14, funding-232.18; saldo final1.47; Sharpe-2.9721. Mediana mensual calendario-13.0230%; neto sin dos mejores meses-12816.69USDT.

## Qué aprendimos

El control realizó6808 operaciones y terminó con1,47USDT. Su resultado bruto de precio fue positivo, pero no cubrió comisiones y funding. Es un resultado simulado completo, no una cuenta operativa ni un experimento cancelado por pérdidas parciales. ETH_CONFIRM redujo a225 operaciones, pero también perdió antes de fees. No basta reducir rotación para encontrar la ventaja. La diferencia mezcla selección, ocupación y trayectorias de capital; no es efecto causal aislado del inputETH.

Ambas fallan CAGR30, PF1.2, DD25, M65 yQ80, mediana y concentración. Los conteos por sí mismos no aportan confianza estadística. Cerrar las dos recetas y sus vecinos; no elegir long-only, otras sigmas u horas tras observar resultados.

## Auditoría y cierre

Protocolo y manifiesto guardados antes de economía. Check7efe483fb2214f7f8418e49f191211b3 passed; fuenteSHA256aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a. Revisión independiente sin errores materiales. Análisis a189e8474f5b4e7ea94da9879d22527c completo225/6808trades: bruto−fees+funding=sumaPNL=equityfinal−10k, error<1e−6USDT. Ambas telemetrías tienen2.741.760marcasM1,63intervalos/62meses/20Q; fronteras y contribuciones reconciliadas. DDM1noextremosintraminuto; cortes mensuales postfunding/predecisión según convención por fase R11. Sin posiciones terminales, errores económicos ni reemplazos.

Fuentes: BTC_DISCOVERY_J_PROTOCOL_20261021.md, BTC_DISCOVERY_J_MANIFEST_20261021.json, BTC_DISCOVERY_J_ACCOUNTING_20261021.json y telemetrías. Framework/configglobal intactos; sinpaper/live/Pi. Desde r9 van19corridas cerradas; no son muestras independientes. Objetivo pendiente; continúa investigación autónoma con otra pregunta material.
