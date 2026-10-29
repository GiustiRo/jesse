# r60: protocolo preregistrado. Una segunda fuente descorrelacionada: L/S entre alts con la cola cortada

El usuario aprobó el plan el 2026-10-27 y el 2026-10-28 pidió avanzar en forma autónoma y decidir según criterio. Las fases se ejecutan con esa aprobación; cada cierre de fase deja su informe y la nota en la carpeta compartida.

Este archivo se commitea **antes de escribir o correr cualquier código de r60**. Un cambio posterior es una variante nueva (suma N) o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones

### Base y contadores
- **Base:** P-r55 congelada (`../20261026-r55/P55_FREEZE.md`). Vara principal: **R1** (`BENCH_R1_common` del almacén de r59), porque r59 F1 mostró que es lo único que sobrevive a la selección.
- **N = 145 al empezar. Techo de r60: 149.** Suman N solo L0, L1 y L2 (F1), una por variante. La consulta q2 es la misma variante elegida y no suma. Queda 1 de reserva para una enmienda.
- **Oráculo:** como máximo una consulta (q2). Quedan 4 al empezar.
- **Cortes:** corte duro el 2024-12-31 con aserciones; 2025 sellado y 2026 reservado; sin live, paper ni Pi; no se baja ninguna moneda.

### Por qué esta ronda y qué no se repite
- El L/S por ranking ya falló 11 veces: r52 X0–X2 (L/S por quintiles, inverso a la vol, funding real, costos), r53 Y1–Y6 y r55 ML1–ML2. La causa común: la mediana del spread de X1 es +0,73%/semana y la media +0,07%, porque pocas subas explosivas en la pata corta se comen la ganancia.
- Los remedios previos actuaron antes de formar la cartera (filtro de cola por la semana pasada) o alargando el holding. **Lo no probado es cortar la cola durante la semana** (stop de la pata corta), no abrir cortos hacinados (funding negativo) y neutralizar beta. r60 prueba solo eso, con la construcción fija de antemano.
- **Expectativa declarada:** con R1 ≈ 1,3 y ρ ≈ 0, Sharpe de cartera ≈ √(1,3² + S²). Una manga de 0,8 lleva a ~1,53; para ~2 hace falta ~1,5.

### Universo
- **Desarrollo (D):** las 48 alts de U50 (`data/r52/universe50.json` sin BTC/ETH) para las patas; BTC solo como cobertura. Ventana de desarrollo **2021-05-24 → 2024-12-31** (desde la primera semana con puntaje X1/X2). Toda esa ventana ya se vio en r52/r53; la CV y la rotación miden estabilidad, no generalización limpia.
- **Holdout (H):** N2 ∪ N3, solo vía `r59_oracle.py`.

## 1. F0 (N + 0)

### 1.1 Reproducción (aserción antes de todo)
`r60.py repro` reconstruye X0/X1/X2 con el código de `r52_xs.py` (panel recortado al 2024-12-31) y tiene que dar el Sharpe de desarrollo de `data/r52/xs.json` (X0 −0,372, X1 −0,016, X2 0,170, desde 2021-05-24 hasta 2023-12-31) con tolerancia 0,005. Los puntajes walk-forward se guardan en `data/r60/scores.npz` y son los «puntajes congelados» de F1.

### 1.2 Diagnóstico de colas (descriptivo, sobre libros ya vistos)
Sobre los libros L/S de r52 de X1 y X2, tal cual (50 monedas, quintiles, inverso a la vol, semanal), en 2021-05-24 → 2024-12-31:
- **Contribución corta por moneda-semana:** c = w (< 0) × Σ retornos diarios simples de la semana (la contabilidad de `r52_xs.simulate`).
- **Colas:** el 1%, 2% y 5% de moneda-semanas cortas con c más negativo. Se reporta su aporte a la pérdida total de la pata corta y el Sharpe del libro si esas moneda-semanas valieran 0 (solo descriptivo).
- **Alcanzable por stop:** para cada moneda-semana de la cola, con entrada = cierre del domingo de formación y σ_sem = `vol30` diaria × √7, se recorre el cierre 1h hasta el domingo siguiente. Si algún cierre 1h ≥ entrada × (1 + 2σ_sem), lo evitable es (retorno final − retorno en ese primer cierre)·|w|; si no, 0.
- **Hacinada:** la suma de funding de los 7 días hasta la formación es < 0.
- **Crédito por moneda-semana:** la pérdida entera si es hacinada; si no, lo evitable.
- **Compuerta de corte (preregistrada):** con la cola del 2% y sumando X1 y X2, **la línea L/S sigue si Σ crédito / Σ pérdida ≥ 0,50**. Si no, F1 y F2 no corren, N no se mueve y la ronda cierra con F0b.

### 1.3 Herramientas para un libro transversal
- **CV año × mitad (8 pliegues).** Las 48 alts se ordenan por `vol24h`; cada par consecutivo reparte una a cada mitad con permutación de semilla 60. La lista va a `data/r60/cv_halves.json` y se commitea antes de calcular. En el pliegue (mitad h, año y): el libro K se arma solo con monedas de h en el año y. Los puntajes de X1/X2 para h se reentrenan walk-forward con las monedas ∉ h (la otra mitad más BTC y ETH), con el mismo código de r52; L0 no se entrena.
- **Rotación transversal.** La serie semanal de puntajes de cada moneda se desfasa en forma circular con un desfase independiente por moneda, uniforme entre 13 semanas y el largo de su tramo con puntaje menos 13. Rompe el alineamiento entre monedas y conserva la persistencia. Estadístico: Sharpe del libro K. 1.000 rotaciones, semilla 60, p = (1 + #{≥ observado}) / 1.001.
- **Calibración con placebos:** 100 placebos, cada uno un AR(1) gaussiano por moneda con la autocorrelación semanal media de los puntajes X1, con 200 rotaciones cada uno. La fracción con p < 0,10 tiene que caer en [0,03, 0,17] (banda binomial al 95% con 100 placebos alrededor de 0,10). Si cae fuera, se reporta y p2 queda como descriptivo.
- **Modo `schema` del oráculo** (sin presupuesto, como `count_q1`): para cada moneda de H devuelve solo el número de columnas del 1h, el primer y último día y si hay funding. Ningún precio ni retorno.
- **Criterio q2** en `r59_criteria.py`, con selftest sobre un holdout falso (24 alts de U50, semilla 60) que cumple los mismos cuatro puntos del selftest de r59.

## 2. F0b: sondeo de unlocks (N + 0)
- Fuentes gratis candidatas: DefiLlama (unlocks/emissions), CryptoRank, páginas públicas de Token Unlocks, datasets públicos en GitHub y la documentación de tokenomics de cada proyecto.
- Para las 48 alts de U50 desde 2021: cobertura por moneda, campos disponibles (fecha, tamaño en % de la oferta circulante y total, tipo cliff/lineal, destinatario) y concordancia entre dos fuentes en una muestra de 10 eventos.
- **No se carga ningún precio ni retorno alrededor de los eventos.** Solo calendario, en `data/r60/unlocks/`. Lo bajado se trata como datos no confiables.

## 3. F1: diseño en U50 (solo si pasa la compuerta 1.2; N 145 → 148)

### 3.1 Construcción K (fija, sin barrido)
- Formación el domingo al cierre UTC, como r52, con la elegibilidad de r52 (≥ 90 días listada, mediana 30 d de volumen ≥ 10 M USDT, ≥ 10 elegibles). Solo las 48 alts.
- **Patas:** quintil superior largo e inferior corto (q = ⌈n/5⌉), pesos inversos a `vol30` dentro de cada pata, bruto 0,5 por pata.
- **Cortos hacinados fuera:** del quintil inferior se sacan las monedas con funding de 7 d < 0 y el 0,5 se reparte entre las que quedan. Si no queda ninguna, la pata corta queda vacía esa semana.
- **Neutral a beta:** β = `beta60` de r52 (60 días contra BTC) al cierre de formación; la cobertura es −(Σ w_i β_i) en el perpetuo de BTC. Un β faltante vale 1.
- **Stop de la pata corta:** si un cierre 1h supera entrada × (1 + 2σ_sem) (σ_sem = `vol30` × √7), la posición se cierra en ese cierre con 5 bps de slippage adverso más el fee, y queda en cash hasta la próxima formación (sin re-entrada, la cobertura de BTC no se reajusta en la semana).
- **Contabilidad:** pesos como fracciones constantes del capital dentro de la semana (simplificación de r52); funding real diario en las dos patas y en BTC (el corto lo cobra si es positivo); costo (0,045% + 2 bp) × rotación en cada formación y en cada stop. Estrés: costos ×2.
- **Escala:** la manga se compara con R1 a igual vol ex post (la escala no cambia el Sharpe). No hay vol objetivo dinámica: sería otra pieza a ajustar.
- **Capacidad (descriptiva):** el capital máximo con el que toda posición queda ≤ 1% de la mediana 30 d del volumen diario; se reporta la mediana semanal y el percentil 10.

### 3.2 Variantes (+1 N cada una)
- **L0, control simple:** puntaje = −rango del retorno de 1 semana (reversión; el signo que dio X0 en r52), con K.
- **L1:** puntajes X1 de `data/r60/scores.npz`, con K.
- **L2:** puntajes X2 de `data/r60/scores.npz`, con K.

### 3.3 Puertas en D (2021-05-24 → 2024-12-31), todas preregistradas
- **p1:** en la CV año × mitad, mediana del Sharpe por pliegue > 0 y ≥ 5 de 8 pliegues con Sharpe > 0;
- **p2:** rotación transversal p < 0,10;
- **g1:** Sharpe neto ≥ 0,8;
- **g2:** con costos ×2, Sharpe ≥ 0,4;
- **g3:** Sharpe de 2024 > 0;
- **g4:** las 20 alts más antiguas (primer dato ≤ 2020-07-01), libro K solo con ellas: Sharpe > 0;
- **g5:** las 5 mejores semanas < 60% del PnL semanal sumado (y PnL > 0);
- **g6:** ρ diaria con R1 ≤ 0,3 y con P-r55 ≤ 0,3 (`BENCH_R1_common`, `BENCH_P55_common`);
- **g7:** en los trimestres bajistas de BTC (etiqueta A de r55, k = 0,5: 2021Q2 desde el 2021-05-24, 2022Q2 y 2024Q2), retorno sumado de la manga ≥ 0 y ρ diaria con R1 en esos días ≤ 0,3;
- **g8:** R1 + manga a igual riesgo (pesos fijos 50/50 sobre series escaladas a igual vol) → ΔSharpe ≥ +0,15 sobre R1 en los días comunes.
- **Selección:** entre las variantes que pasan todo, la de mayor Sharpe neto en D. Si ninguna pasa, F2 no corre.
- Cada variante guarda su serie (`r59.save_series('r60', 'R60_F1_L<k>', …)`) y se registra en `TRIAL_REGISTRY.json`.

## 4. F2: confirmación en H (q2; N + 0)
- **Poder antes de consultar:** EE del Sharpe anual en la ventana de H con la fórmula de Lo (2002), usando el sesgo y la curtosis diarios del libro elegido en D. Poder = Φ((½·S_D − 0,4) / EE). Si es < 0,4, F2 no consulta y se reporta (precedente r59, y el usuario delegó la decisión: con poder < 0,4 no se gasta la consulta).
- **Criterio q2** (α 0,05, commiteado antes de consultar). Libro K de la variante elegida, construido solo con monedas de H (patas) y BTC de U50 (cobertura), con los modelos entrenados walk-forward en U50 (las 50 de r52) aplicados a las features de H rankeadas dentro de H; ventana 2021-07-02 → 2024-12-31:
  - (a) Sharpe neto − 0,4 > 0, con escala el EE bootstrap estacionario (bloque 20, 1.000 réplicas);
  - (b) Sharpe con costos ×2 > 0, misma escala;
  - (c) 0,3 − ρ diaria con R1 > 0, con escala el EE bootstrap de ρ;
  - (d) ΔSharpe de R1 + manga (50/50 a igual vol) sobre R1 − 0,1 > 0, con escala su EE bootstrap.
  - Ruido Laplace(0, 0,1·s) sobre cada margen, como en r59. Respuesta PASA / NO PASA.
- **Aunque pase, nada se congela.** La incorporación a la cartera y el uso de 2025 los decide el usuario.

## 5. F3: cierre (N + 0)
- SPA vs cash y vs R1 sobre la familia transversal del almacén (R52_F1_X0–X3, R53_F1_Y1–Y6, R55_F2_ML1–ML2) más L0–L2 si corrieron, en la intersección de días. PBO si hay ≥ 8 miembros con serie común.
- Informe de cierre, handoff a r61 y `DOCS.md`.

## 6. Advertencias declaradas antes de los resultados
1. D (U50, 2021-05→2024) ya se usó para el ranking en r52, r53 y r55. Los puntajes X1/X2 son los mismos.
2. Sesgo de supervivencia en U50 y H: en un L/S favorece a los largos y perjudica a los cortos (faltan las deslistadas, que habrían sido buenos cortos).
3. El poder de q2 para un Sharpe es bajo (EE ~0,55 en 3,5 años): q2 es un cribado, no una prueba de significancia.
4. Los trimestres bajistas en D son tres, uno parcial: g7 es ruidosa y así se declara.

## 7. Enmiendas
(ninguna)
