# Resultados V2 — E3V
Ventana [2023-01-01,2023-07-01). Cuatro sesiones independientes con 10000 iniciales cada una; controles fijos reutilizados. Fee0,00045 por lado, slip0,isolated3x,funding ON. Sin sumar variantes como cuenta.

Evaluación diagnóstica: el selector del fold quedó plano por selección previa SIN_CANDIDATA.

| Configuración | N | Neto % | PF | DD % | Turnover |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/853089c6-86ed-4e36-a30e-833b61c5b382) | 85 | 20.32 | 1.253 | -17.38 | 188.84 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/22f19971-2e43-4987-b915-8a8504dea4f0) | 56 | 11.94 | 1.242 | -12.37 | 116.76 |
| [H1_ATR_P](http://localhost:9200/#/backtest/91147a26-0231-4731-86ac-31e3eea4f1ac) | 83 | 18.47 | 1.324 | -14.39 | 144.59 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/15edc301-842b-4376-9313-7a75e0ae1102) | 55 | 7.96 | 1.211 | -10.94 | 88.69 |

| Configuración | Bruto USDT | Fees | Funding | Neto |
|---|---:|---:|---:|---:|
| H1_FIXED_P | 2906.95 | 849.79 | -24.67 | 2032.48 |
| H1_FIXED_POI | 1738.14 | 525.42 | -18.63 | 1194.09 |
| H1_ATR_P | 2528.78 | 650.67 | -30.74 | 1847.38 |
| H1_ATR_POI | 1217.32 | 399.10 | -22.02 | 796.20 |

## Dirección
| Configuración | Dirección | N | Neto |
|---|---|---:|---:|
| H1_FIXED_P | long | 53 | 2081.64 |
| H1_FIXED_P | short | 32 | -49.15 |
| H1_FIXED_POI | long | 37 | 842.09 |
| H1_FIXED_POI | short | 19 | 352.00 |
| H1_ATR_P | long | 52 | 1368.08 |
| H1_ATR_P | short | 31 | 479.30 |
| H1_ATR_POI | long | 36 | 466.80 |
| H1_ATR_POI | short | 19 | 329.40 |

## Meses completos
| Mes | FIXED_P % | FIXED_POI % | ATR_P % | ATR_POI % |
|---|---:|---:|---:|---:|
| 2023-01 | 9.45 | 4.87 | 11.51 | 8.07 |
| 2023-02 | 3.94 | 6.26 | 3.02 | 1.42 |
| 2023-03 | 11.68 | 2.25 | 10.38 | 2.18 |
| 2023-04 | -4.72 | -3.78 | -2.47 | -2.11 |
| 2023-05 | -7.78 | -3.34 | -6.36 | -3.00 |
| 2023-06 | 7.77 | 5.64 | 2.31 | 1.54 |

## Evidencia y límites
Auditoría de snapshots completos: V2_AUDIT_E3V.json; job cf341d65d55541a799fb4b504398dd37. Error máximo 7.275958e-12USDT. Fuente de análisis, config, concentración, exposición y detalle de dirección en ese JSON.
No sumar train solapados. Meses usan curva diaria y convención de borde00:00/00:01 de V1; DD de tabla es motor, no índice intraminuto. Métricas total_open_trades/open_pl pueden ser previas al cierre forzado; trades,ledger,saldo final y logs posteriores son los que se concilian, sin inferir posiciones residuales.
OI retrospectivo sin certificación PIT, funding con marcas proxy; no supervivencia económica de fricción. Código/config congelados, sin abrir2026. Las evaluaciones conocidas de controles no son muestra nueva.
