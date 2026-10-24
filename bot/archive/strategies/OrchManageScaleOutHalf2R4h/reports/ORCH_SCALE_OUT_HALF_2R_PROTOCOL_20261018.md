# Protocolo previo — scale-out50% a2R con runner original
Fecha2026-10-18. ÚNICOcontrol propuesto OrchManageScaleOutHalf2R4h, sin variantes de porcentaje/R. Código y draft preparados con autorización del orquestador, sin ejecutar todavía; SLOT1 reservado para prueba técnica/económica. Guardado aquí como registro previo de línea, no cambia FixedR3.
## Hipótesis y falsación
Capturar media posición al alcanzar2R puede evitar posterior giveback sobre esa mitad, conservando cola tendencial sobre el resto. El mero reconocimiento de beneficio NO mejora mesMTM: la hipótesis exige trayectoria posterior mejor. Menor exposición puede perder tendencia, diversificación/capital pueden alterar siguientes señales. No se asume superior.
Comparar cartera con referencia congelada,65–70%mesesactivos/80%trimestres,DD<=25%,economía útil (20%CAGR orientación, no veto automático). Si no mejora regularidad conjunta o destruye expectativa/costes, descartar sin barrerporcentajes/R. Winrate51%noesmeta. Reportar tails, fee, contribución y concentración.
## Fuente y límites invariantes
Referencia MultiAssetRetestBtcShort4h,longBTC/PAXG/SPY,shortBTC. Cuenta10k,4h,5xaislado,fee0.00045todasórdenesinclLIMIT. Inicial3%trade/8%global,gross4.4x,margen90%,asignacióninversoATR,señalesLIMITretest/shortSTOP ycancelaciones sin cambios. Warmup240,normal replay,2020-10-15→2025-12-31exclusivo.2026reservado;sinlive/framework/config.
Dashboard referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Mecánica y API documentada
MCP jesse://strategy documenta (qty,price), on_reduced_position(order), reduced_count yreemplazo automático de STOP alreasignar. jesse://strategy_examples Ejemplo2TrendSwingTrader usa take_profitposition.qty/2 y on_reduced_position reasignandoSTOPposition.qty.
Longentryfillreal;stopinicialoriginalentry−initial_distance. TPúnicoentry+2*initial_distance,qty50%redondeadoabajoastepresearchoriginal(.001BTC/SPY,.0001PAXG);restanteexacto. Si redondeo resulta0, noTPparcial, conserva gestiónoriginal;documentarfrecuencia. Sin minimumquantityadicionalinventado.
Trailingoriginal se mantiene desdeinicio ydespués parcial: best_close/ATR/BE2.25R/tighten5R8R iguales. NO adelantarextraBEa2R, no nuevostops discrecionales.
on_reduced_position únicamentepara long reduceqtySTOPalqtyrestanteactual conservando mismoprecioaverage_stop_loss. Marcar parcial hecho yno rearmarTP. Nunca reescribir TPfillado enupdate;runner sinsegundoobjetivo. No tocarshort.
## Validación necesaria ANTES de interpretar performance
Docsnoexplicitanflush intrabar de cancel/replacedesdehook; prueba técnica autorizada incorpora aserciones en callbacks/after/on_close; auditorV4 verificará ejecuciones antes de interpretar MTM. Invariantes de qtyejecutada,restqty,stopqty ynooverclose. Sin salir porTPvariasveces.
AuditorV3rechazaparciales,porlotantoNOusarsusmeses. RootpreparaV4porórdenes yvalidación previaencontrolesconocidos. Calendario selladohasta reconciliarsaldo,fees yPNL. Ejecucionesregistradas, ningún VWAPfinalsustituye fecha deparciales.
Cashledger: cobrarentryfeealentrar; cadaexitrealizaq*(exit−entry)−exitfee; MTMqtyremanente*(mark−entry). Fee=sumabsqty*price*fee_porfill; no doblecobroentryfee. VWAPexitqtyponderadosólopara reconciliarClosedTrade. Si haygapusarpricefillreal, noTPteórico.
## Sesgos/pendientes
ProxySPYBID/SPX yPAXGspot,horariosnativos,slippage/colas,funding noresueltos;cantidadparcialredondeadaresearch no certificanativefilters. Una nuevahipótesis tras ver datos noesOOS.
