# R20 PAXG: auditoría completa 01–05 y comparadores

Job 5dba914705be496b8fce366a8cb0d72d succeeded / exit 0. Snapshots completos: 393 / 1082 / 17 / 928 / 766 trades, más 35 retest y 60 fin de semana. Cohortes de cierre no son MTM anual. Costes extra RT se aplican como mitad del recargo a cada lado sobre TODOS los fills, sin modificar decisiones. Curvas a las 00:01 no se convierten en cierres UTC.

```json
{
  "exp01": {
    "session_id": "51a0c817-4c43-4940-ab0e-4bfec6b3a52c",
    "title": "MCP Backtest: PAXG20-01 R20PaxgARResponse4h",
    "trades": 393,
    "stored_metrics": {
      "total": 393,
      "total_winning_trades": 172,
      "total_losing_trades": 221,
      "starting_balance": 10000.0,
      "finishing_balance": 8090.479252648093,
      "win_rate": 0.43765903307888043,
      "win_rate_longs": 0.46200607902735563,
      "win_rate_shorts": 0.3125,
      "ratio_avg_win_loss": 1.0102076160106386,
      "longs_count": 329,
      "longs_percentage": 83.7150127226463,
      "shorts_percentage": 16.284987277353693,
      "shorts_count": 64,
      "fee": 1890.2322002406627,
      "net_profit": -1909.5207473518708,
      "net_profit_percentage": -19.09520747351871,
      "average_win": 40.83059349648459,
      "average_loss": 40.41802184953494,
      "expectancy": -4.858831418198147,
      "expectancy_percentage": -0.048588314181981465,
      "expected_net_profit_every_100_trades": -4.858831418198147,
      "average_holding_period": 78185.95419847328,
      "average_winning_holding_period": 86400.0,
      "average_losing_holding_period": 71793.1221719457,
      "gross_profit": 7022.862081395349,
      "gross_loss": -8932.38282874722,
      "max_drawdown": -26.64040871186747,
      "max_underwater_period": 1882.0,
      "annual_return": -3.98275550561622,
      "annualization": 365,
      "sharpe_ratio": -0.6983882428600684,
      "calmar_ratio": -0.14950054065206692,
      "sortino_ratio": -0.9690382322354553,
      "omega_ratio": 0.8222480887077032,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -19.274336000000403,
      "winning_streak": 13,
      "losing_streak": 9,
      "largest_losing_trade": -95.98220463968647,
      "largest_winning_trade": 214.69759172279984,
      "current_streak": -5,
      "avg_trades_per_day": 0.2065159519632919,
      "avg_trades_per_week": 1.4456116637430432,
      "avg_trades_per_month": 6.286345577762606
    },
    "directions": {
      "long": {
        "n": 329,
        "net": -739.1834329437006,
        "fees": 1576.3327547912318,
        "before_fees": 837.1493218475306
      },
      "short": {
        "n": 64,
        "net": -1170.3373144081702,
        "fees": 313.89944544943137,
        "before_fees": -856.4378689587392
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 9,
        "net": -152.38497330926532,
        "static_5bps_RT": -177.0159259009519,
        "static_10bps_RT": -201.6468784926385
      },
      "2021": {
        "n": 53,
        "net": -766.237562138979,
        "static_5bps_RT": -884.3861790580683,
        "static_10bps_RT": -1002.5347959771576
      },
      "2022": {
        "n": 65,
        "net": -1143.0289402285812,
        "static_5bps_RT": -1335.6767618554888,
        "static_10bps_RT": -1528.3245834823965
      },
      "2023": {
        "n": 44,
        "net": -410.82285644668326,
        "static_5bps_RT": -535.5895168797665,
        "static_10bps_RT": -660.3561773128497
      },
      "2024": {
        "n": 73,
        "net": 210.41855760223325,
        "static_5bps_RT": 33.26731690451874,
        "static_10bps_RT": -143.88392379319578
      },
      "2025": {
        "n": 149,
        "net": 352.53502716940505,
        "static_5bps_RT": -60.248680695815494,
        "static_10bps_RT": -473.03238856103604
      }
    },
    "status": "economic_result",
    "net": -1909.520747351871,
    "fees": 1890.232200240663,
    "before_fees": -19.288547111208118,
    "pf_net": 0.7862249319177824,
    "no_losses": false,
    "dd_engine": -26.64040871186747,
    "cagr_engine": -3.98275550561622,
    "sharpe_engine": -0.6983882428600684,
    "entry_notional_sum": 2099411.2066720002,
    "executed_fill_notional_sum": 4200516.000534806,
    "net_bps_entry_notional": -9.095506117540713,
    "before_fee_bps_entry_notional": -0.09187598432316861,
    "extra_5bps_RT_all_fills_static": -2959.6497474855723,
    "extra_10bps_RT_all_fills_static": -4009.7787476192743,
    "top3_net": 549.6085589891993,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -2459.1293063410703,
    "mean_hold_hours": 21.71832061068702,
    "median_hold_hours": 24.0,
    "max_hold_hours": 24.0,
    "holding_hours": 8535.300000000003,
    "time_exposure_pct": 18.68825538623227,
    "recent_closed_cohort_2023_2025": 152.13072832495487,
    "recent_static_5bps_RT": -562.5708806710629,
    "recent_static_10bps_RT": -1277.2724896670818,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "terminal": [
      {
        "type": "long",
        "gross": -19.274336000000158,
        "net": -23.52302412560016,
        "hours": 20.0
      }
    ],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 8.881784197001252e-16,
      "max_pnl_error": 8.810729923425242e-13,
      "max_qty_error": 0.0,
      "wallet_error": 3.54702933691442e-11,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 393,
        "exit_MARKET": 320,
        "exit_STOP": 73
      }
    }
  },
  "exp02": {
    "session_id": "a758809e-9d05-4e7e-a5b9-333751a19395",
    "title": "MCP Backtest: PAXG20-02 R20PaxgPathAnalogue4h",
    "trades": 1082,
    "stored_metrics": {
      "total": 1082,
      "total_winning_trades": 470,
      "total_losing_trades": 612,
      "starting_balance": 10000.0,
      "finishing_balance": 5453.630251645301,
      "win_rate": 0.4343807763401109,
      "win_rate_longs": 0.45147679324894513,
      "win_rate_shorts": 0.40161725067385445,
      "ratio_avg_win_loss": 0.960312430360033,
      "longs_count": 711,
      "longs_percentage": 65.71164510166358,
      "shorts_percentage": 34.28835489833642,
      "shorts_count": 371,
      "fee": 4816.612339258896,
      "net_profit": -4546.369748354696,
      "net_profit_percentage": -45.46369748354696,
      "average_win": 27.17615665964109,
      "average_loss": 28.29928656599021,
      "expectancy": -4.201820469828741,
      "expectancy_percentage": -0.04201820469828741,
      "expected_net_profit_every_100_trades": -4.201820469828741,
      "average_holding_period": 80692.51386321627,
      "average_winning_holding_period": 86400.0,
      "average_losing_holding_period": 76309.3137254902,
      "gross_profit": 12772.793630031312,
      "gross_loss": -17319.16337838601,
      "max_drawdown": -52.9784299099346,
      "max_underwater_period": 1819.0,
      "annual_return": -10.978341950386861,
      "annualization": 365,
      "sharpe_ratio": -1.3360870893971792,
      "calmar_ratio": -0.20722286351351807,
      "sortino_ratio": -1.815173317903557,
      "omega_ratio": 0.8016502023435119,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -5.307060000000092,
      "winning_streak": 7,
      "losing_streak": 9,
      "largest_losing_trade": -96.97052420564643,
      "largest_winning_trade": 144.32911870650003,
      "current_streak": -1,
      "avg_trades_per_day": 0.5685757252526256,
      "avg_trades_per_week": 3.980030076768379,
      "avg_trades_per_month": 17.307445076689923
    },
    "directions": {
      "long": {
        "n": 711,
        "net": -1931.30702119547,
        "fees": 3026.599552087597,
        "before_fees": 1095.2925308921306
      },
      "short": {
        "n": 371,
        "net": -2615.062727159225,
        "fees": 1790.012787171294,
        "before_fees": -825.0499399879309
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2021": {
        "n": 218,
        "net": -1536.6745643634617,
        "static_5bps_RT": -2167.1230005868892,
        "static_10bps_RT": -2797.571436810317
      },
      "2022": {
        "n": 232,
        "net": -2047.4684006376058,
        "static_5bps_RT": -2702.805351327659,
        "static_10bps_RT": -3358.1423020177126
      },
      "2023": {
        "n": 165,
        "net": -752.0628748206957,
        "static_5bps_RT": -1194.5951666471756,
        "static_10bps_RT": -1637.1274584736557
      },
      "2024": {
        "n": 216,
        "net": -491.58474823303277,
        "static_5bps_RT": -927.4386040634081,
        "static_10bps_RT": -1363.2924598937834
      },
      "2025": {
        "n": 251,
        "net": 281.42083970010026,
        "static_5bps_RT": -230.30336976228358,
        "static_10bps_RT": -742.0275792246674
      }
    },
    "status": "economic_result",
    "net": -4546.369748354696,
    "fees": 4816.612339258896,
    "before_fees": 270.24259090420037,
    "pf_net": 0.7374948403091758,
    "no_losses": false,
    "dd_engine": -52.9784299099346,
    "cagr_engine": -10.978341950386861,
    "sharpe_engine": -1.3360870893971792,
    "entry_notional_sum": 5350831.31683,
    "executed_fill_notional_sum": 10703582.97613088,
    "net_bps_entry_notional": -8.49656712977472,
    "before_fee_bps_entry_notional": 0.5050478606085093,
    "extra_5bps_RT_all_fills_static": -7222.265492387416,
    "extra_10bps_RT_all_fills_static": -9898.161236420136,
    "top3_net": 401.42408002520006,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -4947.793828379896,
    "mean_hold_hours": 22.41458718422674,
    "median_hold_hours": 24.0,
    "max_hold_hours": 28.0,
    "holding_hours": 24252.58333333334,
    "time_exposure_pct": 53.101645063350276,
    "recent_closed_cohort_2023_2025": -962.2267833536278,
    "recent_static_5bps_RT": -2352.33714047287,
    "recent_static_10bps_RT": -3742.4474975921094,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "terminal": [
      {
        "type": "long",
        "gross": -5.3070600000003365,
        "net": -8.093870994000337,
        "hours": 4.0
      }
    ],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 8.881784197001252e-16,
      "max_pnl_error": 8.29558643999917e-13,
      "max_qty_error": 0.0,
      "wallet_error": 3.637978807091713e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 1082,
        "exit_MARKET": 929,
        "exit_STOP": 153
      }
    }
  },
  "exp03": {
    "session_id": "f72b8359-4531-42ff-8cc0-5b61a6f23320",
    "title": "MCP Backtest: PAXG20-03 R20PaxgSpyDelayed1h",
    "trades": 17,
    "stored_metrics": {
      "total": 17,
      "total_winning_trades": 8,
      "total_losing_trades": 9,
      "starting_balance": 10000.0,
      "finishing_balance": 9867.378590556405,
      "win_rate": 0.47058823529411764,
      "win_rate_longs": 0.375,
      "win_rate_shorts": 0.5555555555555556,
      "ratio_avg_win_loss": 0.7619385924659793,
      "longs_count": 8,
      "longs_percentage": 47.05882352941176,
      "shorts_percentage": 52.94117647058824,
      "shorts_count": 9,
      "fee": 108.68718656570495,
      "net_profit": -132.62140944359177,
      "net_profit_percentage": -1.3262140944359178,
      "average_win": 34.79072959332501,
      "average_loss": 45.660805132243546,
      "expectancy": -7.801259379034814,
      "expectancy_percentage": -0.07801259379034814,
      "expected_net_profit_every_100_trades": -7.801259379034814,
      "average_holding_period": 80576.4705882353,
      "average_winning_holding_period": 86400.0,
      "average_losing_holding_period": 75400.0,
      "gross_profit": 278.3258367466001,
      "gross_loss": -410.9472461901919,
      "max_drawdown": -1.9905457431986129,
      "max_underwater_period": 1195.0,
      "annual_return": -0.25574529786640543,
      "annualization": 365,
      "sharpe_ratio": -0.2870001882816457,
      "calmar_ratio": -0.12847999034448093,
      "sortino_ratio": -0.38459016231966775,
      "omega_ratio": 0.7092938282355399,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 3,
      "losing_streak": 3,
      "largest_losing_trade": -93.73743363765999,
      "largest_winning_trade": 98.80847318000001,
      "current_streak": -3,
      "avg_trades_per_day": 0.008933260008590235,
      "avg_trades_per_week": 0.06253282006013164,
      "avg_trades_per_month": 0.27192843466148675
    },
    "directions": {
      "short": {
        "n": 9,
        "net": -74.4568881784011,
        "fees": 59.0500241784,
        "before_fees": -15.406864000001107
      },
      "long": {
        "n": 8,
        "net": -58.16452126519067,
        "fees": 49.63716238730495,
        "before_fees": -8.527358877885728
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2021": {
        "n": 3,
        "net": 35.033029651600074,
        "static_5bps_RT": 24.80141501360007,
        "static_10bps_RT": 14.569800375600071
      },
      "2022": {
        "n": 3,
        "net": -60.98805864265998,
        "static_5bps_RT": -70.73605037427855,
        "static_10bps_RT": -80.4840421058971
      },
      "2023": {
        "n": 1,
        "net": -33.71037762500001,
        "static_5bps_RT": -37.49142075,
        "static_10bps_RT": -41.27246387500001
      },
      "2024": {
        "n": 7,
        "net": -40.37272555638225,
        "static_5bps_RT": -67.04203511429422,
        "static_10bps_RT": -93.7113446722062
      },
      "2025": {
        "n": 3,
        "net": -32.58327727114962,
        "static_5bps_RT": -42.53508853289962,
        "static_10bps_RT": -52.48689979464962
      }
    },
    "status": "economic_result",
    "net": -132.62140944359177,
    "fees": 108.68718656570495,
    "before_fees": -23.934222877886825,
    "pf_net": 0.6772787488586482,
    "no_losses": false,
    "dd_engine": -1.9905457431986129,
    "cagr_engine": -0.25574529786640543,
    "sharpe_engine": -0.2870001882816457,
    "entry_notional_sum": 120760.10087600001,
    "executed_fill_notional_sum": 241527.08125712213,
    "net_bps_entry_notional": -10.982220823065665,
    "before_fee_bps_entry_notional": -1.9819644654374031,
    "extra_5bps_RT_all_fills_static": -193.00317975787232,
    "extra_10bps_RT_all_fills_static": -253.38495007215283,
    "top3_net": 213.80993508500003,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -346.4313445285918,
    "mean_hold_hours": 22.38235294117647,
    "median_hold_hours": 24.0,
    "max_hold_hours": 24.0,
    "holding_hours": 380.49999999999994,
    "time_exposure_pct": 0.8331143808022419,
    "recent_closed_cohort_2023_2025": -106.66638045253188,
    "recent_static_5bps_RT": -147.06854439719382,
    "recent_static_10bps_RT": -187.47070834185578,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": true,
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 6.039613253960852e-13,
      "max_qty_error": 0.0,
      "wallet_error": 3.637978807091713e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 17,
        "exit_MARKET": 15,
        "exit_STOP": 2
      }
    }
  },
  "exp04": {
    "session_id": "b8ee439b-4d96-46c3-8948-fca6eb59f5eb",
    "title": "MCP Backtest: PAXG20-04 R20PaxgDirectionalOvershoot1h",
    "trades": 928,
    "stored_metrics": {
      "total": 928,
      "total_winning_trades": 348,
      "total_losing_trades": 580,
      "starting_balance": 10000.0,
      "finishing_balance": 2535.152143356206,
      "win_rate": 0.375,
      "win_rate_longs": 0.4029535864978903,
      "win_rate_shorts": 0.3458149779735683,
      "ratio_avg_win_loss": 1.1063509735488222,
      "longs_count": 474,
      "longs_percentage": 51.077586206896555,
      "shorts_percentage": 48.922413793103445,
      "shorts_count": 454,
      "fee": 5503.709185526543,
      "net_profit": -7464.84785664381,
      "net_profit_percentage": -74.6484785664381,
      "average_win": 42.35472368949779,
      "average_loss": 38.283261552739724,
      "expectancy": -8.044017086900658,
      "expectancy_percentage": -0.08044017086900658,
      "expected_net_profit_every_100_trades": -8.044017086900658,
      "average_holding_period": 53404.137931034486,
      "average_winning_holding_period": 67100.5172413793,
      "average_losing_holding_period": 45186.31034482759,
      "gross_profit": 14739.44384394523,
      "gross_loss": -22204.29170058904,
      "max_drawdown": -74.72866829098068,
      "max_underwater_period": 1896.0,
      "annual_return": -23.142450773759116,
      "annualization": 365,
      "sharpe_ratio": -2.1540600429616243,
      "calmar_ratio": -0.30968638011380534,
      "sortino_ratio": -2.759032592180738,
      "omega_ratio": 0.6689836042187458,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -10.978072999999767,
      "winning_streak": 6,
      "losing_streak": 10,
      "largest_losing_trade": -90.83576135008268,
      "largest_winning_trade": 155.44236576504827,
      "current_streak": -1,
      "avg_trades_per_day": 0.48765089929245514,
      "avg_trades_per_week": 3.413556295047186,
      "avg_trades_per_month": 14.844093374462336
    },
    "directions": {
      "long": {
        "n": 474,
        "net": -2565.557718642323,
        "fees": 2800.101905907868,
        "before_fees": 234.54418726554727
      },
      "short": {
        "n": 454,
        "net": -4899.290138001481,
        "fees": 2703.607279618672,
        "before_fees": -2195.682858382815
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 32,
        "net": -437.43340192990735,
        "static_5bps_RT": -575.0178131625861,
        "static_10bps_RT": -712.6022243952649
      },
      "2021": {
        "n": 113,
        "net": -2066.628113539391,
        "static_5bps_RT": -2477.288073560307,
        "static_10bps_RT": -2887.948033581223
      },
      "2022": {
        "n": 213,
        "net": -900.1620500674856,
        "static_5bps_RT": -1899.2017420694756,
        "static_10bps_RT": -2898.2414340714654
      },
      "2023": {
        "n": 224,
        "net": -2862.538581430913,
        "static_5bps_RT": -3682.4915806906038,
        "static_10bps_RT": -4502.444579950295
      },
      "2024": {
        "n": 107,
        "net": -392.57497079991157,
        "static_5bps_RT": -611.494042546861,
        "static_10bps_RT": -830.4131142938106
      },
      "2025": {
        "n": 239,
        "net": -805.5107388762013,
        "static_5bps_RT": -1276.9708187953895,
        "static_10bps_RT": -1748.4308987145778
      }
    },
    "status": "economic_result",
    "net": -7464.847856643809,
    "fees": 5503.709185526542,
    "before_fees": -1961.1386711172672,
    "pf_net": 0.6638105841292925,
    "no_losses": false,
    "dd_engine": -74.72866829098068,
    "cagr_engine": -23.142450773759116,
    "sharpe_engine": -2.1540600429616243,
    "entry_notional_sum": 6114017.31484,
    "executed_fill_notional_sum": 12230464.85672565,
    "net_bps_entry_notional": -12.209399274230154,
    "before_fee_bps_entry_notional": -3.207610594031477,
    "extra_5bps_RT_all_fills_static": -10522.464070825221,
    "extra_10bps_RT_all_fills_static": -13580.080285006634,
    "top3_net": 464.5699843627651,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -7929.417841006574,
    "mean_hold_hours": 14.83448275862069,
    "median_hold_hours": 16.941666666666666,
    "max_hold_hours": 24.0,
    "holding_hours": 13766.400000000007,
    "time_exposure_pct": 30.14188124014715,
    "recent_closed_cohort_2023_2025": -4060.6242911070285,
    "recent_static_5bps_RT": -5570.956442032853,
    "recent_static_10bps_RT": -7081.288592958679,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "terminal": [
      {
        "type": "long",
        "gross": -10.97807300000003,
        "net": -13.91185703465003,
        "hours": 22.0
      }
    ],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 1.5774048733874224e-12,
      "max_qty_error": 0.0,
      "wallet_error": -1.5006662579253316e-11,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 928,
        "exit_STOP": 416,
        "exit_MARKET": 372,
        "exit_LIMIT": 140
      }
    }
  },
  "exp05": {
    "session_id": "43ec28da-525d-46d6-8c65-c641f32aa1d7",
    "title": "MCP Backtest: PAXG20-05 R20PaxgRoundBarrier1h",
    "trades": 766,
    "stored_metrics": {
      "total": 766,
      "total_winning_trades": 257,
      "total_losing_trades": 509,
      "starting_balance": 10000.0,
      "finishing_balance": 1670.3988355601477,
      "win_rate": 0.33550913838120106,
      "win_rate_longs": 0.36103896103896105,
      "win_rate_shorts": 0.30971128608923887,
      "ratio_avg_win_loss": 1.0860128126443174,
      "longs_count": 385,
      "longs_percentage": 50.26109660574413,
      "shorts_percentage": 49.73890339425587,
      "shorts_count": 381,
      "fee": 6069.891506768089,
      "net_profit": -8329.601164439857,
      "net_profit_percentage": -83.29601164439858,
      "average_win": 39.34868140692014,
      "average_loss": 36.2322441768533,
      "expectancy": -10.8741529561878,
      "expectancy_percentage": -0.10874152956187799,
      "expected_net_profit_every_100_trades": -10.8741529561878,
      "average_holding_period": 18120.78328981723,
      "average_winning_holding_period": 26086.22568093385,
      "average_losing_holding_period": 14098.939096267191,
      "gross_profit": 10112.611121578477,
      "gross_loss": -18442.21228601833,
      "max_drawdown": -83.41552812209399,
      "max_underwater_period": 1880.0,
      "annual_return": -29.05283735361186,
      "annualization": 365,
      "sharpe_ratio": -3.3444192027602155,
      "calmar_ratio": -0.34829051625840796,
      "sortino_ratio": -4.1080388185895504,
      "omega_ratio": 0.4978044606977572,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 7,
      "losing_streak": 10,
      "largest_losing_trade": -89.76937970097605,
      "largest_winning_trade": 152.45896233207196,
      "current_streak": -1,
      "avg_trades_per_day": 0.4025221862694188,
      "avg_trades_per_week": 2.8176553038859318,
      "avg_trades_per_month": 12.252775350041109
    },
    "directions": {
      "short": {
        "n": 381,
        "net": -4993.518727516542,
        "fees": 2957.2414556930203,
        "before_fees": -2036.2772718235212
      },
      "long": {
        "n": 385,
        "net": -3336.0824369233133,
        "fees": 3112.650051075069,
        "before_fees": -223.43238584824712
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 31,
        "net": -825.0944390120248,
        "static_5bps_RT": -1063.8764051557832,
        "static_10bps_RT": -1302.6583712995414
      },
      "2021": {
        "n": 153,
        "net": -2528.790830565227,
        "static_5bps_RT": -3498.4484285910607,
        "static_10bps_RT": -4468.106026616894
      },
      "2022": {
        "n": 101,
        "net": -1501.1232786432179,
        "static_5bps_RT": -2090.0327301480893,
        "static_10bps_RT": -2678.9421816529607
      },
      "2023": {
        "n": 91,
        "net": -751.324632709841,
        "static_5bps_RT": -1209.4104169235982,
        "static_10bps_RT": -1667.4962011373555
      },
      "2024": {
        "n": 158,
        "net": -1080.7057058013313,
        "static_5bps_RT": -1623.614591310576,
        "static_10bps_RT": -2166.5234768198206
      },
      "2025": {
        "n": 232,
        "net": -1642.5622777082158,
        "static_5bps_RT": -2216.380540515245,
        "static_10bps_RT": -2790.198803322274
      }
    },
    "status": "economic_result",
    "net": -8329.601164439857,
    "fees": 6069.891506768089,
    "before_fees": -2259.7096576717677,
    "pf_net": 0.5483404574648129,
    "no_losses": false,
    "dd_engine": -83.41552812209399,
    "cagr_engine": -29.05283735361186,
    "sharpe_engine": -3.3444192027602155,
    "entry_notional_sum": 6743417.473966001,
    "executed_fill_notional_sum": 13488647.792817976,
    "net_bps_entry_notional": -12.352195599037968,
    "before_fee_bps_entry_notional": -3.350985856052549,
    "extra_5bps_RT_all_fills_static": -11701.763112644352,
    "extra_10bps_RT_all_fills_static": -15073.925060848846,
    "top3_net": 451.01977935335344,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -8780.62094379321,
    "mean_hold_hours": 5.03355091383812,
    "median_hold_hours": 3.45,
    "max_hold_hours": 12.0,
    "holding_hours": 3855.6999999999994,
    "time_exposure_pct": 8.442152741285689,
    "recent_closed_cohort_2023_2025": -3474.5926162193864,
    "recent_static_5bps_RT": -5049.405548749422,
    "recent_static_10bps_RT": -6624.218481279448,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 3.552713678800501e-15,
      "max_pnl_error": 1.8047785488306545e-12,
      "max_qty_error": 0.0,
      "wallet_error": -4.547473508864641e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 766,
        "exit_STOP": 458,
        "exit_MARKET": 140,
        "exit_LIMIT": 168
      }
    }
  },
  "retest": {
    "session_id": "93a16137-e819-41a3-b325-0631a6627a6c",
    "title": "MCP Backtest: PAXG isolated retest control1pct2020-25",
    "trades": 35,
    "stored_metrics": {
      "total": 35,
      "total_winning_trades": 14,
      "total_losing_trades": 21,
      "starting_balance": 10000.0,
      "finishing_balance": 10546.110572353738,
      "win_rate": 0.4,
      "win_rate_longs": 0.4,
      "win_rate_shorts": 0.0,
      "ratio_avg_win_loss": 1.9625021019167472,
      "longs_count": 35,
      "longs_percentage": 100.0,
      "shorts_percentage": 0.0,
      "shorts_count": 0,
      "fee": 246.60888105483386,
      "net_profit": 546.110572353739,
      "net_profit_percentage": 5.461105723537391,
      "average_win": 165.5194247738157,
      "average_loss": 84.34101783236578,
      "expectancy": 15.60315921010681,
      "expectancy_percentage": 0.1560315921010681,
      "expected_net_profit_every_100_trades": 15.60315921010681,
      "average_holding_period": 627476.5714285715,
      "average_winning_holding_period": 1211267.142857143,
      "average_losing_holding_period": 238282.85714285713,
      "gross_profit": 2317.27194683342,
      "gross_loss": -1771.1613744796814,
      "max_drawdown": -6.919378335744097,
      "max_underwater_period": 1191.0,
      "annual_return": 1.0250706618597727,
      "annualization": 365,
      "sharpe_ratio": 0.23075746266424707,
      "calmar_ratio": 0.14814490726203924,
      "sortino_ratio": 0.32889418412578003,
      "omega_ratio": 1.0888643148234043,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 3,
      "losing_streak": 5,
      "largest_losing_trade": -101.07354463690129,
      "largest_winning_trade": 637.4985528227819,
      "current_streak": -1,
      "avg_trades_per_day": 0.018392005900038717,
      "avg_trades_per_week": 0.128744041300271,
      "avg_trades_per_month": 0.5598526595971786
    },
    "directions": {
      "long": {
        "n": 35,
        "net": 546.1105723537391,
        "fees": 246.60888105483383,
        "before_fees": 792.7194534085729
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2021": {
        "n": 6,
        "net": -203.7127948722217,
        "static_5bps_RT": -222.8870458834587,
        "static_10bps_RT": -242.06129689469572
      },
      "2022": {
        "n": 3,
        "net": -87.13692885508894,
        "static_5bps_RT": -96.948923070272,
        "static_10bps_RT": -106.76091728545506
      },
      "2023": {
        "n": 5,
        "net": -55.78962675646495,
        "static_5bps_RT": -80.47088461581254,
        "static_10bps_RT": -105.15214247516013
      },
      "2024": {
        "n": 7,
        "net": 495.49747740212723,
        "static_5bps_RT": 470.88797330593343,
        "static_10bps_RT": 446.27846920973957
      },
      "2025": {
        "n": 14,
        "net": 397.25244543538753,
        "static_5bps_RT": 338.5245186979969,
        "static_10bps_RT": 279.7965919606062
      }
    },
    "status": "economic_result",
    "net": 546.1105723537391,
    "fees": 246.60888105483386,
    "before_fees": 792.719453408573,
    "pf_net": 1.308334734611165,
    "no_losses": false,
    "dd_engine": -6.919378335744097,
    "cagr_engine": 1.0250706618597727,
    "sharpe_engine": 0.23075746266424707,
    "entry_notional_sum": 273613.508112,
    "executed_fill_notional_sum": 548019.7356774086,
    "net_bps_entry_notional": 19.95919631753693,
    "before_fee_bps_entry_notional": 28.972233822757172,
    "extra_5bps_RT_all_fills_static": 409.10563843438695,
    "extra_10bps_RT_all_fills_static": 272.1007045150348,
    "top3_net": 1466.657905102516,
    "top3_share_of_net": 2.6856427605516107,
    "net_ex_top3_descriptive": -920.5473327487769,
    "mean_hold_hours": 174.29904761904763,
    "median_hold_hours": 98.4,
    "max_hold_hours": 916.75,
    "holding_hours": 6100.466666666668,
    "time_exposure_pct": 13.357126175045252,
    "recent_closed_cohort_2023_2025": 836.9602960810497,
    "recent_static_5bps_RT": 728.9416073881175,
    "recent_static_10bps_RT": 620.9229186951853,
    "descriptive_initial_gate_pass": true,
    "sample_inconclusive": false,
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 1.0516032489249483e-12,
      "max_qty_error": 0.0,
      "wallet_error": 0.0,
      "overlaps": 0,
      "ordertypes": {
        "entry_LIMIT": 35,
        "exit_STOP": 35
      }
    }
  },
  "weekend": {
    "session_id": "ff199ebe-dab0-4c09-9078-fff98188e97c",
    "title": "MCP Backtest: ResearchPaxgWeekendEvent0751h robustness2020-25",
    "trades": 60,
    "stored_metrics": {
      "total": 60,
      "total_winning_trades": 42,
      "total_losing_trades": 18,
      "starting_balance": 10000.0,
      "finishing_balance": 10764.035579346746,
      "win_rate": 0.7,
      "win_rate_longs": 0.5555555555555556,
      "win_rate_shorts": 0.7619047619047619,
      "ratio_avg_win_loss": 0.742178959113402,
      "longs_count": 18,
      "longs_percentage": 30.0,
      "shorts_percentage": 70.0,
      "shorts_count": 42,
      "fee": 414.31927019361717,
      "net_profit": 764.0355793467392,
      "net_profit_percentage": 7.640355793467392,
      "average_win": 43.051317618401214,
      "average_loss": 58.0066533681173,
      "expectancy": 12.733926322445658,
      "expectancy_percentage": 0.1273392632244566,
      "expected_net_profit_every_100_trades": 12.73392632244566,
      "average_holding_period": 39588.0,
      "average_winning_holding_period": 30201.428571428572,
      "average_losing_holding_period": 61490.0,
      "gross_profit": 1808.155339972851,
      "gross_loss": -1044.1197606261114,
      "max_drawdown": -2.990690170671495,
      "max_underwater_period": 331.0,
      "annual_return": 1.4221718304768594,
      "annualization": 365,
      "sharpe_ratio": 0.744986681862599,
      "calmar_ratio": 0.47553298714240977,
      "sortino_ratio": 1.062638461255163,
      "omega_ratio": 1.571013312993865,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 7,
      "losing_streak": 4,
      "largest_losing_trade": -102.357336675,
      "largest_winning_trade": 144.33149316630096,
      "current_streak": 4,
      "avg_trades_per_day": 0.031529152971494945,
      "avg_trades_per_week": 0.2207040708004646,
      "avg_trades_per_month": 0.9597474164523062
    },
    "directions": {
      "short": {
        "n": 42,
        "net": 821.2603218360483,
        "fees": 276.12920735946204,
        "before_fees": 1097.3895291955102
      },
      "long": {
        "n": 18,
        "net": -57.224742489308916,
        "fees": 138.19006283415516,
        "before_fees": 80.96532034484626
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 3,
        "net": 133.49872632610044,
        "static_5bps_RT": 123.82643984060044,
        "static_10bps_RT": 114.15415335510043
      },
      "2021": {
        "n": 9,
        "net": 78.27333818556586,
        "static_5bps_RT": 54.73512036163302,
        "static_10bps_RT": 31.196902537700176
      },
      "2022": {
        "n": 9,
        "net": 241.5001311414926,
        "static_5bps_RT": 208.6977232078481,
        "static_10bps_RT": 175.8953152742036
      },
      "2023": {
        "n": 17,
        "net": 123.2046939996445,
        "static_5bps_RT": 42.200302049521966,
        "static_10bps_RT": -38.80408990060057
      },
      "2024": {
        "n": 12,
        "net": 177.67280505569028,
        "static_5bps_RT": 133.13268545060407,
        "static_10bps_RT": 88.59256584551785
      },
      "2025": {
        "n": 10,
        "net": 9.88588463824573,
        "static_5bps_RT": -28.734063893255534,
        "static_10bps_RT": -67.3540124247568
      }
    },
    "status": "economic_result",
    "net": 764.0355793467394,
    "fees": 414.3192701936172,
    "before_fees": 1178.3548495403566,
    "pf_net": 1.7317509045979385,
    "no_losses": false,
    "dd_engine": -2.990690170671495,
    "cagr_engine": 1.4221718304768594,
    "sharpe_engine": 0.744986681862599,
    "entry_notional_sum": 460862.956764,
    "executed_fill_notional_sum": 920709.4893191494,
    "net_bps_entry_notional": 16.57836821408905,
    "before_fee_bps_entry_notional": 25.568443552380625,
    "extra_5bps_RT_all_fills_static": 533.8582070169521,
    "extra_10bps_RT_all_fills_static": 303.6808346871647,
    "top3_net": 302.3193192659005,
    "top3_share_of_net": 0.39568748817219684,
    "net_ex_top3_descriptive": 461.7162600808389,
    "mean_hold_hours": 10.996666666666666,
    "median_hold_hours": 7.916666666666667,
    "max_hold_hours": 24.0,
    "holding_hours": 659.7999999999997,
    "time_exposure_pct": 1.4446488001401292,
    "recent_closed_cohort_2023_2025": 310.76338369358047,
    "recent_static_5bps_RT": 146.59892360687053,
    "recent_static_10bps_RT": -17.56553647983952,
    "descriptive_initial_gate_pass": true,
    "sample_inconclusive": false,
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 1.4566126083082054e-12,
      "max_qty_error": 0.0,
      "wallet_error": -7.275957614183426e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 60,
        "exit_MARKET": 15,
        "exit_LIMIT": 37,
        "exit_STOP": 8
      }
    }
  }
}
```
