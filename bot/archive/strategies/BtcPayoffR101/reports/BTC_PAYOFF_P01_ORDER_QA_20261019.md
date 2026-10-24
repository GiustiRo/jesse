# Payoff P01 executed order QA

Job6206e139bf2c40c9a706512b1773e76a succeeded/exit0,2026-10-19T14:43:29Z; PQA2slot released. Four complete immutable session snapshots: [P01B](http://localhost:9200/#/backtest/17867dbb-3676-46e9-a427-d60694384528), [P01C](http://localhost:9200/#/backtest/dc50d6e4-8799-437a-8d1e-8b81e22cf8ee), [baseB](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f), [baseC](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835).

Both:127shorts,125shared entry timestamps with respective control,2additional. Shared125 have exact entry prices;75same close timestamps,50different. No within-trade qty change or partial exit; all entries STOP.54executed STOP exits were replacements created later than fill, all exactly4h boundary and at/after first full postfill close ceil(fill/4h)*4h+4h;9executed initial stops.63LIMIT targets,1MARKETtimeout.50paired STOP prices never exceed baseline static stop;63paired LIMIT prices identical. Hyperparameters identical. Zero violations.

Important limits: underlying candles/EMA and cancelled stop replacements are absent from snapshots. This audit cannot certify all379logged EMAstop events individually nor reconstruct initial stop for a baseline trade that exited at target. Chronology checks apply to finally executed updated STOP orders. Source AST/stubs and final counters complement, not replace, independent engine/data checks. Root MTM/fill/cost/concentration audit separate. B/C are overlapping development histories, not independent validations.

```json
{
  "scope": "Executed short exit order chronology/semantics against baseline. No MTM, cost or concentration audit. Cancelled stop replacements absent from trade snapshots; cannot validate all379logged replacements.",
  "pairs": {
    "B": {
      "shorts": 127,
      "common_opened": 125,
      "new_opened": 2,
      "unchanged_close_time": 75,
      "different_close_time": 50,
      "executed_stops": 63,
      "stops_created_at_fill": 9,
      "executed_modified_stops": 54,
      "initial_stops_compared_to_baseline": 50,
      "paired_limits": 63,
      "types": {
        "STOP": 63,
        "LIMIT": 63,
        "MARKET": 1
      },
      "examples_modified": [
        {
          "opened": 1604319060000,
          "created": 1604347200000,
          "executed": 1604348160000,
          "earliest_full_bar_close": 1604347200000,
          "stop": 13604.70345902575
        },
        {
          "opened": 1606409580000,
          "created": 1606564800000,
          "executed": 1606575960000,
          "earliest_full_bar_close": 1606435200000,
          "stop": 17416.981167095088
        },
        {
          "opened": 1610347380000,
          "created": 1610424000000,
          "executed": 1610437320000,
          "earliest_full_bar_close": 1610366400000,
          "stop": 36536.44619613511
        }
      ]
    },
    "C": {
      "shorts": 127,
      "common_opened": 125,
      "new_opened": 2,
      "unchanged_close_time": 75,
      "different_close_time": 50,
      "executed_stops": 63,
      "stops_created_at_fill": 9,
      "executed_modified_stops": 54,
      "initial_stops_compared_to_baseline": 50,
      "paired_limits": 63,
      "types": {
        "STOP": 63,
        "LIMIT": 63,
        "MARKET": 1
      },
      "examples_modified": [
        {
          "opened": 1604319060000,
          "created": 1604347200000,
          "executed": 1604348160000,
          "earliest_full_bar_close": 1604347200000,
          "stop": 13604.70345902575
        },
        {
          "opened": 1606409580000,
          "created": 1606564800000,
          "executed": 1606575960000,
          "earliest_full_bar_close": 1606435200000,
          "stop": 17416.981167095088
        },
        {
          "opened": 1610347380000,
          "created": 1610424000000,
          "executed": 1610437320000,
          "earliest_full_bar_close": 1610366400000,
          "stop": 36536.44619613511
        }
      ]
    }
  },
  "violations": [],
  "pass": true
}
```

## Code
```python

import json, math
from pathlib import Path
H=4*3600*1000
names=['P01B','P01C','baseB','baseC']
data={n:json.loads(Path('inputs/'+n+'.json').read_text()) for n in names}
report={'scope':'Executed short exit order chronology/semantics against baseline. No MTM, cost or concentration audit. Cancelled stop replacements absent from trade snapshots; cannot validate all379logged replacements.','pairs':{},'violations':[]}
def check(ok, text):
    if not ok: report['violations'].append(text)
def executed(t):
    return [o for o in t['orders'] if o['status'].upper()=='EXECUTED']
def q(o):return abs(float(o.get('filled_qty') or o['qty']))
for p in ['B','C']:
    cand,base=data['P01'+p],data['base'+p]
    shorts=[t for t in cand['trades'] if t['symbol']=='BTC-USDT' and t['type']=='short']
    bs={int(t['opened_at']):t for t in base['trades'] if t['symbol']=='BTC-USDT' and t['type']=='short'}
    result={'shorts':len(shorts),'common_opened':0,'new_opened':0,'unchanged_close_time':0,'different_close_time':0,'executed_stops':0,'stops_created_at_fill':0,'executed_modified_stops':0,'initial_stops_compared_to_baseline':0,'paired_limits':0,'types':{},'examples_modified':[]}
    check(cand['hyperparameters']==base['hyperparameters'],p+' hp mismatch')
    for t in shorts:
        key=int(t['opened_at'])
        orders=executed(t);ins=[o for o in orders if not o.get('reduce_only')];outs=[o for o in orders if o.get('reduce_only')]
        check(len(ins)==1 and len(outs)==1,p+' one full entry/exit '+str(key))
        if len(ins)!=1 or len(outs)!=1:continue
        e,o=ins[0],outs[0]
        check(e['type']=='STOP',p+' entry changed type '+str(key))
        check(math.isclose(q(e),q(o),rel_tol=1e-10,abs_tol=1e-10),p+' qty changed/partial '+str(key))
        check(int(e['executed_at'])==key,p+' entry time mismatch')
        result['types'][o['type']]=result['types'].get(o['type'],0)+1
        if o['type']=='STOP':
            result['executed_stops']+=1
            check(o.get('submitted_via')=='stop-loss',p+' STOP attribution')
            created=int(o['created_at'])
            if created==key:
                result['stops_created_at_fill']+=1
            else:
                result['executed_modified_stops']+=1
                earliest=((key+H-1)//H)*H+H
                check(created%H==0,p+' modified stop off4h '+str(key))
                check(created>=earliest,p+' modified stop includes partial entry bar '+str(key))
                check(created<int(o['executed_at']),p+' modified STOP must precede fill '+str(key))
                if len(result['examples_modified'])<3:result['examples_modified'].append({'opened':key,'created':created,'executed':int(o['executed_at']),'earliest_full_bar_close':earliest,'stop':float(o['price'])})
        b=bs.get(key)
        if b is None:
            result['new_opened']+=1;continue
        result['common_opened']+=1
        check(math.isclose(t['entry_price'],b['entry_price'],rel_tol=1e-10,abs_tol=1e-8),p+' same-time entry price mismatch')
        result['unchanged_close_time' if t['closed_at']==b['closed_at'] else 'different_close_time']+=1
        bx=[z for z in executed(b) if z.get('reduce_only')]
        if len(bx)!=1:continue
        bo=bx[0]
        # Baseline STOP is static. Its executed price exposes the original stop
        # only in this subset; target-only snapshots cannot reconstruct it.
        if bo['type']=='STOP' and o['type']=='STOP':
            check(float(o['price'])<=float(bo['price'])+1e-7,p+' paired stop widened '+str(key))
            result['initial_stops_compared_to_baseline']+=1
        if bo['type']=='LIMIT' and o['type']=='LIMIT':
            check(math.isclose(o['price'],bo['price'],rel_tol=1e-10,abs_tol=1e-8),p+' target changed '+str(key))
            result['paired_limits']+=1
    check(result['executed_modified_stops']>0,p+' no executed updated stop')
    report['pairs'][p]=result
report['pass']=len(report['violations'])==0
Path('output/p01_order_qa.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
assert report['pass'],report['violations']

```
