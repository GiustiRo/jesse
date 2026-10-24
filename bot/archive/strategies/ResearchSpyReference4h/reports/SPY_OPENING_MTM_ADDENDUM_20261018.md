# Apertura SPY — MTM UTC auditado por root
Complementa SPY_OPENING_AUCTION_RESULTS_20261018.md; no reemplaza resultados de fallo.

Root ejecutó auditorV4 inline en run_analysis a19d7e0afb404303aa33ca7cc1c19c53: succeeded. Seis snapshots auditados, con21anclasBTC/67PAXG/15SPY. Error relativo máximo de anclas <2e-15; reconciliación fees/wallet y terminal PASS. No se usa PnL por mes de cierre ni muestras00:01. Los8trades overnight de cada política están incluidos en MTM.

| Política | Meses positivos/activos | Positivos/todos | Trimestres positivos | DD diario MTM |
|---|---:|---:|---:|---:|
|[Referencia aislada](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2)|15/33|15/63|10/21|−5.218%|
|[ORB60](http://localhost:9200/#/backtest/a68dbfa8-3efe-410a-9c8b-861bf3609f38)|15/61|15/63|0/21|−63.748%|
|[Drive60](http://localhost:9200/#/backtest/98918ea4-78a2-4548-8f23-8c7459d07a30)|11/63|11/63|1/21|−87.281%|

Períodos completos: referencia9/19trimestres positivos; ORB15/59meses activos entre61meses completos y0/19trimestres; Drive11/61meses y1/19trimestres. Se conservan bordes/inactividad visibles. Estas métricas aisladas son diagnóstico, no meta que deba cumplir cada señal ni criterio para optimizar horarios.

Datos recibidos del auditor root; root persiste informe unificado. La decisión de archivar ambos sistemas intradía queda reforzada. No nuevo backtest ni variante por este addendum.