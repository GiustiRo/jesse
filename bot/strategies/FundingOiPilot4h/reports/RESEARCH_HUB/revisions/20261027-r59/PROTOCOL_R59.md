# r59: protocolo preregistrado. Validación reutilizable sobre el universo actual

El usuario aprobó el plan el 2026-10-27 y pidió ejecutar F0 y reportar al cerrarla. Las fases siguientes se ejecutan con la misma aprobación, reportando al cierre de cada una.

Este archivo se commitea **antes de escribir o correr cualquier código de r59**. Un cambio posterior es una variante nueva, que suma N, o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones

### Base, contadores y cortes
- **Base:** P-r55 congelada (`../20261026-r55/P55_FREEZE.md`): Sharpe 1,677 en 2018-09→2024 y 1,723 en 2021–24.
- **N = 145 al empezar. Techo de r59: 146.** Solo la consulta q1 al oráculo (F2) suma 1. F0 y F1 no suman.
- **N_régimen sigue en 38. N_temática sigue en 19:** la partición V5a × V1 ya se contó en r58 F1 (D condicional a V1), y la validación cruzada de F0 vuelve a cruzar V1–V6 sobre las mismas alts de U50.
- **Cortes:**
  - corte duro el 2024-12-31, con aserciones;
  - 2025 sellado y 2026 reservado. Los 544 trades de 2025 de `data/r52/v1_events.json` se descartan al cargar;
  - sin live, paper ni Pi. No se baja ninguna moneda nueva.

### Universo fijo
- **Desarrollo (D):** las 48 alts de U50 (`data/r52/universe50.json` sin BTC/ETH). Usadas en r52–r58.
- **Holdout (H):** N2 ∪ N3, 50 monedas (`data/r56/n2/universe_n2.json → selected` y `data/r58/n3_panel.json → n3_syms`). El sha256 de la lista ordenada queda en `data/r59/holdout.json`.
- **Por qué H no es una partición nueva de 1/4 sobre las 98:**
  - una partición que incluya alts de U50 está contaminada para las preguntas pendientes, porque el efecto del funding se descubrió ahí;
  - 1/4 serían ~25 monedas y ~950 trades, contra 1.847 en N2 ∪ N3, con menos poder todavía que el 0,30 de r58.
- **Advertencia declarada:** H **no es virgen para C6**. r58 F2 ya la usó (consulta q0, con los resultados revelados). Lo que r59 agrega es la protección de acá en adelante y la contabilidad explícita de cada consulta.

## 1. F0: infraestructura (N + 0)

### 1.1 Guarda del holdout (`research_scripts/r59_holdout.py`)
- **Rutas protegidas:**
  - `data/r56/n2/` y `data/r58/n3/` (velas 1h y funding);
  - `data/r58/f0_bars_n2.npz`, `f0_bars_n3.npz`, `pred_n3_P5_range40.npy` y `f2_trades_n2n3.csv`;
  - `data/r56/panel70.npz`, `labels70.npz`, `panel_n3.npz`, `labels_n3.npz`, `feat_*_70.npz`, `feat_*_n3.npz`, `chronos_*_panel70.npy` y `pred_n2_*.npy`.
- **Bancos protegidos:** `n2` y `n3` en los loaders de r58 (`banks`, `load_bank`, `h4_bars`, `c6_bank`, `make_gate`, `trade_table`).
- **Mecanismo:** `install()` envuelve `builtins.open` (cubre `np.load` y `pd.read_csv`) y esos loaders. Fuera del contexto del oráculo, tocar algo protegido lanza `HoldoutAccess`. Los scripts de r59 llaman a `install()` al importarse. `r58.py` no se modifica.
- **Límite declarado:** es una guarda contra accidentes, no contra quien lea un archivo a mano. La protección real es el protocolo commiteado antes de cada consulta, más el log append-only.

### 1.2 Oráculo (`research_scripts/r59_oracle.py`)
- **Consulta:** `r59_oracle.py query <qid>`. El criterio es una función registrada en `research_scripts/r59_criteria.py` bajo ese qid. Se rechaza la consulta si:
  - el árbol de git tiene cambios en `research_scripts/r59*.py` o en este protocolo (no commiteados);
  - el qid ya figura en el log;
  - el presupuesto está agotado.
- **Cálculo:** el criterio devuelve una lista de márgenes `m_i = estadístico_i − umbral_i` y la escala `s_i` de cada uno, el error estándar bootstrap o equivalente. A cada margen se le suma ruido Laplace(0, 0,1·s_i).
  - **Semilla:** `sha256(commit_HEAD + qid)`. La misma consulta da siempre la misma respuesta, así que volver a preguntar no sirve.
  - La consulta pasa si todos los márgenes con ruido son mayores que 0.
- **Salida:** solo `PASA` o `NO PASA`.
  - Los estadísticos completos, los márgenes y el ruido quedan en `data/r59/oracle_sealed/<qid>.json`, gitignored y con su sha256 en el log.
  - **Se abren solo cuando el holdout se retire** (presupuesto agotado) **o con autorización del usuario.**
- **Log append-only:** `RESEARCH_HUB/holdout/ORACLE_LOG.jsonl`, commiteado, más la sección `holdout_oracle` de `TRIAL_REGISTRY.json`. Cada línea guarda qid, fecha UTC, commit, sha256 del protocolo, criterio, α, respuesta y sha256 del archivo sellado. Ninguna línea se edita ni se borra.
- **Presupuesto de H:** 5 consultas.
  - **q0 = r58 F2,** registrada hacia atrás: α unilateral 0,10, PASA, sin ruido y con todo revelado.
  - **q1–q4:** α unilateral 0,05 cada una. El α acumulado máximo es 0,30. Es una disciplina de cribado, no un control formal de FWER; el DSR con N sigue siendo la cuenta conservadora.
- **Sobre Dwork y otros (2015):** sus garantías no valen a esta escala. Las monedas están correlacionadas por la beta cripto, el n efectivo es chico y las consultas no son promedios i.i.d. Se toman tres piezas operativas como disciplina: respuesta binaria, ruido sobre el margen y presupuesto finito con un log.
- **Selftest (sin tocar H):** un holdout falso de 12 alts de U50 elegidas con semilla 59 y armado con `f1_trades_u50.csv`. Tiene que pasar:
  - **(i)** con ruido 0, la respuesta coincide con el cálculo directo en tres criterios: uno trivialmente verdadero, uno trivialmente falso y D(V1 ∧ V2) con p10 > 0;
  - **(ii)** la misma consulta da la misma respuesta;
  - **(iii)** se rechaza una consulta repetida, una fuera de presupuesto y otra con el árbol sucio;
  - **(iv)** el log solo crece.
- **El selftest escribe en un log temporal, nunca en el real.**

### 1.3 Validación cruzada por grupo × año (`r59.py cv`, solo D)
- **Grupos:** 6 grupos de 8 alts de U50. Se ordenan por `vol24h` de `universe50.json`; cada sexteto consecutivo reparte una moneda a cada grupo, con permutación de semilla 59. La lista va a `data/r59/cv_groups.json` y se commitea antes de calcular. Se reporta el balance de `onboard` por grupo.
- **Pliegues:** 24, de grupo g × año y en {2021, …, 2024}.
  - **Entrenamiento:** los trades con moneda ∉ g **y** año ≠ y.
  - **Prueba:** los trades con moneda ∈ g **y** año = y.
  - Así se bloquean los shocks comunes de tiempo. Una validación cruzada solo entre monedas sobreestimaría la generalización.
- **Procedimiento dentro de cada pliegue:** la regla de selección de r58 F1, como código:
  - `r58.sweep` sobre V1–V6, con la elegibilidad del §2 de r58 y a lo sumo 3 variables;
  - el AND de las seleccionadas, o la mejor sola si el AND retiene menos del 25%.
  - **Adaptación declarada:** la regla 2 («D > 0 en ≥ 3 de 4 años») pasa a «≥ 2 de los 3 años de entrenamiento».
  - Para que el cómputo sea viable, el bootstrap usa 1.000 réplicas, con semilla 59 + el índice del pliegue.
- **Salida:**
  - por pliegue: las variables seleccionadas y el D de la regla en el pliegue de prueba;
  - en total: la frecuencia de selección de cada variable, y la mediana, la media y la fracción de pliegues con D > 0 fuera del pliegue (sobre pliegues con al menos 10 trades en cada clase).
- **Validación de la herramienta:** si el procedimiento de r58 es estable, V1 o V2 tienen que salir elegidas en al menos la mitad de los pliegues. Se reporta lo que salga, sin reinterpretar.

### 1.4 Prueba de rotación (`r59.py rotation`)
- **La permutación por moneda × semana del plan original se descarta.** Solo el 0,5–1% de los trades cae en una moneda-semana con etiqueta mixta (V1: 22/1.910 en U50 y 9/1.847 en N2 ∪ N3). Esa prueba no puede rechazar.
- **Rotación:** se trabaja por moneda, sobre la serie de la variable en su grilla nativa (diaria para V1 y V2; de velas 4h para V3–V6), restringida al tramo donde la variable existe. Se corre en forma circular un desfase uniforme entre 90 días y el largo del tramo menos 90 días, se reasigna la etiqueta a cada trade según su señal y se recalcula el estadístico.
- **Estadísticos:**
  - D, como en r58;
  - D condicional, que rota solo la variable probada y deja V1 fija.
- **Parámetros:** 2.000 rotaciones con semilla 59. **p = (1 + #{estadístico rotado ≥ observado}) / 2.001.**
- **Validación con placebos:** 200 variables placebo por moneda, cada una una cadena de Markov de dos estados con la persistencia media de V1, evaluadas con 500 rotaciones cada una. La fracción con p < 0,10 tiene que caer en [0,05, 0,15].

### 1.5 Almacén de series (`data/r59/series/`)
- **Formato:** `<ronda>.npz` con claves `<trial_id>__days` (ms UTC) y `<trial_id>__ret` (retorno diario simple). Un `manifest.json` guarda el sha256 por archivo, la ventana y el script que la produjo.
- **Registro:** cada ensayo de `TRIAL_REGISTRY.json` con serie recibe `series: {file, key, sha256}`.
- Desde r59, toda variante económica guarda su serie al correr.

## 2. F1: auditoría SPA/PBO de P-r55 (N + 0)
- **Reconstrucción:** las variantes de r50 a r58 con un entrypoint determinista en `research_scripts/`.
  - Antes de nada, una aserción reproduce P-r55 en 1,677 / 1,723 (±0,0015) con `r57.p55_base`.
  - Se reporta la cobertura sobre 145. Los ensayos anteriores a r50 eran sesiones Jesse con otros objetivos y quedan fuera de la familia.
  - **Antes de calcular cualquier SPA o PBO,** la lista de ids por familia, que se arma solo con el registro y sin mirar series, se commitea en `data/r59/spa_families.json`.
- **Familias:**
  - **P (cartera):** P1 y P-r55, y toda variante evaluada como cartera P1/P-r55 modificada, de r50 F2 a r58 F3;
  - **S (mangas):** mangas y libros evaluados por separado.
- **Ventanas:** 2021-01-01→2024-12-31 en todas. 2018-09→2024 en las que tengan serie completa.
- **Pruebas:**
  - **SPA de Hansen (SPA_c)** con bootstrap estacionario (bloque medio de 20 días, 2.000 réplicas, semilla 59), sobre los retornos diarios. Se reutiliza la lógica de `r56_eval.spa_pvalue`. Hay dos varas: cash (diferencial = retorno) y R1 solo (diferencial = retorno − retorno de R1 escalado a la misma vol).
  - **PBO por CSCV** con S = 16 bloques sobre la familia P (`r50_f1d.pbo`).
- **Lectura preregistrada:**
  - SPA p < 0,10: la ventaja de la mejor variante no se explica por la selección.
  - PBO < 0,2 es bajo, de 0,2 a 0,5 es moderado y más de 0,5 es alto.
  - Es descriptiva: **no cambia P-r55.** Es un insumo para la decisión del usuario sobre 2026.
- **Verificación:** antes de la familia real, SPA y PBO se corren sobre una familia sintética de resultado conocido. Una con 30 series de ruido puro tiene que dar SPA p > 0,10 y PBO cerca de 0,5. Otra con una serie de Sharpe 2 entre 29 de ruido tiene que dar SPA p < 0,05.

## 3. F2: funding no saturado condicionado a la compresión (q1; N + 1 → 146)
- **Hipótesis:** dentro de las rupturas de C6 que salen de compresión (V1 = 1, es decir `persist_vol` = 0), las que ocurren con funding no saturado (V5a = 1) pagan más. En U50 r58 F1 dio +0,79 R [+0,31, +1,30].
- **Prefiltro en D, sin consultar al oráculo.** Se consulta solo si se cumplen las dos:
  - **(p1)** en la validación cruzada grupo × año, la mediana del D(V5a | V1 = 1) en los pliegues de prueba (con al menos 5 trades en cada clase) es mayor que 0;
  - **(p2)** la rotación de V5a, con V1 fija, sobre los trades de U50 con V1 = 1, da p < 0,20.
  - Si el prefiltro falla, F2 cierra sin consultar y N no se mueve.
- **Commit antes de la consulta:**
  - el criterio `q1` en `r59_criteria.py`;
  - el poder esperado: el EE bootstrap de U50 escalado por la raíz del cociente entre los trades con V1 = 1 en U50 y los esperados en H. Esos se estiman con la tasa de U50 por moneda-día con V1 = 1, contando solo las etiquetas diarias de H (`f0_days.npz`), sin trades. La lectura de esas etiquetas la hace el oráculo en modo `count`, que devuelve solo conteos y no consume presupuesto.
  - Si el poder contra la mitad del efecto es menor que 0,4, se le reporta al usuario antes de consultar.
- **Criterio q1 (α 0,05).** Sobre los trades de C6 congelado en H abiertos del 2021-07-02 al 2024-12-31:
  - **(a)** D(V5a | V1 = 1) > 0, con el percentil 5 del bootstrap de bloques semanales > 0 (5.000 réplicas);
  - **(b)** el Sharpe de la canasta con compuerta V1 ∧ V2 ∧ V5a es mayor o igual al de la canasta con la regla de r58 (V1 ∧ V2), con N2 ∪ N3 a igual peso;
  - **(c)** (a) y (b) con costos ×2.
  - Márgenes del oráculo: (a) p5 − 0, con escala el EE bootstrap; (b) la diferencia de Sharpe, con escala 0,1; lo mismo para (c).
- **Aunque pase, P-r55 no cambia.** Sumar alts a P-r55 ya restó tres veces (R54_W1, ML3 e I1). Pasar mejora la regla de C6 para un posible libro de alts aparte, y esa decisión es del usuario.

## 4. Advertencias declaradas antes de los resultados
1. **H ya se usó para C6** (q0, en r58). La consulta q1 sobre H no equivale a un banco virgen.
2. **U50 está muy usada** (r52–r58). La validación cruzada en D mide estabilidad, no generalización limpia.
3. **Sesgo de supervivencia** en U50, N2 y N3: solo monedas que siguen listadas.
4. **El SPA y el PBO cubren solo r50–r58.** La selección anterior a r50 no entra en la familia. El DSR con N = 145 es la cuenta conservadora.
5. **El presupuesto de H es finito.** Después de q1 le quedan 3 consultas.
6. **La F1 sobre BTC/ETH se descarta.** r58 F3 ya registró (descriptivo) ΔSharpe −0,13 / −0,20 y fallan g1, g2 y g4. Correrla de nuevo sería post hoc, y el oráculo de alts no responde por BTC/ETH.

## 5. Enmiendas
- **E1 (2026-10-27, en F0, antes de calcular cualquier cosa sobre V5a en r59). El estadístico de q1 es el de r58, no «D dentro de la compresión».**
  - El +0,79 R [+0,31, +1,30] de r58 F1 (`f1_diag.json → V5a.D_cond_V1`) es el **D condicionado a V1**: el promedio, ponderado por n, de los D de V5a dentro de cada estado de `persist_vol` (0, 1 y 2), calculado con `r58._cond`. No es el D restringido a los trades en compresión.
  - El texto del §3 («dentro de las rupturas que salen de compresión», «D(V5a | V1 = 1)») transcribe mal ese hallazgo. Se corrige así:
    - **hipótesis:** controlando por el estado de la vol pasada (V1), las rupturas con funding no saturado pagan más;
    - **(p1):** mediana del D condicionado a V1 en los pliegues de prueba de la validación cruzada. Cuentan los pliegues con al menos 5 trades de funding saturado (V5a = 0), porque esa clase es solo el 7% de los trades;
    - **(p2):** rotación de V5a con `persist_vol` fija, sobre todos los trades de U50 con V5a y `persist_vol` válidos, usando el D condicionado a V1 como estadístico;
    - **poder:** el EE bootstrap del D condicionado a V1 de U50, escalado por la raíz del cociente entre los trades de U50 con V5a y `persist_vol` válidos y los esperados en H. Se estima con la tasa de U50 por moneda-día con `persist_vol` válido;
    - **criterio (a):** el percentil 5 del bootstrap semanal del D condicionado a V1 es mayor que 0. (b) y (c) no cambian.
  - El D dentro de la compresión queda solo como descriptivo, sellado junto con q1.
- **E2 (2026-10-27, en F1, antes de reconstruir cualquier serie real). La verificación sintética del SPA/PBO pasa a 20 réplicas.**
  - **Por qué:** con una sola réplica, la familia de ruido dio SPA p 0,114 y PBO 0,26. Bajo la nula el p del SPA es casi uniforme y el PBO de un solo conjunto es ruidoso, así que un único valor no verifica la herramienta.
  - **Criterio nuevo, en 20 réplicas con 500 bootstraps cada una:**
    - con ruido puro, SPA p < 0,10 en a lo sumo el 20% de las réplicas, y PBO medio entre 0,35 y 0,65;
    - con Sharpe 2 entre 29 series de ruido, SPA p < 0,05 en al menos el 80% de las réplicas.
  - La auditoría real sigue usando 2.000 bootstraps con semilla 59.
- **E3 (2026-10-27, en F1, con las series reconstruidas y antes de calcular cualquier SPA o PBO). Cómo se arma cada matriz y cómo se reconstruyó cada serie.**
  - **Reconstrucción.** `r59_capture.py` registra cada llamada a las funciones de métricas con las variables locales del script (`cand`, `window`, `eng`, …). El mapa ensayo → curva (`r59.py: F1_P, F1_S`) se escribió leyendo esas llamadas y el código, no los valores de las series.
    - Cada entrada se verifica con el Sharpe que el script registró antes de 2025, que tiene que coincidir con el número commiteado del ensayo, o con las variables de la llamada.
    - Los libros medidos como dev 2021-05→2023 más validación 2024 (r52_xs, r53_xs, r55_ml y r52_q) se unen en el tiempo.
    - R57_Q1 y R57_Q2 se reconstruyen con `r59.py f1_q`, solo con U50. `r57 rev` arma el libro de N2 antes de evaluarlos, y la guarda lo corta ahí. Los Sharpe coinciden con `f4_rev.json` a 1e-4.
    - R52_F2_Q1 es una prueba de IC y no tiene serie: queda como faltante.
  - **Ventana 2021–24.** Se usa la intersección de los días que tienen todos los miembros. En P eso arranca el 2021-03-01; en S, donde empiece el miembro más tardío.
    - En S se agrega una sensibilidad sobre la unión de días: un día sin serie cuenta como retorno 0, porque esa estrategia estaba fuera del mercado (en cash).
  - **Ventana 2018-09→24.** Entran solo los miembros cuya serie larga empieza a más tardar el 2018-10-01. Sobre ellos se usa la intersección.
  - **Vara R1** (= P-r55 sin C6, `eg.portfolio({'R1'})`): P usa la R1 de su propia lente. S usa la R1 de la lente larga, porque es la única que cubre la ventana completa.
  - **Duplicados:** R55_F4_NOBOND y R55_F4_PFINAL son la misma serie por construcción. Los dos quedan en P, como se commiteó.
  - **Fuera de alcance:** el registro marca `fuera_de_alcance_spot` a R50_F1E_P3, R50_F1D_K1 y R50_F1E_K1r. Las dos últimas son carry de funding con Sharpe de 7 a 8, y dominan cualquier SPA contra cash.
    - La corrida principal es la familia como se commiteó.
    - Como sensibilidad, P y S se corren de nuevo sin esos tres.
  - **Recorte de inicio:** cada serie arranca donde la midió su script (`frm` de `en.metrics`). Por ejemplo, R54_M1 arranca el 2022-01-01, después de su año de entrenamiento.
