# r56 F3: HAR-RV, geometría y signatures (2026-10-26)

**N_régimen: 11 → 17** (V1, V2, V3, E1, E2 y S1, registradas en `74173b97` antes de correrlas). La N de estrategias sigue en 140 y el holdout no se tocó. E1, E2 y S1 pasaron la prueba de no mirar el futuro (brecha 0). Datos: `data/r56/f3.json`.

## BSS (desarrollo / 2024), p de Diebold–Mariano y cambios por año
| Config. | Y_vol | Y_trend | Y_range |
|---|---|---|---|
| **V1 HAR-RV agrupado** | **+0,114 (p 0,004) / +0,210 (p 0,0005)** · 43–54 cambios/año | — | — |
| V2 HAR + sección transversal | +0,013 / **+0,280** (p < 0,001) · 40–49 cambios/año | — | — |
| V3 HAR + Markov | +0,116 (p 0,004) / +0,211 · 43–50 cambios/año | — | — |
| E1 canal y caja | −0,029 / +0,034 | +0,006 / +0,023 | +0,029 / +0,074 (p 0,04) |
| E2 banderín y Wyckoff-lite | −0,044 / +0,054 | +0,004 / +0,024 | +0,024 / +0,066 (p 0,01) |
| S1 signatures, nivel 3 | −0,062 / +0,057 | −0,011 / +0,032 | +0,043 / +0,126 (p 0,04) · 50–68 cambios/año |

**SPA acumulado (F1–F3, 17 configuraciones):**

| Eje | Desarrollo | 2024 |
|---|---|---|
| vol | **0,011** | < 0,001 |
| tendencia | < 0,001 | 0,002 |
| rango | 0,054 | 0,028 |

## Lectura
1. **HAR-RV es el mejor detector de vol de r56 hasta ahora.** V1 mejora el Brier un 11% en desarrollo y un 21% en 2024:
   - positivo los 4 años (2021 +0,20, 2022 +0,01, 2023 +0,15, 2024 +0,21), en el 94% de las monedas en desarrollo y en el 100% en 2024;
   - anticipa las transiciones a vol alta por **+14 días** (+18 en 2024), contra −14 (+7) de la persistencia;
   - **es el primero que cumple el criterio 1 del puente:** BSS ≥ 0,05 con SPA de vol 0,011.
   - **Falla en usabilidad:** el argmax cambia 43–54 veces por año, contra el límite de ≤ 12. La calibración de la clase alta queda baja en desarrollo (0,36).
   - Coincide con la literatura: un modelo lineal sobre la RV intradía es la vara a batir.
2. **La sección transversal (V2) es inestable:** en 2024 es la mejor (+0,28), pero en desarrollo cae a +0,013 (2021 −0,27). Indica cambios de régimen en las relaciones entre monedas. No se la elige.
3. **El estado de Markov sobre la log-RV (V3) no agrega nada a V1.**
4. **Geometría (E1, E2):** señal chica y solo en rango (+0,07 en 2024). Wyckoff-lite y los banderines no aportan en vol ni en tendencia.
5. **Signatures (S1):** en rango llegan a +0,126 en 2024, pero son inestables (2022 −0,04) y cambian 50–68 veces por año. En vol son negativas en desarrollo.
6. **Tendencia:** ninguna familia de F3 la mejora.

## Siguiente
**F4:**
- G1 (logística global) y G2 (gradient boosting global) sobre todas las variables;
- X1 (dirección de salida del rango);
- T1 y T2 (Chronos-Bolt y Chronos-2, zero-shot sobre la vol).
