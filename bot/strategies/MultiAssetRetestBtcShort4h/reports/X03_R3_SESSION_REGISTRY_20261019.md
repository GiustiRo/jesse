# X03 R3 — registro final de16contextos

Ocho referencias reutilizadas y ocho backtests nuevos, todos finished y errornull. Los cuatro nuevos nominales son controles de paridad, no evidencia independiente de rentabilidad. Source snapshots3porcontexto:48verificados,24de las nuevas runs. Calendarios de cuatro nominales se reutilizan después de paridad exacta de fills/precios/cantidades/fees/timestamps; los otros12contextos tienen auditoría recomputada. Las comparaciones usan marcas reconstruidas congeladas, no verificadas externamente.

Ventana2020-10-15→2025-12-31exclusiva;2026cerrado.10000USDT,riesgo1%/8%,isolated5x,cap4.4,reserve.001sizingonly;3rutas4h y3feeds1m,warmup240,debugtrue,fastfalse,charttrue. Único cambio de código es la dependencia del piso BE en el clon PAXG; fees reales no se sustituyen.

| Contexto | Nueva | Fee por lado | Trades | NetoUSDT | Sharpe | CAGR% | DDmotor% |
|---|---|---:|---:|---:|---:|---:|---:|
| [X03N_B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127) | Referencia | 0.00045 | 273 | 11964.238131 | 1.491464 | 16.289896 | -8.253965 |
| [X03N_C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c) | Referencia | 0.00045 | 280 | 12135.876834 | 1.480421 | 16.463647 | -9.009386 |
| [N204N_B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142) | Referencia | 0.00045 | 273 | 13056.614915 | 1.582686 | 17.377556 | -8.776801 |
| [N204N_C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794) | Referencia | 0.00045 | 280 | 13239.442380 | 1.569754 | 17.555506 | -9.057884 |
| [X03S_B](http://localhost:9200/#/backtest/1277ad3f-21b3-41d7-9c04-9485dec1f907) | Referencia | 0.0007 | 274 | 9344.147577 | 1.282756 | 13.490865 | -8.282318 |
| [X03S_C](http://localhost:9200/#/backtest/24e0fc97-92d3-4b55-8c19-afc149e9f993) | Referencia | 0.0007 | 281 | 9420.867003 | 1.269477 | 13.577059 | -9.117058 |
| [N204S_B](http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f) | Referencia | 0.0007 | 274 | 10267.311379 | 1.373571 | 14.510218 | -9.026629 |
| [N204S_C](http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960) | Referencia | 0.0007 | 281 | 10408.935274 | 1.363056 | 14.663262 | -9.071460 |
| [FBN0_B](http://localhost:9200/#/backtest/ffa6f374-10d8-4a47-a7c1-213c97dac29d) | Sí | 0.00045 | 273 | 11964.238131 | 1.491464 | 16.289896 | -8.253965 |
| [FBN0_C](http://localhost:9200/#/backtest/c5140d46-d89d-4081-82ba-92991e238bd9) | Sí | 0.00045 | 280 | 12135.876834 | 1.480421 | 16.463647 | -9.009386 |
| [FBN1_B](http://localhost:9200/#/backtest/14c01e8f-b8f5-4cbb-842f-6f24fa5f24b5) | Sí | 0.00045 | 273 | 13056.614915 | 1.582686 | 17.377556 | -8.776801 |
| [FBN1_C](http://localhost:9200/#/backtest/0758f201-1fb0-410c-a7e3-40d9159f4120) | Sí | 0.00045 | 280 | 13239.442380 | 1.569754 | 17.555506 | -9.057884 |
| [FBS0_B](http://localhost:9200/#/backtest/9bebb1e9-d0a0-4d74-a530-76c852c18d3a) | Sí | 0.0007 | 273 | 10220.330399 | 1.369539 | 14.459258 | -8.284311 |
| [FBS0_C](http://localhost:9200/#/backtest/b97e3a45-d5df-4bc5-97c1-cb9ab56fdd18) | Sí | 0.0007 | 280 | 10264.855982 | 1.351625 | 14.507557 | -9.125162 |
| [FBS1_B](http://localhost:9200/#/backtest/931bc4d2-d12d-4e93-a2d0-7bc2f23daa44) | Sí | 0.0007 | 273 | 11175.994090 | 1.459832 | 15.477568 | -9.027062 |
| [FBS1_C](http://localhost:9200/#/backtest/2fd1c355-c50b-4851-921b-3e6432925b31) | Sí | 0.0007 | 280 | 11327.398216 | 1.447622 | 15.635473 | -9.073367 |

```json
[
  {
    "name": "X03N_B",
    "url": "http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127",
    "id": "53937852-34a3-48c7-ab35-fac586341127",
    "new_session": false,
    "fee": 0.00045,
    "btc": "BtcExploreR103",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 273,
    "net": 11964.238131473841,
    "sharpe": 1.4914641051136317,
    "cagr": 16.289896060619434,
    "dd": -8.253965403629948,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 41,
      "win_months_all": 0.6721311475409836,
      "win_months_active": 0.6721311475409836,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 41,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "X03N_C",
    "url": "http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c",
    "id": "3935efb3-2b27-4ada-86ce-94123d7a6e2c",
    "new_session": false,
    "fee": 0.00045,
    "btc": "BtcExploreR103",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 280,
    "net": 12135.87683397664,
    "sharpe": 1.4804210111104101,
    "cagr": 16.463647331914764,
    "dd": -9.009386028595156,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 42,
      "win_months_all": 0.6885245901639344,
      "win_months_active": 0.6885245901639344,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 42,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "N204N_B",
    "url": "http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142",
    "id": "bc5aaba6-2746-4e90-b0de-7b7955b66142",
    "new_session": false,
    "fee": 0.00045,
    "btc": "X03ExploreR204",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 273,
    "net": 13056.614915077666,
    "sharpe": 1.582686191771496,
    "cagr": 17.37755605244038,
    "dd": -8.77680090479469,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 41,
      "win_months_all": 0.6721311475409836,
      "win_months_active": 0.6721311475409836,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 41,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "N204N_C",
    "url": "http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794",
    "id": "6dead093-4663-4da9-ac62-c2ad9f9bb794",
    "new_session": false,
    "fee": 0.00045,
    "btc": "X03ExploreR204",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 280,
    "net": 13239.442379846789,
    "sharpe": 1.569754072854379,
    "cagr": 17.555505981887354,
    "dd": -9.057883731399553,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 42,
      "win_months_all": 0.6885245901639344,
      "win_months_active": 0.6885245901639344,
      "quarters_total": 19,
      "positive_quarters": 17,
      "win_quarters": 0.8947368421052632
    },
    "included": {
      "months": 63,
      "positive_months": 42,
      "active_months": 63,
      "positive_quarters": 18,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "X03S_B",
    "url": "http://localhost:9200/#/backtest/1277ad3f-21b3-41d7-9c04-9485dec1f907",
    "id": "1277ad3f-21b3-41d7-9c04-9485dec1f907",
    "new_session": false,
    "fee": 0.0007,
    "btc": "BtcExploreR103",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 274,
    "net": 9344.147577013518,
    "sharpe": 1.282756353341886,
    "cagr": 13.490864792592072,
    "dd": -8.282318217158057,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 38,
      "win_months_all": 0.6229508196721312,
      "win_months_active": 0.6229508196721312,
      "quarters_total": 19,
      "positive_quarters": 15,
      "win_quarters": 0.7894736842105263
    },
    "included": {
      "months": 63,
      "positive_months": 38,
      "active_months": 63,
      "positive_quarters": 16,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "X03S_C",
    "url": "http://localhost:9200/#/backtest/24e0fc97-92d3-4b55-8c19-afc149e9f993",
    "id": "24e0fc97-92d3-4b55-8c19-afc149e9f993",
    "new_session": false,
    "fee": 0.0007,
    "btc": "BtcExploreR103",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 281,
    "net": 9420.867002574214,
    "sharpe": 1.2694773916600763,
    "cagr": 13.577058547625608,
    "dd": -9.11705774767928,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 38,
      "win_months_all": 0.6229508196721312,
      "win_months_active": 0.6229508196721312,
      "quarters_total": 19,
      "positive_quarters": 15,
      "win_quarters": 0.7894736842105263
    },
    "included": {
      "months": 63,
      "positive_months": 38,
      "active_months": 63,
      "positive_quarters": 16,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "N204S_B",
    "url": "http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f",
    "id": "9a6c7c24-8847-42d1-aadb-206f21723c1f",
    "new_session": false,
    "fee": 0.0007,
    "btc": "X03ExploreR204",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 274,
    "net": 10267.311379187326,
    "sharpe": 1.3735710230285618,
    "cagr": 14.510217938203684,
    "dd": -9.026628677513893,
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
    "included": {
      "months": 63,
      "positive_months": 39,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "N204S_C",
    "url": "http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960",
    "id": "541d2bf4-ffca-4f2d-969b-c25165e7b960",
    "new_session": false,
    "fee": 0.0007,
    "btc": "X03ExploreR204",
    "paxg": "PortComparePaxgMarket4h",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 281,
    "net": 10408.935273900948,
    "sharpe": 1.3630557226109576,
    "cagr": 14.663261754546442,
    "dd": -9.071459738684062,
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
    "included": {
      "months": 63,
      "positive_months": 39,
      "active_months": 63,
      "positive_quarters": 18,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "FBN0_B",
    "url": "http://localhost:9200/#/backtest/ffa6f374-10d8-4a47-a7c1-213c97dac29d",
    "id": "ffa6f374-10d8-4a47-a7c1-213c97dac29d",
    "new_session": true,
    "fee": 0.00045,
    "btc": "BtcExploreR103",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 273,
    "net": 11964.238131473841,
    "sharpe": 1.4914641051136317,
    "cagr": 16.289896060619434,
    "dd": -8.253965403629948,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 41,
      "win_months_all": 0.6721311475409836,
      "win_months_active": 0.6721311475409836,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 41,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "reused_from": "X03N_B",
      "reason": "Four nominal parity comparisons passed exact executed fields and fees, max PNL difference0. Same frozen reconstructed marks imply identical reconstructed MTM.",
      "parity_job": "6f2bfdbdc05c46d49c5c623793a8c444"
    }
  },
  {
    "name": "FBN0_C",
    "url": "http://localhost:9200/#/backtest/c5140d46-d89d-4081-82ba-92991e238bd9",
    "id": "c5140d46-d89d-4081-82ba-92991e238bd9",
    "new_session": true,
    "fee": 0.00045,
    "btc": "BtcExploreR103",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 280,
    "net": 12135.87683397664,
    "sharpe": 1.4804210111104101,
    "cagr": 16.463647331914764,
    "dd": -9.009386028595156,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 42,
      "win_months_all": 0.6885245901639344,
      "win_months_active": 0.6885245901639344,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 42,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "reused_from": "X03N_C",
      "reason": "Four nominal parity comparisons passed exact executed fields and fees, max PNL difference0. Same frozen reconstructed marks imply identical reconstructed MTM.",
      "parity_job": "6f2bfdbdc05c46d49c5c623793a8c444"
    }
  },
  {
    "name": "FBN1_B",
    "url": "http://localhost:9200/#/backtest/14c01e8f-b8f5-4cbb-842f-6f24fa5f24b5",
    "id": "14c01e8f-b8f5-4cbb-842f-6f24fa5f24b5",
    "new_session": true,
    "fee": 0.00045,
    "btc": "X03ExploreR204",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 273,
    "net": 13056.614915077666,
    "sharpe": 1.582686191771496,
    "cagr": 17.37755605244038,
    "dd": -8.77680090479469,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 41,
      "win_months_all": 0.6721311475409836,
      "win_months_active": 0.6721311475409836,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 41,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "reused_from": "N204N_B",
      "reason": "Four nominal parity comparisons passed exact executed fields and fees, max PNL difference0. Same frozen reconstructed marks imply identical reconstructed MTM.",
      "parity_job": "6f2bfdbdc05c46d49c5c623793a8c444"
    }
  },
  {
    "name": "FBN1_C",
    "url": "http://localhost:9200/#/backtest/0758f201-1fb0-410c-a7e3-40d9159f4120",
    "id": "0758f201-1fb0-410c-a7e3-40d9159f4120",
    "new_session": true,
    "fee": 0.00045,
    "btc": "X03ExploreR204",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 280,
    "net": 13239.442379846789,
    "sharpe": 1.569754072854379,
    "cagr": 17.555505981887354,
    "dd": -9.057883731399553,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 42,
      "win_months_all": 0.6885245901639344,
      "win_months_active": 0.6885245901639344,
      "quarters_total": 19,
      "positive_quarters": 17,
      "win_quarters": 0.8947368421052632
    },
    "included": {
      "months": 63,
      "positive_months": 42,
      "active_months": 63,
      "positive_quarters": 18,
      "quarters": 21
    },
    "audit_provenance": {
      "reused_from": "N204N_C",
      "reason": "Four nominal parity comparisons passed exact executed fields and fees, max PNL difference0. Same frozen reconstructed marks imply identical reconstructed MTM.",
      "parity_job": "6f2bfdbdc05c46d49c5c623793a8c444"
    }
  },
  {
    "name": "FBS0_B",
    "url": "http://localhost:9200/#/backtest/9bebb1e9-d0a0-4d74-a530-76c852c18d3a",
    "id": "9bebb1e9-d0a0-4d74-a530-76c852c18d3a",
    "new_session": true,
    "fee": 0.0007,
    "btc": "BtcExploreR103",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 273,
    "net": 10220.330399187802,
    "sharpe": 1.3695392509158284,
    "cagr": 14.459257700702688,
    "dd": -8.28431149561536,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 39,
      "win_months_all": 0.639344262295082,
      "win_months_active": 0.639344262295082,
      "quarters_total": 19,
      "positive_quarters": 15,
      "win_quarters": 0.7894736842105263
    },
    "included": {
      "months": 63,
      "positive_months": 39,
      "active_months": 63,
      "positive_quarters": 16,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "FBS0_C",
    "url": "http://localhost:9200/#/backtest/b97e3a45-d5df-4bc5-97c1-cb9ab56fdd18",
    "id": "b97e3a45-d5df-4bc5-97c1-cb9ab56fdd18",
    "new_session": true,
    "fee": 0.0007,
    "btc": "BtcExploreR103",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 280,
    "net": 10264.855981669978,
    "sharpe": 1.3516254630678104,
    "cagr": 14.507556935887212,
    "dd": -9.125162489847172,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 39,
      "win_months_all": 0.639344262295082,
      "win_months_active": 0.639344262295082,
      "quarters_total": 19,
      "positive_quarters": 15,
      "win_quarters": 0.7894736842105263
    },
    "included": {
      "months": 63,
      "positive_months": 39,
      "active_months": 63,
      "positive_quarters": 16,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "FBS1_B",
    "url": "http://localhost:9200/#/backtest/931bc4d2-d12d-4e93-a2d0-7bc2f23daa44",
    "id": "931bc4d2-d12d-4e93-a2d0-7bc2f23daa44",
    "new_session": true,
    "fee": 0.0007,
    "btc": "X03ExploreR204",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 273,
    "net": 11175.994090003078,
    "sharpe": 1.4598317973543367,
    "cagr": 15.477568249101626,
    "dd": -9.027061799521373,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 40,
      "win_months_all": 0.6557377049180327,
      "win_months_active": 0.6557377049180327,
      "quarters_total": 19,
      "positive_quarters": 16,
      "win_quarters": 0.8421052631578947
    },
    "included": {
      "months": 63,
      "positive_months": 40,
      "active_months": 63,
      "positive_quarters": 17,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  },
  {
    "name": "FBS1_C",
    "url": "http://localhost:9200/#/backtest/2fd1c355-c50b-4851-921b-3e6432925b31",
    "id": "2fd1c355-c50b-4851-921b-3e6432925b31",
    "new_session": true,
    "fee": 0.0007,
    "btc": "X03ExploreR204",
    "paxg": "X03ExecPaxgFixedBeR301",
    "status": "finished",
    "form_verified": true,
    "sources_verified": true,
    "n": 280,
    "net": 11327.39821579347,
    "sharpe": 1.4476220564178297,
    "cagr": 15.635472715307008,
    "dd": -9.073366848682463,
    "full": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 40,
      "win_months_all": 0.6557377049180327,
      "win_months_active": 0.6557377049180327,
      "quarters_total": 19,
      "positive_quarters": 17,
      "win_quarters": 0.8947368421052632
    },
    "included": {
      "months": 63,
      "positive_months": 40,
      "active_months": 63,
      "positive_quarters": 18,
      "quarters": 21
    },
    "audit_provenance": {
      "recomputed_from_executed_fills": true
    }
  }
]
```