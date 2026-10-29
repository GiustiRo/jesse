# Tanda N: preparación técnica final

Fuente final lista para revisión y dos corridas económicas del protocolo predeclarado. No se iniciaron drafts ni motores desde este subagente; los drafts reales y su manifiesto quedan a cargo de root.

Clases nuevas: BtcResearchR14CompositeBase1m, BtcResearchR14CompositeFixed1m y BtcResearchR14CompositeState1m. Ocho readbacks completos vía MCP idénticos a las fuentes suministradas, incluidos los cinco padres/helper congelados. No se modificaron padres, framework, configuración global ni datos.

## Verificación

Check final 639fa5fe891442bb989d546ce9d358e9: succeeded, 131 aserciones, sin fallos, con entradas vacías y código AST suministrado. Usa funciones/clases exactas suministradas y campos artificiales del motor; no importa/relee estrategias, no consulta mercado y no ejecuta backtest. Verifica helpers causales, los nueve arbitrajes, consumo de ambas transiciones aun ocupado, ausencia de cola/reentrada/pirámide, origen y política congelados, stops2ATR/2R/sinTP/48h/720h/estadoopuesto, riesgo fee-aware y cierre terminal antes de FINAL real R11.

Primer check eb081df7f3ac4cc3846a33a7497d9372: succeeded, 123 aserciones. Supersedido por revisión independiente previa a economía que detectó dos omisiones de paridad: (1) conservar la guarda hipotética de precio2R heredada de B aunque no coloque TP; (2) computar estadoCORE con4h válida antes de exigir1h, para mantener salida B por estado opuesto aunque1h tenga hueco. Ambos corregidos y probados específicamente. Dos análisis sintéticos exitosos, cero fallos de análisis, cero backtests técnicos/económicos en esta preparación. Un intento JS de preparar el recibo usó TextEncoder no disponible y falló antes de escribir o llamar análisis; corregido y trazado en JSON.

La falta4h reinicia ambos estados. La falta1h conserva CORE válido, reinicia F y bloquea entradas. Los contadores de eventos y arbitraje corresponden a cierres con ambas ventanas válidas; fills/closes/net corresponden a ejecuciones reales, no a admisiones. El ledger usa closed_trade.pnl antes del callback padre y el test incluye cierre terminal.

## Hashes SHA256

- BtcResearchR14CompositeBase1m: 0e678d3928b8bada8981ae6a2bd5b678c3fb43950701e3d71ef843ba0cdb84d4
- BtcResearchR14CompositeFixed1m: 2fdfcf4f40ac526d9770ce64ec0f35d621ac0f3aaa054bb2fc59e43809b24969
- BtcResearchR14CompositeState1m: 4783828216a301c0eb14f6d4b6f72527b9e7c9c60287bb4dbe784f83ff9bbea3
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- BtcResearchR10Breadth4h: 6abc5094fb8099aea2cc02090c6c6ae9280a42e1c4a0d4b2061407fc4afd286c
- BtcResearchR10BreadthState4h: 78d6986644c688834ab847f2bfc735a6e839d8ccad4c9a38db2bc83655a88d3d
- BtcResearchR12JumpBase1m: 631377b49a213511ca5d08f63e50cf08aa38e18fcec303479b89e3a9fc0b81a6
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87

Código final del check: e458d4d3508e8aa356ff43029f7eddc4f0aa105a37b8691d223845ca17f72229.

## Recibos y límites

Protocolo actualizado antes de economía: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_N_PROTOCOL_20261021.md.

Recibo JSON completo (ambos jobs, razón de supersesión, código exacto del check final, fuentes nuevas completas, hashes, readbacks, controles y análisis de intervalos): strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_N_TECHNICAL_CHECK_20261021.json.

Root debe crear manifiesto desde formularios/drafts reales y preflight, warmup2404h, ruta1m+datos4h/1h, contrato fijo de costos/riesgo/datos y gatesr9. Presupuesto N: exactamente dos económicas; hasta dos reemplazos exclusivamente técnicos documentados. La prueba sintética no valida rentabilidad, precisión de ejecución del motor, independencia estadística ni OOS. Después reconciliar snapshots completos y ledger por origen incluido cierre terminal; no sumar curvas padre.
