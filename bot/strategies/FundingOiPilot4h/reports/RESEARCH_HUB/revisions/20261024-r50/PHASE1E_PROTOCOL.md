# r50 F1e: carry de funding realista y cartera con carry

Fecha: 2026-10-25. El usuario aprobó seguir explorando («yo seguiría explorando, creo que vale la pena»), tras F1d. Este archivo se commitea **antes** de implementar y correr F1e.

**Qué es F1e:**
- **No re-evalúa K1 con otra puerta.** K1 sigue registrado como «no pasa» en F1d.
- F1e define una manga **nueva**, K1r: el mismo carry con restricciones operativas realistas. La juzga con compuertas propias de carry, porque la de concentración (top-5) se pensó para mangas direccionales.
- Se declara que esta elección está informada por el resultado de K1.

## 1. K1r: carry de funding con restricciones realistas (BTC y ETH)
- **Señal:** igual a K1. Se abre si la media de funding de 21 días anualizada supera 10% y se cierra si baja de 0.
- **Estructura:** largo spot y corto perpetuo por el mismo nocional.
  - El perpetuo opera a 2x aislado y su margen es 1/2 del nocional.
  - Nocional por pata: equity / 1,5 (≈ 0,667 × equity). El spot se paga entero y el margen del perpetuo sale del resto.
- **Riesgo de liquidación:**
  - Si el máximo diario del perpetuo supera en 40% el precio de entrada del corto, se fuerza un re-hedge: cerrar y reabrir las dos patas al cierre de ese día, con costes completos. Esto sigue la práctica de reponer margen antes de la liquidación (~+45–50% a 2x).
  - El PnL del spot compensa el del perpetuo, pero los costes se pagan.
- **Costes:**
  - spot: 0,10% por lado, sin descuento BNB;
  - perpetuo: 0,045% por lado;
  - slippage: 2 bp por pata y por lado.
- **Funding:** el real de Binance (datasets `0ab14bc2…` y `22bd891c…`).
- **PnL:** precio spot y perpetuo de los símbolos almacenados, más funding. Se reconcilia con el ledger (§3).

## 2. Compuertas de carry (K1r, ventana 2020-02 → 2025)

**Pasa si cumple todas:**
- Sharpe neto ≥ 1,0;
- meses positivos ≥ 70%;
- DD ≤ 10%;
- Sharpe > 0 en las dos mitades (2020–22 y 2023–25);
- estrés de compresión: con todo el funding multiplicado por 0,5, el Sharpe sigue ≥ 0,5;
- estrés de basis: la peor pérdida de 30 días es ≤ 5% del equity.

**Además se reporta:**
- tiempo en posición;
- cantidad de re-hedges;
- funding cobrado contra costes;
- retorno por año.

## 3. Auditoría contable de K1r
- La suma del funding cobrado tiene que coincidir con la suma directa de qty × mark × rate de los eventos del dataset en los días con posición, con diferencia < 0,1%.
- Los fees tienen que coincidir con nocional × tasa en cada apertura, cierre y re-hedge.

Si la auditoría falla, K1r no pasa.

## 4. Cartera P3 = R1 + C6 + K1r
- **Construcción congelada de F2:** riesgo inverso, vol 17%, k ≤ 8.
- **Techo propio para K1r:** el k aplicado a la manga K1r no puede superar 1,5, porque el apalancamiento real del carry está limitado por el margen del perpetuo. Si la vol objetivo pide más, el resto de la cartera no se re-escala.
- **Compuertas de cartera de F1d §3, en las dos ventanas:**
  - CAGR ≥ 30%;
  - DD ≤ 20%;
  - PF ≥ 1,2;
  - mediana mensual > 0;
  - positiva sin los 2 mejores meses;
  - DSR ≥ 0,95.

  La regularidad se reporta como seguimiento.
- **Ventanas:**
  - común: 2021-03 → 2025;
  - larga: la intersección de componentes, que empieza en 2020-02 por K1r.

## 5. Si P3 pasa
1. Se congelan código, mangas y construcción en un commit.
2. Se cargan los datos de confirmación prerregistrados en F1d §4.
3. **K1r** se confirma sobre los cuatro perpetuos nuevos (SOL, XRP, BNB y DOGE), con su spot y su funding real, desde que existen los datos. Las mismas puertas de §2, con Sharpe > 0 y sin derrumbes, en la mayoría de los cuatro.
4. **R1 y C6** se confirman como en F1d §4: activos nuevos y 2026.
5. 2026 no se usa para K1r, porque el usuario solo lo autorizó para motores R1/R2/R3.

## 6. N
Dos variantes nuevas: K1r y P3. **N declarado: 92.**
