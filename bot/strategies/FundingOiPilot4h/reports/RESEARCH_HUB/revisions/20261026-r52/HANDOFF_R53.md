# Handoff a r53 (desde r52, 2026-10-26)

## Estado
- **Candidata:** P1 = R1 + C6, congelada en `5caf4a53`, confirmada en Jesse en r51.
  - 2018-09+: CAGR 36,9% y Sharpe 1,60.
  - Hasta 2024: Sharpe 1,68.
- **N = 116.**
- **2025 sigue sellado para cualquier manga nueva**: una sola mirada final, con candidata.
- **2026 reservado.**

## Mandato del usuario (vigente)
- Investigación autónoma y creativa, sin techo de N. Igual se registra cada ensayo, para que el DSR sea honesto.
- Solo perpetuos USDT-M de Binance; nada de live, paper ni Pi.
- 4h, 1h o semanal; nada de ideas tipo «apuesta a ciegas».
- Subagentes en paralelo; reintentar ante fallas.
- Abrir r54 y siguientes en sesiones nuevas cuando haga falta.

## Lo que dejó r52
1. **El ranking transversal de 50 perpetuos tiene información real**, pero no se puede cobrar con quintiles largo/corto:
   - IC semanal por rangos de 0,106 (t 5,6, elastic net);
   - mediana del spread de +0,73% semanal, contra +0,07% de media, porque las subas explosivas en la pata corta se comen todo.
2. **El momentum semanal se revierte** en este universo: IC de −0,051, t −2,9.
3. **El reloj del flujo (QOI) se replica:** t ≈ 2,9 en BTC/ETH a 8 h. Como regla sola no paga los costos.
4. **El jump model sobre BTC no mejora a P1.**

## Infraestructura lista
- **`r52_download.py`** baja de `data.binance.vision` velas 1h y funding de U50, y 1m reducido a cuartos de hora para 22 monedas.
  - Corre en el host, porque el DNS del contenedor cayó el 2026-10-26.
  - La salida va a `research_scripts/data/r52/*.npy` (gitignored, se regenera).
- **`r52_xs.py`**: panel, variables, walk-forward, cartera semanal, costos y funding. Corre en el contenedor, porque `p1_returns` usa la base de Jesse.
- **`r52_q.py`** (QOI), **`r52_j1.py`** (jump model) y **`r52_verify.py`**.
- **`r51_lib.py`**: P1 y atribución. **`r51_f6.py`**: regla de inclusión.
- **Pendiente:** guardar por MCP los informes `R52_PHASE1/2` y `R52_CLOSE`. El texto está en las notas compartidas, en `r52-informes-pendientes.md`.

## Agenda propuesta para r53 (preregistrar antes de correr)
1. **Cobrar el IC sin la cola**, sobre los mismos datos de r52:
   - pesos por rango en vez de por vol;
   - excluir las monedas con |retorno 1 semana| > percentil 90 transversal;
   - objetivo = retorno / vol;
   - holding de 2 y 4 semanas con carteras solapadas;
   - largo el quintil superior cubierto con BTC/ETH.
2. **Reversión semanal como factor propio:** largo las perdedoras y corto las ganadoras de la semana, solo en las de mayor liquidez.
3. **QOI como variable del ranking**, con medias semanales del QOI por moneda (requiere 1m de las 50).
4. **QOI como filtro o tamaño de C6** en BTC/ETH: C6 entra solo con z(QOI) > 0. Es una variante nueva de C6 y cuenta en N.
5. **Opcional:** validación congelada de C6 en SOL, XRP y BNB, el pendiente de r50. Esas monedas ya están en U50 como datos de precio, pero C6 nunca se aplicó a ellas.
- **Validación:** la de cada línea va contra 2024. La mirada única a 2025 es solo para lo que pase a cartera.
