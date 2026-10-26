# r56-B F8: mejor pronóstico de vol (2026-10-26)

**N_régimen: 28 → 33.** Las configuraciones H1, H2, K1, O1 y T3 se registraron en `1b59a374` antes de correrlas. La N de estrategias sigue en 140. N2 y el holdout no se tocaron.

- **Estado operable:** todas usan el estabilizador St2 (histéresis), fijado antes de F8. El parámetro se elige por trimestre con los 4 trimestres anteriores.
- **Tope de cambios del criterio 4a** (1,048 × los cambios de la etiqueta): 18,6 por año en desarrollo y 22,5 en 2024.
- **Datos:** `data/r56/f8.json`.

## Resultados (desarrollo / 2024)
| Config. | BSS | RPS (clim. 0,472 / 0,506) | Exactitud balanceada | Cambios/año | Anticipación (modelo − persistencia, días) | Por año (dev) |
|---|---|---|---|---|---|---|
| T1 (referencia, F4) | +0,136 / +0,218 | 0,394 / 0,376 | — | (Z1T: 12,4 / 19,0) | (Z1T: −1 / +1) | 0,22 · 0,03 · 0,17 |
| H1 HExp | +0,131 / +0,208 | 0,398 / 0,380 | 0,39 / 0,53 | 14,3 / **26,4** | −4 / +4 | 0,23 · 0,04 · 0,15 |
| H2 HExpGl | +0,132 / +0,208 | 0,398 / 0,380 | 0,39 / 0,53 | 14,9 / **26,3** | −5 / +4 | 0,24 · 0,04 · 0,15 |
| K1 T1 + H2 | +0,127 / **+0,222** | 0,401 / **0,373** | 0,38 / 0,55 | 12,5 / **25,3** | −6 / +2 | 0,24 · 0,03 · 0,14 |
| O1 ordinal | +0,112 / +0,182 | 0,405 / 0,389 | 0,36 / 0,49 | 12,7 / 15,7 | −7 / +3 | 0,21 · 0,03 · 0,12 |
| **T3 Chronos-2 + covariables** | **+0,139 / +0,215** | **0,393 / 0,377** | **0,42 / 0,55** | **12,9 / 21,4** | **+6 / +3** | **0,20 · 0,05 · 0,18** |

- Las cinco tienen DM p ≤ 0,0005 contra la mejor vara en los dos períodos, y BSS positivo en el 91–100% de las monedas.
- La persistencia da un RPS de 0,61 y 0,62: muy por debajo de cualquier modelo.

## Lectura
1. **HExp (H1 y H2) reproduce la literatura.** Una regresión lineal con cuatro EWMA queda a ~0,005 de BSS de Chronos-Bolt. El factor global no agrega nada. Su estado estabilizado, sin embargo, cambia 26 veces por año en 2024 y excede el tope.
2. **La combinación K1 da el mejor 2024 (+0,222)**, pero no mejora el desarrollo y también excede el tope en 2024. Combinar Chronos con HExp no suma información: los dos miden casi lo mismo.
3. **El ordinal O1 respeta el orden de las clases, pero rinde peor** en BSS, RPS y calibración de la clase media en desarrollo. La logística multinomial ya ordena bien sola.
4. **T3, con BTC y la vol global como covariables, es la mejor configuración de vol de r56:**
   - el mejor BSS en desarrollo (+0,139) y el mejor RPS;
   - 2022, el peor año, sube de +0,03 a +0,05;
   - es la única con anticipación positiva en desarrollo: detecta los cambios 6 días antes que la persistencia;
   - su estado queda bajo el tope en los dos períodos (21,4 contra 22,5 en 2024).
   - Por la regla de la extensión (mejor promedio de BSS entre desarrollo y 2024 que cumpla 4a en ambos), **T3 reemplaza a Z1T como candidata de vol para F10**: 0,1772 contra 0,1766. La diferencia es mínima y se declara así.
5. **La calibración sigue siendo el punto débil de todas.** La pendiente de la clase media es ~0,8 en desarrollo y ~1,9 en 2024; la de la clase alta, 0,3–0,4 en desarrollo. El criterio 4c (0,7–1,3) no lo cumple ninguna configuración de vol. Queda anotado como el próximo paso natural: recalibración isotónica o por temperatura, hacia adelante.

## Selección para F10 (`select_f10`, definitiva)
| Eje | Configuración |
|---|---|
| vol | **T3** |
| tendencia | C3 |
| rango | A3 |
| tendencia a 40 días | P4 |
| rango a 40 días | P5 |

- **Vol a 40 días:** sin candidata (P1 excede el tope en 2024).
- **T3 en N2:** sus pronósticos se generan solo para las 20 columnas nuevas. Las 50 primeras del panel de 70 son idénticas a las del panel original, y las covariables usan solo esas 50, así que esos pronósticos serían los mismos. El script lo verifica con una aserción.
