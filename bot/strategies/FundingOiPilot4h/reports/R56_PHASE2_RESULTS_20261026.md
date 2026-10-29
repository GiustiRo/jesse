# r56 F2: modelos de estados y quiebres (2026-10-26)

**N_régimen: 5 → 11** (C1a, C1b, C2, C3, C4 y D1, registradas en `65f20add` antes de correrlas). La N de estrategias sigue en 140 y el holdout no se tocó.

Todos los modelos de estados se reajustan en cada trimestre con datos anteriores al pliegue de las monedas de desarrollo, y producen probabilidades **solo filtradas** (causales). D1 pasó la prueba de no mirar el futuro (brecha 0). Datos: `data/r56/f2.json`.

## BSS (desarrollo / 2024), p de Diebold–Mariano y cambios por año del estado operable
| Config. | Y_vol | Y_trend | Y_range |
|---|---|---|---|
| C1a CJM, 2 estados | +0,001 / +0,037 · 5 cambios/año | +0,026 (p < 0,001) / +0,027 | +0,047 (p 0,018) / +0,018 · 7–8 cambios/año |
| C1b CJM, 3 estados | +0,039 / +0,116 (p 0,011) · 7–14 cambios/año | +0,021 / +0,028 | **+0,056 (p 0,03) / +0,025** · 8–15 cambios/año |
| C2 sparse JM | +0,024 / +0,130 (p 0,014) · 5–8 cambios/año | +0,006 / +0,030 | −0,008 / +0,003 |
| C3 Wasserstein k-means | **+0,063 (p 0,04) / +0,132 (p 0,02)** · 8–15 cambios/año | +0,040 (p < 0,001) / +0,017 | +0,062 (p 0,009) / +0,010 |
| C4 HMM filtrado (vara) | +0,057 / +0,087 · **35–68 cambios/año** | +0,036 / +0,019 | +0,035 / 0,000 · 38–101 cambios/año |
| D1 BOCPD | −0,031 / +0,007 | +0,023 / +0,024 | +0,020 / +0,021 |

**SPA acumulado (F1 + F2, 11 configuraciones):**

| Eje | Desarrollo | 2024 |
|---|---|---|
| vol | 0,076 | 0,019 |
| tendencia | < 0,001 | 0,001 |
| rango | **0,046** | 0,077 |

**λ elegido por log-loss dentro del pliegue:** casi siempre 10, el valor más bajo de la grilla. Solo dos pliegues eligieron 200, y en el último pliegue C1b eligió 50.

## Lectura
1. **Los jump models cumplen lo que promete la literatura en persistencia:**
   - el estado operable de C1/C2/C3 cambia **5–15 veces por año**, contra 23–43 de los clásicos de F1 y 35–101 del HMM filtrado;
   - es la primera familia que se acerca al límite de usabilidad del puente (≤ 12).
2. **En capacidad de pronóstico no superan a los clásicos.**
   - **En vol,** C3 (WK-means) iguala a A2: +0,063 y +0,132, contra +0,073 y +0,149.
   - **En rango,** C1b y C3 rinden bien en desarrollo (+0,056 y +0,062), pero caen en 2024 (+0,025 y +0,010), mientras A3 sube a +0,13.
3. **El HMM filtrado confirma por qué quedó como vara:** su capacidad es parecida a la de los demás, pero cambia de estado 3 a 7 veces más, lo que lo hace inoperable.
4. **La tendencia sigue sin poder pronosticarse:**
   - todos los modelos dan +0,02 a +0,04, con exactitud balanceada de 0,50;
   - el SPA es significativo porque la mejora es pequeña pero muy consistente, y no alcanza para operar.
5. **BOCPD no aporta como variable de régimen a 20 días.**
6. **Contra el puente:** sigue sin haber un detector que cumpla el criterio 1 completo.
   - Por un lado, el SPA de rango es 0,046 y C3 da +0,062, pero cambia 18 veces por año en 2024.
   - Por otro, los estados persistentes no tienen suficiente capacidad.
   - F4 prueba si combinarlos (G1/G2) resuelve el dilema.

## Siguiente
**F3:** HAR-RV (V1–V3), geometría (E1–E2) y signatures (S1).
