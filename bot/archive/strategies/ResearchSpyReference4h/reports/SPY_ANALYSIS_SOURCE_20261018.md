# Código de análisis de snapshots completos

Reproducir con run_analysis y entradas completas de sesiones indicadas en informe final. Sólo inputs/ y output/. Las curvas son de motor salvo cuando el código demuestraflatdiario. RootV4esautoridadMTM paraestosruns.

## Apertura y referencia
```python
import json, math, collections
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
Path('output').mkdir(exist_ok=True)
NY=ZoneInfo('America/New_York')
FEE=.00045
summary={}
fig,ax=plt.subplots(figsize=(10,5))
for name in ('reference','orb','drive'):
    d=json.load(open('inputs/'+name+'.json'))
    t=d['trades'];m=d['metrics']
    pnls=np.array([float(v['PNL']) for v in t])
    notionals=np.array([float(v['entry_price'])*abs(float(v['qty'])) for v in t])
    round_notionals=np.array([(float(v['entry_price'])+float(v['exit_price']))*abs(float(v['qty'])) for v in t])
    fees=np.array([float(v['fee']) for v in t])
    assert math.isclose(pnls.sum(),m['net_profit'],abs_tol=1e-6)
    assert math.isclose(fees.sum(),m['fee'],abs_tol=1e-6)
    assert np.allclose(fees,FEE*round_notionals,rtol=1e-9,atol=1e-6)
    gross=np.array([(1 if v['type']=='long' else -1)*(v['exit_price']-v['entry_price'])*abs(v['qty']) for v in t])
    assert np.allclose(gross-fees,pnls,atol=1e-6)
    rows=[]
    boundary_cross=0
    duplicate_days=0
    days=set()
    entry_clock=collections.Counter()
    exit_clock=collections.Counter()
    order_types=collections.Counter()
    localyears=collections.Counter()
    cash_events=[]
    for v in t:
        opened=pd.to_datetime(v['opened_at'],unit='ms',utc=True)
        closed=pd.to_datetime(v['closed_at'],unit='ms',utc=True)
        local=opened.to_pydatetime().astimezone(NY)
        endlocal=closed.to_pydatetime().astimezone(NY)
        if opened.floor('D') != closed.floor('D'): boundary_cross+=1
        day=local.date().isoformat()
        if day in days:duplicate_days+=1
        days.add(day)
        entry_clock[local.strftime('%H:%M')]+=1
        exit_clock[endlocal.strftime('%H:%M')]+=1
        order_types.update(o['type'] for o in v['orders'] if o['status']=='EXECUTED')
        if name!='reference':
            assert local.weekday()<5
            clock=local.hour*60+local.minute
            assert clock==630 if name=='drive' else clock in (660,690,720)
        localyears[local.year]+=1
        rows.append({'side':v['type'],'pnl':v['PNL'],'notional':v['entry_price']*abs(v['qty']),'hours':v['holding_period']/3600})
        # Fill-based cash ledger: entry fee and exit gross less exit fee separately.
        # With all positions flat at daily boundaries, this equals daily-close MTM.
        for order in v['orders']:
            if order['status']!='EXECUTED':continue
            q=abs(float(order['filled_qty']))
            when=pd.to_datetime(order['executed_at'],unit='ms',utc=True)
            amount=-FEE*q*float(order['price'])
            if order['reduce_only']:
                amount+=(1 if v['type']=='long' else -1)*q*(float(order['price'])-float(v['entry_price']))
            cash_events.append((when,amount))
    frame=pd.DataFrame(rows)
    side=frame.groupby('side').agg(n=('pnl','size'),net=('pnl','sum'),notional=('notional','sum'),hours=('hours','sum')).to_dict('index') if rows else {}
    top=sorted(pnls,reverse=True)[:5]
    result={'n':len(t),'net':float(pnls.sum()),'fees':float(fees.sum()),'price_pnl':float(gross.sum()),'pf':float(pnls[pnls>0].sum()/-pnls[pnls<0].sum()),'annual_return_engine':m['annual_return'],'dd_engine':m['max_drawdown'],'net_bps_entry_notional':float(pnls.sum()/notionals.sum()*10000),'stress_samefills_5bpsRT':float((pnls-.00025*round_notionals).sum()),'stress_samefills_10bpsRT':float((pnls-.0005*round_notionals).sum()),'top5_pnl':top,'net_ex_top5':float(pnls.sum()-sum(top)),'side':side,'entry_clock_NY':dict(entry_clock),'exit_clock_NY':dict(exit_clock),'duplicate_entry_dates':duplicate_days,'boundary_crossing_trades':boundary_cross,'entry_years':dict(localyears),'executed_order_types':dict(order_types),'total_exposure_hours':sum(v['holding_period'] for v in t)/3600}
    result['crossing_examples']=[{'opened_at':v['opened_at'],'closed_at':v['closed_at'],'side':v['type'],'pnl':v['PNL']} for v in t if pd.to_datetime(v['opened_at'],unit='ms',utc=True).floor('D')!=pd.to_datetime(v['closed_at'],unit='ms',utc=True).floor('D')][:20]
    if name!='reference' and boundary_cross==0:
        assert duplicate_days==0
        daily=pd.Series(0.,index=pd.date_range('2020-10-15','2025-12-31',inclusive='left',tz='UTC'))
        for when,amount in cash_events:daily.loc[when.floor('D')]+=amount
        eq=10000+daily.cumsum()
        assert math.isclose(eq.iloc[-1],m['finishing_balance'],abs_tol=1e-6)
        month=eq.resample('M').last().pct_change()
        month.iloc[0]=eq.resample('M').last().iloc[0]/10000-1
        quarter=eq.resample('Q').last().pct_change()
        quarter.iloc[0]=eq.resample('Q').last().iloc[0]/10000-1
        year=eq.resample('Y').last().pct_change()
        year.iloc[0]=eq.resample('Y').last().iloc[0]/10000-1
        result.update(year_mtm={str(k.year):float(v) for k,v in year.items()},months_positive=int((month>1e-12).sum()),months_total=len(month),quarters_positive=int((quarter>1e-12).sum()),quarters_total=len(quarter),dd_daily_mtm=float((eq/eq.cummax()-1).min()*100),worst_month=float(month.min()*100),monthly_mtm={str(k.date()):float(v) for k,v in month.items()})
        eq.to_csv('output/'+name+'_daily_mtm.csv')
        ax.plot(eq.index,eq.values,label=name)
    else:
        series=next(s for s in d['equity_curve'] if s['name']=='Portfolio')
        # The engine curve is sampled about00:01, not UTC end-of-day. Plot only;
        # never use it to claim month-end MTM regularity for this multi-day control.
        curve=pd.DataFrame(series['data'])
        ax.plot(pd.to_datetime(curve['time'],unit='s',utc=True),curve['value'],label='reference(engine sampling)')
    summary[name]=result
    print(name,json.dumps(result,default=str))
ax.set_title('SPY isolated1%: daily MTM intraday policies; engine-sampled reference')
ax.legend();fig.tight_layout();fig.savefig('output/spy_equity.png',dpi=110);plt.close(fig)
json.dump(summary,open('output/spy_summary.json','w'),indent=2)

```

## Exposición lenta
```python
import json,math
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Path('output').mkdir(exist_ok=True)
out={}
fig,ax=plt.subplots(figsize=(10,5))
for name in ('defense','beta'):
 d=json.load(open('inputs/'+name+'.json'));t=d['trades'];m=d['metrics']
 p=np.array([v['PNL'] for v in t]);fees=np.array([v['fee'] for v in t])
 n=np.array([v['entry_price']*abs(v['qty']) for v in t])
 rn=np.array([(v['entry_price']+v['exit_price'])*abs(v['qty']) for v in t])
 assert math.isclose(p.sum(),m['net_profit'],abs_tol=1e-6)
 assert np.allclose(fees,.00045*rn,atol=1e-6)
 capital=10000.
 risks=[];grossx=[];records=[]
 for v in t:
  e=float(v['entry_price']);q=abs(v['qty']);stop=.9*e
  risk=q*(e-stop+.00045*(e+stop)+.001*e)/capital
  grossx.append(q*e/capital);risks.append(risk)
  assert risk<=.010000001
  opened=pd.to_datetime(v['opened_at'],unit='ms',utc=True)
  assert opened.hour==16 and opened.minute==0
  orders=[o for o in v['orders'] if o['status']=='EXECUTED']
  initialexit=[o for o in orders if o['reduce_only']]
  records.append({'opened':str(opened),'closed':str(pd.to_datetime(v['closed_at'],unit='ms',utc=True)),'entry':e,'exit':v['exit_price'],'pnl':v['PNL'],'fee':v['fee'],'initial_risk_fraction':risk,'initial_notional_equity':q*e/capital,'exit_types':[o['type'] for o in initialexit],'holding_days':v['holding_period']/86400})
  capital+=v['PNL']
 series=next(s for s in d['equity_curve'] if s['name']=='Portfolio')
 curve=pd.DataFrame(series['data'])
 ax.plot(pd.to_datetime(curve['time'],unit='s',utc=True),curve['value'],label=name)
 out[name]={'metrics':m,'pf':float(p[p>0].sum()/-p[p<0].sum()),'trades':records,'max_initial_risk_fraction':max(risks),'max_initial_notional_equity':max(grossx),'price_pnl':float((p+fees).sum()),'stress5bpsRT_samefills':float((p-.00025*rn).sum()),'stress10bpsRT_samefills':float((p-.0005*rn).sum()),'net_ex_top1':float(p.sum()-max(p)),'net_ex_top3':float(p.sum()-sum(sorted(p,reverse=True)[:3])),'exposure_hours':sum(v['holding_period'] for v in t)/3600,'net_bps_entry_notional':float(p.sum()/n.sum()*10000)}
 print(name,json.dumps(out[name]))
json.dump(out,open('output/slow_summary.json','w'),indent=2)
ax.set_title('SPY slow policies1%: engine-sampled equity (not UTC-close MTM)')
ax.legend();fig.tight_layout();fig.savefig('output/slow_equity_engine.png',dpi=110);plt.close(fig)

```
