# X402 occupancy diagnostic — 2026-10-19

Root's completed trade-path join identified30/31 original N204 BTC longs retained with the same30 exits in X402 B/C. Original source rules/helpers/priority are byteexact, but economic execution paths are not all preserved.

The missing reference long opened1721160120000 and closed1721869800000, entry64988.8/exit64421.956662. X402 supplemental short MARKET opened1721116800000 and closed1721172600000, entry62881.8/exit65253.268988, spanning that reference entry timestamp in both portfolios.

This establishes coincident temporal occupancy and is consistent with displacement. It does not establish the exact counterfactual opportunity: regenerating the reference signal and order under a changed position, capital and reservation state could change eligibility, sizing or fill. Do not report all original longs economically intact, or assign an exact opportunity cost solely by subtracting the missing trade. No new run or analysis job was used for this note; timestamps and prices are root's existing joined audit evidence.
