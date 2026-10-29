# Resultados V2 — E2V
Ventana [2022-07-01,2023-01-01). Cuatro sesiones independientes con 10000 iniciales cada una; controles fijos reutilizados. Fee0,00045 por lado, slip0,isolated3x,funding ON. Sin sumar variantes como cuenta.

Evaluación diagnóstica: el selector del fold quedó plano por selección previa SIN_CANDIDATA.

| Configuración | N | Neto % | PF | DD % | Turnover |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/5ba6d867-c4ca-477a-bd8f-25353a8a9eb7) | 96 | -10.94 | 0.865 | -29.11 | 163.11 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f) | 64 | -5.52 | 0.904 | -14.33 | 117.76 |
| [H1_ATR_P](http://localhost:9200/#/backtest/3a3bef6f-0aa5-4ceb-9cf1-5ff0f0150c3e) | 90 | 2.50 | 1.044 | -15.74 | 122.04 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/9b2fac46-e31c-46a2-96b9-36f52b214589) | 60 | 3.08 | 1.078 | -7.46 | 86.10 |

| Configuración | Bruto USDT | Fees | Funding | Neto |
|---|---:|---:|---:|---:|
| H1_FIXED_P | -355.89 | 733.98 | -4.11 | -1093.98 |
| H1_FIXED_POI | -5.00 | 529.93 | -17.07 | -552.01 |
| H1_ATR_P | 812.97 | 549.19 | -13.79 | 250.00 |
| H1_ATR_POI | 716.89 | 387.44 | -20.99 | 308.46 |

## Dirección
| Configuración | Dirección | N | Neto |
|---|---|---:|---:|
| H1_FIXED_P | long | 47 | -1532.65 |
| H1_FIXED_P | short | 49 | 438.66 |
| H1_FIXED_POI | long | 39 | -587.73 |
| H1_FIXED_POI | short | 25 | 35.73 |
| H1_ATR_P | long | 42 | 600.50 |
| H1_ATR_P | short | 48 | -350.50 |
| H1_ATR_POI | long | 36 | 394.87 |
| H1_ATR_POI | short | 24 | -86.42 |

## Meses completos
| Mes | FIXED_P % | FIXED_POI % | ATR_P % | ATR_POI % |
|---|---:|---:|---:|---:|
| 2022-07 | 1.71 | -0.92 | 8.96 | 6.49 |
| 2022-08 | -18.50 | -5.57 | -10.17 | -1.57 |
| 2022-09 | -8.82 | -4.20 | -4.26 | -3.72 |
| 2022-10 | 4.93 | 7.09 | 3.91 | 6.02 |
| 2022-11 | 17.32 | 2.75 | 9.53 | -0.40 |
| 2022-12 | -4.28 | -4.20 | -3.91 | -3.26 |

## Evidencia y límites
Auditoría de snapshots completos: V2_AUDIT_E2V.json; job 7a094179e205496fad78513f8f06b3a4. Error máximo 1.091394e-11USDT. Fuente de análisis, config, concentración, exposición y detalle de dirección en ese JSON.
No sumar train solapados. Meses usan curva diaria y convención de borde00:00/00:01 de V1; DD de tabla es motor, no índice intraminuto. Métricas total_open_trades/open_pl pueden ser previas al cierre forzado; trades,ledger,saldo final y logs posteriores son los que se concilian, sin inferir posiciones residuales.
OI retrospectivo sin certificación PIT, funding con marcas proxy; no supervivencia económica de fricción. Código/config congelados, sin abrir2026. Las evaluaciones conocidas de controles no son muestra nueva.
