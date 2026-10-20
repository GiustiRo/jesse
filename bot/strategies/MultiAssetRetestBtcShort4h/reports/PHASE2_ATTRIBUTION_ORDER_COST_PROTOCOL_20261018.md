# Protocolo: atribución, prioridad de rutas y costes con filtro fijo
Referencia congelada [tres activos long +BTCshort](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Long-only3activos existente [control](http://localhost:9200/#/backtest/11c1a0a6-afe8-4718-80b9-a35e95adf40d). Reusar ambos; no usar BTCMomentumBaseline3 para atribución causal por reglas diferentes.

Todos los controles conservan3rutas BTC/PAXG/SPY,4h,asignacióninverseATR de los3símbolos aun inactivos,10000capital,5xisolated,riesgo3%/8%,fee.00045,2020-10-15 a2025-12-31 exclusivo,modo normal,warmup240. 2026reservado. No retirar rutas ni redistribuir pesos ociosos.

1. BTC long-only con mismas reglaslong de referencia, sin entradasPAXG/SPY ni shorts.
2. BTC long+short con mismas reglas, sin entradasPAXG/SPY.
3. Comparar controles1/2 con3activoslong y3activoslong+BTCshort ya existentes. Medir CAGR/DD,MTMmeses/trimestres,transiciones de signo mensual,exposición y concentración. No declarar diversificación superior por PnL de componentes positivos.
4. Prioridad: referenciaBTC/PAXG/SPY contraSPY/PAXG/BTC yPAXG/BTC/SPY. No escoger orden ganador; detectar diferencias en trades,tamaños y regularidad. El control mide sensibilidad al orden de ejecución completo, no demuestra causa de asignación por sí solo.
5. Costes: clonar referencia con filtroshort de distancia mínima congelado a6*0.00045*entry; aplicar comisiones0.00095/0.0017por lado SOLOenborradores. Comparar con rerunspreviosde filtroadaptativo. Esta separación congela el filtro de elegibilidad concreto, no tamaños/capital ni breakevenlong dependiente de fee. Etiquetar como escenario con filtro fijo, no ejecución totalmente idéntica ni modelo de spread/slippage.
No cambiarcomisión global ni referencia. Comparar tradeslong y short por separado y MTMcalendario conauditorv3. Ningún control es OOS ni demuestra desempeño2026. No optimizartrasverresultados. Documentar resultados negativos.

Prioridad de decisión: si resultado depende mucho del orden, revisar proceso de cartera antes de añadir filtros; si diversificación/shorts no mejoran regularidad sin riesgo excesivo, reconsiderar estructura;siaportan,solo entoncesnuevahipótesisjustificada. Meta65–70%mesesactivos/80%trimestres sigue vigente.
