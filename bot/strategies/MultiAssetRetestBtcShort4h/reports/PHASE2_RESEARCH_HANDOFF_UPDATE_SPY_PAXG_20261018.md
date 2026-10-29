# Actualización del handoff: investigación SPY/PAXG completada

Fecha local: 18 de octubre de 2026. Este documento actualiza el estado del PHASE2_RESEARCH_HANDOFF_20261018.md para la continuación autorizada en este chat. Leer el resultado consolidado antes de nuevas corridas: **SPY_PAXG_RESEARCH_RESULTS_20261018.md**, en esta misma carpeta. No hay trabajos pendientes de esta etapa.

## Acuerdos humanos nuevos
Se invirtió la prioridad: SPY y PAXG se investigan independientemente antes de volver a BTC. Se aceptaron los datos proxy existentes para desarrollar estrategias de precio destinadas a Binance perpetual; funding se excluyó de esta etapa, sin exigir implementarlo. Se autorizó trabajar con dos agentes y hasta cuatro backtests simultáneos globales, dos por agente. El servicio aceptó cuatro. La regularidad es objetivo de cartera, no requisito individual de cada señal. No se abrieron fuentes nuevas, compras, instalaciones, framework, live/paper, Pi o 2026.

## Resultado y qué no repetir
Se completaron 17 full económicos nuevos: cinco SPY, once del agente PAXG y un estrés de ejecución de root. SPY apertura ORB60/impulso fracasa neto por fricción; exposición lenta con SMA200 observaciones no mejora su control beta protegido, sólo siete trades. PAXG shock 1,5 ATR de 4h, continuación/reversión con 48h, pierde incluso antes de fees. No ajustar estas recetas para rescatarlas.

PAXG fin de semana: ancla viernes 16 NY, evento domingo 16 NY, desviación de precio propio frente a ATR 4h fijado al ancla, fade al ancla, stop 2 ATR y 24h. Primaria original 1 ATR sigue documentada: +400,22 USDT, 37 trades, débil temporalmente. El vecino 0,75 fue un hallazgo adaptativo: +764,04, 60 trades; el control hábil 0,75 pierde −1171,40 y la salida MARKET al cierre horario gana +768,17. Esto justifica conservar una candidata de investigación, sin llamarla OOS independiente ni aceptar una prima perpetual demostrada. El vecino alto 1,25 falla costes y muestra.

## Comparación compartida ya ejecutada
No repetir por creer que está pendiente. Se usó PAXG al 1% en ambos controles, BTC/SPY al 3%, share de 4h completas común, ledger de reservas y límites originales:
- [C: retest actual](http://localhost:9200/#/backtest/148f089d-2a06-48e0-b3eb-cd45a9f69eb2): CAGR 27,026%, DD motor −13,523%, 35/61 meses activos positivos, 14/21 trimestres.
- [T: fin de semana 0,75](http://localhost:9200/#/backtest/08975619-224b-415a-9c40-bde9ded32d69): CAGR 27,551%, DD motor −12,359%, también 35/61 y 14/21.

Incremento neto +756,71 USDT y menor DD frente a C, sin mejora de regularidad. PAXG realizado aporta 130,54 menos; la mejora de cuenta surge principalmente de tamaños endógenos BTC/SPY. Los eventos BTC/SPY coinciden C/T. Frente a referencia original, T tiene menos CAGR y trimestres positivos. No reemplazar referencia ni declarar meta alcanzada.

Auditor root V4 final 63531bd31d1a47d28c3f3702a8d8b6a9 succeeded, fills/fees/wallet/MTM conciliados. Períodos completos: C35/59 meses activos, T35/60; ambos35/61 calendario y13/19 trimestres. Se conserva toda la ventana, incluidos bordes parciales. No usar curvas motor00:01 ni PnL por mes de cierre como MTM.

## Fuentes para continuar
- Consolidado de toda la etapa: SPY_PAXG_RESEARCH_RESULTS_20261018.md.
- SPY: strategies/ResearchSpyReference4h/reports/SPY_INDEPENDENT_RESEARCH_FINAL_20261018.md.
- PAXG aislado y controles: strategies/ResearchPaxgWeekendReturn1h/reports/PAXG_RESEARCH_FINAL_20261018.md y protocolos/extension de falsación.
- Integración: strategies/ResearchPortfolioPaxgWeekend075/reports/PAXG_SHARED_ACCOUNT_RESULTS_20261018.md y ROOT_SHARED_ACCOUNT_ANALYSIS_SOURCE_20261018.md.
- Estrés root: strategies/ResearchPaxgWeekendCloseStress1h/reports/EXECUTION_STRESS_RESULTS_20261018.md.

Referencia y 2026 intactos. Desarrollo 2020–2025 sigue ampliamente adaptativo. Hay una pista PAXG útil y descartes concretos, no una estrategia aceptada ni obligación de seguir barriendo parámetros. Una futura línea debe justificar información o payoff distinto, revisar todos los negativos y conservar los criterios antes de abrir una muestra reservada.