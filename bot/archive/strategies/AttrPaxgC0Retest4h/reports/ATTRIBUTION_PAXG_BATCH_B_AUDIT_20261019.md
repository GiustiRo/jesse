# Atribución PAXG: auditoríaB de diez clocks R/U

Job 29403a45aa424ef5a4a19bdfb4176737 succeeded / exit0. Diez snapshots completos. Resumen recuperado entero48.640bytes; todos los detalles conservados en artifacts policy/pair/origin del job y recreables con fuente. Primer jobB d3ed41c54ce54b6583c08b84c2b689be succeeded, pero el resumen67.672bytes fue truncado por la herramienta; no se parseó. Se repitió sólo análisis con resumen más pequeño y artefactos por política, sin rerun económico ni cambios de reglas.

Se auditan cantidades,fees,PnL,wallet y solapamientos. Pares R/U por timestamp fill y por origenexacto son intersecciones seleccionadas, no universo de oportunidades. La diferencia normalizada de PnL en fills comunes es prácticamente cero como corresponde a su misma gestión. Cinco seeds no son test IID o selección automática de mejor camino.

```json
{
  "policies": {
    "R01": {
      "session_id": "fa518c27-144f-4af4-837c-b00c837110b1",
      "title": "MCP Backtest: ATTR-PAXG-R01 predeclared attribution",
      "trades": 33,
      "directions": {
        "long": {
          "n": 33,
          "net": 108.95460408721473,
          "fees": 207.999658866129,
          "before_fees": 316.9542629533439
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 6,
          "net": -448.1948642144446,
          "static_5bps_RT": -465.4250373042814,
          "static_10bps_RT": -482.6552103941182
        },
        "2022": {
          "n": 3,
          "net": -98.26173458901292,
          "static_5bps_RT": -107.95340325626593,
          "static_10bps_RT": -117.64507192351894
        },
        "2023": {
          "n": 4,
          "net": 178.17868589917322,
          "static_5bps_RT": 159.6134032505065,
          "static_10bps_RT": 141.04812060183983
        },
        "2024": {
          "n": 9,
          "net": 2.237807828292297,
          "static_5bps_RT": -26.29415375637788,
          "static_10bps_RT": -54.82611534104806
        },
        "2025": {
          "n": 11,
          "net": 474.9947091632067,
          "static_5bps_RT": 433.4584291168951,
          "static_10bps_RT": 391.92214907058343
        }
      },
      "status": "economic_result",
      "net": 108.95460408721488,
      "fees": 207.999658866129,
      "before_fees": 316.9542629533439,
      "pf_net": 1.0632284670396688,
      "no_losses": false,
      "dd_engine": -8.419993423574446,
      "cagr_engine": 0.20806346552375565,
      "sharpe_engine": 0.07141914833208925,
      "entry_notional_sum": 230952.25494200003,
      "entry_notional_hours": 32959370.492356904,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.07216537592476113,
      "mean_entry_notional_vs_initial_capital": 0.6998553180060607,
      "max_entry_notional_vs_initial_capital": 1.07895775,
      "executed_fill_notional_sum": 462221.46414695337,
      "net_bps_entry_notional": 4.717624606634695,
      "before_fee_bps_entry_notional": 13.723800316777245,
      "extra_5bps_RT_all_fills_static": -6.6007619495234735,
      "extra_10bps_RT_all_fills_static": -122.15612798626182,
      "net_ex_best_descriptive": -248.61793224837265,
      "best_trade_net": 357.57253633558753,
      "top3_net": 1027.7168992919628,
      "top3_share_of_net": 9.432523828633313,
      "net_ex_top3_descriptive": -918.7622952047479,
      "mean_hold_hours": 141.2540404040404,
      "median_hold_hours": 98.81666666666666,
      "max_hold_hours": 567.3333333333334,
      "holding_hours": 4661.383333333333,
      "time_exposure_pct": 10.20621679219945,
      "recent_closed_cohort_2023_2025": 655.4112028906724,
      "recent_static_5bps_RT": 566.7776786110239,
      "recent_static_10bps_RT": 478.1441543313752,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2021-01-03T20:00:00+00:00",
      "last_entry_UTC": "2025-12-17T16:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:24:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1940.0,
      "entry_hours_UTC": {
        "20:00": 8,
        "08:00": 4,
        "12:00": 5,
        "16:00": 7,
        "00:00": 5,
        "04:00": 4
      },
      "entry_hours_New_York": {
        "15:00": 5,
        "04:00": 4,
        "08:00": 4,
        "12:00": 3,
        "19:00": 1,
        "20:00": 4,
        "16:00": 3,
        "00:00": 2,
        "11:00": 4,
        "23:00": 2,
        "07:00": 1
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
        "max_pnl_error": 1.1368683772161603e-12,
        "max_qty_error": 0.0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 33,
          "exit_STOP": 33
        }
      }
    },
    "R02": {
      "session_id": "a8e6461e-2b14-4130-b9f6-0989a4483c8c",
      "title": "MCP Backtest: ATTR-PAXG-R02 predeclared attribution",
      "trades": 30,
      "directions": {
        "long": {
          "n": 30,
          "net": -153.98605911438506,
          "fees": 201.67509346125607,
          "before_fees": 47.68903434687104
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 2,
          "net": -108.4638173876056,
          "static_5bps_RT": -113.99528143207871,
          "static_10bps_RT": -119.52674547655182
        },
        "2021": {
          "n": 2,
          "net": -76.95109032774981,
          "static_5bps_RT": -83.55490651595257,
          "static_10bps_RT": -90.15872270415532
        },
        "2022": {
          "n": 3,
          "net": 241.8480385013715,
          "static_5bps_RT": 229.13949779842983,
          "static_10bps_RT": 216.43095709548817
        },
        "2023": {
          "n": 6,
          "net": -100.59753634144627,
          "static_5bps_RT": -129.23517814617304,
          "static_10bps_RT": -157.8728199508998
        },
        "2024": {
          "n": 5,
          "net": -408.03455798283767,
          "static_5bps_RT": -423.2760069453751,
          "static_10bps_RT": -438.51745590791256
        },
        "2025": {
          "n": 12,
          "net": 298.21290442388283,
          "static_5bps_RT": 254.89409753717786,
          "static_10bps_RT": 211.57529065047285
        }
      },
      "status": "economic_result",
      "net": -153.986059114385,
      "fees": 201.6750934612561,
      "before_fees": 47.6890343468711,
      "pf_net": 0.901581027887423,
      "no_losses": false,
      "dd_engine": -8.810783631607755,
      "cagr_engine": -0.2972040536758369,
      "sharpe_engine": -0.058343035309698435,
      "entry_notional_sum": 224059.592662,
      "entry_notional_hours": 32255649.6768921,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.0706245613874849,
      "mean_entry_notional_vs_initial_capital": 0.7468653088733332,
      "max_entry_notional_vs_initial_capital": 1.14006816,
      "executed_fill_notional_sum": 448166.87435834686,
      "net_bps_entry_notional": -6.872549275168823,
      "before_fee_bps_entry_notional": 2.1284085086600735,
      "extra_5bps_RT_all_fills_static": -266.0277777039717,
      "extra_10bps_RT_all_fills_static": -378.0694962935585,
      "net_ex_best_descriptive": -510.42873477603666,
      "best_trade_net": 356.44267566165166,
      "top3_net": 899.1390205667143,
      "top3_share_of_net": null,
      "net_ex_top3_descriptive": -1053.1250796810994,
      "mean_hold_hours": 131.41500000000002,
      "median_hold_hours": 83.66666666666666,
      "max_hold_hours": 555.65,
      "holding_hours": 3942.4500000000003,
      "time_exposure_pct": 8.632094062007358,
      "recent_closed_cohort_2023_2025": -210.41918990040108,
      "recent_static_5bps_RT": -297.6170875543703,
      "recent_static_10bps_RT": -384.81498520833946,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-11-09T00:00:00+00:00",
      "last_entry_UTC": "2025-12-17T04:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:24:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 600.0,
      "entry_hours_UTC": {
        "00:00": 6,
        "08:00": 4,
        "04:00": 7,
        "20:00": 6,
        "16:00": 3,
        "12:00": 4
      },
      "entry_hours_New_York": {
        "19:00": 3,
        "03:00": 2,
        "00:00": 4,
        "20:00": 3,
        "16:00": 4,
        "23:00": 3,
        "11:00": 1,
        "08:00": 4,
        "04:00": 2,
        "12:00": 2,
        "15:00": 2
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
        "max_pnl_error": 7.389644451905042e-13,
        "max_qty_error": 0.0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 30,
          "exit_STOP": 30
        }
      }
    },
    "R03": {
      "session_id": "0e7552b8-3491-4925-b230-f31c89b92796",
      "title": "MCP Backtest: ATTR-PAXG-R03 predeclared attribution",
      "trades": 30,
      "directions": {
        "long": {
          "n": 30,
          "net": 869.1587134413251,
          "fees": 192.82187705512342,
          "before_fees": 1061.9805904964485
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 8,
          "net": -296.3254504559959,
          "static_5bps_RT": -319.9412600441966,
          "static_10bps_RT": -343.5570696323973
        },
        "2022": {
          "n": 3,
          "net": -177.4430445157903,
          "static_5bps_RT": -187.40702794720548,
          "static_10bps_RT": -197.37101137862066
        },
        "2023": {
          "n": 4,
          "net": 373.0819267366697,
          "static_5bps_RT": 357.1946172157011,
          "static_10bps_RT": 341.30730769473246
        },
        "2024": {
          "n": 7,
          "net": 610.4914766758545,
          "static_5bps_RT": 585.1357840450016,
          "static_10bps_RT": 559.7800914141488
        },
        "2025": {
          "n": 8,
          "net": 359.353805000587,
          "static_5bps_RT": 327.0533351414002,
          "static_10bps_RT": 294.7528652822134
        }
      },
      "status": "economic_result",
      "net": 869.1587134413251,
      "fees": 192.82187705512342,
      "before_fees": 1061.9805904964485,
      "pf_net": 1.8098221924048983,
      "no_losses": false,
      "dd_engine": -7.269274609205656,
      "cagr_engine": 1.6114074512330268,
      "sharpe_engine": 0.3941256621790786,
      "entry_notional_sum": 213715.539766,
      "entry_notional_hours": 42390444.598437816,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.09281495138911766,
      "mean_entry_notional_vs_initial_capital": 0.7123851325533334,
      "max_entry_notional_vs_initial_capital": 1.0976488100000001,
      "executed_fill_notional_sum": 428493.0601224965,
      "net_bps_entry_notional": 40.66895249605988,
      "before_fee_bps_entry_notional": 49.69131358717411,
      "extra_5bps_RT_all_fills_static": 762.035448410701,
      "extra_10bps_RT_all_fills_static": 654.9121833800768,
      "net_ex_best_descriptive": 413.8563109430569,
      "best_trade_net": 455.3024024982682,
      "top3_net": 1155.2960502734336,
      "top3_share_of_net": 1.3292118371559363,
      "net_ex_top3_descriptive": -286.13733683210853,
      "mean_hold_hours": 206.1461111111111,
      "median_hold_hours": 144.125,
      "max_hold_hours": 812.0666666666667,
      "holding_hours": 6184.383333333333,
      "time_exposure_pct": 13.54086384071933,
      "recent_closed_cohort_2023_2025": 1342.9272084131117,
      "recent_static_5bps_RT": 1269.3837364021035,
      "recent_static_10bps_RT": 1195.8402643910947,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2021-02-10T16:00:00+00:00",
      "last_entry_UTC": "2025-12-25T12:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:31:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 2848.0,
      "entry_hours_UTC": {
        "16:00": 6,
        "04:00": 4,
        "08:00": 6,
        "12:00": 5,
        "20:00": 8,
        "00:00": 1
      },
      "entry_hours_New_York": {
        "11:00": 2,
        "00:00": 4,
        "04:00": 3,
        "08:00": 3,
        "03:00": 3,
        "15:00": 4,
        "16:00": 4,
        "20:00": 1,
        "12:00": 4,
        "07:00": 2
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
        "max_pnl_error": 1.1439738045737613e-12,
        "max_qty_error": 0.0,
        "wallet_error": 3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 30,
          "exit_STOP": 30
        }
      }
    },
    "R04": {
      "session_id": "0edfce4f-695a-4213-8426-304b9af6d5a4",
      "title": "MCP Backtest: ATTR-PAXG-R04 predeclared attribution",
      "trades": 25,
      "directions": {
        "long": {
          "n": 25,
          "net": 1252.4370318555846,
          "fees": 189.6537394463859,
          "before_fees": 1442.0907713019706
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2021": {
          "n": 1,
          "net": 44.44443139090237,
          "static_5bps_RT": 40.24138711312965,
          "static_10bps_RT": 36.03834283535693
        },
        "2022": {
          "n": 3,
          "net": -183.649147461672,
          "static_5bps_RT": -193.94994138207076,
          "static_10bps_RT": -204.2507353024695
        },
        "2023": {
          "n": 7,
          "net": 278.5582214886182,
          "static_5bps_RT": 248.21000843737298,
          "static_10bps_RT": 217.86179538612777
        },
        "2024": {
          "n": 9,
          "net": 691.6821889036994,
          "static_5bps_RT": 655.897318264686,
          "static_10bps_RT": 620.1124476256724
        },
        "2025": {
          "n": 5,
          "net": 421.4013375340367,
          "static_5bps_RT": 396.6750708411414,
          "static_10bps_RT": 371.9488041482461
        }
      },
      "status": "economic_result",
      "net": 1252.4370318555846,
      "fees": 189.65373944638588,
      "before_fees": 1442.0907713019706,
      "pf_net": 2.0881540287092446,
      "no_losses": false,
      "dd_engine": -4.580992551167007,
      "cagr_engine": 2.2890676489804473,
      "sharpe_engine": 0.5488214934814057,
      "entry_notional_sum": 210005.331777,
      "entry_notional_hours": 43442175.73996864,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.0951177433437744,
      "mean_entry_notional_vs_initial_capital": 0.8400213271079999,
      "max_entry_notional_vs_initial_capital": 1.5676243875,
      "executed_fill_notional_sum": 421452.754325302,
      "net_bps_entry_notional": 59.63834447715449,
      "before_fee_bps_entry_notional": 68.66924563769146,
      "extra_5bps_RT_all_fills_static": 1147.0738432742592,
      "extra_10bps_RT_all_fills_static": 1041.7106546929335,
      "net_ex_best_descriptive": 715.9431449407707,
      "best_trade_net": 536.4938869148139,
      "top3_net": 1373.515562842259,
      "top3_share_of_net": 1.0966743460206434,
      "net_ex_top3_descriptive": -121.07853098667442,
      "mean_hold_hours": 216.03933333333333,
      "median_hold_hours": 152.2,
      "max_hold_hours": 814.5,
      "holding_hours": 5400.983333333332,
      "time_exposure_pct": 11.825589712150403,
      "recent_closed_cohort_2023_2025": 1391.6417479263546,
      "recent_static_5bps_RT": 1300.7823975432002,
      "recent_static_10bps_RT": 1209.9230471600463,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": true,
      "first_entry_UTC": "2021-11-09T04:00:00+00:00",
      "last_entry_UTC": "2025-12-22T00:00:00+00:00",
      "last_exit_UTC": "2025-12-23T15:03:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 9364.0,
      "entry_hours_UTC": {
        "04:00": 8,
        "16:00": 3,
        "12:00": 4,
        "00:00": 6,
        "08:00": 3,
        "20:00": 1
      },
      "entry_hours_New_York": {
        "23:00": 2,
        "11:00": 2,
        "07:00": 2,
        "19:00": 3,
        "20:00": 3,
        "00:00": 6,
        "08:00": 2,
        "04:00": 2,
        "15:00": 1,
        "12:00": 1,
        "03:00": 1
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
        "max_pnl_error": 1.1510792319313623e-12,
        "max_qty_error": 0.0,
        "wallet_error": -1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 25,
          "exit_STOP": 25
        }
      }
    },
    "R05": {
      "session_id": "cfff7109-04c5-4420-8a90-fc19ceec6ef8",
      "title": "MCP Backtest: ATTR-PAXG-R05 predeclared attribution",
      "trades": 36,
      "directions": {
        "long": {
          "n": 36,
          "net": 47.85636806682561,
          "fees": 228.91731444382972,
          "before_fees": 276.7736825106556
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 1,
          "net": -14.935348417496332,
          "static_5bps_RT": -17.443985634639674,
          "static_10bps_RT": -19.952622851783012
        },
        "2021": {
          "n": 6,
          "net": 169.4498571211554,
          "static_5bps_RT": 150.47043121521742,
          "static_10bps_RT": 131.49100530927947
        },
        "2022": {
          "n": 6,
          "net": -360.83815484173573,
          "static_5bps_RT": -382.1639199973453,
          "static_10bps_RT": -403.4896851529549
        },
        "2023": {
          "n": 5,
          "net": -300.9189877336935,
          "static_5bps_RT": -321.33339807141203,
          "static_10bps_RT": -341.7478084091306
        },
        "2024": {
          "n": 7,
          "net": -311.0709558241582,
          "static_5bps_RT": -335.83476169784535,
          "static_10bps_RT": -360.59856757153244
        },
        "2025": {
          "n": 11,
          "net": 866.1699577627542,
          "static_5bps_RT": 826.9857164507231,
          "static_10bps_RT": 787.8014751386919
        }
      },
      "status": "economic_result",
      "net": 47.8563680668258,
      "fees": 228.91731444382978,
      "before_fees": 276.7736825106556,
      "pf_net": 1.0318390691132129,
      "no_losses": false,
      "dd_engine": -12.408550923653273,
      "cagr_engine": 0.09161267176265309,
      "sharpe_engine": 0.04287474400608809,
      "entry_notional_sum": 254214.184763,
      "entry_notional_hours": 41268293.38084268,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.09035797289552172,
      "mean_entry_notional_vs_initial_capital": 0.7061505132305556,
      "max_entry_notional_vs_initial_capital": 1.0640855,
      "executed_fill_notional_sum": 508705.1432085107,
      "net_bps_entry_notional": 1.8825215481756679,
      "before_fee_bps_entry_notional": 10.887420887575075,
      "extra_5bps_RT_all_fills_static": -79.31991773530189,
      "extra_10bps_RT_all_fills_static": -206.49620353742955,
      "net_ex_best_descriptive": -318.7382477261987,
      "best_trade_net": 366.5946157930245,
      "top3_net": 875.6351513785352,
      "top3_share_of_net": 18.29715013382991,
      "net_ex_top3_descriptive": -827.7787833117094,
      "mean_hold_hours": 173.83703703703702,
      "median_hold_hours": 149.575,
      "max_hold_hours": 788.0666666666667,
      "holding_hours": 6258.133333333332,
      "time_exposure_pct": 13.702341332399135,
      "recent_closed_cohort_2023_2025": 254.1800142049023,
      "recent_static_5bps_RT": 169.81755668146565,
      "recent_static_10bps_RT": 85.45509915802876,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-12-04T04:00:00+00:00",
      "last_entry_UTC": "2025-12-17T00:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:24:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 1204.0,
      "entry_hours_UTC": {
        "04:00": 12,
        "08:00": 4,
        "20:00": 4,
        "12:00": 7,
        "16:00": 4,
        "00:00": 5
      },
      "entry_hours_New_York": {
        "23:00": 4,
        "03:00": 1,
        "00:00": 8,
        "16:00": 3,
        "04:00": 3,
        "07:00": 4,
        "11:00": 1,
        "12:00": 3,
        "20:00": 2,
        "08:00": 3,
        "19:00": 3,
        "15:00": 1
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
        "max_pnl_error": 1.1368683772161603e-12,
        "max_qty_error": 0.0,
        "wallet_error": -5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 36,
          "exit_STOP": 36
        }
      }
    },
    "U01": {
      "session_id": "6cc08024-0aa2-4cdf-a666-25f4351681bd",
      "title": "MCP Backtest: ATTR-PAXG-U01 predeclared attribution",
      "trades": 118,
      "directions": {
        "long": {
          "n": 118,
          "net": 2902.318898578391,
          "fees": 794.0684911939975,
          "before_fees": 3696.387389772388
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 6,
          "net": -353.61821148869603,
          "static_5bps_RT": -373.76685665464856,
          "static_10bps_RT": -393.91550182060104
        },
        "2021": {
          "n": 20,
          "net": -859.5835803689257,
          "static_5bps_RT": -916.0279908595543,
          "static_10bps_RT": -972.4724013501828
        },
        "2022": {
          "n": 22,
          "net": 38.343815650111,
          "static_5bps_RT": -33.08324678189592,
          "static_10bps_RT": -104.51030921390284
        },
        "2023": {
          "n": 21,
          "net": 539.3601996159832,
          "static_5bps_RT": 448.48984050447905,
          "static_10bps_RT": 357.6194813929749
        },
        "2024": {
          "n": 19,
          "net": 1675.774523459854,
          "static_5bps_RT": 1607.133508122087,
          "static_10bps_RT": 1538.4924927843201
        },
        "2025": {
          "n": 30,
          "net": 1862.0421517100654,
          "static_5bps_RT": 1728.4244824734815,
          "static_10bps_RT": 1594.8068132368974
        }
      },
      "status": "economic_result",
      "net": 2902.3188985783913,
      "fees": 794.0684911939976,
      "before_fees": 3696.387389772389,
      "pf_net": 1.5141207622803052,
      "no_losses": false,
      "dd_engine": -14.109308696330336,
      "cagr_engine": 5.008957309215956,
      "sharpe_engine": 0.6610636323532139,
      "entry_notional_sum": 880450.129854,
      "entry_notional_hours": 163062321.0491211,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.35702907919320614,
      "mean_entry_notional_vs_initial_capital": 0.7461441778423729,
      "max_entry_notional_vs_initial_capital": 1.4677391368000001,
      "executed_fill_notional_sum": 1764596.6470977725,
      "net_bps_entry_notional": 32.964035101677666,
      "before_fee_bps_entry_notional": 41.98292741901622,
      "extra_5bps_RT_all_fills_static": 2461.169736803948,
      "extra_10bps_RT_all_fills_static": 2020.020575029505,
      "net_ex_best_descriptive": 2297.83236505825,
      "best_trade_net": 604.486533520141,
      "top3_net": 1648.1906584901333,
      "top3_share_of_net": 0.5678875120502599,
      "net_ex_top3_descriptive": 1254.128240088258,
      "mean_hold_hours": 194.13319209039543,
      "median_hold_hours": 156.55,
      "max_hold_hours": 1051.65,
      "holding_hours": 22907.71666666666,
      "time_exposure_pct": 50.15702545688093,
      "recent_closed_cohort_2023_2025": 4077.1768747859032,
      "recent_static_5bps_RT": 3784.047831100047,
      "recent_static_10bps_RT": 3490.918787414193,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-10-18T00:00:00+00:00",
      "last_entry_UTC": "2025-12-17T16:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:24:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 72.0,
      "entry_hours_UTC": {
        "00:00": 19,
        "20:00": 29,
        "04:00": 15,
        "16:00": 17,
        "12:00": 17,
        "08:00": 21
      },
      "entry_hours_New_York": {
        "20:00": 16,
        "16:00": 17,
        "15:00": 12,
        "23:00": 8,
        "19:00": 3,
        "11:00": 6,
        "08:00": 10,
        "04:00": 14,
        "00:00": 7,
        "12:00": 11,
        "07:00": 7,
        "03:00": 7
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
        "max_pnl_error": 1.5347723092418164e-12,
        "max_qty_error": 0.0,
        "wallet_error": -5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 118,
          "exit_STOP": 118
        }
      }
    },
    "U02": {
      "session_id": "4d938a9b-653e-4226-9a1c-899b689e6b62",
      "title": "MCP Backtest: ATTR-PAXG-U02 predeclared attribution",
      "trades": 107,
      "directions": {
        "long": {
          "n": 107,
          "net": 37.113934700028324,
          "fees": 685.4999184635237,
          "before_fees": 722.6138531635518
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 5,
          "net": -230.43167103748502,
          "static_5bps_RT": -245.62359782928195,
          "static_10bps_RT": -260.8155246210789
        },
        "2021": {
          "n": 17,
          "net": -443.9935583072614,
          "static_5bps_RT": -499.10460635980826,
          "static_10bps_RT": -554.2156544123551
        },
        "2022": {
          "n": 21,
          "net": -56.30842755050347,
          "static_5bps_RT": -133.44290015628843,
          "static_10bps_RT": -210.57737276207342
        },
        "2023": {
          "n": 21,
          "net": -514.3263940831453,
          "static_5bps_RT": -602.6886466983013,
          "static_10bps_RT": -691.0508993134574
        },
        "2024": {
          "n": 20,
          "net": -392.6026395100943,
          "static_5bps_RT": -456.48112546889826,
          "static_10bps_RT": -520.3596114277022
        },
        "2025": {
          "n": 23,
          "net": 1674.7766251885175,
          "static_5bps_RT": 1593.6215231773153,
          "static_10bps_RT": 1512.4664211661132
        }
      },
      "status": "economic_result",
      "net": 37.11393470002805,
      "fees": 685.4999184635236,
      "before_fees": 722.6138531635517,
      "pf_net": 1.00668130183597,
      "no_losses": false,
      "dd_engine": -18.392769242805596,
      "cagr_engine": 0.07107890035329412,
      "sharpe_engine": 0.04607097307465205,
      "entry_notional_sum": 761305.269144,
      "entry_notional_hours": 123362416.0026823,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.27010513225320176,
      "mean_entry_notional_vs_initial_capital": 0.7115002515364487,
      "max_entry_notional_vs_initial_capital": 1.296779602,
      "executed_fill_notional_sum": 1523333.1521411636,
      "net_bps_entry_notional": 0.4875039777638527,
      "before_fee_bps_entry_notional": 9.49177527663834,
      "extra_5bps_RT_all_fills_static": -343.71935333526284,
      "extra_10bps_RT_all_fills_static": -724.5526413705537,
      "net_ex_best_descriptive": -538.412619982662,
      "best_trade_net": 575.5265546826901,
      "top3_net": 1587.9013438733587,
      "top3_share_of_net": 42.784505515448856,
      "net_ex_top3_descriptive": -1550.7874091733306,
      "mean_hold_hours": 170.39672897196263,
      "median_hold_hours": 105.63333333333334,
      "max_hold_hours": 770.0166666666667,
      "holding_hours": 18232.449999999993,
      "time_exposure_pct": 39.920410754948314,
      "recent_closed_cohort_2023_2025": 767.8475915952781,
      "recent_static_5bps_RT": 534.4517510101157,
      "recent_static_10bps_RT": 301.0559104249537,
      "trading_screen_context_only_not_attribution_decision": false,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-10-15T04:00:00+00:00",
      "last_entry_UTC": "2025-12-17T04:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:24:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 4.0,
      "entry_hours_UTC": {
        "04:00": 24,
        "12:00": 21,
        "20:00": 16,
        "08:00": 14,
        "00:00": 16,
        "16:00": 16
      },
      "entry_hours_New_York": {
        "00:00": 13,
        "07:00": 3,
        "15:00": 6,
        "03:00": 4,
        "19:00": 6,
        "23:00": 11,
        "12:00": 14,
        "08:00": 18,
        "20:00": 10,
        "04:00": 10,
        "16:00": 10,
        "11:00": 2
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
        "max_pnl_error": 1.0658141036401503e-12,
        "max_qty_error": 0.0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 107,
          "exit_STOP": 107
        }
      }
    },
    "U03": {
      "session_id": "e572d0cc-9a77-4998-b2ae-ec335daadf7d",
      "title": "MCP Backtest: ATTR-PAXG-U03 predeclared attribution",
      "trades": 129,
      "directions": {
        "long": {
          "n": 129,
          "net": 2611.0960217982592,
          "fees": 840.2635548479909,
          "before_fees": 3451.3595766462513
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 5,
          "net": -250.29681315879606,
          "static_5bps_RT": -265.5874924656945,
          "static_10bps_RT": -280.87817177259285
        },
        "2021": {
          "n": 25,
          "net": -802.4557850726906,
          "static_5bps_RT": -870.6461358477711,
          "static_10bps_RT": -938.8364866228518
        },
        "2022": {
          "n": 21,
          "net": -726.6286040530101,
          "static_5bps_RT": -797.5293471864069,
          "static_10bps_RT": -868.4300903198036
        },
        "2023": {
          "n": 26,
          "net": 1212.6576360388876,
          "static_5bps_RT": 1104.6406771983998,
          "static_10bps_RT": 996.6237183579118
        },
        "2024": {
          "n": 26,
          "net": 1207.0170494723864,
          "static_5bps_RT": 1112.266546833831,
          "static_10bps_RT": 1017.5160441952754
        },
        "2025": {
          "n": 26,
          "net": 1970.8025385714827,
          "static_5bps_RT": 1861.1386872392404,
          "static_10bps_RT": 1751.474835906998
        }
      },
      "status": "economic_result",
      "net": 2611.0960217982597,
      "fees": 840.2635548479908,
      "before_fees": 3451.3595766462504,
      "pf_net": 1.4023615106836755,
      "no_losses": false,
      "dd_engine": -19.106167261375884,
      "cagr_engine": 4.550144357964969,
      "sharpe_engine": 0.5876032192763613,
      "entry_notional_sum": 931900.492265,
      "entry_notional_hours": 163643502.58925927,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.3583015908855738,
      "mean_entry_notional_vs_initial_capital": 0.722403482375969,
      "max_entry_notional_vs_initial_capital": 1.4277601059999998,
      "executed_fill_notional_sum": 1867252.3441066463,
      "net_bps_entry_notional": 28.019043272012297,
      "before_fee_bps_entry_notional": 37.03570934121584,
      "extra_5bps_RT_all_fills_static": 2144.282935771598,
      "extra_10bps_RT_all_fills_static": 1677.4698497449367,
      "net_ex_best_descriptive": 1784.4943963902429,
      "best_trade_net": 826.601625408017,
      "top3_net": 2181.1461912985997,
      "top3_share_of_net": 0.8353374112210726,
      "net_ex_top3_descriptive": 429.94983049966004,
      "mean_hold_hours": 181.72325581395347,
      "median_hold_hours": 127.03333333333333,
      "max_hold_hours": 1063.65,
      "holding_hours": 23442.300000000007,
      "time_exposure_pct": 51.32750919600632,
      "recent_closed_cohort_2023_2025": 4390.477224082758,
      "recent_static_5bps_RT": 4078.0459112714702,
      "recent_static_10bps_RT": 3765.6145984601844,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-10-27T04:00:00+00:00",
      "last_entry_UTC": "2025-12-25T12:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:31:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 292.0,
      "entry_hours_UTC": {
        "04:00": 21,
        "00:00": 16,
        "16:00": 17,
        "20:00": 28,
        "08:00": 28,
        "12:00": 19
      },
      "entry_hours_New_York": {
        "00:00": 16,
        "19:00": 6,
        "11:00": 7,
        "15:00": 12,
        "23:00": 5,
        "03:00": 7,
        "16:00": 16,
        "12:00": 10,
        "04:00": 21,
        "20:00": 10,
        "08:00": 13,
        "07:00": 6
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
        "max_pnl_error": 1.0018652574217413e-12,
        "max_qty_error": 0.0,
        "wallet_error": -3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 129,
          "exit_STOP": 129
        }
      }
    },
    "U04": {
      "session_id": "f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
      "title": "MCP Backtest: ATTR-PAXG-U04 predeclared attribution",
      "trades": 126,
      "directions": {
        "long": {
          "n": 126,
          "net": 1667.025584690351,
          "fees": 863.9696181936976,
          "before_fees": 2530.995202884049
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 5,
          "net": 1.6752114737634027,
          "static_5bps_RT": -14.849945893920493,
          "static_10bps_RT": -31.375103261604387
        },
        "2021": {
          "n": 17,
          "net": -595.2190161454565,
          "static_5bps_RT": -651.1362966896651,
          "static_10bps_RT": -707.0535772338736
        },
        "2022": {
          "n": 31,
          "net": -641.9534490162005,
          "static_5bps_RT": -756.0583143933661,
          "static_10bps_RT": -870.1631797705318
        },
        "2023": {
          "n": 25,
          "net": 51.2910278832768,
          "static_5bps_RT": -49.951658832716234,
          "static_10bps_RT": -151.19434554870926
        },
        "2024": {
          "n": 23,
          "net": 1124.9211775649478,
          "static_5bps_RT": 1046.6420718229726,
          "static_10bps_RT": 968.3629660809976
        },
        "2025": {
          "n": 25,
          "net": 1726.31063293002,
          "static_5bps_RT": 1612.3966074583252,
          "static_10bps_RT": 1498.4825819866303
        }
      },
      "status": "economic_result",
      "net": 1667.0255846903513,
      "fees": 863.9696181936978,
      "before_fees": 2530.995202884049,
      "pf_net": 1.2754622165355791,
      "no_losses": false,
      "dd_engine": -21.721488669670087,
      "cagr_engine": 3.0013978599566116,
      "sharpe_engine": 0.40052987075932217,
      "entry_notional_sum": 958700.744836,
      "entry_notional_hours": 150646659.77185377,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.3298446745749119,
      "mean_entry_notional_vs_initial_capital": 0.7608736070126986,
      "max_entry_notional_vs_initial_capital": 1.625403105,
      "executed_fill_notional_sum": 1919932.4848748841,
      "net_bps_entry_notional": 17.388383118191076,
      "before_fee_bps_entry_notional": 26.400263236647568,
      "extra_5bps_RT_all_fills_static": 1187.04246347163,
      "extra_10bps_RT_all_fills_static": 707.0593422529091,
      "net_ex_best_descriptive": 1035.9108851990409,
      "best_trade_net": 631.1146994913103,
      "top3_net": 1756.2666322430662,
      "top3_share_of_net": 1.0535331001349277,
      "net_ex_top3_descriptive": -89.24104755271492,
      "mean_hold_hours": 174.52645502645504,
      "median_hold_hours": 106.53333333333333,
      "max_hold_hours": 1059.65,
      "holding_hours": 21990.33333333334,
      "time_exposure_pct": 48.148391428738265,
      "recent_closed_cohort_2023_2025": 2902.522838378245,
      "recent_static_5bps_RT": 2609.0870204485823,
      "recent_static_10bps_RT": 2315.6512025189195,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-10-25T00:00:00+00:00",
      "last_entry_UTC": "2025-12-22T00:00:00+00:00",
      "last_exit_UTC": "2025-12-23T15:03:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 240.0,
      "entry_hours_UTC": {
        "00:00": 23,
        "20:00": 18,
        "16:00": 19,
        "04:00": 23,
        "12:00": 22,
        "08:00": 21
      },
      "entry_hours_New_York": {
        "20:00": 18,
        "15:00": 10,
        "11:00": 3,
        "23:00": 9,
        "07:00": 5,
        "03:00": 8,
        "16:00": 8,
        "00:00": 14,
        "08:00": 17,
        "04:00": 13,
        "19:00": 5,
        "12:00": 16
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
        "max_pnl_error": 1.5916157281026244e-12,
        "max_qty_error": 0.0,
        "wallet_error": 1.8189894035458565e-11,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 126,
          "exit_STOP": 126
        }
      }
    },
    "U05": {
      "session_id": "54613844-7e5d-4911-9342-071f65e0922b",
      "title": "MCP Backtest: ATTR-PAXG-U05 predeclared attribution",
      "trades": 122,
      "directions": {
        "long": {
          "n": 122,
          "net": 3873.5353640048947,
          "fees": 932.1098628756964,
          "before_fees": 4805.64522688059
        }
      },
      "closed_year_cohorts_not_MTM": {
        "2020": {
          "n": 4,
          "net": -133.48785527393744,
          "static_5bps_RT": -147.26670181856403,
          "static_10bps_RT": -161.04554836319065
        },
        "2021": {
          "n": 16,
          "net": -278.39252872301654,
          "static_5bps_RT": -325.44110313832266,
          "static_10bps_RT": -372.4896775536288
        },
        "2022": {
          "n": 29,
          "net": 358.1705063324773,
          "static_5bps_RT": 250.36833883051833,
          "static_10bps_RT": 142.56617132855934
        },
        "2023": {
          "n": 26,
          "net": 388.58867554624123,
          "static_5bps_RT": 262.6233022093531,
          "static_10bps_RT": 136.6579288724649
        },
        "2024": {
          "n": 21,
          "net": 1207.1943457344669,
          "static_5bps_RT": 1117.8571072907337,
          "static_10bps_RT": 1028.5198688470002
        },
        "2025": {
          "n": 26,
          "net": 2331.462220388662,
          "static_5bps_RT": 2197.5556079224552,
          "static_10bps_RT": 2063.648995456248
        }
      },
      "status": "economic_result",
      "net": 3873.5353640048943,
      "fees": 932.1098628756963,
      "before_fees": 4805.645226880591,
      "pf_net": 1.6293339988049484,
      "no_losses": false,
      "dd_engine": -9.73397056635823,
      "cagr_engine": 6.480930642303528,
      "sharpe_engine": 0.8148012420134482,
      "entry_notional_sum": 1033274.8028040001,
      "entry_notional_hours": 179189040.44264224,
      "entry_price_notional_time_proxy_vs_initial_capital": 0.39233893948730564,
      "mean_entry_notional_vs_initial_capital": 0.84694655967541,
      "max_entry_notional_vs_initial_capital": 1.9698845892,
      "executed_fill_notional_sum": 2071355.2508348806,
      "net_bps_entry_notional": 37.48794951249438,
      "before_fee_bps_entry_notional": 46.50887850782291,
      "extra_5bps_RT_all_fills_static": 3355.696551296174,
      "extra_10bps_RT_all_fills_static": 2837.857738587454,
      "net_ex_best_descriptive": 3159.9486035330733,
      "best_trade_net": 713.5867604718211,
      "top3_net": 1980.878264397421,
      "top3_share_of_net": 0.5113876803100533,
      "net_ex_top3_descriptive": 1892.6570996074734,
      "mean_hold_hours": 186.41311475409836,
      "median_hold_hours": 135.75833333333333,
      "max_hold_hours": 991.6166666666667,
      "holding_hours": 22742.399999999998,
      "time_exposure_pct": 49.79506043089857,
      "recent_closed_cohort_2023_2025": 3927.245241669372,
      "recent_static_5bps_RT": 3578.036017422543,
      "recent_static_10bps_RT": 3228.8267931757146,
      "trading_screen_context_only_not_attribution_decision": true,
      "sample_under30_descriptive": false,
      "first_entry_UTC": "2020-10-27T08:00:00+00:00",
      "last_entry_UTC": "2025-12-17T00:00:00+00:00",
      "last_exit_UTC": "2025-12-29T00:24:00+00:00",
      "cash_before_first_fill_hours_not_only_warmup": 296.0,
      "entry_hours_UTC": {
        "08:00": 19,
        "00:00": 20,
        "04:00": 28,
        "12:00": 16,
        "16:00": 22,
        "20:00": 17
      },
      "entry_hours_New_York": {
        "04:00": 10,
        "19:00": 7,
        "23:00": 11,
        "03:00": 9,
        "07:00": 5,
        "11:00": 9,
        "00:00": 17,
        "16:00": 14,
        "20:00": 13,
        "08:00": 11,
        "12:00": 13,
        "15:00": 3
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
        "max_pnl_error": 1.7621459846850485e-12,
        "max_qty_error": 0.0,
        "wallet_error": -1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 122,
          "exit_STOP": 122
        }
      }
    }
  },
  "pairs": {
    "R01__U01": {
      "left_n": 33,
      "right_n": 118,
      "common_n": 13,
      "common_fraction_of_left": 0.3939393939393939,
      "common_fraction_of_right": 0.11016949152542373,
      "mean_normalized_PNL_difference_right_minus_left": -2.0987652054305937e-17,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "R02__U02": {
      "left_n": 30,
      "right_n": 107,
      "common_n": 20,
      "common_fraction_of_left": 0.6666666666666666,
      "common_fraction_of_right": 0.18691588785046728,
      "mean_normalized_PNL_difference_right_minus_left": 4.6144999713698677e-17,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "R03__U03": {
      "left_n": 30,
      "right_n": 129,
      "common_n": 15,
      "common_fraction_of_left": 0.5,
      "common_fraction_of_right": 0.11627906976744186,
      "mean_normalized_PNL_difference_right_minus_left": 2.104978517880607e-17,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "R04__U04": {
      "left_n": 25,
      "right_n": 126,
      "common_n": 11,
      "common_fraction_of_left": 0.44,
      "common_fraction_of_right": 0.0873015873015873,
      "mean_normalized_PNL_difference_right_minus_left": 1.013236212104635e-17,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    },
    "R05__U05": {
      "left_n": 36,
      "right_n": 122,
      "common_n": 15,
      "common_fraction_of_left": 0.4166666666666667,
      "common_fraction_of_right": 0.12295081967213115,
      "mean_normalized_PNL_difference_right_minus_left": 1.5894403848637494e-17,
      "interpretation": "Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect."
    }
  },
  "origin_pairs": {
    "R01__U01": {
      "left_eligible_filled": 33,
      "right_eligible_filled": 118,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 13,
      "mean_entry_price_difference_right_minus_left_bps": 1.708035422500241e-13,
      "mean_fill_delay_difference_right_minus_left_hours": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": -2.0987652054305937e-17,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "R02__U02": {
      "left_eligible_filled": 30,
      "right_eligible_filled": 107,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 20,
      "mean_entry_price_difference_right_minus_left_bps": -5.551115123125783e-14,
      "mean_fill_delay_difference_right_minus_left_hours": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": 4.6144999713698677e-17,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "R03__U03": {
      "left_eligible_filled": 30,
      "right_eligible_filled": 129,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 15,
      "mean_entry_price_difference_right_minus_left_bps": 1.4802973661668753e-13,
      "mean_fill_delay_difference_right_minus_left_hours": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": 2.104978517880607e-17,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "R04__U04": {
      "left_eligible_filled": 25,
      "right_eligible_filled": 126,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 11,
      "mean_entry_price_difference_right_minus_left_bps": -2.0185873175002847e-13,
      "mean_fill_delay_difference_right_minus_left_hours": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": 1.013236212104635e-17,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    },
    "R05__U05": {
      "left_eligible_filled": 36,
      "right_eligible_filled": 122,
      "left_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "right_exclusions": {
        "skipped_multi_or_missing_entry": 0,
        "ambiguous_keys": 0
      },
      "common_origin_n": 15,
      "mean_entry_price_difference_right_minus_left_bps": -1.4802973661668753e-13,
      "mean_fill_delay_difference_right_minus_left_hours": 0.0,
      "mean_normalized_PNL_difference_right_minus_left": 1.5894403848637494e-17,
      "interpretation": "Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe."
    }
  }
}
```
