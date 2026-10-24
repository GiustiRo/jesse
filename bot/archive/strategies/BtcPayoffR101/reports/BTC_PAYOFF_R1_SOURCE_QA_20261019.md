# BTC Payoff R1 — source QA before execution — 2026-10-19

Frozen protocol: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_FROZEN_PROTOCOL_20261019.md.

Created three self-contained sources via Jesse MCP: BtcPayoffR101, BtcPayoffR102, BtcPayoffR103. No inheritance from experimental strategies, no cross-file dispatch, no source edits to PortCompare originals. Complete readback exactly equals submitted code for all three.

All 18 original methods outside management/diagnostics are text-identical: hyperparameters, trading_hours, signal_candles, _entry_window, _ledger, _key, _capital, _committed, _volatility_share, _plan, _signal, should_long, should_short, go_long, _short_plan, go_short, should_cancel_entry, _record_capacity. Modified original methods: on_open_position (short logging and R102 latch reset), update_position (short branch only), on_close_position (diagnostic), terminate (diagnostic). Original long update_position branch text-identical in all three. Added _payoff_postfill_bar and _payoff_log.

## Exact management

Initial stop remains actual fill entry + original plan distance; target actual fill entry - original target_distance. Distance comes from EMA20 signal - requested STOP entry, not recalculated after fill. Existing source semantics retained.

Timeout72h retains baseline evaluation and has priority. Otherwise management evaluates only when current closed history open matches closed_candle_open_time, bar open >= recorded fill time and decision time > fill time. Thus an intrabar fill's partial entry candle cannot count as progress or trigger RSI exit. A bar starting exactly at fill has no prefill interval and is eligible at its later close. EMA/RSI indicators retain causal prior history, while the trigger observation must be a complete postfill candle.

R101: finite EMA20; new=min(old_stop,EMA20). Assign only when price<new<old_stop. No fallback, widening, or recalculation of qty.

R102: complete postfill close <= entry - .5*target_distance latches. Nominal BE entry*(1-.00045)/(1+.00045), fixed fee. Assign only price<new<old_stop. Latch retained if price eligibility temporarily fails; resets at next short fill. No partials or target change. Fee formula covers only nominal fees, not gaps/spread.

R103: finite RSI3 >=50 on eligible complete postfill close liquidates MARKET. Hard stop, target and timeout retain original behavior.

## Stop API review

Read local framework Strategy.py _on_open_position, _detect_and_handle_entry_and_exit_modifications, _validate_stop_loss, _validate_exit_order_values and average_stop_loss. average_stop_loss reads normalized _stop_loss. After update_position the engine detects changed stop tuples, validates finite values, cancels prior STOP_LOSS orders and submits reduce_position_at against current price. Hence strict price<new<old is essential for short protective STOP routing and never-widen. No framework edits.

## Diagnostics

BTC_PAYOFF records short_open (fill entry and original stop/target), meaningful stop replacements, milestone latch, RSI neutral, timeout, partial_bar_skipped, invalid_closed_bar and short_close. Fields include current decision time, closed bar open, fill time, price, original/updated relevant levels. BTC_PAYOFF_SUMMARY reports event counts. Existing PORT_CAPACITY and sizing remain intact. ClosedTrade.type verified as framework model field before using in close logging.

No drafts, backtests, analysis jobs, scripts, installations, data imports, global configuration changes, restart, live/paper/Pi or2026. Await root source review and explicit B/C pair ticket. Future forms require debug=true/fast=false/warm240; root handles full MTM/fill/cost/concentration audit. Own later checks restricted to postfill chronology, actual management orders, forms/hp/snapshots and capacity logs, with analysis slots coordinated.

QA details:
```json
[
  {
    "name": "BtcPayoffR101",
    "readback_exact": true,
    "changed": [
      "on_open_position",
      "update_position",
      "on_close_position",
      "terminate"
    ],
    "unchanged": [
      "hyperparameters",
      "trading_hours",
      "signal_candles",
      "_entry_window",
      "_ledger",
      "_key",
      "_capital",
      "_committed",
      "_volatility_share",
      "_plan",
      "_signal",
      "should_long",
      "should_short",
      "go_long",
      "_short_plan",
      "go_short",
      "should_cancel_entry",
      "_record_capacity"
    ],
    "longBranchEqual": true,
    "added": [
      "_payoff_postfill_bar",
      "_payoff_log"
    ],
    "lines": 363
  },
  {
    "name": "BtcPayoffR102",
    "readback_exact": true,
    "changed": [
      "on_open_position",
      "update_position",
      "on_close_position",
      "terminate"
    ],
    "unchanged": [
      "hyperparameters",
      "trading_hours",
      "signal_candles",
      "_entry_window",
      "_ledger",
      "_key",
      "_capital",
      "_committed",
      "_volatility_share",
      "_plan",
      "_signal",
      "should_long",
      "should_short",
      "go_long",
      "_short_plan",
      "go_short",
      "should_cancel_entry",
      "_record_capacity"
    ],
    "longBranchEqual": true,
    "added": [
      "_payoff_postfill_bar",
      "_payoff_log"
    ],
    "lines": 371
  },
  {
    "name": "BtcPayoffR103",
    "readback_exact": true,
    "changed": [
      "on_open_position",
      "update_position",
      "on_close_position",
      "terminate"
    ],
    "unchanged": [
      "hyperparameters",
      "trading_hours",
      "signal_candles",
      "_entry_window",
      "_ledger",
      "_key",
      "_capital",
      "_committed",
      "_volatility_share",
      "_plan",
      "_signal",
      "should_long",
      "should_short",
      "go_long",
      "_short_plan",
      "go_short",
      "should_cancel_entry",
      "_record_capacity"
    ],
    "longBranchEqual": true,
    "added": [
      "_payoff_postfill_bar",
      "_payoff_log"
    ],
    "lines": 360
  }
]
```
