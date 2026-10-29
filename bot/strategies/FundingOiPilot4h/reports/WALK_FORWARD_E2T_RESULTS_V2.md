# Resultados V2 — E2T
Ventana [2020-09-01,2022-07-01). Cuatro sesiones independientes con 10000 iniciales cada una; controles fijos reutilizados. Fee0,00045 por lado, slip0,isolated3x,funding ON. Sin sumar variantes como cuenta.

Entrenamiento expansivo: aplicar gates de protocolo antes de evaluación.

| Configuración | N | Neto % | PF | DD % | Turnover |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/8042b1d6-268a-4c60-9545-1147b44f9851) | 377 | -36.44 | 0.903 | -53.73 | 624.55 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/aa5a6fd5-08c4-4ce8-9d2e-c9ada34fbe9b) | 271 | 1.48 | 1.005 | -36.56 | 549.91 |
| [H1_ATR_P](http://localhost:9200/#/backtest/0062cce6-a9bb-4f00-8fd4-3ad5967edc70) | 353 | -16.43 | 0.928 | -40.39 | 313.34 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/6686347f-bf6e-4d7c-b2b5-202321321786) | 256 | 10.59 | 1.059 | -30.65 | 268.98 |

| Configuración | Bruto USDT | Fees | Funding | Neto |
|---|---:|---:|---:|---:|
| H1_FIXED_P | -350.45 | 2810.46 | -483.42 | -3644.33 |
| H1_FIXED_POI | 2992.36 | 2474.60 | -369.77 | 147.99 |
| H1_ATR_P | 182.03 | 1410.02 | -414.93 | -1642.92 |
| H1_ATR_POI | 2596.04 | 1210.42 | -326.24 | 1059.38 |

## Dirección
| Configuración | Dirección | N | Neto |
|---|---|---:|---:|
| H1_FIXED_P | long | 201 | -1342.73 |
| H1_FIXED_P | short | 176 | -2301.59 |
| H1_FIXED_POI | long | 150 | 41.89 |
| H1_FIXED_POI | short | 121 | 106.10 |
| H1_ATR_P | long | 191 | 661.36 |
| H1_ATR_P | short | 162 | -2304.28 |
| H1_ATR_POI | long | 142 | 2270.22 |
| H1_ATR_POI | short | 114 | -1210.84 |

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
| 2022-06 | 4.18 | 0.40 | 5.43 | 1.27 |

## Evidencia y límites
Auditoría de snapshots completos: V2_AUDIT_E2T.json; job 7ddbdeab507541d78838eaafe7998b26. Error máximo 2.000888e-11USDT. Fuente de análisis, config, concentración, exposición y detalle de dirección en ese JSON.
No sumar train solapados. Meses usan curva diaria y convención de borde00:00/00:01 de V1; DD de tabla es motor, no índice intraminuto. Métricas total_open_trades/open_pl pueden ser previas al cierre forzado; trades,ledger,saldo final y logs posteriores son los que se concilian, sin inferir posiciones residuales.
OI retrospectivo sin certificación PIT, funding con marcas proxy; no supervivencia económica de fricción. Código/config congelados, sin abrir2026. Las evaluaciones conocidas de controles no son muestra nueva.
