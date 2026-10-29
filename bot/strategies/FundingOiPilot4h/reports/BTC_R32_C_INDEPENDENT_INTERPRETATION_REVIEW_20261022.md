# R32 C — revisión independiente de interpretación del cierre
Fecha local: 2026-10-22. Leídos completos BTC_R32_C_FINAL_20261022.md y BTC_R32_C_RESULTS_20261022.json (dos páginas MCP, 78.408 caracteres, JSON completo). Revisión acotada de interpretación; no reauditoría de operaciones/pagos, nuevos jobs, motores ni precios.

## Dictamen
Conforme con NO_CUMPLE y cierre de la comparación sin candidata. INSIDE tiene CAGR−4,0488%, PF0,8782 y DD28,277%; CLOSE_ONLY CAGR−5,1650%, PF0,9337 y DD40,9335%. Ambos fallan múltiples puertas económicas además del techo de DD. N523/1265 supera el mínimo operativo, sin demostrar estabilidad estadística o independencia.

## Comparación y causalidad
La contención completa reduce eventos y operaciones, deja menor pérdida monetaria y menor DD, pero empeora PF y regularidad:25/62 frente34/62 meses positivos y8/20 frente9/20 trimestres. No hay dominancia. La comparación identifica estas dos políticas completas bajo el contrato congelado; no un efecto puro de calidad de entrada sobre un conjunto idéntico de trades. Ocupación, exposición, costos acumulados y capitalización cambian tras restringir señales.

La mediana mensual positiva del control (+0,3833%) es compatible con pérdida total y DD alto: cuenta frecuencia/centro de meses, no magnitud acumulada ni protección frente a meses adversos. No usarla aisladamente para promoverlo. Tampoco afirmar que la contención no contiene información en general: la evidencia no respalda ESTA operativa rentable con gestión24h/stop2ATR y costos base.

INSIDE ya pierde en precio bruto; en el control, su bruto positivo es menor que sus comisiones base. Son diagnósticos distintos y ambos rechazan el nominal neto. No omitir costos ni reetiquetar reserva de sizing como slippage ejecutado.

## Contador abierto y cierre terminal
El cambio del auditor sobre total_open_trades está justificado en el expediente como corrección semántica: contador preterminal de posición forzada a cerrar, no estado final por sí solo. La aceptación requiere el conjunto documentado PRETERMINAL closesN−1, FINAL opens=closes=N, MARKET nativo en FINISH, coincidencia con openPL bruto previo y saldo postfee. No basta ignorar el contador porque session_status diga finished.

El FINAL y RESULTS consignan esas comprobaciones y salidas STOP/24h/terminal verificadas. Esta revisión acepta su alcance documental y no las rehízo. El primer analysisjob fallido permanece registrado; corregir análisis no es repetir motor ni corregir alpha. No sumar emisiones PRETERMINAL y FINAL ni interpretar contador1 como trade final sin cerrar.

## Lados y continuidad
Los aportes long positivos y short negativos pertenecen a cuentas seleccionadas conjuntamente. No acreditan una cuenta long independiente ni autorizan retirar shorts a posteriori, sumar esa contribución con otra pata o promover un “especialista” por dólares positivos modestos.

El cierre conserva dos motores económicos y el incidente técnico de auditoría separados. Es correcto no abrir vecinos automáticos ni un séptimo motor. Nuevas preguntas justificadas pueden pertenecer a esta familia en el futuro; no se deduce agotamiento universal de rupturas o partición definitiva por lado.

Resultado: interpretación conforme con estos límites explícitos; ningún cambio solicitado a estrategias o resultados.
