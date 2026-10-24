# Tanda I: participación secuencial y reparación de precios

La receta creativa produjo una sola operación. Su control de precios produjo 121 y perdió. Ninguna cumple el objetivo; una operación no permite estimar una ventaja ni refutar la familia económica.

## Diseño

Se registraron dos políticas antes de ejecutar: impulso de al menos un ATR seguido por recuperación entre 50% y menos de 100%. PHASE exige además poco volumen durante el impulso y recuperación a volumen normal; PRICE conserva el mismo patrón de precios sin esa condición. Las medianas usan 28 observaciones anteriores del mismo bloque UTC y están disponibles antes de S. Stop 2ATR previo, objetivo 2R y vencimiento 48h comunes. El objetivo supera la reparación inicial: se prueba persistencia después de esa recuperación.

BTC-USDT, Binance Perpetual Futures, [2020-10-15,2026-01-01), desarrollo reutilizado. Capital virtual 10.000 USDT; riesgo 2%/6%/3x; comisión 0,00045 por lado y funding histórico aplicado con marcas proxy declaradas; slippage modelado cero. Sin estrés, cambios de riesgo ni pruebas económicas nuevas de 2026.

## Resultados

### BtcResearchR12Participation1m
Dashboard: http://localhost:9200/#/backtest/17494d8a-eaf8-437e-8b7d-fac709a8d092

1 operaciones; neto -199.45 USDT; CAGR -0.3855%; PF 0.0000; Sharpe -0.4622; DD M1 y ejecuciones 2.4984%. Meses activos positivos 0/1; trimestres positivos 0/20; mediana calendario 0.0000%; neto sin dos mejores meses -199.45 USDT. NO_CUMPLE; muestra insuficiente para estimar una ventaja.

### BtcResearchR12RepairPrice1m
Dashboard: http://localhost:9200/#/backtest/a091d445-a502-4214-b153-182eb3d2af8d

121 operaciones; neto -1777.49 USDT; CAGR -3.6823%; PF 0.8689; Sharpe -0.3386; DD M1 y ejecuciones 39.8695%. Meses activos positivos 22/56; trimestres positivos 9/20; mediana calendario -0.3682%; neto sin dos mejores meses -3289.46 USDT. NO_CUMPLE; cumple sólo el mínimo preliminar de conteo, sin confianza estadística implícita.

## Auditoría y decisión

Check 29ddfe3edf6046fb8d02e16eff4cb3cb pasó antes de ejecutar, fuente SHA256 3928d2b3fd4ba9ffab43b89e134e982fb65e941cccaba9ba38e3c845bf9acfba. Revisión independiente sin errores materiales. Auditoría c330fae100fc4c0bbd271a07bee69348 sobre snapshots completos: bruto − fees + funding = suma de PnL = equity final − 10.000, tolerancia 1e−6 USDT. Las dos registraron 2.741.760 marcas M1, 63 intervalos mensuales, 62 meses completos y 20 trimestres, con fronteras y suma de contribuciones reconciliadas.

DD representa muestras M1 y ejecuciones, no todos los extremos intraminuto. Fronteras mensuales según convención R11: después del funding y antes de las decisiones; no agrupación estricta de eventos por fecha. Meses inactivos incluidos en mediana. No hubo errores económicos ni reemplazos.

Cerrar las dos corridas sin candidata y sin suavizar los límites de volumen después de observar su baja frecuencia. El control negativo no demuestra el efecto del filtro con sólo una operación del tratamiento. Conservar el resultado negativo y la insuficiencia de muestra como hechos distintos. Continuar con otra pregunta material dentro de la autorización autónoma vigente.

Fuentes, configuración y versiones: BTC_DISCOVERY_I_PROTOCOL_20261021.md y BTC_DISCOVERY_I_MANIFEST_20261021.json; contabilidad y telemetrías en archivos de esta tanda. Framework y configuración global intactos; sin live/paper/Pi.
