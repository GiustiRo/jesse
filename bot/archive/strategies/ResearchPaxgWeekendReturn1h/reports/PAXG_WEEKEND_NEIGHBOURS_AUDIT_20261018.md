# PAXG: auditoría completa de vecinos

Job 1ceab28985404f65ab73a7bb72fd9925 succeeded / exit 0. Snapshots completos de 60 / 37 / 24 trades. Las cohortes por año de cierre no son retornos anuales MTM. La primaria sigue en EVENT_ATR = 1.0.

```json
{
  "n075": {
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
  "primary": {
    "session_id": "2da06c02-d246-43a0-b265-8837aa9c4be5",
    "trades": 37,
    "net": 400.2243628684158,
    "fees": 259.1256715182893,
    "before_fees": 659.3500343867051,
    "pf_net": 1.5072644677252123,
    "annual_return_engine": 0.7555162665411785,
    "dd_engine": -2.06221309007516,
    "sharpe_engine": 0.42992675556129295,
    "directions": {
      "short": {
        "n": 26,
        "net": 487.2472754749277,
        "wins": 18
      },
      "long": {
        "n": 11,
        "net": -87.02291260651188,
        "wins": 5
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 1,
        "net": 84.73908699299996
      },
      "2021": {
        "n": 7,
        "net": 12.89340612638722
      },
      "2022": {
        "n": 8,
        "net": 337.41607281500035
      },
      "2023": {
        "n": 10,
        "net": -43.72986978672829
      },
      "2024": {
        "n": 7,
        "net": 6.893209608487602
      },
      "2025": {
        "n": 4,
        "net": 2.0124571122689474
      }
    },
    "recent_closed_cohort_2023_2025": -34.82420306597174,
    "entry_notional_sum": 288249.445395,
    "net_bps_over_entry_notional": 13.88465335362474,
    "gross_bps_over_entry_notional": 22.87428631417385,
    "extra_roundtrip_5bps_static_samefills": 256.0996401709158,
    "extra_roundtrip_10bps_static_samefills": 111.97491747341581,
    "top3_winners_net": 297.3027657460501,
    "top3_share_of_net": 0.742840249941996,
    "net_ex_top3_descriptive": 102.92159712236571,
    "total_holding_hours": 459.46666666666675,
    "time_exposure_pct": 1.0060138961873066,
    "mean_hold_hours": 12.41801801801802,
    "median_hold_hours": 10.15,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.1940217806810443,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.3358203432289883e-12,
      "max_qty_error": 0.0,
      "wallet_delta": -1.8189894035458565e-12,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "24.0": 12
      },
      "ordertypes": {
        "entry_MARKET": 37,
        "exit_LIMIT": 19,
        "exit_STOP": 6,
        "exit_MARKET": 12
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
      "value": 10400.224362868414,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "n125": {
    "session_id": "dd08508d-0124-44a7-99e8-4d2806e18790",
    "trades": 24,
    "net": 80.20648387861993,
    "fees": 166.36722147159057,
    "before_fees": 246.5737053502105,
    "pf_net": 1.1249788455366942,
    "annual_return_engine": 0.15334176225960672,
    "dd_engine": -1.933977115646246,
    "sharpe_engine": 0.10784087866136384,
    "directions": {
      "short": {
        "n": 18,
        "net": 109.80184232667922,
        "wins": 10
      },
      "long": {
        "n": 6,
        "net": -29.595358448059265,
        "wins": 3
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 1,
        "net": 84.73908699299996
      },
      "2021": {
        "n": 4,
        "net": -129.25582431610036
      },
      "2022": {
        "n": 2,
        "net": 79.35862548999945
      },
      "2023": {
        "n": 8,
        "net": 38.84006556978463
      },
      "2024": {
        "n": 5,
        "net": 4.569702731941604
      },
      "2025": {
        "n": 4,
        "net": 1.9548274099946639
      }
    },
    "recent_closed_cohort_2023_2025": 45.364595711720895,
    "entry_notional_sum": 184958.561309,
    "net_bps_over_entry_notional": 4.336456950734139,
    "gross_bps_over_entry_notional": 13.33129451295166,
    "extra_roundtrip_5bps_static_samefills": -12.272796775880067,
    "extra_roundtrip_10bps_static_samefills": -104.75207743038007,
    "top3_winners_net": 292.9899051357501,
    "top3_share_of_net": 3.6529453850532194,
    "net_ex_top3_descriptive": -212.7834212571302,
    "total_holding_hours": 292.9000000000001,
    "time_exposure_pct": 0.641311963566299,
    "mean_hold_hours": 12.204166666666666,
    "median_hold_hours": 9.358333333333334,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.1940212909407226,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 6.821210263296962e-13,
      "max_qty_error": 0.0,
      "wallet_delta": -1.8189894035458565e-12,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "24.0": 8
      },
      "ordertypes": {
        "entry_MARKET": 24,
        "exit_LIMIT": 10,
        "exit_STOP": 6,
        "exit_MARKET": 8
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
      "value": 10080.206483878623,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  }
}
```
