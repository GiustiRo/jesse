# Independent review: N503 exploratory family R6

Reviewer: btc_capacity_r6, author of the other capacity family. Read all five N503ExploreR601..605 sources through Jesse MCP and the frozen root protocol. No files edited or additional analysis/backtests run for this review.

PASS: each source retains the 24 listed original methods byte-identical after whitespace-only boundary normalization, including HP, all original entry/exit/sizing/ledger/priority methods, N503 ER, event sizing and 4h validity gate. before adds exactly one recipe gate to the complete N503 setup before explore_previous; event latch remains price-only and advances while occupied/pending. Original 1..3ATR geometry, MARKET, 2R and 48h remain intact. This source review is not an independent execution or financial audit.

E601 strictly compares trigger volume with median of preceding12 bars through s. E602 examines s upper wick, positive and dominating body/lower wick. E603 requires Ct<Os, using the two fully closed rolling4h bars. E604 recomputes unchanged d and requires Ct−minL(W)>=2d without changing stop/target. E605 reads only [t.open,D) from the existing1mfeed, requires exact240 minute clock and complete finite valid OHLCV, exact terminal close parity with4h close, then terminal minute close<minL(first180 minutes). Empty/short minute arrays are rejected before indexing by Python or short-circuit; duplicates/gaps/future data cannot pass. Counters separate missing/corrupt/mismatch from valid fail/pass. No shadow or intraminute execution inference. No new indicators or routes.

Checked formulas against the frozen protocol. No actionable deviation found. Dataset observability and economic outcomes remain for full-run journals and root auditor. Reused historical sample does not become OOS by this review. 2026 remains closed.

Protected methods: hyperparameters, trading_hours, signal_candles, _entry_window, _ledger, _key, _capital, _committed, _volatility_share, _plan, _signal, should_long, should_short, go_long, _short_plan, go_short, should_cancel_entry, on_open_position, update_position, on_close_position, _record_capacity, _explore_window, _explore_size, _research_gate.

```json
[
  {
    "name": "N503ExploreR601",
    "protected": 24,
    "ruleReviewed": true
  },
  {
    "name": "N503ExploreR602",
    "protected": 24,
    "ruleReviewed": true
  },
  {
    "name": "N503ExploreR603",
    "protected": 24,
    "ruleReviewed": true
  },
  {
    "name": "N503ExploreR604",
    "protected": 24,
    "ruleReviewed": true
  },
  {
    "name": "N503ExploreR605",
    "protected": 24,
    "ruleReviewed": true
  }
]
```