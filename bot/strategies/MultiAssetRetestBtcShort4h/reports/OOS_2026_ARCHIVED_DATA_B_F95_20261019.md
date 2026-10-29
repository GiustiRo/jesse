# Comparación ampliada 2026 — datos B_F95

Análisis cd864bcd130a44f69d6eaed1b468a843 succeeded. Incluye referencias repetidas sólo para comparación; no contarlas como corridas nuevas ni muestras independientes. Métricas motor completas, atribución por activo, meses y trimestres, puertas y firmas.

```json
{
  "rows": [
    {
      "case": "C504_B_F95",
      "candidate": "C504",
      "portfolio": "B",
      "cost": "F95",
      "net": -779.6113516236106,
      "balance": 9220.388648376398,
      "return_pct": -7.796113516236105,
      "dd_pct": -29.880365242317286,
      "pf": 0.8467537945388325,
      "trades": 51,
      "fees": 862.7903951799689,
      "sharpe": -0.47960293655827285,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3823.3150830300274,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": false,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2239.740961916703,
          "fees": 667.1975237066908,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1460.129610293091,
          "fees": 195.59287147327802,
          "trades": 8
        }
      },
      "economic_hash_8dec": "c6896f99843897cf89775bb276868b3e52aaceaf44713b96d48681d60fb0adf9",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 20,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 9220.388648376398,
        "win_rate": 0.39215686274509803,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.3124683815351903,
        "longs_count": 16,
        "longs_percentage": 31.372549019607842,
        "shorts_percentage": 68.62745098039215,
        "shorts_count": 35,
        "fee": 862.7903951799689,
        "net_profit": -779.6113516236104,
        "net_profit_percentage": -7.796113516236105,
        "average_win": 215.38506231402886,
        "average_loss": 164.1068579969093,
        "expectancy": -15.286497090659054,
        "expectancy_percentage": -0.15286497090659054,
        "expected_net_profit_every_100_trades": -15.286497090659054,
        "average_holding_period": 165534.11764705883,
        "average_winning_holding_period": 241398,
        "average_losing_holding_period": 116589.67741935483,
        "gross_profit": 4307.701246280577,
        "gross_loss": -5087.312597904188,
        "max_drawdown": -29.880365242317286,
        "max_underwater_period": 231,
        "annual_return": -9.711456283782184,
        "annualization": 365,
        "sharpe_ratio": -0.47960293655827285,
        "calmar_ratio": -0.32501129772097254,
        "sortino_ratio": -0.6804604909318235,
        "omega_ratio": 0.9067439941708931,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -237.3391618176238,
        "largest_winning_trade": 945.4491149495406,
        "current_streak": 4,
        "avg_trades_per_day": 0.17583638405309568,
        "avg_trades_per_week": 1.2308546883716698,
        "avg_trades_per_month": 5.352459530576232
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 4,
      "calendar_months": 10,
      "positive_full_quarters": 1,
      "full_quarters": 3,
      "best_month": {
        "case": "C504_B_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "C504_B_F95",
        "month": "2026-07",
        "start_equity": 11563.629744258766,
        "end_equity": 9722.365773183414,
        "profit": -1841.263971075352,
        "return_pct": -15.922889367756888,
        "partial": false
      },
      "best_trade": 945.4491149495406,
      "net_excluding_best_trade_arithmetic": -1725.0604665731512,
      "comparisons": {
        "K1001": {
          "delta_net": -251.55752968808963,
          "delta_return_pct": -2.5155752968808933,
          "new_entries": 15,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -55.68701692260311,
          "delta_return_pct": -0.5568701692260278,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 51,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "C504_C_F95",
      "candidate": "C504",
      "portfolio": "C",
      "cost": "F95",
      "net": 215.74229901402975,
      "balance": 10215.742299014035,
      "return_pct": 2.1574229901402986,
      "dd_pct": -22.95486448001942,
      "pf": 1.0399508395493404,
      "trades": 52,
      "fees": 946.3085764438935,
      "sharpe": 0.2349488062379879,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2961.49963802009,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": true,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2424.70716447998,
          "fees": 716.3340407434987,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1468.8741184797464,
          "fees": 198.6195235954715,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1171.5753450142636,
          "fees": 31.35501210492323,
          "trades": 1
        }
      },
      "economic_hash_8dec": "967a5f2da2fae9855d3d9ad35cb8e651b8fdf4226ceb4034a98ac84915eff01b",
      "engine_metrics": {
        "total": 52,
        "total_winning_trades": 21,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 10215.742299014035,
        "win_rate": 0.40384615384615385,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.5351655250490255,
        "longs_count": 17,
        "longs_percentage": 32.69230769230769,
        "shorts_percentage": 67.3076923076923,
        "shorts_count": 35,
        "fee": 946.3085764438936,
        "net_profit": 215.74229901402987,
        "net_profit_percentage": 2.1574229901402986,
        "average_win": 267.42555590919073,
        "average_loss": 174.19981855093476,
        "expectancy": 4.148890365654381,
        "expectancy_percentage": 0.04148890365654381,
        "expected_net_profit_every_100_trades": 4.148890365654381,
        "average_holding_period": 214525.38461538462,
        "average_winning_holding_period": 359097.14285714284,
        "average_losing_holding_period": 116589.67741935483,
        "gross_profit": 5615.936674093005,
        "gross_loss": -5400.194375078978,
        "max_drawdown": -22.95486448001942,
        "max_underwater_period": 105,
        "annual_return": 2.7229124794432735,
        "annualization": 365,
        "sharpe_ratio": 0.2349488062379879,
        "calmar_ratio": 0.1186202811963179,
        "sortino_ratio": 0.34399834854286654,
        "omega_ratio": 1.0461440178367567,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -245.94986814853021,
        "largest_winning_trade": 1171.5753450142636,
        "current_streak": 4,
        "avg_trades_per_day": 0.1792841562894309,
        "avg_trades_per_week": 1.2549890940260162,
        "avg_trades_per_month": 5.457409717450277
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 6,
      "calendar_months": 10,
      "positive_full_quarters": 2,
      "full_quarters": 3,
      "best_month": {
        "case": "C504_C_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "C504_C_F95",
        "month": "2026-07",
        "start_equity": 12811.893274571721,
        "end_equity": 10770.853796592522,
        "profit": -2041.0394779791986,
        "return_pct": -15.930818609222507,
        "partial": false
      },
      "best_trade": 1171.5753450142636,
      "net_excluding_best_trade_arithmetic": -955.8330460002338,
      "comparisons": {
        "K1001": {
          "delta_net": -280.6240777646387,
          "delta_return_pct": -2.8062407776463876,
          "new_entries": 15,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -62.31979868729087,
          "delta_return_pct": -0.6231979868729045,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 52,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1001_B_F95",
      "candidate": "K1001",
      "portfolio": "B",
      "cost": "F95",
      "net": -528.053821935521,
      "balance": 9471.946178064476,
      "return_pct": -5.280538219355211,
      "dd_pct": -27.816571716671625,
      "pf": 0.8813414198945572,
      "trades": 46,
      "fees": 782.4942375242423,
      "sharpe": -0.31250732651784274,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3559.244250867445,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": false,
      "by_symbol": {
        "BTC-USDT": {
          "net": -1984.4714618916319,
          "fees": 585.3411009918782,
          "trades": 38
        },
        "PAXG-USDT": {
          "net": 1456.4176399561106,
          "fees": 197.15313653236407,
          "trades": 8
        }
      },
      "economic_hash_8dec": "9b6a59c8c7ae8dd758ae10672a4413a87cb471c46fd0a0005d74bf0e44377091",
      "engine_metrics": {
        "total": 46,
        "total_winning_trades": 18,
        "total_losing_trades": 28,
        "starting_balance": 10000,
        "finishing_balance": 9471.946178064476,
        "win_rate": 0.391304347826087,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.4666666666666667,
        "ratio_avg_win_loss": 1.3709755420582006,
        "longs_count": 16,
        "longs_percentage": 34.78260869565217,
        "shorts_percentage": 65.21739130434783,
        "shorts_count": 30,
        "fee": 782.4942375242424,
        "net_profit": -528.0538219355211,
        "net_profit_percentage": -5.280538219355211,
        "average_win": 217.89673307130354,
        "average_loss": 158.9355363292494,
        "expectancy": -11.479430911641728,
        "expectancy_percentage": -0.11479430911641728,
        "expected_net_profit_every_100_trades": -11.479430911641728,
        "average_holding_period": 177281.73913043478,
        "average_winning_holding_period": 253870,
        "average_losing_holding_period": 128046.42857142857,
        "gross_profit": 3922.1411952834637,
        "gross_loss": -4450.195017218984,
        "max_drawdown": -27.816571716671625,
        "max_underwater_period": 231,
        "annual_return": -6.600206322576907,
        "annualization": 365,
        "sharpe_ratio": -0.31250732651784274,
        "calmar_ratio": -0.23727605219665263,
        "sortino_ratio": -0.4409284103945683,
        "omega_ratio": 0.9353594125258682,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -237.1798097676238,
        "largest_winning_trade": 945.4491149495406,
        "current_streak": -1,
        "avg_trades_per_day": 0.15859752287141965,
        "avg_trades_per_week": 1.1101826600999376,
        "avg_trades_per_month": 4.827708596206015
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 3,
      "calendar_months": 10,
      "positive_full_quarters": 1,
      "full_quarters": 3,
      "best_month": {
        "case": "K1001_B_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "K1001_B_F95",
        "month": "2026-07",
        "start_equity": 11496.743751937123,
        "end_equity": 9681.15857561043,
        "profit": -1815.5851763266928,
        "return_pct": -15.792168769707327,
        "partial": false
      },
      "best_trade": 945.4491149495406,
      "net_excluding_best_trade_arithmetic": -1473.5029368850614,
      "comparisons": {
        "K1001": {
          "delta_net": 0,
          "delta_return_pct": 0,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 46,
          "changed_exits": 0,
          "economic_identity_at_8dec": true
        },
        "N204": {
          "delta_net": 195.87051276548652,
          "delta_return_pct": 1.9587051276548655,
          "new_entries": 10,
          "removed_entries": 15,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1001_C_F95",
      "candidate": "K1001",
      "portfolio": "C",
      "cost": "F95",
      "net": 496.36637677866844,
      "balance": 10496.366376778666,
      "return_pct": 4.963663767786686,
      "dd_pct": -21.07491447059133,
      "pf": 1.1052735923916222,
      "trades": 47,
      "fees": 858.3715187051457,
      "sharpe": 0.4209520557996771,
      "max_underwater_days": 160,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2733.074464393587,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": true,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2147.098341903286,
          "fees": 626.5898400833771,
          "trades": 38
        },
        "PAXG-USDT": {
          "net": 1465.4443390659046,
          "fees": 200.25417727932796,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1178.0203796160488,
          "fees": 31.527501342440566,
          "trades": 1
        }
      },
      "economic_hash_8dec": "41a3c602eb2b496eb792b7d71449457ad3f6c968813784148f7c729179b1c911",
      "engine_metrics": {
        "total": 47,
        "total_winning_trades": 19,
        "total_losing_trades": 28,
        "starting_balance": 10000,
        "finishing_balance": 10496.366376778666,
        "win_rate": 0.40425531914893614,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.4666666666666667,
        "ratio_avg_win_loss": 1.6288242414192327,
        "longs_count": 17,
        "longs_percentage": 36.17021276595745,
        "shorts_percentage": 63.82978723404255,
        "shorts_count": 30,
        "fee": 858.3715187051457,
        "net_profit": 496.36637677866855,
        "net_profit_percentage": 4.963663767786686,
        "average_win": 274.2831351403526,
        "average_loss": 168.39332824600112,
        "expectancy": 10.560986739971668,
        "expectancy_percentage": 0.10560986739971667,
        "expected_net_profit_every_100_trades": 10.560986739971668,
        "average_holding_period": 231234.89361702127,
        "average_winning_holding_period": 383302.1052631579,
        "average_losing_holding_period": 128046.42857142857,
        "gross_profit": 5211.3795676667,
        "gross_loss": -4715.013190888031,
        "max_drawdown": -21.07491447059133,
        "max_underwater_period": 160,
        "annual_return": 6.286987324163573,
        "annualization": 365,
        "sharpe_ratio": 0.4209520557996771,
        "calmar_ratio": 0.2983161489426993,
        "sortino_ratio": 0.6146509775581037,
        "omega_ratio": 1.087906298917691,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -244.36309480563312,
        "largest_winning_trade": 1178.0203796160488,
        "current_streak": -1,
        "avg_trades_per_day": 0.16204529510775484,
        "avg_trades_per_week": 1.1343170657542838,
        "avg_trades_per_month": 4.932658783080058
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 5,
      "calendar_months": 10,
      "positive_full_quarters": 2,
      "full_quarters": 3,
      "best_month": {
        "case": "K1001_C_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "K1001_C_F95",
        "month": "2026-07",
        "start_equity": 12738.577210109337,
        "end_equity": 10727.625167132144,
        "profit": -2010.9520429771928,
        "return_pct": -15.786315926878402,
        "partial": false
      },
      "best_trade": 1178.0203796160488,
      "net_excluding_best_trade_arithmetic": -681.6540028373804,
      "comparisons": {
        "K1001": {
          "delta_net": 0,
          "delta_return_pct": 0,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 47,
          "changed_exits": 0,
          "economic_identity_at_8dec": true
        },
        "N204": {
          "delta_net": 218.30427907734781,
          "delta_return_pct": 2.183042790773483,
          "new_entries": 10,
          "removed_entries": 15,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1005_B_F95",
      "candidate": "K1005",
      "portfolio": "B",
      "cost": "F95",
      "net": -783.7242984371331,
      "balance": 9216.275701562863,
      "return_pct": -7.837242984371329,
      "dd_pct": -29.772904393195265,
      "pf": 0.8280243599537825,
      "trades": 47,
      "fees": 796.1236851350968,
      "sharpe": -0.5087185788609,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3809.5650273680076,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": false,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2242.2111494177375,
          "fees": 600.4433470922244,
          "trades": 39
        },
        "PAXG-USDT": {
          "net": 1458.4868509806033,
          "fees": 195.6803380428723,
          "trades": 8
        }
      },
      "economic_hash_8dec": "1dd8207ccc9c76e4e265cc620f968dc0548b31ef520d08d298f50fd1ee4079bd",
      "engine_metrics": {
        "total": 47,
        "total_winning_trades": 18,
        "total_losing_trades": 29,
        "starting_balance": 10000,
        "finishing_balance": 9216.275701562863,
        "win_rate": 0.3829787234042553,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.45161290322580644,
        "ratio_avg_win_loss": 1.3340392465922049,
        "longs_count": 16,
        "longs_percentage": 34.04255319148936,
        "shorts_percentage": 65.95744680851064,
        "shorts_count": 31,
        "fee": 796.1236851350967,
        "net_profit": -783.7242984371329,
        "net_profit_percentage": -7.837242984371329,
        "average_win": 209.63654129517505,
        "average_loss": 157.14420833621674,
        "expectancy": -16.674985073130514,
        "expectancy_percentage": -0.16674985073130516,
        "expected_net_profit_every_100_trades": -16.674985073130514,
        "average_holding_period": 173798.29787234042,
        "average_winning_holding_period": 252023.33333333334,
        "average_losing_holding_period": 125244.8275862069,
        "gross_profit": 3773.457743313151,
        "gross_loss": -4557.182041750285,
        "max_drawdown": -29.772904393195265,
        "max_underwater_period": 231,
        "annual_return": -9.762144420460695,
        "annualization": 365,
        "sharpe_ratio": -0.5087185788609,
        "calmar_ratio": -0.3278868696025463,
        "sortino_ratio": -0.713013228464799,
        "omega_ratio": 0.8980665059057852,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -237.1798097676238,
        "largest_winning_trade": 945.4491149495406,
        "current_streak": -1,
        "avg_trades_per_day": 0.16204529510775484,
        "avg_trades_per_week": 1.1343170657542838,
        "avg_trades_per_month": 4.932658783080058
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 3,
      "calendar_months": 10,
      "positive_full_quarters": 1,
      "full_quarters": 3,
      "best_month": {
        "case": "K1005_B_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "K1005_B_F95",
        "month": "2026-07",
        "start_equity": 11496.743751937123,
        "end_equity": 9681.15857561043,
        "profit": -1815.5851763266928,
        "return_pct": -15.792168769707327,
        "partial": false
      },
      "best_trade": 945.4491149495406,
      "net_excluding_best_trade_arithmetic": -1729.1734133866737,
      "comparisons": {
        "K1001": {
          "delta_net": -255.67047650161214,
          "delta_return_pct": -2.556704765016118,
          "new_entries": 1,
          "removed_entries": 0,
          "common_entries": 46,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -59.79996373612562,
          "delta_return_pct": -0.5979996373612524,
          "new_entries": 11,
          "removed_entries": 15,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1005_C_F95",
      "candidate": "K1005",
      "portfolio": "C",
      "cost": "F95",
      "net": 213.93152042607622,
      "balance": 10213.931520426078,
      "return_pct": 2.1393152042607633,
      "dd_pct": -23.20526774202203,
      "pf": 1.0442602439557807,
      "trades": 48,
      "fees": 873.5125848515003,
      "sharpe": 0.23539803085470457,
      "max_underwater_days": 160,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3009.346718518702,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": true,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2431.8083268513205,
          "fees": 643.3530151845731,
          "trades": 39
        },
        "PAXG-USDT": {
          "net": 1467.719467661348,
          "fees": 198.63206832448654,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1178.0203796160488,
          "fees": 31.527501342440566,
          "trades": 1
        }
      },
      "economic_hash_8dec": "5b73198f6c9d3ef66ca3e1eba269eeed25b97e3e95e3f3dd5dc080edd5f3b7e3",
      "engine_metrics": {
        "total": 48,
        "total_winning_trades": 19,
        "total_losing_trades": 29,
        "starting_balance": 10000,
        "finishing_balance": 10213.931520426078,
        "win_rate": 0.3958333333333333,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.45161290322580644,
        "ratio_avg_win_loss": 1.5938708986693495,
        "longs_count": 17,
        "longs_percentage": 35.41666666666667,
        "shorts_percentage": 64.58333333333333,
        "shorts_count": 31,
        "fee": 873.5125848515004,
        "net_profit": 213.9315204260763,
        "net_profit_percentage": 2.1393152042607633,
        "average_win": 265.65385207256213,
        "average_loss": 166.67212651560706,
        "expectancy": 4.456906675543223,
        "expectancy_percentage": 0.04456906675543223,
        "expected_net_profit_every_100_trades": 4.456906675543223,
        "average_holding_period": 226700,
        "average_winning_holding_period": 381552.63157894736,
        "average_losing_holding_period": 125244.8275862069,
        "gross_profit": 5047.42318937868,
        "gross_loss": -4833.491668952604,
        "max_drawdown": -23.20526774202203,
        "max_underwater_period": 160,
        "annual_return": 2.69999601278037,
        "annualization": 365,
        "sharpe_ratio": 0.23539803085470457,
        "calmar_ratio": 0.11635271968403074,
        "sortino_ratio": 0.34162934328860556,
        "omega_ratio": 1.047712869128608,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -244.36309480563312,
        "largest_winning_trade": 1178.0203796160488,
        "current_streak": -1,
        "avg_trades_per_day": 0.16549306734409006,
        "avg_trades_per_week": 1.1584514714086305,
        "avg_trades_per_month": 5.037608969954102
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 5,
      "calendar_months": 10,
      "positive_full_quarters": 2,
      "full_quarters": 3,
      "best_month": {
        "case": "K1005_C_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "K1005_C_F95",
        "month": "2026-07",
        "start_equity": 12738.577210109337,
        "end_equity": 10727.625167132144,
        "profit": -2010.9520429771928,
        "return_pct": -15.786315926878402,
        "partial": false
      },
      "best_trade": 1178.0203796160488,
      "net_excluding_best_trade_arithmetic": -964.0888591899726,
      "comparisons": {
        "K1001": {
          "delta_net": -282.4348563525922,
          "delta_return_pct": -2.824348563525923,
          "new_entries": 1,
          "removed_entries": 0,
          "common_entries": 47,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -64.1305772752444,
          "delta_return_pct": -0.6413057727524398,
          "new_entries": 11,
          "removed_entries": 15,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "N204_B_F95",
      "candidate": "N204",
      "portfolio": "B",
      "cost": "F95",
      "net": -723.9243347010075,
      "balance": 9276.075665298999,
      "return_pct": -7.239243347010077,
      "dd_pct": -29.460581815252162,
      "pf": 0.8562786949761125,
      "trades": 51,
      "fees": 864.9669828327998,
      "sharpe": -0.43833016500389194,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3769.6020746618724,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": false,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2183.0924632185315,
          "fees": 668.9730983691677,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1459.168128517523,
          "fees": 195.9938844636321,
          "trades": 8
        }
      },
      "economic_hash_8dec": "9793773336441bc61e38d48926ecacf992c761f44b66080e4c03b18c2e8bdbc3",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 20,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 9276.075665298999,
        "win_rate": 0.39215686274509803,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.3272319772129741,
        "longs_count": 16,
        "longs_percentage": 31.372549019607842,
        "shorts_percentage": 68.62745098039215,
        "shorts_count": 35,
        "fee": 864.9669828327997,
        "net_profit": -723.9243347010078,
        "net_profit_percentage": -7.239243347010077,
        "average_win": 215.65382546317718,
        "average_loss": 162.48389819240492,
        "expectancy": -14.194594798059,
        "expectancy_percentage": -0.14194594798059,
        "expected_net_profit_every_100_trades": -14.194594798058999,
        "average_holding_period": 166381.17647058822,
        "average_winning_holding_period": 241398,
        "average_losing_holding_period": 117983.2258064516,
        "gross_profit": 4313.076509263544,
        "gross_loss": -5037.000843964553,
        "max_drawdown": -29.460581815252162,
        "max_underwater_period": 231,
        "annual_return": -9.02459224640978,
        "annualization": 365,
        "sharpe_ratio": -0.43833016500389194,
        "calmar_ratio": -0.3063276992628034,
        "sortino_ratio": -0.6229156501310296,
        "omega_ratio": 0.9142156724431502,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -237.3391618176238,
        "largest_winning_trade": 945.4491149495406,
        "current_streak": 4,
        "avg_trades_per_day": 0.17583638405309568,
        "avg_trades_per_week": 1.2308546883716698,
        "avg_trades_per_month": 5.352459530576232
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 4,
      "calendar_months": 10,
      "positive_full_quarters": 1,
      "full_quarters": 3,
      "best_month": {
        "case": "N204_B_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "N204_B_F95",
        "month": "2026-07",
        "start_equity": 11563.629744258766,
        "end_equity": 9783.271189713414,
        "profit": -1780.3585545453516,
        "return_pct": -15.396191281801308,
        "partial": false
      },
      "best_trade": 945.4491149495406,
      "net_excluding_best_trade_arithmetic": -1669.373449650548,
      "comparisons": {
        "K1001": {
          "delta_net": -195.87051276548652,
          "delta_return_pct": -1.9587051276548655,
          "new_entries": 15,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 0,
          "delta_return_pct": 0,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 51,
          "changed_exits": 0,
          "economic_identity_at_8dec": true
        }
      }
    },
    {
      "case": "N204_C_F95",
      "candidate": "N204",
      "portfolio": "C",
      "cost": "F95",
      "net": 278.0620977013206,
      "balance": 10278.06209770132,
      "return_pct": 2.780620977013203,
      "dd_pct": -22.479847019838083,
      "pf": 1.0520379640946433,
      "trades": 52,
      "fees": 948.3694988677561,
      "sharpe": 0.2747696541047526,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2900.2157198508266,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": null,
      "stress_positive": true,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2361.314890140681,
          "fees": 717.9468682909984,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1467.8016428277388,
          "fees": 199.0676184718346,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1171.5753450142636,
          "fees": 31.35501210492323,
          "trades": 1
        }
      },
      "economic_hash_8dec": "44001d144cfbe9bd679376b952a41a0f7b0a6944f6f9747e7969d118c2fcc109",
      "engine_metrics": {
        "total": 52,
        "total_winning_trades": 21,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 10278.06209770132,
        "win_rate": 0.40384615384615385,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.5530084231873305,
        "longs_count": 17,
        "longs_percentage": 32.69230769230769,
        "shorts_percentage": 67.3076923076923,
        "shorts_count": 35,
        "fee": 948.3694988677561,
        "net_profit": 278.0620977013203,
        "net_profit_percentage": 2.780620977013203,
        "average_win": 267.6909044488263,
        "average_loss": 172.36925470077523,
        "expectancy": 5.347348032717704,
        "expectancy_percentage": 0.05347348032717704,
        "expected_net_profit_every_100_trades": 5.347348032717704,
        "average_holding_period": 215356.15384615384,
        "average_winning_holding_period": 359097.14285714284,
        "average_losing_holding_period": 117983.2258064516,
        "gross_profit": 5621.508993425352,
        "gross_loss": -5343.446895724032,
        "max_drawdown": -22.479847019838083,
        "max_underwater_period": 105,
        "annual_return": 3.5122454490292387,
        "annualization": 365,
        "sharpe_ratio": 0.2747696541047526,
        "calmar_ratio": 0.1562397397958154,
        "sortino_ratio": 0.40291768548070755,
        "omega_ratio": 1.0543081574959314,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -245.94986814853021,
        "largest_winning_trade": 1171.5753450142636,
        "current_streak": 4,
        "avg_trades_per_day": 0.1792841562894309,
        "avg_trades_per_week": 1.2549890940260162,
        "avg_trades_per_month": 5.457409717450277
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 6,
      "calendar_months": 10,
      "positive_full_quarters": 2,
      "full_quarters": 3,
      "best_month": {
        "case": "N204_C_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "N204_C_F95",
        "month": "2026-07",
        "start_equity": 12811.893274571721,
        "end_equity": 10838.53994870752,
        "profit": -1973.353325864202,
        "return_pct": -15.402511428820564,
        "partial": false
      },
      "best_trade": 1171.5753450142636,
      "net_excluding_best_trade_arithmetic": -893.5132473129429,
      "comparisons": {
        "K1001": {
          "delta_net": -218.30427907734781,
          "delta_return_pct": -2.183042790773483,
          "new_entries": 15,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 0,
          "delta_return_pct": 0,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 52,
          "changed_exits": 0,
          "economic_identity_at_8dec": true
        }
      }
    }
  ],
  "monthly": [
    {
      "case": "C504_B_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 11600.829902885494,
      "profit": -528.3340655078136,
      "return_pct": -4.355898451736406,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-05",
      "start_equity": 11600.829902885494,
      "end_equity": 11287.359425592991,
      "profit": -313.47047729250335,
      "return_pct": -2.702138380759578,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-06",
      "start_equity": 11287.359425592991,
      "end_equity": 11563.629744258766,
      "profit": 276.27031866577454,
      "return_pct": 2.447608056489803,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-07",
      "start_equity": 11563.629744258766,
      "end_equity": 9722.365773183414,
      "profit": -1841.263971075352,
      "return_pct": -15.922889367756888,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-08",
      "start_equity": 9722.365773183414,
      "end_equity": 9284.326560174452,
      "profit": -438.0392130089622,
      "return_pct": -4.505479666452972,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-09",
      "start_equity": 9284.326560174452,
      "end_equity": 9133.524172717665,
      "profit": -150.80238745678616,
      "return_pct": -1.6242684537148833,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "month": "2026-10",
      "start_equity": 9133.524172717665,
      "end_equity": 9220.388648376398,
      "profit": 86.86447565873277,
      "return_pct": 0.9510510293299745,
      "partial": true
    },
    {
      "case": "C504_C_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 12368.676244352664,
      "profit": 239.51227595935597,
      "return_pct": 1.974680831947584,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-05",
      "start_equity": 12368.676244352664,
      "end_equity": 12504.493905915435,
      "profit": 135.8176615627708,
      "return_pct": 1.0980775863123071,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-06",
      "start_equity": 12504.493905915435,
      "end_equity": 12811.893274571721,
      "profit": 307.39936865628624,
      "return_pct": 2.4583111557267223,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-07",
      "start_equity": 12811.893274571721,
      "end_equity": 10770.853796592522,
      "profit": -2041.0394779791986,
      "return_pct": -15.930818609222507,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-08",
      "start_equity": 10770.853796592522,
      "end_equity": 10286.176878368806,
      "profit": -484.6769182237167,
      "return_pct": -4.499893206024663,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-09",
      "start_equity": 10286.176878368806,
      "end_equity": 10119.522698520494,
      "profit": -166.6541798483122,
      "return_pct": -1.6201761044842167,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "month": "2026-10",
      "start_equity": 10119.522698520494,
      "end_equity": 10215.742299014035,
      "profit": 96.2196004935413,
      "return_pct": 0.9508314113234606,
      "partial": true
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12196.347523526945,
      "profit": -551.915197608223,
      "return_pct": -4.329336551036167,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-04",
      "start_equity": 12196.347523526945,
      "end_equity": 11663.62307978712,
      "profit": -532.7244437398258,
      "return_pct": -4.36790147798094,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-05",
      "start_equity": 11663.62307978712,
      "end_equity": 11496.743751937123,
      "profit": -166.87932784999612,
      "return_pct": -1.4307674957294791,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-06",
      "start_equity": 11496.743751937123,
      "end_equity": 11496.743751937123,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-07",
      "start_equity": 11496.743751937123,
      "end_equity": 9681.15857561043,
      "profit": -1815.5851763266928,
      "return_pct": -15.792168769707327,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-08",
      "start_equity": 9681.15857561043,
      "end_equity": 9502.17205193736,
      "profit": -178.98652367307113,
      "return_pct": -1.8488130555364357,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-09",
      "start_equity": 9502.17205193736,
      "end_equity": 9361.70908335613,
      "profit": -140.46296858122878,
      "return_pct": -1.4782195882528826,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "month": "2026-10",
      "start_equity": 9361.70908335613,
      "end_equity": 9471.946178064476,
      "profit": 110.23709470834547,
      "return_pct": 1.1775317276663921,
      "partial": true
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12196.347523526945,
      "profit": -551.915197608223,
      "return_pct": -4.329336551036167,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-04",
      "start_equity": 12196.347523526945,
      "end_equity": 12435.693474159352,
      "profit": 239.34595063240704,
      "return_pct": 1.9624395760345914,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-05",
      "start_equity": 12435.693474159352,
      "end_equity": 12738.577210109337,
      "profit": 302.88373594998484,
      "return_pct": 2.435599884955031,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-06",
      "start_equity": 12738.577210109337,
      "end_equity": 12738.577210109337,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-07",
      "start_equity": 12738.577210109337,
      "end_equity": 10727.625167132144,
      "profit": -2010.9520429771928,
      "return_pct": -15.786315926878402,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-08",
      "start_equity": 10727.625167132144,
      "end_equity": 10528.52543744716,
      "profit": -199.09972968498369,
      "return_pct": -1.855953452726855,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-09",
      "start_equity": 10528.52543744716,
      "end_equity": 10374.642922769548,
      "profit": -153.88251467761256,
      "return_pct": -1.461577080208154,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "month": "2026-10",
      "start_equity": 10374.642922769548,
      "end_equity": 10496.366376778666,
      "profit": 121.72345400911763,
      "return_pct": 1.1732784917538375,
      "partial": true
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12196.347523526945,
      "profit": -551.915197608223,
      "return_pct": -4.329336551036167,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-04",
      "start_equity": 12196.347523526945,
      "end_equity": 11663.62307978712,
      "profit": -532.7244437398258,
      "return_pct": -4.36790147798094,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-05",
      "start_equity": 11663.62307978712,
      "end_equity": 11496.743751937123,
      "profit": -166.87932784999612,
      "return_pct": -1.4307674957294791,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-06",
      "start_equity": 11496.743751937123,
      "end_equity": 11496.743751937123,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-07",
      "start_equity": 11496.743751937123,
      "end_equity": 9681.15857561043,
      "profit": -1815.5851763266928,
      "return_pct": -15.792168769707327,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-08",
      "start_equity": 9681.15857561043,
      "end_equity": 9244.314679938101,
      "profit": -436.8438956723294,
      "return_pct": -4.512310094505246,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-09",
      "start_equity": 9244.314679938101,
      "end_equity": 9107.249498050454,
      "profit": -137.06518188764676,
      "return_pct": -1.4826970590378519,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "month": "2026-10",
      "start_equity": 9107.249498050454,
      "end_equity": 9216.275701562863,
      "profit": 109.02620351240876,
      "return_pct": 1.197136451963332,
      "partial": true
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12196.347523526945,
      "profit": -551.915197608223,
      "return_pct": -4.329336551036167,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-04",
      "start_equity": 12196.347523526945,
      "end_equity": 12435.693474159352,
      "profit": 239.34595063240704,
      "return_pct": 1.9624395760345914,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-05",
      "start_equity": 12435.693474159352,
      "end_equity": 12738.577210109337,
      "profit": 302.88373594998484,
      "return_pct": 2.435599884955031,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-06",
      "start_equity": 12738.577210109337,
      "end_equity": 12738.577210109337,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-07",
      "start_equity": 12738.577210109337,
      "end_equity": 10727.625167132144,
      "profit": -2010.9520429771928,
      "return_pct": -15.786315926878402,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-08",
      "start_equity": 10727.625167132144,
      "end_equity": 10244.730144665938,
      "profit": -482.8950224662058,
      "return_pct": -4.501415876700509,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-09",
      "start_equity": 10244.730144665938,
      "end_equity": 10094.23185983932,
      "profit": -150.49828482661906,
      "return_pct": -1.4690312258247018,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "month": "2026-10",
      "start_equity": 10094.23185983932,
      "end_equity": 10213.931520426078,
      "profit": 119.69966058675891,
      "return_pct": 1.1858223810272683,
      "partial": true
    },
    {
      "case": "N204_B_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 11600.829902885494,
      "profit": -528.3340655078136,
      "return_pct": -4.355898451736406,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-05",
      "start_equity": 11600.829902885494,
      "end_equity": 11287.359425592991,
      "profit": -313.47047729250335,
      "return_pct": -2.702138380759578,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-06",
      "start_equity": 11287.359425592991,
      "end_equity": 11563.629744258766,
      "profit": 276.27031866577454,
      "return_pct": 2.447608056489803,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-07",
      "start_equity": 11563.629744258766,
      "end_equity": 9783.271189713414,
      "profit": -1780.3585545453516,
      "return_pct": -15.396191281801308,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-08",
      "start_equity": 9783.271189713414,
      "end_equity": 9341.798005805222,
      "profit": -441.47318390819237,
      "return_pct": -4.512531395147034,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-09",
      "start_equity": 9341.798005805222,
      "end_equity": 9189.510840080362,
      "profit": -152.28716572485973,
      "return_pct": -1.630169755653299,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "month": "2026-10",
      "start_equity": 9189.510840080362,
      "end_equity": 9276.075665298999,
      "profit": 86.56482521863654,
      "return_pct": 0.9419960074597444,
      "partial": true
    },
    {
      "case": "N204_C_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 12368.676244352664,
      "profit": 239.51227595935597,
      "return_pct": 1.974680831947584,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-05",
      "start_equity": 12368.676244352664,
      "end_equity": 12504.493905915435,
      "profit": 135.8176615627708,
      "return_pct": 1.0980775863123071,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-06",
      "start_equity": 12504.493905915435,
      "end_equity": 12811.893274571721,
      "profit": 307.39936865628624,
      "return_pct": 2.4583111557267223,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-07",
      "start_equity": 12811.893274571721,
      "end_equity": 10838.53994870752,
      "profit": -1973.353325864202,
      "return_pct": -15.402511428820564,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-08",
      "start_equity": 10838.53994870752,
      "end_equity": 10350.318065708132,
      "profit": -488.22188299938716,
      "return_pct": -4.504498625367037,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-09",
      "start_equity": 10350.318065708132,
      "end_equity": 10183.080275684297,
      "profit": -167.23779002383526,
      "return_pct": -1.6157744038602484,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "month": "2026-10",
      "start_equity": 10183.080275684297,
      "end_equity": 10278.06209770132,
      "profit": 94.98182201702366,
      "return_pct": 0.9327415619400092,
      "partial": true
    }
  ],
  "quarterly": [
    {
      "case": "C504_B_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 11563.629744258766,
      "profit": -565.5342241345425,
      "return_pct": -4.662598556736763,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "quarter": "2026Q3",
      "start_equity": 11563.629744258766,
      "end_equity": 9133.524172717665,
      "profit": -2430.1055715411003,
      "return_pct": -21.01507593450599,
      "partial": false
    },
    {
      "case": "C504_B_F95",
      "quarter": "2026Q4",
      "start_equity": 9133.524172717665,
      "end_equity": 9220.388648376398,
      "profit": 86.86447565873277,
      "return_pct": 0.9510510293299745,
      "partial": true
    },
    {
      "case": "C504_C_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 12811.893274571721,
      "profit": 682.729306178413,
      "return_pct": 5.6288241131664085,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "quarter": "2026Q3",
      "start_equity": 12811.893274571721,
      "end_equity": 10119.522698520494,
      "profit": -2692.3705760512275,
      "return_pct": -21.014619138257128,
      "partial": false
    },
    {
      "case": "C504_C_F95",
      "quarter": "2026Q4",
      "start_equity": 10119.522698520494,
      "end_equity": 10215.742299014035,
      "profit": 96.2196004935413,
      "return_pct": 0.9508314113234606,
      "partial": true
    },
    {
      "case": "K1001_B_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12196.347523526945,
      "profit": 2196.347523526945,
      "return_pct": 21.96347523526945,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "quarter": "2026Q2",
      "start_equity": 12196.347523526945,
      "end_equity": 11496.743751937123,
      "profit": -699.6037715898219,
      "return_pct": -5.7361744591179935,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "quarter": "2026Q3",
      "start_equity": 11496.743751937123,
      "end_equity": 9361.70908335613,
      "profit": -2135.0346685809927,
      "return_pct": -18.570777210036137,
      "partial": false
    },
    {
      "case": "K1001_B_F95",
      "quarter": "2026Q4",
      "start_equity": 9361.70908335613,
      "end_equity": 9471.946178064476,
      "profit": 110.23709470834547,
      "return_pct": 1.1775317276663921,
      "partial": true
    },
    {
      "case": "K1001_C_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12196.347523526945,
      "profit": 2196.347523526945,
      "return_pct": 21.96347523526945,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "quarter": "2026Q2",
      "start_equity": 12196.347523526945,
      "end_equity": 12738.577210109337,
      "profit": 542.2296865823919,
      "return_pct": 4.44583663704583,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "quarter": "2026Q3",
      "start_equity": 12738.577210109337,
      "end_equity": 10374.642922769548,
      "profit": -2363.934287339789,
      "return_pct": -18.557286644726467,
      "partial": false
    },
    {
      "case": "K1001_C_F95",
      "quarter": "2026Q4",
      "start_equity": 10374.642922769548,
      "end_equity": 10496.366376778666,
      "profit": 121.72345400911763,
      "return_pct": 1.1732784917538375,
      "partial": true
    },
    {
      "case": "K1005_B_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12196.347523526945,
      "profit": 2196.347523526945,
      "return_pct": 21.96347523526945,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "quarter": "2026Q2",
      "start_equity": 12196.347523526945,
      "end_equity": 11496.743751937123,
      "profit": -699.6037715898219,
      "return_pct": -5.7361744591179935,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "quarter": "2026Q3",
      "start_equity": 11496.743751937123,
      "end_equity": 9107.249498050454,
      "profit": -2389.494253886669,
      "return_pct": -20.78409596181575,
      "partial": false
    },
    {
      "case": "K1005_B_F95",
      "quarter": "2026Q4",
      "start_equity": 9107.249498050454,
      "end_equity": 9216.275701562863,
      "profit": 109.02620351240876,
      "return_pct": 1.197136451963332,
      "partial": true
    },
    {
      "case": "K1005_C_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12196.347523526945,
      "profit": 2196.347523526945,
      "return_pct": 21.96347523526945,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "quarter": "2026Q2",
      "start_equity": 12196.347523526945,
      "end_equity": 12738.577210109337,
      "profit": 542.2296865823919,
      "return_pct": 4.44583663704583,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "quarter": "2026Q3",
      "start_equity": 12738.577210109337,
      "end_equity": 10094.23185983932,
      "profit": -2644.3453502700177,
      "return_pct": -20.75856123218741,
      "partial": false
    },
    {
      "case": "K1005_C_F95",
      "quarter": "2026Q4",
      "start_equity": 10094.23185983932,
      "end_equity": 10213.931520426078,
      "profit": 119.69966058675891,
      "return_pct": 1.1858223810272683,
      "partial": true
    },
    {
      "case": "N204_B_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 11563.629744258766,
      "profit": -565.5342241345425,
      "return_pct": -4.662598556736763,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "quarter": "2026Q3",
      "start_equity": 11563.629744258766,
      "end_equity": 9189.510840080362,
      "profit": -2374.1189041784037,
      "return_pct": -20.530914225761432,
      "partial": false
    },
    {
      "case": "N204_B_F95",
      "quarter": "2026Q4",
      "start_equity": 9189.510840080362,
      "end_equity": 9276.075665298999,
      "profit": 86.56482521863654,
      "return_pct": 0.9419960074597444,
      "partial": true
    },
    {
      "case": "N204_C_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 12811.893274571721,
      "profit": 682.729306178413,
      "return_pct": 5.6288241131664085,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "quarter": "2026Q3",
      "start_equity": 12811.893274571721,
      "end_equity": 10183.080275684297,
      "profit": -2628.8129988874243,
      "return_pct": -20.51853650783163,
      "partial": false
    },
    {
      "case": "N204_C_F95",
      "quarter": "2026Q4",
      "start_equity": 10183.080275684297,
      "end_equity": 10278.06209770132,
      "profit": 94.98182201702366,
      "return_pct": 0.9327415619400092,
      "partial": true
    }
  ]
}
```
