# X03 R3 — FIXED_STRESS_B

2026 cerrado; muestra de desarrollo2020-10-15→2025-12-31 exclusiva. Auditoría de fills, cantidades, fees,PNL,wallet yterminal, con MTM UTC diario. Costes+5/+10 adicionales al fee de CADA sesión, sobre recorridos y cantidades fijos; no confundir overlays de sesiones ya estresadas con el estrés original. Monthclassallcalendar, denominadores activos se conservan en auditoría.

## [X03S_B](http://localhost:9200/#/backtest/1277ad3f-21b3-41d7-9c04-9485dec1f907)

```json
{
  "audit": {
    "n": 274,
    "net": 9344.147577013517,
    "gross_before_fees": 12038.850036585933,
    "fees": 2694.702459572416,
    "pf_from_trades": 1.6187592623254055,
    "PF_engine": 1.6187592623254048,
    "sharpe_engine": 1.282756353341886,
    "cagr_engine": 13.490864792592072,
    "dd_engine": -8.282318217158057,
    "plus5_samefills": 8381.753841451942,
    "plus10_samefills": 7419.36010589037,
    "exbest": 7471.55063286585,
    "ex3best": 5430.466592899296,
    "ex3best_plus10_samefills": 3529.5020177954166,
    "time_any_position_pct": 38.306876569159805,
    "entry_notional_time_initial_equity": 0.3797076554997592,
    "entry_turnover_initial_equity": 192.2958523488653,
    "two_side_turnover_initial_equity": 384.95749422463086,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4591.424301860271,
        "fees": 209.40426496277615,
        "plus10": 4441.84982688686,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.0510329606793827
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 2588.8187565316452,
        "fees": 1601.658627260521,
        "plus10": 1444.776879916987,
        "time_open_pct": 10.7327246452969,
        "entry_notional_time_initial_equity": 0.0557590950126347
      },
      "PAXG-USDT:long": {
        "n": 39,
        "net": 657.7170224199344,
        "fees": 637.8419020235104,
        "plus10": 202.11566383171268,
        "time_open_pct": 14.987300753196706,
        "entry_notional_time_initial_equity": 0.16711869094819404
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1506.187496201667,
        "fees": 245.7976653256091,
        "plus10": 1330.6177352548034,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.10579690885954791
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 7180.243058391914,
        "fees": 1811.062892223297
      },
      "PAXG-USDT": {
        "n": 39,
        "net": 657.7170224199344,
        "fees": 637.8419020235104
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1506.187496201667,
        "fees": 245.7976653256091
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 383.2169045617464,
        "by_symbol": {
          "BTC-USDT": 253.2851584627375,
          "PAXG-USDT": 0,
          "SPY-USDT": 129.93174609900888
        }
      },
      "2021": {
        "n": 53,
        "net": 1950.9132408682856,
        "by_symbol": {
          "BTC-USDT": 1853.8690273048446,
          "PAXG-USDT": -250.29466175441178,
          "SPY-USDT": 347.33887531785285
        }
      },
      "2022": {
        "n": 41,
        "net": 1057.6226209539427,
        "by_symbol": {
          "BTC-USDT": 1302.4761903552605,
          "PAXG-USDT": -123.75829305648642,
          "SPY-USDT": -121.09527634483122
        }
      },
      "2023": {
        "n": 55,
        "net": 2135.851178068271,
        "by_symbol": {
          "BTC-USDT": 2298.58404936882,
          "PAXG-USDT": -291.540083527325,
          "SPY-USDT": 128.8072122267764
        }
      },
      "2024": {
        "n": 56,
        "net": 1919.1069770745914,
        "by_symbol": {
          "BTC-USDT": 402.1867792474759,
          "PAXG-USDT": 1043.6965842310378,
          "SPY-USDT": 473.223613596078
        }
      },
      "2025": {
        "n": 57,
        "net": 1897.4366554866808,
        "by_symbol": {
          "BTC-USDT": 1069.841853652779,
          "PAXG-USDT": 279.61347652711993,
          "SPY-USDT": 547.9813253067821
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 125,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3809.9003550918787,
        "fees": 178.6168381292548,
        "gross": 3988.517193221134,
        "plus10": 3682.3168992852684,
        "exbest": 1937.3034109442174,
        "ex3": 91.2383545551728,
        "ex3_plus10": -18.344221735508455,
        "year_net": {
          "2020": 475.1237882209012,
          "2021": 1528.7938021690584,
          "2022": -172.0385273566849,
          "2023": 1794.8253208926415,
          "2024": 593.3638502442001,
          "2025": -410.1678790782373
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 781.5239467683921,
        "fees": 30.78742683352134,
        "gross": 812.3113736019134,
        "plus10": 759.532927601591,
        "exbest": 199.0054124483334,
        "ex3": -140.66804830419113,
        "ex3_plus10": -148.64497813091774,
        "year_net": {
          "2021": 339.67346075252453,
          "2025": 441.8504860158675
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 1685.1644426616194,
        "fees": 671.3853938704276,
        "gross": 2356.549836532048,
        "plus10": 1205.6034470398856,
        "exbest": 1356.2941531120787,
        "ex3": 777.3592246991155,
        "ex3_plus10": 321.2654320263347,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 361.91867125574686,
          "2022": 758.1358325195827,
          "2023": 115.84301326405034,
          "2024": -130.74700562580563,
          "2025": 645.8492602400453
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 903.6543138700248,
        "fees": 930.2732333900924,
        "gross": 1833.927547260117,
        "plus10": 239.1734328771022,
        "exbest": 723.1504613235965,
        "ex3": 378.1086671234883,
        "ex3_plus10": -251.02309343559693,
        "year_net": {
          "2020": -156.00330076616365,
          "2021": -376.5169068724855,
          "2022": 716.3788851923625,
          "2023": 387.9157152121272,
          "2024": -60.43006537091861,
          "2025": 392.30998647510296
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 39,
        "net": 657.7170224199344,
        "fees": 637.8419020235104,
        "gross": 1295.5589244434454,
        "plus10": 202.11566383171268,
        "exbest": -265.07966022164476,
        "ex3": -1233.5238325610867,
        "ex3_plus10": -1663.3647255639082,
        "year_net": {
          "2021": -250.29466175441178,
          "2022": -123.75829305648642,
          "2023": -291.540083527325,
          "2024": 1043.6965842310378,
          "2025": 279.61347652711993
        }
      },
      "SPY-USDT:long:LIMIT": {
        "n": 9,
        "net": 1414.6894568838966,
        "fees": 165.26131498118556,
        "gross": 1579.950771865082,
        "plus10": 1296.645660468764,
        "exbest": 693.7312912773453,
        "ex3": 56.96995243657352,
        "ex3_plus10": -17.58501671044766,
        "year_net": {
          "2020": 129.93174609900888,
          "2021": 347.33887531785285,
          "2022": -121.09527634483122,
          "2023": 266.99388088726437,
          "2024": 243.53890561781958,
          "2025": 547.9813253067821
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 3,
        "net": 91.49803931777046,
        "fees": 80.53635034442354,
        "gross": 172.034389662194,
        "plus10": 33.97207478603937,
        "exbest": -31.256514058288474,
        "ex3": 0,
        "ex3_plus10": 0,
        "year_net": {
          "2023": -138.18666866048798,
          "2024": 229.68470797825844
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4800.8285668230465,
        "exbest": 2718.8273577126106,
        "ex3best": 872.7623013235647,
        "ex3best_plus10": 741.1887058660825,
        "years": {
          "2020": {
            "n": 3,
            "net": 475.12378822090125,
            "plus10": 466.90032690386886
          },
          "2021": {
            "n": 6,
            "net": 1868.467262921583,
            "plus10": 1853.5854064005575
          },
          "2022": {
            "n": 4,
            "net": -172.0385273566849,
            "plus10": -182.47148116066936
          },
          "2023": {
            "n": 4,
            "net": 1794.8253208926417,
            "plus10": 1768.5548378940962
          },
          "2024": {
            "n": 8,
            "net": 593.3638502442001,
            "plus10": 551.756468151613
          },
          "2025": {
            "n": 6,
            "net": 31.68260693763017,
            "plus10": -16.475731302606874
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4190.477383792163,
        "exbest": 2259.9484669820913,
        "ex3best": 1681.0135385691333,
        "ex3best_plus10": 560.4388649034275,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.83862975816362,
            "plus10": -243.1288870682934
          },
          "2021": {
            "n": 40,
            "net": -14.598235616738904,
            "plus10": -125.6442621493536
          },
          "2022": {
            "n": 33,
            "net": 1474.5147177119445,
            "plus10": 1330.9122429635504
          },
          "2023": {
            "n": 40,
            "net": 503.7587284761782,
            "plus10": 190.6440397771605
          },
          "2024": {
            "n": 38,
            "net": -191.1770709967239,
            "plus10": -425.450328900248
          },
          "2025": {
            "n": 33,
            "net": 1038.1592467151488,
            "plus10": 717.4440752941711
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1295.5589244434461,
        "exbest": -265.07966022164476,
        "ex3best": -1233.5238325610867,
        "ex3best_plus10": -1663.3647255639082,
        "years": {
          "2021": {
            "n": 6,
            "net": -250.29466175441175,
            "plus10": -291.6734768631107
          },
          "2022": {
            "n": 3,
            "net": -123.75829305648642,
            "plus10": -147.72838967759296
          },
          "2023": {
            "n": 7,
            "net": -291.54008352732507,
            "plus10": -392.08299522374887
          },
          "2024": {
            "n": 7,
            "net": 1043.696584231038,
            "plus10": 972.4734942759537
          },
          "2025": {
            "n": 16,
            "net": 279.61347652712004,
            "plus10": 61.1270313202113
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1751.9851615272757,
        "exbest": 785.2293305951157,
        "ex3best": 148.467991754344,
        "ex3best_plus10": 16.387058075591682,
        "years": {
          "2020": {
            "n": 1,
            "net": 129.93174609900888,
            "plus10": 126.40167796866814
          },
          "2021": {
            "n": 1,
            "net": 347.33887531785285,
            "plus10": 337.42148557447354
          },
          "2022": {
            "n": 1,
            "net": -121.09527634483122,
            "plus10": -127.60858232234307
          },
          "2023": {
            "n": 4,
            "net": 128.80721222677644,
            "plus10": 63.1415307177067
          },
          "2024": {
            "n": 3,
            "net": 473.22361359607805,
            "plus10": 417.779464476096
          },
          "2025": {
            "n": 2,
            "net": 547.9813253067821,
            "plus10": 513.4821588402021
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "X03S_B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6229508196721312,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6031746031746031,
      "win_months_active": 0.6031746031746031,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.03889380782924645
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.039742603856865455
      ],
      "daily_close_drawdown_pct": -8.341075322521164,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.057709216675995434,
          "SPY-USDT": -0.04419022862349414
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.057709216675995434,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.014465626700596949
        },
        "SPY-USDT": {
          "BTC-USDT": -0.04419022862349414,
          "PAXG-USDT": -0.014465626700596949,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04176490528852406,
        "2021-12-31 00:00:00+00:00": 0.18396483533048213,
        "2022-12-31 00:00:00+00:00": 0.08574764563724058,
        "2023-12-31 00:00:00+00:00": 0.15949003952863405,
        "2024-12-31 00:00:00+00:00": 0.12359324619174483,
        "2025-12-31 00:00:00+00:00": 0.10875612394915657
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.0880842950007577,
        "SPY-USDT": -0.05225693363154035
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.0880842950007577,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.026103912156715918
      },
      "SPY-USDT": {
        "BTC-USDT": -0.05225693363154035,
        "PAXG-USDT": -0.026103912156715918,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 30,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 14,
        "both_negative_and_portfolio_negative": 0
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.03889380782924645,
        "contributions": {
          "BTC-USDT": -0.029817694424631787,
          "PAXG-USDT": -0.009076113404614632,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.031883536897538756,
        "contributions": {
          "BTC-USDT": -0.031883536897538686,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.019689719150733254,
        "contributions": {
          "BTC-USDT": -0.019689719150733226,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-06-30 00:00:00+00:00",
        "portfolio_return": -0.01937248020874971,
        "contributions": {
          "BTC-USDT": -0.01937248020874972,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01622180959119135,
        "contributions": {
          "BTC-USDT": -0.015335238274987784,
          "PAXG-USDT": -0.008585308731375252,
          "SPY-USDT": 0.00769873741517175
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.01531558557324908,
        "contributions": {
          "BTC-USDT": -0.015315585573249108,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010567141203166708,
        "contributions": {
          "BTC-USDT": -0.0010309032983314688,
          "PAXG-USDT": -0.0095362379048353,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.010380514888091108,
        "contributions": {
          "BTC-USDT": -0.010380514888091174,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.007433995079969669,
        "contributions": {
          "BTC-USDT": -0.007433995079969688,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006479291261069942,
        "contributions": {
          "BTC-USDT": 0.0029486656184733715,
          "PAXG-USDT": -0.009427956879543257,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -8.341075322521164,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -770.2017664138884,
        "PAXG-USDT": -206.83842407193345,
        "SPY-USDT": 0
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 8381.75384145194,
        "extra_cost": 962.3937355615772,
        "samefills_cagr_pct": 12.385441318969171,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 36,
          "win_months_all": 0.5901639344262295,
          "win_months_active": 0.5901639344262295,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 36,
          "win_months_all": 0.5714285714285714,
          "win_months_active": 0.5714285714285714,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -8.847069855847023,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.040103042306473435
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.039925332140773984,
          "2021-12-31 00:00:00+00:00": 0.17594944849780703,
          "2022-12-31 00:00:00+00:00": 0.07894051064789331,
          "2023-12-31 00:00:00+00:00": 0.1427166137139917,
          "2024-12-31 00:00:00+00:00": 0.11393419791239978,
          "2025-12-31 00:00:00+00:00": 0.09446167232627412
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 7419.360105890364,
        "extra_cost": 1924.7874711231543,
        "samefills_cagr_pct": 11.232207965169305,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 35,
          "win_months_all": 0.5737704918032787,
          "win_months_active": 0.5737704918032787,
          "quarters_total": 19,
          "positive_quarters": 13,
          "win_quarters": 0.6842105263157895
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 35,
          "win_months_all": 0.5555555555555556,
          "win_months_active": 0.5555555555555556,
          "quarters_total": 21,
          "positive_quarters": 14,
          "win_quarters": 0.6666666666666666
        },
        "daily_close_drawdown_pct": -9.568646231517008,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04131980701893323
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03808575899302369,
          "2021-12-31 00:00:00+00:00": 0.16790565381875,
          "2022-12-31 00:00:00+00:00": 0.07201531742142775,
          "2023-12-31 00:00:00+00:00": 0.12543369010642413,
          "2024-12-31 00:00:00+00:00": 0.10368058577395667,
          "2025-12-31 00:00:00+00:00": 0.07901354769142088
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 10120.640721982367,
        "mean_month_USDT": 165.9121429833175,
        "median_month_USDT": 65.59128733454418,
        "sum_positive_months": 13152.160424841519,
        "sum_negative_months": -3031.519702859152,
        "worst_month": "2021-04",
        "worst_month_USDT": -441.0139329197209,
        "best3_share_positive_mtm": 0.2809772717867331,
        "class_counts": {
          "loss_base": 23,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 35
        },
        "positive_months": 38,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 17,
          "zero_months": 0,
          "net_before_actual_fees": 12731.192982072282,
          "fee_total": 2610.552260089917,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-08",
              "gross": 1.1818525125504777,
              "fee": 49.15220054324121,
              "net": -47.97034803069073
            },
            {
              "month": "2023-11",
              "gross": 16.121910758828328,
              "fee": 54.16942365188219,
              "net": -38.04751289305386
            },
            {
              "month": "2024-07",
              "gross": 3.153678611336673,
              "fee": 84.45760868858919,
              "net": -81.30393007725252
            },
            {
              "month": "2025-01",
              "gross": 41.16252158754972,
              "fee": 83.44651162335097,
              "net": -42.28399003580125
            },
            {
              "month": "2025-07",
              "gross": 101.68088343286733,
              "fee": 116.00293033196219,
              "net": -14.322046899094858
            },
            {
              "month": "2025-09",
              "gross": 74.41906735699438,
              "fee": 93.10489847638807,
              "net": -18.685831119393697
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 0,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 36,
            "extra_cost": 932.3400928892565,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 5.949442052493396,
                "extra": 10.568659485878683,
                "after": -4.619217433382801
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -3031.519702859152,
            "already_negative_after_sum": -3397.6123160993757
          },
          "10": {
            "positive_months": 35,
            "extra_cost": 1864.680185778513,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 5.949442052493396,
                "extra": 21.137318971757367,
                "after": -15.187876919262635
              },
              {
                "month": "2025-11",
                "base": 19.524011652745685,
                "extra": 19.793741159638124,
                "after": -0.2697295068974199
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -3031.519702859152,
            "already_negative_after_sum": -3763.704929339616
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 9344.147577013511,
        "mean_month_USDT": 148.31980280973826,
        "median_month_USDT": 53.78174846000002,
        "sum_positive_months": 13152.160424841519,
        "sum_negative_months": -3808.0128478280076,
        "worst_month": "2025-12",
        "worst_month_USDT": -585.2661889760457,
        "best3_share_positive_mtm": 0.2809772717867331,
        "class_counts": {
          "loss_base": 25,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 35
        },
        "positive_months": 38,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 19,
          "zero_months": 0,
          "net_before_actual_fees": 12038.850036585925,
          "fee_total": 2694.7024595724147,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-08",
              "gross": 1.1818525125504777,
              "fee": 49.15220054324121,
              "net": -47.97034803069073
            },
            {
              "month": "2023-11",
              "gross": 16.121910758828328,
              "fee": 54.16942365188219,
              "net": -38.04751289305386
            },
            {
              "month": "2024-07",
              "gross": 3.153678611336673,
              "fee": 84.45760868858919,
              "net": -81.30393007725252
            },
            {
              "month": "2025-01",
              "gross": 41.16252158754972,
              "fee": 83.44651162335097,
              "net": -42.28399003580125
            },
            {
              "month": "2025-07",
              "gross": 101.68088343286733,
              "fee": 116.00293033196219,
              "net": -14.322046899094858
            },
            {
              "month": "2025-09",
              "gross": 74.41906735699438,
              "fee": 93.10489847638807,
              "net": -18.685831119393697
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 0,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 36,
            "extra_cost": 962.393735561577,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 5.949442052493396,
                "extra": 10.568659485878683,
                "after": -4.619217433382801
              }
            ],
            "already_negative_months": 25,
            "already_negative_base_sum": -3808.0128478280076,
            "already_negative_after_sum": -4204.159103740547
          },
          "10": {
            "positive_months": 35,
            "extra_cost": 1924.787471123154,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 5.949442052493396,
                "extra": 21.137318971757367,
                "after": -15.187876919262635
              },
              {
                "month": "2025-11",
                "base": 19.524011652745685,
                "extra": 19.793741159638124,
                "after": -0.2697295068974199
              }
            ],
            "already_negative_months": 25,
            "already_negative_base_sum": -3808.0128478280076,
            "already_negative_after_sum": -4600.305359653108
          }
        }
      }
    }
  }
}
```

## [N204S_B](http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f)

```json
{
  "audit": {
    "n": 274,
    "net": 10267.311379187322,
    "gross_before_fees": 13007.318032983758,
    "fees": 2740.0066537964353,
    "pf_from_trades": 1.6762948428780338,
    "PF_engine": 1.676294842878034,
    "sharpe_engine": 1.3735710230285618,
    "cagr_engine": 14.510217938203684,
    "dd_engine": -9.026628677513893,
    "plus5_samefills": 9288.737574260023,
    "plus10_samefills": 8310.163769332727,
    "exbest": 8362.372518905828,
    "ex3best": 6248.295085206965,
    "ex3best_plus10_samefills": 4315.624159678396,
    "time_any_position_pct": 38.40109914170608,
    "entry_notional_time_initial_equity": 0.3919592915003288,
    "entry_turnover_initial_equity": 195.56403087070277,
    "two_side_turnover_initial_equity": 391.4295219709193,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4636.887791770246,
        "fees": 215.9445574644643,
        "plus10": 4482.641679295628,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05246729506595325
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 3385.998755417234,
        "fees": 1610.359113507295,
        "plus10": 2235.7422457691655,
        "time_open_pct": 10.848623518421206,
        "entry_notional_time_initial_equity": 0.057701937385603204
      },
      "PAXG-USDT:long": {
        "n": 39,
        "net": 698.8884425006825,
        "fees": 660.5783515380272,
        "plus10": 227.04676283066337,
        "time_open_pct": 14.987300753196706,
        "entry_notional_time_initial_equity": 0.17295653780152093
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1545.5363894991651,
        "fees": 253.12463128665004,
        "plus10": 1364.7330814372722,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.10883352124725146
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 8022.886547187472,
        "fees": 1826.3036709717596
      },
      "PAXG-USDT": {
        "n": 39,
        "net": 698.8884425006825,
        "fees": 660.5783515380272
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1545.5363894991651,
        "fees": 253.12463128665004
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 383.2169045617464,
        "by_symbol": {
          "BTC-USDT": 253.2851584627375,
          "PAXG-USDT": 0,
          "SPY-USDT": 129.93174609900888
        }
      },
      "2021": {
        "n": 51,
        "net": 2044.3895775715273,
        "by_symbol": {
          "BTC-USDT": 1947.9196886454872,
          "PAXG-USDT": -253.4815209622899,
          "SPY-USDT": 349.95140988833
        }
      },
      "2022": {
        "n": 45,
        "net": 1196.4652255450044,
        "by_symbol": {
          "BTC-USDT": 1444.5057194739948,
          "PAXG-USDT": -124.2849198186047,
          "SPY-USDT": -123.75557411038558
        }
      },
      "2023": {
        "n": 54,
        "net": 2317.538201724522,
        "by_symbol": {
          "BTC-USDT": 2488.2695284490587,
          "PAXG-USDT": -301.661387674639,
          "SPY-USDT": 130.93006095010207
        }
      },
      "2024": {
        "n": 55,
        "net": 2354.284654523316,
        "by_symbol": {
          "BTC-USDT": 779.9257401306893,
          "PAXG-USDT": 1085.084787841729,
          "SPY-USDT": 489.27412655089813
        }
      },
      "2025": {
        "n": 57,
        "net": 1971.4168152612083,
        "by_symbol": {
          "BTC-USDT": 1108.9807120255105,
          "PAXG-USDT": 293.23148311448733,
          "SPY-USDT": 569.2046201212116
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 125,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3834.2934552322554,
        "fees": 184.12168678541238,
        "gross": 4018.4151420176668,
        "plus10": 3702.777964671245,
        "exbest": 1929.354594950783,
        "ex3": 44.051385673142306,
        "ex3_plus10": -69.10253185196228,
        "year_net": {
          "2020": 475.1237882209012,
          "2021": 1529.404229734846,
          "2022": -179.88897003879882,
          "2023": 1825.406450669598,
          "2024": 614.961404654727,
          "2025": -430.71344800901875
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 802.5943365379896,
        "fees": 31.822870679051928,
        "gross": 834.4172072170416,
        "plus10": 779.8637146243811,
        "exbest": 197.38027490676,
        "ex3": -147.61461859081663,
        "ex3_plus10": -155.98547087812233,
        "year_net": {
          "2021": 344.99489349757664,
          "2025": 457.59944304041306
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 2421.074083404405,
        "fees": 660.3862601255291,
        "gross": 3081.4603435299337,
        "plus10": 1949.36961188617,
        "exbest": 2077.025165106426,
        "ex3": 1468.5331983703904,
        "ex3_plus10": 1021.4717234120378,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 566.9613520726689,
          "2022": 915.4352099049495,
          "2023": 261.65202462830894,
          "2024": 71.63959474534548,
          "2025": 671.2212310451329
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 964.9246720128272,
        "fees": 949.9728533817645,
        "gross": 1914.8975253945916,
        "plus10": 286.37263388299516,
        "exbest": 779.7201983063342,
        "ex3": 419.41510307904093,
        "ex3_plus10": -222.39201077507565,
        "year_net": {
          "2020": -156.00330076616365,
          "2021": -493.4407866596046,
          "2022": 708.9594796078443,
          "2023": 401.2110531511514,
          "2024": 93.32474073061672,
          "2025": 410.8734859489831
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 39,
        "net": 698.8884425006825,
        "fees": 660.5783515380272,
        "gross": 1359.4667940387098,
        "plus10": 227.04676283066337,
        "exbest": -257.66348098462794,
        "ex3": -1272.677433869162,
        "ex3_plus10": -1717.613689059861,
        "year_net": {
          "2021": -253.4815209622899,
          "2022": -124.2849198186047,
          "2023": -301.661387674639,
          "2024": 1085.084787841729,
          "2025": 293.23148311448733
        }
      },
      "SPY-USDT:long:LIMIT": {
        "n": 9,
        "net": 1450.5422367414708,
        "fees": 170.2311750577194,
        "gross": 1620.7734117991904,
        "plus10": 1328.9485402716714,
        "exbest": 701.6926627869618,
        "ex3": 54.51519594795306,
        "ex3_plus10": -22.39748472889471,
        "year_net": {
          "2020": 129.93174609900888,
          "2021": 349.95140988833,
          "2022": -123.75557411038558,
          "2023": 272.79993773192854,
          "2024": 252.41009701137745,
          "2025": 569.2046201212116
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 3,
        "net": 94.99415275769417,
        "fees": 82.89345622893063,
        "gross": 177.8876089866248,
        "plus10": 35.78454116560086,
        "exbest": -31.030320326726297,
        "ex3": 0,
        "ex3_plus10": 0,
        "year_net": {
          "2023": -141.86987678182646,
          "2024": 236.86402953952063
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4852.832349234709,
        "exbest": 2731.9489314887714,
        "ex3best": 846.6457222111317,
        "ex3best_plus10": 710.7611827724199,
        "years": {
          "2020": {
            "n": 3,
            "net": 475.12378822090125,
            "plus10": 466.90032690386886
          },
          "2021": {
            "n": 6,
            "net": 1874.3991232324227,
            "plus10": 1859.4255980031462
          },
          "2022": {
            "n": 4,
            "net": -179.88897003879882,
            "plus10": -190.677535549637
          },
          "2023": {
            "n": 4,
            "net": 1825.406450669598,
            "plus10": 1798.4086422783894
          },
          "2024": {
            "n": 8,
            "net": 614.9614046547271,
            "plus10": 572.0930507046345
          },
          "2025": {
            "n": 6,
            "net": 26.885995031394373,
            "plus10": -23.50840304477464
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4996.3578689245305,
        "exbest": 3041.9498371192467,
        "ex3best": 2433.457870383206,
        "ex3best_plus10": 1307.8443572950341,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.83862975816362,
            "plus10": -243.1288870682934
          },
          "2021": {
            "n": 38,
            "net": 73.52056541306413,
            "plus10": -34.88042316613236
          },
          "2022": {
            "n": 37,
            "net": 1624.394689512793,
            "plus10": 1464.84715680909
          },
          "2023": {
            "n": 39,
            "net": 662.8630777794601,
            "plus10": 352.9940847612644
          },
          "2024": {
            "n": 37,
            "net": 164.96433547596206,
            "plus10": -66.46306253589634
          },
          "2025": {
            "n": 33,
            "net": 1082.0947169941169,
            "plus10": 762.3733769691347
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1359.4667940387103,
        "exbest": -257.66348098462794,
        "ex3best": -1272.677433869162,
        "ex3best_plus10": -1717.613689059861,
        "years": {
          "2021": {
            "n": 6,
            "net": -253.4815209622899,
            "plus10": -295.22584001314436
          },
          "2022": {
            "n": 3,
            "net": -124.2849198186047,
            "plus10": -148.6018580154332
          },
          "2023": {
            "n": 7,
            "net": -301.661387674639,
            "plus10": -404.8009840982983
          },
          "2024": {
            "n": 7,
            "net": 1085.084787841729,
            "plus10": 1011.148054834703
          },
          "2025": {
            "n": 16,
            "net": 293.2314831144873,
            "plus10": 64.52739012283604
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1798.6610207858143,
        "exbest": 796.6868155446559,
        "ex3best": 149.5093487056471,
        "ex3best_plus10": 13.387056436706075,
        "years": {
          "2020": {
            "n": 1,
            "net": 129.93174609900888,
            "plus10": 126.40167796866814
          },
          "2021": {
            "n": 1,
            "net": 349.95140988833,
            "plus10": 339.9594257779085
          },
          "2022": {
            "n": 1,
            "net": -123.75557411038558,
            "plus10": -130.41196852091775
          },
          "2023": {
            "n": 4,
            "net": 130.93006095010207,
            "plus10": 63.38323900196335
          },
          "2024": {
            "n": 3,
            "net": 489.274126550898,
            "plus10": 432.0276574998869
          },
          "2025": {
            "n": 2,
            "net": 569.2046201212116,
            "plus10": 533.3730497097631
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "N204S_B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 39,
        "win_months_all": 0.639344262295082,
        "win_months_active": 0.639344262295082,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6190476190476191,
      "win_months_active": 0.6190476190476191,
      "win_quarters": 0.8095238095238095,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.038848358930312465
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.03999068035568787
      ],
      "daily_close_drawdown_pct": -9.016913649811242,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.05686964789050525,
          "SPY-USDT": -0.041471581527636595
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.05686964789050525,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.014546551320338889
        },
        "SPY-USDT": {
          "BTC-USDT": -0.041471581527636595,
          "PAXG-USDT": -0.014546551320338889,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04176490528852406,
        "2021-12-31 00:00:00+00:00": 0.19293771742976462,
        "2022-12-31 00:00:00+00:00": 0.09627479171191311,
        "2023-12-31 00:00:00+00:00": 0.17010613650971895,
        "2024-12-31 00:00:00+00:00": 0.1476817377857611,
        "2025-12-31 00:00:00+00:00": 0.10775186795994296
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.0867055141640384,
        "SPY-USDT": -0.04930466583726134
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.0867055141640384,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.02616661754939643
      },
      "SPY-USDT": {
        "BTC-USDT": -0.04930466583726134,
        "PAXG-USDT": -0.02616661754939643,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 29,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 1,
        "both_nonzero": 14,
        "both_negative_and_portfolio_negative": 1
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.038848358930312465,
        "contributions": {
          "BTC-USDT": -0.029772348861851945,
          "PAXG-USDT": -0.00907601006846049,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.03200314133146376,
        "contributions": {
          "BTC-USDT": -0.03200314133146369,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.02464440069934226,
        "contributions": {
          "BTC-USDT": -0.02464440069934219,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01624503285280232,
        "contributions": {
          "BTC-USDT": -0.015358409556835356,
          "PAXG-USDT": -0.008585126781087523,
          "SPY-USDT": 0.007698503485120555
        }
      },
      {
        "month": "2023-10-31 00:00:00+00:00",
        "portfolio_return": -0.01562527047553286,
        "contributions": {
          "BTC-USDT": -0.00627611930296148,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.00934915117257136
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.01475124479890444,
        "contributions": {
          "BTC-USDT": -0.014751244798904462,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.013427240727367673,
        "contributions": {
          "BTC-USDT": -0.01342724072736767,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010767341620081194,
        "contributions": {
          "BTC-USDT": -0.001231028612018869,
          "PAXG-USDT": -0.009536313008062177,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.010216421736991332,
        "contributions": {
          "BTC-USDT": -0.010216421736991254,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009224408755350466,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009224408755350574,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-08-20 00:00:00+00:00",
      "drawdown_pct": -9.016913649811242,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1349.2108292307767,
        "PAXG-USDT": -258.70970794838524,
        "SPY-USDT": 12.900012311601245
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 9288.737574260027,
        "extra_cost": 978.5738049272982,
        "samefills_cagr_pct": 13.428440039080304,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 37,
          "win_months_all": 0.5873015873015873,
          "win_months_active": 0.5873015873015873,
          "quarters_total": 21,
          "positive_quarters": 16,
          "win_quarters": 0.7619047619047619
        },
        "daily_close_drawdown_pct": -9.734164055361727,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04005641239528401
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.039925332140773984,
          "2021-12-31 00:00:00+00:00": 0.18503981001218817,
          "2022-12-31 00:00:00+00:00": 0.08892018626356468,
          "2023-12-31 00:00:00+00:00": 0.1537900999189803,
          "2024-12-31 00:00:00+00:00": 0.13896086696672305,
          "2025-12-31 00:00:00+00:00": 0.09379780412861427
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 8310.163769332728,
        "extra_cost": 1957.1476098545963,
        "samefills_cagr_pct": 12.301357088633846,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 36,
          "win_months_all": 0.5901639344262295,
          "win_months_active": 0.5901639344262295,
          "quarters_total": 19,
          "positive_quarters": 13,
          "win_quarters": 0.6842105263157895
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 36,
          "win_months_all": 0.5714285714285714,
          "win_months_active": 0.5714285714285714,
          "quarters_total": 21,
          "positive_quarters": 14,
          "win_quarters": 0.6666666666666666
        },
        "daily_close_drawdown_pct": -10.495714402342893,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04127185261052124
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03808575899302369,
          "2021-12-31 00:00:00+00:00": 0.1771139111145572,
          "2022-12-31 00:00:00+00:00": 0.08144029737387148,
          "2023-12-31 00:00:00+00:00": 0.13696849930882005,
          "2024-12-31 00:00:00+00:00": 0.12970772288095245,
          "2025-12-31 00:00:00+00:00": 0.07875649800664841
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 11071.711833302797,
        "mean_month_USDT": 181.50347267709503,
        "median_month_USDT": 100.96146950946422,
        "sum_positive_months": 14421.394842716363,
        "sum_negative_months": -3349.6830094135657,
        "worst_month": "2021-04",
        "worst_month_USDT": -445.47930970248126,
        "best3_share_positive_mtm": 0.28914186684103627,
        "class_counts": {
          "loss_base": 22,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 18,
          "zero_months": 0,
          "net_before_actual_fees": 13724.054406731108,
          "fee_total": 2652.3425734283137,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-11",
              "gross": 17.176187851565956,
              "fee": 55.61630460125674,
              "net": -38.44011674969079
            },
            {
              "month": "2024-07",
              "gross": 3.3618287716446247,
              "fee": 86.56097869107104,
              "net": -83.19914991942642
            },
            {
              "month": "2025-01",
              "gross": 39.22003773922478,
              "fee": 87.59192154295596,
              "net": -48.37188380373118
            },
            {
              "month": "2025-07",
              "gross": 105.98434373720455,
              "fee": 120.30027403465728,
              "net": -14.315930297452724
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 1,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 37,
            "extra_cost": 947.2652047958264,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 5.985234502499225,
                "extra": 10.854322426989034,
                "after": -4.869087924487758
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -3349.6830094135657,
            "already_negative_after_sum": -3701.898029332584
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 1894.5304095916529,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 5.985234502499225,
                "extra": 21.70864485397807,
                "after": -15.72341035147474
              },
              {
                "month": "2025-11",
                "base": 20.455592572368914,
                "extra": 20.737955647239254,
                "after": -0.28236307486804435
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -3349.6830094135657,
            "already_negative_after_sum": -4054.113049251604
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 10267.311379187311,
        "mean_month_USDT": 162.9731964950367,
        "median_month_USDT": 97.55541860999983,
        "sum_positive_months": 14421.394842716363,
        "sum_negative_months": -4154.083463529052,
        "worst_month": "2025-12",
        "worst_month_USDT": -613.1734981226764,
        "best3_share_positive_mtm": 0.28914186684103627,
        "class_counts": {
          "loss_base": 24,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 20,
          "zero_months": 0,
          "net_before_actual_fees": 13007.318032983745,
          "fee_total": 2740.006653796435,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-11",
              "gross": 17.176187851565956,
              "fee": 55.61630460125674,
              "net": -38.44011674969079
            },
            {
              "month": "2024-07",
              "gross": 3.3618287716446247,
              "fee": 86.56097869107104,
              "net": -83.19914991942642
            },
            {
              "month": "2025-01",
              "gross": 39.22003773922478,
              "fee": 87.59192154295596,
              "net": -48.37188380373118
            },
            {
              "month": "2025-07",
              "gross": 105.98434373720455,
              "fee": 120.30027403465728,
              "net": -14.315930297452724
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 1,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 37,
            "extra_cost": 978.5738049272983,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 5.985234502499225,
                "extra": 10.854322426989034,
                "after": -4.869087924487758
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -4154.083463529052,
            "already_negative_after_sum": -4537.6070835795435
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 1957.1476098545966,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 5.985234502499225,
                "extra": 21.70864485397807,
                "after": -15.72341035147474
              },
              {
                "month": "2025-11",
                "base": 20.455592572368914,
                "extra": 20.737955647239254,
                "after": -0.28236307486804435
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -4154.083463529052,
            "already_negative_after_sum": -4921.130703630035
          }
        }
      }
    }
  }
}
```

## [FBS0_B](http://localhost:9200/#/backtest/9bebb1e9-d0a0-4d74-a530-76c852c18d3a)

```json
{
  "audit": {
    "n": 273,
    "net": 10220.330399187804,
    "gross_before_fees": 12930.312405410494,
    "fees": 2709.9820062226904,
    "pf_from_trades": 1.6698689612998308,
    "PF_engine": 1.6698689612998312,
    "sharpe_engine": 1.3695392509158284,
    "cagr_engine": 14.459257700702688,
    "dd_engine": -8.28431149561536,
    "plus5_samefills": 9252.479682679692,
    "plus10_samefills": 8284.628966171595,
    "exbest": 8347.733455040121,
    "ex3best": 6222.452297120007,
    "ex3best_plus10_samefills": 4319.055784599188,
    "time_any_position_pct": 38.52225287557658,
    "entry_notional_time_initial_equity": 0.3884693270992093,
    "entry_turnover_initial_equity": 193.34835924826535,
    "two_side_turnover_initial_equity": 387.14028660324135,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4602.232165660134,
        "fees": 211.4551120203764,
        "plus10": 4451.192799931292,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.051563300741477636
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 2628.3906443401565,
        "fees": 1618.9250248114695,
        "plus10": 1472.0156266176784,
        "time_open_pct": 10.7327246452969,
        "entry_notional_time_initial_equity": 0.05632299369625736
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1459.224781294631,
        "fees": 631.7669633720666,
        "plus10": 1007.9626646002977,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17339267603849612
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1530.482807892881,
        "fees": 247.83490601877818,
        "plus10": 1353.4578750223254,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.10719035662297817
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 7230.622810000294,
        "fees": 1830.3801368318464
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1459.224781294631,
        "fees": 631.7669633720666
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1530.482807892881,
        "fees": 247.83490601877818
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 383.2169045617464,
        "by_symbol": {
          "BTC-USDT": 253.2851584627375,
          "PAXG-USDT": 0,
          "SPY-USDT": 129.93174609900888
        }
      },
      "2021": {
        "n": 53,
        "net": 1946.7065860564273,
        "by_symbol": {
          "BTC-USDT": 1853.3045829848445,
          "PAXG-USDT": -253.80864969066337,
          "SPY-USDT": 347.21065276224664
        }
      },
      "2022": {
        "n": 41,
        "net": 1057.9537053140284,
        "by_symbol": {
          "BTC-USDT": 1302.7262714128549,
          "PAXG-USDT": -123.71423833407204,
          "SPY-USDT": -121.0583277647541
        }
      },
      "2023": {
        "n": 55,
        "net": 2125.3866518356604,
        "by_symbol": {
          "BTC-USDT": 2298.2292739887625,
          "PAXG-USDT": -301.793224607608,
          "SPY-USDT": 128.95060245450506
        }
      },
      "2024": {
        "n": 56,
        "net": 1921.1906354608266,
        "by_symbol": {
          "BTC-USDT": 405.6685985796528,
          "PAXG-USDT": 1042.719863145358,
          "SPY-USDT": 472.80217373581604
        }
      },
      "2025": {
        "n": 56,
        "net": 2785.8759159591145,
        "by_symbol": {
          "BTC-USDT": 1117.4089245714388,
          "PAXG-USDT": 1095.8210307816164,
          "SPY-USDT": 572.6459606060589
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 124,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3798.01269158057,
        "fees": 180.2348049015375,
        "gross": 3978.2474964821076,
        "plus10": 3669.2735452223283,
        "exbest": 1925.415747432909,
        "ex3": 79.35069104386324,
        "ex3_plus10": -31.387575798447955,
        "year_net": {
          "2020": 475.1237882209012,
          "2021": 1528.7938021690584,
          "2022": -172.0385273566849,
          "2023": 1794.5907241088894,
          "2024": 593.4018062203402,
          "2025": -421.8589017819347
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 804.219474079563,
        "fees": 31.220307118838882,
        "gross": 835.439781198402,
        "plus10": 781.9192547089639,
        "exbest": 199.0054124483334,
        "ex3": -140.66804830419113,
        "ex3_plus10": -148.64497813091774,
        "year_net": {
          "2021": 339.67346075252453,
          "2025": 464.54601332703857
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 1715.5148409702133,
        "fees": 679.6317724605985,
        "gross": 2395.1466134308116,
        "plus10": 1230.0635749269288,
        "exbest": 1371.4659226722345,
        "ex3": 780.2764475058424,
        "ex3_plus10": 319.06757119300994,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 361.35422693574685,
          "2022": 758.6980852795828,
          "2023": 116.46354938179229,
          "2024": -130.74700562580563,
          "2025": 675.5813139908971
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 912.8758033699442,
        "fees": 939.2932523508704,
        "gross": 1852.1690557208146,
        "plus10": 241.95205169075103,
        "exbest": 728.9541215892291,
        "ex3": 376.65436580138527,
        "ex3_plus10": -253.63296941637884,
        "year_net": {
          "2020": -156.00330076616365,
          "2021": -376.5169068724855,
          "2022": 716.0667134899568,
          "2023": 387.17500049807995,
          "2024": -56.9862020148816,
          "2025": 399.1404990354382
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 38,
        "net": 1459.224781294631,
        "fees": 631.7669633720666,
        "gross": 2090.9917446666973,
        "plus10": 1007.9626646002977,
        "exbest": 452.2309806994832,
        "ex3": -1111.9749397720925,
        "ex3_plus10": -1530.20776950502,
        "year_net": {
          "2021": -253.80864969066337,
          "2022": -123.71423833407204,
          "2023": -301.793224607608,
          "2024": 1042.719863145358,
          "2025": 1095.8210307816164
        }
      },
      "SPY-USDT:long:LIMIT": {
        "n": 9,
        "net": 1439.072477763492,
        "fees": 167.37292556090708,
        "gross": 1606.4454033243992,
        "plus10": 1319.52038807713,
        "exbest": 685.6818649053521,
        "ex3": 49.137978898466486,
        "ex3_plus10": -26.118647103684225,
        "year_net": {
          "2020": 129.93174609900888,
          "2021": 347.21065276224664,
          "2022": -121.0583277647541,
          "2023": 267.0111793054313,
          "2024": 243.33126675550062,
          "2025": 572.6459606060589
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 3,
        "net": 91.41033012938914,
        "fees": 80.46198045787108,
        "gross": 171.87231058726022,
        "plus10": 33.937486945195516,
        "exbest": -31.231467394657315,
        "ex3": 0,
        "ex3_plus10": 0,
        "year_net": {
          "2023": -138.06057685092625,
          "2024": 229.4709069803154
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4813.6872776805085,
        "exbest": 2729.635221512472,
        "ex3best": 883.5701651234272,
        "ex3best_plus10": 750.531678910515,
        "years": {
          "2020": {
            "n": 3,
            "net": 475.12378822090125,
            "plus10": 466.90032690386886
          },
          "2021": {
            "n": 6,
            "net": 1868.467262921583,
            "plus10": 1853.5854064005575
          },
          "2022": {
            "n": 4,
            "net": -172.0385273566849,
            "plus10": -182.47148116066936
          },
          "2023": {
            "n": 4,
            "net": 1794.5907241088894,
            "plus10": 1768.3474524566784
          },
          "2024": {
            "n": 8,
            "net": 593.4018062203401,
            "plus10": 551.9262862532532
          },
          "2025": {
            "n": 6,
            "net": 42.687111545103875,
            "plus10": -7.095190922395972
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4247.315669151625,
        "exbest": 2284.341726042174,
        "ex3best": 1693.1522508757857,
        "ex3best_plus10": 561.0196228837516,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.83862975816362,
            "plus10": -243.1288870682934
          },
          "2021": {
            "n": 40,
            "net": -15.162679936738797,
            "plus10": -126.16689526935373
          },
          "2022": {
            "n": 33,
            "net": 1474.7647987695389,
            "plus10": 1331.212048365795
          },
          "2023": {
            "n": 40,
            "net": 503.6385498798722,
            "plus10": 190.74415837174453
          },
          "2024": {
            "n": 38,
            "net": -187.73320764068717,
            "plus10": -421.6155452319069
          },
          "2025": {
            "n": 33,
            "net": 1074.7218130263354,
            "plus10": 740.9707474496937
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2090.9917446666977,
        "exbest": 452.2309806994832,
        "ex3best": -1111.9749397720925,
        "ex3best_plus10": -1530.20776950502,
        "years": {
          "2021": {
            "n": 6,
            "net": -253.8086496906634,
            "plus10": -295.1740344801707
          },
          "2022": {
            "n": 3,
            "net": -123.71423833407205,
            "plus10": -147.67615055345857
          },
          "2023": {
            "n": 7,
            "net": -301.79322460760795,
            "plus10": -402.2749041709985
          },
          "2024": {
            "n": 7,
            "net": 1042.7198631453575,
            "plus10": 971.568634553771
          },
          "2025": {
            "n": 15,
            "net": 1095.8210307816166,
            "plus10": 881.5191192511545
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1778.3177139116597,
        "exbest": 777.0921950347413,
        "ex3best": 140.54830902785568,
        "ex3best_plus10": 7.818839841511192,
        "years": {
          "2020": {
            "n": 1,
            "net": 129.93174609900888,
            "plus10": 126.40167796866814
          },
          "2021": {
            "n": 1,
            "net": 347.21065276224664,
            "plus10": 337.2969240920964
          },
          "2022": {
            "n": 1,
            "net": -121.0583277647541,
            "plus10": -127.56964640291844
          },
          "2023": {
            "n": 4,
            "net": 128.95060245450503,
            "plus10": 63.32461146008171
          },
          "2024": {
            "n": 3,
            "net": 472.80217373581604,
            "plus10": 417.40817910640754
          },
          "2025": {
            "n": 2,
            "net": 572.6459606060589,
            "plus10": 536.5961287979902
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "FBS0_B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 39,
        "win_months_all": 0.639344262295082,
        "win_months_active": 0.639344262295082,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6190476190476191,
      "win_months_active": 0.6190476190476191,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.038903216858959255
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.039749549167352294
      ],
      "daily_close_drawdown_pct": -8.343086215990725,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.08463055975702238,
          "SPY-USDT": -0.04397192288864048
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.08463055975702238,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03195549403934381
        },
        "SPY-USDT": {
          "BTC-USDT": -0.04397192288864048,
          "PAXG-USDT": -0.03195549403934381,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04176490528852406,
        "2021-12-31 00:00:00+00:00": 0.18356103455062267,
        "2022-12-31 00:00:00+00:00": 0.08580375264445261,
        "2023-12-31 00:00:00+00:00": 0.15875456733958093,
        "2024-12-31 00:00:00+00:00": 0.12384180752119778,
        "2025-12-31 00:00:00+00:00": 0.1597914014825661
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.113622840011166,
        "SPY-USDT": -0.052037214423939486
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.113622840011166,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.0430761824309772
      },
      "SPY-USDT": {
        "BTC-USDT": -0.052037214423939486,
        "PAXG-USDT": -0.0430761824309772,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 30,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 14,
        "both_negative_and_portfolio_negative": 0
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.038903216858959255,
        "contributions": {
          "BTC-USDT": -0.029827136731105826,
          "PAXG-USDT": -0.009076080127853409,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.03189328803961111,
        "contributions": {
          "BTC-USDT": -0.03189328803961122,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.019707919864592083,
        "contributions": {
          "BTC-USDT": -0.01970791986459207,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-06-30 00:00:00+00:00",
        "portfolio_return": -0.01937799465890855,
        "contributions": {
          "BTC-USDT": -0.0193779946589086,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01688110440940216,
        "contributions": {
          "BTC-USDT": -0.015339496643852845,
          "PAXG-USDT": -0.009240369387105306,
          "SPY-USDT": 0.007698761621555879
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.015329397572250603,
        "contributions": {
          "BTC-USDT": -0.015329397572250643,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010567747849522191,
        "contributions": {
          "BTC-USDT": -0.001031239847930677,
          "PAXG-USDT": -0.0095365080015916,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.010384056454503687,
        "contributions": {
          "BTC-USDT": -0.010384056454503713,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.007436096075667642,
        "contributions": {
          "BTC-USDT": -0.00743609607566768,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006478170284907714,
        "contributions": {
          "BTC-USDT": 0.002949682183903992,
          "PAXG-USDT": -0.009427852468811705,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -8.343086215990725,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -770.2017664138884,
        "PAXG-USDT": -206.774493962492,
        "SPY-USDT": 0
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 9252.4796826797,
        "extra_cost": 967.8507165081036,
        "samefills_cagr_pct": 13.387513509761039,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 37,
          "win_months_all": 0.5873015873015873,
          "win_months_active": 0.5873015873015873,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -8.84468451811653,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.040112774504266424
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.039925332140773984,
          "2021-12-31 00:00:00+00:00": 0.175547765474368,
          "2022-12-31 00:00:00+00:00": 0.07899701724985553,
          "2023-12-31 00:00:00+00:00": 0.1419777753323921,
          "2024-12-31 00:00:00+00:00": 0.11420062467748404,
          "2025-12-31 00:00:00+00:00": 0.1471043909814751
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 8284.628966171595,
        "extra_cost": 1935.7014330162071,
        "samefills_cagr_pct": 12.271301568566662,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 36,
          "win_months_all": 0.5901639344262295,
          "win_months_active": 0.5901639344262295,
          "quarters_total": 19,
          "positive_quarters": 13,
          "win_quarters": 0.6842105263157895
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 36,
          "win_months_all": 0.5714285714285714,
          "win_months_active": 0.5714285714285714,
          "quarters_total": 21,
          "positive_quarters": 14,
          "win_quarters": 0.6666666666666666
        },
        "daily_close_drawdown_pct": -9.565973965837982,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.041329866603298626
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03808575899302369,
          "2021-12-31 00:00:00+00:00": 0.1675060960574084,
          "2022-12-31 00:00:00+00:00": 0.07207222322869034,
          "2023-12-31 00:00:00+00:00": 0.12469138933323687,
          "2024-12-31 00:00:00+00:00": 0.10396572254707581,
          "2025-12-31 00:00:00+00:00": 0.13339360760594032
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 11023.748025464709,
        "mean_month_USDT": 180.7171807453231,
        "median_month_USDT": 77.32605740253894,
        "sum_positive_months": 14023.342876438583,
        "sum_negative_months": -2999.5948509738737,
        "worst_month": "2021-04",
        "worst_month_USDT": -440.9809766761682,
        "best3_share_positive_mtm": 0.2635380388942463,
        "class_counts": {
          "loss_base": 22,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 17,
          "zero_months": 0,
          "net_before_actual_fees": 13646.206179420062,
          "fee_total": 2622.458153955353,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-08",
              "gross": 1.1818525125504777,
              "fee": 49.15220054324121,
              "net": -47.97034803069073
            },
            {
              "month": "2023-11",
              "gross": 17.00143220714581,
              "fee": 54.06864989895094,
              "net": -37.067217691805126
            },
            {
              "month": "2024-07",
              "gross": 1.816588483901569,
              "fee": 84.23299144066527,
              "net": -82.4164029567637
            },
            {
              "month": "2025-07",
              "gross": 107.55367133038001,
              "fee": 121.09239249283112,
              "net": -13.538721162451111
            },
            {
              "month": "2025-09",
              "gross": 77.4618831517281,
              "fee": 97.13202480455845,
              "net": -19.670141652830353
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 0,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 37,
            "extra_cost": 936.5921978411973,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 5.983222657960141,
                "extra": 10.567103691974314,
                "after": -4.583881034017395
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -2999.5948509738737,
            "already_negative_after_sum": -3338.90579949154
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 1873.1843956823946,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 5.983222657960141,
                "extra": 21.134207383948628,
                "after": -15.150984725991293
              },
              {
                "month": "2025-11",
                "base": 20.406801390130568,
                "extra": 20.69070314289509,
                "after": -0.2839017527658143
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -2999.5948509738737,
            "already_negative_after_sum": -3678.2167480092176
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 10220.330399187795,
        "mean_month_USDT": 162.2274666537745,
        "median_month_USDT": 62.0017508358269,
        "sum_positive_months": 14023.342876438583,
        "sum_negative_months": -3803.012477250788,
        "worst_month": "2025-12",
        "worst_month_USDT": -612.1906702841043,
        "best3_share_positive_mtm": 0.2635380388942463,
        "class_counts": {
          "loss_base": 24,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 19,
          "zero_months": 0,
          "net_before_actual_fees": 12930.312405410485,
          "fee_total": 2709.982006222691,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-08",
              "gross": 1.1818525125504777,
              "fee": 49.15220054324121,
              "net": -47.97034803069073
            },
            {
              "month": "2023-11",
              "gross": 17.00143220714581,
              "fee": 54.06864989895094,
              "net": -37.067217691805126
            },
            {
              "month": "2024-07",
              "gross": 1.816588483901569,
              "fee": 84.23299144066527,
              "net": -82.4164029567637
            },
            {
              "month": "2025-07",
              "gross": 107.55367133038001,
              "fee": 121.09239249283112,
              "net": -13.538721162451111
            },
            {
              "month": "2025-09",
              "gross": 77.4618831517281,
              "fee": 97.13202480455845,
              "net": -19.670141652830353
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 0,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 37,
            "extra_cost": 967.8507165081037,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 5.983222657960141,
                "extra": 10.567103691974314,
                "after": -4.583881034017395
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -3803.012477250788,
            "already_negative_after_sum": -4173.581944435367
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 1935.7014330162074,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 5.983222657960141,
                "extra": 21.134207383948628,
                "after": -15.150984725991293
              },
              {
                "month": "2025-11",
                "base": 20.406801390130568,
                "extra": 20.69070314289509,
                "after": -0.2839017527658143
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -3803.012477250788,
            "already_negative_after_sum": -4544.151411619945
          }
        }
      }
    }
  }
}
```

## [FBS1_B](http://localhost:9200/#/backtest/931bc4d2-d12d-4e93-a2d0-7bc2f23daa44)

```json
{
  "audit": {
    "n": 273,
    "net": 11175.99409000308,
    "gross_before_fees": 13931.116977614542,
    "fees": 2755.1228876114615,
    "pf_from_trades": 1.7279970221951493,
    "PF_engine": 1.727997022195149,
    "sharpe_engine": 1.4598317973543367,
    "cagr_engine": 15.477568249101626,
    "dd_engine": -9.027061799521373,
    "plus5_samefills": 10192.02163014184,
    "plus10_samefills": 9208.049170280603,
    "exbest": 9271.055229721609,
    "ex3best": 7057.78850457624,
    "ex3best_plus10_samefills": 5123.3076842160135,
    "time_any_position_pct": 38.61647544812285,
    "entry_notional_time_initial_equity": 0.40106491311669107,
    "entry_turnover_initial_equity": 196.6024217982098,
    "two_side_turnover_initial_equity": 393.58898394449443,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4648.597506789265,
        "fees": 218.04771073226507,
        "plus10": 4492.849141980506,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.053000055782165226
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 3417.11720791034,
        "fees": 1627.7395405238553,
        "plus10": 2254.4461075361583,
        "time_open_pct": 10.848623518421206,
        "entry_notional_time_initial_equity": 0.058299275979274895
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1539.5799085564677,
        "fees": 654.1083814720198,
        "plus10": 1072.3596360764536,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.1794898633909839
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1570.6994667470049,
        "fees": 255.22725488332128,
        "plus10": 1388.39428468749,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.11027571796426708
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 8065.714714699603,
        "fees": 1845.7872512561205
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1539.5799085564677,
        "fees": 654.1083814720198
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1570.6994667470049,
        "fees": 255.22725488332128
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 383.2169045617464,
        "by_symbol": {
          "BTC-USDT": 253.2851584627375,
          "PAXG-USDT": 0,
          "SPY-USDT": 129.93174609900888
        }
      },
      "2021": {
        "n": 51,
        "net": 2040.7714229729932,
        "by_symbol": {
          "BTC-USDT": 1947.9196886454872,
          "PAXG-USDT": -256.9874808246687,
          "SPY-USDT": 349.8392151521746
        }
      },
      "2022": {
        "n": 45,
        "net": 1195.595476510964,
        "by_symbol": {
          "BTC-USDT": 1443.5549866338529,
          "PAXG-USDT": -124.24827430859554,
          "SPY-USDT": -123.711235814293
        }
      },
      "2023": {
        "n": 54,
        "net": 2305.913075318427,
        "by_symbol": {
          "BTC-USDT": 2486.9899040003697,
          "PAXG-USDT": -312.18230883990077,
          "SPY-USDT": 131.10548015795786
        }
      },
      "2024": {
        "n": 55,
        "net": 2352.9710610793263,
        "by_symbol": {
          "BTC-USDT": 780.2312344278248,
          "PAXG-USDT": 1083.9792522368318,
          "SPY-USDT": 488.76057441467003
        }
      },
      "2025": {
        "n": 56,
        "net": 2897.526149559621,
        "by_symbol": {
          "BTC-USDT": 1153.7337425293315,
          "PAXG-USDT": 1149.018720292801,
          "SPY-USDT": 594.7736867374866
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 124,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3823.3076429401035,
        "fees": 185.7919597678956,
        "gross": 4009.099602707998,
        "plus10": 3690.5991002487485,
        "exbest": 1918.3687826586304,
        "ex3": 33.06557338099017,
        "ex3_plus10": -81.28139627445938,
        "year_net": {
          "2020": 475.1237882209012,
          "2021": 1529.404229734846,
          "2022": -179.88897003879882,
          "2023": 1825.1718538858458,
          "2024": 614.961404654727,
          "2025": -441.46466351741856
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 825.2898638491622,
        "fees": 32.25575096436947,
        "gross": 857.5456148135315,
        "plus10": 802.2500417317553,
        "exbest": 197.38027490676,
        "ex3": -147.61461859081663,
        "ex3_plus10": -155.98547087812233,
        "year_net": {
          "2021": 344.99489349757664,
          "2025": 480.2949703515855
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 2445.350079760425,
        "fees": 668.0152756372214,
        "gross": 3113.365355397646,
        "plus10": 1968.1963114481239,
        "exbest": 2086.122532714004,
        "ex3": 1465.3760192245397,
        "ex3_plus10": 1013.640434253626,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 566.9613520726689,
          "2022": 915.0494819261454,
          "2023": 261.15749820331484,
          "2024": 72.93145871684581,
          "2025": 695.0856178334502
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 971.7671281499136,
        "fees": 959.7242648866336,
        "gross": 1931.4913930365476,
        "plus10": 286.24979608803267,
        "exbest": 779.3192756906152,
        "ex3": 416.34338906475205,
        "ex3_plus10": -227.02115647517573,
        "year_net": {
          "2020": -156.00330076616365,
          "2021": -493.4407866596046,
          "2022": 708.394474746506,
          "2023": 400.6605519112094,
          "2024": 92.33837105625202,
          "2025": 419.81781786171456
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 38,
        "net": 1539.5799085564677,
        "fees": 654.1083814720198,
        "gross": 2193.6882900284886,
        "plus10": 1072.3596360764536,
        "exbest": 483.83869362467146,
        "ex3": -1145.1017868513545,
        "ex3_plus10": -1577.7893083579827,
        "year_net": {
          "2021": -256.9874808246687,
          "2022": -124.24827430859554,
          "2023": -312.18230883990077,
          "2024": 1083.9792522368318,
          "2025": 1149.018720292801
        }
      },
      "SPY-USDT:long:LIMIT": {
        "n": 9,
        "net": 1475.8112647399325,
        "fees": 172.41982679441406,
        "gross": 1648.2310915343464,
        "plus10": 1352.6542456010654,
        "exbest": 693.3133369421461,
        "ex3": 46.32918327409271,
        "ex3_plus10": -31.308735890459474,
        "year_net": {
          "2020": 129.93174609900888,
          "2021": 349.8392151521746,
          "2022": -123.711235814293,
          "2023": 272.8326741026538,
          "2024": 252.14517846290158,
          "2025": 594.7736867374866
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 3,
        "net": 94.8882020070725,
        "fees": 82.80742808890719,
        "gross": 177.69563009597968,
        "plus10": 35.7400390864245,
        "exbest": -30.99913558165713,
        "ex3": 0,
        "ex3_plus10": 0,
        "year_net": {
          "2023": -141.72719394469595,
          "2024": 236.61539595176845
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4866.645217521531,
        "exbest": 2743.6586465077926,
        "ex3best": 858.3554372301517,
        "ex3best_plus10": 720.9686454572964,
        "years": {
          "2020": {
            "n": 3,
            "net": 475.12378822090125,
            "plus10": 466.90032690386886
          },
          "2021": {
            "n": 6,
            "net": 1874.3991232324227,
            "plus10": 1859.4255980031462
          },
          "2022": {
            "n": 4,
            "net": -179.88897003879882,
            "plus10": -190.677535549637
          },
          "2023": {
            "n": 4,
            "net": 1825.1718538858458,
            "plus10": 1798.2012568409714
          },
          "2024": {
            "n": 8,
            "net": 614.9614046547271,
            "plus10": 572.0930507046345
          },
          "2025": {
            "n": 6,
            "net": 38.830306834166976,
            "plus10": -13.093554922479768
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 5044.856748434205,
        "exbest": 3057.8896608639093,
        "ex3best": 2437.1431473744447,
        "ex3best_plus10": 1299.8902303416646,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.83862975816362,
            "plus10": -243.1288870682934
          },
          "2021": {
            "n": 38,
            "net": 73.52056541306413,
            "plus10": -34.88042316613236
          },
          "2022": {
            "n": 37,
            "net": 1623.4439566726508,
            "plus10": 1463.9356299271121
          },
          "2023": {
            "n": 39,
            "net": 661.8180501145239,
            "plus10": 352.221205063055
          },
          "2024": {
            "n": 37,
            "net": 165.26982977309757,
            "plus10": -66.03309981950608
          },
          "2025": {
            "n": 33,
            "net": 1114.9034356951654,
            "plus10": 782.3316825999224
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2193.6882900284895,
        "exbest": 483.83869362467146,
        "ex3best": -1145.1017868513545,
        "ex3best_plus10": -1577.7893083579827,
        "years": {
          "2021": {
            "n": 6,
            "net": -256.9874808246687,
            "plus10": -298.7185485486632
          },
          "2022": {
            "n": 3,
            "net": -124.24827430859553,
            "plus10": -148.5583940552639
          },
          "2023": {
            "n": 7,
            "net": -312.18230883990077,
            "plus10": -415.25412745851384
          },
          "2024": {
            "n": 7,
            "net": 1083.9792522368316,
            "plus10": 1010.1179896268865
          },
          "2025": {
            "n": 15,
            "net": 1149.0187202928012,
            "plus10": 924.7727165120082
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1825.926721630326,
        "exbest": 788.2015389492186,
        "ex3best": 141.21738528116526,
        "ex3best_plus10": 4.431303195964887,
        "years": {
          "2020": {
            "n": 1,
            "net": 129.93174609900888,
            "plus10": 126.40167796866814
          },
          "2021": {
            "n": 1,
            "net": 349.8392151521746,
            "plus10": 339.85043448082854
          },
          "2022": {
            "n": 1,
            "net": -123.711235814293,
            "plus10": -130.36524541760818
          },
          "2023": {
            "n": 4,
            "net": 131.10548015795786,
            "plus10": 63.60163091911164
          },
          "2024": {
            "n": 3,
            "net": 488.76057441467003,
            "plus10": 431.574389152179
          },
          "2025": {
            "n": 2,
            "net": 594.7736867374866,
            "plus10": 557.3313975843107
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "FBS1_B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 40,
        "win_months_all": 0.6557377049180327,
        "win_months_active": 0.6557377049180327,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6349206349206349,
      "win_months_active": 0.6349206349206349,
      "win_quarters": 0.8095238095238095,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.03885764849740381
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.03999728792536594
      ],
      "daily_close_drawdown_pct": -9.017332365408425,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.08401855312796588,
          "SPY-USDT": -0.04112976501358775
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.08401855312796588,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03199964366934717
        },
        "SPY-USDT": {
          "BTC-USDT": -0.04112976501358775,
          "PAXG-USDT": -0.03199964366934717,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04176490528852406,
        "2021-12-31 00:00:00+00:00": 0.19259040734279953,
        "2022-12-31 00:00:00+00:00": 0.09623282355000429,
        "2023-12-31 00:00:00+00:00": 0.1693086300209452,
        "2024-12-31 00:00:00+00:00": 0.14774867490183285,
        "2025-12-31 00:00:00+00:00": 0.1585212808316645
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.11248229850790313,
        "SPY-USDT": -0.048955071885522075
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.11248229850790313,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.043106958714031605
      },
      "SPY-USDT": {
        "BTC-USDT": -0.048955071885522075,
        "PAXG-USDT": -0.043106958714031605,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 29,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 1,
        "both_nonzero": 14,
        "both_negative_and_portfolio_negative": 1
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.03885764849740381,
        "contributions": {
          "BTC-USDT": -0.029781671365891712,
          "PAXG-USDT": -0.009075977131512094,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.032012810965683425,
        "contributions": {
          "BTC-USDT": -0.032012810965683404,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.02467009627793404,
        "contributions": {
          "BTC-USDT": -0.024670096277934015,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01690167587261171,
        "contributions": {
          "BTC-USDT": -0.015359896586737217,
          "PAXG-USDT": -0.00924025233962969,
          "SPY-USDT": 0.007698473053755171
        }
      },
      {
        "month": "2023-10-31 00:00:00+00:00",
        "portfolio_return": -0.015674854277929806,
        "contributions": {
          "BTC-USDT": -0.0063259872244927655,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009348867053437125
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.014755540704759929,
        "contributions": {
          "BTC-USDT": -0.014755540704759824,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.01343096143016742,
        "contributions": {
          "BTC-USDT": -0.013430961430167478,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010767654679165406,
        "contributions": {
          "BTC-USDT": -0.0012314259811742358,
          "PAXG-USDT": -0.009536228697991164,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.01022675846378751,
        "contributions": {
          "BTC-USDT": -0.010226758463787455,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009224390640754199,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.00922439064075427,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-08-20 00:00:00+00:00",
      "drawdown_pct": -9.017332365408425,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1347.9189652592777,
        "PAXG-USDT": -258.44898083059076,
        "SPY-USDT": 12.881607279944092
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 10192.021630141842,
        "extra_cost": 983.9724598612362,
        "samefills_cagr_pct": 14.428504977698097,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6229508196721312,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 38,
          "win_months_all": 0.6031746031746031,
          "win_months_active": 0.6031746031746031,
          "quarters_total": 21,
          "positive_quarters": 16,
          "win_quarters": 0.7619047619047619
        },
        "daily_close_drawdown_pct": -9.734852628209367,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.040066020567982696
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.039925332140773984,
          "2021-12-31 00:00:00+00:00": 0.18469267670328682,
          "2022-12-31 00:00:00+00:00": 0.0888776089531873,
          "2023-12-31 00:00:00+00:00": 0.15298987951540832,
          "2024-12-31 00:00:00+00:00": 0.13902698076846032,
          "2025-12-31 00:00:00+00:00": 0.14612864589103025
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 9208.049170280605,
        "extra_cost": 1967.9449197224724,
        "samefills_cagr_pct": 13.337277013535509,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 13,
          "win_quarters": 0.6842105263157895
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 37,
          "win_months_all": 0.5873015873015873,
          "win_months_active": 0.5873015873015873,
          "quarters_total": 21,
          "positive_quarters": 14,
          "win_quarters": 0.6666666666666666
        },
        "daily_close_drawdown_pct": -10.496713464573393,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.041281783473073985
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03808575899302369,
          "2021-12-31 00:00:00+00:00": 0.17676695521025,
          "2022-12-31 00:00:00+00:00": 0.08139707350444314,
          "2023-12-31 00:00:00+00:00": 0.13616539172405506,
          "2024-12-31 00:00:00+00:00": 0.12977268448892398,
          "2025-12-31 00:00:00+00:00": 0.13277001550276846
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2023-03-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 12008.00469058695,
        "mean_month_USDT": 196.85253591126147,
        "median_month_USDT": 102.93083816352555,
        "sum_positive_months": 15324.807914496625,
        "sum_negative_months": -3316.8032239096756,
        "worst_month": "2021-04",
        "worst_month_USDT": -445.44635345892857,
        "best3_share_positive_mtm": 0.2721112120295782,
        "class_counts": {
          "loss_base": 21,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 37
        },
        "positive_months": 40,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 18,
          "zero_months": 0,
          "net_before_actual_fees": 14671.992275407916,
          "fee_total": 2663.9875848209654,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-11",
              "gross": 17.0110297955071,
              "fee": 55.513723211895964,
              "net": -38.502693416388865
            },
            {
              "month": "2024-07",
              "gross": 4.230048312622515,
              "fee": 86.4285887496887,
              "net": -82.19854043706619
            },
            {
              "month": "2025-07",
              "gross": 112.67349219142292,
              "fee": 125.724213539126,
              "net": -13.050721347703075
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 1,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 38,
            "extra_cost": 951.4241374360593,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 6.026963485719534,
                "extra": 10.852400563930699,
                "after": -4.825437078208779
              }
            ],
            "already_negative_months": 21,
            "already_negative_base_sum": -3316.8032239096756,
            "already_negative_after_sum": -3640.308796109679
          },
          "10": {
            "positive_months": 37,
            "extra_cost": 1902.8482748721185,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 6.026963485719534,
                "extra": 21.704801127861398,
                "after": -15.677837642138911
              },
              {
                "month": "2025-11",
                "base": 21.370220631037228,
                "extra": 21.668223186546097,
                "after": -0.29800255550799193
              }
            ],
            "already_negative_months": 21,
            "already_negative_base_sum": -3316.8032239096756,
            "already_negative_after_sum": -3963.8143683097023
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 11175.994090003074,
        "mean_month_USDT": 177.3967315873504,
        "median_month_USDT": 100.38906402175598,
        "sum_positive_months": 15324.807914496625,
        "sum_negative_months": -4148.813824493551,
        "worst_month": "2025-12",
        "worst_month_USDT": -640.7836445910652,
        "best3_share_positive_mtm": 0.2721112120295782,
        "class_counts": {
          "loss_base": 23,
          "zero_base": 0,
          "positive_within_cost5": 2,
          "positive_between_cost5_cost10": 1,
          "positive_above_cost10": 37
        },
        "positive_months": 40,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 20,
          "zero_months": 0,
          "net_before_actual_fees": 13931.116977614536,
          "fee_total": 2755.1228876114615,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-11",
              "gross": 17.0110297955071,
              "fee": 55.513723211895964,
              "net": -38.502693416388865
            },
            {
              "month": "2024-07",
              "gross": 4.230048312622515,
              "fee": 86.4285887496887,
              "net": -82.19854043706619
            },
            {
              "month": "2025-07",
              "gross": 112.67349219142292,
              "fee": 125.724213539126,
              "net": -13.050721347703075
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 1,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 38,
            "extra_cost": 983.9724598612363,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 7.5512853297571345,
                "after": -3.7371985477020644
              },
              {
                "month": "2023-03",
                "base": 6.026963485719534,
                "extra": 10.852400563930699,
                "after": -4.825437078208779
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -4148.813824493551,
            "already_negative_after_sum": -4504.867719118731
          },
          "10": {
            "positive_months": 37,
            "extra_cost": 1967.9449197224726,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 3.814086782054801,
                "extra": 15.102570659514269,
                "after": -11.288483877460749
              },
              {
                "month": "2023-03",
                "base": 6.026963485719534,
                "extra": 21.704801127861398,
                "after": -15.677837642138911
              },
              {
                "month": "2025-11",
                "base": 21.370220631037228,
                "extra": 21.668223186546097,
                "after": -0.29800255550799193
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -4148.813824493551,
            "already_negative_after_sum": -4860.921613743929
          }
        }
      }
    }
  }
}
```

## Comparaciones por mes
```json
{
  "X03S_B__N204S_B": {
    "delta": 923.1638021737999,
    "months_improve": 37,
    "rescued_negative_to_positive": [
      "2022-06",
      "2023-08",
      "2025-09"
    ],
    "lost_positive_to_nonpositive": [
      "2022-08",
      "2025-04"
    ]
  }
}
```