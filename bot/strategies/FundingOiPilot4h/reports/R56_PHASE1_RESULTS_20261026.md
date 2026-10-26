# r56 F1: clásicos y memoria (2026-10-26)

**N_régimen: 0 → 5** (A1, A2, A3, B1 y B2, registradas en `e07a376c` antes de correrlas). La N de estrategias sigue en 140 y el holdout no se tocó.

**Cómo se evaluó:**
- 34 monedas de desarrollo y walk-forward trimestral con embargo de 40 días;
- desarrollo 2021-07 → 2023-12, y 2024 como validación temporal;
- BSS contra la mejor vara, que en los tres ejes resultó ser la climatología.

Todas las familias pasaron la prueba de no mirar el futuro: brecha 0 en 20 fechas de corte. Script: `r56_eval.py run F1`; datos: `data/r56/f1.json`.

## BSS (desarrollo / 2024) y p de Diebold–Mariano
| Config. | Y_vol | Y_trend | Y_range |
|---|---|---|---|
| T90 (vara r55, sin costo) | −0,037 / +0,047 | +0,008 / +0,017 | +0,015 / +0,003 |
| A1 tendencia clásica | −0,042 / +0,047 | +0,004 / +0,029 | +0,021 / +0,082 (p 0,03) |
| **A2 compresión clásica** | **+0,073 (p 0,027) / +0,149 (p 0,004)** | +0,025 / +0,028 | +0,029 / +0,079 |
| A3 = A1 + A2 | +0,035 / +0,165 (p 0,012) | +0,001 / +0,033 | **+0,069 (p 0,025) / +0,132 (p 0,020)** |
| B1 varianza relativa y autocorrelación | −0,062 / −0,049 | +0,013 / +0,020 | −0,008 / +0,018 |
| B2 Hurst DFA | −0,058 / −0,026 | +0,023 (p 0,003) / +0,029 (p 0,0005) | +0,024 (p 0,02) / +0,007 |

**SPA sobre las 5 configuraciones:**

| Eje | Desarrollo | 2024 |
|---|---|---|
| vol | 0,052 | 0,015 |
| tendencia | 0,007 | 0,0005 |
| rango | 0,069 | 0,057 |

## Lectura
1. **La compresión es pronosticable con indicadores clásicos.** A2 le gana a la climatología en vol con BSS +0,07 en desarrollo y +0,15 en 2024. Es positiva en el 88% de las monedas en desarrollo y en el 100% en 2024. Además anticipa las transiciones a vol alta: mediana de +6 días, contra −14 de la persistencia.
   - Su punto débil es 2022 (−0,03), el año del colapso de LUNA y FTX.
   - Sumarle las variables de tendencia (A3) empeora la vol en desarrollo, lo que sugiere sobreajuste.
2. **El rango también tiene señal.** A3 da +0,069 en desarrollo y +0,132 en 2024, positivo los 4 años y en 79–94% de las monedas, con exactitud balanceada de 0,60–0,66. Es el detector más estable de F1.
3. **La tendencia a 20 días casi no se puede pronosticar con estos indicadores.** El mejor BSS es +0,02–0,03 y la exactitud balanceada queda en 0,50, porque el estado operable nunca predice «tendencia». B2 (Hurst) es estadísticamente significativo, pero muy chico.
4. **La memoria (B) no aporta en vol ni en rango.** T90 queda como vara floja en los tres ejes.
5. **Usabilidad:** el estado operable cambia demasiado. A2 cambia 26–43 veces por año en vol y A3 23–28 en rango, contra el límite de ≤ 12 del puente. Las calibraciones de vol y rango quedan en 0,5–1,2.
6. **Contra el puente:** nada cumple todavía el criterio 1 en desarrollo (BSS ≥ +0,05 con SPA p < 0,05). A2 vol tiene BSS +0,073 con SPA de 0,052, y A3 rango +0,069 con SPA de 0,069.

## Siguiente
**F2:** jump models continuo y sparse, Wasserstein k-means, HMM filtrado (vara) y BOCPD.
