# Payoff P02/P03 executed order QA

Jobf48bbd1e42684a9e8c00a2074f499bb9 succeeded/exit0 at2026-10-19T14:53:54Z. Six complete finished snapshots:P02/P03 B/C and controls B/C. PQA3 slot released. No violations.

P02 each126shorts:125common opens+1new,4changed exits/121same times.55STOP/65LIMIT/6MARKET. Four executed modified STOP prices exactly nominal entry*(1-.00045)/(1+.00045); they satisfy zero nominal fee PnL identity. Creation on4h and at/after first full postfill close. This validates4finally executed replacements, not all22logged replacements. Six MARKET exits at72h timeout clocks; none early.50paired initial stop prices identical,65paired target prices identical.

P03 each130shorts:124common opens+6new (one original opening absent),51changed exits/73same.23STOP/54LIMIT/53MARKET. All53MARKET exits at4h boundaries,created=executed and at/after first full postfill close, before72h. This agrees with53RSIneutral and0timeout log counters but no RSI candle array exists in snapshots to independently recalculate the53RSIvalues. No modified STOP.22paired stop prices identical,51paired targets identical. Qty fullentry=fullexit and BTC.001lot multiple throughout. HP and runner/account/window verified.

No partial exits or pyramiding observed. Cross-session qty need not match due shared capital. These are stop/exit semantics checks, not MTM/cost/concentration or statistical validation. Cancelled replacements and indicator histories absent; boundaries checked only for executed orders. No source changes, further recipes or2026.

```json
{
  "scope": "Postfill clocks, nominal BE STOP prices, MARKET exit chronology, full-entry/exit and lot sizing checks; no MTM/cost/concentration audit.",
  "results": {
    "P02B": {
      "shorts": 126,
      "common_opens": 125,
      "new_opens": 1,
      "changed_close_time": 4,
      "same_close_time": 121,
      "types": {
        "STOP": 55,
        "LIMIT": 65,
        "MARKET": 6
      },
      "executed_modified_stops": 4,
      "nominal_BE_verified": 4,
      "MARKET_early": 0,
      "MARKET_timeout": 6,
      "paired_original_stop_verified": 50,
      "paired_target_verified": 65,
      "all_qty_full_lot": true
    },
    "P02C": {
      "shorts": 126,
      "common_opens": 125,
      "new_opens": 1,
      "changed_close_time": 4,
      "same_close_time": 121,
      "types": {
        "STOP": 55,
        "LIMIT": 65,
        "MARKET": 6
      },
      "executed_modified_stops": 4,
      "nominal_BE_verified": 4,
      "MARKET_early": 0,
      "MARKET_timeout": 6,
      "paired_original_stop_verified": 50,
      "paired_target_verified": 65,
      "all_qty_full_lot": true
    },
    "P03B": {
      "shorts": 130,
      "common_opens": 124,
      "new_opens": 6,
      "changed_close_time": 51,
      "same_close_time": 73,
      "types": {
        "STOP": 23,
        "LIMIT": 54,
        "MARKET": 53
      },
      "executed_modified_stops": 0,
      "nominal_BE_verified": 0,
      "MARKET_early": 53,
      "MARKET_timeout": 0,
      "paired_original_stop_verified": 22,
      "paired_target_verified": 51,
      "all_qty_full_lot": true
    },
    "P03C": {
      "shorts": 130,
      "common_opens": 124,
      "new_opens": 6,
      "changed_close_time": 51,
      "same_close_time": 73,
      "types": {
        "STOP": 23,
        "LIMIT": 54,
        "MARKET": 53
      },
      "executed_modified_stops": 0,
      "nominal_BE_verified": 0,
      "MARKET_early": 53,
      "MARKET_timeout": 0,
      "paired_original_stop_verified": 22,
      "paired_target_verified": 51,
      "all_qty_full_lot": true
    }
  },
  "violations": [],
  "limits": [
    "No candle/EMA/RSI arrays or cancelled orders in snapshots; no reconstruction of every logged signal/replacement.",
    "BE stop price is nominal fee breakeven, not a slippage/gap guarantee. Shared-capital sizing may differ from baseline."
  ],
  "pass": true
}
```

## Code
```python

import json, math
from pathlib import Path
H=14400000
data={n:json.loads(Path('inputs/'+n+'.json').read_text()) for n in ['P02B','P02C','P03B','P03C','baseB','baseC']}
report={'scope':'Postfill clocks, nominal BE STOP prices, MARKET exit chronology, full-entry/exit and lot sizing checks; no MTM/cost/concentration audit.','results':{},'violations':[],'limits':['No candle/EMA/RSI arrays or cancelled orders in snapshots; no reconstruction of every logged signal/replacement.','BE stop price is nominal fee breakeven, not a slippage/gap guarantee. Shared-capital sizing may differ from baseline.']}
def check(ok,s):
    if not ok:report['violations'].append(s)
def ex(t):return [o for o in t['orders'] if str(o['status']).upper()=='EXECUTED']
def q(o):return abs(float(o.get('filled_qty') or o['qty']))
for recipe in ['P02','P03']:
    for p in ['B','C']:
        name=recipe+p;d=data[name];base=data['base'+p]
        bs={int(t['opened_at']):t for t in base['trades'] if t['symbol']=='BTC-USDT' and t['type']=='short'}
        ts=[t for t in d['trades'] if t['symbol']=='BTC-USDT' and t['type']=='short']
        r={'shorts':len(ts),'common_opens':0,'new_opens':0,'changed_close_time':0,'same_close_time':0,'types':{},'executed_modified_stops':0,'nominal_BE_verified':0,'MARKET_early':0,'MARKET_timeout':0,'paired_original_stop_verified':0,'paired_target_verified':0,'all_qty_full_lot':True}
        check(d['hyperparameters']==base['hyperparameters'],name+' hyperparameters')
        f=d['summary']['form']
        check(f['debug_mode'] is True and f['fast_mode'] is False and f['export_chart'] is True,name+' runner')
        check(f['start_date']=='2020-10-15' and f['finish_date']=='2025-12-31',name+' window')
        econf=f['config']['exchange']
        check(econf['balance']==10000 and econf['fee']==.00045 and econf['futures_leverage']==5 and econf['futures_leverage_mode']=='isolated' and f['config']['warm_up_candles']==240,name+' account')
        for t in ts:
            key=int(t['opened_at']);oex=ex(t);ins=[o for o in oex if not o.get('reduce_only')];outs=[o for o in oex if o.get('reduce_only')]
            check(len(ins)==1 and len(outs)==1,name+' nonunique entryexit '+str(key))
            if len(ins)!=1 or len(outs)!=1:continue
            entry,exit=ins[0],outs[0];created=int(exit['created_at']);etype=exit['type']
            check(entry['type']=='STOP',name+' entrytype '+str(key))
            full=math.isclose(q(entry),q(exit),rel_tol=1e-10,abs_tol=1e-10)
            lot=q(entry)>0 and abs(q(entry)/.001-round(q(entry)/.001))<1e-7
            r['all_qty_full_lot'] &= full and lot
            check(full and lot,name+' fullqty/lot '+str(key))
            r['types'][etype]=r['types'].get(etype,0)+1
            earliest=((key+H-1)//H)*H+H
            if etype=='STOP' and created>key:
                r['executed_modified_stops']+=1
                check(created%H==0 and created>=earliest,name+' stopclock '+str(key))
                check(created<int(exit['executed_at']),name+' stopcreation prefill '+str(key))
                if recipe=='P02':
                    nominal=float(t['entry_price'])*(1-.00045)/(1+.00045)
                    check(math.isclose(float(exit['price']),nominal,rel_tol=1e-10,abs_tol=1e-7),name+' BEprice '+str(key))
                    check(abs(float(t['entry_price'])-float(exit['price'])-.00045*(float(t['entry_price'])+float(exit['price'])))<1e-7,name+' BEfeeidentity '+str(key))
                    r['nominal_BE_verified']+=1
                else:check(False,name+' unexpected R103 stopmodification')
            if etype=='MARKET':
                when=int(exit['executed_at']);age=when-key
                check(when%H==0 and when>=earliest and created==when,name+' MARKETclock '+str(key))
                if age>=72*3600000:r['MARKET_timeout']+=1
                else:r['MARKET_early']+=1
            b=bs.get(key)
            if b is None:r['new_opens']+=1;continue
            r['common_opens']+=1
            check(math.isclose(t['entry_price'],b['entry_price'],rel_tol=1e-10,abs_tol=1e-7),name+' pairedentryprice')
            r['same_close_time' if t['closed_at']==b['closed_at'] else 'changed_close_time']+=1
            bx=[o for o in ex(b) if o.get('reduce_only')]
            if len(bx)!=1:continue
            bo=bx[0]
            if etype=='STOP' and bo['type']=='STOP':
                check(float(exit['price'])<=float(bo['price'])+1e-7,name+' neverwiden '+str(key))
                if recipe=='P03' or created==key:
                    check(math.isclose(exit['price'],bo['price'],rel_tol=1e-10,abs_tol=1e-7),name+' original stop '+str(key))
                    r['paired_original_stop_verified']+=1
            if etype=='LIMIT' and bo['type']=='LIMIT':
                check(math.isclose(exit['price'],bo['price'],rel_tol=1e-10,abs_tol=1e-7),name+' original TP '+str(key))
                r['paired_target_verified']+=1
        if recipe=='P02':
            check(r['executed_modified_stops']>0,name+' no observable BEstop exits')
            check(r['MARKET_early']==0,name+' unexplained early MARKET')
        if recipe=='P03':
            check(r['MARKET_early']>0,name+' no observable RSIexits')
        report['results'][name]=r
report['pass']=not report['violations']
Path('output/p02_p03_order_qa.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
assert report['pass'],report['violations']

```
