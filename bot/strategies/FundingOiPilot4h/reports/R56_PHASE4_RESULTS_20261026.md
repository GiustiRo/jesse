# r56 F4: modelos globales, salida de rango y modelos fundacionales (2026-10-26)

**N_régimen: 17 → 22** (G1, G2, X1, T1 y T2, registradas en `babb334f` antes de correrlas). La N de estrategias sigue en 140 y el holdout no se tocó.

**Cómo se calcularon T1 y T2:** Chronos corrió en un entorno virtual aislado del contenedor (`/opt/chronos-venv`, torch CPU y chronos-forecasting 2.3.2, autorizados por el usuario), sin tocar el entorno principal. Script: `r56_chronos.py`. Fueron 72.095 pronósticos zero-shot por modelo, con log-RV diaria hasta t como contexto. Datos: `data/r56/f4.json`.

## BSS (desarrollo / 2024), p de Diebold–Mariano y cambios por año
| Config. | Y_vol | Y_trend | Y_range | Y_exit |
|---|---|---|---|---|
| G1 logística global (~148 variables) | **−0,114** / +0,242 | −0,058 / +0,011 | +0,054 / **+0,159** (p 0,009) | — |
| G2 gradient boosting global | **−0,169** / +0,245 | −0,028 / −0,002 | +0,038 / +0,158 (p 0,018) | — |
| X1 dirección de salida de rango | — | — | — | +0,147 (p 0,018) / **−0,142** (n = 1.994 / 1.033) |
| **T1 Chronos-Bolt zero-shot** | **+0,136 (p 0,0005) / +0,218 (p 0,0005)** · 23–41 cambios/año | — | — | — |
| T2 Chronos-2 zero-shot | +0,133 (p 0,0005) / +0,209 (p 0,0005) · 23–42 cambios/año | — | — | — |
| (referencia: V1 HAR, F3) | +0,114 / +0,210 · 43–54 cambios/año | | | |

**SPA final sobre las 22 configuraciones (desarrollo):**
- vol **0,0005**;
- tendencia < 0,001;
- rango 0,060;
- salida 0,018.

En 2024: vol < 0,001, tendencia 0,002, rango 0,030 y salida 0,33.

## Lectura
1. **Los modelos fundacionales zero-shot son el mejor pronóstico de vol de r56.** T1 supera a HAR en desarrollo (+0,136 contra +0,114) y lo iguala en 2024 (+0,218 contra +0,210):
   - positivo los 4 años (2021 +0,22, 2022 +0,03, 2023 +0,17, 2024 +0,22) y en el 97% de las monedas de desarrollo;
   - el estado operable cambia la mitad de veces que con HAR (23 contra 43 por año);
   - sin entrenar ningún parámetro, salvo la logística de calibración.
   - Chronos-2 (más grande y ~4 veces más lento) no mejora a Bolt.
   - El sesgo de los pronósticos (+0,29–0,33 en log) lo absorbe la calibración.
2. **Los modelos globales sobreajustan:**
   - con todas las variables juntas, la vol en desarrollo cae a −0,11 y −0,17, aunque 2024 sea excelente;
   - las relaciones entre variables cambian de un año a otro (2021 −0,40);
   - el gradient boosting con hiperparámetros fijos no rinde mejor que la logística.
3. **La dirección de salida del rango (X1) no es estable:** da +0,15 en desarrollo y −0,14 en 2024, sobre muestras chicas. No hay evidencia de que Wyckoff-lite o los banderines anticipen hacia dónde sale el precio.
4. **Tendencia:** los modelos globales tampoco la mejoran.

## Selección para F5 (enmienda F5-1, fijada antes de estos resultados)
La mejor configuración por eje, según el BSS promedio entre desarrollo y 2024, con ambos > 0:
- **vol: T1** (0,177);
- **tendencia: C3** (0,029);
- **rango: G1** (0,106; A3 queda segundo con 0,100).
