# Revisión documental del bloque creativo — 2026-10-21

## Decisión única
HOLD: no abrir otro motor creativo con la idea revisada. No hay, todavía, una pregunta suficientemente material y distinguible de las exploraciones cerradas. Este cierre afecta esta propuesta, no declara agotada la investigación de BTC.

## Pregunta examinada y mecanismo
¿La distribución de actividad pasada entre distintos niveles de precio distingue una zona que el precio atraviesa rápidamente de una zona que vuelve a aceptar, más allá de centro y dispersión ponderados por volumen? La persistencia imaginable sería memoria de participación alrededor de niveles negociados, con respuestas diferentes al revisitar una distribución concentrada o dispersa. La dirección no queda determinada: participación anterior puede facilitar aceptación o provocar rechazo. Esa ambigüedad es una rival económica real, no una excusa para probar ambos signos y elegir después.

Con OHLCV sólo se dispondría de una aproximación que asigna el volumen de cada vela a un precio representativo. No es volumen real a cada precio, inventario de tenedores, costo de adquisición, desequilibrio de órdenes ni liquidaciones. La propia agregación podría producir el patrón.

## Antecedente exacto y diferencia evaluada
El antecedente más cercano es V5_VWAP_PROPOSAL.md y su protocolo ratificado RESEARCH_PROTOCOL_V5_20261020.md: ventanas móviles de 24 velas 1h, HLC3 ponderado por volumen base, media M, varianza ponderada y banda M ± 2 max(sigma, ATR14); entrada por excursión previa y reingreso/corrección, salida al centro actual, con y sin OI. No era sólo una media: ya incluía dispersión. Por tanto, presentar ahora concentración frente a dispersión como información nueva sería incorrecto.

También existe X801 de BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md: ancla en la vela de máximo volumen, con resultado inferior al control de entonces. Sus dos referencias nominales eran carteras BTC/PAXG/SPY sin funding y bajo riesgo distinto; no son evidencia comparable de una nueva cuenta BTC neta actual y no se usan para decidir un umbral.

La diferencia matemática posible sería conservar forma multimodal o asimetría de la distribución que media y varianza no identifican. Dos historias pueden compartir M y sigma y diferir en esa forma. Pero diferencia matemática no acredita diferencia económica: no se ha mostrado aquí que la aproximación OHLCV represente memoria de participación, ni una predicción direccional que no sea otra reversión/ruptura/retest. Cambiar momentos por bins, pesos, ventanas o nombres no bastaría. No recomiendo convertir esa posibilidad en otra familia ni abrir una grilla.

## Evidencia existente y decisión que podría cambiar
La lectura de las fuentes anteriores resuelve sin otro motor que media, dispersión, volumen y niveles ya tienen antecedentes explícitos. Los cierres J–M, W, Y y AA corroboran además que niveles nominales, geometría, duración de episodios y asociaciones volumen/precio ya fueron contrastados; no acreditan que una nueva distribución vaya a funcionar. No se extrapolan sus negativos a toda representación posible.

Lo que cambiaría HOLD antes de otro motor sería identificar en fuentes o telemetría ya guardadas un estado observable causal que: (a) se pierda realmente al reducir a M/sigma y al ancla de máximo volumen; (b) tenga una respuesta económica especificable antes de consultar su PnL; y (c) no equivalga a las entradas de reversión/ruptura/retest cerradas. No hay esa identificación en esta revisión. Las tablas de rentabilidad existentes no contienen por sí solas el estado distribucional faltante; no permiten estimar su rentabilidad ni escoger forma/ventana/dirección.

Próximo paso de este bloque: conservar la idea como no habilitada y priorizar la resolución del diagnóstico K y del contraste ya autorizado. No hace falta una ejecución nueva para cerrar esta propuesta. Si otra pregunta material aparece posteriormente, debe contrastarse contra el historial completo antes de redactar receta; este informe no es un protocolo ni una autorización económica.

## Alcance y trazabilidad
Se leyó DOCS.md y la skill backtest-expert, la historia r4, el handoff r29, revision.json r29, cards E–I/J–M/W/Y/AA/V5 y fuentes exactas citadas. La historia r4 es un índice de antecedentes, no un censo exhaustivo independiente. El inventario actual incluye 50 IDs económicos desde r9 y mantiene separados los 209 de V1–V6; no son muestras independientes.

Fuentes principales:
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r29/HANDOFF.md
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md
- strategies/FundingOiPilot4h/reports/V5_VWAP_PROPOSAL.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V5_20261020.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r13/DISCOVERY_RESULTS.md

Sólo revisión documental y este reporte por MCP. Ningún job, backtest, estrategia, consulta de precios, instalación, importación, nueva economía 2026, USDC, cambio de riesgo/configuración o sesión live/paper. No se consultó ni tocó el caso MARKET que audita root. BTC-USDT mantiene costos base taker .00045 más funding histórico, 3x; no se propone estrés.
