# Fase 2: sensibilidad de shorts y estabilidad temporal
Estado: candidata de investigación, NO aprobada. 2026 permanece reservado. No live/paper.

## Protocolo y resultado
Longs LIMIT retest congelados en BTC/PAXG/SPY, shorts de continuación de pullback exclusivamente BTC. Riesgo 3% por trade y 8% agregado planificado; 5x aislado, capital 10000, comisión por lado 0.00045. 2020-10-15 a 2025-12-31 exclusivo, modo normal. PAXG spot y SPX CFD /10 son proxies, no instrumentos futuros nativos.

La selección de BTC para shorts se hizo después de observar componentes de la misma muestra: es exploratoria. La sensibilidad no convierte esa selección en OOS.

| Caso | CAGR % | DD Jesse % | PnL neto shorts USDT | Meses activos positivos % | Trimestres positivos % |
|---|---:|---:|---:|---:|---:|
| Centro RSI3<=20, objetivo1.5ATR |28.8294|-14.8905|5287.02|54.0984|71.4286|
| RSI16, objetivo1.25ATR |28.1725|-13.8765|4193.99|57.3770|76.1905|
| RSI16, objetivo1.75ATR |24.4692|-15.1655|1358.21|57.3770|71.4286|
| RSI24, objetivo1.25ATR |24.6235|-16.4866|622.05|55.7377|71.4286|
| RSI24, objetivo1.75ATR |22.0312|-16.6652|-619.75|57.3770|71.4286|

**Falla el criterio predeclarado de que los shorts sean netamente positivos en las cuatro esquinas.** No seleccionar la mejor esquina para ocultar el resultado. El portafolio total positivo no demuestra robustez de la pata corta.

Sesiones:
- [Centro](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb)
- [R16 T1.25](http://localhost:9200/#/backtest/ba353d00-cd9b-4529-a87c-15838d25cde3)
- [R16 T1.75](http://localhost:9200/#/backtest/b882afe4-d165-4c76-ab69-8d2ca7778014)
- [R24 T1.25](http://localhost:9200/#/backtest/da536680-f0bf-428c-8184-0eabfaa6da1a)
- [R24 T1.75](http://localhost:9200/#/backtest/3e6b9a8d-b9ca-43fb-b5e6-f847e1ca0928)

Asignación de techos nocionales iguales empeora DD a22.3903% para CAGR28.8843%, shorts5210.02: [control igual](http://localhost:9200/#/backtest/103d2155-e7fc-477f-9d5d-10f5fccbe22f). No mejora justificable.

## Estabilidad temporal con parámetros congelados
Cada tramo reinicia capital10000. No son OOS limpios: todo2020–25 es desarrollo ya observado.

| Tramo | CAGR % | DD Jesse % | Meses activos positivos % | Trimestres positivos % |
|---|---:|---:|---:|---:|
|2020-10-15 a2024-01-01|30.7613|-13.0031|51.3514|69.2308|
|2024-01-01 a2025-12-31|25.8129|-14.5784|58.3333|75.0000|

[Tramo temprano](http://localhost:9200/#/backtest/2637b6e3-b8b4-4fec-903c-5046f8f48dfc), [tramo tardío](http://localhost:9200/#/backtest/aaeae284-e164-4fc8-9b88-0d955c4c2cf6).
Rentabilidad repartida temporalmente, consistencia mensual aún insuficiente. Correlaciones de contribuciones MTM no estables: BTC/PAXG +0.2697 temprano, BTC/SPY -0.3504 tarde. La correlación absoluta máxima0.114 del período completo no es garantía por régimen.

## Auditoría
Resultados mensuales/trimestrales de monthly_auditor_v3_mtm.py: cierres UTC verdaderos, MTM incluyendo posiciones abiertas, comisiones y reconciliación final. Incluye períodos parciales de borde; meses activos61/63 en centro. Las cifras antiguas del auditorv2 basadas en la última muestra diaria00:01 dentro del mes quedan sustituidas para toda conclusión de calendario.

Análisis MCP terminales succeeded:
- sensibilidad1f6524312c374bf1a5620d9ff1bb6def
- temporal f9e0463491294c0088898c9d330023f0
- auditor y autocontroles fb321e7f2f9543f5a98d7b792f3cbdd9

## Decisión
Conservar centro como referencia provisional, sin optimizar más esta cuadrícula. No declarar cumplidos65–70% meses activos/80% trimestres. Pendientes: estrés de costes con nuevas simulaciones, validación conjunta de portafolio/calendario, paridad nativa antes de promoción. No abrir2026 ni operar fondos.
