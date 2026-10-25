# r50 F1c: asignación por clase y 6 familias nuevas

Fecha: 2026-10-25. El usuario aprobó la lista y este archivo se commitea **antes** de implementar y correr cualquier candidata.
- Nada se ajusta mirando resultados de F1c.
- Una regla cambiada es una variante nueva: suma a N.

## 1. Reglas comunes
- Igual que F1b (`PHASE1B_PROTOCOL.md` §1): datos, ventanas, costes con la enmienda 4b, métricas y canastas equiponderadas sin estimación.
- Todo es solo-largo.
- Las candidatas de clase se juzgan sobre los activos de su clase.

**Declaración de selección:**
- La asignación por clase (C0) y la elección de familias se decidieron **mirando los resultados de F1/F1b** (2021–25 y ventana larga del núcleo).
- Su evidencia en el núcleo es, por lo tanto, in-sample. La prueba honesta será F3, con la regla de clase aplicada a los activos de validación de esa clase:
  - acciones: Nasdaq, EWJ y EWY;
  - metales: plata y cobre.
- Cripto y energía no tienen activos de validación: sus reglas quedan sin prueba independiente, y se declara.

## 2. Candidatas (valores fijos)

**C0. Cartera por clase**, regla fijada ahora. Por activo, la manga es la media diaria de los retornos indicados, con las mismas implementaciones de F1/F1b:

| Clase | Activos | Manga |
|---|---|---|
| Cripto | BTC, ETH | 50/50 R2 + R3 (rupturas 4h) |
| Acciones | SPX | 50/50 R1 + M2a |
| Metales | Oro | R1 |
| Energía | WTI, gas | 50/50 N1 + M2a |
| Tasas | Bono | R1, por defecto de tendencia en tasas; el bono no tiene una regla propia mejor |

C0 es la media equiponderada de las 7 mangas.

**C1. Momentum diario cripto** (BTC, ETH).
- Largo mientras el retorno de 7 días es > 0; si no, fuera.
- Tamaño 17% / vol 30 d, techo 2x, banda 25%, revisado cada día.

**C2. Momentum 12-1 mensual** (los 7 activos).
- Al último cierre de cada mes: largo si el retorno entre el cierre de hace 13 meses y el de hace 1 mes es > 0.
- Tamaño 17% / vol 30 d, techo 2x. Se rebalancea solo a fin de mes, con banda 25%.

**C3. Comprar y mantener con tamaño por volatilidad** (SPX y oro).
- Siempre largo, 17% / vol 30 d, techo 2x.
- Rebalanceo a fin de mes con banda 25%.

**C4. Ruptura diaria para CFD** (oro, SPX, WTI, gas y bono).
- Reglas de R2 aplicadas a velas diarias, con los mismos valores: canal 26, EMA20/80, ADX ≥ 26, RSI entre 52 y 76, rango ≤ 3·ATR(14), stop 2·ATR(14), chandelier 4,2·ATR con endurecimiento y break-even desde 1,75R.
- *Única diferencia declarada:* se quita el tope del stop en 5,5% del precio. Es una calibración de BTC en 4h que en el diario de gas o WTI impediría toda entrada. El piso de 0,8% se mantiene.

**C5. Tendencia con entrada en retroceso de 4h** (los 7 activos).
- **Dirección:** el ensamble Donchian diario (como N1) con ≥ 50% de componentes activos al último cierre diario completo.
- **Entrada:** RSI(2) de 4h < 10, con límite maker al cierre, válido una vela.
- **Salida** (lo primero que ocurra):
  - el ensamble diario baja de 50%;
  - stop en entrada − 3·ATR(14) de 4h.
- Tamaño 17% / vol 30 d diaria, techo 2x.

**C6. Ensamble de rupturas cripto** (BTC, ETH). Media 50/50 de los retornos diarios de R2 y R3 por activo; los trades de las dos cuentan para top-5.

## 3. Puertas (ventana común; canasta de los activos de cada candidata)

**Direccionales (C1–C6):**
- Sharpe ≥ 0,8;
- top-5 trades < 60% del PnL, salvo C3, que no tiene trades;
- mejorar a R1 en los mismos activos, en Sharpe o en % de trimestres positivos;
- no ser vetada en la ventana larga.

**C0:**
- Sharpe > R1 de 7 activos;
- trimestres positivos ≥ R1;
- top-5 < 60% de todos los trades;
- sin veto largo.

**Veto de la ventana larga** (igual que F1b): Sharpe < 0 o DD < −25%. El bono no tiene lente larga.

**DSR:** con N = 80; se reporta, no es puerta.

## 4. N
Siete candidatas nuevas: C0–C6. **N declarado: 73 + 7 = 80.**

## 5. Salida
- Informe con tabla y puertas, commit y push, resumen al usuario.
- Lo que pase se suma a N4 como candidata para F2.
- **No se avanza a F2 sin que el usuario lo decida.**
