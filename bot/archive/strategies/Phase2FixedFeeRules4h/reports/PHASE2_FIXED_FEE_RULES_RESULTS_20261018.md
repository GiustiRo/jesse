# Costes con umbrales de decisión fijos: resultados
SIGNAL_FEE=.00045 fija filtroshort de distanciamínima y precio de breakevenlong. self.fee_rate usa comisión real en tamaños,risk/reservas y contabilidad. No cambiarreferencia/configglobal.2026reservado.

## Equivalencia
[Controlbase](http://localhost:9200/#/backtest/f1208d5e-52a6-4aec-a3cb-4c7ff78bafc2) reproduce [referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb):220trades,mismos símbolos/direcciones/timestamps,cantidades/precios/fees/PnL dentro rtol1e-12/atol1e-9,saldo37461.46337484. No interpretar sin esta equivalencia; pasó.

|Coste adicional RT|Fee/lado|CAGR%|DDJesse%|Shorts netosUSDT|Mesesactivospositivos%|Trimestrespositivos%|
|---|---:|---:|---:|---:|---:|---:|
|Base|.00045|28.8294|-14.8905|5287.02|54.0984|71.4286|
|10bps|.00095|23.7457|-16.5192|3177.87|50.8197|66.6667|
|25bps|.0017|16.5438|-18.9835|723.65|45.9016|52.3810|

[+10bps](http://localhost:9200/#/backtest/66e5d910-56b8-47a2-99ab-bdfd74915a20),[+25bps](http://localhost:9200/#/backtest/d11139b0-194c-4457-9bfb-613d60f622f8).
220trades97long123short en los3casos;longnet22174.44/17190.74/11491.76,saldo37461.46/30368.60/22215.41. Coincidir counts no prueba por sísolo identidaddeeventos entre costes;equivalencia de tradesvalidada solo enbase. Capital/tamaños varían con comisión.
Rerunsanteriores con reglasadaptativas a fee dieronCAGR21.6433%/14.5454%,short3290.76/692.51 a+10/+25;seconservan como escenarioscompletosdistintos,nocomo coste puro sobre mismasreglas. La diferencia entre ambos cambia dos umbrales (short yBE), no atribuirla a uno solosincontroladicional.
[Adaptativo10](http://localhost:9200/#/backtest/f5d887e7-c807-4939-8b3a-00ac4804277f),[adaptativo25](http://localhost:9200/#/backtest/79ee60b0-286e-4a19-aa7e-10720a3ed430).

AnálisisMCPf36b013822404e04b7b273def00421e2 succeeded,BASE_EQUIVALENCE_PASS220,autocontrolesMTMv3pasaron,saldosreconciliados.61mesesactivos/63total,bordesparcialesincluidos.DDMTMdiariofixed10-16.3959%,fixed25-18.9752%,diferenteJesse por muestreo.
Noesmodelo de spread/slippage/impacto/colafills/funding. FeealtanogarantizaejecuciónLIMITconservadora. Shortsconpococolchón;fase2 noaprobada ni objetivosrebajados.
