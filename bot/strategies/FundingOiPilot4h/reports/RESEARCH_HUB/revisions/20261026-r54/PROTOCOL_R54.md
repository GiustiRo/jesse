# r54: protocolo preregistrado (fijado antes de cualquier resultado)

Continúa r53 bajo el mandato autónomo del usuario. N parte de 123. Rigen las convenciones de r52:
- datos de `data.binance.vision`, U50 y costos de r50;
- 2025 sellado y 2026 reservado.

## V1. Validación congelada de C6 en 48 alts (no suma a N)
- **Qué se prueba:** C6 tal como está congelado en `5caf4a53`, es decir `r50_f1b.r2_r3_decider` R2 y R3 50/50, sin cambiar nada.
- **Activos:** las 48 alts de U50 (sin BTC ni ETH), en perpetuo.
- **Barras:** 4h armadas desde las velas 1h de vision (OHLC exacto por agregación).
- **Costos y funding:**
  - fee taker 0,045% y maker 0,018%, como en r50;
  - funding real por símbolo (archivo de vision), con el mark aproximado por el cierre de la vela 1h de la liquidación (declarado).
- **Ventana:** simulación desde 2020-10-15 o desde el listado más 100 velas; métricas 2021-01-01 → 2024-12-31.
- **Puertas** (las de `P1_FREEZE.md`):
  - mayoría de las alts con Sharpe > 0;
  - ningún derrumbe (Sharpe < −0,5 o DD < −30%) en más del 10% de las alts;
  - canasta equiponderada con Sharpe > 0 y t ≥ 1,28.
  - El protocolo de r50 pedía «ningún derrumbe» con 4 monedas. Con 48 se fija un tope del 10% antes de ver resultados.
- Se reportan aparte SOL, XRP y BNB, la validación pendiente de r50.
- Por construcción, C6 solo opera largo.

## M1. Meta-labeling de C6 con eventos agrupados (1 ensayo)
- **Eventos:** cada entrada de R2 o R3 en las 50 monedas (V1 más BTC/ETH), con su resultado en R.
- **Variables en la vela de entrada:**
  - z(QOI) de 4h, de r52;
  - funding medio de 7 días;
  - vol de 30 días;
  - retorno de 4 semanas;
  - ADX14;
  - distancia del cierre a la EMA80 en ATR;
  - régimen de BTC (cierre diario > SMA200);
  - retorno de BTC a 7 días.
- **Modelo:**
  - regresión logística L2 (`LogisticRegression`, C = 1) sobre variables estandarizadas;
  - etiqueta = trade con R > 0;
  - walk-forward re-ajustado cada trimestre, solo con eventos cerrados antes del inicio del trimestre;
  - primera predicción en 2022-01.
- **Tamaño:** riesgo por trade = 1% × clip(2·p, 0,5, 1,5). Es dimensionamiento, no filtro, para no cortar la cola derecha.
- **Evaluación:**
  - (a) canasta C6 de las 48 alts, dimensionada contra sin dimensionar, 2022–2024;
  - (b) C6 de BTC/ETH dimensionado dentro de P1, con la regla de inclusión de r51 y ventanas cortadas al 2024-12-31.
- **Compuerta:** (b) pasa la regla de inclusión **y** (a) mejora el Sharpe en ≥ 0,1.
- Si V1 falla, M1 se corre igual como información, pero no puede entrar a cartera.

## F3. Cartera
- Si M1 pasa, su versión de P1 tiene la mirada única a 2025.
- Si nada pasa, P1 sigue sin cambios y 2025 sigue sellado.
- Informe de cierre y handoff.

## Enmienda 2026-10-26: W1, C6 ampliado como manga de cartera
Se fijó después de ver V1, que pasa (32/48 positivas, canasta Sharpe 1,03 con t 2,05), y antes de medir cualquier cartera.
- **W1:** P1 más una manga nueva, «C6alts»: la canasta equiponderada de C6 congelado en las 48 alts, con las curvas de V1.
- Se evalúa con la regla de inclusión de r51, con las ventanas de P1 cortadas al 2024-12-31:
  - lente 2018-09+: C6alts existe desde 2020-10, así que se compara con la misma regla de días comunes que usa `r51_f6.compare`;
  - lente 2021+.
- Suma 1 a N.
- Si pasa, W1 tiene la mirada única a 2025 (puertas de F3), y se arma también la variante con M1 si M1 pasa.
