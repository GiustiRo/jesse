# Exploración walk-forward V2 — cierre SIN_CANDIDATA
Fecha: 2026-10-20. Cuatro configuraciones, cuatro folds train/eval. Se completaron32slots nominales:16controles V1 reutilizados y16sesiones ATR nuevas, sin duplicados. Cuatro smokes técnicos anteriores separados. No se agregaron familias ni parámetros durante resultados.

## Selección registrada
Gates de train: >=30trades, neto>0, PF>=1,2, absDD<=25%. Las cuatro decisiones son SIN_CANDIDATA; no finalista.
| Fold | Decisión UTC | Primera solicitud eval ATR UTC | Selección |
|---|---|---|---|
| E1 | 2026-10-20T22:33:49.399Z | 2026-10-20T22:43:33.314Z | SIN_CANDIDATA |
| E2 | 2026-10-20T22:46:29.365Z | 2026-10-20T22:46:45.744Z | SIN_CANDIDATA |
| E3 | 2026-10-20T22:49:52.950Z | 2026-10-20T22:50:10.883Z | SIN_CANDIDATA |
| E4 | 2026-10-20T22:53:33.944Z | 2026-10-20T22:53:49.116Z | SIN_CANDIDATA |
La auditoría independiente releyó las cuatro selecciones y los ocho timestamps de evaluación en V2_AUDIT_CHRONOLOGY.json. Entrenamientos del siguiente fold se prepararon en paralelo según addendum, pero ninguna evaluación se adelantó a su decisión. Controles de evaluación ya eran conocidos de V1.

## Evaluaciones 2022–2023
| Configuración | E1 ene–jun2022 % | E2 jul–dic2022 % | E3 ene–jun2023 % | E4 jul–dic2023 % | N únicos | PF agregado | Semestres positivos |
|---|---:|---:|---:|---:|---:|---:|---:|
| H1_FIXED_P | -10.94 | -10.94 | 20.32 | -5.99 | 342 | 0.975 | 1/4 |
| H1_ATR_P | -4.29 | 2.50 | 18.47 | 3.36 | 332 | 1.093 | 3/4 |
| H1_FIXED_POI | 8.92 | -5.52 | 11.94 | -6.62 | 228 | 1.042 | 2/4 |
| H1_ATR_POI | 10.81 | 3.08 | 7.96 | 2.88 | 223 | 1.172 | 4/4 |

## Precio, costos y concentración
Cada fold reinicia10000. Las sumas de USDT son agregación nominal de esas sesiones independientes; no son rentabilidad de una cuenta continua, una cartera que opere variantes juntas ni retorno anual.
| Configuración | Bruto | Fees | Funding | Suma nominal neta USDT | Suma sin mejor semestre | Mejor trade / neto nominal |
|---|---:|---:|---:|---:|---:|---:|
| H1_FIXED_P | 2117.71 | 2827.39 | -45.16 | -754.85 | -2787.33 | — |
| H1_ATR_P | 4154.30 | 2100.93 | -48.54 | 2004.83 | 157.45 | 23.52% |
| H1_FIXED_POI | 2910.49 | 1990.86 | -47.17 | 872.46 | -321.63 | 48.85% |
| H1_ATR_POI | 3978.74 | 1460.23 | -44.14 | 2474.37 | 1392.89 | 16.67% |

ATR reduce DD y turnover frente al fijo correspondiente en4/4folds para ambos usos de OI. Mejora retorno neto en3/4, sacrificando parte de la ganancia del primer semestre2023. No es efecto puro del stop: cambian escala protectora, sizing, ocupación y entradas posteriores.
ATR_POI presenta4/4semestres positivos, PF1,17171 y223trades; conserva suma nominal positiva al quitar mejor semestre. Aun así, no fue seleccionada en train. Sus PF de E2T/E3T/E4T fueron1,05895/1,06272/1,08668, y el DD histórico alcanzó−30,64639%. E1T tuvo PF0,99860, neto−0,19945% y DD−29,08373%. No se permite relajar gates ni empezar confirmación por buenos resultados posteriores.
ATR_P tuvo3/4positivos y PF1,09289; al quitar su mejor semestre queda+157,45USDT nominales, pequeño frente a su total+2004,83. Menor concentración que V1 no equivale a robustez confirmada.

## Dirección
| Configuración | Long N / neto USDT | Short N / neto USDT |
|---|---|---|
| H1_FIXED_P | 176 / -1094.61 | 166 / 339.76 |
| H1_ATR_P | 169 / 2131.36 | 163 / -126.53 |
| H1_FIXED_POI | 130 / -356.12 | 98 / 1228.58 |
| H1_ATR_POI | 126 / 1609.18 | 97 / 865.19 |
ATR_POI obtuvo suma nominal positiva enambasdirecciones; no eliminar shorts retrospectivamente en variantes donde fueron negativos. OI mejora PF agregado respecto a ATR_P y reduce DD en cada fold, pero su aporte no es una prueba causal aislada ni validación independiente.

## Meses
| Configuración | Negativos /24 | Mediana mes % | Peor mes % | Máxima racha meses negativos |
|---|---:|---:|---:|---:|
| H1_FIXED_P | 12/24 | 0.18 | -18.50 | 3 |
| H1_ATR_P | 11/24 | 1.16 | -10.17 | 3 |
| H1_FIXED_POI | 12/24 | -0.26 | -5.78 | 3 |
| H1_ATR_POI | 11/24 | 1.34 | -5.89 | 3 |
Cuatro semestres positivos en ATR_POI convivieron con11meses negativos y racha de3. Su peor mes fue−5,89%, ligeramente peor que−5,78% del control fijo OI; no todas las métricas mejoran.

| Mes | FIXED_P % | ATR_P % | FIXED_POI % | ATR_POI % | Selector % |
|---|---:|---:|---:|---:|---:|
| 2022-01 | -18.06 | -8.83 | -5.10 | -2.20 | 0,00 |
| 2022-02 | 1.07 | -1.60 | 6.74 | 6.37 | 0,00 |
| 2022-03 | 6.06 | 6.66 | 9.06 | 8.32 | 0,00 |
| 2022-04 | -6.06 | -9.33 | -4.02 | -4.75 | 0,00 |
| 2022-05 | 3.60 | 4.64 | 2.30 | 1.94 | 0,00 |
| 2022-06 | 4.18 | 5.43 | 0.40 | 1.27 | 0,00 |
| 2022-07 | 1.71 | 8.96 | -0.92 | 6.49 | 0,00 |
| 2022-08 | -18.50 | -10.17 | -5.57 | -1.57 | 0,00 |
| 2022-09 | -8.82 | -4.26 | -4.20 | -3.72 | 0,00 |
| 2022-10 | 4.93 | 3.91 | 7.09 | 6.02 | 0,00 |
| 2022-11 | 17.32 | 9.53 | 2.75 | -0.40 | 0,00 |
| 2022-12 | -4.28 | -3.91 | -4.20 | -3.26 | 0,00 |
| 2023-01 | 9.45 | 11.51 | 4.87 | 8.07 | 0,00 |
| 2023-02 | 3.94 | 3.02 | 6.26 | 1.42 | 0,00 |
| 2023-03 | 11.68 | 10.38 | 2.25 | 2.18 | 0,00 |
| 2023-04 | -4.72 | -2.47 | -3.78 | -2.11 | 0,00 |
| 2023-05 | -7.78 | -6.36 | -3.34 | -3.00 | 0,00 |
| 2023-06 | 7.77 | 2.31 | 5.64 | 1.54 | 0,00 |
| 2023-07 | -11.08 | -8.73 | -5.48 | -5.89 | 0,00 |
| 2023-08 | -1.62 | -0.11 | -2.24 | -0.79 | 0,00 |
| 2023-09 | -2.47 | -0.05 | -3.92 | -1.84 | 0,00 |
| 2023-10 | 13.95 | 10.85 | 8.02 | 6.63 | 0,00 |
| 2023-11 | -0.70 | 1.05 | 3.34 | 3.62 | 0,00 |
| 2023-12 | -2.61 | 1.27 | -5.78 | 1.60 | 0,00 |

## Selector real del protocolo
Las cuatro decisiones fueron planas: cero trades seleccionados, índice convencional10000constante durante24meses, retorno0%, DD0 por ausencia de exposición, PF indefinido. No intereses sobre efectivo.
No confundir este selector con el resultado retrospectivo de ATR_POI. El índice reescalado/las sesiones reseteadas no son un replay continuo de capital y posiciones. La meta orientativa20–30% anual no quedó validada.

## Sesiones y duración
Cada enlace es dashboard_url real retornada porMCP. Train empieza2020-09-01; eval corresponde al semestre siguiente. No sumar trades train repetidos.
| Etapa | Configuración | Ventana | N | Neto % | PF | DD % | Motor s |
|---|---|---|---:|---:|---:|---:|---:|
| E1T | [H1_ATR_P](http://localhost:9200/#/backtest/5d77182b-2071-4056-a11f-4f7c5d5ef12f) | 2020-09-01→2022-01-01 | 263 | -12.69 | 0.928 | -31.19 | 12.13 |
| E1T | [H1_ATR_POI](http://localhost:9200/#/backtest/8e030d85-6762-42d7-91ef-546ca2a6b340) | 2020-09-01→2022-01-01 | 198 | -0.20 | 0.999 | -29.08 | 11.39 |
| E1T | [H1_FIXED_P](http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770) | 2020-09-01→2022-01-01 | 284 | -28.63 | 0.907 | -42.72 | 10.69 |
| E1T | [H1_FIXED_POI](http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644) | 2020-09-01→2022-01-01 | 212 | -6.83 | 0.973 | -33.94 | 10.35 |
| E1V | [H1_ATR_P](http://localhost:9200/#/backtest/456e2c59-3c00-4404-8999-c57ab3b2efb0) | 2022-01-01→2022-07-01 | 90 | -4.29 | 0.928 | -16.10 | 9.38 |
| E1V | [H1_ATR_POI](http://localhost:9200/#/backtest/a10275b7-6074-435a-980f-c76f9beb3d66) | 2022-01-01→2022-07-01 | 58 | 10.81 | 1.293 | -8.17 | 5.38 |
| E1V | [H1_FIXED_P](http://localhost:9200/#/backtest/ed789043-2aa2-4714-8963-112eadbc56b8) | 2022-01-01→2022-07-01 | 93 | -10.94 | 0.884 | -20.77 | 4.51 |
| E1V | [H1_FIXED_POI](http://localhost:9200/#/backtest/88e7e822-cb4d-49f7-97ab-ec5743786d29) | 2022-01-01→2022-07-01 | 59 | 8.92 | 1.142 | -8.44 | 4.22 |
| E2T | [H1_ATR_P](http://localhost:9200/#/backtest/0062cce6-a9bb-4f00-8fd4-3ad5967edc70) | 2020-09-01→2022-07-01 | 353 | -16.43 | 0.928 | -40.39 | 19.8 |
| E2T | [H1_ATR_POI](http://localhost:9200/#/backtest/6686347f-bf6e-4d7c-b2b5-202321321786) | 2020-09-01→2022-07-01 | 256 | 10.59 | 1.059 | -30.65 | 19.03 |
| E2T | [H1_FIXED_P](http://localhost:9200/#/backtest/8042b1d6-268a-4c60-9545-1147b44f9851) | 2020-09-01→2022-07-01 | 377 | -36.44 | 0.903 | -53.73 | 14.36 |
| E2T | [H1_FIXED_POI](http://localhost:9200/#/backtest/aa5a6fd5-08c4-4ce8-9d2e-c9ada34fbe9b) | 2020-09-01→2022-07-01 | 271 | 1.48 | 1.005 | -36.56 | 13.62 |
| E2V | [H1_ATR_P](http://localhost:9200/#/backtest/3a3bef6f-0aa5-4ceb-9cf1-5ff0f0150c3e) | 2022-07-01→2023-01-01 | 90 | 2.50 | 1.044 | -15.74 | 6.02 |
| E2V | [H1_ATR_POI](http://localhost:9200/#/backtest/9b2fac46-e31c-46a2-96b9-36f52b214589) | 2022-07-01→2023-01-01 | 60 | 3.08 | 1.078 | -7.46 | 6.81 |
| E2V | [H1_FIXED_P](http://localhost:9200/#/backtest/5ba6d867-c4ca-477a-bd8f-25353a8a9eb7) | 2022-07-01→2023-01-01 | 96 | -10.94 | 0.865 | -29.11 | 4.82 |
| E2V | [H1_FIXED_POI](http://localhost:9200/#/backtest/2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f) | 2022-07-01→2023-01-01 | 64 | -5.52 | 0.904 | -14.33 | 3.7 |
| E3T | [H1_ATR_P](http://localhost:9200/#/backtest/2f62f8ef-ba51-4308-a10e-8a4514327709) | 2020-09-01→2023-01-01 | 443 | -14.96 | 0.946 | -40.39 | 25.29 |
| E3T | [H1_ATR_POI](http://localhost:9200/#/backtest/a0f71b9c-3de8-40d7-a714-7bdfa7492c4c) | 2020-09-01→2023-01-01 | 316 | 14.01 | 1.063 | -30.65 | 22.12 |
| E3T | [H1_FIXED_P](http://localhost:9200/#/backtest/1f11e4be-bb91-4445-b6df-662f909ed76d) | 2020-09-01→2023-01-01 | 473 | -43.40 | 0.898 | -61.60 | 15.51 |
| E3T | [H1_FIXED_POI](http://localhost:9200/#/backtest/d546fc9f-90bf-45d4-85b7-fa6d29d4736f) | 2020-09-01→2023-01-01 | 335 | -4.12 | 0.989 | -36.56 | 13.73 |
| E3V | [H1_ATR_P](http://localhost:9200/#/backtest/91147a26-0231-4731-86ac-31e3eea4f1ac) | 2023-01-01→2023-07-01 | 83 | 18.47 | 1.324 | -14.39 | 5.92 |
| E3V | [H1_ATR_POI](http://localhost:9200/#/backtest/15edc301-842b-4376-9313-7a75e0ae1102) | 2023-01-01→2023-07-01 | 55 | 7.96 | 1.211 | -10.94 | 4.86 |
| E3V | [H1_FIXED_P](http://localhost:9200/#/backtest/853089c6-86ed-4e36-a30e-833b61c5b382) | 2023-01-01→2023-07-01 | 85 | 20.32 | 1.253 | -17.38 | 3.99 |
| E3V | [H1_FIXED_POI](http://localhost:9200/#/backtest/22f19971-2e43-4987-b915-8a8504dea4f0) | 2023-01-01→2023-07-01 | 56 | 11.94 | 1.242 | -12.37 | 3.54 |
| E4T | [H1_ATR_P](http://localhost:9200/#/backtest/670b303c-b0c7-448d-ad7a-f5f7e20cd5a8) | 2020-09-01→2023-07-01 | 526 | 0.75 | 1.002 | -40.39 | 30.75 |
| E4T | [H1_ATR_POI](http://localhost:9200/#/backtest/dbc341d3-0542-4500-99b7-c4fce333f7cf) | 2020-09-01→2023-07-01 | 371 | 23.08 | 1.087 | -30.65 | 26.6 |
| E4T | [H1_FIXED_P](http://localhost:9200/#/backtest/32a12c2b-8c77-46b8-92b6-a905f6577c3d) | 2020-09-01→2023-07-01 | 558 | -31.89 | 0.932 | -61.60 | 17.3 |
| E4T | [H1_FIXED_POI](http://localhost:9200/#/backtest/34995866-f432-45ce-9611-93ae23b9b91c) | 2020-09-01→2023-07-01 | 391 | 7.33 | 1.018 | -36.56 | 21.17 |
| E4V | [H1_ATR_P](http://localhost:9200/#/backtest/898996f7-f78c-4bf9-8058-de8b823dfadb) | 2023-07-01→2024-01-01 | 69 | 3.36 | 1.080 | -11.07 | 5.77 |
| E4V | [H1_ATR_POI](http://localhost:9200/#/backtest/707881ef-fc9b-42d4-aec7-7932f74413b9) | 2023-07-01→2024-01-01 | 50 | 2.88 | 1.096 | -9.59 | 4.86 |
| E4V | [H1_FIXED_P](http://localhost:9200/#/backtest/c29d757d-c834-49ba-8145-fbe8c952cc4f) | 2023-07-01→2024-01-01 | 68 | -5.99 | 0.884 | -15.84 | 3.77 |
| E4V | [H1_FIXED_POI](http://localhost:9200/#/backtest/706268de-8c74-401c-a17a-8bb9d55d6767) | 2023-07-01→2024-01-01 | 49 | -6.62 | 0.818 | -11.39 | 3.43 |
Suma motor16sesiones nuevas216,11segundos; no equivale a tiempo de pared de preparación/MCP/auditoría.

## Verificación y operación paralela
Tres subagentes dedicados: sector ATR_P, sector ATR_POI y auditoría independiente. Hasta2backtests porsector inicialmente (cuatroglobales); porerrores de respuesta se redujo a1porsector, dosglobales. Se mantuvo selecciónprevia porfold.
Hubo HTTPtimeouts de10s hacia API127.0.0.1:9000 y unHTTP502 delMCP al guardar un reporte. Los motores se comprobaron por los mismos IDs; todaslas16sesiones finalizaron sinerror del motor, sinreruns ni duplicados. Las primeras respuestas error deE1V no se conservaron completas por los clientes de rama; se declara esa limitación. Las siguientes se guardaron íntegras. El reporte cuyo guardado falló se leyó como inexistente antes de reintentar cuandoMCPrespondió. No diagnóstico fueraMCP ni reinicio.
ListadosMCP confirman16sesionesWFV2 y cero backtests activos. Branch progress y registry preservan incidentes, timestamps,fuentes,hashes,config y respuestas crudas.
Conciliación de las32sesiones nominales: bruto−fees+funding=PNL y saldo final; error máximo5.093170e-11USDT. 16auditorías ATR concilian barras,entradas/cierres y motivos; algunos cierres forzados suceden después del resumen, registrados aparte. Indicadores total_open_trades/open_pl previos al cierre no prueban posiciones residuales.
Fuentes congeladas no se modificaron. No se ejecutaron nuevos tests de framework porque no se cambió framework; smokes y55assertions técnicas previas permanecen la evidencia técnica documentada.

## Límites y fases cerradas
Shortlistvacía porregla de selecciónalmenosunavez. Confirmación8slots yrobustez24slots NOEJECUTADAS; no reasignar a tuning. Consumo32/64slots nominales (16nuevos+16reutilizados), más4smokes anteriores.
Slippage nominal0; marcasfundingproxy yOIretrospectivo sincertificaciónPIT. No se demostró supervivencia a feesduplicadas/slippage/vecinos/retraso/proxy; los smokes de fricción prueban soporte técnico, no resultados económicos.
2020–2023 es desarrollo observado; reserva2024–2025 no se abrió enV2 y tiene exposición previa de otrasinvestigaciones. 2026permanececerrado. SinML,RST,live/paper,órdenes,Pi,cambiosglobales,instalaciones,reinicio,commit/push.
Una eventualV3 necesita hipótesis y presupuesto distintos fijados antes de resultados. No convertir la variante positiva posterior en candidata alterando las reglas originales.

## Evidencia duradera
RESEARCH_PROTOCOL_V2_20261020.md; RESEARCH_V2_IMPLEMENTATION.md; RESEARCH_V2_IMPLEMENTATION_VERIFIED.md; REGISTRY_V2.json; cuatro WALK_FORWARD_E*_SELECTION_V2.md; ocho WALK_FORWARD_*_RESULTS_V2.md; V2_AUDIT_<stage>.json; 16AUDIT_ResearchV2*.json; V2_FINAL_COMPARISON.json; V2_INDEPENDENT_AUDIT_20261020.md; V2_AUDIT_CHRONOLOGY.json; progresos de rama; FROZEN_SHORTLIST_V2.md; WALK_FORWARD_CONFIRMATION_AND_STRESS_V2.md; FINAL_DECISION_V2.md.
