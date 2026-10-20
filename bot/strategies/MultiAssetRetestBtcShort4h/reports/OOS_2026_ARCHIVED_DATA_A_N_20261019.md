# Comparación ampliada2026 — datos A_N

Análisis af3cd20f65c74629a64dff648bef110a succeeded. Incluye referencias repetidas sólo para comparación; no contarlas como corridas nuevas ni muestrasindependientes. Cada JSON contiene métricasmotor completas, puertas, contribución por activo, meses/Q y comparaciones de firmas. Mismos datoscorregidos delprotocolo y fuentescongeladas.

```json
{
  "rows": [
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
    },
    {
      "case": "N503_B_N",
      "candidate": "N503",
      "portfolio": "B",
      "cost": "N",
      "net": -214.30674277153054,
      "balance": 9785.693257228473,
      "return_pct": -2.1430674277153083,
      "dd_pct": -26.701469363685348,
      "pf": 0.9558883417605528,
      "trades": 50,
      "fees": 415.7961418796011,
      "sharpe": -0.05935248208527564,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3457.2812066581664,
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
          "net": -1813.0777696474795,
          "fees": 318.6604214918325,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1598.771026875949,
          "fees": 97.13572038776867,
          "trades": 8
        }
      },
      "economic_hash_8dec": "ee651c816f533380e0e4a9d06a3a3be0f73b53234103b9908d2a6ef7fd1a7985",
      "engine_metrics": {
        "total": 50,
        "total_winning_trades": 20,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 9785.693257228473,
        "win_rate": 0.4,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.4338325126408298,
        "longs_count": 16,
        "longs_percentage": 32,
        "shorts_percentage": 68,
        "shorts_count": 34,
        "fee": 415.7961418796011,
        "net_profit": -214.30674277153082,
        "net_profit_percentage": -2.1430674277153083,
        "average_win": 232.1986127386079,
        "average_loss": 161.94263325145624,
        "expectancy": -4.286134855430589,
        "expectancy_percentage": -0.04286134855430589,
        "expected_net_profit_every_100_trades": -4.286134855430589,
        "average_holding_period": 169011.6,
        "average_winning_holding_period": 241398,
        "average_losing_holding_period": 120754,
        "gross_profit": 4643.972254772158,
        "gross_loss": -4858.278997543687,
        "max_drawdown": -26.701469363685348,
        "max_underwater_period": 231,
        "annual_return": -2.689794238937848,
        "annualization": 365,
        "sharpe_ratio": -0.05935248208527564,
        "calmar_ratio": -0.10073581353526687,
        "sortino_ratio": -0.08660747156633164,
        "omega_ratio": 0.9878233909467173,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -239.5021749585981,
        "largest_winning_trade": 958.8198632188712,
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
        "case": "N503_B_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "N503_B_N",
        "month": "2026-07",
        "start_equity": 11809.379809873653,
        "end_equity": 10070.87023276668,
        "profit": -1738.5095771069737,
        "return_pct": -14.721429957341458,
        "partial": false
      },
      "best_trade": 958.8198632188712,
      "net_excluding_best_trade_arithmetic": -1173.1266059904017,
      "comparisons": {
        "K1001": {
          "delta_net": -87.44749178531299,
          "delta_return_pct": -0.8744749178531321,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 78.86822614325109,
          "delta_return_pct": 0.7886822614325069,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 50,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "N503_C_N",
      "candidate": "N503",
      "portfolio": "C",
      "cost": "N",
      "net": 937.0203085252068,
      "balance": 10937.020308525212,
      "return_pct": 9.370203085252069,
      "dd_pct": -20.2326883797718,
      "pf": 1.181388875738663,
      "trades": 51,
      "fees": 458.2486627473311,
      "sharpe": 0.6712190252805874,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2690.1682569155964,
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
          "net": -1972.4589745694054,
          "fees": 343.7907486448224,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1616.879668691407,
          "fees": 98.2988964446112,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1292.599614403205,
          "fees": 16.159017657897497,
          "trades": 1
        }
      },
      "economic_hash_8dec": "5e478d316d799444695fca623d080fd5df7ac523e71c2f9a07ea5abcd123ca27",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 21,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 10937.020308525212,
        "win_rate": 0.4117647058823529,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.6876983939123762,
        "longs_count": 17,
        "longs_percentage": 33.33333333333333,
        "shorts_percentage": 66.66666666666667,
        "shorts_count": 34,
        "fee": 458.248662747331,
        "net_profit": 937.0203085252068,
        "net_profit_percentage": 9.370203085252069,
        "average_win": 290.61092515943335,
        "average_loss": 172.19363732742974,
        "expectancy": 18.37294722598446,
        "expectancy_percentage": 0.1837294722598446,
        "expected_net_profit_every_100_trades": 18.37294722598446,
        "average_holding_period": 218895.29411764705,
        "average_winning_holding_period": 359097.14285714284,
        "average_losing_holding_period": 120754,
        "gross_profit": 6102.829428348101,
        "gross_loss": -5165.809119822892,
        "max_drawdown": -20.2326883797718,
        "max_underwater_period": 105,
        "annual_return": 11.93324891425014,
        "annualization": 365,
        "sharpe_ratio": 0.6712190252805874,
        "calmar_ratio": 0.58980046004073,
        "sortino_ratio": 1.011936527818002,
        "omega_ratio": 1.1389728197028002,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -253.05669321019573,
        "largest_winning_trade": 1292.599614403205,
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
        "case": "N503_C_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "N503_C_N",
        "month": "2026-07",
        "start_equity": 13195.051223161678,
        "end_equity": 11252.562401474566,
        "profit": -1942.4888216871113,
        "return_pct": -14.721343546415355,
        "partial": false
      },
      "best_trade": 1292.599614403205,
      "net_excluding_best_trade_arithmetic": -355.5793058779981,
      "comparisons": {
        "K1001": {
          "delta_net": -98.10072592124959,
          "delta_return_pct": -0.9810072592124968,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 93.67444627433156,
          "delta_return_pct": 0.9367444627433166,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 51,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "P604_B_N",
      "candidate": "P604",
      "portfolio": "B",
      "cost": "N",
      "net": -231.82318639170242,
      "balance": 9768.176813608296,
      "return_pct": -2.318231863917022,
      "dd_pct": -26.829842833978645,
      "pf": 0.952323198229535,
      "trades": 50,
      "fees": 416.11273631812173,
      "sharpe": -0.07154348322147806,
      "max_underwater_days": 231,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 3473.9028831746673,
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
          "net": -1826.8720461044704,
          "fees": 318.74896929559094,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1595.048859712768,
          "fees": 97.36376702253088,
          "trades": 8
        }
      },
      "economic_hash_8dec": "e2686a5d3020dba73f249538100a9fcdbb577d0a4a1a05c2c70b26b503540c96",
      "engine_metrics": {
        "total": 50,
        "total_winning_trades": 20,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 9768.176813608296,
        "win_rate": 0.4,
        "win_rate_longs": 0.25,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.4284847973443027,
        "longs_count": 16,
        "longs_percentage": 32,
        "shorts_percentage": 68,
        "shorts_count": 34,
        "fee": 416.1127363181218,
        "net_profit": -231.82318639170222,
        "net_profit_percentage": -2.318231863917022,
        "average_win": 231.52832204557726,
        "average_loss": 162.07965424344155,
        "expectancy": -4.636463727834027,
        "expectancy_percentage": -0.04636463727834027,
        "expected_net_profit_every_100_trades": -4.636463727834027,
        "average_holding_period": 164713.2,
        "average_winning_holding_period": 230652,
        "average_losing_holding_period": 120754,
        "gross_profit": 4630.566440911545,
        "gross_loss": -4862.389627303247,
        "max_drawdown": -26.829842833978645,
        "max_underwater_period": 231,
        "annual_return": -2.9089773132354058,
        "annualization": 365,
        "sharpe_ratio": -0.07154348322147806,
        "calmar_ratio": -0.10842319618627555,
        "sortino_ratio": -0.10439898302842775,
        "omega_ratio": 0.9853334718840819,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -239.5021749585981,
        "largest_winning_trade": 958.8198632188712,
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
        "case": "P604_B_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "P604_B_N",
        "month": "2026-07",
        "start_equity": 11809.379809873653,
        "end_equity": 10093.58238460668,
        "profit": -1715.7974252669737,
        "return_pct": -14.529106971666883,
        "partial": false
      },
      "best_trade": 958.8198632188712,
      "net_excluding_best_trade_arithmetic": -1190.6430496105736,
      "comparisons": {
        "K1001": {
          "delta_net": -104.96393540548488,
          "delta_return_pct": -1.0496393540548457,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 36,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 61.35178252307921,
          "delta_return_pct": 0.6135178252307933,
          "new_entries": 0,
          "removed_entries": 1,
          "common_entries": 50,
          "changed_exits": 2,
          "economic_identity_at_8dec": false
        }
      }
    },
    {
      "case": "P604_C_N",
      "candidate": "P604",
      "portfolio": "C",
      "cost": "N",
      "net": 913.6640771843795,
      "balance": 10913.664077184385,
      "return_pct": 9.136640771843792,
      "dd_pct": -20.391648694387708,
      "pf": 1.1766713505885915,
      "trades": 51,
      "fees": 458.4502928006041,
      "sharpe": 0.6572372431389731,
      "max_underwater_days": 105,
      "terminal_gap": 0,
      "reported_preterminal_open_trades": 0,
      "boundary_closes": 0,
      "max_drawdown_usdt": 2711.303856123297,
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
          "net": -1991.6609837267483,
          "fees": 343.7377769945113,
          "trades": 42
        },
        "PAXG-USDT": {
          "net": 1612.7254465079225,
          "fees": 98.55349814819525,
          "trades": 8
        },
        "SPY-USDT": {
          "net": 1292.599614403205,
          "fees": 16.159017657897497,
          "trades": 1
        }
      },
      "economic_hash_8dec": "fe1080b68434200340906c38d52cc4b0f27b79bd9910a69c29ab58dd723d39ca",
      "engine_metrics": {
        "total": 51,
        "total_winning_trades": 21,
        "total_losing_trades": 30,
        "starting_balance": 10000,
        "finishing_balance": 10913.664077184385,
        "win_rate": 0.4117647058823529,
        "win_rate_longs": 0.29411764705882354,
        "win_rate_shorts": 0.47058823529411764,
        "ratio_avg_win_loss": 1.6809590722694165,
        "longs_count": 17,
        "longs_percentage": 33.33333333333333,
        "shorts_percentage": 66.66666666666667,
        "shorts_count": 34,
        "fee": 458.4502928006041,
        "net_profit": 913.6640771843793,
        "net_profit_percentage": 9.136640771843792,
        "average_win": 289.77192480709306,
        "average_loss": 172.3848781254858,
        "expectancy": 17.914981905576056,
        "expectancy_percentage": 0.17914981905576055,
        "expected_net_profit_every_100_trades": 17.914981905576056,
        "average_holding_period": 214681.17647058822,
        "average_winning_holding_period": 348862.85714285716,
        "average_losing_holding_period": 120754,
        "gross_profit": 6085.210420948954,
        "gross_loss": -5171.546343764574,
        "max_drawdown": -20.391648694387708,
        "max_underwater_period": 105,
        "annual_return": 11.632476696806581,
        "annualization": 365,
        "sharpe_ratio": 0.6572372431389731,
        "calmar_ratio": 0.5704529766643209,
        "sortino_ratio": 0.9907440953391098,
        "omega_ratio": 1.1359616607319711,
        "serenity_index": null,
        "total_open_trades": 0,
        "open_pl": 0,
        "winning_streak": 6,
        "losing_streak": 11,
        "largest_losing_trade": -253.05669321019573,
        "largest_winning_trade": 1292.599614403205,
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
        "case": "P604_C_N",
        "month": "2026-01",
        "start_equity": 10000,
        "end_equity": 12164.114978082376,
        "profit": 2164.114978082376,
        "return_pct": 21.641149780823767,
        "partial": false
      },
      "worst_month": {
        "case": "P604_C_N",
        "month": "2026-07",
        "start_equity": 13195.051223161678,
        "end_equity": 11277.910785224567,
        "profit": -1917.1404379371106,
        "return_pct": -14.529238314527305,
        "partial": false
      },
      "best_trade": 1292.599614403205,
      "net_excluding_best_trade_arithmetic": -378.9355372188254,
      "comparisons": {
        "K1001": {
          "delta_net": -121.45695726207691,
          "delta_return_pct": -1.214569572620773,
          "new_entries": 14,
          "removed_entries": 10,
          "common_entries": 37,
          "changed_exits": 0,
          "economic_identity_at_8dec": false
        },
        "N204": {
          "delta_net": 70.31821493350424,
          "delta_return_pct": 0.7031821493350403,
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
    },
    {
      "case": "N503_B_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 11796.649318694166,
      "profit": -522.8376804581203,
      "return_pct": -4.243989059723807,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-05",
      "start_equity": 11796.649318694166,
      "end_equity": 11518.143941252854,
      "profit": -278.5053774413118,
      "return_pct": -2.360885450752226,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-06",
      "start_equity": 11518.143941252854,
      "end_equity": 11809.379809873653,
      "profit": 291.235868620799,
      "return_pct": 2.528496519111223,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-07",
      "start_equity": 11809.379809873653,
      "end_equity": 10070.87023276668,
      "profit": -1738.5095771069737,
      "return_pct": -14.721429957341458,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-08",
      "start_equity": 10070.87023276668,
      "end_equity": 9783.264908718545,
      "profit": -287.6053240481342,
      "return_pct": -2.8558140200474313,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-09",
      "start_equity": 9783.264908718545,
      "end_equity": 9664.62142448721,
      "profit": -118.6434842313356,
      "return_pct": -1.2127187123963545,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "month": "2026-10",
      "start_equity": 9664.62142448721,
      "end_equity": 9785.693257228473,
      "profit": 121.07183274126328,
      "return_pct": 1.25273228431384,
      "partial": true
    },
    {
      "case": "N503_C_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 12640.69728875743,
      "profit": 321.21028960514377,
      "return_pct": 2.6073349452558015,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-05",
      "start_equity": 12640.69728875743,
      "end_equity": 12869.670459599129,
      "profit": 228.97317084169845,
      "return_pct": 1.811396678610011,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-06",
      "start_equity": 12869.670459599129,
      "end_equity": 13195.051223161678,
      "profit": 325.38076356254896,
      "return_pct": 2.5282757983896564,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-07",
      "start_equity": 13195.051223161678,
      "end_equity": 11252.562401474566,
      "profit": -1942.4888216871113,
      "return_pct": -14.721343546415355,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-08",
      "start_equity": 11252.562401474566,
      "end_equity": 10930.536466725194,
      "profit": -322.025934749372,
      "return_pct": -2.8618009237360242,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-09",
      "start_equity": 10930.536466725194,
      "end_equity": 10800.053011953336,
      "profit": -130.4834547718583,
      "return_pct": -1.1937516074263743,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "month": "2026-10",
      "start_equity": 10800.053011953336,
      "end_equity": 10937.020308525212,
      "profit": 136.96729657187643,
      "return_pct": 1.2682094839745917,
      "partial": true
    },
    {
      "case": "P604_B_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 11796.649318694166,
      "profit": -522.8376804581203,
      "return_pct": -4.243989059723807,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-05",
      "start_equity": 11796.649318694166,
      "end_equity": 11518.143941252854,
      "profit": -278.5053774413118,
      "return_pct": -2.360885450752226,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-06",
      "start_equity": 11518.143941252854,
      "end_equity": 11809.379809873653,
      "profit": 291.235868620799,
      "return_pct": 2.528496519111223,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-07",
      "start_equity": 11809.379809873653,
      "end_equity": 10093.58238460668,
      "profit": -1715.7974252669737,
      "return_pct": -14.529106971666883,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-08",
      "start_equity": 10093.58238460668,
      "end_equity": 9765.418267503335,
      "profit": -328.1641171033443,
      "return_pct": -3.251215520901818,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-09",
      "start_equity": 9765.418267503335,
      "end_equity": 9647.999747970709,
      "profit": -117.4185195326263,
      "return_pct": -1.202391093921329,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "month": "2026-10",
      "start_equity": 9647.999747970709,
      "end_equity": 9768.176813608296,
      "profit": 120.17706563758657,
      "return_pct": 1.2456163845035784,
      "partial": true
    },
    {
      "case": "P604_C_N",
      "month": "2026-01",
      "start_equity": 10000,
      "end_equity": 12164.114978082376,
      "profit": 2164.114978082376,
      "return_pct": 21.641149780823767,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-02",
      "start_equity": 12164.114978082376,
      "end_equity": 12897.326029851978,
      "profit": 733.2110517696019,
      "return_pct": 6.027656373609758,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-03",
      "start_equity": 12897.326029851978,
      "end_equity": 12319.486999152286,
      "profit": -577.8390306996916,
      "return_pct": -4.480301027997847,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-04",
      "start_equity": 12319.486999152286,
      "end_equity": 12640.69728875743,
      "profit": 321.21028960514377,
      "return_pct": 2.6073349452558015,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-05",
      "start_equity": 12640.69728875743,
      "end_equity": 12869.670459599129,
      "profit": 228.97317084169845,
      "return_pct": 1.811396678610011,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-06",
      "start_equity": 12869.670459599129,
      "end_equity": 13195.051223161678,
      "profit": 325.38076356254896,
      "return_pct": 2.5282757983896564,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-07",
      "start_equity": 13195.051223161678,
      "end_equity": 11277.910785224567,
      "profit": -1917.1404379371106,
      "return_pct": -14.529238314527305,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-08",
      "start_equity": 11277.910785224567,
      "end_equity": 10910.46128493155,
      "profit": -367.4495002930162,
      "return_pct": -3.258134483333741,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-09",
      "start_equity": 10910.46128493155,
      "end_equity": 10778.917412745635,
      "profit": -131.54387218591546,
      "return_pct": -1.2056673751053126,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "month": "2026-10",
      "start_equity": 10778.917412745635,
      "end_equity": 10913.664077184385,
      "profit": 134.74666443874958,
      "return_pct": 1.2500945992907964,
      "partial": true
    }
  ],
  "quarterly": [
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
    },
    {
      "case": "N503_B_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 11809.379809873653,
      "profit": -510.1071892786331,
      "return_pct": -4.140652847912696,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "quarter": "2026Q3",
      "start_equity": 11809.379809873653,
      "end_equity": 9664.62142448721,
      "profit": -2144.7583853864435,
      "return_pct": -18.161481973788685,
      "partial": false
    },
    {
      "case": "N503_B_N",
      "quarter": "2026Q4",
      "start_equity": 9664.62142448721,
      "end_equity": 9785.693257228473,
      "profit": 121.07183274126328,
      "return_pct": 1.25273228431384,
      "partial": true
    },
    {
      "case": "N503_C_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 13195.051223161678,
      "profit": 875.5642240093912,
      "return_pct": 7.107148406988362,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "quarter": "2026Q3",
      "start_equity": 13195.051223161678,
      "end_equity": 10800.053011953336,
      "profit": -2394.9982112083417,
      "return_pct": -18.15073068457914,
      "partial": false
    },
    {
      "case": "N503_C_N",
      "quarter": "2026Q4",
      "start_equity": 10800.053011953336,
      "end_equity": 10937.020308525212,
      "profit": 136.96729657187643,
      "return_pct": 1.2682094839745917,
      "partial": true
    },
    {
      "case": "P604_B_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 11809.379809873653,
      "profit": -510.1071892786331,
      "return_pct": -4.140652847912696,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "quarter": "2026Q3",
      "start_equity": 11809.379809873653,
      "end_equity": 9647.999747970709,
      "profit": -2161.3800619029444,
      "return_pct": -18.302231757300625,
      "partial": false
    },
    {
      "case": "P604_B_N",
      "quarter": "2026Q4",
      "start_equity": 9647.999747970709,
      "end_equity": 9768.176813608296,
      "profit": 120.17706563758657,
      "return_pct": 1.2456163845035784,
      "partial": true
    },
    {
      "case": "P604_C_N",
      "quarter": "2026Q1",
      "start_equity": 10000,
      "end_equity": 12319.486999152286,
      "profit": 2319.4869991522864,
      "return_pct": 23.19486999152287,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "quarter": "2026Q2",
      "start_equity": 12319.486999152286,
      "end_equity": 13195.051223161678,
      "profit": 875.5642240093912,
      "return_pct": 7.107148406988362,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "quarter": "2026Q3",
      "start_equity": 13195.051223161678,
      "end_equity": 10778.917412745635,
      "profit": -2416.1338104160423,
      "return_pct": -18.31090891238777,
      "partial": false
    },
    {
      "case": "P604_C_N",
      "quarter": "2026Q4",
      "start_equity": 10778.917412745635,
      "end_equity": 10913.664077184385,
      "profit": 134.74666443874958,
      "return_pct": 1.2500945992907964,
      "partial": true
    }
  ]
}
```
