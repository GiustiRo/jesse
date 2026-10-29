# Revisión de comparabilidad y riesgo — r5
Revisor: risk_comparability. Lecturas MCP separadas, sin motores, jobs ni escrituras del revisor.

El perfil fijo 2%/6%/3xya está representado por K1001yN204B/CenR12. Las fuentes congeladas acreditan TRADE_RISK=.02,PORTFOLIO_RISK=.06,NOTIONAL_CAP=4.4,SLIPPAGE_RESERVE=.001. El formulario de cada sesión acredita 3x aislado. El comentario heredado que dice 5xno cambia ese override; no se modificó código.

Base de sizing:max(0,min(wallet,portfolio_value)); incluye riesgo mark→stop,costes yreservas de entradas pendientes. Cuotas ATR,nominal y margen pueden reducir el 2%objetivo. Reserva de sizing no es slippage ejecutado.

| Referencia | Fee por lado | Neto USDT | CAGR % | DD % | PF | Trades | Meses positivos/61 |
|---|---:|---:|---:|---:|---:|---:|---:|
| K1001 B | .00045 |35727.07|33.85|−13.34|2.058|242|46|
| K1001 B | .00095 |24064.34|26.50|−14.59|1.786|242|38|
| K1001 C | .00045 |37184.83|34.66|−13.82|2.056|249|44|
| K1001 C | .00095 |24652.00|26.92|−14.54|1.775|249|40|
| N204 B | .00045 |33646.45|32.66|−13.38|1.883|273|43|
| N204 B | .00095 |22034.26|25.02|−14.03|1.642|273|42|
| N204 C | .00045 |35025.68|33.46|−15.00|1.888|280|43|
| N204 C | .00095 |22494.18|25.36|−15.66|1.637|280|42|

10 kcompartidos,2020-10-15→2025-12-31 exclusiva,4h+M1,feenominal.00045/estrés.00095,sinfunding/slippageefectivo/liquidez. Las cifras son transcripciones deR12/anexos, no reestimaciones de estadísticas de trades.

K1001 retiene másretorno, pero no domina en todoriesgo/regularidad. N204Bestrés tiene menor DD ymásmesespositivos. R13 con 50 kes otra sensibilidad y no se mezcla o escala.
La tabla 2026 deK1001 ycomparación ampliada es evidencia ya observada; ninguna de las cinco ampliadas pasa yK1001 conjuntoB/Ctampoco. Retener fuentes definitivas corregidas.

Fuentes leídas completas:
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_K1001B_DATA_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_K1001C_DATA_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_N204B_DATA_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_N204C_DATA_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R12_SOURCE_QA_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/CAPITAL_R13_50K_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/K1001_OOS_2026_10K_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/OOS_2026_ARCHIVED_CANDIDATES_RESULTS_20261019.md

Conclusión: conservarK1001B/CyN204B/C como referencias de investigación comparables. No aprobar ni volver a explorar riesgo. Sin discrepancia material de las cifras seleccionadas al redondeo publicado. Root contrastó summaries en SESSION_RECEIPTS.json; no se reauditaron todos losfills.
