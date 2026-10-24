# K1001 — unión y descriptivos V2: clasificación de salidas

Corrección antes de publicar resultados: submitted_via no identifica por sí solo si se tocó un target/stop. Fuente framework Strategy.liquidate líneas1724–1734 cierra MARKET asignando take_profit si PnLabierto>0 ystop_loss en caso contrario. Primera clasificación deJOINv1 podía llamar TP/SL a timeouts. V2 usa tipoMARKET primero y exige closed_at=primercallback4h≥opened_at+72hCORE/48hSUPPLEMENT, created_at=closed_at; otroMARKETnoexplicado bloquea, no se adivina por PnL. LIMIT/STOP con submitted_via correspondiente clasifican barreras. Un STOP puede ocurrir entre plazo nominal y callback4h; no llamar timeout por duraciónsola. No cambia filas,identidades,PNL/R,fuentesestrategia oanymotor. v1 preservada. Fuente exacta corregida:

```javascript
function(records,opens,closes,funding){
  const finite=x=>typeof x==="number"&&Number.isFinite(x);
  const check=(ok,message)=>{if(!ok)throw Error(message);};
  const sum=xs=>xs.reduce((a,x)=>a+x,0);
  check(records.length===192&&opens.length===192&&closes.length===192&&funding.length===1151,"complete universes");
  check(new Set(records.map(r=>r.trade_id)).size===192,"unique trade IDs");
  const O=new Map(),C=new Map();
  for(const x of opens){check(!O.has(x.opened_at),"duplicate open");O.set(x.opened_at,x);}
  for(const x of closes){check(!C.has(x.time),"duplicate close");C.set(x.time,x);}
  const fundById=new Map();
  for(const f of funding){check(finite(f.cashflow),"funding finite");const a=fundById.get(f.trade_id)||[];a.push(f);fundById.set(f.trade_id,a);}
  const ids=new Set(records.map(r=>r.trade_id));check(funding.every(f=>ids.has(f.trade_id)),"orphan funding");
  const joined=records.map(r=>{
    const o=O.get(r.opened_at),c=C.get(r.closed_at);
    check(o&&c,"missing identity log");
    check((o.origin==="LONG_RUNNER"?"long":"short")===r.side,"side mismatch");
    check(Math.abs(o.qty-r.qty_abs)<1e-8&&Math.abs(o.actual_entry-r.entry_price)<1e-6,"quantity/entry mismatch");
    check(o.origin===c.origin&&Math.abs(c.net-r.net)<1e-6,"closing identity/net mismatch");
    const payments=fundById.get(r.trade_id)||[],fund=sum(payments.map(x=>x.cashflow));
    check(payments.every(p=>p.effective_at>=r.opened_at&&p.effective_at<=r.closed_at),"payment outside actual holding interval");
    if(r.funding_present)check(Math.abs(r.funding-fund)<1e-6,"funding field vs complete ledger");
    else check(payments.length===0,"missing field has actual payments");
    check(Math.abs(r.gross_price-r.fee+fund-r.net)<1e-6,"trade ledger");
    const d=Math.abs(r.entry_price-o.stop),q=r.qty_abs;
    check(d>0&&Math.abs(d-o.distance)<1e-6,"initial distance");
    const priceRisk=q*d,stopFees=q*(d+.00045*(r.entry_price+o.stop));
    check(Math.abs(o.actual_loss-(stopFees+o.reserve*q*r.entry_price))<1e-6,"sizing risk definition");
    const exits=r.exported_orders.filter(x=>x.reduce_only===true&&x.status==="EXECUTED"&&x.executed_at===r.closed_at);
    check(exits.length===1,"unique executed exit");
    const e=exits[0];
    let exitClass;
    if(e.type==="MARKET"){
      const hours=o.origin==="CORE_SHORT"?72:o.origin==="SUPPLEMENT"?48:null;
      const deadline=hours===null?null:Math.ceil((r.opened_at+hours*3600000)/14400000)*14400000;
      // liquidate routes profitable/unprofitable MARKET exits through take-profit/
      // stop-loss labels. Type and the actual scheduled callback identify timeout.
      check(hours!==null&&r.closed_at===deadline&&e.created_at===r.closed_at,"unexplained MARKET exit");
      exitClass="TIMEOUT_MARKET";
    }else if(e.submitted_via==="take-profit"&&e.type==="LIMIT")exitClass="TAKE_PROFIT_LIMIT";
    else if(e.submitted_via==="stop-loss"&&e.type==="STOP")exitClass=o.origin==="LONG_RUNNER"?"LONG_STOP_INITIAL_OR_TRAILED":"SHORT_STOP";
    else exitClass="OTHER_EXECUTED_EXIT";
    return {...r,origin:o.origin,origin_status:"UNIQUE_REAL_EXECUTION_LOG_JOIN",opening_log:o,closing_log:c,
      funding_verified:fund,funding_verified_from_complete_ledger:true,
      missing_funding_zero_verified:!r.funding_present&&payments.length===0,funding_payment_count:payments.length,
      initial_price_risk:priceRisk,initial_stop_fees_risk:stopFees,
      net_R_price:r.net/priceRisk,gross_R_price:r.gross_price/priceRisk,fee_R_price:r.fee/priceRisk,
      funding_R_price:fund/priceRisk,net_R_sizing:r.net/o.actual_loss,net_R_budget:r.net/o.risk_budget,
      initial_target_R:o.target===null?null:Math.abs(o.target-r.entry_price)/d,exit_class:exitClass};
  }).sort((a,b)=>a.opened_at-b.opened_at);
  for(let i=1;i<joined.length;i++)check(joined[i].opened_at>=joined[i-1].closed_at,"unexpected native overlap");
  const median=xs=>{if(!xs.length)return null;const s=[...xs].sort((a,b)=>a-b),m=Math.floor(s.length/2);return s.length%2?s[m]:(s[m-1]+s[m])/2;};
  const stats=xs=>({N:xs.length,mean:xs.length?sum(xs)/xs.length:null,median:median(xs),min:xs.length?Math.min(...xs):null,max:xs.length?Math.max(...xs):null});
  const group=rs=>{
    const positive=rs.filter(r=>r.net>0),negative=rs.filter(r=>r.net<0);
    const n=sum(rs.map(r=>r.net)),best=[...rs].sort((a,b)=>b.net-a.net);
    const pp=sum(positive.map(r=>r.net)),ll=-sum(negative.map(r=>r.net));
    const Rpos=sum(rs.filter(r=>r.net_R_price>0).map(r=>r.net_R_price)),Rneg=-sum(rs.filter(r=>r.net_R_price<0).map(r=>r.net_R_price));
    const exitTypes={};for(const r of rs)exitTypes[r.exit_class]=(exitTypes[r.exit_class]||0)+1;
    return {N:rs.length,net:n,gross:sum(rs.map(r=>r.gross_price)),fee:sum(rs.map(r=>r.fee)),
      funding:sum(rs.map(r=>r.funding_verified)),positive:positive.length,negative:negative.length,
      win_fraction:rs.length?positive.length/rs.length:null,pf_dollar:ll?pp/ll:null,
      pf_price_R:Rneg?Rpos/Rneg:null,net_R_price:stats(rs.map(r=>r.net_R_price)),
      gross_R_price:stats(rs.map(r=>r.gross_R_price)),fee_R_price:stats(rs.map(r=>r.fee_R_price)),
      funding_R_price:stats(rs.map(r=>r.funding_R_price)),net_R_budget:stats(rs.map(r=>r.net_R_budget)),
      winner_R_price:stats(positive.map(r=>r.net_R_price)),loser_R_price:stats(negative.map(r=>r.net_R_price)),
      holding_hours:stats(rs.map(r=>r.holding_period/3600)),total_holding_hours:sum(rs.map(r=>r.holding_period/3600)),
      requested_to_fill_minutes:stats(rs.map(r=>(r.opened_at-r.opening_log.signal_at)/60000)),
      target_R_price:stats(rs.map(r=>r.initial_target_R).filter(finite)),margin_limited_fills:rs.filter(r=>r.opening_log.margin_limited).length,
      exit_classes:exitTypes,net_without_best_1:n-sum(best.slice(0,1).map(r=>r.net)),
      net_without_best_3:n-sum(best.slice(0,3).map(r=>r.net)),
      net_without_best_5:n-sum(best.slice(0,5).map(r=>r.net)),
      top_trades:best.slice(0,5).map(r=>({trade_id:r.trade_id,entry:r.opened_at,close:r.closed_at,net:r.net,R:r.net_R_price}))};
  };
  const origins=["LONG_RUNNER","CORE_SHORT","SUPPLEMENT"];
  const byOrigin={};for(const o of origins)byOrigin[o]=group(joined.filter(r=>r.origin===o));
  const targetN={LONG_RUNNER:31,CORE_SHORT:116,SUPPLEMENT:45};
  const targetNet={LONG_RUNNER:10650.419092195123,CORE_SHORT:4686.29849188876,SUPPLEMENT:9191.971406577974};
  for(const o of origins)check(byOrigin[o].N===targetN[o]&&Math.abs(byOrigin[o].net-targetNet[o])<1e-6,"origin ledger mismatch");
  const cohorts={entry:{},close:{}};
  for(const [axis,key]of [["entry","entry_year_utc"],["close","close_year_utc"]]){
    for(let year=2020;year<=2025;year++){const rs=joined.filter(r=>r[key]===year);cohorts[axis][year]={ALL:group(rs)};
      for(const o of origins)cohorts[axis][year][o]=group(rs.filter(r=>r.origin===o));}
  }
  const START=1602720000000,FINISH=1767225600000;
  const exposure={};
  for(let year=2020;year<=2025;year++){
    const start=Math.max(START,Date.UTC(year,0,1)),finish=Math.min(FINISH,Date.UTC(year+1,0,1));
    const rows={};
    for(const o of ["ALL",...origins]){
      const held=sum(joined.filter(r=>o==="ALL"||r.origin===o).map(r=>Math.max(0,Math.min(r.closed_at,finish)-Math.max(r.opened_at,start))))/3600000;
      rows[o]={hours:held,fraction_of_window:held/((finish-start)/3600000)};
    }
    exposure[year]={partial:year===2020,window_hours:(finish-start)/3600000,...rows};
  }
  return {status:"COMPLETE_UNIQUE_ATTRIBUTION_NOT_STANDALONE",join_N:joined.length,unattributed:0,byOrigin,cohorts,exposure,
    overall:group(joined),funding_payments:funding.length,missing_fields_zero_verified:joined.filter(r=>r.missing_funding_zero_verified).length,
    total_net:sum(joined.map(r=>r.net)),total_funding:sum(joined.map(r=>r.funding_verified)),records:joined,
    limits:"Cohorts by entry/close are attribution of realized trades, not MTM annual component returns. Initial-price R excludes fees/reserve in denominator but net numerator includes fees/funding. No standalone CAGR/DD or counterfactual signals."};
}
```
