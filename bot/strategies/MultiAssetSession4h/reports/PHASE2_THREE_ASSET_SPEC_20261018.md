# Fase 2: especificación previa a resultados de tres activos

## Decisiones del usuario

Investigar 2020–2025; no consultar rendimiento ni calibrar con 2026. Objetivo de fase 2: longs y shorts útiles, no shorts forzados. Riesgo máximo por operación 3%, agregado planificado 8%, cuenta compartida de 10000 USDT, 5x aislado, fee 0.00045. Riesgos reales pueden superar presupuestos ante gaps/slippage.

## Datos

BTC nativo futures; PAXG proxy Spot copiado a futures; SPY proxy SPX/USD CFD de HistData dividido por10. Se copiaron a futures 1.974.135 filas de SPY, conservando Custom Data. Se verificó exportación por recuento, extremos y validación estructural. No hay volumen de mercado utilizable en SPY; no se usa. El proxy no reproduce exactamente el ETF ni su contrato tokenizado. Huecos originales preservados; calendario de festivos, cierres tempranos y diferencias de ejecución con el contrato nativo siguen pendientes.

## Comparaciones predeclaradas

Ventana común 2020-10-15 a 2025-12-31, warmup240, fast_mode=False para evitar la diferencia de muestreo diario detectada entre modos.

1. MultiAssetSession4h: long STOP26, EMA20/80, ADX26, RSI52–76, stop2ATR, trailing4.2ATR con ajustes heredados. Presupuesto nocional global4.4x con participaciones inversas a ATR%; reservas de órdenes pendientes incluidas. SPY usa barras filtradas UTC lunes-viernes00–20, decisiones de entrada desde barras00–16; ventanas futuras efectivas04–20, sin órdenes nuevas a20. Es una intersección de barras, no la sesión completa.
2. MultiAssetRelative4h: mismo control, excluyendo menor momentum20barras/ATR entre3 activos. Los horizontes de calendario difieren entre mercados; es una heurística que debe justificar su incorporación con resultados.
3. MultiAssetRejectShort4h: short independiente, sin longs. Macro EMA80 decreciente, precio bajoEMA20 y rechazo de rebote hastaEMA20; cierre bajo mínimo previo, STOP futuro en mínimo actual. Invalidación swing3barras+.25ATR, distancia1–3ATR, objetivo íntegro2.5R, salida48h, trailing2ATR y breakeven tras1.5R. No hay parciales tempranos ni parámetros específicos por activo. MultiAssetReject4h contiene la combinación para evaluar solo si la pata corta merece continuar.

## Criterios

Comparar retornos y drawdown de equity muestreada diariamente, meses positivos totales y activos, trimestres, peor mes, concentración y estabilidad por subperíodos. 2024–2025 ya es desarrollo visto, no OOS independiente. No ejecutar Monte Carlo sobre variantes claramente rechazadas. Correlación de contribuciones realizadas por cierre mensual no equivale a correlación MTM por ruta; no declarar demostrada la descorrelación del portafolio con esa aproximación.

## Sesiones iniciadas

- Control: http://localhost:9200/#/backtest/2e943276-7815-4280-96c8-d634d2dab817
- Fuerza relativa: http://localhost:9200/#/backtest/4ddf1a13-71be-4c8d-94c0-a1addf6cb2cd
- Shorts: http://localhost:9200/#/backtest/2b5242d7-6084-435c-9d7a-608788defb19

Estado al guardar: ejecutándose; sin resultados finales todavía. No se inició live/paper ni se tocó producción.
