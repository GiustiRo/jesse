# Candidata parcial: LIMIT en retesteo de tres activos

Sesión: http://localhost:9200/#/backtest/578cc47c-b7bc-4ae9-8668-05cfc23433e1

Ventana2020-10-15 a2025-12-31;10000USDT compartidos,5x aislado,fee.00045,warmup240,modo normal. 2026 no utilizado. Estrategia long-only, 3% máximo/trade,8% agregado planificado, techo4.4x con reparto inversoATR. Riesgo nominal no garantiza el límite ante gaps/slippage.

Resultados: CAGR23.6908%, equityfinal30298.42, DDdiario-14.0763%, Sharpe1.18268, Calmar1.68302,97trades (31BTC/35PAXG/31SPY). PnLneto porruta13238.85/3776.81/3282.76USDT, los3positivos. Top2trades36.96% delPnLneto; diagnóstico de eliminación nominal fijo, no CAGR contrafactual.

AuditorMTM:63meses,55activos,42.86% positivos totales,49.09% activos,66.67% trimestres positivos. Peormes2023-03:-4.39%, peortrimestre2022Q3:-7.63%, racha9meses no positivos. Años: parcial2020+16.41%,2021+54.67%,2022-10.80%,2023+29.78%,2024+19.42%,2025+21.73%.

Comparado con STOP26 tresactivos (CAGR10.42%,DD-35.49%), el retesteo mejora retorno/riesgo y reduce concentración. Comparado con BTCcontrol3% (CAGR30.74%,DD-12.15%,39trades), aumenta frecuencia y proporción de trimestres positivos pero reduce retorno y no mejora mesespositivos activos (control51.43%). NO cumple objetivo65–70% meses activos/80% trimestres y no contiene shorts. No declarar fase2 completada ni abrir2026.

La mezcla50/50igualgross e inversoATR con STOP no solucionó elproblema: CAGR10.54%,DD-38.87%,46.03%mesesactivos positivos. No incorporarla por rendimiento agregado.

La pata shortcrisis independiente pierde4.48%CAGR, DD-29.92%, pero2022+21.03%. Se abrió contraste combinado con largosLIMIT solo para medir coste/beneficio de cobertura: http://localhost:9200/#/backtest/432afb61-ead3-460f-b2ef-471e82651637 . Aún pendiente al guardar.

Análisis completo run_analysis joba5ed9d2244cc4d3eb1440712c8009a01. DDmuestreada diariamente, no máximo intraminuto. No hay validación de correlaciónMTM porruta ni de ejecución nativa SPY/PAXG. La recuperación del PNG con get_analysis_artifact devolvió artifact_changed dosveces; no se recurrió alectura alternativa de imagen. Los datosnuméricos delanálisis están completos.
