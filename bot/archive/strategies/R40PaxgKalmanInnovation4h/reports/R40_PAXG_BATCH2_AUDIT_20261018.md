# R40 PAXG: auditoría completa 06–10,02 y comparadores

Job 86c6c77a0a3849b2802c5f25a4123724 succeeded / exit0. Ocho snapshots completos, sin truncamiento. La repetición de02 verifica y documenta sus cuatro holdings de8h frente4h nominales; no es backtest ni modificación de receta. Las demás06–10 no exceden horizonte nominal. El motor guarda deuda y espera quote válida; snapshots no prueban la causa exacta de cada espera ni cobertura completa M1.

Sólo se leen inputs y escribe output. Cantidades, fee .00045 sobre todos los fills, PnL y wallet conciliados; cero solapamientos. Antes de fees conserva fills reales; costes5/10bpsRT estáticos aplican2,5/5bps por fill por lado, sin nuevo sizing/decisiones. Cohortes de cierre NO son MTM; no se usa Portfolio00:01 como cierre UTC. Cash anterior al primer fill incluye espera de señal además de entrenamiento. No hay validación OOS ni promoción.

```json
{
  "paxg06": {
    "session_id": "a7ca74dc-e111-40fa-8162-f1500eb87f38",
    "title": "MCP Backtest: PAXG40-06 R40PaxgRangeCenterLead4h primary",
    "trades": 192,
    "stored_metrics": {
      "total": 192,
      "total_winning_trades": 94,
      "total_losing_trades": 98,
      "starting_balance": 10000.0,
      "finishing_balance": 9839.538328488883,
      "win_rate": 0.4895833333333333,
      "win_rate_longs": 0.49019607843137253,
      "win_rate_shorts": 0.4888888888888889,
      "ratio_avg_win_loss": 1.0171171475315741,
      "longs_count": 102,
      "longs_percentage": 53.125,
      "shorts_percentage": 46.875,
      "shorts_count": 90,
      "fee": 1413.2814466183145,
      "net_profit": -160.4616715111381,
      "net_profit_percentage": -1.6046167151113808,
      "average_win": 68.2597773820203,
      "average_loss": 67.11102801450049,
      "expectancy": -0.835737872453862,
      "expectancy_percentage": -0.00835737872453862,
      "expected_net_profit_every_100_trades": -0.835737872453862,
      "average_holding_period": 129495.3125,
      "average_winning_holding_period": 138626.8085106383,
      "average_losing_holding_period": 120736.5306122449,
      "gross_profit": 6416.419073909909,
      "gross_loss": -6576.880745421048,
      "max_drawdown": -10.932195294643886,
      "max_underwater_period": 1488.0,
      "annual_return": -0.3097845352600159,
      "annualization": 365,
      "sharpe_ratio": -0.045256568630749734,
      "calmar_ratio": -0.028336900952710894,
      "sortino_ratio": -0.06698696478013316,
      "omega_ratio": 0.9868271591494538,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 6,
      "losing_streak": 4,
      "largest_losing_trade": -101.17682454274343,
      "largest_winning_trade": 135.82935737617063,
      "current_streak": 1,
      "avg_trades_per_day": 0.10089328950878383,
      "avg_trades_per_week": 0.7062530265614868,
      "avg_trades_per_month": 3.07119173264738
    },
    "directions": {
      "short": {
        "n": 90,
        "net": -241.08149758141764,
        "fees": 651.9207463412581,
        "before_fees": 410.8392487598407
      },
      "long": {
        "n": 102,
        "net": 80.6198260702792,
        "fees": 761.3607002770566,
        "before_fees": 841.9805263473361
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 5,
        "net": -142.81213678178295,
        "static_5bps_RT": -160.00515503761196,
        "static_10bps_RT": -177.19817329344096
      },
      "2021": {
        "n": 36,
        "net": 910.4309669370394,
        "static_5bps_RT": 789.3433113560119,
        "static_10bps_RT": 668.2556557749842
      },
      "2022": {
        "n": 40,
        "net": -761.0223154227455,
        "static_5bps_RT": -926.7531571254718,
        "static_10bps_RT": -1092.483998828198
      },
      "2023": {
        "n": 37,
        "net": 266.9221935362582,
        "static_5bps_RT": 87.02054092102802,
        "static_10bps_RT": -92.88111169420216
      },
      "2024": {
        "n": 32,
        "net": -509.43775336899375,
        "static_5bps_RT": -635.9672161178062,
        "static_10bps_RT": -762.4966788666187
      },
      "2025": {
        "n": 42,
        "net": 75.45737358908644,
        "static_5bps_RT": -99.25635473968501,
        "static_10bps_RT": -273.97008306845646
      }
    },
    "status": "economic_result",
    "net": -160.46167151113812,
    "fees": 1413.2814466183145,
    "before_fees": 1252.8197751071764,
    "pf_net": 0.9756021619180406,
    "no_losses": false,
    "dd_engine": -10.932195294643886,
    "cagr_engine": -0.3097845352600159,
    "sharpe_engine": -0.045256568630749734,
    "entry_notional_sum": 1570097.1478260001,
    "executed_fill_notional_sum": 3140625.4369295877,
    "net_bps_entry_notional": -1.0219856251144575,
    "before_fee_bps_entry_notional": 7.979250053678941,
    "extra_5bps_RT_all_fills_static": -945.6180307435351,
    "extra_10bps_RT_all_fills_static": -1730.774389975932,
    "top3_net": 405.8914634812755,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -566.3531349924136,
    "mean_hold_hours": 35.97092013888889,
    "median_hold_hours": 48.0,
    "max_hold_hours": 48.0,
    "holding_hours": 6906.416666666667,
    "time_exposure_pct": 15.121774099375257,
    "recent_closed_cohort_2023_2025": -167.05818624364912,
    "recent_static_5bps_RT": -648.2030299364632,
    "recent_static_10bps_RT": -1129.3478736292768,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "first_entry_UTC": "2020-10-23T12:00:00+00:00",
    "last_entry_UTC": "2025-12-15T20:00:00+00:00",
    "last_exit_UTC": "2025-12-17T20:00:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 204.0,
    "entry_hours_UTC": {
      "12:00": 47,
      "04:00": 26,
      "00:00": 20,
      "16:00": 49,
      "08:00": 24,
      "20:00": 26
    },
    "entry_hours_New_York": {
      "08:00": 35,
      "23:00": 10,
      "07:00": 12,
      "19:00": 9,
      "11:00": 19,
      "03:00": 6,
      "04:00": 18,
      "00:00": 16,
      "20:00": 11,
      "12:00": 30,
      "16:00": 18,
      "15:00": 8
    },
    "holding_above_nominal_records": [],
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 1.2185807918285718e-12,
      "max_qty_error": 0.0,
      "wallet_error": -2.1827872842550278e-11,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 192,
        "exit_MARKET": 101,
        "exit_STOP": 56,
        "exit_LIMIT": 35
      }
    }
  },
  "paxg07": {
    "session_id": "08061fce-e885-4526-b668-5094344a6644",
    "title": "MCP Backtest: PAXG40-07 R40PaxgWeeklyDailyPullback4h primary",
    "trades": 161,
    "stored_metrics": {
      "total": 161,
      "total_winning_trades": 64,
      "total_losing_trades": 97,
      "starting_balance": 10000.0,
      "finishing_balance": 8934.775701038488,
      "win_rate": 0.39751552795031053,
      "win_rate_longs": 0.43478260869565216,
      "win_rate_shorts": 0.34782608695652173,
      "ratio_avg_win_loss": 1.090665727900405,
      "longs_count": 92,
      "longs_percentage": 57.14285714285714,
      "shorts_percentage": 42.85714285714286,
      "shorts_count": 69,
      "fee": 465.7097170841341,
      "net_profit": -1065.2242989615202,
      "net_profit_percentage": -10.652242989615202,
      "average_win": 42.71746257823519,
      "average_loss": 39.1664113811193,
      "expectancy": -6.616299993549816,
      "expectancy_percentage": -0.06616299993549817,
      "expected_net_profit_every_100_trades": -6.616299993549816,
      "average_holding_period": 404632.17391304346,
      "average_winning_holding_period": 432000.0,
      "average_losing_holding_period": 386575.05154639174,
      "gross_profit": 2733.9176050070523,
      "gross_loss": -3799.1419039685725,
      "max_drawdown": -16.82115789852775,
      "max_underwater_period": 1866.0,
      "annual_return": -2.137179884968954,
      "annualization": 365,
      "sharpe_ratio": -0.6823905742020819,
      "calmar_ratio": -0.1270530779070808,
      "sortino_ratio": -0.9377962094529705,
      "omega_ratio": 0.8519691495196359,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 7,
      "losing_streak": 10,
      "largest_losing_trade": -97.16423791722941,
      "largest_winning_trade": 126.75628769999965,
      "current_streak": 1,
      "avg_trades_per_day": 0.08460322714017811,
      "avg_trades_per_week": 0.5922225899812468,
      "avg_trades_per_month": 2.5753222341470217
    },
    "directions": {
      "short": {
        "n": 69,
        "net": -986.1312537563801,
        "fees": 215.41824622418946,
        "before_fees": -770.7130075321907
      },
      "long": {
        "n": 92,
        "net": -79.09304520513967,
        "fees": 250.29147085994464,
        "before_fees": 171.1984256548048
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 5,
        "net": -67.16316708815488,
        "static_5bps_RT": -74.89411458157572,
        "static_10bps_RT": -82.62506207499656
      },
      "2021": {
        "n": 37,
        "net": -365.5128962943333,
        "static_5bps_RT": -422.38651194070786,
        "static_10bps_RT": -479.2601275870824
      },
      "2022": {
        "n": 30,
        "net": -41.54917923471829,
        "static_5bps_RT": -90.90412104468106,
        "static_10bps_RT": -140.25906285464382
      },
      "2023": {
        "n": 31,
        "net": -994.9932089895632,
        "static_5bps_RT": -1054.3189782417053,
        "static_10bps_RT": -1113.6447474938473
      },
      "2024": {
        "n": 26,
        "net": -81.44415814213771,
        "static_5bps_RT": -119.40290808713604,
        "static_10bps_RT": -157.36165803213436
      },
      "2025": {
        "n": 32,
        "net": 485.4383107873873,
        "static_5bps_RT": 437.95471433198907,
        "static_10bps_RT": 390.4711178765908
      }
    },
    "status": "economic_result",
    "net": -1065.2242989615202,
    "fees": 465.7097170841342,
    "before_fees": -599.514581877386,
    "pf_net": 0.7196145008827413,
    "no_losses": false,
    "dd_engine": -16.82115789852775,
    "cagr_engine": -2.137179884968954,
    "sharpe_engine": -0.6823905742020819,
    "entry_notional_sum": 516984.285488,
    "executed_fill_notional_sum": 1034910.482409187,
    "net_bps_entry_notional": -20.604577911996234,
    "before_fee_bps_entry_notional": -11.596379207377312,
    "extra_5bps_RT_all_fills_static": -1323.951919563817,
    "extra_10bps_RT_all_fills_static": -1582.6795401661138,
    "top3_net": 361.10017414749973,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -1426.32447310902,
    "mean_hold_hours": 112.39782608695651,
    "median_hold_hours": 120.0,
    "max_hold_hours": 120.0,
    "holding_hours": 18096.05,
    "time_exposure_pct": 39.62175950253985,
    "recent_closed_cohort_2023_2025": -590.9990563443134,
    "recent_static_5bps_RT": -735.7671719968527,
    "recent_static_10bps_RT": -880.5352876493905,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "first_entry_UTC": "2020-11-05T00:00:00+00:00",
    "last_entry_UTC": "2025-12-07T00:00:00+00:00",
    "last_exit_UTC": "2025-12-12T00:00:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 504.0,
    "entry_hours_UTC": {
      "00:00": 161
    },
    "entry_hours_New_York": {
      "19:00": 61,
      "20:00": 100
    },
    "holding_above_nominal_records": [],
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 4.440892098500626e-16,
      "max_pnl_error": 4.902744876744691e-13,
      "max_qty_error": 0.0,
      "wallet_error": -9.094947017729282e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 161,
        "exit_STOP": 22,
        "exit_MARKET": 139
      }
    }
  },
  "paxg08": {
    "session_id": "14455aed-0be2-43e2-83de-28df5dc840b8",
    "title": "MCP Backtest: PAXG40-08 R40PaxgDrawdownRecovery4h primary",
    "trades": 120,
    "stored_metrics": {
      "total": 120,
      "total_winning_trades": 48,
      "total_losing_trades": 72,
      "starting_balance": 10000.0,
      "finishing_balance": 8663.748853238862,
      "win_rate": 0.4,
      "win_rate_longs": 0.49122807017543857,
      "win_rate_shorts": 0.31746031746031744,
      "ratio_avg_win_loss": 1.0668769133938438,
      "longs_count": 57,
      "longs_percentage": 47.5,
      "shorts_percentage": 52.5,
      "shorts_count": 63,
      "fee": 761.8058259808564,
      "net_profit": -1336.2511467611457,
      "net_profit_percentage": -13.362511467611457,
      "average_win": 68.5724770019708,
      "average_loss": 64.27402837299645,
      "expectancy": -11.135426223009553,
      "expectancy_percentage": -0.11135426223009552,
      "expected_net_profit_every_100_trades": -11.135426223009553,
      "average_holding_period": 193265.0,
      "average_winning_holding_period": 259200.0,
      "average_losing_holding_period": 149308.33333333334,
      "gross_profit": 3291.4788960945984,
      "gross_loss": -4627.730042855745,
      "max_drawdown": -23.659956080548284,
      "max_underwater_period": 1877.0,
      "annual_return": -2.7136673611012574,
      "annualization": 365,
      "sharpe_ratio": -0.6120927592353166,
      "calmar_ratio": -0.11469452233397266,
      "sortino_ratio": -0.8743254283227537,
      "omega_ratio": 0.8213159041961414,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 6,
      "losing_streak": 11,
      "largest_losing_trade": -95.09910124165513,
      "largest_winning_trade": 247.47309072000002,
      "current_streak": -1,
      "avg_trades_per_day": 0.06305830594298989,
      "avg_trades_per_week": 0.4414081416009292,
      "avg_trades_per_month": 1.9194948329046124
    },
    "directions": {
      "long": {
        "n": 57,
        "net": 139.40626245802855,
        "fees": 352.9736866589027,
        "before_fees": 492.3799491169309
      },
      "short": {
        "n": 63,
        "net": -1475.6574092191734,
        "fees": 408.8321393219537,
        "before_fees": -1066.8252698972206
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 6,
        "net": -317.9432842435383,
        "static_5bps_RT": -337.90899015601303,
        "static_10bps_RT": -357.8746960684877
      },
      "2021": {
        "n": 19,
        "net": -566.4270455940966,
        "static_5bps_RT": -625.4076160115094,
        "static_10bps_RT": -684.3881864289222
      },
      "2022": {
        "n": 23,
        "net": -182.44763995196365,
        "static_5bps_RT": -268.0368531807245,
        "static_10bps_RT": -353.62606640948536
      },
      "2023": {
        "n": 24,
        "net": -664.1118022275587,
        "static_5bps_RT": -765.2375551720476,
        "static_10bps_RT": -866.3633081165365
      },
      "2024": {
        "n": 20,
        "net": -263.8103690781189,
        "static_5bps_RT": -321.0269963515092,
        "static_10bps_RT": -378.24362362489944
      },
      "2025": {
        "n": 28,
        "net": 658.4889943341307,
        "static_5bps_RT": 558.1414052324045,
        "static_10bps_RT": 457.79381613067847
      }
    },
    "status": "economic_result",
    "net": -1336.2511467611455,
    "fees": 761.8058259808564,
    "before_fees": -574.4453207802891,
    "pf_net": 0.7112512755958961,
    "no_losses": false,
    "dd_engine": -23.659956080548284,
    "cagr_engine": -2.7136673611012574,
    "sharpe_engine": -0.6120927592353166,
    "entry_notional_sum": 845671.315147,
    "executed_fill_notional_sum": 1692901.835513014,
    "net_bps_entry_notional": -15.801069787129645,
    "before_fee_bps_entry_notional": -6.79277291887848,
    "extra_5bps_RT_all_fills_static": -1759.4766056393992,
    "extra_10bps_RT_all_fills_static": -2182.7020645176526,
    "top3_net": 654.7172981149996,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -1990.968444876145,
    "mean_hold_hours": 53.68472222222222,
    "median_hold_hours": 72.0,
    "max_hold_hours": 72.0,
    "holding_hours": 6442.166666666668,
    "time_exposure_pct": 14.105286973784088,
    "recent_closed_cohort_2023_2025": -269.4331769715471,
    "recent_static_5bps_RT": -528.1231462911526,
    "recent_static_10bps_RT": -786.8131156107578,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "first_entry_UTC": "2020-10-21T04:00:00+00:00",
    "last_entry_UTC": "2025-12-29T16:00:00+00:00",
    "last_exit_UTC": "2025-12-29T16:58:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 148.0,
    "entry_hours_UTC": {
      "04:00": 11,
      "20:00": 20,
      "16:00": 47,
      "08:00": 16,
      "00:00": 14,
      "12:00": 12
    },
    "entry_hours_New_York": {
      "00:00": 6,
      "15:00": 6,
      "11:00": 20,
      "23:00": 5,
      "03:00": 5,
      "16:00": 14,
      "12:00": 27,
      "20:00": 10,
      "19:00": 4,
      "07:00": 5,
      "08:00": 7,
      "04:00": 11
    },
    "holding_above_nominal_records": [],
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 1.2789769243681803e-12,
      "max_qty_error": 0.0,
      "wallet_error": -7.275957614183426e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 120,
        "exit_STOP": 53,
        "exit_MARKET": 67
      }
    }
  },
  "paxg09": {
    "session_id": "4622a9da-cfc0-45c5-a223-44aad68e1ce0",
    "title": "MCP Backtest: PAXG40-09 R40PaxgCusumDrift4h primary",
    "trades": 283,
    "stored_metrics": {
      "total": 283,
      "total_winning_trades": 119,
      "total_losing_trades": 164,
      "starting_balance": 10000.0,
      "finishing_balance": 7842.852191184301,
      "win_rate": 0.4204946996466431,
      "win_rate_longs": 0.4161073825503356,
      "win_rate_shorts": 0.4253731343283582,
      "ratio_avg_win_loss": 1.0599906278502313,
      "longs_count": 149,
      "longs_percentage": 52.65017667844523,
      "shorts_percentage": 47.34982332155477,
      "shorts_count": 134,
      "fee": 1544.0380829843207,
      "net_profit": -2157.1478088157,
      "net_profit_percentage": -21.571478088157,
      "average_win": 60.39326741884252,
      "average_loss": 56.975284339377794,
      "expectancy": -7.622430419843454,
      "expectancy_percentage": -0.07622430419843454,
      "expected_net_profit_every_100_trades": -7.622430419843454,
      "average_holding_period": 132216.4664310954,
      "average_winning_holding_period": 156856.6386554622,
      "average_losing_holding_period": 114337.31707317074,
      "gross_profit": 7186.79882284226,
      "gross_loss": -9343.946631657958,
      "max_drawdown": -33.26986747798409,
      "max_underwater_period": 1697.0,
      "annual_return": -4.55353156601519,
      "annualization": 365,
      "sharpe_ratio": -0.7594044793346887,
      "calmar_ratio": -0.13686653753665928,
      "sortino_ratio": -1.071114179667286,
      "omega_ratio": 0.8269675853919747,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 6,
      "losing_streak": 10,
      "largest_losing_trade": -98.5376442856685,
      "largest_winning_trade": 178.12695762010293,
      "current_streak": -1,
      "avg_trades_per_day": 0.14871250484888449,
      "avg_trades_per_week": 1.0409875339421915,
      "avg_trades_per_month": 4.526808647600044
    },
    "directions": {
      "long": {
        "n": 149,
        "net": -1195.6178548626947,
        "fees": 841.406889525598,
        "before_fees": -354.21096533709624
      },
      "short": {
        "n": 134,
        "net": -961.5299539530049,
        "fees": 702.6311934587229,
        "before_fees": -258.8987604942828
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 7,
        "net": -24.542168977893496,
        "static_5bps_RT": -45.04089682000084,
        "static_10bps_RT": -65.53962466210818
      },
      "2021": {
        "n": 43,
        "net": -472.81845686830854,
        "static_5bps_RT": -596.2910805216636,
        "static_10bps_RT": -719.7637041750188
      },
      "2022": {
        "n": 57,
        "net": -488.6663152826004,
        "static_5bps_RT": -680.3077482267217,
        "static_10bps_RT": -871.9491811708431
      },
      "2023": {
        "n": 58,
        "net": -913.170891793325,
        "static_5bps_RT": -1123.5845528206337,
        "static_10bps_RT": -1333.9982138479425
      },
      "2024": {
        "n": 51,
        "net": -1030.8134554676012,
        "static_5bps_RT": -1158.2954290440423,
        "static_10bps_RT": -1285.7774026204836
      },
      "2025": {
        "n": 67,
        "net": 772.8634795740286,
        "static_5bps_RT": 588.5729636260728,
        "static_10bps_RT": 404.28244767811714
      }
    },
    "status": "economic_result",
    "net": -2157.1478088157005,
    "fees": 1544.0380829843207,
    "before_fees": -613.1097258313798,
    "pf_net": 0.769139540940107,
    "no_losses": false,
    "dd_engine": -33.26986747798409,
    "cagr_engine": -4.55353156601519,
    "sharpe_engine": -0.7594044793346887,
    "entry_notional_sum": 1715645.526085,
    "executed_fill_notional_sum": 3431195.7399651576,
    "net_bps_entry_notional": -12.573388710068695,
    "before_fee_bps_entry_notional": -3.5736387063035067,
    "extra_5bps_RT_all_fills_static": -3014.94674380699,
    "extra_10bps_RT_all_fills_static": -3872.745678798279,
    "top3_net": 516.1977099053522,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -2673.345518721053,
    "mean_hold_hours": 36.72679623085984,
    "median_hold_hours": 48.0,
    "max_hold_hours": 48.0,
    "holding_hours": 10393.683333333332,
    "time_exposure_pct": 22.757232731943713,
    "recent_closed_cohort_2023_2025": -1171.1208676868978,
    "recent_static_5bps_RT": -1693.3070182386027,
    "recent_static_10bps_RT": -2215.4931687903086,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "first_entry_UTC": "2020-11-04T00:00:00+00:00",
    "last_entry_UTC": "2025-12-29T16:00:00+00:00",
    "last_exit_UTC": "2025-12-30T12:16:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 480.0,
    "entry_hours_UTC": {
      "00:00": 28,
      "16:00": 110,
      "12:00": 44,
      "20:00": 52,
      "08:00": 29,
      "04:00": 20
    },
    "entry_hours_New_York": {
      "19:00": 11,
      "11:00": 43,
      "07:00": 13,
      "15:00": 18,
      "03:00": 13,
      "23:00": 7,
      "12:00": 67,
      "00:00": 13,
      "08:00": 31,
      "16:00": 34,
      "04:00": 16,
      "20:00": 17
    },
    "holding_above_nominal_records": [],
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 1.1510792319313623e-12,
      "max_qty_error": 0.0,
      "wallet_error": -9.094947017729282e-13,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 283,
        "exit_STOP": 94,
        "exit_MARKET": 167,
        "exit_LIMIT": 22
      }
    }
  },
  "paxg10": {
    "session_id": "da3e6ee6-b6f6-4764-a5aa-724d604ab75f",
    "title": "MCP Backtest: PAXG40-10 R40PaxgBetaResidual1h primary",
    "trades": 87,
    "stored_metrics": {
      "total": 87,
      "total_winning_trades": 28,
      "total_losing_trades": 59,
      "starting_balance": 10000.0,
      "finishing_balance": 7650.668536487319,
      "win_rate": 0.3218390804597701,
      "win_rate_longs": 0.37037037037037035,
      "win_rate_shorts": 0.3,
      "ratio_avg_win_loss": 1.0379524170546488,
      "longs_count": 27,
      "longs_percentage": 31.03448275862069,
      "shorts_percentage": 68.9655172413793,
      "shorts_count": 60,
      "fee": 529.8006169249091,
      "net_profit": -2349.331463512684,
      "net_profit_percentage": -23.49331463512684,
      "average_win": 81.45329198838746,
      "average_loss": 78.4749769353819,
      "expectancy": -27.003809925433142,
      "expectancy_percentage": -0.2700380992543314,
      "expected_net_profit_every_100_trades": -27.003809925433142,
      "average_holding_period": 281183.4482758621,
      "average_winning_holding_period": 425828.5714285714,
      "average_losing_holding_period": 212538.30508474575,
      "gross_profit": 2280.692175674849,
      "gross_loss": -4630.023639187532,
      "max_drawdown": -26.851432667941566,
      "max_underwater_period": 1437.0,
      "annual_return": -5.006637395827818,
      "annualization": 365,
      "sharpe_ratio": -1.2750572492831675,
      "calmar_ratio": -0.1864569931050769,
      "sortino_ratio": -1.66200835908042,
      "omega_ratio": 0.6402136384071988,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 3,
      "losing_streak": 8,
      "largest_losing_trade": -97.94565174685083,
      "largest_winning_trade": 227.52165325,
      "current_streak": -8,
      "avg_trades_per_day": 0.04571727180866767,
      "avg_trades_per_week": 0.3200209026606737,
      "avg_trades_per_month": 1.3916337538558439
    },
    "directions": {
      "long": {
        "n": 27,
        "net": -418.56555307256883,
        "fees": 162.66050256667236,
        "before_fees": -255.90505050589658
      },
      "short": {
        "n": 60,
        "net": -1930.765910440115,
        "fees": 367.1401143582369,
        "before_fees": -1563.625796081878
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2021": {
        "n": 15,
        "net": 416.8719394904159,
        "static_5bps_RT": 370.11003723310046,
        "static_10bps_RT": 323.34813497578506
      },
      "2022": {
        "n": 25,
        "net": -334.24386916047547,
        "static_5bps_RT": -423.69300566933686,
        "static_10bps_RT": -513.1421421781982
      },
      "2023": {
        "n": 12,
        "net": -550.1417902392518,
        "static_5bps_RT": -596.622811965573,
        "static_10bps_RT": -643.103833691894
      },
      "2024": {
        "n": 15,
        "net": -819.680745042159,
        "static_5bps_RT": -870.7790660636366,
        "static_10bps_RT": -921.8773870851142
      },
      "2025": {
        "n": 20,
        "net": -1062.1369985612139,
        "static_5bps_RT": -1122.6802931166324,
        "static_10bps_RT": -1183.2235876720508
      }
    },
    "status": "economic_result",
    "net": -2349.331463512684,
    "fees": 529.8006169249093,
    "before_fees": -1819.5308465877747,
    "pf_net": 0.4925875877547485,
    "no_losses": false,
    "dd_engine": -26.851432667941566,
    "cagr_engine": -5.006637395827818,
    "sharpe_engine": -1.2750572492831675,
    "entry_notional_sum": 588013.491766,
    "executed_fill_notional_sum": 1177334.704277576,
    "net_bps_entry_notional": -39.95369998155757,
    "before_fee_bps_entry_notional": -30.943692144258772,
    "extra_5bps_RT_all_fills_static": -2643.665139582078,
    "extra_10bps_RT_all_fills_static": -2937.998815651472,
    "top3_net": 652.4943268098012,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -3001.8257903224853,
    "mean_hold_hours": 78.1065134099617,
    "median_hold_hours": 99.0,
    "max_hold_hours": 120.0,
    "holding_hours": 6795.266666666668,
    "time_exposure_pct": 14.878408361067324,
    "recent_closed_cohort_2023_2025": -2431.9595338426243,
    "recent_static_5bps_RT": -2590.0821711458416,
    "recent_static_10bps_RT": -2748.2048084490584,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "first_entry_UTC": "2021-02-04T21:00:00+00:00",
    "last_entry_UTC": "2025-12-22T21:00:00+00:00",
    "last_exit_UTC": "2025-12-23T00:05:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 2709.0,
    "entry_hours_UTC": {
      "21:00": 28,
      "20:00": 59
    },
    "entry_hours_New_York": {
      "16:00": 87
    },
    "holding_above_nominal_records": [],
    "terminal": [],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_pnl_error": 9.805489753489383e-13,
      "max_qty_error": 0.0,
      "wallet_error": -3.637978807091713e-12,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 87,
        "exit_MARKET": 36,
        "exit_STOP": 51
      }
    }
  },
  "paxg02": {
    "session_id": "6ac794c8-450c-446d-8db8-b2b1b65e8091",
    "title": "MCP Backtest: PAXG40-02 R40PaxgLearnedSeason4h primary",
    "trades": 3645,
    "stored_metrics": {
      "total": 3645,
      "total_winning_trades": 1298,
      "total_losing_trades": 2347,
      "starting_balance": 10000.0,
      "finishing_balance": 724.1586808161899,
      "win_rate": 0.3561042524005487,
      "win_rate_longs": 0.3675675675675676,
      "win_rate_shorts": 0.34428969359331474,
      "ratio_avg_win_loss": 0.8013112252739627,
      "longs_count": 1850,
      "longs_percentage": 50.75445816186557,
      "shorts_percentage": 49.24554183813443,
      "shorts_count": 1795,
      "fee": 8775.540476266307,
      "net_profit": -9275.841319183775,
      "net_profit_percentage": -92.75841319183775,
      "average_win": 5.687387695602253,
      "average_loss": 7.097601426534085,
      "expectancy": -2.5448124332465776,
      "expectancy_percentage": -0.025448124332465776,
      "expected_net_profit_every_100_trades": -2.5448124332465776,
      "average_holding_period": 14310.633744855968,
      "average_winning_holding_period": 14422.187981510015,
      "average_losing_holding_period": 14248.939071154666,
      "gross_profit": 7382.229228891725,
      "gross_loss": -16658.0705480755,
      "max_drawdown": -92.93857617013497,
      "max_underwater_period": 1850.0,
      "annual_return": -39.56154477127212,
      "annualization": 365,
      "sharpe_ratio": -7.131120592890382,
      "calmar_ratio": -0.42567410005130774,
      "sortino_ratio": -7.727040706679005,
      "omega_ratio": 0.34361177545157584,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0.0,
      "winning_streak": 7,
      "losing_streak": 22,
      "largest_losing_trade": -92.81726942938009,
      "largest_winning_trade": 86.27072778,
      "current_streak": -1,
      "avg_trades_per_day": 1.915396043018318,
      "avg_trades_per_week": 13.407772301128226,
      "avg_trades_per_month": 58.3046555494776
    },
    "directions": {
      "short": {
        "n": 1795,
        "net": -5183.605780089595,
        "fees": 4380.98353184441,
        "before_fees": -802.6222482451844
      },
      "long": {
        "n": 1850,
        "net": -4092.2355390941866,
        "fees": 4394.556944421898,
        "before_fees": 302.32140532771695
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 53,
        "net": -663.4391983475352,
        "static_5bps_RT": -826.799699007822,
        "static_10bps_RT": -990.1601996681089
      },
      "2021": {
        "n": 727,
        "net": -3088.5131279750262,
        "static_5bps_RT": -4924.962879841238,
        "static_10bps_RT": -6761.41263170745
      },
      "2022": {
        "n": 731,
        "net": -2658.921872342667,
        "static_5bps_RT": -3991.6311295704427,
        "static_10bps_RT": -5324.340386798218
      },
      "2023": {
        "n": 730,
        "net": -1677.3434614530397,
        "static_5bps_RT": -2547.4016226290887,
        "static_10bps_RT": -3417.4597838051377
      },
      "2024": {
        "n": 730,
        "net": -664.1188371361087,
        "static_5bps_RT": -1076.7247121281182,
        "static_10bps_RT": -1489.3305871201278
      },
      "2025": {
        "n": 674,
        "net": -523.5048219293956,
        "static_5bps_RT": -783.6215405994557,
        "static_10bps_RT": -1043.7382592695158
      }
    },
    "status": "economic_result",
    "net": -9275.841319183774,
    "fees": 8775.540476266307,
    "before_fees": -500.30084291746607,
    "pf_net": 0.4431623222861541,
    "no_losses": false,
    "dd_engine": -92.93857617013497,
    "cagr_engine": -39.56154477127212,
    "sharpe_engine": -7.131120592890382,
    "entry_notional_sum": 9750048.057358,
    "executed_fill_notional_sum": 19501201.058369573,
    "net_bps_entry_notional": -9.513636511959179,
    "before_fee_bps_entry_notional": -0.5131265404788519,
    "extra_5bps_RT_all_fills_static": -14151.141583776167,
    "extra_10bps_RT_all_fills_static": -19026.44184836856,
    "top3_net": 237.5236225921499,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -9513.364941775924,
    "mean_hold_hours": 3.9751760402377685,
    "median_hold_hours": 4.0,
    "max_hold_hours": 8.0,
    "holding_hours": 14489.516666666674,
    "time_exposure_pct": 31.72516348455656,
    "recent_closed_cohort_2023_2025": -2864.9671205185477,
    "recent_static_5bps_RT": -4407.747875356667,
    "recent_static_10bps_RT": -5950.52863019478,
    "descriptive_initial_gate_pass": false,
    "sample_inconclusive": false,
    "first_entry_UTC": "2020-12-05T12:00:00+00:00",
    "last_entry_UTC": "2025-12-30T20:00:00+00:00",
    "last_exit_UTC": "2025-12-31T00:00:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 1236.0,
    "entry_hours_UTC": {
      "12:00": 935,
      "20:00": 478,
      "08:00": 589,
      "16:00": 516,
      "00:00": 632,
      "04:00": 495
    },
    "entry_hours_New_York": {
      "07:00": 411,
      "15:00": 195,
      "03:00": 239,
      "11:00": 116,
      "19:00": 224,
      "04:00": 350,
      "08:00": 524,
      "12:00": 400,
      "20:00": 408,
      "00:00": 379,
      "16:00": 283,
      "23:00": 116
    },
    "holding_above_nominal_records": [
      {
        "opened_at": 1608552000000.0,
        "closed_at": 1608580800000.0,
        "hours": 8.0,
        "type": "short",
        "net": -2.5349530837002106
      },
      {
        "opened_at": 1613001600000.0,
        "closed_at": 1613030400000.0,
        "hours": 8.0,
        "type": "long",
        "net": -4.637098686000051
      },
      {
        "opened_at": 1619323200000.0,
        "closed_at": 1619352000000.0,
        "hours": 8.0,
        "type": "long",
        "net": 4.046775967500401
      },
      {
        "opened_at": 1632888000000.0,
        "closed_at": 1632916800000.0,
        "hours": 8.0,
        "type": "long",
        "net": 1.29875848
      }
    ],
    "terminal": [
      {
        "type": "long",
        "gross": -0.7046160000000444,
        "net": -1.0746196584000445,
        "hours": 4.0
      }
    ],
    "curve_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    },
    "audit": {
      "max_fee_error": 8.881784197001252e-16,
      "max_pnl_error": 7.815970093361102e-13,
      "max_qty_error": 0.0,
      "wallet_error": 3.660716174636036e-11,
      "overlaps": 0,
      "ordertypes": {
        "entry_MARKET": 3645,
        "exit_MARKET": 3576,
        "exit_STOP": 69
      }
    }
  },
  "baseline": {
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
    "first_entry_UTC": "2020-12-27T12:02:00+00:00",
    "last_entry_UTC": "2025-12-27T20:37:00+00:00",
    "last_exit_UTC": "2025-12-29T00:21:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 1764.0333333333333,
    "entry_hours_UTC": {
      "12:02": 1,
      "04:03": 1,
      "12:47": 1,
      "08:10": 1,
      "16:09": 1,
      "20:35": 1,
      "20:23": 1,
      "08:17": 1,
      "00:03": 1,
      "08:01": 1,
      "06:21": 1,
      "08:57": 1,
      "16:03": 1,
      "16:01": 4,
      "12:44": 1,
      "12:28": 1,
      "16:40": 1,
      "12:01": 1,
      "04:24": 1,
      "13:02": 1,
      "13:38": 1,
      "07:24": 1,
      "04:19": 1,
      "12:50": 1,
      "06:12": 1,
      "16:02": 1,
      "12:27": 1,
      "01:03": 1,
      "12:03": 1,
      "20:43": 1,
      "12:29": 1,
      "20:37": 1
    },
    "entry_hours_New_York": {
      "07:02": 1,
      "00:03": 1,
      "08:47": 1,
      "04:10": 1,
      "12:09": 1,
      "16:35": 1,
      "15:23": 1,
      "03:17": 1,
      "20:03": 1,
      "03:01": 1,
      "01:21": 1,
      "04:57": 1,
      "12:03": 1,
      "11:01": 1,
      "07:44": 1,
      "08:28": 1,
      "12:40": 1,
      "12:01": 3,
      "07:01": 1,
      "23:24": 1,
      "08:02": 1,
      "09:38": 1,
      "03:24": 1,
      "00:19": 1,
      "08:50": 1,
      "02:12": 1,
      "12:02": 1,
      "08:27": 1,
      "21:03": 1,
      "08:03": 1,
      "15:43": 1,
      "07:29": 1,
      "15:37": 1
    },
    "holding_above_nominal_records": [],
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
  "weekend075": {
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
    "first_entry_UTC": "2020-10-18T20:00:00+00:00",
    "last_entry_UTC": "2025-11-16T21:00:00+00:00",
    "last_exit_UTC": "2025-11-17T03:01:00+00:00",
    "cash_before_first_fill_hours_not_only_warmup": 92.0,
    "entry_hours_UTC": {
      "20:00": 33,
      "21:00": 27
    },
    "entry_hours_New_York": {
      "16:00": 60
    },
    "holding_above_nominal_records": [],
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
