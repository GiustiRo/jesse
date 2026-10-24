# Primera cartera BTC+PAXG — resultado insuficiente

Dashboard: http://localhost:9200/#/backtest/af13abd2-f8a8-472c-883a-11622bbf9120

Control BTC en fechas idénticas: http://localhost:9200/#/backtest/b5b8924a-08e8-491e-b4a6-58ab4a1b904e

Variante sin cuota de nocional por volatilidad: http://localhost:9200/#/backtest/f6bb59ef-809f-4d60-86a8-bffcb113b41f

2020-10-15 a 2025-12-31, cuenta compartida 10000 USDT, 5x isolated, fee 0.00045, fast_mode=False, warmup 240, 3% máximo planeado por trade / 8% agregado, nocional 4.4x global. PAXG: 2887556 velas copiadas desde Binance Spot para simular futuros; esa procedencia NO es historia nativa del contrato. Parte de 2026 puede estar almacenada por la importación, pero ningún precio/retorno de 2026 se usó en calibración. Para lockbox final PAXG debe contrastarse con datos nativos del perpetuo, no confundir el copy con un cambio de procedencia.

| Variante | CAGR publicado | DD diario | Trades | Meses positivos MTM |
|---|---:|---:|---:|---:|
| BTC control 3% | 30.7362% | -12.1537% | 39 | 28.57% |
| BTC+PAXG STOP | 40.8495% | -38.4939% | 129 | 49.21% |
| BTC+PAXG STOP + reparto vol | 40.4962% | -38.1838% | 129 | 49.21% |

La cartera gana frecuencia pero empeora demasiado el riesgo. Repartir nocional por volatilidad apenas mejora DD. Ambas tienen 64 trades BTC y 65 PAXG, 61 de 63 meses con posiciones y 50.82% de meses activos positivos; 61.90% trimestres positivos. Peor mes -12.35%, peor trimestre -18.01%, 9 meses consecutivos no positivos. En 2022: -25.22% sin cuota y -25.09% con cuota. No cumple metas de 65% meses y DD <=25%.

Correlación de contribuciones realizadas por mes -0.013 / -0.002, respectivamente: NO equivale a correlación MTM por ruta ni garantiza diversificación en crisis. Dos mejores trades aportan 26.96% / 25.88% del beneficio neto (eliminación nominal, no redimensionamiento contrafactual).

Siguiente ablation predeclarada: reflejar las reglas a shorts sin añadir parámetros (MultiAssetTrendBoth4h). No se aprobó cartera final, no se abrió lockbox 2026 y no se inició live/paper.