# R3 corrective presentation source

Root authorized one correctivejob: same eight session inputs and economic calculations; only splitCSV<=40kB, rows/hash/reconstruction manifest added. Initial CSVretrieval hadtruncated=true andwasincorrectlylabelledcomplete; firstreportcorrectedexplicitly. No extra backtests/refit/2026.

```python

import json, math, hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def _fills(trade, fee_rate):
    """Validate one entry and fully closing exits, retaining each executed fill."""
    if trade['type'] not in ('long', 'short'):
        raise ValueError('Unsupported trade direction')
    if any(str(o.get('status')).upper() == 'PARTIALLY_FILLED' for o in trade['orders']):
        raise ValueError('Partially filled order snapshots are unsupported')
    executed = [o for o in trade['orders'] if str(o.get('status')).upper() == 'EXECUTED']
    entries = [o for o in executed if not bool(o.get('reduce_only'))]
    exits = [o for o in executed if bool(o.get('reduce_only'))]
    if len(entries) != 1 or not exits:
        raise ValueError('Exactly one entry and one or more complete exit fills required')
    ids = [o.get('id') for o in executed if o.get('id') is not None]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate executed order IDs')
    sign = 1 if trade['type'] == 'long' else -1
    entry_side = 'BUY' if sign == 1 else 'SELL'
    def unpack(order, side):
        # Jesse simulations can leave filled_qty at zero after full execution.
        # An EXECUTED order then uses its submitted qty; positive filled_qty wins.
        filled = abs(float(order.get('filled_qty') or 0))
        qty = filled if filled > 0 else abs(float(order['qty']))
        price = float(order['price'])
        stamp = order.get('executed_at')
        if stamp is None or qty <= 0 or price <= 0 or not np.isfinite(qty + price):
            raise ValueError('Invalid/missing executed fill economics')
        if str(order['side']).upper() != side:
            raise ValueError('Fill side inconsistent with position direction')
        return {'qty': qty, 'price': price, 'time': int(stamp),
                'fee': qty * price * fee_rate}
    entry = unpack(entries[0], entry_side)
    outgoing = sorted([unpack(o, 'SELL' if sign == 1 else 'BUY') for o in exits],
                      key=lambda o: o['time'])
    remaining = entry['qty']
    realized = -entry['fee']
    for fill in outgoing:
        if fill['time'] < entry['time']:
            raise ValueError('Exit precedes entry')
        remaining -= fill['qty']
        if remaining < -1e-8:
            raise ValueError('Exit quantities exceed opened position')
        realized += sign * fill['qty'] * (fill['price'] - entry['price']) - fill['fee']
    if not np.isclose(remaining, 0, rtol=0, atol=1e-8):
        raise ValueError('Closed trade does not fully close its entry quantity')
    if entry['time'] != int(trade['opened_at']) or outgoing[-1]['time'] != int(trade['closed_at']):
        raise ValueError('Trade lifecycle and fill timestamps disagree')
    expected_fee = entry['fee'] + sum(fill['fee'] for fill in outgoing)
    if not np.isclose(expected_fee, float(trade['fee']), rtol=1e-8, atol=1e-6):
        raise ValueError('Per-fill commissions do not reconcile to closed trade')
    if not np.isclose(realized, float(trade['PNL']), rtol=1e-8, atol=1e-6):
        raise ValueError('Per-fill realized PNL does not reconcile')
    return sign, entry, outgoing



def close(a,b,label):
    if not np.isclose(a,b,rtol=1e-8,atol=1e-6): raise AssertionError((label,a,b))

def summarize(rows):
    rows=list(rows)
    return {'n':len(rows),'net':math.fsum(r['net'] for r in rows),
            'gross':math.fsum(r['gross'] for r in rows),'fees':math.fsum(r['fee'] for r in rows),
            'wins':sum(r['net']>0 for r in rows),'losses':sum(r['net']<0 for r in rows),
            'zeros':sum(r['net']==0 for r in rows),
            'winning_pnl':math.fsum(r['net'] for r in rows if r['net']>0),
            'losing_pnl':math.fsum(r['net'] for r in rows if r['net']<0),
            'entry_notional':math.fsum(r['qty']*r['entry'] for r in rows),
            'entry_notional_hours':math.fsum(r['entry_notional_hours'] for r in rows),
            'two_side_turnover':math.fsum(r['turnover'] for r in rows)}
def union_ms(intervals):
    total=0;right=None
    for left,end in sorted(intervals):
        if right is None or left>right:total+=end-left;right=end
        elif end>right:total+=end-right;right=end
    return total
def normalize(s,name):
    form=s['summary']['form'];fee=float(form['config']['exchange']['fee'])
    assert form['start_date']=='2020-10-15' and form['finish_date']=='2025-12-31'
    assert form['config']['exchange']['balance']==10000
    assert form['config']['exchange']['futures_leverage']==5
    assert form['config']['exchange']['futures_leverage_mode']=='isolated'
    assert fee==(.00045 if name.startswith('nom') else .00070)
    assert s['summary']['session_status']=='finished'
    rows={};intervals=[];terminal=[]
    finish=int(pd.Timestamp('2025-12-31T00:00Z').timestamp()*1000)
    for trade in s['trades']:
        sign,entry,exits=_fills(trade,fee)
        opening=next(o for o in trade['orders'] if str(o['status']).upper()=='EXECUTED' and not o['reduce_only'])
        typ=str(opening['type']).upper()
        symbol=trade['symbol'];side=trade['type'];ts=int(trade['opened_at'])
        key=(symbol,side,ts)
        if key in rows:raise AssertionError(('duplicate match key',name,key))
        if symbol=='BTC-USDT' and side=='short':
            if typ not in ('MARKET','STOP'):raise AssertionError(('unexpected short type',typ))
            group='BTC supplemental MARKET' if typ=='MARKET' else 'BTC original STOP'
        elif symbol=='BTC-USDT':group='BTC original long'
        else:group=symbol+' original '+side
        qty=entry['qty'];net=float(trade['PNL']);gross=net+float(trade['fee'])
        # Actual remaining slices: each exited slice has its own holding duration.
        nh=sum(entry['price']*f['qty']*(f['time']-ts)/3600000 for f in exits)
        intervals.append((ts,exits[-1]['time']))
        if exits[-1]['time']==finish:
            terminal.append(sign*exits[-1]['qty']*(exits[-1]['price']-entry['price']))
        rows[key]={'group':group,'symbol':symbol,'side':side,'opened_at':ts,'closed_at':exits[-1]['time'],
                   'entry_type':typ,'entry':entry['price'],'exit':float(trade['exit_price']),'qty':qty,
                   'net':net,'fee':float(trade['fee']),'gross':gross,'unit_net':net/qty,
                   'unit_gross':gross/qty,'unit_fee':float(trade['fee'])/qty,
                   'holding_hours':(exits[-1]['time']-ts)/3600000,'entry_notional_hours':nh,
                   'turnover':qty*entry['price']+sum(f['qty']*f['price'] for f in exits),
                   'exit_signature':[(f['time'],f['price'],f['qty']/qty) for f in exits]}
    total=summarize(rows.values())
    close(total['net'],s['metrics']['net_profit'],name+' net')
    close(total['fees'],s['metrics']['fee'],name+' fees')
    close(10000+total['net'],s['metrics']['finishing_balance'],name+' wallet')
    n=int(s['metrics'].get('total_open_trades') or 0)
    if n:
        assert len(terminal)==n
        close(sum(terminal),float(s['metrics']['open_pl']),name+' preterminal openPL')
    span=(pd.Timestamp('2025-12-31',tz='UTC')-pd.Timestamp('2020-10-15',tz='UTC')).total_seconds()*1000
    total.update(any_position_pct=100*union_ms(intervals)/span,
                 entry_notional_time_initial_equity=total['entry_notional_hours']/(span/3600000)/10000,
                 terminal_preclose_count=n,terminal_reconciled=True)
    bygroup={g:summarize(r for r in rows.values() if r['group']==g) for g in sorted({r['group'] for r in rows.values()})}
    return rows,total,bygroup

def pair_compare(x,y,pair):
    common=sorted(set(x)&set(y));removed=sorted(set(x)-set(y));added=sorted(set(y)-set(x))
    records=[];effects=defaultdict(lambda:defaultdict(float))
    for k in common:
        a,b=x[k],y[k]
        # A different order family at identical timestamp is a distinct policy
        # event. Do not label it retained supplemental/original membership.
        group=a['group'] if a['group']==b['group'] else a['group']+' -> '+b['group']
        dq=b['qty']-a['qty'];avgq=(a['qty']+b['qty'])/2
        qty_effect=dq*(a['unit_net']+b['unit_net'])/2
        unit_effect=avgq*(b['unit_net']-a['unit_net'])
        gross_qty=dq*(a['unit_gross']+b['unit_gross'])/2
        gross_unit=avgq*(b['unit_gross']-a['unit_gross'])
        fee_qty=-dq*(a['unit_fee']+b['unit_fee'])/2
        fee_unit=-avgq*(b['unit_fee']-a['unit_fee'])
        delta=b['net']-a['net']
        close(qty_effect+unit_effect,delta,'matched midpoint net')
        close(gross_qty+fee_qty,qty_effect,'gross/fee quantity')
        close(gross_unit+fee_unit,unit_effect,'gross/fee unit')
        same_exit=a['exit_signature']==b['exit_signature']
        rec={'pair':pair,'membership':'retained','group':group,
             'symbol':k[0],'side':k[1],'opened_at':k[2],
             'x_closed_at':a['closed_at'],'n_closed_at':b['closed_at'],
             'x_qty':a['qty'],'n_qty':b['qty'],'x_entry':a['entry'],'n_entry':b['entry'],
             'x_exit':a['exit'],'n_exit':b['exit'],'x_net':a['net'],'n_net':b['net'],
             'delta_net':delta,'quantity_midpoint_effect':qty_effect,'unit_net_midpoint_effect':unit_effect,
             'gross_quantity_effect':gross_qty,'gross_unit_effect':gross_unit,
             'fee_quantity_effect':fee_qty,'fee_unit_effect':fee_unit,
             'same_entry_price':a['entry']==b['entry'],'same_exit_path':same_exit,
             'x_loser':a['net']<0,'n_loser':b['net']<0}
        records.append(rec)
        e=effects[group];e['retained_n']+=1;e['retained_x_net']+=a['net'];e['retained_n_net']+=b['net']
        e['retained_quantity_effect']+=qty_effect;e['retained_unit_effect']+=unit_effect
        e['retained_delta']+=delta;e['retained_same_exit']+=same_exit
        e['retained_x_losses']+=a['net']<0;e['retained_n_losses']+=b['net']<0
        e['retained_x_losing_pnl']+=min(0,a['net']);e['retained_n_losing_pnl']+=min(0,b['net'])
        e['retained_fee_qty']+=fee_qty;e['retained_fee_unit']+=fee_unit
    for membership,keys,source,sgn in [('removed',removed,x,-1),('added',added,y,1)]:
        for k in keys:
            a=source[k];group=a['group'];contrib=sgn*a['net'];e=effects[group]
            e[membership+'_n']+=1;e[membership+'_net']+=a['net']
            e[membership+'_signed_contribution']+=contrib
            e[membership+'_losses']+=a['net']<0;e[membership+'_losing_pnl']+=min(0,a['net'])
            records.append({'pair':pair,'membership':membership,'group':group,
                            'symbol':k[0],'side':k[1],'opened_at':k[2],'closed_at':a['closed_at'],
                            'qty':a['qty'],'net':a['net'],'fee':a['fee'],'gross':a['gross'],
                            'delta_net':contrib,'loser':a['net']<0})
    expected=sum(r['net'] for r in y.values())-sum(r['net'] for r in x.values())
    close(sum(r['delta_net'] for r in records),expected,pair+' full matched/add/remove sum')
    for g,e in effects.items():
        e['total_delta']=e.get('retained_delta',0)+e.get('added_signed_contribution',0)+e.get('removed_signed_contribution',0)
        close(e['retained_quantity_effect']+e['retained_unit_effect'],e['retained_delta'],pair+g+' midpoint')
    close(sum(e['total_delta'] for e in effects.values()),expected,pair+' group delta')
    # Complete detail preserves all losses; never emit winners-only matched sets.
    detail=pd.DataFrame(records)
    full_csv=detail.to_csv(index=False)
    Path('output/'+pair+'_all_trade_attribution.csv').write_text(full_csv)
    lines=full_csv.splitlines(keepends=True)
    header=lines[0];data_lines=lines[1:]
    parts=[];rebuilt=header
    for part,start in enumerate(range(0,len(data_lines),100)):
        body=''.join(data_lines[start:start+100])
        payload=header+body
        path=pair+'_part'+str(part+1)+'.csv'
        size=len(payload.encode())
        assert size<=40000,(path,size)
        Path('output/'+path).write_text(payload)
        parts.append({'path':path,'rows':len(data_lines[start:start+100]),
                      'size_bytes':size,'sha256':hashlib.sha256(payload.encode()).hexdigest()})
        rebuilt+=body
    assert rebuilt==full_csv
    csv_manifest[pair]={'full_rows':len(detail),'full_size_bytes':len(full_csv.encode()),
                        'full_sha256':hashlib.sha256(full_csv.encode()).hexdigest(),
                        'concat_sha256':hashlib.sha256(rebuilt.encode()).hexdigest(),
                        'concat_policy':'First header only; append data lines from each part in order.',
                        'parts':parts}
    added_rows=[y[k] for k in added];removed_rows=[x[k] for k in removed]
    result={'delta_net':expected,'retained_n':len(common),'removed_n':len(removed),'added_n':len(added),
            'retained_quantity_effect':sum(e['retained_quantity_effect'] for e in effects.values()),
            'retained_unit_effect':sum(e['retained_unit_effect'] for e in effects.values()),
            'added_net':summarize(added_rows),'removed_net':summarize(removed_rows),
            'groups':{g:dict(e) for g,e in effects.items()},
            'caveat':'Symmetric algebraic decomposition, not causal attribution. Unit economics may combine fees, prices and exits; quantity reflects endogenous capital, occupancy, sizing caps, volatility quotas and rounding, not capital alone.'}
    return result

csv_manifest={}
snapshots={name:json.loads(Path('inputs/'+name+'.json').read_text()) for name in ["nom_X_B","nom_X_C","nom_N_B","nom_N_C","fee_X_B","fee_X_C","fee_N_B","fee_N_C"]}
normalized={};session_totals={};session_groups={}
for name,s in snapshots.items():
    normalized[name],session_totals[name],session_groups[name]=normalize(s,name)
    pd.DataFrame(normalized[name].values()).to_csv('output/'+name+'_normalized_all_trades.csv',index=False)
comparisons={}
for regime in ('nom','fee'):
    for portfolio in ('B','C'):
        pair=regime+'_'+portfolio
        comparisons[pair]=pair_compare(normalized[regime+'_X_'+portfolio],normalized[regime+'_N_'+portfolio],pair)
# Identity and nonlinear midpoint bookkeeping self-tests, independent of real economics.
qx,qy,ux,uy=2,3,-4,5
close((qy-qx)*(ux+uy)/2+(uy-ux)*(qx+qy)/2,qy*uy-qx*ux,'midpoint mixed signs selftest')
for p in ('B','C'):
    for family in ('X','N'):
        name='nom_'+family+'_'+p;fee='fee_'+family+'_'+p
        # Engine fee stress reruns can add/remove entries; no fixed-fill claim.
        session_totals[fee]['stress_vs_nominal_trade_counts']={
            'retained':len(set(normalized[name])&set(normalized[fee])),
            'removed':len(set(normalized[name])-set(normalized[fee])),
            'added':len(set(normalized[fee])-set(normalized[name]))}
result={'input_manifest':json.loads(Path('inputs/manifest.json').read_text()),
        'sessions':session_totals,'session_groups':session_groups,'comparisons':comparisons,
        'method':'Executed fills audited; matching key symbol/side/opened_at, unique per session. Add/remove actual net signed; retained symmetric midpoint quantity and per-unit-net decomposition. Exposure based on actual holding slices and initial10000 denominator; no counterfactual capital replay. All losses retained.',
        'limitations':['No causal attribution of matched PNL to new anchor alone.',
                       'No new signals, filters, refits, candles or 2026 inspection.',
                       'Actual cash equity/risk budgets at decision are not reconstructed; quantity term cannot separate capital from caps/volatility quotas/rounding.',
                       'Fee.00070 inputs are actual engine reruns, distinct from same-fill overlays.',
                       'No daily marks or new calendar/MTM audit; root owns those.',
                       'Shared BTC sample and B/C portfolios are not independent validation.']}
Path('output/attribution.json').write_text(json.dumps(result,indent=2,allow_nan=False))
Path('output/attribution_csv_manifest.json').write_text(json.dumps(csv_manifest,indent=2,allow_nan=False))
# Compact waterfall shows the exact additive identity; not an equity curve.
fig,axes=plt.subplots(2,2,figsize=(12,8))
for ax,(pair,r) in zip(axes.flat,comparisons.items()):
    labels=['Removed','Added','Retained qty','Retained unit','Delta']
    values=[-r['removed_net']['net'],r['added_net']['net'],r['retained_quantity_effect'],r['retained_unit_effect'],r['delta_net']]
    current=0
    for i,v in enumerate(values):
        bottom=current if i<4 else 0
        ax.bar(i,v,bottom=bottom,color=('#31956d' if v>=0 else '#ce6262') if i<4 else '#355c91')
        ax.text(i,bottom+v/2,f'{v:+.0f}',ha='center',va='center',fontsize=9,color='white')
        if i<4:current+=v
    ax.set_xticks(range(5),labels,rotation=15);ax.set_title(pair+' — N204 minus X03');ax.set_ylabel('USDT')
    ax.axhline(0,color='#555',linewidth=.6)
fig.suptitle('Mechanical trade attribution — executed fills; no causal claim')
fig.tight_layout();fig.savefig('output/attribution_waterfalls.png',dpi=130);plt.close(fig)
print(json.dumps({'comparisons':comparisons,'session_totals':session_totals},allow_nan=False))

```
