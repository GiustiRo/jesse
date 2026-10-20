# R20 PAXG: fuente reproducible de los análisis

Sólo run_analysis con snapshots completos. No research scripts ni lecturas fuera de inputs/. Las métricas ausentes de cero operaciones no se fabrican. Estas sesiones tuvieron trades en los diez primarios. Las cohortes por cierre no son MTM.

## Mapa de diez sesiones

```json
[
  {
    "i": 1,
    "name": "R20PaxgARResponse4h",
    "id": "51a0c817-4c43-4940-ab0e-4bfec6b3a52c",
    "url": "http://localhost:9200/#/backtest/51a0c817-4c43-4940-ab0e-4bfec6b3a52c"
  },
  {
    "i": 2,
    "name": "R20PaxgPathAnalogue4h",
    "id": "a758809e-9d05-4e7e-a5b9-333751a19395",
    "url": "http://localhost:9200/#/backtest/a758809e-9d05-4e7e-a5b9-333751a19395"
  },
  {
    "i": 3,
    "name": "R20PaxgSpyDelayed1h",
    "id": "f72b8359-4531-42ff-8cc0-5b61a6f23320",
    "url": "http://localhost:9200/#/backtest/f72b8359-4531-42ff-8cc0-5b61a6f23320"
  },
  {
    "i": 4,
    "name": "R20PaxgDirectionalOvershoot1h",
    "id": "b8ee439b-4d96-46c3-8948-fca6eb59f5eb",
    "url": "http://localhost:9200/#/backtest/b8ee439b-4d96-46c3-8948-fca6eb59f5eb"
  },
  {
    "i": 5,
    "name": "R20PaxgRoundBarrier1h",
    "id": "43ec28da-525d-46d6-8c65-c641f32aa1d7",
    "url": "http://localhost:9200/#/backtest/43ec28da-525d-46d6-8c65-c641f32aa1d7"
  },
  {
    "i": 6,
    "name": "R20PaxgBreakevenRevisit4h",
    "id": "351eb0d1-160b-4079-a4d6-7aa50fec5ed4",
    "url": "http://localhost:9200/#/backtest/351eb0d1-160b-4079-a4d6-7aa50fec5ed4"
  },
  {
    "i": 7,
    "name": "R20PaxgStaircase4h",
    "id": "ffc75a3c-81cb-43cd-8b2f-65fb2201d19b",
    "url": "http://localhost:9200/#/backtest/ffc75a3c-81cb-43cd-8b2f-65fb2201d19b"
  },
  {
    "i": 8,
    "name": "R20PaxgSemivariance4h",
    "id": "842e4385-1c19-4f61-b5d5-acd8f96c9ce9",
    "url": "http://localhost:9200/#/backtest/842e4385-1c19-4f61-b5d5-acd8f96c9ce9"
  },
  {
    "i": 9,
    "name": "R20PaxgTrendExhaustion4h",
    "id": "f081dc32-7dc3-4f28-9a60-77275d6c155c",
    "url": "http://localhost:9200/#/backtest/f081dc32-7dc3-4f28-9a60-77275d6c155c"
  },
  {
    "i": 10,
    "name": "R20PaxgMonthEndRebalance1h",
    "id": "105bd7cf-90dd-454a-b2f8-8942dad5e30f",
    "url": "http://localhost:9200/#/backtest/105bd7cf-90dd-454a-b2f8-8942dad5e30f"
  }
]
```

Comparadores: retest=93a16137-e819-41a3-b325-0631a6627a6c; weekend=ff199ebe-dab0-4c09-9078-fff98188e97c. Cada input es session_type=backtest, session_id según mapa y name exp01..exp10 o retest/weekend.

## Batch1:01–05 y ambos comparadores

Job5dba914705be496b8fce366a8cb0d72d succeeded.

```python
import json, math
from collections import defaultdict, Counter
import numpy as np
import pandas as pd

names=["exp01","exp02","exp03","exp04","exp05","retest","weekend"]
results={}
for name in names:
    d=json.load(open('inputs/'+name+'.json'))
    summary=d.get('summary',{})
    assert summary.get('session_status')=='finished', summary
    m=d.get('metrics') or {};trades=d.get('trades') or []
    form=summary.get('form',{})
    sample_hours=None;finish_ms=None
    if form.get('start_date') and form.get('finish_date'):
        start=pd.Timestamp(form['start_date'],tz='UTC');finish=pd.Timestamp(form['finish_date'],tz='UTC')
        sample_hours=(finish-start).total_seconds()/3600
        finish_ms=int(finish.timestamp()*1000)
    row={'session_id':summary.get('session_id'),'title':summary.get('title'),'trades':len(trades),
         'stored_metrics':m,'directions':{},'closed_year_cohorts_not_MTM':{},
         'status':'no_operations' if not trades else 'economic_result'}
    if not trades:
        row['note']='No completed trades. Missing or shortened metrics are not reconstructed as returns or drawdown.'
        row['audit']={'executed_trade_records':0}
        results[name]=row
        print(name,json.dumps(row,sort_keys=True))
        continue
    pnls=[];fees=[];notionals=[];fill_notionals=[];hours=[];bydir=defaultdict(list);byyear=defaultdict(list);orders=Counter()
    mfe=mpn=mq=0.;last_close=None;overlaps=0;terminal=[]
    for t in sorted(trades,key=lambda x:(x['opened_at'],x['id'])):
        net=float(t['PNL']);fee=float(t['fee']);q=abs(float(t['qty']));ep=float(t['entry_price'])
        opened=float(t['opened_at']);closed=float(t['closed_at'])
        if last_close is not None:overlaps+=int(opened<last_close)
        last_close=closed
        ins=[o for o in t['orders'] if o['status']=='EXECUTED' and not o['reduce_only']]
        outs=[o for o in t['orders'] if o['status']=='EXECUTED' and o['reduce_only']]
        iq=sum(abs(float(o.get('filled_qty') or o['qty'])) for o in ins)
        oq=sum(abs(float(o.get('filled_qty') or o['qty'])) for o in outs)
        inc=sum(abs(float(o.get('filled_qty') or o['qty']))*float(o['price']) for o in ins)
        outc=sum(abs(float(o.get('filled_qty') or o['qty']))*float(o['price']) for o in outs)
        sign=1 if t['type']=='long' else -1
        mfe=max(mfe,abs(.00045*(inc+outc)-fee));mpn=max(mpn,abs(sign*(outc-inc)-fee-net));mq=max(mq,abs(iq-q),abs(oq-q))
        for o in ins+outs:orders[('entry_' if not o['reduce_only'] else 'exit_')+o['type']]+=1
        holding=(closed-opened)/3600000
        pnls.append(net);fees.append(fee);notionals.append(ep*q);fill_notionals.append(inc+outc);hours.append(holding)
        bydir[t['type']].append((net,fee,ep*q,inc+outc))
        byyear[str(pd.Timestamp(closed,unit='ms',tz='UTC').year)].append((net,inc+outc))
        if finish_ms is not None and closed==finish_ms:terminal.append({'type':t['type'],'gross':net+fee,'net':net,'hours':holding})
    assert overlaps==0 and mfe<1e-6 and mpn<1e-6 and mq<1e-7
    net=math.fsum(pnls);fee=math.fsum(fees);notional=math.fsum(notionals);fill_total=math.fsum(fill_notionals)
    losses=abs(sum(p for p in pnls if p<0));wins=sum(p for p in pnls if p>0)
    pf=wins/losses if losses>0 else None
    starting=m.get('starting_balance');finishing=m.get('finishing_balance')
    wallet_error=None
    if starting is not None and finishing is not None:
        wallet_error=float(starting)+net-float(finishing)
        assert abs(wallet_error)<1e-6
    top3=sum(sorted(pnls,reverse=True)[:3])
    for direction,items in bydir.items():
        row['directions'][direction]={'n':len(items),'net':sum(x[0] for x in items),'fees':sum(x[1] for x in items),
                                     'before_fees':sum(x[0]+x[1] for x in items)}
    for year,items in sorted(byyear.items()):
        yn=sum(x[0] for x in items);yf=sum(x[1] for x in items)
        row['closed_year_cohorts_not_MTM'][year]={'n':len(items),'net':yn,'static_5bps_RT':yn-.00025*yf,'static_10bps_RT':yn-.0005*yf}
    recent=[x for y,items in byyear.items() if int(y)>=2023 for x in items]
    curve=d.get('equity_curve') or []
    clocks=Counter()
    for series in curve:
        if series.get('name')=='Portfolio':
            clocks=Counter(pd.to_datetime(p['time'],unit='s',utc=True).strftime('%H:%M:%S') for p in series.get('data',[]))
    dd=m.get('max_drawdown')
    gate=net>0 and (pf is not None and pf>=1.2 or losses==0) and len(trades)>=30 and dd is not None and float(dd)>=-25
    row.update({'net':net,'fees':fee,'before_fees':net+fee,'pf_net':pf,'no_losses':losses==0,
        'dd_engine':dd,'cagr_engine':m.get('annual_return'),'sharpe_engine':m.get('sharpe_ratio'),
        'entry_notional_sum':notional,'executed_fill_notional_sum':fill_total,'net_bps_entry_notional':net/notional*1e4,
        'before_fee_bps_entry_notional':(net+fee)/notional*1e4,'extra_5bps_RT_all_fills_static':net-.00025*fill_total,
        'extra_10bps_RT_all_fills_static':net-.0005*fill_total,
        'top3_net':top3,'top3_share_of_net':top3/net if net>0 else None,'net_ex_top3_descriptive':net-top3,
        'mean_hold_hours':float(np.mean(hours)),'median_hold_hours':float(np.median(hours)),
        'max_hold_hours':max(hours),'holding_hours':sum(hours),'time_exposure_pct':sum(hours)/sample_hours*100 if sample_hours else None,
        'recent_closed_cohort_2023_2025':sum(x[0] for x in recent),
        'recent_static_5bps_RT':sum(x[0]-.00025*x[1] for x in recent),'recent_static_10bps_RT':sum(x[0]-.0005*x[1] for x in recent),
        'descriptive_initial_gate_pass':gate,'sample_inconclusive':len(trades)<30,
        'terminal':terminal,'curve_clock_counts':dict(clocks),
        'audit':{'max_fee_error':mfe,'max_pnl_error':mpn,'max_qty_error':mq,'wallet_error':wallet_error,'overlaps':overlaps,'ordertypes':dict(orders)}})
    results[name]=row
    print(name,json.dumps(row,sort_keys=True))
json.dump(results,open('output/r20_audit.json','w'),indent=2)

```

## Batch2:06–10 y ambos comparadores

Joba703e1e367cf4d868defe61e9dc17a7c succeeded. Mismo análisis con comprobación adicional de contador terminal cuando es distinto de cero.

```python
import json, math
from collections import defaultdict, Counter
import numpy as np
import pandas as pd

names=["exp06","exp07","exp08","exp09","exp10","retest","weekend"]
results={}
for name in names:
    d=json.load(open('inputs/'+name+'.json'))
    summary=d.get('summary',{})
    assert summary.get('session_status')=='finished', summary
    m=d.get('metrics') or {};trades=d.get('trades') or []
    form=summary.get('form',{})
    sample_hours=None;finish_ms=None
    if form.get('start_date') and form.get('finish_date'):
        start=pd.Timestamp(form['start_date'],tz='UTC');finish=pd.Timestamp(form['finish_date'],tz='UTC')
        sample_hours=(finish-start).total_seconds()/3600
        finish_ms=int(finish.timestamp()*1000)
    row={'session_id':summary.get('session_id'),'title':summary.get('title'),'trades':len(trades),
         'stored_metrics':m,'directions':{},'closed_year_cohorts_not_MTM':{},
         'status':'no_operations' if not trades else 'economic_result'}
    if not trades:
        row['note']='No completed trades. Missing or shortened metrics are not reconstructed as returns or drawdown.'
        row['audit']={'executed_trade_records':0}
        results[name]=row
        print(name,json.dumps(row,sort_keys=True))
        continue
    pnls=[];fees=[];notionals=[];fill_notionals=[];hours=[];bydir=defaultdict(list);byyear=defaultdict(list);orders=Counter()
    mfe=mpn=mq=0.;last_close=None;overlaps=0;terminal=[]
    for t in sorted(trades,key=lambda x:(x['opened_at'],x['id'])):
        net=float(t['PNL']);fee=float(t['fee']);q=abs(float(t['qty']));ep=float(t['entry_price'])
        opened=float(t['opened_at']);closed=float(t['closed_at'])
        if last_close is not None:overlaps+=int(opened<last_close)
        last_close=closed
        ins=[o for o in t['orders'] if o['status']=='EXECUTED' and not o['reduce_only']]
        outs=[o for o in t['orders'] if o['status']=='EXECUTED' and o['reduce_only']]
        iq=sum(abs(float(o.get('filled_qty') or o['qty'])) for o in ins)
        oq=sum(abs(float(o.get('filled_qty') or o['qty'])) for o in outs)
        inc=sum(abs(float(o.get('filled_qty') or o['qty']))*float(o['price']) for o in ins)
        outc=sum(abs(float(o.get('filled_qty') or o['qty']))*float(o['price']) for o in outs)
        sign=1 if t['type']=='long' else -1
        mfe=max(mfe,abs(.00045*(inc+outc)-fee));mpn=max(mpn,abs(sign*(outc-inc)-fee-net));mq=max(mq,abs(iq-q),abs(oq-q))
        for o in ins+outs:orders[('entry_' if not o['reduce_only'] else 'exit_')+o['type']]+=1
        holding=(closed-opened)/3600000
        pnls.append(net);fees.append(fee);notionals.append(ep*q);fill_notionals.append(inc+outc);hours.append(holding)
        bydir[t['type']].append((net,fee,ep*q,inc+outc))
        byyear[str(pd.Timestamp(closed,unit='ms',tz='UTC').year)].append((net,inc+outc))
        if finish_ms is not None and closed==finish_ms:terminal.append({'type':t['type'],'gross':net+fee,'net':net,'hours':holding})
    assert overlaps==0 and mfe<1e-6 and mpn<1e-6 and mq<1e-7
    net=math.fsum(pnls);fee=math.fsum(fees);notional=math.fsum(notionals);fill_total=math.fsum(fill_notionals)
    losses=abs(sum(p for p in pnls if p<0));wins=sum(p for p in pnls if p>0)
    pf=wins/losses if losses>0 else None
    starting=m.get('starting_balance');finishing=m.get('finishing_balance')
    wallet_error=None
    if starting is not None and finishing is not None:
        wallet_error=float(starting)+net-float(finishing)
        assert abs(wallet_error)<1e-6
    top3=sum(sorted(pnls,reverse=True)[:3])
    for direction,items in bydir.items():
        row['directions'][direction]={'n':len(items),'net':sum(x[0] for x in items),'fees':sum(x[1] for x in items),
                                     'before_fees':sum(x[0]+x[1] for x in items)}
    for year,items in sorted(byyear.items()):
        yn=sum(x[0] for x in items);yf=sum(x[1] for x in items)
        row['closed_year_cohorts_not_MTM'][year]={'n':len(items),'net':yn,'static_5bps_RT':yn-.00025*yf,'static_10bps_RT':yn-.0005*yf}
    recent=[x for y,items in byyear.items() if int(y)>=2023 for x in items]
    curve=d.get('equity_curve') or []
    clocks=Counter()
    for series in curve:
        if series.get('name')=='Portfolio':
            clocks=Counter(pd.to_datetime(p['time'],unit='s',utc=True).strftime('%H:%M:%S') for p in series.get('data',[]))
    dd=m.get('max_drawdown')
    gate=net>0 and (pf is not None and pf>=1.2 or losses==0) and len(trades)>=30 and dd is not None and float(dd)>=-25
    counter=int(m.get('total_open_trades') or 0)
    terminal_gross=math.fsum(t['gross'] for t in terminal)
    if counter:
        assert len(terminal)==counter and abs(terminal_gross-float(m.get('open_pl') or 0))<1e-6
    row['terminal_counter_reconciled']=bool(counter and len(terminal)==counter)
    row.update({'net':net,'fees':fee,'before_fees':net+fee,'pf_net':pf,'no_losses':losses==0,
        'dd_engine':dd,'cagr_engine':m.get('annual_return'),'sharpe_engine':m.get('sharpe_ratio'),
        'entry_notional_sum':notional,'executed_fill_notional_sum':fill_total,'net_bps_entry_notional':net/notional*1e4,
        'before_fee_bps_entry_notional':(net+fee)/notional*1e4,'extra_5bps_RT_all_fills_static':net-.00025*fill_total,
        'extra_10bps_RT_all_fills_static':net-.0005*fill_total,
        'top3_net':top3,'top3_share_of_net':top3/net if net>0 else None,'net_ex_top3_descriptive':net-top3,
        'mean_hold_hours':float(np.mean(hours)),'median_hold_hours':float(np.median(hours)),
        'max_hold_hours':max(hours),'holding_hours':sum(hours),'time_exposure_pct':sum(hours)/sample_hours*100 if sample_hours else None,
        'recent_closed_cohort_2023_2025':sum(x[0] for x in recent),
        'recent_static_5bps_RT':sum(x[0]-.00025*x[1] for x in recent),'recent_static_10bps_RT':sum(x[0]-.0005*x[1] for x in recent),
        'descriptive_initial_gate_pass':gate,'sample_inconclusive':len(trades)<30,
        'terminal':terminal,'curve_clock_counts':dict(clocks),
        'audit':{'max_fee_error':mfe,'max_pnl_error':mpn,'max_qty_error':mq,'wallet_error':wallet_error,'overlaps':overlaps,'ordertypes':dict(orders)}})
    results[name]=row
    print(name,json.dumps(row,sort_keys=True))
json.dump(results,open('output/r20_audit.json','w'),indent=2)

```
