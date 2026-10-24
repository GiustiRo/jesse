# One filled short per RSI episode — predeclared management control

Adaptive development choice after seeing the reference and rejected exploratory controls, not independent out-of-sample evidence. 2026 remains sealed. The inventory found no equivalent one-fill latch for the existing oversold-BTC signal; squeeze cooldowns belong to different entries. The already completed 24/48-hour expiry controls are NOT repeated.

## Hypothesis

A continuous oversold liquidation episode may produce repeated entry attempts after a short closes. Limiting actual filled shorts to one per episode might avoid chasing an exhausted move. This is a falsifiable premise: later continuations can remain profitable, so suppressing them may reduce expectancy and regularity. Average winner/loser holding time is descriptive and does not prove this mechanism.

## Only change

Start from Phase2FixedFeeRules4h, whose base-fee run reproduces the frozen reference. Keep all original long and short entry thresholds, stops, targets, 72-hour timeout, allocation, 3%/8% planned risk, fees and sizing.

BTC episode is defined solely by CLOSED-bar RSI(period=3)<=20, the existing threshold. A per-BTC latch starts unused. Only on_open_position for a filled short consumes it. Merely planning, submitting, expiring or cancelling an unfilled order does not consume it. An unfilled order can therefore rearm while the episode has had no filled short.

Every BTC before() callback computes the closed-bar RSI3. A finite RSI3>20 resets the latch EVEN WHILE a position is open. A later oversold episode can consequently receive one future fill after the earlier position closes. Holding an old trade through a recovery does not consume the new episode. No fixed-hour cooldown or new RSI threshold.

The latch gates only _short_plan. Long decisions and management remain unmodified. A runtime assertion rejects a duplicate short fill without an intervening closed-bar reset. Entry commissions and breakeven thresholds retain SIGNAL_FEE=0.00045, so future effective-cost tests cannot silently alter these rules.

## Configuration

Three 4h routes, BTC/PAXG/SPY, normal simulation, 2020-10-15 to2025-12-31 exclusive, 10,000 shared USDT, isolated 5x, fee0.00045 per side including LIMIT, warmup240. Up to3% planned per trade/8% aggregate, reference inverse-ATR capacity and 4.4x admission notional retained. Sizing reserve is not simulated slippage. PAXG/CFD SPY proxies, gaps and funding limitations remain.

Only one event-latch control; no RSI16/24, timer24/48 or cooldown grid. Source and draft must pass coordinator review before any run or compute slot use.

## Falsification and reporting

Compare whole-portfolio calendar MTM, CAGR/DD/Sharpe, short net/PF/count, unchanged long rules with capital interactions, and costs if the first screen is promising. Losing beneficial repeat continuations or exchanging a one-bin sign gain for worse return/risk rejects promotion. Targets stay65–70% active positive months,80% quarters,DD<=25%, useful net return. Report all calendar bins too.
Do not treat fewer shorts or a higher win rate as success by themselves. No calibration on2026 and no changes to the frozen reference.
