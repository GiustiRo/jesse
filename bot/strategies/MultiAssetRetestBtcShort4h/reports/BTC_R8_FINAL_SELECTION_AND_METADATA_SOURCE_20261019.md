# R8 — código final de conciliación, selección y cierre

Código ejecutado en el orquestador. El cálculo financiero permanece en el auditor run_analysis congelado y archivado antes de los resultados. La conciliación posterior usa exclusivamente logs MCP completos y paths provenientes de ese auditor; no recalcula PNL ni inventa órdenes canceladas. El cierre sólo procede tras 26 nominales, 13 auditorías, 37 readbacks de fuentes y todas las conciliaciones Y. Los helpers dependen del estado del manifiesto, las fuentes de cada receta y los artefactos de jobs identificados. La aclaración conservadora Y903 se registró antes de sus corridas.

## R8SleeveMetadataFunction

```javascript
async function sleeveMetadataR8(batch){
 const dec=r=>{const t=r.content?.find(x=>x.type==="text")?.text;if(!t?.trim().startsWith("{"))throw Error("MCPnonJSON logs: "+t);return JSON.parse(t);},reg=[...load("R8Registry"),...load("R8References")],pair=reg.filter(x=>x.name===batch+"B"||x.name===batch+"C"),results=load("R8SleeveMetadata")||{};
 if(pair.length!==2)throw Error("unknown batch");
 for(const d of pair){
  const paths=load(d.name+"r8path");if(!paths)throw Error("financialpathfirst");
  let offset=0,pages=0,more=true,records=[],terminal=[],linesRead=0;
  while(more){
   const r=dec(await tools.mcp__jesse_local__get_session_results({session_type:"backtest",session_id:d.id,section:"logs",offset,limit:500}));
   if(r.status!=="success")throw Error(JSON.stringify(r));pages++;linesRead+=r.items.length;
   for(const line of r.items){
    if(line.includes("BTC_EXPLORE_FILL ")){const x=JSON.parse(line.slice(line.indexOf("BTC_EXPLORE_FILL ")+"BTC_EXPLORE_FILL ".length));if(x.recipe===d.name.slice(0,-1))records.push(x);}
    else if(line.includes("BTC_EXPLORE ")){const x=JSON.parse(line.slice(line.indexOf("BTC_EXPLORE ")+"BTC_EXPLORE ".length));if(x.recipe===d.name.slice(0,-1))terminal.push(x);}
   }
   more=!!r.has_more;
   if(more){if(r.next_offset==null||r.next_offset<=offset||pages>=200)throw Error("incomplete log paging "+d.name);offset=r.next_offset;}
  }
  const errors=[],matches=[],used=new Set();
  for(const t of paths)if(t.symbol==="BTC-USDT"&&t.side==="short")t.sleeve="unknown";
  if(terminal.length!==1)errors.push("terminal_count_"+terminal.length);
  const expected=terminal[0]?.counts?.fills||0,closed=terminal[0]?.counts?.closes||0;
  if(records.length!==expected)errors.push("fill_count_mismatch");
  for(const r of records){
   const candidates=paths.map((t,i)=>({t,i})).filter(({t})=>t.symbol==="BTC-USDT"&&t.side===r.side&&t.open===r.time&&Math.abs(t.entry-r.entry)<=1e-7&&Math.abs(t.qty-r.qty)<=1e-7);
   if(candidates.length!==1||used.has(candidates[0]?.i)){errors.push("nonbijective_fill_"+r.time);continue;}
   if(!(Number.isFinite(r.distance)&&r.distance>0&&Math.abs(r.target_distance-2*r.distance)<=1e-7)){errors.push("target_geometry_"+r.time);continue;}
   if(d.name.startsWith("Y")&&!(Number.isFinite(r.requested_entry)&&r.requested_entry>0&&Number.isFinite(r.signal_anchor)&&r.signal_anchor>0)){errors.push("missing_requested_metadata_"+r.time);continue;}
   const {t,i}=candidates[0];used.add(i);t.sleeve="supplement";matches.push({open:t.open,entry:t.entry,qty:t.qty,entry_type:t.entry_type,recipe:r.recipe,requested_entry:r.requested_entry,signal_anchor:r.signal_anchor,distance:r.distance,target_distance:r.target_distance});
  }
  if(matches.length!==expected)errors.push("matched_count_mismatch");
  const finishMs=Date.parse(load("R8Summary"+d.name).form.finish_date+"T00:00:00Z"),boundarySupp=[...used].filter(i=>paths[i].close===finishMs).length;
  let boundaryAdjustment=0;
  if(closed!==expected){
   if(closed+boundarySupp===expected&&load("R8Audits")[d.name].mtm.terminal_reconciles)boundaryAdjustment=boundarySupp;
   else errors.push("close_count_not_reconciled");
  }
  const ok=errors.length===0;
  if(ok)for(const t of paths)if(t.symbol==="BTC-USDT"&&t.side==="short"&&t.sleeve==="unknown")t.sleeve="original";
  store(d.name+"r8path",paths);
  results[d.name]={ok,pages,lines_read:linesRead,log_fill_count:records.length,terminal_fills:expected,terminal_closes:closed,boundary_supplement_closes:boundarySupp,boundary_counter_adjustment:boundaryAdjustment,matched:matches.length,errors,observed_supplement_entry_types:Object.fromEntries([...new Set(matches.map(x=>x.entry_type))].map(type=>[type,matches.filter(x=>x.entry_type===type).length])),matches,note:"Metadata reconciliation of complete MCP logs against run_analysis financial paths; not a second financial calculation. STOP type alone never identifies original sleeve."};
 }
 store("R8SleeveMetadata",results);
 const content="# BTC R8 — "+batch+" identificación de suplementos\n\nSe paginaron logs MCP completos de sesionesfinalizadas, sinestimarlos. Conciliaciónbijectiva deBTC_EXPLORE_FILLconpathsdelanálisisfinancieroporclock/entry/qty1e-7ygeometría2R. Etiquetasmetadata, no recalcularPNL ni inferirSTOPoriginalpormerotipo. Error/faltantesbloqueaelegibilidad; no imputaunknown. Losimportesdefills/fees/wallet/MTMson del auditorrun_analysis.\n\n"+pair.map(d=>"## ["+d.name+"]("+d.url+")\n\n```json\n"+JSON.stringify(results[d.name],null,2)+"\n```").join("\n\n");
 const saved=dec(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R8_"+batch+"_SLEEVE_IDENTIFICATION_20261019.md",content,overwrite:false}));
 if(saved.status!=="success")throw Error(JSON.stringify(saved));return pair.map(d=>({name:d.name,ok:results[d.name].ok,matched:results[d.name].matched,types:results[d.name].observed_supplement_entry_types,errors:results[d.name].errors,path:saved.path}));
}
```

## R8RankFunction

```javascript
function rankR8(){
 const aud=load("R8Audits"),rows=load("R8MonthRows"),paths=load("R8PathChecks")||{},rec=Object.values(load("R8Recipes")).flat();
 const result=rec.map(v=>{
 const rr=["B","C"].map(p=>{
  const n=v.id+p,a=aud[n],b=aud["N204"+p];if(!a||!paths[n]||(v.id.startsWith("Y")&&!load("R8SleeveMetadata")?.[n]))return{portfolio:p,pending:true};
  const f=a.cost_calendar["5"].complete_periods,i=a.cost_calendar["5"].partial_periods;
  const margins=[f.win_months_active-.65,i.win_months_active-.65,f.win_quarters-.8,i.win_quarters-.8];
  const base=new Map(rows["N204"+p].map(x=>[x.month,x])),deltaMonths=rows[n].map(x=>({month:x.month,delta:x.mtm_USDT-base.get(x.month).mtm_USDT}));
  const annual=Object.fromEntries([2021,2022,2023,2024,2025].map(y=>[y,deltaMonths.filter(x=>x.month.startsWith(String(y))).reduce((s,x)=>s+x.delta,0)]));
  const isY=v.id.startsWith("Y"),filter=t=>t.symbol==="BTC-USDT"&&t.side==="short"&&(t.sleeve?t.sleeve==="supplement":t.entry_type==="MARKET"),key=t=>[t.symbol,t.side,t.entry_type,t.open].join("|"),oldEntries=load((isY?"N503":"N204")+p+"r8path").filter(filter),newEntries=load(n+"r8path").filter(filter),oldKeys=new Map(oldEntries.map(t=>[key(t),t])),newKeys=new Set(newEntries.map(key)),changedEntries=oldEntries.filter(t=>!newKeys.has(key(t))).length+newEntries.filter(t=>!oldKeys.has(key(t))).length+(isY?newEntries.filter(t=>oldKeys.has(key(t))&&Math.abs(t.entry-oldKeys.get(key(t)).entry)>1e-7).length:0),supplementFills=newEntries.length;
  const positiveYears=Object.values(annual).filter(x=>x>1e-7).length,best=Math.max(...deltaMonths.map(x=>x.delta)),withoutBest=a.net-b.net-best,modified=v.id==="Y903"?newEntries.filter(t=>{const old=oldKeys.get(key(t));return old&&Math.abs(t.entry-old.entry)<=1e-7&&(t.close!==old.close||Math.abs(t.exit-old.exit)>1e-7);}).length:paths[n].modified_same_entry_exits;
  const gates={nominal:a.net-b.net>1e-7,calendar:margins.every(x=>x>=0),plus10:a.plus10_samefills-b.plus10_samefills>=-1e-7,dd:a.dd_engine>=-25,modified_entries:v.id==="Y903"?modified>=10:changedEntries>=10,supplement_fills:supplementFills>=30,metadata_identified:!isY||load("R8SleeveMetadata")[n].ok,year_distribution:positiveYears>=3,without_best_month:withoutBest>1e-7};
  return{portfolio:p,pending:false,net:a.net,delta:a.net-b.net,delta_seed:a.net-aud[v.seed+p].net,plus10:a.plus10_samefills,delta10:a.plus10_samefills-b.plus10_samefills,dd:a.dd_engine,counts:{Mfull:f.positive_months+"/"+f.months_active,Mall:i.positive_months+"/"+i.months_active,Qfull:f.positive_quarters+"/"+f.quarters_total,Qall:i.positive_quarters+"/"+i.quarters_total},margin:Math.min(...margins),modified_exits:modified,changed_supplement_entries:changedEntries,supplement_fills:supplementFills,diversity_measure:v.id==="Y903"?"modified exits versus N503":isY?"changed execution versus N503":"changed entries versus N204",annual_delta_MTM:annual,positive_years:positiveYears,best_incremental_month:best,delta_without_best_month:withoutBest,gates,eligible:Object.values(gates).every(Boolean)};
 });
 return{id:v.id,strategy:v.strategy,seed:v.seed,rows:rr,pending:rr.some(x=>x.pending),eligible:rr.every(x=>x.eligible),margin:Math.min(...rr.map(x=>x.margin??-999)),delta10:Math.min(...rr.map(x=>x.delta10??-999999)),worstDD:Math.min(...rr.map(x=>x.dd??-999))};
 });
 const eligible=result.filter(x=>x.eligible).sort((a,b)=>b.margin-a.margin||b.delta10-a.delta10||b.worstDD-a.worstDD||a.id.localeCompare(b.id));
 return{matrix:result,eligible:eligible.map(x=>x.id),selected:result.some(x=>x.pending)?null:eligible[0]?.id??null};
}
```

## R8MatrixFunction

```javascript
async function matrixR8(final=false){
 const dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text),rank=eval("("+load("R8RankFunction")+")")(),reg=load("R8Registry"),a=load("R8Audits");
 if(final&&rank.matrix.some(x=>x.pending))throw Error("pendingmatrix");
 const lines=["|Receta|Cartera|Neto|ΔN204|Δsemilla|DDmotor%|Δ+10N204|M+5full/all|Q+5full/all|Diversidad según receta / fills|Bloques anuales Δ>0|Δsinmejormes|Gates N/MQ/+10/DD/diversidad/fills/metadata/bloques/sinmes|","|---|---|---:|---:|---:|---:|---:|---|---|---:|---:|---:|---|"];
 for(const x of rank.matrix)for(const r of x.rows){if(r.pending)continue;const d=reg.find(y=>y.name===x.id+r.portfolio);lines.push(`|[${d.name}](${d.url})|${r.portfolio}|${r.net.toFixed(6)}|${r.delta.toFixed(6)}|${r.delta_seed.toFixed(6)}|${r.dd.toFixed(4)}|${r.delta10.toFixed(6)}|${r.counts.Mfull};${r.counts.Mall}|${r.counts.Qfull};${r.counts.Qall}|${r.diversity_measure.startsWith('modified exits')?r.modified_exits:r.changed_supplement_entries}/${r.supplement_fills}|${r.positive_years}/5|${r.delta_without_best_month.toFixed(6)}|${Object.values(r.gates).map(x=>x?"PASS":"FAIL").join("/")}|`);}
 const content="# BTC R8 — matriz "+(final?"final":"parcial")+"\n\n2026cerrado; misma muestra de desarrollo2020-10-15→2025-12-31exclusiva.26nominales:5seleccióncontextual+5setupsexperimentales+3creativasdeejecución/invalidaciónB/C. AmpliaciónsolicitadaantesdecrearsourcesY yconaddendumcongelado. N204referenceultimate;semillaN503oN204paraatribución. Puertas congeladas en BTC_R8_FROZEN_PROTOCOL_20261019.md. La diversidad de10entradasmodificadas y30fillsdelsuplemento y3/5bloquesanuales(2025parcial) no es prueba estadística; son controlesoperativos prefijados contra concentración. Omitirmejormes sóloaritmético,sinreplay. Overlays5/10bpsRTsobre rutas/cantidadesfijas, no mayorfeeengine. Meses full61/all63 y Q19/21; denominadormensualactivo,calendarioensummaries;positivos>0sinredondear. Elegibles: "+(rank.eligible.join(", ")||"ninguno")+". Selección: "+(rank.selected||"ninguna")+".\n\n"+lines.join("\n")+"\n\n```json\n"+JSON.stringify({ranking:rank,paths:load("R8PathChecks")||{}},null,2)+"\n```\n";
 const r=dec(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R8_RESULTS_MATRIX_20261019.md",content,overwrite:!!load("R8MatrixSaved")}));if(r.status!=="success")throw Error(JSON.stringify(r));store("R8MatrixSaved",r);store("R8Ranking",rank);return{completed:rank.matrix.filter(x=>!x.pending).length*2,selected:rank.selected,eligible:rank.eligible,path:r.path};
}
```

## R8PathFunction

```javascript
async function pathR8Identity(batch){
 const result=await eval("("+load("R8BasePathFunction")+")")(batch),checks=load("R8PathChecks"),job=load("R8Jobs").find(j=>j.batch===batch);
 function compare(a,b){
  const key=t=>[t.symbol,t.side,t.open].join("|"),am=new Map(a.map(t=>[key(t),t]));let max=0,same=a.length===b.length,matched=0;
  for(const t of b){const r=am.get(key(t));if(!r){same=false;continue;}matched++;if(r.close!==t.close||r.entry_type!==t.entry_type)same=false;
   for(const f of ["entry","exit","qty","net","fee"]){const delta=Math.abs(r[f]-t[f]);if(!Number.isFinite(delta))throw Error("missingpathfield "+f);max=Math.max(max,delta);if(delta>1e-7)same=false;}
  }return{economic_identity_within_1e_7:same,matched,max_abs_economic_field_delta:max,note:"Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."};
 }
 for(const n of job.names){const a=load(n+"r8path"),p=n.slice(-1),seed=load("R8Registry").find(x=>x.name===n).seed;checks[n].identity_vs_N204=compare(a,load("N204"+p+"r8path"));checks[n].identity_vs_seed=compare(a,load(seed+p+"r8path"));checks[n].identity_vs_P604=compare(a,load("P604"+p+"r8path"));checks[n].identity_vs_N503=compare(a,load("N503"+p+"r8path"));if(load("P603"+p+"r6path"))checks[n].identity_vs_P603=compare(a,load("P603"+p+"r6path"));const sk=t=>[t.symbol,t.side,t.open].join("|"),sm=new Map(load(seed+p+"r8path").map(t=>[sk(t),t]));checks[n].modified_same_entry_exits=a.filter(t=>sm.has(sk(t))&&sm.get(sk(t)).close!==t.close).length;}
 store("R8PathChecks",checks);return result.map(x=>({...x,identity:checks[x.n].identity_vs_N204}));
}
```

## R8FinalSourceFunction

```javascript
async function finalSourcesR8(){
 const dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text);
 const sources={...load("N204R6BaseSources"),N204ExploreR503:load("R6BaseN503"),...Object.fromEntries(Object.values(load("N204R6Recipes")).flat().map(x=>[x.strategy,load("R6Source"+x.strategy)])),...load("R7Sources"),...load("R8Sources")};
 const results=await Promise.allSettled(Object.entries(sources).map(async([name,source])=>{
  const r=dec(await tools.mcp__jesse_local__read_strategy({name}));if(r.status!=="success"||r.content!==source)throw Error("sourcechanged "+name);
  return {name,exact:true,chars:source.length};
 }));
 store("R8FinalSourceChecks",results);
 if(results.some(x=>x.status!=="fulfilled"))throw Error(JSON.stringify(results));
 return results.map(x=>x.value);
}
```

## R8FinalManifestFunction

```javascript
async function manifestR8(){
 const dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text),reg=load("R8Registry"),forms=load("R8FormChecks"),jobs=load("R8Jobs"),aud=load("R8Audits"),sources=load("R8FinalSourceChecks"),ranking=eval("("+load("R8RankFunction")+")")(),meta=load("R8SleeveMetadata");
 if(reg.length!==26||reg.some(x=>x.status!=="finished")||ranking.matrix.some(x=>x.pending)||jobs.length!==13||jobs.some(x=>x.status!=="succeeded")||reg.some(x=>aud[x.name]?.audit!=="passed"||!aud[x.name]?.mtm?.terminal_reconciles))throw Error("incomplete nominal audit");
 if(sources.length!==37||sources.some(x=>x.status!=="fulfilled"))throw Error("sourcecheck");
 const m={research:"R8",closed_2026:true,window:"2020-10-15 inclusive ->2025-12-31 exclusive",nominal_fulls:26,extra_fulls:0,selected:ranking.selected,eligible:ranking.eligible,registry:reg,forms,source_checks:sources.map(x=>x.value),qa_jobs:load("R8QAJobs"),financial_jobs:jobs,financial_audits:reg.map(x=>({name:x.name,status:aud[x.name].audit,terminal:aud[x.name].mtm.terminal_reconciles})),sleeve_metadata:Object.fromEntries(Object.entries(meta).map(([n,m])=>[n,{ok:m.ok,log_fill_count:m.log_fill_count,terminal_fills:m.terminal_fills,matched:m.matched,pages:m.pages,lines_read:m.lines_read,boundary_counter_adjustment:m.boundary_counter_adjustment,types:m.observed_supplement_entry_types,errors:m.errors}])),ranking};
 for(const d of reg){const f=forms[d.id];if(!f||!f.dates||!f.routes||!f.feeds||!f.settings||f.sources.length!==3||f.sources.some(x=>!x))throw Error("bad finalform "+d.name);}
 if(reg.filter(x=>x.name.startsWith("Y")).some(x=>!meta[x.name]?.ok))throw Error("metadatafail");
 if(ranking.eligible.length)throw Error("eligible requires conditional validation, cannot finalize zero extras");
 const content="# BTC R8 — manifiesto de cierre\n\n26 backtests nominales terminados y auditados; ninguna receta elegible. Se aplica la regla congelada: cero backtests adicionales. 26 formularios / 78 snapshots coherentes, 37 fuentes exactas al readback final, 13 auditorías financieras de pares con cuatro anclas inmutables y reconciliación terminal. Identificación de suplementos creativos por logs paginados completos, separada de los cálculos financieros. Sin reinicios, purgas ni eliminación de historial. 2026 permanece cerrado.\n\nQA registra comprobaciones de fixtures y fuentes, no pruebas de rentabilidad ni cobertura exhaustiva del motor. Análisis y figuras derivadas no cuentan como nuevas observaciones independientes. La muestra de desarrollo se reutilizó; no hay validación fuera de muestra en esta ronda.\n\n```json\n"+JSON.stringify(m,null,2)+"\n```\n";
 const r=dec(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R8_FINAL_MANIFEST_20261019.md",content,overwrite:false}));if(r.status!=="success")throw Error(JSON.stringify(r));store("R8FinalManifest",r);return{path:r.path,fulls:reg.length,forms:reg.length,snapshots:reg.length*3,sources:sources.length,financial_jobs:jobs.length};
}
```
