# V5 — auditoría smoke VWAP

[Sesión](http://localhost:9200/#/backtest/996568bc-0c12-4db0-9f7e-4235556b57ab), finished/errornull,1h[2020-09-01,2020-09-08),config nominal exacta. Revisión técnica PASS;contabilidad completa de snapshots corresponde a root.

168decisiones,56checkssectoriales+61comunesruntimepassed. Logs completos48líneas. Tres entradas MARKET y tres cierres reales: doslong/oneshort; dos STOP loss y una normalizaciónVWAP corta MARKET17hdespués delfill. Entries=trades=closes=3 ysinforced/openresidual. Particiones primary/features/dirección, cuotaUTC, bounds, ATR14offset0,stop2A/targetNone,riskcap yplanes/fills concilian.

Los tres reingresos satisfacen exactamente las desigualdades de banda/centro/corrección usando sus contextos registrados: ventanas25cerradas, actual/previa propias yescala=max(σ,A). Salida corta C11897.39<=Mactual11910.908749 sóloT>opened_at, ventana24propia; el Mentrada era11734.582870, por lo que se ejerció realmente el centro dinámico. SinTP fijo ni fillretroactivo alVWAP. El campo submitted_via de la orden MARKET figura take-profit porconvenciónmotor;request yV5_CLOSE preservan vwap_normalization.

As-of funding/OI válido en relojes registrados; PV permitió una entrada conOIinitialization yotraOInonrising como corresponde. FundingON21settlements/3cashflows ynetcashflow+7.307522USDT,conproxy. Elúltimolong perdió198.313078 sobrepresupuesto197.594287:exceso0.718791 explicado porfunding−0.718793 fuera delpresupuesto stop+fees,conredondeo. No cambióprotección niameritareparacióneconómica.

Cobertura noejercida: hold24h,calendar_boundary,fold_end,normalizaciónVWAPlong,filtroOIencendido ydatoinválido real deVWAP. Checksdeterministas cubren superficies; no seatribuyefillreal aesasramas. Las ventanasOHLCVsubyacentes no se reconstruyeron aquí;hashesyfuentesestáticas validanconstrucción,desigualdadesverificadasdesdeloscontextos.

Root inicióelIDuna vez yrecuperólecturafinishedtrasHTTPtimeout,sinretry. Esteagente no creó drafts,nuevosmotores/jobs nicambiófuentes. Hubo un fallo local de persistencia al faltar variable de progreso enmemoria;seleyóelarchivoMCPexistente yseactualizó, sinrepetir sesión. Auditoríacompleta AUDIT_ResearchV5VwapSmoke1h.json yprogreso V5_VWAP_PROGRESS.json.
