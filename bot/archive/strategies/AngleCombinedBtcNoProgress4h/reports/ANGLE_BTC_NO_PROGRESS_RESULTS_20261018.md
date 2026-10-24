# BTC long failure to progress — completed result — 2026-10-18

[Single tested recipe](http://localhost:9200/#/backtest/c6e326d6-5e63-4489-be8d-741d0f83f43a), compared with the unchanged [reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

## Decision

Rejected. The rule executes as predeclared but greatly reduces BTC-long contribution, increases drawdown, and fails regularity objectives. Do not relax the24h/1R rule, search neighbors or combine this failed variant with another trial to conceal the result. No new run or code change follows this report.

The assumption that a useful breakout trend must reach one initial stop-risk unit at a completed4h close within approximately one day is not supported as a management improvement here. This result does not establish that every slow trade is good, or that every time-based exit is impossible; it rejects this recipe under the full shared-account development test.

## Source and executed form

Full baseline clone with only one BTC-long state/time review plus diagnostics; source readback18431characters and inverse-delta equivalence to12917-character reference were verified before root review. Original LIMIT entries, sizing and reservations stay intact, as do BTC shorts, PAXG/SPY and trailing after passing the review. No external data, framework change or scripts.

Root created and ran the reviewed draft, normal mode, common2020-10-15→2025-12-31exclusive,10000cash,0.00045fee per side on all order types,5xisolated, original3%/8%/4.4gross admission ceilings.2026 remains sealed. Execution277.2s, finished without error, no terminal open positions.

## Economic result and true MTM

Engine:241trades=111long+130short, net7939.441908, final17939.441908, fees2426.185507,CAGR11.861636%,DD−18.265016%,Sharpe0.738878. ReferenceCAGR28.83%,DD−14.89%.

Root V4 job55d0ba2d94654a4394feedbe850bd4d9 succeeded; self-test passed and fills/fees/wallet reconciled:
- Active months33/61positive=54.098%; all months33/63=52.381%.
- Quarters14/21positive=66.667%, versus reference15/21.
- Complete periods:33/59active months,33/61all months,14/19quarters (same complete-quarter count as reference).
- Rescues2months and spoils2; no net month-count improvement.
- Worstmonth−6.79269%,worstquarter−8.30382%.
- AnnualMTM:2020partial−3.33427%,2021−5.24177%,2022+6.31889%,2023+8.59928%,2024+34.3312%,2025+26.27145%.

Components from root accounting:
| Component | Trades | Net | Fees | PF |
|---|---:|---:|---:|---:|
| BTC long |45|1722.628222|303.76636|1.608713|
| BTC short |130|2155.808727|807.98926|1.250446|
| SPY long |31|2001.440573|—|—|
| PAXG long |35|2059.564387|—|—|

The reference had31BTC longs contributing13881.758924net; the new45BTC longs contribute1722.63. This is a full-account comparison, not a fixed-size counterfactual of the original31trades. Earlier exits alter cash, eligibility and later shorts/other-asset fills. Root matched190entry cohorts, with30omitted and51added, by side/time/price identity rather than quantity. More activity did not repair economics.

## Independent lifecycle audit through bounded MCP results

Read16logs pages (maximum500entries/page, API size bounds respected) to exhaustion and retained only46ANGLE_BTC_NO_PROGRESS lines. Read all241trades in3bounded pages. No new analysis job, script, backtest or candle access was used.

All39age_review records are unique by actual fill timestamp and each matches exactly one BTC-long trade:
- Review occurs at exactly ceil((opened_at+24h)/4h)*4h for every record.
- Actual ages range24.0000–27.9833hours; no arbitrary24hclock substitution.
- Five passed: reached_at is strictly after actual fill and no later than review, best_post_entry_close>=entry+initialR.
- Thirty-four failed: reached_at is null, best_post_entry_close<entry+initialR, and every actual full exit is EXECUTED MARKET at exactly review_at; trade.closed_at matches.
- Sixother BTC longs close normally before their first eligible review. A normal protective close can occur after age24h but before the next4hcallback; the longest such holding is26.5167h, so “before review” must not be mistaken for “before24h”.
- All reviewed trades have exactly one executed entry and one executed full exit; no duplicate review or timing/order inconsistency found.

Final counters reconcile45fills/45closes=6closed_before_review+34closed_after_failure+5closed_after_pass;39checks=34exitrequests+5passes;5milestones. No open_at_termination counter or terminal synthetic closure is present. Sparse missing counter keys mean zero. Annual counters refer to event year and can differ between fills/closes across NewYear.

Descriptive cohort net: failure exits−326.536719; passed trades+3398.897663; before-review closures−1349.732723. Sum1722.628222. These are observed outcome groups, not avoided-loss estimates or causal estimates for the original entries. Passing1R did not guarantee positive eventual net PnL.

## Complete review-time trace

| Actual fill UTC | Age review UTC | Age hours | Result / executed exit |
|---|---|---:|---|
| 2020-11-13T05:03:00Z | 2020-11-14T08:00:00Z | 26.9500 | fail; MARKET at review |
| 2020-11-20T18:28:00Z | 2020-11-21T20:00:00Z | 25.5333 | fail; MARKET at review |
| 2020-12-13T12:15:00Z | 2020-12-14T16:00:00Z | 27.7500 | fail; MARKET at review |
| 2020-12-15T04:23:00Z | 2020-12-16T08:00:00Z | 27.6167 | fail; MARKET at review |
| 2020-12-30T20:12:00Z | 2021-01-01T00:00:00Z | 27.8000 | fail; MARKET at review |
| 2021-02-06T05:14:00Z | 2021-02-07T08:00:00Z | 26.7667 | fail; MARKET at review |
| 2021-02-19T12:01:00Z | 2021-02-20T16:00:00Z | 27.9833 | pass; later STOP |
| 2021-03-10T00:04:00Z | 2021-03-11T04:00:00Z | 27.9333 | fail; MARKET at review |
| 2021-03-12T00:00:00Z | 2021-03-13T00:00:00Z | 24.0000 | fail; MARKET at review |
| 2021-03-14T01:10:00Z | 2021-03-15T04:00:00Z | 26.8333 | fail; MARKET at review |
| 2021-07-24T08:00:00Z | 2021-07-25T08:00:00Z | 24.0000 | fail; MARKET at review |
| 2021-10-01T20:01:00Z | 2021-10-03T00:00:00Z | 27.9833 | fail; MARKET at review |
| 2021-10-03T21:00:00Z | 2021-10-05T00:00:00Z | 27.0000 | fail; MARKET at review |
| 2021-10-14T04:38:00Z | 2021-10-15T08:00:00Z | 27.3667 | fail; MARKET at review |
| 2022-03-25T12:14:00Z | 2022-03-26T16:00:00Z | 27.7667 | fail; MARKET at review |
| 2022-07-08T05:52:00Z | 2022-07-09T08:00:00Z | 26.1333 | fail; MARKET at review |
| 2022-07-19T16:18:00Z | 2022-07-20T20:00:00Z | 27.7000 | fail; MARKET at review |
| 2022-07-28T04:10:00Z | 2022-07-29T08:00:00Z | 27.8333 | fail; MARKET at review |
| 2023-01-09T06:54:00Z | 2023-01-10T08:00:00Z | 25.1000 | fail; MARKET at review |
| 2023-03-19T20:39:00Z | 2023-03-21T00:00:00Z | 27.3500 | fail; MARKET at review |
| 2023-09-14T16:39:00Z | 2023-09-15T20:00:00Z | 27.3500 | fail; MARKET at review |
| 2023-09-28T20:01:00Z | 2023-09-30T00:00:00Z | 27.9833 | fail; MARKET at review |
| 2024-01-30T05:32:00Z | 2024-01-31T08:00:00Z | 26.4667 | fail; MARKET at review |
| 2024-05-17T17:02:00Z | 2024-05-18T20:00:00Z | 26.9667 | fail; MARKET at review |
| 2024-06-05T16:48:00Z | 2024-06-06T20:00:00Z | 27.2000 | fail; MARKET at review |
| 2024-07-16T20:02:00Z | 2024-07-18T00:00:00Z | 27.9667 | fail; MARKET at review |
| 2024-07-22T01:40:00Z | 2024-07-23T04:00:00Z | 26.3333 | fail; MARKET at review |
| 2024-07-27T19:02:00Z | 2024-07-28T20:00:00Z | 24.9667 | fail; MARKET at review |
| 2024-09-19T12:03:00Z | 2024-09-20T16:00:00Z | 27.9500 | fail; MARKET at review |
| 2024-09-23T04:23:00Z | 2024-09-24T08:00:00Z | 27.6167 | fail; MARKET at review |
| 2024-09-27T16:00:00Z | 2024-09-28T16:00:00Z | 24.0000 | fail; MARKET at review |
| 2024-10-18T16:14:00Z | 2024-10-19T20:00:00Z | 27.7667 | fail; MARKET at review |
| 2024-11-07T20:25:00Z | 2024-11-09T00:00:00Z | 27.5833 | fail; MARKET at review |
| 2024-11-10T04:02:00Z | 2024-11-11T08:00:00Z | 27.9667 | pass; later STOP |
| 2025-01-06T08:00:00Z | 2025-01-07T08:00:00Z | 24.0000 | pass; later STOP |
| 2025-04-25T16:06:00Z | 2025-04-26T20:00:00Z | 27.9000 | fail; MARKET at review |
| 2025-05-08T08:00:00Z | 2025-05-09T08:00:00Z | 24.0000 | pass; later STOP |
| 2025-08-10T16:21:00Z | 2025-08-11T20:00:00Z | 27.6500 | pass; later STOP |
| 2025-09-12T20:03:00Z | 2025-09-14T00:00:00Z | 27.9500 | fail; MARKET at review |

## Limits and research bookkeeping

One predeclared24h/1R recipe, not a new alpha source and not a parameter sweep. The baseline BTC-long sample was only31; even the new45 are regime-dependent development observations.2020–2025 has already guided extensive adaptive selection, including18earlier economic experiments plus subsequent BTC trials. None of this is clean OOS. The recipe is economically inferior despite functional correctness; no additional stress/neighbor run is needed to reject it. Reference, risk limits and reserved2026 remain unchanged.
