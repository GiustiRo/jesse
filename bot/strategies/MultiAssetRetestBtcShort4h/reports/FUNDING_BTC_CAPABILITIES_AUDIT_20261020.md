# Auditoría inicial: funding BTC sin ML

Fecha2026-10-20. Usuario autoriza avanzar y excluyeML. Se inspeccionaron las capacidades MCP y los recursos jesse://configuration y jesse://backtest_metrics, además del plan previo. No se inspeccionó aún el código interno del framework ni se importaron tasas.

## Hechos verificados
- No hay herramientas de funding en el catálogo actual de jesse-local.
- La configuración backtest expuesta contiene logging,warm_up_candles,exchanges; BinancePerpetual exponebalance/leverage/type/fee, sin opciónfunding.
- read_project_file/write_project_file/list_project_files están limitadas a strategies/ y research_scripts/. No permiten leer o editar el motor ni sus tests. No intentar escapesdepath, análisis que leaelrepo, ni scripts como bypass.
- Los recursos consultados no documentan ledger ni métricasfunding. Esto no prueba ausencia de código interno; sólo ausencia de la interfaz necesaria en el MCP actual.
- El proveedor Binance USDⓈ-M documenta historial de liquidaciones y metadatos de funding. Confirmar paginación,unidades,marcas y disponibilidad antes de crearimportador. Fuentes: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History y Get-Funding-Rate-Info.

## Decisión de alcance
ML queda excluido. El bot anterior mezcla5variablesfunding,3OI y4deprecio/régimen enLightGBM; no identifica causalmente el aporte de funding. No inferir que la rentabilidad procede sólo deML ni que fundingfuncione por sísolo.
Funding puede alimentar reglas deterministas: filtrodecarry, estado de saturación o interacción con señal deprecio. Son hipótesis a comparar, no edge demostrado. Primer paso sigue siendo costecontable correcto antes de condicionespredictivas.

## Límite operativo pendiente
El usuario había pedido trabajar sólo porMCP. Se solicitó una excepción específica para inspeccionar/editarframework ytests conherramientaslocales, manteniendo datos,estrategiasybacktestsporMCP. Esperar esa respuesta antes de acceder alframeworkporotravía.

## Próxima acción al resolver el límite
Inspección no destructiva del motor real, modelos y persistencia; confirmar entornoPythonexistente e instruccionesdetests; cerrar contrato técnico antesde editar. Luego implementación con fundingdisabledpor defecto, ledgerhistóricoBTC, herramientasMCP para tasas, resultadosytests de unidades/signo/reloj/parciales/missing ysinanticipación. Sinlive/paper niOI niML.
