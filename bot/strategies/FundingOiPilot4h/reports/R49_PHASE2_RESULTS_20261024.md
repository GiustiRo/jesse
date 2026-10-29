# r49 Fase 2: motor Donchian nulo en BTC, PAXG y SPY (2026-10-24)

**Veredicto:** la cartera combinada **no pasa** las puertas r9. Lo que falla es la regularidad, no el retorno.
- **Configuración especificada** (risk parity, vol 17%, freno de DD): CAGR 23,1%, DD 15,3%, Sharpe 1,29, meses positivos 60%, trimestres positivos 67%, DSR 0,72. Fallan CAGR, M65, Q80 y DSR.
- **Más volatilidad no lo arregla.** Llegar a CAGR 30% exige vol objetivo ~25% con freno (DD −20,0%, en el límite) o ~20% sin freno (DD −21,3%). Ninguna variante supera 65% de meses ni 70% de trimestres positivos.
- **Las tres mangas están casi descorrelacionadas** (diaria ≤0,16), pero ninguna pasa las puertas de manga, salvo el Sharpe ≥0,8.

## Configuración
- **Motor:** `R49NullDonchianEnsBtc` sin cambios de lógica (lookbacks 20/55/120/250 d, vol objetivo 17%, long/flat, ≤2x nocional, banda de rebalanceo 25%). Las tres mangas cuentan como **una familia** de ensayos.
- **Ruta:** Binance Perpetual Futures 4h, fee 0,00045, 3x aislado, ventana 2020-10-15 → 2026-01-01. No se tocó 2026.
- **Datos:** proxies existentes, sin importar nada nuevo.
  - PAXG-USDT: copia del spot de Binance, desde 2020-08-28.
  - SPY-USDT: HistData SPX CFD /10, volumen 0, desde 2020-01-01.
- **Funding:**
  - BTC: histórico (sesión de Fase 0 reutilizada).
  - PAXG y SPY: **sin funding** (no hay histórico nativo). Es un sesgo a favor; no se inventó un proxy.

| Manga | Sesión | Diferencias respecto del motor BTC |
|---|---|---|
| BTC | http://localhost:9200/#/backtest/b4792187-8847-450d-9f52-320edb4a61dd (Fase 0, reutilizada) | — |
| PAXG | http://localhost:9200/#/backtest/02a484b6-a237-4ffb-a283-7db32354a61e | Ninguna, solo el nombre de clase (opera 24/7). Warmup de 280 velas por falta de historia: el componente de 250 d se activa recién a mediados de 2021. |
| SPY | http://localhost:9200/#/backtest/21063c59-f0f5-4a07-a66a-040f75e3f475 | Ver detalle abajo. |

Diferencias de SPY, todas exigidas por el instrumento:
- `trading_hours()` UTC Mon-Fri 00:00-20:00, la convención K1001/X03.
- Estados y volatilidad calculados sobre velas de sesión, y entradas habilitadas solo en sesión.
- "Día" = día hábil (5 velas de 4h) y anualización con 252.
- Los estados avanzan solo con una vela de sesión nueva.
- Warmup de 840 velas, todo lo disponible: el componente de 250 d arranca inactivo hasta ~2021-07.

Presupuesto: 2 corridas económicas nuevas (PAXG y SPY); quedan 9 de las 15 de r49. Hubo un intento técnico fallido de SPY: el warmup de 1.700 velas excedía los datos y se recuperó con 840.

## Mangas (curvas diarias MTM, `run_analysis`)

| | BTC | PAXG | SPY |
|---|---|---|---|
| CAGR | 12,9% | 16,2% | 9,6% |
| DD | −11,8% | −13,1% | −14,7% |
| Sharpe | 1,04 | 1,26 | 0,98 |
| Vol anual | 12,4% | 12,5% | 14,3% |
| Exposición media (× equity) | 0,19 | 0,64 | 0,85 |
| Meses / trimestres + | 47% / 41% | 47% / 50% | 57% / 62% |
| Ciclos (trades) | 11 | 10 (1 abierto al cierre) | 7 |
| PF | 6,3 | 11,6 | 24,7 |
| Top-5 / PnL | 118% | 109% | 104% |
| DSR (N=50) | 0,54 | 0,73 | 0,35 |
| B&H: CAGR / DD / Sharpe | 47,9% / −76,9% / 0,96 | 16,9% / −21,1% / 1,05 | 14,0% / −25,3% / 0,93 |

Puertas de manga:
- **Pasan:** las tres tienen Sharpe ≥0,8. Las tres superan al B&H en Sharpe y en DD; en CAGR solo frente al B&H escalado.
- **Fallan:** DSR ≥0,95, ≥100 trades y top-5 <60%, en las tres.

## Correlación de retornos de estrategia

| | BTC–PAXG | BTC–SPY | PAXG–SPY |
|---|---|---|---|
| Diaria | 0,01 | 0,16 | 0,09 |
| Semanal | −0,06 | 0,14 | 0,08 |
| Días con BTC < 0 (n=921) | −0,01 | 0,13 | 0,11 |
| Peor decil de BTC (n=191) | −0,02 | 0,13 | 0,16 |

Co-pérdidas:
- **PAXG:** cuando la manga BTC pierde, pierde el 39% de los días contra 38% sin condicionar. Independiente.
- **SPY:** pierde el 37% de los días contra 28% sin condicionar; en semanas, 46% contra 36%. Hay co-pérdida moderada con BTC.
- **En el peor decil de BTC:** PAXG −0,04% y SPY −0,27% por día, contra −0,62% de la manga BTC.

## Cartera combinada de diagnóstico (combinación analítica de curvas, no un backtest)

**Construcción:**
- Risk parity por vol realizada de 365 d (mínimo 120), incluidos los días planos.
- Rebalanceo mensual con pesos aplicados desde el día siguiente.
- Escalado a vol 17% con la covarianza de la misma ventana.
- Techo de 2,5 por manga (= 5x nocional, el techo aislado de r49).
- Freno de DD sobre la curva combinada: −12% → ×0,5, restaura en −6%.
- Medida desde 2021-03-01, el primer mes con pesos.

**Por qué 365 d:** la primera versión, con 60 d sin techo, sobreponderaba hasta 26x una manga plana con vol ≈ 0. Es un artefacto y se descartó. Con 60 d y techo da CAGR 32,2% / DD 22,6%; con 180 d, 27,5% / 16,8%. Hay sensibilidad material a la ventana.

| Puerta r9 | Vol 17% con freno | ¿Pasa? |
|---|---|---|
| CAGR ≥30% | 23,1% | ✗ |
| DD ≤20% | −15,3% | ✓ |
| PF ≥1,2 (trades de las tres mangas) | 9,8 | ✓ |
| Meses + ≥65% | 60% | ✗ |
| Trimestres + ≥80% | 67% | ✗ |
| Mediana mensual >0 | +0,86% | ✓ |
| Positiva sin los 2 mejores meses | +100,8% | ✓ |
| DSR ≥0,95 (N=50) | 0,72 (Sharpe 1,29) | ✗ |

Por año: 2021 −0,4%, 2022 −4,4%, 2023 +25,6%, 2024 +66,6%, 2025 +38,1%. El freno estuvo activo 657 días.

### ¿Qué haría falta?

| Variante | CAGR | DD | Sharpe | M+ / Q+ |
|---|---|---|---|---|
| RP vol 20%, freno | 28,1% | −16,6% | 1,34 | 60% / 71% |
| RP vol 25%, freno | 30,7% | −20,0% | 1,27 | 57% / 62% |
| RP vol 30%, freno | 39,1% | −21,3% | 1,39 | 57% / 62% |
| RP vol 17%, **sin** freno | 29,2% | −18,4% | 1,38 | 61% / 70% |
| RP vol 20%, sin freno | 33,9% | −21,3% | 1,37 | 61% / 70% |
| RP vol 25%, sin freno | 42,1% | −25,7% | 1,38 | 61% / 70% |
| Equiponderada 1/3 ×1 | 13,4% | −8,0% | 1,67 | 65% / 67% |
| Equiponderada ×2,5, freno | 31,8% | −15,8% | 1,64 | 64% / 67% |
| Equiponderada ×3, sin freno | 43,2% | −22,6% | 1,68 | 65% / 67% |

- **Retorno:** CAGR 30% es alcanzable con vol objetivo de ~20–25%, con DD de −17% a −21%.
  - El freno, tal como está definido, **le cuesta ~6 pp de CAGR a vol 17%** (29,2% contra 23,1%). Entra en DD que el trend-following recupera solo.
  - La equiponderada fija, sin estimación de vol, tiene mejor Sharpe (1,67) que el risk parity con vol móvil (1,29). La estimación de vol de mangas con muchos días planos agrega ruido.
- **Regularidad:** ninguna variante pasa Q80; el máximo es 70%. M65 solo se roza (65%) en la equiponderada. Es el hueco real: faltan ~10–13 pp de trimestres positivos. No depende del apalancamiento, que no cambia el signo de los trimestres salvo por el freno.
- **DSR:** como mejor caso, con Sharpe 1,64–1,68 y N=50, quedaría en ≈0,93 (estimado). Está por debajo de 0,95, y cada variante de construcción probada aumenta N.
- **Cuantificación pedida:** con el risk parity especificado, CAGR 30% requiere vol objetivo ~25% (DD −20%) con freno, o ~17,5–18% (DD ≈ −19%, interpolado entre 17% y 20%) sin freno. Con la equiponderada, ×2,5 (vol realizada 17,8%) da 31,8% / −15,8%. La elección de 2,5x mira la vol de toda la muestra: es diagnóstico, no una regla.

## Limitaciones
- PAXG y SPY sin funding (sesgo a favor). El B&H de SPY es solo precio, sin dividendos.
- Las historias son cortas para el lookback de 250 d en PAXG y SPY: el ensamble arranca con 3 componentes hasta mediados de 2021.
- Proxy SPY: el CFD de HistData no es el instrumento operable; sin volumen.
- Las variantes de cartera (ventanas 60/180/365, techos, freno, equiponderada) son ensayos de construcción. Si se elige una mirando estos resultados, entra en N.
- Muestra 2020-10 → 2025: 5 años y 1 régimen por activo. Q80 con 20 trimestres significa ≥16 positivos.

## Recomendación
1. La **descorrelación existe** (ρ ≤ 0,16). El motor nulo ya da un Sharpe de cartera de ~1,3–1,7 frente a ~1,0–1,26 por manga.
2. **El cuello de botella es Q80/M65.** Con tendencia pura sobre tres activos no se alcanza. Opciones, todas a acordar antes de gastar presupuesto:
   - a) más mangas descorrelacionadas: la Fase 3 opcional con 5–10 perps cripto, o activos de tendencia como bonos o FX si hay datos;
   - b) revisar la puerta Q80 a la luz de que la tendencia tiene hit-rate trimestral de ~60–70%;
   - c) una manga de carry o mean-reversion con distribución opuesta.
3. **Redefinir el freno de DD antes de la Fase 3:** en esta curva resta CAGR sin aportar regularidad.
4. **No subir la vol objetivo** para forzar el CAGR: con freno, el DD cruza el −20% a partir de vol ~25%.

Análisis: jobs `7ebbbeed698040d6a88a83a1428a3ca9` (mangas y correlaciones), `27018f7d15b544a08a27354149e6dd22` (cartera y barrido), `0f318feda80a40b6b6b3d07b292ccf50` y `69b680312d0643e688992292603d4eab` (sensibilidades).

Dashboard:
- http://localhost:9200/#/backtest/b4792187-8847-450d-9f52-320edb4a61dd
- http://localhost:9200/#/backtest/02a484b6-a237-4ffb-a283-7db32354a61e
- http://localhost:9200/#/backtest/21063c59-f0f5-4a07-a66a-040f75e3f475
