# BTC R8 — adaptación de ranking Y antes de resultados

LasdiezrecetasV/X conservancriteriosoriginales. Y901/902diversidaddeejecuciónvsN503;Y903salidasvsN503;siempre>=30fillsdel suplemento. Identificaciónporconciliacióncompletadelogs/pathsobligatoriaY. Laelecciónúnicaserealizatras26nominales;máximo6extrasprefijados. VersiónoriginalenBTC_R8_AUDITOR_AND_RANKING_SOURCE_20261019.md;adaptacióncongeladaaquíantesdeYfuentes/corridas. No seclasificanSTOPporsolotipo ni porbracketsausentes.

```javascript
function rankR8(){
 const aud=load("R8Audits"),rows=load("R8MonthRows"),paths=load("R8PathChecks")||{},rec=Object.values(load("R8Recipes")).flat();
 const result=rec.map(v=>{
 const rr=["B","C"].map(p=>{
  const n=v.id+p,a=aud[n],b=aud["N204"+p];if(!a||!paths[n]||(v.id.startsWith("Y")&&!load("R8SleeveMetadata")?.[n]?.ok))return{portfolio:p,pending:true};
  const f=a.cost_calendar["5"].complete_periods,i=a.cost_calendar["5"].partial_periods;
  const margins=[f.win_months_active-.65,i.win_months_active-.65,f.win_quarters-.8,i.win_quarters-.8];
  const base=new Map(rows["N204"+p].map(x=>[x.month,x])),deltaMonths=rows[n].map(x=>({month:x.month,delta:x.mtm_USDT-base.get(x.month).mtm_USDT}));
  const annual=Object.fromEntries([2021,2022,2023,2024,2025].map(y=>[y,deltaMonths.filter(x=>x.month.startsWith(String(y))).reduce((s,x)=>s+x.delta,0)]));
  const isY=v.id.startsWith("Y"),filter=t=>t.symbol==="BTC-USDT"&&t.side==="short"&&(t.sleeve?t.sleeve==="supplement":t.entry_type==="MARKET"),key=t=>[t.symbol,t.side,t.entry_type,t.open].join("|"),oldEntries=load((isY?"N503":"N204")+p+"r8path").filter(filter),newEntries=load(n+"r8path").filter(filter),oldKeys=new Map(oldEntries.map(t=>[key(t),t])),newKeys=new Set(newEntries.map(key)),changedEntries=oldEntries.filter(t=>!newKeys.has(key(t))).length+newEntries.filter(t=>!oldKeys.has(key(t))).length+(isY?newEntries.filter(t=>oldKeys.has(key(t))&&Math.abs(t.entry-oldKeys.get(key(t)).entry)>1e-7).length:0),supplementFills=newEntries.length;
  const positiveYears=Object.values(annual).filter(x=>x>1e-7).length,best=Math.max(...deltaMonths.map(x=>x.delta)),withoutBest=a.net-b.net-best,modified=paths[n].modified_same_entry_exits;
  const gates={nominal:a.net-b.net>1e-7,calendar:margins.every(x=>x>=0),plus10:a.plus10_samefills-b.plus10_samefills>=-1e-7,dd:a.dd_engine>=-25,modified_entries:v.id==="Y903"?modified>=10:changedEntries>=10,supplement_fills:supplementFills>=30,metadata_identified:!isY||load("R8SleeveMetadata")[n].ok,year_distribution:positiveYears>=3,without_best_month:withoutBest>1e-7};
  return{portfolio:p,pending:false,net:a.net,delta:a.net-b.net,delta_seed:a.net-aud[v.seed+p].net,plus10:a.plus10_samefills,delta10:a.plus10_samefills-b.plus10_samefills,dd:a.dd_engine,counts:{Mfull:f.positive_months+"/"+f.months_active,Mall:i.positive_months+"/"+i.months_active,Qfull:f.positive_quarters+"/"+f.quarters_total,Qall:i.positive_quarters+"/"+i.quarters_total},margin:Math.min(...margins),modified_exits:modified,changed_supplement_entries:changedEntries,supplement_fills:supplementFills,diversity_measure:v.id==="Y903"?"modified exits versus N503":isY?"changed execution versus N503":"changed entries versus N204",annual_delta_MTM:annual,positive_years:positiveYears,best_incremental_month:best,delta_without_best_month:withoutBest,gates,eligible:Object.values(gates).every(Boolean)};
 });
 return{id:v.id,strategy:v.strategy,seed:v.seed,rows:rr,pending:rr.some(x=>x.pending),eligible:rr.every(x=>x.eligible),margin:Math.min(...rr.map(x=>x.margin??-999)),delta10:Math.min(...rr.map(x=>x.delta10??-999999)),worstDD:Math.min(...rr.map(x=>x.dd??-999))};
 });
 const eligible=result.filter(x=>x.eligible).sort((a,b)=>b.margin-a.margin||b.delta10-a.delta10||b.worstDD-a.worstDD||a.id.localeCompare(b.id));
 return{matrix:result,eligible:eligible.map(x=>x.id),selected:result.some(x=>x.pending)?null:eligible[0]?.id??null};
}
```
