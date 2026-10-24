import json
import math
from types import SimpleNamespace
import numpy as np
from strategies.ResearchV5Base4h import (
    ResearchV5Base4h, BAR, DAY, closed_window, atr_window, oi_context, v5_entry_plan,
)

def self_checks():
    """Artificial scalar state checks scheduling/risk; it does not simulate broker fills."""
    checks = 0
    def check(value):
        nonlocal checks
        assert value
        checks += 1
    now = 400 * BAR
    candles = np.array([[t,100.,100.,101.,99.,1.] for t in range(now-240*BAR,now,BAR)])
    check(closed_window(candles,now,224).shape == (224,6))
    future = np.vstack([candles,[now,100,100,1000,1,1]])
    check(np.array_equal(closed_window(future,now,224),closed_window(candles,now,224)))
    check(closed_window(candles,now+1,15) is None)
    for column,value in ((0,now-2*BAR),(2,float("nan")),(3,98.)):
        bad=candles.copy(); bad[-1,column]=value
        check(closed_window(bad,now,15) is None)
    check(closed_window(candles[:-1],now,15) is None)
    check(atr_window(candles,now)["value"] == 2.)
    shock=candles.copy();shock[-1,3]=129.
    check(atr_window(shock,now)["value"] > 2.)
    check(atr_window(shock,now,1)["value"] == 2.)
    check(atr_window(candles[-15:],now,1) is None)
    check(atr_window(candles,now,2) is None)
    reference_bars=DAY//BAR
    lag_bars=14400000//BAR
    history=[dict(time=now+i*BAR,value=100.+i,label=now+i*BAR-600000,
                  available_at=now+i*BAR-240000,status="valid")
             for i in range(reference_bars+lag_bars+3)]
    check(oi_context(history[:reference_bars],now+(reference_bars-1)*BAR)["quality"] == "initialization")
    check(oi_context(history[:reference_bars+1],now+reference_bars*BAR)["passed"])
    check(oi_context(history[:reference_bars+lag_bars],now+(reference_bars+lag_bars-1)*BAR,lag_bars)["quality"] == "initialization")
    check(oi_context(history[:reference_bars+lag_bars+1],now+(reference_bars+lag_bars)*BAR,lag_bars)["passed"])
    bad=[dict(r) for r in history];bad[0]["value"]=0
    check(oi_context(bad,now+reference_bars*BAR)["quality"] == "reference_invalid")
    bad=[dict(r) for r in history];bad[reference_bars]["value"]=100.
    check(not oi_context(bad,now+reference_bars*BAR)["passed"])
    bad=[dict(r) for r in history];bad[reference_bars]["available_at"]=bad[reference_bars]["time"]+1
    check(oi_context(bad,now+reference_bars*BAR)["quality"] == "invalid")
    for direction in (-1,1):
        plan=v5_entry_plan(100.,10000.,.00045,direction,4.)
        check(plan["reason"] == "allowed")
        check(plan["qty"]*plan["unit_loss"] <= 200.+1e-8)
        check(plan["qty"]*100 <= 10000.)
        check(plan["qty"] == math.floor(plan["qty"]*1e8+.01)/1e8)
    check(v5_entry_plan(100.,10000.,-.1,1,4.)["reason"] == "distance_invalid")
    check(v5_entry_plan(100.,10000.,.00045,1,101.)["reason"] == "distance_invalid")
    class Surface:
        _entry_window=ResearchV5Base4h._entry_window
        _target=ResearchV5Base4h._target
        _target_valid=staticmethod(ResearchV5Base4h._target_valid)
        request_exit=ResearchV5Base4h.request_exit
        def __init__(self):
            self.vars={};self.time=now;self.START=now-50*BAR;self.FINISH=now+100*BAR
            self.ACTIVE_WINDOWS=None;self.FORCE_BOUNDARIES=()
            self.TARGET_MODE="none";self.REWARD_MULTIPLE=1.;self.MAX_HOLD_BARS=24
            self.STOP_MULTIPLIER=2.;self.ATR_OFFSET_BARS=0;self.OI_LAG_BARS=0
            self.USE_OI=False;self.LINE="test";self.candles=candles
            self.open_interest=100.;self.open_interest_timestamp=now-600000
            self.price=100.;self.available_margin=10000.;self.fee_rate=.00045
            self.is_open=False;self.is_close=True;self.is_long=True;self.entry_orders=[]
            self.position=SimpleNamespace(opened_at=now,entry_price=100.,qty=1.)
            self.exits=0;self.managed=0;self.opened=0;self.logs=[]
        def features(self,*args):return dict(valid=True,direction=1,reason="setup")
        def get_funding_history(self,**kwargs):return []
        def _bucket(self,month,direction):
            return self.vars.setdefault("audit",{}).setdefault(month+direction,
                dict(bars=0,entries=0,opportunities=0,primary={},flags={}))
        def _log_json(self,label,payload):
            check(len(label+" "+json.dumps(payload,allow_nan=False,separators=(",",":"))) <= 1900)
            self.logs.append((label,payload))
        def liquidate(self):self.exits+=1
        def manage_position(self,atr):self.managed+=1
        def on_v5_open(self):self.opened+=1
    surface=Surface()
    check(surface._entry_window(now))
    check(not surface._entry_window(surface.START))
    surface.ACTIVE_WINDOWS=()
    check(not surface._entry_window(now))
    surface=Surface();ResearchV5Base4h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.vars["v5_last_exit_at"]=now
    ResearchV5Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("same_decision_exit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=now//DAY*DAY
    ResearchV5Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("daily_limit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=(now//DAY-1)*DAY
    ResearchV5Base4h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.USE_OI=True
    ResearchV5Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    surface=Surface();surface.is_open=True
    surface.request_exit("first");surface.request_exit("second")
    check(surface.exits == 1 and surface.vars["exit_reason"] == "first")
    surface.time+=BAR;surface.request_exit("next")
    check(surface.exits == 2)
    surface=Surface();surface.vars["context"]={"atr":None}
    ResearchV5Base4h.update_position(surface)
    check(surface.managed == 0)
    surface.time+=BAR;ResearchV5Base4h.update_position(surface)
    check(surface.managed == 1)
    surface.time=now+24*BAR;surface.is_open=True
    ResearchV5Base4h.update_position(surface)
    check(surface.vars["exit_reason"] == "maximum_hold")
    surface=Surface();surface.is_open=True;surface.time=now+24*BAR
    surface.FORCE_BOUNDARIES=(surface.time,)
    ResearchV5Base4h.update_position(surface)
    check(surface.vars["exit_reason"] == "calendar_boundary")
    for direction in (-1,1):
        surface=Surface()
        ResearchV5Base4h.before(surface)
        context=surface.vars["context"];plan=context["plan"]
        surface.vars["intent"]=dict(context=context,plan=plan)
        surface.is_long=direction==1;surface.is_open=True
        surface.position.entry_price=100.+direction*.05
        surface.position.qty=direction*plan["qty"]
        surface.TARGET_MODE="r_multiple"
        surface.vars["v5_exit_requested_at"]=now
        ResearchV5Base4h.on_open_position(surface,None)
        check(surface.stop_loss[1] == surface.position.entry_price-direction*4.)
        check(surface.take_profit[1] == surface.position.entry_price+direction*4.)
        check(surface.opened == 1 and surface.vars["entry_day"] == context["day"])
        check("v5_exit_requested_at" not in surface.vars)
    return dict(status="passed",assertions=checks)
