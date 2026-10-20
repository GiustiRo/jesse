"""Synthetic parity and delayed-training audit for independent adapter."""
import json
import runpy
from pathlib import Path
import numpy as np
import jesse.helpers as jh

def main():
    e=runpy.run_path("research_scripts/fresh_structure_probability/observer_evaluation_v1.py",run_name="adapter_controls")
    core=e["CORE"]
    minute,day=core["MINUTE"],core["DAY"]
    origin=core["START"]
    rows=np.asarray([core["candle"](origin+j*minute) for j in range(1440)])
    checks=[]
    for kind in ("none","up","down","ambiguous","gap_open"):
        a=rows.copy()
        if kind=="up": a[25]=core["candle"](origin+25*minute,100,100.5,101,99.5)
        if kind=="down": a[25]=core["candle"](origin+25*minute,100,99.5,100.5,99)
        if kind=="ambiguous": a[25]=core["candle"](origin+25*minute,100,100,101,99)
        if kind=="gap_open": a[25]=core["candle"](origin+25*minute,102,100,102,98)
        target=e["classify"](a,a[:,0].astype(np.int64),np.ones(len(a),dtype=bool),origin,100,1)
        ep=core["Episode"](origin,"unknown",100,1,[1/3]*3,[1/3]*3,0,0,{})
        for r in a: ep.consume(r)
        assert target==ep.status(origin+day), (kind,target,ep.status(origin+day))
        checks.append("parity_"+kind)
    a=np.delete(rows,25,axis=0)
    assert e["classify"](a,a[:,0].astype(np.int64),np.ones(len(a),dtype=bool),origin,100,1)==("missing_or_invalid",None)
    checks.append("missing_minute_excluded")
    model=e["Model"]()
    row={"origin":origin,"deadline":origin+day,"state":"U","trend_state":"1","status":"valid","label":"up"}
    first,n=model.predict("U","1")
    assert n==0
    try:
        model.advance(origin+day-1,[row])
        raise RuntimeError("Early label accepted")
    except AssertionError as exc:
        assert str(exc)=="Label used before maturity"
    assert model.predict("U","1")== (first,n)
    model.advance(origin+day,[row])
    assert model.predict("U","1")[1]==1
    model.advance(origin+e["WINDOW"]+1,[])
    assert model.predict("U","1")[1]==0
    checks.extend(["no_early_training","maturity_at_deadline","calendar_expiry"])
    unknown,_=model.predict("unknown","1")
    assert unknown["pivot"]==unknown["base"] and unknown["combined"]==unknown["trend"]
    checks.append("unknown_fallback")
    four=np.asarray([core["candle"](j*core["BAR"],100,100+(j//6)%2,102,98) for j in range(30)])
    prefix=e["daily_trends"](four[:24])
    full=e["daily_trends"](four)
    assert all(full[t]==prefix[t] for t in prefix)
    checks.append("daily_trend_prefix_invariance")
    result={"passed":checks,"market_query":False,"trading":False}
    Path("research_scripts/fresh_structure_probability/adapter_controls.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    jh.debug(json.dumps(result))

if __name__=="__main__":
    main()
