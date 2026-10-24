# Primer ciclo autónomo BTC: cierre de las tandas A y B
Fecha: 2026-10-21. Estado: cerrado sin candidata.

## Qué se ejecutó
Se contrastó la evidencia BTC existente y se ejecutaron dos hipótesis nuevas más una iteración de gestión. Tres backtests económicos terminados, sin errores ni reemplazos técnicos. Se mantuvo el perfil 2% por operación / 6% agregado / 3x aislado, con 10.000 USDT virtuales por cuenta, comisión 0,00045 por lado y funding activado. No se hicieron pruebas de estrés, variantes de riesgo o nuevas corridas de 2026.

Ventana común: [2020-10-15, 2026-01-01) UTC. Es desarrollo histórico ya observado; 2020 es parcial y 2021–2025 son años completos. Neto significa después de comisiones y funding modelados, con slippage cero modelado. No significa neto de todos los costos reales.

| Receta | CAGR | DD diario reportado | PF neto | Trades | Retorno total | Decisión |
|---|---:|---:|---:|---:|---:|---|
| [A: persistencia de signos](http://localhost:9200/#/backtest/438b717c-7b5e-4589-a84a-687fa63f8645) | 11,59% | −14,52% | 1,473 | 193 | +77,20% | No cumple CAGR ≥30%. |
| [A: fallo posterior al funding](http://localhost:9200/#/backtest/b3fa7fff-0b6b-44de-ac23-230c118a94b0) | −7,57% | −35,24% | 0,896 | 454 | −33,66% | No cumple retorno, PF ni DD. |
| [B: signos con salida por estado](http://localhost:9200/#/backtest/62c90517-9034-4b34-91af-f77457895157) | 23,39% | −33,10% | 1,576 | 102 | +199,28% | No cumple CAGR ni DD. |

No confundir retorno total de unos cinco años con rentabilidad anual. Ninguna receta alcanza los objetivos decisivos; ninguna se promueve.

## Preguntas y diferencias frente a los antecedentes
La matriz inicial confirmó que V1–V6 sí contiene BTC individual con funding. CHANNEL_P quedó en 17,54% de CAGR en su replay y CROSS_P sólo tiene screening, sin confirmación posterior. Ninguna acredita el objetivo actual. No era necesario repetir sus backtests ni atribuir a BTC el CAGR de K1001/N204 de cartera.

La tanda A se registró antes de sus resultados:
- **Persistencia de signos:** contar cambios positivos o negativos en las últimas 6 y 24 barras de cuatro horas, con una mayoría de dos tercios. Entrar sólo al aparecer el estado. Difiere del cociente de eficiencia de V6 y del cruce de medias de V5: cuenta signos, no magnitudes ni posición respecto de una media.
- **Fallo posterior al funding:** esperar una barra completa después de un pago ya publicado y operar cuando se invalida el movimiento previo del lado pagador. Fue la parte creativa: una de las dos hipótesis iniciales. No usa el próximo pago ni acredita liquidaciones reales; la hora UTC y el evento siguen confundidos.

Ambas tenían stop fijo de 2 ATR, objetivo de 2R y salida máxima a las 48 horas. Los eventos bloqueados por una posición se consumían, sin cola.

Después de observar A se registró una sola iteración B: misma entrada, sizing y stop, pero sin objetivo de beneficio, con salida por estado contrario y límite de 30 días. Es una transferencia explícita de gestión conocida en V5 a otra señal. Cambia una política completa; no identifica por separado el efecto del TP, del plazo o de la salida. El control A se reutilizó.

La revisión de fuentes y los chequeos sintéticos precedieron a la economía. Un segundo agente contrastó las reglas y el reloj de funding. No se quitaron shorts según su resultado ni se probaron vecinos para rescatar una curva.

## Qué aprendimos
La señal de signos produjo utilidad positiva bajo costos base, pero insuficiente para el objetivo. Dejar correr posiciones elevó el retorno y también el drawdown. No demuestra que la gestión inicial fuera la causa del fallo.

La receta posterior al funding perdió pese a recibir funding neto favorable. No se justifica invertir su dirección después de ver el resultado.

Funding neto: −574,54 USDT en A_SIGN, +894,62 en A_EVENT y −4.281,41 en B. Mayor duración cambia exposición y pagos; no es un estrés de comisiones. La concentración de B también aumentó: sus dos mejores meses aproximados aportan 16.695,50 USDT frente a 19.927,68 de neto total. Seguir positivo sin ellos no basta para aprobar regularidad.

## Verificación y límites de medición
La auditoría completa recibió 193, 454 y 102 trades, y 1.905 puntos de equity por cuenta. Reconcilió bruto de precios − comisiones + funding = suma de PnL = saldo final − 10.000, y recalculó PF y CAGR. Error máximo absoluto: 5,10×10⁻¹¹ USDT, inferior a la tolerancia contable de 10⁻⁶. No se calcularon totales desde páginas parciales.

Se verificó funding.applied=true, el dataset congelado y el replay completo M1. El snapshot contiene 6.576 eventos y 4.198 marcas proxy en toda su cobertura; las posiciones de las tres recetas usaron respectivamente 513, 1.207 y 1.772 pagos con marca aproximada. No son precios exactos de ejecución de una cuenta real.

En B, el summary conserva total_open_trades=1 y open_pl preterminal. Los logs finales muestran la orden MARKET reduce-only ejecutada, cierre del trade, cancelación del stop y saldo final 29.927,68. Los 102 trades cerrados reconcilian con ese saldo; el contador previo no se presenta como posición real abierta.

Dos límites importantes:
- El max_drawdown del framework se calcula con daily_balance. Los DD de la tabla son muestreados diariamente y pueden omitir extremos intradiarios. Se aclara la frase imprecisa del protocolo A que sugería otra resolución.
- La curva diaria usa cortes a las 00:01 UTC, más valores inicial y terminal. Los CSV mensuales y anuales derivados se etiquetan como aproximados. No acreditan cortes exactos a las 00:00 ni las puertas M65/Q80, mediana y concentración. Como las tres recetas ya fallan retorno o DD obligatorio, el rechazo no depende de inventar esas mediciones. Una futura candidata requerirá medición suficiente antes de promoverse.

Respecto de V1–V6, la política común de esta tanda no impone su cap nocional 1x ni cuota diaria: aplica el riesgo objetivo hasta donde permite el margen 3x reservado. Es una diferencia explícita de exposición, no evidencia de mejor señal comparando programas. No hubo rejilla de caps o riesgos.

## Cierre y continuidad
Las tandas A (dos corridas) y B (una) agotaron su presupuesto y se cierran sin candidata. No seguir con pequeñas variantes de ventanas, TP o plazo, ni eliminar shorts por su PnL observado. La siguiente tanda deberá justificar otra pregunta material, contrastarla con estos resultados y los antecedentes, y registrar su presupuesto antes de ejecutar. El permiso autónomo del usuario sigue vigente.

Los 209 backtests económicos históricos V1–V6 se conservan aparte de estos tres; no son un censo de todo el proyecto ni muestras independientes. La participación creativa continuará con hipótesis comprobables. PAXG/SPY y cartera siguen diferidos; estrés sólo después de candidatas y acuerdo conjunto. No se operó paper/live, no se accedió a la Pi ni se alteró configuración global.

## Trazabilidad
En strategies/FundingOiPilot4h/reports/:
- BTC_INDIVIDUAL_EVIDENCE_MATRIX_20261021.md.
- BTC_DISCOVERY_A_PROTOCOL_20261021.md y BTC_DISCOVERY_A_MANIFEST_20261021.json.
- BTC_DISCOVERY_A_RESULTS_20261021.md/.json.
- BTC_DISCOVERY_B_PROTOCOL_20261021.md y BTC_DISCOVERY_B_MANIFEST_20261021.json.
- BTC_DISCOVERY_AB_RESULTS_20261021.json y CSV *_monthly_approx.

Auditoría final: job 0fef85256f9e453abcd5e35c2c3ee42c, con snapshots completos. Los resultados y CSV se recuperaron y guardaron mediante MCP. Los manifiestos conservan código, hashes y configuración anterior a cada ejecución.
