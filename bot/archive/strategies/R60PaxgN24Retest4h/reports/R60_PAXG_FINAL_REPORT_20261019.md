# R60 PAXG: sensibilidad local de retest frente a MARKET

Se completaron exactamente diez backtests nuevos, cinco pares predeclarados, sin modificar las fuentes después de observar resultados. MARKET supera el neto de retest en los cinco contextos y conserva esa diferencia tras recargos estáticos de 5 y 10 bps por ida y vuelta. Es evidencia local favorable a la política de entrada MARKET; no justifica elegir un vecino ganador ni promover una estrategia.

Ventana reutilizada: 2020-10-15 a 2025-12-31 exclusiva. Capital inicial 10000 USDT, riesgo planificado 1%, fee 0.00045 por lado en todas las órdenes, aislado 5x, cap 4.4, reserva 0.001 sólo para sizing, ruta PAXG 4h y datos propios M1, warmup 240, modo completo. Se conserva toda la gestión original: stop 2 ATR, BE 2.25R, trailing 4.2 ATR y tightening original. Sin funding, BTC ni consultas de 2026.

## Todas las ejecuciones y las dos referencias existentes

Neto y fees en USDT. CAGR, DD y Sharpe son métricas almacenadas del motor; DD negativo. Tiempo es porcentaje de ventana con posición. Las referencias centrales no se volvieron a ejecutar.

| Contexto / política | N | Neto | Fees | PF | DD motor % | CAGR % | Sharpe | Tiempo % | Dashboard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Cq | 35 | 546.11 | 246.61 | 1.31 | -6.92 | 1.03 | 0.23 | 13.36 | [AttrPaxgCqFreshRetest4h](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) |
| M | 38 | 962.13 | 267.72 | 1.57 | -7.65 | 1.78 | 0.38 | 15.20 | [AttrPaxgMMarketSignal4h](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) |
| P1_Cq | 36 | 960.04 | 260.41 | 1.54 | -6.92 | 1.77 | 0.37 | 13.79 | [R60PaxgN24Retest4h](http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26) |
| P1_M | 39 | 1385.70 | 282.41 | 1.82 | -7.65 | 2.52 | 0.50 | 15.64 | [R60PaxgN24Market4h](http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb) |
| P2_Cq | 35 | 262.21 | 241.35 | 1.14 | -9.11 | 0.50 | 0.13 | 12.24 | [R60PaxgN28Retest4h](http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936) |
| P2_M | 38 | 671.53 | 262.68 | 1.39 | -10.07 | 1.25 | 0.28 | 14.07 | [R60PaxgN28Market4h](http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a) |
| P3_Cq | 41 | 324.50 | 286.29 | 1.16 | -8.30 | 0.61 | 0.14 | 15.44 | [R60PaxgAdx24Retest4h](http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248) |
| P3_M | 46 | 467.98 | 317.66 | 1.21 | -10.38 | 0.88 | 0.19 | 17.15 | [R60PaxgAdx24Market4h](http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c) |
| P4_Cq | 32 | 127.95 | 216.16 | 1.07 | -9.16 | 0.24 | 0.08 | 10.78 | [R60PaxgAdx28Retest4h](http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd) |
| P4_M | 35 | 469.42 | 235.97 | 1.27 | -10.02 | 0.88 | 0.21 | 12.13 | [R60PaxgAdx28Market4h](http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504) |
| P5_Cq | 35 | 532.93 | 246.48 | 1.30 | -7.05 | 1.00 | 0.23 | 13.35 | [R60PaxgFast24Retest4h](http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e) |
| P5_M | 38 | 948.34 | 267.56 | 1.57 | -7.76 | 1.75 | 0.37 | 15.20 | [R60PaxgFast24Market4h](http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14) |

P1 = Donchian 24; P2 = Donchian 28; P3 = ADX mínimo 24; P4 = ADX mínimo 28; P5 = EMA rápida 24. Centro = Donchian 26, ADX mínimo 26 y EMA rápida 20. Cada clase nueva cambia únicamente su nombre, comentario explicativo y ese default de hyperparameters(). Cq exige M1 fresco sólo al entrar. M conserva primero la elegibilidad del retest y luego coloca MARKET al cierre. Las salidas y el resto del motor permanecen iguales.

## Cinco contrastes completos

Las diferencias son MARKET menos retest. Los recargos estáticos usan todos los fills: 5 bps RT equivale a 2.5 bps adicionales por lado; 10 RT a 5 por lado. Son contabilidad sobre los fills observados, sin recalcular sizing, órdenes ni decisiones.

| Contexto | Δ neto | Δ con +5 bps RT | Δ con +10 bps RT | Δ tiempo, puntos % | Δ DD motor, puntos % |
|---|---:|---:|---:|---:|---:|
| Center | 416.02 | 404.29 | 392.56 | 1.85 | -0.73 |
| P1 | 425.66 | 413.44 | 401.22 | 1.85 | -0.73 |
| P2 | 409.32 | 397.48 | 385.63 | 1.83 | -0.96 |
| P3 | 143.48 | 126.05 | 108.62 | 1.71 | -2.08 |
| P4 | 341.47 | 330.46 | 319.46 | 1.35 | -0.86 |
| P5 | 415.41 | 403.70 | 391.99 | 1.85 | -0.71 |

Los cinco contextos nuevos producen diez caminos económicos distintos; con los centros son doce. Coinciden doce hashes distintos de fills económicos sin IDs y doce hashes distintos de curvas almacenadas. Esto descarta duplicación exacta de caminos en esta tanda, pero las ventanas, activos y buena parte de las operaciones se comparten: no son confirmaciones estadísticas independientes.

MARKET aumenta el tiempo en mercado entre 1.35 y 1.85 puntos porcentuales y empeora el DD del motor entre 0.71 y 2.08 puntos. El beneficio por notional de entrada también sube en todos los pares, entre 3.06 y 13.26 bps. La aproximación capital-tiempo a precio de entrada está en la tabla exacta; no representa exposición MTM.

## Fricción, concentración y temporalidad

| Contexto | Retest +10 bps RT | MARKET +10 bps RT | Retest sin mejor trade | MARKET sin mejor trade | Retest sin tres mejores | MARKET sin tres mejores |
|---|---:|---:|---:|---:|---:|---:|
| Center | 272.10 | 664.66 | -91.39 | 337.45 | -920.55 | -635.13 |
| P1 | 670.69 | 1071.91 | 322.54 | 761.03 | -717.87 | -266.74 |
| P2 | -5.96 | 379.67 | -358.26 | 63.24 | -1165.23 | -883.84 |
| P3 | 6.40 | 115.03 | -305.71 | -136.98 | -1125.40 | -1078.88 |
| P4 | -112.22 | 207.24 | -471.84 | -134.57 | -1188.45 | -999.56 |
| P5 | 259.06 | 651.05 | -103.76 | 324.46 | -931.89 | -646.90 |

Las cinco MARKET mantienen neto positivo con +10 bps RT, PF entre 1.21 y 1.82 y N entre 35 y 46. En retest, Donchian 28 y ADX 28 pasan a neto negativo con ese recargo; Donchian 28, ADX 24 y ADX 28 no alcanzan PF 1.2 antes del recargo. Todos los N nuevos superan 30; eso no elimina dependencia temporal ni selección.

Las diez recetas nuevas quedan negativas al excluir descriptivamente sus tres mejores ganancias netas. MARKET ADX 24 y ADX 28 tampoco conservan neto positivo sin su mejor trade. Quitar ganadores no es una regla operativa ni implica que una estrategia tendencial deba sobrevivir sin sus runners, pero hace visible la concentración.

En los cinco pares, la diferencia de neto por cohortes del año de CIERRE es negativa en 2021, 2022 y 2023, y positiva en 2024 y 2025. El agregado 2023–2025 favorece MARKET, pero oculta el deterioro de 2023. Estas cohortes no son rendimientos anuales MTM: una operación se atribuye al año en que cerró. No hubo cierres sintéticos terminales ni posiciones residuales; el mayor holding fue de unas 917.5 horas. La primera entrada fue 2020-12-27: el efectivo previo desde el inicio se conserva en las métricas y no se elimina para mejorar ratios.

## Qué explica y qué no explica el contraste

Las intersecciones inequívocas de órdenes de entrada ejecutadas con exactamente el mismo created_at, símbolo y dirección contienen 25/26/29/23/24 orígenes comunes para P1–P5. MARKET entra entre 13.35 y 15.61 bps más caro en promedio y adelanta el fill entre 0.49 y 0.69 horas. El PnL por notional de entrada es peor en esos subconjuntos, entre aproximadamente −7.78 y −10.45 bps. La mejora total no puede describirse como un mejor precio de ejecución. Incluye selección de fills, tiempo en posición, capital y ocupación posteriores, todos endógenos. Tampoco estas intersecciones representan el universo de señales.

Cq ADX24 registra 40 entradas LIMIT y una MARKET, tal como las clasifica el motor; las demás Cq nuevas registran sólo LIMIT y M sólo MARKET. Todas pagan la misma comisión por lado y las cantidades/precios ejecutados concilian. El nombre de la política retest no se usa para sustituir el tipo de orden realmente guardado.


## Calendario MTM verificado por la auditoría central

Fuente leída: strategies/MultiAssetRetestBtcShort4h/reports/R60_MTM_RESULTS_20261019.md. Cierres diarios UTC, terminales conciliados. Denominadores: 61 meses y 19 trimestres completos; octubre 2020 y diciembre 2025 parciales se preservan separadamente en el JSON canónico.

| Contexto | Meses + Cq / M (de 61) | Trimestres + Cq / M (de 19) | DD diario UTC Cq / M % |
|---|---:|---:|---:|
| Centro | 15 / 17 | 8 / 10 | -6.922 / -7.650 |
| P1 | 16 / 17 | 9 / 10 | -6.922 / -7.650 |
| P2 | 14 / 16 | 7 / 10 | -9.109 / -10.072 |
| P3 | 16 / 17 | 7 / 7 | -8.305 / -10.382 |
| P4 | 12 / 15 | 6 / 9 | -9.159 / -10.019 |
| P5 | 15 / 17 | 8 / 10 | -7.055 / -7.766 |

MARKET añade entre uno y tres meses completos positivos según contexto. No mejora el número de trimestres en ADX24. Ninguna variante aislada demuestra la meta de regularidad de cartera; esa meta tampoco se exige a cada señal. El mayor DD diario de MARKET se confirma en todos los pares. Root verificó las veinte fuentes, formularios y conjuntos de hyperparameters ejecutados de la ronda, todos exactos y sin DNA de optimización.

## Auditoría y decisión

Los dos trabajos de análisis terminaron succeeded: A 921ea63f1aff4d26afe6759e1912dc63 (ocho snapshots completos) y B c6e43c29c97142fc85993bb1f205466a (seis, con centros repetidos sólo como inputs). Fees, PnL, cantidades, wallet y ausencia de solapamientos pasan en todos. Máximo error de fee <2e−15 USDT, de PnL <1.5e−12, de wallet <1.1e−11 y de cantidad cero. Los resúmenes recuperados íntegros tienen 43308 y 32115 bytes, truncated=false. No se necesita inferir calendarios desde curvas del motor marcadas a 00:01; la auditoría MTM UTC es responsabilidad del consolidado central.

Se cierra la tanda sin más corridas, sin optimizar vecinos y sin cambiar referencias. La comparación MARKET frente a retest conserva su signo local, pero la concentración, la mayor exposición/DD y la dependencia de 2024–2025 impiden tratarla como promoción definitiva o validación independiente. No se afirma regularidad objetivo de cartera, ni traslado ya validado al perpetuo.

Archivos dentro del proyecto Jesse:

- Protocolo previo: strategies/AttrPaxgC0Retest4h/reports/R60_PAXG_PROTOCOL_20261019.md.
- Revisión de diez fuentes: strategies/R60PaxgN24Retest4h/reports/R60_PAXG_IMPLEMENTATION_REVIEW_20261019.md.
- Manifiesto completo con IDs y Dashboard: strategies/R60PaxgN24Retest4h/reports/R60_PAXG_RUN_MANIFEST_20261019.md.
- Tabla exacta JSON, 12 filas, cinco contrastes y Sharpe: strategies/R60PaxgN24Retest4h/reports/R60_PAXG_EXACT_TABLE_20261019.md.
- Fuentes reproducibles y auditorías completas: R60_PAXG_ANALYSIS_SOURCE_A_20261019.md, R60_PAXG_ANALYSIS_SOURCE_B_20261019.md, R60_PAXG_AUDIT_A_20261019.md y R60_PAXG_AUDIT_B_20261019.md, todas bajo strategies/R60PaxgN24Retest4h/reports/.
