# Código reproducible de análisis de sesiones

Job final0d756f56648c42369dfcfc17b08c0ba6. Análisis temporal vía MCP; sólo lee snapshots y escribe outputs. Los cálculos de familia corta se obtuvieron por join de las9etiquetasBTC_EXPLORE_FILL con opened_at de los47tradescompletos deC, documentados íntegros en el informe de datos. Los bordes mensualesBTC se leyeron desde el exportMCP y verificaron por timestamp, no desde estos snapshots (benchmarkfalse).

Inputs:
```json
{
  "K_B": "d6ed3b7d-19c5-4240-8ad9-9cb2f7706667",
  "K_C": "3c175497-66bf-4cf0-a9f8-c888834961da",
  "K_B_STRESS": "40239c00-168a-4ab4-b423-069c91e6e6b7",
  "K_C_STRESS": "df30484a-1331-4faa-9097-6c2e7d7011bc",
  "DEV_B": "b9f0cccc-8de0-4076-a7fa-eb9ae8e1be38",
  "DEV_C": "3ec33cac-3ea6-43c7-9cfe-4d315930fee2",
  "N204_B": "3e9cec7e-da5b-4baf-9355-5b29b5e8c295",
  "N204_C": "0d78145f-b775-4e60-b2f0-84a10e1f858e"
}
```

```python

import json, math
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import matplotlib.pyplot as plt
import jesse.models
from jesse import helpers as jh

def dt(v): return datetime.fromtimestamp(v/1000, timezone.utc).isoformat()
def stats(ts):
    pn=[float(t['PNL']) for t in ts]; wins=[p for p in pn if p>0]; losses=[p for p in pn if p<0]
    fees=sum(float(t['fee']) for t in ts)
    raw=[(float(t['exit_price'])-float(t['entry_price']))*abs(float(t['qty']))*(1 if t['type']=='long' else -1) for t in ts]
    return dict(n=len(ts),net=sum(pn),fees=fees,price_pnl=sum(raw),pnl_fee_reconciliation=sum(raw)-fees-sum(pn),wins=len(wins),losses=len(losses),win_rate=len(wins)/len(ts) if ts else None,pf=sum(wins)/abs(sum(losses)) if losses else None,avg_win=sum(wins)/len(wins) if wins else None,avg_loss=sum(losses)/len(losses) if losses else None,avg_net=sum(pn)/len(ts) if ts else None,avg_price_return_pct=sum((float(t['exit_price'])/float(t['entry_price'])-1)*100*(1 if t['type']=='long' else -1) for t in ts)/len(ts) if ts else None)
def brief(t):
    return {**{k:t.get(k) for k in ['id','symbol','type','entry_price','exit_price','qty','PNL','fee','holding_period']},'open':dt(t['opened_at']),'close':dt(t['closed_at']),'exits':[{k:o.get(k) for k in ['type','side','price','qty','status','submitted_via','executed_at','reduce_only']} for o in t.get('orders',[]) if o.get('status')=='EXECUTED']}
out={}
fig,axs=plt.subplots(2,1,figsize=(11,7),sharex=True)
for f in sorted(Path('inputs').glob('*.json')):
    if f.name=='manifest.json':continue
    name=f.stem; d=json.load(f.open()); ts=d['trades']
    assert d['summary']['session_status']=='finished'
    row={'summary':d['summary'],'total':stats(ts),'by_group':{},'closed_month':{},'entry_month':{},'btc_yearly':{},'curve_monthly':[]}
    for sym in sorted(set(t['symbol'] for t in ts)):
        for side in ['long','short']:
            group=[t for t in ts if t['symbol']==sym and t['type']==side]
            if group:row['by_group'][sym+' '+side]=stats(group)
    for field,label in [('closed_at','closed_month'),('opened_at','entry_month')]:
        for m in sorted(set(dt(t[field])[:7] for t in ts)):
            group=[t for t in ts if dt(t[field])[:7]==m]
            row[label][m]={'all':stats(group),'groups':{g:stats([t for t in group if t['symbol']+' '+t['type']==g]) for g in row['by_group']}}
    for y in sorted(set(dt(t['opened_at'])[:4] for t in ts)):
        row['btc_yearly'][y]={side:stats([t for t in ts if t['symbol']=='BTC-USDT' and t['type']==side and dt(t['opened_at'])[:4]==y]) for side in ['long','short']}
    curve=next(s for s in d['equity_curve'] if s['name']=='Portfolio')
    q=pd.DataFrame(curve['data']);q['date']=pd.to_datetime(q.time,unit='s',utc=True);q=q.sort_values('time')
    q=q[q.date<pd.Timestamp(d['summary']['form']['finish_date'],tz='UTC')]
    prev=float(d['metrics']['starting_balance'])
    for m,g in q.groupby(q.date.dt.strftime('%Y-%m')):
        end=float(g.iloc[-1].value);row['curve_monthly'].append({'month':m,'start_equity':prev,'end_equity':end,'pnl':end-prev,'pct':100*(end/prev-1)})
        prev=end
    peak=q.value.cummax();dd=q.value/peak-1;idx=dd.idxmin();pidx=q.loc[:idx,'value'].idxmax()
    row['dd_episode']={'peak_date':q.loc[pidx,'date'].isoformat(),'peak':float(q.loc[pidx,'value']),'trough_date':q.loc[idx,'date'].isoformat(),'trough':float(q.loc[idx,'value']),'pct':float(dd.loc[idx]*100)}
    row['worst_trades']=[brief(t) for t in sorted(ts,key=lambda t:t['PNL'])[:12]]
    row['best_trades']=[brief(t) for t in sorted(ts,key=lambda t:-t['PNL'])[:6]]
    if name in ['K_B','K_C']:
        row['all_trades']=[brief(t) for t in sorted(ts,key=lambda t:t['closed_at'])]
        q2=pd.DataFrame(curve['data']);q2['date']=pd.to_datetime(q2.time,unit='s',utc=True)
        axs[0].plot(q2.date,q2.value,label=name);axs[1].plot(q2.date,100*(q2.value/q2.value.cummax()-1),label=name)
    row['schema']={'trade':list(ts[0]),'order':list(ts[0]['orders'][0])}
    out[name]=row
    jh.debug(json.dumps({'name':name,'groups':row['by_group'],'monthly':row['curve_monthly'],'dd':row['dd_episode']}))
axs[0].set_ylabel('Equity USDT');axs[1].set_ylabel('Drawdown %');axs[0].legend();axs[0].set_title('K1001: 2026 corregido, capital inicial 10.000 USDT')
fig.tight_layout();fig.savefig('output/diagnostico.png',dpi=110);plt.close(fig)
for name,row in out.items():
    Path('output/'+name+'.json').write_text(json.dumps({k:v for k,v in row.items() if k not in ['summary','closed_month','entry_month']},indent=None),encoding='utf8')
Path('output/resumen.json').write_text(json.dumps({k:{z:v[z] for z in ['total','by_group','dd_episode','btc_yearly'] if z in v} for k,v in out.items()},indent=None),encoding='utf8')
Path('output/meses.json').write_text(json.dumps({k:{z:v[z] for z in ['curve_monthly','closed_month','entry_month']} for k,v in out.items() if k in ['K_B','K_C']},indent=None),encoding='utf8')

```