# SPY última ronda — revisión de estado

Doce fuentes reales revisadas antes de correr. RESET01..06: sólo cambia before. MECH01..04/06: sólo before; MECH05: sólo _plan para repricing MARKET antes de sizing. Constantes, indicadores, riesgos, gestión y calendario heredados intactos. Las fuentes completas constan en snapshots de las sesiones y revisiones de implementación por agente.

Job `e97c0f4493b449abba005c64ac9f4d48` succeeded. Artifact `state_qa.json`;113/113 comprobaciones sobre métodos reales extraídos por AST. Fixtures sustituyen indicadores y mercado; no son datos fabricados usados para estimar rentabilidad. Esto verifica lógica, no edge ni robustez estadística. No se cambiaron fuentes por resultados.

Cobertura: censura inicial, exclusión de extrema actual del canal, primera oportunidad omitida, ordinales2/3/4 de las doce, estado fuera de horario y stale, rachas calificantes, ruptura por fresh/ventana, no replay, reset40/60%, horizontes20/32, doble cierre, independencia de reset respecto a quote/ventana/régimen y repricing con riesgo1%.

## Fixture y assertions ejecutados

El código original incrusta los doce snapshots en sources. Aquí se omite esa repetición; cargar exactamente las doce fuentes revisadas antes de ejecutar este mismo bloque.

```python
import ast, math, types, json
import numpy as np
# sources maps strategy names to their complete MCP-read snapshots; see per-agent implementation reports.
checks=[]
def ok(value,label):
    assert value,label
    checks.append(label)
class Fixture:
    def __init__(self,name):
        t=ast.parse(sources[name]);cl=next(x for x in t.body if isinstance(x,ast.ClassDef))
        wanted={'before','_origin','_set_struct_event','_plan'}
        functions=[x for x in cl.body if isinstance(x,ast.FunctionDef) and x.name in wanted]
        assignments=[x for x in t.body if isinstance(x,ast.Assign)]
        self.ns={'np':np,'math':math,'ta':types.SimpleNamespace(ema=lambda c,period:95.)}
        exec(compile(ast.fix_missing_locations(ast.Module(body=assignments+functions,type_ignores=[])),name,'exec'),self.ns)
        for f in functions:setattr(self,f.name,types.MethodType(self.ns[f.name],self))
        self.name=name;self.vars={};self.symbol='SPY-USDT';self.is_trading_hours=True
        self.hp={'donchian_len':26,'ema_fast':20,'stop_atr':2}
        self.closed_candle_open_time=33
        self.signal_candles=np.array([[i,90,90,100,80,0] for i in range(34)],float)
        self.signal_candles[-1,3:5]=[9999,-9999]
        self.price=100.5;self.high=101.;self.low=100.
        self.context={'level':100.,'atr':1.,'regime':True}
        self.fresh=True;self.window=True;self.fee_rate=.00045
        self.leveraged_available_margin=50000
    def _context(self):return self.context
    def _fresh_quote(self):return self.fresh
    def _entry_window(self):return self.window
    def _capital(self):return 10000.
    def _committed(self):return 0.,0.
    def _volatility_share(self):return 1.
    def step(self,price=100.5):
        self.price=price;self.before()
    def reset(self):
        self.step(80)
        if self.name.endswith('Reset05'):self.step(80)
for name in sources:
    x=Fixture(name);x.step()
    ok(not x.vars.get('epoch_seen') and x.vars['struct_event'] is None,name+': left censor')
    x.reset();ok(x.vars.get('epoch_seen') and x.vars['epoch_count']==0,name+': reset excluding current extrema')
    x.step();ok(x.vars['epoch_count']==1 and x.vars['struct_event'] is None,name+': first opportunity skipped')
    for ordinal in (2,3,4):
        x.step()
        if 'Reset' in name:expect=True
        else:
            m=int(name[-2:])
            expect={1:ordinal==2,2:ordinal>=3,3:ordinal==3,4:2<=ordinal<=3,5:True,6:False}[m]
        ok((x.vars['struct_event'] is not None)==expect,name+': ordinal '+str(ordinal))
    prior=x.vars.copy();x.is_trading_hours=False;x.step(80)
    ok(x.vars['epoch_count']==prior['epoch_count'],name+': offsession state preserved')
    x.is_trading_hours=True;x.signal_candles[-1,0]=32;x.step(80)
    ok(x.vars['epoch_count']==prior['epoch_count'],name+': stale state preserved')
x=Fixture('SpyLastMechanism06');x.reset();x.step();x.step()
ok(x.vars['epoch_count']==1,'MECH06: contiguous eligible does not count again')
x.fresh=False;x.step();ok(x.vars['prev_eligible'] is False,'MECH06: missing quote breaks run')
x.fresh=True;x.step()
ok(x.vars['epoch_count']==2 and x.vars['struct_event'] is not None,'MECH06: new run counts and fires')
x.step();ok(x.vars['struct_event'] is None and x.vars['epoch_count']==2,'MECH06: no occupied/unconsumed event replay')
x.window=False;x.step();x.window=True;x.step()
ok(x.vars['epoch_count']==3,'MECH06: closed entry window breaks run')
for name,price,expected in [('SpyLastReset03',89,False),('SpyLastReset04',91,True)]:
    x=Fixture(name);x.step(price)
    ok(bool(x.vars.get('epoch_seen'))==expected,name+': reset threshold contrast')
for name,expected in [('SpyLastReset01',False),('SpyLastReset02',True)]:
    x=Fixture(name);x.signal_candles[1,3]=140;x.step(100)
    ok(bool(x.vars.get('epoch_seen'))==expected,name+': reset horizon only')
x=Fixture('SpyLastReset05');x.fresh=False;x.window=False;x.context['regime']=False;x.step(80)
ok(x.vars['reset_streak']==1 and not x.vars.get('epoch_seen'),'RESET05: one below insufficient')
x.step(91);ok(x.vars['reset_streak']==0,'RESET05: above breaks streak')
x.step(80);x.is_trading_hours=False;x.step(80)
ok(x.vars['reset_streak']==1,'RESET05: offsession does not count')
x.is_trading_hours=True;x.step(80)
ok(x.vars['epoch_seen'],'RESET05: reset independent of quote/window/regime')
x=Fixture('SpyLastReset06');x.step(94)
ok(x.vars['epoch_seen'],'RESET06: same EMA20 used as reset')
x=Fixture('SpyLastReset06');x.step(96)
ok(not x.vars.get('epoch_seen'),'RESET06: price above EMA does not reset')
x=Fixture('SpyLastMechanism05');x.reset();x.step();x.step()
ok(x._plan() and x.vars['plan']['entry']==100.5 and x.vars['plan']['distance']==2,'MECH05: market repricing before sizing')
ok(x.vars['plan']['qty']>0 and x.vars['plan']['risk']<=100.00001,'MECH05: same risk budget')
with open('output/state_qa.json','w') as f:json.dump({'passed':len(checks),'checks':checks},f,indent=2)
print(json.dumps({'passed':len(checks),'checks':checks}))

```

## Salida

```
{"passed": 113, "checks": ["SpyLastReset01: left censor", "SpyLastReset01: reset excluding current extrema", "SpyLastReset01: first opportunity skipped", "SpyLastReset01: ordinal 2", "SpyLastReset01: ordinal 3", "SpyLastReset01: ordinal 4", "SpyLastReset01: offsession state preserved", "SpyLastReset01: stale state preserved", "SpyLastReset02: left censor", "SpyLastReset02: reset excluding current extrema", "SpyLastReset02: first opportunity skipped", "SpyLastReset02: ordinal 2", "SpyLastReset02: ordinal 3", "SpyLastReset02: ordinal 4", "SpyLastReset02: offsession state preserved", "SpyLastReset02: stale state preserved", "SpyLastReset03: left censor", "SpyLastReset03: reset excluding current extrema", "SpyLastReset03: first opportunity skipped", "SpyLastReset03: ordinal 2", "SpyLastReset03: ordinal 3", "SpyLastReset03: ordinal 4", "SpyLastReset03: offsession state preserved", "SpyLastReset03: stale state preserved", "SpyLastReset04: left censor", "SpyLastReset04: reset excluding current extrema", "SpyLastReset04: first opportunity skipped", "SpyLastReset04: ordinal 2", "SpyLastReset04: ordinal 3", "SpyLastReset04: ordinal 4", "SpyLastReset04: offsession state preserved", "SpyLastReset04: stale state preserved", "SpyLastReset05: left censor", "SpyLastReset05: reset excluding current extrema", "SpyLastReset05: first opportunity skipped", "SpyLastReset05: ordinal 2", "SpyLastReset05: ordinal 3", "SpyLastReset05: ordinal 4", "SpyLastReset05: offsession state preserved", "SpyLastReset05: stale state preserved", "SpyLastReset06: left censor", "SpyLastReset06: reset excluding current extrema", "SpyLastReset06: first opportunity skipped", "SpyLastReset06: ordinal 2", "SpyLastReset06: ordinal 3", "SpyLastReset06: ordinal 4", "SpyLastReset06: offsession state preserved", "SpyLastReset06: stale state preserved", "SpyLastMechanism01: left censor", "SpyLastMechanism01: reset excluding current extrema", "SpyLastMechanism01: first opportunity skipped", "SpyLastMechanism01: ordinal 2", "SpyLastMechanism01: ordinal 3", "SpyLastMechanism01: ordinal 4", "SpyLastMechanism01: offsession state preserved", "SpyLastMechanism01: stale state preserved", "SpyLastMechanism02: left censor", "SpyLastMechanism02: reset excluding current extrema", "SpyLastMechanism02: first opportunity skipped", "SpyLastMechanism02: ordinal 2", "SpyLastMechanism02: ordinal 3", "SpyLastMechanism02: ordinal 4", "SpyLastMechanism02: offsession state preserved", "SpyLastMechanism02: stale state preserved", "SpyLastMechanism03: left censor", "SpyLastMechanism03: reset excluding current extrema", "SpyLastMechanism03: first opportunity skipped", "SpyLastMechanism03: ordinal 2", "SpyLastMechanism03: ordinal 3", "SpyLastMechanism03: ordinal 4", "SpyLastMechanism03: offsession state preserved", "SpyLastMechanism03: stale state preserved", "SpyLastMechanism04: left censor", "SpyLastMechanism04: reset excluding current extrema", "SpyLastMechanism04: first opportunity skipped", "SpyLastMechanism04: ordinal 2", "SpyLastMechanism04: ordinal 3", "SpyLastMechanism04: ordinal 4", "SpyLastMechanism04: offsession state preserved", "SpyLastMechanism04: stale state preserved", "SpyLastMechanism05: left censor", "SpyLastMechanism05: reset excluding current extrema", "SpyLastMechanism05: first opportunity skipped", "SpyLastMechanism05: ordinal 2", "SpyLastMechanism05: ordinal 3", "SpyLastMechanism05: ordinal 4", "SpyLastMechanism05: offsession state preserved", "SpyLastMechanism05: stale state preserved", "SpyLastMechanism06: left censor", "SpyLastMechanism06: reset excluding current extrema", "SpyLastMechanism06: first opportunity skipped", "SpyLastMechanism06: ordinal 2", "SpyLastMechanism06: ordinal 3", "SpyLastMechanism06: ordinal 4", "SpyLastMechanism06: offsession state preserved", "SpyLastMechanism06: stale state preserved", "MECH06: contiguous eligible does not count again", "MECH06: missing quote breaks run", "MECH06: new run counts and fires", "MECH06: no occupied/unconsumed event replay", "MECH06: closed entry window breaks run", "SpyLastReset03: reset threshold contrast", "SpyLastReset04: reset threshold contrast", "SpyLastReset01: reset horizon only", "SpyLastReset02: reset horizon only", "RESET05: one below insufficient", "RESET05: above breaks streak", "RESET05: offsession does not count", "RESET05: reset independent of quote/window/regime", "RESET06: same EMA20 used as reset", "RESET06: price above EMA does not reset", "MECH05: market repricing before sizing", "MECH05: same risk budget"]}

```
