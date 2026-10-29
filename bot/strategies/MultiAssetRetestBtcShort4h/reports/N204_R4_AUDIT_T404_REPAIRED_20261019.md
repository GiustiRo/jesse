# N204 R4 — T404_REPAIRED

2026 cerrado; muestra de desarrollo2020-10-15→2025-12-31 exclusiva. Auditoría de fills, cantidades, fees,PNL,wallet yterminal, con MTM UTC diario. Costes+5/+10 adicionales al fee de CADA sesión, sobre recorridos y cantidades fijos; no confundir overlays de sesiones ya estresadas con el estrés original. Monthclassallcalendar, denominadores activos se conservan en auditoría.

## [T404B](http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333)

```json
{
  "audit": {
    "n": 273,
    "net": 11712.874448452887,
    "gross_before_fees": 13566.39921133937,
    "fees": 1853.5247628864834,
    "pf_from_trades": 1.7582991110362833,
    "PF_engine": 1.7582991110362833,
    "sharpe_engine": 1.5045324378771978,
    "cagr_engine": 16.033447565475466,
    "dd_engine": -8.785751847777611,
    "plus5_samefills": 10683.138469071506,
    "plus10_samefills": 9653.402489690132,
    "exbest": 9718.062111866915,
    "ex3best": 7358.098638815357,
    "ex3best_plus10_samefills": 5334.081931720664,
    "time_any_position_pct": 38.61647544812285,
    "entry_notional_time_initial_equity": 0.4232755515492156,
    "entry_turnover_initial_equity": 205.6950632921692,
    "two_side_turnover_initial_equity": 411.89439175255194,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4892.99418029878,
        "fees": 145.22239110213042,
        "plus10": 4731.6359679630805,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05493370555443233
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 3174.7796767555838,
        "fees": 1087.0940878467218,
        "plus10": 1966.8973569258922,
        "time_open_pct": 10.848623518421206,
        "entry_notional_time_initial_equity": 0.060484226706692575
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1867.9995399043892,
        "fees": 445.556588424448,
        "plus10": 1372.9366638772249,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.19008067853211513
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1777.1010514941372,
        "fees": 175.65169551318326,
        "plus10": 1581.9325009239333,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.1177769407559758
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 8067.773857054359,
        "fees": 1232.3164789488521
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1867.9995399043892,
        "fees": 445.556588424448
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1777.1010514941372,
        "fees": 175.65169551318326
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 407.0477243761954,
        "by_symbol": {
          "BTC-USDT": 272.9982611721363,
          "PAXG-USDT": 0,
          "SPY-USDT": 134.04946320405904
        }
      },
      "2021": {
        "n": 51,
        "net": 2196.4646864614083,
        "by_symbol": {
          "BTC-USDT": 2063.156639860288,
          "PAXG-USDT": -243.7483810199544,
          "SPY-USDT": 377.0564276210745
        }
      },
      "2022": {
        "n": 45,
        "net": 1080.257714510848,
        "by_symbol": {
          "BTC-USDT": 1320.4972462864891,
          "PAXG-USDT": -114.96543294814454,
          "SPY-USDT": -125.27409882749666
        }
      },
      "2023": {
        "n": 54,
        "net": 2424.614845833404,
        "by_symbol": {
          "BTC-USDT": 2522.049195403553,
          "PAXG-USDT": -274.2684207108132,
          "SPY-USDT": 176.8340711406637
        }
      },
      "2024": {
        "n": 55,
        "net": 2590.0058882378835,
        "by_symbol": {
          "BTC-USDT": 862.4303009016795,
          "PAXG-USDT": 1170.1005978399255,
          "SPY-USDT": 557.4749894962786
        }
      },
      "2025": {
        "n": 56,
        "net": 3014.4835890331533,
        "by_symbol": {
          "BTC-USDT": 1026.6422134302181,
          "PAXG-USDT": 1330.8811767433765,
          "SPY-USDT": 656.9601988595581
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
        "net": 4023.9924172803344,
        "fees": 123.63881114178994,
        "gross": 4147.631228422125,
        "plus10": 3886.615960456124,
        "exbest": 2029.1800806943475,
        "ex3": 76.97158970247051,
        "ex3_plus10": -40.86565329172811,
        "year_net": {
          "2020": 486.09589306358646,
          "2021": 1565.031681740259,
          "2022": -178.8194658655705,
          "2023": 1922.7118718694255,
          "2024": 678.6395759295743,
          "2025": -449.6671394569405
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 869.0017630184457,
        "fees": 21.583579960340455,
        "gross": 890.585342978786,
        "plus10": 845.0200075069563,
        "exbest": 206.34806803940987,
        "ex3": -150.17880150350217,
        "ex3_plus10": -158.94357625138696,
        "year_net": {
          "2021": 356.52686954291204,
          "2025": 512.4748934755336
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 1779.9749703735902,
        "fees": 446.4799568697406,
        "gross": 2226.454927243332,
        "plus10": 1283.8861294072121,
        "exbest": 1498.0862422866396,
        "ex3": 1002.5950701729612,
        "ex3_plus10": 533.4211513415241,
        "year_net": {
          "2020": -65.09905435199995,
          "2021": 602.5525272720902,
          "2022": 743.0282997597802,
          "2023": 77.03619863307341,
          "2024": 21.102239982463715,
          "2025": 401.3547590781825
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 1394.8047063819924,
        "fees": 640.614130976981,
        "gross": 2035.4188373589736,
        "plus10": 683.0112275186799,
        "exbest": 1179.2648230775214,
        "ex3": 782.7872618206002,
        "ex3_plus10": 115.78764051422948,
        "year_net": {
          "2020": -147.9985775394502,
          "2021": -460.95443869497365,
          "2022": 756.2884123922796,
          "2023": 522.3011249010532,
          "2024": 162.68848498964107,
          "2025": 562.4797003334425
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 38,
        "net": 1867.9995399043892,
        "fees": 445.556588424448,
        "gross": 2313.5561283288375,
        "plus10": 1372.9366638772249,
        "exbest": 727.0937945759138,
        "ex3": -977.3546296716513,
        "ex3_plus10": -1435.9259083952413,
        "year_net": {
          "2021": -243.7483810199544,
          "2022": -114.96543294814454,
          "2023": -274.2684207108132,
          "2024": 1170.1005978399255,
          "2025": 1330.8811767433765
        }
      },
      "SPY-USDT:long:LIMIT": {
        "n": 9,
        "net": 1642.3466658241753,
        "fees": 118.0879757631843,
        "gross": 1760.4346415873597,
        "plus10": 1511.1378038650814,
        "exbest": 793.8339949643719,
        "ex3": 91.63685554809854,
        "ex3_plus10": 9.010443638265258,
        "year_net": {
          "2020": 134.04946320405904,
          "2021": 377.0564276210745,
          "2022": -125.27409882749666,
          "2023": 318.75300854411137,
          "2024": 280.80166642286906,
          "2025": 656.9601988595581
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 3,
        "net": 134.75438566996183,
        "fees": 57.56371974999898,
        "gross": 192.3181054199608,
        "plus10": 70.79469705885184,
        "exbest": -15.662745604320534,
        "ex3": 0,
        "ex3_plus10": 0,
        "year_net": {
          "2023": -141.91893740344767,
          "2024": 276.6733230734095
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 5038.216571400908,
        "exbest": 2898.18184371279,
        "ex3best": 945.973352720917,
        "ex3best_plus10": 804.1543542152278,
        "years": {
          "2020": {
            "n": 3,
            "net": 486.09589306358635,
            "plus10": 477.75755686576565
          },
          "2021": {
            "n": 6,
            "net": 1921.5585512831713,
            "plus10": 1906.3377821114022
          },
          "2022": {
            "n": 4,
            "net": -178.8194658655705,
            "plus10": -189.87556737831844
          },
          "2023": {
            "n": 4,
            "net": 1922.7118718694255,
            "plus10": 1894.7933575020256
          },
          "2024": {
            "n": 8,
            "net": 678.6395759295744,
            "plus10": 634.2044027136623
          },
          "2025": {
            "n": 6,
            "net": 62.80775401859307,
            "plus10": 8.418436148542241
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4261.873764602303,
        "exbest": 2892.890948668624,
        "ex3best": 2397.3997765549448,
        "ex3best_plus10": 1216.43237886021,
        "years": {
          "2020": {
            "n": 8,
            "net": -213.09763189145013,
            "plus10": -234.75744853776132
          },
          "2021": {
            "n": 38,
            "net": 141.5980885771166,
            "plus10": 30.824019791428967
          },
          "2022": {
            "n": 37,
            "net": 1499.3167121520592,
            "plus10": 1333.9473342839308
          },
          "2023": {
            "n": 39,
            "net": 599.3373235341271,
            "plus10": 277.83708114304324
          },
          "2024": {
            "n": 37,
            "net": 183.79072497210487,
            "plus10": -56.500565210274914
          },
          "2025": {
            "n": 33,
            "net": 963.8344594116245,
            "plus10": 615.5469354555253
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2313.5561283288366,
        "exbest": 727.0937945759138,
        "ex3best": -977.3546296716513,
        "ex3best_plus10": -1435.9259083952413,
        "years": {
          "2021": {
            "n": 6,
            "net": -243.74838101995437,
            "plus10": -287.2628901915716
          },
          "2022": {
            "n": 3,
            "net": -114.96543294814455,
            "plus10": -140.53373866924497
          },
          "2023": {
            "n": 7,
            "net": -274.2684207108133,
            "plus10": -383.63281417751784
          },
          "2024": {
            "n": 7,
            "net": 1170.1005978399257,
            "plus10": 1092.1977475583785
          },
          "2025": {
            "n": 15,
            "net": 1330.8811767433763,
            "plus10": 1092.168359357181
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1952.752747007321,
        "exbest": 928.5883806343338,
        "ex3best": 226.3912412180605,
        "ex3best_plus10": 79.80514069711711,
        "years": {
          "2020": {
            "n": 1,
            "net": 134.04946320405904,
            "plus10": 130.45633254926236
          },
          "2021": {
            "n": 1,
            "net": 377.0564276210745,
            "plus10": 366.44206106171225
          },
          "2022": {
            "n": 1,
            "net": -125.27409882749666,
            "plus10": -132.19838658207246
          },
          "2023": {
            "n": 4,
            "net": 176.83407114066367,
            "plus10": 104.65355997676954
          },
          "2024": {
            "n": 3,
            "net": 557.4749894962786,
            "plus10": 495.7195526838649
          },
          "2025": {
            "n": 2,
            "net": 656.9601988595581,
            "plus10": 616.859381234397
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "T404B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 40,
        "win_months_all": 0.6557377049180327,
        "win_months_active": 0.6557377049180327,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6349206349206349,
      "win_months_active": 0.6349206349206349,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.03835710777436052
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.034431416150299765
      ],
      "daily_close_drawdown_pct": -8.77596565057952,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.06641201720967772,
          "SPY-USDT": -0.038709152916968435
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.06641201720967772,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03609681457009178
        },
        "SPY-USDT": {
          "BTC-USDT": -0.038709152916968435,
          "PAXG-USDT": -0.03609681457009178,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.044393834400308974,
        "2021-12-31 00:00:00+00:00": 0.20677774951386407,
        "2022-12-31 00:00:00+00:00": 0.08571084625441006,
        "2023-12-31 00:00:00+00:00": 0.17718909508293512,
        "2024-12-31 00:00:00+00:00": 0.16078619258674554,
        "2025-12-31 00:00:00+00:00": 0.1612162036667737
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
        "PAXG-USDT": -0.09277667135800802,
        "SPY-USDT": -0.046649302950643276
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.09277667135800802,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.04749089096356007
      },
      "SPY-USDT": {
        "BTC-USDT": -0.046649302950643276,
        "PAXG-USDT": -0.04749089096356007,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 3,
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
        "portfolio_return": -0.03835710777436052,
        "contributions": {
          "BTC-USDT": -0.029294977450038024,
          "PAXG-USDT": -0.009062130324322503,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.028945314511512943,
        "contributions": {
          "BTC-USDT": -0.02894531451151289,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.023979174576903017,
        "contributions": {
          "BTC-USDT": -0.023979174576903114,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.014799650523827812,
        "contributions": {
          "BTC-USDT": -0.014914653223710125,
          "PAXG-USDT": -0.008662787330090528,
          "SPY-USDT": 0.008777790029972895
        }
      },
      {
        "month": "2023-10-31 00:00:00+00:00",
        "portfolio_return": -0.014634818280395256,
        "contributions": {
          "BTC-USDT": -0.005309724516034117,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009325093764361091
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.012658142528144567,
        "contributions": {
          "BTC-USDT": -0.01265814252814458,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.012229626326108245,
        "contributions": {
          "BTC-USDT": -0.012229626326108325,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.01037012901089207,
        "contributions": {
          "BTC-USDT": -0.000844477195076173,
          "PAXG-USDT": -0.009525651815815836,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.00996837333299061,
        "contributions": {
          "BTC-USDT": -0.00996837333299062,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193291385583224,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.00919329138558329,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-07-29 00:00:00+00:00",
      "drawdown_pct": -8.77596565057952,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1514.328135618237,
        "PAXG-USDT": -98.74873916274646,
        "SPY-USDT": 34.00360407797825
      }
    },
    "engine_fee_per_side": 0.00045,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.00045,
        "samefills_net": 10683.138469071511,
        "extra_cost": 1029.7359793813796,
        "samefills_cagr_pct": 14.957152041371714,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 40,
          "win_months_all": 0.6349206349206349,
          "win_months_active": 0.6349206349206349,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -9.42214771111466,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.03958539359208613
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.042522490982412675,
          "2021-12-31 00:00:00+00:00": 0.1986940349332702,
          "2022-12-31 00:00:00+00:00": 0.07808479028467907,
          "2023-12-31 00:00:00+00:00": 0.160262791084258,
          "2024-12-31 00:00:00+00:00": 0.1521159414592237,
          "2025-12-31 00:00:00+00:00": 0.14846348756914973
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": []
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.00045,
        "samefills_net": 9653.402489690132,
        "extra_cost": 2059.471958762759,
        "samefills_cagr_pct": 13.836640209586903,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6229508196721312,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 38,
          "win_months_all": 0.6031746031746031,
          "win_months_active": 0.6031746031746031,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -10.109176561691857,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.0408212871951813
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.040651147564516155,
          "2021-12-31 00:00:00+00:00": 0.19058124738983384,
          "2022-12-31 00:00:00+00:00": 0.07032719039411517,
          "2023-12-31 00:00:00+00:00": 0.14279704497035128,
          "2024-12-31 00:00:00+00:00": 0.14290012525978502,
          "2025-12-31 00:00:00+00:00": 0.13469618767943503
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2025-07-31 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.00045,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 12549.726471459488,
        "mean_month_USDT": 205.73322084359816,
        "median_month_USDT": 72.01346736969936,
        "sum_positive_months": 15615.969664051701,
        "sum_negative_months": -3066.2431925922137,
        "worst_month": "2021-04",
        "worst_month_USDT": -440.31302133315876,
        "best3_share_positive_mtm": 0.2816248997692968,
        "class_counts": {
          "loss_base": 21,
          "zero_base": 0,
          "positive_within_cost5": 0,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 38
        },
        "positive_months": 40,
        "gross_fixed_path": {
          "positive_months": 42,
          "negative_months": 19,
          "zero_months": 0,
          "net_before_actual_fees": 14341.340342108906,
          "fee_total": 1791.613870649419,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-11",
              "gross": 23.866590762654795,
              "fee": 36.58755529985703,
              "net": -12.720964537202235
            },
            {
              "month": "2024-07",
              "gross": 15.126049310413428,
              "fee": 59.11312299410266,
              "net": -43.98707368368923
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 3,
          "BTC-USDT__SPY-USDT": 1,
          "PAXG-USDT__SPY-USDT": 0
        },
        "stress": {
          "5": {
            "positive_months": 40,
            "extra_cost": 995.3410392496776,
            "flip_months": [],
            "already_negative_months": 21,
            "already_negative_base_sum": -3066.2431925922137,
            "already_negative_after_sum": -3367.4137733814878
          },
          "10": {
            "positive_months": 38,
            "extra_cost": 1990.6820784993552,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 13.2448703715163,
                "extra": 15.322029364651105,
                "after": -2.0771589931355265
              },
              {
                "month": "2025-07",
                "base": 60.63864315707542,
                "extra": 93.70330926762355,
                "after": -33.0646661105493
              }
            ],
            "already_negative_months": 21,
            "already_negative_base_sum": -3066.2431925922137,
            "already_negative_after_sum": -3668.58435417076
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 11712.87444845288,
        "mean_month_USDT": 185.9186420389346,
        "median_month_USDT": 65.86965401260386,
        "sum_positive_months": 15615.969664051701,
        "sum_negative_months": -3903.0952155988216,
        "worst_month": "2025-12",
        "worst_month_USDT": -645.9606927870882,
        "best3_share_positive_mtm": 0.2816248997692968,
        "class_counts": {
          "loss_base": 23,
          "zero_base": 0,
          "positive_within_cost5": 0,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 38
        },
        "positive_months": 40,
        "gross_fixed_path": {
          "positive_months": 42,
          "negative_months": 21,
          "zero_months": 0,
          "net_before_actual_fees": 13566.399211339361,
          "fee_total": 1853.5247628864831,
          "fee_absorbed_positive_months": [
            {
              "month": "2023-11",
              "gross": 23.866590762654795,
              "fee": 36.58755529985703,
              "net": -12.720964537202235
            },
            {
              "month": "2024-07",
              "gross": 15.126049310413428,
              "fee": 59.11312299410266,
              "net": -43.98707368368923
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
            "positive_months": 40,
            "extra_cost": 1029.7359793813796,
            "flip_months": [],
            "already_negative_months": 23,
            "already_negative_base_sum": -3903.0952155988216,
            "already_negative_after_sum": -4238.660736519792
          },
          "10": {
            "positive_months": 38,
            "extra_cost": 2059.471958762759,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 13.2448703715163,
                "extra": 15.322029364651105,
                "after": -2.0771589931355265
              },
              {
                "month": "2025-07",
                "base": 60.63864315707542,
                "extra": 93.70330926762355,
                "after": -33.0646661105493
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -3903.0952155988216,
            "already_negative_after_sum": -4574.226257440767
          }
        }
      }
    }
  }
}
```

## [T404C](http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0)

```json
{
  "audit": {
    "n": 280,
    "net": 11877.88694749642,
    "gross_before_fees": 13827.718442593048,
    "fees": 1949.8314950966285,
    "pf_from_trades": 1.7425665719390646,
    "PF_engine": 1.7425665719390646,
    "sharpe_engine": 1.4914869510243944,
    "cagr_engine": 16.202066793044743,
    "dd_engine": -9.070557567484483,
    "plus5_samefills": 10794.64722799829,
    "plus10_samefills": 9711.407508500162,
    "exbest": 9918.754181158296,
    "ex3best": 7522.661736114689,
    "ex3best_plus10_samefills": 5391.784448892447,
    "time_any_position_pct": 40.95700502131138,
    "entry_notional_time_initial_equity": 0.4770596234297918,
    "entry_turnover_initial_equity": 216.3788870430298,
    "two_side_turnover_initial_equity": 433.2958877992509,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4845.7337193215435,
        "fees": 145.7400758468258,
        "plus10": 4683.80030171396,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05493040731009481
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 3137.7705209889023,
        "fees": 1085.5201343501953,
        "plus10": 1931.637038377572,
        "time_open_pct": 10.848623518421206,
        "entry_notional_time_initial_equity": 0.060426999343998915
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1922.0571985128756,
        "fees": 446.5625259818227,
        "plus10": 1425.876614088628,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.19115828739612883
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1972.325508673099,
        "fees": 272.0087589177859,
        "plus10": 1670.0935543200035,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.17054392937956944
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 7983.504240310439,
        "fees": 1231.2602101970213
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1922.0571985128756,
        "fees": 446.5625259818227
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1972.325508673099,
        "fees": 272.0087589177859
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 398.2001573526715,
        "by_symbol": {
          "BTC-USDT": 272.9982611721363,
          "PAXG-USDT": 0,
          "SPY-USDT": 125.20189618053519
        }
      },
      "2021": {
        "n": 53,
        "net": 1965.0439246462083,
        "by_symbol": {
          "BTC-USDT": 2037.3985078635415,
          "PAXG-USDT": -240.20281559180526,
          "SPY-USDT": 167.8482323744722
        }
      },
      "2022": {
        "n": 46,
        "net": 1093.8258903952378,
        "by_symbol": {
          "BTC-USDT": 1294.4902881011556,
          "PAXG-USDT": -112.42714114338848,
          "SPY-USDT": -88.23725656252925
        }
      },
      "2023": {
        "n": 56,
        "net": 2964.7548111974365,
        "by_symbol": {
          "BTC-USDT": 2474.006277693128,
          "PAXG-USDT": -267.4366570038275,
          "SPY-USDT": 758.1851905081351
        }
      },
      "2024": {
        "n": 56,
        "net": 2546.259375709347,
        "by_symbol": {
          "BTC-USDT": 870.1634277160258,
          "PAXG-USDT": 1191.856756299675,
          "SPY-USDT": 484.2391916936453
        }
      },
      "2025": {
        "n": 57,
        "net": 2909.802788195521,
        "by_symbol": {
          "BTC-USDT": 1034.447477764458,
          "PAXG-USDT": 1350.2670559522212,
          "SPY-USDT": 525.0882544788403
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 140,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3976.142322215758,
        "fees": 124.00793534590272,
        "gross": 4100.150257561661,
        "plus10": 3838.3557273869774,
        "exbest": 2017.0095558776495,
        "ex3": 49.41662105021413,
        "ex3_plus10": -69.38107052151815,
        "year_net": {
          "2020": 486.09589306358646,
          "2021": 1549.4327293302838,
          "2022": -176.81466579688555,
          "2023": 1886.6830382879953,
          "2024": 686.4577270072994,
          "2025": -455.71239967652116
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 869.5913971057867,
        "fees": 21.732140500923016,
        "gross": 891.3235376067096,
        "plus10": 845.4445743269832,
        "exbest": 199.32099298906093,
        "ex3": -151.86620376758384,
        "ex3_plus10": -160.7294591306134,
        "year_net": {
          "2021": 351.18719675664477,
          "2025": 518.4042003491418
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 1751.9103835520134,
        "fees": 444.8374422184034,
        "gross": 2196.747825770416,
        "plus10": 1257.646558864898,
        "exbest": 1464.9113287333134,
        "ex3": 963.2624610079455,
        "ex3_plus10": 496.3074087119812,
        "year_net": {
          "2020": -65.09905435199995,
          "2021": 594.3944801559969,
          "2022": 728.0649448602655,
          "2023": 77.31423797470987,
          "2024": 16.681072984153644,
          "2025": 400.5547019288864
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 1385.8601374368877,
        "fees": 640.6826921317921,
        "gross": 2026.5428295686797,
        "plus10": 673.990479512674,
        "exbest": 1166.4941023577803,
        "ex3": 764.0155436390934,
        "ex3_plus10": 97.66964037866796,
        "year_net": {
          "2020": -147.9985775394502,
          "2021": -457.615898379384,
          "2022": 743.2400090377755,
          "2023": 510.0090014304228,
          "2024": 167.02462772457284,
          "2025": 571.200975162951
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 38,
        "net": 1922.0571985128756,
        "fees": 446.5625259818227,
        "gross": 2368.6197244946975,
        "plus10": 1425.876614088628,
        "exbest": 764.6847026072262,
        "ex3": -969.180318330388,
        "ex3_plus10": -1428.301277965059,
        "year_net": {
          "2021": -240.20281559180526,
          "2022": -112.42714114338848,
          "2023": -267.4366570038275,
          "2024": 1191.856756299675,
          "2025": 1350.2670559522212
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 19,
        "net": 1972.325508673099,
        "fees": 272.0087589177859,
        "gross": 2244.334267590885,
        "plus10": 1670.0935543200035,
        "exbest": 1115.911707154263,
        "ex3": 17.260693121416836,
        "ex3_plus10": -235.36999336146133,
        "year_net": {
          "2020": 125.20189618053519,
          "2021": 167.8482323744722,
          "2022": -88.23725656252925,
          "2023": 758.1851905081351,
          "2024": 484.2391916936453,
          "2025": 525.0882544788403
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4991.473795168371,
        "exbest": 2886.6009529834346,
        "ex3best": 919.0080181560002,
        "ex3best_plus10": 776.0635038054645,
        "years": {
          "2020": {
            "n": 3,
            "net": 486.09589306358635,
            "plus10": 477.75755686576565
          },
          "2021": {
            "n": 6,
            "net": 1900.6199260869287,
            "plus10": 1885.4913869712832
          },
          "2022": {
            "n": 4,
            "net": -176.81466579688558,
            "plus10": -187.66998135598874
          },
          "2023": {
            "n": 4,
            "net": 1886.6830382879953,
            "plus10": 1859.3485981707981
          },
          "2024": {
            "n": 8,
            "net": 686.4577270072994,
            "plus10": 641.2046840744761
          },
          "2025": {
            "n": 6,
            "net": 62.69180067262059,
            "plus10": 7.668056987626073
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4223.290655339099,
        "exbest": 2850.7714661702,
        "ex3best": 2349.1225984448306,
        "ex3best_plus10": 1170.2978882246584,
        "years": {
          "2020": {
            "n": 8,
            "net": -213.09763189145013,
            "plus10": -234.75744853776132
          },
          "2021": {
            "n": 38,
            "net": 136.77858177661267,
            "plus10": 27.339330893274877
          },
          "2022": {
            "n": 37,
            "net": 1471.3049538980408,
            "plus10": 1308.855212923599
          },
          "2023": {
            "n": 39,
            "net": 587.3232394051337,
            "plus10": 272.465449304894
          },
          "2024": {
            "n": 37,
            "net": 183.70570070872657,
            "plus10": -60.55440525692441
          },
          "2025": {
            "n": 33,
            "net": 971.7556770918382,
            "plus10": 618.2888990504927
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2368.619724494698,
        "exbest": 764.6847026072262,
        "ex3best": -969.180318330388,
        "ex3best_plus10": -1428.301277965059,
        "years": {
          "2021": {
            "n": 6,
            "net": -240.2028155918053,
            "plus10": -283.08943192936124
          },
          "2022": {
            "n": 3,
            "net": -112.4271411433885,
            "plus10": -137.53674869621557
          },
          "2023": {
            "n": 7,
            "net": -267.4366570038276,
            "plus10": -374.3640389972227
          },
          "2024": {
            "n": 7,
            "net": 1191.856756299675,
            "plus10": 1112.6664665911564
          },
          "2025": {
            "n": 15,
            "net": 1350.267055952221,
            "plus10": 1108.2003671202708
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2244.3342675908852,
        "exbest": 1115.911707154263,
        "ex3best": 17.260693121416836,
        "ex3best_plus10": -235.36999336146133,
        "years": {
          "2020": {
            "n": 1,
            "net": 125.20189618053519,
            "plus10": 121.60507371313459
          },
          "2021": {
            "n": 3,
            "net": 167.8482323744722,
            "plus10": 133.651173796825
          },
          "2022": {
            "n": 2,
            "net": -88.23725656252925,
            "plus10": -101.973054835871
          },
          "2023": {
            "n": 6,
            "net": 758.185190508135,
            "plus10": 653.73454226107
          },
          "2024": {
            "n": 4,
            "net": 484.2391916936453,
            "plus10": 406.7751020154433
          },
          "2025": {
            "n": 3,
            "net": 525.0882544788403,
            "plus10": 456.3007173694017
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "T404C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 41,
        "win_months_all": 0.6721311475409836,
        "win_months_active": 0.6721311475409836,
        "quarters_total": 19,
        "positive_quarters": 17,
        "win_quarters": 0.8947368421052632
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6507936507936508,
      "win_months_active": 0.6507936507936508,
      "win_quarters": 0.8571428571428571,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.0470233266865242
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.043221679455063056
      ],
      "daily_close_drawdown_pct": -9.12939004230241,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.066385934079507,
          "SPY-USDT": -0.03480117783596536
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.066385934079507,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.019837583177743905
        },
        "SPY-USDT": {
          "BTC-USDT": -0.03480117783596536,
          "PAXG-USDT": 0.019837583177743905,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04350741280602666,
        "2021-12-31 00:00:00+00:00": 0.18477779173160802,
        "2022-12-31 00:00:00+00:00": 0.08847401888537254,
        "2023-12-31 00:00:00+00:00": 0.2203120602983668,
        "2024-12-31 00:00:00+00:00": 0.1550533761786046,
        "2025-12-31 00:00:00+00:00": 0.1534052023260719
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.09271938482120196,
        "SPY-USDT": -0.050726141167531685
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.09271938482120196,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.015286000290185403
      },
      "SPY-USDT": {
        "BTC-USDT": -0.050726141167531685,
        "PAXG-USDT": -0.015286000290185403,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 3,
        "both_nonzero": 29,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 3,
        "both_nonzero": 21,
        "both_negative_and_portfolio_negative": 3
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 1
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.0470233266865242,
        "contributions": {
          "BTC-USDT": -0.02945990802977919,
          "PAXG-USDT": -0.009054571539797203,
          "SPY-USDT": -0.008508847116947786
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.029028632765105034,
        "contributions": {
          "BTC-USDT": -0.02902863276510496,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.024082391278263393,
        "contributions": {
          "BTC-USDT": -0.02408239127826348,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.015605165511041075,
        "contributions": {
          "BTC-USDT": -0.006589801936765545,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.00901536357427542
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.015021238526033542,
        "contributions": {
          "BTC-USDT": -0.014900691175473874,
          "PAXG-USDT": -0.008662920734501636,
          "SPY-USDT": 0.008542373383941957
        }
      },
      {
        "month": "2023-10-31 00:00:00+00:00",
        "portfolio_return": -0.014584817564799124,
        "contributions": {
          "BTC-USDT": -0.005260465575530945,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009324351989268264
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.012664301124600041,
        "contributions": {
          "BTC-USDT": -0.01266430112460003,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.012298160236750233,
        "contributions": {
          "BTC-USDT": -0.012298160236750276,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010584612994630427,
        "contributions": {
          "BTC-USDT": -0.0010590372573924534,
          "PAXG-USDT": -0.009525575737237911,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.010077920168492627,
        "contributions": {
          "BTC-USDT": -0.010077920168492743,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -9.12939004230241,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -769.9332535250215,
        "PAXG-USDT": -206.25856920155184,
        "SPY-USDT": -96.79026285002361
      }
    },
    "engine_fee_per_side": 0.00045,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.00045,
        "samefills_net": 10794.64722799829,
        "extra_cost": 1083.2397194981274,
        "samefills_cagr_pct": 15.075766735370077,
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
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 40,
          "win_months_all": 0.6349206349206349,
          "win_months_active": 0.6349206349206349,
          "quarters_total": 21,
          "positive_quarters": 17,
          "win_quarters": 0.8095238095238095
        },
        "daily_close_drawdown_pct": -9.427781695713232,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.048908663699877675
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.041636009968650134,
          "2021-12-31 00:00:00+00:00": 0.17561420157263696,
          "2022-12-31 00:00:00+00:00": 0.08066154181612073,
          "2023-12-31 00:00:00+00:00": 0.20312054843184613,
          "2024-12-31 00:00:00+00:00": 0.14591582342728304,
          "2025-12-31 00:00:00+00:00": 0.1397751686389186
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.00045,
        "samefills_net": 9711.407508500162,
        "extra_cost": 2166.479438996255,
        "samefills_cagr_pct": 13.901004741702616,
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
        "daily_close_drawdown_pct": -10.124479840336642,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.05080746356312804
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03976460713127339,
          "2021-12-31 00:00:00+00:00": 0.16641762554646777,
          "2022-12-31 00:00:00+00:00": 0.07269752634175308,
          "2023-12-31 00:00:00+00:00": 0.18533782807618215,
          "2024-12-31 00:00:00+00:00": 0.13618515254468044,
          "2025-12-31 00:00:00+00:00": 0.12501936864391205
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2020-11-30 00:00:00+00:00",
          "2024-08-31 00:00:00+00:00",
          "2025-07-31 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.00045,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 12860.733751640868,
        "mean_month_USDT": 210.8317008465716,
        "median_month_USDT": 70.74062394054636,
        "sum_positive_months": 16138.945845405982,
        "sum_negative_months": -3278.2120937651143,
        "worst_month": "2021-04",
        "worst_month_USDT": -534.902095138812,
        "best3_share_positive_mtm": 0.2657628960197866,
        "class_counts": {
          "loss_base": 20,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 38
        },
        "positive_months": 41,
        "gross_fixed_path": {
          "positive_months": 42,
          "negative_months": 19,
          "zero_months": 0,
          "net_before_actual_fees": 14722.613600483988,
          "fee_total": 1861.8798488431205,
          "fee_absorbed_positive_months": [
            {
              "month": "2024-07",
              "gross": 15.162359577764605,
              "fee": 60.22982303107072,
              "net": -45.06746345330612
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 3,
          "BTC-USDT__SPY-USDT": 3,
          "PAXG-USDT__SPY-USDT": 2
        },
        "stress": {
          "5": {
            "positive_months": 40,
            "extra_cost": 1034.3776938017334,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 4.403136500855908,
                "extra": 7.663043166025551,
                "after": -3.259906665169183
              }
            ],
            "already_negative_months": 20,
            "already_negative_base_sum": -3278.2120937651143,
            "already_negative_after_sum": -3571.405484270317
          },
          "10": {
            "positive_months": 38,
            "extra_cost": 2068.7553876034667,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 4.403136500855908,
                "extra": 15.326086332051101,
                "after": -10.922949831194273
              },
              {
                "month": "2024-08",
                "base": 36.00206434903157,
                "extra": 46.513925820165085,
                "after": -10.51186147113367
              },
              {
                "month": "2025-07",
                "base": 62.0234556623509,
                "extra": 95.10559769065593,
                "after": -33.08214202830641
              }
            ],
            "already_negative_months": 20,
            "already_negative_base_sum": -3278.2120937651143,
            "already_negative_after_sum": -3864.5988747755237
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 11877.886947496423,
        "mean_month_USDT": 188.53788805549877,
        "median_month_USDT": 66.03728734953984,
        "sum_positive_months": 16138.945845405982,
        "sum_negative_months": -4261.058897909559,
        "worst_month": "2025-12",
        "worst_month_USDT": -791.9554739249252,
        "best3_share_positive_mtm": 0.2657628960197866,
        "class_counts": {
          "loss_base": 22,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 38
        },
        "positive_months": 41,
        "gross_fixed_path": {
          "positive_months": 42,
          "negative_months": 21,
          "zero_months": 0,
          "net_before_actual_fees": 13827.718442593052,
          "fee_total": 1949.83149509663,
          "fee_absorbed_positive_months": [
            {
              "month": "2024-07",
              "gross": 15.162359577764605,
              "fee": 60.22982303107072,
              "net": -45.06746345330612
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 4,
          "PAXG-USDT__SPY-USDT": 3
        },
        "stress": {
          "5": {
            "positive_months": 40,
            "extra_cost": 1083.2397194981272,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 4.403136500855908,
                "extra": 7.663043166025551,
                "after": -3.259906665169183
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -4261.058897909559,
            "already_negative_after_sum": -4603.114314111161
          },
          "10": {
            "positive_months": 38,
            "extra_cost": 2166.4794389962544,
            "flip_months": [
              {
                "month": "2020-11",
                "base": 4.403136500855908,
                "extra": 15.326086332051101,
                "after": -10.922949831194273
              },
              {
                "month": "2024-08",
                "base": 36.00206434903157,
                "extra": 46.513925820165085,
                "after": -10.51186147113367
              },
              {
                "month": "2025-07",
                "base": 62.0234556623509,
                "extra": 95.10559769065593,
                "after": -33.08214202830641
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -4261.058897909559,
            "already_negative_after_sum": -4945.16973031276
          }
        }
      }
    }
  }
}
```

## Comparaciones por mes
```json
{}
```