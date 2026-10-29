"""Bounded public research.get_candles contract probe: one historical day only."""
import json
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
from jesse import research
import jesse.helpers as jh

def stamp(date):
    return int(datetime.fromisoformat(date).replace(tzinfo=timezone.utc).timestamp()*1000)

def main():
    start, finish = stamp("2020-10-15"), stamp("2020-10-16")
    result = research.get_candles(
        exchange="Binance Perpetual Futures", symbol="BTC-USDT", timeframe="1m",
        start_date_timestamp=start, finish_date_timestamp=finish,
        warmup_candles_num=0, caching=False, is_for_jesse=False)
    assert isinstance(result, tuple) and len(result)==2, "Unexpected public result"
    summary=[]
    for index, part in enumerate(result):
        a=np.asarray(part)
        row={"tuple_index":index,"python_type":type(part).__name__,"shape":list(a.shape)}
        if a.size and a.ndim==2 and a.shape[1]==6:
            assert np.all(a[:,0]<stamp("2026-01-01")), "Lockbox violation"
            row.update(first_timestamp=int(a[0,0]),last_timestamp=int(a[-1,0]),
                       at_or_after_start=bool(np.all(a[:,0]>=start)),
                       strictly_before_finish=bool(np.all(a[:,0]<finish)),
                       valid_jesse_ohlc=bool(np.all(a[:,3]>=np.maximum(a[:,1],a[:,2])) and np.all(a[:,4]<=np.minimum(a[:,1],a[:,2]))),
                       ordered_unique=bool(np.all(np.diff(a[:,0])>0)),
                       minute_contiguous=bool(np.all(np.diff(a[:,0])==60000)))
        summary.append(row)
    output={"start":start,"finish_exclusive_requested":finish,"parts":summary,"trading":False}
    Path("research_scripts/fresh_structure_probability/contract_probe.json").write_text(json.dumps(output,indent=2),encoding="utf-8")
    jh.debug(json.dumps(output))

if __name__=="__main__":
    main()
