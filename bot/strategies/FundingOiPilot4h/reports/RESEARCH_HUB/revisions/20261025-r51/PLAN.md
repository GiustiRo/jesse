# r51: cortos, bono y WTI con reglas propias, sobre la base P1 confirmada

## Contexto
r50 cerró con P1 = R1 (Donchian solo-largo, 7 activos) + C6 (rupturas cripto 4h), congelada en `5caf4a53`:
- 2018-09 → 2025: CAGR 36,9%, Sharpe 1,60, 70% de trimestres positivos;
- 2021–25: CAGR 24,6%, Sharpe 1,44, 60% de trimestres positivos;
- N = 98; corridas Jesse usadas: 0 de 10.

Tres huecos quedaron abiertos:
1. **Todo es solo largo.** Los cortos probados en r50 (M1 largo/corto y M3 con régimen) perdieron como mangas propias.
2. **El bono resta todos los años y el WTI no aporta.** Son, sin embargo, los activos más descorrelacionados (ρ ≈ 0).
3. **La regularidad no alcanza las metas:** 58% de meses y 70% de trimestres positivos.

Alcance que fijó el usuario para r51:
- reglas específicas para el bono y el WTI;
- **cortos como prioridad central**;
- SOL, XRP y BNB diferidos;
- paper fuera de alcance;
- evaluar un enfoque técnico transversal sin complejizar de más.
- Decisión nueva (2026-10-25): **TLT diario 2002–2025 se suma como lente larga del bono que solo veta.** La ventana que decide sigue siendo 2018-03 → 2025.

Reglas vigentes:
- 2026 reservado;
- solo perpetuos USDT-M de Binance;
- preregistro antes de mirar resultados y conteo en N;
- nada de live, paper ni Pi.

## Qué dice la evidencia externa (investigación del 2026-10-25)
Notas completas en `research_notes/Bono WTI altcoins y regularidad r51/` (raíz del repo).

1. **Bono: el problema de R1 es estructural.** Un sistema solo-largo en bonos se pierde el corto de 2022 y compra los rebotes falsos.
   - La tendencia lenta (3–12 meses) largo/corto es la mejor evidencia: Hurst-Ooi-Pedersen dan Sharpe bruto 0,29–0,38 por activo, y el horizonte de 12 meses es el mejor.
   - Desde 2022 la correlación acciones–bonos es positiva, así que el largo en bonos perdió su papel de cobertura.
   - Regla con lógica económica: permitir el largo en bonos solo con correlación SPX–bono negativa.
   - Efectos de calendario: el ciclo de subastas (Lou-Yan-Zhang 2013) y el fin de mes (Hartley-Schwarz) responden a flujos de dealers e índices, pero no tienen fuera de muestra publicado. El drift pre-FOMC desapareció después de 2015.
2. **WTI:** se espera Sharpe 0,2–0,4 con tendencia largo/corto. Su estacionalidad es in-sample y probablemente minada, así que **no se prueba**.
   - El único proxy de estructura que se calcula solo con precio y tiene mecanismo es el spread Brent–WTI. BZUSDT y CLUSDT existen (verificado en `exchangeInfo`, listados desde 2026-04-01).
3. **Cortos por familia:**
   - En acciones y bonos, la pata corta compra sobre todo protección de crisis. Hamill-Rattray-Van Hemert (Man, 1960–2015): forzar corto-o-plano mejora las crisis pero baja el retorno medio.
   - En commodities, la evidencia está a favor de los cortos en contango, como el gas.
   - En cripto, los perdedores rebotan fuerte: no hay evidencia de cortos simétricos con ventaja propia. Sirven solo como cobertura en bajistas largos (2018, 2022), con salidas rápidas. La mejor mezcla reportada es 70/30 largo/corto, mejor que 50/50.
   - No hay estudios fuera de muestra del filtro SMA200/SMA50; es solo de practicantes.
4. **Regularidad (cálculo propio, aproximación normal).** P(período > 0) = Φ(SR·√(meses/12)).
   - Con Sharpe 1,5 se esperan ~67% de meses y ~77% de trimestres positivos.
   - El 80% de trimestres exige Sharpe ≈ 1,7.
   - P1 queda por debajo de esas cifras por la asimetría positiva de la tendencia.
   - Las palancas con evidencia son mezclar velocidades poco correlacionadas (Man AHL) y sumar mangas descorrelacionadas.
   - El vol targeting solo sube el Sharpe en acciones (Harvey et al. 2018); en los demás activos solo recorta colas.
5. **Ejecución** (solo como supuesto de costos):
   - VIP0: maker 0,02% y taker 0,05%, con 10% de descuento pagando en BNB.
   - Las entradas maker en rupturas se llenan poco y sobre todo en las perdedoras. Por eso el arnés debe **cobrar las entradas no llenadas**.
   - Los commodities TradFi operan 24/5 desde 2026-09: el gap del fin de semana se toma entero (dato de prensa, sin verificar).
   - Si una manga corta y una larga comparten símbolo, en Binance se netean: la cartera tiene que netear por símbolo.

## Recomendación sobre el enfoque transversal
- **Sí: (a) pronósticos continuos por activo, estilo Carver.**
  - Cada activo combina con pesos fijos reglas simples: tendencia de 3 velocidades (EWMAC 16/64, 32/128, 64/256) y una ruptura.
  - Pronóstico con tope ±20; el tamaño es proporcional a la fuerza de la señal.
  - Largo/corto en activos sin deriva (bono, WTI, gas) y largo/plano en los que tienen deriva (BTC, ETH, oro, SPX), fijado por familia de antemano.
  - Es la forma más barata en N de mezclar velocidades, la palanca con mejor evidencia para la regularidad, y aplica a todos los activos.
- **(b) El escalado por vol** se prueba como una sola variante dentro de (a), sin manga aparte.
- **(c) ML como meta-labeling: no en r51.**
  - R1 diario y C6 tienen pocos cientos de trades, insuficientes para entrenar con validación purgada sin sobreajuste.
  - Se reconsidera cuando haya ≥1.000 eventos (por ejemplo, con las altcoins).

## Fases

**F0 — Preparación (no suma a N)**
- Mergear la rama `claude/funding-multi-symbol-66ff4d` (funding por símbolo, ya probada con golden de BTC) en `exploration/gpt-6.1-sol`.
- Reiniciar solo el contenedor `jesse-research-jesse-1` (:9200), sin sesiones activas, y verificar con una lectura autenticada.
- Importar el funding de ETH 2020–2025. **Requiere la aprobación de este plan.**
- Descargas a `research_scripts/data/r51/`, todas hasta 2025-12-31:
  - TLT diario de Yahoo (2002+), con `r50_etf_daily_download.py`;
  - Brent CFD de Dukascopy, con `dukascopy_download_v3.py`; BNO diario ya está como respaldo;
  - índice dólar de Dukascopy, o EURUSD si no existe, **solo como señal**.
- `PROTOCOL_R51.md` en `RESEARCH_HUB/revisions/2026xxxx-r51/` con hipótesis, parámetros por defecto, ventanas y puertas de todas las fases, commiteado antes de cualquier resultado.
- Publicar en el Hub y actualizar `DOCS.md`.

**F1 — Confirmación de P1 en Jesse (es la F4 de r50; ≤10 corridas, máximo 2 simultáneas)**
- Cinco corridas base:
  1. R2 en BTC + ETH;
  2. R3 en BTC + ETH;
  3. R1 en BTC + ETH;
  4. R1 en oro + SPX;
  5. R1 en WTI + gas + bono.
- Las otras cinco quedan de reserva para diagnosticar discrepancias.
- Se reutilizan `bot/strategies/R49NullDonchianEns*`, `BtcMomentumCore4h*` y la estrategia retest K1001; se verifica cuál corresponde a R3 y se completan los clones que falten.
- Tolerancia preregistrada por manga: |ΔSharpe| ≤ 0,10, |ΔCAGR| ≤ 1 pp y DD ±1 pp. Si no coinciden, gana Jesse y se corrige el arnés antes de seguir.
- Reporte con URLs del dashboard.

**F2 — Diagnóstico de P1 (descriptivo, no suma a N)**
- Desarmar los trimestres negativos de P1 (2018–25): qué hizo cada activo y cada manga.
- Medir cuánto habría aportado una cota ideal corta por familia. Es un techo, no una regla.
- Atribuir el PnL por familia y por dirección, y mapear las fortalezas a rescatar (C6/ETH, el oro de golpe, SPX estable).
- Sale una lista de los «trimestres objetivo» contra los que se juzga cada manga corta.

**F3 — Bloque A: activos sin deriva (bono, WTI, gas), 5 ensayos**
- **A1. Tendencia lenta largo/corto común.**
  - Señal: signo de la mezcla de retornos a 3, 6 y 12 meses, con vol objetivo, una sola regla para los tres activos.
  - Ventanas: la común 2018-03 → 2025 decide; la larga veta (bono con TLT 2002+, WTI y gas 2012+).
- **A2. A1 en el bono con compuerta de correlación.** El largo solo se permite si la correlación SPX–bono a 126 días es < 0; el corto, siempre.
- **A3. Spread Brent–WTI** (par largo/corto en BZUSDT/CLUSDT).
  - Entra con |z| > 2 sobre 60 días; sale en z = 0 o a los 20 días.
  - La lente larga veta el quiebre de 2011–13.
- **A4. Fin de mes en el bono:** largo los últimos 3 días hábiles, con entrada maker y cobro de no-llenados.
- **A5. Crudo–dólar:** A1 en el WTI, con el largo vetado cuando el dólar está en tendencia alcista a 3 meses.
- Ejecución del bono en TMF/TBT, con 15 bp de slippage y decaimiento de ETF apalancado declarado (TMF −92,6% contra TLT −48%).

**F4 — Bloque B: cortos en activos con deriva y valor relativo, 3 ensayos**
- **B1. Corto cripto 4h:** espejo de C6 (ruptura bajista con los mismos filtros invertidos), solo con régimen bajista (cierre < SMA200 diaria y SMA50 cayendo).
  - Salida rápida: chandelier más corto y stop temporal de 10 días.
  - Tamaño ≤ 50% de la pata larga, según la evidencia 70/30.
  - Se juzga en 2018 con spot y en 2022 con perpetuo, con el funding real.
- **B2. Corto-o-plano de crisis en SPX, oro y BTC (diario):** corto solo si el retorno a 12 meses es < 0 y el régimen SMA200 está activo. Se juzga por su cobertura de los trimestres objetivo de F2.
- **B3. Momentum entre activos del núcleo:** largo los 2 más fuertes y corto los 2 más débiles a 12-1 meses, rebalanceo mensual, neutral en vol.
- Ningún ensayo repite celdas de r50 (M3 en ETH no se rescata).

**F5 — Enfoque transversal, 2 ensayos**
- **T1.** Pronósticos continuos Carver en los 7 activos del núcleo, en reemplazo de R1 dentro de P1.
- **T2.** T1 más escalado por percentil de vol realizada (Baltas-Kosowski).

**F6 — Cartera y validación (≤2 ensayos de cartera)**
- Construcción de F2 de r50: riesgo inverso, vol 17%, k ≤ 8, **neteo por símbolo**.
- Regla de inclusión preregistrada para mangas diversificadoras:
  - Sharpe propio ≥ 0,3 en la ventana común;
  - PnL > 0 en sus ventanas bajistas;
  - ρ con P1 ≤ 0,2;
  - mejora del Sharpe de cartera ≥ +0,05, o al menos +1 trimestre positivo sin bajar el Sharpe;
  - sin veto de la lente larga.
- Métricas a reportar: las metas r9, la regularidad (en seguimiento), el porcentaje del PnL que aporta el lado corto y el resultado en los trimestres negativos de P1.
- **Validación de las mangas nuevas congeladas** en plata, Nasdaq, cobre, EWJ y EWY, con las puertas de `P1_FREEZE.md`: mayoría con Sharpe > 0, sin derrumbes y canasta con t ≥ 1,28.

**F7 — Cierre**
- Congelar P2, si la hay; si no, P1 sigue.
- Escribir el informe de cierre.
- Proponer r52: validación en SOL, XRP y BNB y la mirada única a 2026, las dos con autorización del usuario.

## Presupuesto y proceso
- **N:** de 98 a ≤ 112 (12 ensayos más 2 de cartera); techo duro de 115. F0, F1 y F2 y la validación no suman.
- Iteración en el arnés r50, reutilizando `r50_harness.py` (barras, cuenta y métricas) y `r50_engines.py`, sin tocar los archivos congelados; los scripts nuevos son `r51_*.py`.
- Un informe corto por fase con `save_strategy_report`, `TRIAL_REGISTRY.json` actualizado, y commit y push a `origin exploration/gpt-6.1-sol` al cerrar cada fase.
- **Autorizaciones que pide este plan:**
  - merge de la rama de funding y reinicio de :9200;
  - las descargas de TLT, Brent y dólar;
  - scripts en `research_scripts/`;
  - push.
- **Fuera de alcance:** paper/live/Pi, 2026, SOL/XRP/BNB, ML, estacionalidad del crudo y carry de funding con spot.

## Verificación
- F1: tabla arnés contra Jesse por manga, con URLs de dashboard y dentro de la tolerancia.
- F3–F5: tabla por ensayo con Sharpe común y largo, trades, resultado en ventanas bajistas, ρ con P1 y cobertura de los trimestres objetivo.
- F6: tablero de cartera contra P1 en 2021–25 y 2018-09+, con DSR calculado con el N final, más la tabla de validación en los 5 activos.
- El `TRIAL_REGISTRY.json` cuadra con el N declarado en cada informe.
