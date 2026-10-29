# PROTOCOL_R63: última fábrica, universo completo USDT-M de Binance (con deslistadas)

**Fecha:** 2026-10-29. **Rama:** `exploration/gpt-6.1-sol`. **Código:** `research_scripts/r63*.py`, que reutiliza `r62_*`.

Este protocolo y la partición `data/r63/partition.json` se commitean **antes de bajar una sola vela**. Hasta ese momento solo se leyeron nombres de archivos del listado S3.

## 0. Decisiones del usuario y presupuesto
- **Último intento de la fábrica.** Si nada pasa el embudo, la búsqueda de un segundo motor se cierra y r64 pasa a la robustez operativa de P-r55 (opción 1 de `HANDOFF_R63.md`).
- **Único dato nuevo:** velas de 1 h y funding de los perpetuos USDT-M de `data.binance.vision`, **incluidas las deslistadas** (lo confirmó el usuario: es para evitar el sesgo de supervivencia).
  - No se usa DVOL, vol implícita, OI ni datos pagos.
  - El funding se usa solo como costo.
- **Sin proponente LLM.** En r62 aportó el 6% de las evaluaciones y ninguna élite, costó ~85 mil tokens por generación y ~5 h de espera, y es un canal de conocimiento previo. Sin él, la calibración y la corrida real son exactamente el mismo procedimiento automático.
- **Contadores:**
  - N global = 155 al empezar; suma +1 por finalista que entra al embudo (≤ 5) y +1 por la prueba `voljump` (§7.4).
  - N_fab = 1.614 al empezar; suma +1 por programa único evaluado sobre datos reales. **Techo de r63: 2.000 programas nuevos.** La calibración no suma.
- **Oráculo:** quedan 4 consultas y r63 usa **como máximo una** (q5, §7.5).
- **Datos reservados:** 2025 sellado y 2026 reservado. No se baja ningún mes posterior a 2024-12 y toda barra ≥ 2025-01-01 se descarta.
- **Cómputo:** nativo en Windows (`C:\Python312\python.exe`, con `-P` para leer datos bajados), con multiprocessing. Nada en Docker. Sin live ni paper.

## 1. Universo y partición (F0a)
1. **Listado** (`r63_list.py`): prefijo S3 `data/futures/um/monthly/klines/`, con paginación. Da 1.056 prefijos (`data/r63/listing_raw.json`).
2. **Filtro** (`r63.universe`):
   - nombre `^[A-Z0-9]+USDT(_?SETTLED)*$`, es decir, perpetuos USDT-M, incluidos los contratos archivados como `…SETTLED` tras un deslistamiento;
   - fuera los índices y estables: BLUEBIRD, BTCDOM, DEFI, FOOTBALL y USDC (TUSDT es el token Threshold y queda);
   - con algún mes de velas de 1 h ≤ 2024-12;
   - **fuera U50** (50 símbolos, incluidos BTC y ETH: muy vistos en r52–r61 y con sesgo de supervivencia);
   - **fuera H = N2 ∪ N3** (50 símbolos, el oráculo de r59): ni se bajan.
3. **Universo r63: 295 símbolos.** Por año de alta: 2020: 25; 2021: 27; 2022: 13; 2023: 99; 2024: 131. **28** dejan de tener archivo antes de 2024-12.
4. **Partición** (`r63.py partition`, semilla 63). Se estratifica por año de alta × (archivo termina antes de 2024-12), y en cada estrato 2/3 van a desarrollo:
   - **D63 = 197 símbolos** (desarrollo: la fábrica solo ve estos);
   - **L63 = 98 símbolos** (holdout local fresco);
   - sha256 `6b3661ea1a555345f5c2159411bd569c28620f9115f09a78d1e4469dd5cdc590`, verificado en cada carga.

## 2. Datos (F0b, `r63_data.py`)
- **Descarga:** velas mensuales de 1 h y funding, de 2020-01 a 2024-12, con verificación `.CHECKSUM` (`r52_download.zip_frame`). Los ZIP no se guardan (se procesan en memoria). Salida en `data/r63/bars/<SYM>.npz` (gitignored) y `data/r63/manifest.json` con sha y cobertura.
- **Limpieza:**
  - orden por tiempo y sin duplicados;
  - una barra con precio ≤ 0 o no finito se descarta;
  - las barras finales de volumen 0 (archivo que sigue publicando un contrato muerto) se recortan: **la vida del símbolo termina en su última barra con volumen > 0**;
  - **huecos ≤ 24 h:** se rellenan con barras planas (O = H = L = C = cierre previo, volumen 0);
  - **huecos > 24 h:** parten el símbolo en **tramos** independientes. Cada tramo es un activo para el motor; la antigüedad (§2, elegibilidad) se cuenta desde la primera barra del símbolo.
- **Fin de tramo:**
  - si el tramo termina antes de 2024-12-24 (deslistamiento o parada), la posición abierta se cierra **al cierre de la última barra, con fee taker + 100 pb de slippage**, sin aviso previo;
  - si termina en el corte (≥ 2024-12-30), se cierra al último cierre con los costos normales.
  
  En r62 el motor descartaba el trade abierto al final de los datos. En r63 se contabiliza siempre.
- **Elegibilidad (causal, por día UTC):** un activo puede **abrir** una posición en el día d solo si:
  - tiene ≥ 90 días desde la primera barra del símbolo;
  - la mediana del volumen diario en USDT de los 30 días completos anteriores a d es ≥ 2 M USD.
  
  No usa retornos. Una posición abierta se maneja hasta su salida aunque el activo deje de ser elegible.
- **Slippage taker por activo**, según esa misma mediana de 30 días al momento de la entrada:
  - ≥ 50 M → 5 pb;
  - 10–50 M → 10 pb;
  - < 10 M → 20 pb.
  
  (El plan hablaba de «tercil de volumen»; se fijan cortes absolutos para no depender del resto del corte transversal.) Fees: taker 0,045% y maker 0,018%, como r62.
- **Funding real** en las horas de liquidación, como costo.
- **Ventana de desarrollo:** de 2020-01-01 a 2024-12-31.
- **Reporte F0** (`R63_PHASE0_*.md`) antes de cualquier evaluación:
  - símbolos elegibles por año en D63 y L63;
  - tramos;
  - deslistamientos dentro de la ventana;
  - huecos.

## 3. DSL (`r63_dsl.py` sobre `r62_dsl.py`)
- **Universos:** `alts_1h` y `alts_1d` (los símbolos de D63; cada tramo es un libro y la canasta es la media diaria de los activos activos ese día).
  - **Activo activo:** elegible ese día o con una posición abierta.
  - Cada trade sigue dimensionado a 10% de vol anual (`voltgt`), así que la canasta es a igual riesgo.
- **Catálogo:** las grillas de r62 sin:
  - `spread_z` (no hay pares);
  - `cascade` (no hay OI);
  - el evento `cme_gap` de `clock` (no aplica a alts).
  
  Quedan `zrev`, `rsi2`, `shock`, `voljump` y `clock` (`funding_hour`, `month_end`) como señales; `volreg`, `trendveto`, `session` y `btcstate` como filtros; salidas `time`, `atr` y `mean`; `voltgt` con lado; ejecución taker o maker. Valen los mismos topes (4 piezas, 6 parámetros) y la misma regla de segunda señal.
- **Restricciones:** en `alts_1d` no hay `clock` ni `session`; `funding_hour` solo en `alts_1h`.
- `btcstate` usa el estado T90 de BTC de r55 (`data/r55/f0_states.npy`), como en r62. BTC no se opera.

## 4. Evaluador
- **Pliegues:** año (2020…2024) × 3 grupos fijos de símbolos (grupo = `int(sha1(símbolo)[:8], 16) % 3`). Son 15 pliegues.
  - Un pliegue cuenta con ≥ 10 trades.
  - Se necesitan ≥ 5 pliegues válidos.
- **Nota** = Sharpe del peor pliegue válido − 0,05 · complejidad (como r62).
- **Puertas de archivo:**
  - e1: costos ×2 y maker con 2 pb, Sharpe > 0;
  - e2: ΔSharpe de 0,85·P55 + 0,15·x̃ contra P55 > 0;
  - e3: rotación con 200 desfases (semilla 63), p < 0,10.
- **Casilleros:** los 27 de r62 (ρ con `BENCH_R1_long` × tenencia × dirección), con las 3 celdas «largo, ρ > 0,3» bloqueadas.

## 5. Búsqueda (F2, `r63_run.py`)
- **Semillas:** 20 programas al azar del DSL (semilla 63).
- **Generaciones:** 10, de **160 evaluaciones** cada una. La búsqueda genética sobre las élites usa:
  - mutación a un vecino de la grilla (60%);
  - cambio de pieza (25%);
  - cruce dentro de la misma fila de ρ (15%).
  
  Ningún hash se repite. Se completa con programas al azar si la vecindad se agota (regla E4 de r62).
- **Total ≈ 1.620 programas;** se corta a los 2.000.
- Un solo proceso nativo corre todo de punta a punta. Las evaluaciones de cada generación se reparten en un pool de procesos, y el resultado no depende del número de procesos (semillas fijas por generación).
- **Registro:**
  - cada evaluación va a `data/r63/runs/<run>/log.jsonl`;
  - las series reales van al almacén de r59 (`data/r59/series/r63.npz`, ids `R63_P_<hash10>`, float32, con sha), por lotes al cerrar cada generación;
  - N_fab se escribe en `TRIAL_REGISTRY.json → factory_trials`.
- **Finalistas:** como máximo 5, con la regla de r62 (la élite de mayor nota por celda no bloqueada, una por combinación de tenencia y dirección).

## 6. Calibración (F1, N + 0)
- **Generadores** (`r63_synth.py`), sobre el panel D63 con su misma disponibilidad, volumen y funding, de modo que elegibilidad y costos sean idénticos:
  - **ruido:** vol real de 1 h (EWMA de 24 barras, sin anticipar) × shocks estandarizados. Los shocks se toman de una única permutación de las horas, compartida por todos los activos (conserva la correlación contemporánea). Si el activo no tenía barra en la hora de origen, se toma un shock propio al azar. Media 0. H/L salen del rango relativo de la barra de origen;
  - **plantado:** el ruido más **P1** (reversión tras un shock) **solo en el 20% de los símbolos de D63** (elegidos con la semilla 6300): después de |z| > 2,5, las 6 barras siguientes derivan −κ·z/6.
- **κ se calibra antes de correr la fábrica,** con semillas aparte (6301–6306): es el valor de la grilla {0,1, 0,15, …} con el que el programa oráculo da un **Sharpe neto medio de 0,8 ± 0,1 en la canasta `alts_1h`**.
  - Programa oráculo: `shock` fade z 3, sin filtros, salida `time` 6, lado both, maker off 0,25 y vida 1.
  - Es el caso que r62 no detectó: una ventaja moderada concentrada en pocos activos.
- **Corridas:** ruido con semillas 631 y 632; plantado con 633 y 634. Mismo presupuesto que §5.
- **Pasa si:**
  - **C1:** en las dos de ruido, ningún finalista tiene SPA p < 0,05 (contra cash y marginal);
  - **C2:** en las dos plantadas aparece un finalista con señal `shock` fade en `alts_1h` y SPA p < 0,05 en ambos.
  
  Si una semilla falla y la otra pasa, decide una tercera (635 o 636). **Si la calibración falla, la fábrica no corre sobre datos reales y r63 cierra negativa.**
- **Descriptivo:** el mejor Sharpe en desarrollo que da el ruido a esta escala.

## 7. Embudo (F3); se corta en el primer escalón que falla
1. **SPA** (`r62_eval.spa_fast`, bloque 20, 2.000 réplicas, semilla 63) sobre **todas** las series reales de r63, con (a) contra cash y (b) marginal reescalado (E3 de r62).
   - Pasa con p < 0,05 en ambos **y** si es la columna del máximo o su t supera el umbral del 5% del máximo bootstrap.
   - **Puertas r49:**
     - DSR ≥ 0,95 con N = 155 + finalistas (también se reporta con + N_eff);
     - Sharpe ≥ 0,8;
     - ≥ 100 trades (30 si es diaria);
     - los 5 mejores trades < 60% del PnL.
2. **PBO** (`r60.pbo_cscv`, S = 16) sobre las élites del archivo: < 0,5.
   - **Filtro sintético** de «regímenes» (bootstrap de días completos de todo el panel, bloque medio 20, 200 historias, semilla 63): se descarta si la mediana del Sharpe es ≤ 0 o si el Sharpe real supera el p95.
3. **Holdout local L63** (programa congelado, mismos datos, costos y elegibilidad, 2020–2024).
   - **Antes de mirar L63** se escriben en `data/r63/l63_power.json`:
     - N_eff de L63 = razón de participación de los autovalores de la correlación de las series por activo del programa en D63, escalada por 98/197;
     - EE_L = EE bootstrap del Sharpe en D63 × √(N_eff_D / N_eff_L);
     - **poder** = Φ((½·S_D − 1,645·EE_L)/EE_L).
     
     Si el poder es < 0,4, se informa al usuario y se decide con él antes de mirar.
   - **Pasa si:**
     - Sharpe de la canasta > 0;
     - p bootstrap unilateral < 0,05 (estacionario, bloque 20, 2.000 réplicas);
     - ≥ 3 de los 5 años con Sharpe positivo.
   - **Advertencia:** mismos años y alta correlación con BTC. L63 prueba amplitud transversal, no tiempo nuevo.
4. **Prueba preregistrada de `voljump` (N + 1; se corre aunque la fábrica no deje finalistas).**
   - El finalista de r62 de mayor nota, `1521f048…`, congelado tal cual salvo el universo:

     `voljump` follow ratio 1,5 · filtro `session` us · salida `time` 24 · lado long · taker.
   - Se corre en `alts_1h` sobre **L63**, con el mismo criterio y el mismo cálculo de poder del paso 3. Su S_D es el Sharpe de r62 en BTC/ETH (1,53).
   - **Descriptivo, sin peso:** el mismo programa sobre D63, que la fábrica también ve, pero sin haberlo elegido ahí.
5. **Oráculo (q5, como mucho 1 consulta).** Solo si un finalista pasa 1–3, o si `voljump` pasa 4.
   - Cálculo: programa congelado en `data/r63/q5_program.json`, sobre las 50 alts de H a 1 h, de 2021-07-02 a 2024-12-31, con los costos de §2.
   - Márgenes, como q4:
     - (a) Sharpe − 0,3;
     - (b) Sharpe con costos ×2;
     - (c) ΔSharpe 0,85·P55 + 0,15·x̃ contra P55.
   - Poder previo Φ((½·S_D − 0,3)/EE) ≥ 0,4.
   - El criterio q5 se agrega a `r59_criteria.py` y se commitea antes de la consulta. Si hay varios candidatos, va el de mayor nota.
- **Resultado:**
  - Un candidato que pase q5 se propone como «P-r55 + programa» (15% a igual vol), **sujeto a la aprobación del usuario**.
  - Si nada pasa, P-r55 queda igual y la búsqueda se cierra.

## 8. Selftests (F0b, `r63.py selftest`)
1. **Elegibilidad sin anticipación:** alterar las barras ≥ d no cambia la elegibilidad del día d.
2. **Fin de tramo:**
   - una posición abierta en la última barra de un tramo deslistado se cierra a su cierre con taker + 100 pb;
   - en el corte, se cierra con los costos normales.
3. **Datos:**
   - ninguna barra ≥ 2025-01-01;
   - ningún símbolo de U50 ni de H en `data/r63/bars/`;
   - D63 ∩ L63 = ∅ y el sha de la partición coincide.
4. **Selftests de r62 que aplican:** parser (el catálogo r63 rechaza `spread_z`, `cascade` y `cme_gap`), maker sin anticipación y `spa_fast` = `r59.spa_pvalue`.
5. **Benchmark:** tiempo por programa y uso de CPU y memoria (`psutil`) antes de F1. Si una generación tarda más de ~30 min con el pool disponible, se avisa al usuario antes de seguir.

## 9. Advertencias declaradas
1. **Mismos años que todo lo anterior (2020–2024).** El universo es nuevo y el tiempo no; la correlación de las alts con BTC reduce la amplitud efectiva.
2. **El universo r63 es lo que dejaron U50 y H.** H tomó alts listadas antes de 2022-07 y vivas, así que r63 tiene muchas altas de 2023–2024 (230 de 295) y pocas monedas viejas. Los primeros años tienen pocos activos.
3. **El deslistamiento sin aviso es conservador:** en la práctica Binance avisa con días de anticipación.
4. **El maker sigue simulado con barras de 1 h,** sin libro ni cola. En alts finas es optimista, y por eso e1 exige Sharpe > 0 con costos ×2.
5. **Poder:** el SPA es conservador a propósito. El resultado negativo descarta ventajas que la calibración C2 sí detecta, no cualquier ventaja.

## 10. Enmiendas

### E1 (2026-10-29, en F1, decisión del usuario, antes de cualquier corrida de la fábrica)
1. **P1 se planta en el 100% de D63, no en el 20%.**
   - Con el 20%, el programa oráculo no pasa de un Sharpe medio de 0,40 en la canasta, aunque la ventaja por moneda sea enorme (κ = 1,2; grilla de 0,1 a 1,2 en `data/r63/f1_kappa_share20.json`).
   - El DSL opera la canasta entera y no puede elegir monedas, así que el 80% sin ventaja solo suma costos. Con eso, el objetivo de 0,8 del §6 era inalcanzable y C2 no podía pasar.
   - **Hallazgo declarado:** esta fábrica no puede detectar una ventaja que vive en una minoría de monedas. Solo ve ventajas amplias. El resultado de r63 no habla de ventajas concentradas.
2. **κ:** con el 100%, la grilla original da 0,45 en κ 0,15 y 1,51 en κ 0,20. Se afina entre ambos (0,16 a 0,18, mismas semillas 6301–6306), y la regla del §6 elige **κ = 0,165**, con un Sharpe medio del oráculo de **0,77** (`data/r63/f1_kappa.json`).
3. **C2** sigue exigiendo un finalista con `shock` fade en `alts_1h` y SPA p < 0,05 en las dos semillas plantadas.
