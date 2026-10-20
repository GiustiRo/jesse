# T404 repaired technical retries started

Only numerical sub-lot guard in on_reduced_position; raw sessions remain quarantined. QA 97ac4f5ab8dd42b39afce79352568a68 passed 41 checks. Prior fixture-only failure 462b207499f84f448c14d87602f588d7 documented in repair QA. Synthetic liquidate request is not proof of real callback flush.

- B: http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333; form exact and all three strategy snapshots equal current reviewed sources before start.
- C: http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0; form exact and all three strategy snapshots equal current reviewed sources before start.

Required real acceptance: dust third fill and closed_at same timestamp as TP2, preserving audit trail; no economic thresholds changed. These two technical retries are repairs, not new variants.
