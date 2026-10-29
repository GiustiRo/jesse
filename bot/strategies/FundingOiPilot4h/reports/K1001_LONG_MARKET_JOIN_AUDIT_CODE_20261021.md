# Unión mecánica prevista MARKET

Se aplicará a un único snapshot MARKET exportado, con logs/pagos completos por MCP. Reutiliza los controles contables ya auditados. Usa las nuevas filas MARKET_SUMMARY/SOURCE/COHORT completas para ensamblar la vista de ledger, sin leer o inferir el sufijo de oldownSTATS. Son unión de filas nativas, no nuevas observaciones independientes.

Añade prueba de todas las órdenes de entrada MARKET en señal/opened_at, precioigualdecision/requested,qty/risk/D y extensión originalH<close<=H+.5D(1ATR). No deriva el tipo desde order_kind. Prefijos,fallos yrawlogs siguen preservados; no másmotores si fallanchecks.

```javascript
function auditQuota(name,summary,rows,logPages,fundPages) {
 const fail=m=>{throw Error(name+": "+m);};
 const near=(a,b,m,tol=1e-6)=>{if(!Number.isFinite(a)||!Number.isFinite(b)||Math.abs(a-b)>=tol)fail(m+" "+a+" vs "+b);};
 const sum=a=>a.reduce((x,y)=>x+y,0);
 const unique=(a,key,m)=>{const map=new Map();for(const x of a){const k=key(x);if(map.has(k))fail(m+" duplicate "+k);map.set(k,x);}return map;};
 const parse=label=>[...logPages].reverse().flatMap(p=>p.items).flatMap(line=>{const i=line.indexOf(label+" ");if(i<0)return []; const text=line.slice(i+label.length+1); if(text.endsWith(" [line cut]")) { if(label!=="K1001_QUOTA_STATS")fail("critical truncated "+label);const cut=text.indexOf(',"close_years":');if(cut<0)fail("cannot isolate complete stats prefix");return [Object.assign(JSON.parse(text.slice(0,cut)+"}"),{raw_stats_line_partial:true,missing_fields:["close_years","trace_errors","open_trace"]})];}return [JSON.parse(text)];});
 const opens=parse("R16_LEGACY_OPEN"),closes=parse("R16_LEGACY_CLOSE"),traces=parse("K1001_QUOTA_PRICE_TRACE"),plans=parse("K1001_QUOTA_PLAN");
 const marketSummaries=parse("K1001_MARKET_SUMMARY"),marketSources=parse("K1001_MARKET_SOURCE"),marketCohorts=parse("K1001_MARKET_COHORT");
 if(!marketSummaries.length)fail("missing bounded market summary");
 const ownStats=marketSummaries.map(s=>{
   const sources={},open_years={},close_years={};
   const sourceRows=marketSources.filter(x=>x.stage===s.stage);
   if(sourceRows.length!==3)fail("bounded source row count");
   for(const x of sourceRows){const {stage,origin,...row}=x;if(sources[origin])fail("duplicate bounded source");sources[origin]=row;}
   for(const x of marketCohorts.filter(x=>x.stage===s.stage)){const {stage,axis,year,origin,...row}=x;if(!["open_years","close_years"].includes(axis))fail("cohort axis");const table=axis==="open_years"?open_years:close_years;table[year] ||= {};if(table[year][origin])fail("duplicate bounded cohort");table[year][origin]=row;}
   if(s.policy!=="MARKET_AT_DECISION_CLOSE")fail("market policy label");
   return {...s,sources,open_years,close_years,raw_bounded_market_rows:true};
 });
 const legacyStats=parse("R16_LEGACY_STATS"),r11all=parse("R11_SUMMARY"),monthsAll=parse("R11_MONTH");
 const stage=r11all.some(x=>x.stage==="FINAL")?"FINAL":"PRETERMINAL";
 const latest=(xs,m)=>{const matches=xs.filter(x=>x.stage===stage);if(matches.length!==1)fail(m+" stage count "+matches.length);return matches[0];};
 const own=latest(ownStats,"ownstats"),legacy=latest(legacyStats,"legacy"),r11=latest(r11all,"r11");
 if(summary.session_status!=="finished")fail("session not finished");
 const m=summary.metrics,N=rows.length;
 const traceErrorRows=parse("K1001_QUOTA_TRACE_ERROR");
 if(m.total_open_trades!==0||own.open_trace||Object.keys(own.trace_errors||{}).length||traceErrorRows.length)fail("open/tracing errors");
 if(!own.raw_stats_line_partial && (!("trace_errors" in own)||!("open_trace" in own)))fail("unexplained missing stats fields");
 if(opens.length!==N||closes.length!==N||traces.length!==N)fail("fill/close/trace coverage");
 if(r11.minute_marks!==2741760||r11.invalid_windows!==0)fail("M1 coverage/history");
 near(r11.equity,m.finishing_balance,"observer terminal");
 const byOpen=unique(opens,x=>x.opened_at,"opening"),byTrace=unique(traces,x=>x.trade_id,"trace"),byClose=unique(closes,x=>x.time+"|"+x.origin,"close");
 const payments=fundPages.flatMap(p=>p.items);
 unique(payments,x=>x.trade_id+"|"+x.settled_at,"funding");
 if(payments.length!==m.funding.event_count)fail("payment count");
 const byId=unique(rows,x=>x.trade_id,"trade");
 const fundingById=new Map();
 for(const p of payments){const t=byId.get(p.trade_id);if(!t)fail("orphan funding");if(p.symbol!=="BTC-USDT")fail("fund symbol");near(p.qty,(t.side==="long"?1:-1)*t.qty,"fund qty");near(p.cashflow,-p.qty*p.mark_price*p.rate_decimal,"fund formula");fundingById.set(p.trade_id,(fundingById.get(p.trade_id)||0)+p.cashflow);}
 near(sum(payments.map(p=>p.cashflow)),m.funding.cashflow,"fund metric");
 let missingVerified=0;
 for(const t of rows){
  const o=byOpen.get(t.opened_at),tr=byTrace.get(t.trade_id);
  if(!o||!tr)fail("missing exact open or trace");
  if((name==="LONG_ONLY"&&o.origin!=="LONG_RUNNER")||(name==="SHORT_BOOK"&&!["CORE_SHORT","SUPPLEMENT"].includes(o.origin)))fail("forbidden origin");
  if(tr.origin!==o.origin||tr.signal_at!==o.signal_at||tr.opened_at!==t.opened_at||tr.closed_at!==t.closed_at)fail("trace identity");
  near(o.actual_entry,t.entry,"open entry");near(o.qty,t.qty,"open qty",1e-8);
  near(tr.entry,t.entry,"trace entry");near(tr.exit,t.exit,"trace exit");near(tr.qty,t.qty,"trace qty",1e-8);near(tr.distance,o.distance,"trace D");
  near(tr.net,t.net,"trace net");
  const c=byClose.get(t.closed_at+"|"+o.origin);if(!c)fail("missing close");near(c.net,t.net,"close net");
  const out=t.orders.find(x=>String(x.id)===tr.exit_order_id);if(!out||out.status!=="EXECUTED"||!out.reduce_only)fail("exit order missing/not executed reduce");
  near(out.price,t.exit,"exit order price");near(Math.abs(out.qty),t.qty,"exit order qty",1e-8);
  if(!tr.trace_complete||tr.first_at!==t.opened_at||tr.last_at!==t.closed_at||tr.last_stage!=="exit"||tr.marks!==2+tr.m1_marks)fail("trace shape");
  const r=(t.side==="long"?1:-1)*(t.exit-t.entry)/tr.distance;
  if(tr.min_r>1e-10||tr.max_r< -1e-10||r<tr.min_r-1e-9||r>tr.max_r+1e-9)fail("R extrema bounds");
  for(const key of ["min","max"]){if(tr[key+"_at"]<t.opened_at||tr[key+"_at"]>t.closed_at)fail("extreme time");if(tr[key+"_stage"]==="pre"&&tr[key+"_at"]<=t.opened_at)fail("pre at fill");}
  const f=fundingById.get(t.trade_id)||0;if(t.funding_present)near(t.funding,f,"trade funding");else{if(fundingById.has(t.trade_id))fail("missing field had payments");missingVerified++;}
  near(t.gross-t.fee+f,t.net,"trade gross-fee+fund");
  t.origin=o.origin;t.opening_log=o;t.price_trace=tr;t.funding_verified=f;t.R_price_exit=r;t.R_net=t.net/(t.qty*tr.distance);t.R_fee=t.fee/(t.qty*tr.distance);t.R_funding=f/(t.qty*tr.distance);t.giveback_observed_R=tr.max_r-r;
 }
 const marketPlans=parse("K1001_MARKET_PLAN");
 if(marketPlans.length!==N||plans.length!==N||legacy.cancellations!==0)fail("market plan/fill/cancel counts");
 const marketByTime=unique(marketPlans,x=>x.time,"market plan");
 for(const t of rows){
   const p=marketByTime.get(t.opened_at);
   if(!p||p.entry_policy!=="MARKET_AT_DECISION_CLOSE"||t.opening_log.signal_at!==t.opened_at)fail("market at decision timestamp");
   near(p.decision_price,t.entry,"market decision actual fill",1e-7);
   near(p.requested_entry,t.entry,"market requested actual fill",1e-7);
   near(p.original_distance,t.opening_log.distance,"market original D");
   near(p.qty,t.qty,"market qty",1e-8);near(p.risk_budget,t.opening_log.risk_budget,"market budget");
   if(!(p.original_trigger_level>0&&p.decision_price>p.original_trigger_level&&p.decision_price<=p.original_trigger_level+.5*p.original_distance+1e-7))fail("original K extension bound");
   const entries=t.orders.filter(o=>o.status==="EXECUTED"&&!o.reduce_only);
   if(entries.length!==1||entries[0].type!=="MARKET"||entries[0].side!=="buy"||entries[0].created_at!==t.opened_at||entries[0].executed_at!==t.opened_at)fail("actual entry order market/time");
 }
 const sources={};
 for(const origin of ["LONG_RUNNER","CORE_SHORT","SUPPLEMENT"]){
  const rr=rows.filter(t=>t.origin===origin),ownrow=own.sources[origin],oldrow=legacy.sources[origin];
  if(ownrow.fills!==rr.length||ownrow.closes!==rr.length||ownrow.trace_completed!==rr.length||ownrow.trace_missing!==0||oldrow.fills!==rr.length||oldrow.closes!==rr.length)fail("ledger source counts "+origin);
  near(ownrow.net,sum(rr.map(t=>t.net)),"own net "+origin);near(oldrow.net,ownrow.net,"parent net "+origin);
  const losses=-sum(rr.filter(t=>t.net<0).map(t=>t.net)),wins=sum(rr.filter(t=>t.net>0).map(t=>t.net));
  const quant=(a,p)=>{if(!a.length)return null;const sorted=[...a].sort((a,b)=>a-b),j=(sorted.length-1)*p,k=Math.floor(j);return sorted[k]+(sorted[Math.min(k+1,sorted.length-1)]-sorted[k])*(j-k);};
  const distribution=key=>({min:quant(rr.map(t=>t[key]),0),q25:quant(rr.map(t=>t[key]),.25),median:quant(rr.map(t=>t[key]),.5),q75:quant(rr.map(t=>t[key]),.75),max:quant(rr.map(t=>t[key]),1)});
  sources[origin]={N:rr.length,net:ownrow.net,pf:losses?wins/losses:null,mean_net_R:rr.length?sum(rr.map(t=>t.R_net))/rr.length:null,net_R:distribution("R_net"),favorable_mark_trades:rr.filter(t=>t.price_trace.max_r>0).length,giveback:distribution("giveback_observed_R"),observed_max_R:quant(rr.map(t=>t.price_trace.max_r),.5)};
 }
 const derivedCloseYears={},derivedOpenYears={};
 for(const t of rows){const oy=String(new Date(t.opened_at).getUTCFullYear()),cy=String(new Date(t.closed_at).getUTCFullYear());for(const [table,year,isOpen] of [[derivedOpenYears,oy,true],[derivedCloseYears,cy,false]]){table[year] ||= {};table[year][t.origin] ||= {fills:0,closes:0,net:0,trace_completed:0,trace_missing:0};const r=table[year][t.origin];if(isOpen)r.fills++;r.closes++;r.net+=t.net;r.trace_completed++;}}
 for(const [year,origins] of Object.entries(derivedOpenYears))for(const [origin,r] of Object.entries(origins)){const actual=own.open_years?.[year]?.[origin];if(!actual||actual.fills!==r.fills||actual.closes!==r.closes||actual.trace_completed!==r.trace_completed||actual.trace_missing!==0)fail("open-year ledger");near(actual.net,r.net,"open-year net");}
 if(!own.raw_stats_line_partial)for(const [year,origins] of Object.entries(derivedCloseYears))for(const [origin,r] of Object.entries(origins)){const actual=own.close_years?.[year]?.[origin];if(!actual||actual.closes!==r.closes||actual.trace_completed!==r.trace_completed||actual.trace_missing!==0)fail("close-year ledger");near(actual.net,r.net,"close-year net");}
 for(const p of plans){near(p.capital_scaled,.5*p.capital_total,"halfcapital");near(p.margin_scaled,.5*p.margin_total,"halfmargin");near(p.risk_budget,.01*p.capital_total,"risk total");if(p.planned_loss>p.risk_budget+1e-6)fail("plan risk");}
 if(plans.length!==legacy.fills+legacy.cancellations||legacy.fills!==N||legacy.closes!==N)fail("plans/fills/cancel reconciliation");
 const months=monthsAll.filter(x=>x.stage===stage);unique(months,x=>x.month,"month");months.sort((a,b)=>a.start-b.start);
 if(months.length!==63||months.filter(x=>x.complete).length!==62)fail("month coverage");
 near(sum(months.map(x=>x.pnl)),m.net_profit,"month net");
 const complete=months.filter(x=>x.complete),active=complete.filter(x=>x.active),positiveActive=active.filter(x=>x.pnl>0).length;
 if(positiveActive!==r11.positive_active||active.length!==r11.active_months)fail("monthly active summary");
 const quarters=new Map();for(const x of complete){const k=x.month.slice(0,4)+"Q"+(Math.floor((Number(x.month.slice(5))-1)/3)+1);if(!quarters.has(k))quarters.set(k,[]);quarters.get(k).push(x);}
 const fullQs=[...quarters.values()].filter(x=>x.length===3),posQs=fullQs.filter(x=>sum(x.map(y=>y.pnl))>0).length;
 if(fullQs.length!==20||r11.positive_quarters!==posQs)fail("quarter summary");
 const returns=complete.map(x=>x.return_fraction).sort((a,b)=>a-b);near((returns[30]+returns[31])/2,r11.median_return,"monthly median",1e-12);
 const best=[...months].sort((a,b)=>b.pnl-a.pnl).slice(0,2);near(sum(months.map(x=>x.pnl))-sum(best.map(x=>x.pnl)),r11.pnl_without_best_two,"top2 arithmetic");
 const annual={};for(let y=2021;y<=2025;y++){const yr=complete.filter(x=>x.month.startsWith(String(y)));if(yr.length!==12)fail("annual month coverage");annual[y]=100*(yr.reduce((v,x)=>v*(1+x.return_fraction),1)-1);}
 const rolling=[];for(let j=0;j+12<=complete.length;j++){const part=complete.slice(j,j+12);rolling.push({start:part[0].month,finish:part[11].month,return_pct:100*(part.reduce((v,x)=>v*(1+x.return_fraction),1)-1)});}
 const cagr=100*((m.finishing_balance/10000)**(365/1904)-1);
 const losses=-sum(rows.filter(t=>t.net<0).map(t=>t.net)),pf=sum(rows.filter(t=>t.net>0).map(t=>t.net))/losses;
 near(sum(rows.map(t=>t.net)),m.net_profit,"all net");near(m.finishing_balance-10000,m.net_profit,"final cash");
 const gates={CAGR30:cagr>=30,PF1_2:pf>=1.2,DD25:-r11.dd_m1_events<=.25,M65:active.length>0&&positiveActive/active.length>=.65,Q80:posQs/20>=.8,median_positive:r11.median_return>0,without_best_two_positive:r11.pnl_without_best_two>0,N100:N>=100};
 return {status:"FULL_ACCOUNTING_AND_TRACE_INVARIANTS_PASS",name,session_id:summary.session_id,dashboard_url:summary.dashboard_url,N,net:m.net_profit,finish:m.finishing_balance,cagr_pct:cagr,pf,dd_m1_events_pct:-100*r11.dd_m1_events,active_months:active.length,positive_active:positiveActive,positive_active_pct:100*positiveActive/active.length,positive_quarters:posQs,complete_quarters:20,median_calendar_month_pct:100*r11.median_return,pnl_without_best_two:r11.pnl_without_best_two,funding:m.funding,market_policy:"MARKET_AT_DECISION_CLOSE",native_market_entries_verified:N,bounded_terminal_market_rows_verified:true,missing_fields_zero_verified:missingVerified,raw_own_stats_partial:!!own.raw_stats_line_partial,terminal_trace_fields_inferred_if_partial:own.raw_stats_line_partial?{trace_errors_zero_from_no_first_error_logs:true,open_trace_false_from_full_closed_trade_trace_coverage_and_open_count_zero:true}:null,derivedCloseYears,derivedOpenYears,sources,annual_pct:annual,rolling12:rolling,gates,economic_all_gates:Object.values(gates).every(Boolean),months,r11,own,legacy,plans,records:rows,limits:["Two alternative scenarios, not joint capital.","Observed M1+fill extrema, not intraminute MFE/MAE.","N100 is operational preliminary, not power.","Adaptive development and reused history."]};
}
```
