# R9 — incertidumbre de la ventaja Y902 frente a N204

Resultados completos de los tres niveles de fee.

## Dictamen independiente

Y902 conserva una ventaja observada de cartera frente a N204 en las dos configuraciones y los tres niveles de fee. Los diferenciales incluidos son nominal+389.62/+440.91USDT, F70+526.64/+508.24 y F95+588.17/+616.44. Es evidencia favorable de resistencia relativa a mayores comisiones dentro de esta muestra. No significa que pagar más fee mejore su neto absoluto: Y902B pasa13446.23→10793.95→9570.52USDT y C13680.35→10917.18→9606.62.

Los seis IC primarios (61meses, B/C por tres fees) incluyen cero y negativos. La mejora observada es pequeña frente a la dispersión temporal, de modo que este diagnóstico no permite descartar una ventaja media no positiva bajo el remuestreo fijado. Eso no prueba que el mecanismo carezca de valor ni exige rechazarlo: sostiene continuar investigando una candidata congelada con incertidumbre explícita.

La lectura de concentración depende de bordes y nivel de costes. En61meses nominal, descontarenero2022dejaδ−220.45/−159.25; F70−50.84/−62.83; F95+24.69/+64.77. En63incluidos nominal persiste el fallo conocido B−19.76 y C+40.33, sin borrarlo. Los dos mesesfrontera aportan nominal+200.69/+199.58USDT (51.51%/45.26% del diferencial incluido). Estas son restas descriptivas sin replay, no pérdidas de una estrategia sin2022.

No se abrió2026, ni se añadió backtest o cambió trading. No se alteró seed, longitud de bloque, número de réplicas, intervalos o muestras tras observar resultados. Este análisis no juzga todavía todos los vecinosTP ni todas las variantes exploratoriasR9: corresponde a la síntesisroot consolidarlos. No promoción automática ni afirmación de ausencia de sobreajuste.

Anclas verificadas:
- benchmarks: http://localhost:9200/#/backtest/2e943276-7815-4280-96c8-d634d2dab817
- fade: http://localhost:9200/#/backtest/b6f5562e-2144-4a54-9d27-108155680338
- reject: http://localhost:9200/#/backtest/5c8e7296-fdc3-46a6-8663-ff00ff0b1d20
- sleeves: http://localhost:9200/#/backtest/262fb59f-2b20-4247-aa9a-e7823cc3c930


## Método fijado

Reconstrucción MTM a cierre diario UTC desde snapshots completos y cuatro anclas inmutables. Se validan fills/cantidades/fees/PNL/wallet/cierre terminal con el core del auditor R8; no se toman las curvasclosed-tradecomoMTM ni se imputan precios desde otra fuente. Jobs secuenciales de ocho inputs (cuatro anclas+N204B/C+Y902B/C) por límiteMCP10; cada nivel reconstruye todo sin leer workspaces ajenos ni transferir arrays. Cero nuevos backtests, cero cambios trading por este subagente.

Bootstrap pareado circular, bloques de seis meses,10000réplicas,seed9022026. Mismo índice de cada réplica aplicado a B/C y regenerado idéntico para cada fee; hashes verifican identidad. Se eligenceil(n/6)inicios uniformes con reemplazo, cada bloque avanza seis posiciones módulo n y se trunca a n. ICpercentiles2.5/97.5de la media mensual δMTM enUSDT, sin studentizar ni escoger longitud. Primario61mesescompletos2020-11..2025-11; secundario63incluyendo2020-10/2025-12parciales. Se remuestrean todos los meses calendario, no sólo activos o ganadores. B/C no son muestras independientes.

## Intervalos y fracciones descriptivas

|Fee por lado|Muestra|Cartera|Media observada δUSDT/mes|ICpercentil95%media|Fracción réplicas conmedia>0|δtotalUSDT|δsinmejormesUSDT|
|---|---|---|---:|---|---:|---:|---:|
|nominal|full61|B|3.09725|[-18.46164, 27.30060]|0.5884|188.93224|-220.44795|
|nominal|full61|C|3.95624|[-17.53069, 27.64878]|0.6215|241.33067|-159.25098|
|nominal|included63|B|6.18444|[-13.99560, 28.44963]|0.7005|389.61961|-19.76058|
|nominal|included63|C|6.99852|[-12.99004, 28.82374]|0.7358|440.90679|40.32515|
|F70|full61|B|5.72512|[-14.47329, 28.58022]|0.6861|349.23205|-50.83646|
|F70|full61|C|5.42563|[-14.86116, 27.89452]|0.6777|330.96324|-62.82649|
|F70|included63|B|8.35933|[-10.77211, 29.44065]|0.7829|526.63806|126.56955|
|F70|included63|C|8.06738|[-10.96831, 28.95892]|0.7802|508.24488|114.45514|
|F95|full61|B|6.85254|[-12.81578, 29.14485]|0.7293|418.00505|24.69265|
|F95|full61|C|7.37082|[-12.38181, 29.37016]|0.7477|449.62009|64.76981|
|F95|included63|B|9.33597|[-9.19442, 29.93509]|0.8175|588.16613|194.85373|
|F95|included63|C|9.78471|[-8.67894, 30.22393]|0.8345|616.43663|231.58636|

La fracción de réplicas positivas describe el remuestreo de esta muestra reutilizada; NO es probabilidad de que exista un edge verdadero ni probabilidad predictiva de ganar. No corrige la búsqueda histórica ni la selección previa de Y902. Los IC son condicionales a las trayectorias observadas y al supuesto de remuestreo; circularidad une extremos y pocos años limitan la incertidumbre representada. No son prueba de ausencia de sobreajuste. Medias enUSDT dependen del capital y sizing endógenos; no son retornos porcentuales ni un edge aislado del suplemento.

## Concentración y bordes

Omitir un mes o año es restar su δMTM registrado del diferencial acumulado; no se reejecutan órdenes/capital ni se elimina un escenario del motor. En61meses se excluyen los dos meses frontera y cambia el total; no comparar su delta sinmejormes directamente con el gateR8calculado sobre63. El año2020 es parcial y2025esparcial en ambas muestras; en61termina ennoviembre y en63incluyehastadiciembre30. Desglose numérico de cada omisión por año enJSON.

## Costes y restricciones

Nominal.00045/lado,F70.00070/lado,F95.00095/lado. Son feeengine emparejados: afectan cantidades, PAXGBE, capital y ocupación; no slippage puro ni liquidez/latencia/rechazos. No mezclar con overlays estáticos+5/+10. Se observa toda la cartera BTC/PAXG/SPY, sin atribución causal sólo suplemento ni identificarSTOPoriginalporentrytype. B=SPYsegundaexacta/precioestructural;C=desde2/preciomercado. Muestra2020-10-15→2025-12-31exclusiva,últimosprecios2025-12-30.2026cerradoinclusoinspección.

## Trazabilidad

Protocolo: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R9_FROZEN_PROTOCOL_20261019.md.
Código: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R9_UNCERTAINTY_SOURCE_20261019.md.

### nominal

Analysis job: 91f0cec7e4204d64b506d3e1c63ab277. Inputs: ocho snapshots completos, todosfinished, manifiesto original del job conservado debajo. Anclasbenchmarks/fade/reject/sleevesidénticasentrejobs.

- N204B: http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142
- N204C: http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794
- Y902B: http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c
- Y902C: http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff

```json
{
  "manifest": [
    {
      "name": "benchmarks",
      "file": "inputs/benchmarks.json",
      "session_type": "backtest",
      "session_id": "2e943276-7815-4280-96c8-d634d2dab817",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 three-asset STOP session-filtered control",
      "size_bytes": 737286
    },
    {
      "name": "fade",
      "file": "inputs/fade.json",
      "session_type": "backtest",
      "session_id": "b6f5562e-2144-4a54-9d27-108155680338",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetRallyFade4h",
      "size_bytes": 380556
    },
    {
      "name": "reject",
      "file": "inputs/reject.json",
      "session_type": "backtest",
      "session_id": "5c8e7296-fdc3-46a6-8663-ff00ff0b1d20",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetRejectShort4h",
      "size_bytes": 574222
    },
    {
      "name": "sleeves",
      "file": "inputs/sleeves.json",
      "session_type": "backtest",
      "session_id": "262fb59f-2b20-4247-aa9a-e7823cc3c930",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetSleeves4h",
      "size_bytes": 397128
    },
    {
      "name": "N204B",
      "file": "inputs/N204B.json",
      "session_type": "backtest",
      "session_id": "bc5aaba6-2746-4e90-b0de-7b7955b66142",
      "session_status": "finished",
      "title": "MCP Backtest: X03 R2 N204 B — positive-pressure cohort VWAP",
      "size_bytes": 527298
    },
    {
      "name": "N204C",
      "file": "inputs/N204C.json",
      "session_type": "backtest",
      "session_id": "6dead093-4663-4da9-ac62-c2ad9f9bb794",
      "session_status": "finished",
      "title": "MCP Backtest: X03 R2 N204 C — positive-pressure cohort VWAP",
      "size_bytes": 537241
    },
    {
      "name": "Y902B",
      "file": "inputs/Y902B.json",
      "session_type": "backtest",
      "session_id": "cb305a17-1312-463e-bbf1-c8173dfae22c",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R8 Y902B creative frozen",
      "size_bytes": 483319
    },
    {
      "name": "Y902C",
      "file": "inputs/Y902C.json",
      "session_type": "backtest",
      "session_id": "b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R8 Y902C creative frozen",
      "size_bytes": 493333
    }
  ],
  "results": {
    "fee_level": "nominal",
    "seed": 9022026,
    "replicates": 10000,
    "circular_block_months": 6,
    "samples": {
      "full61": {
        "months": 61,
        "period_start": "2020-11",
        "period_last": "2025-11",
        "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 3.0972497939606525,
            "observed_total_USDT": 188.9322374315998,
            "ci95_percentile_mean_USDT_month": [
              -18.461644962167256,
              27.300595334617128
            ],
            "fraction_bootstrap_means_gt_zero": 0.5884,
            "positive_delta_months": 27,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 409.38018865441336,
            "delta_omitting_best_month_arithmetic_USDT": -220.44795122281357,
            "year_delta_USDT": {
              "2020": -32.97982371443686,
              "2021": 21.225657331864568,
              "2022": 154.22912855232062,
              "2023": 287.4741597636712,
              "2024": -73.08507298060067,
              "2025": -167.93181152121906
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 221.91206114603665,
              "2021": 167.70658009973522,
              "2022": 34.70310887927917,
              "2023": -98.54192233207141,
              "2024": 262.01731041220046,
              "2025": 356.86404895281885
            }
          },
          "C": {
            "observed_mean_USDT_month": 3.9562404386252026,
            "observed_total_USDT": 241.33066675613736,
            "ci95_percentile_mean_USDT_month": [
              -17.530692280914852,
              27.64878181288945
            ],
            "fraction_bootstrap_means_gt_zero": 0.6215,
            "positive_delta_months": 28,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.58164502733234,
            "delta_omitting_best_month_arithmetic_USDT": -159.25097827119498,
            "year_delta_USDT": {
              "2020": -32.98046405748573,
              "2021": 25.93716357273661,
              "2022": 148.9034131719436,
              "2023": 315.30783956492087,
              "2024": -68.1329541064515,
              "2025": -147.7043313895265
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 274.3111308136231,
              "2021": 215.39350318340075,
              "2022": 92.42725358419375,
              "2023": -73.97717280878351,
              "2024": 309.46362086258887,
              "2025": 389.03499814566385
            }
          }
        }
      },
      "included63": {
        "months": 63,
        "period_start": "2020-10",
        "period_last": "2025-12",
        "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 6.184438261866273,
            "observed_total_USDT": 389.6196104975752,
            "ci95_percentile_mean_USDT_month": [
              -13.995597783500031,
              28.44962979271072
            ],
            "fraction_bootstrap_means_gt_zero": 0.7005,
            "positive_delta_months": 28,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 409.38018865441336,
            "delta_omitting_best_month_arithmetic_USDT": -19.760578156838164,
            "year_delta_USDT": {
              "2020": -32.97982371443686,
              "2021": 21.225657331864568,
              "2022": 154.22912855232062,
              "2023": 287.4741597636712,
              "2024": -73.08507298060067,
              "2025": 32.75556154475635
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 422.59943421201206,
              "2021": 368.3939531657106,
              "2022": 235.39048194525458,
              "2023": 102.145450733904,
              "2024": 462.70468347817587,
              "2025": 356.86404895281885
            }
          },
          "C": {
            "observed_mean_USDT_month": 6.998520492691958,
            "observed_total_USDT": 440.9067910395934,
            "ci95_percentile_mean_USDT_month": [
              -12.990043241773694,
              28.823737025734072
            ],
            "fraction_bootstrap_means_gt_zero": 0.7358,
            "positive_delta_months": 29,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.58164502733234,
            "delta_omitting_best_month_arithmetic_USDT": 40.32514601226103,
            "year_delta_USDT": {
              "2020": -32.98046405748573,
              "2021": 25.93716357273661,
              "2022": 148.9034131719436,
              "2023": 315.30783956492087,
              "2024": -68.1329541064515,
              "2025": 51.87179289392952
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 473.8872550970791,
              "2021": 414.96962746685676,
              "2022": 292.00337786764976,
              "2023": 125.5989514746725,
              "2024": 509.0397451460449,
              "2025": 389.03499814566385
            }
          }
        }
      }
    },
    "audits": {
      "N204B": {
        "name": "N204B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 41,
          "win_months_all": 0.6721311475409836,
          "win_months_active": 0.6721311475409836,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 63,
        "win_months_all": 0.6507936507936508,
        "win_months_active": 0.6507936507936508,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.038363339801451346
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.03892475898116354
        ],
        "daily_close_drawdown_pct": -8.767001235283335,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.07155623932051774,
            "SPY-USDT": -0.04446581775982622
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.07155623932051774,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.036221631169715524
          },
          "SPY-USDT": {
            "BTC-USDT": -0.04446581775982622,
            "PAXG-USDT": -0.036221631169715524,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.044393834400308974,
          "2021-12-31 00:00:00+00:00": 0.20526646535936122,
          "2022-12-31 00:00:00+00:00": 0.10834108700431222,
          "2023-12-31 00:00:00+00:00": 0.1957195771013449,
          "2024-12-31 00:00:00+00:00": 0.16693816310374676,
          "2025-12-31 00:00:00+00:00": 0.1843977062028026
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 0,
          "boundary_liquidations_reconciled": 0,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "N204C": {
        "name": "N204C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 42,
          "win_months_all": 0.6885245901639344,
          "win_months_active": 0.6885245901639344,
          "quarters_total": 19,
          "positive_quarters": 17,
          "win_quarters": 0.8947368421052632
        },
        "months_total": 63,
        "months_active": 63,
        "win_months_all": 0.6666666666666666,
        "win_months_active": 0.6666666666666666,
        "win_quarters": 0.8571428571428571,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.046908056267221165
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.04756286766151652
        ],
        "daily_close_drawdown_pct": -9.116483595648194,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.07197005104132925,
            "SPY-USDT": -0.027676293072567804
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.07197005104132925,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.01961892771460515
          },
          "SPY-USDT": {
            "BTC-USDT": -0.027676293072567804,
            "PAXG-USDT": 0.01961892771460515,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.04350741280602666,
          "2021-12-31 00:00:00+00:00": 0.1829381961996599,
          "2022-12-31 00:00:00+00:00": 0.11156549325981024,
          "2023-12-31 00:00:00+00:00": 0.23934621951238078,
          "2024-12-31 00:00:00+00:00": 0.1614791972366636,
          "2025-12-31 00:00:00+00:00": 0.17660034423036675
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 1,
          "boundary_liquidations_reconciled": 1,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "Y902B": {
        "name": "Y902B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 60,
          "positive_months": 42,
          "win_months_all": 0.6885245901639344,
          "win_months_active": 0.7,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 62,
        "win_months_all": 0.6666666666666666,
        "win_months_active": 0.6774193548387096,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.03864759352480418
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.029834818684366105
        ],
        "daily_close_drawdown_pct": -9.684509247344009,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.11840400005480689,
            "SPY-USDT": -0.060131609315366055
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.11840400005480689,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.03604179963433147
          },
          "SPY-USDT": {
            "BTC-USDT": -0.060131609315366055,
            "PAXG-USDT": -0.03604179963433147,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.04109585202886534,
          "2021-12-31 00:00:00+00:00": 0.2079554885765169,
          "2022-12-31 00:00:00+00:00": 0.12070613973951572,
          "2023-12-31 00:00:00+00:00": 0.21413802037221719,
          "2024-12-31 00:00:00+00:00": 0.15847277269441817,
          "2025-12-31 00:00:00+00:00": 0.1827305525050913
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 0,
          "boundary_liquidations_reconciled": 0,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "Y902C": {
        "name": "Y902C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 60,
          "positive_months": 43,
          "win_months_all": 0.7049180327868853,
          "win_months_active": 0.7166666666666667,
          "quarters_total": 19,
          "positive_quarters": 17,
          "win_quarters": 0.8947368421052632
        },
        "months_total": 63,
        "months_active": 62,
        "win_months_all": 0.6825396825396826,
        "win_months_active": 0.6935483870967742,
        "win_quarters": 0.8571428571428571,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04691767454945284
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.03799927530095615
        ],
        "daily_close_drawdown_pct": -9.627684656189272,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.11810829226435761,
            "SPY-USDT": -0.09749501174089831
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.11810829226435761,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.020145322737921727
          },
          "SPY-USDT": {
            "BTC-USDT": -0.09749501174089831,
            "PAXG-USDT": 0.020145322737921727,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.04020936640027806,
          "2021-12-31 00:00:00+00:00": 0.1860116688302591,
          "2022-12-31 00:00:00+00:00": 0.12369884401606512,
          "2023-12-31 00:00:00+00:00": 0.25964143568722764,
          "2024-12-31 00:00:00+00:00": 0.15335000549508826,
          "2025-12-31 00:00:00+00:00": 0.1757646142427156
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 1,
          "boundary_liquidations_reconciled": 1,
          "boundary_close_is_execution_liquidity_proof": false
        }
      }
    },
    "anchors": {
      "BTC-USDT": {
        "anchor_count": 55,
        "distinct_anchor_timestamps": 35,
        "scale": 1.1501999999999981,
        "max_relative_error": 1.3322676295501878e-15
      },
      "PAXG-USDT": {
        "anchor_count": 24,
        "distinct_anchor_timestamps": 15,
        "scale": 0.19228799999999985,
        "max_relative_error": 1.5543122344752192e-15
      },
      "SPY-USDT": {
        "anchor_count": 17,
        "distinct_anchor_timestamps": 16,
        "scale": 0.034843459999999944,
        "max_relative_error": 1.5543122344752192e-15
      }
    },
    "sessions": {
      "N204B": {
        "session_id": "bc5aaba6-2746-4e90-b0de-7b7955b66142",
        "fee_per_side": 0.00045,
        "net": 13056.614915077666,
        "title": "MCP Backtest: X03 R2 N204 B — positive-pressure cohort VWAP",
        "dashboard_url": null
      },
      "N204C": {
        "session_id": "6dead093-4663-4da9-ac62-c2ad9f9bb794",
        "fee_per_side": 0.00045,
        "net": 13239.442379846789,
        "title": "MCP Backtest: X03 R2 N204 C — positive-pressure cohort VWAP",
        "dashboard_url": null
      },
      "Y902B": {
        "session_id": "cb305a17-1312-463e-bbf1-c8173dfae22c",
        "fee_per_side": 0.00045,
        "net": 13446.23452557522,
        "title": "MCP Backtest: BTC R8 Y902B creative frozen",
        "dashboard_url": null
      },
      "Y902C": {
        "session_id": "b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff",
        "fee_per_side": 0.00045,
        "net": 13680.349170886388,
        "title": "MCP Backtest: BTC R8 Y902C creative frozen",
        "dashboard_url": null
      }
    },
    "limitations": "Reused development sample; descriptive conditional resampling, not probability of true edge, OOS, selection correction or replay of capital."
  }
}
```

### F70

Analysis job: cc2655f762ed4c45bc4a4e88dea202e6. Inputs: ocho snapshots completos, todosfinished, manifiesto original del job conservado debajo. Anclasbenchmarks/fade/reject/sleevesidénticasentrejobs.

- N204B: http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f
- N204C: http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960
- Y902B: http://localhost:9200/#/backtest/c20f22a8-38bf-4ad3-99d0-2d583d91d81c
- Y902C: http://localhost:9200/#/backtest/2297b82f-5db7-457a-8d46-9b53465dde7d

```json
{
  "manifest": [
    {
      "name": "benchmarks",
      "file": "inputs/benchmarks.json",
      "session_type": "backtest",
      "session_id": "2e943276-7815-4280-96c8-d634d2dab817",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 three-asset STOP session-filtered control",
      "size_bytes": 737286
    },
    {
      "name": "fade",
      "file": "inputs/fade.json",
      "session_type": "backtest",
      "session_id": "b6f5562e-2144-4a54-9d27-108155680338",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetRallyFade4h",
      "size_bytes": 380556
    },
    {
      "name": "reject",
      "file": "inputs/reject.json",
      "session_type": "backtest",
      "session_id": "5c8e7296-fdc3-46a6-8663-ff00ff0b1d20",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetRejectShort4h",
      "size_bytes": 574222
    },
    {
      "name": "sleeves",
      "file": "inputs/sleeves.json",
      "session_type": "backtest",
      "session_id": "262fb59f-2b20-4247-aa9a-e7823cc3c930",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetSleeves4h",
      "size_bytes": 397128
    },
    {
      "name": "N204B",
      "file": "inputs/N204B.json",
      "session_type": "backtest",
      "session_id": "9a6c7c24-8847-42d1-aadb-206f21723c1f",
      "session_status": "finished",
      "title": "MCP Backtest: X03 R2 CONF5 B — selected N204 engine-fee confirmation",
      "size_bytes": 527490
    },
    {
      "name": "N204C",
      "file": "inputs/N204C.json",
      "session_type": "backtest",
      "session_id": "541d2bf4-ffca-4f2d-969b-c25165e7b960",
      "session_status": "finished",
      "title": "MCP Backtest: X03 R2 CONF5 C — selected N204 engine-fee confirmation",
      "size_bytes": 539124
    },
    {
      "name": "Y902B",
      "file": "inputs/Y902B.json",
      "session_type": "backtest",
      "session_id": "c20f22a8-38bf-4ad3-99d0-2d583d91d81c",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R9 F70B validation",
      "size_bytes": 485045
    },
    {
      "name": "Y902C",
      "file": "inputs/Y902C.json",
      "session_type": "backtest",
      "session_id": "2297b82f-5db7-457a-8d46-9b53465dde7d",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R9 F70C validation",
      "size_bytes": 495557
    }
  ],
  "results": {
    "fee_level": "F70",
    "seed": 9022026,
    "replicates": 10000,
    "circular_block_months": 6,
    "samples": {
      "full61": {
        "months": 61,
        "period_start": "2020-11",
        "period_last": "2025-11",
        "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 5.725115623867467,
            "observed_total_USDT": 349.23205305591546,
            "ci95_percentile_mean_USDT_month": [
              -14.473294331667992,
              28.580223225555887
            ],
            "fraction_bootstrap_means_gt_zero": 0.6861,
            "positive_delta_months": 30,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.0685127057204,
            "delta_omitting_best_month_arithmetic_USDT": -50.836459649804965,
            "year_delta_USDT": {
              "2020": -31.73123376250078,
              "2021": 45.660599801045464,
              "2022": 170.10405793982864,
              "2023": 313.8709212801805,
              "2024": -34.04164772965305,
              "2025": -114.6306444729853
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 380.96328681841624,
              "2021": 303.57145325487,
              "2022": 179.12799511608682,
              "2023": 35.361131775734975,
              "2024": 383.2737007855685,
              "2025": 463.86269752890075
            }
          },
          "C": {
            "observed_mean_USDT_month": 5.425626951898997,
            "observed_total_USDT": 330.9632440658388,
            "ci95_percentile_mean_USDT_month": [
              -14.861155680133633,
              27.894518808260994
            ],
            "fraction_bootstrap_means_gt_zero": 0.6777,
            "positive_delta_months": 28,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.7897367463156,
            "delta_omitting_best_month_arithmetic_USDT": -62.826492680476804,
            "year_delta_USDT": {
              "2020": -28.923563857602858,
              "2021": 26.12168760300301,
              "2022": 166.06137293689062,
              "2023": 335.2334431373256,
              "2024": -34.50926226997581,
              "2025": -133.02043348380175
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 359.88680792344167,
              "2021": 304.8415564628358,
              "2022": 164.9018711289482,
              "2023": -4.270199071486786,
              "2024": 365.4725063358146,
              "2025": 463.98367754964056
            }
          }
        }
      },
      "included63": {
        "months": 63,
        "period_start": "2020-10",
        "period_last": "2025-12",
        "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 8.35933428166662,
            "observed_total_USDT": 526.638059744997,
            "ci95_percentile_mean_USDT_month": [
              -10.772111865404026,
              29.440652708444023
            ],
            "fraction_bootstrap_means_gt_zero": 0.7829,
            "positive_delta_months": 31,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.0685127057204,
            "delta_omitting_best_month_arithmetic_USDT": 126.56954703927659,
            "year_delta_USDT": {
              "2020": -31.73123376250078,
              "2021": 45.660599801045464,
              "2022": 170.10405793982864,
              "2023": 313.8709212801805,
              "2024": -34.04164772965305,
              "2025": 62.775362216096255
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 558.3692935074978,
              "2021": 480.97745994395154,
              "2022": 356.5340018051684,
              "2023": 212.76713846481653,
              "2024": 560.6797074746501,
              "2025": 463.86269752890075
            }
          },
          "C": {
            "observed_mean_USDT_month": 8.067379053569889,
            "observed_total_USDT": 508.244880374903,
            "ci95_percentile_mean_USDT_month": [
              -10.968305182075092,
              28.95891980795132
            ],
            "fraction_bootstrap_means_gt_zero": 0.7802,
            "positive_delta_months": 29,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.7897367463156,
            "delta_omitting_best_month_arithmetic_USDT": 114.4551436285874,
            "year_delta_USDT": {
              "2020": -28.923563857602858,
              "2021": 26.12168760300301,
              "2022": 166.06137293689062,
              "2023": 335.2334431373256,
              "2024": -34.50926226997581,
              "2025": 44.261202825262444
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 537.1684442325059,
              "2021": 482.1231927719,
              "2022": 342.1835074380124,
              "2023": 173.0114372375774,
              "2024": 542.7541426448788,
              "2025": 463.98367754964056
            }
          }
        }
      }
    },
    "audits": {
      "N204B": {
        "name": "N204B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.639344262295082,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 63,
        "win_months_all": 0.6190476190476191,
        "win_months_active": 0.6190476190476191,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.038848358930312465
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.03999068035568787
        ],
        "daily_close_drawdown_pct": -9.01691364981122,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.05686964789050527,
            "SPY-USDT": -0.04147158152763868
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.05686964789050527,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.014546551320336939
          },
          "SPY-USDT": {
            "BTC-USDT": -0.04147158152763868,
            "PAXG-USDT": -0.014546551320336939,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.04176490528852406,
          "2021-12-31 00:00:00+00:00": 0.19293771742976462,
          "2022-12-31 00:00:00+00:00": 0.09627479171191311,
          "2023-12-31 00:00:00+00:00": 0.17010613650971895,
          "2024-12-31 00:00:00+00:00": 0.1476817377857611,
          "2025-12-31 00:00:00+00:00": 0.10775186795994296
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 0,
          "boundary_liquidations_reconciled": 0,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "N204C": {
        "name": "N204C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.639344262295082,
          "quarters_total": 19,
          "positive_quarters": 17,
          "win_quarters": 0.8947368421052632
        },
        "months_total": 63,
        "months_active": 63,
        "win_months_all": 0.6190476190476191,
        "win_months_active": 0.6190476190476191,
        "win_quarters": 0.8571428571428571,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.047251327773334295
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.04816889094485366
        ],
        "daily_close_drawdown_pct": -9.129358487210226,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.05689878151177862,
            "SPY-USDT": -0.026303851392886733
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.05689878151177862,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.05103008928419279
          },
          "SPY-USDT": {
            "BTC-USDT": -0.026303851392886733,
            "PAXG-USDT": 0.05103008928419279,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.04066056152449837,
          "2021-12-31 00:00:00+00:00": 0.17303460717258634,
          "2022-12-31 00:00:00+00:00": 0.09933372295964626,
          "2023-12-31 00:00:00+00:00": 0.20948307076791073,
          "2024-12-31 00:00:00+00:00": 0.14209026334265262,
          "2025-12-31 00:00:00+00:00": 0.10095775196807155
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 1,
          "boundary_liquidations_reconciled": 1,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "Y902B": {
        "name": "Y902B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 60,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.65,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 62,
        "win_months_all": 0.6190476190476191,
        "win_months_active": 0.6290322580645161,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.03888659189731081
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.030451527729527417
        ],
        "daily_close_drawdown_pct": -9.923047650902506,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.10595059634836348,
            "SPY-USDT": -0.058850821629337795
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.10595059634836348,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.014310818094434479
          },
          "SPY-USDT": {
            "BTC-USDT": -0.058850821629337795,
            "PAXG-USDT": -0.014310818094434479,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03859178191227408,
          "2021-12-31 00:00:00+00:00": 0.19792357929736681,
          "2022-12-31 00:00:00+00:00": 0.10983927548507899,
          "2023-12-31 00:00:00+00:00": 0.19056989340064479,
          "2024-12-31 00:00:00+00:00": 0.14113817299290132,
          "2025-12-31 00:00:00+00:00": 0.1084338218840859
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 0,
          "boundary_liquidations_reconciled": 0,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "Y902C": {
        "name": "Y902C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 60,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6666666666666666,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 62,
        "win_months_all": 0.6349206349206349,
        "win_months_active": 0.6451612903225806,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04730147962280684
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.03894627094830605
        ],
        "daily_close_drawdown_pct": -9.910800423988086,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.10574946115703875,
            "SPY-USDT": -0.09982191619622986
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.10574946115703875,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.05167426692483015
          },
          "SPY-USDT": {
            "BTC-USDT": -0.09982191619622986,
            "PAXG-USDT": 0.05167426692483015,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03776820513873802,
          "2021-12-31 00:00:00+00:00": 0.17603397301931434,
          "2022-12-31 00:00:00+00:00": 0.11296308942708433,
          "2023-12-31 00:00:00+00:00": 0.23164530857531296,
          "2024-12-31 00:00:00+00:00": 0.1357936399299018,
          "2025-12-31 00:00:00+00:00": 0.10082189127555097
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 1,
          "boundary_liquidations_reconciled": 1,
          "boundary_close_is_execution_liquidity_proof": false
        }
      }
    },
    "anchors": {
      "BTC-USDT": {
        "anchor_count": 55,
        "distinct_anchor_timestamps": 35,
        "scale": 1.1501999999999981,
        "max_relative_error": 1.3322676295501878e-15
      },
      "PAXG-USDT": {
        "anchor_count": 24,
        "distinct_anchor_timestamps": 15,
        "scale": 0.19228799999999985,
        "max_relative_error": 1.5543122344752192e-15
      },
      "SPY-USDT": {
        "anchor_count": 17,
        "distinct_anchor_timestamps": 16,
        "scale": 0.034843459999999944,
        "max_relative_error": 1.5543122344752192e-15
      }
    },
    "sessions": {
      "N204B": {
        "session_id": "9a6c7c24-8847-42d1-aadb-206f21723c1f",
        "fee_per_side": 0.0007,
        "net": 10267.311379187326,
        "title": "MCP Backtest: X03 R2 CONF5 B — selected N204 engine-fee confirmation",
        "dashboard_url": null
      },
      "N204C": {
        "session_id": "541d2bf4-ffca-4f2d-969b-c25165e7b960",
        "fee_per_side": 0.0007,
        "net": 10408.935273900948,
        "title": "MCP Backtest: X03 R2 CONF5 C — selected N204 engine-fee confirmation",
        "dashboard_url": null
      },
      "Y902B": {
        "session_id": "c20f22a8-38bf-4ad3-99d0-2d583d91d81c",
        "fee_per_side": 0.0007,
        "net": 10793.949438932308,
        "title": "MCP Backtest: BTC R9 F70B validation",
        "dashboard_url": null
      },
      "Y902C": {
        "session_id": "2297b82f-5db7-457a-8d46-9b53465dde7d",
        "fee_per_side": 0.0007,
        "net": 10917.180154275862,
        "title": "MCP Backtest: BTC R9 F70C validation",
        "dashboard_url": null
      }
    },
    "limitations": "Reused development sample; descriptive conditional resampling, not probability of true edge, OOS, selection correction or replay of capital."
  }
}
```

### F95

Analysis job: 3224245554404942a8def4d4cb26ed83. Inputs: ocho snapshots completos, todosfinished, manifiesto original del job conservado debajo. Anclasbenchmarks/fade/reject/sleevesidénticasentrejobs.

- N204B: http://localhost:9200/#/backtest/9b7b99b1-a5a1-440d-98f5-aa1c45a1108c
- N204C: http://localhost:9200/#/backtest/b1399fa4-5495-43c1-bc45-3bc6d1b3da7b
- Y902B: http://localhost:9200/#/backtest/2b1ef237-1c48-40a9-84b3-d939ab99a3ba
- Y902C: http://localhost:9200/#/backtest/26f5560f-8db8-45f4-8203-1d0612658136

```json
{
  "manifest": [
    {
      "name": "benchmarks",
      "file": "inputs/benchmarks.json",
      "session_type": "backtest",
      "session_id": "2e943276-7815-4280-96c8-d634d2dab817",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 three-asset STOP session-filtered control",
      "size_bytes": 737286
    },
    {
      "name": "fade",
      "file": "inputs/fade.json",
      "session_type": "backtest",
      "session_id": "b6f5562e-2144-4a54-9d27-108155680338",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetRallyFade4h",
      "size_bytes": 380556
    },
    {
      "name": "reject",
      "file": "inputs/reject.json",
      "session_type": "backtest",
      "session_id": "5c8e7296-fdc3-46a6-8663-ff00ff0b1d20",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetRejectShort4h",
      "size_bytes": 574222
    },
    {
      "name": "sleeves",
      "file": "inputs/sleeves.json",
      "session_type": "backtest",
      "session_id": "262fb59f-2b20-4247-aa9a-e7823cc3c930",
      "session_status": "finished",
      "title": "MCP Backtest: Phase2 corrected margin: MultiAssetSleeves4h",
      "size_bytes": 397128
    },
    {
      "name": "N204B",
      "file": "inputs/N204B.json",
      "session_type": "backtest",
      "session_id": "9b7b99b1-a5a1-440d-98f5-aa1c45a1108c",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R9 N95B validation",
      "size_bytes": 526677
    },
    {
      "name": "N204C",
      "file": "inputs/N204C.json",
      "session_type": "backtest",
      "session_id": "b1399fa4-5495-43c1-bc45-3bc6d1b3da7b",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R9 N95C validation",
      "size_bytes": 536490
    },
    {
      "name": "Y902B",
      "file": "inputs/Y902B.json",
      "session_type": "backtest",
      "session_id": "2b1ef237-1c48-40a9-84b3-d939ab99a3ba",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R9 F95B validation",
      "size_bytes": 484132
    },
    {
      "name": "Y902C",
      "file": "inputs/Y902C.json",
      "session_type": "backtest",
      "session_id": "26f5560f-8db8-45f4-8203-1d0612658136",
      "session_status": "finished",
      "title": "MCP Backtest: BTC R9 F95C validation",
      "size_bytes": 493679
    }
  ],
  "results": {
    "fee_level": "F95",
    "seed": 9022026,
    "replicates": 10000,
    "circular_block_months": 6,
    "samples": {
      "full61": {
        "months": 61,
        "period_start": "2020-11",
        "period_last": "2025-11",
        "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 6.852541806546842,
            "observed_total_USDT": 418.00505019935736,
            "ci95_percentile_mean_USDT_month": [
              -12.815780307570055,
              29.144849976911324
            ],
            "fraction_bootstrap_means_gt_zero": 0.7293,
            "positive_delta_months": 29,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.312404021799,
            "delta_omitting_best_month_arithmetic_USDT": 24.692646177558345,
            "year_delta_USDT": {
              "2020": -27.273064877230354,
              "2021": 40.29017471694533,
              "2022": 190.52052043074036,
              "2023": 339.62310783658904,
              "2024": -23.070198451443503,
              "2025": -102.08548945624352
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 445.2781150765877,
              "2021": 377.714875482412,
              "2022": 227.484529768617,
              "2023": 78.38194236276831,
              "2024": 441.07524865080086,
              "2025": 520.0905396556009
            }
          },
          "C": {
            "observed_mean_USDT_month": 7.370821106775469,
            "observed_total_USDT": 449.6200875133036,
            "ci95_percentile_mean_USDT_month": [
              -12.381813987208616,
              29.370157543822952
            ],
            "fraction_bootstrap_means_gt_zero": 0.7477,
            "positive_delta_months": 30,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 384.85027873193394,
            "delta_omitting_best_month_arithmetic_USDT": 64.76980878136965,
            "year_delta_USDT": {
              "2020": -28.621076137931595,
              "2021": 46.37759523836576,
              "2022": 187.26796634474704,
              "2023": 359.39469808471586,
              "2024": -24.06544229000974,
              "2025": -90.73365372658373
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 478.2411636512352,
              "2021": 403.24249227493783,
              "2022": 262.35212116855655,
              "2023": 90.22538942858773,
              "2024": 473.68552980331333,
              "2025": 540.3537412398873
            }
          }
        }
      },
      "included63": {
        "months": 63,
        "period_start": "2020-10",
        "period_last": "2025-12",
        "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 9.33597034360915,
            "observed_total_USDT": 588.1661316473765,
            "ci95_percentile_mean_USDT_month": [
              -9.194416192184264,
              29.935087801304803
            ],
            "fraction_bootstrap_means_gt_zero": 0.8175,
            "positive_delta_months": 30,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.312404021799,
            "delta_omitting_best_month_arithmetic_USDT": 194.85372762557745,
            "year_delta_USDT": {
              "2020": -27.273064877230354,
              "2021": 40.29017471694533,
              "2022": 190.52052043074036,
              "2023": 339.62310783658904,
              "2024": -23.070198451443503,
              "2025": 68.07559199177558
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 615.4391965246068,
              "2021": 547.8759569304311,
              "2022": 397.6456112166361,
              "2023": 248.54302381078742,
              "2024": 611.23633009882,
              "2025": 520.0905396556009
            }
          },
          "C": {
            "observed_mean_USDT_month": 9.784708484292914,
            "observed_total_USDT": 616.4366345104536,
            "ci95_percentile_mean_USDT_month": [
              -8.678941843031119,
              30.223927752737783
            ],
            "fraction_bootstrap_means_gt_zero": 0.8345,
            "positive_delta_months": 31,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 384.85027873193394,
            "delta_omitting_best_month_arithmetic_USDT": 231.58635577851965,
            "year_delta_USDT": {
              "2020": -28.621076137931595,
              "2021": 46.37759523836576,
              "2022": 187.26796634474704,
              "2023": 359.39469808471586,
              "2024": -24.06544229000974,
              "2025": 76.08289327056627
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 645.0577106483852,
              "2021": 570.0590392720878,
              "2022": 429.16866816570655,
              "2023": 257.04193642573773,
              "2024": 640.5020768004633,
              "2025": 540.3537412398873
            }
          }
        }
      }
    },
    "audits": {
      "N204B": {
        "name": "N204B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "months_total": 63,
        "months_active": 63,
        "win_months_all": 0.5873015873015873,
        "win_months_active": 0.5873015873015873,
        "win_quarters": 0.7619047619047619,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.039177614971507624
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.040580995764218475
        ],
        "daily_close_drawdown_pct": -9.284247101760801,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.0645674185673493,
            "SPY-USDT": -0.037044726438042436
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.0645674185673493,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.009909162333127962
          },
          "SPY-USDT": {
            "BTC-USDT": -0.037044726438042436,
            "PAXG-USDT": -0.009909162333127962,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03917120743685154,
          "2021-12-31 00:00:00+00:00": 0.18226255985092954,
          "2022-12-31 00:00:00+00:00": 0.08494277200116374,
          "2023-12-31 00:00:00+00:00": 0.15735921423311794,
          "2024-12-31 00:00:00+00:00": 0.13102442223929756,
          "2025-12-31 00:00:00+00:00": 0.08793270537370224
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 0,
          "boundary_liquidations_reconciled": 0,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "N204C": {
        "name": "N204C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6229508196721312,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 63,
        "win_months_all": 0.6031746031746031,
        "win_months_active": 0.6031746031746031,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.047444595864295835
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.04901335504001203
        ],
        "daily_close_drawdown_pct": -9.29660052880006,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.06479800663884741,
            "SPY-USDT": -0.02852269459870349
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.06479800663884741,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.05816346059845385
          },
          "SPY-USDT": {
            "BTC-USDT": -0.02852269459870349,
            "PAXG-USDT": 0.05816346059845385,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03836464211546797,
          "2021-12-31 00:00:00+00:00": 0.1606428666411599,
          "2022-12-31 00:00:00+00:00": 0.08723104746736565,
          "2023-12-31 00:00:00+00:00": 0.19334999293717647,
          "2024-12-31 00:00:00+00:00": 0.12429216776288565,
          "2025-12-31 00:00:00+00:00": 0.0802189450336841
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 1,
          "boundary_liquidations_reconciled": 1,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "Y902B": {
        "name": "Y902B",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 60,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6333333333333333,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "months_total": 63,
        "months_active": 62,
        "win_months_all": 0.6031746031746031,
        "win_months_active": 0.6129032258064516,
        "win_quarters": 0.7619047619047619,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.03909808977169993
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.0312089025654253
        ],
        "daily_close_drawdown_pct": -10.144603562492172,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.11042183773758557,
            "SPY-USDT": -0.05754639784646065
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.11042183773758557,
            "PAXG-USDT": 1,
            "SPY-USDT": -0.009669708328864064
          },
          "SPY-USDT": {
            "BTC-USDT": -0.05754639784646065,
            "PAXG-USDT": -0.009669708328864064,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.036443900949128416,
          "2021-12-31 00:00:00+00:00": 0.1866295143281571,
          "2022-12-31 00:00:00+00:00": 0.10034391625772643,
          "2023-12-31 00:00:00+00:00": 0.1800886834754405,
          "2024-12-31 00:00:00+00:00": 0.12512350108974468,
          "2025-12-31 00:00:00+00:00": 0.08917615998801698
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 0,
          "boundary_liquidations_reconciled": 0,
          "boundary_close_is_execution_liquidity_proof": false
        }
      },
      "Y902C": {
        "name": "Y902C",
        "method": "UTC day-close MTM from executed fills, right-edge inclusive",
        "partial_boundary_periods_included": true,
        "complete_periods": {
          "months_total": 61,
          "months_active": 60,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.65,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "months_total": 63,
        "months_active": 62,
        "win_months_all": 0.6190476190476191,
        "win_months_active": 0.6290322580645161,
        "win_quarters": 0.8095238095238095,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.047586678082081835
        ],
        "worst_quarter": [
          "2021-06-30 00:00:00+00:00",
          -0.03976554950208122
        ],
        "daily_close_drawdown_pct": -10.153041319267453,
        "mtm_route_contribution_correlation": {
          "BTC-USDT": {
            "BTC-USDT": 1,
            "PAXG-USDT": -0.11064020338315861,
            "SPY-USDT": -0.09713904185748623
          },
          "PAXG-USDT": {
            "BTC-USDT": -0.11064020338315861,
            "PAXG-USDT": 1,
            "SPY-USDT": 0.058805842200698656
          },
          "SPY-USDT": {
            "BTC-USDT": -0.09713904185748623,
            "PAXG-USDT": 0.058805842200698656,
            "SPY-USDT": 1
          }
        },
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03550253450167484,
          "2021-12-31 00:00:00+00:00": 0.16556563266606883,
          "2022-12-31 00:00:00+00:00": 0.10261856446688156,
          "2023-12-31 00:00:00+00:00": 0.21737711308949392,
          "2024-12-31 00:00:00+00:00": 0.11847653396699953,
          "2025-12-31 00:00:00+00:00": 0.08202555415813517
        },
        "terminal_reconciles": true,
        "terminal_diagnostics": {
          "pretermination_open_counter": 1,
          "boundary_liquidations_reconciled": 1,
          "boundary_close_is_execution_liquidity_proof": false
        }
      }
    },
    "anchors": {
      "BTC-USDT": {
        "anchor_count": 55,
        "distinct_anchor_timestamps": 35,
        "scale": 1.1501999999999981,
        "max_relative_error": 1.3322676295501878e-15
      },
      "PAXG-USDT": {
        "anchor_count": 24,
        "distinct_anchor_timestamps": 15,
        "scale": 0.19228799999999985,
        "max_relative_error": 1.5543122344752192e-15
      },
      "SPY-USDT": {
        "anchor_count": 17,
        "distinct_anchor_timestamps": 16,
        "scale": 0.034843459999999944,
        "max_relative_error": 1.5543122344752192e-15
      }
    },
    "sessions": {
      "N204B": {
        "session_id": "9b7b99b1-a5a1-440d-98f5-aa1c45a1108c",
        "fee_per_side": 0.00095,
        "net": 8982.353704810404,
        "title": "MCP Backtest: BTC R9 N95B validation",
        "dashboard_url": null
      },
      "N204C": {
        "session_id": "b1399fa4-5495-43c1-bc45-3bc6d1b3da7b",
        "fee_per_side": 0.00095,
        "net": 8990.183159887889,
        "title": "MCP Backtest: BTC R9 N95C validation",
        "dashboard_url": null
      },
      "Y902B": {
        "session_id": "2b1ef237-1c48-40a9-84b3-d939ab99a3ba",
        "fee_per_side": 0.00095,
        "net": 9570.519836457781,
        "title": "MCP Backtest: BTC R9 F95B validation",
        "dashboard_url": null
      },
      "Y902C": {
        "session_id": "26f5560f-8db8-45f4-8203-1d0612658136",
        "fee_per_side": 0.00095,
        "net": 9606.619794398339,
        "title": "MCP Backtest: BTC R9 F95C validation",
        "dashboard_url": null
      }
    },
    "limitations": "Reused development sample; descriptive conditional resampling, not probability of true edge, OOS, selection correction or replay of capital."
  }
}
```
