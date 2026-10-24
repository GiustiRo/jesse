# Monthly giveback guard — predeclared paired structural test
Design proposed to and approved by coordinator before implementation. 2026 sealed. Reference: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb . Preserve all reference alpha, risk3%/8%, allocation, fees.00045, 5x isolated. No optimization.
Two fixed proportional neighbors only: arm+2%/floor+1%, arm+4%/floor+2%. No new negative monthly stop, no profit cap.

## Hypothesis and valuation
Once a month has accumulated a meaningful net liquidation gain, prevent giving back most of it by flattening after a retracement to a lower positive floor. Favorable trends can continue indefinitely above floor. This changes actual exposure, not merely PnL realization or calendar accounting.
At each actual route callback: estimated liquidable equity=portfolio_value minus sum(open notional*(actual close fee + .0005 assumed close-impact reserve)). Entry fees are already in portfolio equity and must not be deducted again. The .0005 reserve is a modeling hypothesis, not executed slippage.
Month baseline uses this SAME liquidation-equity definition at first callback of UTC month, including carried positions. First/last partial months stay in root audit. All closed/open trade PnL remains included; no denominator gaming.

## Shared state and transitions
shared UTC month, liquidation-equity baseline, armed, locked, exit_pending route-key dictionary.
Only before() performs calendar baseline/reset, arms at >=threshold and locks at <=floor after arming. No reset from fill/close hooks.
Lock adds routes having open position OR pending entry; blocks every new entry globally for rest of month. Each route cancels pending orders through its normal own callback. A previously pending order can fill before cancellation; on_open preserves protective stop and adds exit_pending even after month rollover.
Across rollover: armed/locked reset and new baseline captured, but exit_pending persists. ALL new entries remain blocked until EVERY requested route is confirmed flat with no pending entry. Pending-debt cleanup is based on actual route states, never on an assumed flatten.
Each requested position liquidates only from its own update_position callback, using that route's current observed quote. Never call another strategy's liquidate() from BTC. No stale SPY synthetic execution. Exit priority supersedes original trailing/timeout; otherwise original rules unchanged.

## Limitations and falsification
Marks are latest observed quotes and asynchronous; 4h monitoring, gaps and SPY closures make the floor approximate, not guaranteed. A delayed SPY exit can happen in next month. Monthly reset cannot pretend it already closed.
Bad months before arming remain unconstrained. Cutting subsequent large trends and repeated new-month reentry can reduce CAGR or increase costs. A nicer sign count with economically poor returns does NOT pass.
Compare true-calendar MTM positive months/quarters, CAGR/DD/Sharpe, trade counts/direction economics and concentration to frozen reference. Require economically useful return, DD<=25%, target65–70% active positive months and80% quarters; retain ALL calendar bins as additional report. No threshold edits after observation. No MC independence certificate or2026 use.
Run window2020-10-15→2025-12-31exclusive, all3 assets4h, normal,10k. Coordinator controls compute slot; drafts only until granted.
