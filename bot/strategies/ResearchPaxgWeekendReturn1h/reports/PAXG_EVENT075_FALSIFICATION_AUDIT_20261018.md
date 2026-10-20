# PAXG 0,75 ATR: auditoría de controles

Job fd4426de9efd4a01b1bf74b37f8a27f9 succeeded / exit 0. Snapshots completos: 60 trades de referencia 0,75 pasiva, 188 del control hábil 0,75 y 60 del estrés de ejecución 0,75. Cohortes de cierre no son retorno anual MTM. Entradas del estrés y referencia coinciden en timestamps y sentidos; error máximo de precio 4,55e−13.

```json
{
  "passive075": {
    "session_id": "ff199ebe-dab0-4c09-9078-fff98188e97c",
    "trades": 60,
    "net": 764.0355793467394,
    "fees": 414.3192701936172,
    "before_fees": 1178.3548495403566,
    "pf_net": 1.7317509045979385,
    "annual_return_engine": 1.4221718304768594,
    "dd_engine": -2.990690170671495,
    "sharpe_engine": 0.744986681862599,
    "directions": {
      "short": {
        "n": 42,
        "net": 821.2603218360483,
        "wins": 32
      },
      "long": {
        "n": 18,
        "net": -57.224742489308916,
        "wins": 10
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 3,
        "net": 133.49872632610044
      },
      "2021": {
        "n": 9,
        "net": 78.27333818556586
      },
      "2022": {
        "n": 9,
        "net": 241.5001311414926
      },
      "2023": {
        "n": 17,
        "net": 123.2046939996445
      },
      "2024": {
        "n": 12,
        "net": 177.67280505569028
      },
      "2025": {
        "n": 10,
        "net": 9.88588463824573
      }
    },
    "recent_closed_cohort_2023_2025": 310.7633836935805,
    "recent_5bps_static": 146.42706856408057,
    "recent_10bps_static": -17.909246565419554,
    "entry_notional_sum": 460862.956764,
    "net_bps_over_entry_notional": 16.57836821408905,
    "gross_bps_over_entry_notional": 25.568443552380625,
    "extra_roundtrip_5bps_static_samefills": 533.6041009647394,
    "extra_roundtrip_10bps_static_samefills": 303.1726225827394,
    "top3_winners_net": 302.3193192659005,
    "top3_share_of_net": 0.39568748817219684,
    "net_ex_top3_descriptive": 461.7162600808389,
    "total_holding_hours": 659.7999999999997,
    "time_exposure_pct": 1.4446488001401292,
    "mean_hold_hours": 10.996666666666666,
    "median_hold_hours": 7.916666666666667,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.1940281478992703,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.4566126083082054e-12,
      "max_qty_error": 0.0,
      "wallet_delta": -5.4569682106375694e-12,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "24.0": 15
      },
      "ordertypes": {
        "entry_MARKET": 60,
        "exit_MARKET": 15,
        "exit_LIMIT": 37,
        "exit_STOP": 8
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000.0,
      "value": 10000.0,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200.0,
      "value": 10764.035579346746,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "weekday075": {
    "session_id": "62e11d8f-f098-44df-8b6f-2861a0503811",
    "trades": 188,
    "net": -1171.4029846192202,
    "fees": 1306.5648915515833,
    "before_fees": 135.16190693236308,
    "pf_net": 0.7568847650824209,
    "annual_return_engine": -2.3613207622707133,
    "dd_engine": -12.708985731063116,
    "sharpe_engine": -0.6425233976984623,
    "directions": {
      "short": {
        "n": 108,
        "net": -821.4709886709419,
        "wins": 59
      },
      "long": {
        "n": 80,
        "net": -349.93199594827854,
        "wins": 44
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 8,
        "net": -70.4912735647413
      },
      "2021": {
        "n": 28,
        "net": -367.6152873778329
      },
      "2022": {
        "n": 35,
        "net": -196.28377609723228
      },
      "2023": {
        "n": 42,
        "net": 86.4884111149451
      },
      "2024": {
        "n": 33,
        "net": -6.104236025224054
      },
      "2025": {
        "n": 42,
        "net": -617.3968226691348
      }
    },
    "recent_closed_cohort_2023_2025": -537.0126475794139,
    "recent_5bps_static": -1007.154331553414,
    "recent_10bps_static": -1477.2960155274145,
    "entry_notional_sum": 1451626.732941,
    "net_bps_over_entry_notional": -8.06958812508195,
    "gross_bps_over_entry_notional": 0.9311064880881923,
    "extra_roundtrip_5bps_static_samefills": -1897.2163510897203,
    "extra_roundtrip_10bps_static_samefills": -2623.02971756022,
    "top3_winners_net": 419.43247278695003,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -1590.8354574061702,
    "total_holding_hours": 3588.1833333333334,
    "time_exposure_pct": 7.856418228528056,
    "mean_hold_hours": 19.086081560283688,
    "median_hold_hours": 24.0,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.5183315574962806,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.5223378113660146e-12,
      "max_qty_error": 0.0,
      "wallet_delta": 1.6370904631912708e-11,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "24.0": 97
      },
      "ordertypes": {
        "entry_MARKET": 188,
        "exit_LIMIT": 46,
        "exit_MARKET": 97,
        "exit_STOP": 45
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000.0,
      "value": 10000.0,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200.0,
      "value": 8828.59701538077,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "stress075": {
    "session_id": "d75e1a23-0429-4b61-800e-a1cb24835459",
    "trades": 60,
    "net": 768.170694544663,
    "fees": 413.7194261038445,
    "before_fees": 1181.8901206485075,
    "pf_net": 1.7358715196237493,
    "annual_return_engine": 1.4296437478665602,
    "dd_engine": -2.990724365225994,
    "sharpe_engine": 0.7154034875250569,
    "directions": {
      "short": {
        "n": 42,
        "net": 709.6268536877855,
        "wins": 32
      },
      "long": {
        "n": 18,
        "net": 58.54384085687762,
        "wins": 10
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 3,
        "net": 134.48591300350063
      },
      "2021": {
        "n": 9,
        "net": 55.72250180852362
      },
      "2022": {
        "n": 9,
        "net": 211.57605470823208
      },
      "2023": {
        "n": 17,
        "net": 236.06869488014632
      },
      "2024": {
        "n": 12,
        "net": 133.20620348187583
      },
      "2025": {
        "n": 10,
        "net": -2.8886733376154083
      }
    },
    "recent_closed_cohort_2023_2025": 366.38622502440677,
    "recent_5bps_static": 202.2877441764067,
    "recent_10bps_static": 38.18926332840671,
    "entry_notional_sum": 460082.94828400004,
    "net_bps_over_entry_notional": 16.69635219931008,
    "gross_bps_over_entry_notional": 25.688631257834626,
    "extra_roundtrip_5bps_static_samefills": 538.1292204026629,
    "extra_roundtrip_10bps_static_samefills": 308.0877462606629,
    "top3_winners_net": 412.8121239110514,
    "top3_share_of_net": 0.5373963454252155,
    "net_ex_top3_descriptive": 355.3585706336116,
    "total_holding_hours": 679.45,
    "time_exposure_pct": 1.4876729724995623,
    "mean_hold_hours": 11.324166666666667,
    "median_hold_hours": 8.5,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.1940224343888557,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.2647660696529783e-12,
      "max_qty_error": 0.0,
      "wallet_delta": 0.0,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {},
      "ordertypes": {
        "entry_MARKET": 60,
        "exit_MARKET": 52,
        "exit_STOP": 8
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000.0,
      "value": 10000.0,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200.0,
      "value": 10768.170694544653,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "entry_match_passive_vs_stress": {
    "count": 60,
    "timestamps_and_directions_equal": true,
    "max_price_delta": 4.547473508864641e-13
  }
}
```
