# Daily bear + failed recovery — predeclared single-prototype protocol
Proposed to coordinator before code. New structural exploration, no parameter sweep. 2026 remains sealed. Standalone BTC-only short; no PAXG/SPY or longs, so this is component screening and not a substitute portfolio claim.

## Economic hypothesis
A sustained daily bear regime increases the probability that a failed 4h recovery resumes downward. Sell observable pullback failure rather than chase an oversold 55bar low or fade every oversold bull-market correction.

## Rules frozen before first execution
Daily data route BTC1D, only candles with open timestamp+86400000 <= decisiontime. Latest closed daily close below SMA200, SMA200 below its value ten closed daily observations earlier. Need >=210 valid closed daily bars.
4h previous close >= its EMA20, currentclosedbar closesbelowEMA20 and closesbelowitsopen. Future STOP at signal low only when distance from currentclose is >0 and <=ATR14. Pending order expires after one future4hbar.
Initial stop distance=max(ATR14, highest last3closed4hhighs+.25ATR-entry), reject if >3ATR. Actual fill anchors the same distance. NoTP/noBE/no arbitraryhourlimit.
Trail only downward at lowest CLOSED postentryclose+3ATR14. Fully liquidate if latest CLOSED daily price>SMA200; mere slope flattening blocks new entries without exit.
Risk1% of min(wallet,equity); globalplanned8%,4.4xnotionaladmission,90%availableleveragedmargin. Actualcommission.00045eachside inclSTOP;10bpsroundtripsizingreserve is not fillfriction. Fullentry/fullExit,noadding.
Plannedwindow2020-10-15→2025-12-31exclusive,normal,10k,5xisolated,warmup240. Let engine report coverage; do not fabricate candles or inspect availability preflight. If the daily loader requires unavailable BTC history, record blockedcoverage and coordinate comparable later start; do not silently change window.

## Distinction from discarded variants
RejectShort used only4hEMA80down/RSI30–55/priorlowbreak,2.5Rtarget,48hcap/BE. RallyFade LIMITed an overextended4hrally backtoEMA20 with72hcap. Crisis required55low/ADX/volatilityexpansion, allshort4hregime. This prototype uses a much slower finite-memory daily regime, local mean-cross failure, no RSI/ADX/55low and no short fixedtimeexpiry.

## Screen and decision
First assess samplecount, net/PF/DD, annualCLOSEDPNL(partialedgeyears labeled) and actual cost headroom. Not required to hit portfolio monthlygoals standalone; report both opportunityand sparsecoverage honestly. Root truecalendarMTM will measure whether contribution occurs in weakportfolioyears. No claim hedge until combinedtest. Positive result needs neighbor/time/costcontrols; failedresult is discarded without thresholdhunting. No new run without root compute slot.