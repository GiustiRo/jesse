# BTC exploration causal/state QA — 2026-10-19

XQA1 job 135ee4ae7efb43a6b12555be15de34b6 finished succeeded, exit0. 128 assertions PASS. Sources used are exact MCP readbacks after root-requested validation fixes; no backtests, market data queries or economic changes.

Source SHA256:
- BtcExploreR101: 171d63a9ea37529f8b97b4568323118721e7bac7ecc09a987c495cf5460a1bc7
- BtcExploreR102: 042b14ecb85d8956eee21896ab95f3ba272bf01904e8675d11ab02b272c613ce
- BtcExploreR103: 35cbe5912db176141546c626b137c10ddd0d9a1c1ed82c2bb255094c9994d1c6

Compile actual source; execute actual class methods with explicit synthetic fixtures and fixed ATR stub. Verified event calculation independent of open/pending flags, same-bar before idempotence without clearing computed event, NaN fail closed before timestamp cast, exact spacing and completed-bar validation, R101 ATR source excluding t and frozen stop distance, R102 startup true ineligible until observed false then true and no repeat, R103 whole-setup false-to-true latch/no persistence repeat/half-setup rejection/rearm, original long priority and original short priority in supplements, cached signal, kind-specific fill management, actual-fill-relative stops/targets, fill-based deadline and no early timeout, close reset and original long without supplement target.

AST comparison confirms 16 base methods invariant per source, plus original _short_plan in101/103 and original _signal in102. The long runner remains original behind a kind branch. Root read all three pre-fix sources and confirmed formulas, indices, priority and hooks; final changes are validation/idempotency/comments only: finite check before int, explicit bar_end<=time, event reset after same-bar guard, debugtrue requirement comment.

Limitations: fixtures isolate state/index/lifecycle mechanics; ATR stub does not validate indicator mathematics, pending flag does not emulate broker matching, and this is not actual engine fill or economic evidence. Portfolio and real fills require six authorized fulls and root audit. No drafts/runs yet.

Temporary complete artifact: analysis job output/explore_source_state_qa.json; full QA analysis source stored separately as BTC_EXPLORE_CAUSAL_STATE_QA_SOURCE_20261019.md. Frozen protocol remains central BTC_R1_FROZEN_PROTOCOL_20261019.md. 2026 untouched.