# r49 Fase 2b: diagnóstico 2021–22 y protocolo fijado antes de las corridas

Fecha: 2026-10-24. Este archivo se commitea **antes** de correr el paso C. Nada de lo que sigue se ajusta mirando los resultados de C.

## A. Diagnóstico

Hecho solo con `run_analysis` (job `dcde8606cc594e4895b5ae1fd948cedf`) sobre las curvas de Fase 2:
- BTC: `b4792187…`
- PAXG: `02a484b6…`
- SPY: `21063c59…`
- B&H BTC: `02e52011…`

La cartera es la de Fase 2: risk parity de 365 d, techo 2,5 y freno −12%/−6%.

### Signos trimestrales de la cartera (2021Q1–2025Q4)

14 de 20 positivos (70%).

Negativos:

| Trimestre | Cartera | Sin freno | BTC | PAXG | SPY |
|---|---|---|---|---|---|
| 2021Q3 | −3,2% | −3,2% | +0,8% | −2,1% | −0,4% |
| 2021Q4 | −1,0% | **+1,0%** | +2,6% | −2,2% | +4,4% |
| 2022Q2 | −3,7% | −7,3% | −1,8% | −5,1% | −0,7% |
| 2022Q3 | −1,2% | −2,4% | −0,1% | −0,9% | −1,5% |
| 2022Q4 | −0,6% | −1,2% | −1,1% | +2,6% | −0,7% |
| 2023Q3 | −7,5% | −6,4% | −4,6% | −1,2% | −2,0% |

Sí, los trimestres negativos se concentran en 2021–22: 5 de 6. El restante es 2023Q3.

### Atribución por causa

**(a) Motor solo-largo en mercado bajista.** 3 trimestres (2022Q2–Q4), −5,4 pp sumados en la cartera.
- En 2022 BTC cayó −65% y SPY −19%. El motor quedó casi plano en BTC (exposición media 0,02x, 31% de días con posición), así que no perdió mucho, pero tampoco ganó.
- La pérdida vino de SPY (−9,3% en el año, con 15% de días en el componente 250 d) y de PAXG en 2022Q2 (−5,1%).
- Un lado corto podría capturar ese régimen: es la hipótesis de C1.

**(b) Warmup y componentes inactivos.** 1 trimestre (2021Q3, −3,2 pp), sobre todo por PAXG.
- En 2021 PAXG no tenía historia suficiente para el componente de 250 d (0% activo) y el de 120 d estaba activo solo un 28% del tiempo.
- La manga perdió −8,3% en un oro lateral (−5,1%).
- Además, la cartera estuvo en efectivo hasta 2021-03 por la ventana de vol de 365 d, con mínimo de 120.

**(c) Freno −12%/−6%.** Cambió el signo de 1 trimestre: 2021Q4 pasó de +1,0% a −1,0%. Su costo real está en la recuperación:
- 2022: activo 365 días; ahorró +4,7 pp.
- 2023: activo 265 días; costó **−37,8 pp** (el año dio +25,6% contra +63,5% sin freno). 2023Q1 dio +8,5% contra +24,7%.
- 2021: costó −2,0 pp.
- Neto: −35,1 pp en el período. En 2023Q3 el freno ya estaba restaurado y ese trimestre es negativo igual.

**(d) Whipsaw y fees.** Despreciable como causa de signo.
- Fees totales de las tres mangas: ~460 USDT en 5 años sobre 10.000 por manga, menos de 0,1% anual.
- Trades perdedores de menos de 10 días: 2, por −188 USDT en total.
- 2023Q3 (−7,5%) es devolución de tendencia: BTC −4,6% tras el rally de 2023Q1–Q2, con todas las mangas largas a la vez. Es el costo normal del trend following, no ruido de ejecución.

**Exposición media por año** (× equity de la manga):

| Año | BTC | PAXG | SPY |
|---|---|---|---|
| 2021 | 0,14 | 0,29 | 1,15 |
| 2022 | 0,02 | 0,45 | 0,15 |
| 2023 | 0,32 | 0,68 | 0,74 |
| 2024 | 0,20 | 1,04 | 1,37 |
| 2025 | 0,25 | 0,88 | 0,91 |

**Componentes activos:** se aproximaron con cierres diarios, porque el motor real usa velas de 4h y máximos/mínimos.
- BTC 2022: 20 d 38%, 55 d 19%, 120 d 0%, 250 d 2%.
- SPY 2022: 33%, 16%, 5% y 14%.
- PAXG 2021: 38%, 24%, 28% y 0% (sin historia).

### Aclaración pedida por el usuario
**No hubo walk-forward ni re-estimación de parámetros.**
- Los lookbacks 20/55/120/250, el objetivo de 17%, el techo de 2x, la banda de 25% y la salida N/2 son constantes fijas en el código desde la Fase 0.
- Lo único estimado es la volatilidad realizada:
  - dentro de cada estrategia, sobre las últimas 30 jornadas de velas cerradas, de forma causal;
  - en la cartera, con datos hasta el cierre de mes y pesos aplicados desde el día siguiente (`shift(1)`).

## B. Protocolo fijado (por principio, sin barrer variantes)

### B1. Freno: seguro catastrófico
Con DD de la cartera ≤ −20%, el riesgo se multiplica por 0,5. Se restaura al marcar un nuevo máximo de equity o a los 60 días, lo que ocurra primero. Reemplaza al freno −12%/−6%.

### B2. Construcción de cartera
- Pesos por riesgo inverso con vol de ventana **expansiva**, desde el inicio de cada curva hasta el cierre de mes.
- Una manga entra cuando acumula ≥120 días con retorno distinto de cero (días de exposición).
- Rebalanceo mensual, con pesos aplicados desde el día siguiente.
- Escalado a vol de cartera 17% con la covarianza expansiva.
- Techo de 2,5 por manga.
- Medición desde el primer mes con pesos.
- Las ventanas 60/180/365 de Fase 2 ya cuentan en N y no se reutilizan.

**Verificación sobre las curvas de Fase 2** (sin elegir nada a partir de esto): el freno nuevo se activa **0 días**. El primer mes con pesos es 2021-07.

### B3. Motor largo/corto (C1)
Es la misma lógica que `R49NullDonchianEnsBtc`, con cada componente en −1/0/+1:
- **Largo:** entra con cierre > máximo de N velas previas y sale con cierre < mínimo de N/2.
- **Corto (simétrico):** entra con cierre < mínimo de N velas previas y sale con cierre > máximo de N/2.
- Si en la misma vela un componente sale de un lado y cumple la entrada del otro, cambia de lado.
- La exposición es la media de los componentes, en [−1, 1]. El signo da la dirección y el tamaño es |media| × 17% / vol, con techo de 2x.
- No cambian los lookbacks, la vol objetivo, la ventana de vol, la banda de rebalanceo ni el techo.
- Al cruzar cero, la posición se cierra y se abre la del lado opuesto.

**Separación de tramos:** cada trade de Jesse tiene un único lado (`type` long/short), así que la atribución por trade es exacta. El PnL de un tramo es la suma de `PNL` de sus trades; incluye fees, y el funding va en un campo aparte que se suma.

**PAXG/SPY:** se usan las mismas copias por activo, con las diferencias exigidas por el instrumento ya documentadas en Fase 2.

### B4. Regla de decisión por lado (fijada ahora)
En cada activo (BTC, PAXG, SPY y CL) se conserva el lado corto si, en 2020-10 → 2025, se cumplen ambas condiciones:
- el tramo corto tiene PnL neto > 0;
- el Sharpe de la curva L/S es ≥ al de la curva solo-larga del mismo activo.

Si no se cumplen, el activo queda solo-largo en la cartera, con la curva solo-larga existente.

Para CL no hay curva solo-larga corrida: se compara con su propia curva L/S restándole la contribución del tramo corto. Si el PnL corto > 0, se conserva L/S. **No se corre CL solo-largo.**

### B5. ETH solo-corto (C2)
Es el mismo motor con los componentes en −1/0. Corre en `ETH-USDT` perpetuo con funding histórico **solo si existe dataset para ETH**; si no, sin funding, y se declara.

Entra a la cartera si cumple ambas:
- Sharpe ≥ 0,5;
- correlación diaria con la manga BTC elegida ≤ 0,3.

### B6. 4.ª manga, petróleo WTI con L/S (C3)
- **Datos:** proxy HistData WTIUSD 1m 2020–2025, importado con `clean_and_import_custom_candle_csv`.
  - La descarga de archivos externos necesita aprobación explícita del usuario en esta sesión, con nombre, fuente y tamaño.
  - Si no se obtiene o la importación falla, CL queda fuera y se reporta. No se sustituye la fuente.
- **Sesión:** la de CFD de energía. Domingo 18:00 a viernes 17:00 hora de Nueva York, con pausa diaria de 17:00 a 18:00, en `trading_hours()` con zona `America/New_York`.
- **Día hábil:** como en SPY, se cuenta en velas de sesión y la anualización usa 252 días.

### B7. Cartera final (C4)
Se construye con B1+B2 sobre BTC, PAXG y SPY (cada uno con el lado que dicte B4), más CL si existe y ETH-corto si entra por B5.
- Se evalúan las puertas r9 completas y el DSR.
- Se reporta la correlación de cada manga en los trimestres negativos de la cartera.

### B8. N
Decisiones nuevas de selección:
- 3 a 4 decisiones de lado (BTC, PAXG, SPY, CL);
- la inclusión de ETH;
- la construcción B1/B2, que reemplaza a las variantes de Fase 2 (ya contadas).

Son ≈ +5. **N declarado para C4: 55** (era 50). Se reporta también el DSR con N = 650 como cota.

### Presupuesto
≤ 5 corridas económicas (BTC L/S, PAXG L/S, SPY L/S, ETH corto, CL L/S), dentro de las 9 restantes de r49. Ventana 2020-10-15 → 2026-01-01. No se toca 2026.
