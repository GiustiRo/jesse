# Atribución PAXG: tabla exacta de17 configuraciones

Valores sin redondeo de auditorías completas de snapshots; calendario añadido desde informe MTM root leído completo, con identidad de sesiones comprobada. Un bloque JSON para ingestión. control identifica el contraste primario y reference el comparador conservado. DDmotor y daily_close_drawdown_pct permanecen separados. Ex3 excluye tres mejores PnL incluso pérdidas; E3 sólo tiene una ganadora. Cohortes de cierre NO son MTM; mtm_complete contiene períodos completos. No sumar curvas o N como muestra independiente.

```json
{
  "schema": "ATTRIBUTION_PAXG_EXACT_V1",
  "window": {
    "start": "2020-10-15",
    "finish_exclusive": "2025-12-31"
  },
  "capital": 10000,
  "fee_per_side": 0.00045,
  "leverage": 5,
  "mode": "isolated",
  "units": {
    "net": "USDT",
    "fees": "USDT",
    "before_fees": "USDT",
    "DDmotor": "percent",
    "CAGR": "percent",
    "timeexposure": "percent of entire window",
    "entrynotionaltime": "sum(entry_notional*holding_hours)/(10000*window_hours), entry-price approximation, not MTM",
    "stress5": "USDT net after extra2.5bps per fill side",
    "stress10": "USDT net after extra5bps per fill side",
    "exbest": "USDT net excluding best net-PNL trade",
    "ex3": "USDT net excluding three highest net-PNL trades, even if one or more are losses",
    "cohorts": "By trade closing year, NOT MTM annual returns"
  },
  "interpretation": "All17predeclared paths; seeds not selected. N across policies is not an independent sample. Shared entries and capital/occupancy are endogenous.",
  "rows": [
    {
      "id": "C0",
      "control": "historical_93a16137-e819-41a3-b325-0631a6627a6c",
      "reference": "C0",
      "name": "AttrPaxgC0Retest4h",
      "session_id": "69c90bb0-e2b4-4c6a-a562-edd95399e673",
      "dashboard_url": "http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673",
      "net": 546.1105723537391,
      "fees": 246.60888105483386,
      "before_fees": 792.719453408573,
      "PF": 1.308334734611165,
      "DDmotor": -6.919378335744097,
      "CAGR": 1.0250706618597727,
      "N": 35,
      "timeexposure": 13.357126175045252,
      "entrynotionaltime": 0.10379673439549729,
      "entry_notional_hours": 47406044.53311152,
      "entry_notional_sum": 273613.508112,
      "net_bps_entry_notional": 19.95919631753693,
      "stress5": 409.10563843438695,
      "stress10": 272.1007045150348,
      "exbest": -91.38798046904276,
      "ex3": -920.5473327487769,
      "best_trade_net": 637.4985528227819,
      "winning_trades": 14,
      "mean_holding_hours": 174.29904761904763,
      "max_holding_hours": 916.75,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 836.9602960810497,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
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
      "mtm_complete": {
        "months_total": 61,
        "months_active": 31,
        "positive_months": 15,
        "win_months_all": 0.2459016393442623,
        "win_months_active": 0.4838709677419355,
        "quarters_total": 19,
        "positive_quarters": 8,
        "win_quarters": 0.42105263157894735
      },
      "daily_close_drawdown_pct": -6.921781413307038
    },
    {
      "id": "Cq",
      "control": "C0",
      "reference": "C0",
      "name": "AttrPaxgCqFreshRetest4h",
      "session_id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
      "dashboard_url": "http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
      "net": 546.1105723537391,
      "fees": 246.60888105483386,
      "before_fees": 792.719453408573,
      "PF": 1.308334734611165,
      "DDmotor": -6.919378335744097,
      "CAGR": 1.0250706618597727,
      "N": 35,
      "timeexposure": 13.357126175045252,
      "entrynotionaltime": 0.10379673439549729,
      "entry_notional_hours": 47406044.53311152,
      "entry_notional_sum": 273613.508112,
      "net_bps_entry_notional": 19.95919631753693,
      "stress5": 409.10563843438695,
      "stress10": 272.1007045150348,
      "exbest": -91.38798046904276,
      "ex3": -920.5473327487769,
      "best_trade_net": 637.4985528227819,
      "winning_trades": 14,
      "mean_holding_hours": 174.29904761904763,
      "max_holding_hours": 916.75,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 836.9602960810497,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
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
      "mtm_complete": {
        "months_total": 61,
        "months_active": 31,
        "positive_months": 15,
        "win_months_all": 0.2459016393442623,
        "win_months_active": 0.4838709677419355,
        "quarters_total": 19,
        "positive_quarters": 8,
        "win_quarters": 0.42105263157894735
      },
      "daily_close_drawdown_pct": -6.921781413307038
    },
    {
      "id": "E1",
      "control": "C0",
      "reference": "C0",
      "name": "AttrPaxgE1NoBe4h",
      "session_id": "4cc65389-4537-4e5a-a4f2-1b008214bb1b",
      "dashboard_url": "http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b",
      "net": 491.1691478843695,
      "fees": 245.3273484058306,
      "before_fees": 736.4964962902002,
      "PF": 1.270951168600716,
      "DDmotor": -7.404302414804742,
      "CAGR": 0.9239110792804706,
      "N": 35,
      "timeexposure": 13.363366322181355,
      "entrynotionaltime": 0.10331003816313365,
      "entry_notional_hours": 47183760.6298664,
      "entry_notional_sum": 272217.694425,
      "net_bps_entry_notional": 18.043248398009407,
      "stress5": 354.87617654779694,
      "stress10": 218.58320521122442,
      "exbest": -142.99809718086283,
      "ex3": -967.8437403488713,
      "best_trade_net": 634.1672450652324,
      "winning_trades": 13,
      "mean_holding_hours": 174.3804761904762,
      "max_holding_hours": 916.75,
      "cohorts": {
        "2021": {
          "n": 6,
          "net": -254.74539878840773,
          "static_5bps_RT": -273.82155362488703,
          "static_10bps_RT": -292.89770846136634
        },
        "2022": {
          "n": 3,
          "net": -86.68397531134114,
          "static_5bps_RT": -96.44502243872063,
          "static_10bps_RT": -106.20606956610011
        },
        "2023": {
          "n": 5,
          "net": -55.49970966668191,
          "static_5bps_RT": -80.05236078226726,
          "static_10bps_RT": -104.60501189785259
        },
        "2024": {
          "n": 7,
          "net": 492.90486536892405,
          "static_5bps_RT": 468.42361889166705,
          "static_10bps_RT": 443.94237241441004
        },
        "2025": {
          "n": 14,
          "net": 395.19336628187614,
          "static_5bps_RT": 336.7714945020047,
          "static_10bps_RT": 278.3496227221333
        }
      },
      "recent_closed_cohort_2023_2025": 832.598521984118,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.2789769243681803e-12,
        "max_qty_error": 0,
        "wallet_error": -1.0913936421275139e-11,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 35,
          "exit_STOP": 35
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 31,
        "positive_months": 15,
        "win_months_all": 0.2459016393442623,
        "win_months_active": 0.4838709677419355,
        "quarters_total": 19,
        "positive_quarters": 8,
        "win_quarters": 0.42105263157894735
      },
      "daily_close_drawdown_pct": -7.406692973003759
    },
    {
      "id": "E2",
      "control": "C0",
      "reference": "C0",
      "name": "AttrPaxgE2NoTrail4h",
      "session_id": "4175efce-ac59-4c16-b23a-278fb6c9b8bc",
      "dashboard_url": "http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc",
      "net": 4325.434486548319,
      "fees": 100.76522170331324,
      "before_fees": 4426.199708251632,
      "PF": 6.386025058164697,
      "DDmotor": -10.672145947980683,
      "CAGR": 7.137585313949457,
      "N": 15,
      "timeexposure": 40.14855929234542,
      "entrynotionaltime": 0.2058407012709682,
      "entry_notional_hours": 94011565.0844766,
      "entry_notional_sum": 109748.25759400001,
      "net_bps_entry_notional": 394.1232946540003,
      "stress5": 4269.453807824256,
      "stress10": 4213.473129100194,
      "exbest": -793.9250957345803,
      "ex3": -798.422059528828,
      "best_trade_net": 5119.359582282899,
      "winning_trades": 6,
      "mean_holding_hours": 1222.4433333333334,
      "max_holding_hours": 15971.266666666666,
      "cohorts": {
        "2021": {
          "n": 6,
          "net": -365.6594272424556,
          "static_5bps_RT": -384.73885142352646,
          "static_10bps_RT": -403.8182756045973
        },
        "2022": {
          "n": 3,
          "net": -178.99124462370426,
          "static_5bps_RT": -188.61782547393094,
          "static_10bps_RT": -198.2444063241576
        },
        "2023": {
          "n": 5,
          "net": -249.2744238684202,
          "static_5bps_RT": -272.93651105168556,
          "static_10bps_RT": -296.59859823495094
        },
        "2025": {
          "n": 1,
          "net": 5119.359582282899,
          "static_5bps_RT": 5115.746995773399,
          "static_10bps_RT": 5112.134409263899
        }
      },
      "recent_closed_cohort_2023_2025": 4870.085158414479,
      "terminal": [
        {
          "type": "long",
          "gross": 5125.862238,
          "net": 5119.359582282899,
          "hours": 15971.266666666666
        }
      ],
      "terminal_counter_reconciliation": {
        "stored_open_count": 1,
        "stored_open_pl": 5125.862237999999,
        "terminal_records": 1,
        "gross_open_pl_error": 9.094947017729282e-13,
        "note": "Pretermination counter reconciled with fully closed synthetic boundary trade; not proof of native liquidity."
      },
      "audit": {
        "max_fee_error": 8.881784197001252e-16,
        "max_pnl_error": 9.094947017729282e-13,
        "max_qty_error": 0,
        "wallet_error": 1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 15,
          "exit_STOP": 14,
          "exit_MARKET": 1
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 37,
        "positive_months": 22,
        "win_months_all": 0.36065573770491804,
        "win_months_active": 0.5945945945945946,
        "quarters_total": 19,
        "positive_quarters": 9,
        "win_quarters": 0.47368421052631576
      },
      "daily_close_drawdown_pct": -10.674452139731105
    },
    {
      "id": "E3",
      "control": "C0",
      "reference": "C0",
      "name": "AttrPaxgE3InitialStop4h",
      "session_id": "831637c7-ade9-4be6-a15b-d568cd5d9242",
      "dashboard_url": "http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242",
      "net": 3669.3684495321963,
      "fees": 98.18488423879695,
      "before_fees": 3767.5533337709935,
      "PF": 4.018712149634905,
      "DDmotor": -14.745523767615577,
      "CAGR": 6.178572149107242,
      "N": 15,
      "timeexposure": 40.56584632451685,
      "entrynotionaltime": 0.2010344685193935,
      "entry_notional_hours": 91816462.4621774,
      "entry_notional_sum": 107210.53915400001,
      "net_bps_entry_notional": 342.25818454857506,
      "stress5": 3614.8212916217535,
      "stress10": 3560.2741337113107,
      "exbest": -1215.5410213511036,
      "ex3": -1055.088340899572,
      "best_trade_net": 4884.9094708833,
      "winning_trades": 1,
      "mean_holding_hours": 1235.148888888889,
      "max_holding_hours": 15971.266666666666,
      "cohorts": {
        "2021": {
          "n": 6,
          "net": -548.0480230428889,
          "static_5bps_RT": -566.9258245748175,
          "static_10bps_RT": -585.8036261067462
        },
        "2022": {
          "n": 3,
          "net": -261.9211849637484,
          "static_5bps_RT": -271.34392725153697,
          "static_10bps_RT": -280.7666695393255
        },
        "2023": {
          "n": 5,
          "net": -405.5718133444662,
          "static_5bps_RT": -428.37128570369174,
          "static_10bps_RT": -451.1707580629173
        },
        "2025": {
          "n": 1,
          "net": 4884.9094708833,
          "static_5bps_RT": 4881.4623291518,
          "static_10bps_RT": 4878.0151874203
        }
      },
      "recent_closed_cohort_2023_2025": 4479.337657538834,
      "terminal": [
        {
          "type": "long",
          "gross": 4891.114326,
          "net": 4884.9094708833,
          "hours": 15971.266666666666
        }
      ],
      "terminal_counter_reconciliation": {
        "stored_open_count": 1,
        "stored_open_pl": 4891.114326000001,
        "terminal_records": 1,
        "gross_open_pl_error": 9.094947017729282e-13,
        "note": "Pretermination counter reconciled with fully closed synthetic boundary trade; not proof of native liquidity."
      },
      "audit": {
        "max_fee_error": 8.881784197001252e-16,
        "max_pnl_error": 9.805489753489383e-13,
        "max_qty_error": 0,
        "wallet_error": -5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 15,
          "exit_STOP": 14,
          "exit_MARKET": 1
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 37,
        "positive_months": 19,
        "win_months_all": 0.3114754098360656,
        "win_months_active": 0.5135135135135135,
        "quarters_total": 19,
        "positive_quarters": 6,
        "win_quarters": 0.3157894736842105
      },
      "daily_close_drawdown_pct": -14.747724796307693
    },
    {
      "id": "E4",
      "control": "E3",
      "reference": "C0",
      "name": "AttrPaxgE4InitialStop72h4h",
      "session_id": "573cca4f-01b7-4be4-9af3-e64d9a50c837",
      "dashboard_url": "http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837",
      "net": -374.3541041358759,
      "fees": 312.57348013259855,
      "before_fees": -61.78062400327735,
      "PF": 0.8286523024869447,
      "DDmotor": -6.412482041798828,
      "CAGR": -0.7291338603827469,
      "N": 47,
      "timeexposure": 5.764837683190282,
      "entrynotionaltime": 0.04255271865552756,
      "entry_notional_hours": 19434677.664352547,
      "entry_notional_sum": 347334.757126,
      "net_bps_entry_notional": -10.777905074443048,
      "stress5": -548.0060375428751,
      "stress10": -721.6579709498743,
      "exbest": -618.4891372949257,
      "ex3": -1034.2078856149242,
      "best_trade_net": 244.1350331590498,
      "winning_trades": 19,
      "mean_holding_hours": 56.01950354609929,
      "max_holding_hours": 75.98333333333333,
      "cohorts": {
        "2020": {
          "n": 1,
          "net": -26.92195844400032,
          "static_5bps_RT": -29.75982202400032,
          "static_10bps_RT": -32.59768560400032
        },
        "2021": {
          "n": 6,
          "net": -247.94545489522213,
          "static_5bps_RT": -268.0109890763798,
          "static_10bps_RT": -288.0765232575376
        },
        "2022": {
          "n": 4,
          "net": -93.64930416957222,
          "static_5bps_RT": -107.09171542859639,
          "static_10bps_RT": -120.53412668762056
        },
        "2023": {
          "n": 5,
          "net": -238.88837341328684,
          "static_5bps_RT": -263.1016715040744,
          "static_10bps_RT": -287.3149695948619
        },
        "2024": {
          "n": 11,
          "net": 433.0224265408987,
          "static_5bps_RT": 396.11912709951486,
          "static_10bps_RT": 359.21582765813105
        },
        "2025": {
          "n": 20,
          "net": -199.9714397546931,
          "static_5bps_RT": -276.160966609339,
          "static_10bps_RT": -352.35049346398495
        }
      },
      "recent_closed_cohort_2023_2025": -5.837386627081159,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0942358130705543e-12,
        "max_qty_error": 0,
        "wallet_error": -3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_LIMIT": 47,
          "exit_MARKET": 25,
          "exit_STOP": 22
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 30,
        "positive_months": 11,
        "win_months_all": 0.18032786885245902,
        "win_months_active": 0.36666666666666664,
        "quarters_total": 19,
        "positive_quarters": 6,
        "win_quarters": 0.3157894736842105
      },
      "daily_close_drawdown_pct": -6.293534846043114
    },
    {
      "id": "M",
      "control": "Cq",
      "reference": "C0",
      "name": "AttrPaxgMMarketSignal4h",
      "session_id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
      "dashboard_url": "http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
      "net": 962.1262139358278,
      "fees": 267.71818325273483,
      "before_fees": 1229.8443971885627,
      "PF": 1.5743577329815752,
      "DDmotor": -7.64796155547669,
      "CAGR": 1.777532757709932,
      "N": 38,
      "timeexposure": 15.204866584924389,
      "entrynotionaltime": 0.117065150055092,
      "entry_notional_hours": 53465995.333161615,
      "entry_notional_sum": 296849.72586,
      "net_bps_entry_notional": 32.41122123823637,
      "stress5": 813.3938899065306,
      "stress10": 664.6615658772334,
      "exbest": 337.4547898331979,
      "ex3": -635.127505102286,
      "best_trade_net": 624.6714241026299,
      "winning_trades": 18,
      "mean_holding_hours": 182.74649122807014,
      "max_holding_hours": 917.4833333333333,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 1275.647506856833,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
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
      "mtm_complete": {
        "months_total": 61,
        "months_active": 31,
        "positive_months": 17,
        "win_months_all": 0.2786885245901639,
        "win_months_active": 0.5483870967741935,
        "quarters_total": 19,
        "positive_quarters": 10,
        "win_quarters": 0.5263157894736842
      },
      "daily_close_drawdown_pct": -7.65034683398127
    },
    {
      "id": "R01",
      "control": "U01",
      "reference": "C0",
      "name": "AttrPaxgRegimeSeed1014h",
      "session_id": "fa518c27-144f-4af4-837c-b00c837110b1",
      "dashboard_url": "http://localhost:9200/#/backtest/fa518c27-144f-4af4-837c-b00c837110b1",
      "net": 108.95460408721488,
      "fees": 207.999658866129,
      "before_fees": 316.9542629533439,
      "PF": 1.0632284670396688,
      "DDmotor": -8.419993423574446,
      "CAGR": 0.20806346552375565,
      "N": 33,
      "timeexposure": 10.20621679219945,
      "entrynotionaltime": 0.07216537592476113,
      "entry_notional_hours": 32959370.492356904,
      "entry_notional_sum": 230952.25494200003,
      "net_bps_entry_notional": 4.717624606634695,
      "stress5": -6.6007619495234735,
      "stress10": -122.15612798626182,
      "exbest": -248.61793224837265,
      "ex3": -918.7622952047479,
      "best_trade_net": 357.57253633558753,
      "winning_trades": 13,
      "mean_holding_hours": 141.2540404040404,
      "max_holding_hours": 567.3333333333334,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 655.4112028906724,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.1368683772161603e-12,
        "max_qty_error": 0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 33,
          "exit_STOP": 33
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 30,
        "positive_months": 11,
        "win_months_all": 0.18032786885245902,
        "win_months_active": 0.36666666666666664,
        "quarters_total": 19,
        "positive_quarters": 4,
        "win_quarters": 0.21052631578947367
      },
      "daily_close_drawdown_pct": -8.421614424806378
    },
    {
      "id": "R02",
      "control": "U02",
      "reference": "C0",
      "name": "AttrPaxgRegimeSeed2024h",
      "session_id": "a8e6461e-2b14-4130-b9f6-0989a4483c8c",
      "dashboard_url": "http://localhost:9200/#/backtest/a8e6461e-2b14-4130-b9f6-0989a4483c8c",
      "net": -153.986059114385,
      "fees": 201.6750934612561,
      "before_fees": 47.6890343468711,
      "PF": 0.901581027887423,
      "DDmotor": -8.810783631607755,
      "CAGR": -0.2972040536758369,
      "N": 30,
      "timeexposure": 8.632094062007358,
      "entrynotionaltime": 0.0706245613874849,
      "entry_notional_hours": 32255649.6768921,
      "entry_notional_sum": 224059.592662,
      "net_bps_entry_notional": -6.872549275168823,
      "stress5": -266.0277777039717,
      "stress10": -378.0694962935585,
      "exbest": -510.42873477603666,
      "ex3": -1053.1250796810994,
      "best_trade_net": 356.44267566165166,
      "winning_trades": 11,
      "mean_holding_hours": 131.41500000000002,
      "max_holding_hours": 555.65,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": -210.41918990040108,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 7.389644451905042e-13,
        "max_qty_error": 0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 30,
          "exit_STOP": 30
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 28,
        "positive_months": 10,
        "win_months_all": 0.16393442622950818,
        "win_months_active": 0.35714285714285715,
        "quarters_total": 19,
        "positive_quarters": 7,
        "win_quarters": 0.3684210526315789
      },
      "daily_close_drawdown_pct": -8.680467236789092
    },
    {
      "id": "R03",
      "control": "U03",
      "reference": "C0",
      "name": "AttrPaxgRegimeSeed3034h",
      "session_id": "0e7552b8-3491-4925-b230-f31c89b92796",
      "dashboard_url": "http://localhost:9200/#/backtest/0e7552b8-3491-4925-b230-f31c89b92796",
      "net": 869.1587134413251,
      "fees": 192.82187705512342,
      "before_fees": 1061.9805904964485,
      "PF": 1.8098221924048983,
      "DDmotor": -7.269274609205656,
      "CAGR": 1.6114074512330268,
      "N": 30,
      "timeexposure": 13.54086384071933,
      "entrynotionaltime": 0.09281495138911766,
      "entry_notional_hours": 42390444.598437816,
      "entry_notional_sum": 213715.539766,
      "net_bps_entry_notional": 40.66895249605988,
      "stress5": 762.035448410701,
      "stress10": 654.9121833800768,
      "exbest": 413.8563109430569,
      "ex3": -286.13733683210853,
      "best_trade_net": 455.3024024982682,
      "winning_trades": 16,
      "mean_holding_hours": 206.1461111111111,
      "max_holding_hours": 812.0666666666667,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 1342.9272084131117,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.1439738045737613e-12,
        "max_qty_error": 0,
        "wallet_error": 3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 30,
          "exit_STOP": 30
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 30,
        "positive_months": 17,
        "win_months_all": 0.2786885245901639,
        "win_months_active": 0.5666666666666667,
        "quarters_total": 19,
        "positive_quarters": 7,
        "win_quarters": 0.3684210526315789
      },
      "daily_close_drawdown_pct": -7.2736771785766425
    },
    {
      "id": "R04",
      "control": "U04",
      "reference": "C0",
      "name": "AttrPaxgRegimeSeed4044h",
      "session_id": "0edfce4f-695a-4213-8426-304b9af6d5a4",
      "dashboard_url": "http://localhost:9200/#/backtest/0edfce4f-695a-4213-8426-304b9af6d5a4",
      "net": 1252.4370318555846,
      "fees": 189.65373944638588,
      "before_fees": 1442.0907713019706,
      "PF": 2.0881540287092446,
      "DDmotor": -4.580992551167007,
      "CAGR": 2.2890676489804473,
      "N": 25,
      "timeexposure": 11.825589712150403,
      "entrynotionaltime": 0.0951177433437744,
      "entry_notional_hours": 43442175.73996864,
      "entry_notional_sum": 210005.331777,
      "net_bps_entry_notional": 59.63834447715449,
      "stress5": 1147.0738432742592,
      "stress10": 1041.7106546929335,
      "exbest": 715.9431449407707,
      "ex3": -121.07853098667442,
      "best_trade_net": 536.4938869148139,
      "winning_trades": 11,
      "mean_holding_hours": 216.03933333333333,
      "max_holding_hours": 814.5,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 1391.6417479263546,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.1510792319313623e-12,
        "max_qty_error": 0,
        "wallet_error": -1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 25,
          "exit_STOP": 25
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 24,
        "positive_months": 12,
        "win_months_all": 0.19672131147540983,
        "win_months_active": 0.5,
        "quarters_total": 19,
        "positive_quarters": 8,
        "win_quarters": 0.42105263157894735
      },
      "daily_close_drawdown_pct": -4.48836597574277
    },
    {
      "id": "R05",
      "control": "U05",
      "reference": "C0",
      "name": "AttrPaxgRegimeSeed5054h",
      "session_id": "cfff7109-04c5-4420-8a90-fc19ceec6ef8",
      "dashboard_url": "http://localhost:9200/#/backtest/cfff7109-04c5-4420-8a90-fc19ceec6ef8",
      "net": 47.8563680668258,
      "fees": 228.91731444382978,
      "before_fees": 276.7736825106556,
      "PF": 1.0318390691132129,
      "DDmotor": -12.408550923653273,
      "CAGR": 0.09161267176265309,
      "N": 36,
      "timeexposure": 13.702341332399135,
      "entrynotionaltime": 0.09035797289552172,
      "entry_notional_hours": 41268293.38084268,
      "entry_notional_sum": 254214.184763,
      "net_bps_entry_notional": 1.8825215481756679,
      "stress5": -79.31991773530189,
      "stress10": -206.49620353742955,
      "exbest": -318.7382477261987,
      "ex3": -827.7787833117094,
      "best_trade_net": 366.5946157930245,
      "winning_trades": 15,
      "mean_holding_hours": 173.83703703703702,
      "max_holding_hours": 788.0666666666667,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 254.1800142049023,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.1368683772161603e-12,
        "max_qty_error": 0,
        "wallet_error": -5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 36,
          "exit_STOP": 36
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 32,
        "positive_months": 12,
        "win_months_all": 0.19672131147540983,
        "win_months_active": 0.375,
        "quarters_total": 19,
        "positive_quarters": 6,
        "win_quarters": 0.3157894736842105
      },
      "daily_close_drawdown_pct": -12.31074513108734
    },
    {
      "id": "U01",
      "control": "R01",
      "reference": "C0",
      "name": "AttrPaxgUnconditionalSeed1014h",
      "session_id": "6cc08024-0aa2-4cdf-a666-25f4351681bd",
      "dashboard_url": "http://localhost:9200/#/backtest/6cc08024-0aa2-4cdf-a666-25f4351681bd",
      "net": 2902.3188985783913,
      "fees": 794.0684911939976,
      "before_fees": 3696.387389772389,
      "PF": 1.5141207622803052,
      "DDmotor": -14.109308696330336,
      "CAGR": 5.008957309215956,
      "N": 118,
      "timeexposure": 50.15702545688093,
      "entrynotionaltime": 0.35702907919320614,
      "entry_notional_hours": 163062321.0491211,
      "entry_notional_sum": 880450.129854,
      "net_bps_entry_notional": 32.964035101677666,
      "stress5": 2461.169736803948,
      "stress10": 2020.020575029505,
      "exbest": 2297.83236505825,
      "ex3": 1254.128240088258,
      "best_trade_net": 604.486533520141,
      "winning_trades": 48,
      "mean_holding_hours": 194.13319209039543,
      "max_holding_hours": 1051.65,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 4077.1768747859032,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.5347723092418164e-12,
        "max_qty_error": 0,
        "wallet_error": -5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 118,
          "exit_STOP": 118
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 32,
        "win_months_all": 0.5245901639344263,
        "win_months_active": 0.5245901639344263,
        "quarters_total": 19,
        "positive_quarters": 10,
        "win_quarters": 0.5263157894736842
      },
      "daily_close_drawdown_pct": -14.10930869633047
    },
    {
      "id": "U02",
      "control": "R02",
      "reference": "C0",
      "name": "AttrPaxgUnconditionalSeed2024h",
      "session_id": "4d938a9b-653e-4226-9a1c-899b689e6b62",
      "dashboard_url": "http://localhost:9200/#/backtest/4d938a9b-653e-4226-9a1c-899b689e6b62",
      "net": 37.11393470002805,
      "fees": 685.4999184635236,
      "before_fees": 722.6138531635517,
      "PF": 1.00668130183597,
      "DDmotor": -18.392769242805596,
      "CAGR": 0.07107890035329412,
      "N": 107,
      "timeexposure": 39.920410754948314,
      "entrynotionaltime": 0.27010513225320176,
      "entry_notional_hours": 123362416.0026823,
      "entry_notional_sum": 761305.269144,
      "net_bps_entry_notional": 0.4875039777638527,
      "stress5": -343.71935333526284,
      "stress10": -724.5526413705537,
      "exbest": -538.412619982662,
      "ex3": -1550.7874091733306,
      "best_trade_net": 575.5265546826901,
      "winning_trades": 34,
      "mean_holding_hours": 170.39672897196263,
      "max_holding_hours": 770.0166666666667,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 767.8475915952781,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0658141036401503e-12,
        "max_qty_error": 0,
        "wallet_error": 5.4569682106375694e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 107,
          "exit_STOP": 107
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 59,
        "positive_months": 26,
        "win_months_all": 0.4262295081967213,
        "win_months_active": 0.4406779661016949,
        "quarters_total": 19,
        "positive_quarters": 8,
        "win_quarters": 0.42105263157894735
      },
      "daily_close_drawdown_pct": -18.418622808332085
    },
    {
      "id": "U03",
      "control": "R03",
      "reference": "C0",
      "name": "AttrPaxgUnconditionalSeed3034h",
      "session_id": "e572d0cc-9a77-4998-b2ae-ec335daadf7d",
      "dashboard_url": "http://localhost:9200/#/backtest/e572d0cc-9a77-4998-b2ae-ec335daadf7d",
      "net": 2611.0960217982597,
      "fees": 840.2635548479908,
      "before_fees": 3451.3595766462504,
      "PF": 1.4023615106836755,
      "DDmotor": -19.106167261375884,
      "CAGR": 4.550144357964969,
      "N": 129,
      "timeexposure": 51.32750919600632,
      "entrynotionaltime": 0.3583015908855738,
      "entry_notional_hours": 163643502.58925927,
      "entry_notional_sum": 931900.492265,
      "net_bps_entry_notional": 28.019043272012297,
      "stress5": 2144.282935771598,
      "stress10": 1677.4698497449367,
      "exbest": 1784.4943963902429,
      "ex3": 429.94983049966004,
      "best_trade_net": 826.601625408017,
      "winning_trades": 46,
      "mean_holding_hours": 181.72325581395347,
      "max_holding_hours": 1063.65,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 4390.477224082758,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.0018652574217413e-12,
        "max_qty_error": 0,
        "wallet_error": -3.637978807091713e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 129,
          "exit_STOP": 129
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 60,
        "positive_months": 30,
        "win_months_all": 0.4918032786885246,
        "win_months_active": 0.5,
        "quarters_total": 19,
        "positive_quarters": 10,
        "win_quarters": 0.5263157894736842
      },
      "daily_close_drawdown_pct": -19.108228105716208
    },
    {
      "id": "U04",
      "control": "R04",
      "reference": "C0",
      "name": "AttrPaxgUnconditionalSeed4044h",
      "session_id": "f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
      "dashboard_url": "http://localhost:9200/#/backtest/f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
      "net": 1667.0255846903513,
      "fees": 863.9696181936978,
      "before_fees": 2530.995202884049,
      "PF": 1.2754622165355791,
      "DDmotor": -21.721488669670087,
      "CAGR": 3.0013978599566116,
      "N": 126,
      "timeexposure": 48.148391428738265,
      "entrynotionaltime": 0.3298446745749119,
      "entry_notional_hours": 150646659.77185377,
      "entry_notional_sum": 958700.744836,
      "net_bps_entry_notional": 17.388383118191076,
      "stress5": 1187.04246347163,
      "stress10": 707.0593422529091,
      "exbest": 1035.9108851990409,
      "ex3": -89.24104755271492,
      "best_trade_net": 631.1146994913103,
      "winning_trades": 45,
      "mean_holding_hours": 174.52645502645504,
      "max_holding_hours": 1059.65,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 2902.522838378245,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.5916157281026244e-12,
        "max_qty_error": 0,
        "wallet_error": 1.8189894035458565e-11,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 126,
          "exit_STOP": 126
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 60,
        "positive_months": 29,
        "win_months_all": 0.47540983606557374,
        "win_months_active": 0.48333333333333334,
        "quarters_total": 19,
        "positive_quarters": 9,
        "win_quarters": 0.47368421052631576
      },
      "daily_close_drawdown_pct": -21.694133630144496
    },
    {
      "id": "U05",
      "control": "R05",
      "reference": "C0",
      "name": "AttrPaxgUnconditionalSeed5054h",
      "session_id": "54613844-7e5d-4911-9342-071f65e0922b",
      "dashboard_url": "http://localhost:9200/#/backtest/54613844-7e5d-4911-9342-071f65e0922b",
      "net": 3873.5353640048943,
      "fees": 932.1098628756963,
      "before_fees": 4805.645226880591,
      "PF": 1.6293339988049484,
      "DDmotor": -9.73397056635823,
      "CAGR": 6.480930642303528,
      "N": 122,
      "timeexposure": 49.79506043089857,
      "entrynotionaltime": 0.39233893948730564,
      "entry_notional_hours": 179189040.44264224,
      "entry_notional_sum": 1033274.8028040001,
      "net_bps_entry_notional": 37.48794951249438,
      "stress5": 3355.696551296174,
      "stress10": 2837.857738587454,
      "exbest": 3159.9486035330733,
      "ex3": 1892.6570996074734,
      "best_trade_net": 713.5867604718211,
      "winning_trades": 47,
      "mean_holding_hours": 186.41311475409836,
      "max_holding_hours": 991.6166666666667,
      "cohorts": {
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
      "recent_closed_cohort_2023_2025": 3927.245241669372,
      "terminal": [],
      "terminal_counter_reconciliation": {
        "stored_open_count": 0,
        "stored_open_pl": 0,
        "terminal_records": 0
      },
      "audit": {
        "max_fee_error": 1.7763568394002505e-15,
        "max_pnl_error": 1.7621459846850485e-12,
        "max_qty_error": 0,
        "wallet_error": -1.8189894035458565e-12,
        "overlaps": 0,
        "ordertypes": {
          "entry_MARKET": 122,
          "exit_STOP": 122
        }
      },
      "mtm_complete": {
        "months_total": 61,
        "months_active": 60,
        "positive_months": 28,
        "win_months_all": 0.45901639344262296,
        "win_months_active": 0.4666666666666667,
        "quarters_total": 19,
        "positive_quarters": 12,
        "win_quarters": 0.631578947368421
      },
      "daily_close_drawdown_pct": -9.733970566358085
    }
  ],
  "mtm_source": "strategies/MultiAssetRetestBtcShort4h/reports/ATTRIBUTION_MTM_RESULTS_20261019.md"
}
```
