# r55 F1: motor cripto por régimen (2026-10-26)

**Resultado:** ninguno de los 3 ensayos pasa. P1 sigue sin cambios y 2025 sigue sellado. N pasa de 125 a 128.

- Protocolo: `PROTOCOL_R55.md` F1, con la enmienda post-F0 (`97bbc3da`).
- Los ensayos se registraron antes de correrlos (`18c8f081`).
- Script: `research_scripts/r55_engine.py`. Todo está cortado al 2024-12-31.

**Reproducción:** E2 con escalar 1 en todos los estados da exactamente P1, en las dos ventanas. P1 queda en Sharpe 1,677 / 1,605, como en F0 y en r52 J1.

## Resultados
| Versión | Ventana | CAGR | DD | Sharpe | Trim. + | Alcistas (suma / mediana / +) | Bajistas | Laterales |
|---|---|---|---|---|---|---|---|---|
| P1 | 2018-09+ | 41,2% | −14,3% | 1,677 | 19/26 | +212% / +15,7% / 9 de 9 | +13,2% / −1,3% / 2 de 5 | +29,6% / +1,9% / 8 de 11 |
| P1 | 2021–24 | 29,2% | −14,0% | 1,605 | 11/16 | +95% / +18,1% / 6 de 6 | +16,9% / +3,0% / 2 de 3 | −2,3% / −1,1% / 3 de 7 |
| E1 C6 como núcleo | 2018-09+ | 35,5% | −15,0% | 1,541 | 19/26 | +154% / +8,7% / 8 de 9 | **+31,0% / +1,1% / 3 de 5** | +33,6% / +4,0% / 8 de 11 |
| E1 | 2021–24 | 31,1% | −15,7% | **1,672** | 10/16 | +80% / +15,9% / 5 de 6 | +30,0% / +6,8% / 2 de 3 | **+5,4%** / −0,7% / 3 de 7 |
| E2 R1 cripto por régimen | 2018-09+ | 42,7% | −14,3% | **1,721** | 18/26 | +213% / +15,6% / 9 de 9 | +17,3% / −0,9% / 2 de 5 | +32,1% / +2,2% / 7 de 11 |
| E2 | 2021–24 | 29,8% | −14,3% | 1,645 | 11/16 | +91% / +16,4% / 6 de 6 | +18,9% / +3,6% / 2 de 3 | +0,8% / −1,9% / 3 de 7 |
| E3 seguro B2-BTC | 2018-09+ | 40,5% | **−13,1%** | 1,658 | 19/26 | +208% / +14,3% / 9 de 9 | +18,5% / +2,0% / 3 de 5 | +24,4% / +1,2% / 7 de 11 |
| E3 | 2021–24 | 28,0% | −14,4% | 1,563 | 11/16 | +91% / +16,3% / 6 de 6 | +20,0% / +2,4% / 3 de 3 | −5,4% / −1,1% / 2 de 7 |

## Puertas
| Ensayo | Bajistas | Laterales (con 2021–24) | Alcistas ≥ 80% | Inclusión r51 | Pasa |
|---|---|---|---|---|---|
| E1 | ✓ | ✓ | ✗ (73%) | ✗ (ΔSharpe −0,136 en 2018-09+; +0,067 en 2021–24) | no |
| E2 | ✗ (mediana −0,9%) | ✓ | ✓ | ✗ (ΔSharpe +0,044 y +0,040, contra +0,05; −1 trimestre positivo) | no |
| E3 | ✓ | — | ✓ | — | no: DD +1,2 pp en 2018-09+ y −0,4 pp en 2021–24 (pide +1,5 pp en las dos); ΔSharpe −0,02 y −0,04 |

**Vista mensual** (informativa): suma / meses positivos.

| Versión | Bajistas 2018-09+ | Laterales 2018-09+ | Bajistas 2021–24 | Laterales 2021–24 |
|---|---|---|---|---|
| P1 | −15,6% / 4 de 16 | +5,4% / 14 de 30 | −13,3% / 3 de 12 | −6,2% / 5 de 16 |
| E1 | **−2,5% / 8 de 16** | **+17,9% / 15 de 30** | −2,8% / 5 de 12 | +3,3% / 6 de 16 |
| E2 | −9,3% / 7 de 16 | +4,7% / 14 de 30 | −9,0% / 5 de 12 | −6,2% / 6 de 16 |
| E3 | −10,3% / 7 de 16 | +4,4% / 13 de 30 | −9,7% / 5 de 12 | −7,7% / 6 de 16 |

**Retorno por año, 2018-09+:**

| Año | P1 | E1 | E2 | E3 |
|---|---|---|---|---|
| 2018 | −7,0% | −6,2% | −6,5% | −5,0% |
| 2019 | +83,7% | +72,6% | +88,3% | +82,7% |
| 2020 | +49,0% | **+19,1%** | +47,6% | +47,1% |
| 2021 | +63,2% | +63,3% | +63,2% | +60,8% |
| 2022 | −2,7% | −0,3% | −1,3% | −0,9% |
| 2023 | +37,6% | +33,4% | +36,0% | +35,5% |
| 2024 | +56,0% | +59,8% | +62,2% | +52,3% |

**Manga de seguro de E3:** −3,5% en 2018-09+ (Sharpe −0,23) y −3,7% en 2021–24 (Sharpe −0,38). Hace 41 y 28 rebalanceos.

## Lectura
1. **E1 es el único que cumple lo que se busca en los regímenes difíciles**, pero lo paga en los alcistas.
   - Sin R1 cripto, los meses bajistas pasan de −15,6% a −2,5%, y los laterales de +5% a +18%.
   - En 2021–24 el Sharpe sube a 1,67 (+0,07).
   - El costo: R1 cripto es lo que capturó los alcistas de 2019–2020 (2020: +49% → +19%). En los alcistas retiene 73%, contra el piso de 80%, y el Sharpe de 2018-09+ cae 0,14.
   - Es un intercambio, no una mejora.
2. **E2 es el mejor en Sharpe (+0,04 en las dos ventanas), pero no llega a la puerta**: le falta mejorar en +0,05, la mediana de los trimestres bajistas sigue negativa y pierde un trimestre positivo.
   - Coincide con F0: la señal B llega tarde a los bajistas, así que recorta R1 en los laterales, donde ayuda, y menos en los bajistas.
   - **No se rescata.**
3. **E3 confirmó la expectativa previa baja.** El seguro pierde por sí solo, porque B lo enciende en los laterales. Reduce el DD de 2018-09+ en 1,2 pp, pero empeora el de 2021–24.
4. **Conclusión:** con los tres ensayos de F1, ninguna regla sobre R1 cripto ni la cobertura de la señal B convierte a P1 en un motor que no pierda en los bajistas sin resignar alcistas.
   - La palanca con más efecto en los regímenes difíciles es quitar R1 cripto (E1).
   - Lo que falta para compensar los alcistas tendría que venir de F2: la pata ML o C6 seleccionado por el ranking.
   - Probar un punto intermedio entre E1 y E2 sería un vecino de dos ensayos fallados; no se propone.

## Efecto en el plan
- F4.1 (motor cripto armado) queda sujeto a F2: ninguna pieza de F1 entra.
- El ensayo «R1 sin bono» de F4 se mantiene.

## Archivos
- `research_scripts/r55_engine.py`.
- `research_scripts/data/r55/f1_engine.json`.
