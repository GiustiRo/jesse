# Comparación ampliada de candidatas en 2026 — resultados finales

Fecha local: 19 de octubre de 2026, America/Montevideo. Se ejecutaron las 20 corridas nuevas fijadas antes de sus resultados: N204, N503, P604, C504 y K1005 × carteras B/C × comisiones normales/estresadas. K1001 aporta cuatro sesiones definitivas ya existentes, sin volver a correrla. Son 24 configuraciones únicas comparadas, no 24 corridas nuevas ni muestras independientes.

## Resultado principal
Ninguna de las cinco candidatas nuevas supera los criterios OOS. Todas las carteras B pierden dinero, tienen PF inferior a 1 y drawdown nominal peor que −25%. Las carteras C ganan, pero sus PF nominales quedan entre 1.146 y 1.181, inferiores al mínimo 1.2. En estrés, todas las B pierden y todas las C mantienen un neto positivo, sin que eso rescate el incumplimiento nominal.

K1001 conserva el mayor retorno y el menor drawdown en cada combinación equivalente de cartera y coste frente a las cinco candidatas. Esto NO valida a K1001: su B también falla, y su C depende de una sola operación SPY. La prueba ampliada no encontró una alternativa que supere las puertas fijadas.

## Contrato y alcance
Capital inicial compartido de 10.000 USDT, riesgo objetivo 2% por operación / 6% agregado, isolated 3x; BTC/PAXG/SPY en 4h y tres feeds de 1m, orden original. Warmup 240, fast_mode false, debug true. Fee nominal 0.00045 por lado; estrés 0.00095 por lado. Cap nocional 4.4, buffer de margen 90% y reserva de sizing 0.001 conservados. B usa SPY Second; C SPY Market. Ventana 2026-01-01 inclusiva → 2026-10-19 exclusiva, hasta el 18 de octubre UTC. No se amplió la ventana al cambiar de día UTC durante la ejecución.

Las señales y reglas de gestión existían antes de abrir 2026. N204 reutiliza el perfil R12 2%/6%; las otras cuatro recibieron copias que cambian sólo nombre de clase, esas dos constantes de riesgo y comentarios explicativos. No se retocaron reglas, stops, targets ni umbrales. Los originales siguen intactos. Y902 quedó fuera por instrucción previa.

Esta comparación se decidió después de observar K1001 en 2026: es una ampliación exploratoria, no una nueva selección confirmatoria ciega. Un eventual ajuste o selección por estos resultados necesitará datos posteriores no usados para una validación independiente. No se combinan retrospectivamente mecanismos ni se declara ausencia de sobreajuste.

## Por qué se incluyeron
| Candidata | Motivo documentado en desarrollo 2020–2025 |
|---|---|
| N204 | Referencia congelada de la familia. |
| N503 | Filtro de avance ineficiente, ER ≤ 1/3; mejoró neto pero falló regularidad mensual de C. |
| P604 | Liberación del suplemento tras confirmación de precio para permitir la operativa original; mejora nominal pequeña, sin superar la regularidad de C. |
| C504 | Salida ante recuperación bajo el nivel A congelado; mejora nominal marginal, sin superar la regularidad trimestral de B. |
| K1005 | Trailing persistente tras 1R; mayor neto nominal de desarrollo, con validación propia de costes todavía incompleta. |

No se añadieron controles duplicados, recetas nuevas ni variantes después de ver los resultados de esta lista.

## Retornos del período
| Candidata | B nominal % | C nominal % | B estrés % | C estrés % |
|---|---:|---:|---:|---:|
| K1001 (comparador existente) | -1.27 | +10.35 | -5.28 | +4.96 |
| N204 | -2.93 | +8.43 | -7.24 | +2.78 |
| N503 | -2.14 | +9.37 | -6.31 | +3.79 |
| P604 | -2.32 | +9.14 | -6.51 | +3.56 |
| C504 | -3.57 | +7.75 | -7.80 | +2.16 |
| K1005 | -3.85 | +7.48 | -7.84 | +2.14 |

Son rendimientos acumulados de esa ventana, no rentas anuales proyectadas. El saldo final es 10.000 USDT más el beneficio neto que se detalla a continuación.

## Las 20 corridas nuevas, con enlaces y métricas
| Candidata / cartera / coste | Sesión | Neto USDT | Saldo final | PF | DD % | Trades | Fees USDT | Sharpe |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| N204 B N | [dashboard](http://localhost:9200/#/backtest/3e9cec7e-da5b-4baf-9355-5b29b5e8c295) | -293.17 | 9706.83 | 0.941 | -27.29 | 51 | 425.24 | -0.115 |
| N204 C N | [dashboard](http://localhost:9200/#/backtest/0d78145f-b775-4e60-b2f0-84a10e1f858e) | 843.35 | 10843.35 | 1.161 | -20.91 | 52 | 468.84 | 0.616 |
| N503 B N | [dashboard](http://localhost:9200/#/backtest/21e9be0c-681c-42a9-b075-ac1192d4255e) | -214.31 | 9785.69 | 0.956 | -26.70 | 50 | 415.80 | -0.059 |
| N503 C N | [dashboard](http://localhost:9200/#/backtest/e6dc07dc-6050-412e-a81e-3a04181212a0) | 937.02 | 10937.02 | 1.181 | -20.23 | 51 | 458.25 | 0.671 |
| P604 B N | [dashboard](http://localhost:9200/#/backtest/04715e14-4389-422b-9317-3fe9f2d01a3d) | -231.82 | 9768.18 | 0.952 | -26.83 | 50 | 416.11 | -0.072 |
| P604 C N | [dashboard](http://localhost:9200/#/backtest/26a78404-df8a-4bc9-9cf7-c675614c4abf) | 913.66 | 10913.66 | 1.177 | -20.39 | 51 | 458.45 | 0.657 |
| C504 B N | [dashboard](http://localhost:9200/#/backtest/c607ec3c-55ac-46ef-aec6-34774822e091) | -357.19 | 9642.81 | 0.928 | -27.77 | 51 | 424.41 | -0.160 |
| C504 C N | [dashboard](http://localhost:9200/#/backtest/dcc4b404-774c-4230-9043-d94aed80ef3b) | 775.03 | 10775.03 | 1.146 | -21.40 | 52 | 467.71 | 0.575 |
| K1005 B N | [dashboard](http://localhost:9200/#/backtest/f033cdd0-ce59-4c39-a83e-564b47c1855b) | -385.49 | 9614.51 | 0.913 | -27.83 | 47 | 390.97 | -0.195 |
| K1005 C N | [dashboard](http://localhost:9200/#/backtest/a6dabc9f-0860-46d1-8e56-7105311aa687) | 747.53 | 10747.53 | 1.158 | -21.35 | 48 | 431.02 | 0.571 |
| N204 B F95 | [dashboard](http://localhost:9200/#/backtest/a06b1bcd-a5a9-4275-b512-94e449af8069) | -723.92 | 9276.08 | 0.856 | -29.46 | 51 | 864.97 | -0.438 |
| N204 C F95 | [dashboard](http://localhost:9200/#/backtest/dc59d1d4-c519-407f-a969-0eee85dc34a9) | 278.06 | 10278.06 | 1.052 | -22.48 | 52 | 948.37 | 0.275 |
| N503 B F95 | [dashboard](http://localhost:9200/#/backtest/666e8f1e-dd76-44d7-bc27-20d7dd0b2d58) | -630.55 | 9369.45 | 0.873 | -28.75 | 50 | 845.80 | -0.369 |
| N503 C F95 | [dashboard](http://localhost:9200/#/backtest/bf16cccd-9682-4cba-9fdc-fd475c330289) | 379.05 | 10379.05 | 1.072 | -21.72 | 51 | 927.37 | 0.339 |
| P604 B F95 | [dashboard](http://localhost:9200/#/backtest/242f4120-6bc4-44ae-b040-80af12c432dc) | -651.32 | 9348.68 | 0.869 | -28.92 | 50 | 846.46 | -0.385 |
| P604 C F95 | [dashboard](http://localhost:9200/#/backtest/6ac5ce76-1717-4027-b430-f1b7f80088fb) | 356.16 | 10356.16 | 1.068 | -21.90 | 51 | 928.04 | 0.324 |
| C504 B F95 | [dashboard](http://localhost:9200/#/backtest/5971e31a-b756-47cd-89d3-a84f502f4915) | -779.61 | 9220.39 | 0.847 | -29.88 | 51 | 862.79 | -0.480 |
| C504 C F95 | [dashboard](http://localhost:9200/#/backtest/a8a94a70-ef58-425c-a9f2-69ff4ea14b71) | 215.74 | 10215.74 | 1.040 | -22.95 | 52 | 946.31 | 0.235 |
| K1005 B F95 | [dashboard](http://localhost:9200/#/backtest/e7ee6486-6b4f-470a-8ea1-2831324bbb59) | -783.72 | 9216.28 | 0.828 | -29.77 | 47 | 796.12 | -0.509 |
| K1005 C F95 | [dashboard](http://localhost:9200/#/backtest/4dce0a05-33b1-4ccd-b661-5cbb43923a0d) | 213.93 | 10213.93 | 1.044 | -23.21 | 48 | 873.51 | 0.235 |

Puertas nominales por cartera: neto positivo, PF ≥ 1.2, DD no peor que −25%, al menos 20 trades cerrados. En estrés se exige neto positivo; no se impuso retrospectivamente PF ≥ 1.2 bajo ese coste. Cada candidata necesita cumplir en B y C. Todas tienen muestra de trades suficiente para la puerta mínima, pero eso no certifica confianza estadística ni sustituye los otros criterios.

## De dónde sale el beneficio de C
| Candidata, nominal C | BTC: neto / trades | PAXG: neto / trades | SPY: neto / trades | Total neto |
|---|---:|---:|---:|---:|
| K1001 | -1880.50 / 38 | 1616.64 / 8 | 1298.98 / 1 | 1035.12 |
| N204 | -2067.31 / 43 | 1618.06 / 8 | 1292.60 / 1 | 843.35 |
| N503 | -1972.46 / 42 | 1616.88 / 8 | 1292.60 / 1 | 937.02 |
| P604 | -1991.66 / 42 | 1612.73 / 8 | 1292.60 / 1 | 913.66 |
| C504 | -2136.52 / 43 | 1618.95 / 8 | 1292.60 / 1 | 775.03 |
| K1005 | -2169.41 / 39 | 1617.96 / 8 | 1298.98 / 1 | 747.53 |

BTC tiene contribución neta negativa en las 24 configuraciones. PAXG es positivo. Cada cartera C tiene una sola operación SPY ganadora, cuyo PnL supera el neto total: la suma de aportes BTC+PAXG sigue siendo negativa. B no ejecuta operaciones SPY en esta ventana. Esto es atribución contable de las operaciones observadas; no es un backtest sin SPY, porque quitar un activo cambiaría cuotas, capital y cantidades.

## Regularidad y concentración
| Candidata | Meses positivos nominal B/C, de 10 | Trimestres completos positivos B/C, de 3 | Peor mes nominal B/C % |
|---|---:|---:|---:|
| K1001 | 3/5 | 1/2 | -15.15/-15.12 |
| N204 | 4/6 | 1/2 | -14.72/-14.72 |
| N503 | 4/6 | 1/2 | -14.72/-14.72 |
| P604 | 4/6 | 1/2 | -14.53/-14.53 |
| C504 | 4/6 | 1/2 | -15.27/-15.27 |
| K1005 | 3/5 | 1/2 | -15.15/-15.12 |

Los conteos incluyen octubre parcial; Q4 es parcial y no entra en los tres trimestres completos. Los meses se calculan desde equity, no sumando trades por fecha de cierre. Primer punto de equity 2026-01-01 23:00 UTC, último 2026-10-19 00:00 UTC. DD de equity diaria, no caída máxima intraminuto. Meses y trimestres completos, todos los valores y concentración de mejor trade se conservan en los cuatro anexos de datos.

## Diferencias observadas de ejecución
Las trayectorias no son duplicados económicos a la precisión auditada, aunque comparten señales, activos y datos. En nominal, N503 elimina una entrada de N204, sin cambiar las salidas de entradas comunes; su neto mejora 78.87/93.67 USDT en B/C, pero sigue sin aprobar. P604 también elimina una entrada y modifica dos salidas comunes frente a N204; mejora menos que N503. C504 conserva las entradas de N204 y cambia una salida, empeorando el neto. K1005 frente a K1001 añade una entrada y modifica una salida común, empeorando el neto en ambas carteras. Son diferencias de registros y sizing compartido, no casos estadísticos independientes ni identificación causal de cada modificación.

## Verificación y datos
Las 20 sesiones terminaron sin errores de ejecución. Cada formulario se verificó byte a byte contra el esperado y sus tres snapshots contra las fuentes congeladas. Cuatro análisis terminaron correctamente: suma de PNL igual al neto del motor, saldo inicial + neto igual al saldo final y brecha de equity terminal menor a 0.01 USDT. Se conciliaron las cantidades ejecutadas de entrada y salida por trade, preservando la distinción de campos del motor que pueden ser anteriores a liquidación de frontera.

Mismos datos corregidos de la prueba K1001 definitiva: BTC y PAXG tienen reloj completo de 419.040 minutos por ruta; PAXG conserva la fuente Binance Spot con solape idéntico y apéndice verificado. SPY es HistData SPX CFD BID /10, EST fijo UTC−5, volumen cero y huecos originales; seis minutos ambiguos de julio se reconstruyeron desde ticks del mismo proveedor antes de evaluar rendimientos. La última observación SPX es el viernes 16 de octubre 21:13 UTC; se conserva el fin solicitado en domingo. La aceptación del motor no certifica apertura dominical ni ejecución 24/7 de un instrumento nativo. No se modificaron velas ni caché en esta ampliación.

La réplica no modela funding, slippage real, liquidez ni impacto. La reserva de sizing 0.001 no es slippage aplicado. Aumentar el fee puede cambiar tamaños; no equivale a modelar esos costes. B/C no son muestras independientes. Sin cambios globales, framework, reinicios, live o paper.

## Archivos y estado final
- OOS_2026_ARCHIVED_CANDIDATES_PROTOCOL_20261019.md: lista y criterios fijados antes de nuevos resultados.
- OOS_2026_ARCHIVED_CANDIDATES_REGISTRY_20261019.md: veinte sesiones, cuatro análisis y verificaciones.
- OOS_2026_ARCHIVED_CANDIDATES_SOURCE_QA_20261019.md: normalización de sizing y conservación de fuentes.
- OOS_2026_ARCHIVED_CANDIDATES_ANALYSIS_SOURCE_20261019.md: código reproducible de auditoría.
- OOS_2026_ARCHIVED_DATA_A_N_20261019.md y OOS_2026_ARCHIVED_DATA_B_N_20261019.md: métricas nominales completas, meses, trimestres y firmas.
- OOS_2026_ARCHIVED_DATA_A_F95_20261019.md y OOS_2026_ARCHIVED_DATA_B_F95_20261019.md: equivalentes bajo estrés.

No quedan corridas pendientes de esta matriz. No se promociona ninguna candidata ni se ajusta 2026 para rescatar resultados.
