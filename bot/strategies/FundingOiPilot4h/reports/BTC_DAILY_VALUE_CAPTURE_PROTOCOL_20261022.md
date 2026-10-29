# BTC: captura de retorno al valor diario
Fecha local: 22 de octubre de 2026. Protocolo anterior a fuentes nuevas, drafts, jobs y motores. Root autorizó preparar esta comparación; todavía debe revisar la base de ejecución aislada. El padre R32 y el observador R11 permanecen inmutables.

## Pregunta y antecedentes
¿Conviene capturar una recuperación intradía en un valor conocido antes de comenzar la recuperación, o exigir un beneficio fijo de 2R? Las entradas, stop, riesgo y vencimiento son iguales. Cambia únicamente el destino de la toma de beneficio. No es otro filtro de ruptura R32 ni una selección long-only basada en contribuciones observadas.

Se elige el reinicio diario UTC, no semanal. Las horas de entrada y el cierre a medianoche pertenecen a esta definición del ancla; no representan una sesión económica privilegiada descubierta para cripto. El VWAP de HLC3 y volumen M1 es una aproximación, no precio exacto de ticks, flujo observado, coste de holders ni valor fundamental.

Antecedentes leídos completos:
- Hub r33/HANDOFF y cierre R32: conservar cerrados aceptación, fallo persistente y contención; ningún vecino 120/inside/permanencia.
- ResearchV5VwapPV1h, vwap_features.py y V5_VWAP_SCREEN_REPORT.md: rolling 24 barras de 1h, escala max(sigma, ATR), reingreso K2 y salida MARKET al centro móvil/24h. PV perdió 33.8694%, PF 0.8831 y DD 40.95%, con 546 trades. No se modifica ese screening. Aquí cambia la referencia a M1 desde medianoche, excluyendo la barra de recuperación, se congela el objetivo y se compara su captura con 2R.
- BTCExploreR801 y R8 FINAL: corto por pérdida de HLC3 de una única vela de máximo volumen entre 12, TP 2R/48h en libro combinado. No VWAP diario ni captura del centro.
- OrchManageFastMrBtc4h y MultiAssetSleeves4h: antecedentes de reversión con RSI/medias y salidas SMA5 dinámica o EMA20 fija. La familia es conocida; no se redescubre la reversión.
No se encontró un control equivalente para reutilizar. Se justifican dos motores del par, sin afirmar búsqueda exhaustiva global ni culpar retrospectivamente a la salida antigua.

## Ancla y reloj causales
Entradas sólo a T = 08, 12, 16 o 20 UTC. D es la medianoche UTC de T; S = T - 4h. Se exige S >= D + 4h. A las 04 UTC falta deliberadamente el período mínimo: no es un error de datos ni consume un intento.

La base recibe 64 barras 4h cerradas, contiguas y con OHLC válido. C_T es el cierre de la barra B=[S,T), equivalente a self.price. C_S es el cierre de la barra anterior, terminada en S. ATR_T es ATR14 simple de 15 barras terminadas en T; ATR_S usa 15 terminadas en S, excluyendo B. Se usa media de 14 True Ranges, no Wilder.

El valor G se calcula exclusivamente con M1 de [D,S): 240, 480, 720 o 960 minutos exactos, cerrados y consecutivos, sin duplicados, gaps o futuro. Se obtiene por searchsorted y vista acotada. OHLC finitos y positivos, geometría válida; volumen finito >= 0 y al menos una observación positiva. Si todo el volumen es cero, no existe ancla válida.
p_i = H_i/3 + L_i/3 + C_i/3.
Los pesos se escalan por max(V) y se normalizan para evitar overflow; G = suma(w_i*p_i), finito y positivo.

Comprobar cada agregado OHLC 4h de la referencia contra su fila correspondiente, por timestamps; última C_M1 = C_S. Tolerancias rtol=1e-10/atol=1e-8 sólo para representación. El volumen 4h no sustituye al volumen M1. Ninguna M1 de B entra en G, aunque ya esté disponible al decidir. Por tanto G estaba determinado al comenzar la recuperación.

## Patrón e intento común
Con datos válidos:
- Long: C_S <= G - 2*ATR_S y C_S < C_T < G.
- Short: C_S >= G + 2*ATR_S y G < C_T < C_S.
La igualdad del umbral exterior admite; igualdad en recuperación o centro no admite. No se exige reingreso en una banda en C_T, sigma, RSI o filtro adicional de volumen.

Estado de mercado: D, consumed y last_T. Se actualiza incluso ocupado, con órdenes pendientes o después de una salida en T. No reprocesar T <= last_T. Al nuevo D, reiniciar consumed=False.
El PRIMER PATRÓN BRUTO exante de D consume inmediatamente el día, ANTES de los guards de objetivos, sizing, ocupación o same-exit. También consume si cualquiera de esos guards falla. No esperar otra hora, cambiar de lado, encolar o reintentar ese día. Sin patrón puede evaluarse el siguiente horario.
Datos inválidos en una decisión elegible bloquean todo D para ambas políticas: no se puede reconstruir el primer intento. Recuperación sólo al día siguiente. El assert de paridad de infraestructura es un bloqueo técnico, no una abstención selectiva silenciosa.
Los logs raw y target_guard deben ser comparables entre políticas, independientemente de la cuenta; selected/plans/fills pueden diferir.

## Objetivos y admisibilidad compartida
E = self.price exacto; d = 2*ATR_T. Los dos objetivos propuestos son G congelado y F = E + direction*2*d.
AMBAS políticas exigen que AMBOS objetivos sean finitos, positivos y estén estrictamente del lado favorable. También:
1. No satisfacer la condición nativa is_price_near con threshold 0.00015 (0.015%); preservar su comparación exacta en implementación.
2. direction*(target-E) > fee*(E+target), con fee base 0.00045 por lado.

Es admisibilidad compartida por costos base y semántica de órdenes, no estrés ni optimización. No promete beneficio neto realizado: funding, gaps y ejecución siguen importando. La comprobación de fees no sustituye la comprobación explícita de cercanía. No usar un umbral arbitrario o tarifa maker. El intento ya fue consumido aunque los objetivos sean inválidos o demasiado cercanos.

Sizing: legacy_plan(.5*wallet, .5*available_margin, 3, fee). Reserva 0.001 sólo para sizing; lote 0.001 con floor. Riesgo objetivo 1% del capital BTC total de 10.000 cuando flat; resto de cuota ociosa, sin redistribución. No usar R10 entry_plan, que tiene otra precisión y carece de esa reserva.
Stop desde fill real: E_fill - direction*d. Sin BE, trailing o parciales.
- VALUE: TP LIMIT al G congelado.
- R2: TP a E_fill + direction*2*d.
G no se actualiza con precios o volumen posteriores.

Después del fill, verificar ambos objetivos respecto de E_fill, costo/cercanía y protección. F se calcula desde E_fill; G no cambia. Si falla una condición, no colocar un target atravesado ni sustituir VALUE por R2: conservar el stop inicial y solicitar cierre MARKET inmediato, registrar after_fill_invalid e incluir trade/costos en el ledger. Esto bloquea candidatura por geometría técnica; no se omite el safety trade ni se repite automáticamente el motor.

## Vencimiento y observación
Deadline común = D + DAY. Evaluar el cierre por deadline en CADA M1, sin veto por horario de entrada, indicadores, volumen o ancla inválida. SL/TP nativos operan 24/7. A medianoche no hay nueva entrada; se liquida la posición anterior. FINISH exclusivo conserva cierre y fee terminal, sin nuevo funding o precios de 2026. No atribuir causa de salida sólo por el tipo MARKET.

Base nueva aislada propuesta: BtcResearchR34DailyValueBase1m, con hojas BtcResearchR34ValueTarget1m y BtcResearchR34TwoRTarget1m. Sólo difieren modo de TP/label. Se reutiliza R11 una vez por fase pre/open/close/FINAL; se requieren hooks propios para plan/target/deadline sin editar R32. Root debe aprobar esa normativa antes de crear fuentes. No describir TP dinámico mediante campos heredados tp_r=None que oculten su objetivo real.

Schema para auditoría, cada línea <1800 caracteres y sin logs continuos M1:
- R34_PLAN: time,label,direction,entry,qty,distance,risk_budget,planned_loss,meta con value/deadline/policy/targetlevel.
- R34_OPEN: time,label,signal_at,opened_at,direction,entry,qty,distance,risk_budget,stop,target_distance,deadline,policy.
- R34_CLOSE: time,label,net,reason acreditada.
- R34_SUMMARY: stage,label,opens,closes,long_opens,short_opens,net,events,plans,occupied,rejected_geometry,risk_total=.01,capital_denominator="total BTC wallet",redistribution=false,target_mode="VALUE"/"R2",deadline_mode="next UTC midnight".
Ledger actualizado ANTES de cualquier FINAL. PRETERMINAL/FINAL son snapshots, no sumandos.

## Presupuesto y decisión
Contrato: BTC-USDT Binance Perpetual Futures; UTC [2020-10-15,2026-01-01); 10.000 totales por alternativa y cuota 1%; 3x aislado/6% global; fee 0.00045 taker descontado; funding histórico ON, dataset 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 y proxies declarados; slippage modelado 0. Warmup 240 del 4h, fast OFF y logs de auditoría. Sin datos/importaciones/precheck de velas, 2026 nuevo, USDC, estrés, grids de riesgo, cartera, ML, live/paper/Pi, instalaciones o configuración global.

Máximo DOS IDs económicos: VALUE y R2. Sin réplica adicional, preflight económico o reemplazo automático. Antes: aprobación root de docs/base, fuente/readback/hash, check supplied-source y manifiesto. Hoy no se crean fuentes ni jobs. La semántica MARKET y objetivos nativos se verificará DESPUÉS de esos mismos motores, no por stubs.

Comparar políticas completas: ocupación, reentradas y capitalización pueden cambiar al cambiar TP. No sumar cuentas ni PnL de trades evitados. Informar bruto/fees/funding/net/final, CAGR sobre 10k, PF neto USDT, DD M1+fills, N, lados/exposición, 62 meses calendario incluidos ceros y activos, 20 trimestres, mediana, años y neto sin dos mejores meses. Normalizaciones R son descriptivas.
Auditar órdenes/objetivos/plazos/terminal, pagos completos y gross-fees+funding=PNL=final-10000 a <1e-6 USDT. No imputar funding=0 por ausencia ni confundir contadores preterminales con posiciones residuales.

Gates r9 sin relajar: CAGR>=30%, PF>=1.2, DD<=25% (20% objetivo), meses activos positivos>=65% (70% aspiración), trimestres positivos>=80%, mediana mensual calendario>0, neto sin dos mejores meses>0 y N>=100 como suficiencia operativa preliminar, no potencia estadística. No escalar cuota a 2% o cambiar denominador para aprobar.
Preferencia comparativa VALUE sólo si CAGR mayor, DD no mayor y meses calendario positivos no menores; reportar otros intercambios, sin dominancia global automática. Candidatura exige además todas las puertas y auditoría. Si R2 pasa solo, no afirmar atracción al valor. Si ambos fallan, cerrar sin vecinos de hora/ancla/2ATR/guard/TP/plazo/lado. Desarrollo observado/adaptativo, no OOS ni arquitectura conjunta acreditada.
