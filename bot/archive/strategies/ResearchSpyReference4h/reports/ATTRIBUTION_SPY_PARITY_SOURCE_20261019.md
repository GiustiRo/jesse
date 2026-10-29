# Fuente auditoría de paridad C0 previa a variantes

Compara todos los trades y órdenes ejecutadas por campos económicos, sin UUID; compara métricas y curva completa exacta. Inputs snapshots prior/C0. No nuevas operaciones desde análisis. Fuente fijada antes de resultados.

```python
import json,math
from pathlib import Path
m=json.load(open('inputs/manifest.json'))
d={x['name']:json.load(open(x['file'])) for x in m}
for x in m: assert x['session_status']=='finished'
a,b=d['prior'],d['C0']
aa,bb=a.get('trades',[]),b.get('trades',[])
assert len(aa)==len(bb),'count differs'
keys=['type','opened_at','closed_at','entry_price','exit_price','qty','PNL','fee','holding_period']
maxdiff={}
for x,y in zip(aa,bb):
 for k in keys:
  if isinstance(x[k],(int,float)):
   error=abs(float(x[k])-float(y[k]));maxdiff[k]=max(error,maxdiff.get(k,0.))
   assert math.isclose(x[k],y[k],rel_tol=1e-12,abs_tol=1e-8),(k,x[k],y[k])
  else: assert x[k]==y[k],(k,x[k],y[k])
 executed=lambda t:sorted([(o['side'],o['type'],o['price'],o['qty'],o.get('executed_at'),bool(o.get('reduce_only'))) for o in t['orders'] if o['status']=='EXECUTED'],key=str)
 assert executed(x)==executed(y),'executed order economic fields differ'
for k in ['net_profit','fee','max_drawdown','net_profit_percentage','annual_return','starting_balance','finishing_balance']:
 assert math.isclose(a['metrics'][k],b['metrics'][k],rel_tol=1e-12,abs_tol=1e-8),(k,a['metrics'][k],b['metrics'][k])
assert a.get('equity_curve')==b.get('equity_curve'),'equitycurve differs'
result={'parity_pass':True,'trades':len(aa),'net':b['metrics']['net_profit'],'fees':b['metrics']['fee'],'maxdiff':maxdiff,'executed_orders_equal':True,'equitycurve_equal':True}
Path('output').mkdir(exist_ok=True)
json.dump(result,open('output/parity.json','w'),indent=2)
print(json.dumps(result))

```