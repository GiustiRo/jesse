# r55 F0: regímenes de BTC y mapa de P1 por régimen (2026-10-26)

Fase descriptiva: no suma a N, que sigue en 125. Todo está cortado al 2024-12-31; 2025 sigue sellado.

Protocolo: `RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md` (`1570f73f`), commiteado antes de este cálculo. Script: `research_scripts/r55_regimes.py`.

**Reproducción.** P1 da lo mismo que en r52 J1:
- 2018-09 → 2024: CAGR 41,2%, DD −14,3%, Sharpe 1,677;
- 2021 → 2024: Sharpe 1,605.

La ventana común arranca el 2021-02-28, igual que en J1, así que 2021Q1 entra con un mes (declarado).

**Lo que no se calculó a propósito:** el retorno de P1 separado por estado B. Escalar R1 cripto por estado B es el ensayo E2, y ese corte adelantaría su resultado.

## A. Etiqueta trimestral (k = 0,5), 2018Q4 → 2024Q4
- **9 alcistas, 5 bajistas y 11 laterales.** El lateral es la clase más frecuente.
- El umbral u_q va de 23,5% (2018Q4) a 10,9% (2024Q1), porque sigue a la vol de BTC.

| Trimestre | BTC | Clase | P1 |
|---|---|---|---|
| 2018Q4 | −44% | bajista | −7,0% |
| 2019Q1 | +11% | lateral | +1,9% |
| 2019Q2 | +165% | alcista | +80,5% |
| 2019Q3 | −24% | bajista | −2,5% |
| 2019Q4 | −13% | lateral | +2,4% |
| 2020Q1 | −11% | lateral | +6,5% |
| 2020Q2 | +43% | alcista | +1,8% |
| 2020Q3 | +18% | lateral | +17,4% |
| 2020Q4 | +169% | alcista | +17,0% |
| 2021Q1 | +103% | alcista | +11,0% |
| 2021Q2 | −40% | bajista | +20,6% |
| 2021Q3 | +25% | alcista | +15,2% |
| 2021Q4 | +6% | lateral | +5,7% |
| 2022Q1 | −2% | lateral | +5,9% |
| 2022Q2 | −56% | bajista | −1,3% |
| 2022Q3 | −3% | lateral | −4,9% |
| 2022Q4 | −15% | lateral | −2,0% |
| 2023Q1 | +72% | alcista | +24,1% |
| 2023Q2 | +7% | lateral | 0,0% |
| 2023Q3 | −12% | lateral | −4,2% |
| 2023Q4 | +57% | alcista | +15,7% |
| 2024Q1 | +69% | alcista | +37,4% |
| 2024Q2 | −12% | bajista | +3,3% |
| 2024Q3 | +1% | lateral | +0,8% |
| 2024Q4 | +48% | alcista | +9,0% |

**Los 6 trimestres negativos de P1 en 2018-09 → 2024:**
- 3 bajistas: 2018Q4, 2019Q3 y 2022Q2;
- 3 laterales: 2022Q3, 2022Q4 y 2023Q3;
- más 2023Q2 en cero, también lateral.

## P1 por clase de trimestre
| Ventana | Clase | n | Suma | Mediana | Positivos | R1/BTC | R1/ETH | C6 | R1/oro | R1/SPX | Resto R1 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2018-09 → 2024 | alcista | 9 | +211,7% | +15,7% | 9 | +46,3% | +26,1% | +93,2% | +6,9% | +13,7% | +1,0% |
| | bajista | 5 | +13,2% | **−1,3%** | 2 | −5,5% | −1,0% | +9,7% | +3,7% | −3,5% | +9,4% |
| | lateral | 11 | +29,6% | +1,9% | 8 | +1,1% | +2,1% | +16,7% | +10,9% | +3,2% | −3,7% |
| 2021 → 2024 | alcista | 6 | +94,8% | +18,1% | 6 | +18,2% | +9,0% | +49,9% | +4,4% | +9,7% | −2,6% |
| | bajista | 3 | +16,9% | +3,0% | 2 | −3,4% | +0,9% | +10,4% | 0,0% | +1,7% | +7,3% |
| | lateral | 7 | **−2,3%** | **−1,1%** | 3 | −2,7% | −3,8% | +5,3% | +3,8% | −0,3% | −4,1% |

- Las columnas por manga son la suma de los aportes diarios de cada una a la cartera, como en r51 F2.
- «Resto R1» agrupa WTI, gas y bono.

**Sensibilidad mensual** (no decide):

| Ventana | Clase | Meses | Suma | Mediana | Positivos |
|---|---|---|---|---|---|
| 2018-09 → 2024 | bajista | 16 | −15,6% | −1,0% | 4 |
| 2018-09 → 2024 | lateral | 30 | +5,4% | 0,0% | 14 |
| 2021 → 2024 | bajista | 12 | −13,3% | −1,1% | 3 |
| 2021 → 2024 | lateral | 16 | −6,2% | −0,7% | 5 |

## B. Estado operable T90 (±0,5, 1 día de demora), 2018-09 → 2024
- Días en cada estado: 44% alcista, 26% bajista y 31% lateral.
- **147 cambios en 6,3 años (~23 por año).** El estado cambia seguido cerca de los umbrales. ML2 lo absorbe con su rebalanceo semanal; en E2 la aproximación ignora los fees.

| Año | Alcista | Bajista | Lateral |
|---|---|---|---|
| 2018 (sep–dic) | 0% | 47% | 53% |
| 2019 | 43% | 35% | 22% |
| 2020 | 59% | 2% | 39% |
| 2021 | 63% | 22% | 15% |
| 2022 | 0% | 69% | 31% |
| 2023 | 54% | 9% | 37% |
| 2024 | 58% | 11% | 32% |

**Coincidencia entre capas** (fracción de los días de cada clase A que el estado B pone en cada estado):

| Clase A (trimestre) | Días | B alcista | B bajista | B lateral |
|---|---|---|---|---|
| alcista | 821 | **74%** | 8% | 19% |
| bajista | 457 | 36% | **36%** | 28% |
| lateral | 1.006 | 24% | 37% | **39%** |

## Lectura
1. **La debilidad de P1 está más en los laterales que en los bajistas.**
   - En 2018-09 → 2024, P1 suma +13% en los trimestres bajistas, aunque con mediana negativa (−1,3%).
   - En 2021–24, los laterales son la única clase negativa: −2,3%, con 3 de 7 positivos.
   - La vista mensual muestra pérdidas también en los meses bajistas (−15,6%).
2. **R1 cripto resta en bajistas y en los laterales recientes; C6 suma en todas las clases.**
   - R1/BTC + R1/ETH: −6,5% en bajistas (2018-09+) y −6,5% en laterales (2021–24).
   - C6: +9,7% en bajistas y +16,7% en laterales.
   - Confirma el diagnóstico de r51 y le da sentido a E1 y E2.
3. **El oro compensa en bajistas y laterales.** El resto de R1 (WTI, gas y bono) suma en bajistas, pero resta en laterales.
4. **La señal causal B llega tarde a los bajistas.**
   - En los trimestres bajistas, B dice «bajista» solo el 36% de los días, y «alcista» otro 36%: el trimestre suele empezar con el estado todavía en alcista.
   - En los alcistas acierta el 74%.
   - **No se ajusta:** sería post-hoc. Es una limitación conocida de E2, E3 y ML2 antes de correrlos.
5. **Vara de las puertas de régimen**, sobre P1 en 2018-09 → 2024. El motor nuevo necesita:
   - bajistas: suma ≥ +13,2% y mediana ≥ 0 (P1 hoy no la cumple: −1,3%);
   - laterales: suma ≥ +29,6% y mediana ≥ 0;
   - alcistas: suma ≥ 169% (80% de 211,7%).

## Archivos
- `research_scripts/r55_regimes.py`.
- `research_scripts/data/r55/f0_regimes.json`.
- `research_scripts/data/r55/f0_states.npy`: estado B aplicado por día (gitignored; se regenera).

## Siguiente paso
F1 (E1–E3), F2 (ML1–ML4) y F3 (A3 v2), con los ensayos registrados en `TRIAL_REGISTRY.json` antes de leer sus resultados.
