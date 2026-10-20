# X03 R3 — protocolo cerrado de ejecución y atribución
Congelado2026-10-19 antes de nuevas fuentes, backtests y análisis económicos de esta ronda.

## Objetivo
Separar el efecto de la comisión sobre el piso de breakeven de PAXG del coste cobrado; explicar mejora N204−X03 y fragilidad de meses positivos. No crear señales ni seleccionar una gestión por rentabilidad.2026 cerrado incluso a inspección. Sin OOS nuevo, live/paper, config global, funding, datos nuevos, research_scripts, RST ni MonteCarlo.

## Hipótesis y único cambio de código
El piso actual de PAXG long es entry*(1+2.5*fee_rate), activado cuando (best_close−entry)/initial_distance>=2.25, combinado con trailing y guardas originales. La comisión real también afecta sizing y riesgo compartido. Elevarla puede cambiar salidas y ocupación, además del coste directo.

Copiar PortComparePaxgMarket4h a X03ExecPaxgFixedBeR301 autocontenido: renombrar clase, añadir BE_FEE_ANCHOR=.00045 con comentario de origen nominal congelado, sustituir SÓLO self.fee_rate en el piso BE por esa constante. Mantener todos los demás métodos, HP, señales, ATR/trailing, horarios, entradas, ledger, logs y riesgos exactos. No sobreescribir fuente base. No convertir el piso en BE neto al fee elevado; puede cerrar con pérdida después de comisión. No modificar BTC ni SPY.

El ancla fija es un contrafactual diagnóstico, no un arreglo validado ni una candidata de cartera. Trailing y guardas pueden dominar el piso. Costes reales, sizing, riesgo y capital siguen usando el fee motor. No es un overlay ni un experimento que fije todas las decisiones.

## Matriz:8backtests nuevos exactos
BTC X03=BtcExploreR103 o N204=X03ExploreR204; cada uno en B/C; fee .00045 y .00070 por lado. Único PAXG del nuevo lado: clon fixedBE. Cuatro referencias nominales y cuatro de fee alto con PAXG original se reutilizan, sin reruns.

Nombres de pares nuevos: FBN0_B/C (BTCX03,fee.00045), FBN1_B/C (BTCN204,fee.00045), FBS0_B/C (BTCX03,fee.00070), FBS1_B/C (BTCN204,fee.00070). Cada ticketroot permite sólo su parB/C simultáneo, máximo4fulls globales. Sin variantes adicionales. No ejecutar stress hasta comprobar paridad nominal de los cuatro nuevos: mismos trades, precios, timestamps, qty y fees, tolerancia numérica PNL1e-7USDT, contra referencias respectivas. Etiqueta de clase/log cambia, no economía. Si no hay paridad, investigar y reparar sólo implementación; no interpretar económica ni cambiar hipótesis.

Contrato idéntico:2020-10-15→2025-12-31 exclusivo;10000USDT shared,riesgo1%trade/8%agregado,isolated5x,cap4.4,reserve.001sizingonly. Orden rutas BTC/PAXG/SPY4h,SPYSecondB/SpyMarketC,3feeds1m,warmup240,debugtrue,fastfalse,charttrue. Todos tipos misma fee. Source snapshots3 yform exactos; comparar fuentes al cerrar. QA de intervención y reviewroot antes de tickets. Sin nuevas dependencias ni cambios de framework.

## Tres roles y concurrencia de análisis
Costes: fuente y QA del clon, ocho runs en pares y tickets, interpretación de BE frente motor.
Atribución: análisis temporal de ocho referencias existentes, comparando operaciones añadidas/eliminadas/retenciones por símbolo,side,open_ts único; BTC suplemento MARKET vs original STOP y long. Cerrar exactoΔneto; pares retenidos descomposición simétrica Δ(q*u)=Δq*(uN+uX)/2+Δu*(qN+qX)/2,u=PNLnet/qty. No llamar causal alpha al efecto unitario: entradas/salidas/fees/capital cambian. Exposición notional×time y desplazamientos descriptivos, perdedores incluidos. No inferir señales bloqueadas no observadas.
Revisor: revisar protocolo, métricas, paridad y conclusiones. No nuevos runs ni elegir métricas a posteriori. Como máximo2run_analysis globales, ticketsroot; root ocupa el segundo slot con auditoría/calendario. Datos sólo inputs y output temporales, víaMCP.

## Auditoría/calendario, antes de resultados nuevos
Reutilizar auditor de fills/qty/fee/PNL/wallet/terminal, cuatro anchors de precios y MTM UTC diario.61meses/19Q completos,63/21 con fronteras, activos y todos; >0 sin redondear. DDmotor ydayclose separados. Para las ocho referencias, overlays+5/+10bpsRT fijos por fill adicionales a la fee de su sesión, claramente etiquetados. Para las nuevas, fee real y overlays sólo como diagnóstico, sin confundir+5sobre.00070 con+5sobre.00045.

Para cada mes de cada referencia, reportar neto nominal de esa run, coste adicional, neto después del overlay, contribuciones por ruta y estado positivo/no positivo. Clasificación exhaustiva: positivo que siguepositivo; positivo que pasa<=0; pérdida base<0; cero base=0. Ganancia absorbida: mes base>0 y<=su propio coste adicional, sin umbral arbitrario de "pequeño". Pérdida económica bajo motor: MTM de la run<=0 antes deoverlay. Comparar meses emparejados al mismofee ymes; no imputar causas desde cierre de trades si MTM sitúa el movimiento enotro mes. Mostrar media/mediana, ganancias/pérdidas, peor mes, concentración y co-loss, sin escoger otra frecuencia o umbral para aprobar.

Comparar feealtofixedBE−feealtoactualBE porBTC/B/C y diferencia de diferencias N204−X03 entreBE. Es contraste de implementación en este simulador y sample, con interacciones de capital y otras dependencias de fees; no efecto universal ni purocoste directo. Conservar cualquier resultado adverso y conteos de runners/reentradas.

## Criterios de cierre y próxima candidata
No se cambia M65%activos/Q80%, completos e incluidos,ambosB/C;DDno peor−25%. Tratamiento oficial siguePAXGoriginal, independientemente del beneficio fixedBE. El contrafactual no es elegible para sustituirlo.

Preseleccionar N204 como BTC congelado para un eventual examen reservado sólo si mantiene Δneto>0 frenteX03 en ambasB/C confee.00070 bajoambaspolíticasBE, DDmotor dentro25% yQA/paridadcorrectas. Si falla, conservarX03referencia yN204no preferida; no rescatar con filtros o más recetas. Una preselección para investigación no equivale a pasar objetivo regularidad ni promoción. Reportar explícitamente cualquier fallo M/Q, no redondear ni aflojar umbral.2026 no se abre ni se prepara un backtest sobreél en esta ronda; requiere decisión humana posterior.

Entregables: protocolo, fuente+QA,8URLs nuevas y8referencias, auditorías completas, atribución, diagnóstico mensual, revisiónindependiente, resultado+handoff. Sólo terminar tras todaslasruns/análisis terminales ysave_strategy_report success.


Precisión editorial tras revisión independiente, antes de resultados nuevos: el trigger se expresa en R y categorías base<0/base=0 disjuntas. Sin cambios de hipótesis, umbrales ni matriz.
