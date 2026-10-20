# R12 — Riesgo intermedio y apalancamiento: protocolo congelado
Fecha de ejecución 2026-10-19. Autorización: usuario solicita investigar combinaciones y niveles de riesgo sobre K1001 y referencia N204, y explicación para una cartera de 10000 USDT.

## Hipótesis
Los perfiles de riesgo 2%/6% y 3%/9%, combinados con 1x o 3x, pueden ocupar un compromiso entre el sizing original y el extremo 5%/15% de R11. El margen puede limitar la aplicación del riesgo objetivo. Se comparan políticas completas de riesgo por operación + límite agregado; no se atribuye causalmente el cambio sólo al primer porcentaje.

## Matriz exacta: 28 corridas nuevas
16 nominales: riesgo 2%/6% y 3%/9% × leverage isolated 1x/3x × K1001/N204 × B/C; fee 0.00045 por lado.
12 de estrés: riesgo original 1%/8%, 2%/6%, 3%/9% × isolated 3x × K1001/N204 × B/C; fee 0.00095 por lado.
No selección adaptativa de candidatos para el estrés: todos los perfiles a 3x pasan por el mismo estrés. No se infiere estrés equivalente para 1x, que no se corre con fee mayor en esta fase.
Anclas existentes nominales: perfiles originales 1%/8% a 1x/3x/5x, las cuatro carteras de R11. Cada análisis final tiene 10 inputs: tres anclas nominales, cuatro objetivos nominales y tres escenarios de estrés. No añadir variantes por resultados parciales.

## Condiciones
Misma ventana 2020-10-15 inclusiva → 2025-12-31 exclusiva, datos de desarrollo reutilizados. 2026 permanece cerrado incluso inspección.
10000 USDT compartidos, BTC/PAXG/SPY 4h con tres feeds 1m, warmup 240, fast_mode false, debug true, export_chart true, benchmark false. Orden BTC/PAXG/SPY constante. B usa SPY Second, C SPY Market.
Mismos cap nominal 4.4, pesos inversos ATR, reserva de sizing .001, margen disponible × .90, base capital max(0,min(wallet,equity)) y reservas de órdenes pendientes. Al bajar leverage, el margen del motor puede impedir alcanzar el porcentaje objetivo.
Clonar completas las cinco estrategias por perfil y modificar sólo nombre de clase, comentario explicativo y constantes TRADE_RISK / PORTFOLIO_RISK. No alterar señales, stops, objetivos, entradas, relojes ni calendarios. Los porcentajes de los tres activos cambian juntos. Perfil original de estrés usa fuentes originales, sólo modifica fee por sesión.
Todos los overrides dentro de form.config.exchange por sesión; configuración global intacta. Máximo dos backtests simultáneos y un análisis. No live/paper, reinicios, instalaciones, purgas ni research_scripts.

## Evaluación previa
Objetivo orientativo ya documentado: 20–30% anual, negociable; no es un filtro para ocultar resultados mayores/menores. Reportar todos los escenarios, años, meses, activos y costes.
DD diario no peor que -25%, neto positivo y PF >=1.2 son puertas descriptivas de investigación tomadas del proyecto; no validación OOS ni permiso para operar. Viabilidad nominal de ambos B/C y, por separado, supervivencia a fee estresado a 3x.
Comparación primaria: K1001 vs N204 bajo perfil/leverage/fee idénticos. Para capital, comparar objetivos contra 1%/8% al mismo leverage y fee. No presentar una delta nominal/estresada como cambio de edge a igual coste.
CAGR/DD, Calmar, Sharpe, PF, fees, recuperación, regularidad de 61 meses completos y año a año; extremos 2020/2025 parciales. Medir sensibilidad al mejor mes y concentración por activo. No sumar B/C como muestras independientes.
Frontera retorno/DD descriptiva; diferencias ínfimas no son un óptimo robusto. Si varios perfiles sobreviven, preferir explicar el coste de aumentar riesgo y señalar compromisos, sin promoción automática por ranking IS.
El estrés de fee se corre en el motor: puede cambiar cantidades, señales dependientes de cuenta y breakeven dependiente de fee en PAXG. No es slippage simulado ni funding.
Auditar PnL de trades/motor, terminal equity/wallet, configuración ejecutada y entradas/salidas contra ancla original. Si cambian fills, mostrarlos; no asumir que sólo varían cantidades.

## Explicación para 10000 USDT
En los backtests multiactivo originales: objetivo 1%=100 USDT por trade y límite agregado8%=800 USDT, no margen de100 USDT. Con tres entradas nuevas de1% serían aproximadamente300 USDT de riesgo inicial, no800 USDT automáticamente; el agregado se mide desde mark a stop y puede variar luego.
Nuevos perfiles:2%=200 USDT y máximo agregado6%=600 USDT;3%=300 USDT y9%=900 USDT. Son objetivos/límites de admisión, no garantía de pérdida máxima ante gaps y slippage.
El stop técnico no se aleja: crece la cantidad hasta donde permiten margen, notional y cuotas por activo. Ejemplo sin costes: stop2%, riesgo100USDT→nominal5000USDT; riesgo200USDT→10000USDT. A3x, margen inicial aproximado1666.67/3333.33 USDT respectivamente. El apalancamiento no vuelve a multiplicar el riesgo elegido.
Capital varía: si baja a9000, 2%=180; si sube a11000, 2%=220, antes de otros límites conservadores.
La decisión general antigua de DOCS sobre2% para BTC no sustituye los parámetros1% de las fuentes multiactivo verificadas. Esta tarea evalúa investigación y no inspecciona ni modifica el live.

## Entregables
Fuentes y auditoría de cambios, registro de28sesiones con estado y links, cuatro análisis completos, tablas de riesgo/retorno/estrés y datos mensuales/anuales persistentes. Cero datos2026, cero cambios operativos. No afirmar que ya queda elegido un nuevo riesgo antes de la validación.
