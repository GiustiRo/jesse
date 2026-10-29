# r56 F0: panel, etiquetas, varas, holdout y pruebas sintéticas (2026-10-26)

**N_régimen = 0 · N de estrategias = 140** (r56 no la mueve). 2025 sigue sellado y 2026 reservado. Protocolo: `RESEARCH_HUB/revisions/20261026-r56/PROTOCOL_R56.md`.

## Qué se hizo
- **Panel diario de las 50 monedas de U50** (2020-01 → 2024-12-31), armado desde barras de 1h, con RV intradía y ATR20. Corte duro con aserción: ninguna barra ni ventana de etiqueta cruza 2024 (`r56_panel.py`).
- **Etiquetas a 20 días** por moneda y día, más sus varas mínimas: persistencia y climatología.
- **Holdout de monedas:** 16 alts, una por cada triplete por fecha de listado, sorteadas con `default_rng(56)`. Son AAVE, ADA, AR, COMP, DASH, EGLD, GTC, ICP, IOST, LINK, OP, QNT, RLC, UNI, XRP y ZEN. Quedan intocables hasta F5.
- **Modelos en numpy** (`r56_models.py`): jump model de k estados, jump model continuo, BOCPD, signatures y Wasserstein k-means. Todos pasaron sus pruebas sintéticas.

## Umbrales (los fijó una regla escrita antes de mirar)
| Eje | Grilla → elegido | Proporción |
|---|---|---|
| Y_trend (eficiencia de Kaufman) | 0,25–0,45 → **0,30** | 31,7% tendencia |
| Y_range (±k·ATR20) | 2,0–4,0 → **3,0** | 45,7% rango |
| y_volchg (cociente, reportada) | ln 1,15–1,5 → **ln 1,5** | colas de 32,6% y 26,3% |
| Y_vol (nivel) | terciles fijos | 51,4% compresión / 27,4% media / 21,2% alta |

## Enmienda F0-1: la vol pasa de cociente a nivel
- **El problema:** la etiqueta del plan era ln(RV futura / RV pasada). La RV pasada aparece también en la vara de persistencia, así que la persistencia queda **anticorrelacionada por construcción**: exactitud balanceada de 0,23, debajo del azar.
- **Además,** con el cociente «compresión» significaba «la vol va a bajar» y no «la vol está baja».
- **El cambio:** se reemplazó por el tercil de la RV futura dentro del año previo de la propia moneda. Solo se miraron las monedas de desarrollo hasta 2023.

## Varas (desarrollo: 34 monedas, ventanas cerradas al 2023-12-31, ~32.700 moneda-días)
| Eje | Persistencia: exactitud balanceada | Persistencia: Brier | Persistencia: cambios/año | Climatología: exactitud balanceada | Climatología: Brier | Cambios/año de la etiqueta |
|---|---|---|---|---|---|---|
| Y_vol | **0,450** (azar 0,33) | 0,986 | 19,9 | 0,367 | 0,664 | 17,7 |
| Y_trend | 0,478 | 0,909 | 46,8 | 0,496 | **0,447** | 46,6 |
| Y_range | 0,440 | 1,111 | 38,4 | 0,482 | **0,517** | 38,7 |
| y_volchg | 0,235 | 1,488 | 32,0 | 0,312 | 0,684 | 31,9 |

**Lectura:**
1. **La vol por nivel tiene memoria real:** la persistencia supera claramente al azar. Esa es la vara que debe batir la familia V (HAR).
2. **Tendencia y rango a 20 días no tienen persistencia en cripto diario:**
   - cambian ~40–47 veces por año;
   - la ventana pasada predice peor que el azar, porque la eficiencia y el rango revierten entre ventanas consecutivas.
   - Para esos ejes, la vara efectiva es la climatología. Batirla es la pregunta abierta de r56.
3. **El Brier de la persistencia es alto porque es un pronóstico duro (0/1).** El BSS se mide contra la mejor vara de cada eje, que en tendencia y rango es la climatología.
4. **Sensibilidades** (proporciones con los mismos umbrales):
   - con H = 10 hay más tendencia (48%) y más rango (68%);
   - con H = 40, menos (17% y 23%).
   - Se reportan, pero no deciden.

## Pruebas sintéticas (`data/r56/f0_selftest.json`: pasa)
- **JM de k estados:** reproduce exactamente `r52_j1.fit`, con el mismo camino y el mismo objetivo.
- **Variables sin rezago:**
  - el JM acierta 0,981 en la muestra y 0,909 online;
  - el CJM acierta 0,995 en la muestra y **0,965 online**;
  - la penalización λ = 50 reduce los cambios de 436 a 18 frente a λ = 0.
- **Variables EWMA, que sí tienen rezago** (reportado): JM 0,889, JM online 0,822 y CJM online 0,861.
- **Otros modelos:**
  - JM de 3 estados: usa los 3 estados;
  - BOCPD: detecta 3 de 3 quiebres;
  - signatures: el nivel 1 y el área de Lévy son exactos y se cumple la identidad de Chen;
  - Wasserstein k-means: acierta 0,90.

## Siguiente
**F1:** clásicos (A1–A3) y memoria (B1–B2). Cada configuración se especifica en `TRIAL_REGISTRY.json → regime_trials` antes de correrla.

## Archivos
- Scripts: `research_scripts/r56_panel.py` y `r56_models.py`.
- Datos: `research_scripts/data/r56/` (`f0_labels.json`, `holdout.json`, `f0_selftest.json`; los `*.npz` están en gitignore y se regeneran).
