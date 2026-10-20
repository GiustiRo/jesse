# Verificación de grupos idénticos — adenda de análisis

Después del lote1, root pidió distinguir trayectorias/fills repetidos de nueva evidencia. Lote2 incluirá Cq+S06..10+S04/S05 (8inputs, sin nuevosfulls) y añade comparación exacta de campos económicos de TODAS las operaciones y curva completa. Lógica económica/criterios/variantes congelados sin cambios. No se interpreta igualdad de fills como ausencia de armings distintos. JSON compactos<50KB se mantienen.

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
 out[name]={'session_id':meta['session_id'],'n':len(t),'net':float(p.sum()) if len(t) else None,'gross_price':float(gross.sum()) if len(t) else None,'fee':float(f.sum()) if len(t) else None,'PF':pf,'return_pct':m.get('net_profit_percentage'),'CAGR_engine_pct':m.get('annual_return'),'Sharpe_engine':m.get('sharpe_ratio'),'DD_engine_pct':m.get('max_drawdown'),'hours_open':float(hold.sum()/3600000),'fraction_time_open':float(hold.sum()/window_ms),'entry_notional_time_over_initial_equity_WINDOW_NOT_MTM':float(np.dot(notion,hold)/(10000*window_ms)) if len(t) else 0.,'entry_turnover_initial_equity':float(notion.sum()/10000),'roundtrip_turnover_initial_equity':float(rn.sum()/10000),'net_bps_entry':float(p.sum()/notion.sum()*10000) if len(t) else None,'net_per_exposure_entry_time_measure':float(p.sum()/np.dot(notion,hold)*window_ms) if len(t) else None,'max_initial_gross_equity':maxgross,'mean_hours':float(hold.mean()/3600000) if len(t) else None,'max_hours':float(hold.max()/3600000) if len(t) else None,'stress5_RT_samefills':float((p-.00025*rn).sum()) if len(t) else None,'stress10_RT_samefills':float((p-.0005*rn).sum()) if len(t) else None,'net_without_top1':float(p.sum()-max(p)) if len(t) else None,'net_without_top3':float(p.sum()-sum(sorted(p,reverse=True)[:3])) if len(t) else None,'net_without_top5':float(p.sum()-sum(sorted(p,reverse=True)[:5])) if len(t) else None,'closed_trade_year_cohorts_NOT_MTM':dict(years),'entry_order_types':dict(entrytypes),'exit_order_types':dict(exittypes),'entry_clock_UTC':dict(clocks),'terminal_liquidations':terminal,'engine_open_count_preterminal':m.get('total_open_trades')}
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
  econ_keys=['symbol','type','opened_at','closed_at','entry_price','exit_price','qty','PNL','fee','holding_period']
  full_economic_equal=(len(ta)==len(tb)==len(common) and all(all(ta[k][field]==tb[k][field] for field in econ_keys) for k in common))
  curve_equal=datasets[a].get('equity_curve')==datasets[b].get('equity_curve')
  pairs[label]={'full_trade_economic_path_equal':full_economic_equal,'equity_curve_exact_equal':curve_equal,'common_entries':len(common),'total_a':len(ta),'total_b':len(tb),'only_a':len(set(ta)-set(tb)),'only_b':len(set(tb)-set(ta)),'sum_normalized_net_a':sum(r['net_per_entrynotional_a'] for r in rows),'sum_normalized_net_b':sum(r['net_per_entrynotional_b'] for r in rows),'rows':rows,'limitation':'Intersection conditional on endogenous occupancy, not causal.'}
  print('PAIR',label,json.dumps({k:v for k,v in pairs[label].items() if k!='rows'}))
json.dump({'metrics':out,'pairs':{key:{k:v for k,v in value.items() if k!='rows'} for key,value in pairs.items()}},open('output/results.json','w'),indent=2)
for key,value in pairs.items():
 json.dump(value,open('output/pairs_'+key+'.json','w'),indent=2)
assert Path('output/results.json').stat().st_size < 50000, 'Compact summary exceeded50KB'
for path in Path('output').glob('pairs_*.json'):
 assert path.stat().st_size < 50000, 'Pair artifact exceeded50KB'
ax.set_title('R60 SPY isolated1% — engine sampling, not UTC-close MTM')
ax.legend();fig.tight_layout();fig.savefig('output/equity_engine.png',dpi=110);plt.close(fig)

```