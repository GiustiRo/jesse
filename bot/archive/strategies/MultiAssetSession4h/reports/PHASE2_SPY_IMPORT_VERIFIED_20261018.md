# Verificación de importación SPY — 2026-10-18

La llamada original clean_and_import_custom_candle_csv agotó la espera MCP de 300 segundos. No se repitió la importación. La serie Custom Data / SPY-USDT aparece en el MCP y en Manage Candles, con cobertura extrema 2020-01-01 a 2025-12-31. El usuario confirmó que apareció en su navegador después de logout/login; la causa de la falta de actualización del panel no está determinada.

## Integridad comprobada sobre datos exportados de la base

La exportación research_scripts/candle_exports/SPY_import_timeout_verification_20261018.csv existe y se validó mediante preview_custom_candle_csv (solo lectura, sin reimportar). Resultado: 1.974.135 filas, exactamente el recuento del CSV de origen; 0 inválidas, 0 duplicadas, 0 conflictos, 0 fallos de orden. Primer timestamp 1577919600000, último 1767215520000, coincidentes con el origen. No se hizo comparación byte a byte o checksum del contenido completo.

La validación contabiliza 1.180.798 minutos ausentes entre extremos: incluye cierres de mercado y huecos originales de la fuente. No se rellenaron. Esta validación estructural no certifica cobertura de mercado completa ni equivalencia entre SPX/USD y el ETF SPY.

## Error de exportación independiente

El endpoint /candles/export-to-project devolvió HTTP 500, pero los registros muestran que falló al eliminar el temporal durante _publish/nofollow_fs.rename, después de crear el destino: PermissionError [Errno 13] Permission denied para un archivo .jesse-*.tmp. El destino resultante se pudo leer y validar mediante MCP. Es un fallo de publicación/limpieza del archivo exportado; no evidencia corrupción de velas. No se cambiaron permisos ni código, no se reinició el servicio ni se borraron temporales.

## Estado

Importación verificada por recuento, estructura y extremos. No se repitió. Datos siguen bajo Custom Data; este diagnóstico no copió a Binance ni ejecutó backtests. 2026 sigue excluido de esta serie y de la calibración.
