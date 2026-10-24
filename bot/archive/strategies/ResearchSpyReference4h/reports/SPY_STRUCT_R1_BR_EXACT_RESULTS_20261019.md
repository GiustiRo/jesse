# Structural R1 BR — seis filas exactas

Seis nuevos fulls finished; referenciasCq/M existentes no rerun. Auditoría completa8snapshots succeeded43639f36bc2c4a60911d6558528dff69, costes/PnL/balance/tamaño reconciliados. DD/CAGR/Sharpe del motor. Exposición temporal fracción de ventana; entrynotionaltime=precioentrada×qty×duración/(10k×ventana), NO MTM. Stress estático5/10bpsRT mismosfills/sizes. Cohortes por cierre NO retornosMTM anuales. Sin redondeo.

```json
[
  {
    "id": "bb193097-9600-4ca0-94a5-434bb1c30e1b",
    "control": "BR01",
    "name": "SpyStructR1BR01",
    "dashboard_url": "http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b",
    "N": 24,
    "net": 71.82254556636093,
    "fees": 209.42311948805448,
    "gross_price": 281.2456650544155,
    "PF": 1.056700075118146,
    "DDmotor": -6.697704900221568,
    "CAGR": 0.1373592818407765,
    "Sharpe": 0.06587705134787052,
    "timeexposure": 0.10037769311613243,
    "entrynotionaltime": 0.09325670050269083,
    "stress5": -44.523631927002555,
    "stress10": -160.8698094203663,
    "exbest": -304.56704758893335,
    "ex3": -836.4792929987366,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 2,
        "net": -1.669740719287958,
        "fee": 22.82665381564336
      },
      "2022": {
        "n": 5,
        "net": -205.62835179669645,
        "fee": 28.422052764555534
      },
      "2023": {
        "n": 5,
        "net": 267.07480844473315,
        "fee": 43.26826827596431
      },
      "2024": {
        "n": 7,
        "net": -100.10449957972207,
        "fee": 72.88209316484331
      },
      "2025": {
        "n": 5,
        "net": 112.15032921733436,
        "fee": 42.02405146704797
      }
    },
    "mean_hours": 191.01875,
    "max_hours": 820.6166666666667,
    "entry_turnover_initial_equity": 23.25517321542,
    "roundtrip_turnover_initial_equity": 46.53847099734545,
    "net_bps_entry": 3.0884545516408783,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 5,
      "LIMIT": 19
    },
    "exit_order_types": {
      "STOP": 24
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "f89d7afb-9876-4e7e-9ddf-78ff85137810",
    "control": "BR02",
    "name": "SpyStructR1BR02",
    "dashboard_url": "http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810",
    "N": 16,
    "net": 874.7958565504186,
    "fees": 150.5940012513908,
    "gross_price": 1025.3898578018095,
    "PF": 2.320269711623377,
    "DDmotor": -3.8005064163188162,
    "CAGR": 1.6215132040717561,
    "Sharpe": 0.7183938780138998,
    "timeexposure": 0.0878747737490512,
    "entrynotionaltime": 0.08121036182627324,
    "stress5": 791.1325225218683,
    "stress10": 707.4691884933177,
    "exbest": 455.51451397897824,
    "ex3": -86.35598247698874,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -67.92668184187508,
        "fee": 63.022585116543596
      },
      "2024": {
        "n": 3,
        "net": 345.7151991124811,
        "fee": 34.721055221010076
      },
      "2025": {
        "n": 2,
        "net": 323.3476595470383,
        "fee": 17.94832618586981
      }
    },
    "mean_hours": 250.83854166666666,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 16.68139731282,
    "roundtrip_turnover_initial_equity": 33.46533361142018,
    "net_bps_entry": 52.44140164913643,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "exit_order_types": {
      "STOP": 16
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "4921c591-e830-43be-80c0-c1ac795ecc41",
    "control": "BR03",
    "name": "SpyStructR1BR03",
    "dashboard_url": "http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41",
    "N": 10,
    "net": 223.87119915761406,
    "fees": 89.19180028306832,
    "gross_price": 313.06299944068246,
    "PF": 1.5903257638471178,
    "DDmotor": -4.392481438329177,
    "CAGR": 0.4255574507011861,
    "Sharpe": 0.2630170740044828,
    "timeexposure": 0.06053928008407777,
    "entrynotionaltime": 0.04762433559715391,
    "stress5": 174.3201990003539,
    "stress10": 124.76919884309369,
    "exbest": -61.23865740684636,
    "ex3": -309.78683385175583,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 168.79131639148233,
        "fee": 3.5746040598531006
      },
      "2021": {
        "n": 2,
        "net": 268.6161524958744,
        "fee": 19.27791202001215
      },
      "2022": {
        "n": 2,
        "net": -100.72028437883203,
        "fee": 12.935218434415013
      },
      "2023": {
        "n": 3,
        "net": -262.01933130244146,
        "fee": 31.481508511173928
      },
      "2024": {
        "n": 2,
        "net": 149.20334595153088,
        "fee": 21.922557257614116
      }
    },
    "mean_hours": 276.495,
    "max_hours": 822.1666666666666,
    "entry_turnover_initial_equity": 9.89454688148,
    "roundtrip_turnover_initial_equity": 19.820400062904067,
    "net_bps_entry": 22.625715137763642,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 10
    },
    "exit_order_types": {
      "STOP": 10
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "6f66fc51-6829-4ee0-80f9-ba26943ba75f",
    "control": "BR04",
    "name": "SpyStructR1BR04",
    "dashboard_url": "http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f",
    "N": 7,
    "net": 628.9148646426152,
    "fees": 63.12680740865307,
    "gross_price": 692.0416720512683,
    "PF": 5.848766864542775,
    "DDmotor": -2.1673204184637918,
    "CAGR": 1.176730342441079,
    "Sharpe": 0.6611886061903214,
    "timeexposure": 0.044701348747591525,
    "entrynotionaltime": 0.04394532849820264,
    "stress5": 593.8444160822523,
    "stress10": 558.7739675218895,
    "exbest": 221.0011224060616,
    "ex3": -54.55566604832984,
    "cohorts_closing_trades_NOT_MTM": {
      "2022": {
        "n": 1,
        "net": 70.07919006361743,
        "fee": 5.1693320781638015
      },
      "2023": {
        "n": 1,
        "net": -90.1917512977791,
        "fee": 9.420528322361061
      },
      "2024": {
        "n": 3,
        "net": 236.04239338294934,
        "fee": 31.766761970799188
      },
      "2025": {
        "n": 2,
        "net": 412.9850324938274,
        "fee": 16.77018503732902
      }
    },
    "mean_hours": 291.65714285714284,
    "max_hours": 804.6666666666666,
    "entry_turnover_initial_equity": 6.97948762847,
    "roundtrip_turnover_initial_equity": 14.028179424145126,
    "net_bps_entry": 90.10903065107689,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 7
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "8932b93b-d380-4699-8f7c-d2fd895553f1",
    "control": "BR05",
    "name": "SpyStructR1BR05",
    "dashboard_url": "http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1",
    "N": 4,
    "net": 430.81350793008016,
    "fees": 36.95623692905661,
    "gross_price": 467.76974485913684,
    "PF": 5.782747241747338,
    "DDmotor": -1.8290474850964356,
    "CAGR": 0.8122879761032875,
    "Sharpe": 0.6842669387065272,
    "timeexposure": 0.03453757225433526,
    "entrynotionaltime": 0.026053608983243024,
    "stress5": 410.28226519171534,
    "stress10": 389.7510224533506,
    "exbest": 153.90279356307514,
    "ex3": -90.07657861774987,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 164.5483325029549,
        "fee": 3.57618405228986
      },
      "2021": {
        "n": 1,
        "net": 276.910714367005,
        "fee": 10.713420991961534
      },
      "2023": {
        "n": 1,
        "net": -90.07657861774982,
        "fee": 12.86937260999651
      },
      "2024": {
        "n": 1,
        "net": 79.43103967787007,
        "fee": 9.797259274808704
      }
    },
    "mean_hours": 394.35,
    "max_hours": 822.0833333333334,
    "entry_turnover_initial_equity": 4.08286006043,
    "roundtrip_turnover_initial_equity": 8.212497095345913,
    "net_bps_entry": 105.51757874471642,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "STOP": 4
    },
    "exit_order_types": {
      "STOP": 4
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "fb232660-27f5-47d8-a6c4-fb9b152f95da",
    "control": "BR06",
    "name": "SpyStructR1BR06",
    "dashboard_url": "http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da",
    "N": 4,
    "net": 179.58819064449804,
    "fees": 38.814248200700334,
    "gross_price": 218.4024388451984,
    "PF": 2.03562089214586,
    "DDmotor": -2.622662998859071,
    "CAGR": 0.341981458962648,
    "Sharpe": 0.3133417131115916,
    "timeexposure": 0.019883079348397267,
    "entrynotionaltime": 0.02099137606857476,
    "stress5": 158.02471942188677,
    "stress10": 136.46124819927547,
    "exbest": -93.45644719997168,
    "ex3": -87.88560287973482,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 1,
        "net": 273.0446378444697,
        "fee": 10.539941477364826
      },
      "2023": {
        "n": 2,
        "net": -173.41113143476855,
        "fee": 18.715986848075985
      },
      "2024": {
        "n": 1,
        "net": 79.95468423479687,
        "fee": 9.558319875259524
      }
    },
    "mean_hours": 227.025,
    "max_hours": 465.68333333333334,
    "entry_turnover_initial_equity": 4.3017741225799995,
    "roundtrip_turnover_initial_equity": 8.62538848904452,
    "net_bps_entry": 41.74747104963976,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "STOP": 2,
      "MARKET": 2
    },
    "exit_order_types": {
      "STOP": 4
    },
    "engine_open_count_preterminal": 0
  }
]
```

## Referencias

```json
{
  "Cq": {
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
  },
  "M": {
    "session_id": "64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "n": 38,
    "net": 151.6012639172099,
    "gross_price": 488.3315562886899,
    "fee": 336.73029237147995,
    "PF": 1.074122772361648,
    "return_pct": 1.516012639172099,
    "CAGR_engine_pct": 0.28900965265155065,
    "Sharpe_engine": 0.10588870453443279,
    "DD_engine_pct": -7.718707541843617,
    "hours_open": 7305.716666666666,
    "fraction_time_open": 0.15996051556022653,
    "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.1446681109984161,
    "entry_turnover_initial_equity": 37.390060352350005,
    "roundtrip_turnover_initial_equity": 74.82895386032888,
    "net_bps_entry": 4.054587301774217,
    "net_per_exposure_entry_time_measure": 0.10479245417040782,
    "max_initial_gross_equity": 1.5992931529349965,
    "mean_hours": 192.25570175438597,
    "max_hours": 842.1666666666666,
    "stress5_RT_samefills": -35.47112073361228,
    "stress10_RT_samefills": -222.54350538443452,
    "net_without_top1": -224.7296691424284,
    "net_without_top3": -864.90548009341,
    "net_without_top5": -1306.5405470655624,
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 144.46030476585108,
        "fee": 3.2856353550544073
      },
      "2021": {
        "n": 5,
        "net": 234.68215351049457,
        "fee": 52.67854808982013
      },
      "2022": {
        "n": 6,
        "net": -412.947657460623,
        "fee": 33.94331524034087
      },
      "2023": {
        "n": 10,
        "net": 325.2519289120968,
        "fee": 90.9032396483522
      },
      "2024": {
        "n": 10,
        "net": -145.8798868876506,
        "fee": 103.61885607926621
      },
      "2025": {
        "n": 6,
        "net": 6.034421077041072,
        "fee": 52.30069795864606
      }
    },
    "entry_order_types": {
      "MARKET": 38
    },
    "exit_order_types": {
      "STOP": 37,
      "MARKET": 1
    },
    "entry_clock_UTC": {
      "Thu 12:00": 2,
      "Tue 04:00": 3,
      "Fri 04:00": 2,
      "Fri 16:00": 6,
      "Tue 08:00": 1,
      "Tue 12:00": 4,
      "Mon 16:00": 4,
      "Mon 08:00": 1,
      "Fri 08:00": 2,
      "Thu 04:00": 4,
      "Thu 16:00": 2,
      "Mon 12:00": 1,
      "Tue 16:00": 2,
      "Thu 08:00": 1,
      "Mon 04:00": 1,
      "Fri 12:00": 1,
      "Wed 16:00": 1
    },
    "terminal_liquidations": [
      "5664a1ca-00dc-4ece-9064-aeb07980f28f"
    ],
    "engine_open_count_preterminal": 1
  }
}
```