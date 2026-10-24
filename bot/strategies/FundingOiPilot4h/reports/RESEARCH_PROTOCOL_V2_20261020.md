# Protocolo V2 — H1 con protección adaptada a volatilidad
Fecha: 2026-10-20.
Estado: ESPECIFICACIÓN CONGELADA; implementación y ejecución pendientes. Ningún backtest V2 iniciado al guardar este protocolo.
Autoriza este entregable la continuación del usuario tras el diagnóstico V1. Este documento especifica el siguiente ciclo; no inicia sesiones ni abre resultados reservados.
V1 permanece COMPLETE_SIN_CANDIDATA. Sus 64 slots económicos no utilizados no se reasignan.

## 1. Pregunta y criterio de falsación
Hipótesis: para las entradas H1, escalar conjuntamente stop y objetivo por volatilidad reciente, manteniendo relación 1:2, riesgo presupuestado y holding, produce resultados más estables que distancias porcentuales constantes. Es una intervención sobre protección y sizing asociado; no identifica por separado el efecto del stop frente al tamaño.
Motivación mecánica: una barrera porcentual fija equivale a distintas cantidades de volatilidad según el régimen. El diagnóstico V1 no demostró que sus salidas fueran la causa del fracaso ni estimó una escala óptima.
Se rechaza la variante ATR si no llega a shortlist, falla confirmación o estrés. Si sólo pasa un control fijo, no se atribuye éxito al cambio ATR. No se ajustan valores tras resultados.

## 2. Cuatro configuraciones nominales
| ID V2 | Entrada | Stop/objetivo | Gate OI |
|---|---|---|---|
| H1_FIXED_P | H1 | 2%/4% | apagado |
| H1_FIXED_POI | H1 | 2%/4% | creciente 24h |
| H1_ATR_P | H1 | 2 A / 4 A | apagado |
| H1_ATR_POI | H1 | 2 A / 4 A | creciente 24h |

Sin gate económico de funding en ninguna configuración. Funding contable activo en todas. No agregar filtro de tendencia, elegir dirección, ampliar holding ni cambiar timeframe.
Los cuatro IDs son especificaciones, no nombres de clases ya creadas. Guardar el mapeo exacto a estrategias y hashes antes de resultados nuevos.
Los fijos corresponden a H1_P/H1_POI de V1. Reutilizar sólo tras verificar equivalencia íntegra de padre/helpers/subclase, config, datasets, warmup, reloj y ventana. Un nombre parecido no basta. Mantener el código V1 intacto; no modificar su padre para incorporar ATR.

## 3. Datos, reloj y entradas comunes
Únicamente BTC-USDT, Binance Perpetual Futures. Ejecución histórica 1m completa, señales 4h UTC sobre barras cerradas; funding fuerza effective_fast_mode=false aunque la forma conserve fast_mode=true.
Dataset funding: 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571.
Dataset OI: 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
No sustituir versiones ni revisar cobertura por fuera de MCP. Funding liquidado visible con publicación +1m; marcas proxy conservadas. OI retrospectivo label+6m, stale máximo 10m desde disponibilidad; ceros inválidos, ausencias sin interpolar. No point-in-time certificado.
Capital inicial 10.000 USDT, plano por sesión; isolated 3x, sin multiplicar notional por leverage. Fee nominal 0,00045 por lado; slippage nominal 0 bps. Warmup 240 velas 4h sin operar.
En instante T usar sólo barras open_time+4h<=T. Exigir última barra cerrada terminada exactamente en T y su anterior consecutiva, igual que H1 V1.
D=inicio del día UTC de T. H y L son high máximo y low mínimo de las seis velas 4h únicas del día [D−24h,D). Día incompleto: no señal.
Long si último cierre c>H; short si c<L; otro caso sin señal.
Sólo plano, sin entrada pendiente y sin entrada ejecutada durante el mismo día UTC. Gate start<T<finish. Orden de entrada MARKET en la decisión; guardar precio realmente ejecutado.
OI encendido: valor observado disponible en T y valor efectivamente observado en la decisión T−24h deben ser válidos y >0; exigir actual>referencia. Primeras seis decisiones inicializan referencia; no reconstruirla desde warmup. OI apagado no exige su disponibilidad.
Gestión de posiciones siempre activa aun si faltan features. Los datos de funding económico no condicionan entradas.

## 4. Volatilidad definida sin ambigüedad
A es la media aritmética de los últimos 14 true ranges de barras 4h cerradas, en unidades de precio USDT/BTC. No es el ATR de Wilder ni una llamada a indicador con semilla implícita.
Para las últimas 15 barras cerradas consecutivas B0...B14:
TR_i=max(high_i−low_i, abs(high_i−close_(i−1)), abs(low_i−close_(i−1))), i=1...14.
A=sum(TR_i)/14. B14 termina en T. No usar la vela en formación ni valores posteriores a T.
Exigir timestamps separados exactamente 4h, OHLC finito y coherente, A finito y >0. Sin ello, ATR no entra; registrar atr_invalid. No forzar una máscara ATR nueva sobre controles reutilizados: cuantificar las oportunidades con diferencia de disponibilidad; si las hay, no atribuir la diferencia exclusivamente a distancias.
Ventana 14 y multiplicador 2 son elecciones iniciales fijadas antes de observar V2, con vecindad ya definida abajo; no se presentan como óptimos. No winsorizar, limitar a porcentajes ni prolongar ventanas para rescatar datos.

## 5. Stops, objetivos, holding y sizing
Sea s=+1 long, −1 short; p=precio de decisión; C=available_margin antes de la entrada; f=fee configurada para esa sesión.
Distancia previa d_pre=0,02*p en FIXED, o 2*A en ATR.
stop_pre=p−s*d_pre; target_pre=p+s*2*d_pre.
Rechazar si p,C,d_pre,stop_pre o target_pre no son finitos y positivos; causa distance_invalid. Este control evita stops/objetivos no positivos en escenarios extremos, no filtra volatilidad por conveniencia.
Pérdida unitaria presupuestada u=d_pre+f*(p+stop_pre).
qty=floor a 8 decimales de min(C/p, 0,02*C/u). Sin tamaño positivo: no entrar. El cap de notional C conserva la convención V1; con baja volatilidad puede arriesgar menos de 2%, y se reportará.
Funding y slippage se añaden fuera de ese presupuesto, igual que V1. No garantizar una pérdida máxima real 2% ante gaps, fricción o funding.
Al fill e:
- FIXED: d_fill=0,02*e.
- ATR: d_fill=2*A almacenada en la decisión de entrada, sin recalcular con datos posteriores.
Stop=e−s*d_fill y objetivo=e+s*2*d_fill. STOP protector y LIMIT objetivo, qty completa, sin trailing, parciales ni cambios posteriores.
Validar positividad también tras fill; si no es válida, cierre MARKET inmediato con causa invalid_after_fill, registrar como incidente de ejecución y no ocultar el trade. No sustituir una distancia a posteriori.
Salida MARKET en la primera decisión 4h con edad>=24h, o cierre forzado al final exclusivo del fold. Cualquier stop/target ejecutado antes mantiene prioridad según motor 1m. Preservar y describir la resolución y resolución de conflictos del motor, sin elegir trayectorias favorables.
En estrés se usa f estresada también en sizing. Slippage adverso real se aplica a MARKET/STOP, no LIMIT, según integración existente; no aplicar haircut posterior como sustituto de fills.
Guardar motivos explícitos de salida temporal/final e inválida en logs acotados; para órdenes protectoras preservar submitted_via. No volver a inferir silenciosamente motivos desde sólo holding.

## 6. Prerrequisitos técnicos y trazabilidad
Antes del primer resultado ATR económico: fuentes completas inmutables de padre, helpers y subclases; hashes SHA256; config exacta por sesión; datasets; versión/runtime/framework y estado dirty preservado.
Pruebas deterministas de true range con gaps, media de 14 TR, necesidad de 15 barras, prefijos y mutación futura, alineación UTC, datos inválidos, sizing long/short y cap de notional. Verificar distancias ancladas a fill con A congelada; no usar resultados económicos para corregir reglas.
Hasta cuatro sesiones técnicas adicionales registradas por separado, máximo 10 días cada una dentro de 2020–2021, sin selección ni métricas usadas para elegir parámetros: nominal P, nominal POI, estrés combinado long/short si aparecen, y sensibilidad OI si necesaria. Reutilizar smokes V1 para lo que ya prueban; no afirmar cobertura de casos no ejecutados.
Para cada sesión: ID y dashboard_url real MCP, timestamps, duración, config, fuente/hash, etapa, estado, errores y reintentos. Ante timeout consultar la misma sesión; no duplicar.
Contadores mensuales por dirección y total: barras, señales precio, oportunidades estando plano/con cupo, entradas, salidas y causas exclusivas y flags simultáneos. Preservar causas V1 y añadir atr_invalid, distance_invalid, qty_invalid, invalid_after_fill.
Cada entrada: p, fill, C, qty, A, 15 timestamps o extremos de ventana más hash de barras, d_pre/d_fill, riesgo presupuestado y realizado, stop/target, features OI y sus timestamps. Conciliar precio bruto−fees+funding=PNL y saldo final por trade (tolerancia 1e-6 USDT), ledger completo.
Sólo Jesse MCP local para estrategias, sesiones, datos y reportes; run_analysis sobre snapshots para análisis. Sin research_scripts, ML, RST no solicitado, cuentas, Pi, live/paper, cambios globales, instalación ni reinicio.
Errores MCP bloquean el trabajo dependiente: no reemplazar por CLI/DB. Cambios de framework que pudieran resultar necesarios no se autorizan por este protocolo.

## 7. Exploración cronológica y controles ya vistos
Train expansivo desde 2020-09-01, termina al comienzo de su evaluación; límites exclusivos.
| Fold | Fin train / inicio eval | Fin eval |
|---|---|---|
| E1 | 2022-01-01 | 2022-07-01 |
| E2 | 2022-07-01 | 2023-01-01 |
| E3 | 2023-01-01 | 2023-07-01 |
| E4 | 2023-07-01 | 2024-01-01 |

Cuatro configuraciones × cuatro folds × train/eval = 32 slots nominales; 16 controles V1 reutilizables, 16 ATR nuevos previstos. Si la equivalencia no permite reutilizar, los reruns ocupan esos mismos 16 slots, sin ampliar presupuesto.
Orden de trabajo nuevo: train E1 ATR y verificación de controles train → guardar selección → evaluar E1 ATR → repetir E2–E4. Un backtest activo.
Los controles de evaluación ya fueron vistos en V1 y el diagnóstico. Registrar ese hecho: guardar selección antes del nuevo resultado ATR no convierte controles en evidencia inédita ni a V2 en validación independiente de 2022–2023.
Elegibilidad train por configuración: >=30 trades, neto>0, PF>=1,2 y abs(DD motor)<=25%.
Orden: menor absDD, mayor PF, menor turnover (suma notional de fills ejecutados/10000), menos features OI, ID lexicográfico. PF sin pérdidas pero con beneficios se ordena como infinito y se informa como tal; sin trades/beneficios no elegible.
Elegir entre las cuatro; si ninguna pasa SIN_CANDIDATA, selector plano. No sustituir por mejor evaluación. No mover umbrales según fold.
Ejecutar las ablaciones aunque selector esté plano para diagnóstico, manteniendo 32 slots; no abrir confirmación si no hay shortlist.

## 8. Shortlist: máximo una finalista
Después de E1–E4, candidatos elegidos al menos una vez en train, con suma nominal neta de cuatro evaluaciones>0, >=2 semestres positivos y >=30 trades únicos de evaluación. Estas reglas conservan el gate exploratorio V1; no equivalen a confirmación.
Orden: menor peor absDD de las cuatro evaluaciones, mayor PF agregado de sus trades únicos, menor turnover agregado, menos features, ID. Guardar una finalista como máximo en FROZEN_SHORTLIST_V2.md antes de consultar métricas nuevas de 2024–2025.
Candidata fija que supere esto no valida ATR. Reportar además comparación ATR vs fijo para igual uso OI, fold a fold, exposición, cantidad, bps no ponderados y precio/fees/funding; mejora no requiere el mismo conjunto de trades porque la salida modifica ocupación y cupo diario. No tratar la comparación como efecto puro entre entradas emparejadas.
Sin candidata: cerrar V2 y no reasignar reserva de confirmación/estrés a tuning.

## 9. Confirmación interna 2024–2025
Sólo la finalista congelada, train expansivo desde 2020-09-01.
C1: eval [2024-01-01,2024-07-01).
C2: eval [2024-07-01,2025-01-01).
C3: eval [2025-01-01,2025-07-01).
C4: eval [2025-07-01,2026-01-01).
Ocho slots nominales (una × cuatro × train/eval).
Cada train aplica el mismo gate y decide finalista o plano; decisión persistida antes del siguiente resultado de eval. La eval de la finalista se puede ejecutar aun con selector plano, pero sus operaciones no se agregan al selector ni acreditan sus gates.
La incorporación por calendario de resultados anteriores a train siguiente no permite cambiar reglas.
2024–2025 es reserva interna de este ciclo con exposición histórica de otras investigaciones; no muestra virgen absoluta.

## 10. Índice, gates y presentación
Cada sesión reinicia 10000 y está plana en bordes. Índice selector inicial 10000: escalar curva eval elegida por índice al comienzo/10000; en folds sin elegible mantener plano. Cierres de borde con costos incluidos. Convención de reinversión proporcional por semestre; no replay continuo de capital/órdenes.
PF agregado usa trades únicos seleccionados de sesiones nominales reseteadas; no sumar train. Separarlo del índice reescalado. Reportar DD motor por fold y DD de índice a resolución de curvas guardadas, normalmente diaria; no afirmar DD intraminuto.
Gates nominales de confirmación: índice neto>0, PF agregado>=1,2, DD índice<=25%, >=100 trades seleccionados, >=3/4 semestres positivos. PF indefinido sin pérdidas se informa con su caso exacto; ausencia de curvas o datos necesarios deja INCONCLUSO.
Reportar todos los meses, peor mes, mediana, rachas, long/short, exposición, tamaño/turnover, neto/bruto/fees/funding, concentración por mejor trade y semestre y signo al retirar mejor semestre. No crear un gate de concentración después de verla.
20–30% anual es meta orientativa, sin cuota mensual ni anualizar el mejor semestre.
No sumar netos de distintas configuraciones ni solapar entrenamientos. Un neto sumado de folds reseteados es descriptivo, no retorno real de cuenta.

## 11. Robustez fija: hasta 24 slots
Sólo si shortlist existe y se completó confirmación nominal. Escenarios se ejecutan sobre los cuatro folds C1–C4 de la finalista sin cambiar retrospectivamente las decisiones de exposición tomadas por train nominal; fold nominalmente plano permanece plano en todos los índices de estrés. Las sesiones contrafactuales no seleccionadas se separan.
Fricción: 12 slots nuevos, cuatro folds por escenario:
S1 fee=0,0009 y slip=0.
S2 fee=0,00045 y slip=5 bps.
S3 fee=0,0009 y slip=10 bps.
Estos son escenarios deterministas por lado, no estimaciones calibradas de mercado. Validar propagación/aplicación real en fills.
Vecinos: ocho slots, dos por fold:
- ATR finalista: stop 1,8 A / objetivo 3,6 A; stop 2,2 A / objetivo 4,4 A.
- FIXED finalista: stop 1,8% / objetivo 3,6%; stop 2,2% / objetivo 4,4%.
Período TR14, holding, entradas, OI y resto idénticos. No seleccionar el vecino ganador; sizing se adapta a su distancia.
OI retrasado: cuatro slots si finalista usa OI; si no usa, reutilizar nominal sin nuevas sesiones. Entregar en T la observación que se obtuvo causalmente en T−4h; frescura se juzga en ese reloj original, sin ampliar stale ni leer futuro. Referencia de 24h igualmente retrasada; siete decisiones de inicialización. No reasignar slots ahorrados.
Gates de fricción: índices S1 y S3 deben ser netamente positivos con misma exposición nominal seleccionada. Reportar PF/DD/trades y todos los gates también en S2 y demás escenarios; supervivencia de fees sola no basta.
Fragilidad preregistrada: si cualquiera de los dos vecinos o retraso OI aplicable cambia el signo del índice completo a negativo, marcar FRÁGIL y no promover como robusta. No elegir vecino para reemplazar nominal. Índice exactamente cero deja evidencia insuficiente para robustez; requiere neto>0 en cada vecino y retraso aplicable para conclusión favorable.
Sensibilidad proxy funding por run_analysis: cashflows ×0,5 y ×1,5, conservando cantidades/fills ejecutados y exposición nominal. Atribución contable aproximada sin replay ni sizing recalculado; informar signo en ambos extremos. Si se invierte a negativo, marcar dependencia de proxy e INCONCLUSO para robustez. No slots adicionales ni bootstrap obligatorio.
Máscaras OI: conservar detalle de ausencias/ceros/stale y oportunidades rechazadas, sin borrar meses. No se presupuesta replay con máscara común; por eso aporte de OI no se atribuye exclusivamente a su señal económica.
No afirmar latencia, liquidez o sensibilidad a revisión PIT resueltas por estas pruebas.

## 12. Presupuesto cerrado y estados de cierre
Exploración 32 + confirmación 8 + robustez 24 = máximo 64 slots económicos nominales V2, contando reutilizaciones. Nuevos runs esperados como máximo 48 si se reutilizan los 16 controles; máximo 64 nuevos si requieren rerun verificado. Hasta cuatro smokes técnicos separados. Sin ampliar automáticamente por abortos o errores: registrar todo intento; reintento sólo con misma lógica/datos y motivo técnico, y aclarar su costo además de slots únicos.
No reusar los slots de V1 como permiso de búsqueda libre.
Estados: SIN_CANDIDATA si shortlist vacía; RECHAZADA si falla gate económico/ejecución; FRÁGIL según vecindad/retraso; INCONCLUSA si evidencia/datos insuficientes; CANDIDATA_HISTÓRICA únicamente si cumple nominal, fricción y estabilidad aquí fijadas.
Ni siquiera CANDIDATA_HISTÓRICA autoriza live, paper o abrir 2026.
No alterar este protocolo tras resultados para rescatar una variante. Un cambio material es otra versión que declara datos ya observados; no sobrescribir este archivo.

## 13. Próximo paso y entregables
Protocolo listo para revisión. Próxima acción operativa: implementar ATR aislada del padre V1, congelar fuentes/hashes, completar tests/smokes y registry V2 antes del primer lote económico.
Entregables previstos: RESEARCH_V2_IMPLEMENTATION.md, REGISTRY_V2.json, selecciones previas por fold, WALK_FORWARD_EXPLORATION_V2.md, FROZEN_SHORTLIST_V2.md, WALK_FORWARD_CONFIRMATION_AND_STRESS_V2.md y FINAL_DECISION_V2.md, incluso si no hay candidata.
Los documentos V1 y POSTMORTEM_V1_20261020.md son antecedente observado, no resultados V2.
2026 cerrado a consultas/backtests; cualquier examen posterior requiere candidata inmutable y autorización específica. Sin commit/push ni despliegue.
