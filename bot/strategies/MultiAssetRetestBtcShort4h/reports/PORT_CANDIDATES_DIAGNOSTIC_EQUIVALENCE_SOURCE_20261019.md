# Portfolio — comprobación predeclarada de réplica diagnóstica

Ocho snapshots: cuatro primarias y cuatro debugtrue. Se comparan trades/cantidades/precios/PNL/fees/timestamps/fills ejecutados y curvas numéricas completas, sinIDs. Cualquier diferencia invalida atribuir los contadores diagnósticos a primarias hasta explicación. No se busca una nueva estrategia ni se comparan como muestras independientes.

Se añade comparación entre las cuatro primarias de BTC por dirección/timestamps/precios, ignorando cantidad y PNL: permite distinguir capital endógeno de cambios en señales/fillsBTC. No es igualdad económica de tamaños ni atribución causal por sí sola.

```python
import json, hashlib
from pathlib import Path
pairs=[('CONTROL','DIAG_CONTROL'),('A','DIAG_A'),('B','DIAG_B'),('C','DIAG_C')]
def fingerprint(snapshot):
    trades=[]
    keys=('symbol','type','qty','entry_price','exit_price','PNL','fee','opened_at','closed_at')
    order_keys=('symbol','side','type','qty','filled_qty','price','executed_at','reduce_only')
    for t in sorted(snapshot['trades'],key=lambda t:(t['opened_at'],t['symbol'],t['closed_at'])):
        row={k:t.get(k) for k in keys}
        row['orders']=sorted([{k:o.get(k) for k in order_keys} for o in t['orders'] if str(o.get('status')).upper()=='EXECUTED'],key=lambda o:(o['executed_at'],str(o['side']),o['price']))
        trades.append(row)
    curves=[{'name':c['name'],'data':c['data']} for c in snapshot['equity_curve']]
    digest=lambda obj:hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
    return {'trade_hash':digest(trades),'equity_hash':digest(curves),'n':len(trades)}
results={}
for a,b in pairs:
    sa=json.loads(Path('inputs/'+a+'.json').read_text())
    sb=json.loads(Path('inputs/'+b+'.json').read_text())
    fa,fb=fingerprint(sa),fingerprint(sb)
    results[a]={'primary':fa,'diagnostic':fb,'economic_identity':fa==fb,
                'primary_net':sa['metrics']['net_profit'],'diagnostic_net':sb['metrics']['net_profit'],
                'primary_debug':sa['summary']['form']['debug_mode'],'diagnostic_debug':sb['summary']['form']['debug_mode']}
Path('output/diagnostic_equivalence.json').write_text(json.dumps(results,indent=2,allow_nan=False))
print(json.dumps(results))

btc_keys=('symbol','type','opened_at','closed_at','entry_price','exit_price')
def btc_decisions(name):
    snap=json.loads(Path('inputs/'+name+'.json').read_text())
    return [{k:t.get(k) for k in btc_keys} for t in sorted(snap['trades'],key=lambda t:(t['opened_at'],t['closed_at'])) if t['symbol']=='BTC-USDT']
base=btc_decisions('CONTROL')
btc_comparison={n:{'same_BTC_times_prices_sides_ignoring_qty':btc_decisions(n)==base,'n':len(btc_decisions(n))} for n in ('A','B','C')}
Path('output/btc_decision_identity.json').write_text(json.dumps(btc_comparison,indent=2))
print('BTC_DECISION_IDENTITY',json.dumps(btc_comparison))

```
