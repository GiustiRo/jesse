# N204 R4 — diagnóstico de trayectorias validado

[D400 retry B](http://localhost:9200/#/backtest/c26a2bbc-d960-4a13-873b-07e52f57b05b),[D400 retry C](http://localhost:9200/#/backtest/cacecd6c-6f04-46d4-b456-5b667010bee8). Comparación ejecutada enrun_analysis job25e703b4972645fe932465cacf5895fb: paridad exacta273/280trades frenteN204B/C, maxΔPNL0, iguales fills,qty,precios,fechas,fees y métricas. Cada una de79filas se une al BTCshortMARKET real poropened_at; se comprobaron también closed_at,entry,exit,qty. 79/79con cobertura completa de minutos elegibles,ne=n,errores0,sin observaciónabierta.

Hay19salidas2R,21stops1R y39timeouts48h. Las79operaciones son los mismos eventos B/C, NO158observaciones independientes. PNLneto suplemento2856.514711B/2836.631155C. La distanciainicialdse conserva sin normalizarporPAXG/SPY ni porfee.

Mediana MFE observada0.777R yMAE0.583R. Entre42ganadoras netas,MFE mediana1.519R; entre37no positivas,0.316R.32casos registran MFE>=1R,todos del grupo ganador. Esto NO prueba que ningúnperdedor tocara1R: se excluyen los minutos parciales de entrada y de salida; son cotas inferiores, sin orden intraminuto. Tampoco justifica imponer1R después de ver estos datos. Los cuatro T estaban definidos previamente y no se ajustan.

Horizontes6/12/24h tienen74/66/51observaciones y5/13/28cierres anteriores o simultáneos,0missing; sus medianas están condicionadas a seguirabierto y no son proyecciones contrafácticas. Agrupar por resultado final es diagnóstico retrospectivo, nunca una regla disponible en la entrada. La ausencia de gaps sólo valida los minutos esperados de esta captura, no exactitudexterna ni liquidezreal.

2026cerrado incluso a inspección. Toda la muestra2020-10-15→2025-12-31exclusiva es desarrollo reutilizado, no OOS. Los2reruns corrigen el corteAPI porlínea y se cuentan aparte delpresupuesto26–32; fuentes operativas intactas.

```json
{
  "B": {
    "fill_clock_join_pass": true,
    "coverage_79_of_79": true,
    "all": {
      "n": 79,
      "net": 2856.514710837504,
      "MFE_lower_bound_R": {
        "q25": 0.3015475614167751,
        "median": 0.7771206248491174,
        "q75": 1.540793908166776
      },
      "MAE_lower_bound_R": {
        "q25": 0.2719527167474314,
        "median": 0.5833473202796631,
        "q75": 0.8385111005223135
      },
      "observed_MFE_at_least_1R": 32,
      "observed_MAE_at_least_halfR": 43,
      "horizons": {
        "6": {
          "observed": 74,
          "closed_before_or_at": 5,
          "missing": 0,
          "median_R_observable_only": 0.02354409446307676
        },
        "12": {
          "observed": 66,
          "closed_before_or_at": 13,
          "missing": 0,
          "median_R_observable_only": 0.10441354236353965
        },
        "24": {
          "observed": 51,
          "closed_before_or_at": 28,
          "missing": 0,
          "median_R_observable_only": -0.004397413155393522
        }
      }
    },
    "positive_net": {
      "n": 42,
      "net": 6795.004008289457,
      "MFE_lower_bound_R": {
        "q25": 1.0210898825287735,
        "median": 1.5186043098564288,
        "q75": 1.8679733177073279
      },
      "MAE_lower_bound_R": {
        "q25": 0.15451300638550183,
        "median": 0.29840878661032155,
        "q75": 0.5837690523235143
      },
      "observed_MFE_at_least_1R": 32,
      "observed_MAE_at_least_halfR": 12,
      "horizons": {
        "6": {
          "observed": 40,
          "closed_before_or_at": 2,
          "missing": 0,
          "median_R_observable_only": 0.09738597294711049
        },
        "12": {
          "observed": 37,
          "closed_before_or_at": 5,
          "missing": 0,
          "median_R_observable_only": 0.28221338962750436
        },
        "24": {
          "observed": 31,
          "closed_before_or_at": 11,
          "missing": 0,
          "median_R_observable_only": 0.5464301282230218
        }
      }
    },
    "nonpositive_net": {
      "n": 37,
      "net": -3938.4892974519516,
      "MFE_lower_bound_R": {
        "q25": 0.16278632985019123,
        "median": 0.31598820292130186,
        "q75": 0.4986083271357872
      },
      "MAE_lower_bound_R": {
        "q25": 0.6019677387479934,
        "median": 0.8118164207746957,
        "q75": 0.9748364459659793
      },
      "observed_MFE_at_least_1R": 0,
      "observed_MAE_at_least_halfR": 31,
      "horizons": {
        "6": {
          "observed": 34,
          "closed_before_or_at": 3,
          "missing": 0,
          "median_R_observable_only": -0.11270554775074099
        },
        "12": {
          "observed": 29,
          "closed_before_or_at": 8,
          "missing": 0,
          "median_R_observable_only": -0.12098171074178064
        },
        "24": {
          "observed": 20,
          "closed_before_or_at": 17,
          "missing": 0,
          "median_R_observable_only": -0.12754696174289404
        }
      }
    },
    "counts": {
      "target2R": 19,
      "stop1R": 21,
      "timeout48h": 39
    }
  },
  "C": {
    "fill_clock_join_pass": true,
    "coverage_79_of_79": true,
    "all": {
      "n": 79,
      "net": 2836.6311553139217,
      "MFE_lower_bound_R": {
        "q25": 0.3015475614167751,
        "median": 0.7771206248491174,
        "q75": 1.540793908166776
      },
      "MAE_lower_bound_R": {
        "q25": 0.2719527167474314,
        "median": 0.5833473202796631,
        "q75": 0.8385111005223135
      },
      "observed_MFE_at_least_1R": 32,
      "observed_MAE_at_least_halfR": 43,
      "horizons": {
        "6": {
          "observed": 74,
          "closed_before_or_at": 5,
          "missing": 0,
          "median_R_observable_only": 0.02354409446307676
        },
        "12": {
          "observed": 66,
          "closed_before_or_at": 13,
          "missing": 0,
          "median_R_observable_only": 0.10441354236353965
        },
        "24": {
          "observed": 51,
          "closed_before_or_at": 28,
          "missing": 0,
          "median_R_observable_only": -0.004397413155393522
        }
      }
    },
    "positive_net": {
      "n": 42,
      "net": 6763.696645596143,
      "MFE_lower_bound_R": {
        "q25": 1.0210898825287735,
        "median": 1.5186043098564288,
        "q75": 1.8679733177073279
      },
      "MAE_lower_bound_R": {
        "q25": 0.15451300638550183,
        "median": 0.29840878661032155,
        "q75": 0.5837690523235143
      },
      "observed_MFE_at_least_1R": 32,
      "observed_MAE_at_least_halfR": 12,
      "horizons": {
        "6": {
          "observed": 40,
          "closed_before_or_at": 2,
          "missing": 0,
          "median_R_observable_only": 0.09738597294711049
        },
        "12": {
          "observed": 37,
          "closed_before_or_at": 5,
          "missing": 0,
          "median_R_observable_only": 0.28221338962750436
        },
        "24": {
          "observed": 31,
          "closed_before_or_at": 11,
          "missing": 0,
          "median_R_observable_only": 0.5464301282230218
        }
      }
    },
    "nonpositive_net": {
      "n": 37,
      "net": -3927.06549028222,
      "MFE_lower_bound_R": {
        "q25": 0.16278632985019123,
        "median": 0.31598820292130186,
        "q75": 0.4986083271357872
      },
      "MAE_lower_bound_R": {
        "q25": 0.6019677387479934,
        "median": 0.8118164207746957,
        "q75": 0.9748364459659793
      },
      "observed_MFE_at_least_1R": 0,
      "observed_MAE_at_least_halfR": 31,
      "horizons": {
        "6": {
          "observed": 34,
          "closed_before_or_at": 3,
          "missing": 0,
          "median_R_observable_only": -0.11270554775074099
        },
        "12": {
          "observed": 29,
          "closed_before_or_at": 8,
          "missing": 0,
          "median_R_observable_only": -0.12098171074178064
        },
        "24": {
          "observed": 20,
          "closed_before_or_at": 17,
          "missing": 0,
          "median_R_observable_only": -0.12754696174289404
        }
      }
    },
    "counts": {
      "target2R": 19,
      "stop1R": 21,
      "timeout48h": 39
    }
  }
}
```
