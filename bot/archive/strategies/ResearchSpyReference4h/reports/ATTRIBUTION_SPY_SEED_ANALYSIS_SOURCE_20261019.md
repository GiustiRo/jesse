# Fuente resumen cinco semillas

Reutiliza auditoría predeclarada, añade mediana/media/rango descriptivos de cinco semillas y diferencias pareadas R−U. No tests ni selección. Se aplica a diez snapshots completos.

```python
import json,math,collections
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Path('output').mkdir(exist_ok=True)
manifest=json.load(open('inputs/manifest.json'))
datasets={}
out={}
window_ms=(pd.Timestamp('2025-12-31',tz='UTC')-pd.Timestamp('2020-10-15',tz='UTC')).total_seconds()*1000
fig,ax=plt.subplots(figsize=(11,6))
for meta in manifest:
 assert meta['session_status']=='finished'
 name=meta['name'];d=json.load(open(meta['file']));datasets[name]=d
 t=d.get('trades',[]);m=d.get('metrics') or {}
 p=np.array([float(v['PNL']) for v in t])
 f=np.array([float(v['fee']) for v in t])
 rn=np.array([(float(v['entry_price'])+float(v['exit_price']))*abs(v['qty']) for v in t])
 notion=np.array([float(v['entry_price'])*abs(v['qty']) for v in t])
 gross=np.array([(1 if v['type']=='long' else -1)*(v['exit_price']-v['entry_price'])*abs(v['qty']) for v in t])
 hold=np.array([v['closed_at']-v['opened_at'] for v in t])
 if len(t):
  assert np.allclose(f,.00045*rn,atol=1e-6,rtol=1e-9)
  assert np.allclose(gross-f,p,atol=1e-6)
  assert math.isclose(float(p.sum()),m['net_profit'],abs_tol=1e-6)
  assert math.isclose(float(f.sum()),m['fee'],abs_tol=1e-6)
  assert math.isclose(10000+float(p.sum()),m['finishing_balance'],abs_tol=1e-6)
 capital=10000.;maxgross=0.;entrytypes=collections.Counter();exittypes=collections.Counter();years=collections.defaultdict(lambda:{'n':0,'net':0.,'fee':0.})
 clocks=collections.Counter();terminal=[];freshchecks=[]
 for trade in t:
  maxgross=max(maxgross,abs(trade['qty'])*trade['entry_price']/capital)
  assert maxgross<=4.40000001
  capital+=trade['PNL']
  year=str(pd.to_datetime(trade['closed_at'],unit='ms',utc=True).year)
  years[year]['n']+=1;years[year]['net']+=trade['PNL'];years[year]['fee']+=trade['fee']
  clocks[pd.to_datetime(trade['opened_at'],unit='ms',utc=True).strftime('%a %H:%M')]+=1
  if trade['closed_at']==int(pd.Timestamp('2025-12-31',tz='UTC').timestamp()*1000):terminal.append(trade['id'])
  for order in trade['orders']:
   if order['status']=='EXECUTED':
    (exittypes if order.get('reduce_only') else entrytypes)[order['type']]+=1
 winners=float(p[p>0].sum());losses=float(-p[p<0].sum())
 pf=winners/losses if losses else None
 out[name]={'session_id':meta['session_id'],'n':len(t),'net':float(p.sum()) if len(t) else None,'gross_price':float(gross.sum()) if len(t) else None,'fee':float(f.sum()) if len(t) else None,'PF':pf,'return_pct':m.get('net_profit_percentage'),'DD_engine_pct':m.get('max_drawdown'),'hours_open':float(hold.sum()/3600000),'fraction_time_open':float(hold.sum()/window_ms),'entry_notional_time_over_initial_equity_WINDOW_NOT_MTM':float(np.dot(notion,hold)/(10000*window_ms)) if len(t) else 0.,'entry_turnover_initial_equity':float(notion.sum()/10000),'roundtrip_turnover_initial_equity':float(rn.sum()/10000),'net_bps_entry':float(p.sum()/notion.sum()*10000) if len(t) else None,'net_per_exposure_entry_time_measure':float(p.sum()/np.dot(notion,hold)*window_ms) if len(t) else None,'max_initial_gross_equity':maxgross,'mean_hours':float(hold.mean()/3600000) if len(t) else None,'max_hours':float(hold.max()/3600000) if len(t) else None,'stress5_RT_samefills':float((p-.00025*rn).sum()) if len(t) else None,'stress10_RT_samefills':float((p-.0005*rn).sum()) if len(t) else None,'net_without_top1':float(p.sum()-max(p)) if len(t) else None,'net_without_top3':float(p.sum()-sum(sorted(p,reverse=True)[:3])) if len(t) else None,'net_without_top5':float(p.sum()-sum(sorted(p,reverse=True)[:5])) if len(t) else None,'closed_trade_year_cohorts_NOT_MTM':dict(years),'entry_order_types':dict(entrytypes),'exit_order_types':dict(exittypes),'entry_clock_UTC':dict(clocks),'terminal_liquidations':terminal,'engine_open_count_preterminal':m.get('total_open_trades')}
 print(name,json.dumps(out[name]))
 for series in d.get('equity_curve',[]):
  if series['name']=='Portfolio' and series['data']:
   c=pd.DataFrame(series['data']);ax.plot(pd.to_datetime(c['time'],unit='s',utc=True),c['value'],label=name)
pairs={}
key=lambda t:(t['symbol'],t['type'],t['opened_at'])
for ia,a in enumerate(datasets):
 for b in list(datasets)[ia+1:]:
  # Exact same entry event only. Not nearest matching, not causal isolation.
  ta={key(t):t for t in datasets[a].get('trades',[])}
  tb={key(t):t for t in datasets[b].get('trades',[])}
  assert len(ta)==len(datasets[a].get('trades',[]))
  assert len(tb)==len(datasets[b].get('trades',[]))
  common=sorted(set(ta)&set(tb));rows=[]
  for k in common:
   x,y=ta[k],tb[k]
   nx,ny=abs(x['qty'])*x['entry_price'],abs(y['qty'])*y['entry_price']
   rows.append({'symbol':k[0],'side':k[1],'opened_at':k[2],'price_a':x['entry_price'],'price_b':y['entry_price'],'qty_a':x['qty'],'qty_b':y['qty'],'closed_a':x['closed_at'],'closed_b':y['closed_at'],'net_a':x['PNL'],'net_b':y['PNL'],'net_per_entrynotional_a':x['PNL']/nx,'net_per_entrynotional_b':y['PNL']/ny})
  label=a+'__'+b
  pairs[label]={'common_entries':len(common),'total_a':len(ta),'total_b':len(tb),'only_a':len(set(ta)-set(tb)),'only_b':len(set(tb)-set(ta)),'sum_normalized_net_a':sum(r['net_per_entrynotional_a'] for r in rows),'sum_normalized_net_b':sum(r['net_per_entrynotional_b'] for r in rows),'rows':rows,'limitation':'Intersection conditional on endogenous occupancy, not causal.'}
  print('PAIR',label,json.dumps({k:v for k,v in pairs[label].items() if k!='rows'}))
json.dump({'metrics':out,'pairs':{key:{k:v for k,v in value.items() if k!='rows'} for key,value in pairs.items()}},open('output/results.json','w'),indent=2)
for key,value in pairs.items():
 json.dump(value,open('output/pairs_'+key+'.json','w'),indent=2)
ax.set_title('ATTR SPY isolated1% — engine sampling, not UTC-close MTM')
ax.legend();fig.tight_layout();fig.savefig('output/equity_engine.png',dpi=110);plt.close(fig)

summary={}
fields=['net','PF','DD_engine_pct','fraction_time_open','entry_notional_time_over_initial_equity_WINDOW_NOT_MTM','entry_turnover_initial_equity','net_bps_entry','stress5_RT_samefills','stress10_RT_samefills','net_without_top1','net_without_top3']
for group in ['R','U']:
 records=[out['AttrSpy'+group+str(i).zfill(2)] for i in range(1,6)]
 stats={}
 for field in fields:
  values=[r[field] for r in records if r[field] is not None]
  stats[field]={'median':float(np.median(values)),'mean':float(np.mean(values)),'min':float(min(values)),'max':float(max(values))}
 summary[group]={'fixed_seeds':[101,202,303,404,505],'stats':stats,'positive_net_count':sum(r['net']>0 for r in records),'positive_stress5_count':sum(r['stress5_RT_samefills']>0 for r in records),'positive_stress10_count':sum(r['stress10_RT_samefills']>0 for r in records),'limitation':'Five dependent scenario controls, no winning-seed selection and no IID significance.'}
summary['paired_seed_differences_R_minus_U']=[]
for i,seed in enumerate([101,202,303,404,505],1):
 r,u=out['AttrSpyR'+str(i).zfill(2)],out['AttrSpyU'+str(i).zfill(2)]
 summary['paired_seed_differences_R_minus_U'].append({'seed':seed,'net_R':r['net'],'net_U':u['net'],'net_difference':r['net']-u['net'],'time_R':r['fraction_time_open'],'time_U':u['fraction_time_open'],'notionaltime_R':r['entry_notional_time_over_initial_equity_WINDOW_NOT_MTM'],'notionaltime_U':u['entry_notional_time_over_initial_equity_WINDOW_NOT_MTM'],'common_entries':pairs['AttrSpyR'+str(i).zfill(2)+'__AttrSpyU'+str(i).zfill(2)]['common_entries']})
json.dump(summary,open('output/seed_summary.json','w'),indent=2)
print('GROUPS',json.dumps(summary))

```