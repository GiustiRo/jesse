# FixedBE observed divergence auditor

Finaljob e59c586237944330917483c5429ccedd succeeded. Prior411aff846d8644a6ac5fdb613ebadc88 succeeded but initialsummaryartifacttruncated by MCP effective65512chars; no partial computed/interpreted. Correction outputonly, same numerical logic and8inputs. Allfinal83artifacts+manifestreadcomplete truncatedfalse, max34066bytes; DID identical. Listsdynamicallypartitioned<=35000bytes,permanifestrows+SHA256concat.

```python
import json
from pathlib import Path
import math
import hashlib
import pandas as pd
pairs=[('X03S_B','FBS0B'),('X03S_C','FBS0C'),('N204S_B','FBS1B'),('N204S_C','FBS1C')]
data={p.stem:json.loads(p.read_text()) for p in Path('inputs').glob('*.json') if p.name!='manifest.json'}
fields=['closed_at','entry_price','exit_price','qty','fee','PNL']
order_fields=['side','type','qty','filled_qty','price','status','created_at','canceled_at','executed_at','reduce_only','submitted_via']
def orders(t):
    return sorted([{k:o.get(k) for k in order_fields} for o in t['orders']],
                  key=lambda o:(o.get('created_at') or 0,bool(o.get('reduce_only')),o.get('type') or '',o.get('price') or 0,o.get('executed_at') or 0))
def key(t):return (t['symbol'],t['type'],int(t['opened_at']))
def trade_map(ts):
    out={}
    for t in ts:
        k=key(t);assert k not in out,('duplicate',k);out[k]=t
    return out
def compact(t):
    return {k:t[k] for k in ['symbol','type','opened_at']+fields}
def first_exec_change(t,u):
    # Only observable order lifecycle endpoints are compared; snapshots do not
    # contain the full sequence of in-place stop amendments.
    a=[o for o in orders(t) if o['status']=='EXECUTED'];b=[o for o in orders(u) if o['status']=='EXECUTED']
    changes=[]
    for i in range(max(len(a),len(b))):
        x=a[i] if i<len(a) else None;y=b[i] if i<len(b) else None
        if x!=y:
            times=[z['executed_at'] for z in [x,y] if z is not None and z['executed_at'] is not None]
            changes.append({'earliest_execution_time':min(times) if times else None,'reference':x,'fixed':y})
    return sorted(changes,key=lambda x:x['earliest_execution_time'] or 0)

def write_partitioned(prefix, rows):
    """Connector wrappers truncate near64KiB; each compact JSON part stays35kB."""
    paths=[];chunks=[];current=[]
    def raw(values):
        return json.dumps(values,separators=(',',':'),ensure_ascii=True).encode()
    for row in rows:
        assert len(raw([row]))<=35000,('single record too large',prefix)
        if current and len(raw(current+[row]))>35000:
            chunks.append(current);current=[]
        current.append(row)
    if current:chunks.append(current)
    concat=b''
    for index,chunk in enumerate(chunks):
        path=prefix+'_part'+str(index+1)+'.json'
        payload=raw(chunk)
        assert len(payload)<=35000
        Path('output/'+path).write_bytes(payload)
        concat+=payload
        paths.append({'path':path,'rows':len(chunk),'size_bytes':len(payload),
                      'sha256':hashlib.sha256(payload).hexdigest()})
    result={'prefix':prefix,'rows':len(rows),'parts':paths,
            'sha256_concatenated_part_bytes':hashlib.sha256(concat).hexdigest(),
            'sha256_canonical_full_rows':hashlib.sha256(raw(rows)).hexdigest()}
    assert sum(x['rows'] for x in paths)==len(rows)
    for part in paths:
        payload=Path('output/'+part['path']).read_bytes()
        assert len(json.loads(payload))==part['rows']
        assert hashlib.sha256(payload).hexdigest()==part['sha256']
    return result

results=[]
for old,new in pairs:
    a,b=data[old],data[new]
    aa,bb=trade_map(a['trades']),trade_map(b['trades'])
    common=set(aa)&set(bb); removed=set(aa)-set(bb);added=set(bb)-set(aa)
    out={'reference':old,'fixed':new,'reference_net':a['metrics']['net_profit'],'fixed_net':b['metrics']['net_profit'],
         'delta_net':b['metrics']['net_profit']-a['metrics']['net_profit'],'symbols':{}}
    for symbol in ['BTC-USDT','PAXG-USDT','SPY-USDT']:
        kept=sorted([k for k in common if k[0]==symbol],key=lambda k:k[2])
        lost=sorted([k for k in removed if k[0]==symbol],key=lambda k:k[2])
        gained=sorted([k for k in added if k[0]==symbol],key=lambda k:k[2])
        rows=[];same_exit=0;same_economics=0;first_exec=[];first_execution_path=[];stop_records=[]
        for k in kept:
            t,u=aa[k],bb[k]
            diff={f:{'reference':t[f],'fixed':u[f]} for f in fields if t[f]!=u[f]}
            same_exit+=int(t['closed_at']==u['closed_at'])
            same_economics+=int(not diff)
            xs=[o for o in orders(t) if o['type']=='STOP' and o['reduce_only']]
            ys=[o for o in orders(u) if o['type']=='STOP' and o['reduce_only']]
            if xs!=ys:
                stop_records.append({'trade_open':k[2],'reference_stop_snapshot':xs,'fixed_stop_snapshot':ys,
                 'amendment_instruction_time':None,
                 'limitation':'STOP snapshot price can be amended in place while created_at stays entry time; no complete amendment history. These endpoint records are not first changed instruction timestamps.'})
            changes=first_exec_change(t,u)
            if changes:
                first_exec.append({'trade_open':k[2],**changes[0]})
                # A path difference excludes quantity/fee-only changes induced
                # by capital and risk budgets.
                for ch in changes:
                    x,y=ch['reference'],ch['fixed']
                    if x is None or y is None or any(x[f]!=y[f] for f in ['side','type','price','executed_at']):
                        first_execution_path.append({'trade_open':k[2],**ch})
            if diff or orders(t)!=orders(u):
                rows.append({'kind':'retained_changed','symbol':symbol,'side':k[1],'open':k[2],
                    'differences':diff,'reference_orders':orders(t),'fixed_orders':orders(u)})
        for k in lost:rows.append({'kind':'removed','symbol':symbol,'side':k[1],'open':k[2],'reference':compact(aa[k]),'reference_orders':orders(aa[k])})
        for k in gained:rows.append({'kind':'added','symbol':symbol,'side':k[1],'open':k[2],'fixed':compact(bb[k]),'fixed_orders':orders(bb[k])})
        # Partition reports by year, keeping each artifact below the connector's
        # text limit rather than interpreting a truncated all-years file.
        paths=[]
        for year in sorted(set(pd.Timestamp(r['open'],unit='ms',tz='UTC').year for r in rows)):
            sub=[r for r in rows if pd.Timestamp(r['open'],unit='ms',tz='UTC').year==year]
            prefix=new+'_'+symbol.replace('-','_')+'_'+str(year)+'_changes'
            paths.append(write_partitioned(prefix,sub))
        s={'reference_count':sum(t['symbol']==symbol for t in a['trades']),
           'fixed_count':sum(t['symbol']==symbol for t in b['trades']),
           'retained_entry':len(kept),'retained_entry_and_exit':same_exit,'retained_same_economics':same_economics,
           'removed':len(lost),'added':len(gained),
           'retained_qty_changed':sum(aa[k]['qty']!=bb[k]['qty'] for k in kept),
           'retained_entry_price_changed':sum(aa[k]['entry_price']!=bb[k]['entry_price'] for k in kept),
           'retained_exit_price_changed':sum(aa[k]['exit_price']!=bb[k]['exit_price'] for k in kept),
           'retained_fee_changed':sum(aa[k]['fee']!=bb[k]['fee'] for k in kept),
           'retained_PNL_changed':sum(aa[k]['PNL']!=bb[k]['PNL'] for k in kept),
           'reference_losing_trades':sum(t['PNL']<0 for t in a['trades'] if t['symbol']==symbol),
           'fixed_losing_trades':sum(t['PNL']<0 for t in b['trades'] if t['symbol']==symbol),
           'changed_stop_snapshot_count':len(stop_records),
           'first_changed_stop_amendment_instruction':None,
           'stop_instruction_history_available':False,
           'first_changed_stop_endpoint_record':stop_records[0] if stop_records else None,
           'changed_stop_endpoint_manifest':write_partitioned(new+'_'+symbol.replace('-','_')+'_stop_endpoints',stop_records),
           'reference_net':sum(t['PNL'] for t in a['trades'] if t['symbol']==symbol),
           'fixed_net':sum(t['PNL'] for t in b['trades'] if t['symbol']==symbol),
           'first_observed_execution_economic_difference':min(first_exec,key=lambda r:r['earliest_execution_time']) if first_exec else None,
           'first_observed_price_or_time_path_difference':min(first_execution_path,key=lambda r:r['earliest_execution_time']) if first_execution_path else None,
           'first_removed_entry':compact(aa[lost[0]]) if lost else None,
           'first_added_entry':compact(bb[gained[0]]) if gained else None,'change_files':paths}
        s['delta_net']=s['fixed_net']-s['reference_net']
        out['symbols'][symbol]=s
    assert math.isclose(sum(x['delta_net'] for x in out['symbols'].values()),out['delta_net'],rel_tol=0,abs_tol=1e-7)
    summary_bytes=json.dumps(out,separators=(',',':')).encode()
    assert len(summary_bytes)<=40000,('summary over40k',new,len(summary_bytes))
    Path('output/'+new+'_divergence_summary.json').write_bytes(summary_bytes)
    results.append(out)
# Difference in differences within each portfolio: N204-X03 under fixedBE,
# minus that same contrast under dynamicBE. This is an implementation contrast
# with endogenous capital, not a universal causal estimate of signal alpha.
did=[]
for side in ['B','C']:
    x=next(r for r in results if r['fixed']=='FBS0'+side)
    n=next(r for r in results if r['fixed']=='FBS1'+side)
    did.append({'portfolio':side,'N204_minus_X03_dynamicBE':n['reference_net']-x['reference_net'],
                'N204_minus_X03_fixedBE':n['fixed_net']-x['fixed_net'],
                'difference_in_differences':n['delta_net']-x['delta_net']})
Path('output/fixedBE_implementation_contrasts.json').write_text(json.dumps({'status':'PASS','pairs':[{'reference':r['reference'],'fixed':r['fixed'],'delta_net':r['delta_net']} for r in results],'difference_in_differences':did,
 'limitations':'Only stored trade/order lifecycle endpoints, not full amendment/cancel history or unobserved blocked signals. Actual engine fee/sizing/capital/BTC/SPY fee dependencies remain; fixedBE not pure overlay or eligible replacement.'},indent=2))

output_manifest=[]
for p in sorted(Path('output').glob('*.json')):
    payload=p.read_bytes()
    assert len(payload)<=40000,(str(p),len(payload))
    output_manifest.append({'path':p.name,'size_bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()})
Path('output/output_manifest.json').write_text(json.dumps({'artifacts':output_manifest,'total_artifacts':len(output_manifest),'all_parts_max35000':True,'all_summaries_max40000':True},indent=2))

```
