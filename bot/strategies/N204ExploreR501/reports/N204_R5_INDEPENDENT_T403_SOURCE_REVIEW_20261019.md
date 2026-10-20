# R5 — independent source review of T403 family

Review by the N204-family agent, reading the frozen R5 protocol and N204ExitR403 plus T403ExploreR501..505 through Jesse MCP. No backtests, analyses or source changes were started for this review.

## Outcome

PASS: all five sources implement the declared rule. Twenty-two protected methods per class are byte-identical to T403. Original non-supplement branches of on_open_position and update_position are byte-identical. before is identical after normalizing the recipe label and removing C504's observational r5_anchor plan field. Entry q/cohort/return/geometry/latch, priority, sizing, risk and ledger are unchanged.

C501 resets a recovery counter per fill; only strictly later complete bar clocks after first adverse count. Two adjacent closes<=E exit; close>E or a skipped decision clock resets the count. Duplicate clocks cannot count twice.

C502 freezes the FIRST later recovery bar's high; it cannot exit at that bar. Subsequent close>frozen high exits. No retrospective high selection, barrier recursion or stop movement.

C503 requires a later close<=E and H>L and close>=(H+L)/2. Lower-half recovery leaves the position available for later observations. Midpoint is a condition, never an assumed fill.

C504 stores the source positive-cohort VWAP in event→plan→fill; _explore_size copies event fields. After adversity, later close<that frozen anchor replaces close<=E; it is not additionally restricted to E and does not recalculate A. Entries remain unchanged.

C505 records close<=E-d only BEFORE first adversity, permanently disabling rescue until next fill. This uses close, not intrabar low. Progress and first adverse cannot coincide with positive d. Later disabled paths still retain stop/target/deadline.

All five: fill reset, 48h deadline checked first, inherited exact complete-postfill helper, no partial entry bar, expected contiguous clock validation, strictly later adverse/recovery stamp, and duplicate-decision protection. Newly added helpers only log counters or call liquidate for the declared exit; no additional entry, sizing, stop or TP effect. SL1R/TP2R retained, no partial exits.

This is source conformance review, not proof of economic robustness, data completeness or absence of overfit. Independent final matrix gate review follows after all20 results are audited. 2026 remains closed.
