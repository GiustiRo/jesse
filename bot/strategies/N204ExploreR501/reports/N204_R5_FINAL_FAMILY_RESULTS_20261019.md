# N204 R5 — final family results

All5 frozen hypotheses completed in B/C:10 nominal backtests, with two running simultaneously per root ticket. No repaired/full repeat runs, no subsequent tuning, no2026 inspection. Sources remained unchanged throughout; final9-source byte equality confirmed against N204, five new classes and PAXG/2SPY companions.

|Recipe|Net B|Net C|N B/C|Supplement fills B/C|Conclusion|
|---|---:|---:|---|---|---|
|N501|[9498.021641](http://localhost:9200/#/backtest/16ce69b3-da09-4bc4-9eb4-be31b7e5d39d)|[9654.293855](http://localhost:9200/#/backtest/febab2e7-f15f-4260-b9c0-8d92c669ac10)|239/246|37/37|Below N204 nominal in both|
|N502|[10708.848117](http://localhost:9200/#/backtest/8e4fd64f-49c6-4049-b6da-abafede9cb8e)|[10916.219870](http://localhost:9200/#/backtest/d492f34b-8a1e-4099-8ec3-eae1b3b5d284)|238/245|40/40|Below N204 nominal in both|
|N503|[13328.711713](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752)|[13536.902513](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65)|264/271|67/67|Nominal gain in both; fails frozen monthly cost gate in C|
|N504|[8759.054435](http://localhost:9200/#/backtest/e3201a9a-3ac0-47f5-94f5-6f16feeee8ab)|[8925.804090](http://localhost:9200/#/backtest/72d9e745-e4e1-4e09-99eb-e550f2560206)|214/221|8/8|Below N204 nominal in both|
|N505|[9785.311035](http://localhost:9200/#/backtest/6a2cc667-11cf-4467-b1a4-0c8e84f2b792)|[9988.394945](http://localhost:9200/#/backtest/8e693681-095b-4db9-affb-053f19085948)|221/228|21/21|Below N204 nominal in both|

N503 increases net by272.096798/297.460133USDT and remains above reference at static+10bpsRT. It does not qualify: under+5bpsRT C has40/63=63.49% positive included active months, below65%. No winner is selected by this family. N504 has8 supplementary trades per portfolio, a limited sample; loss here does not universally invalidate12h engulfing.

Portfolio PNL includes occupancy/capital effects on original BTC and other routes. N503's supplementary PNL is lower than N204's in root attribution; its overall gain must not be described as stronger standalone supplement alpha. B/C are dependent controls sharing the same BTC events, not independent replicated samples. Original source code/priority preservation does not imply identical execution paths.

Source QA: first harness job failed an incorrectly calculated1/3 efficiency fixture; corrected synthetic arithmetic and ATR stub only, final250PASS. No source rule or threshold changed. Reports: N204_R5_SOURCE_QA_20261019.md, N204_R5_QA_SOURCE_20261019.md, N204_R5_DRAFT_REGISTRY_20261019.md, N204_R5_EXECUTED_QC_20261019.md, and independent T403/source/matrix reviews, all inside this strategy's reports directory in Jesse.

## N501B

Dashboard: http://localhost:9200/#/backtest/16ce69b3-da09-4bc4-9eb4-be31b7e5d39d

Net 9498.021640569941USDT; Sharpe 1.3198259410516398; N 239; DDmotor -8.213281557396346%. Event/fill/close 46/37/37. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N501C

Dashboard: http://localhost:9200/#/backtest/febab2e7-f15f-4260-b9c0-8d92c669ac10

Net 9654.293855083359USDT; Sharpe 1.310992734137451; N 246; DDmotor -9.055353586223003%. Event/fill/close 46/37/37. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N502B

Dashboard: http://localhost:9200/#/backtest/8e4fd64f-49c6-4049-b6da-abafede9cb8e

Net 10708.848117185807USDT; Sharpe 1.4299215925440345; N 238; DDmotor -8.869363435715428%. Event/fill/close 46/40/40. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N502C

Dashboard: http://localhost:9200/#/backtest/d492f34b-8a1e-4099-8ec3-eae1b3b5d284

Net 10916.219869572262USDT; Sharpe 1.420107458720613; N 245; DDmotor -9.049083388458223%. Event/fill/close 46/40/40. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N503B

Dashboard: http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752

Net 13328.711712815926USDT; Sharpe 1.6088359688476044; N 264; DDmotor -8.78368484676294%. Event/fill/close 82/67/67. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N503C

Dashboard: http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65

Net 13536.902513059398USDT; Sharpe 1.5964007117474932; N 271; DDmotor -9.054184091363382%. Event/fill/close 82/67/67. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N504B

Dashboard: http://localhost:9200/#/backtest/e3201a9a-3ac0-47f5-94f5-6f16feeee8ab

Net 8759.05443468399USDT; Sharpe 1.2701544805184466; N 214; DDmotor -7.610430098731003%. Event/fill/close 8/8/8. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N504C

Dashboard: http://localhost:9200/#/backtest/72d9e745-e4e1-4e09-99eb-e550f2560206

Net 8925.804089688183USDT; Sharpe 1.2629047802947684; N 221; DDmotor -8.168012803517167%. Event/fill/close 8/8/8. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N505B

Dashboard: http://localhost:9200/#/backtest/6a2cc667-11cf-4467-b1a4-0c8e84f2b792

Net 9785.311034515398USDT; Sharpe 1.3561325757159672; N 221; DDmotor -8.275696786118136%. Event/fill/close 22/21/21. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

## N505C

Dashboard: http://localhost:9200/#/backtest/8e693681-095b-4db9-affb-053f19085948

Net 9988.394944602309USDT; Sharpe 1.3502603526976942; N 228; DDmotor -8.273773880405566%. Event/fill/close 22/21/21. Exact form/source snapshots/HP/log manifests verified. Full fills/fees/wallet/MTM audit is root's frozen auditor.

No OOS, live deployment, new data, funding or actual slippage conclusion. N204 remains frozen;2026 closed.
