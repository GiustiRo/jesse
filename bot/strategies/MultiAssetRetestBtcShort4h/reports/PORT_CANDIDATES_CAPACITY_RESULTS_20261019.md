# Portfolio — contadores de capacidad y equivalencia final

Las primarias no persistieron logs con debugfalse. Se ejecutaron cuatro réplicas debugtrue con los mismos códigos/configuración económica, para recuperar12JSON PORT_CAPACITY por MCP. Son repeticiones de captura, no variantes nuevas ni evidencia independiente. Las ocho ejecuciones terminaron. Rutas, fechas, snapshots y configuración económica comprobados.

Los trades económicos completos, cantidades, precios,PNL,fees,timestamps yfills ejecutados son EXACTOS en4/4 pares (hashes idénticos). Las curvas son byte-exactas paraB/C y equivalentes numéricamente paraCONTROL/A: timestamps y1904puntos iguales; diferencia máxima3.64e-12USDT en16/9puntos, respectivamente. No afirmar cuatro hashes de curva iguales. Métricas derivadas de curva también pueden reflejar ese redondeo. Job inicial860e4312396e4a6f9fa5b409066d49d8 y seguimiento a37ac71dbee84379ac8046cb17f906cc, ambos succeeded. Se acepta identidad de las operaciones y equivalencia numérica de curvas, no identidad byte por byte4/4.

BTC entre las cuatro primarias conserva156entradas/salidas con dirección ytimestamps EXACTOS. Precios difieren como máximo2.91e-11USDT y cumplenrtol1e-10/atol1e-8. Cantidades yPNL son endógenos; no decir que BTC tieneidéntico PNLni omitir ese matiz. El chequeo exacto inicial de precios falló sólo por estas diferencias numéricas.

No hubo capacidad nula, lotes redondeados a cero, recorte por margen ni por presupuesto agregado8% en ningún intento contado. Hubo18–19recortes de tamaño BTCshort por nocional/peso, no rechazos completos. Ese contador no distingue techo global vs cuota de volatilidad; las categorías de límites pueden solaparse. Sólo cuenta planes que llegan a sizing flat/sinpending. No cubre señales ocupadas ni demuestra que una oportunidad rechazada habría llenado.

| Cartera | BTC long intentos | BTC short intentos | BTC short recortados | PAXG intentos | SPY intentos | Capacidad nula |
|---|---:|---:|---:|---:|---:|---:|
| CONTROL | 45 | 212 | 19 | 55 | 47 | 0 |
| A | 45 | 212 | 19 | 38 | 47 | 0 |
| B | 45 | 212 | 19 | 38 | 20 | 0 |
| C | 45 | 212 | 18 | 38 | 19 | 0 |

Intentos no son fills: BTC31long/125short en cada cartera, PAXG35/38 ySPY31/31/12/19. Las diferencias entre órdenes intentadas y trades no se atribuyen a margen: STOP/LIMIT pueden expirar sin fill. Las fuentes conservan el comentario original que esperaba persistencia debugfalse; este runner no la produjo, lo que motivó captura adicional y quedó documentado.

## Hashes exactos iniciales

```json
{
  "CONTROL": {
    "primary": {
      "trade_hash": "0c242eb911addafc1f98b502e0f127662c301c790905426fadbd02afbaedd29e",
      "equity_hash": "d8ed887c3608fff31f6f9fe04f0cf50291eb16c59c809e52fcdd861eb6cfc5a3",
      "n": 222
    },
    "diagnostic": {
      "trade_hash": "0c242eb911addafc1f98b502e0f127662c301c790905426fadbd02afbaedd29e",
      "equity_hash": "6e41f3b0e781cc347c4387e681dce77beb039ad0693fd82309ee76b2de85e3d5",
      "n": 222
    },
    "economic_identity": false,
    "primary_net": 7815.591290800872,
    "diagnostic_net": 7815.591290800872,
    "primary_debug": false,
    "diagnostic_debug": true
  },
  "A": {
    "primary": {
      "trade_hash": "3467496955d1982157304f8bcb77316a784fca709d9e33a3860f458d09efd3fa",
      "equity_hash": "2833bcc79d9702689ecb7eea040388cbf5a04c8158a038fe371b4cffc57c2358",
      "n": 225
    },
    "diagnostic": {
      "trade_hash": "3467496955d1982157304f8bcb77316a784fca709d9e33a3860f458d09efd3fa",
      "equity_hash": "f37ebdbcf33f32a89bed988a52f174c4d6e9aca9ab1dfa4de5981ae0596aa0a0",
      "n": 225
    },
    "economic_identity": false,
    "primary_net": 8527.169363478119,
    "diagnostic_net": 8527.169363478119,
    "primary_debug": false,
    "diagnostic_debug": true
  },
  "B": {
    "primary": {
      "trade_hash": "74ed0c4ad306f3977eb81f134bbe83cd59e54f0bcee3c06c10d5e2531ace4202",
      "equity_hash": "89f8d2c942db5ce0f591f70cb50395aa7532aebbd15e9ca70cd3e391ae07e520",
      "n": 206
    },
    "diagnostic": {
      "trade_hash": "74ed0c4ad306f3977eb81f134bbe83cd59e54f0bcee3c06c10d5e2531ace4202",
      "equity_hash": "89f8d2c942db5ce0f591f70cb50395aa7532aebbd15e9ca70cd3e391ae07e520",
      "n": 206
    },
    "economic_identity": true,
    "primary_net": 9234.194391279196,
    "diagnostic_net": 9234.194391279196,
    "primary_debug": false,
    "diagnostic_debug": true
  },
  "C": {
    "primary": {
      "trade_hash": "460235579444ee8c6cd0d2cc717505e674e360ca45b92c1709282c24227296f6",
      "equity_hash": "6650b9f040b0af96f9dcb86806e443b61d9592c6b0f4a4d0e89482b8cf2d7ad7",
      "n": 213
    },
    "diagnostic": {
      "trade_hash": "460235579444ee8c6cd0d2cc717505e674e360ca45b92c1709282c24227296f6",
      "equity_hash": "6650b9f040b0af96f9dcb86806e443b61d9592c6b0f4a4d0e89482b8cf2d7ad7",
      "n": 213
    },
    "economic_identity": true,
    "primary_net": 9407.82622551297,
    "diagnostic_net": 9407.82622551297,
    "primary_debug": false,
    "diagnostic_debug": true
  }
}
```

## Revisión numérica

```json
{
  "diagnostic_curves": {
    "CONTROL": {
      "curve_count_equal": true,
      "curves": {
        "Portfolio": {
          "names_equal": true,
          "counts": [
            1904,
            1904
          ],
          "timestamps_equal": true,
          "max_abs_difference": 3.637978807091713e-12,
          "numerically_equal_rtol1e-12_atol1e-8": true,
          "different_values_count": 16
        }
      },
      "same_primary_metrics": false
    },
    "A": {
      "curve_count_equal": true,
      "curves": {
        "Portfolio": {
          "names_equal": true,
          "counts": [
            1904,
            1904
          ],
          "timestamps_equal": true,
          "max_abs_difference": 3.637978807091713e-12,
          "numerically_equal_rtol1e-12_atol1e-8": true,
          "different_values_count": 9
        }
      },
      "same_primary_metrics": false
    },
    "B": {
      "curve_count_equal": true,
      "curves": {
        "Portfolio": {
          "names_equal": true,
          "counts": [
            1904,
            1904
          ],
          "timestamps_equal": true,
          "max_abs_difference": 0,
          "numerically_equal_rtol1e-12_atol1e-8": true,
          "different_values_count": 0
        }
      },
      "same_primary_metrics": true
    },
    "C": {
      "curve_count_equal": true,
      "curves": {
        "Portfolio": {
          "names_equal": true,
          "counts": [
            1904,
            1904
          ],
          "timestamps_equal": true,
          "max_abs_difference": 0,
          "numerically_equal_rtol1e-12_atol1e-8": true,
          "different_values_count": 0
        }
      },
      "same_primary_metrics": true
    }
  },
  "btc_decisions": {
    "A": {
      "n": 156,
      "timestamps_sides_exact": true,
      "max_abs_price_difference": {
        "entry_price": 1.4551915228366852e-11,
        "exit_price": 1.4551915228366852e-11
      },
      "prices_equal_rtol1e-10_atol1e-8": true
    },
    "B": {
      "n": 156,
      "timestamps_sides_exact": true,
      "max_abs_price_difference": {
        "entry_price": 1.4551915228366852e-11,
        "exit_price": 1.4551915228366852e-11
      },
      "prices_equal_rtol1e-10_atol1e-8": true
    },
    "C": {
      "n": 156,
      "timestamps_sides_exact": true,
      "max_abs_price_difference": {
        "entry_price": 2.9103830456733704e-11,
        "exit_price": 1.4551915228366852e-11
      },
      "prices_equal_rtol1e-10_atol1e-8": true
    }
  }
}
```

## Contadores exactos

```json
{
  "CONTROL": [
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 45,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        },
        "short": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 212,
          "margin_limited": 0,
          "notional_or_weight_limited": 19,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 19,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareBtc4h",
      "symbol": "BTC-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 55,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortComparePaxgRetest4h",
      "symbol": "PAXG-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 47,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareSpyRetest4h",
      "symbol": "SPY-USDT",
      "trade_risk": 0.01
    }
  ],
  "A": [
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 45,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        },
        "short": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 212,
          "margin_limited": 0,
          "notional_or_weight_limited": 19,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 19,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareBtc4h",
      "symbol": "BTC-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 38,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortComparePaxgMarket4h",
      "symbol": "PAXG-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 47,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareSpyRetest4h",
      "symbol": "SPY-USDT",
      "trade_risk": 0.01
    }
  ],
  "B": [
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 45,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        },
        "short": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 212,
          "margin_limited": 0,
          "notional_or_weight_limited": 19,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 19,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareBtc4h",
      "symbol": "BTC-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 38,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortComparePaxgMarket4h",
      "symbol": "PAXG-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 20,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareSpySecond4h",
      "symbol": "SPY-USDT",
      "trade_risk": 0.01
    }
  ],
  "C": [
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 45,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        },
        "short": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 212,
          "margin_limited": 0,
          "notional_or_weight_limited": 18,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 18,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareBtc4h",
      "symbol": "BTC-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 38,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortComparePaxgMarket4h",
      "symbol": "PAXG-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 19,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareSpyMarket4h",
      "symbol": "SPY-USDT",
      "trade_risk": 0.01
    }
  ]
}
```

## Fuente del seguimiento

```python
import json, math
from pathlib import Path
import numpy as np
pairs=[('CONTROL','DIAG_CONTROL'),('A','DIAG_A'),('B','DIAG_B'),('C','DIAG_C')]
out={}
for a,b in pairs:
    sa=json.loads(Path('inputs/'+a+'.json').read_text());sb=json.loads(Path('inputs/'+b+'.json').read_text())
    curves={}
    for ca,cb in zip(sa['equity_curve'],sb['equity_curve']):
        da,db=ca['data'],cb['data'];ts_equal=[p['time'] for p in da]==[p['time'] for p in db]
        va=np.array([p['value'] for p in da],float);vb=np.array([p['value'] for p in db],float)
        same_shape=va.shape==vb.shape
        curves[ca['name']]={'names_equal':ca['name']==cb['name'],'counts':[len(da),len(db)],'timestamps_equal':ts_equal,
            'max_abs_difference':float(np.max(np.abs(va-vb))) if same_shape else None,
            'numerically_equal_rtol1e-12_atol1e-8':bool(np.allclose(va,vb,rtol=1e-12,atol=1e-8)) if same_shape else False,
            'different_values_count':int(np.sum(va!=vb)) if same_shape else None}
    out[a]={'curve_count_equal':len(sa['equity_curve'])==len(sb['equity_curve']),'curves':curves,
        'same_primary_metrics':sa['metrics']==sb['metrics']}
def btc(name):
    s=json.loads(Path('inputs/'+name+'.json').read_text())
    return sorted([t for t in s['trades'] if t['symbol']=='BTC-USDT'],key=lambda t:(t['opened_at'],t['closed_at']))
base=btc('CONTROL');btc_out={}
for name in ['A','B','C']:
    new=btc(name)
    exact=all(all(a.get(k)==b.get(k) for k in ('symbol','type','opened_at','closed_at')) for a,b in zip(base,new)) and len(base)==len(new)
    diffs={k:max(abs(float(a[k])-float(b[k])) for a,b in zip(base,new)) for k in ('entry_price','exit_price')}
    numerical=all(all(math.isclose(float(a[k]),float(b[k]),rel_tol=1e-10,abs_tol=1e-8) for k in ('entry_price','exit_price')) for a,b in zip(base,new))
    btc_out[name]={'n':len(new),'timestamps_sides_exact':exact,'max_abs_price_difference':diffs,'prices_equal_rtol1e-10_atol1e-8':numerical}
Path('output/numerical_equivalence.json').write_text(json.dumps({'diagnostic_curves':out,'btc_decisions':btc_out},indent=2,allow_nan=False))
print(json.dumps({'diagnostic_curves':out,'btc_decisions':btc_out}))

```

## Réplicas diagnósticas

[DIAG_CONTROL](http://localhost:9200/#/backtest/c78f7c96-d16f-4e8e-a29c-7192bd93d1ec)

Dashboard: http://localhost:9200/#/backtest/c78f7c96-d16f-4e8e-a29c-7192bd93d1ec

[DIAG_A](http://localhost:9200/#/backtest/57adc5f5-59ad-4780-9011-0cb8a154235d)

Dashboard: http://localhost:9200/#/backtest/57adc5f5-59ad-4780-9011-0cb8a154235d

[DIAG_B](http://localhost:9200/#/backtest/4dfe4912-0565-43e6-a362-aaf045375a58)

Dashboard: http://localhost:9200/#/backtest/4dfe4912-0565-43e6-a362-aaf045375a58

[DIAG_C](http://localhost:9200/#/backtest/1c0f7bcb-f6b9-4deb-94ce-7046885c8a73)

Dashboard: http://localhost:9200/#/backtest/1c0f7bcb-f6b9-4deb-94ce-7046885c8a73
