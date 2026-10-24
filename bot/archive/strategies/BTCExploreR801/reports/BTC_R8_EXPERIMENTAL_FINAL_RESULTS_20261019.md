# R8 — familia experimental BTC: cinco hipótesis, diez backtests

## Decisión de esta familia

Ninguna de las cinco hipótesis supera el neto nominal de N204 en ninguna cartera. Por esa condición necesaria ya quedan descartadas para promoción; no corresponde elegir la menos mala como nueva referencia. La selección consolidada, conciliación financiera completa y comparación de cohortes pertenecen a la auditoría central de R8. N204 sigue siendo el control, N503/P604 candidatas no promovidas.

## Diseño y límites

Se reemplazó sólo el setup del suplemento MARKET SHORT desde el esqueleto N204. Cada setup completo avanza su latch false→true incluso ocupado o pendiente; sin cola ni intento diferido. Geometría original d=max(Hs,Ht)+0.25ATR−Ct, gate1..3ATR; SL1R, TP2R y48h desde fill real. Largo y corto STOP originales, prioridades, HP, ledger y sizing intactos.

2020-10-15→2025-12-31 exclusiva; última fecha de precios2025-12-30. 2026 cerrado incluso inspección. Desarrollo reutilizado, sin prueba OOS. Capital compartido10000USDT, riesgo1% por trade/8% agregado, isolated5x, cap4.4, reserva.001 sólo sizing, fee.00045/lado, warm240, debugtrue, fastfalse, charttrue. BTC/PAXG/SPY4h+feeds1m. B=SPYsegunda oportunidad exacta/precioestructural; C=desde segunda/preciomercado. PAXG mantiene BE original dependiente del fee. Ningún cambio de datos, fee global, live/paper/Pi o funding.

## Hipótesis y resultados nominales

|Receta|Lectura|Neto B/C USDT|Sharpe B/C|Operaciones totales B/C|DDmotor B/C%|Eventos/ocupados/fills suplemento|
|---|---|---:|---:|---:|---:|---|
|X801|Pérdida del coste de la vela de mayor volumen|4947.13 / 5129.70|0.736565 / 0.748464|392 / 399|-12.6172 / -12.4988|294/79/210|
|X802|Ruptura bajista de la intersección de seis rangos|7971.10 / 8181.46|1.071839 / 1.076872|325 / 332|-13.0368 / -13.7806|171/37/127|
|X803|Recuperación fallida del mayor cuerpo vendedor|8013.23 / 8180.37|1.077109 / 1.079897|323 / 330|-11.7726 / -11.4880|185/49/133|
|X804|Transición de presión volumen × innovación entre cierres|5040.50 / 5213.66|0.749344 / 0.758312|365 / 372|-14.8298 / -11.7468|268/67/178|
|X805|Reversión intrabar usando una partición por volumen|3846.19 / 3967.02|0.539656 / 0.548995|590 / 597|-16.0514 / -15.7965|665/229/421|

X801 sustituye el VWAP de una cohorte por HLC3 de la vela de volumen máximo W12, empate más reciente; exige esa vela verde y cruce bajista del coste tras avance. X802 usa intersección real de los rangos previos W6 y pérdida por cierre de su límite inferior. X803 usa el cuerpo vendedor más negativo W12, empate más reciente, recuperación posterior limitada por su apertura y pérdida de su mitad. X804 mide cambio de signo entre dos bloques de seis de V×(C−Cprevio), con avance neto anterior y trigger bajista. X805 usa los240M1 de t y corta después del primer minuto que alcance50% del volumen, minuto completo al primer grupo, con VWAP HLC3 del segundo menor al primero y cierre por debajo del mínimo del primero. No son filtros añadidos a N204/N503 ni defensas de salida. Definiciones exactas y fórmulas en protocolo congelado central, fuentes y snapshots.

La fuerte degradación en las cinco familias indica que esos reemplazos no preservan la selección del suplemento de referencia bajo este contrato. Tener más señales no compensó su calidad y su interacción con el STOP original/capital compartido. No permite afirmar que todo método basado en volumen o aceptación sea inválido; sí descarta estas reglas concretas sin ajustar umbrales después de observar resultados.

## Observación M1 de X805

Ambas carteras:3024 consultas con datos válidos y3024 particiones. Missing_shape=0, missing_clock=0, corrupt=0, close_mismatch=0, zero_volume=0, empty_partition=0 (contadores ausentes se interpretan0). Se consulta sólo cuando Cs>Cprev12 y t roja; la cobertura observada no describe todos los minutos del histórico ni otros símbolos.

Primer grupo: fracción mínima0.5000020315817414, máxima0.6461235991665403, suma1530.0156635170379, count3024, media0.5059575606868512. Es un corte de minutos completos cercano a mitad de volumen; no mitad exacta ni fracción de OHLC compartida. valid=3024 significa cobertura/OHLC/volumen y partición válidos, NO3024 setups aceptados. Eventos665, ocupados229, fills421. VWAP HLC3×V y volumen OHLCV son proxies, no flujo taker ni fills intraminuto observados.

## QA, ejecución y trazabilidad

QA184PASS,0FAIL, job02f73c58f2c3422cbd48344fcc4cb74e; fuente/harness y review cruzada en esta carpeta. Primer harness falló porque ATR sintético2 volvía inelegible una geometría12.5; corregido sólo el stubATR5 y expectativa13.25. No se cambió ninguna fuente económica. Helpers y fixtures no demuestran el ciclo real del motor ni sustituyen la conciliación financiera central.

Revisión final: cinco fuentes exactas sin cambios desde creación, diez formularios exactos, treinta snapshots exactos; diez sesiones finished sin excepción, cero corridas propias activas. No nuevas corridas sin ticket. Dos simultáneas por par; máximo global coordinado4. Hubo interrupción MCP después del primer par; se detuvieron llamadas, luego se comprobó estado finished antes de continuar con X802. Nunca se relanzó X801 ni se usó acceso alternativo.

Los contadores terminate se imprimen antes del cierre forzado final del motor en algunos casos. X803 fills133/closes132 y X805421/420 no se interpretan como pérdidas de registro: la auditoría central debe reconstruir fills y terminal completo. Las métricas motor total_open_trades/open_pl pueden reflejar ese instante previo. No se ajustaron salidas para borrar esa diferencia observacional.

Diario de métricas y contadores: strategies/BTCExploreR801/reports/BTC_R8_EXPERIMENTAL_TERMINAL_JOURNAL_20261019.md.
Registro y formularios: strategies/BTCExploreR801/reports/BTC_R8_EXPERIMENTAL_DRAFT_REGISTRY_20261019.md.
Protocolo: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FROZEN_PROTOCOL_20261019.md.
Matriz/auditoría financiera final: responsabilidad root; este informe no presenta los overlays como mayor fee engine ni afirma validación independiente.

## Sesiones

### X801B

Dashboard: http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f

ID: f660ef63-d7c6-4792-9f21-06c1d7ebd85f

### X801C

Dashboard: http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660

ID: 4e432aac-71c2-4023-a978-6d8a618aa660

### X802B

Dashboard: http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3

ID: 261696a9-33ee-4504-a310-b8a44c63dcd3

### X802C

Dashboard: http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e

ID: 07a45656-81e2-4fd8-9851-3aa16a782c2e

### X803B

Dashboard: http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf

ID: 5208fe79-c420-4328-b5dd-1a67177f1ccf

### X803C

Dashboard: http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757

ID: a86de192-2f0d-4b34-a4ae-ce4f686d4757

### X804B

Dashboard: http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9

ID: ed50a692-6ce7-4014-baea-eb7b6b5acad9

### X804C

Dashboard: http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d

ID: 09421154-a313-480c-9ab0-6c28cdcf810d

### X805B

Dashboard: http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8

ID: 22b632fe-7fa2-450a-9f34-47c6e13efec8

### X805C

Dashboard: http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41

ID: 69c41479-2763-4150-ad60-68e1fd605b41


## Revisión de matriz central V/X tras auditorías

Las cinco X incumplen además calendario, Δ+10 y distribución; ninguna elegible. Revisión independiente de gates V/X190comprobacionesPASS, sin reconstruir MTMdesde cero. V801replicaN503yC40/63falla; V803/V805replicanN204, noavance. X805retiene30de31entradaslargasBTC y sus30salidas en ambascarteras: se preservó código/prioridad, no todas las ejecuciones; la ocupación y el capital compartido pueden desplazar operaciones. El resultado confirma que no se deben atribuir los netos sólo al suplemento. Revisión en BTC_R8_INDEPENDENT_VX_GATE_REVIEW_20261019.md.
