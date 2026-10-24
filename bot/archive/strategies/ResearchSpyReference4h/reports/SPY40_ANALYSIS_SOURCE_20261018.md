# Auditoría SPY40 completa de snapshots

Comisión de ambas piernas exacta, reconciliaciónPnL, gross conequity aislada, horariodeentryNY,DST,concentración,stress+5/+10bpsRTmismaejecución,cohortescierresnoMTM. Curva del motor etiquetada como samplingmotor, nofinUTC. Pocos trades no prueban efecto; ningún dato fabricado si faltanmétricas.

```python
import json,math,collections
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Path('output').mkdir(exist_ok=True)
manifest=json.load(open('inputs/manifest.json'))
out={}
fig,ax=plt.subplots(figsize=(11,6))
for entry in manifest:
 name=entry['name'];d=json.load(open(entry['file']))
 if entry.get('session_status')!='finished':raise AssertionError('Nonterminal input')
 t=d.get('trades',[]);m=d.get('metrics') or {}
 p=np.array([float(v['PNL']) for v in t]);fees=np.array([float(v['fee']) for v in t])
 rn=np.array([(float(v['entry_price'])+float(v['exit_price']))*abs(float(v['qty'])) for v in t])
 notions=np.array([float(v['entry_price'])*abs(float(v['qty'])) for v in t])
 gross=np.array([(1 if v['type']=='long' else -1)*(v['exit_price']-v['entry_price'])*abs(v['qty']) for v in t])
 if len(t):
  assert np.allclose(fees,.00045*rn,atol=1e-6,rtol=1e-9)
  assert np.allclose(gross-fees,p,atol=1e-6)
  assert math.isclose(p.sum(),m['net_profit'],abs_tol=1e-6)
  assert math.isclose(fees.sum(),m['fee'],abs_tol=1e-6)
 winners=float(p[p>0].sum());losers=float(-p[p<0].sum())
 pf=winners/losers if losers else (None if not winners else 'infinite_no_losses')
 side={};years=collections.defaultdict(lambda:{'n':0,'net':0.,'fees':0.})
 entry_clock=collections.Counter();capital=10000.;maxgross=0.;hold=[];crosses=0
 first=None;last=None;terminal=[];types=collections.Counter()
 for v in t:
  opened=pd.to_datetime(v['opened_at'],unit='ms',utc=True)
  closed=pd.to_datetime(v['closed_at'],unit='ms',utc=True)
  loc=opened.to_pydatetime().astimezone(ZoneInfo('America/New_York'))
  entry_clock[loc.strftime('%H:%M')]+=1
  if name!='reference': assert loc.weekday()<5 and (loc.hour,loc.minute) in ((10,0),(11,30),(13,30),(15,30),(16,0))
  if first is None:first=str(opened)
  last=str(closed)
  q=abs(float(v['qty']));ratio=q*v['entry_price']/capital
  maxgross=max(maxgross,ratio)
  assert ratio<=4.40000001
  capital+=v['PNL']
  s=side.setdefault(v['type'],{'n':0,'net':0.,'fees':0.})
  s['n']+=1;s['net']+=v['PNL'];s['fees']+=v['fee']
  year=years[str(closed.year)];year['n']+=1;year['net']+=v['PNL'];year['fees']+=v['fee']
  hold.append(v['holding_period']/3600)
  crosses+=int(opened.floor('D')!=closed.floor('D'))
  if closed==pd.Timestamp('2025-12-31',tz='UTC'):terminal.append(v['id'])
  for order in v['orders']:
   if order['status']=='EXECUTED':types[(order['side'],order['type'],bool(order['reduce_only']))]+=1
 net=float(p.sum());stress5=float((p-.00025*rn).sum());stress10=float((p-.0005*rn).sum())
 dd=m.get('max_drawdown')
 passing=(len(t)>=30 and net>0 and isinstance(pf,float) and pf>=1.2 and dd is not None and dd>=-25 and stress5>0)
 classification='candidate_descriptive' if passing else ('no_trades' if not len(t) else ('inconclusive_small_sample' if len(t)<30 else 'fails_economic_screen'))
 out[name]={'session_id':entry['session_id'],'n':len(t),'net':net,'fees':float(fees.sum()),'gross_price':float(gross.sum()),'pf':pf,'return_pct':m.get('net_profit_percentage'),'cagr_engine':m.get('annual_return'),'dd_engine':dd,'stress5_samefills':stress5,'stress10_samefills':stress10,'net_bps_entry':net/float(notions.sum())*10000 if len(t) else None,'ex_top1':net-max(p) if len(t) else None,'ex_top3':net-sum(sorted(p,reverse=True)[:3]) if len(t) else None,'ex_top5':net-sum(sorted(p,reverse=True)[:5]) if len(t) else None,'side':side,'closed_trade_year_cohorts_NOT_MTM':dict(years),'hours':sum(hold),'mean_hours':np.mean(hold).item() if hold else 0,'max_hours':max(hold) if hold else 0,'crossing_UTC_days':crosses,'first_entry':first,'last_exit':last,'max_initial_gross_equity':maxgross,'entry_clock_NY':dict(entry_clock),'terminal_liquidations':terminal,'engine_open_count_preterminal':m.get('total_open_trades'),'classification':classification}
 print(name,json.dumps(out[name],default=str))
 curves=d.get('equity_curve',[])
 for series in curves:
  if series['name']=='Portfolio' and series['data']:
   c=pd.DataFrame(series['data']);ax.plot(pd.to_datetime(c['time'],unit='s',utc=True),c['value'],label=name)
json.dump(out,open('output/results.json','w'),indent=2,default=str)
ax.set_title('SPY40 isolated1% — engine sampling, not UTC-close MTM')
ax.legend();fig.tight_layout();fig.savefig('output/equity_engine.png',dpi=110);plt.close(fig)

```