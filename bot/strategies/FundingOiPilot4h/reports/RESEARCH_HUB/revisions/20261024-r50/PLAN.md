# r50: varios motores sobre un núcleo de 7 activos, validados en 3 más

## Contexto

r49 cerró sin candidata, pero con aprendizajes claros:
- **El motor de tendencia es real pero débil.** La cartera BTC+oro+SPY dio Sharpe 1,4 en 2021–25, pero en historia larga (2013–2020) apenas 0,35 y ~50% de trimestres positivos. 2021–25 fue un régimen favorable.
- **Los cortos del motor de tendencia simétrico pierden** en todos los activos. Solo se evaluaron en 2020–25, sin un bajista largo salvo 2022.
- **WTI no aportó con ese motor**, pero se queda: puede rendir con motores nuevos.
- **El freno −20%/60 d** estuvo activo 1.740 días en la historia larga y deprimió el resultado.

Decisiones del usuario para r50:
- Mantener la ambición r9 (Q80, M65, CAGR 30%, DD 20%) y buscar motores mejores.
- **Varios motores** con perfiles distintos, sin dar ninguno por sentado. Un motor corto no se limita a cripto.
- Universo: núcleo de 7 activos y 10 descargados en total, bajando datos en paralelo mientras se desarrollan los motores.
- BTC/ETH spot de Binance desde 2017-08, aprobado para desarrollo.
- 2026 queda reservado por definición: no se usa hasta que el usuario lo apruebe.
- Foco total en investigación; live/paper y la Pi quedan fuera de alcance.

## Respuestas a las preguntas del usuario

**¿Hay evidencia de que la tendencia necesita muchos mercados?**
Sí:
- Moskowitz-Ooi-Pedersen (2012, 58 futuros): el Sharpe por mercado va de 0,2 a 1,0 y la cartera diversificada supera 1.
- Hurst-Ooi-Pedersen (67 mercados desde 1880): Sharpe medio por mercado ≈0,4.
- Man AHL opera ~900 mercados.
- Con Sharpe 0,4 por manga y correlación 0,1, una cartera da 0,70 con 4 mercados, 0,76 con 5, ~0,85 con 7 y 1,16 con 50. Nuestro 0,8 en 2013–2025 cae justo en esa línea.
- El índice SG Trend (CTAs con 100+ mercados) tuvo 2011 −7,9%, 2012 −3,4%, 2016 −6,2%, 2018 ≈−8% y 2022 +27%. No lo hicimos peor que la industria.

**¿Qué es un "motor de distribución opuesta"?**
- La tendencia gana poco seguido y mucho de golpe, y pierde de a poco en mercados laterales.
- La reversión a la media hace lo contrario: compra caídas cortas (por ejemplo, SPY cierra cerca de su mínimo o el RSI(2) está muy bajo) y sale en el rebote, a 1–5 días. Gana el 60–78% de las veces con ganancias chicas, justo en los mercados laterales donde la tendencia sufre.
- Su riesgo es el opuesto: alguna pérdida grande en un crash. Se controla con filtro de tendencia, stop temporal y tamaño por volatilidad.
- Combinados, los años malos de uno tienden a ser aceptables para el otro. Además suma frecuencia: ~50+ trades/año en una canasta, que también ataca el problema de evidencia estadística.

**¿Los mercados pasan mucho tiempo en lateral?**
Sí. El motor de tendencia estuvo invertido en promedio solo 0,19x en BTC, y oro y SPX tuvieron largos tramos sin dirección en 2013–2020. Ese tiempo muerto es el que puede aprovechar la reversión.

**¿Historia larga y corta son dos líneas de investigación?**
No. Es **una sola investigación con dos lentes**, reportadas por separado:
1. **Ventana común (decide):** todos los activos en el mismo período, el que se operaría.
   - 2020-10 → 2025, o 2018 → 2025 en los motores cripto que usen spot.
2. **Ventana larga por activo (solo veta):** la mayor historia disponible de cada activo.
   - Oro, SPX, WTI y gas desde 2012; BTC/ETH spot desde 2017-08.

Una manga entra **solo si pasa la ventana común y no falla en la larga**. BTC nunca se compara contra 2013–2020; su lente larga es 2017–2025, con el bajista de 2018 incluido.

**¿ETH o gas natural?** Cumplen roles distintos, así que propongo los dos:
- ETH se mueve casi igual que BTC (correlación ~0,8), así que como manga direccional aporta poca descorrelación. Su valor está en los motores corto y de valor relativo ETH/BTC.
- El gas natural es de los activos más descorrelacionados de todo (con energía, acciones, oro y cripto). Es muy volátil y estacional, candidato a tendencia, reversión y corto. Aporta más descorrelación que ETH.

**¿Bonos aunque tengan poco volumen?** Sí, en investigación. Son el mejor diversificador documentado: los mayores aportes de crisis de los CTA vinieron de bonos, y 2022 se ganó en corto en bonos.
- Las señales se calculan sobre el bono del Tesoro largo subyacente (proxy de precio de 20+ años), no sobre el contrato.
- La operabilidad queda **pendiente de verificar**. `TMFUSDT` (0,7 M/día) es un ETF apalancado 3x con decaimiento y `TBTUSDT` mueve 0,1 M/día. Antes de operarlo hay que medir spread y profundidad del libro. Con una cuenta de 10k podría alcanzar, pero no se asume.

**¿Bono chino?** Lo revisé en la API de Binance (`exchangeInfo`, hoy). **No existe ningún bono chino** ni ningún otro bono fuera de EE.UU.
- Los únicos productos de renta fija son `TMFUSDT` (3x largo, Tesoro 20+ años) y `TBTUSDT` (2x corto).
- La exposición a China disponible es solo acciones: Tencent, BYD y otras de Hong Kong y China continental.
- Queda en el radar: si Binance lista un bono chino, se evalúa.

**Spot de BTC/ETH: ¿hay que hacer un proxy a futuros?** No hace falta mezclar series; cada lente usa una distinta:
- **Ventana común** (decide): el **perpetuo** 2020-10 → 2025 con funding real, igual que hasta ahora.
- **Ventana larga** (solo veta): la serie **spot** completa 2017-08 → 2025 como símbolo aparte, sin funding (sesgo declarado). Spot y perp difieren en menos de ~0,1% (la base), irrelevante para señales diarias.
- No se empalman series ni se copia spot dentro del símbolo perp, así que los datos 2020+ quedan intactos.

**Realismo:** la evidencia publicada no muestra ninguna cartera con Q80 sostenido en historia larga. r50 lo persigue igual, como pidió el usuario, y cada fase reporta qué tan lejos queda y por qué.

## Universo: 10 activos descargados

**Núcleo (7):** aquí se diseñan y calibran los motores; se puede operar en Binance.

| Activo | Perpetuo (vol. 24h) | Datos | Estado |
|---|---|---|---|
| BTC | BTCUSDT (9,8 B) | perp 2020-08+ con funding; spot 2017-08+ | perp listo; spot a importar |
| ETH | ETHUSDT | perp 2020-08+ con funding; spot 2017-08+ | perp y funding listos; spot a importar |
| Oro | XAUUSDT (519 M) / PAXG | Dukascopy XAUUSD 2010+ | listo |
| SPX | SPYUSDT (200 M) | Dukascopy USA500 2012+ | listo |
| WTI | CLUSDT (411 M) | Dukascopy 2011-12 → 2025 (sin abr–jul 2020) | listo |
| Gas natural | NATGASUSDT (22 M) | Dukascopy (proxy CFD) 2012+ | a descargar |
| Bono largo EE.UU. | TMFUSDT/TBTUSDT (<1 M, sin verificar) | proxy del Tesoro 20+ años (Dukascopy bond CFD o TLT diario) | a descargar |

**Validación (3), todos operables en Binance futuros:** **no se usan para diseñar ni calibrar.** Al final se corre el motor congelado sobre ellos, como prueba de que generaliza a mercados que no vio:

| Activo | Perpetuo (vol. 24h) | Para qué | Datos |
|---|---|---|---|
| Plata | XAGUSDT (133 M) | metales preciosos | Dukascopy XAGUSD 2010+ |
| Nasdaq 100 | QQQUSDT (39 M) | otro índice de acciones | Dukascopy USATECH 2012+ |
| Cobre | COPPERUSDT (2,8 M) | metal industrial, ligado al ciclo | Dukascopy COPPER (CFD) |
| Japón | EWJUSDT (perp desde 2026-03) | acciones de Japón, con exposición al yen | ETF EWJ diario (Stooq/Yahoo, ~2000+) |
| Corea | EWYUSDT (perp desde 2026-03) | acciones de Corea, muy cargado en semiconductores | ETF EWY diario (Stooq/Yahoo, ~2000+) |
| Platino | XPTUSDT | metal precioso e industrial | Dukascopy XPTUSD 1m si existe; si no, diario |

*Ampliación del 2026-10-25, pedida por el usuario:* la validación pasa de 3 a 6 activos con EWJ, EWY y platino, sin tocar el núcleo.
- Las reglas son las mismas: no se usan para diseñar ni calibrar, solo entran en la F3 con los motores congelados y sus datos llegan hasta 2025-12-31.
- EWJ y EWY se evalúan con velas diarias de los ETF. Sus perpetuos existen recién desde 2026-03, así que no hay confirmación posible en Jesse con 1m; queda declarado.
- Liquidez medida en Binance (spread / profundidad a ±0,2%):
  - EWY: 0,7 bp / 475k;
  - EWJ: 2,1 bp / 27k;
  - XPT: 0,1 bp / ~38k.
- Slippage extra en F3: 10 bp por lado en EWJ y XPT.

Todos los activos del universo deben ser operables con la integración actual de Binance USDT-M. No hay FX operable salvo `USDBRLUSDT` (0,5 M/día), así que FX queda fuera.

**Descargas en paralelo**, en background y sin bloquear el desarrollo. Orden de prioridad:
1. BTC/ETH spot;
2. gas natural;
3. bono;
4. plata, Nasdaq y cobre.

Si un proxy no está en Dukascopy, se reporta y se propone una alternativa antes de sustituirlo.

## Motores candidatos (hipótesis falsables, valores por defecto de la literatura)

**M1. Tendencia v2.** Velocidades rápida (10–20 d), media y lenta, con señal continua, volatility targeting y reducción de exposición cuando sube la correlación (Baltas-Kosowski).
- Solo-largo en activos con deriva alcista (BTC, oro, SPX).
- Largo/corto en activos sin deriva (WTI, gas, bono).
- Los cortos se juzgan solo en ventanas que incluyan bajistas.
- *Falsación:* no mejora al nulo de r49 en Sharpe ni en trimestres positivos, en la ventana común.

**M2. Reversión de corto plazo.** IBS/RSI(2) con filtro de tendencia de 200 d, salida a 1–5 días con stop temporal y entradas maker modeladas.
- Canasta oro, SPX, WTI, gas y bono. No para BTC/ETH: en cripto grande hay momentum diario, no reversión (Zaremba 2021; Fičura 2023).
- *Falsación:* Sharpe < 0,5, <50 trades/año en la canasta, o correlación con M1 > 0,2 en los trimestres en que M1 pierde.

**M3. Corto con régimen.** Para los 7 activos del núcleo.
- Solo cuando el activo está bajo su media de 200 d y la de 50 d cae.
- Entrada por ruptura de mínimos de 10–20 d; salida rápida por máximos de 5–10 d o 2×ATR, con stop temporal. Funding real aplicado.
- *Falsación:* Sharpe < 0,5; quitar el filtro de régimen no le resta ≥0,4 de Sharpe; o más del 50% del PnL en 3 trades.

**M4. Valor relativo ETH/BTC.** Momentum del ratio a 4–12 semanas: corto ETH / largo BTC.
- *Falsación:* Sharpe < 0,6 neto del funding diferencial, o |correlación con la dirección de BTC| > 0,3.

**M5. Carry/funding.** Solo como freno de riesgo o filtro dentro de M1/M3, no como manga propia (en 2025 rindió negativo).

**Pruebas múltiples:** cada variante cuenta en N (hoy 57), declarado en `TRIAL_REGISTRY.json`.

## Fases

**F0 — Infraestructura y datos**
- Descargas en background según la prioridad de arriba, con `dukascopy_download_v3.py` (ya tiene `--base-url`), la importación nativa de Jesse para spot y `clean_and_import_custom_candle_csv`.
- **Arnés vectorizado diario** en `bot/research_scripts/` con motores, mangas, cartera y métricas.
- El arnés debe **reproducir** las sesiones Jesse de r49 (BTC `b4792187…`, PAXG `02a484b6…`, SPY `21063c59…`) con error de equity < 0,5% antes de usarse para decidir. Así la iteración no consume corridas Jesse.

**F1 — Screening de motores** (arnés, núcleo, desarrollo hasta 2025-12-31)
- M1–M4 con hipótesis, valores y puertas fijados en un protocolo commiteado **antes** de mirar resultados.
- Costos: taker 0,045% o maker 0,018% según la orden, funding real en cripto y slippage de stop de 3–5 bps.
- Reporte por motor×activo:
  - Sharpe y trades/año;
  - trimestres positivos;
  - correlación con M1, también en los trimestres en que M1 pierde;
  - ventana común y ventana larga.
- Activos con datos aún no listos: se agregan cuando llegan, con el mismo protocolo.

**F2 — Combinación** (núcleo)
- Cartera motor×activo con risk parity, volatility targeting 17% y control por correlación, sin freno de DD.
- Regla prerregistrada: una manga entra si cumple sus puertas y mejora el Sharpe o los trimestres positivos de la cartera.
- Se reportan las puertas r9 y el DSR en las dos ventanas.

**F3 — Validación en los 3 activos no vistos**
- Motores congelados sobre plata, Nasdaq y cobre.
- Puerta: Sharpe > 0 en la mayoría de las combinaciones motor×activo, sin derrumbes. No se re-ajusta nada después de verlos.

**F4 — Confirmación en Jesse** (≤10 corridas)
- Las mangas seleccionadas se implementan como estrategias Jesse, con fees, funding y fills reales.
- Tienen que coincidir con el arnés dentro de la tolerancia. Si no coinciden, gana Jesse y se revisa el arnés.

**F5 — Freno y congelamiento**
- Freno de DD por principio: solo ante catástrofe, restaurado por tiempo.
- Se congelan código, parámetros y pesos.
- Lo que sigue (2026 o paper) lo decide el usuario.

## Proceso
- Nueva sesión "r50" con MCP `jesse-local`. A la sesión r49 se le responde que su pregunta quedó resuelta aquí y se cierra.
- Un informe corto por fase, `TRIAL_REGISTRY.json` actualizado, y commit y push al cerrar cada fase.
- Reutilizar:
  - `bot/strategies/R49NullDonchianEns*` como base y control de M1;
  - `run_analysis`;
  - `dukascopy_download_v3.py`;
  - `clean_and_import_custom_candle_csv`;
  - el funding por símbolo (`jesse/services/funding.py`; datasets BTC `0ab14bc2…` y ETH `22bd891c…`).
- Publicar r50 en el Hub (`RESEARCH_HUB/revisions/<fecha>-r50/`) y actualizar `DOCS.md`: r49 cerrada, universo, ventanas, motores y 2026 reservado.

## Verificación
- F0: tabla de reproducción arnés vs Jesse (equity y Sharpe) e inventario de los 10 activos con su cobertura.
- F1–F2: puertas por motor×activo y puertas r9 de cartera, en las dos ventanas.
- F3: tabla de los motores congelados sobre los 3 activos no vistos.
- F4: arnés vs Jesse por manga, con URLs de dashboard.
