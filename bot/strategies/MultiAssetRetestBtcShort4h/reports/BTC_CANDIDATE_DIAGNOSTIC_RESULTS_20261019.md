# BTC — diagnóstico consolidado de candidatos tras R6

## Resultado

N204 conserva mejor regularidad estática; N503 mejora cartera con un suplemento menos rentable y más cortos originales; P604 protege ganancias en cuatro casos pero su ventaja marginal es concentrada. Ninguno se promociona. 2026 cerrado incluso a inspección. Ventana2020-10-15→2025-12-31 exclusiva; misma muestra reutilizada, noOOS.

N503 frente a N204: delta cartera+272.10/+297.46USDT. Suplemento79→67; su neto cae257.11/258.84USDT, STOP113→116 mejora433.80/431.35. La descomposición exacta por entradas compartidas atribuye140.54/180.93USDT a diferencias de cantidad, y131.56/116.53 al saldo de altas/bajas. No es atribución causal. Omitir aritméticamente el MTM incremental de2023 deja−132.92/−119.83USDT: evidencia de concentración temporal de la ventaja.

P604 frente a N503: cambia4salidas, todas en trades que N503 ya cerraba con beneficio;2mejoran y2empeoran. Efecto de salida a cantidad base+57.47/+55.96USDT;2STOPadicionales suman−11.49/−6.83; componente cantidad−26.73/−23.82; delta final+19.25/+25.31. Omitir sólo el componente de la mejor salida deja el componente directo de las otras tres en−12.77/−13.33; la diferencia de cartera ajustada aritméticamente queda−50.99/−43.98. Esto no reejecuta capital, posiciones ni reglas. C sigue40/63meses positivos bajo5bpsadicionales.

P603 es contraste: cumple regularidad pero pierde aproximadamente913/929USDTfrenteN204. Preparación técnica no implica una orden asequible ni una ejecución. La siguiente investigación debe separar defensa de ganancias de convivencia, registrar oportunidades sin alterar órdenes y mantener estrictamente intactos los originales.

## Ejecución del análisis

Joba454bd0f40334d2f952d2b6852f6c455 succeeded. Seis sesiones completas y cuatro anclas históricas. Código/protocolo: strategies/MultiAssetRetestBtcShort4h/reports/BTC_CANDIDATE_DIAGNOSTIC_PROTOCOL_20261019.md. El intento de lectura de PNG devolvióartifact_changed dos veces; no hay evidencia de que sea causado por número de estrategias. Recuperaciones de texto, fuentes y reportes responden normalmente al retomar. No se borraron fuentes ni sesiones.

## Sesiones

- [N204B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142)
- [N204C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794)
- [N503B](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752)
- [N503C](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65)
- [P604C](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb)
- [P604B](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52)

## Comparativas completas

### N204B__N503B

```json
{
  "base": "N204B",
  "new": "N503B",
  "delta": 272.09679773826156,
  "groups": {
    "BTC-USDT:long:LIMIT": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 27,
        "delta": -5.480137218674011,
        "path_base_qty": -1.5517471751991255e-12,
        "quantity_effect": -5.480137218672569
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 4,
        "delta": 6.518940960941535,
        "path_base_qty": -2.7857822715304793e-12,
        "quantity_effect": 6.51894096094431
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:MARKET": {
      "added": {
        "n": 1,
        "delta": 44.400339620000366,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 13,
        "delta": -322.7989303376587,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 66,
        "delta": 21.2891269105931,
        "path_base_qty": -1.9922197225241685e-12,
        "quantity_effect": 21.289126910595098
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:STOP": {
      "added": {
        "n": 3,
        "delta": 409.95881591016735,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 113,
        "delta": 23.83651009329865,
        "path_base_qty": 4.461753633222544e-12,
        "quantity_effect": 23.83651009329402
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "PAXG-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 38,
        "delta": 66.30435489416558,
        "path_base_qty": 5.718743073535039e-12,
        "quantity_effect": 66.30435489416006
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "SPY-USDT:long:LIMIT": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 9,
        "delta": 24.558706121059572,
        "path_base_qty": -2.3217578970502473e-12,
        "quantity_effect": 24.55870612106189
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "SPY-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 3,
        "delta": 3.509070784368106,
        "path_base_qty": -5.99516036814407e-12,
        "quantity_effect": 3.509070784374095
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    }
  },
  "changed_same_entry_executions": [],
  "changed_path_effect_sum_at_base_qty": 0,
  "omit_one_changed_path_component_arithmetic": [],
  "quantity_component_all_matched": 140.53657254575685,
  "added_and_removed_component": 131.560225192509,
  "all_matched_path_component": -4.466170727690508e-12,
  "year_delta_MTM": {
    "2020": 0,
    "2021": -72.90188103549735,
    "2022": 87.3283107686093,
    "2023": 405.01430376222015,
    "2024": 74.43740092361622,
    "2025": -221.78133668067676
  },
  "delta_omitting_each_recorded_year": {
    "2020": 272.09679773826156,
    "2021": 344.9986787737589,
    "2022": 184.76848696965226,
    "2023": -132.9175060239586,
    "2024": 197.65939681464533,
    "2025": 493.8781344189383
  },
  "months_improve": 40,
  "months_worsen": 19,
  "extra5_rescued_months": [
    {
      "month": "2023-05",
      "delta_nominal": 152.97710350059606,
      "delta_after5": 157.71836067689676,
      "delta_after10": 162.45961785319747,
      "base_after5": -125.51368848546394,
      "new_after5": 32.20467219143282
    }
  ],
  "extra5_lost_months": [
    {
      "month": "2021-01",
      "delta_nominal": -70.93173499237128,
      "delta_after5": -71.11833507962223,
      "delta_after10": -71.30493516687318,
      "base_after5": 61.94559039726213,
      "new_after5": -9.172744682360097
    }
  ],
  "delta_without_best_incremental_month_arithmetic": 112.51472928379826,
  "best_incremental_month": {
    "month": "2023-10",
    "delta_nominal": 159.5820684544633,
    "delta_after5": 161.73901859110856,
    "delta_after10": 163.89596872775383,
    "base_after5": -269.1785182991312,
    "new_after5": -107.43949970802265
  },
  "top3_positive_ledger_deltas": [
    {
      "group": "BTC-USDT:short:STOP",
      "kind": "added",
      "delta": 163.91501801021673,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2022-12-15T16:51:00+00:00",
      "close": "2022-12-16T09:02:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "removed",
      "delta": 162.2109820910198,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2023-10-18T12:00:00+00:00",
      "close": "2023-10-20T03:18:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "removed",
      "delta": 153.9464785280649,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2023-05-21T12:00:00+00:00",
      "close": "2023-05-23T03:19:00+00:00"
    }
  ],
  "limitations": "Accounting decomposition of recorded portfolios, endogenous sizing and occupancy. Omissions do NOT replay execution, capital or gates. No causal or OOS inference; no p-values after selection."
}
```

### N204C__N503C

```json
{
  "base": "N204C",
  "new": "N503C",
  "delta": 297.4601332126087,
  "groups": {
    "BTC-USDT:long:LIMIT": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 27,
        "delta": 5.5783227951491625,
        "path_base_qty": -9.178862114822553e-13,
        "quantity_effect": 5.578322795150091
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 4,
        "delta": 4.8315386968614575,
        "path_base_qty": 1.389253156958148e-12,
        "quantity_effect": 4.831538696860088
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:MARKET": {
      "added": {
        "n": 1,
        "delta": 43.32178886000035,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 13,
        "delta": -332.56535034406124,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 66,
        "delta": 30.405642261344653,
        "path_base_qty": 9.285912483392168e-12,
        "quantity_effect": 30.405642261335533
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:STOP": {
      "added": {
        "n": 3,
        "delta": 405.77532275955645,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 113,
        "delta": 25.57580789563307,
        "path_base_qty": 1.0796270544233267e-11,
        "quantity_effect": 25.575807895622162
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "PAXG-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 38,
        "delta": 68.5956403327266,
        "path_base_qty": -1.0658782290118297e-11,
        "quantity_effect": 68.59564033273709
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "SPY-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 19,
        "delta": 45.941419955398054,
        "path_base_qty": -2.3369830515207467e-12,
        "quantity_effect": 45.941419955400384
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    }
  },
  "changed_same_entry_executions": [],
  "changed_path_effect_sum_at_base_qty": 0,
  "omit_one_changed_path_component_arithmetic": [],
  "quantity_component_all_matched": 180.92837193710534,
  "added_and_removed_component": 116.53176127549561,
  "all_matched_path_component": 7.55778463146229e-12,
  "year_delta_MTM": {
    "2020": 0,
    "2021": -63.82971253784126,
    "2022": 83.56625363574494,
    "2023": 417.2901000535858,
    "2024": 73.62851916740328,
    "2025": -213.19502710629968
  },
  "delta_omitting_each_recorded_year": {
    "2020": 297.4601332126087,
    "2021": 361.28984575044996,
    "2022": 213.89387957686375,
    "2023": -119.82996684097708,
    "2024": 223.8316140452054,
    "2025": 510.6551603189084
  },
  "months_improve": 40,
  "months_worsen": 20,
  "extra5_rescued_months": [],
  "extra5_lost_months": [
    {
      "month": "2021-01",
      "delta_nominal": -70.9317349923731,
      "delta_after5": -71.11833507962405,
      "delta_after10": -71.304935166875,
      "base_after5": 61.96236843060358,
      "new_after5": -9.155966649020467
    }
  ],
  "delta_without_best_incremental_month_arithmetic": 141.91115435463252,
  "best_incremental_month": {
    "month": "2023-10",
    "delta_nominal": 155.54897885797618,
    "delta_after5": 157.64724465797323,
    "delta_after10": 159.74551045797028,
    "base_after5": -262.7293973186098,
    "new_after5": -105.08215266063658
  },
  "top3_positive_ledger_deltas": [
    {
      "group": "BTC-USDT:short:STOP",
      "kind": "added",
      "delta": 161.23277226095863,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2022-12-15T16:51:00+00:00",
      "close": "2022-12-16T09:02:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "removed",
      "delta": 158.60629360010887,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2023-10-18T12:00:00+00:00",
      "close": "2023-10-20T03:18:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "removed",
      "delta": 150.0436100583368,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2023-05-21T12:00:00+00:00",
      "close": "2023-05-23T03:19:00+00:00"
    }
  ],
  "limitations": "Accounting decomposition of recorded portfolios, endogenous sizing and occupancy. Omissions do NOT replay execution, capital or gates. No causal or OOS inference; no p-values after selection."
}
```

### N503B__P604B

```json
{
  "base": "N503B",
  "new": "P604B",
  "delta": 19.252421877522636,
  "groups": {
    "BTC-USDT:long:LIMIT": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 27,
        "delta": -21.042442814368627,
        "path_base_qty": 2.607976057333872e-13,
        "quantity_effect": -21.04244281436881
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 4,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 63,
        "delta": 1.1078881373446272,
        "path_base_qty": -6.47418119115173e-13,
        "quantity_effect": 1.107888137345292
      },
      "changed_execution": {
        "n": 4,
        "delta": 60.93710475066678,
        "path_base_qty": 57.47040448266679,
        "quantity_effect": 3.4667002680000034
      }
    },
    "BTC-USDT:short:STOP": {
      "added": {
        "n": 2,
        "delta": -11.489889339142607,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 116,
        "delta": -12.06484020722175,
        "path_base_qty": -1.6729018170735797e-12,
        "quantity_effect": -12.064840207220035
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "PAXG-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 38,
        "delta": -0.02438583628904567,
        "path_base_qty": 6.7447834595224526e-12,
        "quantity_effect": -0.02438583629586466
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "SPY-USDT:long:LIMIT": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 9,
        "delta": 2.075361474676015,
        "path_base_qty": 1.3721166425284537e-12,
        "quantity_effect": 2.0753614746746885
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "SPY-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 3,
        "delta": -0.24637428814276063,
        "path_base_qty": 3.7275516007184705e-14,
        "quantity_effect": -0.24637428814278
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    }
  },
  "changed_same_entry_executions": [
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2021-08-23T20:00:00+00:00",
      "base_close": "2021-08-25T20:00:00+00:00",
      "new_close": "2021-08-25T00:00:00+00:00",
      "base_net": 42.55814484700017,
      "new_net": 112.79723822200016,
      "delta": 70.23909337499998,
      "base_qty": 0.074,
      "new_qty": 0.074,
      "base_hold_h": 48,
      "new_hold_h": 28,
      "path_effect_at_base_qty": 70.23909337499998,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 116.68524457618946,
      "new_net_bps_entry_notional": 309.26567351021504
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2021-11-10T20:00:00+00:00",
      "base_close": "2021-11-12T20:00:00+00:00",
      "new_close": "2021-11-12T16:00:00+00:00",
      "base_net": 111.54020870000004,
      "new_net": 142.13471098800002,
      "delta": 30.594502287999987,
      "base_qty": 0.04,
      "new_qty": 0.041,
      "base_hold_h": 48,
      "new_hold_h": 44,
      "path_effect_at_base_qty": 27.127802019999983,
      "quantity_effect_at_new_unit_PNL": 3.4667002680000034,
      "base_net_bps_entry_notional": 417.8157465972092,
      "new_net_bps_entry_notional": 519.4331183650241
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2024-10-31T16:00:00+00:00",
      "base_close": "2024-11-02T16:00:00+00:00",
      "new_close": "2024-11-01T04:00:00+00:00",
      "base_net": 86.26302580499977,
      "new_net": 85.99280425999999,
      "delta": -0.2702215449997851,
      "base_qty": 0.073,
      "new_qty": 0.073,
      "base_hold_h": 48,
      "new_hold_h": 12,
      "path_effect_at_base_qty": -0.27022154499977113,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 167.28581995421732,
      "new_net_bps_entry_notional": 166.7617920488344
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2024-12-18T04:00:00+00:00",
      "base_close": "2024-12-19T01:59:00+00:00",
      "new_close": "2024-12-19T00:00:00+00:00",
      "base_net": 355.11448146233323,
      "new_net": 315.4882120949998,
      "delta": -39.62626936733341,
      "base_qty": 0.07100000000000001,
      "new_qty": 0.07100000000000001,
      "base_hold_h": 21.983333333333334,
      "new_hold_h": 20,
      "path_effect_at_base_qty": -39.626269367333414,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 477.632282018018,
      "new_net_bps_entry_notional": 424.33458098413973
    }
  ],
  "changed_path_effect_sum_at_base_qty": 57.47040448266679,
  "omit_one_changed_path_component_arithmetic": [
    {
      "omit_event_open": "2021-08-23T20:00:00+00:00",
      "direct_path_delta_omitting_one": -12.768688892333195,
      "recorded_portfolio_delta_minus_event_path_component": -50.986671497477346
    },
    {
      "omit_event_open": "2021-11-10T20:00:00+00:00",
      "direct_path_delta_omitting_one": 30.342602462666804,
      "recorded_portfolio_delta_minus_event_path_component": -7.875380142477347
    },
    {
      "omit_event_open": "2024-10-31T16:00:00+00:00",
      "direct_path_delta_omitting_one": 57.74062602766656,
      "recorded_portfolio_delta_minus_event_path_component": 19.522643422522407
    },
    {
      "omit_event_open": "2024-12-18T04:00:00+00:00",
      "direct_path_delta_omitting_one": 97.0966738500002,
      "recorded_portfolio_delta_minus_event_path_component": 58.87869124485605
    }
  ],
  "quantity_component_all_matched": -26.728093266007495,
  "added_and_removed_component": -11.489889339142607,
  "all_matched_path_component": 57.470404482672876,
  "year_delta_MTM": {
    "2020": 0,
    "2021": -16.99393725005575,
    "2022": -3.7616900882821938,
    "2023": -5.63788814662621,
    "2024": 45.350199984924984,
    "2025": 0.2957373775607266
  },
  "delta_omitting_each_recorded_year": {
    "2020": 19.252421877522636,
    "2021": 36.24635912757839,
    "2022": 23.01411196580483,
    "2023": 24.890310024148846,
    "2024": -26.09777810740235,
    "2025": 18.95668449996191
  },
  "months_improve": 20,
  "months_worsen": 23,
  "extra5_rescued_months": [],
  "extra5_lost_months": [],
  "delta_without_best_incremental_month_arithmetic": -49.2772901339311,
  "best_incremental_month": {
    "month": "2021-08",
    "delta_nominal": 68.52971201145374,
    "delta_after5": 68.52353725013967,
    "delta_after10": 68.5173624888256,
    "base_after5": -375.87935068045743,
    "new_after5": -307.35581343031777
  },
  "top3_positive_ledger_deltas": [
    {
      "group": "BTC-USDT:short:STOP",
      "kind": "added",
      "delta": 105.53353917482202,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2024-12-19T01:59:00+00:00",
      "close": "2024-12-19T18:20:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "changed_execution",
      "delta": 70.23909337499998,
      "path_base_qty": 70.23909337499998,
      "qty_effect": 0,
      "open": "2021-08-23T20:00:00+00:00",
      "close": "2021-08-25T00:00:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "changed_execution",
      "delta": 30.594502287999987,
      "path_base_qty": 27.127802019999983,
      "qty_effect": 3.4667002680000034,
      "open": "2021-11-10T20:00:00+00:00",
      "close": "2021-11-12T16:00:00+00:00"
    }
  ],
  "limitations": "Accounting decomposition of recorded portfolios, endogenous sizing and occupancy. Omissions do NOT replay execution, capital or gates. No causal or OOS inference; no p-values after selection."
}
```

### N503C__P604C

```json
{
  "base": "N503C",
  "new": "P604C",
  "delta": 25.312630001084692,
  "groups": {
    "BTC-USDT:long:LIMIT": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 27,
        "delta": -26.132154995863928,
        "path_base_qty": -2.906972440541722e-13,
        "quantity_effect": -26.13215499586384
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 4,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 63,
        "delta": -0.5951449196632268,
        "path_base_qty": -2.8989006750634874e-12,
        "quantity_effect": -0.5951449196603344
      },
      "changed_execution": {
        "n": 4,
        "delta": 55.959409410204614,
        "path_base_qty": 55.95940941020462,
        "quantity_effect": 0
      }
    },
    "BTC-USDT:short:STOP": {
      "added": {
        "n": 2,
        "delta": -6.827631768995815,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 116,
        "delta": 0.5363540106755238,
        "path_base_qty": -3.460826292212005e-12,
        "quantity_effect": 0.5363540106790174
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "PAXG-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 38,
        "delta": 0.9066861088477864,
        "path_base_qty": 9.446508020261037e-13,
        "quantity_effect": 0.9066861088472113
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    },
    "SPY-USDT:long:MARKET": {
      "added": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "removed": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      },
      "same_execution": {
        "n": 19,
        "delta": 1.4651121558797513,
        "path_base_qty": 1.1615997941305523e-11,
        "quantity_effect": 1.4651121558679894
      },
      "changed_execution": {
        "n": 0,
        "delta": 0,
        "path_base_qty": 0,
        "quantity_effect": 0
      }
    }
  },
  "changed_same_entry_executions": [
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2021-08-23T20:00:00+00:00",
      "base_close": "2021-08-25T20:00:00+00:00",
      "new_close": "2021-08-25T00:00:00+00:00",
      "base_net": 41.983034781500166,
      "new_net": 111.27295121900016,
      "delta": 69.2899164375,
      "base_qty": 0.073,
      "new_qty": 0.073,
      "base_hold_h": 48,
      "new_hold_h": 28,
      "path_effect_at_base_qty": 69.28991643750001,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 116.68524457618946,
      "new_net_bps_entry_notional": 309.26567351021504
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2021-11-10T20:00:00+00:00",
      "base_close": "2021-11-12T20:00:00+00:00",
      "new_close": "2021-11-12T16:00:00+00:00",
      "base_net": 111.54020870000004,
      "new_net": 138.6680107200003,
      "delta": 27.12780202000026,
      "base_qty": 0.04,
      "new_qty": 0.04,
      "base_hold_h": 48,
      "new_hold_h": 44,
      "path_effect_at_base_qty": 27.127802020000253,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 417.8157465972092,
      "new_net_bps_entry_notional": 519.4331183650253
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2024-10-31T16:00:00+00:00",
      "base_close": "2024-11-02T16:00:00+00:00",
      "new_close": "2024-11-01T04:00:00+00:00",
      "base_net": 87.44471108999979,
      "new_net": 87.17078787999999,
      "delta": -0.27392320999979347,
      "base_qty": 0.074,
      "new_qty": 0.074,
      "base_hold_h": 48,
      "new_hold_h": 12,
      "path_effect_at_base_qty": -0.2739232099997848,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 167.28581995421735,
      "new_net_bps_entry_notional": 166.76179204883442
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "open": "2024-12-18T04:00:00+00:00",
      "base_close": "2024-12-19T01:59:00+00:00",
      "new_close": "2024-12-19T00:00:00+00:00",
      "base_net": 360.11609387729567,
      "new_net": 319.9317080399998,
      "delta": -40.18438583729585,
      "base_qty": 0.07200000000000001,
      "new_qty": 0.07200000000000001,
      "base_hold_h": 21.983333333333334,
      "new_hold_h": 20,
      "path_effect_at_base_qty": -40.18438583729586,
      "quantity_effect_at_new_unit_PNL": 0,
      "base_net_bps_entry_notional": 477.6322820180181,
      "new_net_bps_entry_notional": 424.3345809841398
    }
  ],
  "changed_path_effect_sum_at_base_qty": 55.95940941020462,
  "omit_one_changed_path_component_arithmetic": [
    {
      "omit_event_open": "2021-08-23T20:00:00+00:00",
      "direct_path_delta_omitting_one": -13.33050702729539,
      "recorded_portfolio_delta_minus_event_path_component": -43.97728643641532
    },
    {
      "omit_event_open": "2021-11-10T20:00:00+00:00",
      "direct_path_delta_omitting_one": 28.83160739020437,
      "recorded_portfolio_delta_minus_event_path_component": -1.8151720189155611
    },
    {
      "omit_event_open": "2024-10-31T16:00:00+00:00",
      "direct_path_delta_omitting_one": 56.23333262020441,
      "recorded_portfolio_delta_minus_event_path_component": 25.586553211084478
    },
    {
      "omit_event_open": "2024-12-18T04:00:00+00:00",
      "direct_path_delta_omitting_one": 96.14379524750048,
      "recorded_portfolio_delta_minus_event_path_component": 65.49701583838055
    }
  ],
  "quantity_component_all_matched": -23.81914764012996,
  "added_and_removed_component": -6.827631768995815,
  "all_matched_path_component": 55.95940941021052,
  "year_delta_MTM": {
    "2020": 0,
    "2021": -16.00263891754912,
    "2022": -0.22442105878326402,
    "2023": -3.837237065901718,
    "2024": 47.84014069872501,
    "2025": -2.4632136554137105
  },
  "delta_omitting_each_recorded_year": {
    "2020": 25.312630001084692,
    "2021": 41.31526891863381,
    "2022": 25.537051059867956,
    "2023": 29.14986706698641,
    "2024": -22.527510697640317,
    "2025": 27.775843656498402
  },
  "months_improve": 22,
  "months_worsen": 26,
  "extra5_rescued_months": [],
  "extra5_lost_months": [],
  "delta_without_best_incremental_month_arithmetic": -43.97728643641472,
  "best_incremental_month": {
    "month": "2021-08",
    "delta_nominal": 69.28991643749941,
    "delta_after5": 69.30723112499942,
    "delta_after10": 69.32454581249942,
    "base_after5": -366.58172180142356,
    "new_after5": -297.27449067642414
  },
  "top3_positive_ledger_deltas": [
    {
      "group": "BTC-USDT:short:STOP",
      "kind": "added",
      "delta": 107.98780752772421,
      "path_base_qty": 0,
      "qty_effect": 0,
      "open": "2024-12-19T01:59:00+00:00",
      "close": "2024-12-19T18:20:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "changed_execution",
      "delta": 69.2899164375,
      "path_base_qty": 69.28991643750001,
      "qty_effect": 0,
      "open": "2021-08-23T20:00:00+00:00",
      "close": "2021-08-25T00:00:00+00:00"
    },
    {
      "group": "BTC-USDT:short:MARKET",
      "kind": "changed_execution",
      "delta": 27.12780202000026,
      "path_base_qty": 27.127802020000253,
      "qty_effect": 0,
      "open": "2021-11-10T20:00:00+00:00",
      "close": "2021-11-12T16:00:00+00:00"
    }
  ],
  "limitations": "Accounting decomposition of recorded portfolios, endogenous sizing and occupancy. Omissions do NOT replay execution, capital or gates. No causal or OOS inference; no p-values after selection."
}
```