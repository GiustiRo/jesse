# r50: congelamiento de P1 antes de la confirmación única

Fecha: 2026-10-25. El usuario decidió cerrar r50 validando lo que hay: «Validaría en los activos que ya seleccionamos, no descartaría más por ahora».

## Qué se congela
- **Código:** `bot/research_scripts/r50_harness.py`, `r50_engines.py`, `r50_f1b.py`, `r50_f1c.py`, `r50_f2.py`, `r50_f3.py`, `r50_f1d.py` y `r50_f1e.py`, tal como están en el commit que contiene este archivo. La confirmación los importa sin cambios.
- **Cartera P1:**
  - **R1:** ensamble Donchian r49 en 4h, en BTC, ETH, oro, SPX, WTI, gas y bono, con las configuraciones de `r50_f1b.R1_CFG`.
  - **C6:** rupturas R2 (Core4h) y R3 (retest K1001) en 4h, 50/50, en BTC y ETH.
  - **Construcción de F2:** riesgo inverso con vol expansiva, vol objetivo 17% con covarianza expansiva, k ≤ 8, rebalanceo mensual y sin freno de DD.
- **Métricas de referencia** (`f1d_screen.json`, P1):

| Ventana | CAGR | DD | Sharpe | DSR |
|---|---|---|---|---|
| 2021–25 | 24,6% | −14,0% | 1,44 | 0,76 |
| 2018-09+ | 36,9% | −14,3% | 1,60 | 0,99 |

## Confirmación única (PHASE1D_PROTOCOL.md §4, sin cambios)

**Datos.** Ninguno se cargó ni se miró antes de este commit. La descarga del DAX quedó como archivo, sin abrir.
- **Cripto** (Binance Perpetual Futures, con su funding real): SOL, XRP, BNB y DOGE, desde 2020-10. Se les aplica C6.
- **CFD** (Dukascopy, hasta 2025-12-31): DAX, Nikkei 225, FTSE 100, soja, azúcar y cacao. Se les aplica R1.
  - Índices con la configuración de SPX.
  - Agrícolas con la configuración del gas.
  - Si un instrumento no existe en la fuente, se excluye y se reporta.
- **2026** (desde 2026-01-01 hasta el último dato disponible antes del 2026-10-24) en los 7 activos del núcleo: P1 completa, porque P1 solo contiene mangas R1/R2/R3.
  - Para los CFD del núcleo se descarga 2026 de Dukascopy. El descargador y el arnés solo se habilitan para 2026 en esta confirmación, por autorización del usuario.

**Puertas:**
- Sharpe > 0 en la mayoría de las combinaciones manga × activo nuevo;
- ningún derrumbe (Sharpe < −0,5 o DD < −30%);
- canasta agregada de los activos nuevos con Sharpe > 0 y t ≥ 1,28;
- 2026: Sharpe de P1 ≥ −0,5 y DD no peor que el percentil 5 de un bootstrap por bloques de 21 días de los retornos diarios 2021–25 de P1, sobre la misma longitud.

**Sin re-ajustes.** Si falla, P1 se retira.

## Después
- F4: confirmación en Jesse de mangas de P1, con ≤ 10 corridas y máximo 2 simultáneas.
- Cierre de r50.
- **Paper trading:** requiere autorización explícita del usuario.
