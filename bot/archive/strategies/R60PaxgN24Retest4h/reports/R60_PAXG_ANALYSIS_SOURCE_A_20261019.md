# R60 PAXG: análisis A reproducible

Sólo snapshots completos. Auditorías fills, fees, PnL, wallet, exposición, concentración, cohortes por cierre (no MTM), intersecciones seleccionadas y fingerprints sin IDs. Artefactos cada uno <50000 bytes, sin truncado.

```json
[
  {
    "session_type": "backtest",
    "session_id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
    "name": "Cq"
  },
  {
    "session_type": "backtest",
    "session_id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
    "name": "M"
  },
  {
    "session_type": "backtest",
    "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
    "name": "P1_Cq"
  },
  {
    "session_type": "backtest",
    "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
    "name": "P1_M"
  },
  {
    "session_type": "backtest",
    "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
    "name": "P2_Cq"
  },
  {
    "session_type": "backtest",
    "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
    "name": "P2_M"
  },
  {
    "session_type": "backtest",
    "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
    "name": "P3_Cq"
  },
  {
    "session_type": "backtest",
    "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
    "name": "P3_M"
  }
]
```

```python
import json, math, hashlib
from collections import defaultdict, Counter
import numpy as np
import pandas as pd

names=["Cq","M","P1_Cq","P1_M","P2_Cq","P2_M","P3_Cq","P3_M"]
results={}
datasets={}
paired_results={}
origin_pairs={}
for name in names:
    d=json.load(open('inputs/'+name+'.json'))
    datasets[name]=d
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
    notional_hours=0.0
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
        notional_hours+=ep*q*holding
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
    terminal_check={'stored_open_count':m.get('total_open_trades'),'stored_open_pl':m.get('open_pl'),'terminal_records':len(terminal)}
    if m.get('total_open_trades',0):
        assert int(m['total_open_trades'])==len(terminal)==1,(name,terminal_check)
        error=abs(sum(x['gross'] for x in terminal)-float(m.get('open_pl',0)))
        assert error<1e-6,(name,'terminal counter mismatch',error)
        terminal_check['gross_open_pl_error']=error
        terminal_check['note']='Pretermination counter reconciled with fully closed synthetic boundary trade; not proof of native liquidity.'
    dd=m.get('max_drawdown')
    gate=net>0 and (pf is not None and pf>=1.2 or losses==0) and len(trades)>=30 and dd is not None and float(dd)>=-25
    row.update({'net':net,'fees':fee,'before_fees':net+fee,'pf_net':pf,'no_losses':losses==0,
        'dd_engine':dd,'cagr_engine':m.get('annual_return'),'sharpe_engine':m.get('sharpe_ratio'),
        'entry_notional_sum':notional,
        'entry_notional_hours':notional_hours,
        'entry_price_notional_time_proxy_vs_initial_capital':notional_hours/(10000*sample_hours) if sample_hours else None,
        'mean_entry_notional_vs_initial_capital':float(np.mean(notionals))/10000,
        'max_entry_notional_vs_initial_capital':max(notionals)/10000,'executed_fill_notional_sum':fill_total,'net_bps_entry_notional':net/notional*1e4,
        'before_fee_bps_entry_notional':(net+fee)/notional*1e4,'extra_5bps_RT_all_fills_static':net-.00025*fill_total,
        'extra_10bps_RT_all_fills_static':net-.0005*fill_total,
        'net_ex_best_descriptive':net-max(pnls),
        'best_trade_net':max(pnls),'top3_net':top3,'top3_share_of_net':top3/net if net>0 else None,'net_ex_top3_descriptive':net-top3,
        'mean_hold_hours':float(np.mean(hours)),'median_hold_hours':float(np.median(hours)),
        'max_hold_hours':max(hours),'holding_hours':sum(hours),'time_exposure_pct':sum(hours)/sample_hours*100 if sample_hours else None,
        'recent_closed_cohort_2023_2025':sum(x[0] for x in recent),
        'recent_static_5bps_RT':sum(x[0]-.00025*x[1] for x in recent),'recent_static_10bps_RT':sum(x[0]-.0005*x[1] for x in recent),
        'trading_screen_context_only_not_attribution_decision':gate,'sample_under30_descriptive':len(trades)<30,
        'first_entry_UTC':pd.Timestamp(min(entry_times),unit='ms',tz='UTC').isoformat(),
        'last_entry_UTC':pd.Timestamp(max(entry_times),unit='ms',tz='UTC').isoformat(),
        'last_exit_UTC':pd.Timestamp(max(exit_times),unit='ms',tz='UTC').isoformat(),
        'cash_before_first_fill_hours_not_only_warmup':(min(entry_times)/1000-start.timestamp())/3600 if sample_hours else None,
        'entry_hours_UTC':dict(entry_hours),'entry_hours_New_York':dict(entry_hours_ny),
        'terminal_counter_reconciliation':terminal_check,'terminal':terminal,'curve_clock_counts':dict(clocks),
        'audit':{'max_fee_error':mfe,'max_pnl_error':mpn,'max_qty_error':mq,'wallet_error':wallet_error,'overlaps':overlaps,'ordertypes':dict(orders)}})
    def economic_trade(t):
        return {k:t.get(k) for k in ['symbol','type','entry_price','exit_price','qty','opened_at','closed_at','fee','PNL']} | {'executed_orders':[{k:o.get(k) for k in ['type','side','reduce_only','qty','filled_qty','price','created_at','executed_at']} for o in t['orders'] if o['status']=='EXECUTED']}
    canonical=[economic_trade(t) for t in sorted(trades,key=lambda x:(x['opened_at'],x['closed_at']))]
    row['economic_fills_sha256']=hashlib.sha256(json.dumps(canonical,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    row['stored_equity_curve_sha256']=hashlib.sha256(json.dumps(d.get('equity_curve'),sort_keys=True,separators=(',',':')).encode()).hexdigest()
    results[name]=row
    print(name,round(net,4),len(trades),round(fee,4))
# Exact executed-entry matches are conditional subsets, not causal matched opportunities.
pair_specs=[('Cq','M')]+[('P'+str(i)+'_Cq','P'+str(i)+'_M') for i in range(1,6)]
for left,right in pair_specs:
    if left not in datasets or right not in datasets:
        continue
    def entries(name):
        out={}
        for t in datasets[name].get('trades',[]):
            key=(t['symbol'],t['type'],int(t['opened_at']))
            assert key not in out,(name,key)
            notional=abs(float(t['qty']))*float(t['entry_price'])
            out[key]={'PNL':float(t['PNL']),'entry_notional':notional,
                      'PNL_per_entry_notional':float(t['PNL'])/notional,
                      'entry_price':float(t['entry_price']),'qty':abs(float(t['qty'])),
                      'closed_at':t['closed_at']}
        return out
    aa,bb=entries(left),entries(right)
    common=sorted(set(aa).intersection(bb))
    records=[]
    for key in common:
        x,y=aa[key],bb[key]
        records.append({'symbol':key[0],'type':key[1],'opened_at':key[2],
                        'left':x,'right':y,
                        'normalized_PNL_difference_right_minus_left':y['PNL_per_entry_notional']-x['PNL_per_entry_notional']})
    paired_results[left+'__'+right]={'left_n':len(aa),'right_n':len(bb),'common_n':len(common),
        'common_fraction_of_left':len(common)/len(aa) if aa else None,
        'common_fraction_of_right':len(common)/len(bb) if bb else None,
        'mean_normalized_PNL_difference_right_minus_left':float(np.mean([r['normalized_PNL_difference_right_minus_left'] for r in records])) if records else None,
        'records':records,
        'interpretation':'Actual executed-entry intersection only. Occupancy, capital and duration are endogenous; not pure causal effect.'}
# Secondary exact-order-origin link: selected double-fill subset only.
for left,right in pair_specs:
    if left not in datasets or right not in datasets:
        continue
    def origins(name):
        out={};ambiguous=set();skipped=0
        for t in datasets[name].get('trades',[]):
            ins=[o for o in t['orders'] if o['status']=='EXECUTED' and not o['reduce_only']]
            if len(ins)!=1 or ins[0].get('created_at') is None:
                skipped+=1
                continue
            created=float(ins[0]['created_at'])
            if not math.isfinite(created):
                skipped+=1
                continue
            key=(t['symbol'],t['type'],int(created))
            notional=abs(float(t['qty']))*float(t['entry_price'])
            row={'entry_price':float(t['entry_price']),'opened_at':t['opened_at'],
                 'closed_at':t['closed_at'],'created_at':created,
                 'fill_delay_hours':(float(t['opened_at'])-created)/3600000,
                 'PNL':float(t['PNL']),'entry_notional':notional,
                 'PNL_per_entry_notional':float(t['PNL'])/notional}
            if key in out:
                ambiguous.add(key)
            else:
                out[key]=row
        for key in ambiguous:
            out.pop(key,None)
        return out,{'skipped_multi_or_missing_entry':skipped,'ambiguous_keys':len(ambiguous)}
    aa,qa=origins(left);bb,qb=origins(right)
    common=sorted(set(aa).intersection(bb))
    records=[]
    for key in common:
        x,y=aa[key],bb[key]
        records.append({'symbol':key[0],'type':key[1],'created_at':key[2],
            'left':x,'right':y,
            'entry_price_difference_right_minus_left_bps':(y['entry_price']/x['entry_price']-1)*10000,
            'fill_delay_difference_right_minus_left_hours':y['fill_delay_hours']-x['fill_delay_hours'],
            'normalized_PNL_difference_right_minus_left':y['PNL_per_entry_notional']-x['PNL_per_entry_notional']})
    origin_pairs[left+'__'+right]={'left_eligible_filled':len(aa),'right_eligible_filled':len(bb),
        'left_exclusions':qa,'right_exclusions':qb,'common_origin_n':len(common),
        'mean_entry_price_difference_right_minus_left_bps':float(np.mean([r['entry_price_difference_right_minus_left_bps'] for r in records])) if records else None,
        'mean_fill_delay_difference_right_minus_left_hours':float(np.mean([r['fill_delay_difference_right_minus_left_hours'] for r in records])) if records else None,
        'mean_normalized_PNL_difference_right_minus_left':float(np.mean([r['normalized_PNL_difference_right_minus_left'] for r in records])) if records else None,
        'records':records,'interpretation':'Exact order-created-at, symbol and direction; unique double-filled subset only, not causal or opportunity universe.'}

def save_small(path,payload):
    data=json.dumps(payload,indent=2,allow_nan=False)
    assert len(data.encode())<50000,(path,len(data.encode()))
    open('output/'+path,'w').write(data)
compact={k:{kk:vv for kk,vv in v.items() if kk!='stored_metrics'} for k,v in results.items()}
ps={k:{kk:vv for kk,vv in v.items() if kk!='records'} for k,v in paired_results.items()}
os={k:{kk:vv for kk,vv in v.items() if kk!='records'} for k,v in origin_pairs.items()}
save_small('r60_summary.json',{'policies':compact,'pairs':ps,'origin_pairs':os})
for k,v in compact.items():save_small('row_'+k+'.json',v)
for k,v in paired_results.items():save_small('pair_'+k+'.json',v)
for k,v in origin_pairs.items():save_small('origin_'+k+'.json',v)
print('AUDIT_COMPLETE',len(results),len(ps))

```