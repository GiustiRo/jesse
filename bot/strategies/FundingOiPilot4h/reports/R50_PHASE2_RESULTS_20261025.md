# r50 F2: cartera escalada a vol 17% (2026-10-25)

**Veredicto:** la cartera final **C0 + C6** cumple 7 de las 9 puertas r9.

| Ventana | CAGR | DD | Sharpe | DSR (N=81) | Meses + | Trimestres + |
|---|---|---|---|---|---|---|
| Común (2021-03 → 2025) | 34,2% | −14,5% | 1,81 | 0,96 | 56% | 75% (15/20) |
| Larga (2018-09 → 2025) | 39,0% | −15,0% | 1,72 | 0,998 | 64% | 77% |

- **Fallan solo las de regularidad:** meses positivos (56% contra la meta de 65%) y trimestres positivos (75% contra 80%).
- Es el mejor resultado de cartera de r49–r50 y el primero que cumple CAGR, DD y DSR a la vez.
- **Corridas Jesse:** 0 de 10. **N declarado: 81.**

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE2_PROTOCOL.md`, commiteado antes del código (`2fd4b92d`).
- Pesos de riesgo inverso con vol expansiva.
- Vol objetivo 17% con covarianza expansiva y techo k ≤ 8.
- Rebalanceo mensual, sin freno de DD.
- Inclusión greedy: C0 → C6 → N4.

## Inclusión

| Paso | Sharpe sin / con | Trimestres + sin / con | Veto largo | Decisión |
|---|---|---|---|---|
| C0 (base) | — / 1,77 | — / 65% | no | base |
| + C6 | 1,77 / 1,81 | 65% / **75%** | no | **entra** |
| + N4 | 1,81 / 1,69 | 75% / 75% | no | no entra |

**Pesos finales:** C0 65%, C6 35%. **Factor k medio:** 5,0 en la común y 4,5 en la larga; el techo de 8 se alcanzó en 0% y 8% de los días.

## Puertas r9

| Puerta | Común | Larga (2018-09+) |
|---|---|---|
| CAGR ≥ 30% | ✓ 34,2% | ✓ 39,0% |
| DD ≤ 20% | ✓ −14,5% | ✓ −15,0% |
| PF ≥ 1,2 | ✓ 2,74 | ✓ 2,76 |
| Meses + ≥ 65% | **✗ 56%** | ✗ 64% |
| Trimestres + ≥ 80% | **✗ 75%** | ✗ 77% |
| Mediana mensual > 0 | ✓ +0,46% | ✓ +0,68% |
| Positiva sin los 2 mejores meses | ✓ +164% | ✓ +511% |
| DSR ≥ 0,95 (N=81) | ✓ 0,96 | ✓ 0,998 |

**Por año:**

| Ventana | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Común | — | — | — | +52,3% | −2,8% | +56,1% | +42,6% | +26,1% |
| Larga | −10,5% | +91,1% | +30,6% | +52,4% | +1,8% | +50,5% | +56,7% | +33,5% |

La vol realizada es 17,0% en la común y 20,3% en la larga.

## Carteras de un componente (misma construcción)

| Componente | Ventana | CAGR | DD | Sharpe | Meses + | Trimestres + | DSR |
|---|---|---|---|---|---|---|---|
| C0 | común | 36,4% | −16,3% | 1,77 | **68%** | 65% | 0,93 |
| C0 | larga 2011+ | 14,0% | −17,2% | 1,27 | 63% | 68% (59) | 0,99 |
| C6 | común | 24,8% | −10,6% | 1,43 | 31% | 60% | 0,80 |
| C6 | larga 2018+ | 29,0% | −13,6% | 1,24 | 34% | 53% | 0,91 |
| N4 | común | 16,1% | −22,7% | 0,98 | 61% | 55% | 0,38 |
| N4 | larga 2011+ | 12,7% | −23,1% | 0,91 | 58% | 63% | 0,85 |

- C0 solo cumple M65 (68%) pero no Q80.
- En 2011–25, C0 da 14% de CAGR: su k medio es 2,7, porque la vol estimada de 2011–13 es alta y diluye el escalado. Sus años negativos son 2014 (−0,8%), 2015 (−4,7%) y 2018 (−6,6%).

## Límites y advertencias
1. **Selección in-sample:** la asignación de C0 se eligió mirando F1/F1b, así que el DSR de 0,96 es optimista. F3 lo pone a prueba en activos no vistos.
2. **Ventana larga de la cartera final:** cubre solo 2018-09 → 2025, porque C6 depende de cripto spot y la cartera usa los días comunes a sus componentes. La historia 2011–2017 solo se ve en C0 solo.
3. **Cripto pesa mucho en el resultado:** C6 más la parte cripto de C0 suman cerca del 44% del riesgo inicial. Los años 2019–2021 de cripto explican buena parte del CAGR largo.
4. **Fills:** son del arnés, no de Jesse. F4 los confirma.
5. **Topes de r49:** con k ≈ 5, el riesgo por trade de las mangas con stop queda debajo del 0,5% del equity y el nocional por activo debajo de 1,5x. Ambos quedan dentro de los topes, pero no se modeló el margen aislado real.

## Siguiente paso
F3 según el roadmap:
- se congelan los motores (R1, R2, R3, M2a, N1), la asignación por clase y la construcción;
- se corren sobre los activos de validación: plata, Nasdaq, cobre, EWJ y EWY.
