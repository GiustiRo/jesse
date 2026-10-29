# BTC probability: initial result and completed technical diagnosis — 2026-10-18

## Verdict

This particular four-state, shrinkage, one-SE monetary-expectancy recipe abstains economically throughout the development window. It is not a missing-data or immature-training-window result. Do not relax thresholds, remove the friction haircut, increase risk or add an unconditional comparison to manufacture trades.

This is evidence against usefulness of the tested recipe, not a proof that every causal probabilistic approach to BTC is impossible.

## Sessions and unchanged design

[Initial run](http://localhost:9200/#/backtest/8fb36f9a-ead7-41cd-9341-bc95de116f5a): finished20.11s, zero trades, metrics null, no error, empty stored equity curves. Debug=False prevented access to the diagnostic self.log summaries. Source was reviewed and unchanged.

[Same-policy diagnostic repeat](http://localhost:9200/#/backtest/ab8e72a8-f81f-41d8-8d95-8681d27e1b9c): finished100.51s, zero trades, metrics null, no error, empty stored equity curves; debug=True. No source, threshold, fee, risk or calendar change. This repeat is a technical diagnostic, not a second economic hypothesis or an optimization.

Both forms specify BTC-USDT4h, Binance Perpetual Futures,2020-10-15 through2025-12-31 exclusive, initialcash10000, fee0.00045,5xisolated, normal mode, warmup240 and benchmarkTrue.2026 was not evaluated.

## Directly verified final diagnostics

The bounded MCP logs page of the repeat shows at2025-12-31T00:00:
- labels_total11297, missing_labels0;
- window_length1080, state_counts[264,272,273,271];
- skip_window1200, skip_state_cases0;
- skip_edge10218, skip_stop_safety120, skip_qty0;
- long_signals0, short_signals0;
- final saved daily portfolio balance10000.0.

Thus the M1 maturation clock and exact contiguous240-minute coverage produced11297 valid causal labels, the rolling window filled, all states had adequate samples, and quantity constraints never suppressed a positive forecast. No eligible decision overcame the unchanged positive lower-score gate. The stop-safety count is an ex-ante protection, not a reason to loosen leverage or stops. Counters are cumulative and can overlap in diagnostic purpose: do not sum them as mutually exclusive trade cohorts.

There are no actual executed trades. Do not invent a CAGR, drawdown, winrate or positive-month rate from null metrics or absent curves. The logged cash balance supports cash retention; the dashboard does not supply a normal performance curve in this zero-trade storage path.

## Interpretation and next step

Short-horizon return-sign states did not support positive net expectancy under the tested stop/horizon, both taker fees,10bps forecast haircut and one-SE shrinkage score. This remains development evidence across2020–2025, not clean out-of-sample validation. No policy adjustment or additional run is justified on these results alone.

The independent combined intrabar-acceptance gate is separately predeclared under AngleCombinedBtcAcceptance4h; it does not modify or rescue this recipe. Reference MultiAssetRetestBtcShort4h remains unchanged.
