# R11 N204C — datos completos

Snapshots completos de siete políticas. Neto de trades reconciliado con motor a tolerancia0.01 USDT; identidad de entradas única, comparación de entradas y salidas vsL5. Curvas diarias, extremos parciales marcados. B/C no son muestras independientes.

## Métricas, anuales y atribución

```json
{
  "rows": [
    {
      "case": "L1",
      "leverage": 1,
      "net": 12307.768574629501,
      "return_pct": 123.07768574629499,
      "cagr_pct": 16.63656691119437,
      "dd_engine_pct": -8.182245647817844,
      "dd_curve_pct": -8.182245647817865,
      "calmar": 2.0332519490699044,
      "sharpe": 1.657760787872279,
      "sortino": 2.986015288408941,
      "pf": 1.9033210447635505,
      "trades": 280,
      "fees": 1596.8976281268197,
      "underwater_days_engine": 219,
      "curve_terminal": 22307.768574629506,
      "wallet_terminal_engine": 22307.768574629506,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 12307.768574629506,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 1888.0956663202141,
      "worst_observed_month_delta": -619.2726655700426,
      "observed_net_ex_best_month": 10419.672908309292
    },
    {
      "case": "L2",
      "leverage": 2,
      "net": 13011.721110365677,
      "return_pct": 130.11721110365676,
      "cagr_pct": 17.333685612799865,
      "dd_engine_pct": -9.466809482887474,
      "dd_curve_pct": -9.46680948288744,
      "calmar": 1.83099550531072,
      "sharpe": 1.5634867188419888,
      "sortino": 2.7192960668244948,
      "pf": 1.8001212946335736,
      "trades": 280,
      "fees": 1974.5337766809942,
      "underwater_days_engine": 220,
      "curve_terminal": 23011.72111036567,
      "wallet_terminal_engine": 23011.72111036567,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13011.72111036567,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 2007.3108320661086,
      "worst_observed_month_delta": -810.7594475335245,
      "observed_net_ex_best_month": 11004.410278299561
    },
    {
      "case": "L3",
      "leverage": 3,
      "net": 13239.619171923641,
      "return_pct": 132.3961917192364,
      "cagr_pct": 17.55567750901328,
      "dd_engine_pct": -9.057235280291742,
      "dd_curve_pct": -9.057235280291732,
      "calmar": 1.9383042358647653,
      "sharpe": 1.5693937539620852,
      "sortino": 2.7272080768780214,
      "pf": 1.8049692385580105,
      "trades": 280,
      "fees": 2012.6368192497744,
      "underwater_days_engine": 219,
      "curve_terminal": 23239.619171923638,
      "wallet_terminal_engine": 23239.619171923638,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13239.619171923638,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 2032.9786450637184,
      "worst_observed_month_delta": -887.565188090517,
      "observed_net_ex_best_month": 11206.64052685992
    },
    {
      "case": "L4",
      "leverage": 4,
      "net": 13237.646261527316,
      "return_pct": 132.37646261527317,
      "cagr_pct": 17.55376329302818,
      "dd_engine_pct": -9.057883731399553,
      "dd_curve_pct": -9.057883731399608,
      "calmar": 1.9379541417800814,
      "sharpe": 1.5694223697243939,
      "sortino": 2.7272029070462316,
      "pf": 1.8048705060594152,
      "trades": 280,
      "fees": 2012.4979153240956,
      "underwater_days_engine": 219,
      "curve_terminal": 23237.64626152735,
      "wallet_terminal_engine": 23237.64626152735,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13237.646261527349,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 2032.966018077277,
      "worst_observed_month_delta": -887.4993053132093,
      "observed_net_ex_best_month": 11204.680243450071
    },
    {
      "case": "L5",
      "leverage": 5,
      "net": 13239.442379846789,
      "return_pct": 132.3944237984679,
      "cagr_pct": 17.555505981887354,
      "dd_engine_pct": -9.057883731399553,
      "dd_curve_pct": -9.057883731399608,
      "calmar": 1.9381465364840598,
      "sharpe": 1.569754072854379,
      "sortino": 2.7281116510374783,
      "pf": 1.8050568929499935,
      "trades": 280,
      "fees": 2012.4242239197674,
      "underwater_days_engine": 219,
      "curve_terminal": 23239.442379846816,
      "wallet_terminal_engine": 23239.442379846816,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13239.442379846816,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 2032.966018077277,
      "worst_observed_month_delta": -887.5608787233687,
      "observed_net_ex_best_month": 11206.476361769539
    },
    {
      "case": "M5A15",
      "leverage": 5,
      "net": 6350.891394697322,
      "return_pct": 63.50891394697321,
      "cagr_pct": 9.88989621083103,
      "dd_engine_pct": -6.476548181638431,
      "dd_curve_pct": -6.476548181638442,
      "calmar": 1.5270319826956174,
      "sharpe": 1.441941612053119,
      "sortino": 2.559808124770346,
      "pf": 1.7438967809323398,
      "trades": 280,
      "fees": 820.5071194133432,
      "underwater_days_engine": 220,
      "curve_terminal": 16350.891394697323,
      "wallet_terminal_engine": 16350.891394697323,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 6350.8913946973225,
      "positive_full_months": 42,
      "complete_months": 61,
      "best_observed_month_delta": 1032.8646606396323,
      "worst_observed_month_delta": -408.9607030306033,
      "observed_net_ex_best_month": 5318.02673405769
    },
    {
      "case": "R5A15",
      "leverage": 5,
      "net": 43833.91902366031,
      "return_pct": 438.33919023660303,
      "cagr_pct": 38.10783184897173,
      "dd_engine_pct": -18.56750789132976,
      "dd_curve_pct": -18.567507891329726,
      "calmar": 2.0523934645406277,
      "sharpe": 1.5699080703488808,
      "sortino": 2.6750315516460867,
      "pf": 1.8737189791325901,
      "trades": 280,
      "fees": 6120.456588976929,
      "underwater_days_engine": 229,
      "curve_terminal": 53833.9190236603,
      "wallet_terminal_engine": 53833.9190236603,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 43833.9190236603,
      "positive_full_months": 39,
      "complete_months": 61,
      "best_observed_month_delta": 5111.197542692495,
      "worst_observed_month_delta": -3833.2771274577826,
      "observed_net_ex_best_month": 38722.72148096781
    }
  ],
  "annual": [
    {
      "case": "L1",
      "year": 2020,
      "return_pct": 3.981733218081418,
      "equity_delta": 398.1733218081408,
      "partial": true
    },
    {
      "case": "L1",
      "year": 2021,
      "return_pct": 20.38213887484901,
      "equity_delta": 2119.370126898435,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2022,
      "return_pct": 9.677460573606766,
      "equity_delta": 1211.3803320326751,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2023,
      "return_pct": 19.689410576361908,
      "equity_delta": 2703.144170905538,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2024,
      "return_pct": 12.566842498254239,
      "equity_delta": 2064.992098689312,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2025,
      "return_pct": 20.601698399236025,
      "equity_delta": 3810.7085242954054,
      "partial": true
    },
    {
      "case": "L2",
      "year": 2020,
      "return_pct": 3.986501604552717,
      "equity_delta": 398.65016045527227,
      "partial": true
    },
    {
      "case": "L2",
      "year": 2021,
      "return_pct": 18.26351954002039,
      "equity_delta": 1899.1595039531094,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2022,
      "return_pct": 11.179858428086442,
      "equity_delta": 1374.8777102363892,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2023,
      "return_pct": 23.36332720348777,
      "equity_delta": 3194.3946888482205,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2024,
      "return_pct": 15.637424380271048,
      "equity_delta": 2637.5772028369793,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2025,
      "return_pct": 17.98063629898823,
      "equity_delta": 3507.0618440356993,
      "partial": true
    },
    {
      "case": "L3",
      "year": 2020,
      "return_pct": 3.986501604552717,
      "equity_delta": 398.65016045527227,
      "partial": true
    },
    {
      "case": "L3",
      "year": 2021,
      "return_pct": 18.719907379832136,
      "equity_delta": 1946.617678789993,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2022,
      "return_pct": 11.158646312737153,
      "equity_delta": 1377.564774541468,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2023,
      "return_pct": 23.93222711828935,
      "equity_delta": 3284.1794681941246,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2024,
      "return_pct": 16.14683221514688,
      "equity_delta": 2746.0937056872062,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2025,
      "return_pct": 17.650456701508755,
      "equity_delta": 3486.5133842555733,
      "partial": true
    },
    {
      "case": "L4",
      "year": 2020,
      "return_pct": 3.9838234606026868,
      "equity_delta": 398.3823460602689,
      "partial": true
    },
    {
      "case": "L4",
      "year": 2021,
      "return_pct": 18.711231761296542,
      "equity_delta": 1945.6654201970814,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2022,
      "return_pct": 11.156549325981091,
      "equity_delta": 1377.1697778651687,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2023,
      "return_pct": 23.934621951238167,
      "equity_delta": 3284.121546292692,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2024,
      "return_pct": 16.147676230071518,
      "equity_delta": 2745.9670981460367,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2025,
      "return_pct": 17.65118741860818,
      "equity_delta": 3486.3400729661007,
      "partial": true
    },
    {
      "case": "L5",
      "year": 2020,
      "return_pct": 3.9838234606026868,
      "equity_delta": 398.3823460602689,
      "partial": true
    },
    {
      "case": "L5",
      "year": 2021,
      "return_pct": 18.711231761296542,
      "equity_delta": 1945.6654201970814,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2022,
      "return_pct": 11.156549325981091,
      "equity_delta": 1377.1697778651687,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2023,
      "return_pct": 23.934621951238167,
      "equity_delta": 3284.121546292692,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2024,
      "return_pct": 16.14791972366636,
      "equity_delta": 2746.0085050575035,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2025,
      "return_pct": 17.660034423036652,
      "equity_delta": 3488.0947843741014,
      "partial": true
    },
    {
      "case": "M5A15",
      "year": 2020,
      "return_pct": 4.051473996587585,
      "equity_delta": 405.1473996587574,
      "partial": true
    },
    {
      "case": "M5A15",
      "year": 2021,
      "return_pct": 20.245975314122823,
      "equity_delta": 2106.623573933004,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2022,
      "return_pct": 5.054966521810278,
      "equity_delta": 632.465834000639,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2023,
      "return_pct": 7.227734371959937,
      "equity_delta": 950.0305216741654,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2024,
      "return_pct": 9.23914559550154,
      "equity_delta": 1302.1898791701442,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2025,
      "return_pct": 6.1990506863982775,
      "equity_delta": 954.4341862606125,
      "partial": true
    },
    {
      "case": "R5A15",
      "year": 2020,
      "return_pct": 9.553189636037175,
      "equity_delta": 955.3189636037168,
      "partial": true
    },
    {
      "case": "R5A15",
      "year": 2021,
      "return_pct": 55.62287172873219,
      "equity_delta": 6093.663014598769,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2022,
      "return_pct": 10.593367649223474,
      "equity_delta": 1806.061341400844,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2023,
      "return_pct": 37.5960716088501,
      "equity_delta": 7088.755588317774,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2024,
      "return_pct": 37.694272865120396,
      "equity_delta": 9779.326351929907,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2025,
      "return_pct": 50.69767449536084,
      "equity_delta": 18110.79376380929,
      "partial": true
    }
  ],
  "fills": [
    {
      "case": "L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9038.228165429167,
          "fees": 1057.5438644786084
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 1603.1607636798335,
          "fees": 203.45179029181722
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1666.379645520496,
          "fees": 335.9019733563946
        }
      },
      "entry_notional_sum": 1772095.7559422115,
      "entry_notional_turnover_initial_equity": 177.20957559422115,
      "time_weighted_entry_notional_over_initial_equity": 0.37701805381872466
    },
    {
      "case": "L2",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9065.745896552095,
          "fees": 1255.7515403543116
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 1969.7256443226947,
          "fees": 272.41789731895875
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1976.2495694908873,
          "fees": 446.3643390077244
        }
      },
      "entry_notional_sum": 2191732.9397302507,
      "entry_notional_turnover_initial_equity": 219.17329397302507,
      "time_weighted_entry_notional_over_initial_equity": 0.47834174332975404
    },
    {
      "case": "L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9189.391973780348,
          "fees": 1268.5468227959254
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2035.4760959837363,
          "fees": 280.7890895879873
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2014.7511021595576,
          "fees": 463.3009068658616
        }
      },
      "entry_notional_sum": 2234039.0175696407,
      "entry_notional_turnover_initial_equity": 223.40390175696407,
      "time_weighted_entry_notional_over_initial_equity": 0.4927059397461788
    },
    {
      "case": "L4",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9187.733877247454,
          "fees": 1268.4869242178015
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2035.3444372428262,
          "fees": 280.75388761145445
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2014.5679470370371,
          "fees": 463.2571034948395
        }
      },
      "entry_notional_sum": 2233885.283048578,
      "entry_notional_turnover_initial_equity": 223.3885283048578,
      "time_weighted_entry_notional_over_initial_equity": 0.49265698486304577
    },
    {
      "case": "L5",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9189.421279511538,
          "fees": 1268.3982916641712
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2035.4301531490387,
          "fees": 280.7511694974209
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2014.5909471862112,
          "fees": 463.2747627581751
        }
      },
      "entry_notional_sum": 2233802.5424969783,
      "entry_notional_turnover_initial_equity": 223.38025424969783,
      "time_weighted_entry_notional_over_initial_equity": 0.49265415546712815
    },
    {
      "case": "M5A15",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 5242.608626077985,
          "fees": 640.1006957690144
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 432.30440837606983,
          "fees": 58.23160872070355
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 675.978360243268,
          "fees": 122.1748149236251
        }
      },
      "entry_notional_sum": 910541.4516098766,
      "entry_notional_turnover_initial_equity": 91.05414516098766,
      "time_weighted_entry_notional_over_initial_equity": 0.1601874101456795
    },
    {
      "case": "R5A15",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 24596.58923438946,
          "fees": 3337.074115556069
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 7005.585574273632,
          "fees": 978.3890024416718
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 12231.744214997212,
          "fees": 1804.9934709791892
        }
      },
      "entry_notional_sum": 6788235.645302936,
      "entry_notional_turnover_initial_equity": 678.8235645302937,
      "time_weighted_entry_notional_over_initial_equity": 1.7630169163622897
    }
  ],
  "engine_metrics": {
    "L1": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 22307.768574629506,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.697556607491815,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 1596.8976281268197,
      "net_profit": 12307.7685746295,
      "net_profit_percentage": 123.07768574629499,
      "average_win": 175.2215539473761,
      "average_loss": 103.21985916350124,
      "expectancy": 43.9563163379625,
      "expectancy_percentage": 0.439563163379625,
      "expected_net_profit_every_100_trades": 43.9563163379625,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 25932.78998421166,
      "gross_loss": -13625.021409582163,
      "max_drawdown": -8.182245647817844,
      "max_underwater_period": 219,
      "annual_return": 16.63656691119437,
      "annualization": 365,
      "sharpe_ratio": 1.657760787872279,
      "calmar_ratio": 2.0332519490699044,
      "sortino_ratio": 2.986015288408941,
      "omega_ratio": 1.440473860887152,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -80.16525000000183,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -212.84749197532315,
      "largest_winning_trade": 2007.7867257670353,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "L2": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 23011.72111036567,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6055135871056199,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 1974.5337766809942,
      "net_profit": 13011.721110365677,
      "net_profit_percentage": 130.11721110365676,
      "average_win": 197.7966679290321,
      "average_loss": 123.19837684190206,
      "expectancy": 46.47043253702029,
      "expectancy_percentage": 0.4647043253702029,
      "expected_net_profit_every_100_trades": 46.47043253702029,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 29273.906853496752,
      "gross_loss": -16262.185743131073,
      "max_drawdown": -9.466809482887474,
      "max_underwater_period": 220,
      "annual_return": 17.333685612799865,
      "annualization": 365,
      "sharpe_ratio": 1.5634867188419888,
      "calmar_ratio": 1.83099550531072,
      "sortino_ratio": 2.7192960668244948,
      "omega_ratio": 1.4026567417242317,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -117.27100000000064,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -221.1593530022147,
      "largest_winning_trade": 1991.5687392907264,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "L3": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 23239.619171923638,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6098374289841717,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 2012.6368192497744,
      "net_profit": 13239.619171923641,
      "net_profit_percentage": 132.3961917192364,
      "average_win": 200.5876997636796,
      "average_loss": 124.60121509924953,
      "expectancy": 47.284354185441586,
      "expectancy_percentage": 0.4728435418544159,
      "expected_net_profit_every_100_trades": 47.28435418544159,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 29686.979565024583,
      "gross_loss": -16447.36039310094,
      "max_drawdown": -9.057235280291742,
      "max_underwater_period": 219,
      "annual_return": 17.55567750901328,
      "annualization": 365,
      "sharpe_ratio": 1.5693937539620852,
      "calmar_ratio": 1.9383042358647653,
      "sortino_ratio": 2.7272080768780214,
      "omega_ratio": 1.405418024526862,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -118.76974999999948,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -223.99268285843212,
      "largest_winning_trade": 1998.0559338812498,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "L4": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 23237.64626152735,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.609749370269208,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 2012.4979153240956,
      "net_profit": 13237.646261527316,
      "net_profit_percentage": 132.37646261527317,
      "average_win": 200.57143931016444,
      "average_loss": 124.59792997255323,
      "expectancy": 47.27730807688326,
      "expectancy_percentage": 0.4727730807688326,
      "expected_net_profit_every_100_trades": 47.27730807688326,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 29684.57301790434,
      "gross_loss": -16446.926756377026,
      "max_drawdown": -9.057883731399553,
      "max_underwater_period": 219,
      "annual_return": 17.55376329302818,
      "annualization": 365,
      "sharpe_ratio": 1.5694223697243939,
      "calmar_ratio": 1.9379541417800814,
      "sortino_ratio": 2.7272029070462316,
      "omega_ratio": 1.4054108078195822,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -118.75874999999724,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -223.96987939882473,
      "largest_winning_trade": 1998.0559338812498,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "L5": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 23239.442379846816,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6099156072256704,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 2012.4242239197674,
      "net_profit": 13239.442379846789,
      "net_profit_percentage": 132.3944237984679,
      "average_win": 200.57292153053464,
      "average_loss": 124.58598489903284,
      "expectancy": 47.28372278516712,
      "expectancy_percentage": 0.4728372278516712,
      "expected_net_profit_every_100_trades": 47.28372278516712,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 29684.792386519126,
      "gross_loss": -16445.350006672335,
      "max_drawdown": -9.057883731399553,
      "max_underwater_period": 219,
      "annual_return": 17.555505981887354,
      "annualization": 365,
      "sharpe_ratio": 1.569754072854379,
      "calmar_ratio": 1.9381465364840598,
      "sortino_ratio": 2.7281116510374783,
      "omega_ratio": 1.4054903057639654,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -118.76974999999948,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -223.9869819935303,
      "largest_winning_trade": 1998.0559338812498,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "M5A15": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 16350.891394697323,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.5553673992099246,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 820.5071194133432,
      "net_profit": 6350.891394697321,
      "net_profit_percentage": 63.50891394697321,
      "average_win": 100.59608223870934,
      "average_loss": 64.67673315630046,
      "expectancy": 22.681754981061868,
      "expectancy_percentage": 0.2268175498106187,
      "expected_net_profit_every_100_trades": 22.681754981061868,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 14888.220171328983,
      "gross_loss": -8537.32877663166,
      "max_drawdown": -6.476548181638431,
      "max_underwater_period": 220,
      "annual_return": 9.88989621083103,
      "annualization": 365,
      "sharpe_ratio": 1.441941612053119,
      "calmar_ratio": 1.5270319826956174,
      "sortino_ratio": 2.559808124770346,
      "omega_ratio": 1.3935702767105342,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -16.293750000000273,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -152.5668440230159,
      "largest_winning_trade": 904.4621850848553,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R5A15": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 53833.9190236603,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6711547651723102,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 6120.456588976929,
      "net_profit": 43833.9190236603,
      "net_profit_percentage": 438.33919023660303,
      "average_win": 635.1572676606914,
      "average_loss": 380.0708832585002,
      "expectancy": 156.54971079878683,
      "expectancy_percentage": 1.5654971079878683,
      "expected_net_profit_every_100_trades": 156.54971079878683,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 94003.27561378233,
      "gross_loss": -50169.35659012203,
      "max_drawdown": -18.56750789132976,
      "max_underwater_period": 229,
      "annual_return": 38.10783184897173,
      "annualization": 365,
      "sharpe_ratio": 1.5699080703488808,
      "calmar_ratio": 2.0523934645406277,
      "sortino_ratio": 2.6750315516460867,
      "omega_ratio": 1.4110599921059355,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -548.443499999994,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -2061.8319206539004,
      "largest_winning_trade": 7339.398025650299,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    }
  }
}
```

## Todos los meses de equity observada

```csv
case,month,return_pct,equity_delta,partial
L1,2020-10,-1.908913302195192,-190.89133021951966,True
L1,2020-11,0.25973959100202837,25.478138739832502,False
L1,2020-12,5.730657772012937,563.586513287828,False
L1,2021-01,1.012755871364468,105.30811083126537,False
L1,2021-02,8.528584772264525,895.7983180217161,False
L1,2021-03,0.3670642609819863,41.84268197403435,False
L1,2021-04,-3.797704304189198,-434.4999990717406,False
L1,2021-05,-1.0372478185785017,-114.16595109130867,False
L1,2021-06,1.0024157936802336,109.18770410004618,False
L1,2021-07,6.257223066189788,688.397417702321,False
L1,2021-08,-3.6422152462477597,-425.77647760359105,False
L1,2021-09,-0.9193216720993047,-103.55483051221017,False
L1,2021-10,6.967815408803912,777.6576917477087,False
L1,2021-11,3.2950236308076253,393.372046334287,False
L1,2021-12,1.5067088176526466,185.80341446590683,False
L1,2022-01,-0.4698130633856601,-58.80905433699991,False
L1,2022-02,-1.5936771360446134,-198.55200148359472,False
L1,2022-03,4.729834225132823,579.8863028824289,False
L1,2022-04,0.2719119496474631,34.913681126736265,False
L1,2022-05,0.23230768586275374,29.909573615002955,False
L1,2022-06,0.3022535275049698,39.00549114112255,False
L1,2022-07,-0.9723124864431276,-125.85513105756763,False
L1,2022-08,-0.933553809720522,-119.66332232213608,False
L1,2022-09,2.4583703838850335,312.1731882811491,False
L1,2022-10,0.450953661834097,58.671561465000195,False
L1,2022-11,0.9774723133416874,127.74804360780217,False
L1,2022-12,4.030864109707211,531.9519991137313,False
L1,2023-01,13.752685181114366,1888.0956663202141,False
L1,2023-02,0.9157902155533693,143.01913605723712,False
L1,2023-03,0.09354454947283486,14.742657089320346,False
L1,2023-04,0.3728219738496019,58.81185079019269,False
L1,2023-05,-0.7875651227718383,-124.69985686629843,False
L1,2023-06,2.8253848465974674,443.8366890052803,False
L1,2023-07,-2.1586943778041046,-348.68807271260084,False
L1,2023-08,0.7244550729631483,114.49318291860618,False
L1,2023-09,-0.23572746172529913,-37.52435857794808,False
L1,2023-10,-1.3482156225816722,-214.1102669410211,False
L1,2023-11,0.9301539334159781,145.72629038772357,False
L1,2023-12,3.9173836533114015,619.4412534348321,False
L1,2024-01,-0.38364981838266976,-63.04159885300214,False
L1,2024-02,-0.9019633261803994,-147.64261455498672,False
L1,2024-03,2.400002007692259,389.31353539315023,False
L1,2024-04,3.263648646165196,542.1147966894241,False
L1,2024-05,0.7402195560709535,126.9684693606032,False
L1,2024-06,-2.1856427015585767,-377.67426221085407,False
L1,2024-07,-2.916724950193439,-492.9879509031525,False
L1,2024-08,0.6673604970076852,109.50797361875084,False
L1,2024-09,2.6458022209279397,437.05018151707554,False
L1,2024-10,1.2464455092135784,211.34326806295576,False
L1,2024-11,6.898603903350309,1184.2846945461897,False
L1,2024-12,0.7942520187895541,145.75560602315818,False
L1,2025-01,4.1831615603251215,773.7619058158307,False
L1,2025-02,1.4405057446459146,277.59729731882544,False
L1,2025-03,2.878412892036386,562.684219981169,False
L1,2025-04,0.8773742887761227,176.4496510652134,False
L1,2025-05,3.6199679497326276,734.4029208924294,False
L1,2025-06,1.285825047061051,270.30557621401385,False
L1,2025-07,1.8185268014594191,387.2054842260477,False
L1,2025-08,2.350845841466298,509.6508509098712,False
L1,2025-09,0.9629279426552229,213.6652170343441,False
L1,2025-10,1.9869855122897073,445.1400560129223,False
L1,2025-11,0.346280970918067,79.11801039478087,False
L1,2025-12,-2.7010579301625204,-619.2726655700426,True
L2,2020-10,-1.908913302195192,-190.89133021951966,True
L2,2020-11,0.2646114909586661,25.95602870086259,False
L2,2020-12,5.730368627477911,563.5854619739293,False
L2,2021-01,1.0127203721846056,105.30924860713822,False
L2,2021-02,8.342740337481235,876.318058652505,False
L2,2021-03,0.3676771686168312,41.84268197403435,False
L2,2021-04,-5.117665765407297,-584.5459325843203,False
L2,2021-05,-1.0584881327735385,-114.7144369685775,False
L2,2021-06,1.0042967671014091,107.68933411272337,False
L2,2021-07,6.285969143328396,680.8049753747055,False
L2,2021-08,-3.648984804533395,-420.04756152639493,False
L2,2021-09,-0.9193150463384869,-101.96404974831967,False
L2,2021-10,7.325191544754106,804.9903860480754,False
L2,2021-11,2.70460919015838,318.9906105683476,False
L2,2021-12,1.523002253051975,184.48618944319242,False
L2,2022-01,-0.46937993695380653,-57.7234512494997,False
L2,2022-02,-1.5867951153017756,-194.22509013913077,False
L2,2022-03,4.732138286835186,570.0268061814131,False
L2,2022-04,1.6293482753324318,205.55675239231095,False
L2,2022-05,0.23754861820466378,30.457164675000968,False
L2,2022-06,0.3093401306061727,39.75608995662333,False
L2,2022-07,-0.9734255410741466,-125.49069101912755,False
L2,2022-08,-0.9431274036159953,-120.40122168098605,False
L2,2022-09,2.4643136589571846,311.63133939749423,False
L2,2022-10,0.4510138604471914,58.43965805999869,False
L2,2022-11,0.9743488848686477,126.81966287026262,False
L2,2022-12,4.032903723668246,530.0306907920294,False
L2,2023-01,14.681172596607105,2007.3108320661086,False
L2,2023-02,0.9169193296935108,143.7729344529289,False
L2,2023-03,0.09006903311241654,14.252317668766409,False
L2,2023-04,0.3712546917911119,58.79940517789146,False
L2,2023-05,-1.1371626157964831,-180.77272670891398,False
L2,2023-06,4.419696360268488,694.6016958962882,False
L2,2023-07,-1.7966693958111457,-294.8451591401863,False
L2,2023-08,0.7243595912455048,116.73639135012127,False
L2,2023-09,-0.6470836181294848,-105.0381269820682,False
L2,2023-10,-1.3473021434646792,-217.28621972278233,False
L2,2023-11,0.37932131677789194,60.35085114602771,False
L2,2023-12,5.613528620397967,896.5124936440388,False
L2,2024-01,-0.3787638251612768,-63.88640521677735,False
L2,2024-02,-0.7928790975522682,-133.2290260952832,False
L2,2024-03,2.3890841983681854,398.25953868268334,False
L2,2024-04,3.4553981264013878,589.7751673179737,False
L2,2024-05,1.3277238048689632,234.4494872311152,False
L2,2024-06,-2.1870577919928635,-391.318239955679,False
L2,2024-07,-2.085785408412677,-365.03606977441814,False
L2,2024-08,1.189919974752618,203.90583533299287,False
L2,2024-09,2.798661168009775,485.2879123298553,False
L2,2024-10,1.32905536204313,236.90797604474574,False
L2,2024-11,7.147563204188123,1291.0070352261682,False
L2,2024-12,0.7825783355496663,151.4539917136026,False
L2,2025-01,3.57188188373756,696.68339081878,False
L2,2025-02,2.2119450688553144,446.8426027473688,False
L2,2025-03,3.6761663807217237,759.0616447534376,False
L2,2025-04,0.5827652906004399,124.75400463343249,False
L2,2025-05,3.649789137539572,785.8726302819305,False
L2,2025-06,1.3873465555141573,309.6262498151591,False
L2,2025-07,0.008380384902650917,1.8962715761954314,False
L2,2025-08,2.345171138161617,530.6980651618287,False
L2,2025-09,0.9405115214387916,217.82335363221137,False
L2,2025-10,1.5500068071063966,362.3593122958446,False
L2,2025-11,0.34626287879075957,82.20376585303529,False
L2,2025-12,-3.4033376396845783,-810.7594475335245,True
L3,2020-10,-1.908913302195192,-190.89133021951966,True
L3,2020-11,0.2646114909586661,25.95602870086259,False
L3,2020-12,5.730368627477911,563.5854619739293,False
L3,2021-01,1.0127203721846056,105.30924860713822,False
L3,2021-02,8.342740337481235,876.318058652505,False
L3,2021-03,0.3676771686168312,41.84268197403435,False
L3,2021-04,-4.690506018306428,-535.7552330393519,False
L3,2021-05,-1.0580134051336176,-115.17920014991614,False
L3,2021-06,0.9997908953306878,107.68933411272337,False
L3,2021-07,6.25691901562504,680.6824017278559,False
L3,2021-08,-3.6435809464243407,-421.1818328244444,False
L3,2021-09,-0.9193184481411376,-102.39714189346341,False
L3,2021-10,7.318848345000628,807.706528164088,False
L3,2021-11,2.700754166862507,319.8688163038478,False
L3,2021-12,1.49392208735053,181.71401715497632,False
L3,2022-01,-0.47520839281430804,-58.66574888749892,False
L3,2022-02,-1.5843424737828848,-194.66185550223418,False
L3,2022-03,4.736140912480291,572.6913285756582,False
L3,2022-04,1.6150224369483324,204.53664130625475,False
L3,2022-05,0.2324126403444593,29.909573615001136,False
L3,2022-06,0.30238976624035185,39.00549114112255,False
L3,2022-07,-0.9727494284591409,-125.85513105756581,False
L3,2022-08,-0.9339774552027613,-119.66332232213608,False
L3,2022-09,2.4594965068433616,312.1731882811491,False
L3,2022-10,0.4493720522493305,58.43965805999869,False
L3,2022-11,0.9753502424344029,127.41173500039258,False
L3,2022-12,4.035022244222097,532.243216331326,False
L3,2023-01,14.814570011014139,2032.9786450637184,False
L3,2023-02,0.9160930083814911,144.33788535611166,False
L3,2023-03,0.09289740851561312,14.770826505086006,False
L3,2023-04,0.36826265661071833,58.60870708161201,False
L3,2023-05,-1.1340720241938995,-181.1513200114423,False
L3,2023-06,4.421537366457029,698.2658659262215,False
L3,2023-07,-1.5025808620644843,-247.78524911077147,False
L3,2023-08,0.7263362017779995,117.97775767288476,False
L3,2023-09,-0.6460981421103185,-105.70705569991878,False
L3,2023-10,-1.3503398465084748,-219.49947962095393,False
L3,2023-11,0.38107037872394667,61.10703291158279,False
L3,2023-12,5.655033660993669,910.2758521199939,False
L3,2024-01,-0.37439000069955375,-63.67255265270069,False
L3,2024-02,-0.7902970741410553,-133.9027165620646,False
L3,2024-03,2.384318899447191,400.7905788174139,False
L3,2024-04,3.4492912294928235,593.6308639936615,False
L3,2024-05,1.3780986344318569,245.35472749629116,False
L3,2024-06,-2.182257690303857,-393.8803383624436,False
L3,2024-07,-1.764761817761562,-311.5745693126519,False
L3,2024-08,1.1996546155435661,208.06519426022714,False
L3,2024-09,2.803809599490137,492.11970572022983,False
L3,2024-10,1.334334686944194,240.76659001291046,False
L3,2024-11,7.170494795300475,1311.1041477222207,False
L3,2024-12,0.8026820261556544,157.29207455411233,False
L3,2025-01,3.5692533156509,705.0383832703737,False
L3,2025-02,2.215448647575502,453.23967835410076,False
L3,2025-03,3.6714993786306938,767.7613280898549,False
L3,2025-04,0.5964896938327025,129.31386669411586,False
L3,2025-05,3.6436162625196333,794.6165603349073,False
L3,2025-06,1.3867454996423945,313.4471337249415,False
L3,2025-07,0.0010404813507891575,0.23844214533892227,False
L3,2025-08,2.3593202647433253,540.6797905492167,False
L3,2025-09,0.9336209468413514,219.00358249662168,False
L3,2025-10,1.5521168194147394,367.48607815159994,False
L3,2025-11,0.34625673235815224,83.25372853501904,False
L3,2025-12,-3.678693604884431,-887.565188090517,True
L4,2020-10,-1.908913302195192,-190.89133021951966,True
L4,2020-11,0.2646114909586661,25.95602870086259,False
L4,2020-12,5.72764557070895,563.317647578926,False
L4,2021-01,1.0034076265094338,104.33816149397899,False
L4,2021-02,8.343828785627316,876.3290169832944,False
L4,2021-03,0.3677168456276192,41.84268197403435,False
L4,2021-04,-4.690805626722138,-535.7318542449157,False
L4,2021-05,-1.058026347205654,-115.16786446256447,False
L4,2021-06,0.9999016641345948,107.68933411272337,False
L4,2021-07,6.257632456561457,680.6853482097522,False
L4,2021-08,-3.6439561628827555,-421.1818328244444,False
L4,2021-09,-0.9193232214755542,-102.38673102458961,False
L4,2021-10,7.319437024610997,807.6851347791362,False
L4,2021-11,2.700869302752862,319.8500080456997,False
L4,2021-12,1.4940719511860712,181.71401715497632,False
L4,2022-01,-0.47525536192319917,-58.66574888749892,False
L4,2022-02,-1.5844003712222499,-194.64963828928012,False
L4,2022-03,4.736616776403535,572.691658257585,False
L4,2022-04,1.6151548745109823,204.53391061906405,False
L4,2022-05,0.23243449921088732,29.909573615002955,False
L4,2022-06,0.3024181406413362,39.00549114112255,False
L4,2022-07,-0.972840430093791,-125.85513105756763,False
L4,2022-08,-0.9340656880471809,-119.66332232213608,False
L4,2022-09,2.4597310462149746,312.1731882811491,False
L4,2022-10,0.449413875943927,58.43965805999869,False
L4,2022-11,0.9730826989446051,127.10374496640361,False
L4,2022-12,4.034752617552262,532.1463934813255,False
L4,2023-01,14.81622174956403,2032.966018077277,False
L4,2023-02,0.9161876576227801,144.33788535611166,False
L4,2023-03,0.09299038023071748,14.784095545142918,False
L4,2023-04,0.36830001738401563,58.60870708161201,False
L4,2023-05,-1.134090987604186,-181.13604005919115,False
L4,2023-06,4.4217760719105215,698.2328524636996,False
L4,2023-07,-1.5027390042826383,-247.78680065797744,False
L4,2023-08,0.7264092642907283,117.97775767288658,False
L4,2023-09,-0.6460731461118252,-105.69241116683224,False
L4,2023-10,-1.3503826148268727,-219.48456805152455,False
L4,2023-11,0.38106198356844256,61.09957386474525,False
L4,2023-12,5.6552185707276825,910.2144761667423,False
L4,2024-01,-0.3744268333266465,-63.67255265270069,False
L4,2024-02,-0.7904412049896226,-133.9139131264128,False
L4,2024-03,2.384288751430197,400.745355197414,False
L4,2024-04,3.4493036848284975,593.5733549220349,False
L4,2024-05,1.3780801195372616,245.3268059301081,False
L4,2024-06,-2.182477137657246,-393.8803383624436,False
L4,2024-07,-1.7651317293754465,-311.60784407975007,False
L4,2024-08,1.2001616918555946,208.13095995492768,False
L4,2024-09,2.8039752003367058,492.0987949952287,False
L4,2024-10,1.3343069956359033,240.73753235554614,False
L4,2024-11,7.171392395456566,1311.136868457972,False
L4,2024-12,0.8027557479489023,157.29207455411233,False
L4,2025-01,3.5691078592748227,704.9454214853758,False
L4,2025-02,2.21569130237087,453.2473877149023,False
L4,2025-03,3.6717105797972938,767.736286883417,False
L4,2025-04,0.5962332042271479,129.2468745254955,False
L4,2025-05,3.6439465776039848,794.6165603349145,False
L4,2025-06,1.3869330421111492,313.46210602097926,False
L4,2025-07,0.000812011319206718,0.18606882765016053,False
L4,2025-08,2.3595276571980683,540.6797905492167,False
L4,2025-09,0.9336176499857407,218.98400340972148,False
L4,2025-10,1.5522621807900983,367.4889236396084,False
L4,2025-11,0.3462536498016311,83.24595488802879,False
L4,2025-12,-3.678731400207824,-887.4993053132093,True
L5,2020-10,-1.908913302195192,-190.89133021951966,True
L5,2020-11,0.2646114909586661,25.95602870086259,False
L5,2020-12,5.72764557070895,563.317647578926,False
L5,2021-01,1.0034076265094338,104.33816149397899,False
L5,2021-02,8.343828785627316,876.3290169832944,False
L5,2021-03,0.3677168456276192,41.84268197403435,False
L5,2021-04,-4.690805626722138,-535.7318542449157,False
L5,2021-05,-1.058026347205654,-115.16786446256447,False
L5,2021-06,0.9999016641345948,107.68933411272337,False
L5,2021-07,6.257632456561457,680.6853482097522,False
L5,2021-08,-3.6439561628827555,-421.1818328244444,False
L5,2021-09,-0.9193232214755542,-102.38673102458961,False
L5,2021-10,7.319437024610997,807.6851347791362,False
L5,2021-11,2.700869302752862,319.8500080456997,False
L5,2021-12,1.4940719511860712,181.71401715497632,False
L5,2022-01,-0.47525536192319917,-58.66574888749892,False
L5,2022-02,-1.5844003712222499,-194.64963828928012,False
L5,2022-03,4.736616776403535,572.691658257585,False
L5,2022-04,1.6151548745109823,204.53391061906405,False
L5,2022-05,0.23243449921088732,29.909573615002955,False
L5,2022-06,0.3024181406413362,39.00549114112255,False
L5,2022-07,-0.972840430093791,-125.85513105756763,False
L5,2022-08,-0.9340656880471809,-119.66332232213608,False
L5,2022-09,2.4597310462149746,312.1731882811491,False
L5,2022-10,0.449413875943927,58.43965805999869,False
L5,2022-11,0.9730826989446051,127.10374496640361,False
L5,2022-12,4.034752617552262,532.1463934813255,False
L5,2023-01,14.81622174956403,2032.966018077277,False
L5,2023-02,0.9161876576227801,144.33788535611166,False
L5,2023-03,0.09299038023071748,14.784095545142918,False
L5,2023-04,0.36830001738401563,58.60870708161201,False
L5,2023-05,-1.134090987604186,-181.13604005919115,False
L5,2023-06,4.4217760719105215,698.2328524636996,False
L5,2023-07,-1.5027390042826383,-247.78680065797744,False
L5,2023-08,0.7264092642907283,117.97775767288658,False
L5,2023-09,-0.6460731461118252,-105.69241116683224,False
L5,2023-10,-1.3503826148268727,-219.48456805152455,False
L5,2023-11,0.38106198356844256,61.09957386474525,False
L5,2023-12,5.6552185707276825,910.2144761667423,False
L5,2024-01,-0.3744268333266465,-63.67255265270069,False
L5,2024-02,-0.7904412049896226,-133.9139131264128,False
L5,2024-03,2.384288751430197,400.745355197414,False
L5,2024-04,3.4493036848284975,593.5733549220349,False
L5,2024-05,1.3780801195372616,245.3268059301081,False
L5,2024-06,-2.182477137657246,-393.8803383624436,False
L5,2024-07,-1.7651317293754465,-311.60784407975007,False
L5,2024-08,1.2004059093476016,208.1733119324963,False
L5,2024-09,2.8039684337651583,492.0987949952323,False
L5,2024-10,1.3343038635014404,240.7375323555425,False
L5,2024-11,7.171370613964956,1311.1359233918702,False
L5,2024-12,0.8027540515346043,157.29207455411233,False
L5,2025-01,3.5776436029682834,706.6328237494599,False
L5,2025-02,2.215364079724713,453.2187496445622,False
L5,2025-03,3.6715152496749726,767.75786637485,False
L5,2025-04,0.5965010508384827,129.31520652604013,False
L5,2025-05,3.6436474725083823,794.6165603349145,False
L5,2025-06,1.3867569604456342,313.4471337249415,False
L5,2025-07,0.0010404898322713407,0.23844214533892227,False
L5,2025-08,2.3593394965214065,540.6797905492167,False
L5,2025-09,0.9336283817502844,219.00358249662168,False
L5,2025-10,1.5521290653958575,367.48607815159994,False
L5,2025-11,0.3462831329075877,83.25942939992456,False
L5,2025-12,-3.6787033566139105,-887.5608787233687,True
M5A15,2020-10,-1.30056677680348,-130.056677680348,True
M5A15,2020-11,0.4650219370084141,45.89740161908412,False
M5A15,2020-12,4.934595959561361,489.3066757200213,False
M5A15,2021-01,0.917846942356837,95.50332725549015,False
M5A15,2021-02,8.993554630310175,944.3817596630961,False
M5A15,2021-03,0.6492248311921411,74.30399284086707,False
M5A15,2021-04,-2.7490440776817504,-316.67163727568004,False
M5A15,2021-05,-0.5866623831696893,-65.7218205414265,False
M5A15,2021-06,1.008325006753541,112.29658147469672,False
M5A15,2021-07,6.066371129974435,682.4206236226419,False
M5A15,2021-08,-3.4275255518549486,-408.9607030306033,False
M5A15,2021-09,-0.2849126963578863,-32.82963390609984,False
M5A15,2021-10,5.643934927408112,648.4807798220099,False
M5A15,2021-11,2.110395037112456,256.1671501182009,False
M5A15,2021-12,0.9460081916492946,117.25315388981107,False
M5A15,2022-01,-0.610359401144589,-76.36677038699781,False
M5A15,2022-02,-1.0272916308425972,-127.74786664097155,False
M5A15,2022-03,3.9168166007992777,482.06832655985454,False
M5A15,2022-04,0.5678109262155395,72.62145407009848,False
M5A15,2022-05,0.10220933312024005,13.146518190000279,False
M5A15,2022-06,0.27492114531506573,35.39745181815306,False
M5A15,2022-07,-1.306022970472387,-168.6191902312985,False
M5A15,2022-08,-0.7665679387989566,-97.67816337108707,False
M5A15,2022-09,1.4279312226357588,180.55608761819894,False
M5A15,2022-10,0.29654360312045824,38.032158420001,False
M5A15,2022-11,0.5340358405978796,68.69399667223479,False
M5A15,2022-12,1.6421580913168476,212.36183128245284,False
M5A15,2023-01,4.696160306493402,617.2744315496493,False
M5A15,2023-02,0.07350890779074248,10.11593660739345,False
M5A15,2023-03,0.23060330295081588,31.75782713735134,False
M5A15,2023-04,-0.015789385440301285,-2.1794696619144815,False
M5A15,2023-05,-0.09378028900954849,-12.942810435859428,False
M5A15,2023-06,1.4780407664633621,203.79614402989318,False
M5A15,2023-07,-0.7989491838812035,-111.78944012462671,False
M5A15,2023-08,0.29538689829513576,41.00049733452033,False
M5A15,2023-09,-0.20883716567142718,-29.072785534810464,False
M5A15,2023-10,-0.8110078147002264,-112.66680442674806,False
M5A15,2023-11,0.2697877468726073,37.17548441790677,False
M5A15,2023-12,2.0088834084464935,277.5615107814101,False
M5A15,2024-01,0.05905287322338637,8.323069817717624,False
M5A15,2024-02,-0.7414828078368907,-104.56828326886534,False
M5A15,2024-03,1.5885464623894174,222.36508512527325,False
M5A15,2024-04,1.7263123371617617,245.48829864201252,False
M5A15,2024-05,0.14957610333128368,21.637492885029133,False
M5A15,2024-06,-1.140420896216432,-165.2186255081724,False
M5A15,2024-07,-2.0479154770972174,-293.308483016388,False
M5A15,2024-08,0.7437241477683099,104.33695570589407,False
M5A15,2024-09,1.3203403219052223,186.60796027692595,False
M5A15,2024-10,-0.2966175695238715,-42.47543069624044,False
M5A15,2024-11,7.234234910414239,1032.8646606396323,False
M5A15,2024-12,0.5626086090903204,86.13717856732546,False
M5A15,2025-01,0.4684060767055742,72.1179411616904,False
M5A15,2025-02,1.0165404155054958,157.24431809850648,False
M5A15,2025-03,1.3256768502772687,207.14787134937615,False
M5A15,2025-04,-0.19030628393501559,-30.131131779584393,False
M5A15,2025-05,2.148259949907705,339.4860011902256,False
M5A15,2025-06,1.1090251848099308,179.02241870495345,False
M5A15,2025-07,-0.8300566865364734,-135.47641241041856,False
M5A15,2025-08,0.7729644799108204,125.1110120652047,False
M5A15,2025-09,0.03717974902590626,6.064381140198748,False
M5A15,2025-10,1.2993222761287004,212.01098240381725,False
M5A15,2025-11,0.11602427952721595,19.17771650112627,False
M5A15,2025-12,-1.1925195906432595,-197.3409121644836,True
R5A15,2020-10,-3.7936285818260918,-379.36285818260876,True
R5A15,2020-11,1.731921107410983,166.62184532655556,False
R5A15,2020-12,11.934495429150038,1168.05997645977,False
R5A15,2021-01,-0.1246455410987557,-13.655316601278173,False
R5A15,2021-02,21.260081281872132,2326.206584941774,False
R5A15,2021-03,2.687217658661356,356.53655180107853,False
R5A15,2021-04,-7.9316326864183555,-1080.6379017901418,False
R5A15,2021-05,-1.9871826587330221,-249.26759997376212,False
R5A15,2021-06,1.635302670911809,201.0523078395272,False
R5A15,2021-07,12.627856031870888,1577.9205177078584,False
R5A15,2021-08,-5.90319746713207,-830.7849670531268,False
R5A15,2021-09,-1.5994891332750116,-211.81537375529842,False
R5A15,2021-10,19.947805256940953,2599.3733222631818,False
R5A15,2021-11,7.137428238186838,1115.597669427485,False
R5A15,2021-12,1.8102235161305602,303.1372197914716,False
R5A15,2022-01,-2.257753597898915,-384.9240040180048,False
R5A15,2022-02,-4.311210585869896,-718.422631418538,False
R5A15,2022-03,11.149402870140989,1777.8431245685624,False
R5A15,2022-04,1.3772492513099754,244.09647449744807,False
R5A15,2022-05,-0.010456215438547911,-1.8787283450001269,False
R5A15,2022-06,0.7271454460500593,130.63674186755816,False
R5A15,2022-07,-4.754871407826311,-860.4573615592017,False
R5A15,2022-08,-1.8087231013641847,-311.74926358736775,False
R5A15,2022-09,4.125912419519628,698.2746301532425,False
R5A15,2022-10,0.9764408771373079,172.0723265100023,False
R5A15,2022-11,-1.023626317088433,-182.14891155168516,False
R5A15,2022-12,7.0559621649103565,1242.718944283828,False
R5A15,2023-01,24.29315122711737,4580.4841875697275,False
R5A15,2023-02,1.6359215941187166,383.3868551854757,False
R5A15,2023-03,-1.6196200645192116,-385.7759161634058,False
R5A15,2023-04,-0.2739914961499723,-64.20480662362388,False
R5A15,2023-05,-1.7919767401606057,-418.7658552446883,False
R5A15,2023-06,6.325348174568202,1451.6780190062564,False
R5A15,2023-07,-1.3805231482054925,-336.87312990442297,False
R5A15,2023-08,0.8176752365895767,196.77332224267593,False
R5A15,2023-09,-1.373866562419468,-333.3240156936736,False
R5A15,2023-10,-2.9207148223163726,-698.8809675156153,False
R5A15,2023-11,1.581330379705581,367.33578909622884,False
R5A15,2023-12,9.945901426276272,2346.9221063628393,False
R5A15,2024-01,-0.09177772884589874,-23.810629414037976,False
R5A15,2024-02,-0.44651391071693913,-115.73635331973492,False
R5A15,2024-03,6.51566842536111,1681.3194950900652,False
R5A15,2024-04,7.378634887870983,2028.0599619472814,False
R5A15,2024-05,2.848740417445783,840.7667458413998,False
R5A15,2024-06,-2.682792942387202,-814.3456506838702,False
R5A15,2024-07,-3.1473034146087486,-929.7150802978649,False
R5A15,2024-08,-0.48677563162778936,-139.26815057549902,False
R5A15,2024-09,5.0701694682864895,1443.5314602311955,False
R5A15,2024-10,1.116086738987887,333.8728915091051,False
R5A15,2024-11,16.89737343635198,5111.197542692495,False
R5A15,2024-12,1.0278775429235942,363.4541189093725,False
R5A15,2025-01,9.004374982279483,3216.6441537863866,False
R5A15,2025-02,2.533932981342213,986.7076600307628,False
R5A15,2025-03,6.175535724907033,2465.6738553811956,False
R5A15,2025-04,6.813671232082008,2888.4617925134226,False
R5A15,2025-05,9.876500941824995,4472.14014190928,False
R5A15,2025-06,3.719232403025985,1850.420505895694,False
R5A15,2025-07,2.8327761269871576,1461.8023759752396,False
R5A15,2025-08,1.431307977304197,759.5232309976273,False
R5A15,2025-09,1.5158406331145624,815.8936260537012,False
R5A15,2025-10,4.287405891056628,2342.6554113315215,False
R5A15,2025-11,1.2006169575685899,684.1481373922434,False
R5A15,2025-12,-6.64724034338795,-3833.2771274577826,True

```
