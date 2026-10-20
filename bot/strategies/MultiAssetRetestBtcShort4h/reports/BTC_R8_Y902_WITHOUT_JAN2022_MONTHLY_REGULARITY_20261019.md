# Y902 frente a N204 — regularidad mensual sin enero de 2022

Análisis descriptivo solicitado por el usuario después de cerrar las 26 corridas nominales. No modifica selección, receta ni datos; no se reinicia la operativa sin enero. Se omite la contribución mensual en ambas series de MTM UTC ya reconstruidas desde snapshots completos. No prueba fuera de muestra. 2026 cerrado.

|Coste|Cartera|N204 positivos /62 calendario|Y902 positivos /62 calendario|N204 activos|Y902 activos|
|---|---|---|---|---|---|
|Nominal|B|41/62 (66.13%)|41/62 (66.13%)|41/62 (66.13%)|41/61 (67.21%)|
|Nominal|C|42/62 (67.74%)|42/62 (67.74%)|42/62 (67.74%)|42/61 (68.85%)|
|+5 bps RT|B|41/62 (66.13%)|40/62 (64.52%)|41/62 (66.13%)|40/61 (65.57%)|
|+5 bps RT|C|41/62 (66.13%)|41/62 (66.13%)|41/62 (66.13%)|41/61 (67.21%)|
|+10 bps RT|B|38/62 (61.29%)|38/62 (61.29%)|38/62 (61.29%)|38/61 (62.30%)|
|+10 bps RT|C|39/62 (62.90%)|39/62 (62.90%)|39/62 (62.90%)|39/61 (63.93%)|

Quedan62 meses calendario incluyendo las dos fronteras parciales;60 si se usan sólo meses completos. Y902 tiene un mes inactivo con MTM cero, N204 ninguno. Comparar calendario con calendario evita presentar el efecto del denominador activo como una ganancia de meses positivos. Sin enero, la frecuencia nominal de meses positivos coincide exactamente. Bajo +5bps RT, B tiene un mes positivo menos y C coincide; bajo +10 coincide en ambas. El porcentaje entre meses activos difiere por el mes plano de Y902. Los resultados sólo con meses completos conservan este mismo orden y están en el JSON.

Enero2022 fue negativo para N204 (−181.78/−177.24 USDT) y positivo para Y902 (+227.60/+223.34). Retirarlo elimina tanto un mes perdedor de la referencia como uno ganador de la candidata. En nominal la ventaja restante Y902−N204 es −19.76/+40.33 USDT; bajo +5 overlay es +54.33/+111.64 USDT, bajo +10 +128.43/+182.95. Son diferencias aritméticas sobre cantidades/fills fijos, no una simulación endógena de costes ni del capital sin ese mes.

Y902 sigue retenida como candidata positiva. La frecuencia sin ese mes es aproximadamente comparable; su mérito no debe atribuirse a una mejora uniforme de regularidad. La condición previa de concentración nominal B sigue sin cumplirse y no se relajó.

Job análisis: 3025c86117854b62ac3e9b8f5581e7d6. Auditor completo reutilizado con4anclas y4sesiones, sin arrays financieros transcritos.

[N204B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142) · [N204C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794) · [Y902B](http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c) · [Y902C](http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff)

```json
{
  "omitted_month": "2022-01",
  "method": "Arithmetic omission from fixed-path UTC MTM months; not replay, not OOS.",
  "sessions": {
    "N204B": {
      "omitted": {
        "month": "2022-01",
        "complete": true,
        "mtm_USDT": -181.7840608425322,
        "return": -0.014441371105438,
        "turnover": 26320.851177812518,
        "fees": 11.844383030015631,
        "gross_arithmetic_fixed_path": -169.93967781251658,
        "cost5": 6.5802127944531295,
        "cost10": 13.160425588906259,
        "mtm_after5": -188.36427363698385,
        "mtm_after10": -194.94448643143915,
        "class": "loss_base",
        "positive_base": false,
        "positive_after5": false,
        "positive_after10": false,
        "extra_RT_bps_to_zero": null,
        "routes": {
          "BTC-USDT": {
            "mtm": -181.7840608425313,
            "fees": 11.844383030015631,
            "turnover": 26320.851177812518
          },
          "PAXG-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          },
          "SPY-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          }
        }
      },
      "samples": {
        "included": {
          "nominal": {
            "calendar_months": 62,
            "active_months": 62,
            "positive": 41,
            "negative": 21,
            "zero": 0,
            "pct_positive_calendar": 66.12903225806451,
            "positive_active": 41,
            "pct_positive_active": 66.12903225806451,
            "sum_mtm_USDT": 13238.398975920183
          },
          "plus5": {
            "calendar_months": 62,
            "active_months": 62,
            "positive": 41,
            "negative": 21,
            "zero": 0,
            "pct_positive_calendar": 66.12903225806451,
            "positive_active": 41,
            "pct_positive_active": 66.12903225806451,
            "sum_mtm_USDT": 12182.27660294875
          },
          "plus10": {
            "calendar_months": 62,
            "active_months": 62,
            "positive": 38,
            "negative": 24,
            "zero": 0,
            "pct_positive_calendar": 61.29032258064516,
            "positive_active": 38,
            "pct_positive_active": 61.29032258064516,
            "sum_mtm_USDT": 11126.154229977303
          }
        },
        "complete_only": {
          "nominal": {
            "calendar_months": 60,
            "active_months": 60,
            "positive": 41,
            "negative": 19,
            "zero": 0,
            "pct_positive_calendar": 68.33333333333333,
            "positive_active": 41,
            "pct_positive_active": 68.33333333333333,
            "sum_mtm_USDT": 14115.517700883453
          },
          "plus5": {
            "calendar_months": 60,
            "active_months": 60,
            "positive": 41,
            "negative": 19,
            "zero": 0,
            "pct_positive_calendar": 68.33333333333333,
            "positive_active": 41,
            "pct_positive_active": 68.33333333333333,
            "sum_mtm_USDT": 13095.69228441116
          },
          "plus10": {
            "calendar_months": 60,
            "active_months": 60,
            "positive": 38,
            "negative": 22,
            "zero": 0,
            "pct_positive_calendar": 63.333333333333336,
            "positive_active": 38,
            "pct_positive_active": 63.333333333333336,
            "sum_mtm_USDT": 12075.866867938868
          }
        }
      }
    },
    "N204C": {
      "omitted": {
        "month": "2022-01",
        "complete": true,
        "mtm_USDT": -177.239650445581,
        "return": -0.0143583088628405,
        "turnover": 25643.464811280504,
        "fees": 11.539559165076227,
        "gross_arithmetic_fixed_path": -165.70009128050475,
        "cost5": 6.4108662028201255,
        "cost10": 12.821732405640251,
        "mtm_after5": -183.6505166484003,
        "mtm_after10": -190.0613828512196,
        "class": "loss_base",
        "positive_base": false,
        "positive_after5": false,
        "positive_after10": false,
        "extra_RT_bps_to_zero": null,
        "routes": {
          "BTC-USDT": {
            "mtm": -177.23965044557963,
            "fees": 11.539559165076227,
            "turnover": 25643.464811280504
          },
          "PAXG-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          },
          "SPY-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          }
        }
      },
      "samples": {
        "included": {
          "nominal": {
            "calendar_months": 62,
            "active_months": 62,
            "positive": 42,
            "negative": 20,
            "zero": 0,
            "pct_positive_calendar": 67.74193548387096,
            "positive_active": 42,
            "pct_positive_active": 67.74193548387096,
            "sum_mtm_USDT": 13416.682030292375
          },
          "plus5": {
            "calendar_months": 62,
            "active_months": 62,
            "positive": 41,
            "negative": 21,
            "zero": 0,
            "pct_positive_calendar": 66.12903225806451,
            "positive_active": 41,
            "pct_positive_active": 66.12903225806451,
            "sum_mtm_USDT": 12305.079438761984
          },
          "plus10": {
            "calendar_months": 62,
            "active_months": 62,
            "positive": 39,
            "negative": 23,
            "zero": 0,
            "pct_positive_calendar": 62.903225806451616,
            "positive_active": 39,
            "pct_positive_active": 62.903225806451616,
            "sum_mtm_USDT": 11193.476847231597
          }
        },
        "complete_only": {
          "nominal": {
            "calendar_months": 60,
            "active_months": 60,
            "positive": 42,
            "negative": 18,
            "zero": 0,
            "pct_positive_calendar": 70,
            "positive_active": 42,
            "pct_positive_active": 70,
            "sum_mtm_USDT": 14448.872096235264
          },
          "plus5": {
            "calendar_months": 60,
            "active_months": 60,
            "positive": 41,
            "negative": 19,
            "zero": 0,
            "pct_positive_calendar": 68.33333333333333,
            "positive_active": 41,
            "pct_positive_active": 68.33333333333333,
            "sum_mtm_USDT": 13388.937008012868
          },
          "plus10": {
            "calendar_months": 60,
            "active_months": 60,
            "positive": 39,
            "negative": 21,
            "zero": 0,
            "pct_positive_calendar": 65,
            "positive_active": 39,
            "pct_positive_active": 65,
            "sum_mtm_USDT": 12329.001919790475
          }
        }
      }
    },
    "Y902B": {
      "omitted": {
        "month": "2022-01",
        "complete": true,
        "mtm_USDT": 227.59612781188298,
        "return": 0.0180976931900269,
        "turnover": 9731.8645331482,
        "fees": 4.37933903991669,
        "gross_arithmetic_fixed_path": 231.97546685179967,
        "cost5": 2.43296613328705,
        "cost10": 4.8659322665741,
        "mtm_after5": 225.1631616785944,
        "mtm_after10": 222.73019554530765,
        "class": "positive_above_cost10",
        "positive_base": true,
        "positive_after5": true,
        "positive_after10": true,
        "extra_RT_bps_to_zero": 467.7338592962452,
        "routes": {
          "BTC-USDT": {
            "mtm": 227.59612781188207,
            "fees": 4.37933903991669,
            "turnover": 9731.8645331482
          },
          "PAXG-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          },
          "SPY-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          }
        }
      },
      "samples": {
        "included": {
          "nominal": {
            "calendar_months": 62,
            "active_months": 61,
            "positive": 41,
            "negative": 20,
            "zero": 1,
            "pct_positive_calendar": 66.12903225806451,
            "positive_active": 41,
            "pct_positive_active": 67.21311475409836,
            "sum_mtm_USDT": 13218.638397763347
          },
          "plus5": {
            "calendar_months": 62,
            "active_months": 61,
            "positive": 40,
            "negative": 21,
            "zero": 1,
            "pct_positive_calendar": 64.51612903225806,
            "positive_active": 40,
            "pct_positive_active": 65.57377049180327,
            "sum_mtm_USDT": 12236.60931415434
          },
          "plus10": {
            "calendar_months": 62,
            "active_months": 61,
            "positive": 38,
            "negative": 23,
            "zero": 1,
            "pct_positive_calendar": 61.29032258064516,
            "positive_active": 38,
            "pct_positive_active": 62.295081967213115,
            "sum_mtm_USDT": 11254.58023054534
          }
        },
        "complete_only": {
          "nominal": {
            "calendar_months": 60,
            "active_months": 59,
            "positive": 41,
            "negative": 18,
            "zero": 1,
            "pct_positive_calendar": 68.33333333333333,
            "positive_active": 41,
            "pct_positive_active": 69.49152542372882,
            "sum_mtm_USDT": 13895.069749660637
          },
          "plus5": {
            "calendar_months": 60,
            "active_months": 59,
            "positive": 40,
            "negative": 19,
            "zero": 1,
            "pct_positive_calendar": 66.66666666666667,
            "positive_active": 40,
            "pct_positive_active": 67.79661016949153,
            "sum_mtm_USDT": 12942.947714826874
          },
          "plus10": {
            "calendar_months": 60,
            "active_months": 59,
            "positive": 38,
            "negative": 21,
            "zero": 1,
            "pct_positive_calendar": 63.333333333333336,
            "positive_active": 38,
            "pct_positive_active": 64.40677966101696,
            "sum_mtm_USDT": 11990.825679993111
          }
        }
      }
    },
    "Y902C": {
      "omitted": {
        "month": "2022-01",
        "complete": true,
        "mtm_USDT": 223.34199458175135,
        "return": 0.0181034217180828,
        "turnover": 9549.960523182814,
        "fees": 4.297482235432266,
        "gross_arithmetic_fixed_path": 227.6394768171836,
        "cost5": 2.3874901307957037,
        "cost10": 4.774980261591407,
        "mtm_after5": 220.95450445095776,
        "mtm_after10": 218.56701432016234,
        "class": "positive_above_cost10",
        "positive_base": true,
        "positive_after5": true,
        "positive_after10": true,
        "extra_RT_bps_to_zero": 467.73385929623896,
        "routes": {
          "BTC-USDT": {
            "mtm": 223.34199458175317,
            "fees": 4.297482235432266,
            "turnover": 9549.960523182814
          },
          "PAXG-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          },
          "SPY-USDT": {
            "mtm": 0,
            "fees": 0,
            "turnover": 0
          }
        }
      },
      "samples": {
        "included": {
          "nominal": {
            "calendar_months": 62,
            "active_months": 61,
            "positive": 42,
            "negative": 19,
            "zero": 1,
            "pct_positive_calendar": 67.74193548387096,
            "positive_active": 42,
            "pct_positive_active": 68.85245901639344,
            "sum_mtm_USDT": 13457.007176304636
          },
          "plus5": {
            "calendar_months": 62,
            "active_months": 61,
            "positive": 41,
            "negative": 20,
            "zero": 1,
            "pct_positive_calendar": 66.12903225806451,
            "positive_active": 41,
            "pct_positive_active": 67.21311475409836,
            "sum_mtm_USDT": 12416.719394981385
          },
          "plus10": {
            "calendar_months": 62,
            "active_months": 61,
            "positive": 39,
            "negative": 22,
            "zero": 1,
            "pct_positive_calendar": 62.903225806451616,
            "positive_active": 39,
            "pct_positive_active": 63.9344262295082,
            "sum_mtm_USDT": 11376.431613658135
          }
        },
        "complete_only": {
          "nominal": {
            "calendar_months": 60,
            "active_months": 59,
            "positive": 42,
            "negative": 17,
            "zero": 1,
            "pct_positive_calendar": 70,
            "positive_active": 42,
            "pct_positive_active": 71.1864406779661,
            "sum_mtm_USDT": 14289.621117964069
          },
          "plus5": {
            "calendar_months": 60,
            "active_months": 59,
            "positive": 41,
            "negative": 18,
            "zero": 1,
            "pct_positive_calendar": 68.33333333333333,
            "positive_active": 41,
            "pct_positive_active": 69.49152542372882,
            "sum_mtm_USDT": 13294.86346117061
          },
          "plus10": {
            "calendar_months": 60,
            "active_months": 59,
            "positive": 39,
            "negative": 20,
            "zero": 1,
            "pct_positive_calendar": 65,
            "positive_active": 39,
            "pct_positive_active": 66.10169491525424,
            "sum_mtm_USDT": 12300.10580437715
          }
        }
      }
    }
  }
}
```

## Código descriptivo añadido al auditor

```python

# User-requested descriptive omission; no rerun, retuning, or selection change.
omit_results={"omitted_month":"2022-01","method":"Arithmetic omission from fixed-path UTC MTM months; not replay, not OOS.","sessions":{}}
for name in ["N204B","N204C","Y902B","Y902C"]:
    month_rows=json.loads(Path("output/"+name+"_r3_month_rows.json").read_text())
    snap=json.loads(Path("inputs/"+name+".json").read_text())
    fee=float(snap["summary"]["form"]["config"]["exchange"]["fee"])
    active_periods=set()
    for trade in snap["trades"]:
        _,entry,outs=_fills(trade,fee)
        left=pd.Timestamp(entry["time"],unit="ms")-pd.Timedelta(milliseconds=1)
        right=pd.Timestamp(outs[-1]["time"],unit="ms")-pd.Timedelta(milliseconds=1)
        active_periods.update(str(v) for v in pd.period_range(left.to_period("M"),right.to_period("M"),freq="M"))
    result={"omitted":next(r for r in month_rows if r["month"]=="2022-01"),"samples":{}}
    for sample,full_only in [("included",False),("complete_only",True)]:
        subset=[r for r in month_rows if r["month"]!="2022-01" and (not full_only or r["complete"])]
        metrics={}
        for label,key in [("nominal","mtm_USDT"),("plus5","mtm_after5"),("plus10","mtm_after10")]:
            vals=[r[key] for r in subset]
            active=[r for r in subset if r["month"] in active_periods]
            pos=sum(v>0 for v in vals)
            metrics[label]={"calendar_months":len(vals),"active_months":len(active),"positive":pos,"negative":sum(v<0 for v in vals),"zero":sum(v==0 for v in vals),"pct_positive_calendar":100*pos/len(vals),"positive_active":sum(r[key]>0 for r in active),"pct_positive_active":100*sum(r[key]>0 for r in active)/len(active),"sum_mtm_USDT":sum(vals)}
        result["samples"][sample]=metrics
    omit_results["sessions"][name]=result
Path("output/january_2022_omission.json").write_text(json.dumps(omit_results,indent=2,allow_nan=False))
print("JANUARY_OMISSION_DIAGNOSTIC_SAVED")

```
