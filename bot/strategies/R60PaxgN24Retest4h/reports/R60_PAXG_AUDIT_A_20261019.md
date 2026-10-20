# R60 PAXG: auditoría A

Job 921ea63f1aff4d26afe6759e1912dc63 succeeded. Artefacto r60_summary.json completo, 43308 bytes, truncated=false. Auditoría ocho snapshots: fees, PnL, cantidades, wallet y ausencia de solapamientos pasan; cohortes por cierre no representan años MTM. Hashes excluyen IDs. Intersecciones de ejecución y origen son subconjuntos seleccionados por ocupación endógena.

```json
{
  "policies": {
    "Cq": {
      "session_id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
      "title": "MCP Backtest: ATTR-PAXG-Cq predeclared attribution",
      "trades": 35,
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
      "entry_notional_hours": 47406044.53311152,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.10379673439549729,
      "mean_entry_notional_vs_initial_capital": 0.78175288032,
      "max_entry_notional_vs_initial_capital": 1.18656648,
      "executed_fill_notional_sum": 548019.7356774086,
      "net_bps_entry_notional": 19.95919631753693,
      "before_fee_bps_entry_notional": 28.972233822757172,
      "extra_5bps_RT_all_fills_static": 409.10563843438695,
      "extra_10bps_RT_all_fills_static": 272.1007045150348,
      "net_ex_best_descriptive": -91.38798046904276,
      "best_trade_net": 637.4985528227819,
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
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
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
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
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
      },
      "economic_fills_sha256": "ba98ce176d8da1221aa363cb4b4e1c3f588655222cbadb8a424738012d43c6e5",
      "stored_equity_curve_sha256": "69451990cb5679d4ecec251a5155fc7ada6b6e4200eb48776aa7c38ada449ef8"
    },
    "M": {
      "session_id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
      "title": "MCP Backtest: ATTR-PAXG-M predeclared attribution",
      "trades": 38,
      "directions": {
        "long": {
          "n": 38,
          "net": 962.1262139358276,
          "fees": 267.7181832527349,
          "before_fees": 1229.8443971885624
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 6,
          "net": -222.1758726493901,
          "static_5bps_RT": -241.3643302021265,
          "static_10bps_RT": -260.5527877548629
        },
        "2022": {
          "n": 3,
          "net": -91.34542027161518,
          "static_5bps_RT": -101.16066377612431,
          "static_10bps_RT": -110.97590728063344
        },
        "2023": {
          "n": 7,
          "net": -149.53453422456812,
          "static_5bps_RT": -183.8400193593226,
          "static_10bps_RT": -218.1455044940771
        },
        "2024": {
          "n": 7,
          "net": 700.8322782343985,
          "static_5bps_RT": 677.3762759137956,
          "static_10bps_RT": 653.9202735931927
        },
        "2025": {
          "n": 15,
          "net": 724.3497628470029,
          "static_5bps_RT": 662.3826273303087,
          "static_10bps_RT": 600.4154918136144
        }
      },
      "status": "economic_result",
      "net": 962.1262139358278,
      "fees": 267.71818325273483,
      "before_fees": 1229.8443971885627,
      "pf_net": 1.5743577329815752,
      "no_losses": false,
      "dd_engine": -7.64796155547669,
      "cagr_engine": 1.777532757709932,
      "sharpe_engine": 0.3772629743596269,
      "entry_notional_sum": 296849.72586,
      "entry_notional_hours": 53465995.333161615,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.117065150055092,
      "mean_entry_notional_vs_initial_capital": 0.7811834891052633,
      "max_entry_notional_vs_initial_capital": 1.14024608,
      "executed_fill_notional_sum": 594929.2961171885,
      "net_bps_entry_notional": 32.41122123823637,
      "before_fee_bps_entry_notional": 41.42986467734117,
      "extra_5bps_RT_all_fills_static": 813.3938899065306,
      "extra_10bps_RT_all_fills_static": 664.6615658772334,
      "net_ex_best_descriptive": 337.4547898331979,
      "best_trade_net": 624.6714241026299,
      "top3_net": 1597.2537190381138,
      "top3_share_of_net": 1.660129093151024,
      "net_ex_top3_descriptive": -635.127505102286,
      "mean_hold_hours": 182.74649122807014,
      "median_hold_hours": 98.24166666666667,
      "max_hold_hours": 917.4833333333333,
      "holding_hours": 6944.366666666668,
      "time_exposure_pct": 15.204866584924389,
      "recent_closed_cohort_2023_2025": 1275.647506856833,
      "recent_static_5bps_RT": 1155.9188838847813,
      "recent_static_10bps_RT": 1036.1902609127296,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "last_entry_UTC": "2025-12-27T20:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:21:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1764.0,
      "entry_hours_UTC": {
        "12:00": 7,
        "04:00": 4,
        "08:00": 10,
        "16:00": 8,
        "20:00": 6,
        "00:00": 3
      },
      "entry_hours_New_York": {
        "07:00": 4,
        "00:00": 2,
        "08:00": 3,
        "04:00": 5,
        "12:00": 7,
        "16:00": 2,
        "15:00": 4,
        "03:00": 5,
        "20:00": 3,
        "23:00": 2,
        "11:00": 1
      },
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0800249583553523e-12,
        "max_qty_error": 0.0,
        "wallet_error": -1.0913936421275139e-11,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 38,
          "exit_STOP": 38
        }
      },
      "economic_fills_sha256": "b1ebbbb575b72b65420f9c3a149b3fa44a7c1cb4d0ccdec729a448a6e6260259",
      "stored_equity_curve_sha256": "e2304db4dc37a23b920761b990d264d44e22acf25c6d376e333060c234570fe5"
    },
    "P1_Cq": {
      "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
      "title": "MCP Backtest: R60 PAXG P1_Cq R60PaxgN24Retest4h",
      "trades": 36,
      "directions": {
        "long": {
          "n": 36,
          "net": 960.0415136226013,
          "fees": 260.41477650305654,
          "before_fees": 1220.4562901256577
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
          "n": 15,
          "net": 811.1833867042496,
          "static_5bps_RT": 744.7855180511797,
          "static_10bps_RT": 678.3876493981097
        }
      },
      "status": "economic_result",
      "net": 960.0415136226013,
      "fees": 260.41477650305654,
      "before_fees": 1220.456290125658,
      "pf_net": 1.5382710146147627,
      "no_losses": false,
      "dd_engine": -6.919378335744097,
      "cagr_engine": 1.773820071833243,
      "sharpe_engine": 0.3655840693972553,
      "entry_notional_sum": 288739.523525,
      "entry_notional_hours": 50143672.944856,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.10979084109488528,
      "mean_entry_notional_vs_initial_capital": 0.8020542320138888,
      "max_entry_notional_vs_initial_capital": 1.326811827,
      "executed_fill_notional_sum": 578699.5033401257,
      "net_bps_entry_notional": 33.2493973080716,
      "before_fee_bps_entry_notional": 42.2684180962149,
      "extra_5bps_RT_all_fills_static": 815.3666377875699,
      "extra_10bps_RT_all_fills_static": 670.6917619525384,
      "net_ex_best_descriptive": 322.5429607998194,
      "best_trade_net": 637.4985528227819,
      "top3_net": 1677.9119474860147,
      "top3_share_of_net": 1.7477493667483353,
      "net_ex_top3_descriptive": -717.8704338634134,
      "mean_hold_hours": 174.925462962963,
      "median_hold_hours": 108.21666666666667,
      "max_hold_hours": 916.75,
      "holding_hours": 6297.316666666668,
      "time_exposure_pct": 13.788134232498397,
      "recent_closed_cohort_2023_2025": 1250.8912373499118,
      "recent_static_5bps_RT": 1135.2026067413005,
      "recent_static_10bps_RT": 1019.5139761326894,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
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
        "13:44": 1,
        "13:38": 1,
        "07:24": 1,
        "04:19": 1,
        "12:50": 1,
        "06:12": 1,
        "16:02": 1,
        "04:06": 1,
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
        "08:44": 1,
        "09:38": 1,
        "03:24": 1,
        "00:19": 1,
        "08:50": 1,
        "02:12": 1,
        "12:02": 1,
        "00:06": 1,
        "08:27": 1,
        "21:03": 1,
        "08:03": 1,
        "15:43": 1,
        "07:29": 1,
        "15:37": 1
      },
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.1084466677857563e-12,
        "max_qty_error": 0.0,
        "wallet_error": -7.275957614183426e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 36,
          "exit_STOP": 36
        }
      },
      "economic_fills_sha256": "b869fcbe888482d2db40184e1a118dae92ed7b4e2cdb27711a4290aba73bec9b",
      "stored_equity_curve_sha256": "d304c27aac67f44f3e27409f64baa0fed9cd27fc843e619402ba3769e1f78610"
    },
    "P1_M": {
      "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
      "title": "MCP Backtest: R60 PAXG P1_M R60PaxgN24Market4h",
      "trades": 39,
      "directions": {
        "long": {
          "n": 39,
          "net": 1385.7017179838736,
          "fees": 282.4113203992724,
          "before_fees": 1668.1130383831455
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 6,
          "net": -222.1758726493901,
          "static_5bps_RT": -241.3643302021265,
          "static_10bps_RT": -260.5527877548629
        },
        "2022": {
          "n": 3,
          "net": -91.34542027161518,
          "static_5bps_RT": -101.16066377612431,
          "static_10bps_RT": -110.97590728063344
        },
        "2023": {
          "n": 7,
          "net": -149.53453422456812,
          "static_5bps_RT": -183.8400193593226,
          "static_10bps_RT": -218.1455044940771
        },
        "2024": {
          "n": 7,
          "net": 700.8322782343985,
          "static_5bps_RT": 677.3762759137956,
          "static_10bps_RT": 653.9202735931927
        },
        "2025": {
          "n": 16,
          "net": 1147.9252668950485,
          "static_5bps_RT": 1077.7952774080557,
          "static_10bps_RT": 1007.6652879210626
        }
      },
      "status": "economic_result",
      "net": 1385.701717983873,
      "fees": 282.4113203992724,
      "before_fees": 1668.1130383831455,
      "pf_net": 1.8194081220776872,
      "no_losses": false,
      "dd_engine": -7.64796155547669,
      "cagr_engine": 2.520318386957743,
      "sharpe_engine": 0.5028090084653423,
      "entry_notional_sum": 312956.29948,
      "entry_notional_hours": 56357185.88676388,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.12339548495087554,
      "mean_entry_notional_vs_initial_capital": 0.8024520499487179,
      "max_entry_notional_vs_initial_capital": 1.3836701368,
      "executed_fill_notional_sum": 627580.7119983832,
      "net_bps_entry_notional": 44.27780237324888,
      "before_fee_bps_entry_notional": 53.30178817792895,
      "extra_5bps_RT_all_fills_static": 1228.8065399842774,
      "extra_10bps_RT_all_fills_static": 1071.9113619846814,
      "net_ex_best_descriptive": 761.0302938812432,
      "best_trade_net": 624.6714241026299,
      "top3_net": 1652.4410554551528,
      "top3_share_of_net": 1.192494051215706,
      "net_ex_top3_descriptive": -266.73933747127967,
      "mean_hold_hours": 183.12863247863248,
      "median_hold_hours": 102.41666666666667,
      "max_hold_hours": 917.4833333333333,
      "holding_hours": 7142.016666666667,
      "time_exposure_pct": 15.637626262626265,
      "recent_closed_cohort_2023_2025": 1699.2230109048787,
      "recent_static_5bps_RT": 1571.331533962528,
      "recent_static_10bps_RT": 1443.4400570201776,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "last_entry_UTC": "2025-12-27T20:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:21:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1764.0,
      "entry_hours_UTC": {
        "12:00": 7,
        "04:00": 5,
        "08:00": 10,
        "16:00": 8,
        "20:00": 6,
        "00:00": 3
      },
      "entry_hours_New_York": {
        "07:00": 4,
        "00:00": 3,
        "08:00": 3,
        "04:00": 5,
        "12:00": 7,
        "16:00": 2,
        "15:00": 4,
        "03:00": 5,
        "20:00": 3,
        "23:00": 2,
        "11:00": 1
      },
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0800249583553523e-12,
        "max_qty_error": 0.0,
        "wallet_error": -7.275957614183426e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 39,
          "exit_STOP": 39
        }
      },
      "economic_fills_sha256": "e6d0e73c7cf5abbd4db8a9f3a0bb89aa2cba2b3246519eed4e4ca6fbbbd4998f",
      "stored_equity_curve_sha256": "5caf6e46644e01dc962c88c5ca1036969bb3eb472b0a19dc3fdeb32f63130286"
    },
    "P2_Cq": {
      "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
      "title": "MCP Backtest: R60 PAXG P2_Cq R60PaxgN28Retest4h",
      "trades": 35,
      "directions": {
        "long": {
          "n": 35,
          "net": 262.2074518891359,
          "fees": 241.35025060012012,
          "before_fees": 503.55770248925586
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
          "net": -313.67299543342284,
          "static_5bps_RT": -337.6691813682352,
          "static_10bps_RT": -361.66536730304745
        },
        "2024": {
          "n": 7,
          "net": 482.2551862987327,
          "static_5bps_RT": 458.30327259098954,
          "static_10bps_RT": 434.35135888324635
        },
        "2025": {
          "n": 14,
          "net": 384.47498475113696,
          "static_5bps_RT": 327.32585706449015,
          "static_10bps_RT": 270.17672937784334
        }
      },
      "status": "economic_result",
      "net": 262.207451889136,
      "fees": 241.35025060012018,
      "before_fees": 503.55770248925614,
      "pf_net": 1.1437380198190137,
      "no_losses": false,
      "dd_engine": -9.106780300664042,
      "cagr_engine": 0.4976741004134366,
      "sharpe_engine": 0.12787878979034237,
      "entry_notional_sum": 267915.16626,
      "entry_notional_hours": 40526550.756624974,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.08873390864561433,
      "mean_entry_notional_vs_initial_capital": 0.7654719036000001,
      "max_entry_notional_vs_initial_capital": 1.16266875,
      "executed_fill_notional_sum": 536333.8902224893,
      "net_bps_entry_notional": 9.78695814609745,
      "before_fee_bps_entry_notional": 18.79541608333495,
      "extra_5bps_RT_all_fills_static": 128.1239793335137,
      "extra_10bps_RT_all_fills_static": -5.95949322210862,
      "net_ex_best_descriptive": -358.25538890520136,
      "best_trade_net": 620.4628407943374,
      "top3_net": 1427.4371452699145,
      "top3_share_of_net": 5.44392287475281,
      "net_ex_top3_descriptive": -1165.2296933807784,
      "mean_hold_hours": 159.7414285714286,
      "median_hold_hours": 93.93333333333334,
      "max_hold_hours": 916.75,
      "holding_hours": 5590.950000000002,
      "time_exposure_pct": 12.241526537046772,
      "recent_closed_cohort_2023_2025": 553.0571756164469,
      "recent_static_5bps_RT": 447.9599482872442,
      "recent_static_10bps_RT": 342.86272095804213,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "last_entry_UTC": "2025-12-27T20:37:00+00:00",
      "last_exit_UTC": "2025-12-29T00:21:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1764.0333333333333,
      "entry_hours_UTC": {
        "12:02": 2,
        "04:03": 1,
        "12:47": 1,
        "08:10": 1,
        "16:09": 1,
        "20:35": 1,
        "20:23": 1,
        "08:17": 1,
        "00:03": 1,
        "06:21": 1,
        "08:57": 1,
        "16:03": 1,
        "16:01": 4,
        "12:44": 1,
        "12:28": 1,
        "16:40": 1,
        "12:01": 1,
        "04:24": 1,
        "12:25": 1,
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
        "07:02": 2,
        "00:03": 1,
        "08:47": 1,
        "04:10": 1,
        "12:09": 1,
        "16:35": 1,
        "15:23": 1,
        "03:17": 1,
        "20:03": 1,
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
        "07:25": 1,
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
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.4210854715202004e-12,
        "max_qty_error": 0.0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 35,
          "exit_STOP": 35
        }
      },
      "economic_fills_sha256": "51797f4e6d6b08b74c8e384a9b68190e6307c036e1b67cd9a5722dd07ab4ac76",
      "stored_equity_curve_sha256": "5f50d98fd2e5da089b77990043f238fc76236a71c243254e3288fd4daf4f33e8"
    },
    "P2_M": {
      "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
      "title": "MCP Backtest: R60 PAXG P2_M R60PaxgN28Market4h",
      "trades": 38,
      "directions": {
        "long": {
          "n": 38,
          "net": 671.5315157024733,
          "fees": 262.6770458779112,
          "before_fees": 934.2085615803845
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 6,
          "net": -222.1758726493901,
          "static_5bps_RT": -241.3643302021265,
          "static_10bps_RT": -260.5527877548629
        },
        "2022": {
          "n": 3,
          "net": -91.34542027161518,
          "static_5bps_RT": -101.16066377612431,
          "static_10bps_RT": -110.97590728063344
        },
        "2023": {
          "n": 7,
          "net": -399.5995380448951,
          "static_5bps_RT": -433.2638305920301,
          "static_10bps_RT": -466.9281231391651
        },
        "2024": {
          "n": 7,
          "net": 682.4615355151286,
          "static_5bps_RT": 659.6204918115832,
          "static_10bps_RT": 636.7794481080379
        },
        "2025": {
          "n": 15,
          "net": 702.1908111532449,
          "static_5bps_RT": 641.7681563067756,
          "static_10bps_RT": 581.3455014603064
        }
      },
      "status": "economic_result",
      "net": 671.5315157024731,
      "fees": 262.67704587791116,
      "before_fees": 934.2085615803843,
      "pf_net": 1.3880104453725206,
      "no_losses": false,
      "dd_engine": -10.069493774953775,
      "cagr_engine": 1.2544127318831366,
      "sharpe_engine": 0.28133814630238096,
      "entry_notional_sum": 291396.280028,
      "entry_notional_hours": 46639442.92299181,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.10211824076675384,
      "mean_entry_notional_vs_initial_capital": 0.7668323158631579,
      "max_entry_notional_vs_initial_capital": 1.14995048,
      "executed_fill_notional_sum": 583726.7686175804,
      "net_bps_entry_notional": 23.045301595406308,
      "before_fee_bps_entry_notional": 32.05972847321925,
      "extra_5bps_RT_all_fills_static": 525.599823548078,
      "extra_10bps_RT_all_fills_static": 379.6681313936829,
      "net_ex_best_descriptive": 63.24231060321131,
      "best_trade_net": 608.2892050992618,
      "top3_net": 1555.3763553652561,
      "top3_share_of_net": 2.316162859070306,
      "net_ex_top3_descriptive": -883.844839662783,
      "mean_hold_hours": 169.11184210526315,
      "median_hold_hours": 93.79166666666666,
      "max_hold_hours": 917.4833333333333,
      "holding_hours": 6426.250000000001,
      "time_exposure_pct": 14.070437029252062,
      "recent_closed_cohort_2023_2025": 985.0528086234785,
      "recent_static_5bps_RT": 868.1248175263291,
      "recent_static_10bps_RT": 751.1968264291792,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "last_entry_UTC": "2025-12-27T20:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:21:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1764.0,
      "entry_hours_UTC": {
        "12:00": 9,
        "04:00": 3,
        "08:00": 9,
        "16:00": 8,
        "20:00": 6,
        "00:00": 3
      },
      "entry_hours_New_York": {
        "07:00": 5,
        "00:00": 2,
        "08:00": 4,
        "04:00": 4,
        "12:00": 7,
        "16:00": 2,
        "15:00": 4,
        "03:00": 5,
        "20:00": 3,
        "11:00": 1,
        "23:00": 1
      },
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.3073986337985843e-12,
        "max_qty_error": 0.0,
        "wallet_error": 0.0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 38,
          "exit_STOP": 38
        }
      },
      "economic_fills_sha256": "4df36381d2681564dda83f9b0e36345e9a3e858d9f1001ddf005970e52c43717",
      "stored_equity_curve_sha256": "fa2fcc6f6bf5b220ac69a4f4232f1430f1068728643226e775b3c06c15057221"
    },
    "P3_Cq": {
      "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
      "title": "MCP Backtest: R60 PAXG P3_Cq R60PaxgAdx24Retest4h",
      "trades": 41,
      "directions": {
        "long": {
          "n": 41,
          "net": 324.5022024258256,
          "fees": 286.2911119024477,
          "before_fees": 610.793314328273
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 8,
          "net": -321.574018897198,
          "static_5bps_RT": -348.38913754286426,
          "static_10bps_RT": -375.2042561885305
        },
        "2022": {
          "n": 4,
          "net": -174.8859706507475,
          "static_5bps_RT": -188.12369033194136,
          "static_10bps_RT": -201.3614100131352
        },
        "2023": {
          "n": 6,
          "net": 39.5068884297239,
          "static_5bps_RT": 11.484485126129847,
          "static_10bps_RT": -16.537918177464206
        },
        "2024": {
          "n": 7,
          "net": 489.8299184967466,
          "static_5bps_RT": 465.5016175316881,
          "static_10bps_RT": 441.17331656662964
        },
        "2025": {
          "n": 16,
          "net": 291.62538504730065,
          "static_5bps_RT": 224.9783099192312,
          "static_10bps_RT": 158.33123479116173
        }
      },
      "status": "economic_result",
      "net": 324.50220242582566,
      "fees": 286.2911119024477,
      "before_fees": 610.7933143282734,
      "pf_net": 1.1589347242023043,
      "no_losses": false,
      "dd_engine": -8.302396935878553,
      "cagr_engine": 0.6143975204656593,
      "sharpe_engine": 0.14487194173342102,
      "entry_notional_sum": 317795.83879,
      "entry_notional_hours": 54744899.93679449,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.1198653440549888,
      "mean_entry_notional_vs_initial_capital": 0.7751118019268293,
      "max_entry_notional_vs_initial_capital": 1.16143976,
      "executed_fill_notional_sum": 636202.4708943283,
      "net_bps_entry_notional": 10.211027421295382,
      "before_fee_bps_entry_notional": 19.21967627561941,
      "extra_5bps_RT_all_fills_static": 165.45158470224357,
      "extra_10bps_RT_all_fills_static": 6.400966978661472,
      "net_ex_best_descriptive": -305.71080741499827,
      "best_trade_net": 630.2130098408239,
      "top3_net": 1449.8982391230156,
      "top3_share_of_net": 4.468069024753174,
      "net_ex_top3_descriptive": -1125.39603669719,
      "mean_hold_hours": 172.04715447154473,
      "median_hold_hours": 118.03333333333333,
      "max_hold_hours": 916.75,
      "holding_hours": 7053.933333333335,
      "time_exposure_pct": 15.444765574823382,
      "recent_closed_cohort_2023_2025": 820.9621919737715,
      "recent_static_5bps_RT": 701.9644125770495,
      "recent_static_10bps_RT": 582.9666331803269,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": false,
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
        "12:28": 2,
        "20:35": 1,
        "04:09": 1,
        "20:23": 1,
        "08:17": 1,
        "00:03": 1,
        "08:20": 1,
        "08:01": 1,
        "06:21": 1,
        "08:57": 1,
        "00:51": 1,
        "19:58": 1,
        "16:01": 4,
        "12:44": 1,
        "16:40": 1,
        "12:01": 1,
        "04:24": 1,
        "13:02": 1,
        "13:38": 1,
        "07:24": 1,
        "04:19": 1,
        "05:55": 1,
        "12:50": 1,
        "12:00": 1,
        "06:12": 1,
        "16:02": 1,
        "12:27": 1,
        "01:03": 1,
        "12:03": 1,
        "20:43": 1,
        "04:07": 1,
        "20:37": 1
      },
      "entry_hours_New_York": {
        "07:02": 1,
        "00:03": 1,
        "08:47": 1,
        "04:10": 1,
        "12:09": 1,
        "08:28": 2,
        "16:35": 1,
        "23:09": 1,
        "15:23": 1,
        "03:17": 1,
        "20:03": 1,
        "04:20": 1,
        "03:01": 1,
        "01:21": 1,
        "04:57": 1,
        "20:51": 1,
        "15:58": 1,
        "11:01": 1,
        "07:44": 1,
        "12:40": 1,
        "12:01": 3,
        "07:01": 1,
        "23:24": 1,
        "08:02": 1,
        "09:38": 1,
        "03:24": 1,
        "00:19": 1,
        "01:55": 1,
        "08:50": 1,
        "08:00": 1,
        "02:12": 1,
        "12:02": 1,
        "08:27": 1,
        "21:03": 1,
        "08:03": 1,
        "15:43": 1,
        "23:07": 1,
        "15:37": 1
      },
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 9.094947017729282e-13,
        "max_qty_error": 0.0,
        "wallet_error": 3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 40,
          "exit_STOP": 41,
          "entry_MARKET": 1
        }
      },
      "economic_fills_sha256": "e7568fb144ffd4c141b1920183771d380a8c669f1a20ae2ca3eb3659e92c501b",
      "stored_equity_curve_sha256": "c4673ad12d93c5a18741256e5a4a8e1dae471251e473ba7c2a36a0e1d50396de"
    },
    "P3_M": {
      "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
      "title": "MCP Backtest: R60 PAXG P3_M R60PaxgAdx24Market4h",
      "trades": 46,
      "directions": {
        "long": {
          "n": 46,
          "net": 467.98072714989485,
          "fees": 317.65969595929914,
          "before_fees": 785.6404231091944
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 8,
          "net": -323.30289139385695,
          "static_5bps_RT": -350.26173626620107,
          "static_10bps_RT": -377.2205811385451
        },
        "2022": {
          "n": 4,
          "net": -179.14018387558735,
          "static_5bps_RT": -192.39701435333345,
          "static_10bps_RT": -205.65384483107954
        },
        "2023": {
          "n": 10,
          "net": -261.50663595336107,
          "static_5bps_RT": -306.7156499506715,
          "static_10bps_RT": -351.92466394798197
        },
        "2024": {
          "n": 7,
          "net": 678.7255459134898,
          "static_5bps_RT": 656.0094880009508,
          "static_10bps_RT": 633.2934300884117
        },
        "2025": {
          "n": 17,
          "net": 553.2048924592107,
          "static_5bps_RT": 484.86803085287306,
          "static_10bps_RT": 416.5311692465354
        }
      },
      "status": "economic_result",
      "net": 467.9807271498951,
      "fees": 317.65969595929914,
      "before_fees": 785.6404231091942,
      "pf_net": 1.213754179173589,
      "no_losses": false,
      "dd_engine": -10.379926008484453,
      "cagr_engine": 0.8810874299219007,
      "sharpe_engine": 0.19368089130092866,
      "entry_notional_sum": 352562.397521,
      "entry_notional_hours": 59416505.685191624,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.1300939430837091,
      "mean_entry_notional_vs_initial_capital": 0.7664399946108693,
      "max_entry_notional_vs_initial_capital": 1.132622064,
      "executed_fill_notional_sum": 705910.4354651092,
      "net_bps_entry_notional": 13.27369936330264,
      "before_fee_bps_entry_notional": 22.283727040470854,
      "extra_5bps_RT_all_fills_static": 291.50311828361777,
      "extra_10bps_RT_all_fills_static": 115.02550941734046,
      "net_ex_best_descriptive": -136.977933941458,
      "best_trade_net": 604.9586610913531,
      "top3_net": 1546.8602669789857,
      "top3_share_of_net": 3.305393101121285,
      "net_ex_top3_descriptive": -1078.8795398290906,
      "mean_hold_hours": 170.3173913043478,
      "median_hold_hours": 98.24166666666667,
      "max_hold_hours": 917.4833333333333,
      "holding_hours": 7834.600000000002,
      "time_exposure_pct": 17.154055000875815,
      "recent_closed_cohort_2023_2025": 970.4238024193394,
      "recent_static_5bps_RT": 834.1618689031525,
      "recent_static_10bps_RT": 697.8999353869651,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "last_entry_UTC": "2025-12-27T20:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:21:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1764.0,
      "entry_hours_UTC": {
        "12:00": 9,
        "04:00": 7,
        "08:00": 11,
        "16:00": 9,
        "20:00": 6,
        "00:00": 4
      },
      "entry_hours_New_York": {
        "07:00": 4,
        "00:00": 3,
        "08:00": 5,
        "04:00": 6,
        "12:00": 8,
        "23:00": 4,
        "15:00": 4,
        "03:00": 5,
        "20:00": 4,
        "16:00": 2,
        "11:00": 1
      },
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0.0,
        "terminal_records": 0
      },
      "terminal": [],
      "curve_clock_counts": {
        "00:00:00": 2,
        "00:01:00": 1902
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.3642420526593924e-12,
        "max_qty_error": 0.0,
        "wallet_error": 0.0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 46,
          "exit_STOP": 46
        }
      },
      "economic_fills_sha256": "5da1e54aa3895416aea02ebce0d90c436326f87aaf933e263a6e5bed8d2f846b",
      "stored_equity_curve_sha256": "7446ff6e627affe880c33ea5acf0eaaff23ffec352f34e3fa3bd789e0a325253"
    }
  },
  "pairs": {
    "Cq__M": {
      "left_n": 35,
      "right_n": 38,
      "common_n": 0,
      "common_fraction_of_left": 0.0,
      "common_fraction_of_right": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": null,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "P1_Cq__P1_M": {
      "left_n": 36,
      "right_n": 39,
      "common_n": 0,
      "common_fraction_of_left": 0.0,
      "common_fraction_of_right": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": null,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "P2_Cq__P2_M": {
      "left_n": 35,
      "right_n": 38,
      "common_n": 0,
      "common_fraction_of_left": 0.0,
      "common_fraction_of_right": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": null,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "P3_Cq__P3_M": {
      "left_n": 41,
      "right_n": 46,
      "common_n": 1,
      "common_fraction_of_left": 0.024390243902439025,
      "common_fraction_of_right": 0.021739130434782608,
      "mean_normalized_PNL_difference_right_minus_left": -8.673617379884035e-19,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    }
  },
  "origin_pairs": {
    "Cq__M": {
      "left_eligible_filled": 35,
      "right_eligible_filled": 38,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 24,
      "mean_entry_price_difference_right_minus_left_bps": 15.610374061265178,
      "mean_fill_delay_difference_right_minus_left_hours": -0.5527777777777777,
      "mean_normalized_PNL_difference_right_minus_left": -0.0008359940349510286,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "P1_Cq__P1_M": {
      "left_eligible_filled": 36,
      "right_eligible_filled": 39,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 25,
      "mean_entry_price_difference_right_minus_left_bps": 15.247379126674243,
      "mean_fill_delay_difference_right_minus_left_hours": -0.5626666666666666,
      "mean_normalized_PNL_difference_right_minus_left": -0.0008289171066631808,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "P2_Cq__P2_M": {
      "left_eligible_filled": 35,
      "right_eligible_filled": 38,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 26,
      "mean_entry_price_difference_right_minus_left_bps": 14.666914605550458,
      "mean_fill_delay_difference_right_minus_left_hours": -0.4897435897435897,
      "mean_normalized_PNL_difference_right_minus_left": -0.0007776175826728932,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "P3_Cq__P3_M": {
      "left_eligible_filled": 41,
      "right_eligible_filled": 46,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 29,
      "mean_entry_price_difference_right_minus_left_bps": 14.552569282170804,
      "mean_fill_delay_difference_right_minus_left_hours": -0.6879310344827586,
      "mean_normalized_PNL_difference_right_minus_left": -0.0010445545679857939,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    }
  }
}
```