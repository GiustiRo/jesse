# r50 F1c: asignación por clase y 6 familias nuevas (2026-10-25)

**Veredicto:** pasan **C0** (cartera por clase) y **C6** (ensamble de rupturas cripto R2 + R3).

| Candidata | Común: Sharpe / DSR | Larga: Sharpe / DSR |
|---|---|---|
| C0 | 1,82 / 0,95 | 1,07 / 0,95 |
| C6 | 1,53 / 0,88 | 1,47 / 0,98 |

- Las demás candidatas no pasan.
- **C3** (comprar y mantener SPX + oro con tamaño por vol): Sharpe 1,40 y 80% de trimestres positivos en la común, pero la veta el DD largo de −27,6%.
- **N declarado: 80. Corridas Jesse: 0 de 10.**

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1C_PROTOCOL.md`, commiteado antes del código (`dc15e14c`).

**Advertencia de selección:** la asignación de C0 y la elección de C6 se decidieron mirando F1/F1b, así que en el núcleo son evidencia in-sample. La prueba honesta será F3, con la regla de clase en activos no vistos:
- acciones → Nasdaq, EWJ y EWY;
- metales → plata y cobre.

Cripto y energía no tienen activos de validación.

## Canastas (equiponderadas; Sharpe de calendario √365)

| Candidata | Activos | Común: Sharpe | CAGR | DD | Trim. + | Top-5 / PnL | R1, mismos activos (Sharpe / Trim. +) | Larga: Sharpe / DD / Trim. + | DSR común / larga |
|---|---|---|---|---|---|---|---|---|---|
| **C0 por clase** | 7 | **1,82** | 5,5% | −2,5% | 70% | 34% | 0,99 / 55% | **1,07 / −12,6% / 69%** | **0,95 / 0,95** |
| C1 momentum diario cripto | BTC, ETH | 0,62 | 6,9% | −15,3% | 55% | 103% | 0,61 / 45% | 1,11 / −14,3% / 52% | 0,14 / 0,74 |
| C2 momentum 12-1 | 7 | 0,81 | 5,2% | −9,3% | 50% | 392% | 0,99 / 55% | 0,54 / −20,9% / 54% | 0,26 / 0,36 |
| C3 comprar y mantener por vol | SPX, oro | 1,40 | 22,1% | −19,0% | 80% | n/a | 1,40 / 75% | 0,92 / **−27,6%** / 69% | 0,75 / 0,87 |
| C4 ruptura diaria CFD | 5 CFD | 0,41 | 0,5% | −1,9% | 45% | 196% | 0,89 / 60% | 0,17 / −8,8% / 33% | 0,06 / 0,04 |
| C5 tendencia + retroceso 4h | 7 | 0,78 | 7,6% | −15,9% | 60% | 102% | 0,99 / 55% | 0,63 / −22,0% / 59% | 0,24 / 0,50 |
| **C6 rupturas cripto R2 + R3** | BTC, ETH | **1,53** | 8,6% | −3,4% | 65% | 39% | 0,61 / 45% | **1,47 / −4,9% / 55%** | **0,88 / 0,98** |

Los CAGR de C0 y C6 son bajos porque promedian mangas de riesgo chico (1% por trade, o vol 17% con exposición parcial). El escalado a vol de cartera corresponde a F2. Como referencia aritmética, no un resultado: a vol 17%, el Sharpe 1,82 de C0 implicaría un CAGR del orden del 30%; F2 lo mide con la construcción prerregistrada.

## Puertas (PHASE1C_PROTOCOL.md §3)

| Candidata | Sharpe | Top-5 < 60% | Mejora a R1 (mismos activos) | Veto largo | Resultado |
|---|---|---|---|---|---|
| C0 | ✓ 1,82 > 0,99 y trimestres + 70% ≥ 55% | ✓ 34% | — | no | **pasa** |
| C1 | ✗ 0,62 | ✗ | ✓ | no | no pasa |
| C2 | ✓ 0,81 | ✗ | ✗ | no | no pasa |
| C3 | ✓ 1,40 | n/a | ✓ (trimestres +) | **sí** (−27,6%) | no pasa |
| C4 | ✗ 0,41 | ✗ | ✗ | no | no pasa |
| C5 | ✗ 0,78 | ✗ | ✓ | no | no pasa |
| C6 | ✓ 1,53 | ✓ 39% | ✓ | no | **pasa** |

## Por activo (Sharpe común / larga)

| Activo | R1 | R2 | R3 | C1 | C2 | C3 | C4 | C5 | M2a | N1 |
|---|---|---|---|---|---|---|---|---|---|---|
| BTC | 0,62 / 1,22 | 1,18 / 1,21 | 0,95 / 1,02 | 0,21 / 0,85 | 0,59 / 0,84 | — | — | 0,26 / 0,91 | — | — |
| ETH | 0,50 / 0,89 | 1,26 / 1,10 | 1,24 / 1,24 | 0,89 / 1,13 | −0,22 / 0,57 | — | — | 0,47 / 0,67 | — | — |
| Oro | 1,31 / 0,76 | — | — | — | 1,33 / 0,52 | 1,15 / 0,60 | 0,22 / 0,18 | 1,03 / 0,46 | — | — |
| SPX | 0,80 / 0,64 | — | — | — | 0,79 / 0,58 | 0,94 / 0,80 | 0,15 / 0,14 | 0,93 / 0,71 | 0,88 / 0,34 | — |
| WTI | 0,06 / −0,09 | — | — | — | −0,08 / −0,18 | — | 0,12 / −0,13 | 0,10 / 0,09 | 0,55 / 0,14 | 0,61 / 0,35 |
| Gas | 0,33 / 0,06 | — | — | — | 0,04 / 0,18 | — | 0,48 / 0,20 | 0,23 / −0,03 | 0,23 / 0,47 | 0,44 / 0,33 |
| Bono (sin larga) | −1,29 | — | — | — | −0,47 | — | −0,38 | −0,92 | — | — |

## Lectura
1. **La diversificación entre clases es la palanca más fuerte.**
   - C0 combina reglas modestas: cada manga tiene Sharpe de 0,5 a 1,3.
   - Con 7 activos poco correlacionados, la cartera llega a 1,82 en la común y 1,07 en la larga, con 70% de trimestres positivos.
   - La concentración (34%) está bien repartida.
   - Es la primera candidata de r50 con DSR ≥ 0,95 en las dos ventanas (N=80), aunque in-sample por la selección.
2. **Las rupturas cripto (C6) son el bloque más sólido y estable entre ventanas:** 1,53 en la común y 1,47 en la larga desde 2018, con DD −3 a −5% al riesgo de 1% por trade.
3. **El bono resta en todas las reglas.** Ninguna regla probada le da Sharpe positivo.
   - En C0 entra con R1 por defecto y pesa en contra.
   - Sacarlo sería una decisión mirando resultados, así que no se hace aquí y queda para la F2 o para el usuario.
4. **Comprar y mantener SPX + oro (C3) es un piso exigente:** Sharpe 1,40 en 2021–25. La lente larga muestra su costo (DD −27,6% en 2013–15).

## Candidatas para F2
- **N4** de F1b: R1 + M2a.
- **C0**: cartera por clase.
- **C6**: rupturas cripto.

F2 las escalaría a vol de cartera 17% y mediría las puertas r9 (CAGR, DD, M65, Q80) y el DSR en las dos ventanas. **No se avanza a F2 sin la decisión del usuario.**
