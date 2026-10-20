# Fase2 — primera familia de tres activos rechazada

Ventana común2020-10-15 a2025-12-31, 10000 USDT, fee.00045,5x aislado, fast_mode=False, riesgo máximo3% por trade/8% agregado planificado. 2026 reservado.

| Implementación | CAGR Jesse | DD diario | Trades | Meses positivos activos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| BTC control3% |30.736%|-12.154%|39|51.43%|52.38%|
| Tres activos STOP |10.418%|-35.486%|169|49.21%|52.38%|
| Excluir menor fuerza relativa |9.728%|-35.802%|167|46.03%|47.62%|
| Shorts rechazo rebote | -17.187%|-64.280%|307|37.70%|33.33%|

La cartera STOP realiza +9538.35USDT en BTC, -2965.11 enPAXG y+191.68 enSPY; el top2 de trades explica86.52% del beneficio neto. No cumple los criterios de consistencia, concentración o drawdown. No se incorpora filtro de fuerza relativa porque empeora el control. Shorts rechazo pierden en los3activos (-1717.75BTC/-3549.71PAXG/-991.59SPY); no se evalúa su combinación como candidata ni se ejecuta MC sobre ella.

Análisis completo guardado por run_analysis, job4cab29cca7a84ff6a7aec6ac05251ce7; artefactos temporales summary.json, CSVmensuales, three_asset_comparison.png. Los resultados se extrajeron de snapshots completos, no de páginas parciales. DD es equity diaria, no máximo intraminuto; contribuciones por cierre no son retornos MTM porruta.

Siguientes contrastes predeclarados: mezcla50/50 de presupuesto igualitario e inversoATR (solo asignación cambia); LIMITretst (solo entrada cambia); shortsdecontinuación decrisis en BTC/SPY (pataindependiente). Son investigaciones de desarrollo, noOOS.

URLs:
- http://localhost:9200/#/backtest/b5b8924a-08e8-491e-b4a6-58ab4a1b904e
- http://localhost:9200/#/backtest/2e943276-7815-4280-96c8-d634d2dab817
- http://localhost:9200/#/backtest/4ddf1a13-71be-4c8d-94c0-a1addf6cb2cd
- http://localhost:9200/#/backtest/2b5242d7-6084-435c-9d7a-608788defb19
