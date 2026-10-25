# r51: protocolo preregistrado (fijado antes de cualquier resultado)

Plan aprobado por el usuario el 2026-10-25 ([`PLAN.md`](PLAN.md)). Este archivo fija reglas, parámetros, ventanas y puertas de todas las fases. Se commitea antes de correr nada. Un cambio posterior es una variante nueva que suma a N, o una enmienda fechada y explicada antes de mirar el resultado afectado.

## 0. Convenciones heredadas de r50 (sin cambios)
- Arnés: `r50_harness.py` y `r50_engines.py`, congelados en `5caf4a53`. Los scripts nuevos (`r51_*.py`) los importan sin modificarlos.
- Costes:
  - taker 0,045%; maker 0,018%, que llena solo si la vela siguiente cruza el límite de forma estricta;
  - stops con 5 bp de slippage;
  - slippage extra por lado: bono 15 bp y gas 5 bp (enmienda 4b de r50); el resto, 0;
  - funding real en los perpetuos BTC y ETH. Los CFD van sin funding, sesgo a favor declarado.
- Cuenta por manga: 10.000 USDT, aislada.
- Mangas continuas: vol objetivo 17% (vol realizada de 30 días), techo de 2x nocional, banda de rebalanceo de 25%.
- Mangas con stop: 1% de riesgo por trade.
- **2026 reservado:** nada posterior al 2025-12-31.
- Activos de validación (plata, Nasdaq, cobre, EWJ y EWY): solo en la F6, con reglas congeladas.

## 1. Ventanas
| Lente | Activos | Período | Rol |
|---|---|---|---|
| Decisión | TradFi (CFD) | 2018-09-01 → 2025-12-31, desde que haya historia para los lookbacks (bono: ~2019-03) | decide |
| Decisión, sub-ventana | todas | 2021-01-01 → 2025-12-31 | se reporta; P2 no puede empeorar a P1 aquí (§F6) |
| Decisión | BTC/ETH | perpetuo 2020-10-15 → 2025 con funding, más spot 2018-01 → 2025 (lente r50) | decide |
| Larga (solo veta) | oro, SPX, WTI, gas | desde 2011–2012, según los datos | veto |
| Larga (solo veta) | bono | **TLT diario 2002–2025** (Yahoo; decisión del usuario 2026-10-25) | veto |

**Veto** (igual que en r50): Sharpe < 0 en la lente larga, o DD de la lente larga mayor que 1,5 veces el de la lente de decisión.

**Ventanas bajistas**, fijadas por calendario antes de los resultados:
- Bono: 2021-01 → 2023-10. En TLT, además: 2013-05 → 2013-12 y 2016-07 → 2018-10.
- WTI: 2018-10 → 2018-12 y 2022-06 → 2023-05. En la larga, además: 2014-06 → 2016-02.
- Gas: 2022-08 → 2024-03. En la larga, además: 2014-01 → 2016-03.
- BTC/ETH: 2018-01 → 2018-12 (spot) y 2021-11 → 2022-12.
- SPX: 2018-10 → 2018-12, 2020-02 → 2020-03 y 2022-01 → 2022-10.
- Oro: 2022-03 → 2022-10. En la larga, además: 2013-01 → 2015-12.

## F0. Preparación (no suma a N)
- Descargas a `research_scripts/data/r51/`, todas hasta el 2025-12-31:
  - TLT diario de Yahoo, desde 2002, con `r50_etf_daily_download.py`;
  - Brent de Dukascopy (o BNO diario si Dukascopy no lo tiene; sustitución declarada);
  - índice dólar de Dukascopy (o −EURUSD si no existe), **solo como señal**.
- El funding por símbolo y el funding con margen aislado ya están en la rama (`d234d45c`, `7101324e`). No hace falta reiniciar.

## F1. Confirmación de P1 en Jesse (≤10 corridas, máximo 2 simultáneas)

**Cambio respecto del plan**, antes de correr nada:
- En una sesión Jesse todas las rutas comparten la billetera, y el arnés usa 10k por manga. Por eso se corre una manga por sesión.
- R1 en BTC y en WTI ya tiene sesiones Jesse idénticas en motor y ventana (`b4792187`, F0 de r50; `063c2564`, r49 F2c). Se comparan sin gastar corridas.
- **Corridas nuevas (9):**
  - R1 en ETH (funding `22bd891c…`), oro (XAU), SPX (SPXD), gas y bono;
  - R2 en BTC y ETH, y R3 en BTC y ETH, con funding real.
- Queda 1 corrida de reserva.

**Configuración**
- Ventana 2020-10-15 → 2026-01-01; fee 0,00045; aislado.
- Apalancamiento: 3x en R1 (igual que el arnés de R1) y 5x en R2/R3.
- Warmup en velas observadas: 1.520 para R1 en CFD y BTC; las disponibles en ETH (perpetuo desde 2020-08-15, ~360); 1.700 para R2/R3 en BTC y 360 en ETH.

**Estrategias**
- R1: clases r49 sin cambios.
  - `R49NullDonchianEnsBtc` para ETH y XAU (24h, 6 velas/día, 365 días);
  - `R49NullDonchianEnsSpy` para SPXD;
  - `R49NullDonchianEnsWti` para gas y bono (sesión de energía).
- R2/R3: dos estrategias nuevas, `R51C6R2` y `R51C6R3`, copia literal de `r50_f1b.r2_r3_decider`. Mismos filtros, stop, chandelier y BE, 1% de riesgo y sin reentrada en la vela de un cierre.
  - R3 no ajusta el trailing en la vela del llenado.

**Comparación**
- Se compara contra el arnés sobre la misma ventana y con el mismo slippage. Jesse no modela slippage, así que **la corrida del arnés para comparar usa slippage 0**: bono y gas sin su extra, y stops sin los 5 bp.
- La comparación se hace sobre la curva diaria de equity, con el método `repro` de r50.

**Tolerancia por manga:** |ΔSharpe diario| ≤ 0,10, |ΔCAGR| ≤ 1 pp y |ΔDD| ≤ 1 pp.

**Si falla**
- Gana Jesse: se diagnostica la orden divergente con la corrida de reserva o con el log y se corrige el arnés.
- Las métricas de P1 se recalculan con el arnés corregido y se reportan antes de seguir.
- Una diferencia que cambie el signo de una manga se reporta al usuario y frena r51.

## F2. Diagnóstico de P1 (descriptivo, no suma a N)
- Curva diaria de P1 2018-09+ desagregada por manga y por activo.
- **Trimestres objetivo:** los trimestres de P1 con retorno ≤ 0. Para cada uno: el retorno de cada activo subyacente (comprar y mantener) y el aporte de cada manga.
- **Cota corta ideal** por familia: el retorno de estar corto con vol 17% en cada trimestre objetivo donde el subyacente cayó. Es un techo informativo, no una regla.
- Atribución del PnL de P1 por familia (cripto, metales, acciones, energía, bono) y por dirección.

## F3. Bloque A: activos sin deriva (5 ensayos)
Barras diarias de sesión (`en.daily_from_minutes`), decisión al cierre y llenado al cierre con taker.

**A1. Tendencia lenta largo/corto común** en WTI, gas y bono.
- s = media(signo(r63), signo(r126), signo(r252)), con r_k el retorno logarítmico de k días hábiles; s ∈ {−1, −⅓, ⅓, 1}.
- Posición = s · 0,17/σ30, con techo de 2x y banda de 25%.
- Una regla, un ensayo; se reporta por activo y en canasta.

**A2. Bono con compuerta de correlación**
- A1 en el bono, pero el lado largo vale 0 salvo que la correlación a 126 días entre los retornos diarios de SPX y del bono sea < 0. El lado corto no cambia.
- Lente larga: TLT con SPX (SPXD 2011+); el veto rige desde 2012.

**A3. Spread Brent–WTI**, par en BZUSDT/CLUSDT.
- x = ln(Brent) − ln(WTI); z = (x − media60) / desvío60.
- Entrada:
  - z > 2: corto Brent / largo WTI;
  - z < −2: largo Brent / corto WTI.
- Salida: z cruza 0, pasan 20 días o |z| > 4 (stop).
- Tamaño: nocional por pata = equity · min(1; 0,17/σ30(Δx)), con taker en las dos patas.
- Lente larga desde 2012.

**A4. Fin de mes en el bono**
- Largo desde el cierre del 4.º día hábil antes del fin de mes hasta el cierre del último día hábil.
- Tamaño 0,17/σ30 con techo de 2x.
- Entrada maker: límite al cierre, válido una vela. Si no llena, se pierde el mes. Salida taker.

**A5. Crudo–dólar**
- A1 en WTI, con el lado largo en 0 si el retorno del dólar a 63 días es > 0 (o el de EURUSD < 0 si se usa el sustituto).

## F4. Bloque B: cortos en activos con deriva y valor relativo (3 ensayos)

**B1. Corto cripto 4h** en BTC y ETH. Es el espejo de R2.
- Régimen: cierre diario < SMA200 diaria y SMA50 diaria por debajo de su valor de 5 días antes. Solo se usan días cerrados antes de la vela.
- Setup:
  - cierre < EMA80; EMA20 < EMA80 < EMA80[−4];
  - ADX14 ≥ 26 y 24 ≤ RSI14 ≤ 48;
  - rango ≤ 3·ATR14.
- Entrada en corto con cierre < mínimo de las 26 velas previas.
- Stop: frac = max(2·ATR/c; 0,8%), sin entrar si supera 5,5%.
- Chandelier: peor cierre + 3,0·ATR (más corto que el 4,2 de R2), con el mismo endurecimiento a 5R y 8R; BE desde 1,75R; stop temporal de 60 velas (10 días).
- Riesgo 0,5% por trade, la mitad del largo.

**B2. Corto-o-plano de crisis**, diario, en SPX, oro y BTC.
- Posición = −0,17/σ30 (techo 2x) si r252 < 0 y cierre < SMA200; si no, 0.
- BTC usa perpetuo con funding y spot en 2018.

**B3. Momentum entre activos del núcleo** (los 7).
- Al cierre de cada mes, ranking por retorno de 12 meses saltando el último (r252 − r21).
- Largo los 2 primeros y corto los 2 últimos. Cada pata: nocional = equity · ¼ · min(2; 0,17/σ60,i).
- Un activo entra al ranking cuando tiene 252 días de historia.
- Decisión desde 2019-04 (los 7 disponibles). Cripto: perpetuo desde 2020-10 y spot antes.

## F5. Pronósticos continuos (2 ensayos)

**T1. Pronósticos estilo Carver** en los 7 activos del núcleo, diarios.
- Reglas, con escalares de la literatura (Carver, *Systematic Trading*), sin ajustar:
  - EWMAC(16,64), escalar 3,75;
  - EWMAC(32,128), escalar 2,65;
  - EWMAC(64,256), escalar 1,87.
  - El crudo de cada EWMAC es (EMA_r − EMA_l) / σ_precio, con σ_precio = desvío de 25 días de las diferencias diarias de precio.
  - Ruptura de 80 días: 40·(p − media80)/(máx80 − mín80), suavizada con EMA de 20 y escalar 0,75.
- Cada pronóstico tiene tope ±20. El combinado es la media de los 4 por 1,2 (multiplicador fijo), con tope ±20.
- Posición = (pronóstico/10) · 0,17/σ30, con techo de 2x y banda de 25%.
- Por familia, fijado de antemano:
  - BTC, ETH, oro y SPX: largo/plano (el pronóstico se recorta a ≥ 0);
  - WTI, gas y bono: largo/corto.
- Se evalúa reemplazando a R1 dentro de P1: T1 + C6.

**T2. T1 con atenuación por vol** (Carver, *Advanced Futures Trading Strategies*).
- Multiplicador = EMA10 de (2 − 1,5·Q), con Q el percentil de σ30 actual dentro de su historia previa (mínimo 1 año).

## F6. Cartera y validación (≤ 2 ensayos de cartera)

**Construcción:** la de F2 de r50, sin cambios: riesgo inverso con vol expansiva, vol 17%, k ≤ 8, rebalanceo mensual y sin freno.
- Las mangas se simulan con cuentas separadas, lo que es conservador en fees.
- En una operativa real el neteo por símbolo es obligatorio. Queda como requisito de ejecución.

**Compuertas de manga diversificadora**, todas obligatorias:
1. Sharpe propio ≥ 0,3 en la lente de decisión (canasta del ensayo).
2. PnL > 0 sumado sobre sus ventanas bajistas (§1) dentro de la decisión.
3. Sin veto en la lente larga.
4. ρ diaria con P1 ≤ 0,2 en la decisión.
5. Mangas con stop: ≥ 30 trades y top-5 < 60% del PnL.

**Inclusión greedy** sobre P1, por mejora de Sharpe en 2018-09+. Una manga entra si:
- sube el Sharpe de cartera ≥ +0,05, o suma ≥ +1 trimestre positivo sin bajar el Sharpe;
- y no baja el Sharpe 2021–25 en más de 0,05.

T1 o T2 reemplazan a R1 solo si su cartera supera a P1 con esa misma regla.

**Ensayos de cartera:**
- P2, la cartera final;
- P2b, solo si hace falta una variante, por ejemplo T1 contra R1.

**Métricas a reportar:**
- metas r9, con la regularidad como seguimiento;
- DSR con el N final;
- porcentaje del PnL que aporta el lado corto;
- retorno en los trimestres objetivo de F2.

**Validación congelada.** El mapeo de familias se fija ahora:
- A1 en cobre (commodity sin deriva);
- B2 en Nasdaq, EWJ, EWY y plata;
- T1 en los 5: plata y equity largo/plano, cobre largo/corto.
- A2, A3, A4, A5 y B1 no tienen activo de validación (declarado; las altcoins están diferidas a r52).

**Puertas de validación** (las de `P1_FREEZE.md`):
- mayoría de combinaciones con Sharpe > 0;
- ningún derrumbe (Sharpe < −0,5 o DD < −30%);
- canasta con Sharpe > 0 y t ≥ 1,28.

**Una manga que falla la validación sale de P2.**

## F7. Cierre
- Se congela P2 si mejora a P1; si no, sigue P1.
- Informe de cierre. Propuesta de r52: SOL/XRP/BNB y la mirada única a 2026, con autorización del usuario.

## Presupuesto
- N parte de 98:
  - A1–A5: +5;
  - B1–B3: +3;
  - T1–T2: +2;
  - P2/P2b: ≤ +2.
- Final ≤ 110; techo duro de 115.
- F0, F1, F2 y la validación no suman.
- Jesse: ≤ 10 corridas en F1. Las mangas nuevas no se confirman en Jesse en r51.
