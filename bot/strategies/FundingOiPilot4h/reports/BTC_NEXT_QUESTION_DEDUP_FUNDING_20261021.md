# Descarte previo de posible pregunta: carry funding BTC

No constituye U ni corrida nueva. Revisión sólo lectura de fuentes y decisiones por btc_next_material;0jobs/0datosobservados/0estrategias. Se conserva para evitar repetir trabajo.

ResearchV5Base4h/funding_features.py YA define Persistent carry state:3pagos publicados negativos→long,positivos→short,available_at<=now,secuencia8h,freshness8h+1s,precioSMA120/retorno30alineado,salida funding_adverse porúltimopago. ResearchV5FundingFPReplay4h sinOI:[replay](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4),107trades,CAGR−1.043844%,PF.960575,net−207.96,fundingfavorable+167.58. FINAL_DECISION_V5 cierra nominal,costos,vecinos y40slots.

FundingWfPilotFiltered4h comparó breakoutprecio con/sinveto fundingadversoextremo(últimopagovs30previos),OI_PILOT_RESULTS_20261020 cierrarescatesporumbral. ResearchV4FundingFP1h/funding_features.py fundingextremonormalizado+confirmaciónprecio:[sesión](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068),26trades,−6.93%,PF.590;FINAL_DECISION_V4shortlistvacía. A_EVENTpostpagofallo454trades,CAGR−7.57%con fundingfavorable ya cerradoBTC_DISCOVERY_AB_FINAL_20261021.

Decisiónroot: no nuevo experimento de carrydireccional,filtroveto oclockpostpago;quitarfiltroprecio,cambiarcantidadpagos/signo sería vecino de líneas cerradas. No tocarlabelsSfunding nirescatarsulínea. Conteoseconómicossincambios.
