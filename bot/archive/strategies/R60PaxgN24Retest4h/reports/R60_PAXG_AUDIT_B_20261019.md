# R60 PAXG: auditoría B

Job c6e43c29c97142fc85993bb1f205466a succeeded. Artefacto r60_summary.json completo, 32115 bytes, truncated=false. Seis snapshots auditados; fees, PnL, cantidades, wallet y ausencia de solapamientos pasan. Cohortes por cierre no representan años MTM. Hashes excluyen IDs; intersecciones seleccionadas no son efectos causales.

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
    "P4_Cq": {
      "session_id": "2c562667-f6cc-498b-932b-2983bc41b7dd",
      "title": "MCP Backtest: R60 PAXG P4_Cq R60PaxgAdx28Retest4h",
      "trades": 32,
      "directions": {
        "long": {
          "n": 32,
          "net": 127.95384526532457,
          "fees": 216.15780743761638,
          "before_fees": 344.1116527029409
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 5,
          "net": -295.26790000316447,
          "static_5bps_RT": -310.8761235757714,
          "static_10bps_RT": -326.4843471483782
        },
        "2022": {
          "n": 3,
          "net": -86.32438521967192,
          "static_5bps_RT": -96.04479055576826,
          "static_10bps_RT": -105.76519589186458
        },
        "2023": {
          "n": 4,
          "net": -228.08125956367084,
          "static_5bps_RT": -246.2728111469924,
          "static_10bps_RT": -264.464362730314
        },
        "2024": {
          "n": 7,
          "net": 381.3353632788884,
          "static_5bps_RT": 357.6995834371399,
          "static_10bps_RT": 334.0638035953914
        },
        "2025": {
          "n": 13,
          "net": 356.2920267729434,
          "static_5bps_RT": 303.360316308041,
          "static_10bps_RT": 250.4286058431385
        }
      },
      "status": "economic_result",
      "net": 127.95384526532453,
      "fees": 216.15780743761633,
      "before_fees": 344.1116527029409,
      "pf_net": 1.0742084531174207,
      "no_losses": false,
      "dd_engine": -9.15661198500345,
      "cagr_engine": 0.24415930646946027,
      "sharpe_engine": 0.07571707467587487,
      "entry_notional_sum": 240003.28577100002,
      "entry_notional_hours": 35510662.32791667,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.07775149397424388,
      "mean_entry_notional_vs_initial_capital": 0.7500102680343751,
      "max_entry_notional_vs_initial_capital": 1.00103526,
      "executed_fill_notional_sum": 480350.68319470296,
      "net_bps_entry_notional": 5.331337229583271,
      "before_fee_bps_entry_notional": 14.337789234738903,
      "extra_5bps_RT_all_fills_static": 7.866174466648786,
      "extra_10bps_RT_all_fills_static": -112.22149633202696,
      "net_ex_best_descriptive": -471.8434571438979,
      "best_trade_net": 599.7973024092224,
      "top3_net": 1316.4056812968945,
      "top3_share_of_net": 10.288129118489573,
      "net_ex_top3_descriptive": -1188.4518360315699,
      "mean_hold_hours": 153.88385416666665,
      "median_hold_hours": 69.39166666666667,
      "max_hold_hours": 893.7333333333333,
      "holding_hours": 4924.283333333336,
      "time_exposure_pct": 10.781842996438378,
      "recent_closed_cohort_2023_2025": 509.546130488161,
      "recent_static_5bps_RT": 414.78708859818835,
      "recent_static_10bps_RT": 320.0280467082159,
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
        "12:16": 1,
        "20:23": 1,
        "08:17": 1,
        "00:03": 1,
        "06:21": 1,
        "08:57": 1,
        "16:03": 1,
        "16:01": 4,
        "12:46": 1,
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
        "20:37": 1
      },
      "entry_hours_New_York": {
        "07:02": 1,
        "00:03": 1,
        "08:47": 1,
        "04:10": 1,
        "07:16": 1,
        "15:23": 1,
        "03:17": 1,
        "20:03": 1,
        "01:21": 1,
        "04:57": 1,
        "12:03": 1,
        "11:01": 1,
        "07:46": 1,
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
        "max_pnl_error": 1.0231815394945443e-12,
        "max_qty_error": 0.0,
        "wallet_error": 0.0,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 32,
          "exit_STOP": 32
        }
      },
      "economic_fills_sha256": "b186c6a17e1066fd57e81b503954c62140e1b2303e913e027cef0f7d3e99229c",
      "stored_equity_curve_sha256": "8deb3c8cf24acd2c15a62c74657288aaf7dc9a133dbeee2e51196157c9980b21"
    },
    "P4_M": {
      "session_id": "ac0ed1df-254d-4d7d-9fc1-ce5656107504",
      "title": "MCP Backtest: R60 PAXG P4_M R60PaxgAdx28Market4h",
      "trades": 35,
      "directions": {
        "long": {
          "n": 35,
          "net": 469.42486325793527,
          "fees": 235.9707304507689,
          "before_fees": 705.395593708704
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 5,
          "net": -302.57513556738724,
          "static_5bps_RT": -318.19802279774905,
          "static_10bps_RT": -333.82091002811086
        },
        "2022": {
          "n": 3,
          "net": -90.59600065490487,
          "static_5bps_RT": -100.33044040262762,
          "static_10bps_RT": -110.06488015035038
        },
        "2023": {
          "n": 6,
          "net": -314.5236572749898,
          "static_5bps_RT": -342.4318194836649,
          "static_10bps_RT": -370.3399816923401
        },
        "2024": {
          "n": 7,
          "net": 606.5489277985856,
          "static_5bps_RT": 583.9393510571023,
          "static_10bps_RT": 561.329774315619
        },
        "2025": {
          "n": 14,
          "net": 570.5707289566316,
          "static_5bps_RT": 515.3509446344474,
          "static_10bps_RT": 460.13116031226326
        }
      },
      "status": "economic_result",
      "net": 469.4248632579352,
      "fees": 235.9707304507689,
      "before_fees": 705.3955937087042,
      "pf_net": 1.2736454475843284,
      "no_losses": false,
      "dd_engine": -10.016952972445935,
      "cagr_engine": 0.883756652770451,
      "sharpe_engine": 0.21055217953357508,
      "entry_notional_sum": 261837.002704,
      "entry_notional_hours": 39723988.23943498,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.0869766777006371,
      "mean_entry_notional_vs_initial_capital": 0.7481057220114287,
      "max_entry_notional_vs_initial_capital": 1.07024549,
      "executed_fill_notional_sum": 524379.4010017087,
      "net_bps_entry_notional": 17.928133090822456,
      "before_fee_bps_entry_notional": 26.94025620611521,
      "extra_5bps_RT_all_fills_static": 338.330013007508,
      "extra_10bps_RT_all_fills_static": 207.23516275708084,
      "net_ex_best_descriptive": -134.5701378920432,
      "best_trade_net": 603.9950011499784,
      "top3_net": 1468.9817243493899,
      "top3_share_of_net": 3.1293223672778225,
      "net_ex_top3_descriptive": -999.5568610914547,
      "mean_hold_hours": 158.25619047619048,
      "median_hold_hours": 68.3,
      "max_hold_hours": 894.5,
      "holding_hours": 5538.966666666667,
      "time_exposure_pct": 12.12770771296783,
      "recent_closed_cohort_2023_2025": 862.5959994802274,
      "recent_static_5bps_RT": 756.8584762078845,
      "recent_static_10bps_RT": 651.1209529355422,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "last_entry_UTC": "2025-12-27T20:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:21:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1764.0,
      "entry_hours_UTC": {
        "12:00": 8,
        "04:00": 4,
        "08:00": 9,
        "20:00": 5,
        "00:00": 2,
        "16:00": 7
      },
      "entry_hours_New_York": {
        "07:00": 4,
        "00:00": 2,
        "08:00": 4,
        "04:00": 5,
        "15:00": 4,
        "03:00": 4,
        "20:00": 2,
        "12:00": 6,
        "11:00": 1,
        "16:00": 1,
        "23:00": 2
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
        "max_pnl_error": 1.3358203432289883e-12,
        "max_qty_error": 0.0,
        "wallet_error": 0.0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 35,
          "exit_STOP": 35
        }
      },
      "economic_fills_sha256": "d72e41f85104e04aeeda20ee1d924592d8c2e35d5694cfc4c6b19e38ec1c99ae",
      "stored_equity_curve_sha256": "04fb51bd5f75c57cebe988d6fd7de53a98faa0504e7a947ef7d675f3c1e599ac"
    },
    "P5_Cq": {
      "session_id": "9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
      "title": "MCP Backtest: R60 PAXG P5_Cq R60PaxgFast24Retest4h",
      "trades": 35,
      "directions": {
        "long": {
          "n": 35,
          "net": 532.9256826889152,
          "fees": 246.4761416626582,
          "before_fees": 779.4018243515734
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
          "net": -99.26421329554772,
          "static_5bps_RT": -109.1372194950136,
          "static_10bps_RT": -119.01022569447946
        },
        "2023": {
          "n": 5,
          "net": -55.72148213211413,
          "static_5bps_RT": -80.37193261429809,
          "static_10bps_RT": -105.02238309648206
        },
        "2024": {
          "n": 7,
          "net": 494.8565794346956,
          "static_5bps_RT": 470.27788107557535,
          "static_10bps_RT": 445.6991827164551
        },
        "2025": {
          "n": 14,
          "net": 396.7675935541032,
          "static_5bps_RT": 338.1128097935224,
          "static_10bps_RT": 279.45802603294163
        }
      },
      "status": "economic_result",
      "net": 532.9256826889153,
      "fees": 246.47614166265822,
      "before_fees": 779.4018243515736,
      "pf_net": 1.3011636743164046,
      "no_losses": false,
      "dd_engine": -7.052402092339594,
      "cagr_engine": 1.0008332111861806,
      "sharpe_engine": 0.225863618840498,
      "entry_notional_sum": 273472.67871300003,
      "entry_notional_hours": 47356739.96883575,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.10368878080407197,
      "mean_entry_notional_vs_initial_capital": 0.7813505106085715,
      "max_entry_notional_vs_initial_capital": 1.18507528,
      "executed_fill_notional_sum": 547724.7592503516,
      "net_bps_entry_notional": 19.487346421475696,
      "before_fee_bps_entry_notional": 28.500171498650086,
      "extra_5bps_RT_all_fills_static": 395.99449287632746,
      "extra_10bps_RT_all_fills_static": 259.06330306373957,
      "net_ex_best_descriptive": -103.76035604665935,
      "best_trade_net": 636.6860387355747,
      "top3_net": 1464.8195027919385,
      "top3_share_of_net": 2.748637474930998,
      "net_ex_top3_descriptive": -931.8938201030231,
      "mean_hold_hours": 174.18333333333334,
      "median_hold_hours": 98.4,
      "max_hold_hours": 916.75,
      "holding_hours": 6096.416666666668,
      "time_exposure_pct": 13.348258597536056,
      "recent_closed_cohort_2023_2025": 835.9026908566848,
      "recent_static_5bps_RT": 728.0187582547999,
      "recent_static_10bps_RT": 620.1348256529146,
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
        "04:06": 1,
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
        "00:06": 1,
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
        "max_pnl_error": 1.0231815394945443e-12,
        "max_qty_error": 0.0,
        "wallet_error": -1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 35,
          "exit_STOP": 35
        }
      },
      "economic_fills_sha256": "75559c623db30f35f646411bf8cc6a0afd8b6063a3943e7464ab1c60a00f30ad",
      "stored_equity_curve_sha256": "b09a8d7007f95fc72436470fa0b62768d76fa697b8c8cc1595b014a354b74f37"
    },
    "P5_M": {
      "session_id": "09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
      "title": "MCP Backtest: R60 PAXG P5_M R60PaxgFast24Market4h",
      "trades": 38,
      "directions": {
        "long": {
          "n": 38,
          "net": 948.3391088951033,
          "fees": 267.55788663158705,
          "before_fees": 1215.89699552669
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
          "net": -103.50940651887106,
          "static_5bps_RT": -113.38547429774184,
          "static_10bps_RT": -123.26154207661261
        },
        "2023": {
          "n": 7,
          "net": -149.3456908993723,
          "static_5bps_RT": -183.60824462582437,
          "static_10bps_RT": -217.87079835227644
        },
        "2024": {
          "n": 7,
          "net": 699.9511278961663,
          "static_5bps_RT": 676.5245280942814,
          "static_10bps_RT": 653.0979282923965
        },
        "2025": {
          "n": 15,
          "net": 723.4189510665702,
          "static_5bps_RT": 661.5293595756326,
          "static_10bps_RT": 599.6397680846951
        }
      },
      "status": "economic_result",
      "net": 948.339108895103,
      "fees": 267.557886631587,
      "before_fees": 1215.89699552669,
      "pf_net": 1.5666292344865935,
      "no_losses": false,
      "dd_engine": -7.7639248506052745,
      "cagr_engine": 1.7529684167542303,
      "sharpe_engine": 0.3723356919327944,
      "entry_notional_sum": 296678.59220400004,
      "entry_notional_hours": 53409221.74537375,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.11694084284763914,
      "mean_entry_notional_vs_initial_capital": 0.7807331373789473,
      "max_entry_notional_vs_initial_capital": 1.13882944,
      "executed_fill_notional_sum": 594573.0814035267,
      "net_bps_entry_notional": 31.965201865425218,
      "before_fee_bps_entry_notional": 40.98364450545267,
      "extra_5bps_RT_all_fills_static": 799.6958385442213,
      "extra_10bps_RT_all_fills_static": 651.0525681933395,
      "net_ex_best_descriptive": 324.4622815862381,
      "best_trade_net": 623.8768273088649,
      "top3_net": 1595.239112882296,
      "top3_share_of_net": 1.682139962297756,
      "net_ex_top3_descriptive": -646.900003987193,
      "mean_hold_hours": 182.64122807017543,
      "median_hold_hours": 98.24166666666667,
      "max_hold_hours": 917.4833333333333,
      "holding_hours": 6940.366666666668,
      "time_exposure_pct": 15.19610848368074,
      "recent_closed_cohort_2023_2025": 1274.0243880633645,
      "recent_static_5bps_RT": 1154.4456430440898,
      "recent_static_10bps_RT": 1034.866898024815,
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
        "00:00": 2
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
        "23:00": 2,
        "11:00": 1,
        "20:00": 2
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
      "economic_fills_sha256": "3e7704e04cd233c902f869a7bd095ed32d44e95d62eb4ccb0f27feb9e7146845",
      "stored_equity_curve_sha256": "e21dd70aea3e8e90fe1e762c5b8ac3d462ca2bebb781266ece202468763feff3"
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
    "P4_Cq__P4_M": {
      "left_n": 32,
      "right_n": 35,
      "common_n": 0,
      "common_fraction_of_left": 0.0,
      "common_fraction_of_right": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": null,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "P5_Cq__P5_M": {
      "left_n": 35,
      "right_n": 38,
      "common_n": 0,
      "common_fraction_of_left": 0.0,
      "common_fraction_of_right": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": null,
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
    "P4_Cq__P4_M": {
      "left_eligible_filled": 32,
      "right_eligible_filled": 35,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 23,
      "mean_entry_price_difference_right_minus_left_bps": 13.350139795124454,
      "mean_fill_delay_difference_right_minus_left_hours": -0.6079710144927537,
      "mean_normalized_PNL_difference_right_minus_left": -0.0010398566679801716,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "P5_Cq__P5_M": {
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
      "mean_entry_price_difference_right_minus_left_bps": 15.610044485447617,
      "mean_fill_delay_difference_right_minus_left_hours": -0.5548611111111111,
      "mean_normalized_PNL_difference_right_minus_left": -0.0008359274497087792,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    }
  }
}
```