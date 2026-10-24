# K1001 LONG MARKET: revision independiente de implementacion y check preparado

Fecha documental: 2026-10-21. Conclusion estatica: CONFORME con el cambio autorizado, sin defecto material detectado. No es un resultado de tests ni certificacion de fills.

Fuente nueva leida completa por MCP: BtcResearchR16K1001LongMarket1m. Freeze comunicado por implementador/root: SHA256 f3aeb9be8082cfb7f5cbd4a310da1b741a7bec9d675e25d657131754f5e8b32b. El check preparado exige ese hash y los seis hashes padres congelados al ejecutarse. Solo se anaden _prepare_entry y _emit; no se cambia fuente padre.

## Revision del cambio

La fuente ejecuta legacy_long real ANTES de dict(original,entry=self.price,order_kind=MARKET), preservando la cota de extension<=1ATR y distancia respecto a la frontera original. El original no se muta. Replanifica con legacy_plan(.5wallet,.5available_margin,leverage,fee), no reutiliza qty LIMIT; preserva memo, guards, registro signals y plan/expiry. Si falta setup o sizing, cash sin fallback short/supplemento. Log de trigger original separado del precio nuevo, una vez por plan.

before, gestion, apertura, submission, cierre y trace son heredados. Geometria desde fill real, mismo2ATR de senal y runner original, sin gestion en el mismo cierre de entrada. El texto order_kind no determina el broker por si solo.

_emit llama super()._emit(stage) una vez. Luego expone estado heredado mediante SUMMARY/SOURCE/COHORT por origen/ano con stage, sin recomputar trades o incrementar ledger. La fila vieja permanece intacta. El check compara todos los campos de las filas compactas, longitud<1900caracteres/bytes, super una vez, estado completo/R11 sin cambios y repeticion de FINAL sin recuento. Repetir snapshots puede repetir filas: el consumidor conserva stage y no suma reemisiones.

## Precision necesaria sobre la politica del control

Root comunico auditoria nativa de sus ordenes: control long31 =27LIMIT+4MARKET reales, por conversion near-price del runtime (tolerancia relativa .00015); short172 =171STOP+1MARKET. Son politicas nominales con esa conversion, NO31LIMIT estrictos. No invalida ledger, pero limita la atribucion a la politica completa y se incorpora a este check como contexto, no como hallazgo independiente de stubs.

Separar los gates:
1. ANTES del unico motor: esta revision estatica, literalidad/hash, protocolo actualizado, check sintetico y framework ya auditado.
2. DESPUES de ese unico motor: verificar todas las ordenes/fills MARKET nuevos con evidencia nativa, instante/precio real, geometry y ledgers. No ejecutar motor economico adicional de preflight ni llamar a un tuple buy=(qty,self.price) prueba nativa.

## Artefacto preparado, NO ejecutado por este autor

strategies/FundingOiPilot4h/reports/K1001_LONG_MARKET_SUPPLIED_SYNTHETIC_CHECK_20261021.md

Guardado por MCP y readback exacto completo:71484bytes,370lineas; unico bloque Python completo69891caracteres. Incluye seis padres congelados y nueva fuente, AST de supplied-source con imports eliminados, stubs de indicadores/atributos, versiones Python/NumPy/Pandas y hashes registrados en runtime. Solo escribe su resultado en output/K1001_LONG_MARKET_SYNTHETIC_CHECK_RESULT.json dentro del workspace temporal de analysis.

La bateria se centra en el CAMBIO; no repite68outcomes de padres: rechazo de predicados originales y bordes inclusivos, evento original inmutable, entry exacta y qty rehecha frente LIMIT mediante oraculo escalar independiente, cupos/margen/lot, memo/guards/sin fallback, herencia y emision observacional. Los fixtures usan OHLC sintetico, nunca velas observadas. No importa estrategias reales ni simula engine/broker ni anida backtests.

No se han creado jobs, drafts, motores ni nuevas fuentes en esta revision. Root debe revisar/ejecutar el check coordinado y guardar el recibo antes de decidir el unico motor. Aun si el check pasa, no demuestra rentabilidad ni ejecucion real de venue.
