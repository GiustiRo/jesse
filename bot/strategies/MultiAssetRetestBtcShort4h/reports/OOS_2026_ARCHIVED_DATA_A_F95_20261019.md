# Comparación ampliada2026 — datos A_F95

Análisis ff681776a3f044f886025a9fb6c7f27b succeeded. Incluye referencias repetidas sólo para comparación; no contarlas como corridas nuevas ni muestrasindependientes. Cada JSON contiene métricasmotor completas, puertas, contribución por activo, meses/Q y comparaciones de firmas. Mismos datoscorregidos delprotocolo y fuentescongeladas.

```json
{
  "rows": [
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
    },
    {
      "case": "N503_B_F95",
      "candidate": "N503",
      "portfolio": "B",
      "cost": "F95",
      "net": -630.5454238506136,
      "balance": 9369.454576149394,
      "return_pct": -6.305454238506138,
      "dd_pct": -28.753248901269725,
      "pf": 0.8726776058992074,
      "trades": 50,
      "fees": 845.7966466231055,
      "sharpe": -0.36905379083983025,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3679.0959320220045,
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
          "net": -2088.2242552230064,
          "fees": 649.1806362477453,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1457.6788313723926,
          "fees": 196.61601037536036,
          "trades": 8
        }
      },
      "economic_hash_8dec": "fc1b09f773ea058d3166e97a461f285384c0fa49b34e62a9260e2a0a588edc3d",
      "engine_metrics": {
        "total": 50,
        "total_winning_trades": 20,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 9369.454576149394,
        "win_rate": 0.4,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.3090164088488112,
        "longs_count": 16,
        "longs_percentage": 32,
        "shorts_percentage": 68,
        "shorts_count": 34,
        "fee": 845.7966466231055,
        "net_profit": -630.5454238506137,
        "net_profit_percentage": -6.305454238506138,
        "average_win": 216.09037231150714,
        "average_loss": 165.07842900269185,
        "expectancy": -12.610908477012245,
        "expectancy_percentage": -0.12610908477012245,
        "expected_net_profit_every_100_trades": -12.610908477012245,
        "average_holding_period": 169011.6,
        "average_winning_holding_period": 241398,
        "average_losing_holding_period": 120754,
        "gross_profit": 4321.807446230143,
        "gross_loss": -4952.352870080756,
        "max_drawdown": -28.753248901269725,
        "max_underwater_period": 231,
        "annual_return": -7.870429737286844,
        "annualization": 365,
        "sharpe_ratio": -0.36905379083983025,
        "calmar_ratio": -0.2737231456630034,
        "sortino_ratio": -0.5255526401256017,
        "omega_ratio": 0.9269088651439494,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -237.3391618176238,
        "largest_winning_trade": 945.4491149495406,
        "current_streak": 4,
        "avg_trades_per_day": 0.1723886118167605,
        "avg_trades_per_week": 1.2067202827173233,
        "avg_trades_per_month": 5.247509343702189
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 4,
      "calendar_months": 10,
      "positive_full_quarters": 1,
      "full_quarters": 3,
      "best_month": {
        "case": "N503_B_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "N503_B_F95",
        "month": "2026-07",
        "start_equity": 11563.629744258766,
        "end_equity": 9783.271189713414,
        "profit": -1780.3585545453516,
        "return_pct": -15.396191281801308,
        "partial": false
      },
      "best_trade": 945.4491149495406,
      "net_excluding_best_trade_arithmetic": -1575.9945388001543,
      "comparisons": {
        "K1001": {
          "delta_net": -102.49160191509259,
          "delta_return_pct": -1.0249160191509263,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 93.37891085039394,
          "delta_return_pct": 0.9337891085039391,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 50,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "N503_C_F95",
      "candidate": "N503",
      "portfolio": "C",
      "cost": "F95",
      "net": 379.05107409606154,
      "balance": 10379.05107409606,
      "return_pct": 3.7905107409606136,
      "dd_pct": -21.720309624733826,
      "pf": 1.0721802794144868,
      "trades": 51,
      "fees": 927.3736801021305,
      "sharpe": 0.3389323220960393,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2802.2247374766102,
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
          "net": -2258.6746151548055,
          "fees": 696.2616745618191,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1466.1503442366034,
          "fees": 199.7569934353884,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1171.5753450142636,
          "fees": 31.35501210492323,
          "trades": 1
        }
      },
      "economic_hash_8dec": "3799344c0725ee0069e9b9c2d5ef8d4bd6c327dc9dc0725488e8ad9603551811",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 21,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 10379.05107409606,
        "win_rate": 0.4117647058823529,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.5316861134492665,
        "longs_count": 17,
        "longs_percentage": 33.33333333333333,
        "shorts_percentage": 66.66666666666667,
        "shorts_count": 34,
        "fee": 927.3736801021307,
        "net_profit": 379.0510740960613,
        "net_profit_percentage": 3.7905107409606136,
        "average_win": 268.1190629862635,
        "average_loss": 175.04830828718244,
        "expectancy": 7.432374001883517,
        "expectancy_percentage": 0.07432374001883517,
        "expected_net_profit_every_100_trades": 7.432374001883517,
        "average_holding_period": 218895.29411764705,
        "average_winning_holding_period": 359097.14285714284,
        "average_losing_holding_period": 120754,
        "gross_profit": 5630.500322711533,
        "gross_loss": -5251.449248615473,
        "max_drawdown": -21.720309624733826,
        "max_underwater_period": 105,
        "annual_return": 4.793983993912088,
        "annualization": 365,
        "sharpe_ratio": 0.3389323220960393,
        "calmar_ratio": 0.22071434877028537,
        "sortino_ratio": 0.4978944658208374,
        "omega_ratio": 1.0677251018694704,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -245.94986814853021,
        "largest_winning_trade": 1171.5753450142636,
        "current_streak": 4,
        "avg_trades_per_day": 0.17583638405309568,
        "avg_trades_per_week": 1.2308546883716698,
        "avg_trades_per_month": 5.352459530576232
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 6,
      "calendar_months": 10,
      "positive_full_quarters": 2,
      "full_quarters": 3,
      "best_month": {
        "case": "N503_C_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "N503_C_F95",
        "month": "2026-07",
        "start_equity": 12811.893274571721,
        "end_equity": 10838.53994870752,
        "profit": -1973.353325864202,
        "return_pct": -15.402511428820564,
        "partial": false
      },
      "best_trade": 1171.5753450142636,
      "net_excluding_best_trade_arithmetic": -792.5242709182021,
      "comparisons": {
        "K1001": {
          "delta_net": -117.3153026826069,
          "delta_return_pct": -1.1731530268260726,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 100.98897639474092,
          "delta_return_pct": 1.0098897639474105,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 51,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "P604_B_F95",
      "candidate": "P604",
      "portfolio": "B",
      "cost": "F95",
      "net": -651.3213747292556,
      "balance": 9348.678625270748,
      "return_pct": -6.513213747292558,
      "dd_pct": -28.915619249260615,
      "pf": 0.8686093544462422,
      "trades": 50,
      "fees": 846.456171117054,
      "sharpe": -0.38456079099898666,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3699.8718829006502,
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
          "net": -2105.3016024428853,
          "fees": 649.4128805655023,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1453.98022771363,
          "fees": 197.0432905515519,
          "trades": 8
        }
      },
      "economic_hash_8dec": "bf902c6a4ff265409dc9460cf0a36ce06753e241cb2e2ad33f3731f2d22f2da9",
      "engine_metrics": {
        "total": 50,
        "total_winning_trades": 20,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 9348.678625270748,
        "win_rate": 0.4,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.3029140316693637,
        "longs_count": 16,
        "longs_percentage": 32,
        "shorts_percentage": 68,
        "shorts_count": 34,
        "fee": 846.456171117054,
        "net_profit": -651.3213747292558,
        "net_profit_percentage": -6.513213747292558,
        "average_win": 215.2907600294675,
        "average_loss": 165.23788584395348,
        "expectancy": -13.026427494585079,
        "expectancy_percentage": -0.1302642749458508,
        "expected_net_profit_every_100_trades": -13.02642749458508,
        "average_holding_period": 164713.2,
        "average_winning_holding_period": 230652,
        "average_losing_holding_period": 120754,
        "gross_profit": 4305.81520058935,
        "gross_loss": -4957.136575318605,
        "max_drawdown": -28.915619249260615,
        "max_underwater_period": 231,
        "annual_return": -8.127478725262039,
        "annualization": 365,
        "sharpe_ratio": -0.38456079099898666,
        "calmar_ratio": -0.28107572779959955,
        "sortino_ratio": -0.5473006263342922,
        "omega_ratio": 0.9239351363082948,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -237.3391618176238,
        "largest_winning_trade": 945.4491149495406,
        "current_streak": 4,
        "avg_trades_per_day": 0.1723886118167605,
        "avg_trades_per_week": 1.2067202827173233,
        "avg_trades_per_month": 5.247509343702189
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 4,
      "calendar_months": 10,
      "positive_full_quarters": 1,
      "full_quarters": 3,
      "best_month": {
        "case": "P604_B_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "P604_B_F95",
        "month": "2026-07",
        "start_equity": 11563.629744258766,
        "end_equity": 9801.272323563413,
        "profit": -1762.3574206953526,
        "return_pct": -15.24052101002582,
        "partial": false
      },
      "best_trade": 945.4491149495406,
      "net_excluding_best_trade_arithmetic": -1596.7704896787961,
      "comparisons": {
        "K1001": {
          "delta_net": -123.26755279373458,
          "delta_return_pct": -1.2326755279373467,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 72.60295997175194,
          "delta_return_pct": 0.7260295997175188,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 50,
          "changed_exits": 2,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "P604_C_F95",
      "candidate": "P604",
      "portfolio": "C",
      "cost": "F95",
      "net": 356.1596161624322,
      "balance": 10356.15961616243,
      "return_pct": 3.56159616162432,
      "dd_pct": -21.897743485562472,
      "pf": 1.0677614231968475,
      "trades": 51,
      "fees": 928.0387042887968,
      "sharpe": 0.32445530918748655,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2825.116195410241,
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
          "net": -2277.4735525732967,
          "fees": 696.460070576311,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1462.0578237214654,
          "fees": 200.22362160756256,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1171.5753450142636,
          "fees": 31.35501210492323,
          "trades": 1
        }
      },
      "economic_hash_8dec": "0d1a198dfcb4bf5b9d9755c583d612297ddc69b419b22441f35636e41b642d34",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 21,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 10356.15961616243,
        "win_rate": 0.4117647058823529,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.525373461709782,
        "longs_count": 17,
        "longs_percentage": 33.33333333333333,
        "shorts_percentage": 66.66666666666667,
        "shorts_count": 34,
        "fee": 928.0387042887969,
        "net_profit": 356.159616162432,
        "net_profit_percentage": 3.56159616162432,
        "average_win": 267.24961440508355,
        "average_loss": 175.2027428781441,
        "expectancy": 6.9835218855378685,
        "expectancy_percentage": 0.06983521885537868,
        "expected_net_profit_every_100_trades": 6.983521885537868,
        "average_holding_period": 214681.17647058822,
        "average_winning_holding_period": 348862.85714285716,
        "average_losing_holding_period": 120754,
        "gross_profit": 5612.241902506755,
        "gross_loss": -5256.082286344324,
        "max_drawdown": -21.897743485562472,
        "max_underwater_period": 105,
        "annual_return": 4.503164793320513,
        "annualization": 365,
        "sharpe_ratio": 0.32445530918748655,
        "calmar_ratio": 0.20564515226372623,
        "sortino_ratio": 0.47637094841317784,
        "omega_ratio": 1.0647558975927087,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -245.94986814853021,
        "largest_winning_trade": 1171.5753450142636,
        "current_streak": 4,
        "avg_trades_per_day": 0.17583638405309568,
        "avg_trades_per_week": 1.2308546883716698,
        "avg_trades_per_month": 5.352459530576232
      },
      "first_equity_date": "2026-01-01T23:00:00+00:00",
      "last_equity_date": "2026-10-19T00:00:00+00:00",
      "positive_months": 6,
      "calendar_months": 10,
      "positive_full_quarters": 2,
      "full_quarters": 3,
      "best_month": {
        "case": "P604_C_F95",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12072.209439475968,
        "profit": 2072.209439475968,
        "return_pct": 20.722094394759672,
        "partial": false
      },
      "worst_month": {
        "case": "P604_C_F95",
        "month": "2026-07",
        "start_equity": 12811.893274571721,
        "end_equity": 10858.426915627517,
        "profit": -1953.4663589442043,
        "return_pct": -15.247288726806108,
        "partial": false
      },
      "best_trade": 1171.5753450142636,
      "net_excluding_best_trade_arithmetic": -815.4157288518313,
      "comparisons": {
        "K1001": {
          "delta_net": -140.20676061623624,
          "delta_return_pct": -1.4020676061623663,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 78.09751846111158,
          "delta_return_pct": 0.7809751846111168,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 51,
          "changed_exits": 2,
          "economic_identity_at_8dec": false
        }
      }
    }
  ],
  "monthly": [
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
    },
    {
      "case": "N503_B_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 11600.829902885494,
      "profit": -528.3340655078136,
      "return_pct": -4.355898451736406,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-05",
      "start_equity": 11600.829902885494,
      "end_equity": 11287.359425592991,
      "profit": -313.47047729250335,
      "return_pct": -2.702138380759578,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-06",
      "start_equity": 11287.359425592991,
      "end_equity": 11563.629744258766,
      "profit": 276.27031866577454,
      "return_pct": 2.447608056489803,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-07",
      "start_equity": 11563.629744258766,
      "end_equity": 9783.271189713414,
      "profit": -1780.3585545453516,
      "return_pct": -15.396191281801308,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-08",
      "start_equity": 9783.271189713414,
      "end_equity": 9431.589997747305,
      "profit": -351.6811919661086,
      "return_pct": -3.5947198554189375,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-09",
      "start_equity": 9431.589997747305,
      "end_equity": 9280.01698272023,
      "profit": -151.5730150270756,
      "return_pct": -1.6070780755236158,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "month": "2026-10",
      "start_equity": 9280.01698272023,
      "end_equity": 9369.454576149394,
      "profit": 89.43759342916383,
      "return_pct": 0.9637654068489265,
      "partial": true
    },
    {
      "case": "N503_C_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 12368.676244352664,
      "profit": 239.51227595935597,
      "return_pct": 1.974680831947584,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-05",
      "start_equity": 12368.676244352664,
      "end_equity": 12504.493905915435,
      "profit": 135.8176615627708,
      "return_pct": 1.0980775863123071,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-06",
      "start_equity": 12504.493905915435,
      "end_equity": 12811.893274571721,
      "profit": 307.39936865628624,
      "return_pct": 2.4583111557267223,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-07",
      "start_equity": 12811.893274571721,
      "end_equity": 10838.53994870752,
      "profit": -1973.353325864202,
      "return_pct": -15.402511428820564,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-08",
      "start_equity": 10838.53994870752,
      "end_equity": 10449.873339679567,
      "profit": -388.6666090279523,
      "return_pct": -3.5859683210772375,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-09",
      "start_equity": 10449.873339679567,
      "end_equity": 10281.071258058513,
      "profit": -168.80208162105373,
      "return_pct": -1.6153505036284987,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "month": "2026-10",
      "start_equity": 10281.071258058513,
      "end_equity": 10379.05107409606,
      "profit": 97.9798160375467,
      "return_pct": 0.9530117395183613,
      "partial": true
    },
    {
      "case": "P604_B_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 11600.829902885494,
      "profit": -528.3340655078136,
      "return_pct": -4.355898451736406,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-05",
      "start_equity": 11600.829902885494,
      "end_equity": 11287.359425592991,
      "profit": -313.47047729250335,
      "return_pct": -2.702138380759578,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-06",
      "start_equity": 11287.359425592991,
      "end_equity": 11563.629744258766,
      "profit": 276.27031866577454,
      "return_pct": 2.447608056489803,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-07",
      "start_equity": 11563.629744258766,
      "end_equity": 9801.272323563413,
      "profit": -1762.3574206953526,
      "return_pct": -15.24052101002582,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-08",
      "start_equity": 9801.272323563413,
      "end_equity": 9410.81404686866,
      "profit": -390.4582766947533,
      "return_pct": -3.9837509233984436,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-09",
      "start_equity": 9410.81404686866,
      "end_equity": 9259.241031841582,
      "profit": -151.57301502707742,
      "return_pct": -1.610625969997903,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "month": "2026-10",
      "start_equity": 9259.241031841582,
      "end_equity": 9348.678625270748,
      "profit": 89.43759342916564,
      "return_pct": 0.9659279105231011,
      "partial": true
    },
    {
      "case": "P604_C_F95",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12072.209439475968,
      "profit": 2072.209439475968,
      "return_pct": 20.722094394759672,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-02",
      "start_equity": 12072.209439475968,
      "end_equity": 12748.262721135168,
      "profit": 676.0532816592004,
      "return_pct": 5.600079132561397,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-03",
      "start_equity": 12748.262721135168,
      "end_equity": 12129.163968393308,
      "profit": -619.0987527418602,
      "return_pct": -4.856338202973065,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-04",
      "start_equity": 12129.163968393308,
      "end_equity": 12368.676244352664,
      "profit": 239.51227595935597,
      "return_pct": 1.974680831947584,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-05",
      "start_equity": 12368.676244352664,
      "end_equity": 12504.493905915435,
      "profit": 135.8176615627708,
      "return_pct": 1.0980775863123071,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-06",
      "start_equity": 12504.493905915435,
      "end_equity": 12811.893274571721,
      "profit": 307.39936865628624,
      "return_pct": 2.4583111557267223,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-07",
      "start_equity": 12811.893274571721,
      "end_equity": 10858.426915627517,
      "profit": -1953.4663589442043,
      "return_pct": -15.247288726806108,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-08",
      "start_equity": 10858.426915627517,
      "end_equity": 10425.673236805278,
      "profit": -432.7536788222387,
      "return_pct": -3.9854177974842475,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-09",
      "start_equity": 10425.673236805278,
      "end_equity": 10258.179800124883,
      "profit": -167.49343668039546,
      "return_pct": -1.606547921424406,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "month": "2026-10",
      "start_equity": 10258.179800124883,
      "end_equity": 10356.15961616243,
      "profit": 97.9798160375467,
      "return_pct": 0.9551384158460019,
      "partial": true
    }
  ],
  "quarterly": [
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
    },
    {
      "case": "N503_B_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 11563.629744258766,
      "profit": -565.5342241345425,
      "return_pct": -4.662598556736763,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "quarter": "2026Q3",
      "start_equity": 11563.629744258766,
      "end_equity": 9280.01698272023,
      "profit": -2283.612761538536,
      "return_pct": -19.7482348712551,
      "partial": false
    },
    {
      "case": "N503_B_F95",
      "quarter": "2026Q4",
      "start_equity": 9280.01698272023,
      "end_equity": 9369.454576149394,
      "profit": 89.43759342916383,
      "return_pct": 0.9637654068489265,
      "partial": true
    },
    {
      "case": "N503_C_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 12811.893274571721,
      "profit": 682.729306178413,
      "return_pct": 5.6288241131664085,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "quarter": "2026Q3",
      "start_equity": 12811.893274571721,
      "end_equity": 10281.071258058513,
      "profit": -2530.822016513208,
      "return_pct": -19.75369262196581,
      "partial": false
    },
    {
      "case": "N503_C_F95",
      "quarter": "2026Q4",
      "start_equity": 10281.071258058513,
      "end_equity": 10379.05107409606,
      "profit": 97.9798160375467,
      "return_pct": 0.9530117395183613,
      "partial": true
    },
    {
      "case": "P604_B_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 11563.629744258766,
      "profit": -565.5342241345425,
      "return_pct": -4.662598556736763,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "quarter": "2026Q3",
      "start_equity": 11563.629744258766,
      "end_equity": 9259.241031841582,
      "profit": -2304.3887124171833,
      "return_pct": -19.927901215976675,
      "partial": false
    },
    {
      "case": "P604_B_F95",
      "quarter": "2026Q4",
      "start_equity": 9259.241031841582,
      "end_equity": 9348.678625270748,
      "profit": 89.43759342916564,
      "return_pct": 0.9659279105231011,
      "partial": true
    },
    {
      "case": "P604_C_F95",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12129.163968393308,
      "profit": 2129.163968393308,
      "return_pct": 21.291639683933084,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "quarter": "2026Q2",
      "start_equity": 12129.163968393308,
      "end_equity": 12811.893274571721,
      "profit": 682.729306178413,
      "return_pct": 5.6288241131664085,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "quarter": "2026Q3",
      "start_equity": 12811.893274571721,
      "end_equity": 10258.179800124883,
      "profit": -2553.7134744468385,
      "return_pct": -19.932366120433553,
      "partial": false
    },
    {
      "case": "P604_C_F95",
      "quarter": "2026Q4",
      "start_equity": 10258.179800124883,
      "end_equity": 10356.15961616243,
      "profit": 97.9798160375467,
      "return_pct": 0.9551384158460019,
      "partial": true
    }
  ]
}
```
