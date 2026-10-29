# Fase2: estrés de costes mediante nuevas simulaciones
Reglas congeladas, mismos datos de desarrollo2020-10-15 a2025-12-31 exclusivo. Capital10000 compartido,5xaislado,3%/8%riesgo planificado, modo normal. 2026 reservado.
Se eleva la comisión solo en el borrador de cada prueba, sin alterar configuración global: base0.00045 por lado; estrés0.00095 y0.0017 por lado. Diferencias equivalen a10bps/25bps adicionales por ida y vuelta, respectivamente (0.10%/0.25%).

| Caso | CAGR % | DD Jesse % | Sharpe | Saldo final USDT | Shorts netos USDT | Meses activos positivos % | Trimestres positivos % |
|---|---:|---:|---:|---:|---:|---:|---:|
|Base|28.8294|-14.8905|1.3164|37461.46|5287.02|54.0984|71.4286|
|+10bps RT|21.6433|-16.5229|1.0443|27773.11|3290.76|49.1803|66.6667|
|+25bps RT|14.5454|-18.9906|0.7531|20299.82|692.51|42.6230|52.3810|

[Base](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb), [+10bps](http://localhost:9200/#/backtest/f5d887e7-c807-4939-8b3a-00ac4804277f), [+25bps](http://localhost:9200/#/backtest/79ee60b0-286e-4a19-aa7e-10720a3ed430).

Las nuevas ejecuciones sí recalculan tamaños, capital, reservas y reglas dependientes de costes. Por eso cambian incluso los conteos:220trades97L123S base;222trades98L124S a+10;220trades98L122S a+25. No es el antiguo descuento manteniendo fills/cantidades. Longs netos22174.44/14482.34/9607.32.
Los shorts sobreviven estos dos escenarios agregados, pero con escaso colchón en el más severo. Esto NO revoca el fallo de sensibilidad RSI24/TP1.75ATR, con shorts negativos.

## Límites
Aumentar comisión es un proxy de coste por volumen negociado, NO un modelo de spread, slippage de ejecución, impacto, cola, fills perdidos, financiación o PAXG/SPY nativos. El código reserva10bps para sizing, pero esa reserva no aplica fricción al precio simulado. No presentar estas pruebas como ejecución realista certificada.

## Auditoría
monthly_auditor_v3_mtm.py inline en run_analysis; job c32d0c9de1c44ee286bbc8659a029591 terminó succeeded. Autocontroles pasaron; saldos terminales reconciliados para todos los casos. Meses activos61/63 incluyendo bordes parciales; valoración diaria UTC de posiciones abiertas. DD al cierre diario base-14.8784%,+10-16.3996%,+25-18.9718%; no confundir con DD Jesse de tabla.
Artefactos temporales: calendar_audit.json, *_calendar_month_returns.csv, *_route_mtm_contributions.csv, *_daily_close_equity.csv. Los jobs de análisis caducan; este informe conserva las conclusiones.

## Decisión
Conservar el centro como referencia de investigación, sin promocionarlo ni abrir2026. No cumple la regularidad buscada y el retorno depende materialmente de costes. La siguiente hipótesis debe tener una motivación estructural y controles predeclarados; no seleccionar la mejor esquina de parámetros ni rebajar objetivos a posteriori.
