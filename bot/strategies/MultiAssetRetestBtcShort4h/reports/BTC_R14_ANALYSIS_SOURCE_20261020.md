# Análisis R14

Código final de tablas, conciliación y comparaciones. Lee exclusivamente snapshotscompletosinputs, escribeoutput. Importamodelsanteshelpersporcircularidad. Capturafinaldeequity enfinish_exclusivo conserva liquidación sobreúltimodato yseatribuyeperíodoanterior. El campo open_pl/total_open_trades puede ser fotografía anterior a liquidación: contrastar con tradesfinalesyequitybalance.

```python

import json, math
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import jesse.models
from jesse import helpers as jh

def stats(ts):
    vals=[float(t['PNL']) for t in ts]; pos=sum(x for x in vals if x>0); neg=-sum(x for x in vals if x<0)
    fee=sum(float(t['fee']) for t in ts)
    price=sum((float(t['exit_price'])-float(t['entry_price']))*abs(float(t['qty']))*(1 if t['type']=='long' else -1) for t in ts)
    return dict(trades=len(ts),net=sum(vals),fee=fee,price_pnl=price,pf=pos/neg if neg else None,wins=sum(x>0 for x in vals),reconciliation=price-fee-sum(vals))
def signature(t):return (t['symbol'],t['type'],t['opened_at'])
rows={}
for f in Path('inputs').glob('*.json'):
    if f.name=='manifest.json':continue
    d=json.load(f.open()); m=d['metrics']; ts=d['trades']; summary=d['summary'];name=f.stem
    assert summary['session_status']=='finished',name
    q=pd.DataFrame(next(x for x in d['equity_curve'] if x['name']=='Portfolio')['data']).sort_values('time')
    q['date']=pd.to_datetime(q.time,unit='s',utc=True)
    finish=pd.Timestamp(summary['form']['finish_date'],tz='UTC')
    q=q[q.date<=finish].copy()
    # The engine records final liquidation at the exclusive boundary using prior data.
    # Retain its cash/fee reconciliation and attribute it to the preceding period.
    q.loc[q.date==finish,'date']=finish-pd.Timedelta(nanoseconds=1)
    prev=float(m['starting_balance']); months=[]; years={}
    for month,g in q.groupby(q.date.dt.strftime('%Y-%m')):
        end=float(g.iloc[-1].value);months.append(dict(month=month,start=prev,end=end,pnl=end-prev,pct=100*(end/prev-1)));prev=end
    prev=float(m['starting_balance'])
    for year,g in q.groupby(q.date.dt.year):
        end=float(g.iloc[-1].value);years[str(year)]=dict(start=prev,end=end,pct=100*(end/prev-1));prev=end
    full=[x for x in months if '2020-11'<=x['month']<='2025-11']
    groups={sym+' '+side:stats([t for t in ts if t['symbol']==sym and t['type']==side]) for sym,side in sorted(set((t['symbol'],t['type']) for t in ts))}
    total=stats(ts)
    assert abs(total['net']-m['net_profit'])<1e-6,name
    assert abs(total['reconciliation'])<1e-6,name
    best=sorted((float(t['PNL']) for t in ts),reverse=True)
    end=float(q.iloc[-1].value)
    row=dict(name=name,url=summary.get('dashboard_url'),metrics=m,total=total,groups=groups,months=months,years=years,full_months=len(full),positive_full_months=sum(x['pnl']>1e-7 for x in full),terminal_curve=end,terminal_balance=float(m['finishing_balance']),curve_balance_gap=end-float(m['finishing_balance']),recorded_open_pl=m.get('open_pl'),recorded_open_trades=m.get('total_open_trades'),net_without_best3_arithmetic=total['net']-sum(best[:3]),btc_signatures=[list(signature(t)) for t in ts if t['symbol']=='BTC-USDT'])
    row['btc_yearly_closed']={str(y):stats([t for t in ts if t['symbol']=='BTC-USDT' and datetime.fromtimestamp(t['closed_at']/1000,timezone.utc).year==y]) for y in range(2020,2026)}
    rows[name]=row
comparisons={}
for name,row in rows.items():
    if name.startswith('BASE'):continue
    _,p,fee=name.split('_')
    base=rows['BASE_'+p+'_'+fee]
    a=set(map(tuple,row['btc_signatures']));b=set(map(tuple,base['btc_signatures']))
    comparisons[name]=dict(net_ratio=row['total']['net']/base['total']['net'],delta_net=row['total']['net']-base['total']['net'],dd_delta=row['metrics']['max_drawdown']-base['metrics']['max_drawdown'],calmar_ratio=row['metrics']['calmar_ratio']/base['metrics']['calmar_ratio'],changed_btc_entries=len(a^b),removed_btc=len(b-a),added_btc=len(a-b),positive_month_delta=row['positive_full_months']-base['positive_full_months'],annual_return_deltas={str(y):row['years'][str(y)]['pct']-base['years'][str(y)]['pct'] for y in range(2021,2026)})
Path('output/results.json').write_text(json.dumps({'rows':rows,'comparisons':comparisons}),encoding='utf8')
compact={'rows':{k:{x:v[x] for x in ['url','total','groups','years','full_months','positive_full_months','terminal_curve','terminal_balance','curve_balance_gap','recorded_open_pl','recorded_open_trades','net_without_best3_arithmetic']}|{'cagr':v['metrics']['annual_return'],'dd':v['metrics']['max_drawdown'],'calmar':v['metrics']['calmar_ratio'],'sharpe':v['metrics']['sharpe_ratio']} for k,v in rows.items()},'comparisons':comparisons}
Path('output/compact.json').write_text(json.dumps(compact),encoding='utf8')
jh.debug(json.dumps({'names':list(rows),'comparisons':comparisons}))

```

# QA de fuente
```json
[
  {
    "variant": "BtcRefineR1401",
    "changed_methods": [
      "_signal",
      "terminate"
    ],
    "methods_preserved": 24,
    "compile": true
  },
  {
    "variant": "BtcRefineR1402",
    "changed_methods": [
      "_plan",
      "terminate"
    ],
    "methods_preserved": 24,
    "compile": true
  },
  {
    "variant": "BtcRefineR1403",
    "changed_methods": [
      "_plan",
      "terminate"
    ],
    "methods_preserved": 24,
    "compile": true
  }
]
```