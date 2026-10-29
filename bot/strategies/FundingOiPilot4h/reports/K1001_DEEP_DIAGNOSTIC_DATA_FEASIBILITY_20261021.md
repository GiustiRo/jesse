# K1001 BTC aislado — viabilidad del diagnóstico de registros

Fecha: 2026-10-21. Estado: revisión documental terminada; propuesta de análisis pendiente de protocolo y revisión root. No se lanzó run_analysis, estrategia, draft, backtest, importación o consulta de velas. No se cambia el contrato ni se autoriza simultaneidad, hedge o cartera.

[Cuenta BTC aislada K1001](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4): sesión terminada, 192 operaciones y posición final cero. Su cierre P permanece NO_CUMPLE: CAGR26,8148%, M37/58 y Q15/20 no alcanzan30%/65%/80%, pese a PF/DD favorables. Que sea una referencia próxima al objetivo no la convierte en candidata aprobada.

## Evidencia ya disponible

Se leyeron summary y record completo de la sesión, una muestra de dos trades para verificar esquema, página terminal150líneas y una muestra de dos pagos de funding para esquema. También fuentes completas BtcResearchR16LegacyK1001m y BtcResearchR16LegacyBase1m, protocolo P completo en dos páginas, cierre P, accounting P completo, telemetría K1001 completa, auditoría framework P y recurso jesse://session_analysis. No se agregaron estadísticas desde la muestra parcial de trades o pagos.

| Registro existente | Qué contiene | Uso defendible |
|---|---|---|
| Snapshot completo de sesión |192trades,1905puntos Portfolio diarios,formulario/metrics y wrapper guardado | Cuenta global; precios/qty/fees/funding por trade, tiempos, órdenes exportadas. El trade NO contiene origin. |
| R16_LEGACY_OPEN y CLOSE en log |OPEN guarda origin,signal_at,opened_at,qty,precio,distancia,stop/target,budget,reserva; CLOSE guarda time,origin,net | Identificar las ejecuciones por componente, mediante unión1:1 comprobada con trades. OPEN no guarda trade_id. |
| R16_LEGACY_STATS terminal | LONG_RUNNER31; CORE_SHORT116; SUPPLEMENT45; cierres iguales; netos10650,419092/4686,298492/9191,971407USDT | Ledger ejecutado ya conciliado; NO tres estrategias standalone.313planes,192fills,121cancelaciones,82eventos de suplemento. |
| R11 y telemetría guardada |63intervalos/62meses completos,20Q,DDM1+fills16,5039%,2.741.760marcas contabilizadas,58meses activos | Medición del libro y años/ventanas ya publicados. El número de marcas NO implica que se haya guardado toda la serieM1 de equity o precio. |
| Ledger histórico de funding |1151movimientos con trade_id,effective_at,cashflow,qty,marca/provenance;698pagos con proxy | Asignación temporal de financiación si se dispone del ledger completo; lectura parcial actual sólo acredita campos. |
| Logs genéricos de órdenes |submit/execute/cancel y secuencia temporal | Vida de órdenes ejecutadas o canceladas y estado realizado del libro; no todos los setups rechazados. |

La auditoría financiera P existente, job0aceae731d224b0585f7fe7ff6ac3d47, ya reconcilia todo el libro a1e−6USDT. No repetirla como nueva evidencia si basta reutilizar su recibo. La telemetría guardada tiene resumen, ledger agregado y63meses, pero NO mapa trade_id→origin ni matriz origen×año.

## Identificación de origen: requisito previo

LONG_RUNNER es la única rama long. CORE_SHORT y SUPPLEMENT son AMBAS short con entrada solicitada STOP; ni lado ni tipoSTOP distinguen estas dos ramas. No clasificarlas por rentabilidad, duración realizada o año.

La vía principal es extraer TODOS los R16_LEGACY_OPEN/CLOSE del log y unirlos a los192trades por opened_at, lado, qty y entry_price, con unicidad y coherencia de close_time/net. Validar31/116/45,192aperturas/cierres y suma neta contra ledger; empates, ausencias o duplicados deben quedar UNATTRIBUTED y bloquear una atribución completa, sin elegir el match por PnL favorable.

La geometría inicial TP2R frente TP1.5ATR del core NO es sustituto garantizado del log: la muestra del primer short cerrado porSL sólo exporta entradaSTOP y salidaSL, sin TPcancelado que sabemos existía por fuente. No presumir que orders del snapshot conserva todas las barreras canceladas. Tampoco todos los registros genéricos de cancelación llevan origin.

Limitación operativa para el futuro análisis: el recurso run_analysis garantiza summary/metrics/trades/equity/hyperparameters, no logs de ejecución. El record completo inspeccionado contiene infoLogs vacío. Antes de lanzar el job hay que fijar una vía permitida para unir/cotejar el log completo; no pegar arrays de resultados al código, leer archivos del proyecto desde analysis, inventar inputs no admitidos o asumir que el snapshot trae origin. Si no hay vía soportada, limitar la primera fase al libro completo/long frente short agregado y dejar CORE/SUPPLEMENT por año como pendiente explícito. La lectura documental actual no resuelve por sí sola esa ingestión.

## Prioridad y ocupación: qué se sabe y qué falta

La fuente fija LONG_RUNNER→CORE_SHORT→SUPPLEMENT, incluyendo elegibilidad de sizing: si una candidata superior no forma plan se considera la siguiente. Una sola posición; pendientes hasta cuatro horas; cancelación puede permitir rearmado en el mismo cierre4h después de liberar margen, mientras una posición recién cerrada no reentra ese timestamp. Esto ya fue auditado en P; no requiere reinterpretar el resumen genérico del lifecycle.

El suplemento actualiza su latch aun abierto o con orden pendiente, antes del gate de cuenta. Sus82eventos cuentan eventos que superaron la geometría de la función, no todos los estados de precio. Los313planes son seleccionados con cuenta elegible, no el universo de oportunidades.

La variable occupied se incrementa en memoria, pero R16_LEGACY_STATS NO la emite; tampoco persiste por cada cierre4h el estado del latch, candidatos de las tres ramas, motivo de rechazo o su precio de entrada. Por ello:
- Se puede reconstruir exposición efectiva por componente y, con los logs completos de órdenes, intervalos con pendiente, vacíos y cancelaciones. Son estados REALIZADOS del libro.
- No se puede reconstruir con estos registros el universo completo de señales no ejecutadas, su resultado hipotético o cuántas habría tomado una rama aislada.
-82−45=37 NO equivale a37trades perdidos por ocupación: mezcla prioridad, bloqueo, sizing, cancelación/no fill y reglas de consumo. No asignar ese residuo a una sola causa.

## Análisis mínimo propuesto, sin ejecutar todavía

1. Congelar un solo universo: esta sesión BTC aislada192trades, contrato P intacto; ningún derivado, N204 comparativo, 2026 nuevo, vela o motor. Recuperar recibos existentes y determinar la ingestión legítima del mapa de origen antes del job.
2. Verificar integridad del mapa y contabilidad agregada ya acreditada. Mantener orden temporal, fees/funding y timestamps; si funding falta en un trade, no imputar automáticamente hasta contrastar que no tiene pagos vinculados.
3. Con origen identificado, tabla origen×año de APERTURA y, separadamente, año de CIERRE: N, PnL bruto/fees/funding/neto, ganadoras/perdedoras/PF descriptivo, duración/exposición efectiva y concentración en pocas operaciones. Incluir2020parcial etiquetado y todos2021–2025; no elegir años/lados por resultado. PNL de cohorte por cierre no es retorno anual de equity.
4. Diagnóstico de riesgo ejecutado: con OPEN, neto/actual_loss o budget como múltiplos realizados claramente etiquetados; actual_loss incorpora reserva de sizing y no es pérdida máxima garantizada. Describir órdenes/salidas registradas sin llamar a todo STOP una pérdida ni a toda MARKET un timeout.
5. Mantener retornos mensuales/trimestrales, DD y ventanas12m EXACTOS del LIBRO como ya publicados. No anunciar CAGR, mediana mensual o DD standalone de cada rama desde una suma de trades. Para MTM por origen harían falta cortes y cashflows completos más identificación inequívoca de posición abierta/phase a cada frontera; si no se acredita eso, no fabricarlo.
6. Formular como máximo una pregunta posterior basada en una limitación concreta, con bloque creativo documental separado. No crear variantes long-only/short-only/trend/range, filtros o libros paralelos automáticamente a partir de estas tablas.

Una separación futura en2–3operativas con cuentas y exposición propias cambiaría selección, capitalización, tamaños, margen y oportunidades bloqueadas. La contribución realizada en este libro puede ser positiva sin que exista una operativa independiente rentable. No sumar sus curvas hipotéticas ni prometer diversificación/edges por lado.

## Límites de datos y entregable

Sin nuevos precios no hay trayectoriaM1 completa acreditada para MFE/MAE, extremos intraminuto, stop alternativo, entrada contrafactual o etiqueta de mercado trend/range. Las modificaciones de trailing registradas no recuperan toda la excursión ni ATR/feature en cada momento. Portfolio diario no sustituye esas series.

Entregable futuro mínimo: mapa y auditoría de origen, tablas de cohortes/concentración/exposición, conciliación contra libro, lista explícita de UNATTRIBUTED y datos no observados, más una pregunta material revisable. Diagnóstico descriptivo/causalmente ordenado por información disponible; no causalidad experimental de quitar o independizar componentes. Todavía cero jobs o nuevos motores autorizados por este informe.

Fuentes duraderas en strategies/FundingOiPilot4h/reports/: BTC_DISCOVERY_P_PROTOCOL_20261021.md, BTC_DISCOVERY_P_FINAL_20261021.md, BTC_DISCOVERY_P_ACCOUNTING_20261021.json, BTC_DISCOVERY_P_BtcResearchR16LegacyK1001m_TELEMETRY_20261021.json y BTC_DISCOVERY_P_FRAMEWORK_AUDIT_20261021.md. Fuentes de estrategias víaMCP, sin cambios. Recursos y sesión también leídos porMCP; el Hub queda bajo publicación de root.
