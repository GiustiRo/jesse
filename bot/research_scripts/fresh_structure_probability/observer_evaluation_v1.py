"""Frozen independent first-touch evaluation; public DB reads, no trading/network."""
import csv
import json
import math
import runpy
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
from jesse import research
import jesse.helpers as jh

CORE = runpy.run_path("research_scripts/portfolio_roles/causal_multiscale_observer.py", run_name="frozen_core")
MINUTE, BAR, DAY = CORE["MINUTE"], CORE["BAR"], CORE["DAY"]
START, FINISH, WINDOW = CORE["START"], CORE["FINISH"], CORE["WINDOW"]
CLASSES, STATES = CORE["CLASSES"], CORE["STATES"]
MODELS = ("base", "trend", "pivot", "combined")
PAIRS = (("pivot", "base"), ("trend", "base"), ("combined", "trend"))
OUT = Path("research_scripts/fresh_structure_probability/output_v1")

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def date_stamp(year):
    return int(datetime(year, 1, 1, tzinfo=timezone.utc).timestamp()*1000)

def load():
    parts, manifest = [], []
    boundaries = [START-40*DAY]+[date_stamp(y) for y in range(2021,2026)]+[FINISH]
    for start, finish in zip(boundaries[:-1], boundaries[1:]):
        require(finish <= FINISH, "2026 lockbox")
        warmup, a = research.get_candles(
            exchange="Binance Perpetual Futures", symbol="BTC-USDT", timeframe="1m",
            start_date_timestamp=start, finish_date_timestamp=finish,
            warmup_candles_num=0, caching=False, is_for_jesse=False)
        a = np.asarray(a)
        require(warmup is None or np.asarray(warmup).size==0, "Unexpected warmup")
        require(a.ndim==2 and a.shape[1]==6, "Unexpected candle array")
        require(len(a)>0 and np.all(a[:,0]>=start) and np.all(a[:,0]<finish),
                "Public reader violated requested exclusive clock")
        parts.append(a)
        manifest.append({"start":start,"finish_exclusive":finish,"count":len(a),
                         "first":int(a[0,0]),"last":int(a[-1,0])})
        jh.debug("Bounded historical chunk loaded: "+json.dumps(manifest[-1]))
    result=np.concatenate(parts)
    CORE["validate_clock"](result, MINUTE)
    return result, manifest

def classify(minutes, timestamps, valid, origin, reference, atr):
    deadline=origin+DAY
    if deadline>FINISH:
        return "right_censored", None
    a,b=np.searchsorted(timestamps,[origin,deadline])
    block=minutes[a:b]
    if len(block)!=1440 or int(block[0,0])!=origin or int(block[-1,0])!=deadline-MINUTE:
        return "missing_or_invalid", None
    if not np.all(np.diff(block[:,0])==MINUTE) or not np.all(valid[a:b]):
        return "missing_or_invalid", None
    upper,lower=reference+atr, reference-atr
    hits=np.flatnonzero((block[:,3]>=upper)|(block[:,4]<=lower))
    if not len(hits):
        return "valid", "none"
    row=block[hits[0]]
    if row[1]>=upper:
        return "valid", "up"
    if row[1]<=lower:
        return "valid", "down"
    if row[3]>=upper and row[4]<=lower:
        return "ambiguous", None
    return "valid", "up" if row[3]>=upper else "down"

class Model:
    def __init__(self):
        self.events=deque()
        self.counts=Counter()
        self.trend=defaultdict(Counter)
        self.pivot=defaultdict(Counter)
        self.joint=defaultdict(Counter)

    def change(self, row, amount):
        label=row["label"]
        self.counts[label]+=amount
        self.trend[row["trend_state"]][label]+=amount
        if row["state"] in STATES:
            self.pivot[row["state"]][label]+=amount
            self.joint[(row["trend_state"],row["state"])][label]+=amount

    def advance(self, now, matured):
        for row in matured:
            require(row["deadline"]<=now, "Label used before maturity")
            if row["status"]=="valid":
                self.events.append(row)
                self.change(row,1)
        while self.events and self.events[0]["origin"]<now-WINDOW:
            self.change(self.events.popleft(),-1)
        require(all(row["deadline"]<=now for row in self.events), "Future label")
        require(sum(self.counts.values())==len(self.events), "Count conservation")
        require(all(n>=0 for n in self.counts.values()), "Negative count")

    @staticmethod
    def smooth(counts, prior):
        c=np.array([counts[k] for k in CLASSES],dtype=float)
        return (c+20*prior)/(c.sum()+20)

    def predict(self, state, trend):
        counts=np.array([self.counts[k] for k in CLASSES],dtype=float)
        base=(counts+1)/(counts.sum()+3)
        simple=self.smooth(self.trend[trend],base) if trend!="unknown" else base
        pivot=self.smooth(self.pivot[state],base) if state in STATES else base
        combined=self.smooth(self.joint[(trend,state)],simple) if state in STATES else simple
        result=dict(zip(MODELS,[base,simple,pivot,combined]))
        require(all(np.all(p>0) and np.isclose(p.sum(),1) for p in result.values()),"Bad probabilities")
        return {key:value.tolist() for key,value in result.items()},int(counts.sum())

def daily_trends(four):
    days=CORE["aggregate_complete"](four,BAR,DAY)
    result={}
    for index,row in enumerate(days):
        trend="unknown"
        if index and int(row[0]-days[index-1,0])==DAY:
            trend=str(int(np.sign(row[2]-days[index-1,2])))
        result[int(row[0])+DAY]=trend
    return result

def replay(minutes):
    four=CORE["aggregate_complete"](minutes,MINUTE,BAR)
    features,pivots=CORE["causal_features"](four)
    trends=daily_trends(four)
    timestamps=minutes[:,0].astype(np.int64)
    price=minutes[:,1:5]
    valid=(np.isfinite(price).all(axis=1)&(price>0).all(axis=1)
           &(minutes[:,3]>=np.maximum(minutes[:,1],minutes[:,2]))
           &(minutes[:,4]<=np.minimum(minutes[:,1],minutes[:,2])))
    model=Model()
    pending=deque()
    records=[]
    absent=Counter()
    for now in range(START,FINISH,BAR):
        matured=[]
        while pending and pending[0]["deadline"]<=now:
            matured.append(pending.popleft())
        model.advance(now,matured)
        if now not in features:
            absent["missing_complete_4h"]+=1
            continue
        f=features[now]
        atr=f["atr"]
        if atr is None or not math.isfinite(atr) or not 0<atr<f["reference"]:
            absent["invalid_atr"]+=1
            continue
        day_close=now//DAY*DAY
        trend=trends.get(day_close,"unknown")
        probs,n=model.predict(f["state"],trend)
        status,label=classify(minutes,timestamps,valid,now,f["reference"],atr)
        # Outcome was computed offline for speed; only queued deadlines authorize training.
        row={"origin":now,"deadline":now+DAY,"year":datetime.fromtimestamp(now/1000,timezone.utc).year,
             "midnight":now%DAY==0,"state":f["state"],"trend_state":trend,
             "reference":f["reference"],"atr":atr,"probabilities":probs,
             "evidence_n":n,"status":status,"label":label,"structure":f["daily"],
             "structure_4h":f["four_h"]}
        records.append(row)
        pending.append(row)
    return records,pivots,absent

def losses(p,label):
    return CORE["losses"](p,label)

def summarize(records, absent):
    groups=defaultdict(list)
    for row in records:
        for key in ("global","year:"+str(row["year"]),"state:"+row["state"]):
            groups[key].append(row)
        groups["year_state:"+str(row["year"])+":"+row["state"]].append(row)
        if row["midnight"]:
            groups["midnight"].append(row)
    result={}
    for key,rows in groups.items():
        good=[r for r in rows if r["status"]=="valid"]
        amb=[r for r in rows if r["status"]=="ambiguous"]
        summary={"n":len(rows),"statuses":dict(Counter(r["status"] for r in rows)),
                 "labels":dict(Counter(r["label"] for r in good)),
                 "known_structure":sum(r["state"] in STATES for r in rows)}
        for model in MODELS:
            scores=[losses(r["probabilities"][model],r["label"]) for r in good]
            summary[model]={"brier":float(np.mean([s[0] for s in scores])) if scores else None,
                            "logloss":float(np.mean([s[1] for s in scores])) if scores else None}
        for m,b in PAIRS:
            pair=m+"-"+b
            summary[pair]={}
            for j,metric in enumerate(("brier","logloss")):
                known=sum(losses(r["probabilities"][m],r["label"])[j]
                          -losses(r["probabilities"][b],r["label"])[j] for r in good)
                bounds=[0.,0.]
                for r in amb:
                    d=[losses(r["probabilities"][m],label)[j]-losses(r["probabilities"][b],label)[j]
                       for label in ("up","down")]
                    bounds[0]+=min(d)
                    bounds[1]+=max(d)
                summary[pair][metric+"_delta"]=known/len(good) if good else None
                total=len(good)+len(amb)
                summary[pair][metric+"_ambiguous_bounds"]=[(known+v)/total for v in bounds] if total else None
        result[key]=summary
    calibration=[]
    for model in MODELS:
        for k,label in enumerate(CLASSES):
            for bucket in range(5):
                rows=[r for r in records if r["status"]=="valid"
                      and min(4,int(r["probabilities"][model][k]*5))==bucket]
                calibration.append({"model":model,"class":label,"bin":bucket,"n":len(rows),
                                    "probability":float(np.mean([r["probabilities"][model][k] for r in rows])) if rows else None,
                                    "frequency":float(np.mean([r["label"]==label for r in rows])) if rows else None})
    return {"groups":result,"calibration":calibration,"absent_forecasts":dict(absent),
            "expected_slots":(FINISH-START)//BAR,"trading":False,"iid_inference":False,
            "development_adaptive":True,"lockbox_2026_queried":False}

def main():
    require(not OUT.exists(),"Output must be fresh")
    minutes,manifest=load()
    records,pivots,absent=replay(minutes)
    summary=summarize(records,absent)
    OUT.mkdir()
    with (OUT/"forecasts.jsonl").open("w",encoding="utf-8") as stream:
        for row in records:
            stream.write(json.dumps(row,allow_nan=False)+"\n")
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2,allow_nan=False),encoding="utf-8")
    (OUT/"manifest.json").write_text(json.dumps({"queries":manifest,"start":START,"finish_exclusive":FINISH,
        "warmup_days":40,"models":MODELS,"window_days":180,"shrink":20,
        "baseline_modified":False,"external_data":False,"script_version":"v1"},indent=2),encoding="utf-8")
    jh.debug(json.dumps({"global":summary["groups"].get("global"),"midnight":summary["groups"].get("midnight"),
                         "absent":dict(absent),"output":str(OUT)},allow_nan=False))

if __name__=="__main__":
    main()
