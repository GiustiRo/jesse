# V3 — plan de auditoría de replay, contabilidad y fricción
Fecha: 2026-10-20. Estado: PLAN PREVIO A FASE C; no ejecuta sesiones ni análisis.
Fuentes leídas por MCP: RESEARCH_PROTOCOL_V3_20261020.md, ResearchV3Base4h, REGISTRY_V3.json, V3_AUDIT_ANALYSIS_SOURCE.json, jesse://funding y dos filas del ledger de la prueba técnica RANGE ya terminada. Esa página parcial se usó sólo para verificar nombres de campos, no para calcular estadísticas.
Root conserva el único registry global y la decisión económica. Este plan no cambia gates, reglas ni presupuesto, y no autoriza accesos a cuentas, Pi, live/paper o2026.

## 1. Objeto que se evalúa
Cada finalista tiene su propio replay [2024-01-01,2026-01-01),10000USDT al comienzo, capital transportado dentro de la sesión. Mantener símbolo/exchange/timeframe, datasets y fuentes congelados; isolated3x,notionalcapC y warmup240.
No reiniciar capital, margin disponible, cuota diaria o historia OI en cada semestre. No unir dos replays como si fuesen una cuenta y no sustituirlos por suma/rebase de backtests semestrales.
Los cuatro intervalos son:
- C1=[2024-01-01,2024-07-01).
- C2=[2024-07-01,2025-01-01).
- C3=[2025-01-01,2025-07-01).
- C4=[2025-07-01,2026-01-01).
Los gates de entrada usan a<T<b y gestión protectora/holding siempre activa. Conservar los semestres como intervalos separados, incluso si dos adyacentes son elegibles: fusionarlos habilitaría una entrada exactamente en un borde que el código actual bloquea.
FORCE_BOUNDARIES debe conservar todos los bordes semestrales internos. El final del replay se cierra mediante la terminación normal; no requiere una barra de2026.
Antes de iniciar cualquier replay guardar sus wrappers completos, hashes de dependencias, config exacta, calendario de exposición y fechas de decisiones train. La fase C sólo puede comenzar después de completar la confirmación nominal prevista.

## 2. Dos calendarios diferentes, ambos explícitos
Para finalista j y semestre f, E(j,f)=pasa gate train congelado de esa finalista. El train termina al comenzar ese semestre. Registrar cada E(j,f) antes de consultar su evaluación correspondiente; ningún rendimiento de evaluación crea o elimina un semestre activo.
El selector global G(f) elige entre finalistas elegibles mediante ranking congelado o queda plano. E(j,f) y G(f) son objetos diferentes.
El replay individual j opera en los semestres donde E(j,f)=verdadero, aunque G(f) haya elegido a la otra finalista. Se informa como política individual condicionada por train, no como replay del selector global.
El índice WF del selector reescala evaluaciones elegidas y es una convención aparte. Ni su PF con cantidades de sesiones reseteadas, ni la suma de saldos de finalistas, sustituyen el replay continuo.
Todos los escenarios de una finalista conservan SU calendario E(j,f) nominal. No recalcular elegibilidad con train estresado, no elegir retrospectivamente otro calendario ni volver a seleccionar finalista después de observar estrés. Cambios naturales de qty, ocupación, entradas posteriores o cantidad de trades por distintos fills/fees son resultados del replay; no exigir artificialmente la misma lista de trades.

## 3. Matriz prerregistrada que debe coincidir con config y fuente
| Caso | Fee por lado | Slippage adverso MARKET/STOP por lado | Otros cambios |
|---|---:|---:|---|
| Nominal | 0,00045 | 0bps | Calendario E(j,f) nominal |
| S1 | 0,0009 | 0bps | Mismo calendario |
| S2 | 0,00045 | 5bps | Mismo calendario |
| S3 | 0,0009 | 10bps | Mismo calendario |

Fee estresada interviene también en sizing; no se aplica solamente como una resta posterior.
LIMIT conserva el comportamiento del motor, sin el ajuste MARKET/STOP de esta implementación; sí paga la fee configurada. La ausencia de ajuste adverso a LIMIT no acredita profundidad ni aceptación de venue.
Vecinos por replay, sin elegir ganador:
- Escala0,9: stop1,8ATR. CHANNEL trailing2,7ATR; PULLBACK objetivo5,4ATR; RANGE objetivo SMA20 congelada sin escalar.
- Escala1,1: stop2,2ATR. CHANNEL trailing3,3ATR; PULLBACK objetivo6,6ATR; RANGE objetivo SMA20 congelada sin escalar.
Mantener ventanas, entradas, holding, OI y calendario nominal. Sizing utiliza la distancia vecina desde el comienzo; no ajustar trades nominales retrospectivamente.
Lag OI: una decisión4h adicional, sólo cuando la finalista exige OI. Si no usa OI es equivalente al nominal y se reutiliza, sin reasignar el slot a otra prueba.
Presupuesto de fase C: hasta2nominales+6fricción+4vecinos+2lag=14slots, dentro del máximo36V3; reutilizaciones y todos los intentos se registran. No iniciar pruebas adicionales por este documento.

## 4. Requisitos del snapshot y procedencia
Usar run_analysis con snapshots completos o rechazados, no calcular totales desde páginas parciales. Cada resultado debe conservar manifiesto, session_id/dashboard_url real, estado finished, fuentes/hashes y config completa.
Verificar:
- Una sola ruta BTC-USDT/Binance Perpetual Futures,4h, y ejecución efectiva1m por funding.
- Capital inicial10000,isolated3x, warmup240, fee/slip del caso, datasets exactos y modos historical.
- Funding9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; OI6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
- OI max_age_ms600000 y allow_missing_observations=True; no rellenar ausencias/ceros/stale.
- Start2024-01-01 y finish2026-01-01 exclusivos, sin eventos de ejecución o efectivo funding>=finish. Los metadatos del dataset pueden describir toda su cobertura; no se confunden con resultados económicos consultados.
- ACTIVE_WINDOWS/FORCE_BOUNDARIES coinciden con el calendario guardado y con el caso; no deriva de las fechas donde salió ganando.
- Cada orden, trade y cashflow tiene identidad coherente; duplicados no se eliminan arbitrariamente para hacer coincidir una suma.
- No posiciones de otra ruta, depósitos, retiros, interés de caja o FX implícitos. Un estado incompleto/fallido conserva esa etiqueta; no inventar terminal o curvas.
La captura de una subclase no basta: conservar toda la cadena base/helpers y atributos de escenario. Los timeouts de respuesta no prueban fallo del motor: consultar el mismoID antes de cualquier reintento y preservar raw.

## 5. Invariantes contables sobre órdenes y ledger completos
Para trade cerrado t, q=abs(cantidad real cerrada), s=+1long/−1short, precios VWAP reales:
G_t=s*q*(exit_price−entry_price).
FEE_t=sum(abs(filled_qty_o)*fill_price_o*fee_sesion) de sus órdenes EXECUTED.
F_t=sum(cashflow_l) del ledger con trade_id=t.id.
PNL_t=G_t−FEE_t+F_t.
Comparar con el PNL, fee y funding exportados del trade y con los campos métricos. No usar qty solicitada en lugar de filled_qty, ni multiplicar costos por leverage otra vez.
Sin piramidar/parciales previstos, comprobar que cantidades efectivamente entradas/salidas cubren q; una reducción efectiva capada se valida por fills reales, no por qty inicialmente solicitada. Conservar el tipo de salida y motivo explícito del log, incluidos calendar_boundary, maximum_hold, trailing_crossed_at_decision y fold_end.
Ausencia del campo funding no autoriza omitir costos: reconstruir F_t del ledger completo; un valor0 sólo se acepta cuando esa reconstrucción lo respalda, incluso si varios pagos se cancelan exactamente.
Por fila de ledger histórica:
cashflow=−qty_firmada_en_evento*mark_price*rate_decimal.
Rate0,0001 significa0,01%, sin división extra por100. El qty es el vigente en ese evento, no qty final reconstruida desde una operación distinta.
Los campos observados del ledger son settled_at,effective_at,qty,mark_price,mark_price_source,rate_decimal,cashflow,trade_id,exchange ysymbol. Sumar cashflow reconciliará funding.cashflow y las atribuciones por trade; revisar filas con trade_id ausente o no vinculado, no ignorarlas.
Saldo realizado final=10000+sum(PNL_t), plano después del cierre final y sin flujos externos. Los logs de cierre deben reconciliar balance previo más PNL; el riesgo usa C disponible antes de la entrada e incorpora fees presupuestadas, no funding/slippage futuros.
Tolerancia numérica existente1e−6USDT. Cualquier discrepancia superior se investiga como integridad antes de interpretar performance; no es permiso para redondear pérdidas o relajar gates.
Al concatenar evidencias no sumar trades de trains expansivos ni repetir el trainC1 ya reutilizado del screening.

## 6. Fills adversos y riesgo
Para cada MARKET/STOP ejecutada con bps>0:
buy_fill=reference_price*(1+bps/10000);
sell_fill=reference_price*(1−bps/10000).
Comprobar slippage.bps y reference_price conservados. La referencia ya puede incluir un gap: no imponer que sea igual al stop originalmente solicitado, ni aplicar dos veces el ajuste a una misma ejecución.
En nominal yS1 sin slip, no atribuirle ajustes inexistentes. En LIMIT no inventar ajuste MARKET/STOP. Recalcular fees sobre fill adverso.
Por entrada, auditar C,p,e,d,qty y presupuesto:
u=d+fee*(p+stop_pre), stop_pre=p−s*d;
qty=floor8(min(C/p,0,02*C/u)).
Capital previo debe incorporar toda fee y financiación anteriores del replay. Ninguna reasignación de10000 al cambiar semestre.
Stop se ancla a fill real con d de la decisión, objetivo según modo congelado; validar ratchets CHANNEL con sólo barras cerradas posteriores al fill y sin aflojar. Un umbral nuevo ya atravesado exige MARKET al precio actual, nunca rellenado retrospectivamente.
Riesgo real al stop puede exceder2% por funding, slippage y gaps. Reportar exceso; no corregir el trade ni excluirlo por eso. Ejemplo técnico ya observado: RANGE tuvo un stop con pérdida mayor que presupuesto por funding adicional, contemplado por el diseño.
Liquidaciones invalid_after_fill deben permanecer como entradas/cierres con costos, no desaparecer del conjunto.

## 7. Bordes: secuencia económica del motor, no sólo comparación de timestamps
La documentación jesse://funding fija: fills durante[T−1m,T) → funding efectivo en T → decisiones y órdenes MARKET de T.
Por tanto:
- Una entrada MARKET decidida en T no paga el evento efectivo T.
- Una salida MARKET decidida en T todavía paga ese evento si seguía abierta al comenzar su fase de funding.
- Una protección ejecutada en el minuto precedente puede dejar la posición plana antes del fundingT; auditar el tipo de orden y su orden temporal, no inferir cargo sólo con opened_at<=T<=closed_at.
- Estando plano no se inventa financiación. Un rate0 puede generar cashflow0 auténtico; no convertir falta de evento en rate0.
Jitter del proveedor hasta1000ms se asigna al borde de minuto para contabilidad conservando settled_at crudo. Usar effective_at para secuencia económica; la publicación para señales sigue disponible desde el minuto posterior, diferente de cobrar un evento ya liquidado.
En cada borde semestral interno guardar una tabla de evidencia: posición justo antes de funding, eventos de ese borde, cashflows, orden de cierre yprecio/fee, balance postcierre y primera entrada posterior. Paginación parcial de ledger no basta.
FORCE_BOUNDARIES cierra en la decisión exacta T y puede pagar fundingT antes de cerrar; una evaluación semestral finish-exclusive no procesa ese mismo evento final. Es una diferencia esperada entre el replay y sesiones semestrales reseteadas, no una razón para eliminar cargos ni exigir igualdad de sus PnL.
La convención mensual/semestral central asigna sellos diarios00:01 y punto de cierre00:00 al período que acaba mediante−61segundos, excepto saldo inicial. En replay, conservar los intervalos separados bloquea entradas nuevas en T exacto; la equity postcierre que se atribuye al semestre que termina incluye su cierre y el funding de borde descrito. Registrar los timestamps originales y esa convención: no llamarla una observación exacta intraminuto ni esconder que difiere del corte finish-exclusive.
Si faltan registros para demostrar un estado de borde, señalar evidencia insuficiente, no simular una posición con el último trade de una página parcial.
El intervalo de datos termina exclusivo2026-01-01: no leer velas con apertura>=finish ni aplicar funding efectivo>=finish. La estrategia puede etiquetar el cierre de la última vela de2025 con T=finish; eso no significa consultar datos2026. Distinguir ese reloj de cierre del timestamp de apertura/procesamiento y conciliar el cierre final separado.

## 8. Continuidad OI y caso lag
La base obtiene observaciones en todos los cierres del replay, aun con entradas deshabilitadas por calendario. Mantener ese historial a través de semestres y meses planos. No reiniciar la inicialización en cada semestre activo.
El replay nominal inicializa seis decisiones4h; el lag una adicional (siete). La primera decisión de la sesión puede serTstart+4h, por lo que no inventar una muestraTstart para completar una referencia24h inexistente.
En el lag se entrega en T lo observado causalmente en T−4h; la referencia es la observación igualmente retrasada en T−28h. Ambas se juzgan con su calidad y freshness en sus relojes originales. No extender stale a4h10m ni recalcular freshness contra T, lo que invalidaría artificialmente todo el lag.
Comprobar label+6m<=reloj_original yreloj_original<=available_at+10m; valores>0 y actual>referencia. Archivo retrospectivo sigue sin certificaciónPIT; el lag no prueba ausencia de revisiones del proveedor.
Las diferencias frente al WF reiniciado por semestre son esperadas por distinto capital e historiaOI. No imponer mismos trades, quantities o retornos.

## 9. Métricas y gates existentes, sin criterios nuevos
El PF se reconstruye con PNL netos positivos/negativos de trades únicos del replay completo, no promediando PF semestrales. Sin pérdidas y con beneficio: PF infinito conceptual; sin trades/beneficio, indefinido, no cero inventado.
DDmotor es el gate congelado. Conservar DDmuestreado de Portfolio y terminal como evidencia complementaria, sin sustituir la métrica que favorezca el resultado. Una discrepancia material de capturas pre/postcierre se documenta y se explica antes de afirmar la integridad de la medida.
Conservar curva original, saldo terminal verdadero, curve_terminal_delta,24meses completos y cuatro retornos semestrales de la misma cuenta continua. No usar suma dePnL de trades cerrados dentro de un semestre para medir equity del semestre: existen mark-to-market y costos en sus bordes.
Saldo terminal real se asigna al último mes del intervalo exclusivo; no crear un mes extra2026 ni dejar fuera fees de cierre. Si faltan puntos/baselines, no rellenarlos para aprobar.
Días exactos UTC de [2024-01-01,2026-01-01)=731. CAGR=(saldo_final/10000)^(365/731)−1, usando todo el período incluso semestres planos. No dividir por tiempo expuesto, omitir meses negativos o anualizar el mejor semestre.
La fase C exige para considerar candidata histórica: neto>0,PF>=1,2,DDmotor<=25%,>=100trades,>=3/4semestres positivos por equity del replay yCAGRnominal>=15%. Un CAGR inferior con el resto cumplido es progreso parcial según protocolo, no objetivo logrado.
S1 yS3 deben quedar neto>0 yDD<=25; reportar PF,N,CAGR yresto de métricas también enS2. No añadir aS2 un gate distinto del protocolo.
Ambos vecinos ylagOI aplicable deben conservar neto>0 yDD<=25; si no,FRÁGIL. No seleccionar el vecino o retraso que salió mejor ni cambiar exposición después. SinOI, nominal equivalente cubre ese escenario sin otro run.
Meta20–30%anual orientativa, no cuota mensual ni promesa. Nada de este plan convierte una candidata histórica en autorización de operar.

## 10. Dos sensibilidades contables de funding, autorizadas antes de fase C
Root resolvió explícitamente que se reportarán ambas, con k=0,5 y1,5, cantidades/fills y decisiones originales fijos:
A. Sólo proxy: G−fees+F_no_proxy+k*F_proxy. Clasificar filas por mark_price_source; el proxy conocido es markPriceKlines.1h_open_proxy. Enumerar fuentes reales presentes. No llamar exactas a filas desconocidas/ausentes: conservarlas identificadas y sin transformación, y advertir esa falta de clasificación.
B. Financiación global: G−fees+k*F_total.
A estudia únicamente sensibilidad a los pagos asociados a marcas proxy; B es sensibilidad global a financiación, incluidos pagos/ingresos con marcas de liquidación. Mostrar los cuatro resultados, sus componentes y si cambia signo; no elegir el más favorable ni omitir el que empeora.
Escalar cashflow equivale a escalar la marca sólo con qty yrate originales fijos. No se recalculan capital en entradas posteriores, qty, señales, margin calls, stops ni compounding. Por eso son atribuciones contables aproximadas, no replay de fricción ni simulación de una nueva cuenta.
No aplicar estas diferencias como doble funding encima de un neto que ya lo incluye: usar G−fees+F_sens o, equivalentemente, neto+(F_sens−F_original).
No se crea un gate nuevo, un CAGR promocional o una nueva candidata a partir de estas sensibilidades. La inversión de signo es un riesgo material que se reporta con claridad; no se reescribe el protocolo para rescatar o descartar selectivamente tras observarla.

## 11. Riesgos materiales y entregables
- Cortes de funding/market-close en el borde pueden diferir de sesiones finish-exclusive y deben verse enledger.
- Calendario individual distinto del selector global puede producir un replay positivo sin representar la selecciónglobal.
- Fee/slippage modifican capital,sizing yocupación: un haircut no sustituye S1/S2/S3.
- OI histórico revisable y marksproxy no pasan a ser exactos por conciliar internamente.
- Campo open_trades/open_pl puede ser precierre forzado; el snapshot completo ysaldo postcierre mandan para contabilidad, sin inferir posición residual activa.
- El modelo no acredita profundidad/latencia, precisión de órdenes aceptada por venue o liquidación aislada real. Si un debitamiento histórico agota margen yel motor falla, informar fallo explícito, no fingir un costo omitido.

Guardar por escenario: manifiesto completo, config/calendario/hashes, fuente auditora, métricas,24meses/foursemesters,ledger agregado ytabla de bordes, motivos/bloqueos yconciliación de cantidades/fees/funding/saldo. Root registra selección yconclusión con todas las pruebas, incluidas fallidas.
Este plan es sólolectura/especificación. No se ejecutaron nuevos run_analysis,backtests, cambios productivos ni consultas económicas2024–2025 desde este sector al redactarlo.
