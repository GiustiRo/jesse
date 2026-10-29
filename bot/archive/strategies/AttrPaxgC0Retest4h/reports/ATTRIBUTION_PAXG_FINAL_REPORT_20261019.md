# Atribución PAXG: entrada, gestión y exposición direccional

Fecha: 19 de octubre de 2026, America/Montevideo. **Diecisiete configuraciones terminadas, con reproducción exacta de la referencia aislada y auditoría completa.** Esta etapa explica de dónde provienen las diferencias de rendimiento; no promueve una seed, una gestión nueva o una sustitución de la referencia.

La evidencia más clara es la sensibilidad al horizonte y al tiempo de exposición. Quitar trailing aumenta mucho el total, pero concentra la ganancia en un runner de casi665 días que llega al corte final. Entrar mediante relojes sin filtros genera más beneficio en estas cinco trayectorias y también mucha más exposición. El retest original no muestra una superioridad inequívoca frente a esos controles. Esto no prueba ausencia general de calidad de entrada ni identifica una política óptima.

## Contrato y comparabilidad

Cuenta aislada de 10.000 USDT; riesgo planificado del 1%; fee de 0,00045 por lado para todas las órdenes; 5x isolated; techo bruto de 4,4x; sin piramidado. Ventana 2020-10-15→2025-12-31 exclusiva, warmup de 240, modo normal. Reserva de 10 bps sólo en sizing. Proxy spot PAXG aceptado; sin funding, fuentes nuevas, BTC o 2026.

Se predeclararon C0, Cq, E1–E4 y M y diez clocks R/U. Root revisó matriz y código. Los 17 archivos son autocontenidos y se leyeron completos; root además verificó sus snapshots/formularios. No se cambió una señal, salida, seed o umbral después de observar sus resultados. Hubo exactamente17 fulls PAXG, no sensibilidades encubiertas.

C0 reproduce el benchmark93a161:35 operaciones, 70 órdenes ejecutadas, 1.904 puntos de equity y métricas idénticos, con diferencias numéricas máximas de 0. C0 sólo renombra clase. Cq añade quote M1 exacta por searchsorted exclusivamente al armar entrada LIMIT; no condiciona trailing. M/R/U comparten ese guard. E1–E3 conservan la entrada original; E4 añade sólo liquidación temporal con deuda y quote fresca, manteniendo stop activo.

La comparación corresponde a políticas con ocupación y capital endógenos. Igual riesgo por entrada no iguala exposición, duración ni conjunto futuro de trades.

## Diecisiete resultados

| ID y sesión | N | Neto USDT | PF | DD motor | Tiempo expuesto | Proxy nocional-tiempo |
|---|---:|---:|---:|---:|---:|---:|
| [C0 Réplica](http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673) | 35 | 546,11 | 1,308 | -6,92% | 13,36% | 0,1038x |
| [Cq Guard M1](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) | 35 | 546,11 | 1,308 | -6,92% | 13,36% | 0,1038x |
| [E1 Sin BE](http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b) | 35 | 491,17 | 1,271 | -7,40% | 13,36% | 0,1033x |
| [E2 Sin trailing](http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc) | 15 | 4325,43 | 6,386 | -10,67% | 40,15% | 0,2058x |
| [E3 Stop inicial](http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242) | 15 | 3669,37 | 4,019 | -14,75% | 40,57% | 0,2010x |
| [E4 Stop +72h](http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837) | 47 | -374,35 | 0,829 | -6,41% | 5,76% | 0,0426x |
| [M MARKET](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) | 38 | 962,13 | 1,574 | -7,65% | 15,20% | 0,1171x |
| [R01 R seed101](http://localhost:9200/#/backtest/fa518c27-144f-4af4-837c-b00c837110b1) | 33 | 108,95 | 1,063 | -8,42% | 10,21% | 0,0722x |
| [R02 R seed202](http://localhost:9200/#/backtest/a8e6461e-2b14-4130-b9f6-0989a4483c8c) | 30 | -153,99 | 0,902 | -8,81% | 8,63% | 0,0706x |
| [R03 R seed303](http://localhost:9200/#/backtest/0e7552b8-3491-4925-b230-f31c89b92796) | 30 | 869,16 | 1,810 | -7,27% | 13,54% | 0,0928x |
| [R04 R seed404](http://localhost:9200/#/backtest/0edfce4f-695a-4213-8426-304b9af6d5a4) | 25 | 1252,44 | 2,088 | -4,58% | 11,83% | 0,0951x |
| [R05 R seed505](http://localhost:9200/#/backtest/cfff7109-04c5-4420-8a90-fc19ceec6ef8) | 36 | 47,86 | 1,032 | -12,41% | 13,70% | 0,0904x |
| [U01 U seed101](http://localhost:9200/#/backtest/6cc08024-0aa2-4cdf-a666-25f4351681bd) | 118 | 2902,32 | 1,514 | -14,11% | 50,16% | 0,3570x |
| [U02 U seed202](http://localhost:9200/#/backtest/4d938a9b-653e-4226-9a1c-899b689e6b62) | 107 | 37,11 | 1,007 | -18,39% | 39,92% | 0,2701x |
| [U03 U seed303](http://localhost:9200/#/backtest/e572d0cc-9a77-4998-b2ae-ec335daadf7d) | 129 | 2611,10 | 1,402 | -19,11% | 51,33% | 0,3583x |
| [U04 U seed404](http://localhost:9200/#/backtest/f9af824c-8ac8-4fd5-9b2f-52adaebb112a) | 126 | 1667,03 | 1,275 | -21,72% | 48,15% | 0,3298x |
| [U05 U seed505](http://localhost:9200/#/backtest/54613844-7e5d-4911-9342-071f65e0922b) | 122 | 3873,54 | 1,629 | -9,73% | 49,80% | 0,3923x |

Proxy nocional-tiempo = sum(nocional de entrada × horas de holding)/(10.000 × horas de ventana). Su unidad es múltiplo del capital inicial sobre el período. Usa precio de entrada: **no es exposición MTM, margen medio ni capital de una cartera nueva**. Tiempo expuesto usa toda la ventana, incluido cash de inicio y espera. Las17 filas exactas, CAGR y cohortes están en ATTRIBUTION_PAXG_EXACT_TABLE_20261019.md.

## Qué aporta cada contraste

**Frescura:** Cq yC0 comparten35 entradas ejecutadas y resultados económicos. El efecto económico observado del guard es nulo en esta ventana. Los snapshots no contienen todos los armados no ejecutados: no se concluye que el guard nunca rechazó uno.

**BE:** E1 conserva35 fills de entrada comunes conC0. Quitar BE reduce el neto54,94USDT y empeora DD; la diferencia media de PnL/nocional en esas entradas es aproximadamente−2,62bps. Cantidades/capital futuros siguen siendo endógenos. Aquí BE no explica la mayor parte de la diferencia de retorno de la referencia.

**Trailing y duración:** E2 gana 4.325,43 con 15 trades frente a 546,11 y 35 enC0, pero su mayor trade aporta 5.119,36 netos; sin él queda−793,93. E3 gana 3.669,37 con 15 trades y sólo una operación ganadora, de 4.884,91; sin ella pierde1.215,54. Ambos últimos runners duran 15.971,27 horas, aproximadamente 665,47 días, hasta la frontera del motor. El contador preterminación 1 y su open_pl concilian con cierre sintético y wallet. Ese cierre no prueba liquidez nativa y no equivale a una regla operativa de salida.

La exposición temporal sube de 13,36% enC0 a 40,15%/40,57% enE2/E3. Sus proxies nocional-tiempo pasan de0,1038x a0,2058x/0,2010x. Mayor retorno total mezcla gestión, duración y oportunidades perdidas por ocupación. El mejor PF deE2 no demuestra una fuente amplia e independiente de alpha.

**Expiración:** E4 conserva stop inicial y limita a 72 h desde fill, con decisiones de 4 h y espera de quote válida. Genera 47 trades, pero pierde 374,35; también pierde 61,78 antes de fees. Su máximo observado de 75,98 h es coherente con el reloj de 4 h, no un fill ficticio a las 72 h. Recortar duración no produjo el ingreso corto y regular buscado bajo esta receta.

**MARKET frente LIMIT:** M gana 962,13 frente a 546,11 enCq, con 38 frente a 35 trades y mayor DD/exposición. No hay fills en timestamp real idéntico. El vínculo secundario por EXACTO created_at, símbolo y dirección encuentra 24 orígenes inequívocos, sin claves ambiguas. En esa intersección seleccionada, MARKET paga de media 15,61 bps más y llena 33,17 minutos antes; la diferencia media PnL/nocional MARKET−LIMIT es −8,36 bps. El mayor neto global no se explica como mejora de precio en esos24 casos. Participación, selección de fill, gestión anclada al entry y capital posterior cambian; no se adjudica una causa pura sin medirla.

## Entrada original y clocks: todas las seeds

R mantiene EMA/ADX/RSI/rango de la base y elimina ruptura/retest/desplazamiento Donchian. U conserva sólo calendario,history de 100 velas, ATR, quote y riesgo. Ambos usan SHA256 de ATTR1|symbol|seed|closed_candle_open_time, primeros8bytes big-endian%48==0, con seeds101/202/303/404/505. El bit se procesa aun ocupado y no se encola. Gestión y riesgo originales en todas.

| Familia, cinco seeds completas | Neto mínimo | Mediana | Máximo | Media | Tiempo expuesto medio | Proxy nocional-tiempo medio |
|---|---:|---:|---:|---:|---:|---:|
| R | -153,99 | 108,95 | 1252,44 | 424,88 | 11,58% | 0,0842x |
| U | 37,11 | 2611,10 | 3873,54 | 2218,22 | 47,87% | 0,3415x |

Estas medias/medianas describen cinco cuentas alternativas, **no un ensemble ejecutado ni una cartera**. C0 supera tres R y queda debajo de dos. R tiene entre25 y36 trades, con exposición temporal8,63–13,70%; por sí solas cinco trayectorias no proporcionan un test de significación ni prueban que el timing original carezca de información.

Las cinco U ganan más neto que sus R emparejadas, con107–129 trades y exposición temporal39,92–51,33%. Su exposición media y su proxy nocional-tiempo son unas cuatro veces los deR. También aparecen DD mayores y más fricción. No se concluye que eliminar el régimen sea una mejora causal o apropiada para cartera.

Los pares R/U comparten13/20/15/11/15 fills efectivos por seed. En ellos el PnL normalizado coincide hasta ruido numérico, coherente con misma gestión y precio. Las diferencias globales provienen de trayectorias con entradas/ocupación distintas y de tamaños endógenos. Una entrada perdida estando ocupado no se trata como trade hipotético.

No se selecciona U05, R04 o cualquier seed ganadora. La variación entre U02 (+37,11) yU05 (+3.873,54) importa tanto como su media. Las mismas fechas, familias y precios se reutilizan: N agregado no es una muestra independiente.

## Fricción y concentración

Recargos estáticos sobre TODOS los fills: otros 5/10 bps RT son 2,5/5 bps por lado, conservando tamaños y decisiones. No son backtests con nuevo sizing.

| ID | Fees | Neto +5 bps RT | Neto +10 bps RT | Sin mejor trade | Sin tres mejores trades |
|---|---:|---:|---:|---:|---:|
| C0 | 246,61 | 409,11 | 272,10 | -91,39 | -920,55 |
| Cq | 246,61 | 409,11 | 272,10 | -91,39 | -920,55 |
| E1 | 245,33 | 354,88 | 218,58 | -143,00 | -967,84 |
| E2 | 100,77 | 4269,45 | 4213,47 | -793,93 | -798,42 |
| E3 | 98,18 | 3614,82 | 3560,27 | -1215,54 | -1055,09 |
| E4 | 312,57 | -548,01 | -721,66 | -618,49 | -1034,21 |
| M | 267,72 | 813,39 | 664,66 | 337,45 | -635,13 |
| R01 | 208,00 | -6,60 | -122,16 | -248,62 | -918,76 |
| R02 | 201,68 | -266,03 | -378,07 | -510,43 | -1053,13 |
| R03 | 192,82 | 762,04 | 654,91 | 413,86 | -286,14 |
| R04 | 189,65 | 1147,07 | 1041,71 | 715,94 | -121,08 |
| R05 | 228,92 | -79,32 | -206,50 | -318,74 | -827,78 |
| U01 | 794,07 | 2461,17 | 2020,02 | 2297,83 | 1254,13 |
| U02 | 685,50 | -343,72 | -724,55 | -538,41 | -1550,79 |
| U03 | 840,26 | 2144,28 | 1677,47 | 1784,49 | 429,95 |
| U04 | 863,97 | 1187,04 | 707,06 | 1035,91 | -89,24 |
| U05 | 932,11 | 3355,70 | 2837,86 | 3159,95 | 1892,66 |

“Sin tres mejores” excluye tres operaciones por mayor PnL neto, incluso si alguna es pérdida. E3 tiene una sola ganadora: por eso quitar tres mejores puede resultar menos negativo que quitar sólo la mejor. No equivale a eliminar tres ganadores inexistentes.

Dos R y cuatro U conservan neto positivo con otros10bpsRT. M conserva neto positivo y337,45 USDT positivos sin su mayor ganador, pero −635,13 sin tres mejores. Tres U conservan neto positivo al quitar sus tres mejores; esto describe concentración, no valida esos clocks como estrategia. No se exige mecánicamente a todo seguidor de tendencia sobrevivir sin runners.

## Calendario MTM verificado por root

Se leyó completo strategies/MultiAssetRetestBtcShort4h/reports/ATTRIBUTION_MTM_RESULTS_20261019.md y se comprobaron IDs de las 17 sesiones. Root reconstruyó cierres diarios UTC con fills/precios anclados; la curva00:01 no se usa como cierre. La siguiente tabla conserva períodos completos:61 meses y 19 trimestres.

| Cuenta | Meses positivos / activos completos | Positivos /61 calendario | Trimestres positivos /19 | DD diario UTC |
|---|---:|---:|---:|---:|
| C0 | 15/31 | 15/61 | 8/19 | -6,922% |
| Cq | 15/31 | 15/61 | 8/19 | -6,922% |
| E1 | 15/31 | 15/61 | 8/19 | -7,407% |
| E2 | 22/37 | 22/61 | 9/19 | -10,674% |
| E3 | 19/37 | 19/61 | 6/19 | -14,748% |
| E4 | 11/30 | 11/61 | 6/19 | -6,294% |
| M | 17/31 | 17/61 | 10/19 | -7,650% |

Las cinco U tienen32/26/30/29/28 meses completos positivos de 61, y 10/8/10/9/12 trimestres de 19. Sus meses activos completos son 61/59/60/60/60. Los conteos diarios y el drawdown del motor permanecen separados; no se elige la medida más favorable.

M mejora descriptivamente dos meses y dos trimestres frenteC0, con más DD. E2 añade meses positivos a través de mayor duración, con fuerte dependencia del runner terminal. Los objetivos de regularidad son de cartera; aquí no se suman cuentas ni se simula una integración nueva. Cohortes por año de cierre, presentes en las auditorías, no sustituyen este MTM.

## Estado de la investigación

Se identifica una contribución material del payoff y de la permanencia long, y una evidencia limitada sobre el valor incremental del retest como selección de entrada. Las comparaciones no separan completamente exposición y selección, y cinco seeds no forman un contraste confirmatorio. El estudio evita atribuir toda ganancia a los indicadores o declarar mejor política por su mayor total.

M queda como una pregunta concreta sobre participación/ejecución; E2/E3 como controles de duración y convexidad; U como exposición sin régimen bajo clocks fijos. Ninguna se promueve ni sustituye a la referencia. Todo2020–2025 sigue siendo desarrollo seleccionado. No se abre 2026.

## Auditoría, incidencias y persistencia

976 registros de trades entre 17 cuentas, con solapamiento económico entre políticas; no son 976 observaciones independientes. Cantidades,fees,PnL,wallet y cierres terminales conciliados. Root verificó 34/34 fuentes/snapshots/formularios del estudio de ambos activos y su MTM. Todos los fulls PAXG terminaron y todos los análisis propios terminales.

Incidencias sólo de análisis/reporting: primer comparador de paridad trató color de equity como float; se corrigió comparación de metadata sin rerun deC0. Los primeros resultados A/B excedieron el tamaño de texto recuperable; se separaron resúmenes y archivos por par/política. No se parseó texto truncado, no se usó fallback de FS/red y no se cambió ninguna política. Jobs PASS completos: paridad a15c9d66b73d4bd8b57c5cde76d1993d, auditoríaA2527826629b9451ab234f9c1a7606bdf, auditoríaB29403a45aa424ef5a4a19bdfb4176737.

Todos los siguientes informes están dentro del proyecto de la máquina que ejecuta Jesse:

- strategies/R40PaxgKalmanInnovation4h/reports/ATTRIBUTION_PAXG_PROTOCOL_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_IMPLEMENTATION_REVIEW_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_C0_PARITY_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_SESSION_REGISTRY_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_EXACT_TABLE_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_BATCH_A_AUDIT_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_BATCH_B_AUDIT_20261019.md
- strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_ANALYSIS_SOURCE_20261019.md

Referencia, benchmark histórico, candidata anterior, BTC y 2026 intactos. Esta etapa de atribución no deja corridas o tareas económicas adicionales pendientes.
