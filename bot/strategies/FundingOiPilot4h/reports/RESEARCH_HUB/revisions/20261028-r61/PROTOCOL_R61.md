# PROTOCOL_R61: libro de asimetría neutral (variante de C6)

**Fecha:** 2026-10-28. **Rama:** `exploration/gpt-6.1-sol`. **Código:** `research_scripts/r61.py`. Este protocolo se commitea antes de cualquier resultado económico de r61.

## 0. Decisiones del usuario y presupuesto
- **Funding como entrada (regla r49):** se prueban dos variantes. **A** = solo rupturas (respeta r49). **B** = rupturas + largo en las alts con funding 7 d < 0, como **enmienda de r49 válida solo para esta manga**.
- **Lugar en el historial:** el libro es una **variante de C6** (continuación de rupturas en alts) y hereda su historial de selección (g9, g10 y el margen (e) de q3).
- **N = 148 al empezar; techo de r61: 151.** Suman N solo A y B (F1, una por variante). q3 no suma. Queda 1 de reserva para una enmienda.
- **Oráculo:** quedan 4 consultas; r61 usa como máximo una (q3).
- 2025 sellado y 2026 reservado. Sin live ni paper. No se bajan monedas. Todo se calcula en el contenedor descartable `salehmir/jesse` con el checkout en `/src`. Toda serie va a `r59.save_series('r61', …)`.

## 1. El libro
**Panel y universo:** los de r60 (`r60.Panel`, `r60.dev_panel()`). Las patas son las 48 alts de U50 y la cobertura es el perpetuo de BTC. Las formaciones son las filas semanales elegibles de `Panel.S` (la misma elegibilidad que K, sin pedir puntaje), con d0 = cierre del domingo y d1 = el cierre de formación siguiente.

**Tamaño por nombre (sin parámetros nuevos).** En cada formación, con las n alts elegibles y q = ⌈n/5⌉:

u_i = 0,5 · inv_i / (q · media_j inv_j), con inv = 1 / `vol30_raw` (NaN → mediana, mínimo 1e-4).

Es el tamaño típico de un nombre dentro de una pata de K.

**Pata de ruptura (A y B).**
- **Disparo:** el primer cierre 1h en (d0, d1] con c ≥ C_d0 · (1 + 2·σ_sem), donde σ_sem = vol30(d0)·√7. Es el mismo disparo que `r60.stop_path`.
- **Entrada:** largo u_i al precio c·(1 + 5 pb), pagando COST.
- **Retorno del día de entrada:** C_día / (c·1,0005) − 1. Los días siguientes usan el retorno diario normal.
- **Salida:** al cierre de d1.
- **En B**, la pata se aplica solo a las alts que no están en la pata de funding, igual que K, que nunca corta las hacinadas.

**Pata de funding (solo B):** largo u_i toda la semana en las alts con fund7(d0) < 0.

**Cobertura:** corto en BTC por β_i·u_i para cada posición, desde el momento en que se abre.
- β = `beta60` en d0 (NaN → 1).
- Para la ruptura, el retorno de BTC del día de entrada se mide desde el cierre 1h de BTC de la hora del disparo.

**Costos y funding:**
- Costo COST (r52) por unidad de rotación, contando la cobertura.
- En la formación, la rotación es |w_inicio − w_fin_semana_previa|; las entradas intrasemana se cobran en su día.
- El funding diario se cobra sobre los pesos vigentes. El del día de entrada se cuenta entero, la misma aproximación declarada en r60.

**Forma límite (solo para la aserción del §2.2):** la cobertura de cada formación queda fija en d0 (−Σ_{funding} q/n·u_i·β_i en B; 0 en A), sin COST, con los pesos escalados por q/n.

## 2. F0: código, aserción, solapamiento y selftests (N + 0)
1. Este protocolo se commitea primero. Después, en un solo commit antes de F1: `r61.py`, el criterio q3 en `r59_criteria.py` y `r61.py` más este protocolo en `TRACKED` de `r59_oracle.py`.
2. **Aserción del límite (`r61.py assert_limit`, semilla 61).**
   - **Comparación:** la forma límite contra la media de 400 corridas de `FastBook.run` con puntajes uniformes al azar (patas al azar), `cost_mult=0`. A se compara contra `crowded=False` y B contra K completa.
   - **Exige:** correlación diaria ≥ 0,95 y |media anualizada de la diferencia| ≤ 10% de |media anualizada del límite|.
   - **Si falla:** se corrige el código, nunca la cota, antes de cualquier resultado económico.
   - **Descriptivo:** el Sharpe del libro operable y el de la media de K.
3. **Solapamiento con C6 (descriptivo).** `BENCH_C6ALTS` es la canasta equiponderada de C6 congelado en las 48 alts (`r58.c6_bank('u50')` + `r50_f1b.basket`, cortada al 2024-12-31). Se reportan:
   - la ρ diaria de A y B con esa canasta, con R1 y con P-r55;
   - la fracción de disparos del libro que caen en una semana con un trade de C6 abierto en la misma moneda.
4. **Selftests:**
   - `r60.py q2_selftest` (plantilla, no corrido en r60);
   - `r61.py q3_selftest`, con los cuatro puntos del selftest de r59 sobre el holdout falso: mitad 1 de `data/r60/cv_halves.json`, con la mitad 0 como banco de entrenamiento de C6alts.

## 3. F1: diseño en D (48 alts, 2021-05-24 → 2024-12-31; N +2: `R61_F1_A`, `R61_F1_B`)
Una variante pasa si cumple **todas** las puertas.
- **g1–g8, como en r60** (`r60.gates_of`):
  - g1: Sharpe neto ≥ 0,8;
  - g2: con costos ×2, Sharpe ≥ 0,4;
  - g3: Sharpe de 2024 > 0;
  - g4: el libro solo con las 20 alts más antiguas (`r60.old20`), Sharpe > 0;
  - g5: las 5 mejores semanas < 60% del PnL;
  - g6: ρ con R1 y con P-r55 ≤ 0,3;
  - g7: en los trimestres bajistas, suma ≥ 0 y ρ con R1 ≤ 0,3;
  - g8: R1 + manga (50/50 a igual vol) con ΔSharpe ≥ +0,15.
- **p1, CV año × mitad:** las mitades de `data/r60/cv_halves.json` × 2021–2024, libro solo con las monedas de cada mitad. Mediana del Sharpe por pliegue > 0 y ≥ 5 de 8 pliegues > 0.
- **p2', placebo de timing (reemplaza la rotación de r60; semilla 61, 500 sorteos).**
  - **Sorteo:** en cada semana se toman tantas entradas de ruptura como tuvo el libro, con (moneda, hora) al azar: monedas sin reposición entre las elegibles (en B, entre las que no están en la pata de funding) y la hora uniforme entre los cierres 1h de (d0, d1]. Los u_i, la cobertura, el slip y COST son los mismos.
  - **En B**, la pata de funding también se sortea: el mismo número de monedas, la semana entera, elegidas antes que la pata de ruptura.
  - **Mismo motor:** libro y placebos se evalúan con el mismo motor simplificado (costos de entrada y salida por posición, sin netear entre semanas).
  - **p** = (1 + #{placebo ≥ libro}) / 501. Pasa con p < 0,10.
  - **Descriptivo:** el sorteo de solo la hora con las mismas monedas. Tiene sesgo de anticipación, porque esas monedas se eligieron por haber subido 2σ.
  - **Control mecánico:** 100 libros placebo, cada uno contra 200 sorteos. La fracción con p < 0,10 tiene que caer en [0,03, 0,17]. Por intercambiabilidad debería cumplirse por construcción, así que verifica el cómputo del p, no el tamaño frente a una nula estructurada. Si cae fuera, p2' queda como descriptivo.
- **g9 (variante de C6):** R1 + C6alts + libro (tercios sobre series escaladas a igual vol) contra R1 + C6alts (mitades a igual vol), días comunes. ΔSharpe ≥ +0,10.
- **g10 (herencia de selección):** Deflated Sharpe (`r50_f1b.dsr`, varianza del estimador 1/T) en D con **N = 11** ≥ 0,90. N = 11 son los 9 ensayos de C6 en alts más A y B:
  - **regla:** id o hipótesis con «C6» y universo de alts;
  - **de `trials`:** R54_W1, R54_M1, R55_F2_ML3, R55_F2_ML4, R57_Q1, R57_Q2, R58_F2_CONF y R58_F3_I1;
  - **además:** R54_V1, que está en `r54_v1_validation`.
- **Descriptivo:** capacidad (posición ≤ 1% del volumen diario), atribución por pata (ruptura, funding, cobertura) y CAGR/DD/vol.

**Regla de selección para q3:**
- Si no pasa ninguna variante, q3 no se consulta.
- Si pasa una, se consulta esa.
- Si pasan las dos, se consulta **una sola**: la de mayor ΔSharpe en g9, es decir, la que más suma sobre R1 + C6alts.
- **Precisión respecto del plan:** el plan aprobado decía «Holm si pasan las dos». Los márgenes del oráculo no son pruebas a un nivel α (son estadístico − umbral, más ruido), así que Holm no es aplicable. La multiplicidad se paga en D con g10 y se declara.

## 4. F2: confirmación en H = N2 ∪ N3 (q3; N + 0)
- **Poder antes de consultar:** EE anual de Lo (2002) en la ventana de H, con el sesgo y la curtosis diarios del libro elegido en D. Poder = Φ((½·S_D − 0,4) / EE). Si es < 0,4, no se consulta y se reporta.
- **Criterio q3** (en `r59_criteria.py`, commiteado antes de consultar). El libro de la variante elegida se arma solo con las monedas de H como patas y BTC de U50 como cobertura. C6alts(H) es la canasta de C6 congelado sobre las monedas de H (`r58.c6_bank('n2')` ∪ `('n3')`). Ventana 2021-07-02 → 2024-12-31. Márgenes con EE bootstrap estacionario (bloque 20, 1.000 réplicas, semilla 61) y ruido Laplace(0; 0,1·s):
  - (a) Sharpe − 0,4;
  - (b) Sharpe con costos ×2;
  - (c) 0,3 − ρ diaria con R1;
  - (d) ΔSharpe R1 + manga (50/50 a igual vol) − 0,1;
  - (e) ΔSharpe de R1 + C6alts(H) + manga (tercios) contra R1 + C6alts(H) − 0,05.

  La respuesta es PASA / NO PASA.
- **Advertencia:** q0 (r58 F2) ya usó H para rupturas de C6 en alts y pasó. H no es independiente para esta familia, así que un PASA en q3 es un cribado condicionado a q0, no una confirmación limpia.
- **Aunque pase, nada se congela.** La integración en P-r55 y el uso de 2025 los decide el usuario.

## 5. F3: cierre (N + 0)
- SPA contra cash y contra R1, más la combinación R1 + miembro contra R1, sobre la familia de C6 en alts con serie en el almacén (R54_W1, R54_M1, R55_F2_ML3, R55_F2_ML4, R57_Q1, R57_Q2, R58_F3_I1) más A y B, en la intersección de días. PBO si hay ≥ 8 miembros.
- Informe de cierre, handoff a r62, `DOCS.md`, `index.json` del Hub y `TRIAL_REGISTRY.json`.

## 6. Advertencias declaradas antes de los resultados
1. **Post hoc:** el mecanismo salió de la rotación de r60 en D. F1 en D es casi la misma evidencia, y el peso real está en q3.
2. **Supervivencia:** el sesgo de supervivencia de U50 y H favorece a un libro largo más que a un L/S. La cobertura beta lo atenúa, pero no lo elimina.
3. **B y r49:** B choca con r49. Si solo pasa B, la conclusión depende de una regla que el historial vetó sin probarla aislada.
4. **Poder:** con ~3,5 años de H, el EE del Sharpe es ~0,55, así que el poder para un efecto de la mitad del de D es bajo.
5. **Promedio contra libro:** el promedio de Sharpe de K sobre rotaciones (1,12) no es el Sharpe del libro promedio. El libro concentra la exposición en pocos nombres y su Sharpe puede quedar lejos de 1,12 hacia cualquiera de los dos lados.
6. **Cobertura:** en K la cobertura se fija en la formación y no cubre el largo implícito después del stop. El libro operable sí lo cubre, así que difiere de la forma límite en eso.

## 7. Enmiendas
(ninguna)
