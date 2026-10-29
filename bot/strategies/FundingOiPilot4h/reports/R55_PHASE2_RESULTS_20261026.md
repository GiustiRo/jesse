# r55 F2: monetización del ranking ML (2026-10-26)

**Resultado:** ninguno de los 4 ensayos pasa. P1 sigue sin cambios y 2025 sigue sellado. N pasa de 128 a 132.

ML3 (C6 en las alts del top-10) cumple la regla de inclusión y supera a V1 por amplio margen, pero falla la puerta de régimen bajista. **No se rescata.**

- Protocolo: `PROTOCOL_R55.md` F2, con los detalles de implementación fijados antes de correr y los ensayos registrados (`dad565de`).
- Script: `research_scripts/r55_ml.py`.
- Métricas hasta el 2024-12-31.

**Reproducciones:**
- el puntaje X1 da el mismo IC de desarrollo que r52 (0,1060);
- C6 en alts con multiplicador 1 da exactamente las 48 curvas de V1.

## ML1 y ML2: libro largo top-10 cubierto con BTC (desarrollo 2021-05-24 → 2023-12)
| Ensayo | Sharpe | CAGR | DD | Costos ×2 | 2024 | Old20 | ρ P1 | Bajistas (suma, + / n) | Laterales | Alcistas | Top-5 semanas | Pasa |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ML1 | 0,24 | 1,9% | −46% | 0,16 | 0,00 | −0,15 | 0,03 | +34% (2/2) | −9,6% (3/6) | −9,2% (2/3) | 351% del PnL | no |
| ML2 | −0,46 | −12,9% | −49% | −0,56 | −0,29 | −0,51 | 0,03 | −4,9% (0/1) | −13,9% (1/6) | −10,3% (2/3) | PnL ≤ 0 | no |

**Puertas que falla cada uno:**
- ML1: Sharpe ≥ 0,5, old20, laterales y top-5.
- ML2: todas salvo ρ.

**Lectura**
- La cobertura con BTC (β medio 0,9) convierte al libro en «largo alts, corto BTC». Gana en los bajistas (+34%) y pierde en los alcistas y laterales.
- Apagarlo en los bajistas (ML2) le saca justo lo único que ganaba.
- Peor que Y4 (0,49): cubrir solo con BTC y concentrar en 10 monedas no ayuda.
- El PnL depende de 5 semanas, y en las 20 monedas antiguas es negativo.

## ML3 y ML4: el ranking aplicado a C6 en las alts
**Canasta de alts, desde la primera semana con puntaje (2021-05-24) hasta 2024:**

| Variante | Sharpe | CAGR | DD | Trades |
|---|---|---|---|---|
| V1 (C6 sin filtro) | 0,85 | 1,7% | −2,4% | 2.454 |
| **ML3** (solo top-10) | **1,31** | 1,0% | −0,5% | 429 |
| ML4 (riesgo por rango) | 0,99 | 2,1% | −2,4% | 2.454 |

**Dentro de P1**, reemplazando la mitad del riesgo de C6 (C6' = 0,5·C6 + 0,5·alts escaladas a la vol de C6):

| Versión | Ventana | CAGR | DD | Sharpe | Trim. + | Bajistas (suma / mediana / +) | Laterales | Alcistas |
|---|---|---|---|---|---|---|---|---|
| P1 | 2018-09+ | 41,2% | −14,3% | 1,677 | 19/26 | +13,2% / −1,3% / 2 de 5 | +29,6% / +1,9% / 8 de 11 | +212% |
| P1 | 2021–24 | 29,2% | −14,0% | 1,605 | 11/16 | +16,9% / +3,0% / 2 de 3 | −2,3% / −1,1% / 3 de 7 | +95% |
| **ML3** | 2018-09+ | 43,2% | −14,3% | **1,736** | 19/26 | **+10,1% / −2,2% / 2 de 5** | +30,5% / +1,9% / 8 de 11 | +225% |
| **ML3** | 2021–24 | 33,4% | −13,6% | **1,774** | 12/16 | +13,9% / +1,1% / 2 de 3 | −1,0% / +0,2% / 4 de 7 | +112% |
| ML4 | 2018-09+ | 40,0% | −14,7% | 1,637 | 17/26 | +8,9% / −2,4% / 2 de 5 | +24,3% / +1,9% / 6 de 11 | +216% |
| ML4 | 2021–24 | 27,5% | −16,2% | 1,554 | 9/16 | +12,6% / −0,2% / 1 de 3 | −7,7% / −2,0% / 2 de 7 | +99% |

**Puertas**
| Ensayo | Bajistas | Laterales (con 2021–24) | Alcistas ≥ 80% | Inclusión r51 | Alts ≥ V1 + 0,1 | Pasa |
|---|---|---|---|---|---|---|
| ML3 | **✗** (suma 10,1% < 13,2%; mediana −2,2%) | ✓ | ✓ | ✓ (ΔSharpe +0,059 / +0,169) | ✓ (1,31 vs 0,85) | **no** |
| ML4 | ✗ | ✗ | ✓ | ✗ (−0,040 / −0,051; −2 trim.) | ✓ (0,99 vs 0,85) | no |

**Retorno por año, 2018-09+:**

| Año | P1 | ML3 | ML4 |
|---|---|---|---|
| 2021 | +63,2% | +58,8% | +64,6% |
| 2022 | −2,7% | −1,6% | −6,4% |
| 2023 | +37,6% | +25,2% | +29,1% |
| 2024 | +56,0% | **+89,7%** | +61,9% |

**Vista mensual de ML3:**
- bajistas: −14,9%, 4 de 16 (P1: −15,6%, 4 de 16);
- laterales: +7,7%, 13 de 30 (P1: +5,4%, 14 de 30).

## Lectura de ML3 (por qué no se rescata, aunque es el resultado más interesante de r55)
1. **El ranking sí selecciona mejores rupturas de C6:** con 17% de los trades, la canasta de alts sube de Sharpe 0,85 a 1,31. Es la primera forma de cobrar el IC del ranking que funciona como señal.
2. **Falla la puerta bajista por 3,1 pp sobre 5 trimestres.** Los bajistas anteriores a 2021 son iguales en las dos versiones, así que la diferencia sale de 2021Q2, 2022Q2 y 2024Q2. Con tan pocos trimestres, la puerta es ruidosa. Pero estaba preregistrada, y cambiarla ahora sería un rescate.
3. **Tres razones para desconfiar del Sharpe de cartera, además de la puerta:**
   - **La mejora viene casi toda de 2024** (+89,7% contra +56%). En 2023 y 2021, ML3 rinde menos que P1. Y 2024 es el año que ya se había mirado con el ranking en r52/r53 (advertencia 1 del protocolo).
   - **La manga de alts tiene muy poco riesgo propio** (CAGR 1%, DD −0,5%): para igualar la vol de C6 se escala entre 7,3 y 12,7 veces (mediana 9,6). Un resultado así descansa en 429 trades escalados unas 10 veces.
   - El 2018-09+ mejora solo desde 2021: antes, ML3 es igual a P1.
4. **ML4**, que solo cambia tamaños sin filtrar, mejora la canasta (0,99), pero empeora la cartera. El valor está en no tomar las rupturas de las alts mal rankeadas, no en cambiar su tamaño.

## Conclusión de F2
- El IC del ranking se puede cobrar mejor como **filtro de rupturas** (ML3) que como libro direccional (ML1/ML2, Y4).
- No entra a cartera: falla la puerta bajista y su mejora se concentra en un año ya visto.
- **Para una ronda futura:** ML3 congelado tal cual, preregistrado con un fuera de muestra limpio. Usaría 2025 (sellado) o 2026 (reservado), y la decisión es del usuario.

## Efecto en el plan
- F4.1 (motor cripto armado) no tiene piezas: ni F1 ni F2 pasaron. Por el protocolo, ese ensayo no se corre y no suma a N.
- Quedan F3 (A3 v2) y, en F4, los 5 activos marginales, «R1 sin bono» y la cartera final.

## Archivos
- `research_scripts/r55_ml.py`.
- `research_scripts/data/r55/f2_ml.json`.
- `research_scripts/data/r55/f2_curves.npy` (gitignored).
- Log de la corrida: `research_scripts/data/r55/f2_run.log`.
