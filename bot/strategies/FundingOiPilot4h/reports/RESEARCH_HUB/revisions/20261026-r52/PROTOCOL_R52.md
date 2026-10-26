# r52: protocolo preregistrado (fijado antes de cualquier resultado)

Plan aprobado por el usuario el 2026-10-25 ([`PLAN.md`](PLAN.md)). Evidencia de partida: `reports/Nuevas fuentes de ventaja r52.md`.

Reglas de este protocolo:
- N no tiene techo, por decisión del usuario, pero cada ensayo se registra para el DSR (parte de 108).
- Una variante nueva se agrega acá con fecha **antes** de correrla.

## 0. Convenciones
- **Solo perpetuos USDT-M de Binance.** Datos de `data.binance.vision`: velas 1h y 1m con volumen agresor, más funding, hasta el 2025-12-31. 2026 sigue reservado.
- **Universo U50** (`research_scripts/data/r52/universe50.json`):
  - los 50 perpetuos cripto USDT-M activos con más volumen 24h al 2026-10-25;
  - listados antes de 2023;
  - sin stablecoins, índices ni TradFi.
- **Sesgo declarado:** el universo se eligió con el volumen de hoy y no tiene deslistados, por decisión del usuario.
  - Mitigación: elegibilidad punto a punto (§1).
  - Se reporta aparte el subconjunto de las 20 monedas listadas antes del 2020-07, que tienen toda la historia.
- **Costos:**
  - fee taker 0,045% más 2 bp de slippage por lado sobre la rotación;
  - funding real por símbolo: los largos pagan funding positivo.
- **Cortes:**
  - desarrollo hasta el 2023-12-31, para entrenar y elegir;
  - **validación 2024**: una mirada;
  - **2025 sellado**: una mirada final, solo en la F4.
- **Métricas:** retornos diarios y Sharpe con √365, con las métricas y el DSR de r50 (`r50_f2.r9`, `r50_f1b.dsr`).
- **ρ con P1:** contra los retornos diarios de P1 2018-09+ (`r51_lib`).

## 1. Elegibilidad semanal
- Cada lunes 00:00 UTC, una moneda es elegible si cumple todo esto:
  - tiene ≥ 90 días de velas 1h;
  - la mediana de su volumen diario en USDT de los últimos 30 días es ≥ 10 M;
  - tiene la vela del rebalanceo.
- Hacen falta ≥ 10 monedas elegibles para operar esa semana.

## F1. Ranking transversal semanal

**Variables**, calculadas al cierre del domingo sobre barras diarias armadas desde 1h, sin datos posteriores:
- precio / SMA_n − 1, con n ∈ {3, 5, 10, 20, 50, 100, 200} días;
- volumen SMA_n / volumen SMA_200, con n ∈ {3, 5, 10, 20, 50};
- retornos de 1, 2, 4, 8, 12 y 26 semanas;
- vol realizada de 7 y 30 días;
- desbalance agresor (2·compra agresora / volumen − 1), promedio de 7 y 30 días;
- RSI14 diario y MACD(12, 26) / precio;
- beta con BTC a 60 días.
- Cada variable se transforma a su rango transversal en [−0,5, 0,5] dentro de la semana.

**Objetivo:** rango transversal del retorno de la semana siguiente.

**Entrenamiento**
- Walk-forward expansivo, re-entrenado cada 4 semanas.
- Solo con semanas cuyo objetivo ya se conoció al momento del ajuste: purga y embargo de 1 semana.
- La primera predicción sale después de 52 semanas con datos.

**Ensayos**
- **X0, referencia:** puntaje = media de los rangos de los retornos de 1, 4 y 12 semanas. Sin ML.
- **X1, elastic net:** `ElasticNetCV`, con l1_ratio ∈ {0,1; 0,5; 0,9} y validación cruzada temporal (`TimeSeriesSplit`, 5) dentro del entrenamiento.
- **X2, gradient boosting:** `HistGradientBoostingRegressor` con `max_depth=3`, `learning_rate=0,05`, `max_iter=200`, `min_samples_leaf=50` y `l2_regularization=1,0`. Hiperparámetros fijos.
- **X3:** el mejor de X1/X2 por Sharpe neto de desarrollo, en versión **largo el quintil superior** (bruto 1,0) **cubierto por beta** con un corto 50/50 de BTC y ETH. El beta es el de la canasta larga contra BTC/ETH a 60 días.

**Cartera de X0–X2**
- Largo el quintil superior y corto el inferior.
- Pesos por vol inversa a 30 días dentro de cada pata; bruto 0,5 por pata.
- Rebalanceo semanal.
- Retornos diarios con los pesos de la semana, fijos en fracción del equity (simplificación declarada).

**Compuertas**, en desarrollo salvo indicación:
- Sharpe neto ≥ 0,5;
- X1–X3 superan a X0 por ≥ 0,2 de Sharpe neto;
- con costos ×2, Sharpe > 0;
- ρ con P1 ≤ 0,3;
- validación 2024: Sharpe neto > 0.

## F2. Reloj del flujo de órdenes

**Señal (QOI):** desbalance agresor del primer minuto de cada cuarto de hora (minutos :00, :15, :30 y :45), sumado sobre las 16 aperturas de las últimas 4 horas.
- QOI = Σ(2·compra agresora − volumen) / Σ volumen.
- Se estandariza con la media y el desvío de los 90 días previos.

**Ensayos**
- **Q1, estadística**, en BTC y ETH: IC de Spearman entre el QOI al cierre de cada barra de 4h y el retorno de las 8 h siguientes.
  - Se mide en 2021-01 → 2023-12, con t de Newey-West de 12 rezagos.
  - Compuerta: t ≥ 2 en la canasta.
- **Q2, regla:** en cada cierre de 4h, largo si z(QOI) > +1 y corto si z < −1, con salida a las 8 h (2 barras).
  - Tamaño 0,17/σ30 con techo de 2x; taker en la entrada y en la salida; funding real.
  - Compuertas: Sharpe neto ≥ 0,5 en desarrollo, ρ con P1 ≤ 0,3 y Sharpe > 0 en 2024.
  - Signo: el del paper (desbalance positivo → retorno positivo). Si Q1 diera el signo opuesto, Q2 no se corre invertida sin un ensayo nuevo registrado.
- **Q3:** Q2 congelada sobre las 20 alts de mayor volumen de U50, sin BTC ni ETH.
  - Compuerta: la mayoría de las alts con Sharpe > 0 y canasta con t ≥ 1,28.

## F3. Permiso de régimen

**J1: statistical jump model de 2 estados sobre BTC diario** (Shu, Yu y Mulvey 2024).
- Spot 2017-08+ y perpetuo desde 2020.
- Rasgos: desvío negativo EWMA y Sortino EWMA con vidas medias de 5, 10 y 21 días.
- Penalización de salto λ = 50, fija y tomada de la literatura.
- Re-ajuste mensual sobre la historia expansiva. El estado de cada día sale del camino óptimo hasta ese día y se aplica con 1 día de demora.
- El estado de riesgo es el de menor retorno medio en el ajuste.
- En el estado de riesgo, los retornos diarios de R1/BTC, R1/ETH y C6 se multiplican por 0,5 dentro de P1. La aproximación ignora los fees ahorrados.
- Compuerta: la regla de inclusión de r51 en las dos ventanas de P1, medidas solo hasta el 2024-12-31. 2025 queda sellado también para J1.

## F4. Cartera y mirada sellada
- Construcción de F2 de r50 sobre P1 más las mangas de F1/F2 que pasen y la versión J1 de P1 si pasa, con la regla de inclusión de r51.
- La inclusión se mide con las ventanas de P1 cortadas al 2024-12-31 (2018-09 → 2024 y 2021 → 2024), para no mirar 2025.
- **2025 sellado:** se corren una vez las mangas incluidas.
  - Puertas: Sharpe > 0 y ningún derrumbe (Sharpe < −0,5 o DD < −30%).
  - Si falla, la manga se retira, sin ajuste.
- Cierre, congelamiento y handoff a r53.
