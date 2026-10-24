# Atribución PAXG: gate C0 de reproducción

Fecha:19oct2026local. **PARITY_PASS**. No se lanzó otra configuración de atribución durante este gate.

[Réplica C0](http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673) frente a [benchmark aislado](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c).

Coincidencia exacta de35 operaciones,70 órdenes ejecutadas y1.904 puntos de curva almacenada. Máxima diferencia en floats de trades,órdenes,métricas,equity: **0,0**. Símbolo/tipo/timestamps de entrada y salida y creación/ejecución de órdenes coinciden exactamente; se excluyen IDs y nombre de clase. Formulario idéntico salvo clase de ruta. Neto546,110572353739USDT yfees246,608881054834. Wallet conciliado.

Primer análisis 661ecd2d88844c2d83baf809686b648c falló por intentar convertir metadata color de equity '#818CF8' a float. Forms,trades,órdenes y métricas ya habían pasado, pero no se declaró PASS parcial. Se corrigió únicamente comparador: campos numéricos con tolerancia1e−8, metadata no numérica por igualdad exacta. C0 no se volvió a correr ni se cambió fuente.

Segundo análisis a15c9d66b73d4bd8b57c5cde76d1993d succeeded / exit0, snapshots completos sin truncamiento. Se puede continuar al resto16 sujeto a confirmación de root. Cq/E4/M/R/U contienen guard exacto searchsorted y todos los readbacks fueron verificados; C0/E1/E2/E3 no fueron alterados.

## Resultado reproducible

```json
{
  "status": "PARITY_PASS",
  "reference_session": "93a16137-e819-41a3-b325-0631a6627a6c",
  "replica_session": "69c90bb0-e2b4-4c6a-a562-edd95399e673",
  "trade_count": 35,
  "executed_order_count": 70,
  "equity_points": 1904,
  "net": 546.1105723537391,
  "fees": 246.60888105483383,
  "tolerance": 1e-8,
  "maximum_differences": {
    "trade_float": 0,
    "order_float": 0,
    "metric_float": 0,
    "equity_float": 0
  },
  "scope": "Executed events, signal/order creation times, prices, quantities, fees, PNL, metrics, full stored curve and wallet. IDs and class name excluded."
}
```

## Código exacto del análisis PASS

Inputs: reference=backtest93a16137-e819-41a3-b325-0631a6627a6c; C0=backtest69c90bb0-e2b4-4c6a-a562-edd95399e673.

```python
import json, math
import numpy as np

reference=json.load(open('inputs/reference.json'))
replica=json.load(open('inputs/C0.json'))
assert reference['summary']['session_status']==replica['summary']['session_status']=='finished'
tolerance=1e-8
errors={'trade_float':0.0,'order_float':0.0,'metric_float':0.0,'equity_float':0.0}
def equal_float(a,b,category):
    if a is None or b is None:
        assert a is b,(a,b)
        return
    x,y=float(a),float(b)
    assert math.isfinite(x) and math.isfinite(y),(a,b)
    delta=abs(x-y)
    errors[category]=max(errors[category],delta)
    assert delta<=tolerance,(category,a,b,delta)

fa=dict(reference['summary']['form']);fb=dict(replica['summary']['form'])
ra=fa.pop('routes');rb=fb.pop('routes')
assert fa==fb,(fa,fb)
assert len(ra)==len(rb)==1
for key in ('symbol','timeframe','exchange'):
    assert ra[0][key]==rb[0][key]

ta=reference['trades'];tb=replica['trades']
assert len(ta)==len(tb)==35
executed_orders=0
for a,b in zip(ta,tb):
    for key in ('symbol','exchange','type','opened_at','closed_at'):
        assert a[key]==b[key],(key,a[key],b[key])
    for key in ('entry_price','exit_price','qty','fee','size','PNL','PNL_percentage','holding_period'):
        equal_float(a[key],b[key],'trade_float')
    oa=sorted((o for o in a['orders'] if o['status']=='EXECUTED'),
              key=lambda o:(o['executed_at'],o['reduce_only'],o['type'],o['created_at']))
    ob=sorted((o for o in b['orders'] if o['status']=='EXECUTED'),
              key=lambda o:(o['executed_at'],o['reduce_only'],o['type'],o['created_at']))
    assert len(oa)==len(ob)
    executed_orders+=len(oa)
    for x,y in zip(oa,ob):
        for key in ('symbol','exchange','side','type','reduce_only','status','created_at','executed_at'):
            assert x[key]==y[key],(key,x[key],y[key])
        for key in ('price','qty','filled_qty'):
            equal_float(x[key],y[key],'order_float')

ma=reference['metrics'];mb=replica['metrics']
assert set(ma)==set(mb)
for key,a in ma.items():
    b=mb[key]
    if a is None or isinstance(a,(str,bool)):
        assert a==b,(key,a,b)
    else:
        equal_float(a,b,'metric_float')
ea=reference['equity_curve'];eb=replica['equity_curve']
assert len(ea)==len(eb)
points=0
for sa,sb in zip(ea,eb):
    assert sa['name']==sb['name']
    assert len(sa['data'])==len(sb['data'])
    for a,b in zip(sa['data'],sb['data']):
        assert a['time']==b['time']
        assert set(a)==set(b)
        for key in a:
            if key!='time':
                if isinstance(a[key],(int,float)) and not isinstance(a[key],bool):
                    equal_float(a[key],b[key],'equity_float')
                else:
                    assert a[key]==b[key],(key,a[key],b[key])
        points+=1
net=sum(float(t['PNL']) for t in tb)
fees=sum(float(t['fee']) for t in tb)
assert abs(float(mb['starting_balance'])+net-float(mb['finishing_balance']))<tolerance
result={'status':'PARITY_PASS','reference_session':reference['summary']['session_id'],
        'replica_session':replica['summary']['session_id'],'trade_count':len(tb),
        'executed_order_count':executed_orders,'equity_points':points,
        'net':net,'fees':fees,'tolerance':tolerance,'maximum_differences':errors,
        'scope':'Executed events, signal/order creation times, prices, quantities, fees, PNL, metrics, full stored curve and wallet. IDs and class name excluded.'}
json.dump(result,open('output/parity.json','w'),indent=2)
print(json.dumps(result,sort_keys=True))

```

No valida alpha, paridad spot/perpetual ni ejecución futura. La curva reproducida sigue muestreada00:01 y no se usa como cierre diario UTC.
