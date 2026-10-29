# R32 — revisión estática independiente del auditor nativo
Fecha local2026-10-22. Leídos completos BTC_R32_NATIVE_AUDIT_CODE_20261022.md (Python) y BTC_R32_NATIVE_JOIN_AUDIT_CODE_20261022.md (JavaScript), y base común R32 ya leída. Sólo revisión de código, sin mirar resultados intermedios, ejecutar jobs, motores o consultar precios.

## Hallazgo bloqueante de transporte
Python itera Path("inputs").glob("*.json") y accede summary/metrics/trades en todos. El contrato run_analysis también crea inputs/manifest.json, que no tiene esa forma de snapshot. Por tanto el manifiesto puede provocar KeyError antes de auditar el primer par. Root confirmó corrección V2 ANTES del primer análisis: lista EXPECTED_NAMES explícita e inputs/<name>.json, preservando V1 y referencias anteriores. Cambio técnico, no reejecución económica.

## Coberturas faltantes que conviene completar antes de declarar auditoría íntegra
1. Cantidad nativa de entrada: Python valida precio/tipo/reloj y JS compara cantidad del trade/logs/salida, pero ninguno compara entries[0].qty contra t.qty. Añadir near(abs(entries[0].qty),t.qty, tolerancia1e-8).
2. Funding: se verifican fórmula, signo, conteos, unicidad trade|settled_at, metadata y suma; falta verificar el reloj efectivo dentro de la posición y de la ventana, según boundary_policy y fase de settlement. No sustituir effective_at por settled_at raw sin documentar normalización/jitter. Inspeccionar el schema real del ledger al auditar; esta revisión no consultó pagos.
3. Meses: conteos y sumaPNL están controlados, pero return_fraction alimenta años/rolling/mediana sin conciliarlo con equity encadenada. Desde10000, verificar pnl≈equity_previa*return_fraction, sumar pnl, comprobar continuidad start/finish, extremos START/FINISH y saldo terminal. Esto vincula porcentajes publicados al mismo ledger.
4. Ejecución de salida: hold_hours del log no verifica duración nativa. Para C sinTP, revisar que no aparezca un objetivoLIMIT; salida temporalMARKET debe corresponder al primer4h elegible desde24h o terminaldocumentado. A/B análogo48h y su objetivo2R. Contrastar tipos/valores con conversiones y prioridades reales del broker antes de imponer igualdades que rechacen una conversión legítima. La versión leída comprueba cantidad/precio de salida pero no estas causas/geometrías.

Las coberturas anteriores son carencias del chequeo estático, no evidencia de anomalías en las sesiones o motivo para repetir motores. Si se verifican fuera de esta función, registrar el recibo explícito y conservar el alcance real de cada verificación.

## Aspectos coherentes y límites
CAGR usa1904días para [2020-10-15,2026-01-01), denominador10000total. Join exacto por opened_at/closed_at es razonable bajo una posición sin parciales/reentrada mismo timestamp y falla ante duplicados. Comparación gross−fees+funding, lot.001 y riesgo previsto con reserva.001 están presentes. Mediana62meses usa índices30/31 correctos; sumas y20trimestres completos corresponden al período declarado.

La cuota1% se deriva de fuente/helper comunes y presupuesto registrado; el auditor no reconstruye wallet/margen preentrada independientemente. No atribuirle una comprobación separada de sizing desde cero. DD procede de R11M1+fills, no se reconstruye desde velas o extremos intraminuto en estas funciones.

No detecté otro defecto bloqueante de sintaxis/forma en la lectura; esta revisión no ejecutó el auditor ni certifica schemas observados, completitud de páginas o resultados. Root realiza auditoría real al terminar C.
