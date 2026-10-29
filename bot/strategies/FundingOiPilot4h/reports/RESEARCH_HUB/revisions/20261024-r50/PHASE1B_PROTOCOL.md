# r50 F1b: protocolo de screening de 10 candidatas «todo terreno»

Fecha: 2026-10-25. El usuario aprobó la lista y este archivo se commitea **antes** de implementar y correr cualquier candidata.
- Nada se ajusta mirando resultados.
- Una regla cambiada es una variante nueva: suma a N y se reporta junto a la original.

## 1. Qué se reutiliza de F1
Se aplican sin cambios las reglas comunes de `PHASE1_PROTOCOL.md` §1 y la enmienda 4b:
- datos y símbolos del núcleo de 7 activos;
- ventanas: común 2021-01-01 → 2025-12-31 (decide) y larga por activo (solo veta); el bono no tiene lente larga;
- costes: taker 0,045%, maker 0,018%, stops +5 bp, slippage extra por lado de 15 bp en el bono y 5 bp en el gas, funding real en los perpetuos BTC y ETH;
- métricas: Sharpe de calendario √365, CAGR, DD, % de trimestres positivos, trades/año y top-5 / PnL;
- canasta equiponderada de mangas, sin estimación.

**Diferencias de alcance:**
- **Todas las candidatas son solo-largo y se aplican a los 7 activos del núcleo,** con los mismos valores en todos («todo terreno»).
- **Activos de validación:** no se cargan.

**Tamaño:**
- Las candidatas con stop (R2, R3, R4, N2) arriesgan 1% del equity de la manga por trade hasta el stop inicial, con techo de 2x nocional.
- Las demás usan vol objetivo 17% / vol 30 d, con techo 2x.

**Anualización de la vol:** 365 en cripto y 252 en CFD.

**Velas:**
- 4h: velas observadas de Jesse.
- 1D: velas UTC con el fin de semana sumado al lunes en los CFD.

## 2. Candidatas (valores fijos)

### Revalidaciones

**R1. Ensamble Donchian r49 (4h).**
- `DonchianEnsR49`, validado contra Jesse en F0: lookbacks 20/55/120/250 d, salida N/2, vol 17%, ≤2x, banda 25%.
- Configuración por activo:
  - BTC, ETH y oro: 6 velas por día, 365;
  - SPX: sesión UTC lun–vie 00–20, 5 velas por día, 252;
  - WTI, gas y bono: sesión de energía NY, 6 velas por día, 252.

**R2. Ruptura Core4h (4h).** Reglas de `BtcMomentumCore4h` con sus valores por defecto del código.
- **Entrada a mercado al cierre**, si se cumplen todas:
  - cierre > máximo de las 26 velas previas;
  - EMA20 > EMA80;
  - EMA80 > EMA80 de 4 velas antes;
  - cierre > EMA80;
  - ADX(14) ≥ 26;
  - 52 ≤ RSI(14) ≤ 76;
  - rango de la vela ≤ 3·ATR(14).
- **Stop inicial:** 2·ATR(14), acotado a entre 0,8% y 5,5% del precio; con más de 5,5% no se entra.
- **Trailing chandelier:** mejor cierre − 4,2·ATR(14), multiplicado por 0,78 desde 5R y por 0,62 desde 8R.
- **Break-even** (entrada + fees) desde 1,75R, sobre el máximo alcanzado.

**R3. Retest K1001, tramo largo (4h).** Mismos filtros que R2, salvo la entrada:
- se exige entry < cierre ≤ entry + ATR(14), donde entry es el máximo de las 26 velas previas;
- se coloca un límite (maker) en entry, válido una sola vela.
- Sale como K1001: stop 2·ATR(14), chandelier 4,2·ATR con el mismo endurecimiento y break-even desde 2,25R sobre el mejor cierre.
- Sin el corto de BTC.

**R4. Turtle diario.**
- Entrada a mercado si el cierre supera el máximo de los 55 días previos.
- Stop inicial 2·ATR(20).
- El stop sube al mínimo de los últimos 10 días (incluido el actual) cuando queda por encima del vigente.

**R5. M2a en 4h sobre los 7 activos.**
- **Filtro:** el último cierre diario completo está sobre la SMA 200 diaria.
- **Disparo:** RSI(2) de 4h < 10.
- **Entrada:** límite maker al cierre de la señal, válido una vela de 4h.
- **Salida:** cierre de 4h > SMA 5 de 4h, o tras 30 velas (5 días).
- **Tamaño:** 17% / vol 30 d diaria, techo 2x.

**R6. Rotación mensual entre los 7 activos.**
- Al último cierre diario de cada mes se ordenan los activos con ≥126 días de historia por su retorno de 63 velas diarias.
- Se toman los 3 primeros con retorno > 0 (momentum absoluto). Si son menos, el resto queda en efectivo.
- Cada elegido recibe 1/3 × 17% / vol 30 d de nocional, con techo 2x por activo. Los pesos rigen desde el día siguiente.
- Costes sobre el cambio de nocional: fee taker + slippage del activo. Funding de BTC/ETH sobre el nocional largo.

### Nuevas

**N1. Pullback dentro de tendencia (1D).**
- **Entrada:** el ensamble Donchian diario (20/55/120/250 velas diarias, salida N/2) tiene ≥ 50% de componentes activos y RSI(2) diario < 10. Límite maker al cierre, válido un día.
- **Salida:** cierre > SMA 5, o a los 5 días.
- **Tamaño:** 17% / vol 30 d, techo 2x.

**N2. Ruptura tras compresión (1D).**
- **Compresión:** el ancho de Bollinger(20, 2) de alguno de los 5 días previos está en el 20% inferior de los 250 días previos.
- **Entrada a mercado** si el cierre > banda superior.
- **Salida:**
  - stop inicial 2·ATR(20);
  - chandelier: mejor cierre − 4,2·ATR(20), sin endurecimiento;
  - break-even desde 2,25R sobre el mejor cierre.

**N3. Comprar y mantener con filtro de tendencia (Faber, 1D).**
- Al último cierre de cada mes: largo si el cierre > media de los últimos 10 cierres mensuales; si no, efectivo.
- **Tamaño:** 17% / vol 30 d, techo 2x. Se rebalancea solo a fin de mes, con banda 25%.

**N4. Cartera R1 + M2a.** Media 50/50 de los retornos diarios de la canasta R1 y de la canasta M2a de F1 (5 activos, sin re-correr ni cambiar M2a).

## 3. Puertas (canasta de 7 activos, ventana común)

**Roles:**
- **Tendencia:** R1, R2, R3, R4, R6, N2 y N3.
- **Diversificador:** R5 y N1.
- **Combinación:** N4.

| Rol | Pasa si | Además |
|---|---|---|
| Tendencia | Sharpe ≥ 0,8 (puerta de manga r49) y top-5 trades < 60% del PnL de la canasta. Fuera de R1, también tiene que mejorar a R1 en Sharpe o en % de trimestres positivos. | Para R6, top-5 no aplica: no tiene trades individuales. |
| Diversificador | Sharpe ≥ 0,5, ≥ 50 trades/año en la canasta y ρ diaria con R1 ≤ 0,2 en los trimestres en que R1 pierde. | Las puertas de M2 en F1, sin cambios. |
| Combinación | Sharpe > Sharpe de R1 y % de trimestres positivos ≥ el de R1. | — |

**Veto de la ventana larga** (todas): Sharpe largo < 0 o DD largo peor que −25% (techo r49).
- *Diferencia declarada con F1:* allí el veto era un DD largo > 1,5 × el DD común.
- Se reemplaza por un umbral absoluto porque el relativo veta motores por tener DD común chico. Eso se observó en los resultados de F1, así que esta elección está informada por F1 y se declara como tal.
- El DSR se reporta siempre.

**DSR:** Bailey–López de Prado sobre retornos diarios de la canasta, con N = 73. Se reporta y no es puerta de F1b; lo es de F2.

## 4. N
Diez candidatas nuevas: R1–R6 y N1–N4. **N declarado: 63 + 10 = 73.**

R1 ya contaba en r49, pero se cuenta igual porque cambian el universo y el uso.

## 5. Salida
- Tabla candidata × activo y canastas en las dos ventanas, con las puertas.
- Commit y push.
- Resumen al usuario.
- Las candidatas que pasan van a F2 (combinación) sin esperar confirmación, salvo que haga falta una decisión del usuario. Si no pasa ninguna, se reporta y se espera.
