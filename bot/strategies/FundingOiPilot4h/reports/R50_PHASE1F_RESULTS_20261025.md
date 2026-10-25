# r50 F1f: repaso en futuros y tendencia sobre el universo amplio (2026-10-25)

**Veredicto:** ampliar la tendencia a 21–22 perpetuos operables **no mejora la cartera: la diluye.**
- **R1 amplio:** Sharpe 0,64 en la común (contra 0,99 de R1 en el núcleo) y **0,46 desde 2001**, debajo de la compuerta de 0,5.
- **Cartera P4 = R1 amplio + C6:** común con CAGR 21,9%, Sharpe 1,32 y DSR 0,66; larga (2018-09+) con CAGR 31,7%, Sharpe 1,43 y DSR 0,95.
  - En la común falla CAGR y DSR.
  - En la larga cumple CAGR y queda a 0,002 del DSR.
- **La mejor cartera operable en futuros sigue siendo P1 = R1 (7 activos del núcleo) + C6.** Tampoco pasa la ventana común (F1d).
- **N declarado: 94. Corridas Jesse:** 0 de 10.

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1F_PROTOCOL.md`, commiteado antes de bajar los datos nuevos (`0ca8b769`).

## 1. Repaso de r50 con la regla «solo futuros»
- **Sigue válido en futuros:**
  - todos los motores de tendencia, rupturas, reversión y rotación;
  - en cripto se probaron sobre perpetuos con funding real;
  - en TradFi, sobre CFD que hacen de proxy de los perpetuos TradFi de Binance.
- **Queda fuera:** el carry de funding (K1, K1r y P3), porque opera una pata en spot.
- **Sesgos declarados:**
  - en la ventana larga cripto se usa spot como proxy, sin funding, lo que favorece a los largos;
  - en los perpetuos TradFi se toma funding = 0, porque no hay historia.

| Hallazgo | Estado en futuros |
|---|---|
| La tendencia (R1) y las rupturas cripto (R2/R3) generalizan a activos no vistos (F3: 10 de 13) | ✓ válido |
| La reversión de corto plazo no generaliza (F3: 2 de 10, 7 derrumbes) | ✓ válido |
| C0 + C6 (F2: 34%, Sharpe 1,81) | válido en futuros, pero falló la validación por la reversión |
| P1 = R1 + C6 (F1d) | ✓ operable; pasa 2018+; falla 2021–25 |
| Carry de funding (F1e) | ✗ fuera de alcance (spot) |

## 2. R1 por mercado (Sharpe común / larga)

| Mercado | Común | Larga | Mercado | Común | Larga |
|---|---|---|---|---|---|
| BTC | 0,62 | 1,22 | IWM | 0,02 | 0,14 |
| ETH | 0,50 | 0,89 | EWZ | −0,42 | 0,11 |
| Oro | 1,31 | 0,76 | EWT | −0,38 | −0,04 |
| SPX | 0,80 | 0,64 | GDX | 0,36 | −0,03 |
| WTI | 0,06 | −0,09 | SMH | 0,77 | 0,43 |
| Gas | 0,33 | 0,06 | XLE | 0,12 | 0,19 |
| Bono | −1,29 | — | XBI | 0,31 | 0,38 |
| Plata | 0,39 | 0,30 | Brent (BNO) | 0,42 | 0,10 |
| Cobre | 0,30 | 0,28 | Platino (PPLT) | 0,34 | −0,24 |
| Nasdaq | 0,77 | 0,74 | Paladio (PALL) | 0,15 | 0,36 |
| EWJ | −0,18 | 0,12 | EWY | 0,22 | 0,34 |

Los ETF nuevos corren R1 en velas diarias (adaptación declarada), con 5 bp de slippage extra.

## 3. Canasta y carteras

| | Ventana | Mercados | Sharpe | CAGR | DD | Trim. + | Top-5 / PnL | DSR |
|---|---|---|---|---|---|---|---|---|
| R1 amplio (canasta) | común | 22 | 0,64 | 3,2% | −6,7% | 60% | 67% | — |
| R1 amplio (canasta) | larga 2001+ | 21 | 0,46 | 2,7% | −12,8% | 51% | 35% | — |
| R1 amplio escalado a vol 17% | común | 22 | 0,56 | 8,2% | −22,6% | 50% | — | 0,11 |
| R1 amplio escalado a vol 17% | larga 2001+ | 21 | 0,52 | 7,7% | −30,7% | 52% | — | 0,52 |
| **P4** (R1 amplio + C6) | común | — | 1,32 | 21,9% | −15,4% | 60% | — | 0,66 |
| **P4** (R1 amplio + C6) | larga 2018-09+ | — | 1,43 | 31,7% | −15,3% | 67% | — | 0,95 |

**P4 por año:**

| Ventana | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Común | — | — | — | +23,6% | −5,1% | +35,2% | +25,2% | +31,4% |
| Larga | −9,9% | +87,3% | +40,4% | +38,7% | −2,8% | +30,7% | +31,2% | +35,0% |

## 4. Lo que dicen los datos
1. **La tendencia diversificada fuera de cripto rinde un Sharpe de ~0,5 en 25 años.** Coincide con la literatura (Hurst-Ooi-Pedersen: ~0,4 neto por mercado). Sumar mercados TradFi no la sube a 1 con este motor: agrega mercados débiles (EWZ, EWT, IWM, GDX) que diluyen a los buenos (oro, SPX, Nasdaq, SMH).
2. **El motor fuerte de la investigación es cripto:** las rupturas R2/R3 (C6, Sharpe ~1,5 estable en 2018–25) y R1 en BTC y ETH.
   - Lo que sostiene a las carteras de r50 es cripto.
   - La parte TradFi aporta diversificación, no rendimiento.
3. **Ninguna cartera operable en futuros pasa las compuertas en 2021–25.** La mejor, P1 (R1 del núcleo + C6), da 24,6% / Sharpe 1,44; P4 da 21,9% / 1,32.
4. **2025 fue un año flojo para P1 (+7,9%) y bueno para P4 (+31,4%):** la diversificación ayuda en algunos años, pero baja el promedio.

## 5. Opciones
- **a) Confirmar P1 (R1 + C6) tal cual,** con la confirmación única (C6 en SOL, XRP, BNB y DOGE; R1 en los CFD nuevos; 2026) y F4 en Jesse, aceptando que no pasa la ventana común.
- **b) Foco cripto:** una cartera centrada en rupturas y tendencia sobre varios perpetuos cripto líquidos, con TradFi como diversificador menor. Requiere prerregistrar el universo cripto de exploración, distinto de los 4 de confirmación, y suma a N.
- **c) Cerrar r50** con este diagnóstico.
