# SPY20 — estadísticas completas persistidas

Diez primarias terminales y referencia contextual reutilizada. No sumar curvas ni agregados de estrategias como cuenta compartida. Cero trades implica cero sumas contables sobre ese conjunto vacío, NO métricas motor de retorno/DD que están ausentes. DatosdecohortesporcierreetiquetadosNO MTM. Los períodos MTM están en reportesroot batch1/batch2.

```json
{
  "spy01": {
    "session_id": "3e887db0-3e26-4405-a62f-100a1f466432",
    "n": 36,
    "net": -197.1576464164274,
    "fees": 129.27355354499784,
    "gross_price": -67.88409287142946,
    "pf": 0.7964419588036036,
    "return_pct": -1.9715764641642743,
    "cagr_engine": -0.38120222680712024,
    "dd_engine": -3.280554372172728,
    "stress5_samefills": -268.9762872747596,
    "stress10_samefills": -340.7949281330916,
    "net_bps_entry": -13.720454350697535,
    "ex_top1": -275.99822141392735,
    "ex_top3": -414.05849678052755,
    "ex_top5": -534.630970171896,
    "side": {
      "short": {
        "n": 19,
        "net": -48.7154938439683,
        "fees": 73.64156444397001
      },
      "long": {
        "n": 17,
        "net": -148.4421525724591,
        "fees": 55.631989101027855
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 2,
        "net": 78.61898291192976,
        "fees": 6.19465908807
      },
      "2021": {
        "n": 3,
        "net": -35.26347347606979,
        "fees": 10.56231887607
      },
      "2022": {
        "n": 7,
        "net": 2.6866037418894706,
        "fees": 15.15541985811
      },
      "2023": {
        "n": 1,
        "net": -22.848591756760193,
        "fees": 3.5980725567599996
      },
      "2024": {
        "n": 8,
        "net": -162.62689571555427,
        "fees": 38.03828515840929
      },
      "2025": {
        "n": 15,
        "net": -57.724272121862406,
        "fees": 55.72479800757857
      }
    },
    "hours": 1447.2333333333336,
    "mean_hours": 40.20092592592593,
    "max_hours": 81.5,
    "crossing_UTC_days": 27,
    "first_entry": "2020-11-09 15:00:00+00:00",
    "last_exit": "2025-12-21 23:30:00+00:00",
    "max_initial_gross_equity": 0.6964095706731175,
    "entry_clock_NY": {
      "10:00": 36
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "fails_economic_screen"
  },
  "spy02": {
    "session_id": "32a9b1f5-ea19-43ff-bd30-17a4a9fb4379",
    "n": 36,
    "net": 174.96780779592152,
    "fees": 128.95286176121786,
    "gross_price": 303.92066955713943,
    "pf": 1.2348049803782244,
    "return_pct": 1.7496780779592152,
    "cagr_engine": 0.33324442199076376,
    "dd_engine": -2.4987424457368346,
    "stress5_samefills": 103.32732903968942,
    "stress10_samefills": 31.68685028345739,
    "net_bps_entry": 12.19822510979252,
    "ex_top1": -128.07741277362354,
    "ex_top3": -320.42526201684416,
    "ex_top5": -454.31557931502357,
    "side": {
      "short": {
        "n": 18,
        "net": 245.82890580098453,
        "fees": 62.27744681330357
      },
      "long": {
        "n": 18,
        "net": -70.861098005063,
        "fees": 66.67541494791428
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": -45.73889415263969,
        "fees": 3.92752455264
      },
      "2021": {
        "n": 5,
        "net": 83.56630870915363,
        "fees": 17.469343990845
      },
      "2022": {
        "n": 8,
        "net": 124.59087789892413,
        "fees": 19.876098058219284
      },
      "2023": {
        "n": 2,
        "net": 74.12845087468513,
        "fees": 6.904937025315
      },
      "2024": {
        "n": 8,
        "net": -28.030704906529778,
        "fees": 36.83212172081357
      },
      "2025": {
        "n": 12,
        "net": -33.54823062767191,
        "fees": 43.942836413385
      }
    },
    "hours": 2698.366666666667,
    "mean_hours": 74.95462962962962,
    "max_hours": 105.5,
    "crossing_UTC_days": 34,
    "first_entry": "2020-12-21 15:00:00+00:00",
    "last_exit": "2025-11-20 17:17:00+00:00",
    "max_initial_gross_equity": 0.6969537339100884,
    "entry_clock_NY": {
      "10:00": 36
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "candidate_descriptive"
  },
  "reference": {
    "session_id": "23c4974f-7503-4afe-8ffa-f69eb78c5ef2",
    "n": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "gross_price": 1037.8232411744636,
    "pf": 1.4930482284215572,
    "return_pct": 7.513477149671152,
    "cagr_engine": 1.3992310944554776,
    "dd_engine": -5.2131810594609025,
    "stress5_samefills": 592.1946448519213,
    "stress10_samefills": 433.0415747367277,
    "net_bps_entry": 23.64310605728177,
    "ex_top1": 349.57799671604494,
    "ex_top3": -298.2237721588764,
    "ex_top5": -757.536337350717,
    "side": {
      "long": {
        "n": 31,
        "net": 751.3477149671149,
        "fees": 286.47552620734854
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fees": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fees": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fees": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 395.7611513896043,
        "fees": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024080012,
        "fees": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.70108055231466,
        "fees": 44.85926795981045
      }
    },
    "hours": 6971.416666666667,
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "crossing_UTC_days": 28,
    "first_entry": "2020-11-05 16:12:00+00:00",
    "last_exit": "2025-10-30 19:22:00+00:00",
    "max_initial_gross_equity": 1.5989937330573134,
    "entry_clock_NY": {
      "11:12": 1,
      "00:00": 2,
      "05:40": 1,
      "04:02": 1,
      "10:20": 1,
      "12:01": 1,
      "08:01": 1,
      "09:46": 1,
      "06:06": 1,
      "04:34": 1,
      "08:00": 2,
      "15:01": 1,
      "02:02": 1,
      "12:06": 1,
      "07:02": 1,
      "11:00": 1,
      "03:00": 1,
      "11:04": 2,
      "07:00": 1,
      "11:01": 1,
      "11:06": 1,
      "14:50": 1,
      "04:23": 1,
      "01:04": 1,
      "12:25": 1,
      "10:01": 1,
      "02:20": 1,
      "12:03": 1
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "candidate_descriptive"
  },
  "spy03": {
    "session_id": "fc9e0fb9-3be4-4d79-9ea6-cd5289ba62f5",
    "n": 25,
    "net": 136.98596740192156,
    "fees": 91.89800579808,
    "gross_price": 228.88397320000155,
    "pf": 1.329481728739323,
    "return_pct": 1.3698596740192157,
    "cagr_engine": 0.2612998578785053,
    "dd_engine": -2.2803257829429824,
    "stress5_samefills": 85.93151973632155,
    "stress10_samefills": 34.87707207072157,
    "net_bps_entry": 13.430727153279474,
    "ex_top1": 61.20054759384114,
    "ex_top3": -56.91391042823889,
    "ex_top5": -152.9790137005738,
    "side": {
      "long": {
        "n": 25,
        "net": 136.98596740192153,
        "fees": 91.89800579807998
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 12.2708384747208,
        "fees": 2.2371067252800003
      },
      "2021": {
        "n": 2,
        "net": 44.38687791819979,
        "fees": 9.7990084818
      },
      "2022": {
        "n": 8,
        "net": -153.07750930995468,
        "fees": 22.796354609955003
      },
      "2023": {
        "n": 4,
        "net": 85.83229202084999,
        "fees": 14.61538677915
      },
      "2024": {
        "n": 5,
        "net": -66.06807563666018,
        "fees": 22.405549236659997
      },
      "2025": {
        "n": 5,
        "net": 213.64154393476582,
        "fees": 20.044599965235
      }
    },
    "hours": 1378.1166666666666,
    "mean_hours": 55.12466666666666,
    "max_hours": 75.5,
    "crossing_UTC_days": 25,
    "first_entry": "2020-11-09 21:00:00+00:00",
    "last_exit": "2025-12-18 15:36:00+00:00",
    "max_initial_gross_equity": 0.628510685210215,
    "entry_clock_NY": {
      "16:00": 25
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "spy04": {
    "session_id": "f9055a4a-00ae-4a77-b153-c9bc811ae2eb",
    "n": 0,
    "net": 0,
    "fees": 0,
    "gross_price": 0,
    "pf": null,
    "return_pct": null,
    "cagr_engine": null,
    "dd_engine": null,
    "stress5_samefills": 0,
    "stress10_samefills": 0,
    "net_bps_entry": null,
    "ex_top1": 0,
    "ex_top3": 0,
    "ex_top5": 0,
    "side": {},
    "closed_trade_year_cohorts_NOT_MTM": {},
    "hours": 0,
    "mean_hours": 0,
    "max_hours": 0,
    "crossing_UTC_days": 0,
    "first_entry": null,
    "last_exit": null,
    "max_initial_gross_equity": 0,
    "entry_clock_NY": {},
    "terminal_liquidations": [],
    "engine_open_count_preterminal": null,
    "classification": "inconclusive_small_sample"
  },
  "spy05": {
    "session_id": "3e5679ee-7c30-4629-a4ac-099c272b1e2d",
    "n": 16,
    "net": -59.15077456283244,
    "fees": 42.59858914854643,
    "gross_price": -16.552185414285987,
    "pf": 0.8747866488612266,
    "return_pct": -0.5915077456283244,
    "cagr_engine": -0.1137247693068888,
    "dd_engine": -3.8008837086290104,
    "stress5_samefills": -82.81665742313601,
    "stress10_samefills": -106.48254028343959,
    "net_bps_entry": -12.49924192571791,
    "ex_top1": -155.53039382937757,
    "ex_top3": -319.6255609375478,
    "ex_top5": -408.4311137352881,
    "side": {
      "short": {
        "n": 16,
        "net": -59.15077456283245,
        "fees": 42.59858914854643
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2022": {
        "n": 9,
        "net": 295.1420413403501,
        "fees": 20.97362365965
      },
      "2023": {
        "n": 4,
        "net": -285.53340127996955,
        "fees": 13.819937951397858
      },
      "2025": {
        "n": 3,
        "net": -68.75941462321299,
        "fees": 7.805027537498572
      }
    },
    "hours": 1866.8333333333333,
    "mean_hours": 116.67708333333334,
    "max_hours": 147.5,
    "crossing_UTC_days": 16,
    "first_entry": "2022-01-19 21:00:00+00:00",
    "last_exit": "2025-04-09 18:21:00+00:00",
    "max_initial_gross_equity": 0.4675289051832201,
    "entry_clock_NY": {
      "16:00": 16
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "spy06": {
    "session_id": "2624be2b-8db2-4400-9858-4bfd67aeabce",
    "n": 2,
    "net": 122.69405032586513,
    "fees": 5.3744911741350005,
    "gross_price": 128.06854150000015,
    "pf": "infinite_no_losses",
    "return_pct": 1.2269405032586513,
    "cagr_engine": 0.2341719301405254,
    "dd_engine": -0.8085152933640538,
    "stress5_samefills": 119.70822189579013,
    "stress10_samefills": 116.72239346571514,
    "net_bps_entry": 207.6876924162591,
    "ex_top1": 45.8541123837,
    "ex_top3": 0,
    "ex_top5": 0,
    "side": {
      "long": {
        "n": 2,
        "net": 122.69405032586513,
        "fees": 5.3744911741350005
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2023": {
        "n": 1,
        "net": 76.83993794216514,
        "fees": 4.163335157835
      },
      "2025": {
        "n": 1,
        "net": 45.854112383700006,
        "fees": 1.2111560163000001
      }
    },
    "hours": 507.5,
    "mean_hours": 253.75,
    "max_hours": 267.5,
    "crossing_UTC_days": 2,
    "first_entry": "2023-08-23 20:00:00+00:00",
    "last_exit": "2025-05-08 20:00:00+00:00",
    "max_initial_gross_equity": 0.45854263166000003,
    "entry_clock_NY": {
      "16:00": 2
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "spy07": {
    "session_id": "9f03cc46-9c01-4856-9a1a-5bab7387f2da",
    "n": 12,
    "net": 77.12745458315025,
    "fees": 51.781553773990716,
    "gross_price": 128.90900835714095,
    "pf": 1.1613931609589867,
    "return_pct": 0.7712745458315026,
    "cagr_engine": 0.14747339174248086,
    "dd_engine": -3.211751217725589,
    "stress5_samefills": 48.35992470871095,
    "stress10_samefills": 19.592394834271673,
    "net_bps_entry": 13.420331011785025,
    "ex_top1": -71.29369725424924,
    "ex_top3": -259.7768618122485,
    "ex_top5": -408.6447113423078,
    "side": {
      "long": {
        "n": 12,
        "net": 77.12745458315027,
        "fees": 51.781553773990716
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2021": {
        "n": 3,
        "net": 222.42754868721022,
        "fees": 8.42152491279
      },
      "2024": {
        "n": 5,
        "net": -116.5515620301766,
        "fees": 23.33973834446143
      },
      "2025": {
        "n": 4,
        "net": -28.748532073883325,
        "fees": 20.020290516739287
      }
    },
    "hours": 1271.0333333333333,
    "mean_hours": 105.91944444444444,
    "max_hours": 147.5,
    "crossing_UTC_days": 12,
    "first_entry": "2021-03-04 21:00:00+00:00",
    "last_exit": "2025-12-23 21:00:00+00:00",
    "max_initial_gross_equity": 0.7014941626489013,
    "entry_clock_NY": {
      "16:00": 12
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "spy08": {
    "session_id": "f4252286-205b-4fa0-8111-c36f00d4e9a3",
    "n": 10,
    "net": -21.711902588186234,
    "fees": 26.04316734532928,
    "gross_price": 4.331264757143067,
    "pf": 0.9197764668651996,
    "return_pct": -0.21711902588186235,
    "cagr_engine": -0.04168053925869275,
    "dd_engine": -2.987188078249936,
    "stress5_samefills": -36.18032889114693,
    "stress10_samefills": -50.64875519410765,
    "net_bps_entry": -7.50263965743355,
    "ex_top1": -117.56659344250137,
    "ex_top3": -205.80817071212678,
    "ex_top5": -256.20133363185676,
    "side": {
      "short": {
        "n": 10,
        "net": -21.711902588186234,
        "fees": 26.04316734532928
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2022": {
        "n": 5,
        "net": 234.4894310436705,
        "fees": 11.292156156329998
      },
      "2024": {
        "n": 1,
        "net": -75.02669519781941,
        "fees": 2.5187761978199994
      },
      "2025": {
        "n": 4,
        "net": -181.17463843403732,
        "fees": 12.232234991179286
      }
    },
    "hours": 1184.4333333333334,
    "mean_hours": 118.44333333333331,
    "max_hours": 147.5,
    "crossing_UTC_days": 10,
    "first_entry": "2022-04-25 20:00:00+00:00",
    "last_exit": "2025-11-23 23:30:00+00:00",
    "max_initial_gross_equity": 0.45746899746003644,
    "entry_clock_NY": {
      "16:00": 10
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "spy09": {
    "session_id": "f2461e76-9adc-4adb-9677-8e8ef4791a6d",
    "n": 23,
    "net": -213.647491784976,
    "fees": 87.27374229926143,
    "gross_price": -126.37374948571455,
    "pf": 0.6573322602017723,
    "return_pct": -2.13647491784976,
    "cagr_engine": -0.4133651378726233,
    "dd_engine": -4.090442515704762,
    "stress5_samefills": -262.13290417345456,
    "stress10_samefills": -310.6183165619331,
    "net_bps_entry": -22.01779439480002,
    "ex_top1": -291.80577045443573,
    "ex_top3": -430.7997833199002,
    "ex_top5": -529.0611168162204,
    "side": {
      "long": {
        "n": 23,
        "net": -213.6474917849759,
        "fees": 87.27374229926143
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2021": {
        "n": 2,
        "net": -97.94056244725802,
        "fees": 8.798783618687143
      },
      "2022": {
        "n": 3,
        "net": -241.29791584774526,
        "fees": 7.636902347745
      },
      "2023": {
        "n": 2,
        "net": 70.16317750360506,
        "fees": 7.064187796395
      },
      "2024": {
        "n": 4,
        "net": -60.491339435004235,
        "fees": 18.104429335005
      },
      "2025": {
        "n": 12,
        "net": 115.91914844142647,
        "fees": 45.66943920142928
      }
    },
    "hours": 2604.9333333333334,
    "mean_hours": 113.25797101449275,
    "max_hours": 123.5,
    "crossing_UTC_days": 23,
    "first_entry": "2021-05-11 20:00:00+00:00",
    "last_exit": "2025-11-18 15:05:00+00:00",
    "max_initial_gross_equity": 0.6330784550620301,
    "entry_clock_NY": {
      "16:00": 23
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "spy10": {
    "session_id": "cb0d1d11-8695-44d9-8a2f-20a7f1cf3183",
    "n": 0,
    "net": 0,
    "fees": 0,
    "gross_price": 0,
    "pf": null,
    "return_pct": null,
    "cagr_engine": null,
    "dd_engine": null,
    "stress5_samefills": 0,
    "stress10_samefills": 0,
    "net_bps_entry": null,
    "ex_top1": 0,
    "ex_top3": 0,
    "ex_top5": 0,
    "side": {},
    "closed_trade_year_cohorts_NOT_MTM": {},
    "hours": 0,
    "mean_hours": 0,
    "max_hours": 0,
    "crossing_UTC_days": 0,
    "first_entry": null,
    "last_exit": null,
    "max_initial_gross_equity": 0,
    "entry_clock_NY": {},
    "terminal_liquidations": [],
    "engine_open_count_preterminal": null,
    "classification": "inconclusive_small_sample"
  }
}
```
