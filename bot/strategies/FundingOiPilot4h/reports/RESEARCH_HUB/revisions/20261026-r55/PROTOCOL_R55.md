# r55: protocolo preregistrado (fijado antes de cualquier resultado)

Plan aprobado por el usuario el 2026-10-26. El usuario pidió explícitamente definir los regímenes y el presupuesto antes de sumar un solo ensayo a N: «desarrollar esto de forma correcta antes de sumar N». Este archivo se commitea antes de correr nada.

Un cambio posterior es una variante nueva, que suma a N, o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones
- Solo perpetuos USDT-M de Binance; sin live, paper ni Pi.
- **Arnés:** `r50_harness.py` y `r50_engines.py`, congelados en `5caf4a53`. Los scripts `r55_*.py` importan sin modificar `r50_*`, `r51_lib`, `r51_f6`, `r52_xs`, `r53_xs` y `r54_v1`.
- **Costos y datos:** los de r51 para P1, R1 y A3, y los de r52 para U50 (vision, elegibilidad, fee taker 0,045% más 2 bp, funding real).
- **Cortes de datos:**
  - toda decisión de r55 se mide con datos hasta el **2024-12-31**;
  - **2025 sellado:** se abre una sola vez en F5, sobre la cartera congelada y con autorización explícita del usuario;
  - **2026 reservado.**
  - Cada script verifica con una aserción que no entra ninguna fecha posterior al corte vigente.
- **Advertencias declaradas antes de los resultados:**
  1. **2024 no es una validación limpia para el ranking.** X1 y la familia Y ya se midieron en 2024 en r52/r53, así que en F2 cuenta como control.
  2. **U50 tiene sesgo de supervivencia** (sin deslistados, decisión del usuario). Ese sesgo favorece a los libros solo-largo, y por eso se agrega la puerta de las 20 monedas antiguas.
  3. **A3 y los activos de validación (Nasdaq, plata, cobre, EWY y EWJ) ya tienen 2025 visto** desde r50/r51. Para ellos 2025 no es independiente, y A3 v2 solo puede entrar como provisional (§F3).
- **Inclusión en cartera:** construcción de r50 F2 y regla de inclusión de r51 (`r51_f6.compare`), con las ventanas de P1 cortadas al 2024-12-31:
  - 2018-09 → 2024;
  - 2021 → 2024.

## F0. Regímenes de BTC (no suma a N)
Un solo parámetro común: **k = 0,5**. Serie de BTC: spot hasta el 2020-10-15 y perpetuo después, como en la lente de r50.

### A. Etiqueta de evaluación (ex post, trimestral): juzga los ensayos y nunca se usa para operar
- r_q es el retorno simple de BTC en el trimestre calendario, de cierre a cierre.
- Umbral u_q = k · σ_a · √0,25, donde σ_a es el desvío de los retornos diarios logarítmicos de los 365 días previos al primer día del trimestre, anualizado con √365.
- La etiqueta:
  - **alcista** si r_q ≥ +u_q;
  - **bajista** si r_q ≤ −u_q;
  - **lateral** en el resto.
- **Sensibilidad mensual:** misma fórmula con √(1/12). Se reporta, pero no decide.
- El trimestre 2018Q3 de P1 (un solo día) queda excluido, como en r51 F2.

### B. Señal operable (causal, diaria)
- T90_t = ln(P_t / P_{t−90}) / (σ_d · √90), con σ_d el desvío de los retornos diarios logarítmicos de esos mismos 90 días.
- El estado:
  - **alcista** si T90 ≥ +0,5;
  - **bajista** si T90 ≤ −0,5;
  - **lateral** en el resto.
- Se calcula al cierre diario UTC y se aplica desde el día siguiente (1 día de demora), sin histéresis.
- Se reportan la cantidad de cambios y el porcentaje de días en cada estado por año.

### Descripción permitida tras este commit
No es un ensayo. Todo se corta al 2024-12-31.
- Mapa de etiquetas A y estados B entre 2018-09 y 2024.
- Matriz de confusión entre las dos capas: la fracción de días de cada estado B dentro de cada clase A.
- Atribución de P1 por clase de trimestre (A): R1/BTC, R1/ETH, C6, oro, SPX y el resto, con `r51_lib.p1_components` y `portfolio_attr`.

## Presupuesto
| Bloque | Ensayos | N acumulado |
|---|---|---|
| F1: E1–E3 | 3 | 128 |
| F2: ML1–ML4 | 4 | 132 |
| F3: A3 v2 | 1 | 133 |
| F4: motor cripto armado, 5 activos y cartera final | 7 | 140 |
| Reserva para enmiendas fechadas antes de medir | 3 | **techo 143** |

- El tuning anidado de GBM queda **fuera de r55**, por decisión del usuario del 2026-10-26: F2 usa el puntaje X1 congelado.
- **Jesse:** ≤ 6 corridas, solo para las mangas nuevas que entren a la cartera congelada, con un máximo de 2 simultáneas.
- Cada ensayo se registra en `TRIAL_REGISTRY.json` antes de leer su resultado.

## Puertas de régimen (comunes a F1, ML3, ML4 y F4.1)
Se miden con la etiqueta A sobre la cartera resultante, comparada con P1, en 2018-09 → 2024:
1. **Bajistas:** la suma de los retornos de los trimestres bajistas no es peor que la de P1, y su mediana es ≥ 0.
2. **Laterales:** igual, sobre los trimestres laterales.
3. **Alcistas:** la suma de los retornos de los trimestres alcistas es ≥ 80% de la de P1.
4. **Inclusión:** cumple la regla de r51 y el Sharpe no cae más de 0,05 en ninguna de las dos ventanas.

## F1. Motor cripto (3 ensayos)
Cada ensayo es un **reemplazo** dentro de P1.

**E1, C6 como núcleo**
- P1 sin R1/BTC ni R1/ETH. C6 queda como único motor cripto.
- La construcción de r50 F2 se recalcula sin cambiar sus parámetros.

**E2, R1 cripto según el régimen**
- Los retornos diarios de R1/BTC y R1/ETH se multiplican por el escalar del estado B: ×1 en alcista, ×0,5 en lateral y ×0 en bajista.
- C6 y los demás activos no se tocan.
- Aproximación sobre retornos, como J1: los fees ahorrados se ignoran, lo que es conservador.

**E3, B2-BTC chico como seguro**
- Corto en BTC (perpetuo con funding real; spot antes de 2020-10, declarado) solo en estado B bajista.
- Tamaño: nocional = −0,25 · 0,17/σ30 · equity, con techo de 0,5x y banda de rebalanceo de 25%. Taker.
- Es un overlay de peso fijo sobre P1, fuera de la construcción por riesgo inverso.
- Se juzga por DD, no por Sharpe. Pasa si cumple todo esto:
  - el DD mejora ≥ 1,5 pp en las dos ventanas;
  - cumple la puerta de régimen 1;
  - ΔSharpe ≥ −0,05 en las dos ventanas.
  - La puerta 3 rige igual.

## F2. Monetización del ranking ML (4 ensayos)
- **Puntaje:** los puntajes walk-forward de X1 (r52), sin cambios. Se reutilizan `r52_xs.weekly_samples` y `predict_walk_forward`.
- **Ventanas:** desarrollo 2021-05 → 2023-12, control 2024 y 2025 sellado.
- **Controles de salto**, en ML1 y ML2:
  - se excluyen las monedas del decil superior de vol a 30 días de la semana;
  - se excluyen las que no pasan el filtro de cola p90 de r53 (`r53_xs.tail_ok`);
  - tope de 15% del bruto largo por moneda, con el exceso redistribuido de forma proporcional.

**ML1, largo top-k cubierto con BTC**
- Largo las k = 10 mejores por puntaje, con pesos proporcionales al rango dentro del top-k (como la pata larga de Y4, `r53_xs.weights_long_hedged`), bruto 1,0.
- Cubierto **solo con BTC**, por el beta de la canasta larga contra BTC a 60 días. Sin cortos en alts.
- Rebalanceo semanal y costos de r52.

**ML2, ML1 con régimen**
- ML1 con exposición cero cuando el estado B del día de rebalanceo es bajista.
- Los cambios de estado se aplican en el rebalanceo semanal y se les cobran los costos.

**ML3, ranking como selector de C6**
- C6 congelado en las 48 alts (eventos y curvas de V1 de r54). Una entrada se toma solo si la moneda está en el top-10 del puntaje X1 vigente en esa vela; si no, se descarta.
- La manga «C6-top» es la canasta equiponderada de esas curvas.
- Se evalúa como **reemplazo** del bloque C6 en P1: C6 BTC/ETH y C6-top comparten el presupuesto de riesgo que hoy tiene C6. No es una suma, para evitar el fallo de W1.

**ML4, inclinación de pesos dentro de C6 en alts**
- El riesgo por trade de C6 en las alts es 1% · clip(1 + 2·r, 0,5, 1,5), con r el rango centrado del puntaje X1 en [−0,5, 0,5].
- Se evalúa igual que ML3.
- Si ML3 y ML4 pasan los dos, entra solo el de mayor Sharpe en desarrollo.

**Puertas de ML1 y ML2**
- Las de r52 F1: Sharpe neto ≥ 0,5 en desarrollo, costos ×2 > 0, ρ con P1 ≤ 0,3 y Sharpe > 0 en 2024.
- Además:
  - Sharpe > 0 en las 20 monedas antiguas, con la misma regla aplicada solo a ellas;
  - suma de los retornos ≥ 0 en los trimestres bajistas y laterales (A) dentro del desarrollo;
  - top-5 semanas < 60% del PnL.

**Puertas de ML3 y ML4**
- Las puertas de régimen.
- Además, el Sharpe de la canasta C6 filtrada o inclinada en las alts (2021–2024) supera al de V1 por ≥ 0,1.

**Descartados:** el largo/corto por quintiles (falló dos veces) y la cobertura BTC/ETH 50/50 (es Y4, y sería un rescate).

## F3. Brent–WTI re-preregistrado (1 ensayo)
**A3 v2:** la regla A3 de `PROTOCOL_R51.md` sin cambios, más un **veto de quiebre estructural**:
- Cada día se estima, sobre los 252 días hábiles previos, Δx_t = a + b·x_{t−1} + e_t, con x = ln Brent − ln WTI, por MCO.
- Solo se permiten entradas nuevas si se cumplen las dos condiciones:
  - t(b) ≤ −2;
  - vida media = −ln 2 / ln(1 + b), entre 0 y 60 días.
- Las posiciones abiertas salen por sus reglas normales.
- **Declaración:** la regla es genérica (prueba de reversión a la media), pero se eligió conociendo el antecedente de A3. Por eso la lente larga deja de ser una prueba independiente para A3.
- **Puertas:** las de manga diversificadora de r51 F6 y el veto de lente larga de r51 (Sharpe < 0, o DD largo > 1,5× el de la decisión), con datos hasta el 2024-12-31.
- **Si pasa, entra como provisional:** su único fuera de muestra limpio es 2026. Abrir 2026 requiere autorización del usuario y no forma parte de r55.

## F4. Integración (7 ensayos)
1. **Motor cripto armado (1):** E1 o E2 (el que pase; si pasan los dos, el de mayor Sharpe en 2018-09 → 2024), más E3, ML1 o ML2 y ML3 o ML4 si pasan.
   - Pasa con las puertas de régimen.
   - Si solo pasó una pieza, este ensayo es esa pieza y no suma.
2. **Activos marginales (5)**, uno por uno y en este orden fijo: Nasdaq, plata, cobre, EWY, EWJ.
   - Cada uno se agrega como manga R1 con su configuración de r50.
   - Entra si cumple todo esto:
     - Sharpe propio en la lente larga ≥ 0,3;
     - la regla de inclusión de r51 sobre la cartera vigente en ese paso;
     - el DD de cartera no empeora más de 1 pp en ninguna ventana.
3. **Cartera final P-r55 (1):** el motor cripto, más R1 en los activos no cripto de P1, más A3 v2 provisional y los activos marginales que entraron.
   - Se congela en un archivo `P55_FREEZE.md` con su commit.
   - Las mangas nuevas representables en Jesse (R1 cripto con régimen, B2-BTC y A3 v2) se confirman con la tolerancia de r51 F1 antes del congelamiento.
   - Los libros ML semanales quedan solo en el arnés, declarado: los datos de U50 se verificaron contra Jesse en r52.

## F5. Cierre
- **Mirada única a 2025** sobre P-r55 congelada, solo con autorización explícita del usuario.
  - Puertas por manga nueva: Sharpe > 0 y ningún derrumbe (Sharpe < −0,5 o DD < −30%).
  - Una manga que falla se retira, sin ajuste.
- Si nada nuevo entra, P1 sigue sin cambios y 2025 sigue sellado.
- Informe de cierre, `TRIAL_REGISTRY.json`, `DOCS.md` y handoff.

## Verificación de reproducción, antes de cada fase
- E2 con el escalar 1 en todos los estados reproduce P1 exacto.
- ML3 con el selector siempre verdadero reproduce exacto la canasta V1.
- A3 v2 con el veto apagado reproduce exacto A3 de r51.

## Informes
- Un informe por fase vía MCP: `R55_PHASE0…4_RESULTS_*.md` y `R55_CLOSE_*.md`.
- Al cierre de cada fase, se reporta al usuario.

## Enmienda 2026-10-26 (después de F0, antes de cualquier ensayo)
Aprobada por el usuario después de ver F0 (`R55_PHASE0_RESULTS_20261026.md`), que es descriptivo y no mide ningún ensayo.

**Sin cambios:**
- **Las definiciones de régimen A y B.** B coincide poco con A en los bajistas (36%) y cambia de estado ~23 veces por año. Ajustar su umbral, su ventana o su histéresis para acercarlo a A sería sobreajustar al mismo período. El retraso es inherente a una señal causal.
- **E1, E2, E3 y F2–F3.** E3 se mantiene por decisión del usuario, con una expectativa previa baja y declarada: B marca como bajista el 37% de los días de los trimestres laterales, así que el seguro va a estar activo en mercados laterales.

**Cambios:**
1. **Puerta de régimen 2 (laterales), más estricta para E1, E2, ML3, ML4 y F4.1.** Además de la condición en 2018-09 → 2024, la suma de los retornos de los trimestres laterales de **2021 → 2024** tiene que superar a la de P1 en esa ventana (P1: −2,3%). No aplica a E3, que conserva sus puertas propias.
2. **Vista mensual.** Junto a cada puerta de régimen se reporta la misma tabla con la etiqueta mensual. Es informativa: con 5 trimestres bajistas y 11 laterales, un solo trimestre puede definir una puerta.
3. **F4: ensayo nuevo, «R1 sin bono»**, tomado de la reserva.
   - Sobre la cartera vigente en ese paso de F4, se prueba quitar la manga R1/bono.
   - Entra con la regla de inclusión de r51 en las dos ventanas.
   - **Post-hoc, declarado:** el bono resta en 22 reglas probadas (r50–r51), y en F0 el resto de R1 resta en los laterales.
   - El WTI no se incluye.
   - Presupuesto: F4 pasa a 8 ensayos y la reserva a 2. **El techo sigue en 143.**
