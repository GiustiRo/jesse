# r58: protocolo preregistrado. Qué distingue una ruptura buena de C6 de una mala

El usuario aprobó el plan el 2026-10-27 y pidió ejecutar F0 y reportar al cerrarla. Las fases siguientes se ejecutan con la misma aprobación, reportando al cierre de cada una.

Este archivo se commitea **antes de bajar N3 y antes de leer cualquier trade de C6 junto con una variable**. Un cambio posterior es una variante nueva, que suma N, o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones

### Base, contadores y cortes
- **Base:** P-r55 congelada (`../20261026-r55/P55_FREEZE.md`), con Sharpe 1,677 en 2018-09→2024 y 1,723 en 2021–24.
- **N de estrategias = 143 al empezar. Techo de r58: 146.**
  - La confirmación en N2 ∪ N3 suma 1.
  - La integración a P-r55 suma 1 más, solo si la confirmación pasa.
- **N_régimen sigue en 38:** r58 no evalúa detectores nuevos.
- **N_temática (contador nuevo, aparte de N y de N_régimen):** cuenta cada variable o partición que se cruza con el resultado de los trades de C6. **Arranca en 12**, por las miradas previas sobre el mismo tema:
  - 1 de `R53_F2_C6q` (C6 filtrado por z(QOI));
  - 8 de `R54_M1` (meta-labeling de C6: z_qoi, fund7, vol30, ret4w, adx14, dist_e80_atr, btc_regime y btc_ret7);
  - 3 de r57 F1 (T3, persistencia y p(rango)).
- **Cortes:**
  - corte duro el 2024-12-31, con aserciones;
  - 2025 sellado y 2026 reservado;
  - sin live, paper ni Pi.
- **Riesgo declarado:** `data/r52/v1_events.json` guarda **544 trades de C6 de 2025** (r54 los calculó, pero midió solo hasta 2024). Se descartan al cargar y nadie los mira.

### Universos
- **U50 alts:** las 48 de r54, en `data/r52`. Están usadas en r52–r57. **Son solo de desarrollo.**
- **N2:** las 20 de `data/r56/n2/universe_n2.json`. Sus pronósticos se evaluaron en r56 F10, pero **C6 nunca corrió sobre ellas.**
- **N3, nuevo:** la regla de N2 aplicada hoy (`r58.py n3_select`).
  - Perpetuos USDT-M en TRADING, con onboarding antes del 2022-07-01, base que no sea stablecoin, fuera de U50 y de N2.
  - **Enmienda previa a la descarga:** se excluyen los contratos índice (`underlyingType` INDEX). La primera corrida traía BTCDOMUSDT, un índice de dominancia y no una moneda.
  - Se toman las 30 con mayor volumen en 24 horas. La lista queda en `data/r58/universe_n3.json`, commiteada en este mismo commit, antes de bajar nada.
  - Se bajan 1h con taker + funding de 2020-01 a 2024-12, con el checksum verificado.
  - Ninguna de las 30 aparece en código, datos ni informes anteriores.
- **Sesgo de supervivencia declarado** en N2 y N3: solo monedas que siguen listadas.

### Regla anti-futuro
- Las variables de un trade salen de su **vela de señal**, la vela 4h cuyo cierre coloca la orden:
  - R2 llena en ese cierre;
  - R3 deja ahí un límite que llena en la vela siguiente, así que su vela de señal cierra 4h antes de la apertura.
- Los estados diarios usan la fila del último día cerrado antes de ese cierre (`r57.row_for`, con aserción).

### Corrección al plan
**P5 es una logística sobre las variables A1 + A2, no un modelo torch.** Sus pronósticos para N3 salen del mismo camino de r56 F10:
- `fit_predict` reajustado por trimestre solo con las monedas de desarrollo de U50, que predice las columnas nuevas.
- Primero tiene que reproducir exacto `pred_n2_P5_range40` desde panel70.
- **r58 no usa torch.**

## 1. Variables (fijadas antes de mirar), F0
Todas son para C6, que es **solo largo** (`r50_f1b.r2_r3_decider`). «Alineado con el lado» significa del lado comprador.

| Id | Variable | Clase favorable (dirección previa) | Notas |
|---|---|---|---|
| V1 | Compresión de la vol pasada: `persist_vol` (vara de r56) del día anterior | clase 0 (compresión) | Réplica de r57 F1. Existe desde el 2020-12-30 |
| V2 | p(rango a 40 días) de P5, corte 0,3874 (`data/r57/f0_cuts.json`; ver enmienda E1) | p < 0,3874 | Réplica de r57 F1. Existe desde el 2021-07 |
| V3 | Volumen relativo: volumen de la vela de señal / mediana de las 180 velas 4h previas (mínimo 90) | tercil superior | Nueva |
| V4 | Desbalance taker de la vela de señal: 2·tbv/v − 1 | tercil superior | **Réplica de R53/R54** (prior bajo). En r53, z(QOI) > 0 restó |
| V5a | Funding saturado: suma de funding de 7 días en el percentil ≥ 0,90 de su propia historia expansiva de sumas de 7 días (mínimo 90 liquidaciones) | **no** saturado | Réplica parcial de `fund7` de R54 |
| V5b | OI saturado | — | **Descartada sin consumir N_temática:** el sondeo (`data/r58/oi_probe.json`) muestra que el OI histórico de las alts en `data.binance.vision` empieza el 2021-12-01 y que solo hay archivos diarios. La regla exigía cobertura desde ≤ 2021-07 |
| V6 | Número redondo (Osler): distancia en ATR(14, 4h) desde el cierre de la vela de señal hasta el próximo nivel {1, 2, 5}·10^k por encima | distancia ≥ 1 ATR (sin nivel redondo cerca adelante) | Nueva. Prior: las órdenes de toma de ganancia se agrupan en niveles redondos |
| V7 | DVOL − RV a 20 días (desde 1h), BTC/ETH, del día anterior; corte en la mediana de los días 2021-03-24→2024 | debajo de la mediana | **Solo descriptiva:** no puede elegirse como filtro |

- **Control (no es candidata):** σ30, la std de 30 días de los retornos 4h, en terciles.
- **Cortes:** los terciles de V3, V4 y σ30 se calculan sobre todas las velas 4h de las alts de U50 desde el 2020-10-15 hasta el 2024-12-31, sin trades. Se aplican sin cambios a N2 y N3.
- **Archivos:** las particiones por vela se escriben en `data/r58/f0_bars_{u50,n2,n3}.npz` y las diarias en `f0_days.npz` y `f0_dvol.npz`. Los cortes y las proporciones de clase, sin trades, van a `f0_cuts.json`, todo **antes** de cualquier unión con trades (commit A).

## 2. F1: barrido en las alts de U50, ≤ 2024 (N + 0; N_temática + 7)
Suman a N_temática V1, V2, V3, V4, V5a y V6. V7 también, como descriptiva: en total **+7, que deja N_temática en 19**. σ30 es solo control.

**Muestra:** los trades de C6 congelado en las 48 alts, abiertos del 2020-10-15 al 2024-12-31. Son 1.910 trades. Cada variable usa los que tienen valor.

**Por variable:**
- **D** = R medio (favorable) − R medio (resto), con IC90 por bootstrap de bloques semanales (5.000 réplicas, semilla 58).
- Signo de D por año: 2021, 2022, 2023 y 2024. Los trades de 2020 entran al total, pero no a esta cuenta.
- **D condicional a V1:** promedio de los D dentro de cada estado de V1, ponderado por n.
- **D condicional a σ30:** lo mismo, por tercil de σ30.
- **Fracción retenida:** los trades favorables sobre el total.
- **Pérdida del decil superior:** la fracción de trades del decil superior de R que cae en la clase excluida.
- **Sharpe aproximado de la canasta:** con la suma semanal de R por fecha de cierre, filtrada contra sin filtrar. Es una aproximación declarada; el Sharpe de verdad se mide por simulación en F2.

**Regla de elegibilidad (todas):**
1. D > 0 y el IC90 de D sin cruzar 0. Un efecto de signo opuesto al previo se reporta, pero **no es elegible**.
2. D > 0 en ≥ 3 de los 4 años.
3. D condicional a V1 > 0 y ≥ 50% de D (no aplica a V1).
4. Fracción retenida ≥ 40%.
5. Pérdida del decil superior ≤ 1,5 × (1 − fracción retenida).

**Selección:** las elegibles (sin V7) se ordenan por D condicional a V1 dividido por su error estándar bootstrap (V1 por su D) y se toman **como máximo 3**. Si ninguna es elegible, r58 cierra en F1 sin gastar N2 ni N3, y N no se mueve.

**Descriptivo (b):** C6 en BTC/ETH de P-r55 en 2021-03→24, con R por trade según V1, V3 y V7.

## 3. F2: confirmación única en N2 ∪ N3 (N + 1 → 144)

### Commit B, antes de correr C6 en N2 o N3
Se commitea:
- **La regla compuesta única:** el AND de las elegidas. Si en las alts de U50 el AND retiene menos del 25% de los trades, se usa la mejor variable sola. Esa elección queda escrita en este commit.
- **El cálculo de poder:** el error estándar esperado de D en N2 ∪ N3, escalando el bootstrap de U50 por la raíz del cociente de tamaños de muestra (estimado con el número de trades que daría C6 en N2 ∪ N3), y el poder contra la mitad del D de U50.
  - Si el poder es menor que 0,4, se reporta al usuario antes de seguir.

### Corrida
- **C6 congelado sin condición** sobre N2 y N3, con los costos de r50 y el funding real, como validación tipo r54, sin N. Puertas de r54: mayoría de monedas positivas, colapsos ≤ 10% y canasta con Sharpe > 0.
- **Regla compuesta sobre los mismos trades:**
  - **D** de la unión N2 ∪ N3 > 0, con la cota inferior unilateral al 90% (percentil 10 del bootstrap semanal) > 0;
  - D > 0 en N2 y en N3 por separado;
  - Sharpe de la canasta filtrada ≥ Sharpe de la canasta sin filtrar en N2 ∪ N3. La canasta filtrada se simula con la regla como compuerta de entrada, sin cambiar nada más de C6;
  - lo mismo con costos ×2.
- **Pasa si se cumplen todas.** Los componentes se reportan por separado, pero no deciden.
- **Si no pasa:** r58 cierra con P-r55 sin cambios y F3 no corre.

## 4. F3: integración a P-r55 (N + 1 → 145; solo si pasa F2)
- **Variante única:** la construcción ML3 (`r55_ml.py`), con C6' = 0,5 C6(BTC/ETH) + 0,5 canasta filtrada de las alts de U50, escalada a σ_C6.
- **Puertas:**
  - inclusión r51 (`DS_MIN` 0,05) en las dos ventanas;
  - las puertas de régimen de r55, incluida la bajista que tumbó a ML3;
  - costos ×2.
- **Descriptivo, sin N:** la regla aplicada a C6 en BTC/ETH dentro de P-r55.
- 2025 sigue sellado. Abrirlo es una decisión del usuario.

## 5. Advertencias declaradas antes de los resultados
1. **Las alts de U50 están usadas en r52–r57.** F1 es desarrollo contaminado. Solo N2 ∪ N3 confirma.
2. **V4 y V5a ya fallaron** como filtro o variable en R53/R54. Entran como réplicas con prior bajo.
3. **Poder bajo.** Con unos 700 trades, N2 sola tendría un poder de ~35% contra +0,6 R. N3 lo sube a ~55–60% en la unión, y el efecto real probablemente es menor que el de U50 (maldición del ganador).
4. **Antecedente estructural:** `R54_W1` (C6 en alts no diversifica a P1) y `R55_F2_ML3` (falló la puerta bajista). F3 tiene un prior bajo, aunque F2 pase.
5. **R tiene colas gordas** (22–25% de ganadores). Por eso la regla de elegibilidad mira el decil superior y el Sharpe de la canasta, no solo el R medio.
6. **Sesgo de supervivencia** en U50, N2 y N3.

## 6. Enmiendas
- **E1 (2026-10-27, antes de cualquier unión con trades).** El corte de p(rango) commiteado en r57 (`9f3df218`, `data/r57/f0_cuts.json`) es **0,3874**. Con ese valor corrieron r57 F1 (`f1_diag.json`) y Q2.
  - El «0,447» de los informes de r57 (F1, F4 y el cierre) y de la versión anterior de este protocolo es un **error de transcripción**.
  - r58 usa el valor commiteado, que es el que produjo el hallazgo −0,19 R / +0,41 R.
