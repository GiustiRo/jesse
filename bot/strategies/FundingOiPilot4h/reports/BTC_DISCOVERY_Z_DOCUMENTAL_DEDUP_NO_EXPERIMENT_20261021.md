# Próxima pregunta BTC: revisión documental Z sin experimento seleccionado

Fecha: 2026-10-21. Estado: DESCARTE DOCUMENTAL; Z no tiene receta ejecutable, protocolo ni presupuesto económico aprobado. Este archivo registra trabajo de deduplicación y no cuenta como hipótesis nueva probada. Se elaboró sin consultar resultados Y. Cero fuentes nuevas de estrategia, jobs, drafts, importaciones o velas observadas.

## Decisión

No recomendar una nueva economía sobre funding acumulado. La hipótesis tentativa era que el coste de financiación ya pagado por un lado, combinado con resistencia del precio, informase sobre posterior reversión o continuación frente a un control de precio. La motivación económica sería presión de mantenimiento de posiciones apalancadas. Sin embargo, el dato no identifica quién mantuvo posiciones, su coste de entrada, patrimonio o liquidación: sumar tasas no mide el coste acumulado de una cohorte real.

La traducción concreta disponible sería otra persistencia/signo/magnitud o ventana de pagos publicados condicionada por precio. Eso permanece dentro de los mecanismos de carry, veto o normalización ya cerrados. No se encuentra aquí una diferencia estructural suficiente; cambiar una suma por tres signos, una ventana, normalización o tabla de medias no basta. No se autoriza un intento para averiguar si un vecino sale mejor.

Esta decisión no demuestra que todo funding carezca de información, ni que sea imposible otra pregunta material con datos existentes. Es una conclusión acotada sobre esta propuesta y los antecedentes consultados. Tampoco afirma un inventario exhaustivo de todas las fuentes del servidor.

## Comparación concreta

| Idea considerada | Antecedente exacto leído | Qué se conserva / diferencia tentativa | Decisión |
|---|---|---|---|
| Coste acumulado de financiación y resistencia del precio | ResearchV5FundingFP4h; ResearchV5Base4h/funding_features.py; RESEARCH_PROTOCOL_V5_20261020.md; FINAL_DECISION_V5.md | Misma fuente de tasas finales publicadas y condición de precio; sustituir persistencia de tres signos por acumulación/tamaño sería reformulación o vecino. V5 ya usa carry favorable alineado con SMA120/ROC30, salida por tasa o tendencia adversa. | Retirar; no control ni motor nuevo. |
| Veto de crowding a señal de precio | FundingWfPilotBase4h; RESEARCH_PROTOCOL_V1.md; BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md | H1 ya bloquea precio con funding extremo adverso; H2/H3 combinan extremos o normalización y confirmación de precio. | Reutilizar evidencia; no cambiar umbral/suma para rescatar. |
| Descarga o reversión después de pago conocido | BtcResearchR10FundingEvent4h; BtcResearchR10Base4h previamente leído y congelado; BTC_DISCOVERY_AB_FINAL_20261021.md | A_EVENT ya espera una barra completa tras pago publicado e invalida el movimiento del lado pagador. Otro reloj de pago o selección posterior de sentido sería vecino. | Cerrado sin candidata; no repetir. |
| Normalización de extremos de funding | ResearchV4FundingFP1h; FINAL_DECISION_V4.md | Receta V4 usa extremos normalizados, confirmación de precio y salida por SMA24. No convertir nueva agregación en supuesto input virgen. | Cerrado; no rescate. |
| Nueva tabla de OHLCV o lag volumen/amplitud | BTC_DISCOVERY_Y_PROTOCOL_20261021.md | Y ya pregunta si orientación temporal D añade a asociación simétrica S y dirección actual. Cambiar sólo ecuación, celda o ventana no acredita otro mecanismo económico. | No proponer por obligación. |
| Reapertura de proxy o aceptación/ocupación M1 | Hub r23 HANDOFF.md y BTC_DISCOVERY_W_FINAL_20261021.md | X está HOLD por producto/calendario; ocupación ya descartada por AngleCombinedBtcAcceptance4h según cierre root. No se reevalúa aquí esa fuente como novedad. | Preservar HOLD/descarte; no sustituir validación faltante por otro motor. |

El descarte previo de carry fue leído antes de decidir. Su decisión root explícita ya retiraba un nuevo experimento de carry direccional, veto o reloj postpago; quitar filtro de precio, cambiar número de pagos o signo tampoco queda pendiente.

## Evidencia económica que se reutiliza

V5 Funding sin OI ya tiene [replay continuo](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4): 107 trades, CAGR −1,043844%, PF 0,960575, neto −207,960651 USDT y funding favorable +167,581792 USDT. V5 completa nominal, costes, vecinos y selección bajo su contrato original; no cambiar el ranking cerrado ni atribuirle riesgo actual idéntico: usa cap nocional 1x y cuota diaria.

V4 funding sin OI [screening](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068): 26 trades, neto del período −6,93%, PF 0,590. Es resultado de screening 2020–2023, no CAGR ni confirmación 2024–2025. A_EVENT ya fue evaluada bajo riesgo de investigación actual y cerró negativa; ninguna se reejecuta para este documento.

Hub r23 registra W cerrada y 44 ejecuciones económicas por ID desde r9, no muestras independientes. Esto no incorpora Y: no se inspeccionaron sus resultados, sesiones ni datos para seleccionar esta decisión.

## Fuentes consultadas y límites

Ruta base de los documentos: strategies/FundingOiPilot4h/reports/.

- RESEARCH_HUB/index.json: revisión actual 20261021-r23.
- RESEARCH_HUB/revisions/20261021-r23/revision.json, HANDOFF.md y DISCOVERY_RESULTS.md.
- RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md.
- BTC_INDIVIDUAL_EVIDENCE_MATRIX_20261021.md.
- BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md.
- BTC_DISCOVERY_AB_FINAL_20261021.md y BTC_DISCOVERY_CD_FINAL_20261021.md.
- BTC_DISCOVERY_K_FINAL_20261021.md, BTC_DISCOVERY_L_FINAL_20261021.md, BTC_DISCOVERY_V_FINAL_20261021.md y BTC_DISCOVERY_W_FINAL_20261021.md.
- BTC_DISCOVERY_Y_PROTOCOL_20261021.md, sólo especificación, sin resultados.
- RESEARCH_PROTOCOL_V1.md, RESEARCH_PROTOCOL_V5_20261020.md.
- FINAL_DECISION_V1.md, FINAL_DECISION_V4.md, FINAL_DECISION_V5.md.
- RESEARCH_DATA_AND_EXECUTION_FREEZE.md: leído únicamente como documento histórico de disponibilidad/unidades, sin consultas de series.

Fuentes completas obtenidas por read_strategy: FundingWfPilotBase4h, FundingOiPilot4h, ResearchV4FundingFP1h, ResearchV5FundingFP4h y BtcResearchR10FundingEvent4h. Helper completo leído por read_project_file: strategies/ResearchV5Base4h/funding_features.py. La fuente R10 base ya estaba leída y congelada durante W; no se editó ni se infirió un comportamiento nuevo de un nombre de wrapper.

Dos búsquedas de nombres tentativos (ResearchV5FundingBase4h y ResearchV4FundingBase1h) devolvieron strategy_not_found. Se corrigieron consultando las fuentes exactas anteriores; son ausencias semánticas, no outage MCP ni experimentos técnicos. Los listados alfabéticos acotados truncados no se trataron como censo ni evidencia de ausencia.

No se reauditan todos los fills o todas las estrategias antiguas. La evidencia suficiente para este descarte es la equivalencia conceptual concreta y los cierres existentes, no una pretendida refutación universal.

## Contrato que no cambia

Cualquier futura pregunta realmente distinta conserva BTC individual, capital 10.000 USDT, riesgo 2% por trade / 6% agregado / 3x aislado, fee taker con descuento 0,00045 por lado, funding BTC histórico aplicado con proxies declarados y slippage modelado cero. Ventana UTC [2020-10-15,2026-01-01), sin nueva economía 2026. R10 sizing y observador R11; gestión usual R12AR: stop 2 ATR14 simple, sin TP, 24 horas. No se cambian exposición, lados, gestión, riesgo o costes para recuperar resultados.

No se consume presupuesto económico por este descarte. Root puede continuar buscando otra pregunta independiente; este archivo no obliga a abrir Z y no altera el Hub, sus veredictos ni el protocolo Y.
