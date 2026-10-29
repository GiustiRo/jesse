# Resultados V2 — E3T
Ventana [2020-09-01,2023-01-01). Cuatro sesiones independientes con 10000 iniciales cada una; controles fijos reutilizados. Fee0,00045 por lado, slip0,isolated3x,funding ON. Sin sumar variantes como cuenta.

Entrenamiento expansivo: aplicar gates de protocolo antes de evaluación.

| Configuración | N | Neto % | PF | DD % | Turnover |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/1f11e4be-bb91-4445-b6df-662f909ed76d) | 473 | -43.40 | 0.898 | -61.60 | 728.21 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/d546fc9f-90bf-45d4-85b7-fa6d29d4736f) | 335 | -4.12 | 0.989 | -36.56 | 669.42 |
| [H1_ATR_P](http://localhost:9200/#/backtest/2f62f8ef-ba51-4308-a10e-8a4514327709) | 443 | -14.96 | 0.946 | -40.39 | 414.60 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/a0f71b9c-3de8-40d7-a714-7bdfa7492c4c) | 316 | 14.01 | 1.063 | -30.65 | 364.20 |

| Configuración | Bruto USDT | Fees | Funding | Neto |
|---|---:|---:|---:|---:|
| H1_FIXED_P | -576.64 | 3276.95 | -486.03 | -4339.63 |
| H1_FIXED_POI | 2987.28 | 3012.37 | -387.09 | -412.18 |
| H1_ATR_P | 796.42 | 1865.69 | -426.73 | -1496.00 |
| H1_ATR_POI | 3388.88 | 1638.91 | -349.45 | 1400.51 |

## Dirección
| Configuración | Dirección | N | Neto |
|---|---|---:|---:|
| H1_FIXED_P | long | 248 | -2316.83 |
| H1_FIXED_P | short | 225 | -2022.80 |
| H1_FIXED_POI | long | 189 | -554.54 |
| H1_FIXED_POI | short | 146 | 142.35 |
| H1_ATR_P | long | 233 | 1159.57 |
| H1_ATR_P | short | 210 | -2655.57 |
| H1_ATR_POI | long | 178 | 2706.93 |
| H1_ATR_POI | short | 138 | -1306.41 |

## Meses completos
| Mes | FIXED_P % | FIXED_POI % | ATR_P % | ATR_POI % |
|---|---:|---:|---:|---:|
| 2020-09 | -1.41 | -3.05 | -4.63 | -1.47 |
| 2020-10 | 2.66 | 4.73 | 1.43 | 6.40 |
| 2020-11 | 19.50 | 14.51 | 10.92 | 7.61 |
| 2020-12 | -3.76 | 5.18 | 10.86 | 13.04 |
| 2021-01 | 4.28 | 13.06 | -0.12 | 5.67 |
| 2021-02 | -18.60 | -16.15 | -4.67 | -4.23 |
| 2021-03 | 7.40 | -1.53 | -1.69 | -3.13 |
| 2021-04 | -4.46 | -7.14 | -1.95 | -4.12 |
| 2021-05 | -17.41 | -1.38 | -8.45 | 0.99 |
| 2021-06 | 0.27 | 3.08 | -1.81 | -0.97 |
| 2021-07 | 2.38 | -3.68 | -4.66 | -5.23 |
| 2021-08 | -10.89 | -3.38 | -5.18 | -5.06 |
| 2021-09 | -3.42 | -5.79 | -2.78 | -2.16 |
| 2021-10 | 7.71 | 9.38 | 5.46 | 3.43 |
| 2021-11 | 2.04 | 0.14 | 3.19 | -1.68 |
| 2021-12 | -12.22 | -9.96 | -6.98 | -7.00 |
| 2022-01 | -18.06 | -5.10 | -8.83 | -2.20 |
| 2022-02 | 1.07 | 6.74 | -1.60 | 6.37 |
| 2022-03 | 6.06 | 9.06 | 6.66 | 8.32 |
| 2022-04 | -6.06 | -4.02 | -9.33 | -4.75 |
| 2022-05 | 3.60 | 2.30 | 4.64 | 1.94 |
| 2022-06 | 4.18 | 0.40 | 5.79 | 1.27 |
| 2022-07 | 1.71 | -0.92 | 7.81 | 6.49 |
| 2022-08 | -18.50 | -5.57 | -10.17 | -1.57 |
| 2022-09 | -8.82 | -4.20 | -4.26 | -3.72 |
| 2022-10 | 4.93 | 7.09 | 3.91 | 6.02 |
| 2022-11 | 17.32 | 2.75 | 9.53 | -0.40 |
| 2022-12 | -4.28 | -4.20 | -3.91 | -3.26 |

## Evidencia y límites
Auditoría de snapshots completos: V2_AUDIT_E3T.json; job b464620d13c3491cbc1cd4e95bfc2b98. Error máximo 3.092282e-11USDT. Fuente de análisis, config, concentración, exposición y detalle de dirección en ese JSON.
No sumar train solapados. Meses usan curva diaria y convención de borde00:00/00:01 de V1; DD de tabla es motor, no índice intraminuto. Métricas total_open_trades/open_pl pueden ser previas al cierre forzado; trades,ledger,saldo final y logs posteriores son los que se concilian, sin inferir posiciones residuales.
OI retrospectivo sin certificación PIT, funding con marcas proxy; no supervivencia económica de fricción. Código/config congelados, sin abrir2026. Las evaluaciones conocidas de controles no son muestra nueva.
