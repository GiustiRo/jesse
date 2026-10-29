# Continuidad r30

Diagnóstico K1001, dos cuotas y contraste MARKET cerrados, auditados, sin candidata. MARKET mejora CAGR/DD relativos pero falla retorno absoluto, regularidad y suficiencia.51IDs económicos completados desde r9.

Continuar desde preguntas sobre fortalezas/debilidades de K1001 y contrastar antecedentes antes de otro protocolo. Bloque creativo distribucional HOLD por solapamiento con V5. No vecinos MARKET/TTL/BE/trailing ni aumento de cuota.

La instrucción humana más reciente confirma: entender K1001, plantear y responder preguntas, luego investigar/probar a partir de esas respuestas. Diagnóstico realizado antes de cuotas y MARKET; no reinterpretar como permiso para pruebas sin pregunta.

# K1001 LONG MARKET: crítica independiente del cierre

Fecha: 2026-10-21. Dictamen: CONFORME, sin bloqueo material para cerrar NO_CUMPLE y sin nuevos vecinos. No hay candidata ni objetivo cumplido.

## Evidencia y alcance de esta revisión

Leí completo K1001_LONG_MARKET_FINAL_20261021.md (66 líneas, has_more=false), los summaries nativos actuales de [MARKET](http://localhost:9200/#/backtest/1e016570-d981-47d1-b6d8-38fcde982084) y [control reutilizado](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c), y una página terminal nativa de65 logs que contiene R11_SUMMARY, R16_LEGACY_STATS y las16 filas MARKET completas. Releí la fuente MARKET completa y confirmé SHA256 f3aeb9be8082cfb7f5cbd4a310da1b741a7bec9d675e25d657131754f5e8b32b, idéntica a la implementación entregada; contrasté semántica terminal con el R11 congelado ya leído.

No reaudité las36 trazas,36 órdenes,717 pagos, todos los meses, ni todos los cruces entre políticas; su verificación por fila pertenece a los recibos del auditor de root. Esta revisión no convierte esos recibos en una segunda auditoría exhaustiva.

## Resultado y precisión del dictamen

El summary nativo confirma36 trades long,15 ganadores/21 perdedores, neto5108.599226632841 y capital15108.59922663284 sobre10000, CAGR8.232472711789862%, funding aplicado−513.5101221360909 con717 eventos y441 proxies. El control nativo confirma31 trades, neto4030.903490447631, CAGR6.707897732817347%. Son cuentas alternativas completas, misma cuota1%; no capital5000, mezcla conjunta ni escalado a2%.

Los logs terminales R11 confirman33 meses activos/15 positivos,62 meses completos,9/20 trimestres positivos, mediana calendario0, neto sin dos mejores meses2342.1258804146473 y DD M1+fills6.232971890977668%. No debe sustituirse ese DD por4.7548% diario nativo. SOURCE acredita36 fills/36 closes/36 trazas completas, sin shorts, con errors vacío y open_trace falso; summary nativo acredita flat. El stage observado es PRETERMINAL, económicamente final al estar ya cerrado y coincidir con saldo nativo; no se debe inventar un callback FINAL adicional ni sumarlo al snapshot.

La mejora de CAGR de1.5246 puntos y DD de2.2400 puntos es descriptiva de esta historia reutilizada. PF monetario baja de3.5520 a3.3049, y meses activos positivos de46.43% a45.45%; aumenta el número absoluto de meses ganadores, pero no su proporción activa. No dominancia ni prueba de mejora futura. N36 insuficiente es una limitación adicional; los fallos de CAGR, M, Q y mediana ya bastan para NO_CUMPLE. No rescatar bajando las puertas debido a cuota1%.

## Límites de interpretación correctamente preservados

- El contraste cambia entrada de cuenta, con ocupación, stop absoluto, tamaños y capitalización posteriores; no aísla el beneficio de las14 cancelaciones ni permite explicar su PnL contrafactual.31→36 no significa14 fills recuperados. Los conteos24 señales comunes/12 nuevas/7 ausentes se aceptan del join auditado, no se reconstituyeron aquí.
- El control nominal LIMIT incluye4 entradas MARKET por conversión near nativa. El cierre lo declara correctamente; afirmar31 LIMIT estrictas sería falso. La fuente nueva pide self.price exacto, pero la prueba de36 MARKET reales reside en órdenes auditadas, no en order_kind ni en esta inspección estática.
- PF monetario usa PnL USDT después de costos. El PF en R usa PnL/(qty×distancia inicial) y pondera de otra manera; distancia excluye fees/reserva y ambos denominadores evolucionan con la política. No tratar la diferencia entre PF como mejora o deterioro puro de señal. Los gross_profit/gross_loss del summary son sumas de trades ganadores/perdedores netos, distintos del bruto de precio5769.4003 del cierre.
- Las marcas Rprecio M1+fills sólo describen la trayectoria observada mientras la posición real estuvo abierta. No son MFE/MAE intraminuto, salida disponible garantizada ni licencia para optimizar trailing.
- El setup original se valida completo antes del clone; no se cambiaron señales, gestión ni cuota. Eso acredita una ablación limitada y adaptativa, sin novedad universal, causalidad identificada u OOS. Cerrar sin offsets, TTL, filtros o cambios de gestión vecinos es coherente con el protocolo.

No encontré sobreclaim material en FINAL. Mantener el cierre y los límites explícitos. Cero jobs, tests, motores o modificaciones de código en esta revisión.


Recibos completos conservados en los informes de cierre, resultados, raw y análisis. Stage terminal observado PRETERMINAL ya flat; no callback FINAL inventado. Conservadas 36órdenes/36traces/717pagos auditados por root y revisión independiente de alcance más acotado. No reruncontrol ni motor adicional.

Pendiente documental creativo: revisar mecanismos que expliquen debilidades K; rival spot–perp sólo dedup documental, sin precios/imports/coverage/estrategias/jobs. No hipótesis económica autorizada por esa revisión aún. Mantener mismas cuotas y costos. Objetivo activo/no cumplido, no live/paper.
