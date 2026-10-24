# R40 PAXG: fuentes reproducibles de auditoría

Sólo snapshots de sesiones existentes. Las fechas/cohortes no se presentan como MTM. Los artefactos temporales pueden caducar; este reporte conserva código exacto e identidades de inputs para reproducir. No es archivo ejecutable nuevo ni research script. No acceder a DB, FS externo, red, credenciales o velas desde análisis.

## Batch 1, job cf816b2073384def8a7883458bc592ed

Inputs:

```json
[
  {
    "name": "paxg01",
    "session_id": "3db140a6-e6a4-4f41-b8f3-c79537cedc47",
    "session_type": "backtest"
  },
  {
    "name": "paxg02",
    "session_id": "6ac794c8-450c-446d-8db8-b2b1b65e8091",
    "session_type": "backtest"
  },
  {
    "name": "paxg03",
    "session_id": "a62ef27f-e5d3-42ab-b877-f762891a1a50",
    "session_type": "backtest"
  },
  {
    "name": "paxg04",
    "session_id": "b2aaf16b-e9fe-43cc-9a72-bdf189f3ae66",
    "session_type": "backtest"
  },
  {
    "name": "paxg05",
    "session_id": "32f7e55f-2dca-476d-87f2-4037bb97c71d",
    "session_type": "backtest"
  },
  {
    "name": "baseline",
    "session_id": "93a16137-e819-41a3-b325-0631a6627a6c",
    "session_type": "backtest"
  },
  {
    "name": "weekend075",
    "session_id": "ff199ebe-dab0-4c09-9078-fff98188e97c",
    "session_type": "backtest"
  }
]
```

Código exacto:

```python
import json, math
from collections import defaultdict, Counter
import numpy as np
import pandas as pd

names=["paxg01","paxg02","paxg03","paxg04","paxg05","baseline","weekend075"]
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
    entry_times=[];exit_times=[];entry_hours=Counter();entry_hours_ny=Counter()
    pnls=[];fees=[];notionals=[];fill_notionals=[];hours=[];bydir=defaultdict(list);byyear=defaultdict(list);orders=Counter()
    mfe=mpn=mq=0.;last_close=None;overlaps=0;terminal=[]
    for t in sorted(trades,key=lambda x:(x['opened_at'],x['id'])):
        net=float(t['PNL']);fee=float(t['fee']);q=abs(float(t['qty']));ep=float(t['entry_price'])
        opened=float(t['opened_at']);closed=float(t['closed_at'])
        entry_times.append(opened);exit_times.append(closed)
        ot=pd.Timestamp(opened,unit='ms',tz='UTC')
        entry_hours[ot.strftime('%H:%M')]+=1
        entry_hours_ny[ot.tz_convert('America/New_York').strftime('%H:%M')]+=1
        if finish_ms is not None: assert closed<=finish_ms and opened<finish_ms
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
        'first_entry_UTC':pd.Timestamp(min(entry_times),unit='ms',tz='UTC').isoformat(),
        'last_entry_UTC':pd.Timestamp(max(entry_times),unit='ms',tz='UTC').isoformat(),
        'last_exit_UTC':pd.Timestamp(max(exit_times),unit='ms',tz='UTC').isoformat(),
        'cash_before_first_fill_hours_not_only_warmup':(min(entry_times)/1000-start.timestamp())/3600 if sample_hours else None,
        'entry_hours_UTC':dict(entry_hours),'entry_hours_New_York':dict(entry_hours_ny),
        'terminal':terminal,'curve_clock_counts':dict(clocks),
        'audit':{'max_fee_error':mfe,'max_pnl_error':mpn,'max_qty_error':mq,'wallet_error':wallet_error,'overlaps':overlaps,'ordertypes':dict(orders)}})
    results[name]=row
    print(name,json.dumps(row,sort_keys=True))
json.dump(results,open('output/r40_audit.json','w'),indent=2)

```

## Batch 2, job 86c6c77a0a3849b2802c5f25a4123724

Inputs:

```json
[
  {
    "name": "paxg06",
    "session_id": "a7ca74dc-e111-40fa-8162-f1500eb87f38",
    "session_type": "backtest"
  },
  {
    "name": "paxg07",
    "session_id": "08061fce-e885-4526-b668-5094344a6644",
    "session_type": "backtest"
  },
  {
    "name": "paxg08",
    "session_id": "14455aed-0be2-43e2-83de-28df5dc840b8",
    "session_type": "backtest"
  },
  {
    "name": "paxg09",
    "session_id": "4622a9da-cfc0-45c5-a223-44aad68e1ce0",
    "session_type": "backtest"
  },
  {
    "name": "paxg10",
    "session_id": "da3e6ee6-b6f6-4764-a5aa-724d604ab75f",
    "session_type": "backtest"
  },
  {
    "name": "paxg02",
    "session_id": "6ac794c8-450c-446d-8db8-b2b1b65e8091",
    "session_type": "backtest"
  },
  {
    "name": "baseline",
    "session_id": "93a16137-e819-41a3-b325-0631a6627a6c",
    "session_type": "backtest"
  },
  {
    "name": "weekend075",
    "session_id": "ff199ebe-dab0-4c09-9078-fff98188e97c",
    "session_type": "backtest"
  }
]
```

Código exacto:

```python
import json, math
from collections import defaultdict, Counter
import numpy as np
import pandas as pd

names=["paxg06","paxg07","paxg08","paxg09","paxg10","paxg02","baseline","weekend075"]
results={}
nominal_hours={'paxg02':4,'paxg06':48,'paxg07':120,'paxg08':72,'paxg09':48,'paxg10':120}
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
    overdue=[]
    entry_times=[];exit_times=[];entry_hours=Counter();entry_hours_ny=Counter()
    pnls=[];fees=[];notionals=[];fill_notionals=[];hours=[];bydir=defaultdict(list);byyear=defaultdict(list);orders=Counter()
    mfe=mpn=mq=0.;last_close=None;overlaps=0;terminal=[]
    for t in sorted(trades,key=lambda x:(x['opened_at'],x['id'])):
        net=float(t['PNL']);fee=float(t['fee']);q=abs(float(t['qty']));ep=float(t['entry_price'])
        opened=float(t['opened_at']);closed=float(t['closed_at'])
        entry_times.append(opened);exit_times.append(closed)
        ot=pd.Timestamp(opened,unit='ms',tz='UTC')
        entry_hours[ot.strftime('%H:%M')]+=1
        entry_hours_ny[ot.tz_convert('America/New_York').strftime('%H:%M')]+=1
        if finish_ms is not None: assert closed<=finish_ms and opened<finish_ms
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
        if name in nominal_hours and holding>nominal_hours[name]+1e-9:
            overdue.append({'opened_at':opened,'closed_at':closed,'hours':holding,'type':t['type'],'net':net})
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
        'first_entry_UTC':pd.Timestamp(min(entry_times),unit='ms',tz='UTC').isoformat(),
        'last_entry_UTC':pd.Timestamp(max(entry_times),unit='ms',tz='UTC').isoformat(),
        'last_exit_UTC':pd.Timestamp(max(exit_times),unit='ms',tz='UTC').isoformat(),
        'cash_before_first_fill_hours_not_only_warmup':(min(entry_times)/1000-start.timestamp())/3600 if sample_hours else None,
        'entry_hours_UTC':dict(entry_hours),'entry_hours_New_York':dict(entry_hours_ny),
        'holding_above_nominal_records':overdue,
        'terminal':terminal,'curve_clock_counts':dict(clocks),
        'audit':{'max_fee_error':mfe,'max_pnl_error':mpn,'max_qty_error':mq,'wallet_error':wallet_error,'overlaps':overlaps,'ordertypes':dict(orders)}})
    results[name]=row
    print(name,json.dumps(row,sort_keys=True))
json.dump(results,open('output/r40_audit.json','w'),indent=2)

```
