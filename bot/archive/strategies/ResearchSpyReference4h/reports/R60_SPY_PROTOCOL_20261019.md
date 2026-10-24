# R60 SPY — diez sensibilidades de una pieza

Protocolo previo a código/resultados. Exactamente10fulls SPY,20conPAXG. No diez ideas independientes ni optimización automática; vecinos fijados por usuario/root antes de resultados. No combinaciones ni selección del máximo. Baseline existente [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) no se vuelve a ejecutar.

| ID | Clase | Único cambio |
| --- | --- | --- |
| S01 | R60SpyGapMin10 | 0.10 < g <= 1.0 |
| S02 | R60SpyGapMin25 | 0.25 < g <= 1.0 |
| S03 | R60SpyGapMax50 | 0.0 < g <= 0.50 |
| S04 | R60SpyGapMax75 | 0.0 < g <= 0.75 |
| S05 | R60SpyN24 | donchian_len26→24 |
| S06 | R60SpyN28 | donchian_len26→28 |
| S07 | R60SpyAdx24 | adx_min26→24 |
| S08 | R60SpyAdx28 | adx_min26→28 |
| S09 | R60SpyFast16 | ema_fast20→16 |
| S10 | R60SpyFast24 | ema_fast20→24 |

Baseline: g=(self.price−priorDonchianHigh)/ATR,0<g<=1; Donchian26,ADXmín26,EMAfast20. Priorhigh excluye barra actual (c[-n-1:-1,3]); ATR14delhistorialfiltrado y quotecloseactual. Para S01..04 g sólo se calcula tras finitud y conATR>0, sin futura información; misma entrada al boundary. S05..10 sólo cambian defaultHP correspondiente; no rango ni gestión. No otra regla alterada.

Todas autocontenidas derivadas de AttrSpyCqFreshLimit. UTCMon-Fri00:00–20:00features y baropen00:00–16:00entry,SPY4h+M1,warm240. Mismas salidas BE2.25R/trail4.2ATR/tightening5R/8R,stop2ATR,sizing1%presupuestado10k,.00045porladoinclLIMIT,reserva.001sólosizing,isolated5x,gross4.4,margin90%,cartera8%,step.001,guardfreshentry y cancelación original. Stops/gestión fuera del horarioentry idénticos. No RTH/funding/datos/BTCaux/framework/live/Pi/scripts/install/restarts. ProxySPXCFDBID/10aceptado. Ventana2020-10-15→2025-12-31exclusiva;2026cerrado.

Fuentes/readback/diff revisados por root ANTES de lanzar; máximo2backtests propios y1análisis,4/2globales. Registrar las10 sesiones y fuentes en notes antesrun. Analizar snapshots completos: N/PnL/fees/PF/DDmotor/CAGR, exposición temporal/notional×tiempo a precioentry (noMTM), turnover, net/notional, costes estáticos+5/+10bpsRT mismosfills, exbest/ex3, cohortes cierre NOanualMTM. Root hace MTM. No inferir independencia ni escoger variante sólo por retorno máximo; mostrar todas y contrasteCq. Historia reutilizada, sin OOSlimpio. Cambiar umbral altera ocupación/entradas futuras: contraste de políticas, no efectoscausalespuros.

ArtefactosJSON compactos por bloque<50KB, guardar íntegros; no matrices de pares45innecesarias. Si haydatosfaltantes se conservan null/sinoperaciones; no métricasfabricadas. Ninguna nueva prueba después de estas10sincoordinación. Malosresultados/muestraspocas se conservan, sinrescate.