# X03 R2 — comprobación de N204 con comisión dentro del motor

N204 fue seleccionada después de auditar las 14 variantes económicas. Fue la única elegible según el protocolo congelado. Se ejecutó un único par B/C, con la misma fuente, sin sustitución posterior.

La comisión es .00070 por lado:14bps ida y vuelta, +5bps frente a los9bps nominales. Los resultados siguientes son el MTM de esas ejecuciones, sin otro overlay. El campo cost_calendar["5"] de estas sesiones añadiría otros5bps: no debe confundirse con esta comprobación.

La mejora frente a X03 con idéntica comisión es +923,163802USDT B y +988,068271USDT C. Frente a las carteras sin X03, es +3060,402599 / +3086,159974USDT.

La regularidad mensual falla:39/61 meses completos =63,934426%, y39/63 incluyendo fronteras =61,904762%, en ambas carteras. El objetivo es65%. Los trimestres sí pasan:16/19B y17/19C completos;17/21B y18/21C incluyendo fronteras. La comprobación no cumple el objetivo conjunto. No se promueve ni se elige otra candidata.

El código es idéntico. Frente a N204 nominal, las223operaciones BTC y12/19SPY conservan todos los timestamps de entrada/salida. PAXG pasa de38 a39trades y sólo36de38salidas coinciden. Su BE depende de entry·(1+2,5·fee_rate). Para la entrada del3-ene-2025 a2661, el BE pasa de2663,993625 a2665,65675, adelantando la salida y permitiendo una reentrada. El diagnóstico previo conserva las órdenes ejecutadas del simulador. Además, la comisión modifica cantidades y capital compartido.

No se debe atribuir toda la penalidad a BTC ni equiparar la comisión del motor a un descuento estático o a slippage puro. El hallazgo merece una investigación separada sobre gestión y ejecución; no se cambió PAXG adaptativamente en esta ronda.

```json
{
  "confirmation": {
    "selected": "N204",
    "engine_fee_per_side": 0.0007,
    "extra_bps_RT_vs_nominal": 5,
    "portfolios": [
      {
        "portfolio": "B",
        "url": "http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f",
        "net": 10267.311379187322,
        "cagr": 14.510217938203684,
        "dd_engine": -9.026628677513893,
        "full": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.639344262295082,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6190476190476191,
          "win_quarters": 0.8095238095238095
        },
        "delta_samefee_X03": 923.1638021738054,
        "delta_samefee_noX03": 3060.402598820153,
        "regularity_pass": false
      },
      {
        "portfolio": "C",
        "url": "http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960",
        "net": 10408.935273900946,
        "cagr": 14.663261754546442,
        "dd_engine": -9.071459738684062,
        "full": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.639344262295082,
          "quarters_total": 19,
          "positive_quarters": 17,
          "win_quarters": 0.8947368421052632
        },
        "partial": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6190476190476191,
          "win_quarters": 0.8571428571428571
        },
        "delta_samefee_X03": 988.0682713267361,
        "delta_samefee_noX03": 3086.1599743569386,
        "regularity_pass": false
      }
    ],
    "no_replacement": true,
    "promoted": false,
    "conclusion": "Net improvement persists, but monthly regularity target is not confirmed under actual engine fees. Development candidate only."
  },
  "path": {
    "B": {
      "BTC-USDT": {
        "nominal": 223,
        "enginefee": 223,
        "same_entry": 223,
        "same_entry_and_exit": 223
      },
      "PAXG-USDT": {
        "nominal": 38,
        "enginefee": 39,
        "same_entry": 38,
        "same_entry_and_exit": 36
      },
      "SPY-USDT": {
        "nominal": 12,
        "enginefee": 12,
        "same_entry": 12,
        "same_entry_and_exit": 12
      }
    },
    "C": {
      "BTC-USDT": {
        "nominal": 223,
        "enginefee": 223,
        "same_entry": 223,
        "same_entry_and_exit": 223
      },
      "PAXG-USDT": {
        "nominal": 38,
        "enginefee": 39,
        "same_entry": 38,
        "same_entry_and_exit": 36
      },
      "SPY-USDT": {
        "nominal": 19,
        "enginefee": 19,
        "same_entry": 19,
        "same_entry_and_exit": 19
      }
    }
  }
}
```
