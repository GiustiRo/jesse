# Portfolio — QA de instrumentación y ledger

48assertions del AST real de las seis copias pasaron. Job `659f1f80c4d44319a8005daf3ad32392` succeeded. Se comprobaron diagnóstico que no muta plan, clasificación de recortes/rechazos, capital conservador, ledger compartido con pendientes y posiciones a mark, exclusión de reservas obsoletas de posiciones ya abiertas y constantes comunes. Pruebas sintéticas, sin inferencia de rentabilidad.

El primer intento `73a9b331bd304e31b2dde6098b97bfd8` falló porque el fixture omitió fee_rate; se corrigió únicamente el fixture y se repitió el análisis, sin editar estrategias ni repetir backtests.

Las fuentes completas están en los snapshots y estrategias. Este bloque omite su duplicación en la variable sources:

```python
import ast, math, json, types
import numpy as np
# sources is the map of six reviewed immutable strategy snapshots.
checks=[]
def ok(value,label):
    assert value,label
    checks.append(label)
for name,source in sources.items():
    tree=ast.parse(source)
    cl=next(x for x in tree.body if isinstance(x,ast.ClassDef))
    methods=[x for x in cl.body if isinstance(x,ast.FunctionDef) and x.name in {'_record_capacity','_ledger','_committed','_capital'}]
    assign=[x for x in tree.body if isinstance(x,ast.Assign)]
    ns={'math':math,'np':np}
    exec(compile(ast.fix_missing_locations(ast.Module(body=assign+methods,type_ignores=[])),name,'exec'),ns)
    x=types.SimpleNamespace(vars={'plan':{'sentinel':7}},exchange='X',balance=10000,portfolio_value=11000,fee_rate=.00045)
    for f in methods:setattr(x,f.name,types.MethodType(ns[f.name],x))
    cases=[(100,10000,10000,50),(50,10000,10000,25),(100,2000,10000,20),(100,10000,1000,10),(0,10000,10000,0),(100,10000,10000,.0001)]
    for budget,room,margin,qty in cases:x._record_capacity('long',10000,budget,2,100,room,margin,qty,.001)
    r=x.vars['portfolio_capacity_audit']['long']
    ok(r['eligible_sizing_attempts']==6,name+': attempts')
    ok(r['risk_budget_limited']==2 and r['notional_or_weight_limited']==1 and r['margin_limited']==1,name+': bottlenecks')
    ok(r['sized_below_trade_target']==5 and r['capacity_zero']==1 and r['zero_after_lot_rounding']==1,name+': zero vs reduced/rounding')
    ok(x.vars['plan']=={'sentinel':7},name+': diagnostic does not mutate plan')
    ok(x._capital()==10000,name+': gains do not increase capital budget')
    x.portfolio_value=9000;ok(x._capital()==9000,name+': losses decrease budget')
    def pos(qty,entry,value,stop,long):
        return types.SimpleNamespace(is_open=True,position=types.SimpleNamespace(qty=qty,entry_price=entry,value=value),average_stop_loss=stop,is_long=long)
    x.routes=[types.SimpleNamespace(exchange='X',symbol='BTC-USDT',strategy=pos(2,100,220,105,True)),
              types.SimpleNamespace(exchange='X',symbol='PAXG-USDT',strategy=pos(-3,100,270,95,False)),
              types.SimpleNamespace(exchange='X',symbol='SPY-USDT',strategy=types.SimpleNamespace(is_open=False)),
              types.SimpleNamespace(exchange='OTHER',symbol='Z-USD',strategy=pos(999,1,999,999,True))]
    x.shared_vars={'phase2_reservations':{'X:BTC-USDT':{'risk':99999,'notional':99999},
                                         'X:SPY-USDT':{'risk':7,'notional':80}}}
    risk,notional=x._committed()
    ok(math.isclose(risk,32.7105) and notional==570,name+': open marks plus pending reservation, no duplicate stale open reservation')
    ok(ns['TRADE_RISK']==.01 and ns['PORTFOLIO_RISK']==.08 and ns['NOTIONAL_CAP']==4.4,name+': same constants')
with open('output/portfolio_qa.json','w') as f:json.dump({'passed':len(checks),'checks':checks},f,indent=2)
print(json.dumps({'passed':len(checks),'checks':checks}))

```

```
{"passed": 48, "checks": ["PortCompareBtc4h: attempts", "PortCompareBtc4h: bottlenecks", "PortCompareBtc4h: zero vs reduced/rounding", "PortCompareBtc4h: diagnostic does not mutate plan", "PortCompareBtc4h: gains do not increase capital budget", "PortCompareBtc4h: losses decrease budget", "PortCompareBtc4h: open marks plus pending reservation, no duplicate stale open reservation", "PortCompareBtc4h: same constants", "PortComparePaxgRetest4h: attempts", "PortComparePaxgRetest4h: bottlenecks", "PortComparePaxgRetest4h: zero vs reduced/rounding", "PortComparePaxgRetest4h: diagnostic does not mutate plan", "PortComparePaxgRetest4h: gains do not increase capital budget", "PortComparePaxgRetest4h: losses decrease budget", "PortComparePaxgRetest4h: open marks plus pending reservation, no duplicate stale open reservation", "PortComparePaxgRetest4h: same constants", "PortComparePaxgMarket4h: attempts", "PortComparePaxgMarket4h: bottlenecks", "PortComparePaxgMarket4h: zero vs reduced/rounding", "PortComparePaxgMarket4h: diagnostic does not mutate plan", "PortComparePaxgMarket4h: gains do not increase capital budget", "PortComparePaxgMarket4h: losses decrease budget", "PortComparePaxgMarket4h: open marks plus pending reservation, no duplicate stale open reservation", "PortComparePaxgMarket4h: same constants", "PortCompareSpyRetest4h: attempts", "PortCompareSpyRetest4h: bottlenecks", "PortCompareSpyRetest4h: zero vs reduced/rounding", "PortCompareSpyRetest4h: diagnostic does not mutate plan", "PortCompareSpyRetest4h: gains do not increase capital budget", "PortCompareSpyRetest4h: losses decrease budget", "PortCompareSpyRetest4h: open marks plus pending reservation, no duplicate stale open reservation", "PortCompareSpyRetest4h: same constants", "PortCompareSpySecond4h: attempts", "PortCompareSpySecond4h: bottlenecks", "PortCompareSpySecond4h: zero vs reduced/rounding", "PortCompareSpySecond4h: diagnostic does not mutate plan", "PortCompareSpySecond4h: gains do not increase capital budget", "PortCompareSpySecond4h: losses decrease budget", "PortCompareSpySecond4h: open marks plus pending reservation, no duplicate stale open reservation", "PortCompareSpySecond4h: same constants", "PortCompareSpyMarket4h: attempts", "PortCompareSpyMarket4h: bottlenecks", "PortCompareSpyMarket4h: zero vs reduced/rounding", "PortCompareSpyMarket4h: diagnostic does not mutate plan", "PortCompareSpyMarket4h: gains do not increase capital budget", "PortCompareSpyMarket4h: losses decrease budget", "PortCompareSpyMarket4h: open marks plus pending reservation, no duplicate stale open reservation", "PortCompareSpyMarket4h: same constants"]}

```
