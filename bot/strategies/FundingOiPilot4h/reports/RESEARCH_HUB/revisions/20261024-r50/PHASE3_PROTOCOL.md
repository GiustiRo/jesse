# r50 F3: validación con motores congelados en 5 activos no vistos

Fecha: 2026-10-25. Aprobado por el usuario («seguir con el roadmap F3, F4»). Este archivo se commitea **antes** de cargar o mirar cualquier activo de validación en el arnés.

## 1. Qué se congela
- **Código:** `r50_harness.py`, `r50_engines.py`, `r50_f1b.py`, `r50_f1c.py` y `r50_f2.py`, tal como quedaron en el commit `8e6b82e0`.
- **Motores:** R1 (ensamble Donchian r49), R2 (ruptura Core4h), R3 (retest K1001), M2a (RSI(2)) y N1 (pullback en tendencia). Sus valores son los de F1/F1b; no se cambia nada.
- **Reglas de clase de C0:**
  - acciones: 50/50 R1 + M2a;
  - metales: R1.
- **Construcción de cartera de F2:** pesos de riesgo inverso, vol 17%, k ≤ 8.

Nada se re-ajusta después de ver los resultados de F3.

## 2. Activos de validación

| Activo | Clase | Datos | Símbolo | Velas | Coste extra |
|---|---|---|---|---|---|
| Plata | metales | Dukascopy XAGUSD 1m 2010+ | `Custom Data / XAG-USDT` | 4h y 1D | 0 |
| Cobre | metales | Dukascopy COPPER.CMD 1m (divisor 10.000) | `Custom Data / COPPER-USDT` | 4h y 1D | 5 bp |
| Nasdaq 100 | acciones | Dukascopy USATECH.IDX 1m | `Custom Data / NDX-USDT` | 4h y 1D | 0 |
| EWJ | acciones | Yahoo diario 2000+ | CSV (`data/r50/etf`) | solo 1D | 10 bp |
| EWY | acciones | Yahoo diario 2000+ | CSV (`data/r50/etf`) | solo 1D | 0 |

**Configuración de R1 en 4h, la del activo análogo del núcleo:**
- plata y cobre: la de oro (6 velas por día, 365);
- Nasdaq: la de SPX (sesión UTC lun–vie 00–20, 5 velas por día, 252).

**EWJ y EWY no tienen 1m ni 4h:**
- R2 y R3, que solo existen en 4h, no se aplican a ellos.
- R1 se corre en velas diarias con el mismo ensamble (20/55/120/250 velas diarias, 1 vela por día, 252). Es una adaptación declarada, no una variante elegida.

**Ventanas:** las mismas de F1.
- Común: 2021-01 → 2025.
- Larga: por activo, desde el primer año con calentamiento completo.

Sin funding: son CFD y ETF.

## 3. Pruebas y puertas

**A. Motor × activo** (todas las combinaciones aplicables; ventana común):
- **Puerta:** Sharpe > 0 en la **mayoría** (> 50%) de las combinaciones, y **ningún derrumbe**.
- **Derrumbe:** DD < −30% o Sharpe < −0,5 en la ventana común.
- La ventana larga se reporta.

**B. Regla de clase** (C0 aplicado a activos nuevos):
- **Puerta:** el Sharpe de la manga de clase es > 0 en cada uno de los 5 activos (ventana común).
- La canasta equiponderada de esas 5 mangas también se reporta.

**C. Diagnóstico de cartera** (se reporta, no es puerta):
- la cartera F2 (C0 + C6), sumando a C0 las 5 mangas de clase de validación;
- escalada con la construcción congelada de F2.

**Resultado:**
- F3 **pasa** si pasan A y B.
- Si falla, se reporta y **no se re-ajusta**: la decisión vuelve al usuario.

## 4. N
F3 es validación, no selección: **N queda en 81.**

## 5. Salida
- Informe con las tablas A, B y C, commit y push.
- Resumen al usuario.
- Si pasa, F4 confirma en Jesse las mangas de la cartera final, con ≤ 10 corridas y máximo 2 a la vez.
