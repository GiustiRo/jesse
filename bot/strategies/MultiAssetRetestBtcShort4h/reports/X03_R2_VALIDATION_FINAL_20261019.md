# X03 R2 — validación final de estabilidad

X03 mantiene un aporte nominal positivo alrededor de seis vecinos, pero no supera una validación de regularidad robusta a costes y timing. Ninguno cumple conjuntamente el objetivo de 65% de meses y 80% de trimestres positivos en ambas carteras, con bins completos y parciales, bajo +5 bps RT. El retraso de 4h elimina la ventaja de cartera frente al control sin X03. Los vecinos están excluidos de selección económica; no se cambia la regla original de 12 barras, 2R y 48h.

Las 14 sesiones V201–V207 B/C finalizaron sin errores. QA: 156 checks PASS; 42 snapshots de rutas exactos; formularios y HP comprobados; fuente X03 original intacta en la lectura final. Root concilió fills, cantidades, fees, PNL, wallet, cierre terminal y MTM diario UTC. Fuente numérica: X03_R2_VALIDATION_COMPACT_20261019.md y auditorías NOM1/3/4/6/8/9/10. Todos los datos siguen siendo desarrollo 2020–2025 intensamente reutilizado; 2026 permanece cerrado. B/C comparten mecanismo BTC y muestra.

## Aporte y fricción

USDT. Los incrementos nominal y +10 se comparan con el control sin X03 al mismo coste. Los overlays conservan fills, cantidades y horarios; no reejecutan gestión ni sizing. Ex3 elimina los tres mejores suplementos según neto nominal y añade +10 bps RT, sin rerun.

| Variante/cartera | Cambio | Neto nominal | Δ nominal sin X03 | Δ +10 sin X03 | Suplemento +10 | Ex3 suplemento +10 |
|---|---|---:|---:|---:|---:|---:|
| [V201B](http://localhost:9200/#/backtest/dc09487b-eb8a-44c3-97c4-4b2acfeab83f) | Ventana 8 | 9748.31 | 514.11 | -157.54 | -330.39 | -1318.96 |
| [V201C](http://localhost:9200/#/backtest/7f1c089a-2751-43fc-989d-8922c09d92a5) | Ventana 8 | 9928.66 | 520.83 | -157.46 | -375.35 | -1384.83 |
| [V202B](http://localhost:9200/#/backtest/ad180c10-f055-4b12-8432-e369caac8c3a) | Ventana 16 | 12393.83 | 3159.63 | 2747.29 | 2014.30 | 873.23 |
| [V202C](http://localhost:9200/#/backtest/7895cfd4-60e8-4813-86a3-31c5a4345666) | Ventana 16 | 12614.45 | 3206.62 | 2785.38 | 2012.96 | 849.96 |
| [V203B](http://localhost:9200/#/backtest/282ac385-0a2d-4793-9a80-038232c399d9) | TP 1.5R | 11525.62 | 2291.43 | 1701.95 | 1001.65 | 234.01 |
| [V203C](http://localhost:9200/#/backtest/e039907b-67a5-4531-8ffe-14842cc4fd01) | TP 1.5R | 11733.80 | 2325.97 | 1728.55 | 977.96 | 200.65 |
| [V204B](http://localhost:9200/#/backtest/ef335fc4-a08a-47b5-ba2f-d29e5b9159fa) | TP 2.5R | 12701.16 | 3466.96 | 2866.93 | 2330.45 | 1103.51 |
| [V204C](http://localhost:9200/#/backtest/798a0f06-6005-4bea-bebc-dc22a89093dd) | TP 2.5R | 12906.32 | 3498.50 | 2889.40 | 2326.55 | 1080.36 |
| [V205B](http://localhost:9200/#/backtest/e6e91629-fb28-4a05-ac74-2329ee932bfe) | Hold 24h | 9992.67 | 758.47 | 270.96 | 317.15 | -548.47 |
| [V205C](http://localhost:9200/#/backtest/608630f0-127d-4330-9a43-34f94b25ac72) | Hold 24h | 10184.26 | 776.43 | 288.18 | 312.45 | -564.13 |
| [V206B](http://localhost:9200/#/backtest/046eb445-5e0a-413f-aec9-2498a6a3cb38) | Hold 72h | 11516.32 | 2282.13 | 1781.83 | 1387.97 | 359.76 |
| [V206C](http://localhost:9200/#/backtest/79037f88-5dcd-4c0e-814f-38ad77b5e6af) | Hold 72h | 11692.92 | 2285.09 | 1779.54 | 1382.01 | 337.49 |
| [V207B](http://localhost:9200/#/backtest/37a6818d-37d3-4ffc-b821-f6ed69a1e459) | Retraso 4h | 8453.33 | -780.87 | -1050.98 | 144.45 | -682.38 |
| [V207C](http://localhost:9200/#/backtest/cfda043d-15dc-4443-9655-fbabf6fae45b) | Retraso 4h | 8588.88 | -818.95 | -1078.21 | 159.05 | -680.83 |

Los 6/6 vecinos OFAT mantienen incremento de cartera nominal y suplemento nominal positivo en ambas carteras. A +10 bps RT, 5/6 mantienen el incremento de cartera: falla V201, cuya ventana de 8 barras también produce suplemento negativo bajo coste. Tras excluir los tres mejores suplementos y añadir +10, sobreviven 4/6; fallan V201 y V205.

Esto muestra continuidad parcial del aporte económico, pero no una meseta del objetivo conjunto. Cantidad y PNL reflejan ocupación, señales desplazadas y capital endógeno. El horizonte 16 y TP 2.5R mejoran algunas métricas nominales; esos resultados no autorizan escogerlos.

## Regularidad bajo +5 bps RT

Meses positivos/activos. Todos los vecinos tienen 61 meses completos activos y 63 incluyendo fronteras, por lo que coinciden los denominadores activos y calendario. Trimestres positivos/todos: 19 completos y 21 incluyendo fronteras. La aprobación se calcula sin redondear porcentajes.

| Variante/cartera | Meses completos | Q completos | Meses con parciales | Q con parciales |
|---|---:|---:|---:|---:|
| V201B | 39/61 | 12/19 | 39/63 | 13/21 |
| V201C | 38/61 | 12/19 | 38/63 | 13/21 |
| V202B | 43/61 | 13/19 | 43/63 | 15/21 |
| V202C | 44/61 | 16/19 | 44/63 | 18/21 |
| V203B | 39/61 | 14/19 | 39/63 | 15/21 |
| V203C | 38/61 | 15/19 | 38/63 | 16/21 |
| V204B | 39/61 | 15/19 | 39/63 | 16/21 |
| V204C | 39/61 | 15/19 | 39/63 | 16/21 |
| V205B | 36/61 | 15/19 | 36/63 | 16/21 |
| V205C | 37/61 | 16/19 | 37/63 | 17/21 |
| V206B | 39/61 | 15/19 | 39/63 | 16/21 |
| V206C | 40/61 | 15/19 | 40/63 | 16/21 |
| V207B | 39/61 | 14/19 | 39/63 | 15/21 |
| V207C | 40/61 | 13/19 | 40/63 | 14/21 |

V202 C supera individualmente las cuatro proporciones; V202 B falla en trimestres: 13/19 y 15/21. No se debe seleccionar la cartera favorable ni recalibrar el horizonte por su resultado. TP 1.5R/2.5R y timeout 24h/72h tampoco rescatan el objetivo conjunto bajo +5. Todos los drawdowns del motor se mantienen dentro del límite de 25%, que por sí solo no satisface regularidad.

## Retraso fuerte y atribución

V207 consume la señal una vez y espera exactamente al siguiente cierre de 4h. Expira si hay ocupación, entrada pendiente, prioridad original o un clock perdido; no revalida ni mantiene cola. La distancia y TP se congelan al origen; protección y plazo de 48h se anclan al fill.

Su cartera termina en 8453.33/8588.88, frente a 9234.19/9407.83 sin X03: incrementos de −780.87/−818.95 nominales y −1050.98/−1078.21 bajo +10. El suplemento aislado aún gana 144.45/159.05 bajo +10 mientras la cartera empeora. Su PNL aislado no mide el valor incremental total.

Los contadores concilian en ambas: 95 eventos = 78 llegados al vencimiento + 17 expirados por ocupación/entrada pendiente; 78 = 76 fills/cierres + 2 prioridades originales. No hubo clock inválido o perdido contado. Los seis vecinos OFAT conservan las 31 entradas y salidas long BTC originales. V207 conserva 30/31, con 32 long en total y dos nuevos. Las reglas long no cambian; sus fills sí cambian por la ocupación. Este estrés no permite cuantificar latencia de minutos.

## Evidencia temporal condicionada

En X03 original, aproximadamente 80% del neto suplementario procede de 2022 y 2025; 2024 pierde. Esos dos años explican alrededor de 77% del incremento MTM de cartera, una atribución distinta por el capital endógeno y las otras patas. Eliminar aritméticamente cualquier año deja incremento positivo incluso bajo +10, pero conserva los caminos observados: no es rerun ni OOS.

Bootstrap pareado: 10.000 réplicas, semilla 20261019, bloques circulares de 3 meses como principal y 6 como sensibilidad; índices comunes para B/C y costes, sin agrupar B/C. Los 61 meses completos son principales; 63 incluyendo fronteras son secundarios. En 61, los límites inferiores de la media incremental son positivos. En 63 con bloques de 3, las bandas cruzan cero bajo +5 y +10 estáticos.

Con comisión real del motor de .00070 por lado, las bandas de 63 meses/bloques de 3 también cruzan cero: B [−1.74, 70.96], C [−2.22, 70.16] USDT por mes. Con bloques de 6 son apenas positivas. Las fronteras y longitud de bloque influyen; no corresponde escoger la especificación favorable ni interpretar la fracción positiva como probabilidad de ausencia de sobreajuste.

El estrés del motor afecta todas las patas. Root identificó un BE de PAXG dependiente de fee que adelantó un runner; la fuente permanece congelada. X03 frente a sin X03 al mismo fee .00070 conserva +2137.24/+2098.09 USDT. Es una comparación condicionada de carteras, no identificación causal de alpha BTC. Detalles en X03_R2_ENGINEFEE_BOOTSTRAP_20261019.md. Overlay fijo y reejecución del motor responden preguntas diferentes.

## Disposición

La muestra fue explorada repetidamente y X03 fue seleccionado tras búsquedas previas. El remuestreo y B/C no eliminan selección múltiple, crean datos inéditos ni prueban ausencia de sobreajuste. Las bandas son descriptivas condicionadas: no son p-values confirmatorios ni drawdowns simulados.

No se ejecutó MC de candles multiasset: la documentación no garantiza correlaciones ni semillas compartidas. No se comprobó ni se afirma un fallo del runner. Tampoco se ejecutaron trades MC o RST.

La validación encuentra aporte económico nominal, continuidad parcial de parámetros, concentración temporal y fragilidad de regularidad, fricción y timing. X03 permanece como investigación congelada. Los vecinos no autorizan recalibración o promoción. La selección y confirmación de otras familias corresponde al protocolo de root y conserva las mismas limitaciones de desarrollo. Sin operativa real ni apertura de 2026.
