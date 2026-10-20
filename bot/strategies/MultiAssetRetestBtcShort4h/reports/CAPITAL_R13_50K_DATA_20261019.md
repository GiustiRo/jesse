# R13 — datos completos: ocho snapshots

Equity diaria; extremos parciales señalados. Beneficios de trades y saldo final conciliados. DD absoluto/porcentual distinguidos por fecha.

```json
{
  "rows": [
    {
      "case": "B_F95_10k",
      "capital": 10000,
      "fee_rate": 0.00095,
      "net": 24064.339531872713,
      "final_balance": 34064.33953187272,
      "return_pct": 240.64339531872713,
      "cagr_pct": 26.5017173759847,
      "dd_pct": -14.585142774601845,
      "calmar": 1.8170351696614202,
      "sharpe": 1.4419293277435346,
      "pf": 1.7855599455991142,
      "trades": 242,
      "fees": 7794.134645025067,
      "max_underwater_days": 291,
      "terminal_gap": 0,
      "max_drawdown_usdt": 4024.4010672931254,
      "max_drawdown_usdt_date": "2024-08-21T00:01:00+00:00",
      "percent_dd_trough_date": "2024-08-21T00:01:00+00:00",
      "peak_at_percent_dd": 27592.46947037862,
      "usdt_loss_at_percent_dd": 4024.4010672931254,
      "net_minus_scaled_10k": 0,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 18775.174806331222,
          "fees": 4464.48525354194,
          "trades": 191
        },
        "SPY-USDT": {
          "net": 3795.9660998108566,
          "fees": 905.7307229079328,
          "trades": 12
        },
        "PAXG-USDT": {
          "net": 1493.198625730637,
          "fees": 2423.91866857519,
          "trades": 39
        }
      },
      "engine_metrics": {
        "total": 242,
        "total_winning_trades": 133,
        "total_losing_trades": 109,
        "starting_balance": 10000,
        "finishing_balance": 34064.33953187272,
        "win_rate": 0.5495867768595041,
        "win_rate_longs": 0.4878048780487805,
        "win_rate_shorts": 0.58125,
        "ratio_avg_win_loss": 1.4633536396263422,
        "longs_count": 82,
        "longs_percentage": 33.88429752066116,
        "shorts_percentage": 66.11570247933884,
        "shorts_count": 160,
        "fee": 7794.134645025068,
        "net_profit": 24064.339531872713,
        "net_profit_percentage": 240.64339531872713,
        "average_win": 411.2608883678641,
        "average_loss": 281.0399873491119,
        "expectancy": 99.43941955319303,
        "expectancy_percentage": 0.9943941955319304,
        "expected_net_profit_every_100_trades": 99.43941955319305,
        "average_holding_period": 296590.9090909091,
        "average_winning_holding_period": 397630.37593984965,
        "average_losing_holding_period": 173304.22018348624,
        "gross_profit": 54697.69815292592,
        "gross_loss": -30633.3586210532,
        "max_drawdown": -14.585142774601845,
        "max_underwater_period": 291,
        "annual_return": 26.5017173759847,
        "annualization": 365,
        "sharpe_ratio": 1.4419293277435346,
        "calmar_ratio": 1.8170351696614202,
        "sortino_ratio": 2.460234208957361,
        "omega_ratio": 1.3918496068695827,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -662.1264540806644,
        "largest_winning_trade": 4188.996925019079,
        "current_streak": -2,
        "avg_trades_per_day": 0.12716758365169628,
        "avg_trades_per_week": 0.8901730855618739,
        "avg_trades_per_month": 3.8709812463576347
      }
    },
    {
      "case": "B_F95_50k",
      "capital": 50000,
      "fee_rate": 0.00095,
      "net": 120674.58877740613,
      "final_balance": 170674.58877740605,
      "return_pct": 241.34917755481223,
      "cagr_pct": 26.551946769448143,
      "dd_pct": -14.598471507055844,
      "calmar": 1.8188169053599108,
      "sharpe": 1.4425410340614155,
      "pf": 1.7854436887055627,
      "trades": 242,
      "fees": 39079.659160969844,
      "max_underwater_days": 291,
      "terminal_gap": 0,
      "max_drawdown_usdt": 20179.699704426923,
      "max_drawdown_usdt_date": "2024-08-21T00:01:00+00:00",
      "percent_dd_trough_date": "2024-08-21T00:01:00+00:00",
      "peak_at_percent_dd": 138231.59290802098,
      "usdt_loss_at_percent_dd": 20179.699704426923,
      "net_minus_scaled_10k": 352.8911180425639,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 94177.6964037484,
          "fees": 22400.241079924253,
          "trades": 191
        },
        "SPY-USDT": {
          "net": 19012.94334531675,
          "fees": 4537.0674343507035,
          "trades": 12
        },
        "PAXG-USDT": {
          "net": 7483.949028340938,
          "fees": 12142.350646694886,
          "trades": 39
        }
      },
      "engine_metrics": {
        "total": 242,
        "total_winning_trades": 133,
        "total_losing_trades": 109,
        "starting_balance": 50000,
        "finishing_balance": 170674.58877740605,
        "win_rate": 0.5495867768595041,
        "win_rate_longs": 0.4878048780487805,
        "win_rate_shorts": 0.58125,
        "ratio_avg_win_loss": 1.4632583614203487,
        "longs_count": 82,
        "longs_percentage": 33.88429752066116,
        "shorts_percentage": 66.11570247933884,
        "shorts_count": 160,
        "fee": 39079.65916096984,
        "net_profit": 120674.58877740611,
        "net_profit_percentage": 241.34917755481223,
        "average_win": 2062.506328128802,
        "average_loss": 1409.5298427864634,
        "expectancy": 498.65532552647153,
        "expectancy_percentage": 0.997310651052943,
        "expected_net_profit_every_100_trades": 99.7310651052943,
        "average_holding_period": 296590.9090909091,
        "average_winning_holding_period": 397630.37593984965,
        "average_losing_holding_period": 173304.22018348624,
        "gross_profit": 274313.3416411307,
        "gross_loss": -153638.7528637245,
        "max_drawdown": -14.598471507055844,
        "max_underwater_period": 291,
        "annual_return": 26.551946769448143,
        "annualization": 365,
        "sharpe_ratio": 1.4425410340614155,
        "calmar_ratio": 1.8188169053599108,
        "sortino_ratio": 2.461960756231748,
        "omega_ratio": 1.392073694797522,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -3317.5013858413217,
        "largest_winning_trade": 20993.3564140679,
        "current_streak": -2,
        "avg_trades_per_day": 0.12716758365169628,
        "avg_trades_per_week": 0.8901730855618739,
        "avg_trades_per_month": 3.8709812463576347
      }
    },
    {
      "case": "B_N_10k",
      "capital": 10000,
      "fee_rate": 0.00045,
      "net": 35727.07072805941,
      "final_balance": 45727.07072805946,
      "return_pct": 357.2707072805941,
      "cagr_pct": 33.85137915295113,
      "dd_pct": -13.344208838110882,
      "calmar": 2.5367842757580386,
      "sharpe": 1.7433899477762427,
      "pf": 2.0578244934613017,
      "trades": 242,
      "fees": 4379.332765335456,
      "max_underwater_days": 278,
      "terminal_gap": 0,
      "max_drawdown_usdt": 4118.0350346740815,
      "max_drawdown_usdt_date": "2024-08-21T00:01:00+00:00",
      "percent_dd_trough_date": "2024-08-21T00:01:00+00:00",
      "peak_at_percent_dd": 30860.091329753555,
      "usdt_loss_at_percent_dd": 4118.0350346740815,
      "net_minus_scaled_10k": 0,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 23609.713648466135,
          "fees": 2471.3167749561776,
          "trades": 192
        },
        "SPY-USDT": {
          "net": 5444.111561471941,
          "fees": 520.8311081294106,
          "trades": 12
        },
        "PAXG-USDT": {
          "net": 6673.245518121336,
          "fees": 1387.1848822498669,
          "trades": 38
        }
      },
      "engine_metrics": {
        "total": 242,
        "total_winning_trades": 134,
        "total_losing_trades": 108,
        "starting_balance": 10000,
        "finishing_balance": 45727.07072805946,
        "win_rate": 0.5537190082644629,
        "win_rate_longs": 0.5061728395061729,
        "win_rate_shorts": 0.577639751552795,
        "ratio_avg_win_loss": 1.6585451141329894,
        "longs_count": 81,
        "longs_percentage": 33.47107438016529,
        "shorts_percentage": 66.52892561983471,
        "shorts_count": 161,
        "fee": 4379.332765335456,
        "net_profit": 35727.07072805941,
        "net_profit_percentage": 357.2707072805941,
        "average_win": 518.6654567461729,
        "average_loss": 312.7231525548868,
        "expectancy": 147.63252366966697,
        "expectancy_percentage": 1.4763252366966695,
        "expected_net_profit_every_100_trades": 147.63252366966694,
        "average_holding_period": 298099.8347107438,
        "average_winning_holding_period": 412348.2089552239,
        "average_losing_holding_period": 156347.22222222222,
        "gross_profit": 69501.17120398718,
        "gross_loss": -33774.10047592777,
        "max_drawdown": -13.344208838110882,
        "max_underwater_period": 278,
        "annual_return": 33.85137915295113,
        "annualization": 365,
        "sharpe_ratio": 1.7433899477762427,
        "calmar_ratio": 2.5367842757580386,
        "sortino_ratio": 3.0819465209101025,
        "omega_ratio": 1.4876179367373537,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -880.846336849131,
        "largest_winning_trade": 4476.164267461241,
        "current_streak": -2,
        "avg_trades_per_day": 0.12716758365169628,
        "avg_trades_per_week": 0.8901730855618739,
        "avg_trades_per_month": 3.8709812463576347
      }
    },
    {
      "case": "B_N_50k",
      "capital": 50000,
      "fee_rate": 0.00045,
      "net": 178914.2484174308,
      "final_balance": 228914.24841743018,
      "return_pct": 357.82849683486165,
      "cagr_pct": 33.88268027818966,
      "dd_pct": -13.361714270107505,
      "calmar": 2.5358033851981965,
      "sharpe": 1.7431000988466419,
      "pf": 2.056843996893946,
      "trades": 242,
      "fees": 21941.94071601311,
      "max_underwater_days": 278,
      "terminal_gap": 0,
      "max_drawdown_usdt": 20645.596803194465,
      "max_drawdown_usdt_date": "2024-08-21T00:01:00+00:00",
      "percent_dd_trough_date": "2024-08-21T00:01:00+00:00",
      "peak_at_percent_dd": 154513.08406872788,
      "usdt_loss_at_percent_dd": 20645.596803194465,
      "net_minus_scaled_10k": 278.8947771337698,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 118253.4888397898,
          "fees": 12390.2601741522,
          "trades": 192
        },
        "SPY-USDT": {
          "net": 27251.568295219004,
          "fees": 2607.435910196467,
          "trades": 12
        },
        "PAXG-USDT": {
          "net": 33409.191282422005,
          "fees": 6944.244631664437,
          "trades": 38
        }
      },
      "engine_metrics": {
        "total": 242,
        "total_winning_trades": 134,
        "total_losing_trades": 108,
        "starting_balance": 50000,
        "finishing_balance": 228914.24841743018,
        "win_rate": 0.5537190082644629,
        "win_rate_longs": 0.5061728395061729,
        "win_rate_shorts": 0.577639751552795,
        "ratio_avg_win_loss": 1.6577548631682546,
        "longs_count": 81,
        "longs_percentage": 33.47107438016529,
        "shorts_percentage": 66.52892561983471,
        "shorts_count": 161,
        "fee": 21941.940716013112,
        "net_profit": 178914.24841743082,
        "net_profit_percentage": 357.82849683486165,
        "average_win": 2598.547133728326,
        "average_loss": 1567.5098842793052,
        "expectancy": 739.3150761050858,
        "expectancy_percentage": 1.4786301522101717,
        "expected_net_profit_every_100_trades": 147.86301522101718,
        "average_holding_period": 298099.8347107438,
        "average_winning_holding_period": 412348.2089552239,
        "average_losing_holding_period": 156347.22222222222,
        "gross_profit": 348205.3159195957,
        "gross_loss": -169291.06750216495,
        "max_drawdown": -13.361714270107505,
        "max_underwater_period": 278,
        "annual_return": 33.88268027818966,
        "annualization": 365,
        "sharpe_ratio": 1.7431000988466419,
        "calmar_ratio": 2.5358033851981965,
        "sortino_ratio": 3.0817704057302686,
        "omega_ratio": 1.4874905391472355,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -4409.630403307703,
        "largest_winning_trade": 22416.500907554087,
        "current_streak": -2,
        "avg_trades_per_day": 0.12716758365169628,
        "avg_trades_per_week": 0.8901730855618739,
        "avg_trades_per_month": 3.8709812463576347
      }
    },
    {
      "case": "C_F95_10k",
      "capital": 10000,
      "fee_rate": 0.00095,
      "net": 24652.003040557607,
      "final_balance": 34652.00304055762,
      "return_pct": 246.52003040557608,
      "cagr_pct": 26.917410033490796,
      "dd_pct": -14.544128162832859,
      "calmar": 1.8507407066363413,
      "sharpe": 1.4427802728360979,
      "pf": 1.7753289395272298,
      "trades": 249,
      "fees": 8217.90174915877,
      "max_underwater_days": 223,
      "terminal_gap": 0,
      "max_drawdown_usdt": 4141.5348404129945,
      "max_drawdown_usdt_date": "2024-08-23T00:01:00+00:00",
      "percent_dd_trough_date": "2024-08-23T00:01:00+00:00",
      "peak_at_percent_dd": 28475.648688221685,
      "usdt_loss_at_percent_dd": 4141.5348404129945,
      "net_minus_scaled_10k": 0,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 18410.933158514603,
          "fees": 4467.731085587982,
          "trades": 191
        },
        "SPY-USDT": {
          "net": 4256.101164928908,
          "fees": 1391.8474548292204,
          "trades": 19
        },
        "PAXG-USDT": {
          "net": 1984.9687171140918,
          "fees": 2358.323208741563,
          "trades": 39
        }
      },
      "engine_metrics": {
        "total": 249,
        "total_winning_trades": 135,
        "total_losing_trades": 114,
        "starting_balance": 10000,
        "finishing_balance": 34652.00304055762,
        "win_rate": 0.5421686746987951,
        "win_rate_longs": 0.47191011235955055,
        "win_rate_shorts": 0.58125,
        "ratio_avg_win_loss": 1.4991666600452165,
        "longs_count": 89,
        "longs_percentage": 35.7429718875502,
        "shorts_percentage": 64.2570281124498,
        "shorts_count": 160,
        "fee": 8217.90174915877,
        "net_profit": 24652.003040557607,
        "net_profit_percentage": 246.52003040557608,
        "average_win": 418.1299554292392,
        "average_loss": 278.9082538806112,
        "expectancy": 99.00402827533175,
        "expectancy_percentage": 0.9900402827533175,
        "expected_net_profit_every_100_trades": 99.00402827533175,
        "average_holding_period": 309927.9518072289,
        "average_winning_holding_period": 417605.3333333333,
        "average_losing_holding_period": 182415.26315789475,
        "gross_profit": 56447.54398294729,
        "gross_loss": -31795.540942389678,
        "max_drawdown": -14.544128162832859,
        "max_underwater_period": 223,
        "annual_return": 26.917410033490796,
        "annualization": 365,
        "sharpe_ratio": 1.4427802728360979,
        "calmar_ratio": 1.8507407066363413,
        "sortino_ratio": 2.4381326437120263,
        "omega_ratio": 1.3809536716225903,
        "serenity_index": null,
        "total_open_trades": 1,
        "open_pl": -316.07675000000745,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -677.2898887830698,
        "largest_winning_trade": 4082.578989279564,
        "current_streak": -3,
        "avg_trades_per_day": 0.13084598483170404,
        "avg_trades_per_week": 0.9159218938219282,
        "avg_trades_per_month": 3.982951778277071
      }
    },
    {
      "case": "C_F95_50k",
      "capital": 50000,
      "fee_rate": 0.00095,
      "net": 123613.99695097592,
      "final_balance": 173613.99695097565,
      "return_pct": 247.2279939019518,
      "cagr_pct": 26.967103528013414,
      "dd_pct": -14.553963418673721,
      "calmar": 1.852904446180811,
      "sharpe": 1.4435422002724119,
      "pf": 1.7751965530496012,
      "trades": 249,
      "fees": 41199.11201272673,
      "max_underwater_days": 223,
      "terminal_gap": 0,
      "max_drawdown_usdt": 20759.677109989847,
      "max_drawdown_usdt_date": "2024-08-23T00:01:00+00:00",
      "percent_dd_trough_date": "2024-08-23T00:01:00+00:00",
      "peak_at_percent_dd": 142639.33825306868,
      "usdt_loss_at_percent_dd": 20759.677109989847,
      "net_minus_scaled_10k": 353.9817481878854,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 92330.81895285708,
          "fees": 22416.18033398004,
          "trades": 191
        },
        "SPY-USDT": {
          "net": 21335.773533003197,
          "fees": 6968.946682829301,
          "trades": 19
        },
        "PAXG-USDT": {
          "net": 9947.404465115686,
          "fees": 11813.98499591738,
          "trades": 39
        }
      },
      "engine_metrics": {
        "total": 249,
        "total_winning_trades": 135,
        "total_losing_trades": 114,
        "starting_balance": 50000,
        "finishing_balance": 173613.99695097565,
        "win_rate": 0.5421686746987951,
        "win_rate_longs": 0.47191011235955055,
        "win_rate_shorts": 0.58125,
        "ratio_avg_win_loss": 1.4990548670196637,
        "longs_count": 89,
        "longs_percentage": 35.7429718875502,
        "shorts_percentage": 64.2570281124498,
        "shorts_count": 160,
        "fee": 41199.11201272673,
        "net_profit": 123613.99695097591,
        "net_profit_percentage": 247.2279939019518,
        "average_win": 2096.8554546804357,
        "average_loss": 1398.7849950077448,
        "expectancy": 496.44175482319645,
        "expectancy_percentage": 0.9928835096463929,
        "expected_net_profit_every_100_trades": 99.28835096463929,
        "average_holding_period": 309927.9518072289,
        "average_winning_holding_period": 417605.3333333333,
        "average_losing_holding_period": 182415.26315789475,
        "gross_profit": 283075.4863818588,
        "gross_loss": -159461.4894308829,
        "max_drawdown": -14.553963418673721,
        "max_underwater_period": 223,
        "annual_return": 26.967103528013414,
        "annualization": 365,
        "sharpe_ratio": 1.4435422002724119,
        "calmar_ratio": 1.852904446180811,
        "sortino_ratio": 2.4402107152066304,
        "omega_ratio": 1.38117619532344,
        "serenity_index": null,
        "total_open_trades": 1,
        "open_pl": -1583.6232500000042,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -3393.3919604087855,
        "largest_winning_trade": 20451.592377575827,
        "current_streak": -3,
        "avg_trades_per_day": 0.13084598483170404,
        "avg_trades_per_week": 0.9159218938219282,
        "avg_trades_per_month": 3.982951778277071
      }
    },
    {
      "case": "C_N_10k",
      "capital": 10000,
      "fee_rate": 0.00045,
      "net": 37184.829395397166,
      "final_balance": 47184.82939539717,
      "return_pct": 371.8482939539716,
      "cagr_pct": 34.659478110543105,
      "dd_pct": -13.818055144302422,
      "calmar": 2.508274699195581,
      "sharpe": 1.7551320481235293,
      "pf": 2.0561736518440212,
      "trades": 249,
      "fees": 4666.532549522785,
      "max_underwater_days": 215,
      "terminal_gap": 0,
      "max_drawdown_usdt": 4257.031778943383,
      "max_drawdown_usdt_date": "2024-08-23T00:01:00+00:00",
      "percent_dd_trough_date": "2021-06-18T00:01:00+00:00",
      "peak_at_percent_dd": 13475.325000937512,
      "usdt_loss_at_percent_dd": 1862.0278395035184,
      "net_minus_scaled_10k": 7.275957614183426e-12,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 23376.865211537897,
          "fees": 2498.93713303448,
          "trades": 192
        },
        "SPY-USDT": {
          "net": 6246.943722365729,
          "fees": 818.1298672760888,
          "trades": 19
        },
        "PAXG-USDT": {
          "net": 7561.02046149355,
          "fees": 1349.4655492122176,
          "trades": 38
        }
      },
      "engine_metrics": {
        "total": 249,
        "total_winning_trades": 136,
        "total_losing_trades": 113,
        "starting_balance": 10000,
        "finishing_balance": 47184.82939539717,
        "win_rate": 0.5461847389558233,
        "win_rate_longs": 0.48863636363636365,
        "win_rate_shorts": 0.577639751552795,
        "ratio_avg_win_loss": 1.7084384018998118,
        "longs_count": 88,
        "longs_percentage": 35.34136546184739,
        "shorts_percentage": 64.65863453815261,
        "shorts_count": 161,
        "fee": 4666.532549522784,
        "net_profit": 37184.82939539716,
        "net_profit_percentage": 371.8482939539716,
        "average_win": 532.293723931432,
        "average_loss": 311.56740760422656,
        "expectancy": 149.33666423854285,
        "expectancy_percentage": 1.4933666423854286,
        "expected_net_profit_every_100_trades": 149.33666423854285,
        "average_holding_period": 311394.4578313253,
        "average_winning_holding_period": 431959.85294117645,
        "average_losing_holding_period": 166289.203539823,
        "gross_profit": 72391.94645467476,
        "gross_loss": -35207.1170592776,
        "max_drawdown": -13.818055144302422,
        "max_underwater_period": 215,
        "annual_return": 34.659478110543105,
        "annualization": 365,
        "sharpe_ratio": 1.7551320481235293,
        "calmar_ratio": 2.508274699195581,
        "sortino_ratio": 3.0699587021132344,
        "omega_ratio": 1.476953837259024,
        "serenity_index": null,
        "total_open_trades": 1,
        "open_pl": -476.2642499999929,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -911.7678280767439,
        "largest_winning_trade": 4378.856348603388,
        "current_streak": -3,
        "avg_trades_per_day": 0.13084598483170404,
        "avg_trades_per_week": 0.9159218938219282,
        "avg_trades_per_month": 3.982951778277071
      }
    },
    {
      "case": "C_N_50k",
      "capital": 50000,
      "fee_rate": 0.00045,
      "net": 186427.68151825797,
      "final_balance": 236427.6815182578,
      "return_pct": 372.855363036516,
      "cagr_pct": 34.71455553592242,
      "dd_pct": -13.849828589532343,
      "calmar": 2.506497124604096,
      "sharpe": 1.755891903333301,
      "pf": 2.0559946929176705,
      "trades": 249,
      "fees": 23393.555678690554,
      "max_underwater_days": 215,
      "terminal_gap": 0,
      "max_drawdown_usdt": 21362.473858976417,
      "max_drawdown_usdt_date": "2024-08-23T00:01:00+00:00",
      "percent_dd_trough_date": "2021-06-18T00:01:00+00:00",
      "peak_at_percent_dd": 67459.04043960644,
      "usdt_loss_at_percent_dd": 9342.96146902877,
      "net_minus_scaled_10k": 503.5345412721799,
      "new_entries_vs_10k": 0,
      "removed_entries_vs_10k": 0,
      "changed_exits_vs_10k": 0,
      "by_symbol": {
        "BTC-USDT": {
          "net": 117241.95481846963,
          "fees": 12535.055539420293,
          "trades": 192
        },
        "SPY-USDT": {
          "net": 31299.1690411104,
          "fees": 4097.938228046802,
          "trades": 19
        },
        "PAXG-USDT": {
          "net": 37886.5576586779,
          "fees": 6760.561911223455,
          "trades": 38
        }
      },
      "engine_metrics": {
        "total": 249,
        "total_winning_trades": 136,
        "total_losing_trades": 113,
        "starting_balance": 50000,
        "finishing_balance": 236427.6815182578,
        "win_rate": 0.5461847389558233,
        "win_rate_longs": 0.48863636363636365,
        "win_rate_shorts": 0.577639751552795,
        "ratio_avg_win_loss": 1.7082897080860053,
        "longs_count": 88,
        "longs_percentage": 35.34136546184739,
        "shorts_percentage": 64.65863453815261,
        "shorts_count": 161,
        "fee": 23393.55567869055,
        "net_profit": 186427.681518258,
        "net_profit_percentage": 372.855363036516,
        "average_win": 2668.896572288646,
        "average_loss": 1562.3208169291845,
        "expectancy": 748.7055482660963,
        "expectancy_percentage": 1.4974110965321927,
        "expected_net_profit_every_100_trades": 149.74110965321927,
        "average_holding_period": 311394.4578313253,
        "average_winning_holding_period": 431959.85294117645,
        "average_losing_holding_period": 166289.203539823,
        "gross_profit": 362969.9338312558,
        "gross_loss": -176542.25231299785,
        "max_drawdown": -13.849828589532343,
        "max_underwater_period": 215,
        "annual_return": 34.71455553592242,
        "annualization": 365,
        "sharpe_ratio": 1.755891903333301,
        "calmar_ratio": 2.506497124604096,
        "sortino_ratio": 3.0719973714978965,
        "omega_ratio": 1.4772151611962872,
        "serenity_index": null,
        "total_open_trades": 1,
        "open_pl": -2386.4115000000456,
        "winning_streak": 8,
        "losing_streak": 5,
        "largest_losing_trade": -4568.587619365876,
        "largest_winning_trade": 21939.692105150607,
        "current_streak": -3,
        "avg_trades_per_day": 0.13084598483170404,
        "avg_trades_per_week": 0.9159218938219282,
        "avg_trades_per_month": 3.982951778277071
      }
    }
  ],
  "annual": [
    {
      "case": "B_F95_10k",
      "year": 2020,
      "start_equity": 10000,
      "end_equity": 10634.430769790244,
      "profit": 634.4307697902441,
      "return_pct": 6.34430769790244,
      "partial": true
    },
    {
      "case": "B_F95_10k",
      "year": 2021,
      "start_equity": 10634.430769790244,
      "end_equity": 15290.224279742668,
      "profit": 4655.793509952424,
      "return_pct": 43.78037349378745,
      "partial": false
    },
    {
      "case": "B_F95_10k",
      "year": 2022,
      "start_equity": 15290.224279742668,
      "end_equity": 17562.687391029747,
      "profit": 2272.4631112870793,
      "return_pct": 14.86219606534982,
      "partial": false
    },
    {
      "case": "B_F95_10k",
      "year": 2023,
      "start_equity": 17562.687391029747,
      "end_equity": 22722.763322369727,
      "profit": 5160.075931339979,
      "return_pct": 29.38090177460837,
      "partial": false
    },
    {
      "case": "B_F95_10k",
      "year": 2024,
      "start_equity": 22722.763322369727,
      "end_equity": 28991.86769920742,
      "profit": 6269.104376837695,
      "return_pct": 27.589533402682555,
      "partial": false
    },
    {
      "case": "B_F95_10k",
      "year": 2025,
      "start_equity": 28991.86769920742,
      "end_equity": 34064.33953187272,
      "profit": 5072.471832665298,
      "return_pct": 17.496188535669855,
      "partial": true
    },
    {
      "case": "B_F95_50k",
      "year": 2020,
      "start_equity": 50000,
      "end_equity": 53175.11480517182,
      "profit": 3175.114805171819,
      "return_pct": 6.350229610343638,
      "partial": true
    },
    {
      "case": "B_F95_50k",
      "year": 2021,
      "start_equity": 53175.11480517182,
      "end_equity": 76567.07329118677,
      "profit": 23391.958486014948,
      "return_pct": 43.990424038990206,
      "partial": false
    },
    {
      "case": "B_F95_50k",
      "year": 2022,
      "start_equity": 76567.07329118677,
      "end_equity": 87967.09139017998,
      "profit": 11400.018098993212,
      "return_pct": 14.888930200634176,
      "partial": false
    },
    {
      "case": "B_F95_50k",
      "year": 2023,
      "start_equity": 87967.09139017998,
      "end_equity": 113823.75316535031,
      "profit": 25856.66177517033,
      "return_pct": 29.393562258961747,
      "partial": false
    },
    {
      "case": "B_F95_50k",
      "year": 2024,
      "start_equity": 113823.75316535031,
      "end_equity": 145258.520564334,
      "profit": 31434.76739898369,
      "return_pct": 27.617054019751762,
      "partial": false
    },
    {
      "case": "B_F95_50k",
      "year": 2025,
      "start_equity": 145258.520564334,
      "end_equity": 170674.58877740605,
      "profit": 25416.068213072052,
      "return_pct": 17.497127269594802,
      "partial": true
    },
    {
      "case": "B_N_10k",
      "year": 2020,
      "start_equity": 10000,
      "end_equity": 10733.461092061803,
      "profit": 733.4610920618034,
      "return_pct": 7.334610920618023,
      "partial": true
    },
    {
      "case": "B_N_10k",
      "year": 2021,
      "start_equity": 10733.461092061803,
      "end_equity": 16033.605602933058,
      "profit": 5300.144510871254,
      "return_pct": 49.3796405969283,
      "partial": false
    },
    {
      "case": "B_N_10k",
      "year": 2022,
      "start_equity": 16033.605602933058,
      "end_equity": 18824.914468222225,
      "profit": 2791.3088652891674,
      "return_pct": 17.409115169819,
      "partial": false
    },
    {
      "case": "B_N_10k",
      "year": 2023,
      "start_equity": 18824.914468222225,
      "end_equity": 25011.43875538822,
      "profit": 6186.524287165994,
      "return_pct": 32.86349214286886,
      "partial": false
    },
    {
      "case": "B_N_10k",
      "year": 2024,
      "start_equity": 25011.43875538822,
      "end_equity": 33473.831305615255,
      "profit": 8462.392550227036,
      "return_pct": 33.834089406008204,
      "partial": false
    },
    {
      "case": "B_N_10k",
      "year": 2025,
      "start_equity": 33473.831305615255,
      "end_equity": 45727.07072805946,
      "profit": 12253.239422444203,
      "return_pct": 36.60542861249563,
      "partial": true
    },
    {
      "case": "B_N_50k",
      "year": 2020,
      "start_equity": 50000,
      "end_equity": 53674.69685625465,
      "profit": 3674.6968562546535,
      "return_pct": 7.349393712509311,
      "partial": true
    },
    {
      "case": "B_N_50k",
      "year": 2021,
      "start_equity": 53674.69685625465,
      "end_equity": 80246.10670531697,
      "profit": 26571.409849062315,
      "return_pct": 49.50453641167789,
      "partial": false
    },
    {
      "case": "B_N_50k",
      "year": 2022,
      "start_equity": 80246.10670531697,
      "end_equity": 94244.74173376634,
      "profit": 13998.635028449367,
      "return_pct": 17.444628285650943,
      "partial": false
    },
    {
      "case": "B_N_50k",
      "year": 2023,
      "start_equity": 94244.74173376634,
      "end_equity": 125226.57471452799,
      "profit": 30981.832980761654,
      "return_pct": 32.87380538246132,
      "partial": false
    },
    {
      "case": "B_N_50k",
      "year": 2024,
      "start_equity": 125226.57471452799,
      "end_equity": 167572.73193180715,
      "profit": 42346.157217279164,
      "return_pct": 33.81563163714518,
      "partial": false
    },
    {
      "case": "B_N_50k",
      "year": 2025,
      "start_equity": 167572.73193180715,
      "end_equity": 228914.24841743018,
      "profit": 61341.516485623026,
      "return_pct": 36.60590585262145,
      "partial": true
    },
    {
      "case": "C_F95_10k",
      "year": 2020,
      "start_equity": 10000,
      "end_equity": 10618.801048040415,
      "profit": 618.8010480404155,
      "return_pct": 6.18801048040416,
      "partial": true
    },
    {
      "case": "C_F95_10k",
      "year": 2021,
      "start_equity": 10618.801048040415,
      "end_equity": 14827.396298609903,
      "profit": 4208.595250569488,
      "return_pct": 39.63343160427832,
      "partial": false
    },
    {
      "case": "C_F95_10k",
      "year": 2022,
      "start_equity": 14827.396298609903,
      "end_equity": 17107.340546922795,
      "profit": 2279.9442483128914,
      "return_pct": 15.376565125777608,
      "partial": false
    },
    {
      "case": "C_F95_10k",
      "year": 2023,
      "start_equity": 17107.340546922795,
      "end_equity": 23494.15642033834,
      "profit": 6386.815873415544,
      "return_pct": 37.3337740947957,
      "partial": false
    },
    {
      "case": "C_F95_10k",
      "year": 2024,
      "start_equity": 23494.15642033834,
      "end_equity": 29664.25025829259,
      "profit": 6170.093837954253,
      "return_pct": 26.26224890804314,
      "partial": false
    },
    {
      "case": "C_F95_10k",
      "year": 2025,
      "start_equity": 29664.25025829259,
      "end_equity": 34652.00304055762,
      "profit": 4987.752782265026,
      "return_pct": 16.8140193628211,
      "partial": true
    },
    {
      "case": "C_F95_50k",
      "year": 2020,
      "start_equity": 50000,
      "end_equity": 53091.1627482613,
      "profit": 3091.1627482612967,
      "return_pct": 6.1823254965226,
      "partial": true
    },
    {
      "case": "C_F95_50k",
      "year": 2021,
      "start_equity": 53091.1627482613,
      "end_equity": 74266.89715688527,
      "profit": 21175.734408623975,
      "return_pct": 39.88561054695956,
      "partial": false
    },
    {
      "case": "C_F95_50k",
      "year": 2022,
      "start_equity": 74266.89715688527,
      "end_equity": 85694.8317572415,
      "profit": 11427.934600356224,
      "return_pct": 15.387655924570609,
      "partial": false
    },
    {
      "case": "C_F95_50k",
      "year": 2023,
      "start_equity": 85694.8317572415,
      "end_equity": 117690.3202845248,
      "profit": 31995.488527283305,
      "return_pct": 37.33654395625741,
      "partial": false
    },
    {
      "case": "C_F95_50k",
      "year": 2024,
      "start_equity": 117690.3202845248,
      "end_equity": 148627.68586790905,
      "profit": 30937.36558338425,
      "return_pct": 26.287094391952493,
      "partial": false
    },
    {
      "case": "C_F95_50k",
      "year": 2025,
      "start_equity": 148627.68586790905,
      "end_equity": 173613.99695097565,
      "profit": 24986.311083066597,
      "return_pct": 16.811343685504767,
      "partial": true
    },
    {
      "case": "C_N_10k",
      "year": 2020,
      "start_equity": 10000,
      "end_equity": 10714.390149837101,
      "profit": 714.3901498371015,
      "return_pct": 7.143901498371008,
      "partial": true
    },
    {
      "case": "C_N_10k",
      "year": 2021,
      "start_equity": 10714.390149837101,
      "end_equity": 15594.158775117048,
      "profit": 4879.768625279947,
      "return_pct": 45.544063236806224,
      "partial": false
    },
    {
      "case": "C_N_10k",
      "year": 2022,
      "start_equity": 15594.158775117048,
      "end_equity": 18416.62348122361,
      "profit": 2822.4647061065625,
      "return_pct": 18.09949960629009,
      "partial": false
    },
    {
      "case": "C_N_10k",
      "year": 2023,
      "start_equity": 18416.62348122361,
      "end_equity": 26164.60243057277,
      "profit": 7747.978949349159,
      "return_pct": 42.07057258486331,
      "partial": false
    },
    {
      "case": "C_N_10k",
      "year": 2024,
      "start_equity": 26164.60243057277,
      "end_equity": 34660.807123078084,
      "profit": 8496.204692505315,
      "return_pct": 32.47213373507134,
      "partial": false
    },
    {
      "case": "C_N_10k",
      "year": 2025,
      "start_equity": 34660.807123078084,
      "end_equity": 47184.82939539717,
      "profit": 12524.02227231909,
      "return_pct": 36.13309473102333,
      "partial": true
    },
    {
      "case": "C_N_50k",
      "year": 2020,
      "start_equity": 50000,
      "end_equity": 53585.19733878256,
      "profit": 3585.1973387825565,
      "return_pct": 7.170394677565106,
      "partial": true
    },
    {
      "case": "C_N_50k",
      "year": 2021,
      "start_equity": 53585.19733878256,
      "end_equity": 78099.34006409113,
      "profit": 24514.14272530857,
      "return_pct": 45.74797508036112,
      "partial": false
    },
    {
      "case": "C_N_50k",
      "year": 2022,
      "start_equity": 78099.34006409113,
      "end_equity": 92247.6334552106,
      "profit": 14148.29339111947,
      "return_pct": 18.11576561275534,
      "partial": false
    },
    {
      "case": "C_N_50k",
      "year": 2023,
      "start_equity": 92247.6334552106,
      "end_equity": 131079.57550209004,
      "profit": 38831.94204687944,
      "return_pct": 42.09532601802049,
      "partial": false
    },
    {
      "case": "C_N_50k",
      "year": 2024,
      "start_equity": 131079.57550209004,
      "end_equity": 173674.56439303665,
      "profit": 42594.98889094661,
      "return_pct": 32.49551940322499,
      "partial": false
    },
    {
      "case": "C_N_50k",
      "year": 2025,
      "start_equity": 173674.56439303665,
      "end_equity": 236427.6815182578,
      "profit": 62753.11712522115,
      "return_pct": 36.132589331392715,
      "partial": true
    }
  ]
}
```

## Todos los meses

```csv
case,month,start_equity,end_equity,profit,return_pct,partial
B_F95_10k,2020-10,10000.0,9649.986622317967,-350.013377682033,-3.5001337768203356,True
B_F95_10k,2020-11,9649.986622317967,9624.371812450143,-25.61480986782408,-0.26543881220086885,False
B_F95_10k,2020-12,9624.371812450143,10634.430769790244,1010.0589573401012,10.494803993684897,False
B_F95_10k,2021-01,10634.430769790244,10654.071731584607,19.640961794362738,0.18469217788465997,False
B_F95_10k,2021-02,10654.071731584607,12592.893562878193,1938.821831293586,18.197942346735264,False
B_F95_10k,2021-03,12592.893562878193,12582.990438746776,-9.903124131416916,-0.07864057678220737,False
B_F95_10k,2021-04,12582.990438746776,11778.89711477449,-804.0933239722854,-6.39031975655201,False
B_F95_10k,2021-05,11778.89711477449,11751.748791061782,-27.14832371270859,-0.2304827306680135,False
B_F95_10k,2021-06,11751.748791061782,11935.622384345961,183.87359328417915,1.5646487731598713,False
B_F95_10k,2021-07,11935.622384345961,13378.984060449904,1443.361676103943,12.092889919146298,False
B_F95_10k,2021-08,13378.984060449904,12503.645794863374,-875.3382655865298,-6.542636284126746,False
B_F95_10k,2021-09,12503.645794863374,12286.194545994778,-217.45124886859594,-1.7391027579966134,False
B_F95_10k,2021-10,12286.194545994778,13997.884478554493,1711.689932559715,13.931815308245433,False
B_F95_10k,2021-11,13997.884478554493,14470.205344257241,472.32086570274805,3.3742303447808153,False
B_F95_10k,2021-12,14470.205344257241,15290.224279742668,820.0189354854265,5.666947468792238,False
B_F95_10k,2022-01,15290.224279742668,15629.52354959206,339.29926984939266,2.219060123917971,False
B_F95_10k,2022-02,15629.52354959206,15415.30986855372,-214.21368103833993,-1.370570768575552,False
B_F95_10k,2022-03,15415.30986855372,16366.474246247275,951.1643776935543,6.170257917642452,False
B_F95_10k,2022-04,16366.474246247275,16148.661540597912,-217.81270564936312,-1.3308468419782393,False
B_F95_10k,2022-05,16148.661540597912,16148.661540597912,0.0,0.0,False
B_F95_10k,2022-06,16148.661540597912,16473.71237090791,325.05083030999776,2.012865459424096,False
B_F95_10k,2022-07,16473.71237090791,16268.70723298764,-205.0051379202705,-1.244438007077897,False
B_F95_10k,2022-08,16268.70723298764,16091.160604469555,-177.54662851808462,-1.0913382727674725,False
B_F95_10k,2022-09,16091.160604469555,16641.097961632382,549.9373571628275,3.4176363699339074,False
B_F95_10k,2022-10,16641.097961632382,16773.531473297386,132.4335116650036,0.7958219582045789,False
B_F95_10k,2022-11,16773.531473297386,16788.680782753003,15.149309455617185,0.09031675577522158,False
B_F95_10k,2022-12,16788.680782753003,17562.687391029747,774.0066082767444,4.61028843357294,False
B_F95_10k,2023-01,17562.687391029747,21663.187859647653,4100.500468617905,23.347796253051012,False
B_F95_10k,2023-02,21663.187859647653,21910.319859307536,247.13199965988315,1.1407923951959997,False
B_F95_10k,2023-03,21910.319859307536,21835.640690621545,-74.67916868599059,-0.3408401573574804,False
B_F95_10k,2023-04,21835.640690621545,21865.679249281227,30.038558659682167,0.13756664659070328,False
B_F95_10k,2023-05,21865.679249281227,22364.102226769835,498.422977488608,2.2794763053381573,False
B_F95_10k,2023-06,22364.102226769835,23696.402995741588,1332.3007689717524,5.957318364324893,False
B_F95_10k,2023-07,23696.402995741588,23101.76009450148,-594.6429012401095,-2.5094226383091556,False
B_F95_10k,2023-08,23101.76009450148,23248.35099589053,146.5909013890523,0.634544297877726,False
B_F95_10k,2023-09,23248.35099589053,22834.06502842025,-414.2859674702813,-1.7820015171979842,False
B_F95_10k,2023-10,22834.06502842025,22826.529611246777,-7.535417173472524,-0.03300076952611475,False
B_F95_10k,2023-11,22826.529611246777,22816.65662995518,-9.872981291595352,-0.04325222212810953,False
B_F95_10k,2023-12,22816.65662995518,22722.763322369727,-93.89330758545475,-0.41151212076437904,False
B_F95_10k,2024-01,22722.763322369727,22951.696968038552,228.9336456688252,1.0075079444384683,False
B_F95_10k,2024-02,22951.696968038552,22765.34581017733,-186.35115786122333,-0.8119275804343684,False
B_F95_10k,2024-03,22765.34581017733,24051.992750993737,1286.6469408164085,5.65177859165753,False
B_F95_10k,2024-04,24051.992750993737,25452.702486388287,1400.70973539455,5.82367436202007,False
B_F95_10k,2024-05,25452.702486388287,25808.86831872363,356.165832335344,1.3993242270671002,False
B_F95_10k,2024-06,25808.86831872363,24878.376249988047,-930.4920687355843,-3.605319137765284,False
B_F95_10k,2024-07,24878.376249988047,24101.784104759496,-776.5921452285511,-3.121554788885883,False
B_F95_10k,2024-08,24101.784104759496,24093.88672612724,-7.897378632256732,-0.032766780243032034,False
B_F95_10k,2024-09,24093.88672612724,25059.38081698441,965.4940908571698,4.007216028828564,False
B_F95_10k,2024-10,25059.38081698441,25398.154464150248,338.77364716583907,1.3518835506750815,False
B_F95_10k,2024-11,25398.154464150248,28748.026282129846,3349.871817979598,13.18943005369928,False
B_F95_10k,2024-12,28748.026282129846,28991.86769920742,243.8414170775759,0.8482022893834262,False
B_F95_10k,2025-01,28991.86769920742,28874.069507694923,-117.7981915124983,-0.4063146008206897,False
B_F95_10k,2025-02,28874.069507694923,28857.145800577517,-16.923707117406593,-0.058612129865853735,False
B_F95_10k,2025-03,28857.145800577517,29962.80280694264,1105.6570063651234,3.8314842847104957,False
B_F95_10k,2025-04,29962.80280694264,30699.13993056976,736.3371236271196,2.457504153972212,False
B_F95_10k,2025-05,30699.13993056976,32812.044608235185,2112.904677665425,6.8826184787067035,False
B_F95_10k,2025-06,32812.044608235185,33356.75065659781,544.7060483626265,1.6600795679337699,False
B_F95_10k,2025-07,33356.75065659781,33809.32899097258,452.578334374768,1.3567818371579055,False
B_F95_10k,2025-08,33809.32899097258,34481.86718446125,672.5381934886682,1.9892089359958787,False
B_F95_10k,2025-09,34481.86718446125,34741.460318139725,259.5931336784779,0.7528395498126006,False
B_F95_10k,2025-10,34741.460318139725,35371.859432702215,630.3991145624896,1.814544088791048,False
B_F95_10k,2025-11,35371.859432702215,35523.77801225325,151.91857955103478,0.4294899447965683,False
B_F95_10k,2025-12,35523.77801225325,34064.33953187272,-1459.4384803805297,-4.108342530113562,True
B_F95_50k,2020-10,50000.0,48247.618057580665,-1752.3819424193352,-3.5047638848386686,True
B_F95_50k,2020-11,48247.618057580665,48113.534763670265,-134.08329391040024,-0.27790655644467366,False
B_F95_50k,2020-12,48113.534763670265,53175.11480517182,5061.580041501555,10.520075206204705,False
B_F95_50k,2021-01,53175.11480517182,53272.20535969155,97.09055451973109,0.18258645021351771,False
B_F95_50k,2021-02,53272.20535969155,63020.69270817644,9748.487348484887,18.299387612477336,False
B_F95_50k,2021-03,63020.69270817644,62964.9371768674,-55.75553130903427,-0.08847178428713631,False
B_F95_50k,2021-04,62964.9371768674,58936.87783901882,-4028.059337848579,-6.397305418623434,False
B_F95_50k,2021-05,58936.87783901882,58808.74256693058,-128.13527208824235,-0.21741102818210178,False
B_F95_50k,2021-06,58808.74256693058,59732.55294391787,923.8103769872905,1.5708725210981989,False
B_F95_50k,2021-07,59732.55294391787,66973.84119819489,7241.288254277017,12.122850769622673,False
B_F95_50k,2021-08,66973.84119819489,62581.49362521749,-4392.3475729774,-6.558303203752613,False
B_F95_50k,2021-09,62581.49362521749,61493.132590612586,-1088.3610346049027,-1.7391100332676324,False
B_F95_50k,2021-10,61493.132590612586,70074.72361380105,8581.591023188463,13.955364870285546,False
B_F95_50k,2021-11,70074.72361380105,72447.640882227,2372.917268425954,3.3862670390306215,False
B_F95_50k,2021-12,72447.640882227,76567.07329118677,4119.432408959765,5.686082195079933,False
B_F95_50k,2022-01,76567.07329118677,78273.9775934966,1706.9043023098347,2.2292928656400868,False
B_F95_50k,2022-02,78273.9775934966,77199.98861226137,-1073.988981235234,-1.3720894405198414,False
B_F95_50k,2022-03,77199.98861226137,81972.52540765787,4772.536795396503,6.182043392994108,False
B_F95_50k,2022-04,81972.52540765787,80876.16756819873,-1096.357839459146,-1.3374698827525955,False
B_F95_50k,2022-05,80876.16756819873,80876.16756819873,0.0,0.0,False
B_F95_50k,2022-06,80876.16756819873,82507.08180883374,1630.9142406350147,2.0165572747493865,False
B_F95_50k,2022-07,82507.08180883374,81478.9159352583,-1028.1658735754463,-1.2461546948874913,False
B_F95_50k,2022-08,81478.9159352583,80589.4942470879,-889.4216881703906,-1.0915973512425126,False
B_F95_50k,2022-09,80589.4942470879,83345.90497447425,2756.4107273863483,3.4203102440811595,False
B_F95_50k,2022-10,83345.90497447425,84009.77312363926,663.8681491650059,0.7965216159909971,False
B_F95_50k,2022-11,84009.77312363926,84087.97222698631,78.19910334705492,0.09308334071080893,False
B_F95_50k,2022-12,84087.97222698631,87967.09139017998,3879.119163193667,4.6131676867202875,False
B_F95_50k,2023-01,87967.09139017998,108516.42229565851,20549.330905478535,23.36024822547733,False
B_F95_50k,2023-02,108516.42229565851,109754.03483504964,1237.6125393911207,1.1404840974384323,False
B_F95_50k,2023-03,109754.03483504964,109379.48056039866,-374.55427465097455,-0.3412669750263775,False
B_F95_50k,2023-04,109379.48056039866,109530.52147498974,151.04091459108167,0.13808889365467536,False
B_F95_50k,2023-05,109530.52147498974,112029.30233701922,2498.780862029482,2.281355761279791,False
B_F95_50k,2023-06,112029.30233701922,118705.44794524416,6676.145608224935,5.959285177141416,False
B_F95_50k,2023-07,118705.44794524416,115725.20690257849,-2980.2410426656716,-2.510618589334146,False
B_F95_50k,2023-08,115725.20690257849,116459.58558428018,734.3786817016953,0.634588350591514,False
B_F95_50k,2023-09,116459.58558428018,114384.09456963826,-2075.491014641928,-1.7821555900522479,False
B_F95_50k,2023-10,114384.09456963826,114347.61725408622,-36.47731555203791,-0.0318901991481213,False
B_F95_50k,2023-11,114347.61725408622,114295.96334995248,-51.65390413373825,-0.04517269828103743,False
B_F95_50k,2023-12,114295.96334995248,113823.75316535031,-472.21018460216874,-0.41314686080062835,False
B_F95_50k,2024-01,113823.75316535031,114973.00404889119,1149.2508835408807,1.0096757940070589,False
B_F95_50k,2024-02,114973.00404889119,114035.75153412441,-937.2525147667766,-0.8151935513211583,False
B_F95_50k,2024-03,114035.75153412441,120488.99653316819,6453.244999043774,5.658966519033015,False
B_F95_50k,2024-04,120488.99653316819,127508.50744340214,7019.510910233948,5.825852245604524,False
B_F95_50k,2024-05,127508.50744340214,129288.42629743024,1779.918854028103,1.3959216445366796,False
B_F95_50k,2024-06,129288.42629743024,124619.64849878772,-4668.777798642521,-3.6111335966777958,False
B_F95_50k,2024-07,124619.64849878772,120716.7578793592,-3902.8906194285228,-3.131842102304183,False
B_F95_50k,2024-08,120716.7578793592,120688.86224686334,-27.895632495856262,-0.023108334738197733,False
B_F95_50k,2024-09,120688.86224686334,125537.44655964641,4848.584312783074,4.017424824890248,False
B_F95_50k,2024-10,125537.44655964641,127231.018620941,1693.572061294588,1.349057279486665,False
B_F95_50k,2024-11,127231.018620941,144022.98700478682,16791.968383845815,13.198014576833717,False
B_F95_50k,2024-12,144022.98700478682,145258.520564334,1235.5335595471843,0.8578724724728204,False
B_F95_50k,2025-01,145258.520564334,144661.18876127352,-597.331803060486,-0.4112198036575254,False
B_F95_50k,2025-02,144661.18876127352,144585.78146224597,-75.40729902754538,-0.052126834898325036,False
B_F95_50k,2025-03,144585.78146224597,150129.78786823657,5544.0064059906,3.834406364112808,False
B_F95_50k,2025-04,150129.78786823657,153807.23136718024,3677.4434989436704,2.4495095551398727,False
B_F95_50k,2025-05,153807.23136718024,164396.17026088326,10588.938893703016,6.88455204581655,False
B_F95_50k,2025-06,164396.17026088326,167140.51328120264,2744.3430203193857,1.669347294383039,False
B_F95_50k,2025-07,167140.51328120264,169393.5423936762,2253.029112473567,1.3479850386022285,False
B_F95_50k,2025-08,169393.5423936762,172767.4926139365,3373.9502202603035,1.9917820789290275,False
B_F95_50k,2025-09,172767.4926139365,174059.63976702446,1292.1471530879498,0.7479110413296075,False
B_F95_50k,2025-10,174059.63976702446,177225.74469699434,3166.104929969879,1.8189770668304517,False
B_F95_50k,2025-11,177225.74469699434,177986.90799330676,761.1632963124139,0.42948799431696827,False
B_F95_50k,2025-12,177986.90799330676,170674.58877740605,-7312.319215900701,-4.108346674675467,True
B_N_10k,2020-10,10000.0,9657.168403513784,-342.83159648621586,-3.428315964862161,True
B_N_10k,2020-11,9657.168403513784,9666.691299277118,9.522895763333509,0.09860960651641992,False
B_N_10k,2020-12,9666.691299277118,10733.461092061803,1066.7697927846857,11.03552145980351,False
B_N_10k,2021-01,10733.461092061803,10764.737359364808,31.276267303004715,0.2913903263331852,False
B_N_10k,2021-02,10764.737359364808,12773.583842271797,2008.846482906989,18.661360847409703,False
B_N_10k,2021-03,12773.583842271797,12788.577834808422,14.993992536625228,0.11738281692728059,False
B_N_10k,2021-04,12788.577834808422,12006.908665643874,-781.6691691645483,-6.112244686324486,False
B_N_10k,2021-05,12006.908665643874,11989.66109318256,-17.24757246131412,-0.14364706971300434,False
B_N_10k,2021-06,11989.66109318256,12185.397531283115,195.73643810055546,1.6325435438025337,False
B_N_10k,2021-07,12185.397531283115,13715.078636677175,1529.68110539406,12.553395172106342,False
B_N_10k,2021-08,13715.078636677175,12836.362500687255,-878.7161359899201,-6.4069347268636,False
B_N_10k,2021-09,12836.362500687255,12631.045591282877,-205.31690940437875,-1.5994944782323328,False
B_N_10k,2021-10,12631.045591282877,14499.729065477195,1868.6834741943185,14.794368848482042,False
B_N_10k,2021-11,14499.729065477195,15137.379600939577,637.6505354623823,4.397672070856706,False
B_N_10k,2021-12,15137.379600939577,16033.605602933058,896.2260019934802,5.920615229453929,False
B_N_10k,2022-01,16033.605602933058,16397.333994109056,363.7283911759987,2.268537721231345,False
B_N_10k,2022-02,16397.333994109056,16191.009084943325,-206.3249091657308,-1.2582832626319318,False
B_N_10k,2022-03,16191.009084943325,17247.784045331835,1056.7749603885095,6.526924633568676,False
B_N_10k,2022-04,17247.784045331835,17105.40337391703,-142.38067141480497,-0.8255012414382645,False
B_N_10k,2022-05,17105.40337391703,17105.40337391703,0.0,0.0,False
B_N_10k,2022-06,17105.40337391703,17458.67525024703,353.27187632999994,2.06526480906426,False
B_N_10k,2022-07,17458.67525024703,17267.18601739983,-191.4892328472015,-1.0968142204517584,False
B_N_10k,2022-08,17267.18601739983,17101.539711146776,-165.6463062530529,-0.9593126875805602,False
B_N_10k,2022-09,17101.539711146776,17710.433462591882,608.8937514451063,3.5604615825803654,False
B_N_10k,2022-10,17710.433462591882,17870.21490863688,159.78144604499903,0.9021882292293393,False
B_N_10k,2022-11,17870.21490863688,17942.25961976386,72.04471112697865,0.4031552585982645,False
B_N_10k,2022-12,17942.25961976386,18824.914468222225,882.6548484583654,4.919418552421906,False
B_N_10k,2023-01,18824.914468222225,23070.3018734454,4245.387405223177,22.551961191588354,False
B_N_10k,2023-02,23070.3018734454,23431.031238765423,360.7293653200213,1.5636092119593492,False
B_N_10k,2023-03,23431.031238765423,23370.103671064528,-60.92756770089545,-0.2600293904268858,False
B_N_10k,2023-04,23370.103671064528,23433.754717893346,63.651046828817925,0.27236099473373354,False
B_N_10k,2023-05,23433.754717893346,23994.35428115957,560.5995632662234,2.3922737521792303,False
B_N_10k,2023-06,23994.35428115957,25522.277576888333,1527.923295728764,6.367845026479801,False
B_N_10k,2023-07,25522.277576888333,24960.45632406354,-561.8212528247932,-2.20129747877027,False
B_N_10k,2023-08,24960.45632406354,25165.514780400877,205.0584563373377,0.8215332831861932,False
B_N_10k,2023-09,25165.514780400877,24806.25924884342,-359.2555315574573,-1.4275707637709356,False
B_N_10k,2023-10,24806.25924884342,24874.056381962804,67.79713311938394,0.273306557184938,False
B_N_10k,2023-11,24874.056381962804,24948.836527899275,74.78014593647094,0.3006351066676016,False
B_N_10k,2023-12,24948.836527899275,25011.43875538822,62.602227488943754,0.25092243247069046,False
B_N_10k,2024-01,25011.43875538822,25280.251719423384,268.81296403516535,1.0747600994255313,False
B_N_10k,2024-02,25280.251719423384,25167.635557789716,-112.61616163366853,-0.44547088725047645,False
B_N_10k,2024-03,25167.635557789716,26724.43083233272,1556.7952745430048,6.185703344949922,False
B_N_10k,2024-04,26724.43083233272,28426.41773874551,1701.9869064127888,6.368655396595502,False
B_N_10k,2024-05,28426.41773874551,29038.196853329242,611.7791145837327,2.1521498776466252,False
B_N_10k,2024-06,29038.196853329242,28081.28710836448,-956.9097449647634,-3.2953483640808523,False
B_N_10k,2024-07,28081.28710836448,27302.336590160536,-778.9505182039429,-2.7739131586027588,False
B_N_10k,2024-08,27302.336590160536,27357.70831877268,55.37172861214276,0.2028094863942842,False
B_N_10k,2024-09,27357.70831877268,28588.017733251614,1230.3094144789357,4.49712161612128,False
B_N_10k,2024-10,28588.017733251614,29034.49897757022,446.4812443186056,1.5617775547945412,False
B_N_10k,2024-11,29034.49897757022,33128.8668480153,4094.3678704450795,14.10173419423586,False
B_N_10k,2024-12,33128.8668480153,33473.831305615255,344.9644575999555,1.0412805822261895,False
B_N_10k,2025-01,33473.831305615255,35996.34740855482,2522.5161029395676,7.535785431637798,False
B_N_10k,2025-02,35996.34740855482,36806.58491369005,810.2375051352283,2.250888113560845,False
B_N_10k,2025-03,36806.58491369005,38409.632125824995,1603.0472121349449,4.355327221729555,False
B_N_10k,2025-04,38409.632125824995,39525.47599331002,1115.8438674850258,2.9051146957868923,False
B_N_10k,2025-05,39525.47599331002,42422.10258466855,2896.6265913585303,7.328505270496444,False
B_N_10k,2025-06,42422.10258466855,43504.31493162836,1082.2123469598082,2.551057776544341,False
B_N_10k,2025-07,43504.31493162836,44500.95306621188,996.638134583518,2.2908949058267902,False
B_N_10k,2025-08,44500.95306621188,45461.608642292915,960.655576081037,2.1587303414641434,False
B_N_10k,2025-09,45461.608642292915,46040.48785778528,578.8792154923649,1.2733364101723321,False
B_N_10k,2025-10,46040.48785778528,47276.16352158655,1235.675663801274,2.6838891621178362,False
B_N_10k,2025-11,47276.16352158655,47592.204512657874,316.0409910713206,0.6684996571834967,False
B_N_10k,2025-12,47592.204512657874,45727.07072805946,-1865.1337845984162,-3.918990102890396,True
B_N_50k,2020-10,50000.0,48285.309894868034,-1714.6901051319655,-3.4293802102639326,True
B_N_50k,2020-11,48285.309894868034,48335.74954944088,50.43965457284503,0.10446169794222637,False
B_N_50k,2020-12,48335.74954944088,53674.69685625465,5338.947306813774,11.045545701846947,False
B_N_50k,2021-01,53674.69685625465,53835.19645704015,160.49960078549339,0.2990228360587155,False
B_N_50k,2021-02,53835.19645704015,63922.0257428716,10086.829285831453,18.736495730782043,False
B_N_50k,2021-03,63922.0257428716,64000.20082297198,78.17508010038,0.12229756362047706,False
B_N_50k,2021-04,64000.20082297198,60075.01204460166,-3925.1887783703205,-6.133088221437932,False
B_N_50k,2021-05,60075.01204460166,59996.63219091656,-78.37985368509544,-0.13046997581440678,False
B_N_50k,2021-06,59996.63219091656,60976.955344649665,980.3231537331012,1.6339636375148459,False
B_N_50k,2021-07,60976.955344649665,68633.23975236481,7656.284407715146,12.556029346563523,False
B_N_50k,2021-08,68633.23975236481,64232.99582625228,-4400.243926112533,-6.411243213913586,False
B_N_50k,2021-09,64232.99582625228,63205.59090276314,-1027.4049234891354,-1.5994971280309356,False
B_N_50k,2021-10,63205.59090276314,72550.86600510222,9345.275102339074,14.785519712514116,False
B_N_50k,2021-11,72550.86600510222,75738.3484478801,3187.4824427778804,4.393445065912394,False
B_N_50k,2021-12,75738.3484478801,80246.10670531697,4507.758257436872,5.9517514572408725,False
B_N_50k,2022-01,80246.10670531697,82073.25692765722,1827.1502223402495,2.2769331714122654,False
B_N_50k,2022-02,82073.25692765722,81040.82139253285,-1032.435535124372,-1.2579439073977627,False
B_N_50k,2022-03,81040.82139253285,86347.0975651497,5306.276172616854,6.547658428725867,False
B_N_50k,2022-04,86347.0975651497,85628.93228072017,-718.1652844295313,-0.8317190787885731,False
B_N_50k,2022-05,85628.93228072017,85628.93228072017,0.0,0.0,False
B_N_50k,2022-06,85628.93228072017,87400.26732260016,1771.3350418799964,2.0686174575585747,False
B_N_50k,2022-07,87400.26732260016,86442.201383703,-958.065938897169,-1.096181931985274,False
B_N_50k,2022-08,86442.201383703,85610.85059686362,-831.350786839379,-0.9617418038084691,False
B_N_50k,2022-09,85610.85059686362,88660.931362649,3050.0807657853875,3.562726855907594,False
B_N_50k,2022-10,88660.931362649,89460.766206494,799.8348438449902,0.9021277258789873,False
B_N_50k,2022-11,89460.766206494,89822.76359571864,361.99738922464894,0.40464373889788074,False
B_N_50k,2022-12,89822.76359571864,94244.74173376634,4421.9781380476925,4.923003881232679,False
B_N_50k,2023-01,94244.74173376634,115504.17276538794,21259.4310316216,22.557684004989632,False
B_N_50k,2023-02,115504.17276538794,117310.65327430815,1806.4805089202127,1.5639958848842062,False
B_N_50k,2023-03,117310.65327430815,117003.57144070948,-307.0818335986696,-0.2617680705269132,False
B_N_50k,2023-04,117003.57144070948,117324.76699229327,321.1955515837908,0.2745177327741155,False
B_N_50k,2023-05,117324.76699229327,120133.09072801506,2808.3237357217877,2.393632485037256,False
B_N_50k,2023-06,120133.09072801506,127785.81757001994,7652.726842004879,6.370207239012005,False
B_N_50k,2023-07,127785.81757001994,124970.64070012576,-2815.176869894174,-2.2030432824453383,False
B_N_50k,2023-08,124970.64070012576,125995.83541309182,1025.1947129660548,0.8203484492218305,False
B_N_50k,2023-09,125995.83541309182,124197.27858143728,-1798.5568316545396,-1.4274732381096333,False
B_N_50k,2023-10,124197.27858143728,124537.60887703822,340.3302956009429,0.2740239556680679,False
B_N_50k,2023-11,124537.60887703822,124913.93018598881,376.321308950588,0.30217483083536667,False
B_N_50k,2023-12,124913.93018598881,125226.57471452799,312.6445285391819,0.2502879607371833,False
B_N_50k,2024-01,125226.57471452799,126574.72927766407,1348.1545631360787,1.0765722580925008,False
B_N_50k,2024-02,126574.72927766407,126004.98649231037,-569.7427853536938,-0.4501236452213675,False
B_N_50k,2024-03,126004.98649231037,133790.52265716816,7785.536164857782,6.178752430034118,False
B_N_50k,2024-04,133790.52265716816,142314.5586306336,8524.035973465448,6.371180711587376,False
B_N_50k,2024-05,142314.5586306336,145371.96255824823,3057.4039276146214,2.1483423460208817,False
B_N_50k,2024-06,145371.96255824823,140575.52955072222,-4796.433007526008,-3.2994209633815386,False
B_N_50k,2024-07,140575.52955072222,136671.39949068788,-3904.1300600343384,-2.7772472723466834,False
B_N_50k,2024-08,136671.39949068788,136951.84294859046,280.44345790258376,0.20519542416896908,False
B_N_50k,2024-09,136951.84294859046,143115.57390181502,6163.730953224556,4.500655719936764,False
B_N_50k,2024-10,143115.57390181502,145347.81910269675,2232.2452008817345,1.5597500258170083,False
B_N_50k,2024-11,145347.81910269675,165865.09000688963,20517.270904192876,14.115981258512189,False
B_N_50k,2024-12,165865.09000688963,167572.73193180715,1707.6419249175233,1.0295366703424902,False
B_N_50k,2025-01,167572.73193180715,180187.41715139674,12614.685219589592,7.527886592386079,False
B_N_50k,2025-02,180187.41715139674,184256.11077236227,4068.693620965525,2.2580342652600116,False
B_N_50k,2025-03,184256.11077236227,192284.8784576254,8028.767685263127,4.357395611797221,False
B_N_50k,2025-04,192284.8784576254,197852.80061468246,5567.922157057066,2.8956630400263528,False
B_N_50k,2025-05,197852.80061468246,212373.43043349148,14520.629818809015,7.339107545456414,False
B_N_50k,2025-06,212373.43043349148,217793.13569581878,5419.705262327305,2.551969543113164,False
B_N_50k,2025-07,217793.13569581878,222764.05110976737,4970.915413948591,2.282402242874748,False
B_N_50k,2025-08,222764.05110976737,227583.77657195483,4819.72546218746,2.1636011008852263,False
B_N_50k,2025-09,227583.77657195483,230480.6013409747,2896.824769019877,1.272860839491341,False
B_N_50k,2025-10,230480.6013409747,236669.18719749796,6188.585856523248,2.685078839831645,False
B_N_50k,2025-11,236669.18719749796,238251.30136226985,1582.1141647718905,0.6684918233363479,False
B_N_50k,2025-12,238251.30136226985,228914.24841743018,-9337.05294483967,-3.918993470949539,True
C_F95_10k,2020-10,10000.0,9649.986622317967,-350.013377682033,-3.5001337768203356,True
C_F95_10k,2020-11,9649.986622317967,9608.690281259886,-41.29634105808145,-0.4279419513657512,False
C_F95_10k,2020-12,9608.690281259886,10618.801048040415,1010.11076678053,10.51247086973528,False
C_F95_10k,2021-01,10618.801048040415,10638.37926766635,19.578219625935162,0.18437316545776294,False
C_F95_10k,2021-02,10638.37926766635,12500.1548494996,1861.7755818332498,17.500556569663004,False
C_F95_10k,2021-03,12500.1548494996,12486.546221691042,-13.608627808558595,-0.10886767382007889,False
C_F95_10k,2021-04,12486.546221691042,11437.211479423033,-1049.334742268009,-8.403722884116293,False
C_F95_10k,2021-05,11437.211479423033,11412.38179428323,-24.829685139802677,-0.21709561971879898,False
C_F95_10k,2021-06,11412.38179428323,11590.379910715546,177.99811643231624,1.5596929689250416,False
C_F95_10k,2021-07,11590.379910715546,12994.225307965917,1403.8453972503703,12.112160326621279,False
C_F95_10k,2021-08,12994.225307965917,12142.782435108838,-851.4428728570783,-6.552471214541078,False
C_F95_10k,2021-09,12142.782435108838,11931.606757154275,-211.17567795456307,-1.7391045181208487,False
C_F95_10k,2021-10,11931.606757154275,13570.052117055056,1638.445359900781,13.731975862499478,False
C_F95_10k,2021-11,13570.052117055056,14031.878981769352,461.8268647142959,3.403279963338268,False
C_F95_10k,2021-12,14031.878981769352,14827.396298609903,795.5173168405508,5.66935702534288,False
C_F95_10k,2022-01,14827.396298609903,15156.287615396433,328.8913167865303,2.218132638819159,False
C_F95_10k,2022-02,15156.287615396433,14948.642443854147,-207.64517154228633,-1.3700265976171577,False
C_F95_10k,2022-03,14948.642443854147,16225.6407643885,1276.9983205343524,8.542570506523607,False
C_F95_10k,2022-04,16225.6407643885,15728.131131643107,-497.5096327453921,-3.066194056491811,False
C_F95_10k,2022-05,15728.131131643107,15728.131131643107,0.0,0.0,False
C_F95_10k,2022-06,15728.131131643107,16045.096120403106,316.96498875999896,2.015274326663663,False
C_F95_10k,2022-07,16045.096120403106,15846.101011890414,-198.99510851269224,-1.2402238479559347,False
C_F95_10k,2022-08,15846.101011890414,15673.572943838775,-172.5280680516389,-1.0887729916790212,False
C_F95_10k,2022-09,15673.572943838775,16209.017174003655,535.4442301648796,3.4162231680260335,False
C_F95_10k,2022-10,16209.017174003655,16338.049503988655,129.03232998500062,0.7960527686523999,False
C_F95_10k,2022-11,16338.049503988655,16353.100556953152,15.051052964496193,0.09212270388103683,False
C_F95_10k,2022-12,16353.100556953152,17107.340546922795,754.2399899696429,4.6122139795009565,False
C_F95_10k,2023-01,17107.340546922795,21103.7689087169,3996.4283617941037,23.360897918835,False
C_F95_10k,2023-02,21103.7689087169,21344.459996472353,240.69108775545465,1.1405123359554903,False
C_F95_10k,2023-03,21344.459996472353,21271.67902364771,-72.78097282464296,-0.3409829662435637,False
C_F95_10k,2023-04,21271.67902364771,21301.19954319498,29.52051954726994,0.13877851162784616,False
C_F95_10k,2023-05,21301.19954319498,21394.889580237283,93.69003704230272,0.43983455885814315,False
C_F95_10k,2023-06,21394.889580237283,22661.945491046747,1267.055910809464,5.922236270758119,False
C_F95_10k,2023-07,22661.945491046747,22088.61294706369,-573.3325439830551,-2.5299352353025717,False
C_F95_10k,2023-08,22088.61294706369,22228.777807942613,140.1648608789219,0.6345570960695213,False
C_F95_10k,2023-09,22228.777807942613,21832.73894035648,-396.03886758613226,-1.7816493151711743,False
C_F95_10k,2023-10,21832.73894035648,21825.342383480143,-7.396556876337854,-0.033878282044885744,False
C_F95_10k,2023-11,21825.342383480143,21974.7033104884,149.3609270082561,0.6843463180733922,False
C_F95_10k,2023-12,21974.7033104884,23494.15642033834,1519.4531098499392,6.914555743397521,False
C_F95_10k,2024-01,23494.15642033834,23730.59849540146,236.4420750631216,1.006386740740517,False
C_F95_10k,2024-02,23730.59849540146,23537.571301096912,-193.02719430454817,-0.8134105608080366,False
C_F95_10k,2024-03,23537.571301096912,24870.538806819837,1332.9675057229251,5.663148031168386,False
C_F95_10k,2024-04,24870.538806819837,26320.297627864456,1449.7588210446193,5.8292216035427336,False
C_F95_10k,2024-05,26320.297627864456,26637.78716778589,317.4895399214329,1.2062536085660325,False
C_F95_10k,2024-06,26637.78716778589,25676.60887207895,-961.1782957069408,-3.6083263585397596,False
C_F95_10k,2024-07,25676.60887207895,24873.995910932015,-802.6129611469332,-3.1258526589144076,False
C_F95_10k,2024-08,24873.995910932015,24651.652324645383,-222.34358628663176,-0.8938796447615083,False
C_F95_10k,2024-09,24651.652324645383,25640.333455558757,988.6811309133736,4.010607962067292,False
C_F95_10k,2024-10,25640.333455558757,25987.37803119397,347.0445756352128,1.3535103833057782,False
C_F95_10k,2024-11,25987.37803119397,29411.952029137316,3424.5739979433456,13.177835770244517,False
C_F95_10k,2024-12,29411.952029137316,29664.25025829259,252.2982291552762,0.8578085157534998,False
C_F95_10k,2025-01,29664.25025829259,29544.13642884876,-120.11382944383149,-0.4049110575793269,False
C_F95_10k,2025-02,29544.13642884876,29527.3419777284,-16.794451120360463,-0.05684529368731317,False
C_F95_10k,2025-03,29527.3419777284,30658.65108530088,1131.3091075724806,3.8313950115313133,False
C_F95_10k,2025-04,30658.65108530088,31412.93289895925,754.2818136583701,2.460257666130672,False
C_F95_10k,2025-05,31412.93289895925,33576.05687241894,2163.123973459693,6.886093636711532,False
C_F95_10k,2025-06,33576.05687241894,34120.78817467096,544.7313022520175,1.6223802107611096,False
C_F95_10k,2025-07,34120.78817467096,34584.88540253322,464.09722786225757,1.3601597521324837,False
C_F95_10k,2025-08,34584.88540253322,35272.64874640759,687.7633438743724,1.988624035816522,False
C_F95_10k,2025-09,35272.64874640759,35536.858864996946,264.21011858935526,0.7490509728625527,False
C_F95_10k,2025-10,35536.858864996946,36182.05119774921,645.1923327522672,1.8155581369848406,False
C_F95_10k,2025-11,36182.05119774921,36337.44763033889,155.39643258967408,0.4294848618182856,False
C_F95_10k,2025-12,36337.44763033889,34652.00304055762,-1685.4445897812693,-4.638313089370804,True
C_F95_50k,2020-10,50000.0,48247.618057580665,-1752.3819424193352,-3.5047638848386686,True
C_F95_50k,2020-11,48247.618057580665,48035.14305356913,-212.4750040115323,-0.44038444293343915,False
C_F95_50k,2020-12,48035.14305356913,53091.1627482613,5056.019694692164,10.525668028205203,False
C_F95_50k,2021-01,53091.1627482613,53191.60126727418,100.43851901288144,0.18918123810760523,False
C_F95_50k,2021-02,53191.60126727418,62577.04342470188,9385.4421574277,17.64459413483015,False
C_F95_50k,2021-03,62577.04342470188,62520.52432693997,-56.51909776190587,-0.09031922038617024,False
C_F95_50k,2021-04,62520.52432693997,57255.45504331309,-5265.069283626879,-8.421345374671096,False
C_F95_50k,2021-05,57255.45504331309,57129.97044495854,-125.48459835455287,-0.21916618819922684,False
C_F95_50k,2021-06,57129.97044495854,58027.29821259946,897.3277676409198,1.5706778082537953,False
C_F95_50k,2021-07,58027.29821259946,65054.12408492164,7026.825872322181,12.10951756977796,False
C_F95_50k,2021-08,65054.12408492164,60792.239394175806,-4261.8846907458355,-6.551290561044787,False
C_F95_50k,2021-09,60792.239394175806,59734.99586397688,-1057.2435301989244,-1.73910936779903,False
C_F95_50k,2021-10,59734.99586397688,67961.93861861646,8226.942754639582,13.772400308477838,False
C_F95_50k,2021-11,67961.93861861646,70272.66984197793,2310.731223361465,3.400037241916598,False
C_F95_50k,2021-12,70272.66984197793,74266.89715688527,3994.2273149073444,5.683898625011907,False
C_F95_50k,2022-01,74266.89715688527,75921.76169388079,1654.8645369955193,2.2282666980144583,False
C_F95_50k,2022-02,75921.76169388079,74879.79318328778,-1041.9685105930112,-1.3724240419950573,False
C_F95_50k,2022-03,74879.79318328778,81286.16788678395,6406.374703496171,8.555545403036714,False
C_F95_50k,2022-04,81286.16788678395,78786.34759766578,-2499.820289118172,-3.0753329306899335,False
C_F95_50k,2022-05,78786.34759766578,78786.34759766578,0.0,0.0,False
C_F95_50k,2022-06,78786.34759766578,80375.21546224078,1588.8678645750042,2.0166791747839197,False
C_F95_50k,2022-07,80375.21546224078,79374.32656648762,-1000.8888957531599,-1.2452705600812575,False
C_F95_50k,2022-08,79374.32656648762,78508.07051931924,-866.2560471683828,-1.0913554604369047,False
C_F95_50k,2022-09,78508.07051931924,81193.06085556939,2684.99033625015,3.4200182458813844,False
C_F95_50k,2022-10,81193.06085556939,81839.71052247939,646.6496669100015,0.7964346461334815,False
C_F95_50k,2022-11,81839.71052247939,81915.99153626656,76.2810137871711,0.09320782453918763,False
C_F95_50k,2022-12,81915.99153626656,85694.8317572415,3778.840220974933,4.613067790679093,False
C_F95_50k,2023-01,85694.8317572415,105713.67027211316,20018.838514871662,23.360613591705892,False
C_F95_50k,2023-02,105713.67027211316,106919.02973802252,1205.359465909365,1.1402115382113776,False
C_F95_50k,2023-03,106919.02973802252,106552.89450546015,-366.13523256237386,-0.3424415966544858,False
C_F95_50k,2023-04,106552.89450546015,106699.57243441361,146.67792895346065,0.13765738569020414,False
C_F95_50k,2023-05,106699.57243441361,107172.51482338508,472.94238897146715,0.4432467517732297,False
C_F95_50k,2023-06,107172.51482338508,113522.02193473256,6349.507111347484,5.924566687467547,False
C_F95_50k,2023-07,113522.02193473256,110646.79433492257,-2875.227599809994,-2.5327487572966767,False
C_F95_50k,2023-08,110646.79433492257,111349.34383067439,702.549495751824,0.634947898829541,False
C_F95_50k,2023-09,111349.34383067439,109364.91466715805,-1984.429163516339,-1.7821651167823638,False
C_F95_50k,2023-10,109364.91466715805,109329.93516331348,-34.97950384457363,-0.03198420988214101,False
C_F95_50k,2023-11,109329.93516331348,110080.14282224786,750.2076589343778,0.6861868689611361,False
C_F95_50k,2023-12,110080.14282224786,117690.3202845248,7610.177462276944,6.913306312261502,False
C_F95_50k,2024-01,117690.3202845248,118877.52228879713,1187.2020042723307,1.0087507633611548,False
C_F95_50k,2024-02,118877.52228879713,117908.86294600126,-968.6593427958724,-0.8148380990332549,False
C_F95_50k,2024-03,117908.86294600126,124580.28522459202,6671.422278590762,5.6581177291533,False
C_F95_50k,2024-04,124580.28522459202,131838.08185363057,7257.796629038552,5.825798693552731,False
C_F95_50k,2024-05,131838.08185363057,133424.98704055775,1586.9051869271789,1.203677393220115,False
C_F95_50k,2024-06,133424.98704055775,128606.54098014421,-4818.446060413538,-3.611352091755393,False
C_F95_50k,2024-07,128606.54098014421,124580.96013180714,-4025.5808483370784,-3.1301524927558666,False
C_F95_50k,2024-08,124580.96013180714,123473.3089640085,-1107.6511677986418,-0.8891014859949253,False
C_F95_50k,2024-09,123473.3089640085,128433.7494799352,4960.440515926704,4.017419276722101,False
C_F95_50k,2024-10,128433.7494799352,130166.40135804638,1732.6518781111808,1.3490627542426914,False
C_F95_50k,2024-11,130166.40135804638,147361.71684943745,17195.31549139107,13.210256496292171,False
C_F95_50k,2024-12,147361.71684943745,148627.68586790905,1265.9690184716019,0.8590894877840372,False
C_F95_50k,2025-01,148627.68586790905,148017.1492332591,-610.536634649965,-0.41078257464935986,False
C_F95_50k,2025-02,148017.1492332591,147941.57118487408,-75.57804838501033,-0.05106033238480023,False
C_F95_50k,2025-03,147941.57118487408,153613.93742621643,5672.366241342359,3.8341935913698943,False
C_F95_50k,2025-04,153613.93742621643,157378.08456163527,3764.1471354188398,2.4503942796380906,False
C_F95_50k,2025-05,157378.08456163527,168210.4258935228,10832.341331887525,6.883004938114601,False
C_F95_50k,2025-06,168210.4258935228,170962.7054912191,2752.2795976962952,1.636212252050595,False
C_F95_50k,2025-07,170962.7054912191,173270.1761053221,2307.4706141030183,1.3496923831856078,False
C_F95_50k,2025-08,173270.1761053221,176721.57720688308,3451.401101560972,1.9919187358954593,False
C_F95_50k,2025-09,176721.57720688308,178041.56215356718,1319.984946684097,0.7469291342611983,False
C_F95_50k,2025-10,178041.56215356718,181279.8799526039,3238.317799036711,1.8188549683941568,False
C_F95_50k,2025-11,181279.8799526039,182058.455777091,778.5758244871104,0.42948827232822673,False
C_F95_50k,2025-12,182058.455777091,173613.99695097565,-8444.458826115355,-4.63832277939048,True
C_N_10k,2020-10,10000.0,9657.168403513784,-342.83159648621586,-3.428315964862161,True
C_N_10k,2020-11,9657.168403513784,9650.377314608259,-6.791088905525612,-0.07032174051200268,False
C_N_10k,2020-12,9650.377314608259,10714.390149837101,1064.012835228843,11.025608642453744,False
C_N_10k,2021-01,10714.390149837101,10745.602132803348,31.21198296624607,0.29130900153677697,False
C_N_10k,2021-02,10745.602132803348,12686.684800853087,1941.0826680497394,18.063973000862845,False
C_N_10k,2021-03,12686.684800853087,12700.526671554968,13.841870701880907,0.10910549855349672,False
C_N_10k,2021-04,12700.526671554968,11701.29055945615,-999.2361120988171,-7.867674608619025,False
C_N_10k,2021-05,11701.29055945615,11685.549444768285,-15.741114687865775,-0.1345246031442704,False
C_N_10k,2021-06,11685.549444768285,11875.19734075754,189.64789598925563,1.622926648726497,False
C_N_10k,2021-07,11875.19734075754,13364.57020367818,1489.3728629206398,12.541878843637221,False
C_N_10k,2021-08,13364.57020367818,12507.362693375722,-857.2075103024581,-6.414029761065853,False
C_N_10k,2021-09,12507.362693375722,12307.307437100077,-200.05525627564566,-1.5994999200079296,False
C_N_10k,2021-10,12307.307437100077,14099.101853140426,1791.7944160403495,14.558784894241207,False
C_N_10k,2021-11,14099.101853140426,14721.98601332885,622.8841601884233,4.417899570316841,False
C_N_10k,2021-12,14721.98601332885,15594.158775117048,872.1727617881988,5.92428739572608,False
C_N_10k,2022-01,15594.158775117048,15949.37889983279,355.2201247157409,2.277905014552961,False
C_N_10k,2022-02,15949.37889983279,15748.661269730592,-200.7176301021973,-1.2584667488481416,False
C_N_10k,2022-03,15748.661269730592,17184.2442349087,1435.5829651781078,9.115587290821626,False
C_N_10k,2022-04,17184.2442349087,16734.054188530437,-450.1900463782622,-2.6197837986015715,False
C_N_10k,2022-05,16734.054188530437,16734.054188530437,0.0,0.0,False
C_N_10k,2022-06,16734.054188530437,17079.86257451544,345.8083859850012,2.0664949574623614,False
C_N_10k,2022-07,17079.86257451544,16893.07659310619,-186.78598140924805,-1.0936035380515796,False
C_N_10k,2022-08,16893.07659310619,16730.353176588367,-162.72341651782335,-0.9632550685541141,False
C_N_10k,2022-09,16730.353176588367,17326.152241393804,595.7990648054365,3.561186416788664,False
C_N_10k,2022-10,17326.152241393804,17482.455136363806,156.30289497000194,0.9021212141757662,False
C_N_10k,2022-11,17482.455136363806,17552.8325497669,70.37741340309367,0.40256024027602866,False
C_N_10k,2022-12,17552.8325497669,18416.62348122361,863.7909314567114,4.921091390848953,False
C_N_10k,2023-01,18416.62348122361,22569.630814628592,4153.007333404981,22.550318942226944,False
C_N_10k,2023-02,22569.630814628592,22922.323351945088,352.6925373164959,1.5626863381739353,False
C_N_10k,2023-03,22922.323351945088,22861.696799964408,-60.62655198068023,-0.264486941615083,False
C_N_10k,2023-04,22861.696799964408,22924.754681525486,63.05788156107883,0.2758232781793213,False
C_N_10k,2023-05,22924.754681525486,23085.40169800255,160.64701647706534,0.7007578432519868,False
C_N_10k,2023-06,23085.40169800255,24547.181915508558,1461.780217506006,6.33205450192571,False
C_N_10k,2023-07,24547.181915508558,24001.448925305234,-545.7329902033234,-2.2232001705195237,False
C_N_10k,2023-08,24001.448925305234,24197.94960075722,196.50067545198544,0.8187033877142813,False
C_N_10k,2023-09,24197.94960075722,23852.45180738126,-345.4977933759583,-1.4277978055014517,False
C_N_10k,2023-10,23852.45180738126,23918.24592695006,65.79411956879994,0.27583797296864,False
C_N_10k,2023-11,23918.24592695006,24202.91858633179,284.6726593817293,1.1901903686882598,False
C_N_10k,2023-12,24202.91858633179,26164.60243057277,1961.683844240979,8.105154083974032,False
C_N_10k,2024-01,26164.60243057277,26446.308227028654,281.7057964558844,1.076667597772163,False
C_N_10k,2024-02,26446.308227028654,26327.940498016298,-118.367729012356,-0.4475775143971905,False
C_N_10k,2024-03,26327.940498016298,27954.133292024424,1626.192794008126,6.176680603371354,False
C_N_10k,2024-04,27954.133292024424,29735.01840036418,1780.8851083397567,6.370739846360607,False
C_N_10k,2024-05,29735.01840036418,30310.73197481518,575.7135744509978,1.9361466897358515,False
C_N_10k,2024-06,30310.73197481518,29313.199495708595,-997.5324791065832,-3.2910207511168688,False
C_N_10k,2024-07,29313.199495708595,28500.023909745727,-813.1755859628684,-2.774093582250947,False
C_N_10k,2024-08,28500.023909745727,28339.214484083157,-160.80942566257,-0.5642431254507807,False
C_N_10k,2024-09,28339.214484083157,29612.19525728689,1272.9807732037334,4.491940924893001,False
C_N_10k,2024-10,29612.19525728689,30074.64362734013,462.44837005324007,1.561682158432487,False
C_N_10k,2024-11,30074.64362734013,34308.02763055413,4233.384003213996,14.076256582357406,False
C_N_10k,2024-12,34308.02763055413,34660.807123078084,352.77949252395774,1.0282709817156066,False
C_N_10k,2025-01,34660.807123078084,37272.90992173806,2612.102798659973,7.536185725233047,False
C_N_10k,2025-02,37272.90992173806,38113.37491840064,840.4649966625802,2.2548950388561195,False
C_N_10k,2025-03,38113.37491840064,39773.80863562577,1660.4337172251326,4.356564383972983,False
C_N_10k,2025-04,39773.80863562577,40929.1418385283,1155.3332029025332,2.904758791109807,False
C_N_10k,2025-05,40929.1418385283,43929.56836960732,3000.4265310790142,7.330782900154986,False
C_N_10k,2025-06,43929.56836960732,45031.758838572605,1102.1904689652874,2.5089945334583197,False
C_N_10k,2025-07,45031.758838572605,46062.36158745641,1030.602748883808,2.288613137626405,False
C_N_10k,2025-08,46062.36158745641,47056.175200234036,993.8136127776233,2.1575394281309723,False
C_N_10k,2025-09,47056.175200234036,47656.23775579638,600.062555562341,1.2752046952582585,False
C_N_10k,2025-10,47656.23775579638,48935.69806373696,1279.460307940586,2.6847698605519277,False
C_N_10k,2025-11,48935.69806373696,49262.83050804907,327.1324443121048,0.6684944881873989,False
C_N_10k,2025-12,49262.83050804907,47184.82939539717,-2078.001112651895,-4.218192684466981,True
C_N_50k,2020-10,50000.0,48285.309894868034,-1714.6901051319655,-3.4293802102639326,True
C_N_50k,2020-11,48285.309894868034,48254.69267859296,-30.617216275073588,-0.06340896712009325,False
C_N_50k,2020-12,48254.69267859296,53585.19733878256,5330.504660189596,11.046603686182731,False
C_N_50k,2021-01,53585.19733878256,53744.7835921683,159.58625338574348,0.29781779541986353,False
C_N_50k,2021-02,53744.7835921683,63481.90945242735,9737.125860259053,18.117341273801223,False
C_N_50k,2021-03,63481.90945242735,63559.0788609639,77.16940853654523,0.12156125926612305,False
C_N_50k,2021-04,63559.0788609639,58555.587692860645,-5003.491168103254,-7.872189556189824,False
C_N_50k,2021-05,58555.587692860645,58480.25378577068,-75.3339070899674,-0.1286536606636357,False
C_N_50k,2021-06,58480.25378577068,59436.08017781558,955.8263920449026,1.6344429618010192,False
C_N_50k,2021-07,59436.08017781558,66899.15843283212,7463.078255016539,12.556477871167093,False
C_N_50k,2021-08,66899.15843283212,62609.838132066965,-4289.320300765154,-6.411620715784794,False
C_N_50k,2021-09,62609.838132066965,61608.39375120111,-1001.4443808658543,-1.599500031853529,False
C_N_50k,2021-10,61608.39375120111,70598.62146376114,8990.22771256003,14.592537096269865,False
C_N_50k,2021-11,70598.62146376114,73713.67828000673,3115.0568162455893,4.412347934930394,False
C_N_50k,2021-12,73713.67828000673,78099.34006409113,4385.661784084397,5.949590206888256,False
C_N_50k,2022-01,78099.34006409113,79877.56775428489,1778.2276901937585,2.2768792780252456,False
C_N_50k,2022-02,79877.56775428489,78872.48319617643,-1005.0845581084577,-1.258281375317094,False
C_N_50k,2022-03,78872.48319617643,86065.66736821493,7193.184172038498,9.120017375574662,False
C_N_50k,2022-04,86065.66736821493,83813.93803422281,-2251.729333992116,-2.6162921904254066,False
C_N_50k,2022-05,83813.93803422281,83813.93803422281,0.0,0.0,False
C_N_50k,2022-06,83813.93803422281,85547.9556243778,1734.0175901549956,2.0688892931471248,False
C_N_50k,2022-07,85547.9556243778,84609.60124866405,-938.3543757137522,-1.096875277573972,False
C_N_50k,2022-08,84609.60124866405,83796.32947469655,-813.271773967499,-0.9612050665235072,False
C_N_50k,2022-09,83796.32947469655,86782.02079251088,2985.6913178143295,3.563033532054538,False
C_N_50k,2022-10,86782.02079251088,87564.92668779088,782.9058952799969,0.902152183286753,False
C_N_50k,2022-11,87564.92668779088,87919.3720408924,354.44535310151696,0.4047800489404674,False
C_N_50k,2022-12,87919.3720408924,92247.6334552106,4328.2614143182,4.922989454821258,False
C_N_50k,2023-01,92247.6334552106,113054.85343961402,20807.21998440342,22.55583065391704,False
C_N_50k,2023-02,113054.85343961402,114823.3659747125,1768.512535098489,1.5642959866761563,False
C_N_50k,2023-03,114823.3659747125,114523.8221183361,-299.5438563764037,-0.2608736068949402,False
C_N_50k,2023-04,114523.8221183361,114838.73661638686,314.91449805075536,0.274977286145206,False
C_N_50k,2023-05,114838.73661638686,115647.99894131147,809.2623249246099,0.7046945558343287,False
C_N_50k,2023-06,115647.99894131147,122973.62887990674,7325.629938595273,6.334419968920391,False
C_N_50k,2023-07,122973.62887990674,120237.18610424832,-2736.442775658419,-2.225227311402489,False
C_N_50k,2023-08,120237.18610424832,121223.65356549056,986.4674612422386,0.8204345870061802,False
C_N_50k,2023-09,121223.65356549056,119493.14255247383,-1730.5110130167304,-1.427535767251753,False
C_N_50k,2023-10,119493.14255247383,119823.05132747813,329.90877500429633,0.27609013200018406,False
C_N_50k,2023-11,119823.05132747813,121251.54646051196,1428.4951330338372,1.19217055250056,False
C_N_50k,2023-12,121251.54646051196,131079.57550209004,9828.029041578076,8.105487582196558,False
C_N_50k,2024-01,131079.57550209004,132490.49401070963,1410.918508619594,1.076383184195695,False
C_N_50k,2024-02,132490.49401070963,131894.34908525716,-596.1449254524778,-0.44995297957323155,False
C_N_50k,2024-03,131894.34908525716,140042.82727562232,8148.47819036516,6.178034348611816,False
C_N_50k,2024-04,140042.82727562232,148963.81008269143,8920.982807069115,6.370181879798431,False
C_N_50k,2024-05,148963.81008269143,151842.27620772005,2878.4661250286154,1.9323257933794524,False
C_N_50k,2024-06,151842.27620772005,146833.157512205,-5009.118695515033,-3.298895946911762,False
C_N_50k,2024-07,146833.157512205,142752.66144204998,-4080.49607015503,-2.7790017863069227,False
C_N_50k,2024-08,142752.66144204998,141948.7827244292,-803.8787176207697,-0.5631269564435382,False
C_N_50k,2024-09,141948.7827244292,148334.9033024761,6386.120578046888,4.498890695276003,False
C_N_50k,2024-10,148334.9033024761,150649.5600985054,2314.656796029303,1.5604262681921721,False
C_N_50k,2024-11,150649.5600985054,171902.91886001057,21253.358761505166,14.107813356778621,False
C_N_50k,2024-12,171902.91886001057,173674.56439303665,1771.6455330260796,1.030608173947778,False
C_N_50k,2025-01,173674.56439303665,186751.22678522175,13076.662392185099,7.529405608636952,False
C_N_50k,2025-02,186751.22678522175,190968.01371184437,4216.786926622619,2.257970134499976,False
C_N_50k,2025-03,190968.01371184437,199290.33137524436,8322.317663399997,4.357964196013331,False
C_N_50k,2025-04,199290.33137524436,205059.0168511832,5768.685475938837,2.894613821017211,False
C_N_50k,2025-05,205059.0168511832,220103.8752859148,15044.858434731606,7.3368431516718235,False
C_N_50k,2025-06,220103.8752859148,225641.36867774607,5537.49339183126,2.5158545639589747,False
C_N_50k,2025-07,225641.36867774607,230791.58666279068,5150.217985044612,2.282479500645107,False
C_N_50k,2025-08,230791.58666279068,235785.275986413,4993.689323622326,2.1637224284603684,False
C_N_50k,2025-09,235785.275986413,238787.36263256968,3002.0866461566766,1.2732290570721005,False
C_N_50k,2025-10,238787.36263256968,245200.72479106704,6413.362158497359,2.6858046790213974,False
C_N_50k,2025-11,245200.72479106704,246839.87077652657,1639.1459854595305,0.6684914927785002,False
C_N_50k,2025-12,246839.87077652657,236427.6815182578,-10412.189258268772,-4.218195879585163,True

```