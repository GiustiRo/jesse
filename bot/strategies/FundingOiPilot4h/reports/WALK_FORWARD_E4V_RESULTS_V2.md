# Resultados V2 — E4V
Ventana [2023-07-01,2024-01-01). Cuatro sesiones independientes con 10000 iniciales cada una; controles fijos reutilizados. Fee0,00045 por lado, slip0,isolated3x,funding ON. Sin sumar variantes como cuenta.

Evaluación diagnóstica: el selector del fold quedó plano por selección previa SIN_CANDIDATA.

| Configuración | N | Neto % | PF | DD % | Turnover |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/c29d757d-c834-49ba-8145-fbe8c952cc4f) | 68 | -5.99 | 0.884 | -15.84 | 120.73 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/706268de-8c74-401c-a17a-8bb9d55d6767) | 49 | -6.62 | 0.818 | -11.39 | 89.05 |
| [H1_ATR_P](http://localhost:9200/#/backtest/898996f7-f78c-4bf9-8058-de8b823dfadb) | 69 | 3.36 | 1.080 | -11.07 | 116.88 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/707881ef-fc9b-42d4-aec7-7932f74413b9) | 50 | 2.88 | 1.096 | -9.59 | 86.32 |

| Configuración | Bruto USDT | Fees | Funding | Neto |
|---|---:|---:|---:|---:|
| H1_FIXED_P | -53.16 | 543.28 | -2.46 | -598.90 |
| H1_FIXED_POI | -257.35 | 400.72 | -3.83 | -661.89 |
| H1_ATR_P | 855.08 | 525.97 | 7.16 | 336.26 |
| H1_ATR_POI | 673.61 | 388.43 | 3.05 | 288.23 |

## Dirección
| Configuración | Dirección | N | Neto |
|---|---|---:|---:|
| H1_FIXED_P | long | 38 | -100.62 |
| H1_FIXED_P | short | 30 | -498.28 |
| H1_FIXED_POI | long | 28 | -152.21 |
| H1_FIXED_POI | short | 21 | -509.68 |
| H1_ATR_P | long | 38 | 529.63 |
| H1_ATR_P | short | 31 | -193.36 |
| H1_ATR_POI | long | 28 | 549.41 |
| H1_ATR_POI | short | 22 | -261.18 |

## Meses completos
| Mes | FIXED_P % | FIXED_POI % | ATR_P % | ATR_POI % |
|---|---:|---:|---:|---:|
| 2023-07 | -11.08 | -5.48 | -8.73 | -5.89 |
| 2023-08 | -1.62 | -2.24 | -0.11 | -0.79 |
| 2023-09 | -2.47 | -3.92 | -0.05 | -1.84 |
| 2023-10 | 13.95 | 8.02 | 10.85 | 6.63 |
| 2023-11 | -0.70 | 3.34 | 1.05 | 3.62 |
| 2023-12 | -2.61 | -5.78 | 1.27 | 1.60 |

## Evidencia y límites
Auditoría de snapshots completos: V2_AUDIT_E4V.json; job 8c995833ae784198a0fa49d9be422e31. Error máximo 1.455192e-11USDT. Fuente de análisis, config, concentración, exposición y detalle de dirección en ese JSON.
No sumar train solapados. Meses usan curva diaria y convención de borde00:00/00:01 de V1; DD de tabla es motor, no índice intraminuto. Métricas total_open_trades/open_pl pueden ser previas al cierre forzado; trades,ledger,saldo final y logs posteriores son los que se concilian, sin inferir posiciones residuales.
OI retrospectivo sin certificación PIT, funding con marcas proxy; no supervivencia económica de fricción. Código/config congelados, sin abrir2026. Las evaluaciones conocidas de controles no son muestra nueva.
