# Diagnóstico posterior de V1: costos, dirección y salidas
Fecha: 2026-10-20. Diagnóstico descriptivo; V1 continúa cerrada como SIN_CANDIDATA.

## Alcance y método
Se analizaron 60 snapshots completos de sesiones existentes mediante seis jobs MCP run_analysis: los 12 E1T (2020-09-01 → 2022-01-01) y las 48 evaluaciones E1V–E4V (2022-01-01 → 2024-01-01). Dentro de cada configuración, estas ventanas no se solapan. Los entrenamientos expansivos E2T–E4T se omiten para no duplicar trades ya observados.
Se mantienen separados 2020–2021 y 2022–2023. No se agregan estrategias entre sí: comparten operaciones y no son muestras independientes. Cada semestre de evaluación reinicia 10.000 USDT. Los netos sumados aquí son sumas nominales de PnL de sesiones independientes, no retorno de una cuenta continua ni rentabilidad anual.
Precio bruto = (salida − entrada) × cantidad × dirección; neto = precio bruto − fees + funding. Funding se reconstruye del ledger vinculado por trade_id. Error máximo 5.684342e-14 USDT.
Se incluyeron 4562 registros de operaciones entre variantes, sin afirmar independencia entre ellos. Las 48 evaluaciones contienen 2505 registros.
No hubo nuevos backtests, modificaciones de estrategia, consultas económicas 2024–2025 ni consultas de 2026. Tampoco RST, Monte Carlo, instalaciones ni reinicios. Las 96 sesiones económicas de V1 siguen siendo 96.

## Hallazgos
1. **No basta reducir costos.** H1_P en 2022–2023: precio +2.117,71; fees −2.827,39; funding −45,16; neto −754,85 USDT. H3_P: precio +3.336,41; fees −5.495,68; funding −78,27; neto −2.237,54. En 2020–2021 ambos controles ya eran negativos antes de costos (−79,12 y −642,65). Sus medias netas no ponderadas por notional fueron −9,43 y −10,95 bps por operación en ese primer período, y −0,89 y −2,57 bps en evaluación. La diferencia entre medias en bps y sumas en USDT refleja sizing y resets distintos; no es contradicción.
2. **H2 falla también antes de fees.** El control perdió por precio en ambos períodos (−1.994,71 y −1.131,54). OI produjo +303,12 netos en el primer período, pero −1.208,39 en evaluación. No hay base para priorizar esta reversión en el próximo ciclo.
3. **Funding como filtro fuerte deja poca evidencia.** H2_PF hizo dos trades en evaluación y H2_PFOI ninguno. H3_PF y H3_PFOI hicieron 28 y 15, ambos negativos incluso por precio. El funding cobrado ayuda en algunas variantes, pero no compensa esas pérdidas. H1_PF mejora descriptivamente frente a H1_P en evaluación, pero empeora en 2020–2021. No aporta una mejora estable entre ambos períodos.
4. **OI en H1 sigue siendo una hipótesis de filtro, no una candidata.** H1_POI dio +872,46 netos, PF 1,042 y 228 trades en evaluación; en 2020–2021 perdió −683,31 y PF 0,973. El aporte neto de evaluación se concentra en shorts (+1.228,58 frente a −356,12 long); en el primer período sucede lo contrario (+468,85 long y −1.152,15 short). No justificar eliminar una dirección retrospectivamente. Agregar funding empeora el neto de H1_POI a +325,59 en evaluación y a −920,57 en el primer período.
5. **El cierre a 24h no aparece como una fuente agregada de pérdida de los controles.** H1_P tiene 145 cierres de mercado compatibles con 24h en evaluación y suman +2.831,62 netos; H3_P tiene 352 y suman +9.144,94. Stops y targets sumados pierden −3.504,72 y −11.369,72 respectivamente. Esto describe grupos condicionados por la salida observada: stops pierden por diseño y targets ganan por diseño. No demuestra que ampliar stops, quitar objetivos, cambiar el holding o evitar esos trades hubiera mejorado el resultado.
6. **La asimetría contractual 2%/4% no garantiza expectativa positiva.** En H1_P hubo 133 stops y 63 targets en evaluación; en H3_P, 227 y 91. H2_P tuvo 50 y 16. Las ganancias de targets y cierres temporales no alcanzaron para cubrir stops y costos en esos controles.
7. Los pocos netos positivos de evaluación permanecen sujetos a concentración ya documentada: H1_POI, H1_PFOI y H3_POI cambian a negativo al quitar su mejor semestre. Este diagnóstico no altera la selección original ni abre confirmación.

## Descomposición 2020–2021
| Configuración | Trades | Precio bruto USDT | Fees | Funding | Neto | PF |
|---|---:|---:|---:|---:|---:|---:|
| H1_P | 284 | -79.12 | 2310.65 | -473.49 | -2863.25 | 0.907 |
| H1_PF | 277 | -1057.41 | 2101.02 | -441.55 | -3599.98 | 0.873 |
| H1_PFOI | 208 | 1328.06 | 1907.54 | -341.09 | -920.57 | 0.963 |
| H1_POI | 212 | 1655.69 | 1976.35 | -362.65 | -683.31 | 0.973 |
| H2_P | 104 | -1994.71 | 698.96 | 81.39 | -2612.28 | 0.721 |
| H2_PF | 6 | -371.61 | 50.12 | 55.46 | -366.27 | 0.453 |
| H2_PFOI | 4 | -84.87 | 33.87 | 48.54 | -70.20 | 0.817 |
| H2_POI | 56 | 685.95 | 451.94 | 69.11 | 303.12 | 1.056 |
| H3_P | 476 | -642.65 | 3659.23 | -403.14 | -4705.02 | 0.905 |
| H3_PF | 40 | -1763.51 | 310.24 | 144.03 | -1929.72 | 0.591 |
| H3_PFOI | 26 | -1725.91 | 199.05 | 107.45 | -1817.51 | 0.415 |
| H3_POI | 364 | -1525.72 | 2393.60 | -343.91 | -4263.23 | 0.868 |

## Descomposición 2022–2023
| Configuración | Trades | Precio bruto USDT | Fees | Funding | Neto | PF |
|---|---:|---:|---:|---:|---:|---:|
| H1_P | 342 | 2117.71 | 2827.39 | -45.16 | -754.85 | 0.975 |
| H1_PF | 329 | 2529.28 | 2742.04 | -51.04 | -263.80 | 0.991 |
| H1_PFOI | 219 | 2282.23 | 1911.96 | -44.68 | 325.59 | 1.016 |
| H1_POI | 228 | 2910.49 | 1990.86 | -47.17 | 872.46 | 1.042 |
| H2_P | 124 | -1131.54 | 1058.65 | -0.26 | -2190.45 | 0.806 |
| H2_PF | 2 | -128.63 | 17.22 | -0.71 | -146.55 | 0.269 |
| H2_PFOI | 0 | 0.00 | 0.00 | 0.00 | 0.00 | — |
| H2_POI | 69 | -611.30 | 585.21 | -11.87 | -1208.39 | 0.799 |
| H3_P | 672 | 3336.41 | 5495.68 | -78.27 | -2237.54 | 0.957 |
| H3_PF | 28 | -174.90 | 239.73 | 43.01 | -371.63 | 0.819 |
| H3_PFOI | 15 | -361.29 | 128.48 | 34.86 | -454.91 | 0.593 |
| H3_POI | 477 | 4728.18 | 3983.35 | -63.93 | 680.91 | 1.018 |

## Dirección y tipos de salida
Los stops se identifican por órdenes reduce_only ejecutadas tipo STOP; los objetivos por tipo LIMIT, consistentes con el código congelado. Para MARKET se infiere 24h cuando holding_period ≥ 86.400 segundos, o fin del fold si se ejecutó en su último minuto y antes de 24h. Esas inferencias no equivalen a un motivo explícito persistido. No aparecieron tipos ambiguos con estas reglas. Se conserva la clasificación y el código para auditarla.

### H1_P, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 163 | 1741.16 | 1352.69 | -630.02 | -241.55 | -2.38 | 14.72 |
| dirección short | 121 | -1820.27 | 957.96 | 156.53 | -2621.70 | -18.93 | 7.93 |
| market_24h_inferred | 69 | 3259.71 | 547.03 | -136.79 | 2575.89 | 43.43 | 24.00 |
| stop_order | 149 | -27235.04 | 1224.21 | -236.68 | -28695.93 | -210.58 | 6.32 |
| target_order | 66 | 23896.21 | 539.40 | -100.02 | 23256.79 | 389.42 | 7.50 |

### H1_P, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 176 | 586.26 | 1484.05 | -196.82 | -1094.61 | -6.14 | 17.68 |
| dirección short | 166 | 1531.44 | 1343.34 | 151.66 | 339.76 | 4.68 | 20.26 |
| market_24h_inferred | 145 | 4036.00 | 1195.59 | -8.79 | 2831.62 | 20.59 | 24.00 |
| market_fold_end_inferred | 1 | -73.61 | 8.14 | 0.00 | -81.75 | -90.05 | 4.00 |
| stop_order | 133 | -24672.15 | 1108.95 | -31.01 | -25812.11 | -209.23 | 8.35 |
| target_order | 63 | 22827.47 | 514.72 | -5.37 | 22307.39 | 390.94 | 9.28 |

### H1_PF, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 158 | 946.17 | 1221.73 | -585.98 | -861.54 | -6.81 | 14.59 |
| dirección short | 119 | -2003.59 | 879.29 | 144.43 | -2738.44 | -23.20 | 7.93 |
| market_24h_inferred | 65 | 2509.28 | 480.50 | -117.85 | 1910.93 | 37.19 | 24.00 |
| stop_order | 148 | -25193.21 | 1132.36 | -230.20 | -26555.77 | -210.64 | 6.80 |
| target_order | 64 | 21626.52 | 488.16 | -93.50 | 21044.85 | 389.38 | 7.96 |

### H1_PF, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 172 | 326.26 | 1462.01 | -190.67 | -1326.42 | -7.49 | 17.53 |
| dirección short | 157 | 2203.02 | 1280.03 | 139.62 | 1062.62 | 9.48 | 20.52 |
| market_24h_inferred | 141 | 3816.62 | 1163.79 | -9.17 | 2643.65 | 19.94 | 24.00 |
| market_fold_end_inferred | 1 | -76.69 | 8.48 | 0.00 | -85.17 | -90.05 | 4.00 |
| stop_order | 126 | -23669.67 | 1063.42 | -37.72 | -24770.82 | -209.29 | 8.09 |
| target_order | 61 | 22459.03 | 506.35 | -4.15 | 21948.54 | 390.96 | 9.28 |

### H1_PFOI, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 121 | 1877.97 | 1118.75 | -487.60 | 271.61 | 4.91 | 12.83 |
| dirección short | 87 | -549.91 | 788.78 | 146.52 | -1192.18 | -11.28 | 11.57 |
| market_24h_inferred | 50 | 3337.32 | 443.21 | -123.72 | 2770.39 | 56.48 | 24.00 |
| stop_order | 108 | -22374.32 | 1005.23 | -158.27 | -23537.82 | -210.25 | 8.76 |
| target_order | 50 | 20365.06 | 459.10 | -59.09 | 19846.87 | 389.94 | 6.72 |

### H1_PFOI, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 126 | 718.06 | 1103.59 | -147.01 | -532.53 | -1.68 | 18.43 |
| dirección short | 93 | 1564.17 | 808.37 | 102.32 | 858.12 | 9.78 | 24.00 |
| market_24h_inferred | 101 | 2188.03 | 865.48 | -20.04 | 1302.51 | 13.71 | 24.00 |
| stop_order | 78 | -15483.92 | 694.95 | -18.34 | -16197.21 | -209.20 | 9.25 |
| target_order | 40 | 15578.12 | 351.53 | -6.31 | 15220.29 | 390.81 | 9.92 |

### H1_POI, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 124 | 2148.04 | 1166.79 | -512.41 | 468.85 | 6.38 | 12.72 |
| dirección short | 88 | -492.35 | 809.56 | 149.76 | -1152.15 | -10.25 | 11.25 |
| market_24h_inferred | 53 | 3900.44 | 476.11 | -141.00 | 3283.33 | 62.43 | 24.00 |
| stop_order | 109 | -22983.32 | 1032.68 | -161.17 | -24177.18 | -210.24 | 8.67 |
| target_order | 50 | 20738.57 | 467.55 | -60.48 | 20210.54 | 389.94 | 6.72 |

### H1_POI, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 130 | 939.16 | 1139.71 | -155.57 | -356.12 | -0.02 | 18.43 |
| dirección short | 98 | 1971.33 | 851.15 | 108.40 | 1228.58 | 13.35 | 23.71 |
| market_24h_inferred | 105 | 2663.33 | 904.18 | -21.48 | 1737.66 | 17.49 | 24.00 |
| stop_order | 81 | -16026.91 | 719.45 | -18.07 | -16764.44 | -209.19 | 9.17 |
| target_order | 42 | 16274.08 | 367.22 | -7.61 | 15899.24 | 390.79 | 9.92 |

### H2_P, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 46 | -356.99 | 301.37 | -95.78 | -754.14 | -17.22 | 9.69 |
| dirección short | 58 | -1637.72 | 397.58 | 177.17 | -1858.13 | -36.21 | 11.68 |
| market_24h_inferred | 32 | 986.79 | 226.77 | 36.01 | 796.03 | 40.41 | 24.00 |
| stop_order | 54 | -7986.97 | 359.84 | 28.57 | -8318.24 | -208.29 | 6.11 |
| target_order | 18 | 5005.47 | 112.35 | 16.81 | 4909.93 | 392.35 | 8.97 |

### H2_P, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 63 | -1113.81 | 545.66 | -57.27 | -1716.74 | -27.63 | 20.45 |
| dirección short | 61 | -17.73 | 512.99 | 57.01 | -473.71 | -7.78 | 22.78 |
| market_24h_inferred | 58 | 2273.01 | 476.30 | 2.38 | 1799.09 | 34.16 | 24.00 |
| stop_order | 50 | -9767.83 | 439.12 | -3.05 | -10210.00 | -209.05 | 6.54 |
| target_order | 16 | 6363.28 | 143.23 | 0.41 | 6220.45 | 391.03 | 7.58 |

### H2_PF, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 1 | -184.58 | 8.22 | 0.15 | -192.65 | -208.75 | 7.68 |
| dirección short | 5 | -187.03 | 41.90 | 55.31 | -173.62 | -34.37 | 24.00 |
| market_24h_inferred | 3 | 187.96 | 24.86 | 40.23 | 203.34 | 76.70 | 24.00 |
| stop_order | 3 | -559.57 | 25.27 | 15.22 | -569.61 | -203.56 | 6.55 |

### H2_PF, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 2 | -128.63 | 17.22 | -0.71 | -146.55 | -75.98 | 15.79 |
| dirección short | 0 | 0.00 | 0.00 | 0.00 | 0.00 | — | — |
| market_24h_inferred | 1 | 63.87 | 8.64 | -1.43 | 53.80 | 56.19 | 24.00 |
| stop_order | 1 | -192.50 | 8.58 | 0.73 | -200.35 | -208.16 | 7.58 |

### H2_PFOI, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 1 | -190.25 | 8.48 | 0.15 | -198.57 | -208.75 | 7.68 |
| dirección short | 3 | 105.38 | 25.39 | 48.39 | 128.37 | 47.33 | 24.00 |
| market_24h_inferred | 2 | 296.68 | 16.70 | 32.85 | 312.83 | 167.42 | 24.00 |
| stop_order | 2 | -381.56 | 17.17 | 15.69 | -383.04 | -200.80 | 7.12 |

### H2_PFOI, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 0 | 0.00 | 0.00 | 0.00 | 0.00 | — | — |
| dirección short | 0 | 0.00 | 0.00 | 0.00 | 0.00 | — | — |

### H2_POI, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 23 | 141.62 | 185.22 | -63.77 | -107.37 | -4.41 | 8.07 |
| dirección short | 33 | 544.33 | 266.72 | 132.88 | 410.50 | 17.41 | 15.07 |
| market_24h_inferred | 17 | 1306.23 | 139.07 | 23.36 | 1190.52 | 80.80 | 24.00 |
| stop_order | 27 | -4845.08 | 218.12 | 28.22 | -5034.99 | -207.87 | 6.55 |
| target_order | 12 | 4224.80 | 94.74 | 17.54 | 4147.59 | 392.67 | 9.75 |

### H2_POI, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 36 | -261.85 | 307.46 | -34.37 | -603.68 | -15.61 | 23.92 |
| dirección short | 33 | -349.45 | 277.75 | 22.49 | -604.71 | -19.25 | 19.43 |
| market_24h_inferred | 34 | 929.03 | 280.93 | -8.41 | 639.70 | 21.21 | 24.00 |
| stop_order | 26 | -5019.33 | 225.83 | -5.05 | -5250.20 | -209.19 | 6.54 |
| target_order | 9 | 3478.99 | 78.45 | 1.58 | 3402.12 | 391.14 | 8.18 |

### H3_P, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 254 | 534.06 | 1971.53 | -794.00 | -2231.48 | -8.20 | 12.30 |
| dirección short | 222 | -1176.71 | 1687.70 | 390.86 | -2473.54 | -14.10 | 8.26 |
| market_24h_inferred | 110 | 5639.03 | 786.52 | -201.02 | 4651.49 | 54.90 | 24.00 |
| stop_order | 257 | -44657.38 | 2008.97 | -182.28 | -46848.63 | -209.59 | 6.98 |
| target_order | 109 | 38375.70 | 863.75 | -19.83 | 37492.12 | 390.94 | 7.95 |

### H3_P, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 339 | 2570.96 | 2794.92 | -447.56 | -671.53 | -2.67 | 24.00 |
| dirección short | 333 | 765.45 | 2700.76 | 369.30 | -1566.01 | -2.47 | 24.00 |
| market_24h_inferred | 352 | 12053.29 | 2875.95 | -32.40 | 9144.94 | 28.98 | 24.00 |
| market_fold_end_inferred | 2 | 13.65 | 17.81 | -8.61 | -12.76 | -9.00 | 16.00 |
| stop_order | 227 | -41440.04 | 1864.73 | -42.12 | -43346.89 | -209.22 | 10.53 |
| target_order | 91 | 32709.52 | 737.21 | 4.86 | 31977.16 | 391.04 | 13.10 |

### H3_PF, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 8 | -402.29 | 66.21 | 10.07 | -458.43 | -59.27 | 17.28 |
| dirección short | 32 | -1361.22 | 244.03 | 133.96 | -1471.29 | -51.88 | 8.70 |
| market_24h_inferred | 8 | 196.12 | 57.75 | 57.88 | 196.25 | 31.77 | 24.00 |
| stop_order | 25 | -4388.25 | 198.60 | 60.93 | -4525.92 | -206.20 | 6.87 |
| target_order | 7 | 2428.62 | 53.89 | 25.22 | 2399.95 | 395.22 | 10.95 |

### H3_PF, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 13 | 132.57 | 111.76 | -5.47 | 15.34 | 1.16 | 24.00 |
| dirección short | 15 | -307.47 | 127.98 | 48.48 | -386.97 | -27.80 | 24.00 |
| market_24h_inferred | 18 | 566.88 | 154.49 | 40.75 | 453.13 | 26.99 | 24.00 |
| stop_order | 8 | -1510.13 | 67.95 | 0.35 | -1577.73 | -208.95 | 6.24 |
| target_order | 2 | 768.35 | 17.29 | 1.91 | 752.97 | 391.99 | 10.53 |

### H3_PFOI, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 7 | -486.60 | 57.96 | 8.56 | -536.00 | -82.82 | 15.78 |
| dirección short | 19 | -1239.32 | 141.09 | 98.89 | -1281.51 | -76.76 | 15.20 |
| market_24h_inferred | 7 | 49.13 | 51.47 | 52.45 | 50.11 | 9.88 | 24.00 |
| stop_order | 16 | -2773.59 | 125.23 | 49.93 | -2848.89 | -205.38 | 11.27 |
| target_order | 3 | 998.55 | 22.34 | 5.07 | 981.27 | 392.92 | 1.42 |

### H3_PFOI, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 6 | -101.27 | 51.96 | -2.12 | -155.34 | -26.43 | 23.36 |
| dirección short | 9 | -260.02 | 76.52 | 36.98 | -299.57 | -35.22 | 24.00 |
| market_24h_inferred | 10 | 13.66 | 85.59 | 34.81 | -37.13 | -3.04 | 24.00 |
| stop_order | 4 | -757.89 | 34.10 | 0.05 | -791.93 | -208.98 | 8.47 |
| target_order | 1 | 382.94 | 8.79 | 0.00 | 374.15 | 390.82 | 6.55 |

### H3_POI, 2020-2021
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 204 | -1178.93 | 1375.06 | -587.45 | -3141.44 | -18.54 | 12.26 |
| dirección short | 160 | -346.79 | 1018.54 | 243.55 | -1121.79 | -5.82 | 10.02 |
| market_24h_inferred | 84 | 2786.97 | 557.69 | -114.95 | 2114.33 | 36.47 | 24.00 |
| stop_order | 195 | -28661.24 | 1287.85 | -184.42 | -30133.51 | -210.08 | 7.93 |
| target_order | 85 | 24348.55 | 548.06 | -44.53 | 23755.95 | 390.45 | 8.02 |

### H3_POI, 2022-2023
| Grupo | N | Precio bruto | Fees | Funding | Neto | Media neta bps | Mediana horas |
|---|---:|---:|---:|---:|---:|---:|---:|
| dirección long | 255 | 3535.27 | 2136.84 | -307.91 | 1090.51 | 4.43 | 23.40 |
| dirección short | 222 | 1192.91 | 1846.51 | 243.99 | -409.60 | -1.62 | 24.00 |
| market_24h_inferred | 242 | 6433.17 | 1990.96 | -20.07 | 4422.14 | 19.52 | 24.00 |
| market_fold_end_inferred | 1 | 5.50 | 7.12 | 1.58 | -0.04 | -0.04 | 20.00 |
| stop_order | 159 | -29958.14 | 1347.35 | -38.46 | -31343.94 | -209.25 | 10.67 |
| target_order | 75 | 28247.66 | 637.93 | -6.98 | 27602.75 | 390.90 | 12.58 |

## Límites de interpretación
- Quitar fees o funding de trades ya ejecutados es una atribución contable con cantidades fijas, no un replay sin costos: el sizing y el capital habrían cambiado.
- La media de bps divide cada PnL por su notional de entrada, sin ponderar; no usar PNL_percentage del framework, que depende del margen/apalancamiento, como retorno del precio.
- No se midieron MFE/MAE, oportunidades omitidas ni trayectorias alternativas después de un cierre. Los snapshots de resultados no contienen las velas intratrade necesarias. No se concluye si una entrada acertaba a mayor horizonte ni cuál habría sido la salida óptima.
- Los grupos de salida son resultados de las mismas trayectorias; comparar su PnL no identifica efecto causal del método de salida.
- El nominal tiene slippage cero; funding con marcas proxy y OI retrospectivo sin certificación point-in-time. No acredita robustez de ejecución.
- Todo este análisis es posterior a ver V1. No ofrece validación independiente ni permite relajar gates originales.

## Cómo seguir
Recomendación: formular un ciclo V2 pequeño con **una sola pregunta controlada**: si adaptar la distancia de protección a la volatilidad mejora la estabilidad de H1 frente al esquema fijo 2%/4%. Mantener entradas, direcciones, límite de una entrada/día y holding 24h; conservar el control V1 inmutable. Comparar P y P+OI para cada esquema, cuatro configuraciones en total, sin filtro de funding económico pero con su contabilidad activa.
La motivación es que una distancia porcentual constante representa barreras distintas en unidades de volatilidad según régimen; V1 no prueba esa hipótesis. ATR, período, múltiplos, cálculo causal, sizing, gates, vecinos y presupuesto deben congelarse antes de ver el primer resultado. No elegir valores para rescatar V1 ni cambiar horizonte y régimen al mismo tiempo.
Si se conserva el esquema de cuatro folds train/evaluación, son 32 sesiones nominales de exploración para esas cuatro configuraciones, en un **ciclo nuevo**, no slots reasignados de V1. Reservar confirmación/estrés en el protocolo antes de ejecutar y detenerse si no pasa selección. 2022–2023 es desarrollo observado; 2024–2025 continúa reserva interna con contaminación previa de otras investigaciones; 2026 permanece cerrado.
Este informe no inicia V2 ni declara una candidata. El próximo entregable es un protocolo V2 completo y revisable.

## Procedencia reproducible
Jobs exitosos: f393c7189a584b06a1f435fa81ee70a6, c532bc3349a0468da52b532d306c64ce, 9fbc048976af4cf39a8a5d68c74ee90d, a69707c5d80b4840bb67d2c637151583, 194a25bf2dd6485cb60c26351cdd6a3f, d06b268ed65b4e6f89dac17224363e7b.
Un primer job 249666ccc1e44abf98f948124fb4cf72 falló al esperar dashboard_url dentro del snapshot; esa clave no existe allí. Se corrigió sólo el análisis, se repitió con los mismos inputs y las URLs se conservaron de los registros MCP previos. No se repitió ningún backtest.
Código completo: POSTMORTEM_V1_ANALYSIS_SOURCE_20261020.md.
Resultados completos, folds y manifiesto: POSTMORTEM_V1_DATA_20261020.json.

### Sesiones existentes analizadas
- [H1_P E1T](http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770): 2020-09-01 → 2022-01-01, 284 trades.
- [H1_PF E1T](http://localhost:9200/#/backtest/d3ea7127-8add-4952-8143-bf4c26f69958): 2020-09-01 → 2022-01-01, 277 trades.
- [H1_P E1V](http://localhost:9200/#/backtest/ed789043-2aa2-4714-8963-112eadbc56b8): 2022-01-01 → 2022-07-01, 93 trades.
- [H1_PF E1V](http://localhost:9200/#/backtest/7ea4be97-2bdc-4bfd-a7d3-401b39af2a40): 2022-01-01 → 2022-07-01, 91 trades.
- [H1_P E2V](http://localhost:9200/#/backtest/5ba6d867-c4ca-477a-bd8f-25353a8a9eb7): 2022-07-01 → 2023-01-01, 96 trades.
- [H1_PF E2V](http://localhost:9200/#/backtest/a5d0a2ec-2c93-438a-b8e1-c4904c9effc8): 2022-07-01 → 2023-01-01, 95 trades.
- [H1_P E3V](http://localhost:9200/#/backtest/853089c6-86ed-4e36-a30e-833b61c5b382): 2023-01-01 → 2023-07-01, 85 trades.
- [H1_PF E3V](http://localhost:9200/#/backtest/75a05170-6a21-461d-ae17-a87c8d7cca30): 2023-01-01 → 2023-07-01, 82 trades.
- [H1_P E4V](http://localhost:9200/#/backtest/c29d757d-c834-49ba-8145-fbe8c952cc4f): 2023-07-01 → 2024-01-01, 68 trades.
- [H1_PF E4V](http://localhost:9200/#/backtest/2556bc80-1e69-4196-ba55-d87646c46459): 2023-07-01 → 2024-01-01, 61 trades.
- [H1_POI E1T](http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644): 2020-09-01 → 2022-01-01, 212 trades.
- [H1_PFOI E1T](http://localhost:9200/#/backtest/279d4b93-7932-41a8-9b38-14077469675d): 2020-09-01 → 2022-01-01, 208 trades.
- [H1_POI E1V](http://localhost:9200/#/backtest/88e7e822-cb4d-49f7-97ab-ec5743786d29): 2022-01-01 → 2022-07-01, 59 trades.
- [H1_PFOI E1V](http://localhost:9200/#/backtest/d2c228a6-1cc3-4ca4-b452-424d137c2e2d): 2022-01-01 → 2022-07-01, 58 trades.
- [H1_POI E2V](http://localhost:9200/#/backtest/2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f): 2022-07-01 → 2023-01-01, 64 trades.
- [H1_PFOI E2V](http://localhost:9200/#/backtest/90be152d-6530-4e40-9bac-8067ccd169db): 2022-07-01 → 2023-01-01, 63 trades.
- [H1_POI E3V](http://localhost:9200/#/backtest/22f19971-2e43-4987-b915-8a8504dea4f0): 2023-01-01 → 2023-07-01, 56 trades.
- [H1_PFOI E3V](http://localhost:9200/#/backtest/0910f976-03e3-4d8f-a9f3-1f654b41f853): 2023-01-01 → 2023-07-01, 54 trades.
- [H1_POI E4V](http://localhost:9200/#/backtest/706268de-8c74-401c-a17a-8bb9d55d6767): 2023-07-01 → 2024-01-01, 49 trades.
- [H1_PFOI E4V](http://localhost:9200/#/backtest/e62bb0ab-f354-41f0-819c-644f24c2336d): 2023-07-01 → 2024-01-01, 44 trades.
- [H2_P E1T](http://localhost:9200/#/backtest/232577e2-4517-4257-a069-53217d2c6da8): 2020-09-01 → 2022-01-01, 104 trades.
- [H2_PF E1T](http://localhost:9200/#/backtest/969b42d2-0136-488e-915c-0065bc61f839): 2020-09-01 → 2022-01-01, 6 trades.
- [H2_P E1V](http://localhost:9200/#/backtest/801e04d7-eb9b-4d92-bc49-7fc2db1fe5cb): 2022-01-01 → 2022-07-01, 38 trades.
- [H2_PF E1V](http://localhost:9200/#/backtest/372dea0d-af5b-4c45-a712-7b199e4f35fd): 2022-01-01 → 2022-07-01, 2 trades.
- [H2_P E2V](http://localhost:9200/#/backtest/5a46a1f1-df6e-41ba-a8de-495e07a1421a): 2022-07-01 → 2023-01-01, 37 trades.
- [H2_PF E2V](http://localhost:9200/#/backtest/cce04e8d-ad70-4052-86c4-517d366d6edd): 2022-07-01 → 2023-01-01, 0 trades.
- [H2_P E3V](http://localhost:9200/#/backtest/201fc419-1e0c-4245-baa2-79a5bf7df80a): 2023-01-01 → 2023-07-01, 30 trades.
- [H2_PF E3V](http://localhost:9200/#/backtest/9e719e69-81e6-43b5-b814-5bc0d02e1ee2): 2023-01-01 → 2023-07-01, 0 trades.
- [H2_P E4V](http://localhost:9200/#/backtest/c14e42b9-192b-4e9a-933e-24b7dbb29ec9): 2023-07-01 → 2024-01-01, 19 trades.
- [H2_PF E4V](http://localhost:9200/#/backtest/79b80520-9207-4878-826c-9f87c888f1f7): 2023-07-01 → 2024-01-01, 0 trades.
- [H2_POI E1T](http://localhost:9200/#/backtest/e7506dac-942f-4cf0-bae7-8608d184490f): 2020-09-01 → 2022-01-01, 56 trades.
- [H2_PFOI E1T](http://localhost:9200/#/backtest/91ad7aa1-3553-44d3-ad00-64777281ce3b): 2020-09-01 → 2022-01-01, 4 trades.
- [H2_POI E1V](http://localhost:9200/#/backtest/6ed903fb-abca-4f00-aadb-a841e8f2d45e): 2022-01-01 → 2022-07-01, 18 trades.
- [H2_PFOI E1V](http://localhost:9200/#/backtest/76d2e287-1535-4574-ab52-90622ab3b3de): 2022-01-01 → 2022-07-01, 0 trades.
- [H2_POI E2V](http://localhost:9200/#/backtest/bb3ade90-a481-4f9e-beeb-4f715d9a32e4): 2022-07-01 → 2023-01-01, 25 trades.
- [H2_PFOI E2V](http://localhost:9200/#/backtest/21c23ca0-a816-4416-b0bc-c5b67c0f6772): 2022-07-01 → 2023-01-01, 0 trades.
- [H2_POI E3V](http://localhost:9200/#/backtest/ba6a2f8a-6bff-4c29-b4d4-83fe3808b578): 2023-01-01 → 2023-07-01, 12 trades.
- [H2_PFOI E3V](http://localhost:9200/#/backtest/6b6cbe4e-c30e-4c77-a34f-d93dc6cfe833): 2023-01-01 → 2023-07-01, 0 trades.
- [H2_POI E4V](http://localhost:9200/#/backtest/75618e87-4f6a-4249-b69d-dfbc124ac12f): 2023-07-01 → 2024-01-01, 14 trades.
- [H2_PFOI E4V](http://localhost:9200/#/backtest/045b1386-b9e6-4862-bc80-1b8c98d8a95c): 2023-07-01 → 2024-01-01, 0 trades.
- [H3_P E1T](http://localhost:9200/#/backtest/db1f164b-17e3-4dac-8580-bbcdcf6815e9): 2020-09-01 → 2022-01-01, 476 trades.
- [H3_PF E1T](http://localhost:9200/#/backtest/8b0c6493-efad-40e5-bb12-97a89a821bbb): 2020-09-01 → 2022-01-01, 40 trades.
- [H3_P E1V](http://localhost:9200/#/backtest/5a8a5b98-c60d-46c7-98a1-b256e8575cbf): 2022-01-01 → 2022-07-01, 176 trades.
- [H3_PF E1V](http://localhost:9200/#/backtest/d79395ab-ab58-4bcc-b4b8-88a363e78bb0): 2022-01-01 → 2022-07-01, 5 trades.
- [H3_P E2V](http://localhost:9200/#/backtest/0a64060d-6f97-4f56-bdd0-323aace59405): 2022-07-01 → 2023-01-01, 170 trades.
- [H3_PF E2V](http://localhost:9200/#/backtest/ebc60c54-a190-465a-9584-5702df136796): 2022-07-01 → 2023-01-01, 6 trades.
- [H3_P E3V](http://localhost:9200/#/backtest/8bf944d4-de4b-450a-ba9d-2aee9399d84e): 2023-01-01 → 2023-07-01, 168 trades.
- [H3_PF E3V](http://localhost:9200/#/backtest/c7abf3e9-0f5f-4c07-b4b4-20249105fcd6): 2023-01-01 → 2023-07-01, 6 trades.
- [H3_P E4V](http://localhost:9200/#/backtest/bed27bc9-4f98-40c4-b848-261a5f55e541): 2023-07-01 → 2024-01-01, 158 trades.
- [H3_PF E4V](http://localhost:9200/#/backtest/dd024a64-431d-4c23-835d-39b311415509): 2023-07-01 → 2024-01-01, 11 trades.
- [H3_POI E1T](http://localhost:9200/#/backtest/fdb13394-9dd1-40bf-b0f4-e5136d6c8115): 2020-09-01 → 2022-01-01, 364 trades.
- [H3_PFOI E1T](http://localhost:9200/#/backtest/18c9272f-edd7-481e-8d8b-2a056e136adc): 2020-09-01 → 2022-01-01, 26 trades.
- [H3_POI E1V](http://localhost:9200/#/backtest/6d688cbc-1adf-4452-a3c9-99a111221146): 2022-01-01 → 2022-07-01, 125 trades.
- [H3_PFOI E1V](http://localhost:9200/#/backtest/f21f62e6-8b5e-40c0-a108-e564ccfc8562): 2022-01-01 → 2022-07-01, 2 trades.
- [H3_POI E2V](http://localhost:9200/#/backtest/241076dd-c905-4237-a1aa-3ddf2a405fa8): 2022-07-01 → 2023-01-01, 125 trades.
- [H3_PFOI E2V](http://localhost:9200/#/backtest/2ee58971-a2f6-4249-9e8a-454006769816): 2022-07-01 → 2023-01-01, 4 trades.
- [H3_POI E3V](http://localhost:9200/#/backtest/fec06767-c58f-4c48-889d-96fb2840bad4): 2023-01-01 → 2023-07-01, 117 trades.
- [H3_PFOI E3V](http://localhost:9200/#/backtest/c6f6d185-d860-49b3-ab78-0fdd630f5dd3): 2023-01-01 → 2023-07-01, 2 trades.
- [H3_POI E4V](http://localhost:9200/#/backtest/1a8bdcf1-bddb-4baa-93a8-113e2213f258): 2023-07-01 → 2024-01-01, 110 trades.
- [H3_PFOI E4V](http://localhost:9200/#/backtest/be11950c-23b5-4fea-8b63-44db06b49ddc): 2023-07-01 → 2024-01-01, 7 trades.
