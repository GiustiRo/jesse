# r57: protocolo preregistrado. Usos continuos de los pronósticos de r56 sobre P-r55

El usuario aprobó el plan el 2026-10-26 y autorizó a ejecutar todas las fases de forma autónoma.
- Habilitó los usos continuos de los pronósticos de r56, como **enmienda del puente r56 → r57**.
- Los interruptores duros por régimen siguen descartados.
- U2 se descarta por separado: es U1 con otra forma.
- Refinar los detectores con los mismos datos diarios también queda fuera: F8 tocó el techo.

Este archivo se commitea antes de cualquier corrida de r57. Un cambio posterior es una variante nueva, que suma N, o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones
- **Base:** P-r55 congelada (`../20261026-r55/P55_FREEZE.md`), con Sharpe 1,677 en 2018-09→2024 y 1,723 en 2021–24.
  - Se reconstruye con `r51_lib.p1_components` sin el bono y se evalúa con `r55_engine.portfolio`/`evaluate`.
  - Toda corrida verifica primero que reproduce esas cifras.
- **Contador:** N de estrategias = 140 al empezar. **Techo de r57: 146.** N_régimen queda en 38: r57 no evalúa detectores nuevos.
- **Cortes:**
  - corte duro el 2024-12-31, con aserciones;
  - 2025 sellado y 2026 reservado;
  - sin live, paper ni Pi.
- **Pronósticos:** todos son los ya guardados por r56, calculados con datos hasta 2024-12-31. r57 no recalcula nada con torch.
  | Uso | Archivo | Contenido |
  |---|---|---|
  | Vol | `pred_T3_vol.npy` (34 monedas de desarrollo) y `pred_hold_T3_vol.npy` (16 del holdout, columnas 0–49 de panel70) | Probabilidades de T3 |
  | Rango a 40 días | `pred_P5_range40.npy` y `pred_hold_P5_range40.npy` | Probabilidades de P5 |
  | N2 | `pred_n2_*` | Probabilidades de T3 y P5 en las 20 monedas de N2 |
  | U1 | `chronos_chronos2cov.npy` | log-RV crudo de Chronos-2 con covariables |
  - Las probabilidades empiezan el 2021-07-01.
- **Regla anti-futuro (aplica a todo r57):**
  - El pronóstico de la fila del día d usa datos hasta el cierre UTC de d.
  - Una barra cuya hora de cierre es `ts` usa la fila `floor(ts / día) − 1`.
  - Hay una aserción en cada consulta: `day_ms[fila] + 1 día ≤ ts`.
- **Estado de vol T3:** las probabilidades se estabilizan con la histéresis de r56-B (`r56_eval.apply_picks(pred, 'hyst', picks)`), usando los parámetros trimestrales de T3 guardados en `data/r56/f8.json`, que ya estaban fijados.
  - Para el holdout se aplica la misma secuencia, igual que en F10.
  - **Clases:** 0 compresión, 1 media, 2 alta.
- **Vara de persistencia:** `persist_vol` de `labels.npz`, la vara de r56. Es la clase de la ventana de 20 días ya cerrada.
- **p(rango a 40 días):** la columna 1 de P5.
  - **Corte «alto»:** el cuantil 2/3 de p sobre las filas elegibles de las monedas de desarrollo, entre 2021-07-01 y 2023-12-31. Se calcula sin mirar trades ni retornos y se escribe en `data/r57/f0_cuts.json`.
- **Universos:**
  - **«48 alts»:** U50 sin BTC ni ETH, las de r54.
  - **N2:** las 20 de `data/r56/n2/universe_n2.json`. Ni C6 ni ninguna regla de r57 corrió nunca sobre ellas.
- **Advertencias declaradas antes de los resultados:**
  1. **Posible contaminación del preentrenamiento.** Chronos-2 (2025) pudo haber visto series cripto de 2021–24 al entrenarse, así que su «zero-shot» puede no estar fuera de muestra en sentido estricto. N2 no lo corrige; solo lo resuelve 2026.
  2. **U1 toca solo R1-BTC y R1-ETH.** Son 2 de 6 activos de R1, diluidos por el riesgo inverso de la cartera, y C6 no usa vol. El efecto esperado es chico y la puerta de inclusión r51 (+0,05 de Sharpe) tiene poco poder.
  3. **Las alts de U50 ya se usaron** en r52–r55: X1, ML3 y la validación de C6 en r54. Lo que se desarrolla en ellas queda contaminado por esas miradas; **N2 es la confirmación limpia.**
  4. **U50 y N2 tienen sesgo de supervivencia:** solo monedas que siguen listadas.
  5. **F3 es hermana de ML3,** que falló la puerta bajista en r55. Hereda su construcción y sus puertas.

## 1. F1: diagnóstico de atribución (N + 0)
Script `research_scripts/r57.py diag` → `data/r57/f1_diag.json`.

Las particiones de cada moneda-día se escriben primero en `data/r57/f0_states.npz` (estado T3, persistencia, p(rango), corte), **antes de unirlas con trades o retornos**.

**Muestras:**
- **(a) Decide:** los 2.454 trades R2/R3 de C6 congelado en las 48 alts (`data/r52/v1_events.json`, con R por trade). Se usan los que abren el 2021-07-02 o después y tienen estado. El estado se toma de la fila del día anterior a la apertura.
- **(b) Descriptiva:** trades de R1 y de C6 en BTC/ETH de P-r55, en la ventana común, por el estado de su moneda.
- **(c) Descriptiva:** retornos diarios de las mangas R1 y C6 de P-r55 según el estado T3 de BTC del día anterior. Se reportan la media, la vol y el Sharpe por estado.

**Métrica:**
- **D_T3** = R medio de los trades con T3 = alta − R medio del resto.
- **D_pers:** la misma diferencia, pero partiendo por `persist_vol`.
- **IC al 90%:** bootstrap de 5.000 réplicas por bloques de semana ISO de apertura, con semilla 57.
- Además se reporta el signo por año: 2021 S2, 2022, 2023 y 2024.

**Regla F3 (veta C6 con selección):** sigue si se cumplen las tres condiciones:
1. D_T3 > 0, con el IC 90% por encima de 0;
2. D_T3 > 0 en al menos 3 de los 4 años;
3. D_T3 > D_pers en el punto.

**Regla F4 (veta de reversión), sin PnL:**
- **Datos:** los retornos log diarios de las 48 alts, demeaned por moneda.
- **Grupos:** cada día d se clasifica por su p(rango) contra el corte, alto o bajo.
- **Estadístico:** AC(g) = Σ_{k=1..5} corr(r_{d+1}, r_{d+1−k}), agrupando todas las moneda-días del grupo g.
- **Pasa si:**
  - AC(alto) < 0, con el IC 90% (mismo bootstrap por semanas) por debajo de 0;
  - y AC(alto) < AC(bajo) en el punto.

**U1 no depende de F1.**

## 2. F2: U1, vol pronosticada en R1 cripto (N + 1 → 141)
**Regla:** subclase de `DonchianEnsR49` en la que solo cambia la vol de la regla de tamaño:
`rv_U1 = σ30 · m`, con `m = clip( sqrt( exp( pred_d − l20_d + b_q ) ), 0,5 , 2,0 )`.
- `pred_d`: log de la suma de RV a 20 días que pronostica Chronos-2 con covariables (`chronos_chronos2cov.npy`).
- `l20_d`: log de la suma de RV de 1h de los 20 días previos, hasta d (`r56_eval.har_inputs()['l_20']`).
- `b_q`: sesgo del trimestre calendario q que contiene a d, calculado como en `r56_eval.chronos_feats`. Es la media de (objetivo − pred) en las filas elegibles de las monedas de desarrollo con índice ≤ q0 − 40, es decir, con el objetivo ya conocido. Así el cociente no mueve el apalancamiento medio.
- **El clip [0,5; 2,0]** es solo una salvaguarda contra datos rotos y se fija acá.
- **Desde cuándo:** `m` actúa desde el 2021-01-01. Antes de esa fecha, cuando falta el pronóstico y en los otros cuatro activos se usa σ30 sin cambios.
- La forma de cociente conserva el nivel de σ30: el RV de 1h y la std de los cierres 4h tienen escalas distintas.

**Puertas, todas con N = 141:**
1. Puertas de r55 (`r55_engine.gates`) contra P-r55: g1 bajista, g2 lateral, g3 alcista y g4 inclusión r51. La g4 pide ΔSharpe largo ≥ 0,05, o +1 trimestre positivo sin bajar el Sharpe, y que el Sharpe común no caiga más de 0,05.
2. **Costos ×2:** se corren R1-BTC y R1-ETH con la comisión taker duplicada, tanto en la base como en U1. ΔSharpe común de la cartera ≥ 0.
3. **DD:** no empeora más de 1 pp en ninguna de las dos ventanas.

Bolt (T1) no entra como segunda variante.

## 3. F3: C6 con selección de monedas (N + 2 → 143; solo si pasa la regla F3)
- **Construcción de ML3** (`r55_ml.c6_alts` + `c6_prime`): C6' = 0,5 C6(BTC/ETH) + 0,5 canasta de alts · σ_C6 / σ_alts, con C6 solo antes de la primera señal.
- **Selección:** al abrir, cada trade de C6 congelado en una alt se multiplica por 1 si la moneda está seleccionada en la fila del día anterior y por 0 si no.
  - **S1:** la alt está en el tercil superior de p(vol alta) de T3 entre las alts con pronóstico ese día.
  - **S2:** la alt está en el tercil superior de log(vol pronosticada / RV previa) = `pred_d − l20_d` entre las alts con pronóstico ese día.
- **Puertas:**
  1. las de r55 contra P-r55;
  2. la canasta de alts seleccionada tiene Sharpe ≥ el de la canasta sin selección + 0,10 en la misma ventana (puerta de ML3);
  3. **confirmación única en N2.**
- **Confirmación en N2:**
  - Primero corre C6 congelado sin selección sobre las 20 monedas, como validación tipo r54, sin N.
  - La variante pasa si la canasta seleccionada en N2 tiene Sharpe > 0 y > el de la canasta sin selección. La selección en N2 es el tercil entre las monedas de N2.
- **Ventana:** de 2021-07-01 a 2024-12-31.
- **Si pasan las dos,** queda la de mayor ΔSharpe común.

## 4. F4: reversión solo-largo condicionada a p(rango) (N + 2 → 145; solo si pasa la regla F4)
- **Reapertura declarada de M2a,** que no generalizó sin condición en r50. Se usan las reglas congeladas de `r50_engines.m2_decider(·, cfd = False, 'a')`:
  - RSI2 < 10 con el cierre sobre la SMA200;
  - límite maker al cierre;
  - salida en la SMA5 o a los 5 días;
  - tamaño 0,17/σ.
- **Barras y costos:** barras diarias UTC desde 1h, con el funding real de cada moneda y los costos de r50, sobre las 48 alts.
- **Q1:** sin condición. Es la vara contrafáctica y cuenta N. **No puede ser candidata en r57:** la hipótesis es la condición.
- **Q2:** la señal del día i se toma solo si p(rango) de la fila i (cierre de i) ≥ el corte.
- **Construcción:** Q entra como reparto de la manga cripto, C6'' = 0,5 C6 + 0,5 Q · σ_C6 / σ_Q (`c6_prime`). Así se reparte la manga entre rupturas y rango.
- **Pasa Q2 si se cumplen las tres:**
  1. las puertas de r55 contra P-r55;
  2. la canasta de Q2 tiene Sharpe > el de Q1 en 2021-07→2024;
  3. en N2, la canasta de Q2 tiene Sharpe > 0 y > el de Q1.
- **Opcional Q3 (N + 1 → 146), solo si pasa Q2:** el peso de Q es w(d) = clip(p̄(rango)_{d−1}, 0,2, 0,8), con p̄ = la media transversal de p(rango) en las alts. Así, C6''' = (1 − w) C6 + w Q · σ_C6/σ_Q. Mismas puertas, contra Q2.

## 5. En paralelo: DVOL de Deribit (N + 0)
- **Fuente:** endpoint público `public/get_volatility_index_data`, sin clave.
- **Qué se baja:** BTC y ETH, resolución diaria, desde el inicio de la serie y **solo hasta el 2024-12-31**.
- **Dónde:** `data/r58/` (gitignore), con manifiesto, controles de huecos y duplicados, y una revisión de los términos de uso.
- **Script:** `r57_dvol_probe.py`, en el Python del host.
- **Entregable:** una nota de factibilidad para r58, sin pruebas económicas.

## 6. Cierre
- Si pasa alguna variante, queda como **candidata provisional**: P-r57 = P-r55 + el cambio.
- No se abre 2025 sin autorización del usuario.
- La confirmación en Jesse queda para cuando el usuario lo decida.
- Se actualizan:
  - `R57_CLOSE_*.md`, `HANDOFF_R58.md`;
  - `TRIAL_REGISTRY.json → r57_closed`;
  - `DOCS.md`.
