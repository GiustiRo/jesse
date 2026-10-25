# r50 F1g: operativas descorrelacionadas fuera de cripto (por clase)

Fecha: 2026-10-25. Pedido del usuario: «Sí o sí seguiremos buscando, ya sea por clase o por activo, una operativa descorrelacionada»; el foco no puede ser solo cripto. Este archivo se commitea **antes** de implementar y correr F1g.

## 0. Alcance
- Solo futuros USDT-M de Binance. Los CFD y ETF son proxies de datos históricos.
- Solo-largo. Los cortos como manga propia fallaron en todo r50.
- **Universo de exploración: acciones** (perpetuos de Binance con proxy). Ya cargados:

| Perpetuo | Proxy |
|---|---|
| SPYUSDT | SPX CFD |
| QQQUSDT | Nasdaq CFD |
| IWMUSDT | IWM |
| SMHUSDT | SMH |
| EWJUSDT | EWJ |
| EWYUSDT | EWY |
| EWZUSDT | EWZ |
| EWTUSDT | EWT |

- **Confirmación** (reservada desde F1d §4, sin cargar): DAX, Nikkei 225 y FTSE 100 (Dukascopy). Sirve para la clase acciones.
- **Declaración:** la elección de la clase acciones y de estas familias está informada por r50. En r50, la energía y los bonos fallaron con todo; los metales ya los cubre R1.

## 1. Candidatas (valores fijos, de la literatura)

**G1. Efecto cambio de mes** (Lakonishok-Smidt 1988; McConnell-Xu 2008, 35 países).
- Largo desde el cierre del penúltimo día hábil del mes hasta el cierre del tercer día hábil del mes siguiente: cubre los días −1 a +3.
- Tamaño 17% / vol 30 d, techo 2x.
- Costes: taker 0,045% por lado, más 5 bp de slippage en los perpetuos TradFi nuevos.
- Los días hábiles salen de las velas diarias de cada activo.

**G2. Reversión de corto plazo solo en índices de EE.UU.** (SPX, Nasdaq, IWM y SMH).
- Regla M2a sin cambios: cierre > SMA 200 y RSI(2) < 10; salida con cierre > SMA 5 o a los 5 días; entrada maker.
- *Hipótesis:* la evidencia publicada de esta familia es de índices de EE.UU.; F3 mostró que fuera de EE.UU. falla.
- Confirmación: DAX, Nikkei y FTSE. Es una prueba de si la regla sale de EE.UU.; si falla se reporta, sin re-ajustar.

**G3. Compra en pánico de volatilidad** (acciones, los 8 activos).
- **Entrada:** largo si la vol realizada de 10 días supera 2 veces su mediana de 252 días y el cierre es menor que el mínimo de 20 días. La entrada es a mercado al cierre.
- **Salida:** cierre > SMA 20 o a los 20 días.
- **Tamaño:** 17% / vol 30 d, techo 2x.
- Se basa en la prima de volatilidad, que paga más después de los shocks.

## 2. Compuertas (canasta de la clase; ventanas de F1)

**Manga:**
- Sharpe ≥ 0,5 en la ventana larga y en la común;
- Sharpe > 0 en las dos mitades de la larga (corte 2018-01-01);
- top-5 trades < 60% del PnL.
- **Además, descorrelación:** la correlación diaria con P1 (R1 + C6) debe ser ≤ 0,3, tanto en todo el período como en los trimestres negativos de P1.

**Cartera P5** = P1 + las mangas G que pasen. Se agregan en forma greedy por Sharpe largo; una manga entra si mejora el Sharpe o los trimestres positivos de la cartera en la común. Construcción de F2 congelada. Puertas de F1d §3 en las dos ventanas:
- CAGR ≥ 30%;
- DD ≤ 20%;
- PF ≥ 1,2;
- mediana mensual > 0;
- positiva sin los 2 mejores meses;
- DSR ≥ 0,95 con N = 98.

La regularidad se reporta como seguimiento.

## 3. N
Cuatro variantes nuevas: G1, G2, G3 y P5. **N declarado: 98.**

## 4. Si P5 pasa
Se congela y sigue la confirmación única de F1d §4.
- Las mangas G se confirman en DAX, Nikkei y FTSE.
- R1 y C6, como estaba previsto.
- 2026 solo para las mangas R1/R2/R3.
