# r50 F1: protocolo de screening de M1–M4

Fecha: 2026-10-25. Este archivo se commitea **antes** de correr cualquier screening de M1–M4.
- Ningún parámetro, regla o puerta se ajusta mirando los resultados de F1.
- Si un motor necesita cambiar, la versión nueva es una variante distinta: suma a N y se reporta junto a la original.

## 1. Reglas comunes

**Datos**
- Velas diarias UTC armadas con el arnés `r50_harness.py` desde las velas de 1m guardadas en Jesse, con la agregación propia de Jesse (`generate_completed_candles_from_observed_minutes`).
- En los CFD (oro, SPX, WTI, gas y bono), los minutos de sábado y domingo UTC se suman a la vela del lunes. Así la reapertura del domingo no forma una vela corta propia.
- Nada posterior al 2025-12-31: el arnés lo rechaza.
- Los activos de validación (plata, Nasdaq, cobre, EWJ, EWY y platino) no se cargan en F1.

**Símbolos del núcleo**

| Activo | Ventana común (decide) | Ventana larga (solo veta) |
|---|---|---|
| BTC | `Binance Perpetual Futures / BTC-USDT`, con funding `0ab14bc2…86ca` | `Binance Spot / BTC-USDT` desde 2017-08, sin funding |
| ETH | `Binance Perpetual Futures / ETH-USDT`, con funding `22bd891c…893b` | `Binance Spot / ETH-USDT` desde 2017-08, sin funding |
| Oro | `Custom Data / XAU-USDT` (Dukascopy) | ídem desde 2012 |
| SPX | `Custom Data / SPXD-USDT` (Dukascopy) | ídem desde 2012 |
| WTI | `Custom Data / WTI-USDT` (Dukascopy) | ídem desde 2012, sin abr–jul 2020 |
| Gas | símbolo nuevo `Custom Data / NATGAS-USDT` (Dukascopy) | ídem desde el primer dato |
| Bono | símbolo nuevo `Custom Data / USTBOND-USDT` (Dukascopy) | ídem desde el primer dato |

**Ventanas**
- **Común:** 2020-10-15 → 2025-12-31. Las métricas se miden desde 2021-01-01; el tramo previo es calentamiento.
- **Larga:** desde el primer día con calentamiento completo de cada activo hasta 2025-12-31.
- Antes del primer dato no hay posición.

**Ejecución y costes**
- La señal se calcula al cierre diario. Las órdenes a mercado se llenan a ese cierre, igual que Jesse en la reproducción de F0, con taker 0,045%.
- Órdenes maker (entradas de M2): límite al cierre de la señal, válida solo la vela siguiente.
  - Se llena si el mínimo de esa vela queda estrictamente por debajo del límite (por encima en cortos), con fee 0,018%.
  - Si no, se cancela.
- Stops (M3): se llenan al precio de stop o a la apertura si hay gap, empeorados 5 bps, con taker.
- Funding: el real de Binance en los perpetuos BTC y ETH.
  - Spot y CFD sin funding. Es un sesgo a favor declarado; los perpetuos TradFi de Binance tienen funding ≈0.

**Tamaño de posición**
- Cada manga apunta a una volatilidad anual del 17% sobre la vol realizada de 30 días.
- Techo de 2x nocional sobre el equity de la manga y banda de rebalanceo del 25%, como el nulo r49.
- Cuenta de 10.000 USDT por manga, sin freno de DD (el freno es asunto de F5).

**Métricas por motor × activo y por canasta**
- Sharpe de retornos diarios de calendario (equity sin cambio en días sin vela) anualizado con √365, igual para todos los activos.
- Trades por año.
- % de trimestres positivos.
- Correlación diaria con M1:
  - en todo el período;
  - solo en los trimestres en que la canasta M1 pierde.
- CAGR, DD y los 5 mejores trades como % del PnL.
- Todas las métricas en las dos ventanas.

**Nulo de referencia:** el ensamble Donchian r49, `DonchianEnsR49` del arnés validado en F0, en 4h, sobre los mismos activos y ventanas.

## 2. Motores (valores por defecto fijos)

### M1. Tendencia v2
**Hipótesis:** una señal continua de tres velocidades mejora al nulo Donchian r49 en Sharpe o en regularidad trimestral.

**Señal:** para cada velocidad N ∈ {15, 60, 250} días:
- s_N = clip(r_N / (σ_d · √N), −2, 2) / 2, donde r_N es el log-retorno de N días y σ_d la vol diaria de 60 días.
- La señal es la media de las tres, en [−1, 1].

**Lados:**
- Solo-largo (señal recortada a ≥0) en BTC, oro y SPX.
- Largo/corto en WTI, gas y bono.
- ETH no lleva M1.

**Posición:** señal × 17% / vol 30 d, con techo 2x y banda 25%.

**Correlación (Baltas-Kosowski):** se aplica en F2 a nivel cartera, no en F1.

**Falsación** (por activo y en la canasta M1 equiponderada en riesgo, ventana común):
- Falla si no mejora al nulo r49 ni en Sharpe ni en % de trimestres positivos.
- En los activos L/S, el tramo corto se juzga aparte, solo en ventanas con bajista: 2022 en la común y la ventana larga completa.

### M2. Reversión de corto plazo
**Hipótesis:** comprar caídas de 1–3 días dentro de una tendencia alcista paga con alta tasa de acierto y poca correlación con M1 cuando M1 pierde.

**Canasta:** oro, SPX, WTI, gas y bono. Sin cripto (Zaremba 2021; Fičura 2023). Solo-largo, como la regla de Connors.

Se prerregistran **dos variantes**, que se reportan las dos:

| | Entrada | Salida |
|---|---|---|
| **M2a RSI(2)** | cierre > SMA 200 y RSI(2) < 10 | cierre > SMA 5 o a los 5 días |
| **M2b IBS** | cierre > SMA 200 e IBS = (C−L)/(H−L) < 0,2 | IBS > 0,8, cierre > máximo previo o a los 5 días |

- Entradas maker según §1; salidas a mercado (taker).
- Tamaño: 17% / vol 30 d, con techo 2x.

**Falsación** (canasta, ventana común). Falla si se cumple cualquiera:
- Sharpe < 0,5;
- menos de 50 trades por año;
- correlación con la canasta M1 > 0,2 en los trimestres en que M1 pierde.

### M3. Corto con régimen
**Hipótesis:** en régimen bajista, la ruptura de mínimos con salida rápida captura caídas que el canal simétrico r49 llegaba tarde a tomar.

**Activos:** los 7 del núcleo.

**Régimen:** cierre < SMA 200 y SMA 50 hoy < SMA 50 de hace 5 días.

**Entrada:** con régimen activo, corto si el cierre < mínimo de los 20 días previos.

**Salida** (lo primero que ocurra):
- cierre > máximo de los 10 días previos;
- stop en entrada + 2 × ATR(20), fijado al entrar;
- 20 días de tenencia.

El régimen no se exige para salir. El funding real se aplica en BTC y ETH.

**Ablación prerregistrada (M3-nr):** la misma regla sin filtro de régimen. Suma a N.

**Falsación** (canasta, ventana común). Falla si se cumple cualquiera:
- Sharpe < 0,5;
- quitar el régimen resta menos de 0,4 de Sharpe (Sharpe M3 − Sharpe M3-nr < 0,4);
- más del 50% del PnL en 3 trades.

### M4. Valor relativo ETH/BTC
**Hipótesis:** el momentum del ratio ETH/BTC a 4–12 semanas persiste y su lado corto ETH / largo BTC es casi neutral a la dirección de BTC.

**Señal:**
- Para L ∈ {28, 56, 84} días, cada componente vale 1 si el log-retorno de L días del ratio es < 0, y 0 si no.
- La exposición es la media de los tres componentes, en [0, 1]. Se usa ese ensamble para no elegir un L.

**Posición:**
- Corto ETH y largo BTC por el mismo nocional, exposición × 17% / vol 30 d del spread. Techo 2x por pata.
- Banda 25%.
- Funding real en las dos patas.

**Falsación** (ventana común). Falla si se cumple cualquiera:
- Sharpe neto < 0,6;
- |correlación diaria con los retornos de BTC| > 0,3.

## 3. Ventana larga: veto
- Una manga que pasa en la común **se veta** si en la ventana larga su Sharpe es < 0 o su DD supera 1,5 veces el de la ventana común.
- En BTC/ETH la ventana larga es spot 2017-08 → 2025, sin funding: el sesgo se declara y no se corrige.

## 4. N y registro
Variantes nuevas: M1, M2a, M2b, M3, M3-nr y M4. Son +6.

**N declarado para F1: 63** (57 + 6). Los activos que llegan tarde (gas y bono) se evalúan con las mismas reglas y no suman variantes.

Cada variante se registra en `TRIAL_REGISTRY.json`, con métricas por activo y canasta en las dos ventanas.

## 4b. Enmienda de costes (2026-10-25, antes de cualquier resultado)

**Fuente:** libro de Binance medido hoy por la sesión coordinadora.
- La profundidad a ±0,2% es de 3–6 k en TMFUSDT/TBTUSDT y de 0,09–0,14 M en NATGASUSDT.
- Spreads: 3,4 / 7,7 bp en TMF/TBT y 3,3 bp en gas.

**Cambio:** se suma un slippage adverso por lado a cada fill taker y a cada stop, además de las fees:
- **bono: 15 bp;**
- **gas natural: 5 bp;**
- cobre (F3): 5 bp;
- EWJ y platino (F3, por la ampliación de la validación del 2026-10-25): 10 bp;
- resto: 0.

Las entradas maker (límite) no llevan slippage.

**Bono:**
- Las señales se calculan sobre el Tesoro largo subyacente.
- La ejecución real sería con TMF (3x largo) o TBT (2x corto), que tienen decaimiento por apalancamiento diario. El decaimiento no se modela en F1 y queda declarado como sesgo a favor.
- La operabilidad con tamaño mayor a una cuenta chica sigue pendiente de verificar.

## 5. Salida de F1
- Un informe corto con la tabla motor × activo y las puertas, para el usuario.
- **No se pasa a F2 sin reportar F1.**
