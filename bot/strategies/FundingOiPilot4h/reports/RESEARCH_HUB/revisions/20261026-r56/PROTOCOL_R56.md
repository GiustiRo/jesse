# r56: protocolo preregistrado. Detección de régimen cripto como pronóstico de estados

Plan aprobado por el usuario el 2026-10-26, con tres decisiones explícitas:
- el plan se aprueba tal como se presentó;
- la exclusión «HMM/LightGBM sobre un solo activo» se levanta **solo en r56** y solo en formato agrupado sobre las 50 monedas;
- se autoriza instalar `torch` CPU y `chronos-forecasting` en el contenedor de investigación para la familia T.

Este archivo se commitea con el cierre de F0 y antes de ajustar cualquier detector. Un cambio posterior es una configuración nueva, que suma a N_régimen, o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones
- **Objetivo:** pronosticar el estado del mercado de cada moneda durante los próximos 20 días. Se evalúa **sin PnL** y contra etiquetas fijadas en F0. Las estrategias por régimen quedan para r57, y solo si se cumple el puente (§6).
- **Contadores:**
  - **N_régimen**, nuevo, cuenta cada configuración de detector evaluada. Techo de **30**.
  - **La N de estrategias sigue en 140** y r56 no la mueve.
- **Datos:** las 50 monedas de U50 (`data/r52/*_1h.npy`, data.binance.vision), con barras diarias UTC armadas desde 1h y la RV intradía desde 1h. Solo perpetuos USDT-M de Binance.
- **Cortes de datos:**
  - **corte duro en 2024-12-31**, con aserciones en el código: ninguna barra ni ventana de etiqueta lo cruza;
  - **2025 sellado:** queda reservado para un candidato nuevo preregistrado, con autorización del usuario;
  - **2026 reservado.**
- **Herramientas:** numpy, scipy, sklearn 1.8 y statsmodels 0.14, ya instaladas. No se instalan `hmmlearn`, `iisignature`, `jumpmodels`, `ruptures` ni `arch`. La única instalación autorizada es `torch` + `chronos-forecasting`, y solo para la familia T.
- **Advertencias declaradas antes de los resultados:**
  1. **U50 tiene sesgo de supervivencia** (sin deslistados). En r56 importa menos que en un libro largo, porque no se mide retorno direccional, pero las monedas que murieron en régimen bajista no están.
  2. **2024 ya se usó en el trabajo de estrategias de r52–r55**, pero nunca con estas etiquetas: queda como validación temporal. La prueba limpia es el holdout de monedas.
  3. **La etiqueta de vol es relativa al último año de cada moneda.** Como la vol cripto bajó entre 2021 y 2023, la clase «compresión» es mayoría en desarrollo (51%). Por eso las métricas son balanceadas y por clase.

## 1. Etiquetas (fijadas en F0; `r56_panel.py`, `data/r56/f0_labels.json`)
Horizonte H = 20 días. Para cada moneda y día t, la ventana es t+1..t+20, que se conoce al cierre de t+20.

| Eje | Definición | Clases | Proporción en desarrollo ≤ 2023 |
|---|---|---|---|
| **Y_vol** (nivel) | q = proporción de las sumas de RV a 20 días de la moneda (ventanas cerradas en los 365 días previos a t, mínimo 180) que quedan por debajo de RV(t+1..t+20) | 0 compresión (q ≤ 1/3), 1 media, 2 alta (q ≥ 2/3) | 51,4% / 27,4% / 21,2% |
| **Y_trend** | eficiencia de Kaufman de la ventana: \|c(t+20) − c(t)\| / Σ\|Δc\| | 1 tendencia (≥ 0,30), 0 no | 31,7% / 68,3% |
| **Y_range** | todos los high ≤ c(t) + 3,0·ATR20(t) y todos los low ≥ c(t) − 3,0·ATR20(t) | 1 rango, 0 no | 45,7% / 54,3% |
| y_volchg (reportada, nunca decide) | ln(RV futura / RV pasada), umbral ±ln 1,5 | 3 | 32,6% / 41,1% / 26,3% |
| Y_exit (F4) | dirección del primer cierre fuera de la caja de Y_range, en los días que estaban en rango | arriba / abajo | se fija en el registro de X1 |

**Cómo se fijaron los umbrales:** con la regla escrita en `r56_panel.py` antes de imprimir cualquier estadística, eligiendo el punto de la grilla cuya proporción quedara más cerca del objetivo (35% de tendencia y 40% de rango). Resultaron e = 0,30 y k = 3,0.

**Sensibilidades H = 10 y H = 40:** se guardan y se reportan, pero no deciden.

**Enmienda F0-1 (2026-10-26, antes de cualquier detector):** la etiqueta de vol del plan era el cociente ln(RV futura / RV pasada).
- La RV pasada aparece tanto en la etiqueta como en su propia vara de persistencia, así que la persistencia queda anticorrelacionada por construcción: exactitud balanceada de 0,23 en desarrollo, debajo del 0,33 del azar.
- Además, con el cociente «compresión» significaba «la vol va a bajar» y no «la vol está baja».
- Se reemplazó por la etiqueta de nivel. El cociente queda como y_volchg, que se reporta pero no decide.
- Para decidirlo solo se miraron las monedas de desarrollo hasta 2023.

## 2. Varas mínimas (sin costo de N_régimen)
- **Persistencia:** la misma etiqueta calculada sobre la última ventana ya cerrada (t−19..t), que se conoce en t. En Y_range, la caja se ancla en c(t−20) y ATR20(t−20).
- **Climatología:** la frecuencia de cada clase entre las etiquetas de la moneda conocidas en t, en los 365 días previos, con un mínimo de 60.
- **T90 de r55**, como variable mapeada a probabilidades con una logística ajustada en el pliegue. Es la vara de referencia de la señal anterior.

| Desarrollo ≤ 2023 | Persistencia: exactitud balanceada | Persistencia: cambios/año | Climatología: exactitud balanceada | Climatología: Brier | Cambios/año de la etiqueta |
|---|---|---|---|---|---|
| Y_vol | 0,450 | 19,9 | 0,367 | 0,664 | 17,7 |
| Y_trend | 0,478 | 46,8 | 0,496 | 0,447 | 46,6 |
| Y_range | 0,440 | 38,4 | 0,482 | 0,517 | 38,7 |

## 3. Validación
- **Monedas:** 16 de las 48 alts quedan como **holdout**, sorteadas con `default_rng(56)` (una por cada triplete por fecha de listado, `data/r56/holdout.json`):
  - AAVE, ADA, AR, COMP, DASH, EGLD, GTC, ICP, IOST, LINK, OP, QNT, RLC, UNI, XRP y ZEN.
  - No se tocan hasta F5.
  - BTC y ETH quedan en desarrollo, junto con las otras 32 alts (34 monedas en total).
- **Tiempo:**
  - **Walk-forward:** expansivo, con reajuste trimestral, entrenando con etiquetas cuya ventana cerró ≥ 20 días antes del inicio del trimestre de prueba (embargo de H).
  - **Desarrollo:** 2021-07 → 2023-12.
  - **Validación temporal:** 2024, que se mira una vez por configuración ya fijada y se reporta junto con el desarrollo.
- **Elegibilidad (como r52):** ≥ 90 días desde el listado, mediana de volumen de 30 días ≥ 10 M USDT y barra válida.
- **Prueba de no mirar el futuro, obligatoria para cada familia de variables:** se recalcula cada variable con la serie truncada en 20 fechas al azar y debe coincidir exactamente con el valor de la serie completa.

## 4. Métricas (fijas)
- **Primaria:** **Brier skill score** (BSS) contra la mejor vara de cada eje: la de menor Brier entre persistencia y climatología, medido en la misma muestra. Se agrupa sobre todas las monedas y días evaluables.
- **Secundarias:**
  - log-loss;
  - exactitud balanceada del argmax;
  - pendiente de calibración (regresión de la etiqueta sobre la probabilidad pronosticada, por clase);
  - **cambios por año** del estado operable (argmax);
  - **anticipación:** para las transiciones hacia vol alta, hacia tendencia y fuera de rango, la mediana de días entre el primer día cuya etiqueta futura cambia y el primer cruce de p > 0,5 del detector, comparada con la misma medida de la persistencia.
- **Inferencia:**
  - **Diebold–Mariano** sobre la diferencia diaria de Brier (promedio transversal por día), con bootstrap estacionario de bloques de fechas (bloque medio de 20 días, 2.000 réplicas, remuestreando todas las monedas a la vez);
  - **SPA de Hansen** (2005) sobre todas las configuraciones de N_régimen evaluadas en el eje, contra su mejor vara, con el mismo bootstrap.

## 5. Configuraciones (techo N_régimen = 30)
Cada familia se evalúa como **logística multinomial regularizada y agrupada** (sklearn, C = 1, variables estandarizadas en el pliegue) sobre sus propias variables causales. Así se mide cuánta información aporta cada familia.

La especificación exacta de cada configuración (ventanas, λ, cuadrículas) se registra en `TRIAL_REGISTRY.json → regime_trials` **antes** de correrla. Cada configuración se evalúa en los tres ejes, salvo que su ficha diga otra cosa: por ejemplo, la familia V es solo para Y_vol. N_régimen cuenta configuraciones, no ejes. El SPA cubre la multiplicidad de ejes.

| Fase | ID | Familia | Tecnología |
|---|---|---|---|
| F1 | A1, A2, A3 | **Clásicos.** A1: tendencia (ADX, eficiencia de Kaufman y T90 a 20/60/90). A2: compresión (ancho de Bollinger en percentil, squeeze Bollinger/Keltner, Donchian/ATR, choppiness). A3: A1 + A2 | numpy |
| F1 | B1, B2 | **Memoria.** B1: varianza relativa y autocorrelación multi-escala. B2: Hurst por DFA | numpy |
| F2 | C1a, C1b | **Jump model continuo online**, con 2 y 3 estados. Variables EWMA multi-escala de retorno, vol, downside y drawdown. λ elegido por log-loss dentro del pliegue de entrenamiento. Probabilidades filtradas (`r56_models.cjm_online`) | numpy |
| F2 | C2 | **Sparse JM:** el JM con selección de variables por pesos ℓ1 (Nystrup y otros 2021) sobre el set amplio | numpy |
| F2 | C3 | **Wasserstein k-means** 1D sobre ventanas de 20 días de retornos de 4h | numpy |
| F2 | C4 | **HMM gaussiano agrupado, solo filtrado** (vara de comparación) | statsmodels |
| F2 | D1 | **BOCPD** sobre retornos y log-RV: run-length esperado y probabilidad de quiebre reciente | numpy/scipy |
| F3 | V1, V2, V3 | **Vol.** V1: HAR-RV agrupado (log RV 1d/5d/22d). V2: V1 + sección transversal (vol de BTC, dispersión, correlación media, funding mediano, desbalance agresor q15). V3: HAR con cambio de régimen de Markov. Solo Y_vol | numpy / statsmodels |
| F3 | E1, E2 | **Geometría con definiciones fijas.** E1: canal (R² y pendiente a 20/50 días) y caja de rango (ancho y toques). E2: banderín (impulso ≥ 2·ATR seguido de consolidación con rango decreciente) y Wyckoff-lite (rango después de una caída ≥ 25%, más spring: perforar el piso y recuperarlo en ≤ 3 días) | numpy |
| F3 | S1 | **Path signatures** de nivel 3 sobre (tiempo, log-precio, log-vol) en ventanas de 20 y 60 días | numpy (`r56_models.signature`) |
| F4 | G1 | Global: logística con todas las variables y las probabilidades de C, D y V | sklearn |
| F4 | G2 | **Gradient boosting agrupado** (`HistGradientBoostingClassifier`): hiperparámetros fijos (máx. 200 iteraciones, learning rate 0,05, máx. 15 hojas, mínimo 200 por hoja, L2 = 1) y sin tuning anidado | sklearn |
| F4 | X1 | **Y_exit:** dirección de la salida de rango con G1, sobre los días en rango (aquí entran Wyckoff y banderines) | sklearn |
| F4 | T1, T2 | **Modelo fundacional zero-shot:** T1 con Chronos-Bolt y T2 con Chronos-2, si corre en CPU en tiempo razonable. Ambos pronostican log-RV a 20 días, que se mapea a Y_vol contra la distribución del año previo. Comparados contra V1 | torch + chronos-forecasting |

**Total:** 22 configuraciones. Las otras **8 quedan de reserva** para enmiendas fechadas.

**Selección para F5:** solo pasan las ≤ 3 configuraciones con mayor BSS promedio entre desarrollo y 2024, con BSS > 0 en ambos.

## 6. Puente a r57 (fijo)
Un detector **habilita gastar N de estrategias** en r57 solo si cumple todo lo siguiente en un mismo eje:
1. **Desarrollo:** BSS ≥ +0,05 contra la mejor vara y SPA con p < 0,05.
2. **2024 (tiempo) y holdout de monedas:** BSS > 0 en ambos, con Diebold–Mariano p < 0,10 en el holdout.
3. **Estabilidad:**
   - BSS > 0 en ≥ 60% de las monedas del holdout;
   - BSS > 0 en ≥ 3 de los 4 años entre 2021 y 2024 (2021 solo desde 07).
4. **Usabilidad:**
   - el estado operable cambia ≤ 12 veces por año;
   - en la mediana de las transiciones, anticipa a la persistencia por ≥ 3 días;
   - pendiente de calibración entre 0,7 y 1,3 en las clases del eje.

Si ningún detector lo cumple, r57 no gasta N en estrategias por régimen.

Advertencia: una buena clasificación no garantiza PnL. r57 tiene que preregistrar sus propias puertas económicas.

## 7. Fases e informes
| Fase | Contenido | N_régimen |
|---|---|---|
| F0 | Panel, etiquetas, varas, holdout, pruebas sintéticas y este protocolo | 0 |
| F1 | A1–A3, B1–B2 | 5 |
| F2 | C1a, C1b, C2, C3, C4, D1 | 11 |
| F3 | V1–V3, E1–E2, S1 | 17 |
| F4 | G1, G2, X1, T1–T2 | 22 |
| F5 | ≤ 3 configuraciones sobre el holdout (no suman N_régimen: son las mismas configuraciones), veredicto del puente, cierre y handoff a r57 | — |

- **Informes:** `reports/R56_PHASE{n}_RESULTS_<fecha>.md`, guardados con `save_strategy_report`.
- **Commits:** uno al cerrar cada fase.
- **Scripts:** corren en el contenedor de investigación: `docker exec -w /src/bot jesse-research-jesse-1 python research_scripts/<script> <acción>`.

## 8. Fuera de alcance
- PnL;
- retornos direccionales condicionados al estado (salvo Y_exit, como etiqueta);
- 2025 y 2026;
- spot;
- LSTM o *deep learning* propio;
- patrones de velas;
- tuning por PnL;
- tuning anidado de GBM;
- live, paper y Pi.

## Enmienda F5-1 (2026-10-26, antes de ver cualquier resultado de F4 y antes de abrir el holdout)
El §5 decía «las ≤ 3 mejores configuraciones», pero no aclaraba si se cuentan en total o por eje. Como el puente (§6) se juzga por eje, F5 toma **la mejor configuración de cada eje del puente** (vol, tendencia y rango; como máximo 3):
- el criterio es el BSS promedio entre desarrollo y 2024, con BSS > 0 en ambos;
- X1 (dirección de salida) no es un eje del puente: se reporta, pero no va al holdout.

Así se evita que un solo eje ocupe los tres lugares. Implementación: `r56_eval.select_f5` y `run_f5`.

## Extensión r56-B (2026-10-26). Estabilizar y mejorar el pronóstico antes de r57
Plan aprobado por el usuario. Se commitea antes de cualquier corrida de r56-B. Decisiones del usuario:
- techo de **N_régimen de 30 a 40**;
- **descargar un set nuevo N2** como validación final intocada;
- **Docker sin cambios** (ya tiene los 22 hilos), con un máximo de 2 trabajos pesados en paralelo.

### Puente enmendado (criterio 4a), con el factor de mercado
El tope fijo de 12 cambios por año queda reemplazado por: **cambios por año del estado operable ≤ f_mkt × cambios por año de la etiqueta del mismo eje y horizonte**, medidos en la misma muestra.

**De dónde sale f_mkt** (`r56_noise.py`, `data/r56/f6_noise.json`): no interviene ningún detector. Cada etiqueta se mide por segunda vez con los mismos datos de mercado:
- en vol, la RV sale de retornos de 2h en horas pares e impares;
- en tendencia y rango, los días se cortan a las 12 UTC.

f_mkt es la mediana, sobre las monedas de desarrollo hasta 2023, del cociente entre los cambios de la segunda medición y los de la oficial.

| Horizonte | vol | tendencia | rango |
|---|---|---|---|
| 20 días | 1,048 | 0,987 → **1,0** | 1,000 |
| 40 días | 1,058 | 1,000 | 1,001 |

**Piso de 1,0:** un tope menor que la etiqueta haría fallar incluso a un pronosticador perfecto.

**Qué cuenta como «estado operable»:** puede ser el estado estabilizado de F7. Los demás criterios del puente no cambian.

**Advertencia declarada:** esta enmienda se hace después de ver los resultados de r56. El factor sale de un procedimiento que no usa ningún detector, pero la decisión de enmendar sí es posterior a esos resultados.

### Etiquetas H = 40 (`r56_panel.py h40`, `data/r56/f6_labels_h40.json`)
- **Regla de F0:** terciles de vol; eficiencia con objetivo de 35%; caja ATR con objetivo de 40%. Se fijaron mirando solo las tasas base de desarrollo hasta 2023.
- **Grilla de k ampliada hasta 6,0:** con la grilla de F0, el máximo (4,0) ya quedaba cerca del objetivo, y la sensibilidad H = 40 de F0 (23% con k = 3) mostraba que la grilla original se quedaba corta.
- **Resultado:** e = 0,25 (26,5% de tendencia) y k = 4,0 (39,7% de rango).
- **Cambios por año de la etiqueta** (desarrollo): vol 9,0, tendencia 29,4 y rango 28,3.

### Set nuevo N2 (`r56_fresh.py`, `data/r56/n2/universe_n2.json`)
**Regla de selección:**
- perpetuos USDT-M en estado TRADING, listados antes del 2022-07-01, fuera de U50, sin stablecoins;
- los 20 de mayor volumen de 24h al 2026-10-26.

**Lista:** CHZ, COTI, RSR, VET, CELO, KAVA, RUNE, DUSK, OGN, ONE, DYDX, RVN, PEOPLE, JASMY, MANA, GRT, TRB, ENS, THETA y IOTX.

**Descarga:** velas de 1h y funding de 2020-01 a 2024-12, con verificación SHA-256. 2025 ni siquiera se descarga.

N2 se usa **una sola vez**, en F10.

### Configuraciones de r56-B (N_régimen de 22 a 38; techo 40)
**F7, estabilizadores** sobre las predicciones fuera de muestra de T1 y V1 en Y_vol a 20 días (6 configuraciones):
- **St1, confirmación:** el estado cambia solo si el nuevo argmax se mantiene d días seguidos (d de 1 a 10).
- **St2, histéresis:** el estado cambia solo si p(nuevo) − p(actual) ≥ m (m de 0 a 0,40, cada 0,05).
- **St3, decodificador con penalización:** DP hacia adelante con costo −log p más λ por cada cambio, quedándose con el último estado (λ en {0,1; 0,2; 0,5; 1; 2; 5; 10}).

**Cómo se elige el hiperparámetro, sin mirar el futuro:**
- en cada trimestre, con las predicciones fuera de muestra de los 4 trimestres anteriores;
- se maximiza la exactitud balanceada del estado, sujeta a cambios ≤ f_mkt × los de la etiqueta en esas filas;
- si ninguno cumple, se toma el que menos cambia;
- si hay menos de 4 trimestres previos, se usan d = 3, m = 0,15 y λ = 1.

Las probabilidades no se tocan, así que el BSS es el del modelo base.

**F8, mejor pronóstico de vol** (5 configuraciones):
- **H1, HExp agrupado:** EWMA de la log-RV con centros de masa 1, 5, 25 y 125, centradas por la media de 365 días de la moneda. Variables z a los terciles, como V1.
- **H2, HExpGl:** H1 más un factor de vol global (media transversal de la EWMA de 25 días, rezagada un día).
- **K1:** logística sobre las variables de T1 + H2.
- **O1:** logit acumulado ordinal (statsmodels OrderedModel) sobre las variables de K1.
- **T3:** Chronos-2 con covariables pasadas (log-RV de BTC y vol global media).

**F9, horizonte de 40 días** (5 configuraciones):
- vol40 con T1 y con la mejor de F8;
- trend40 con A3 y C3;
- range40 con A3.

**Estabilizador en F8 y F9:** a cada configuración se le aplica el estabilizador de F7 con mejor exactitud balanceada en desarrollo dentro del tope. Es una regla fija y no suma configuraciones.

### F10, validación final (no suma N_régimen)
- **Selección:** por eje y horizonte, la mejor configuración (con su estabilizador) según el BSS promedio entre desarrollo y 2024, que además cumpla en desarrollo y 2024 el criterio 4a enmendado.
- **Corrida única:**
  - sobre N2, con modelos entrenados solo en las monedas de desarrollo;
  - el holdout de 16 alts se reporta como **segunda mirada declarada**.
- **Puente:** el veredicto se toma sobre N2, con todos los criterios y el 4a enmendado. El SPA final cubre las 38 configuraciones.

### Enmienda F9-1 (2026-10-26, antes de ver T3 y antes de correr F9)
**Problema:** T3 (Chronos-2 con covariables) avanza a ~5 pronósticos por segundo, porque comparte la CPU con otros cálculos. Le quedan ~4 horas, y una versión a 40 días tardaría otro tanto.

**Cambio:** la «mejor de F8» que usa F9 (configuración P2) se elige entre H1, H2, K1 y O1, sin T3, por BSS promedio de desarrollo y 2024. Resulta K1 (0,174). T3 se evalúa igual dentro de F8 y entra en el SPA y en la selección de F10.

**Estabilizador de F8 y F9:** St2 (histéresis), que es el de mejor exactitud balanceada en desarrollo dentro del tope (Z2V), según la regla fija.
