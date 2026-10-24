# R5 — independent review of20-row matrix and frozen selection

PASS. Ten recipes,20 nominal B/C sessions, all finished with error=null. No eligible recipe and no selected candidate. Optional verification is therefore not triggered. No new runs or analyses were executed for this review. 2026 remained closed.

Read: frozen N204_T403_R5_FROZEN_PROTOCOL_20261019.md and full N204_T403_R5_RESULTS_MATRIX_20261019.md via MCP, plus20 session summaries (10 this agent had already checked and10 freshly read) and N204 B/C reference summaries. Summaries agree with matrix nominal net and motor DD within1e-7USDT/tolerance. All20 +10 overlays independently reconcile to net−reportedfee×(0.00050/0.00045), since the common nominal fee is0.00045 per side. This is a cross-check of an additional static10bpsRT charge, not a new engine run or fill-friction estimate.

Recomputed20 rows: nominal Δ>1e-7; minimum of Mfull−.65, Mall−.65, Qfull−.80, Qall−.80; +10Δ>=−1e-7; DD>=−25. Compared each Boolean and each exact margin with JSON matrix. Recomputed10 recipe-level both-portfolio eligibility, minimum margin, minimumΔ+10 and worstDD. All agree, eligible=[], selected=null. This independently applies the frozen gates to reported MTM counts; it does not independently reconstruct the underlying MTM monthly series, which root's audit did.

Only N503 and C504 improve nominal net in both portfolios and pass the+10 non-inferiority comparison. N503 C has40/63=63.49206349% included active months under+5, below65%; its complete-month40/61 passes, so both bins matter. C504 B has15/19=78.94736842% complete positive quarters and16/21=76.19047619% included quarters, below80%. Neither can qualify by selecting its better portfolio or dropping partial calendar bins.

C502 has zero incremental nominal/+10 net relative to N204 and fails strict improvement. C505 matches its T403 seed economically according to root path identity checks, and remains below N204. Reported path checks preserve these identities instead of presenting clones as advances.

## Row checks

|Session|Margin MQ|Nominal/MQ/+10/DD|Eligible|
|---|---:|---|---|
|[N501B](http://localhost:9200/#/backtest/16ce69b3-da09-4bc4-9eb4-be31b7e5d39d)|-0.08571428571|FAIL/FAIL/FAIL/PASS|false|
|[N501C](http://localhost:9200/#/backtest/febab2e7-f15f-4260-b9c0-8d92c669ac10)|-0.03809523810|FAIL/FAIL/FAIL/PASS|false|
|[N502B](http://localhost:9200/#/backtest/8e4fd64f-49c6-4049-b6da-abafede9cb8e)|-0.03809523810|FAIL/FAIL/FAIL/PASS|false|
|[N502C](http://localhost:9200/#/backtest/d492f34b-8a1e-4099-8ec3-eae1b3b5d284)|-0.08571428571|FAIL/FAIL/FAIL/PASS|false|
|[N503B](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752)|0.0007936507937|PASS/PASS/PASS/PASS|true|
|[N503C](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65)|-0.01507936508|PASS/FAIL/PASS/PASS|false|
|[N504B](http://localhost:9200/#/backtest/e3201a9a-3ac0-47f5-94f5-6f16feeee8ab)|-0.08571428571|FAIL/FAIL/FAIL/PASS|false|
|[N504C](http://localhost:9200/#/backtest/72d9e745-e4e1-4e09-99eb-e550f2560206)|-0.05983606557|FAIL/FAIL/FAIL/PASS|false|
|[N505B](http://localhost:9200/#/backtest/6a2cc667-11cf-4467-b1a4-0c8e84f2b792)|-0.06269841270|FAIL/FAIL/FAIL/PASS|false|
|[N505C](http://localhost:9200/#/backtest/8e693681-095b-4db9-affb-053f19085948)|-0.04682539683|FAIL/FAIL/FAIL/PASS|false|
|[C501B](http://localhost:9200/#/backtest/e798f4aa-2793-4900-95b7-94b0b44d3fb0)|0.0007936507937|FAIL/PASS/FAIL/PASS|false|
|[C501C](http://localhost:9200/#/backtest/b8b318ea-c2ca-4269-b602-e1e3f97ab06c)|0.0007936507937|FAIL/PASS/FAIL/PASS|false|
|[C502B](http://localhost:9200/#/backtest/4ac5e198-139d-4f17-8c8f-de1c8aa6a67f)|0.0007936507937|FAIL/PASS/PASS/PASS|false|
|[C502C](http://localhost:9200/#/backtest/7e4411c6-6d8c-4bb8-9092-343f8089cc3d)|0.0007936507937|FAIL/PASS/PASS/PASS|false|
|[C503B](http://localhost:9200/#/backtest/57634d6a-96a9-480f-b4f4-2e5546c8693e)|0.0007936507937|FAIL/PASS/FAIL/PASS|false|
|[C503C](http://localhost:9200/#/backtest/cf4808de-d32d-46ec-98cf-2e453b486b85)|0.0007936507937|FAIL/PASS/FAIL/PASS|false|
|[C504B](http://localhost:9200/#/backtest/2ce5ecba-4ae6-4fd1-9917-4bf8117b09c8)|-0.03809523810|PASS/FAIL/PASS/PASS|false|
|[C504C](http://localhost:9200/#/backtest/6c7b3c72-9096-4004-bac4-ef61c251c082)|0.0007936507937|PASS/PASS/PASS/PASS|true|
|[C505B](http://localhost:9200/#/backtest/8b0b2376-126b-4918-806e-d63aa0fec3f1)|-0.03809523810|FAIL/FAIL/FAIL/PASS|false|
|[C505C](http://localhost:9200/#/backtest/ddac5c97-6655-417d-855a-fac467e06c6d)|0.0007936507937|FAIL/PASS/FAIL/PASS|false|

## Sources and bounds

The N204 agent independently reviewed the T403 family source conformance in N204_R5_INDEPENDENT_T403_SOURCE_REVIEW_20261019.md. Its own five sources had250 synthetic QA checks and post-run byte-equal readbacks against originals; all10 own-run forms/30 snapshots/HP/manifests reconcile in N204_R5_EXECUTED_QC_20261019.md. No protected risk/capital/priority code changed. This round is heavily reused development evidence, not OOS validation, absence-of-overfit proof, live promotion or funding/slippage validation.

## Dashboard registry

N501B

Dashboard: http://localhost:9200/#/backtest/16ce69b3-da09-4bc4-9eb4-be31b7e5d39d

N501C

Dashboard: http://localhost:9200/#/backtest/febab2e7-f15f-4260-b9c0-8d92c669ac10

N502B

Dashboard: http://localhost:9200/#/backtest/8e4fd64f-49c6-4049-b6da-abafede9cb8e

N502C

Dashboard: http://localhost:9200/#/backtest/d492f34b-8a1e-4099-8ec3-eae1b3b5d284

N503B

Dashboard: http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752

N503C

Dashboard: http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65

N504B

Dashboard: http://localhost:9200/#/backtest/e3201a9a-3ac0-47f5-94f5-6f16feeee8ab

N504C

Dashboard: http://localhost:9200/#/backtest/72d9e745-e4e1-4e09-99eb-e550f2560206

N505B

Dashboard: http://localhost:9200/#/backtest/6a2cc667-11cf-4467-b1a4-0c8e84f2b792

N505C

Dashboard: http://localhost:9200/#/backtest/8e693681-095b-4db9-affb-053f19085948

C501B

Dashboard: http://localhost:9200/#/backtest/e798f4aa-2793-4900-95b7-94b0b44d3fb0

C501C

Dashboard: http://localhost:9200/#/backtest/b8b318ea-c2ca-4269-b602-e1e3f97ab06c

C502B

Dashboard: http://localhost:9200/#/backtest/4ac5e198-139d-4f17-8c8f-de1c8aa6a67f

C502C

Dashboard: http://localhost:9200/#/backtest/7e4411c6-6d8c-4bb8-9092-343f8089cc3d

C503B

Dashboard: http://localhost:9200/#/backtest/57634d6a-96a9-480f-b4f4-2e5546c8693e

C503C

Dashboard: http://localhost:9200/#/backtest/cf4808de-d32d-46ec-98cf-2e453b486b85

C504B

Dashboard: http://localhost:9200/#/backtest/2ce5ecba-4ae6-4fd1-9917-4bf8117b09c8

C504C

Dashboard: http://localhost:9200/#/backtest/6c7b3c72-9096-4004-bac4-ef61c251c082

C505B

Dashboard: http://localhost:9200/#/backtest/8b0b2376-126b-4918-806e-d63aa0fec3f1

C505C

Dashboard: http://localhost:9200/#/backtest/ddac5c97-6655-417d-855a-fac467e06c6d
