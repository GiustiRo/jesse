# Resultados V2 — E1V
Ventana [2022-01-01,2022-07-01). Cuatro sesiones independientes con 10000 iniciales cada una; controles fijos reutilizados. Fee0,00045 por lado, slip0,isolated3x,funding ON. Sin sumar variantes como cuenta.

Evaluación diagnóstica: el selector del fold quedó plano por selección previa SIN_CANDIDATA.

| Configuración | N | Neto % | PF | DD % | Turnover |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/ed789043-2aa2-4714-8963-112eadbc56b8) | 93 | -10.94 | 0.884 | -20.77 | 155.63 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/88e7e822-cb4d-49f7-97ab-ec5743786d29) | 59 | 8.92 | 1.142 | -8.44 | 118.84 |
| [H1_ATR_P](http://localhost:9200/#/backtest/456e2c59-3c00-4404-8999-c57ab3b2efb0) | 90 | -4.29 | 0.928 | -16.10 | 83.35 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/a10275b7-6074-435a-980f-c76f9beb3d66) | 58 | 10.81 | 1.293 | -8.17 | 63.39 |

| Configuración | Bruto USDT | Fees | Funding | Neto |
|---|---:|---:|---:|---:|
| H1_FIXED_P | -380.19 | 700.34 | -13.91 | -1094.44 |
| H1_FIXED_POI | 1434.70 | 534.79 | -7.64 | 892.27 |
| H1_ATR_P | -42.53 | 375.10 | -11.18 | -428.81 |
| H1_ATR_POI | 1370.92 | 285.25 | -4.19 | 1081.48 |

## Dirección
| Configuración | Dirección | N | Neto |
|---|---|---:|---:|
| H1_FIXED_P | short | 55 | 448.54 |
| H1_FIXED_P | long | 38 | -1542.98 |
| H1_FIXED_POI | short | 33 | 1350.54 |
| H1_FIXED_POI | long | 26 | -458.27 |
| H1_ATR_P | short | 53 | -61.97 |
| H1_ATR_P | long | 37 | -366.83 |
| H1_ATR_POI | short | 32 | 883.38 |
| H1_ATR_POI | long | 26 | 198.10 |

## Meses completos
| Mes | FIXED_P % | FIXED_POI % | ATR_P % | ATR_POI % |
|---|---:|---:|---:|---:|
| 2022-01 | -18.06 | -5.10 | -8.83 | -2.20 |
| 2022-02 | 1.07 | 6.74 | -1.60 | 6.37 |
| 2022-03 | 6.06 | 9.06 | 6.66 | 8.32 |
| 2022-04 | -6.06 | -4.02 | -9.33 | -4.75 |
| 2022-05 | 3.60 | 2.30 | 4.64 | 1.94 |
| 2022-06 | 4.18 | 0.40 | 5.43 | 1.27 |

## Evidencia y límites
Auditoría de snapshots completos: V2_AUDIT_E1V.json; job f81e9c42202b4c8286350b8a55b8508e. Error máximo 9.094947e-12USDT. Fuente de análisis, config, concentración, exposición y detalle de dirección en ese JSON.
No sumar train solapados. Meses usan curva diaria y convención de borde00:00/00:01 de V1; DD de tabla es motor, no índice intraminuto. Métricas total_open_trades/open_pl pueden ser previas al cierre forzado; trades,ledger,saldo final y logs posteriores son los que se concilian, sin inferir posiciones residuales.
OI retrospectivo sin certificación PIT, funding con marcas proxy; no supervivencia económica de fricción. Código/config congelados, sin abrir2026. Las evaluaciones conocidas de controles no son muestra nueva.
