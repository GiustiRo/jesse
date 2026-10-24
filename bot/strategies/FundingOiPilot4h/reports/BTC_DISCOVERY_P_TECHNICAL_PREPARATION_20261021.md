# P — preparación técnica y límites antes del motor

Clases nuevas BtcResearchR16LegacyBase1m, BtcResearchR16LegacyK1001m y BtcResearchR16LegacyN2041m creadas vía MCP; siete readbacks completos idénticos, padres y observador congelados.

Análisis final d51ec9023e254adf866ad6b9de27d089: succeeded,5962 aserciones. Paridad de ramas/geometría de métodos padres reales suministrados con features artificiales:75long/29short/6K/7Ncasospositivos. ATR/EMA usan ta existente en economía; fakes del check no prueban sus semillas reales. Se verifican ventanaasof,planúnico ante shouldshort/long repetidos,prioridad,setupconsumidoocupado,TTL4h yrearmadolazy trascancel,riesgofeeaware/reserva/lote/margen, requested-vs-fill,gaps/protecciones,48h/72hprimer4h,sinTP/plazorunner,ratchet y cierreterminal antesFINAL R11.

Dos análisis sintéticos: primerjob9b621b05a6384925bfd5ab3a8e91e8f4 falló al ASTparse por paréntesis VWAP nuevo faltante; corregido antes de prueba. Segundo pasó. Cero económicas/drafts/backtests técnicos del subagente. Error de alias de recurso MCP inicial desconocido corregido a jesse-local; sin pérdida de conectividad.

La documentación MCP simplifica el flujo y sugería cancelación sin nuevaentrada enmismociclo. Root revisó código real y corrigió esa interpretación: cancelación libera margen y _check puede volver a should_* enmismociclo. Implementación final prepara lazy memoizado en should_*, permite TTLrearm enmismo4h y mantiene veto de reentrada tras cierre de posición enmismotimestamp. No se inventa orden de fill intrabar frenteexpiry.

## Hashes SHA256

- BtcResearchR16LegacyBase1m: 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542
- BtcResearchR16LegacyK1001m: bf88cb663d8561e107446bfce32024ed87531d096362671f7aafce72a09f25ad
- BtcResearchR16LegacyN2041m: ca7387d9263552dbb14a15be8bb060d645511480175628d76d5293a7f614b045
- CapitalR12K1001R2A6: 5ae10247b55da1af56bcd46c8a84d4df36ad7e923e3a499fa0902e6a3e9413a0
- CapitalR12N204R2A6: 5cf339d1a2f2096bc484a88c5790c677e41088db0067fe46ca333a4c5a7cfff4
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9

Checkcode f698c25fcd4338973986af7e0659f06010c1e8acd7a449b8ddb98c1dafc121bb; protocolo 023288325d809b06d2afebbe67fab0a97384557a57dd2aa2266363c010aa1fd2.

## Recibos y gates pendientes

- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_P_PROTOCOL_20261021.md contiene reglas, diferenciasinevitables, CODEScompletos padres/deps, presupuesto y gates.
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_P_TECHNICAL_CHECK_20261021.json contieneCODES completos de siete fuentes, ambasrespuestasjobs/error, código exacto final,hashes,readbacks ydocs/metadatosreales.
- Esta preparación no es manifiesto económico ni acredita rentabilidad/OOS.

- Actual broker replay/fill versus expiry cancellation ordering; must follow current framework, no invented cancellation-before-fill rule.
- Retention/seeding equivalence4h trading-route versus1m execution+4h data. Preserve ta.atr and full exposed closed buffer; do not claim identical seeds absent evidence.
- Root final source/protocol review then genuine draft/manifests/preflight/funding-applied checks before exactly2 economic runs.

No inspección prebacktest de cobertura. El motor informará faltantes; no autoriza importación/reinicio/cambioglobal. Ningún resultado sintético sustituye una auditoría financiera del posterior snapshot completo.
