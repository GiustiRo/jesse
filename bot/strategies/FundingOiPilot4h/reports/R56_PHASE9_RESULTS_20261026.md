# r56-B F9: horizonte de 40 días (2026-10-26)

**N_régimen: 33 → 38** (P1–P5, registradas en `b495c205` junto con la enmienda F9-1, antes de correrlas). La N de estrategias sigue en 140; N2 y el holdout no se tocaron. A todas se les aplicó el estabilizador St2 (histéresis), según la regla fija. Embargo de 80 días. Datos: `data/r56/f9.json`.

## Resultados (desarrollo / 2024)
| Config. | Eje (40 días) | BSS | Exactitud balanceada | Cambios/año (etiqueta) | Calibración | Por año |
|---|---|---|---|---|---|---|
| P1 Chronos-Bolt, 40 pasos | vol | **+0,158 / +0,192** (p 0,004 / 0,002) | 0,38 / 0,43 | 5,1 (9,4) / **15,0 (14,0)** | 0,20–0,95 / 0,56–2,98 | 2021 +0,15 · 2022 +0,11 · 2023 +0,20 |
| P2 K1 a 40 días | vol | +0,129 / +0,198 | 0,36 / 0,44 | 5,6 / 25,8 (14,0) | baja | — |
| P3 A3 | tendencia | −0,022 / +0,073 | 0,50 / 0,50 | 0 | — | 2021 −0,12 |
| P4 WK-means (C3) | tendencia | +0,052 (p < 0,001) / +0,049 | **0,50 / 0,50** | 0 | 1,4–1,7 | 2021 +0,01 · 2022 +0,06 · 2023 +0,06 |
| **P5 A3** | **rango** | **+0,137 (p < 0,001) / +0,163 (p 0,03)** | **0,59 / 0,72** | **15,0 (30,0) / 23,8 (28,5)** | **0,95 / 1,11** | **2021 +0,12 · 2022 +0,14 · 2023 +0,14** |

## Lectura
1. **El rango a 40 días es el hallazgo nuevo más sólido de r56-B.** Con indicadores clásicos (P5) da +0,14 en desarrollo y +0,16 en 2024:
   - estable año a año (a 20 días, A3 tenía años negativos o casi nulos);
   - en el 94% y el 91% de las monedas;
   - bien calibrado (0,95 y 1,11);
   - su estado cambia la mitad que la etiqueta.
   - En la métrica de anticipación empata con la persistencia (20 contra 20): con la clase objetivo «sale del rango», la persistencia ya está en ese estado la mayor parte del tiempo, así que esta métrica casi no discrimina en este eje (limitación declarada).
2. **La vol a 40 días con Chronos (P1) rinde tan bien o mejor que a 20 días** (+0,158 / +0,192). Su estado estabilizado cambia 15,0 veces por año en 2024, contra un tope de 1,058 × 14,0 = 14,8: lo excede por muy poco. Como el estado operable no puede cumplir el criterio 4a en 2024, no queda elegible para F10. La clase media está mal calibrada en 2024.
3. **La tendencia sigue sin poder pronosticarse en un horizonte mensual.** P4 supera a la climatología por +0,05 de forma consistente, pero nunca predice «tendencia» (exactitud balanceada 0,50): la mejora viene de ajustar la probabilidad base, no de detectar tramos de tendencia.

## Selección prevista para F10 (regla de la extensión; la decide `select_f10` cuando termine T3)
- vol: Z1T (T1 con confirmación);
- rango: A3 a 20 días;
- rango a 40 días: P5;
- tendencia: C3 y P4 (cumplen el tope de cambios de forma trivial, porque su estado no cambia nunca).

Vol a 40 días queda sin candidato. T3 (Chronos-2 con covariables) todavía está calculando y puede cambiar la elección en vol.
