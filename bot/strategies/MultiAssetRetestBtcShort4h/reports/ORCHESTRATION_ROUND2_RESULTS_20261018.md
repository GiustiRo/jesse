# Orquestación: segunda ronda y auditoría de salidas parciales
Fecha: 2026-10-18. Desarrollo 2020-10-15 a 2025-12-31 (fin exclusivo). 2026 reservado. Ninguna variante promovida.

| Diseño | CAGR | DD motor | Meses activos positivos | Meses calendario positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| Referencia |28.83%|−14.89%|33/61 (54.10%)|33/63|15/21|
| Longs salida completa 3R |12.47%|−22.44%|35/61 (57.38%)|35/63|13/21|
| Longs salida completa 5R |20.85%|−22.43%|39/61 (63.93%)|39/63|16/21|
| Longs 50% a2R + runner original |23.48%|−9.96%|35/61 (57.38%)|35/63|14/21|
| Guarda mensual +2% / +1% |7.67%|−12.58%|31/60 (51.67%)|31/63|12/21|
| Guarda mensual +4% / +2% |2.89%|−14.11%|32/61 (52.46%)|32/63|13/21|
| Cortos BTC recuperación fallida, régimen diario |−1.30%|−16.30%|1/17 (5.88%)|1/63|1/21|

Los meses se calculan con equity MTM al cierre UTC, incluyendo beneficios no realizados y comisiones en cada fill, no asignando el beneficio completo al mes de cierre. Se incluyen periodos parciales en los bordes. El DD motor y el DD de cierres diarios difieren ligeramente por instante de muestreo; no se selecciona el menor para aceptación. Las métricas de regularidad son descriptivas del desarrollo ya observado.

## Decisiones
- Las dos salidas completas fijas no cumplen los objetivos y empeoran drawdown; no barrer R intermedios después de observarlas.
- La salida parcial merece conservarse como comparación de menor drawdown, no como solución de regularidad.
- Las guardas mensuales ejecutaron cierres reales, pero destruyen rentabilidad y tampoco mejoran regularidad. Familia descartada.
- El corto con régimen diario pierde antes de comisiones. No elevar riesgo para ocultarlo.
- Nuevas hipótesis deben aportar mecanismo económico diferente, no una rejilla de ajustes a los descartes: reversión corta dentro de tendencia, expansión bajista y valor relativo BTC/ETH. Revisar protocolos antes de lanzar.

## Auditoría V4
Archivo: research_scripts/monthly_auditor_v4_orders.py, escrito mediante MCP por autorización original del auditor mensual.
Soporta una entrada y múltiples salidas totalmente ejecutadas; devenga comisiones por fill, realiza sólo la cantidad que sale, y valora sólo el remanente. Reconcilia cada trade, comisiones y wallet terminal, rechaza sobrecierres, entradas múltiples y snapshots PARTIALLY_FILLED. No acredita soporte de funding, fees variables ni posiciones terminales abiertas.
Paridad V3/V4 comprobada para referencia y cuatro sesiones sin parciales: retornos mensuales y contribuciones a1e-9, equity a1e-6 y conteos iguales. La primera comprobación falló por orden distinto de columnas; se corrigió ordenando etiquetas antes de comparar, sin alterar economía.
Autopruebas: long/short, parcial antes/en/después de medianoche, qty enviada distinta de filled_qty real, sobrecierre y cartera vacía.
Sesión parcial real: todos los fills, fees y wallet reconciliaron. Los benchmarks sólo aportan precios del mismo histórico; la vieja simulación con fallo de margen no se reutiliza como resultado económico.
Anclas MARKET deben estar EXECUTED y aparecer en al menos dos timestamps distintos. Los inputs deben compartir exchange/symbol e histórico inmutable por contrato: igualdad de símbolo por sí sola no demuestra igualdad de fuente.

## Sesiones
- [Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb)
- [3R](http://localhost:9200/#/backtest/c29560ed-3da9-4bb3-9162-d99c0c3806ac)
- [5R](http://localhost:9200/#/backtest/efc9d485-56ea-49fb-95ed-0f93aa690e71)
- [Parcial](http://localhost:9200/#/backtest/0c6cfad7-c5da-465d-a45e-7009d284a1ec)
- [Guarda2/1](http://localhost:9200/#/backtest/ace2ad08-48bf-4326-9602-3a8e71b2fb18)
- [Guarda4/2](http://localhost:9200/#/backtest/5437d456-3483-42a8-b354-c287451875f4)
- [Corto diario](http://localhost:9200/#/backtest/79338950-d982-49ca-b9dd-dfc9926adba5)

No se ha alcanzado el objetivo. No se modificó la referencia ni se evaluó2026. La prueba técnica de pares es demasiado corta para una conclusión económica; esperar importación ETH y backtest completo.
