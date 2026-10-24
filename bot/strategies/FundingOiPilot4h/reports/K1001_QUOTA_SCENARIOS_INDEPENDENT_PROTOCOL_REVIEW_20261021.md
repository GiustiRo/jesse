# K1001 cuota — revisión independiente de protocolo
Fecha documental: 2026-10-21. Revisión de sólo lectura por MCP de K1001_QUOTA_SCENARIOS_PROTOCOL_20261021.md y K1001_QUOTA_SCENARIOS_SOURCES_20261021.md. No es revisión de implementaciones todavía inexistentes ni autorización económica.

Veredicto: CONFORME documentalmente tras las precisiones root verificadas por readback. No se detectó otro bloqueo material antes de implementar.

## Denominador y evidencia
legacy_plan(event,.5*balance,.5*available_margin,3,fee) conserva el helper congelado y produce risk_budget=.01*wallet total propio de cada escenario. Reserva.001/lote.001, margen90% sobre la mitad reservada y floor permanecen; qty no tiene por qué ser exactamente la mitad por lote, capitalización y selección.

LONG_ONLY y SHORT_BOOK son dos cuentas alternativas de10000 con cuota1% y capitalización propia, no dos partes ya financiadas de un libro conjunto. No sumar curvas/CAGR ni atribuir el delta contra Koriginal sólo a retirar competencia: también cambian sizing, trayectoria de capital, fills y oportunidades. Koriginal2% permanece referencia NO_CUMPLE.

## Reglas y ciclo
before y sus helpers de señal/indicadores/consumo de estado se heredan literalmente. SHORT_BOOK conserva CORE_SHORT→SUPPLEMENT y el fallback si core no forma plan; LONG_ONLY sólo LONG_RUNNER. Única sustitución económica es allowlist y argumentos.5/.5 del helper en preparación lazy, preservando guards, memo, TTL, cancelación/rearmado y no sameexit. legacy_rows inválido impide usar un evento antiguo.

El anexo contiene invariantes históricos de una propuesta de ocupación en HOLD. Root añadió expresamente que NO gobiernan las nuevas fuentes: no capturar previous_setup ni recomputar suplemento en observador. Esta precisión se corroboró en la versión actualizada.

## Rprecio y callbacks
La primera lectura detectó la palabra opcional. Root la corrigió a OBLIGATORIO en ambos escenarios mediante una misma base común; readback actualizado confirmado.

Diseño coherente: llamar al _observe padre una sola vez y conservar su retorno; identidad propia/open0; preM1 sólo después de opened_at; exitfill y finalización diagnóstica ANTES del callback parent que puede emitir FINAL. Dedup por identidad/etapa/T conserva holding0 y open/exit en mismo timestamp. Extremos estrictos retienen primer empate. La traza es Rprecio observado M1+fill, sin fees/funding y sin extremos intraminuto; no MFE/MAE exacta ni precio posterior a salida. Nunca afecta entradas, sizing, stops o gestión.

## Alcance pendiente
La conformidad es del contrato y de los snapshots de padres ya auditados. Requiere lectura completa posterior de las tres fuentes nuevas, verificaciones sintéticas de allowlist/cuotas/TTL/trace/FINAL, y recibos/manifiesto antes de cualquier motor. Un fallo de identidad o cobertura de traza debe hacerse visible; no reparar precios ni alterar órdenes para esconderlo.

La excepción a la restricción anterior de componentes deriva del pedido humano nuevo tras el diagnóstico, no de reinterpretar P. Se preservan cierres y evidencia adaptativa; no 2026 nuevo, estrés, USDC, cartera conjunta o live/paper. Esta revisión no ejecutó jobs, drafts, backtests o cambios de estrategias/configuración.
