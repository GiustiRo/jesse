# K1001 — protocolo y código de atribución MTM mensual

Revisiónindependiente: K1001_MTM_ORIGIN_METHOD_CRITIQUE_20261021.md. Corrige límite preliminar de viabilidad: con única posición, wallet íntegro y equity total observado en cada frontera, se puede asignar el PnL abierto residual al único origen que está expuesto. No se requieren nuevas velas; no son trescuentasindependientes.

Se construyen64fronteras desde63R11_MONTHPRETERMINALdeKflatfinal. Ningúntrade abre/cierra enninguna frontera; esa condición se comprueba por código ybloquea si falla. Fee real=.00045*q*(entry+exit), error máximo observado1.42e−14. Wallet pororigen restaentryfee alopen ysumagross−exitfee alclose, añadefundingcompleto efectivo1151pagos. No restar margen,riesgo o reserva.001, que no soncashflows. Funding.py settle consume effective_at<=timestamp y aplica walletantes decisiones, backtest_mode1280–1289llamaantesstrategy._execute yR11pre;M1continuo yfastOFF, no catchupomitido. Publicationdelay condiciona información de señal, noel pago efectivo. FINISH esexclusivo yKyaflat, porloquesuPRETERMINALesfinal; no liquidaciónterminalposteriorenesta sesión.

Enfronteraflat, equity−wallet debe ser<1e−6. Conposiciónabiertaúnica, residual se asigna a su origen; no se publica como precio observado. ContribucionesMTM acumuladas pororigen deben sumar equity−10000 encadafrontera yterminar enledgers31/116/45. Mensuales son diferencias, susporcentajes usan equityTOTALinicio: no capitalficticio pororigen ni CAGRstandalone. Inactividad se determina por exposición/fills, nunca porPnL=0. Se reconcilian mensual/anual yterminal. Pequeño ruido enflat comprobado se trata0; inactivo exige|PnL|<1e−6 yse fija0 para evitar positivofantasma porflotante. Resto valores sinredondeo.

Código aejecutarenorquestador sobreartefactos/logs ya recuperados, no run_analysis nuevo, no datos embebidos enharness ni lecturas de proyecto/precios desdeanalysis:

```javascript
function(records,funding,months){
  const origins=["LONG_RUNNER","CORE_SHORT","SUPPLEMENT"];
  const sum=a=>a.reduce((s,x)=>s+x,0), check=(b,s)=>{if(!b)throw Error(s);};
  const rows=[...months].sort((a,b)=>a.start-b.start);
  check(rows.length>0&&rows.every((m,i)=>!i||m.start===rows[i-1].finish),"month continuity");
  const points=[{time:rows[0].start,equity:10000}];
  for(const m of rows)points.push({time:m.finish,equity:points.at(-1).equity+m.pnl});
  const boundaries=points.map(p=>{
    check(!records.some(r=>r.opened_at===p.time||r.closed_at===p.time),"fill at boundary needs explicit phase");
    const cash=Object.fromEntries(origins.map(o=>[o,0]));
    for(const r of records){
      const entryFee=.00045*r.qty_abs*r.entry_price;
      const exitFee=r.fee-entryFee;
      check(exitFee>=0&&Math.abs(r.fee-.00045*r.qty_abs*(r.entry_price+r.exit_price))<1e-6,"fee split");
      if(r.opened_at<p.time)cash[r.origin]-=entryFee;
      if(r.closed_at<p.time)cash[r.origin]+=r.gross_price-exitFee;
    }
    for(const f of funding)if(f.effective_at<=p.time){
      const r=records.find(r=>r.trade_id===f.trade_id);check(r,"orphan funding");
      cash[r.origin]+=f.cashflow;
    }
    const wallet=10000+sum(Object.values(cash));
    const open=records.filter(r=>r.opened_at<p.time&&r.closed_at>p.time);
    check(open.length<=1,"not a single-position book");
    const residual=p.equity-wallet;
    if(!open.length)check(Math.abs(residual)<1e-6,"flat boundary equity/wallet mismatch");
    const cumulative={...cash};
    if(open.length)cumulative[open[0].origin]+=residual;
    check(Math.abs(10000+sum(Object.values(cumulative))-p.equity)<1e-6,"boundary additive reconciliation");
    return {...p,wallet,open_origin:open[0]?.origin||null,unrealized_residual:open.length?residual:0,
      flat_residual_error:open.length?null:residual,cash_by_origin:cash,cumulative_contribution:cumulative};
  });
  const monthly=rows.map((m,i)=>{
    const a=boundaries[i],b=boundaries[i+1],components={};
    for(const o of origins){
      const active=records.some(r=>r.origin===o&&
        ((r.opened_at<m.finish&&r.closed_at>m.start)||(r.opened_at>=m.start&&r.opened_at<m.finish)));
      let pnl=b.cumulative_contribution[o]-a.cumulative_contribution[o];
      if(!active){check(Math.abs(pnl)<1e-6,"inactive component changed");pnl=0;}
      components[o]={pnl,contribution_fraction:pnl/a.equity,active};
    }
    const shortPnl=components.CORE_SHORT.pnl+components.SUPPLEMENT.pnl;
    components.SHORT_COMBINED={pnl:shortPnl,contribution_fraction:shortPnl/a.equity,
      active:components.CORE_SHORT.active||components.SUPPLEMENT.active};
    check(Math.abs(sum(origins.map(o=>components[o].pnl))-m.pnl)<1e-6,"monthly additive mismatch");
    return {...m,book_equity_start:a.equity,book_equity_finish:b.equity,components};
  });
  const median=a=>{if(!a.length)return null;const s=[...a].sort((x,y)=>x-y),n=s.length;return n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;};
  const complete=monthly.filter(m=>m.complete),summaries={};
  for(const o of [...origins,"SHORT_COMBINED"]){
    const active=complete.filter(m=>m.components[o].active);
    const values=complete.map(m=>m.components[o].contribution_fraction);
    const quarters=[];
    for(let y=2021;y<=2025;y++)for(let q=0;q<4;q++){
      const mm=complete.filter(m=>m.month.slice(0,4)===String(y)&&Math.floor((Number(m.month.slice(5))-1)/3)===q);
      if(mm.length===3)quarters.push({year:y,quarter:q+1,pnl:sum(mm.map(m=>m.components[o].pnl))});
    }
    summaries[o]={active_months:active.length,positive_active_months:active.filter(m=>m.components[o].pnl>0).length,
      positive_calendar_months:complete.filter(m=>m.components[o].pnl>0).length,
      calendar_months:complete.length,median_calendar_contribution_fraction:median(values),
      complete_quarters:quarters.length,positive_quarters:quarters.filter(q=>q.pnl>0).length,
      total_pnl:sum(monthly.map(m=>m.components[o].pnl)),
      best_month:monthly.reduce((a,m)=>!a||m.components[o].pnl>a.pnl?{month:m.month,pnl:m.components[o].pnl}:a,null),
      worst_month:monthly.reduce((a,m)=>!a||m.components[o].pnl<a.pnl?{month:m.month,pnl:m.components[o].pnl}:a,null)};
  }
  const annual=[];
  for(let y=2021;y<=2025;y++){
    const mm=monthly.filter(m=>m.month.startsWith(String(y)));
    if(mm.length!==12)continue;
    const e0=mm[0].book_equity_start,all={};
    for(const o of [...origins,"SHORT_COMBINED"]){const pnl=sum(mm.map(m=>m.components[o].pnl));all[o]={pnl,contribution_pct:100*pnl/e0};}
    const bookPct=100*(mm.at(-1).book_equity_finish/e0-1);
    check(Math.abs(sum(origins.map(o=>all[o].contribution_pct))-bookPct)<1e-8,"annual contribution mismatch");
    annual.push({year:y,book_return_pct:bookPct,book_equity_start:e0,components:all});
  }
  const end=boundaries.at(-1);
  check(end.open_origin===null,"terminal not flat for this reconstruction");
  for(const o of origins)check(Math.abs(end.cumulative_contribution[o]-sum(records.filter(r=>r.origin===o).map(r=>r.net)))<1e-6,"terminal origin net");
  return {status:"MONTHLY_MTM_CONTRIBUTIONS_OF_EXECUTED_BOOK_NOT_STANDALONE",boundaries,monthly,summaries,annual,
    flat_boundary_count:boundaries.filter(b=>b.open_origin===null).length,
    max_flat_residual_error:Math.max(...boundaries.filter(b=>b.open_origin===null).map(b=>Math.abs(b.flat_residual_error))),
    funding_phase:"effective_at<=boundary, settled before R11 pre; no fill at any boundary; terminal flat",
    denominator:"Total historical K1001 book equity at interval start; no independent capital assigned to components",
    limits:"Realized historical policy/priority/sizing kept. No standalone CAGR/DD, hypothetical signals or new price observations."};
}
```
