# Portfolio — auditoría económica exacta

Job `9ed855c0d58f4062bfdcfbcb2ec3c4bb` succeeded. Fuente en PORT_CANDIDATES_ANALYSIS_SOURCE_20261019.md. Fills/cantidades/comisiones/PNL/balances y MTM de las cuatro concilian. Artefacto portfolio_summary.json íntegro44539bytes. Todos los retornos son sobre capital compartido10k; no se sumaron curvas aisladas. Cohortes por cierre y MTM anual están claramente separados. Contadores de capacidad se reportarán aparte tras réplica diagnóstica.

```json
{
  "results": {
    "CONTROL": {
      "n": 222,
      "net": 7815.591290800872,
      "gross_before_fees": 9365.231702570745,
      "fees": 1549.640411769873,
      "pf_from_trades": 1.591372572345478,
      "PF_engine": 1.5913725723454775,
      "sharpe_engine": 1.1332815027260958,
      "cagr_engine": 11.713097159064745,
      "dd_engine": -8.544575811263911,
      "plus5_samefills": 6954.6799509287175,
      "plus10_samefills": 6093.768611056568,
      "exbest": 5999.17680545428,
      "ex3best": 3899.6689005456938,
      "ex3best_plus10_samefills": 2209.567062375219,
      "time_any_position_pct": 38.78955742395049,
      "entry_notional_time_initial_equity": 0.4239657759502964,
      "entry_turnover_initial_equity": 171.90133709336956,
      "two_side_turnover_initial_equity": 344.3645359488606,
      "by_group": {
        "BTC-USDT:long": {
          "n": 31,
          "net": 4650.842743651732,
          "fees": 132.36823949541622,
          "plus10": 4503.766921990158,
          "time_open_pct": 11.577443510246978,
          "entry_notional_time_initial_equity": 0.05020640010978535
        },
        "BTC-USDT:short": {
          "n": 125,
          "net": 1223.6142076437054,
          "fees": 649.6928330333004,
          "plus10": 501.73328205114973,
          "time_open_pct": 5.535813335668827,
          "entry_notional_time_initial_equity": 0.028285198441587243
        },
        "PAXG-USDT:long": {
          "n": 35,
          "net": 938.7626445331489,
          "fees": 367.935573984533,
          "plus10": 529.9453401058897,
          "time_open_pct": 13.35712617504525,
          "entry_notional_time_initial_equity": 0.150890732993963
        },
        "SPY-USDT:long": {
          "n": 31,
          "net": 1002.371694972285,
          "fees": 399.64376525662306,
          "plus10": 558.3230669093703,
          "time_open_pct": 15.264093244584574,
          "entry_notional_time_initial_equity": 0.19458344440496103
        }
      },
      "by_symbol": {
        "BTC-USDT": {
          "n": 156,
          "net": 5874.45695129544,
          "fees": 782.0610725287167
        },
        "PAXG-USDT": {
          "n": 35,
          "net": 938.7626445331489,
          "fees": 367.935573984533
        },
        "SPY-USDT": {
          "n": 31,
          "net": 1002.371694972285,
          "fees": 399.64376525662306
        }
      },
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 11,
          "net": 475.812630198268,
          "by_symbol": {
            "BTC-USDT": 341.763166994209,
            "PAXG-USDT": 0,
            "SPY-USDT": 134.04946320405904
          }
        },
        "2021": {
          "n": 45,
          "net": 1637.4486429869248,
          "by_symbol": {
            "BTC-USDT": 1491.0446661219917,
            "PAXG-USDT": -222.54641384540193,
            "SPY-USDT": 368.9503907103351
          }
        },
        "2022": {
          "n": 28,
          "net": 242.84173202124805,
          "by_symbol": {
            "BTC-USDT": 599.3271726371519,
            "PAXG-USDT": -106.49159493456784,
            "SPY-USDT": -249.99384568133593
          }
        },
        "2023": {
          "n": 42,
          "net": 2655.3161890516308,
          "by_symbol": {
            "BTC-USDT": 2215.2781737410564,
            "PAXG-USDT": -117.07425170425847,
            "SPY-USDT": 557.1122670148325
          }
        },
        "2024": {
          "n": 51,
          "net": 1574.761326267533,
          "by_symbol": {
            "BTC-USDT": 839.7620565949818,
            "PAXG-USDT": 760.7488887530828,
            "SPY-USDT": -25.749619080531986
          }
        },
        "2025": {
          "n": 45,
          "net": 1229.4107702752665,
          "by_symbol": {
            "BTC-USDT": 387.28171520604724,
            "PAXG-USDT": 624.1260162642941,
            "SPY-USDT": 218.00303880492618
          }
        }
      },
      "entry_order_types": {
        "LIMIT": 86,
        "MARKET": 11,
        "STOP": 125
      },
      "audit": "passed",
      "mtm": {
        "name": "CONTROL",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 59,
          "positive_months": 33,
          "win_months_all": 0.5409836065573771,
          "win_months_active": 0.559322033898305,
          "quarters_total": 19,
          "positive_quarters": 13,
          "win_quarters": 0.6842105263157895
        },
        "months_total": 63,
        "months_active": 61,
        "win_months_all": 0.5238095238095238,
        "win_months_active": 0.5409836065573771,
        "win_quarters": 0.6666666666666666,
        "worst_month": [
          "2021-08-31 00:00:00+00:00",
          -0.04701880605670283
        ],
        "worst_quarter": [
          "2023-09-30 00:00:00+00:00",
          -0.02865635028415181
        ],
        "daily_close_drawdown_pct": -8.534151038468174,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": 0.005348912284306448,
            "SPY-USDT": -0.050731912874285724
          },
          "PAXG-USDT": {
            "BTC-USDT": 0.005348912284306448,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.0777846445849215
          },
          "SPY-USDT": {
            "BTC-USDT": -0.050731912874285724,
            "PAXG-USDT": -0.0777846445849215,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.05187550288400611,
          "2021-12-31 00:00:00+00:00": 0.14714866909247237,
          "2022-12-31 00:00:00+00:00": 0.023994145265200162,
          "2023-12-31 00:00:00+00:00": 0.21489916261889164,
          "2024-12-31 00:00:00+00:00": 0.10490422696808643,
          "2025-12-31 00:00:00+00:00": 0.07412259674575838
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
          "PAXG-USDT": -0.0039956831317608885,
          "SPY-USDT": -0.05394768150942237
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.0039956831317608885,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.08372283512944892
        },
        "SPY-USDT": {
          "BTC-USDT": -0.05394768150942237,
          "PAXG-USDT": -0.08372283512944892,
          "SPY-USDT": 1
        }
      },
      "co_loss_complete_months": {
        "BTC-USDT__PAXG-USDT": {
          "both_negative": 4,
          "both_nonzero": 29,
          "both_negative_and_portfolio_negative": 4
        },
        "BTC-USDT__SPY-USDT": {
          "both_negative": 6,
          "both_nonzero": 30,
          "both_negative_and_portfolio_negative": 5
        },
        "PAXG-USDT__SPY-USDT": {
          "both_negative": 3,
          "both_nonzero": 16,
          "both_negative_and_portfolio_negative": 2
        }
      },
      "worst_10_complete_months": [
        {
          "month": "2021-08-31 00:00:00+00:00",
          "portfolio_return": -0.04701880605670283,
          "contributions": {
            "BTC-USDT": -0.04406960363913311,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.0029492024175697194
          }
        },
        {
          "month": "2021-04-30 00:00:00+00:00",
          "portfolio_return": -0.02997886503788927,
          "contributions": {
            "BTC-USDT": -0.029356791770237284,
            "PAXG-USDT": -0.009056544833233737,
            "SPY-USDT": 0.008434471565581783
          }
        },
        {
          "month": "2025-09-30 00:00:00+00:00",
          "portfolio_return": -0.01760999347549619,
          "contributions": {
            "BTC-USDT": 0.0003627734941899547,
            "PAXG-USDT": -0.017972766969686207,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-03-31 00:00:00+00:00",
          "portfolio_return": -0.017070895844737644,
          "contributions": {
            "BTC-USDT": -0.007980309257633236,
            "PAXG-USDT": -0.00909058658710438,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-09-30 00:00:00+00:00",
          "portfolio_return": -0.014752219875773576,
          "contributions": {
            "BTC-USDT": 0,
            "PAXG-USDT": -0.00912973913077297,
            "SPY-USDT": -0.005622480745000716
          }
        },
        {
          "month": "2023-07-31 00:00:00+00:00",
          "portfolio_return": -0.014227948559936587,
          "contributions": {
            "BTC-USDT": -0.014097664195775279,
            "PAXG-USDT": -0.008912383575731396,
            "SPY-USDT": 0.008782099211570131
          }
        },
        {
          "month": "2023-09-30 00:00:00+00:00",
          "portfolio_return": -0.011369211938152324,
          "contributions": {
            "BTC-USDT": 0.003258401386954127,
            "PAXG-USDT": -0.008887281255343792,
            "SPY-USDT": -0.005740332069762574
          }
        },
        {
          "month": "2025-10-31 00:00:00+00:00",
          "portfolio_return": -0.011334676075651973,
          "contributions": {
            "BTC-USDT": -0.004390281205651742,
            "PAXG-USDT": 0.0018921697594605448,
            "SPY-USDT": -0.008836564629460617
          }
        },
        {
          "month": "2024-02-29 00:00:00+00:00",
          "portfolio_return": -0.0105813310433025,
          "contributions": {
            "BTC-USDT": -0.009560267932495795,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.001021063110806722
          }
        },
        {
          "month": "2024-06-30 00:00:00+00:00",
          "portfolio_return": -0.009831043403084161,
          "contributions": {
            "BTC-USDT": -0.00983104340308419,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        }
      ],
      "daily_drawdown_episode": {
        "peak": "2024-05-20 00:00:00+00:00",
        "trough": "2024-07-29 00:00:00+00:00",
        "drawdown_pct": -8.534151038468174,
        "route_pnl_delta_USDT": {
          "BTC-USDT": -1153.7504105610496,
          "PAXG-USDT": -310.7263929012041,
          "SPY-USDT": 61.33784592035988
        }
      }
    },
    "A": {
      "n": 225,
      "net": 8527.169363478115,
      "gross_before_fees": 10107.443824787124,
      "fees": 1580.2744613090094,
      "pf_from_trades": 1.6538444444003262,
      "PF_engine": 1.6538444444003253,
      "sharpe_engine": 1.205869049427831,
      "cagr_engine": 12.555423733209636,
      "dd_engine": -7.427526935307682,
      "plus5_samefills": 7649.239107195341,
      "plus10_samefills": 6771.308850912549,
      "exbest": 6730.216461903082,
      "ex3best": 4607.50036797944,
      "ex3best_plus10_samefills": 2883.492029690053,
      "time_any_position_pct": 39.88322531675133,
      "entry_notional_time_initial_equity": 0.44442135727309645,
      "entry_turnover_initial_equity": 175.26846235069678,
      "two_side_turnover_initial_equity": 351.1721025131134,
      "by_group": {
        "BTC-USDT:long": {
          "n": 31,
          "net": 4652.940192433214,
          "fees": 132.63498014065826,
          "plus10": 4505.567992276925,
          "time_open_pct": 11.577443510246978,
          "entry_notional_time_initial_equity": 0.05026972746309081
        },
        "BTC-USDT:short": {
          "n": 125,
          "net": 1226.9823827566759,
          "fees": 650.8504710380428,
          "plus10": 503.81519271440607,
          "time_open_pct": 5.535813335668827,
          "entry_notional_time_initial_equity": 0.02833365388584397
        },
        "PAXG-USDT:long": {
          "n": 38,
          "net": 1657.3662366060676,
          "fees": 398.1910878551075,
          "plus10": 1214.931694544836,
          "time_open_pct": 15.204866584924389,
          "entry_notional_time_initial_equity": 0.1717872257381192
        },
        "SPY-USDT:long": {
          "n": 31,
          "net": 989.8805516821639,
          "fees": 398.59792227520086,
          "plus10": 546.9939713763848,
          "time_open_pct": 15.264093244584574,
          "entry_notional_time_initial_equity": 0.19403075018604243
        }
      },
      "by_symbol": {
        "BTC-USDT": {
          "n": 156,
          "net": 5879.922575189889,
          "fees": 783.4854511787015
        },
        "PAXG-USDT": {
          "n": 38,
          "net": 1657.3662366060676,
          "fees": 398.1910878551075
        },
        "SPY-USDT": {
          "n": 31,
          "net": 989.8805516821639,
          "fees": 398.59792227520086
        }
      },
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 11,
          "net": 475.812630198268,
          "by_symbol": {
            "BTC-USDT": 341.763166994209,
            "PAXG-USDT": 0,
            "SPY-USDT": 134.04946320405904
          }
        },
        "2021": {
          "n": 45,
          "net": 1614.4101136540235,
          "by_symbol": {
            "BTC-USDT": 1489.8952337329724,
            "PAXG-USDT": -244.23141470172354,
            "SPY-USDT": 368.74629462277437
          }
        },
        "2022": {
          "n": 28,
          "net": 237.33422435235633,
          "by_symbol": {
            "BTC-USDT": 598.5049709381691,
            "PAXG-USDT": -111.73824733393221,
            "SPY-USDT": -249.43249925188053
          }
        },
        "2023": {
          "n": 44,
          "net": 2505.0513701767673,
          "by_symbol": {
            "BTC-USDT": 2190.739707901246,
            "PAXG-USDT": -236.21041902509856,
            "SPY-USDT": 550.5220813006193
          }
        },
        "2024": {
          "n": 51,
          "net": 1910.9856609525232,
          "by_symbol": {
            "BTC-USDT": 873.2655587717499,
            "PAXG-USDT": 1067.7121131323242,
            "SPY-USDT": -29.99201095155108
          }
        },
        "2025": {
          "n": 46,
          "net": 1783.5753641441815,
          "by_symbol": {
            "BTC-USDT": 385.75393685154154,
            "PAXG-USDT": 1181.834204534497,
            "SPY-USDT": 215.98722275814262
          }
        }
      },
      "entry_order_types": {
        "LIMIT": 51,
        "MARKET": 49,
        "STOP": 125
      },
      "audit": "passed",
      "mtm": {
        "name": "A",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 59,
          "positive_months": 35,
          "win_months_all": 0.5737704918032787,
          "win_months_active": 0.5932203389830508,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "months_total": 63,
        "months_active": 61,
        "win_months_all": 0.5555555555555556,
        "win_months_active": 0.5737704918032787,
        "win_quarters": 0.7142857142857143,
        "worst_month": [
          "2021-08-31 00:00:00+00:00",
          -0.04705010050332359
        ],
        "worst_quarter": [
          "2025-12-31 00:00:00+00:00",
          -0.030004357064758125
        ],
        "daily_close_drawdown_pct": -7.416944659785008,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.07821070137891747,
            "SPY-USDT": -0.0509224549828708
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.07821070137891747,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.06121165436259584
          },
          "SPY-USDT": {
            "BTC-USDT": -0.0509224549828708,
            "PAXG-USDT": -0.06121165436259584,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.051311512385931124,
          "2021-12-31 00:00:00+00:00": 0.14558088344148512,
          "2022-12-31 00:00:00+00:00": 0.02357540086752774,
          "2023-12-31 00:00:00+00:00": 0.20320744626350695,
          "2024-12-31 00:00:00+00:00": 0.1288367910320658,
          "2025-12-31 00:00:00+00:00": 0.10652285072220025
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
          "PAXG-USDT": -0.09345879906342656,
          "SPY-USDT": -0.05414224029905034
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.09345879906342656,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.06814321021973692
        },
        "SPY-USDT": {
          "BTC-USDT": -0.05414224029905034,
          "PAXG-USDT": -0.06814321021973692,
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
          "both_negative": 6,
          "both_nonzero": 30,
          "both_negative_and_portfolio_negative": 5
        },
        "PAXG-USDT__SPY-USDT": {
          "both_negative": 3,
          "both_nonzero": 16,
          "both_negative_and_portfolio_negative": 2
        }
      },
      "worst_10_complete_months": [
        {
          "month": "2021-08-31 00:00:00+00:00",
          "portfolio_return": -0.04705010050332359,
          "contributions": {
            "BTC-USDT": -0.044100963356309496,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.0029491371470141015
          }
        },
        {
          "month": "2021-04-30 00:00:00+00:00",
          "portfolio_return": -0.029978448567634097,
          "contributions": {
            "BTC-USDT": -0.029356788860400544,
            "PAXG-USDT": -0.00905613043679293,
            "SPY-USDT": 0.008434470729559393
          }
        },
        {
          "month": "2023-03-31 00:00:00+00:00",
          "portfolio_return": -0.017110826118462708,
          "contributions": {
            "BTC-USDT": -0.007995300969154752,
            "PAXG-USDT": -0.009115525149307952,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-09-30 00:00:00+00:00",
          "portfolio_return": -0.014751573600462975,
          "contributions": {
            "BTC-USDT": 0,
            "PAXG-USDT": -0.009129032654277424,
            "SPY-USDT": -0.005622540946185485
          }
        },
        {
          "month": "2023-07-31 00:00:00+00:00",
          "portfolio_return": -0.013996966134263156,
          "contributions": {
            "BTC-USDT": -0.014111807727134136,
            "PAXG-USDT": -0.008662570927058326,
            "SPY-USDT": 0.008777412519929409
          }
        },
        {
          "month": "2025-10-31 00:00:00+00:00",
          "portfolio_return": -0.011437902440898373,
          "contributions": {
            "BTC-USDT": -0.004358707491441681,
            "PAXG-USDT": 0.0017575097824420892,
            "SPY-USDT": -0.008836704731898643
          }
        },
        {
          "month": "2023-09-30 00:00:00+00:00",
          "portfolio_return": -0.011374348746047369,
          "contributions": {
            "BTC-USDT": 0.003252792493994129,
            "PAXG-USDT": -0.00888681979045146,
            "SPY-USDT": -0.005740321449590036
          }
        },
        {
          "month": "2024-02-29 00:00:00+00:00",
          "portfolio_return": -0.010624288166608431,
          "contributions": {
            "BTC-USDT": -0.009603554115599345,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.001020734051009004
          }
        },
        {
          "month": "2024-06-30 00:00:00+00:00",
          "portfolio_return": -0.009843993574851884,
          "contributions": {
            "BTC-USDT": -0.009843993574851955,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2024-01-31 00:00:00+00:00",
          "portfolio_return": -0.009279994456903862,
          "contributions": {
            "BTC-USDT": -0.0003587387180818459,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.00892125573882215
          }
        }
      ],
      "daily_drawdown_episode": {
        "peak": "2024-05-20 00:00:00+00:00",
        "trough": "2024-06-07 00:00:00+00:00",
        "drawdown_pct": -7.416944659785008,
        "route_pnl_delta_USDT": {
          "BTC-USDT": -878.2638956313394,
          "PAXG-USDT": -230.90145208645322,
          "SPY-USDT": -91.40403443710466
        }
      }
    },
    "B": {
      "n": 206,
      "net": 9234.194391279198,
      "gross_before_fees": 10596.115222063538,
      "fees": 1361.9208307843405,
      "pf_from_trades": 1.796287003921919,
      "PF_engine": 1.7962870039219192,
      "sharpe_engine": 1.3239806209896499,
      "cagr_engine": 13.366850134409681,
      "dd_engine": -7.496635153613385,
      "plus5_samefills": 8477.57170751012,
      "plus10_samefills": 7720.949023741038,
      "exbest": 7417.779905932609,
      "ex3best": 5275.689175292896,
      "ex3best_plus10_samefills": 3794.723629782647,
      "time_any_position_pct": 34.4906434285047,
      "entry_notional_time_initial_equity": 0.36204638942146256,
      "entry_turnover_initial_equity": 150.98647327226607,
      "two_side_turnover_initial_equity": 302.6490735076313,
      "by_group": {
        "BTC-USDT:long": {
          "n": 31,
          "net": 4663.021116968694,
          "fees": 134.29267887412925,
          "plus10": 4513.807029330772,
          "time_open_pct": 11.577443510246978,
          "entry_notional_time_initial_equity": 0.05086836897580137
        },
        "BTC-USDT:short": {
          "n": 125,
          "net": 1256.556119305704,
          "fees": 660.8666762311436,
          "plus10": 522.2598123822113,
          "time_open_pct": 5.535813335668827,
          "entry_notional_time_initial_equity": 0.02876201701071935
        },
        "PAXG-USDT:long": {
          "n": 38,
          "net": 1669.7805103621536,
          "fees": 406.215739766758,
          "plus10": 1218.4296883990894,
          "time_open_pct": 15.204866584924389,
          "entry_notional_time_initial_equity": 0.17427680317781127
        },
        "SPY-USDT:long": {
          "n": 12,
          "net": 1644.836644642646,
          "fees": 160.54573591230974,
          "plus10": 1466.4524936289686,
          "time_open_pct": 8.130765749985404,
          "entry_notional_time_initial_equity": 0.10813920025713068
        }
      },
      "by_symbol": {
        "BTC-USDT": {
          "n": 156,
          "net": 5919.577236274396,
          "fees": 795.159355105273
        },
        "PAXG-USDT": {
          "n": 38,
          "net": 1669.7805103621536,
          "fees": 406.215739766758
        },
        "SPY-USDT": {
          "n": 12,
          "net": 1644.836644642646,
          "fees": 160.54573591230974
        }
      },
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 11,
          "net": 475.812630198268,
          "by_symbol": {
            "BTC-USDT": 341.763166994209,
            "PAXG-USDT": 0,
            "SPY-USDT": 134.04946320405904
          }
        },
        "2021": {
          "n": 43,
          "net": 1614.6918853450438,
          "by_symbol": {
            "BTC-USDT": 1487.3210755859832,
            "PAXG-USDT": -243.26424643361068,
            "SPY-USDT": 370.6350561926713
          }
        },
        "2022": {
          "n": 24,
          "net": 375.4822229209399,
          "by_symbol": {
            "BTC-USDT": 606.1869609803175,
            "PAXG-USDT": -113.54925800096672,
            "SPY-USDT": -117.15548005841087
          }
        },
        "2023": {
          "n": 39,
          "net": 2141.2346776080594,
          "by_symbol": {
            "BTC-USDT": 2222.7421859917226,
            "PAXG-USDT": -243.5959803821611,
            "SPY-USDT": 162.08847199849674
          }
        },
        "2024": {
          "n": 46,
          "net": 2453.9295284644713,
          "by_symbol": {
            "BTC-USDT": 873.2900868496109,
            "PAXG-USDT": 1071.9438049700266,
            "SPY-USDT": 508.69563664483337
          }
        },
        "2025": {
          "n": 43,
          "net": 2173.043446742414,
          "by_symbol": {
            "BTC-USDT": 388.27375987255334,
            "PAXG-USDT": 1198.2461902088653,
            "SPY-USDT": 586.5234966609964
          }
        }
      },
      "entry_order_types": {
        "LIMIT": 36,
        "MARKET": 45,
        "STOP": 125
      },
      "audit": "passed",
      "mtm": {
        "name": "B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 57,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6491228070175439,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 59,
        "win_months_all": 0.5873015873015873,
        "win_months_active": 0.6271186440677966,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-08-31 00:00:00+00:00",
          -0.043935167167247435
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.02968161486672516
        ],
        "daily_close_drawdown_pct": -7.486828490893316,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.07742718225397777,
            "SPY-USDT": -0.0584106967530117
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.07742718225397777,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.035466162582898864
          },
          "SPY-USDT": {
            "BTC-USDT": -0.0584106967530117,
            "PAXG-USDT": -0.035466162582898864,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.051311512385931124,
          "2021-12-31 00:00:00+00:00": 0.150040152048192,
          "2022-12-31 00:00:00+00:00": 0.03105595985992382,
          "2023-12-31 00:00:00+00:00": 0.1717661603955667,
          "2024-12-31 00:00:00+00:00": 0.16799427204987905,
          "2025-12-31 00:00:00+00:00": 0.1273679280962139
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
          "PAXG-USDT": -0.0926537079234676,
          "SPY-USDT": -0.06480453570995764
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.0926537079234676,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.04688802119654392
        },
        "SPY-USDT": {
          "BTC-USDT": -0.06480453570995764,
          "PAXG-USDT": -0.04688802119654392,
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
          "month": "2021-08-31 00:00:00+00:00",
          "portfolio_return": -0.043935167167247435,
          "contributions": {
            "BTC-USDT": -0.04393516716724733,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-04-30 00:00:00+00:00",
          "portfolio_return": -0.0384179941811591,
          "contributions": {
            "BTC-USDT": -0.029356788860400544,
            "PAXG-USDT": -0.009061205320758629,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-03-31 00:00:00+00:00",
          "portfolio_return": -0.01710078503999235,
          "contributions": {
            "BTC-USDT": -0.007985264355228944,
            "PAXG-USDT": -0.009115520684763425,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-07-31 00:00:00+00:00",
          "portfolio_return": -0.013975266422752375,
          "contributions": {
            "BTC-USDT": -0.014090204741656934,
            "PAXG-USDT": -0.00866282411693078,
            "SPY-USDT": 0.00877776243583532
          }
        },
        {
          "month": "2024-06-30 00:00:00+00:00",
          "portfolio_return": -0.009882143460111625,
          "contributions": {
            "BTC-USDT": -0.009882143460111632,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-09-30 00:00:00+00:00",
          "portfolio_return": -0.009193289785775716,
          "contributions": {
            "BTC-USDT": 0,
            "PAXG-USDT": -0.009193289785775794,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-03-31 00:00:00+00:00",
          "portfolio_return": -0.00901590704146249,
          "contributions": {
            "BTC-USDT": -0.009015907041462481,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2022-11-30 00:00:00+00:00",
          "portfolio_return": -0.006830161025010439,
          "contributions": {
            "BTC-USDT": 0.0026669467296931925,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.009497107754703653
          }
        },
        {
          "month": "2022-02-28 00:00:00+00:00",
          "portfolio_return": -0.006190055039593023,
          "contributions": {
            "BTC-USDT": 0.00322180826268023,
            "PAXG-USDT": -0.009411863302273338,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-09-30 00:00:00+00:00",
          "portfolio_return": -0.005666942565455413,
          "contributions": {
            "BTC-USDT": 0.0032712177679581414,
            "PAXG-USDT": -0.008938160333413455,
            "SPY-USDT": 0
          }
        }
      ],
      "daily_drawdown_episode": {
        "peak": "2024-05-20 00:00:00+00:00",
        "trough": "2024-06-07 00:00:00+00:00",
        "drawdown_pct": -7.486828490893316,
        "route_pnl_delta_USDT": {
          "BTC-USDT": -886.1204996328338,
          "PAXG-USDT": -233.43359289761935,
          "SPY-USDT": -105.91803263409588
        }
      }
    },
    "C": {
      "n": 213,
      "net": 9407.826225512972,
      "gross_before_fees": 10861.593642289721,
      "fees": 1453.76741677675,
      "pf_from_trades": 1.7764073161597513,
      "PF_engine": 1.7764073161597511,
      "sharpe_engine": 1.3154302129959168,
      "cagr_engine": 13.56242675878292,
      "dd_engine": -8.168012803517177,
      "plus5_samefills": 8600.177660637002,
      "plus10_samefills": 7792.529095761029,
      "exbest": 7620.604115823741,
      "ex3best": 5442.756352116708,
      "ex3best_plus10_samefills": 3859.9175243373616,
      "time_any_position_pct": 36.95670578618555,
      "entry_notional_time_initial_equity": 0.41184408813525536,
      "entry_turnover_initial_equity": 161.17792481160987,
      "two_side_turnover_initial_equity": 323.0594259503889,
      "by_group": {
        "BTC-USDT:long": {
          "n": 31,
          "net": 4618.732513139611,
          "fees": 134.90596125647824,
          "plus10": 4468.837000632415,
          "time_open_pct": 11.577443510246978,
          "entry_notional_time_initial_equity": 0.050880793951029804
        },
        "BTC-USDT:short": {
          "n": 125,
          "net": 1251.4936273012945,
          "fees": 661.421557996964,
          "plus10": 516.5807850824464,
          "time_open_pct": 5.535813335668827,
          "entry_notional_time_initial_equity": 0.028789326270889797
        },
        "PAXG-USDT:long": {
          "n": 38,
          "net": 1721.2570535973296,
          "fees": 407.3640667696651,
          "plus10": 1268.630312742147,
          "time_open_pct": 15.204866584924389,
          "entry_notional_time_initial_equity": 0.1753615213355421
        },
        "SPY-USDT:long": {
          "n": 19,
          "net": 1816.343031474734,
          "fees": 250.07583075364275,
          "plus10": 1538.4809973040194,
          "time_open_pct": 11.413265604017049,
          "entry_notional_time_initial_equity": 0.15681244657779367
        }
      },
      "by_symbol": {
        "BTC-USDT": {
          "n": 156,
          "net": 5870.226140440905,
          "fees": 796.3275192534423
        },
        "PAXG-USDT": {
          "n": 38,
          "net": 1721.2570535973296,
          "fees": 407.3640667696651
        },
        "SPY-USDT": {
          "n": 19,
          "net": 1816.343031474734,
          "fees": 250.07583075364275
        }
      },
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 11,
          "net": 466.96506317474416,
          "by_symbol": {
            "BTC-USDT": 341.763166994209,
            "PAXG-USDT": 0,
            "SPY-USDT": 125.20189618053519
          }
        },
        "2021": {
          "n": 45,
          "net": 1391.8747847940872,
          "by_symbol": {
            "BTC-USDT": 1470.2387039322425,
            "PAXG-USDT": -239.79890441855406,
            "SPY-USDT": 161.43498528039905
          }
        },
        "2022": {
          "n": 25,
          "net": 401.42662475398413,
          "by_symbol": {
            "BTC-USDT": 594.1347263895591,
            "PAXG-USDT": -111.05717230322162,
            "SPY-USDT": -81.65092933235327
          }
        },
        "2023": {
          "n": 41,
          "net": 2643.4703457069663,
          "by_symbol": {
            "BTC-USDT": 2181.5975774639423,
            "PAXG-USDT": -237.62021450236603,
            "SPY-USDT": 699.4929827453907
          }
        },
        "2024": {
          "n": 47,
          "net": 2421.007960261222,
          "by_symbol": {
            "BTC-USDT": 886.4018915038351,
            "PAXG-USDT": 1092.894879266541,
            "SPY-USDT": 441.7111894908456
          }
        },
        "2025": {
          "n": 44,
          "net": 2083.081446821969,
          "by_symbol": {
            "BTC-USDT": 396.0900741571201,
            "PAXG-USDT": 1216.8384655549307,
            "SPY-USDT": 470.15290710991655
          }
        }
      },
      "entry_order_types": {
        "LIMIT": 27,
        "MARKET": 61,
        "STOP": 125
      },
      "audit": "passed",
      "mtm": {
        "name": "C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 57,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6666666666666666,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 59,
        "win_months_all": 0.6031746031746031,
        "win_months_active": 0.6440677966101694,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.046955269279550294
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.03829863262349764
        ],
        "daily_close_drawdown_pct": -8.227718310465637,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.07771894738387049,
            "SPY-USDT": -0.10036532846573472
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.07771894738387049,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.021055784462945155
          },
          "SPY-USDT": {
            "BTC-USDT": -0.10036532846573472,
            "PAXG-USDT": 0.021055784462945155,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.05042509079164881,
          "2021-12-31 00:00:00+00:00": 0.1289562627480143,
          "2022-12-31 00:00:00+00:00": 0.03385041284816226,
          "2023-12-31 00:00:00+00:00": 0.2156127969639383,
          "2024-12-31 00:00:00+00:00": 0.16244301612112677,
          "2025-12-31 00:00:00+00:00": 0.120237352609321
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
          "PAXG-USDT": -0.0929486084491788,
          "SPY-USDT": -0.11139265076359911
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.0929486084491788,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.014376252351836392
        },
        "SPY-USDT": {
          "BTC-USDT": -0.11139265076359911,
          "PAXG-USDT": -0.014376252351836392,
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
          "both_negative": 2,
          "both_nonzero": 21,
          "both_negative_and_portfolio_negative": 2
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
          "portfolio_return": -0.046955269279550294,
          "contributions": {
            "BTC-USDT": -0.029391691171712853,
            "PAXG-USDT": -0.009055148703179779,
            "SPY-USDT": -0.008508429404657713
          }
        },
        {
          "month": "2021-08-31 00:00:00+00:00",
          "portfolio_return": -0.04389147505951252,
          "contributions": {
            "BTC-USDT": -0.04389147505951241,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-03-31 00:00:00+00:00",
          "portfolio_return": -0.017075133975382628,
          "contributions": {
            "BTC-USDT": -0.007959605627139536,
            "PAXG-USDT": -0.009115528348243175,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-07-31 00:00:00+00:00",
          "portfolio_return": -0.014214382366409484,
          "contributions": {
            "BTC-USDT": -0.014093795852005573,
            "PAXG-USDT": -0.008662717044692032,
            "SPY-USDT": 0.008542130530287989
          }
        },
        {
          "month": "2024-06-30 00:00:00+00:00",
          "portfolio_return": -0.009943338559720405,
          "contributions": {
            "BTC-USDT": -0.009943338559720358,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-09-30 00:00:00+00:00",
          "portfolio_return": -0.009193175021420918,
          "contributions": {
            "BTC-USDT": 0,
            "PAXG-USDT": -0.009193175021420974,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2021-03-31 00:00:00+00:00",
          "portfolio_return": -0.008964226865126546,
          "contributions": {
            "BTC-USDT": -0.008964226865126518,
            "PAXG-USDT": 0,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2022-11-30 00:00:00+00:00",
          "portfolio_return": -0.00685293330300818,
          "contributions": {
            "BTC-USDT": 0.002643552775068677,
            "PAXG-USDT": 0,
            "SPY-USDT": -0.009496486078076932
          }
        },
        {
          "month": "2022-02-28 00:00:00+00:00",
          "portfolio_return": -0.006283439156724024,
          "contributions": {
            "BTC-USDT": 0.003128392411492799,
            "PAXG-USDT": -0.009411831568216934,
            "SPY-USDT": 0
          }
        },
        {
          "month": "2023-09-30 00:00:00+00:00",
          "portfolio_return": -0.0056638553360971455,
          "contributions": {
            "BTC-USDT": 0.0032742676462299268,
            "PAXG-USDT": -0.008938122982326973,
            "SPY-USDT": 0
          }
        }
      ],
      "daily_drawdown_episode": {
        "peak": "2021-03-13 00:00:00+00:00",
        "trough": "2021-06-17 00:00:00+00:00",
        "drawdown_pct": -8.227718310465637,
        "route_pnl_delta_USDT": {
          "BTC-USDT": -662.7152627390869,
          "PAXG-USDT": -205.86733675573072,
          "SPY-USDT": -96.59635326563487
        }
      }
    }
  },
  "comparisons": {
    "CONTROL__A": {
      "net_delta": 711.5780726772427,
      "fees_delta": 30.634049539136413,
      "plus10_delta": 677.5402398559809,
      "dd_engine_delta": 1.117048875956229,
      "by_symbol_closed_trade_net_delta": {
        "BTC-USDT": 5.4656238944489814,
        "PAXG-USDT": 718.6035920729187,
        "SPY-USDT": -12.491143290121158
      },
      "complete_months_positive_return_delta": 31,
      "limitation": "Capital, sizing and occupancy endogenous; not fixed-trade causal attribution."
    },
    "A__B": {
      "net_delta": 707.0250278010826,
      "fees_delta": -218.35363052466892,
      "plus10_delta": 949.6401728284891,
      "dd_engine_delta": -0.06910821830570235,
      "by_symbol_closed_trade_net_delta": {
        "BTC-USDT": 39.65466108450619,
        "PAXG-USDT": 12.414273756086004,
        "SPY-USDT": 654.9560929604821
      },
      "complete_months_positive_return_delta": 30,
      "limitation": "Capital, sizing and occupancy endogenous; not fixed-trade causal attribution."
    },
    "A__C": {
      "net_delta": 880.6568620348571,
      "fees_delta": -126.50704453225944,
      "plus10_delta": 1021.2202448484795,
      "dd_engine_delta": -0.740485868209495,
      "by_symbol_closed_trade_net_delta": {
        "BTC-USDT": -9.696434748984757,
        "PAXG-USDT": 63.890816991262,
        "SPY-USDT": 826.4624797925702
      },
      "complete_months_positive_return_delta": 34,
      "limitation": "Capital, sizing and occupancy endogenous; not fixed-trade causal attribution."
    },
    "B__C": {
      "net_delta": 173.6318342337745,
      "fees_delta": 91.84658599240947,
      "plus10_delta": 71.58007201999044,
      "dd_engine_delta": -0.6713776499037927,
      "by_symbol_closed_trade_net_delta": {
        "BTC-USDT": -49.351095833490945,
        "PAXG-USDT": 51.476543235175996,
        "SPY-USDT": 171.50638683208808
      },
      "complete_months_positive_return_delta": 27,
      "limitation": "Capital, sizing and occupancy endogenous; not fixed-trade causal attribution."
    }
  },
  "price_anchors": {
    "BTC-USDT": {
      "anchor_count": 25,
      "distinct_anchor_timestamps": 22,
      "scale": 1.1501999999999981,
      "max_relative_error": 1.3322676295501878e-15
    },
    "PAXG-USDT": {
      "anchor_count": 21,
      "distinct_anchor_timestamps": 15,
      "scale": 0.19228799999999985,
      "max_relative_error": 1.5543122344752192e-15
    },
    "SPY-USDT": {
      "anchor_count": 16,
      "distinct_anchor_timestamps": 16,
      "scale": 0.03484345999999995,
      "max_relative_error": 1.7763568394002505e-15
    }
  }
}
```
