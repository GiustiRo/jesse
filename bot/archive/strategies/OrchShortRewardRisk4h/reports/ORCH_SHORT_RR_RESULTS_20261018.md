# Net 1R short eligibility — initial result
Development 2020-10-15 to2025-12-31 exclusive, three 4h assets, normal engine, base fee. 2026 sealed.
[Experiment](http://localhost:9200/#/backtest/1f0b9301-0754-4044-ab29-9c9d9c979696), [frozen reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Protocol saved before run.

Hypothesis: require net planned target reward >= net planned loss while preserving 1.5ATR target and original EMA20 stop. No RSI tuning. Long rules and allocation unchanged.

Finished 148 trades:97long,51short, terminal flat.
CAGR23.43424455%, DD engine-13.30028039%, Sharpe1.14261518, net19972.15659USDT.
Reference CAGR28.82938670%, DD-14.89050602%, net27461.46337.

Short contribution collapsed from5287.019403 to190.650165USDT; PF1.360236→1.033331, WR55.28%→43.14%, commissions523.693221USDT. Short closed-PnL per year2020partial-527.38,2021-88.37,2022+712.55,2023-272.56,2024+329.70,2025partial+36.71. These are closed-trade amounts, not MTM calendar returns.
Long97trade count unchanged; net19781.506424 vs22174.443971 because capital/sizing interact with shorts. Do not claim fixed-quantity comparison.
Complete-snapshot analysis f583b3a77a174c2fbf1b93b1e814e331 succeeded.

Initial decision: reject economic superiority. A 1R eligibility rule improves payoff geometry by construction but does not create predictive advantage. Smaller DD mostly follows reduced/changed exposure and cannot by itself justify promotion. No harder threshold sweep. Root true-calendar MTM comparison pending; reference remains unchanged.