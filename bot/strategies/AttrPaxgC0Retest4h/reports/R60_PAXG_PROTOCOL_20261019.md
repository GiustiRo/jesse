# R60 PAXG: cinco pares de estabilidad local, diez fulls

Fecha local: 19 de octubre de 2026. Estado: protocolo anterior a código y resultados R60. Leer junto con strategies/MultiAssetRetestBtcShort4h/reports/R60_SPY_PAXG_FROZEN_PROTOCOL_20261019.md y el handoff de atribución completo.

## Pregunta y presupuesto

¿Persiste la diferencia de política MARKET−retest al alterar una sola pieza cercana de su señal? No son diez ideas independientes ni una optimización para elegir el máximo.

Exactamente diez fulls nuevos PAXG, cinco pares completos en ordenP1Retest/Market, P2, P3, P4 yP5. En paralelo SPY tiene otros diez bajo root. No hay otro full de paridad, sensibilidad o control dentro de esta ronda. Sin MonteCarlo/RST ni seeds nuevas.

| Par | Cambio único | Retest nuevo | MARKET nuevo |
|---|---|---|---|
| P1 | donchian_len: 26→24 | R60PaxgN24Retest4h | R60PaxgN24Market4h |
| P2 | donchian_len: 26→28 | R60PaxgN28Retest4h | R60PaxgN28Market4h |
| P3 | adx_min: 26→24 | R60PaxgAdx24Retest4h | R60PaxgAdx24Market4h |
| P4 | adx_min: 26→28 | R60PaxgAdx28Retest4h | R60PaxgAdx28Market4h |
| P5 | ema_fast: 20→24 | R60PaxgFast24Retest4h | R60PaxgFast24Market4h |

P1–P4 son los cuatro contextos de la propuesta de estabilidad anterior. P5 añade confirmación rápida+20% para completar diez, fijada antes de resultados y aplicada simétricamente a ambas políticas; no deriva de un vecino ganador. No se combinan cambios ni se estudian más valores.

## Bases vigentes verificadas

Bases actuales leídas completas por MCP: AttrPaxgCqFreshRetest4h y AttrPaxgMMarketSignal4h. Se cotejaron con sus strategy_codes: igualdad exacta en ambos casos, sesiones finished. El antiguo store conversacional no se usa como prueba de fuente.

- [Cq 26/26/EMA20](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1):35trades,neto546,1105723537391USDT.
- [M 26/26/EMA20](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae):38trades,neto962,1262139358278USDT.

Son referencias existentes, no nuevas corridas. Diferencia central de netoM−Cq=416,0156415820887USDT. La atribución previa ya mostró concentración y cohortes2021–2023 débiles. No se declara valida M antes de estudiar vecinos. Cq yM no son la estrategia de fin de semana.

## Contrato congelado

Cuenta aislada10.000USDT; riesgo planificado1%; fee0,00045 por lado para TODAS las órdenes;5x isolated; cap nocional4,4x, sin piramidado. Reserva0,001 sólo en sizing, no slippage aplicado. Ruta PAXG-USDT4h, data PAXG1m, sin calendario adicional. Ventana2020-10-15 a2025-12-31 exclusiva, último día observado2025-12-30;2026 permanece cerrado. Warmup240, fast/debug false.

Proxies de precio existentes aceptados. Sin nuevos datos, funding, BTC, scripts de investigación, instalaciones, framework, config global, reinicios, live/paper oPi. Sólo Jesse MCP. Máximo dos backtests y un análisis propios; cuatro/dos globales coordinados.

Salidas originales en todas: stop inicial2ATR, BE2,25R, trailing4,2ATR, tightening5R×0,78 y8R×0,62. Conservados ledger, reservas, precisión, sizing, capital prudente, ratchet y cancelación de una barra. ATR/ADX/RSI mantienen períodos originales; alterar adx_min cambia umbral, no período ADX. EMAfast24 no cambia EMA80 ni shareATR. No guard fresco añadido a trailing.

Entrada Cq: filtros completos y LIMIT a frontera Donchian previa, quoteM1 propia exactaT−60s buscada por searchsorted, precio positivo/finito y paridad con cierre. EntradaM: mismos filtros y guard; valida primero distancia frente al boundary original, después repricing al cierre y sizing correspondiente. No se cambia semántica smart-order del motor.

## Fuente nueva y revisión antes de lanzar

Diez clases R60Paxg... autocontenidas copiadas de su base actual, cambiando sólo clase y el DEFAULT de un parámetro en hyperparameters. Comentario de trazabilidad local, sin optimizer ni overrides de sesión. Min/max originales no se usan como espacio de búsqueda.

Prueba mecánica previa: restituir clase, línea de default y quitar comentario de trazabilidad devuelve cada base byte por byte. Sólo hyperparameters puede diferir entre métodos. _plan, guard, gestión, sizing/ledger y hooks idénticos a su política base. Se leerán las diez fuentes completas y se presentará informe de diffs. Ningún run antes de revisión y autorización root.

## Evaluación de los cinco pares, sin escoger un vecino

Todas las filas se conservan, incluidas negativas o sin operaciones. Para cada par: netoM−Cq y diferencias descriptivas de PF, Sharpe, CAGR/DDmotor,fees, duración, exposición temporal, nocional-tiempo a precio de entrada, turnover y neto por nocional. Stress5/10bpsRT extra aplica2,5/5bps por cada lado sobre todos los fills, con tamaños/decisiones originales; no es nueva simulación.

Un cambio de signo de la diferenciaM−Cq respecto al centro señala fragilidad local de esa mejora, no una conclusión universal sobre MARKET o retest. Si todos los contextos conservan el signo, seguir considerando magnitud, DD/exposición, fricción, concentración y temporalidad. No convertir cinco puntos relacionados en test IID o validación OOS.

Excluir mejor trade y tres mejores PnL como diagnóstico de concentración, no veto universal a seguidores de tendencia. “Tres mejores” significa tres operaciones por PnL neto, incluso pérdidas si hay menos de tres ganadoras. Mantener cohortes por año de cierre etiquetadas, sin fingir retornos MTM. No seleccionar años, lados, contexto o plazo después de ver resultados.

Pareado por fill exacto y por created_at exacto de entrada ejecutada, si se utiliza, es intersección seleccionada; medir precio/retraso y PnL/nocional sin atribuir efecto causal puro. Ocupación y capital futuros cambian. No ajustar frecuencia, duración o exposición retrospectivamente para igualarlas.

Root hará MTM daycloseUTC y cotejo final de snapshots/formularios. No usar Portfolio00:01 o mes de cierre para regularidad. Cierres sintéticos de frontera concilian con wallet/open_pl, sin certificar liquidez nativa.

## Análisis y persistencia

Inputs por lote: referencias2+primeros3pares=8; referencias2+últimos2pares=6. Un análisis propio activo como máximo. Artefactos JSON por fila/par y resúmenes de tamaño menor de50KB; lectura íntegra verificada, sin parsear texto truncado. Fuente de análisis persistida en reporteMarkdown para reproducir sin scripts nuevos.

Entregables: diez URLs, tabla exacta con Sharpe y todas las métricas, cinco diferencias pareadas, costes/cohortes/concentración/exposición, registro de incidencias y conclusión del conjunto. Nada se integra o promueve automáticamente. Todo2020–2025 sigue seleccionado y2026 no se abre.
