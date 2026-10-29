# r49 Fase 2c: manga WTI (Dukascopy) e historia larga oro+SPX (2026-10-24)

**Veredicto:**
- **La cartera de 4 mangas no pasa r9 y empeora frente a la de 3.**
  - Con WTI: CAGR 18,9%, DD −22,5%, Sharpe 1,10, trimestres positivos 65% (13/20), DSR 0,54 (N=57).
  - Sin WTI: 29,98%, DD −18,4%, Q 75%.
  - El WTI solo-largo queda plano (Sharpe 0,05) y el L/S pierde; la regla B4 lo deja solo-largo.
- **Historia larga:** la regularidad de 2021–25 **no se sostiene**. La cartera oro+SPX da 50% de trimestres positivos en 2013–2020 (Sharpe 0,35, DD −30%) contra 70% en 2021–25. Q80 queda lejos en ~50 trimestres.

## Datos (Dukascopy, descarga aprobada por el usuario)

| Serie | Símbolo Jesse | Cobertura | Notas |
|---|---|---|---|
| WTI (LIGHTCMDUSD) | `Custom Data / WTI-USDT` | 2020-08-02 → 2025-12-31, 1,89 M velas 1m | Ver abajo. |
| Oro (XAUUSD) | `Custom Data / XAU-USDT` | 2010-01-01 → 2025-12-31 | Los días hábiles vacíos son feriados. |
| SPX (USA500IDXUSD /10) | `Custom Data / SPXD-USDT` | velas 1m desde **2012-01-16** (no desde 2010) | Símbolo separado de `SPY-USDT`, el proxy HistData, para no mezclar fuentes. |

**WTI:**
- **Escala verificada** contra niveles conocidos: 40,0 en 2020-09, 106 en 2022-06, 57,4 en 2025-12. Abril de 2020, con precio negativo, queda fuera porque los datos empiezan en agosto.
- **Sesión observada:** domingo 18:00 a viernes 17:00 Nueva York, con pausa 17–18.
- **Huecos fuera de horario** (más de 5 min): 300. Son feriados, cierres anticipados (Acción de Gracias, Navidad, 4 de julio) y micro-huecos. No hay huecos largos fuera de feriados.
- **Rolls:** es un CFD continuo con roll mensual sin ajustar. Entre minutos consecutivos hay 11 saltos de más de 2%: 9 son aperturas de fin de semana (por ejemplo, Ucrania en 2022-02/03) y 2, a mitad de semana (2022-06-16 y 2022-07-18), coinciden con fechas de roll. Los rolls típicos dejan gaps menores al 2% que el motor ve como precio.

**Transporte:** `datafeed.dukascopy.com` por HTTPS expira desde esta red, así que se usó HTTP. La integridad la garantiza el decodificador estricto (LZMA, registros de 24 bytes, precios positivos, timestamps por minuto, envolvente OHLC). Se agregó `--base-url` a `dukascopy_download_v3.py`.

**Importación:** la importación completa excedía el tiempo del MCP, pero terminó en el host. Se verificó la cobertura con `get_existing_candles` antes de seguir.

## Manga WTI (2020-10-15 → 2026-01-01, sin funding: perpetuo TradFi con funding 0, declarado)
- Motor solo-largo idéntico al nulo. Cambian solo el nombre y `trading_hours`: sesión CFD de energía, día hábil de 6 velas y anualización con 252, igual que la manga SPY.

| | Sesión | CAGR | DD | Sharpe | Trades | PnL largo | PnL corto |
|---|---|---|---|---|---|---|---|
| WTI solo-largo | http://localhost:9200/#/backtest/063c2564-80c9-4e19-9b64-4add88e660a0 | −0,02% | −28,4% | 0,05 | 13 | −8 | — |
| WTI L/S | http://localhost:9200/#/backtest/bb04bfbf-5be1-4201-ac23-1aa14533191f | −4,2% | −38,8% | −0,33 | 27 | +759 | **−2.750** (14) |
| B&H WTI (precio) | — | 6,8% | −56,4% | 0,36 | — | — | — |

- **Regla B4:** el corto pierde y el Sharpe L/S es menor que el del solo-largo, así que WTI queda **solo-largo**.
- **Lectura:** en 2020–25 el petróleo no tuvo tendencias que el canal 20–250 d capturara con ventaja. Fue mayormente rango de 65–90 tras el pico de 2022.

## Cartera de 4 mangas (construcción B fijada; N=57)
- **Construcción:** BTC, PAXG, SPY y WTI, todas solo-largo; vol expansiva, ≥120 días de exposición, rebalanceo mensual, 17%, techo 2,5, freno −20%.
- **Freno:** activo 360 días.

| Puerta r9 | 4 mangas | 3 mangas (Fase 2b) |
|---|---|---|
| CAGR ≥30% | 18,9% ✗ | 29,98% ✗ |
| DD ≤20% | −22,5% ✗ | −18,4% ✓ |
| PF ≥1,2 | 6,1 ✓ | 9,8 ✓ |
| Meses + ≥65% | 62,7% ✗ | 62,7% ✗ |
| Trimestres + ≥80% | 65% (13/20) ✗ | 75% ✗ |
| Mediana mensual >0 | +0,47% ✓ | +1,43% ✓ |
| Sin los 2 mejores meses | +69% ✓ | +147% ✓ |
| DSR ≥0,95 | 0,54 ✗ | 0,79 ✗ |

**Correlación de WTI:**
- **Período completo:** con BTC −0,01, con PAXG 0,07 y con SPY 0,06 (diaria). Semanal ≤0,10.
- **Trimestres negativos (agregado):** con BTC 0,01, con PAXG 0,05 y con SPY 0,14.
- **Por trimestre:** con PAXG 0,63 en 2022Q3; con SPY 0,32 en 2021Q3 y 0,26 en 2023Q2.
- **Lectura:** WTI está descorrelacionado, pero sin retorno propio. Le quita peso de riesgo a las mangas que sí rinden y suma trimestres negativos: 2021Q3, 2022Q3 y 2023Q2.

## Historia larga (motor solo-largo sin cambios; 2026 sin tocar)

| | Sesión | Ventana | CAGR | DD | Sharpe | Trim. + | DSR (N=57) |
|---|---|---|---|---|---|---|---|
| Oro | http://localhost:9200/#/backtest/124232e7-30d0-4dfb-a5b6-9cfc0c8461b2 | 2011-01 → 2025 | 7,8% | −29,9% | 0,68 | 48% (60) | 0,62 |
| SPX | http://localhost:9200/#/backtest/3b113aa3-1c44-4ac9-b0c5-e780d3c6eee8 | 2013-01 → 2025 | 6,9% | −21,1% | 0,62 | 58% (52) | 0,46 |
| **Cartera oro+SPX** (B) | analítica | 2013-08 → 2025 | 14,3% | −30,2% | 0,81 | **58% (50)** | 0,70 |

Por subperíodos:
- **Oro:** 2013–2020 CAGR 1,7%, Sharpe 0,22, Q 38%; 2021–25 CAGR 16,9%, Sharpe 1,20, Q 60%. El B&H del oro da 7,8% / DD −44,9%.
- **SPX:** 2013–2020 CAGR 5,1%, Sharpe 0,49, Q 53%; 2021–25 CAGR 9,8%, Sharpe 0,81, Q 65%. Pierde contra su B&H (12,7%, Sharpe 0,79).
- **Cartera:** 2013–2020 CAGR 4,7%, DD −30,2%, Sharpe 0,35, Q **50%** (30 trimestres); 2021–25 CAGR 30,3%, Sharpe 1,39, Q 70%.
  - Por año: 2014 −19,3%, 2015 −13,0%, 2018 −5,5% y 2022 −7,9%. El freno estuvo activo 1.740 días.
  - Signos trimestrales 2013Q3 → 2025Q4: `-+-+------+---++++--+-++++-+++++-+---+++-++++-++++`.

**Conclusión:** 2021–25 fue un período favorable para este motor (oro, BTC y SPY con tendencias fuertes). En 2013–2020 la misma construcción da la mitad de trimestres positivos. Q80 no es una propiedad estable del motor de tendencia sobre estos activos.

**Pendiente por presupuesto:** la corrida larga de WTI (extender la ventana a 2010–2020). Requiere además completar la descarga WTI 2010–2020, que no se hizo. La cartera larga es solo oro+SPX.

## Frecuencia (preocupación marcada por el usuario)

| Manga | Trades por año | Ajustes de tamaño por año |
|---|---|---|
| BTC (2020–25) | 1–5 (≈2) | 6–24 (≈20) |
| PAXG | 1–4 (≈2, ninguno nuevo en 2024–25: posición abierta) | 11–25 (≈17) |
| SPY | 0–3 (≈1,4) | 3–26 (≈17) |
| WTI | 1–3 (≈2,2) | 8–13 (≈11) |
| Oro (2011–25) | 0–6 (≈2) | 4–24 (≈13) |
| SPX (2013–25) | 0–3 (≈1) | 6–26 (≈17) |
| **Cartera de 4 mangas** | **5–13 (≈7)** | **40–71 (≈65 en 2023–25)** |

- **Rebalanceo de cartera:** el cambio medio mensual de peso es 1,9% relativo, y casi ningún mes supera la banda de 25% (1 en 5 años). En la práctica, los ajustes los hace cada manga, por su banda de 25% y la vol objetivo.
- El motor opera muy poco: un trade nuevo cada ~6 meses por activo, más unos 1–2 ajustes de tamaño por mes y por manga. Eso explica por qué no alcanza ≥100 trades por manga.

## Presupuesto y N
- **Corridas económicas:** 4 de las 4 permitidas en la Fase 2c (WTI solo-largo, WTI L/S, oro largo, SPX largo). Quedan 1 de 15 en r49.
- **Intentos técnicos fallidos:** 3, todos de warmup de SPX; el último resuelto bajando a 600 velas.
- **N declarado: 57.** Suma la decisión de lado de WTI y su inclusión. Las corridas de historia larga son validación del mismo motor, no una selección nueva.

## Recomendación
- No incluir WTI con este motor.
- La historia larga indica que la regularidad r9 (Q80, M65) **no es alcanzable con el motor de tendencia sobre 3–4 activos**: en 2013–2020 cae a ~50% de trimestres positivos.
- Antes de gastar la última corrida, decidir con el usuario entre:
  1. redefinir la vara de regularidad para una cartera de tendencia, por ejemplo Q ≥ 60–65% en historia larga;
  2. la Fase 3b propuesta (validación multimercado de 15–20 mercados, aún no aprobada);
  3. cerrar r49 con la cartera de 3 mangas como mejor resultado documentado.

Análisis: jobs `31e758e48d584b659c24cefcb6b73ead` (cartera de 4 mangas y frecuencia) y `42ed3bf8a7184f539b4618f149b15f50` (historia larga).

Dashboard (sesiones nuevas):
- http://localhost:9200/#/backtest/063c2564-80c9-4e19-9b64-4add88e660a0
- http://localhost:9200/#/backtest/bb04bfbf-5be1-4201-ac23-1aa14533191f
- http://localhost:9200/#/backtest/124232e7-30d0-4dfb-a5b6-9cfc0c8461b2
- http://localhost:9200/#/backtest/3b113aa3-1c44-4ac9-b0c5-e780d3c6eee8
