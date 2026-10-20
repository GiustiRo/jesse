# Comparación ampliada2026 — datos B_N

Análisis 1be4fbc3be4c47e3a4f46ac702bc2de9 succeeded. Incluye referencias repetidas sólo para comparación; no contarlas como corridas nuevas ni muestrasindependientes. Cada JSON contiene métricasmotor completas, puertas, contribución por activo, meses/Q y comparaciones de firmas. Mismos datoscorregidos delprotocolo y fuentescongeladas.

```json
{
  "rows": [
    {
      "case": "C504_B_N",
      "candidate": "C504",
      "portfolio": "B",
      "cost": "N",
      "net": -357.1922362302051,
      "balance": 9642.807763769793,
      "return_pct": -3.5719223623020513,
      "dd_pct": -27.772408369367064,
      "pf": 0.9284114458494492,
      "trades": 51,
      "fees": 424.41065867317366,
      "sharpe": -0.15994393334885273,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3595.9453845500393,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -1957.8186608965825,
          "fees": 327.7448413449761,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1600.6264246663768,
          "fees": 96.66581732819756,
          "trades": 8
        }
      },
      "economic_hash_8dec": "e29c65c380e012c1f51023c05fc25fcfcb72094cc1c001ad8c3ff7dc9d90ce66",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 20,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 9642.807763769793,
        "win_rate": 0.39215686274509803,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.4390377410666462,
        "longs_count": 16,
        "longs_percentage": 31.372549019607842,
        "shorts_percentage": 68.62745098039215,
        "shorts_count": 35,
        "fee": 424.4106586731736,
        "net_profit": -357.19223623020514,
        "net_profit_percentage": -3.5719223623020513,
        "average_win": 231.61618810409522,
        "average_loss": 160.95212897781002,
        "expectancy": -7.003769337847203,
        "expectancy_percentage": -0.07003769337847203,
        "expected_net_profit_every_100_trades": -7.003769337847203,
        "average_holding_period": 165534.11764705883,
        "average_winning_holding_period": 241398,
        "average_losing_holding_period": 116589.67741935483,
        "gross_profit": 4632.3237620819045,
        "gross_loss": -4989.51599831211,
        "max_drawdown": -27.772408369367064,
        "max_underwater_period": 231,
        "annual_return": -4.474744172859291,
        "annualization": 365,
        "sharpe_ratio": -0.15994393334885273,
        "calmar_ratio": -0.16112193488393786,
        "sortino_ratio": -0.23264231583806425,
        "omega_ratio": 0.9677647201123589,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -239.5021749585981,
        "largest_winning_trade": 958.8198632188712,
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
        "case": "C504_B_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "C504_B_N",
        "month": "2026-07",
        "start_equity": 11809.379809873653,
        "end_equity": 10005.792148976681,
        "profit": -1803.587660896972,
        "return_pct": -15.272501096027224,
        "partial": false
      },
      "best_trade": 958.8198632188712,
      "net_excluding_best_trade_arithmetic": -1316.0120994490762,
      "comparisons": {
        "K1001": {
          "delta_net": -230.33298524398754,
          "delta_return_pct": -2.303329852439875,
          "new_entries": 15,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -64.01726731542345,
          "delta_return_pct": -0.6401726731542361,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 51,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "C504_C_N",
      "candidate": "C504",
      "portfolio": "C",
      "cost": "N",
      "net": 775.02779004529,
      "balance": 10775.027790045298,
      "return_pct": 7.7502779004528985,
      "dd_pct": -21.402546775397504,
      "pf": 1.1458838384346262,
      "trades": 52,
      "fees": 467.7147369786922,
      "sharpe": 0.5745797039660432,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2845.714364379244,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2136.5174507212128,
          "fees": 353.778086818505,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1618.9456263632987,
          "fees": 97.77763250228952,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1292.599614403205,
          "fees": 16.159017657897497,
          "trades": 1
        }
      },
      "economic_hash_8dec": "4e5478d090abe72114af320634e0f68ea6b0b6908667d49e207ddaa8a8758c1b",
      "engine_metrics": {
        "total": 52,
        "total_winning_trades": 21,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 10775.027790045298,
        "win_rate": 0.40384615384615385,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.6915428091177824,
        "longs_count": 17,
        "longs_percentage": 32.69230769230769,
        "shorts_percentage": 67.3076923076923,
        "shorts_count": 35,
        "fee": 467.7147369786921,
        "net_profit": 775.0277900452899,
        "net_profit_percentage": 7.7502779004528985,
        "average_win": 289.8887708911392,
        "average_loss": 171.3753676989881,
        "expectancy": 14.904380577794086,
        "expectancy_percentage": 0.14904380577794085,
        "expected_net_profit_every_100_trades": 14.904380577794086,
        "average_holding_period": 214525.38461538462,
        "average_winning_holding_period": 359097.14285714284,
        "average_losing_holding_period": 116589.67741935483,
        "gross_profit": 6087.664188713923,
        "gross_loss": -5312.636398668631,
        "max_drawdown": -21.402546775397504,
        "max_underwater_period": 105,
        "annual_return": 9.850608664487591,
        "annualization": 365,
        "sharpe_ratio": 0.5745797039660432,
        "calmar_ratio": 0.460254042094233,
        "sortino_ratio": 0.8636786088590725,
        "omega_ratio": 1.1169825097685582,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -253.05669321019573,
        "largest_winning_trade": 1292.599614403205,
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
        "case": "C504_C_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "C504_C_N",
        "month": "2026-07",
        "start_equity": 13195.051223161678,
        "end_equity": 11179.664300259567,
        "profit": -2015.386922902111,
        "return_pct": -15.273809012309403,
        "partial": false
      },
      "best_trade": 1292.599614403205,
      "net_excluding_best_trade_arithmetic": -517.5718243579149,
      "comparisons": {
        "K1001": {
          "delta_net": -260.09324440116643,
          "delta_return_pct": -2.600932444011667,
          "new_entries": 15,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -68.31807220558528,
          "delta_return_pct": -0.6831807220558535,
          "new_entries": 0,
          "removed_entries": 0,
          "common_entries": 52,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1001_B_N",
      "candidate": "K1001",
      "portfolio": "B",
      "cost": "N",
      "net": -126.85925098621755,
      "balance": 9873.140749013795,
      "return_pct": -1.2685925098621762,
      "dd_pct": -25.883011163935965,
      "pf": 0.9708012741395763,
      "trades": 46,
      "fees": 384.12347139389385,
      "sharpe": -0.005416179600296317,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3351.30800668598,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -1725.6046750501298,
          "fees": 286.86996404966027,
          "trades": 38
        },
        "PAXG-USDT": {
          "net": 1598.7454240639127,
          "fees": 97.25350734423368,
          "trades": 8
        }
      },
      "economic_hash_8dec": "36529d0bf52f284ac31dfd9e7903188c051d58cf79604b58f77ed08d999ca1a5",
      "engine_metrics": {
        "total": 46,
        "total_winning_trades": 18,
        "total_losing_trades": 28,
        "starting_balance": 10000,
        "finishing_balance": 9873.140749013795,
        "win_rate": 0.391304347826087,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.4666666666666667,
        "ratio_avg_win_loss": 1.51013531532823,
        "longs_count": 16,
        "longs_percentage": 34.78260869565217,
        "shorts_percentage": 65.21739130434783,
        "shorts_count": 30,
        "fee": 384.1234713938939,
        "net_profit": -126.85925098621762,
        "net_profit_percentage": -1.2685925098621762,
        "average_win": 234.32362365269987,
        "average_loss": 155.16730274052912,
        "expectancy": -2.7578098040482075,
        "expectancy_percentage": -0.027578098040482075,
        "expected_net_profit_every_100_trades": -2.7578098040482075,
        "average_holding_period": 177281.73913043478,
        "average_winning_holding_period": 253870,
        "average_losing_holding_period": 128046.42857142857,
        "gross_profit": 4217.825225748597,
        "gross_loss": -4344.684476734816,
        "max_drawdown": -25.883011163935965,
        "max_underwater_period": 231,
        "annual_return": -1.5940492999751088,
        "annualization": 365,
        "sharpe_ratio": -0.005416179600296317,
        "calmar_ratio": -0.061586702176143,
        "sortino_ratio": -0.007831444513644018,
        "omega_ratio": 0.9988377645575783,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -239.42341055859808,
        "largest_winning_trade": 958.8198632188712,
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
        "case": "K1001_B_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "K1001_B_N",
        "month": "2026-07",
        "start_equity": 11718.139941468007,
        "end_equity": 9942.74805369767,
        "profit": -1775.3918877703381,
        "return_pct": -15.150799500931056,
        "partial": false
      },
      "best_trade": 958.8198632188712,
      "net_excluding_best_trade_arithmetic": -1085.6791142050888,
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
          "delta_net": 166.31571792856408,
          "delta_return_pct": 1.663157179285639,
          "new_entries": 10,
          "removed_entries": 15,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1001_C_N",
      "candidate": "K1001",
      "portfolio": "C",
      "cost": "N",
      "net": 1035.1210344464564,
      "balance": 11035.121034446462,
      "return_pct": 10.351210344464565,
      "dd_pct": -19.255823725787845,
      "pf": 1.2241287460250772,
      "trades": 47,
      "fees": 423.64005524328513,
      "sharpe": 0.7487080805790655,
      "max_underwater_days": 160,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2557.7372605171495,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": true,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": true,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -1880.4989749834053,
          "fees": 308.9414278955253,
          "trades": 38
        },
        "PAXG-USDT": {
          "net": 1616.638966026936,
          "fees": 98.4598343110521,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1298.9810434029262,
          "fees": 16.238793036707833,
          "trades": 1
        }
      },
      "economic_hash_8dec": "bb6cd819fa78a3b9ffff2ced4f2c8e64c50f7f8839f95074d276bdc1e6bfbb0e",
      "engine_metrics": {
        "total": 47,
        "total_winning_trades": 19,
        "total_losing_trades": 28,
        "starting_balance": 10000,
        "finishing_balance": 11035.121034446462,
        "win_rate": 0.40425531914893614,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.4666666666666667,
        "ratio_avg_win_loss": 1.8039792046685357,
        "longs_count": 17,
        "longs_percentage": 36.17021276595745,
        "shorts_percentage": 63.82978723404255,
        "shorts_count": 30,
        "fee": 423.6400552432852,
        "net_profit": 1035.1210344464566,
        "net_profit_percentage": 10.351210344464565,
        "average_win": 297.5548737649365,
        "average_loss": 164.94362739597622,
        "expectancy": 22.023851796733155,
        "expectancy_percentage": 0.22023851796733157,
        "expected_net_profit_every_100_trades": 22.023851796733158,
        "average_holding_period": 231234.89361702127,
        "average_winning_holding_period": 383302.1052631579,
        "average_losing_holding_period": 128046.42857142857,
        "gross_profit": 5653.542601533793,
        "gross_loss": -4618.421567087335,
        "max_drawdown": -19.255823725787845,
        "max_underwater_period": 160,
        "annual_return": 13.198362436168498,
        "annualization": 365,
        "sharpe_ratio": 0.7487080805790655,
        "calmar_ratio": 0.6854218559600203,
        "sortino_ratio": 1.122308911472623,
        "omega_ratio": 1.1621496023495101,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -250.00781738838492,
        "largest_winning_trade": 1298.9810434029262,
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
        "case": "K1001_C_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "K1001_C_N",
        "month": "2026-07",
        "start_equity": 13093.169309445526,
        "end_equity": 11113.380946785064,
        "profit": -1979.7883626604616,
        "return_pct": -15.120772640068324,
        "partial": false
      },
      "best_trade": 1298.9810434029262,
      "net_excluding_best_trade_arithmetic": -263.86000895646976,
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
          "delta_net": 191.77517219558115,
          "delta_return_pct": 1.9177517219558133,
          "new_entries": 10,
          "removed_entries": 15,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1005_B_N",
      "candidate": "K1005",
      "portfolio": "B",
      "cost": "N",
      "net": -385.49018366198106,
      "balance": 9614.50981633803,
      "return_pct": -3.854901836619811,
      "dd_pct": -27.82628151924299,
      "pf": 0.9133536653739626,
      "trades": 47,
      "fees": 390.96954199817276,
      "sharpe": -0.1945690151614398,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3602.920829461804,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -1985.4193722524014,
          "fees": 294.39701819189423,
          "trades": 39
        },
        "PAXG-USDT": {
          "net": 1599.9291885904204,
          "fees": 96.57252380627851,
          "trades": 8
        }
      },
      "economic_hash_8dec": "731f33406e63b45aa462f1c934a6ae0a87c2d4657aff0d0f9a3d1e47384757b1",
      "engine_metrics": {
        "total": 47,
        "total_winning_trades": 18,
        "total_losing_trades": 29,
        "starting_balance": 10000,
        "finishing_balance": 9614.50981633803,
        "win_rate": 0.3829787234042553,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.45161290322580644,
        "ratio_avg_win_loss": 1.4715142386580506,
        "longs_count": 16,
        "longs_percentage": 34.04255319148936,
        "shorts_percentage": 65.95744680851064,
        "shorts_count": 31,
        "fee": 390.9695419981727,
        "net_profit": -385.4901836619811,
        "net_profit_percentage": -3.854901836619811,
        "average_win": 225.75095628873635,
        "average_loss": 153.41404816755986,
        "expectancy": -8.201918801318755,
        "expectancy_percentage": -0.08201918801318754,
        "expected_net_profit_every_100_trades": -8.201918801318755,
        "average_holding_period": 173798.29787234042,
        "average_winning_holding_period": 252023.33333333334,
        "average_losing_holding_period": 125244.8275862069,
        "gross_profit": 4063.517213197254,
        "gross_loss": -4449.007396859236,
        "max_drawdown": -27.82628151924299,
        "max_underwater_period": 231,
        "annual_return": -4.827439371192543,
        "annualization": 365,
        "sharpe_ratio": -0.1945690151614398,
        "calmar_ratio": -0.17348488937891954,
        "sortino_ratio": -0.27952691471592206,
        "omega_ratio": 0.9595241275604688,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -239.42341055859808,
        "largest_winning_trade": 958.8198632188712,
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
        "case": "K1005_B_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "K1005_B_N",
        "month": "2026-07",
        "start_equity": 11718.139941468007,
        "end_equity": 9942.74805369767,
        "profit": -1775.3918877703381,
        "return_pct": -15.150799500931056,
        "partial": false
      },
      "best_trade": 958.8198632188712,
      "net_excluding_best_trade_arithmetic": -1344.3100468808523,
      "comparisons": {
        "K1001": {
          "delta_net": -258.6309326757635,
          "delta_return_pct": -2.586309326757635,
          "new_entries": 1,
          "removed_entries": 0,
          "common_entries": 46,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -92.31521474719943,
          "delta_return_pct": -0.9231521474719959,
          "new_entries": 11,
          "removed_entries": 15,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "K1005_C_N",
      "candidate": "K1005",
      "portfolio": "C",
      "cost": "N",
      "net": 747.5313616437771,
      "balance": 10747.531361643782,
      "return_pct": 7.47531361643777,
      "dd_pct": -21.35134408853706,
      "pf": 1.157982294615155,
      "trades": 48,
      "fees": 431.01786799148164,
      "sharpe": 0.5711361345522245,
      "max_underwater_days": 160,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2836.083727970432,
      "max_usdt_dd_date": "2026-10-01T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2169.4126802511,
          "fees": 317.0833554209622,
          "trades": 39
        },
        "PAXG-USDT": {
          "net": 1617.962998491952,
          "fees": 97.6957195338116,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1298.9810434029262,
          "fees": 16.238793036707833,
          "trades": 1
        }
      },
      "economic_hash_8dec": "fdf62d6117ec26e81410efeafa598788626c0231e75fcc0f3010a24701f45566",
      "engine_metrics": {
        "total": 48,
        "total_winning_trades": 19,
        "total_losing_trades": 29,
        "starting_balance": 10000,
        "finishing_balance": 10747.531361643782,
        "win_rate": 0.3958333333333333,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.45161290322580644,
        "ratio_avg_win_loss": 1.7674466602020793,
        "longs_count": 17,
        "longs_percentage": 35.41666666666667,
        "shorts_percentage": 64.58333333333333,
        "shorts_count": 31,
        "fee": 431.01786799148164,
        "net_profit": 747.531361643777,
        "net_profit_percentage": 7.47531361643777,
        "average_win": 288.3827761777864,
        "average_loss": 163.16349605979875,
        "expectancy": 15.573570034245364,
        "expectancy_percentage": 0.15573570034245363,
        "expected_net_profit_every_100_trades": 15.573570034245362,
        "average_holding_period": 226700,
        "average_winning_holding_period": 381552.63157894736,
        "average_losing_holding_period": 125244.8275862069,
        "gross_profit": 5479.272747377941,
        "gross_loss": -4731.7413857341635,
        "max_drawdown": -21.35134408853706,
        "max_underwater_period": 160,
        "annual_return": 9.497903517738182,
        "annualization": 365,
        "sharpe_ratio": 0.5711361345522245,
        "calmar_ratio": 0.4448386705002492,
        "sortino_ratio": 0.851147906025365,
        "omega_ratio": 1.1201782010311423,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -250.00781738838492,
        "largest_winning_trade": 1298.9810434029262,
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
        "case": "K1005_C_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "K1005_C_N",
        "month": "2026-07",
        "start_equity": 13093.169309445526,
        "end_equity": 11113.380946785064,
        "profit": -1979.7883626604616,
        "return_pct": -15.120772640068324,
        "partial": false
      },
      "best_trade": 1298.9810434029262,
      "net_excluding_best_trade_arithmetic": -551.449681759149,
      "comparisons": {
        "K1001": {
          "delta_net": -287.5896728026793,
          "delta_return_pct": -2.8758967280267953,
          "new_entries": 1,
          "removed_entries": 0,
          "common_entries": 47,
          "changed_exits": 1,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": -95.81450060709813,
          "delta_return_pct": -0.958145006070982,
          "new_entries": 11,
          "removed_entries": 15,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "N204_B_N",
      "candidate": "N204",
      "portfolio": "B",
      "cost": "N",
      "net": -293.17496891478163,
      "balance": 9706.825031085215,
      "return_pct": -2.931749689147815,
      "dd_pct": -27.293540820090346,
      "pf": 0.9405475418551664,
      "trades": 51,
      "fees": 425.238966579904,
      "sharpe": -0.11487390362431123,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3533.94206345774,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": false,
        "pf_ge_1_2": false,
        "dd_ge_minus25": false,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -1892.996128708871,
          "fees": 328.36885852357136,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1599.8211597940895,
          "fees": 96.8701080563327,
          "trades": 8
        }
      },
      "economic_hash_8dec": "f978f7216a1dc3519882532b0882ca9981705f8527ff80f3d15a8ebf8a90fd12",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 20,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 9706.825031085215,
        "win_rate": 0.39215686274509803,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.4578486898755083,
        "longs_count": 16,
        "longs_percentage": 31.372549019607842,
        "shorts_percentage": 68.62745098039215,
        "shorts_count": 35,
        "fee": 425.23896657990394,
        "net_profit": -293.1749689147815,
        "net_profit_percentage": -2.931749689147815,
        "average_win": 231.90378072721046,
        "average_loss": 159.07259946641904,
        "expectancy": -5.748528802250604,
        "expectancy_percentage": -0.05748528802250604,
        "expected_net_profit_every_100_trades": -5.748528802250604,
        "average_holding_period": 166381.17647058822,
        "average_winning_holding_period": 241398,
        "average_losing_holding_period": 117983.2258064516,
        "gross_profit": 4638.075614544209,
        "gross_loss": -4931.25058345899,
        "max_drawdown": -27.293540820090346,
        "max_underwater_period": 231,
        "annual_return": -3.6758693031791134,
        "annualization": 365,
        "sharpe_ratio": -0.11487390362431123,
        "calmar_ratio": -0.13467909229546957,
        "sortino_ratio": -0.16739319446335765,
        "omega_ratio": 0.9766733243616085,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -239.5021749585981,
        "largest_winning_trade": 958.8198632188712,
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
        "case": "N204_B_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "N204_B_N",
        "month": "2026-07",
        "start_equity": 11809.379809873653,
        "end_equity": 10070.87023276668,
        "profit": -1738.5095771069737,
        "return_pct": -14.721429957341458,
        "partial": false
      },
      "best_trade": 958.8198632188712,
      "net_excluding_best_trade_arithmetic": -1251.9948321336528,
      "comparisons": {
        "K1001": {
          "delta_net": -166.31571792856408,
          "delta_return_pct": -1.663157179285639,
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
      "case": "N204_C_N",
      "candidate": "N204",
      "portfolio": "C",
      "cost": "N",
      "net": 843.3458622508753,
      "balance": 10843.345862250884,
      "return_pct": 8.433458622508752,
      "dd_pct": -20.912192666346463,
      "pf": 1.160598165740897,
      "trades": 52,
      "fees": 468.8389197081256,
      "sharpe": 0.6155407840976062,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2780.516154726789,
      "max_usdt_dd_date": "2026-10-02T23:01:00+00:00",
      "gates": {
        "positive_net": true,
        "pf_ge_1_2": false,
        "dd_ge_minus25": true,
        "trades_ge_20": true
      },
      "nominal_pass": false,
      "stress_positive": null,
      "by_symbol": {
        "BTC-USDT": {
          "net": -2067.3090214306785,
          "fees": 354.6756727293584,
          "trades": 43
        },
        "PAXG-USDT": {
          "net": 1618.0552692783494,
          "fees": 98.00422932086965,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1292.599614403205,
          "fees": 16.159017657897497,
          "trades": 1
        }
      },
      "economic_hash_8dec": "2c33a95857fc4edb320d0aad426be5ce6c5b09e33e3d1f614c6a09e96e066349",
      "engine_metrics": {
        "total": 52,
        "total_winning_trades": 21,
        "total_losing_trades": 31,
        "starting_balance": 10000,
        "finishing_balance": 10843.345862250884,
        "win_rate": 0.40384615384615385,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.45714285714285713,
        "ratio_avg_win_loss": 1.7132639589508487,
        "longs_count": 17,
        "longs_percentage": 32.69230769230769,
        "shorts_percentage": 67.3076923076923,
        "shorts_count": 35,
        "fee": 468.83891970812556,
        "net_profit": 843.3458622508751,
        "net_profit_percentage": 8.433458622508752,
        "average_win": 290.22025734912756,
        "average_loss": 169.39611426067103,
        "expectancy": 16.218189658670724,
        "expectancy_percentage": 0.16218189658670723,
        "expected_net_profit_every_100_trades": 16.218189658670724,
        "average_holding_period": 215356.15384615384,
        "average_winning_holding_period": 359097.14285714284,
        "average_losing_holding_period": 117983.2258064516,
        "gross_profit": 6094.6254043316785,
        "gross_loss": -5251.279542080802,
        "max_drawdown": -20.912192666346463,
        "max_underwater_period": 105,
        "annual_return": 10.727952655469398,
        "annualization": 365,
        "sharpe_ratio": 0.6155407840976062,
        "calmar_ratio": 0.5129998956414388,
        "sortino_ratio": 0.9266850111445716,
        "omega_ratio": 1.1261762253599834,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -253.05669321019573,
        "largest_winning_trade": 1292.599614403205,
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
        "case": "N204_C_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "N204_C_N",
        "month": "2026-07",
        "start_equity": 13195.051223161678,
        "end_equity": 11252.562401474566,
        "profit": -1942.4888216871113,
        "return_pct": -14.721343546415355,
        "partial": false
      },
      "best_trade": 1292.599614403205,
      "net_excluding_best_trade_arithmetic": -449.25375215232964,
      "comparisons": {
        "K1001": {
          "delta_net": -191.77517219558115,
          "delta_return_pct": -1.9177517219558133,
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
      "case": "C504_B_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 11796.649318694166,
      "profit": -522.8376804581203,
      "return_pct": -4.243989059723807,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-05",
      "start_equity": 11796.649318694166,
      "end_equity": 11518.143941252854,
      "profit": -278.5053774413118,
      "return_pct": -2.360885450752226,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-06",
      "start_equity": 11518.143941252854,
      "end_equity": 11809.379809873653,
      "profit": 291.235868620799,
      "return_pct": 2.528496519111223,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-07",
      "start_equity": 11809.379809873653,
      "end_equity": 10005.792148976681,
      "profit": -1803.587660896972,
      "return_pct": -15.272501096027224,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-08",
      "start_equity": 10005.792148976681,
      "end_equity": 9639.826271064996,
      "profit": -365.9658779116853,
      "return_pct": -3.6575402772994203,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-09",
      "start_equity": 9639.826271064996,
      "end_equity": 9523.726523091576,
      "profit": -116.09974797341965,
      "return_pct": -1.204375936959634,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "month": "2026-10",
      "start_equity": 9523.726523091576,
      "end_equity": 9642.807763769793,
      "profit": 119.081240678217,
      "return_pct": 1.2503639241371323,
      "partial": true
    },
    {
      "case": "C504_C_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 12640.69728875743,
      "profit": 321.21028960514377,
      "return_pct": 2.6073349452558015,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-05",
      "start_equity": 12640.69728875743,
      "end_equity": 12869.670459599129,
      "profit": 228.97317084169845,
      "return_pct": 1.811396678610011,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-06",
      "start_equity": 12869.670459599129,
      "end_equity": 13195.051223161678,
      "profit": 325.38076356254896,
      "return_pct": 2.5282757983896564,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-07",
      "start_equity": 13195.051223161678,
      "end_equity": 11179.664300259567,
      "profit": -2015.386922902111,
      "return_pct": -15.273809012309403,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-08",
      "start_equity": 11179.664300259567,
      "end_equity": 10771.471056990897,
      "profit": -408.1932432686699,
      "return_pct": -3.651211989068337,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-09",
      "start_equity": 10771.471056990897,
      "end_equity": 10642.276180985926,
      "profit": -129.19487600497087,
      "return_pct": -1.199417194934771,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "month": "2026-10",
      "start_equity": 10642.276180985926,
      "end_equity": 10775.027790045298,
      "profit": 132.75160905937264,
      "return_pct": 1.2473986466969622,
      "partial": true
    },
    {
      "case": "K1001_B_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12381.120738941088,
      "profit": -516.2052909108897,
      "return_pct": -4.002421042284954,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-04",
      "start_equity": 12381.120738941088,
      "end_equity": 11854.116407741594,
      "profit": -527.0043311994941,
      "return_pct": -4.256515563586749,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-05",
      "start_equity": 11854.116407741594,
      "end_equity": 11718.139941468007,
      "profit": -135.976466273587,
      "return_pct": -1.1470822589930374,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-06",
      "start_equity": 11718.139941468007,
      "end_equity": 11718.139941468007,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-07",
      "start_equity": 11718.139941468007,
      "end_equity": 9942.74805369767,
      "profit": -1775.3918877703381,
      "return_pct": -15.150799500931056,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-08",
      "start_equity": 9942.74805369767,
      "end_equity": 9823.32631224472,
      "profit": -119.42174145294848,
      "return_pct": -1.2010939109387997,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-09",
      "start_equity": 9823.32631224472,
      "end_equity": 9718.395450667143,
      "profit": -104.93086157757716,
      "return_pct": -1.0681805555698753,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "month": "2026-10",
      "start_equity": 9718.395450667143,
      "end_equity": 9873.140749013795,
      "profit": 154.7452983466519,
      "return_pct": 1.5922926694244444,
      "partial": true
    },
    {
      "case": "K1001_C_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12381.120738941088,
      "profit": -516.2052909108897,
      "return_pct": -4.002421042284954,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-04",
      "start_equity": 12381.120738941088,
      "end_equity": 12703.261438021344,
      "profit": 322.1406990802552,
      "return_pct": 2.601870265807671,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-05",
      "start_equity": 12703.261438021344,
      "end_equity": 13093.169309445526,
      "profit": 389.9078714241823,
      "return_pct": 3.069352491299382,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-06",
      "start_equity": 13093.169309445526,
      "end_equity": 13093.169309445526,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-07",
      "start_equity": 13093.169309445526,
      "end_equity": 11113.380946785064,
      "profit": -1979.7883626604616,
      "return_pct": -15.120772640068324,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-08",
      "start_equity": 11113.380946785064,
      "end_equity": 10981.353595378027,
      "profit": -132.0273514070377,
      "return_pct": -1.1880034711239773,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-09",
      "start_equity": 10981.353595378027,
      "end_equity": 10862.53689281464,
      "profit": -118.81670256338657,
      "return_pct": -1.0819859458254366,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "month": "2026-10",
      "start_equity": 10862.53689281464,
      "end_equity": 11035.121034446462,
      "profit": 172.5841416318217,
      "return_pct": 1.5888014313303112,
      "partial": true
    },
    {
      "case": "K1005_B_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12381.120738941088,
      "profit": -516.2052909108897,
      "return_pct": -4.002421042284954,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-04",
      "start_equity": 12381.120738941088,
      "end_equity": 11854.116407741594,
      "profit": -527.0043311994941,
      "return_pct": -4.256515563586749,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-05",
      "start_equity": 11854.116407741594,
      "end_equity": 11718.139941468007,
      "profit": -135.976466273587,
      "return_pct": -1.1470822589930374,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-06",
      "start_equity": 11718.139941468007,
      "end_equity": 11718.139941468007,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-07",
      "start_equity": 11718.139941468007,
      "end_equity": 9942.74805369767,
      "profit": -1775.3918877703381,
      "return_pct": -15.150799500931056,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-08",
      "start_equity": 9942.74805369767,
      "end_equity": 9568.956291831031,
      "profit": -373.7917618666379,
      "return_pct": -3.7594411509565107,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-09",
      "start_equity": 9568.956291831031,
      "end_equity": 9464.191196838105,
      "profit": -104.7650949929266,
      "return_pct": -1.0948434896955739,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "month": "2026-10",
      "start_equity": 9464.191196838105,
      "end_equity": 9614.50981633803,
      "profit": 150.31861949992526,
      "return_pct": 1.5882880678715017,
      "partial": true
    },
    {
      "case": "K1005_C_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12381.120738941088,
      "profit": -516.2052909108897,
      "return_pct": -4.002421042284954,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-04",
      "start_equity": 12381.120738941088,
      "end_equity": 12703.261438021344,
      "profit": 322.1406990802552,
      "return_pct": 2.601870265807671,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-05",
      "start_equity": 12703.261438021344,
      "end_equity": 13093.169309445526,
      "profit": 389.9078714241823,
      "return_pct": 3.069352491299382,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-06",
      "start_equity": 13093.169309445526,
      "end_equity": 13093.169309445526,
      "profit": 0,
      "return_pct": 0,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-07",
      "start_equity": 13093.169309445526,
      "end_equity": 11113.380946785064,
      "profit": -1979.7883626604616,
      "return_pct": -15.120772640068324,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-08",
      "start_equity": 11113.380946785064,
      "end_equity": 10695.607384277306,
      "profit": -417.77356250775847,
      "return_pct": -3.759194114808184,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-09",
      "start_equity": 10695.607384277306,
      "end_equity": 10580.303278781534,
      "profit": -115.30410549577209,
      "return_pct": -1.0780510292970447,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "month": "2026-10",
      "start_equity": 10580.303278781534,
      "end_equity": 10747.531361643782,
      "profit": 167.2280828622479,
      "return_pct": 1.5805603909069266,
      "partial": true
    },
    {
      "case": "N204_B_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 11796.649318694166,
      "profit": -522.8376804581203,
      "return_pct": -4.243989059723807,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-05",
      "start_equity": 11796.649318694166,
      "end_equity": 11518.143941252854,
      "profit": -278.5053774413118,
      "return_pct": -2.360885450752226,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-06",
      "start_equity": 11518.143941252854,
      "end_equity": 11809.379809873653,
      "profit": 291.235868620799,
      "return_pct": 2.528496519111223,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-07",
      "start_equity": 11809.379809873653,
      "end_equity": 10070.87023276668,
      "profit": -1738.5095771069737,
      "return_pct": -14.721429957341458,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-08",
      "start_equity": 10070.87023276668,
      "end_equity": 9701.994139441953,
      "profit": -368.87609332472675,
      "return_pct": -3.6628025662027497,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-09",
      "start_equity": 9701.994139441953,
      "end_equity": 9585.729844183876,
      "profit": -116.26429525807725,
      "return_pct": -1.1983546226380648,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "month": "2026-10",
      "start_equity": 9585.729844183876,
      "end_equity": 9706.825031085215,
      "profit": 121.09518690133882,
      "return_pct": 1.2632860394538703,
      "partial": true
    },
    {
      "case": "N204_C_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 12640.69728875743,
      "profit": 321.21028960514377,
      "return_pct": 2.6073349452558015,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-05",
      "start_equity": 12640.69728875743,
      "end_equity": 12869.670459599129,
      "profit": 228.97317084169845,
      "return_pct": 1.811396678610011,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-06",
      "start_equity": 12869.670459599129,
      "end_equity": 13195.051223161678,
      "profit": 325.38076356254896,
      "return_pct": 2.5282757983896564,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-07",
      "start_equity": 13195.051223161678,
      "end_equity": 11252.562401474566,
      "profit": -1942.4888216871113,
      "return_pct": -14.721343546415355,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-08",
      "start_equity": 11252.562401474566,
      "end_equity": 10840.242667923507,
      "profit": -412.31973355105947,
      "return_pct": -3.664229700223909,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-09",
      "start_equity": 10840.242667923507,
      "end_equity": 10709.705114142143,
      "profit": -130.53755378136339,
      "return_pct": -1.2041940183463495,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "month": "2026-10",
      "start_equity": 10709.705114142143,
      "end_equity": 10843.345862250884,
      "profit": 133.6407481087408,
      "return_pct": 1.2478471319650852,
      "partial": true
    }
  ],
  "quarterly": [
    {
      "case": "C504_B_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 11809.379809873653,
      "profit": -510.1071892786331,
      "return_pct": -4.140652847912696,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "quarter": "2026Q3",
      "start_equity": 11809.379809873653,
      "end_equity": 9523.726523091576,
      "profit": -2285.653286782077,
      "return_pct": -19.354558186629532,
      "partial": false
    },
    {
      "case": "C504_B_N",
      "quarter": "2026Q4",
      "start_equity": 9523.726523091576,
      "end_equity": 9642.807763769793,
      "profit": 119.081240678217,
      "return_pct": 1.2503639241371323,
      "partial": true
    },
    {
      "case": "C504_C_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 13195.051223161678,
      "profit": 875.5642240093912,
      "return_pct": 7.107148406988362,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "quarter": "2026Q3",
      "start_equity": 13195.051223161678,
      "end_equity": 10642.276180985926,
      "profit": -2552.775042175752,
      "return_pct": -19.346457993999955,
      "partial": false
    },
    {
      "case": "C504_C_N",
      "quarter": "2026Q4",
      "start_equity": 10642.276180985926,
      "end_equity": 10775.027790045298,
      "profit": 132.75160905937264,
      "return_pct": 1.2473986466969622,
      "partial": true
    },
    {
      "case": "K1001_B_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12381.120738941088,
      "profit": 2381.1207389410883,
      "return_pct": 23.811207389410892,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "quarter": "2026Q2",
      "start_equity": 12381.120738941088,
      "end_equity": 11718.139941468007,
      "profit": -662.9807974730811,
      "return_pct": -5.354772087698612,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "quarter": "2026Q3",
      "start_equity": 11718.139941468007,
      "end_equity": 9718.395450667143,
      "profit": -1999.7444908008638,
      "return_pct": -17.065374716376212,
      "partial": false
    },
    {
      "case": "K1001_B_N",
      "quarter": "2026Q4",
      "start_equity": 9718.395450667143,
      "end_equity": 9873.140749013795,
      "profit": 154.7452983466519,
      "return_pct": 1.5922926694244444,
      "partial": true
    },
    {
      "case": "K1001_C_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12381.120738941088,
      "profit": 2381.1207389410883,
      "return_pct": 23.811207389410892,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "quarter": "2026Q2",
      "start_equity": 12381.120738941088,
      "end_equity": 13093.169309445526,
      "profit": 712.0485705044375,
      "return_pct": 5.751083326930995,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "quarter": "2026Q3",
      "start_equity": 13093.169309445526,
      "end_equity": 10862.53689281464,
      "profit": -2230.632416630886,
      "return_pct": -17.036611716474848,
      "partial": false
    },
    {
      "case": "K1001_C_N",
      "quarter": "2026Q4",
      "start_equity": 10862.53689281464,
      "end_equity": 11035.121034446462,
      "profit": 172.5841416318217,
      "return_pct": 1.5888014313303112,
      "partial": true
    },
    {
      "case": "K1005_B_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12381.120738941088,
      "profit": 2381.1207389410883,
      "return_pct": 23.811207389410892,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "quarter": "2026Q2",
      "start_equity": 12381.120738941088,
      "end_equity": 11718.139941468007,
      "profit": -662.9807974730811,
      "return_pct": -5.354772087698612,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "quarter": "2026Q3",
      "start_equity": 11718.139941468007,
      "end_equity": 9464.191196838105,
      "profit": -2253.9487446299026,
      "return_pct": -19.234697280356393,
      "partial": false
    },
    {
      "case": "K1005_B_N",
      "quarter": "2026Q4",
      "start_equity": 9464.191196838105,
      "end_equity": 9614.50981633803,
      "profit": 150.31861949992526,
      "return_pct": 1.5882880678715017,
      "partial": true
    },
    {
      "case": "K1005_C_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12381.120738941088,
      "profit": 2381.1207389410883,
      "return_pct": 23.811207389410892,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "quarter": "2026Q2",
      "start_equity": 12381.120738941088,
      "end_equity": 13093.169309445526,
      "profit": 712.0485705044375,
      "return_pct": 5.751083326930995,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "quarter": "2026Q3",
      "start_equity": 13093.169309445526,
      "end_equity": 10580.303278781534,
      "profit": -2512.866030663992,
      "return_pct": -19.192190762027263,
      "partial": false
    },
    {
      "case": "K1005_C_N",
      "quarter": "2026Q4",
      "start_equity": 10580.303278781534,
      "end_equity": 10747.531361643782,
      "profit": 167.2280828622479,
      "return_pct": 1.5805603909069266,
      "partial": true
    },
    {
      "case": "N204_B_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 11809.379809873653,
      "profit": -510.1071892786331,
      "return_pct": -4.140652847912696,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "quarter": "2026Q3",
      "start_equity": 11809.379809873653,
      "end_equity": 9585.729844183876,
      "profit": -2223.6499656897777,
      "return_pct": -18.82952366245868,
      "partial": false
    },
    {
      "case": "N204_B_N",
      "quarter": "2026Q4",
      "start_equity": 9585.729844183876,
      "end_equity": 9706.825031085215,
      "profit": 121.09518690133882,
      "return_pct": 1.2632860394538703,
      "partial": true
    },
    {
      "case": "N204_C_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 13195.051223161678,
      "profit": 875.5642240093912,
      "return_pct": 7.107148406988362,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "quarter": "2026Q3",
      "start_equity": 13195.051223161678,
      "end_equity": 10709.705114142143,
      "profit": -2485.346109019534,
      "return_pct": -18.83544115885606,
      "partial": false
    },
    {
      "case": "N204_C_N",
      "quarter": "2026Q4",
      "start_equity": 10709.705114142143,
      "end_equity": 10843.345862250884,
      "profit": 133.6407481087408,
      "return_pct": 1.2478471319650852,
      "partial": true
    }
  ]
}
```
