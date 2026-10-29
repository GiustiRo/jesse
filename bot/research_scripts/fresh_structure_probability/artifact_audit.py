"""Audit persisted forecasts only; no DB query and no re-estimation choice."""
import json
import runpy
from collections import Counter, deque
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import jesse.helpers as jh

def main():
    root=Path("research_scripts/fresh_structure_probability/output_v1")
    e=runpy.run_path("research_scripts/fresh_structure_probability/observer_evaluation_v1.py",run_name="artifact_audit")
    rows=[json.loads(line) for line in (root/"forecasts.jsonl").read_text(encoding="utf-8").splitlines()]
    summary=json.loads((root/"summary.json").read_text(encoding="utf-8"))
    model=e["Model"]()
    queue=deque()
    previous=None
    maximum=0
    for row in rows:
        now=row["origin"]
        assert previous is None or now>previous
        previous=now
        assert e["START"]<=now<e["FINISH"] and now%e["BAR"]==0
        assert row["deadline"]==now+e["DAY"]
        matured=[]
        while queue and queue[0]["deadline"]<=now:
            matured.append(queue.popleft())
        model.advance(now,matured)
        p,n=model.predict(row["state"],row["trend_state"])
        assert n==row["evidence_n"]
        maximum=max(maximum,n)
        for name in e["MODELS"]:
            assert np.array_equal(p[name],row["probabilities"][name])
        for key in ("structure","structure_4h"):
            snapshot=row[key]
            assert snapshot["asof_close"]<=now
            for pivot in snapshot["highs"]+snapshot["lows"]:
                assert pivot["confirmed_at"]<=now
        if row["status"]=="right_censored":
            assert row["deadline"]>e["FINISH"]
        else:
            assert row["deadline"]<=e["FINISH"]
        queue.append(row)
    regenerated=e["summarize"](rows,Counter(summary["absent_forecasts"]))
    assert regenerated==summary
    def date(t):
        return datetime.fromtimestamp(t/1000,timezone.utc).isoformat()
    output={"n":len(rows),"probabilities_replay_exact":True,"scores_recomputed_exact":True,
            "no_future_confirmation":True,"deferred_maturity_verified":True,
            "first_origin":date(rows[0]["origin"]),"last_origin":date(rows[-1]["origin"]),
            "finish_exclusive":date(e["FINISH"]),"max_training_n":maximum,
            "midnight_n":sum(r["midnight"] for r in rows),
            "trend_states":dict(Counter(r["trend_state"] for r in rows)),
            "first_evidence_n":rows[0]["evidence_n"],"market_query":False,"trading":False}
    (root/"artifact_audit.json").write_text(json.dumps(output,indent=2),encoding="utf-8")
    jh.debug(json.dumps(output))

if __name__=="__main__":
    main()
