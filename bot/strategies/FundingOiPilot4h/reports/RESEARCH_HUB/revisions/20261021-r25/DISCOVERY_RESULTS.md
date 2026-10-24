# AA — Interacción entre retorno y volumen

Resultado: cerrada sin candidata. Dos cuentas BTC individuales, histórico UTC [2020-10-15,2026-01-01), capital10k, riesgo2%/6%/3x, taker.00045 por lado y funding histórico aplicado; slippage0 modelado. Desarrollo ampliamente observado, sin economía2026 ni OOS nuevo.

|Política|CAGR neto|PF|DD M1+fills|M+ activos|Q+|Mediana mensual|N|
|---|---:|---:|---:|---:|---:|---:|---:|
|[INTERACTION](http://localhost:9200/#/backtest/7ec2626e-9767-4139-90bc-4bd4d596e755)|−8.3836%|0.96635|66.8575%|28/62|8/20|−1.6598%|1660|
|[MAIN_EFFECTS](http://localhost:9200/#/backtest/8b003c2c-4ca3-4cca-9c76-497e2cfa4fb4)|−14.1298%|0.94040|71.1385%|28/62|6/20|−2.5333%|1635|

El tratamiento mejora al control dentro de esta trayectoria, pero ambas políticas incumplen todas las puertas económicas y de regularidad. N≥100 es sólo suficiencia operativa preliminar, no potencia o confirmación. Ninguna promoción, ni selección posterior de lados: el PnL long positivo de INTERACTION no autoriza convertirla en long-only.

La comparación usa360 orígenes maduros por ajuste y predicción directa24h: [1,r,v,r×v] frente[1,r,v]. Producto bruto antes de centrar, scalers TRAIN comunes, misma admisión numérica y controles de rango. El diagnóstico ex ante coincide exactamente entre políticas:11423 ajustes válidos, gamma negativa5707/positiva5716/cero0, sin errores de agregación. No se interpreta la secuencia solapada como observaciones independientes ni como identificación causal o prueba de demanda.

Conciliación de todas las filas del snapshot: bruto−fees+funding=PnL=capital final−10000, discrepancias inferiores1e−6USDT. Ambos FINAL incluyen la liquidación terminal y su comisión; total_open_trades1 de métricas no acredita exposición pendiente al cierre.63intervalos mensuales continuos,62 completos/20Q,2741760marcasM1. Fronteras por fase postfunding/predecisión, DD M1+fills no extremos intraminuto. Funding usa proxies explícitos2591/2564 pagos.

Se conservan protocolo, fuentes iniciales y finales, recibos, fallo de harness y corrección, manifest previo a economía, auditoría y resultados desfavorables. Dos backtests terminados, cero reemplazos/económicos fallidos. Check técnico final129PASS; primera ejecución de harness falló por predicado de imports demasiado amplio sin fuente productiva cambiada entre jobs. NumPy1.26.4 enAA se etiqueta continuidad inferida del baselineY, no nueva mediciónAA.

Cierre: no variar volumen, ventanas, horizonte, interacción, normalización, estimador, rank/regularización, signos, hurdle, riesgo o gestión para rescatar este resultado. No retirar componentes o financiar costos omitidos. Siguiente pregunta debe ser material y contrastarse con antecedentes antes de código.
