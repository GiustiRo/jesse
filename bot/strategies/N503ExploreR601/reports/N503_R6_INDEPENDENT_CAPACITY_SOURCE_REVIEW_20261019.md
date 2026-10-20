# R6 independent capacity source review

Reviewed all five N503CapacityR601..605 through read_strategy against frozen protocol and unchanged N204ExploreR503 seed. No mutations, new runs, market-data inspection or analysis jobs. This is source review, not independent financial reconstruction or additional market evidence.

## Protected behavior

All five preserve constants/imports, risk, ledger, sizing, original signals/priority, HP and ER helper. P601/P602 differ onlybefore/terminate plus added pure helpers; P603..605 onlybefore recipe label/terminate, supplement onopen state-reset and supplement update_position branch plus helpers. Original non-supplement on_open/update branches identical. P603..605 before identical after kind normalization.

## Protocol matching

P601 veto follows N503 latch, ATRgeometry and event/events_occupied counters; G omits only RSI<=20 requirement while keeping finite RSI for guard. No retry while N503setup true. P602 checks current visible prefixes c[:-1],[:-2],[:-3], >=143 contiguous input, current R excluded; same event consumption. R/G compute EMA120/20, ATR,RSI3 and original technical STOP fee geometry without calling original sizing/mutation methods.

P603 deadline first, then full postfill4h exact clock and R current -> MARKET close. P604 arms a one-bar observation at R technicalentry; strictly next fullbar low<=frozenentry AND close<frozenentry triggers MARKET at close, not a simulated STOP fill. Shadow popped/expires each evaluation, gap clears, resetonfill, may rearm only when not exiting. P605 from >=6 fullpostfillbars, no complete favorableclose below actualentry, G current; progressflag permanently disables untilnewfill. No partialentrybar used, idempotent clocks, deadline prioritized. No method forces original entry or concurrent BTC position.

R/G input guards reject missing/nonfinite/clock/positive-price data. P602 prefixes recompute from current visible array and are not claimed identical to historical rolling-buffer indicator states. Technicalreadiness does not imply a filled or affordable original trade. Actual PNL, engine final liquidation and financial causality remain root audits.

```json
[
  {
    "name": "P601",
    "ERidentical": true,
    "entryEqual": "veto only after seed event counters",
    "originalUpdateEqual": true,
    "originalOpenEqual": true
  },
  {
    "name": "P602",
    "ERidentical": true,
    "entryEqual": "veto only after seed event counters",
    "originalUpdateEqual": true,
    "originalOpenEqual": true
  },
  {
    "name": "P603",
    "ERidentical": true,
    "entryEqual": true,
    "originalUpdateEqual": true,
    "originalOpenEqual": true
  },
  {
    "name": "P604",
    "ERidentical": true,
    "entryEqual": true,
    "originalUpdateEqual": true,
    "originalOpenEqual": true
  },
  {
    "name": "P605",
    "ERidentical": true,
    "entryEqual": true,
    "originalUpdateEqual": true,
    "originalOpenEqual": true
  }
]
```

Conclusion: no actionable mismatch with frozen five mechanisms found.