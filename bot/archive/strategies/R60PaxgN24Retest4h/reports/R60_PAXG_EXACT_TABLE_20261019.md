# R60 PAXG: tabla exacta (10 nuevos + 2 referencias)

Todos finished. Stress5/10: recargos estáticos RT sobre TODOS los fills, sin resimulación. Exbest/ex3: ablaciones descriptivas. time_exposure_pct en porcentaje; entry_notional_time_proxy es fracción a precio de entrada, no MTM. Cohortes por cierre NO son años MTM. MTM_root: campos exactos de strategies/MultiAssetRetestBtcShort4h/reports/R60_MTM_RESULTS_20261019.md; referencias reutilizadas sin nuevas corridas. Doce caminos económicos y curvas almacenadas únicos, no independientes.

```json
{
  "rows": [
    {
      "id": "Cq",
      "name": "AttrPaxgCqFreshRetest4h",
      "session_id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
      "dashboard_url": "http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
      "reference": true,
      "N": 35,
      "net": 546.1105723537391,
      "before_fees": 792.719453408573,
      "fees": 246.60888105483386,
      "PF": 1.308334734611165,
      "DD_engine": -6.919378335744097,
      "CAGR_engine": 1.0250706618597727,
      "Sharpe_engine": 0.23075746266424707,
      "time_exposure_pct": 13.357126175045252,
      "entry_notional_time_proxy": 0.10379673439549729,
      "entry_notional_sum": 273613.508112,
      "executed_fill_notional_sum": 548019.7356774086,
      "net_bps_entry_notional": 19.95919631753693,
      "mean_hold_hours": 174.29904761904763,
      "max_hold_hours": 916.75,
      "stress5": 409.10563843438695,
      "stress10": 272.1007045150348,
      "exbest": -91.38798046904276,
      "ex3": -920.5473327487769,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 836.9602960810497,
      "recent2023_25_stress10": 620.9229186951853,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "cash_before_first_fill_hours": 1764.0333333333333,
      "fill_sha256": "ba98ce176d8da1221aa363cb4b4e1c3f588655222cbadb8a424738012d43c6e5",
      "curve_sha256": "69451990cb5679d4ecec251a5155fc7ada6b6e4200eb48776aa7c38ada449ef8",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0516032489249483e-12,
        "max_qty_error": 0,
        "wallet_error": 0,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 35,
          "exit_STOP": 35
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 15,
          "win_months_all": 0.2459016393442623,
          "win_months_active": 0.4838709677419355,
          "quarters_total": 19,
          "positive_quarters": 8,
          "win_quarters": 0.42105263157894735
        },
        "daily_close_drawdown_pct": -6.921781413307038,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.002430923667209983,
          "2021-12-31 00:00:00+00:00": -0.02274690715946248,
          "2022-12-31 00:00:00+00:00": -0.008894893241745416,
          "2023-12-31 00:00:00+00:00": -0.005746087470991701,
          "2024-12-31 00:00:00+00:00": 0.051329013324179495,
          "2025-12-31 00:00:00+00:00": 0.03914257549642297
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "M",
      "name": "AttrPaxgMMarketSignal4h",
      "session_id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
      "dashboard_url": "http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
      "reference": true,
      "N": 38,
      "net": 962.1262139358278,
      "before_fees": 1229.8443971885627,
      "fees": 267.71818325273483,
      "PF": 1.5743577329815752,
      "DD_engine": -7.64796155547669,
      "CAGR_engine": 1.777532757709932,
      "Sharpe_engine": 0.3772629743596269,
      "time_exposure_pct": 15.204866584924389,
      "entry_notional_time_proxy": 0.117065150055092,
      "entry_notional_sum": 296849.72586,
      "executed_fill_notional_sum": 594929.2961171885,
      "net_bps_entry_notional": 32.41122123823637,
      "mean_hold_hours": 182.74649122807014,
      "max_hold_hours": 917.4833333333333,
      "stress5": 813.3938899065306,
      "stress10": 664.6615658772334,
      "exbest": 337.4547898331979,
      "ex3": -635.127505102286,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 1275.647506856833,
      "recent2023_25_stress10": 1036.1902609127296,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "cash_before_first_fill_hours": 1764,
      "fill_sha256": "b1ebbbb575b72b65420f9c3a149b3fa44a7c1cb4d0ccdec729a448a6e6260259",
      "curve_sha256": "e2304db4dc37a23b920761b990d264d44e22acf25c6d376e333060c234570fe5",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0800249583553523e-12,
        "max_qty_error": 0,
        "wallet_error": -1.0913936421275139e-11,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 38,
          "exit_STOP": 38
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 17,
          "win_months_all": 0.2786885245901639,
          "win_months_active": 0.5483870967741935,
          "quarters_total": 19,
          "positive_quarters": 10,
          "win_quarters": 0.5263157894736842
        },
        "daily_close_drawdown_pct": -7.65034683398127,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.0018925338842750161,
          "2021-12-31 00:00:00+00:00": -0.024064578119711633,
          "2022-12-31 00:00:00+00:00": -0.009342100970716194,
          "2023-12-31 00:00:00+00:00": -0.015437450362151273,
          "2024-12-31 00:00:00+00:00": 0.07348604181087892,
          "2025-12-31 00:00:00+00:00": 0.0707526450013436
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P1_Cq",
      "name": "R60PaxgN24Retest4h",
      "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
      "dashboard_url": "http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26",
      "reference": false,
      "N": 36,
      "net": 960.0415136226013,
      "before_fees": 1220.456290125658,
      "fees": 260.41477650305654,
      "PF": 1.5382710146147627,
      "DD_engine": -6.919378335744097,
      "CAGR_engine": 1.773820071833243,
      "Sharpe_engine": 0.3655840693972553,
      "time_exposure_pct": 13.788134232498397,
      "entry_notional_time_proxy": 0.10979084109488528,
      "entry_notional_sum": 288739.523525,
      "executed_fill_notional_sum": 578699.5033401257,
      "net_bps_entry_notional": 33.2493973080716,
      "mean_hold_hours": 174.925462962963,
      "max_hold_hours": 916.75,
      "stress5": 815.3666377875699,
      "stress10": 670.6917619525384,
      "exbest": 322.5429607998194,
      "ex3": -717.8704338634134,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 1250.8912373499118,
      "recent2023_25_stress10": 1019.5139761326894,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "cash_before_first_fill_hours": 1764.0333333333333,
      "fill_sha256": "b869fcbe888482d2db40184e1a118dae92ed7b4e2cdb27711a4290aba73bec9b",
      "curve_sha256": "d304c27aac67f44f3e27409f64baa0fed9cd27fc843e619402ba3769e1f78610",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.1084466677857563e-12,
        "max_qty_error": 0,
        "wallet_error": -7.275957614183426e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 36,
          "exit_STOP": 36
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 16,
          "win_months_all": 0.26229508196721313,
          "win_months_active": 0.5161290322580645,
          "quarters_total": 19,
          "positive_quarters": 9,
          "win_quarters": 0.47368421052631576
        },
        "daily_close_drawdown_pct": -6.921781413307038,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.002430923667209983,
          "2021-12-31 00:00:00+00:00": -0.02274690715946248,
          "2022-12-31 00:00:00+00:00": -0.008894893241745416,
          "2023-12-31 00:00:00+00:00": -0.005746087470991701,
          "2024-12-31 00:00:00+00:00": 0.051329013324179495,
          "2025-12-31 00:00:00+00:00": 0.0799285374334584
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P1_M",
      "name": "R60PaxgN24Market4h",
      "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
      "dashboard_url": "http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb",
      "reference": false,
      "N": 39,
      "net": 1385.701717983873,
      "before_fees": 1668.1130383831455,
      "fees": 282.4113203992724,
      "PF": 1.8194081220776872,
      "DD_engine": -7.64796155547669,
      "CAGR_engine": 2.520318386957743,
      "Sharpe_engine": 0.5028090084653423,
      "time_exposure_pct": 15.637626262626265,
      "entry_notional_time_proxy": 0.12339548495087554,
      "entry_notional_sum": 312956.29948,
      "executed_fill_notional_sum": 627580.7119983832,
      "net_bps_entry_notional": 44.27780237324888,
      "mean_hold_hours": 183.12863247863248,
      "max_hold_hours": 917.4833333333333,
      "stress5": 1228.8065399842774,
      "stress10": 1071.9113619846814,
      "exbest": 761.0302938812432,
      "ex3": -266.73933747127967,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 1699.2230109048787,
      "recent2023_25_stress10": 1443.4400570201776,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "cash_before_first_fill_hours": 1764,
      "fill_sha256": "e6d0e73c7cf5abbd4db8a9f3a0bb89aa2cba2b3246519eed4e4ca6fbbbd4998f",
      "curve_sha256": "5caf6e46644e01dc962c88c5ca1036969bb3eb472b0a19dc3fdeb32f63130286",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0800249583553523e-12,
        "max_qty_error": 0,
        "wallet_error": -7.275957614183426e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 39,
          "exit_STOP": 39
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 17,
          "win_months_all": 0.2786885245901639,
          "win_months_active": 0.5483870967741935,
          "quarters_total": 19,
          "positive_quarters": 10,
          "win_quarters": 0.5263157894736842
        },
        "daily_close_drawdown_pct": -7.65034683398127,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.0018925338842750161,
          "2021-12-31 00:00:00+00:00": -0.024064578119711633,
          "2022-12-31 00:00:00+00:00": -0.009342100970716194,
          "2023-12-31 00:00:00+00:00": -0.015437450362151273,
          "2024-12-31 00:00:00+00:00": 0.07348604181087892,
          "2025-12-31 00:00:00+00:00": 0.11212642436365794
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P2_Cq",
      "name": "R60PaxgN28Retest4h",
      "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
      "dashboard_url": "http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936",
      "reference": false,
      "N": 35,
      "net": 262.207451889136,
      "before_fees": 503.55770248925614,
      "fees": 241.35025060012018,
      "PF": 1.1437380198190137,
      "DD_engine": -9.106780300664042,
      "CAGR_engine": 0.4976741004134366,
      "Sharpe_engine": 0.12787878979034237,
      "time_exposure_pct": 12.241526537046772,
      "entry_notional_time_proxy": 0.08873390864561433,
      "entry_notional_sum": 267915.16626,
      "executed_fill_notional_sum": 536333.8902224893,
      "net_bps_entry_notional": 9.78695814609745,
      "mean_hold_hours": 159.7414285714286,
      "max_hold_hours": 916.75,
      "stress5": 128.1239793335137,
      "stress10": -5.95949322210862,
      "exbest": -358.25538890520136,
      "ex3": -1165.2296933807784,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 553.0571756164469,
      "recent2023_25_stress10": 342.86272095804213,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "cash_before_first_fill_hours": 1764.0333333333333,
      "fill_sha256": "51797f4e6d6b08b74c8e384a9b68190e6307c036e1b67cd9a5722dd07ab4ac76",
      "curve_sha256": "5f50d98fd2e5da089b77990043f238fc76236a71c243254e3288fd4daf4f33e8",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.4210854715202004e-12,
        "max_qty_error": 0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 35,
          "exit_STOP": 35
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 14,
          "win_months_all": 0.22950819672131148,
          "win_months_active": 0.45161290322580644,
          "quarters_total": 19,
          "positive_quarters": 7,
          "win_quarters": 0.3684210526315789
        },
        "daily_close_drawdown_pct": -9.109126905714259,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.002430923667209983,
          "2021-12-31 00:00:00+00:00": -0.02274690715946248,
          "2022-12-31 00:00:00+00:00": -0.008894893241745416,
          "2023-12-31 00:00:00+00:00": -0.03230694618044805,
          "2024-12-31 00:00:00+00:00": 0.0513284394058644,
          "2025-12-31 00:00:00+00:00": 0.03892340534937899
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P2_M",
      "name": "R60PaxgN28Market4h",
      "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
      "dashboard_url": "http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
      "reference": false,
      "N": 38,
      "net": 671.5315157024731,
      "before_fees": 934.2085615803843,
      "fees": 262.67704587791116,
      "PF": 1.3880104453725206,
      "DD_engine": -10.069493774953775,
      "CAGR_engine": 1.2544127318831366,
      "Sharpe_engine": 0.28133814630238096,
      "time_exposure_pct": 14.070437029252062,
      "entry_notional_time_proxy": 0.10211824076675384,
      "entry_notional_sum": 291396.280028,
      "executed_fill_notional_sum": 583726.7686175804,
      "net_bps_entry_notional": 23.045301595406308,
      "mean_hold_hours": 169.11184210526315,
      "max_hold_hours": 917.4833333333333,
      "stress5": 525.599823548078,
      "stress10": 379.6681313936829,
      "exbest": 63.24231060321131,
      "ex3": -883.844839662783,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 985.0528086234785,
      "recent2023_25_stress10": 751.1968264291792,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "cash_before_first_fill_hours": 1764,
      "fill_sha256": "4df36381d2681564dda83f9b0e36345e9a3e858d9f1001ddf005970e52c43717",
      "curve_sha256": "fa2fcc6f6bf5b220ac69a4f4232f1430f1068728643226e775b3c06c15057221",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.3073986337985843e-12,
        "max_qty_error": 0,
        "wallet_error": 0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 38,
          "exit_STOP": 38
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 16,
          "win_months_all": 0.26229508196721313,
          "win_months_active": 0.5161290322580645,
          "quarters_total": 19,
          "positive_quarters": 10,
          "win_quarters": 0.5263157894736842
        },
        "daily_close_drawdown_pct": -10.071816509860465,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.0018925338842750161,
          "2021-12-31 00:00:00+00:00": -0.024064578119711633,
          "2022-12-31 00:00:00+00:00": -0.009342100970716194,
          "2023-12-31 00:00:00+00:00": -0.041253333654970636,
          "2024-12-31 00:00:00+00:00": 0.07348663884749462,
          "2025-12-31 00:00:00+00:00": 0.07043502995467077
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P3_Cq",
      "name": "R60PaxgAdx24Retest4h",
      "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
      "dashboard_url": "http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248",
      "reference": false,
      "N": 41,
      "net": 324.50220242582566,
      "before_fees": 610.7933143282734,
      "fees": 286.2911119024477,
      "PF": 1.1589347242023043,
      "DD_engine": -8.302396935878553,
      "CAGR_engine": 0.6143975204656593,
      "Sharpe_engine": 0.14487194173342102,
      "time_exposure_pct": 15.444765574823382,
      "entry_notional_time_proxy": 0.1198653440549888,
      "entry_notional_sum": 317795.83879,
      "executed_fill_notional_sum": 636202.4708943283,
      "net_bps_entry_notional": 10.211027421295382,
      "mean_hold_hours": 172.04715447154473,
      "max_hold_hours": 916.75,
      "stress5": 165.45158470224357,
      "stress10": 6.400966978661472,
      "exbest": -305.71080741499827,
      "ex3": -1125.39603669719,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 820.9621919737715,
      "recent2023_25_stress10": 582.9666331803269,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "cash_before_first_fill_hours": 1764.0333333333333,
      "fill_sha256": "e7568fb144ffd4c141b1920183771d380a8c669f1a20ae2ca3eb3659e92c501b",
      "curve_sha256": "c4673ad12d93c5a18741256e5a4a8e1dae471251e473ba7c2a36a0e1d50396de",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 9.094947017729282e-13,
        "max_qty_error": 0,
        "wallet_error": 3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 40,
          "exit_STOP": 41,
          "entry_MARKET": 1
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 38,
          "positive_months": 16,
          "win_months_all": 0.26229508196721313,
          "win_months_active": 0.42105263157894735,
          "quarters_total": 19,
          "positive_quarters": 7,
          "win_quarters": 0.3684210526315789
        },
        "daily_close_drawdown_pct": -8.304764307824941,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.002430923667209761,
          "2021-12-31 00:00:00+00:00": -0.03450444787795903,
          "2022-12-31 00:00:00+00:00": -0.018069670728712794,
          "2023-12-31 00:00:00+00:00": 0.00415707077428773,
          "2024-12-31 00:00:00+00:00": 0.05132846183058626,
          "2025-12-31 00:00:00+00:00": 0.029066975540072315
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P3_M",
      "name": "R60PaxgAdx24Market4h",
      "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
      "dashboard_url": "http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c",
      "reference": false,
      "N": 46,
      "net": 467.9807271498951,
      "before_fees": 785.6404231091942,
      "fees": 317.65969595929914,
      "PF": 1.213754179173589,
      "DD_engine": -10.379926008484453,
      "CAGR_engine": 0.8810874299219007,
      "Sharpe_engine": 0.19368089130092866,
      "time_exposure_pct": 17.154055000875815,
      "entry_notional_time_proxy": 0.1300939430837091,
      "entry_notional_sum": 352562.397521,
      "executed_fill_notional_sum": 705910.4354651092,
      "net_bps_entry_notional": 13.27369936330264,
      "mean_hold_hours": 170.3173913043478,
      "max_hold_hours": 917.4833333333333,
      "stress5": 291.50311828361777,
      "stress10": 115.02550941734046,
      "exbest": -136.977933941458,
      "ex3": -1078.8795398290906,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 970.4238024193394,
      "recent2023_25_stress10": 697.8999353869651,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "cash_before_first_fill_hours": 1764,
      "fill_sha256": "5da1e54aa3895416aea02ebce0d90c436326f87aaf933e263a6e5bed8d2f846b",
      "curve_sha256": "7446ff6e627affe880c33ea5acf0eaaff23ffec352f34e3fa3bd789e0a325253",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.3642420526593924e-12,
        "max_qty_error": 0,
        "wallet_error": 0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 46,
          "exit_STOP": 46
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 39,
          "positive_months": 17,
          "win_months_all": 0.2786885245901639,
          "win_months_active": 0.4358974358974359,
          "quarters_total": 19,
          "positive_quarters": 7,
          "win_quarters": 0.3684210526315789
        },
        "daily_close_drawdown_pct": -10.382240725513636,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.001892533884274794,
          "2021-12-31 00:00:00+00:00": -0.034158177515287824,
          "2022-12-31 00:00:00+00:00": -0.018512533963294664,
          "2023-12-31 00:00:00+00:00": -0.027534095138975534,
          "2024-12-31 00:00:00+00:00": 0.07348655807322912,
          "2025-12-31 00:00:00+00:00": 0.055796006050243596
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P4_Cq",
      "name": "R60PaxgAdx28Retest4h",
      "session_id": "2c562667-f6cc-498b-932b-2983bc41b7dd",
      "dashboard_url": "http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd",
      "reference": false,
      "N": 32,
      "net": 127.95384526532453,
      "before_fees": 344.1116527029409,
      "fees": 216.15780743761633,
      "PF": 1.0742084531174207,
      "DD_engine": -9.15661198500345,
      "CAGR_engine": 0.24415930646946027,
      "Sharpe_engine": 0.07571707467587487,
      "time_exposure_pct": 10.781842996438378,
      "entry_notional_time_proxy": 0.07775149397424388,
      "entry_notional_sum": 240003.28577100002,
      "executed_fill_notional_sum": 480350.68319470296,
      "net_bps_entry_notional": 5.331337229583271,
      "mean_hold_hours": 153.88385416666665,
      "max_hold_hours": 893.7333333333333,
      "stress5": 7.866174466648786,
      "stress10": -112.22149633202696,
      "exbest": -471.8434571438979,
      "ex3": -1188.4518360315699,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 509.546130488161,
      "recent2023_25_stress10": 320.0280467082159,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "cash_before_first_fill_hours": 1764.0333333333333,
      "fill_sha256": "b186c6a17e1066fd57e81b503954c62140e1b2303e913e027cef0f7d3e99229c",
      "curve_sha256": "8deb3c8cf24acd2c15a62c74657288aaf7dc9a133dbeee2e51196157c9980b21",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0231815394945443e-12,
        "max_qty_error": 0,
        "wallet_error": 0,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 32,
          "exit_STOP": 32
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 29,
          "positive_months": 12,
          "win_months_all": 0.19672131147540983,
          "win_months_active": 0.41379310344827586,
          "quarters_total": 19,
          "positive_quarters": 6,
          "win_quarters": 0.3157894736842105
        },
        "daily_close_drawdown_pct": -9.158957303540971,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.002430923667209761,
          "2021-12-31 00:00:00+00:00": -0.0318802152976434,
          "2022-12-31 00:00:00+00:00": -0.008895081732313237,
          "2023-12-31 00:00:00+00:00": -0.02371299557340034,
          "2024-12-31 00:00:00+00:00": 0.040609382974877706,
          "2025-12-31 00:00:00+00:00": 0.0364617639651299
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P4_M",
      "name": "R60PaxgAdx28Market4h",
      "session_id": "ac0ed1df-254d-4d7d-9fc1-ce5656107504",
      "dashboard_url": "http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504",
      "reference": false,
      "N": 35,
      "net": 469.4248632579352,
      "before_fees": 705.3955937087042,
      "fees": 235.9707304507689,
      "PF": 1.2736454475843284,
      "DD_engine": -10.016952972445935,
      "CAGR_engine": 0.883756652770451,
      "Sharpe_engine": 0.21055217953357508,
      "time_exposure_pct": 12.12770771296783,
      "entry_notional_time_proxy": 0.0869766777006371,
      "entry_notional_sum": 261837.002704,
      "executed_fill_notional_sum": 524379.4010017087,
      "net_bps_entry_notional": 17.928133090822456,
      "mean_hold_hours": 158.25619047619048,
      "max_hold_hours": 894.5,
      "stress5": 338.330013007508,
      "stress10": 207.23516275708084,
      "exbest": -134.5701378920432,
      "ex3": -999.5568610914547,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 862.5959994802274,
      "recent2023_25_stress10": 651.1209529355422,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "cash_before_first_fill_hours": 1764,
      "fill_sha256": "d72e41f85104e04aeeda20ee1d924592d8c2e35d5694cfc4c6b19e38ec1c99ae",
      "curve_sha256": "04fb51bd5f75c57cebe988d6fd7de53a98faa0504e7a947ef7d675f3c1e599ac",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.3358203432289883e-12,
        "max_qty_error": 0,
        "wallet_error": 0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 35,
          "exit_STOP": 35
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 30,
          "positive_months": 15,
          "win_months_all": 0.2459016393442623,
          "win_months_active": 0.5,
          "quarters_total": 19,
          "positive_quarters": 9,
          "win_quarters": 0.47368421052631576
        },
        "daily_close_drawdown_pct": -10.019277064382148,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.001892533884274794,
          "2021-12-31 00:00:00+00:00": -0.03208931732066089,
          "2022-12-31 00:00:00+00:00": -0.009342274049184418,
          "2023-12-31 00:00:00+00:00": -0.032739591985538996,
          "2024-12-31 00:00:00+00:00": 0.0652743226055601,
          "2025-12-31 00:00:00+00:00": 0.05764007845913155
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P5_Cq",
      "name": "R60PaxgFast24Retest4h",
      "session_id": "9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
      "dashboard_url": "http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
      "reference": false,
      "N": 35,
      "net": 532.9256826889153,
      "before_fees": 779.4018243515736,
      "fees": 246.47614166265822,
      "PF": 1.3011636743164046,
      "DD_engine": -7.052402092339594,
      "CAGR_engine": 1.0008332111861806,
      "Sharpe_engine": 0.225863618840498,
      "time_exposure_pct": 13.348258597536056,
      "entry_notional_time_proxy": 0.10368878080407197,
      "entry_notional_sum": 273472.67871300003,
      "executed_fill_notional_sum": 547724.7592503516,
      "net_bps_entry_notional": 19.487346421475696,
      "mean_hold_hours": 174.18333333333334,
      "max_hold_hours": 916.75,
      "stress5": 395.99449287632746,
      "stress10": 259.06330306373957,
      "exbest": -103.76035604665935,
      "ex3": -931.8938201030231,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 835.9026908566848,
      "recent2023_25_stress10": 620.1348256529146,
      "first_entry_UTC": "2020-12-27T12:02:00+00:00",
      "cash_before_first_fill_hours": 1764.0333333333333,
      "fill_sha256": "75559c623db30f35f646411bf8cc6a0afd8b6063a3943e7464ab1c60a00f30ad",
      "curve_sha256": "b09a8d7007f95fc72436470fa0b62768d76fa697b8c8cc1595b014a354b74f37",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0231815394945443e-12,
        "max_qty_error": 0,
        "wallet_error": -1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 35,
          "exit_STOP": 35
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 15,
          "win_months_all": 0.2459016393442623,
          "win_months_active": 0.4838709677419355,
          "quarters_total": 19,
          "positive_quarters": 8,
          "win_quarters": 0.42105263157894735
        },
        "daily_close_drawdown_pct": -7.054801735606542,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.002430923667209761,
          "2021-12-31 00:00:00+00:00": -0.02274690715946226,
          "2022-12-31 00:00:00+00:00": -0.010132840250292707,
          "2023-12-31 00:00:00+00:00": -0.005746246263316768,
          "2024-12-31 00:00:00+00:00": 0.051326740371807844,
          "2025-12-31 00:00:00+00:00": 0.03914378505791105
        },
        "terminal_reconciles": true
      }
    },
    {
      "id": "P5_M",
      "name": "R60PaxgFast24Market4h",
      "session_id": "09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
      "dashboard_url": "http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
      "reference": false,
      "N": 38,
      "net": 948.339108895103,
      "before_fees": 1215.89699552669,
      "fees": 267.557886631587,
      "PF": 1.5666292344865935,
      "DD_engine": -7.7639248506052745,
      "CAGR_engine": 1.7529684167542303,
      "Sharpe_engine": 0.3723356919327944,
      "time_exposure_pct": 15.19610848368074,
      "entry_notional_time_proxy": 0.11694084284763914,
      "entry_notional_sum": 296678.59220400004,
      "executed_fill_notional_sum": 594573.0814035267,
      "net_bps_entry_notional": 31.965201865425218,
      "mean_hold_hours": 182.64122807017543,
      "max_hold_hours": 917.4833333333333,
      "stress5": 799.6958385442213,
      "stress10": 651.0525681933395,
      "exbest": 324.4622815862381,
      "ex3": -646.900003987193,
      "cohorts_closed_not_MTM": {
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
      "recent2023_25": 1274.0243880633645,
      "recent2023_25_stress10": 1034.866898024815,
      "first_entry_UTC": "2020-12-27T12:00:00+00:00",
      "cash_before_first_fill_hours": 1764,
      "fill_sha256": "3e7704e04cd233c902f869a7bd095ed32d44e95d62eb4ccb0f27feb9e7146845",
      "curve_sha256": "e21dd70aea3e8e90fe1e762c5b8ac3d462ca2bebb781266ece202468763feff3",
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.3073986337985843e-12,
        "max_qty_error": 0,
        "wallet_error": 0,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 38,
          "exit_STOP": 38
        }
      },
      "MTM_root": {
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "complete_periods": {
          "months_total": 61,
          "months_active": 31,
          "positive_months": 17,
          "win_months_all": 0.2786885245901639,
          "win_months_active": 0.5483870967741935,
          "quarters_total": 19,
          "positive_quarters": 10,
          "win_quarters": 0.5263157894736842
        },
        "daily_close_drawdown_pct": -7.766307133997263,
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.001892533884274794,
          "2021-12-31 00:00:00+00:00": -0.02406457811971141,
          "2022-12-31 00:00:00+00:00": -0.01058613912162032,
          "2023-12-31 00:00:00+00:00": -0.015437340546487266,
          "2024-12-31 00:00:00+00:00": 0.07348592165460688,
          "2025-12-31 00:00:00+00:00": 0.07075057212184643
        },
        "terminal_reconciles": true
      }
    }
  ],
  "pair_deltas": [
    {
      "context": "Center",
      "delta_net": 416.0156415820886,
      "delta_stress5": 404.28825147214366,
      "delta_stress10": 392.56086136219864,
      "delta_time_pct": 1.8477404098791368,
      "delta_notional_time": 0.013268415659594704,
      "delta_net_bps_entry_notional": 12.452024920699444,
      "delta_DD_engine": -0.7285832197325925,
      "delta_recent2023_25": 438.6872107757832,
      "cohort_deltas": {
        "2021": -18.463077777168394,
        "2022": -4.208491416526243,
        "2023": -93.74490746810318,
        "2024": 205.33480083227124,
        "2025": 327.0973174116154
      }
    },
    {
      "context": "P1",
      "delta_net": 425.6602043612718,
      "delta_stress5": 413.4399021967075,
      "delta_stress10": 401.21960003214303,
      "delta_time_pct": 1.849492030127868,
      "delta_notional_time": 0.013604643855990264,
      "delta_net_bps_entry_notional": 11.028405065177282,
      "delta_DD_engine": -0.7285832197325925,
      "delta_recent2023_25": 448.33177355496696,
      "cohort_deltas": {
        "2021": -18.463077777168394,
        "2022": -4.208491416526243,
        "2023": -93.74490746810318,
        "2024": 205.33480083227124,
        "2025": 336.74188019079884
      }
    },
    {
      "context": "P2",
      "delta_net": 409.32406381333715,
      "delta_stress5": 397.4758442145643,
      "delta_stress10": 385.62762461579155,
      "delta_time_pct": 1.8289104922052903,
      "delta_notional_time": 0.013384332121139514,
      "delta_net_bps_entry_notional": 13.258343449308857,
      "delta_DD_engine": -0.9627134742897336,
      "delta_recent2023_25": 431.99563300703164,
      "cohort_deltas": {
        "2021": -18.463077777168394,
        "2022": -4.208491416526243,
        "2023": -85.92654261147226,
        "2024": 200.2063492163959,
        "2025": 317.71582640210795
      }
    },
    {
      "context": "P3",
      "delta_net": 143.47852472406942,
      "delta_stress5": 126.0515335813742,
      "delta_stress10": 108.62454243867899,
      "delta_time_pct": 1.7092894260524325,
      "delta_notional_time": 0.010228599028720309,
      "delta_net_bps_entry_notional": 3.062671942007258,
      "delta_DD_engine": -2.0775290726059,
      "delta_recent2023_25": 149.46161044556789,
      "cohort_deltas": {
        "2021": -1.728872496658937,
        "2022": -4.2542132248398445,
        "2023": -301.013524383085,
        "2024": 188.8956274167432,
        "2025": 261.57950741191
      }
    },
    {
      "context": "P4",
      "delta_net": 341.47101799261065,
      "delta_stress5": 330.46383854085923,
      "delta_stress10": 319.4566590891078,
      "delta_time_pct": 1.3458647165294515,
      "delta_notional_time": 0.009225183726393221,
      "delta_net_bps_entry_notional": 12.596795861239185,
      "delta_DD_engine": -0.8603409874424859,
      "delta_recent2023_25": 353.0498689920664,
      "cohort_deltas": {
        "2021": -7.307235564222765,
        "2022": -4.271615435232945,
        "2023": -86.44239771131893,
        "2024": 225.21356451969723,
        "2025": 214.27870218368815
      }
    },
    {
      "context": "P5",
      "delta_net": 415.41342620618764,
      "delta_stress5": 403.7013456678938,
      "delta_stress10": 391.98926512959997,
      "delta_time_pct": 1.8478498861446848,
      "delta_notional_time": 0.013252062043567173,
      "delta_net_bps_entry_notional": 12.477855443949522,
      "delta_DD_engine": -0.7115227582656809,
      "delta_recent2023_25": 438.12169720667976,
      "cohort_deltas": {
        "2021": -18.463077777168394,
        "2022": -4.245193223323341,
        "2023": -93.62420876725817,
        "2024": 205.0945484614707,
        "2025": 326.65135751246703
      }
    }
  ]
}
```