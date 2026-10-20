# X03 R3 — nominal parity

Finaljob6f2bfdbdc05c46d49c5c623793a8c444 SUCCEEDED. FourpairsPASS: trades keys/prices/qty/fees/timestamps/executedorders identical;maxPNLdifference0. Configallcontrols exact;onlyknownoptionalmetadata defaults normalized: simulation_modelperpetual_futures,annualization365. Bothmetricsannualization365andconfigexchange.typefutures asserted. No strategychanges/reruns.

First75de1c39efa54164a2fe2b7840d130ddfailedconfigassert:refX03C explicitlypersistsdefaultmetadata while newdraftomits,without economicmismatch. Harnessrepaironly;allotherconfigcontrols remain exact. Rootinformedbefore retry. Stressawaitingroot ticket.

```json
{
  "status": "PASS",
  "pairs": [
    {
      "reference": "X03B",
      "clone": "FBN0B",
      "status": "PASS",
      "trades": 273,
      "by_symbol": {
        "BTC-USDT": 223,
        "SPY-USDT": 12,
        "PAXG-USDT": 38
      },
      "max_abs_trade_PNL_difference": 0.0,
      "same_trade_keys_prices_qty_fees_timestamps_executed_orders": true,
      "reference_net": 11964.238131473841,
      "clone_net": 11964.238131473841
    },
    {
      "reference": "X03C",
      "clone": "FBN0C",
      "status": "PASS",
      "trades": 280,
      "by_symbol": {
        "BTC-USDT": 223,
        "SPY-USDT": 19,
        "PAXG-USDT": 38
      },
      "max_abs_trade_PNL_difference": 0.0,
      "same_trade_keys_prices_qty_fees_timestamps_executed_orders": true,
      "reference_net": 12135.87683397664,
      "clone_net": 12135.87683397664
    },
    {
      "reference": "N204B",
      "clone": "FBN1B",
      "status": "PASS",
      "trades": 273,
      "by_symbol": {
        "BTC-USDT": 223,
        "SPY-USDT": 12,
        "PAXG-USDT": 38
      },
      "max_abs_trade_PNL_difference": 0.0,
      "same_trade_keys_prices_qty_fees_timestamps_executed_orders": true,
      "reference_net": 13056.614915077666,
      "clone_net": 13056.614915077666
    },
    {
      "reference": "N204C",
      "clone": "FBN1C",
      "status": "PASS",
      "trades": 280,
      "by_symbol": {
        "BTC-USDT": 223,
        "SPY-USDT": 19,
        "PAXG-USDT": 38
      },
      "max_abs_trade_PNL_difference": 0.0,
      "same_trade_keys_prices_qty_fees_timestamps_executed_orders": true,
      "reference_net": 13239.442379846789,
      "clone_net": 13239.442379846789
    }
  ],
  "tolerance_PNL_USDT": 1e-07
}
```

```python
import json
import math
from pathlib import Path
pairs=[('X03B','FBN0B'),('X03C','FBN0C'),('N204B','FBN1B'),('N204C','FBN1C')]
data={p.stem:json.loads(p.read_text()) for p in Path('inputs').glob('*.json') if p.name!='manifest.json'}
results=[]
def same_number(a,b,tolerance=0):
    return a==b if tolerance==0 else math.isclose(float(a),float(b),rel_tol=0,abs_tol=tolerance)
def mapping(trades):
    out={}
    for t in trades:
        key=(t['symbol'],t['type'],int(t['opened_at']))
        assert key not in out,('duplicate trade key',key)
        out[key]=t
    return out
def fills(t):
    fields=['symbol','side','type','reduce_only','executed_at','price','qty','filled_qty']
    return sorted([{k:o.get(k) for k in fields} for o in t['orders'] if str(o.get('status')).upper()=='EXECUTED'],
                  key=lambda o:(o['executed_at'],bool(o['reduce_only']),str(o['side']),str(o['type']),o['price'],o['qty']))
for old,new in pairs:
    a,b=data[old],data[new]
    aa,bb=mapping(a['trades']),mapping(b['trades'])
    assert set(aa)==set(bb),(old,new,'trade keys')
    max_pnl=0.;symbols={}
    for key,t in aa.items():
        u=bb[key]
        for field in ['closed_at','qty','entry_price','exit_price','fee']:
            assert t[field]==u[field],(old,new,key,field,t[field],u[field])
        pnl_diff=abs(float(t['PNL'])-float(u['PNL']))
        assert pnl_diff<=1e-7,(old,new,key,'PNL')
        max_pnl=max(max_pnl,pnl_diff)
        assert fills(t)==fills(u),(old,new,key,'executed orders')
        symbols[key[0]]=symbols.get(key[0],0)+1
    for metric in ['starting_balance','finishing_balance','net_profit','fee']:
        assert same_number(a['metrics'][metric],b['metrics'][metric],1e-7),(old,new,metric)
    af=a['summary']['form'];bf=b['summary']['form']
    # Older snapshots may explicitly persist defaults which newer draft forms
    # omit. Treat only these two known metadata defaults as equivalent; all
    # actual config controls and executed economics remain exact.
    ac=json.loads(json.dumps(af['config']));bc=json.loads(json.dumps(bf['config']))
    for cfg in [ac,bc]:
        assert cfg['exchange']['type']=='futures'
        assert cfg['exchange'].pop('simulation_model','perpetual_futures')=='perpetual_futures'
        assert cfg['exchange'].pop('annualization',365)==365
    assert ac==bc,(old,new,'config')
    assert a['metrics']['annualization']==b['metrics']['annualization']==365
    assert bf['config']['exchange']['fee']==.00045
    assert af['start_date']==bf['start_date']=='2020-10-15'
    assert af['finish_date']==bf['finish_date']=='2025-12-31'
    assert af['data_routes']==bf['data_routes']
    assert af['routes'][0]==bf['routes'][0] and af['routes'][2]==bf['routes'][2]
    assert bf['routes'][1]['strategy']=='X03ExecPaxgFixedBeR301'
    for k in ['debug_mode','fast_mode','export_chart','benchmark']:
        assert af[k]==bf[k],(old,new,k)
    results.append({'reference':old,'clone':new,'status':'PASS','trades':len(aa),
      'by_symbol':symbols,'max_abs_trade_PNL_difference':max_pnl,
      'same_trade_keys_prices_qty_fees_timestamps_executed_orders':True,
      'reference_net':a['metrics']['net_profit'],'clone_net':b['metrics']['net_profit']})
Path('output/nominal_parity.json').write_text(json.dumps({'status':'PASS','pairs':results,'tolerance_PNL_USDT':1e-7},indent=2))

```
