# BTC R1 frozen protocol — 2026-10-19

Frozen before implementation/results. Nine hypotheses, each separately in B and C, 18 economic full runs, no adaptive parameter search or combinations.

## entry
- R101 gate original short: last six closed 4h close-to-close returns; sum volume on negative returns D > sum on positive U; ties zero. Exact contiguous timestamps, positive finite closes/volume, otherwise reject.
- R102 gate original short: last six log returns; d=max(-r,0); D>0 and max(d)<=D/2. Exact timestamps and finite positive closes.
- R103 gate original short: planned target E-1.5ATR >= min(low of 30 bars strictly before signal). No signal in floor. Original plan otherwise unchanged.

## payoff
- R101 postfill closed4h EMA20 stop: min(current_stop,EMA20), update only price<new<old. Never widen. Original TP/72h.
- R102 first postfill close reaches half original target distance: latch nominal fee BE entry*(1-.00045)/(1+.00045); update only price<new<old. Original TP/72h.
- R103 first strictly postfill close RSI3>=50 liquidate MARKET. Original protective stop/TP/72h.

## explore
- R101 supplemental LONG, original plans priority. s=t-1 red body>=ATR14_s, V_s>=2*median previous30, range>0, close in upper half. t low>=low_s and close>high_s. MARKET, stop low_s-.25ATR_s, distance1..3ATR_s, TP2R, timeout24h. Event consumed even occupied.
- R102 replace shorts. Log returns last24 and preceding24: D=sum negative returns squared>=2*U and cumulative return<0 in EACH. First false-to-true crossing only; startup must see false. MARKET short stop2ATR, TP3ATR, timeout72h. Original long runner preserved. State advances while occupied.
- R103 supplemental SHORT, original plans priority. q=V*(2C-H-L)/(H-L), zero if range0. At s=t-1, C_s>C_s-12, sum last12q<0, C_s>=VWAP12_s(HLC3). At t red and C_t<VWAP12_s. First transition into complete setup only; consume while occupied, no retry persistent setup. MARKET stop max(H_s,H_t)+.25ATR_t, distance1..3ATR, TP2R, timeout48h.

## Fixed experiment
2020-10-15 through 2025-12-31 EXCLUSIVE; 2026 closed. Existing OHLCV only. Reused development sample, not OOS. 4h BTC/PAXG/SPY, three M1 data routes, route order BTC/PAXG/SPY. debug=true (capacity logs), fast=false, warmup240, chart exports. 10000 shared USDT, 1% trade/8% aggregate risk, isolated5x, gross4.4, fee.00045 each side all order types, reserve.001 sizing only. No pyramiding; common ledger unchanged. PAXG PortComparePaxgMarket4h; B SPY PortCompareSpySecond4h; C SPY PortCompareSpyMarket4h. Controls B29387384-c48c-4ac9-94bd-632a2ec3bb7f and C30ab3788-51bb-4435-8c21-9b12c45f8835 reused with previously validated debug equivalence. Original sources untouched. Entry/payoff preserve long runner. No new funding/data.

## Gates and schedule
Root reviews actual source before tickets. Each ticket permits only one B/C pair simultaneously. Max4 backtests globally, rotate entry/payoff/explore. Max2 analyses globally, explicit slots. State calculated causally on closed bars and advances even while occupied for new event recipes; no queued setups. Inspect timestamps at/after fills to avoid partial entry-bar inference. Invalid windows fail closed. No automatic second round or promotion.

## Evaluation
Reconcile executed fills/qty/fees/PNL/equity/terminal close. Report net, CAGR, PF, Sharpe, DD, costs +5/+10bps RT, exclusion best1/best3 and joint stress, exposure/notional-time, calendar daily MTM monthly/quarter denominators full and partial, temporal cohorts and year concentration, per-route incremental attribution, capacity logs. Goal >=65% active months positive (aspiration70%), >=80% quarters, DD within25%, useful profit after friction; 20–30%CAGR aspirational. No rounding a failure into acceptance. B/C share data and are not independent validation. Save all failures/zeros. Hypothesis improvement requires meaningful consistent portfolio benefit rather than selecting maximum in table; robustness remains limited by reused sample.

## Pre-run causal clarification (before management results)
Payoff new management rules R101/R102/R103 only evaluate a full closed4h bar with open_time>=actual fill_time and close_time>fill_time. The original72h timeout remains active without that gate. Thus no partial entry bar is interpreted as postfill progress. Explore R103 consumes false-to-true of the full two-bar setup, not merely crossing a newly moving VWAP.
