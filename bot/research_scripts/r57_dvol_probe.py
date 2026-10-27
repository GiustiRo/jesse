"""r57 (parallel, N + 0): feasibility of Deribit DVOL as an r58 input (PROTOCOL_R57.md §5).

Public, unauthenticated endpoint public/get_volatility_index_data (docs.deribit.com), daily
resolution ('1D'), BTC and ETH, from 2019-01-01 to 2024-12-31 23:59:59 UTC only: 2025 stays sealed,
so nothing past the cut is requested. Pages are followed through `continuation`, which the API
returns as the next end_timestamp (it walks backwards in time).

Runs on the host's Python (stdlib only; the container's DNS failed in r52):

    python research_scripts/r57_dvol_probe.py

writes research_scripts/data/r58/dvol_<CUR>_1d.csv (gitignored) and data/r57/dvol_probe.json
(manifest: rows, first/last day, gaps, duplicates, OHLC sanity, sha256).
"""
import csv
import hashlib
import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'data', 'r58')
OUT = os.path.join(HERE, 'data', 'r57')
URL = 'https://www.deribit.com/api/v2/public/get_volatility_index_data'
START_MS = int(datetime(2019, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
END_MS = int(datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc).timestamp() * 1000)
DAY = 86_400_000
PAUSE_S = 0.5            # polite spacing; the docs page states no rate limit for this method


def fetch(cur):
    rows, end, pages = {}, END_MS, 0
    while True:
        q = urllib.parse.urlencode({'currency': cur, 'start_timestamp': START_MS, 'end_timestamp': end,
                                    'resolution': '1D'})
        with urllib.request.urlopen(f'{URL}?{q}', timeout=30) as r:
            res = json.load(r)['result']
        pages += 1
        for t, o, h, l, c in res['data']:
            rows.setdefault(int(t), []).append((o, h, l, c))
        cont = res.get('continuation')
        if not cont or not res['data'] or cont >= end or pages > 50:
            break
        end = int(cont)
        time.sleep(PAUSE_S)
    return rows, pages


def day(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime('%Y-%m-%d')


def main():
    os.makedirs(RAW, exist_ok=True)
    man = {'endpoint': URL, 'resolution': '1D', 'requested': [day(START_MS), day(END_MS)], 'currencies': {}}
    for cur in ('BTC', 'ETH'):
        rows, pages = fetch(cur)
        ts = sorted(rows)
        assert not ts or ts[-1] <= END_MS, 'row past the 2024 cut'
        dups = sum(len(v) > 1 for v in rows.values())
        gaps = [(day(a), day(b)) for a, b in zip(ts, ts[1:]) if b - a != DAY]
        bad = sum(not (v[0][2] <= min(v[0][0], v[0][3]) <= max(v[0][0], v[0][3]) <= v[0][1]) for v in rows.values())
        path = os.path.join(RAW, f'dvol_{cur}_1d.csv')
        with open(path, 'w', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(['ts_ms', 'day', 'open', 'high', 'low', 'close'])
            for t in ts:
                w.writerow([t, day(t), *rows[t][0]])
        closes = [rows[t][0][3] for t in ts]
        man['currencies'][cur] = {
            'rows': len(ts), 'pages': pages, 'first': day(ts[0]) if ts else None, 'last': day(ts[-1]) if ts else None,
            'duplicates': dups, 'gaps': gaps[:20], 'n_gaps': len(gaps), 'ohlc_violations': bad,
            'close_min_median_max': [min(closes), sorted(closes)[len(closes) // 2], max(closes)] if closes else None,
            'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest()}
        print(cur, json.dumps(man['currencies'][cur]))
    json.dump(man, open(os.path.join(OUT, 'dvol_probe.json'), 'w'), indent=2)


if __name__ == '__main__':
    main()
