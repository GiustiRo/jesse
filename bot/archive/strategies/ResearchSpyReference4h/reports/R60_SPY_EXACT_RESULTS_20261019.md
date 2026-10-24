# R60 SPY — diez filas exactas

Diez controles nuevos finished. BaselineCq existente sin rerun. DD/CAGR/Sharpe del motor; exposición temporal como fracción y entrynotionaltime como notional a precioentrada×tiempo/(10k×ventana), NO MTM. Stressestático+5/+10bpsRT mismosfills/tamaños; exbest/ex3 diagnósticos, no criterios automáticos de descarte runners. Cohortes por cierre NO retornos anualesMTM. Valores completos, sin redondeo.

```json
[
  {
    "id": "d404c47e-025a-4789-b1a8-b054402f6c21",
    "control": "S01",
    "name": "R60SpyGapMin10",
    "dashboard_url": "http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21",
    "change": "0.10 < g <= 1.0",
    "N": 23,
    "net": 82.9535236572004,
    "fees": 212.01672727526963,
    "PF": 1.06596462316971,
    "DDmotor": -6.654984999592428,
    "CAGR": 0.15857616602510394,
    "Sharpe": 0.07648903056030368,
    "timeexposure": 0.11080640217200911,
    "entrynotionaltime": 0.09984102700401203,
    "stress5": -34.83354705128272,
    "stress10": -152.62061775976576,
    "exbest": -251.68933926337243,
    "ex3": -690.9944515622414,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.54068155404738,
        "fee": 20.392452668440114
      },
      "2022": {
        "n": 4,
        "net": -118.313081514564,
        "fee": 22.925577513149364
      },
      "2023": {
        "n": 6,
        "net": -85.92178478984678,
        "fee": 61.77352323935228
      },
      "2024": {
        "n": 7,
        "net": -157.96197597635802,
        "fee": 77.75021022473177
      },
      "2025": {
        "n": 3,
        "net": 60.63017110188187,
        "fee": 25.84633726771632
      }
    },
    "mean_hours": 220.0326086956522,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 23.54266562915,
    "roundtrip_turnover_initial_equity": 47.11482828339325,
    "net_bps_entry": 3.5235399832756924,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 23
    },
    "exit_order_types": {
      "STOP": 23
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": null,
    "identical_to_Cq_equity_curve": null
  },
  {
    "id": "cd61d362-4b1c-4793-80b7-e85a9494edae",
    "control": "S02",
    "name": "R60SpyGapMin25",
    "dashboard_url": "http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae",
    "change": "0.25 < g <= 1.0",
    "N": 14,
    "net": 245.8742418595162,
    "fees": 125.36052140162752,
    "PF": 1.3446510233072277,
    "DDmotor": -4.099687568281962,
    "CAGR": 0.46697537512865317,
    "Sharpe": 0.23228570468090567,
    "timeexposure": 0.06816430197933088,
    "entrynotionaltime": 0.06647236035378323,
    "stress5": 176.22950774750092,
    "stress10": 106.58477363548562,
    "exbest": -73.85444125549776,
    "ex3": -512.8090386653323,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 2,
        "net": 232.82492507750962,
        "fee": 20.141113353764077
      },
      "2022": {
        "n": 4,
        "net": -279.5241368405673,
        "fee": 24.043099005974433
      },
      "2023": {
        "n": 2,
        "net": 100.95029262654408,
        "fee": 18.973196111221995
      },
      "2024": {
        "n": 4,
        "net": 36.653719086849826,
        "fee": 43.527720320823455
      },
      "2025": {
        "n": 2,
        "net": 154.9694419091799,
        "fee": 18.675392609843563
      }
    },
    "mean_hours": 222.37142857142857,
    "max_hours": 683.25,
    "entry_turnover_initial_equity": 13.91038508424,
    "roundtrip_turnover_initial_equity": 27.85789364480612,
    "net_bps_entry": 17.675588444929787,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 14
    },
    "exit_order_types": {
      "STOP": 14
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": null,
    "identical_to_Cq_equity_curve": null
  },
  {
    "id": "9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
    "control": "S03",
    "name": "R60SpyGapMax50",
    "dashboard_url": "http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
    "change": "0.0 < g <= 0.50",
    "N": 30,
    "net": 743.9711828862412,
    "fees": 276.63145167598293,
    "PF": 1.4896904685510277,
    "DDmotor": -6.132698354864685,
    "CAGR": 1.3858836381329676,
    "Sharpe": 0.4596199367125393,
    "timeexposure": 0.14441999474513925,
    "entrynotionaltime": 0.13718877951137115,
    "stress5": 590.2870430662508,
    "stress10": 436.6029032462603,
    "exbest": 342.4612407364584,
    "ex3": -302.32269970477955,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -314.92014410268337,
        "fee": 30.436143613609914
      },
      "2023": {
        "n": 9,
        "net": 391.9223598197066,
        "fee": 88.25015752215383
      },
      "2024": {
        "n": 7,
        "net": 73.5204387094704,
        "fee": 78.09488095358837
      },
      "2025": {
        "n": 5,
        "net": 119.64121195392713,
        "fee": 44.828449060056286
      }
    },
    "mean_hours": 219.865,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 30.68579783227,
    "roundtrip_turnover_initial_equity": 61.473655927996234,
    "net_bps_entry": 24.244804940475145,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 23,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 30
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": null,
    "identical_to_Cq_equity_curve": null
  },
  {
    "id": "89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
    "control": "S04",
    "name": "R60SpyGapMax75",
    "dashboard_url": "http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
    "change": "0.0 < g <= 0.75",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fee": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 395.7611513896043,
        "fee": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024080012,
        "fee": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.70108055231466,
        "fee": 44.85926795981045
      }
    },
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": true,
    "identical_to_Cq_equity_curve": true
  },
  {
    "id": "8bae70a3-ab31-4fc5-9905-c65023b03134",
    "control": "S05",
    "name": "R60SpyN24",
    "dashboard_url": "http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134",
    "change": "donchian_len26→24",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fee": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 395.7611513896043,
        "fee": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024080012,
        "fee": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.70108055231466,
        "fee": 44.85926795981045
      }
    },
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": true,
    "identical_to_Cq_equity_curve": true
  },
  {
    "id": "2327e98c-4c6d-4a70-b54d-75646cdd82c2",
    "control": "S06",
    "name": "R60SpyN28",
    "dashboard_url": "http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2",
    "change": "donchian_len26→28",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fee": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 395.7611513896043,
        "fee": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024080012,
        "fee": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.70108055231466,
        "fee": 44.85926795981045
      }
    },
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": true,
    "identical_to_Cq_equity_curve": true
  },
  {
    "id": "60d1237b-6b7a-435b-ae6d-fa1103205b60",
    "control": "S07",
    "name": "R60SpyAdx24",
    "dashboard_url": "http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60",
    "change": "adx_min26→24",
    "N": 39,
    "net": 597.9379578325991,
    "fees": 350.46780701762265,
    "PF": 1.3048982927072252,
    "DDmotor": -8.096205641424326,
    "CAGR": 1.1201069472235758,
    "Sharpe": 0.3377375270170746,
    "timeexposure": 0.1810503882758218,
    "entrynotionaltime": 0.1655766793706388,
    "stress5": 403.2336206005866,
    "stress10": 208.529283368574,
    "exbest": 198.3763364424717,
    "ex3": -451.92482537426145,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 5,
        "net": 530.5196353485741,
        "fee": 46.31573518160858
      },
      "2022": {
        "n": 7,
        "net": -347.13703384618935,
        "fee": 43.86384649054997
      },
      "2023": {
        "n": 11,
        "net": 203.19320101426078,
        "fee": 103.96390267245903
      },
      "2024": {
        "n": 9,
        "net": 48.48226908108998,
        "fee": 96.92647166184433
      },
      "2025": {
        "n": 6,
        "net": 24.900372952823645,
        "fee": 56.06922464928094
      }
    },
    "mean_hours": 212.02393162393162,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 38.893447158159994,
    "roundtrip_turnover_initial_equity": 77.88173489280503,
    "net_bps_entry": 15.373745489853023,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 32,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 39
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": false,
    "identical_to_Cq_equity_curve": false
  },
  {
    "id": "19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
    "control": "S08",
    "name": "R60SpyAdx28",
    "dashboard_url": "http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
    "change": "adx_min26→28",
    "N": 24,
    "net": 686.0308434052209,
    "fees": 218.9783135961006,
    "PF": 1.555117092021026,
    "DDmotor": -5.892075684490239,
    "CAGR": 1.2807852033825728,
    "Sharpe": 0.47295715146124506,
    "timeexposure": 0.12023413323991358,
    "entrynotionaltime": 0.113510417707401,
    "stress5": 564.3762247407205,
    "stress10": 442.7216060762202,
    "exbest": 290.36587299061233,
    "ex3": -360.3540051435342,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 427.64749313911625,
        "fee": 19.751448193079487
      },
      "2022": {
        "n": 5,
        "net": -400.45703000137615,
        "fee": 32.0045898020403
      },
      "2023": {
        "n": 7,
        "net": 231.8844849968417,
        "fee": 68.59311195120661
      },
      "2024": {
        "n": 6,
        "net": 83.80710197659216,
        "fee": 70.5014641882642
      },
      "2025": {
        "n": 3,
        "net": 205.16928001200694,
        "fee": 24.799073099630235
      }
    },
    "mean_hours": 228.80555555555554,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 24.28567327505,
    "roundtrip_turnover_initial_equity": 48.661847465800136,
    "net_bps_entry": 28.248376548407986,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 19,
      "MARKET": 5
    },
    "exit_order_types": {
      "STOP": 24
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": false,
    "identical_to_Cq_equity_curve": false
  },
  {
    "id": "84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
    "control": "S09",
    "name": "R60SpyFast16",
    "dashboard_url": "http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
    "change": "ema_fast20→16",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fee": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 395.7611513896043,
        "fee": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024080012,
        "fee": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.70108055231466,
        "fee": 44.85926795981045
      }
    },
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": true,
    "identical_to_Cq_equity_curve": true
  },
  {
    "id": "333221fd-d6ed-462d-87eb-2eb255bbc50a",
    "control": "S10",
    "name": "R60SpyFast24",
    "dashboard_url": "http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a",
    "change": "ema_fast20→24",
    "N": 31,
    "net": 751.7119522395761,
    "fees": 286.7708466456683,
    "PF": 1.4933836938880178,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.399889971337509,
    "Sharpe": 0.4584228742218906,
    "timeexposure": 0.15253364570561104,
    "entrynotionaltime": 0.14140980381744386,
    "stress5": 592.394815214205,
    "stress10": 433.0776781888338,
    "exbest": 349.91625637837717,
    "ex3": -297.899045359473,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fee": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 396.09988130755266,
        "fee": 89.40507957741823
      },
      "2024": {
        "n": 8,
        "net": -22.5085097573902,
        "fee": 87.70929772822687
      },
      "2025": {
        "n": 5,
        "net": 119.72169164013778,
        "fee": 44.86091017023466
      }
    },
    "mean_hours": 224.72634408602153,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.811503265130007,
    "roundtrip_turnover_initial_equity": 63.726854810148524,
    "net_bps_entry": 23.630192700247548,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 25,
      "MARKET": 6
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0,
    "identical_to_Cq_full_trade_economic_path": false,
    "identical_to_Cq_equity_curve": false
  }
]
```

## Baseline existente auditado en ambos lotes

```json
{
  "session_id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
  "n": 31,
  "net": 751.3477149671152,
  "gross_price": 1037.8232411744636,
  "fee": 286.47552620734854,
  "PF": 1.4930482284215572,
  "return_pct": 7.513477149671152,
  "CAGR_engine_pct": 1.3992310944554776,
  "Sharpe_engine": 0.4581998683996086,
  "DD_engine_pct": -5.2131810594609025,
  "hours_open": 6971.416666666667,
  "fraction_time_open": 0.15264093244584573,
  "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14148527769141334,
  "entry_turnover_initial_equity": 31.77872286098001,
  "roundtrip_turnover_initial_equity": 63.66122804607744,
  "net_bps_entry": 23.64310605728177,
  "net_per_exposure_entry_time_measure": 0.5310430365806986,
  "max_initial_gross_equity": 1.5989937330573134,
  "mean_hours": 224.88440860215056,
  "max_hours": 837.9666666666667,
  "stress5_RT_samefills": 592.1946448519213,
  "stress10_RT_samefills": 433.0415747367277,
  "net_without_top1": 349.57799671604494,
  "net_without_top3": -298.2237721588764,
  "net_without_top5": -757.536337350717,
  "closed_trade_year_cohorts_NOT_MTM": {
    "2020": {
      "n": 1,
      "net": 137.97951328204002,
      "fee": 3.3286263618797642
    },
    "2021": {
      "n": 3,
      "net": 335.8278032237806,
      "fee": 31.69319416469481
    },
    "2022": {
      "n": 5,
      "net": -215.40842745654456,
      "fee": 29.773738643213996
    },
    "2023": {
      "n": 9,
      "net": 395.7611513896043,
      "fee": 89.11426287503907
    },
    "2024": {
      "n": 8,
      "net": -22.513406024080012,
      "fee": 87.70643620271038
    },
    "2025": {
      "n": 5,
      "net": 119.70108055231466,
      "fee": 44.85926795981045
    }
  },
  "entry_order_types": {
    "LIMIT": 24,
    "MARKET": 7
  },
  "exit_order_types": {
    "STOP": 31
  },
  "entry_clock_UTC": {
    "Thu 16:12": 1,
    "Fri 04:00": 1,
    "Tue 09:40": 1,
    "Tue 08:02": 1,
    "Tue 15:20": 1,
    "Mon 16:01": 1,
    "Thu 12:01": 1,
    "Tue 13:46": 1,
    "Fri 11:06": 1,
    "Mon 08:34": 1,
    "Tue 12:00": 2,
    "Mon 19:01": 1,
    "Fri 06:02": 1,
    "Thu 16:06": 1,
    "Thu 04:00": 1,
    "Mon 12:02": 1,
    "Mon 16:00": 1,
    "Thu 08:00": 1,
    "Fri 16:04": 2,
    "Fri 12:00": 1,
    "Fri 16:01": 1,
    "Fri 16:06": 1,
    "Tue 18:50": 1,
    "Fri 08:23": 1,
    "Mon 05:04": 1,
    "Mon 17:25": 1,
    "Fri 14:01": 1,
    "Tue 06:20": 1,
    "Wed 16:03": 1
  },
  "terminal_liquidations": [],
  "engine_open_count_preterminal": 0
}
```

Grupo económico exacto: Cq/S04/S05/S06/S09, ver lote2. Camposnull de igualdadS01/S02/S03 significan no comparados por flag completo en lote1, no ausencia de datos; filas de pares exactos sí preservadas. No se selecciona máximo ni se toman variantes idénticas como confirmaciones independientes.