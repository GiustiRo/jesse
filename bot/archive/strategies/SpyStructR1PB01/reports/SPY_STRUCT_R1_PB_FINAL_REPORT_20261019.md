# SPY estructura ronda1: resultados de correcciones PB

Fecha local19octubre2026. Completados exactamente6fulls nuevos, sin cambios tras resultados. Dos slots paralelos por agente; otros6BR pertenecen al especialista A y se consolidan por root. No rondas2/3.

**Ninguna PB demuestra mejora robusta de la referencia Cq.** B01/B02/B05 negativos; B03/B04/B06 positivos pero sólo16/7/19trades y todos negativos al retirar su mayor ganador. B06 mejora frente al comparador MARKET y aporta una pregunta concreta de confirmación de sweep, sin superar Cq en retorno/DD ni resolver selección.

## Contrato y auditoría

Referencia de ejecución AttrSpyMarket, fuentes autocontenidas SpyStructR1PB01..06 revisadas por root antes de correr, readback exacto6/6. Sólo reemplazar eventoDonchian y desplazamiento desde su frontera por los seis patrones congelados; régimenEMA20/80/pendiente/ADX26/RSI52–76/rango<=3ATR, ATR4h y gestiónBE2,25R/trail4,2 con tightening intactos. Distancia inicial2ATR calculada contra precio MARKET. No1h.

Ventana2020-10-15→2025-12-31exclusiva,2026cerrado,10k aislados/riesgo1%/fee0,00045porlado/isolated5x/cap4,4/reserva0,001sólosizing;4h+M1,warm240,fast/debugfalse. SPY UTCMonFri00–20historia y baropen00–16entradas. Quote M1exacta al último minuto, sinnuevofiltroenexits. Sin BTC/PAXG/riesgonuevo/funding/datos/framework/scripts/instalaciones/restarts/live/Pi.

Auditor job028bb8cbb6a5484ba89cca3b7abeb27f succeeded:8snapshots íntegros,163tradesPB+69referencias=232. Cantidades entrada/salida, precios, fees de cada fill, PNL, wallet, holding, ausencia de solapamientos y límites temporales conciliados. Detalles por fila guardados. B01/B02/B05/B06 y M tienen cierre MARKET forzado exactamente en END y contador de una posición capturado ANTES del cierre; gross coincide open_pl y balancefinal incluye fee de salida, sin posición residual afirmada por ese contador.

Dos intentos previos de análisis fallaron: ba69baadc7a347709d080ea74a551d31 por llave de print;7a144c17114544f5b2706150dd96fced por dashboard_url ausente del summary embebido. Reparaciones de presentación/metadata, sin tocar estrategias/fills/métricas. Historial y fuente final en ANALYSIS_SOURCE.

## Comparación económica

PF y neto después de fees. DD/Sharpe/CAGR del motor; exposición de tiempo sobre toda ventana. Cq y M existentes no cuentan como fulls nuevos. No sumar cuentas.

|Política|N|NetoUSDT|Fees|PF|Sharpe|DDmotor%|Tiempo%|Neto+10bpsRT|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|31|751.35|286.48|1.49|0.458|-5.21|15.26|433.04|
|[M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07)|38|151.60|336.73|1.07|0.106|-7.72|16.00|-222.54|
|[B01](http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6)|44|-575.41|401.75|0.78|-0.290|-13.10|16.13|-1021.81|
|[B02](http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983)|29|-1007.01|261.33|0.44|-0.744|-14.00|7.46|-1297.37|
|[B03](http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff)|16|387.31|154.92|1.52|0.326|-4.29|6.47|215.18|
|[B04](http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2)|7|181.97|74.83|1.53|0.214|-2.93|3.17|98.83|
|[B05](http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0)|48|-43.46|435.79|0.98|0.002|-7.77|19.72|-527.66|
|[B06](http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646)|19|571.75|190.93|1.51|0.418|-6.28|7.13|359.61|

## Qué enseñan los pares

- B01→B02: exigir recuperar máximo previo en giro tras dos rojas reduce neto431,60USDT; ambas negativas y DD cercano−13/−14%. No respalda añadir confirmación automáticamente.
- B03→B04: recuperar mother frente al techoinside reduce N16→7 y neto205,34. Ambas concentradas: exmejorB03−11,35 yB04−208,79. MenorDD con menos exposición no demuestra mejora superior.
- B05→B06: confirmar sweep superando highprevio aumenta neto615,21 y reduce N48→19. PeroB06 queda−38,52sinmayortrade, DD−6,28peorqueCq−5,21 y neto571,75menor751,35. Es una pista seleccionada, no candidata robusta.

Intersecciones de timestamp exacto de apertura:20,4,8trades por par, todas con mismo entryprice. El PNL normalizado de las intersecciones cambia muy poco; la diferencia global surge sobre todo de selección de oportunidades/ocupación posterior, no mejores precios en esos fills comunes. Intersección seleccionada, sin atribución causal sobre exposición idéntica.

Cq se denomina retest por su política, pero órdenes ejecutadas incluyen24LIMIT y7MARKET por clasificaciónautomática cercanía del motor. Las seis PB entraron siempre MARKET; M38MARKET. Nunca afirmar Cq31LIMITpuras.

## Costes, concentración y capital-tiempo

|Política|CAGRmotor%|Neto+5bpsRT|Netoexmejor|Netoex3mejores|Neto bps/entrynotional|Nocionalentrada-tiempo|
|---|---:|---:|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|1.40|592.19|349.58|-298.22|23.64|0.14149|
|[M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07)|0.29|-35.47|-224.73|-864.91|4.05|0.14467|
|[B01](http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6)|-1.13|-798.61|-1048.02|-1680.85|-12.89|0.15189|
|[B02](http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983)|-2.02|-1152.19|-1347.23|-1603.96|-34.64|0.06950|
|[B03](http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff)|0.73|301.25|-11.35|-451.83|22.54|0.06430|
|[B04](http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2)|0.35|140.40|-208.79|-346.41|21.92|0.03108|
|[B05](http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0)|-0.08|-285.56|-395.45|-996.61|-0.90|0.18360|
|[B06](http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646)|1.07|465.68|-38.52|-610.57|27.00|0.07979|

Stress estático:2,5/5bpsadicionales por lado sobre TODOS los fills, equivalente5/10bpsRT; conserva decisiones/cantidades, sin simular redimensionamiento. Reserva0,001del sizing no se descuenta como fillcoste adicional ya aplicado.
Nocionalentrada-tiempo=sum(entrynotional*holdinghours)/(10000*45672hours); usa precio de entrada, no nocionalMTM real. No equiparar menor tiempoexpuesto con mejor selectividad causal.

Las positivasB03/B04/B06 conservan beneficio con+10bps, pero eso no elimina selección histórica ni concentración. TodasPB negativas sin3mejores;Cq también−298,22sin3, por lo que esta exclusión es diagnóstico comparativo y no una regla para descartar todo payoff de tendencias.

## Cohortes por año de cierre, NO rentabilidadMTM

|Política|2020|2021|2022|2023|2024|2025|
|---|---:|---:|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|137.98|335.83|-215.41|395.76|-22.51|119.70|
|[M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07)|144.46|234.68|-412.95|325.25|-145.88|6.03|
|[B01](http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6)|97.02|424.26|-211.90|20.98|-281.71|-624.08|
|[B02](http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983)|-93.67|167.67|40.77|-561.27|-312.15|-248.36|
|[B03](http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff)|0.00|199.54|-99.98|126.78|-242.65|403.62|
|[B04](http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2)|0.00|-173.81|100.55|-85.50|-50.02|390.76|
|[B05](http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0)|168.79|253.87|-224.33|64.57|-78.85|-227.52|
|[B06](http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646)|0.00|499.26|-40.10|718.42|-358.14|-247.69|

Cero en cohorte sin cierres significa ausencia de trades cerrados ese año, no cero retornoMTM. B06 depende de2021/2023 y termina negativo en cohortes2024/2025. B03 debe más que su ganancia total a dos cierres2025;B04 a uno2025. Root calcula calendarioMTM aparte; no interpretar Portfolio00:01 como cierreUTCdiario.

## Cierre y evidencia

Se conserva referencia. No se decide combinación dePB/BR ni cartera a partir de esta tabla; no hay nueva rutaBTC o avance a operativa. No se autoriza otra ronda automáticamente. Si root evalúa profundizar sweepconfirmado, exigir contraste de confirmación y estabilidad predeclarado, con muestra/concentración como limitantes; no convertir19trades en evidencia por búsqueda de máximos.

Archivos en strategies/SpyStructR1PB01/reports/:
- SPY_STRUCT_R1_PB_FROZEN_PROTOCOL_20261019.md
- SPY_STRUCT_R1_PB_IMPLEMENTATION_REVIEW_20261019.md
- SPY_STRUCT_R1_PB_SESSION_MANIFEST_20261019.md
- SPY_STRUCT_R1_PB_ANALYSIS_SOURCE_20261019.md
- SPY_STRUCT_R1_PB_EXACT_RESULTS_20261019.md
- SPY_STRUCT_R1_PB_B01/B02/B03/B04/B05/B06/Cq/M_AUDIT_20261019.md (ocho archivos)

Ocho trayectorias económicas/fingerprints distintas; siguen siendo una misma historia de desarrollo ya usada, sin OOS limpio.2026intacto.

## Calendario MTM reconciliado por root

Root informó auditoría independiente jobb7ed075be282430e8ce8fd78bde752f6 succeeded/passed para las seis PB; no se ejecutó otra corrida económica. Reconstrucción a cierre diarioUTC, sin usar Portfolio00:01 como cierre.

|Política|DD diarioUTC%|Meses completos positivos/61|Trimestres completos positivos/19|
|---|---:|---:|---:|
|[PB03](http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff)|−4,6831|9|8|
|[PB04](http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2)|−2,9379|4|4|
|[PB06](http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646)|−6,27539|8|6|

El DD diario dePB03 difiere del motor−4,2914; reportar cada frecuencia por su nombre. Las menores exposiciones también reducen oportunidades de mesespositivos, no interpretar los conteos aislados como causalidad. Los bordes2020oct/2025dic no cuentan como meses completos;19trimestres completos. Tabla comunicada por root tras su análisis independiente; fuente MTM completa se conserva en la consolidación root.
