# SPY Structural R1 — protocolo BR definitivo previo a resultados

Sólo seis fulls BR01..BR06 de ronda1 autorizados; rondas2/3 NO autorizadas para ejecución ahora. Referencias Cq y M existentes, sin rerun. Propuesta SPY_BREAKOUT_PLAN_PROPOSAL_20261019.md y plan central preceden; este contrato incorpora precisiones root definitivas.

## Reglas comunes

Capital10 000, riesgo presupuestado1%, cartera8%, fee.00045 por lado incluyendoLIMIT, isolated5x, cap4.4, margin90%, reserva.001 sólo sizing y step.001. SPY4h+M1, warm240, debug/fastfalse, ventana2020-10-15→2025-12-31exclusiva;2026cerrado. EXACTO calendarioUTCMon-Fri00–20features/baropen00–16entry. Proxies aceptados, funding fuera. Mismos stop2ATR desde fill, BE2.25R, trail4.2/tightening5R/8R, gestión sin gate nuevo. Sólo MCP, sin instalaciones/scripts/framework/configglobal/restarts/PAXG/BTC/live/Pi.

Origen Cq es señal de PRECIO antes de sizing/capital/posición: history>=100, EMA20>EMA80actual>EMA80[-5], close>EMA80,ADX>=26,RSI52..76,high-low<=3ATR,ATR finito>0,priorDonchianHigh26<close<=L+ATR,0<2ATR<L, entrywindow y fresh M1T−60s con paridad. Comparadores existentes [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) y [M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07).

## Matriz

| ID / clase | Trigger / precio |
| --- | --- |
| BR01 / SpyStructR1BR01 | Reset alclose<=(maxHigh26previo+minLow26previo)/2. Censurado hasta primerreset observado. Contar señales origen Cq incluso ocupado; aceptar sólo ordinal1 deépoca. LIMIT enL con vigencia original1barra. |
| BR02 / SpyStructR1BR02 | Mismo estado; aceptar ordinal>=2. Misma LIMIT L y gestión. |
| BR03 / SpyStructR1BR03 | Origen congela L=priorhigh26/H=high de ruptura. Primer contacto observado posterior low<=L<=high yclose>L activa MARKET alcloseactual. |
| BR04 / SpyStructR1BR04 | Primercontacto real conclose<=L; primerclose FUTURO>L dentroepisodio activa MARKET. Si el primercontacto sostuvoL, receta no entra. |
| BR05 / SpyStructR1BR05 | MISMO holdBR03, comprar alhigh de su vela de retest: max(highretouch,priceactual), STOP previsto oMARKET si ya alcanzado. Caduca1barra. |
| BR06 / SpyStructR1BR06 | MISMO holdBR03, comprar alH de la ruptura original: max(H,priceactual), STOP previsto oMARKET si ya superado. Caduca1barra. |

BR03..06 comparten generador de episodios independiente de posiciones y sizing: sólo uno activo, no sobrescribir origen, vidaCUATRO observaciones4h FILTRADAS posteriores. Armado no es contacto. Incluso si trigger se consume/falla, episodio bloquea rearmado hasta expiry común; no rearmar en la misma barra de expiry. Gaps/fines de semana hacen que4observaciones no sean16h; no imputar datos.

Primera interacción conlow<=L perohigh<L es gap enteramente debajo: episodio queda inválido para triggers hastaexpiry, sin inventar contacto. Contacto real exige low<=L<=high. El high usado pertenece a barra YA cerrada; STOP se envía para futuro, nunca retrofill por high conocido. BR04 exige barra posterior al primercontacto, no reclaim retrospectivo.

BR01/02 resets y contador y BR03..06 episodios evolucionan en before aun ocupado. Trigger ocupado/sinregimen/quote/entrywindow se consume sin replay. Para entradas demoradas se exige régimen original EMA/ADX/RSI/rango y ATRválido actual, pero no una NUEVA rupturaDonchian; suL/H ya están congelados. Sizing y stop2ATR usan ATR de la decisión actual, medidos desde fill por on_openoriginal. Rechazo por sizing no rearmaevento.

Smart-order puede convertir precio cercano enMARKET (tolerancia1.5bps). BR05/06 nunca mandan entrada por debajo deprice que se convierta accidentalmenteLIMIT; max(anchor,priceactual). Tipos ejecutados se auditan, sin afirmar que todoSTOP previsto se ejecutó comoSTOP.

## Evaluación y persistencia

Máximo2backtests propios/4globales y1análisis propio/2globales. Fuentes autocontenidas/readbacks/diffs y revisión root ANTESrun; notas con fuente completa antesderun. Snapshots completos por run_analysis,6variantes+2refs=8inputs. ResúmenesJSON<50KB, detalles porfila/pareja, preservaríntegros. MétricasN/net/fees/PF/Sharpe/DD/CAGR, duración/exposicióntemporal ynotional×tiempo a precioentrada(noMTM),turnover/netnotional,stressestático5/10bpsRT,exbest/ex3,cohortes cierres NOretornosMTM,tiposórdenes/terminales. Root auditaMTM/snapshots.

No elegir máximo ni tratar pares/semillas como independientes; ocupación alteracartera. Escasez=>inconcluso y no cambiarvida/filtrosparaN. No asumirvars/counters exportados por snapshots ni añadirlogginghooks. Guardar todoslosresultados, incluidos ceros/malos. No sustituirreferencia ni combinar vecinos. Ninguna nueva corrida posterior aestas6 sincoordinación.
