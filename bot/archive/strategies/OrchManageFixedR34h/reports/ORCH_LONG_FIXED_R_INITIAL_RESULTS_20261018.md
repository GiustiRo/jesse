# Salida swing long3R/5R — resultado inicial
Dashboard3R: http://localhost:9200/#/backtest/c29560ed-3da9-4bb3-9162-d99c0c3806ac
Dashboard5R: http://localhost:9200/#/backtest/efc9d485-56ea-49fb-95ed-0f93aa690e71
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Hipótesis predeclarada
Ver ORCH_LONG_FIXED_R_PROTOCOL_20261018.md: salida completa3R/5R con stop fijo inicial2ATR reemplaza trailing/BElong; todas las señales,asignación inversoATRoriginal yshortsBTC72h inalteradas. Cuenta10k/5xisolated,fees0.00045todasórdenes,riesgo3%/8%,global4.4x,warmup240,normal replay,2020-10-15→2025-12-31exclusivo,2026reservado.
Objetivo: menorgiveback yliberación de rutas; realizarbeneficio NO cambia por sísolo unmesMTM. No pretender ganar51%comoobjetivo.
## Todos los resultados, sin seleccionar pico
|Variante|CAGR|DDmotor|Sharpe|NetoUSDT|TradesL/S|FeeUSDT|WRlong|
|---|---:|---:|---:|---:|---:|---:|---:|
|Referencia|28.829387%|−14.890506%|1.316428|27461.463375|97/123|4595.616325|44.33%|
|3R|12.473588%|−22.444295%|0.715971|8457.045110|106/102|2587.697835|33.02%|
|5R|20.846105%|−22.433084%|1.000791|16837.143906|93/100|2925.700148|26.88%|
Ambas terminalflat. Permanencia global3R370900seg(4.29d),5R498556seg(5.77d),base341554seg(3.95d).
## Verificación y límites
Fuentes MCP releídas idénticas a preparación. _short_plan y_volatility_share son byteidénticos a referencia. Diferencias de cantidadde shortsrealizados no implican nuevafórmula short: ocupación/margen/compounding alteran admisión, por eso se compara cartera completa.
Stop yTPdesdeentryfillreal. Salidas completas sinpiramidar para auditorV3. Lasfamiliastrailing/behyperparametersheredadas no intervienen en nuevoslongs. No se cambióframework/config/live.
## Interpretación y datos pendientes
Ambosvecinos empeoran claramente drawdown y retorno contra referencia; familia NO se promueve. Un targetmáslejano conservamásretorno,pero no demuestra meseta niregularidad. El5Rduplica CAGRde3R sinreducirDD; interpretar sensibilidad, no seleccionar sólo5R.
MTMcalendarmensual/trimestral,contribuciones ytails quedan en análisis unificado del orquestador. Hastaentonces no declarar objetivo cumplido/fallomatemático de meses. No barrerR4/R6uotrosparámetros para rescatar familia. 2026sellado.
