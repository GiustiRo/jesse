# BTC Discovery U — cierre

Se compararon dos libros BTC completos, con las tres ramas legacy conservadas. La única diferencia entre políticas fue qué volumen fija la frontera temporal del suplemento X805: BTC o ETH. Los precios, HLC3, pesos de volumen y estructura siempre fueron BTC. No se reabrieron P/J/Q ni el ranking R8. X805 histórico negativo sigue como antecedente; el contrato actual, validez compartida y guard físico de TP impiden llamarlo réplica histórica literal.

Contrato UTC [2020-10-15,2026-01-01), capital10000, riesgo2%/6%, aislado3x, fee.00045 por lado, funding BTC histórico aplicado/verificado con proxies declarados, slippage0. Reserva legacy.001 sólo en sizing, LOT.001, mismos valores en ambos. ATR Wilder real y lifecycle R16 conservados; ETH sólo dato auxiliar. Desarrollo ampliamente observado, no OOS.

|Política|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin dos mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[BTC_CLOCK](http://localhost:9200/#/backtest/3cd02a5c-4275-49fa-8a0c-fa7e9528d604)|536|3.859745|1.031535|44.502762|31/62|11/20|-0.098729|-2429.751038|
|[ETH_CLOCK](http://localhost:9200/#/backtest/81bf2f14-98ad-48f2-a6c2-2151c11512c8)|537|6.274067|1.052468|42.658798|33/62|10/20|0.146945|-963.970162|

BTC_CLOCK: bruto de precio 7214.607093135738; comisiones 5706.126775729788; funding 675.6934126488663; neto 2184.1737300548198; capital final 12184.173730054858. Años completos: {"2021":60.107586045176696,"2022":-13.056408133610697,"2023":21.158885223012458,"2024":-9.72762906976542,"2025":-14.330024120352036}. Peor/mejor ventana12m: -24.441176779606977/74.43843811006272%. Ledger por rama: {"LONG_RUNNER":{"fills":30,"closes":30,"net":7925.40886030179},"CORE_SHORT":{"fills":86,"closes":86,"net":3174.040000436401},"SUPPLEMENT":{"fills":420,"closes":420,"net":-8915.275130683383}}.

ETH_CLOCK: bruto de precio 8888.735350665738; comisiones 5892.35354673626; funding 739.4950400590908; neto 3735.8768439885503; capital final 13735.87684398853. Años completos: {"2021":54.34736488070793,"2022":-4.11018065601546,"2023":20.35491800104039,"2024":-10.151180083909884,"2025":-8.124309285975285}. Peor/mejor ventana12m: -24.823456692167913/68.15060462447178%. Ledger por rama: {"LONG_RUNNER":{"fills":30,"closes":30,"net":8195.35949730576},"CORE_SHORT":{"fills":86,"closes":86,"net":2567.8023146166006},"SUPPLEMENT":{"fills":421,"closes":421,"net":-7027.284967933809}}.

Ambas políticas tuvieron11423 ventanas M1 completas y válidas; los contadores comunes de observación son idénticos. Cortes iguales645 veces y distintos10778; setups distintos151. La distribución temporal externa sí modificó la representación, sin demostrar causalidad de ETH ni alpha aislado. Mismo corte actual no implica misma transición si los latches históricos difieren. Las diferencias del libro incluyen ocupación, selección y capital endógenos; los aportes por rama no son cuentas independientes.

Ambas usan FINAL tras liquidación terminal. R16 ledger: fills=closes=N, suma de ramas=neto, reconciliado a1e-6. total_open_trades1/open_pl son metadatos previos a esa liquidación, no exposición residual. R11:2741760 marcas M1,63intervalos/62meses completos/20Q,0ventanas inválidas. Historia4h241..11664. DD observa M1+fills, no todos extremos intraminuto. Corte mensual por fase postfunding/predecisión; mediana calendario incluye inactivos. 51ventanas móviles solapadas, no independientes.

Auditoría financiera b8962441b3fd486e89b177a8ecd8af98 succeeded sobre snapshots completos: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. No totales de páginas parciales. Check técnico2d9df9fc38ef470f983d39e1a3f17acc PASS172; corregido un formato de fuente antes de jobs y dos fallos del harness antes de PASS. Fuentes sin cambios entre los tres análisis; padres intactos. CODES/recibos preservan todo. Fakes no prueban semillas Wilder reales o paridad completa del broker.

Decisión: NO_CUMPLE en ambas, ninguna candidata. Mejor resultado relativo no alcanza CAGR/PF/DD/M/Q/concentración. Cerrar sin vecinos de50%/240/setup/horas/otros activos reloj/gestión/riesgo, sin quitar ramas/lados ni operar sólo desacuerdos. Sin estrés ni nuevas pruebas2026/live/paper/imports/Pi.

40económicas desde r9;209legacy V1–V6 aparte, sin afirmar censo global o independencia. V fue documentada antes del resultado U: dinámica conjunta BTC/ETH frente AR1 con admisibilidad común. Sólo implementación/checks autorizados por root por ahora, aún sin economía. Objetivo pendiente; continuar autónomamente.
