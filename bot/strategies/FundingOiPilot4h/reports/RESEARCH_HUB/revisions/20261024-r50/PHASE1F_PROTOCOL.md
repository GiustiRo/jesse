# r50 F1f: tendencia sobre el universo amplio de futuros operables

Fecha: 2026-10-25. Pedido del usuario: «repasemos todo lo que hicimos pero en futuros, y si hace falta exploraciones nuevas aplicadas en futuros». Este archivo se commitea **antes** de descargar los datos nuevos o correr F1f.

## 0. Regla de alcance (usuario, 2026-10-25)
- Toda candidata se opera **solo con futuros USDT-M de Binance**.
- Spot y ETF sirven únicamente como **proxy de datos históricos** del perpetuo que se operaría.
- K1, K1r y P3 quedan fuera de alcance, porque operan una pata en spot.

## 1. Repaso de r50 bajo la regla
- **Motores de r50 que siguen válidos en futuros:** R1–R6, M1–M4, N1–N4, C0–C6, T1–T4, X1 y V1.
  - En cripto se probaron sobre perpetuos con funding real.
  - En TradFi se probaron sobre CFD de Dukascopy, como proxy de los perpetuos TradFi de Binance (XAUUSDT, SPYUSDT, CLUSDT, NATGASUSDT, TMF/TBT, XAGUSDT, QQQUSDT, COPPERUSDT, EWJUSDT, EWYUSDT).
- **Sesgos declarados:**
  - la ventana larga cripto usa spot y no paga funding;
  - los perpetuos TradFi no tienen historia de funding, así que se toma funding = 0.
- **Lo aprendido que se mantiene:** la tendencia (R1) y las rupturas cripto (R2/R3) generalizan; la reversión de corto plazo no.

## 2. Universo amplio (solo perpetuos que hoy existen en Binance)
Universo verificado con `exchangeInfo` de Binance USD-M el 2026-10-25: 225 contratos `TRADIFI_PERPETUAL`.
- **Ya cargados (exploración):**
  - núcleo: XAU, SPX→SPY, WTI→CL, NATGAS, bono→TMF/TBT, BTC y ETH;
  - validación ya gastada: XAG, NDX→QQQ, COPPER, EWJ y EWY.
- **Nuevos para exploración**, con proxy diario de Yahoo (ETF, precio ajustado por splits):

| Perpetuo | Proxy | Qué es |
|---|---|---|
| IWMUSDT | IWM | Russell 2000 |
| EWZUSDT | EWZ | Brasil |
| EWTUSDT | EWT | Taiwán |
| GDXUSDT | GDX | Mineras de oro |
| SMHUSDT | SMH | Semiconductores |
| XLEUSDT | XLE | Energía |
| XBIUSDT | XBI | Biotecnología |
| BZUSDT | BNO | Brent |
| XPTUSDT | PPLT | Platino |
| XPDUSDT | PALL | Paladio |

**Se excluyen:**
- ETF apalancados, inversos o de volatilidad: TQQQ, SQQQ, SOXL, SOXS, TZA, UVXY, KORU, NVDL, TSLL, MSTU, TMF/TBT como manga nueva y BITO;
- acciones individuales (riesgo idiosincrático);
- FX (USDBRL);
- pre-market.

Los activos de confirmación de F1d §4 siguen reservados y no se cargan.

## 3. Mangas
- **R1-amplio:** R1 sin cambios.
  - Activos con datos de 1m (núcleo y validación gastada): en 4h, con la configuración de F1b/F3.
  - ETF con datos solo diarios: en velas diarias (1 vela por día, 252), con la misma adaptación declarada en F3.
  - Costes: taker 0,045%, slippage extra de 5 bp por lado en los perpetuos TradFi nuevos (liquidez no medida) y los de la enmienda 4b en los ya conocidos.
- **C6:** rupturas cripto R2 + R3 en BTC y ETH, sin cambios.

## 4. Compuertas

**R1-amplio (canasta equiponderada de todos los mercados):**
- Sharpe ≥ 0,5 en la ventana larga y en la común;
- Sharpe > 0 en las dos mitades de la larga (corte en 2018-01-01);
- top-5 trades < 60% del PnL.

**Cartera P4 = R1-amplio + C6** (construcción de F2 congelada: riesgo inverso, vol 17%, k ≤ 8). En las dos ventanas:
- CAGR ≥ 30%;
- DD ≤ 20%;
- PF ≥ 1,2;
- mediana mensual > 0;
- positiva sin los 2 mejores meses;
- DSR ≥ 0,95 con N = 94.

La regularidad se reporta como seguimiento. También se reporta R1-amplio solo, como cartera escalada desde 2011.

## 5. Si P4 pasa
Se congela y sigue la confirmación única de F1d §4:
- R1 en DAX, Nikkei, FTSE, soja, azúcar y cacao;
- C6 en SOL, XRP, BNB y DOGE;
- 2026 para R1/R2/R3.

Después, F4 en Jesse, que puede confirmar R1 sobre los perpetuos con datos de 1m y C6.

## 6. N
Dos variantes nuevas: R1-amplio y P4. **N declarado: 94.**
