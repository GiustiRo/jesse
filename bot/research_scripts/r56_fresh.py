"""r56 F6: the fresh validation set N2 (USDT-M perpetuals outside U50), selected and then downloaded.

Authorised by the user on 2026-10-26 as an untouched final check for r56 F10.

* select: from fapi/v1/exchangeInfo and fapi/v1/ticker/24hr, USDT-margined PERPETUAL contracts in
  status TRADING, onboarded before 2022-07-01, not in U50, base asset not a stablecoin; the 20 with
  the largest 24h quote volume. Written to data/r56/n2/universe_n2.json and committed BEFORE any
  download, so the list cannot depend on the data.
* download: 1h klines and funding from data.binance.vision for 2020-01..2024-12 only (2025 stays
  sealed, so it is not even fetched), SHA-256 checked, with r52_download's helpers.

    python research_scripts/r56_fresh.py select
    python research_scripts/r56_fresh.py download [--workers 6]
"""
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import numpy as np

import r52_download as dl

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r56', 'n2')
FAPI = 'https://fapi.binance.com/fapi/v1'
ONBOARD_BEFORE_MS = 1656633600000          # 2022-07-01 00:00 UTC
N_PICK = 20
STABLES = {'USDC', 'BUSD', 'TUSD', 'FDUSD', 'DAI', 'USDP', 'USDE', 'EUR'}
MONTHS = [f'{y}-{m:02d}' for y in range(2020, 2025) for m in range(1, 13)]


def _get(url):
    return json.loads(urllib.request.urlopen(url, timeout=30).read())


def select():
    os.makedirs(OUT, exist_ok=True)
    u50 = {u['symbol'] for u in json.load(open(os.path.join(HERE, 'data', 'r52', 'universe50.json')))}
    info = _get(f'{FAPI}/exchangeInfo')
    vol = {t['symbol']: float(t['quoteVolume']) for t in _get(f'{FAPI}/ticker/24hr')}
    cands = []
    for s in info['symbols']:
        if (s.get('contractType') == 'PERPETUAL' and s.get('quoteAsset') == 'USDT' and s.get('status') == 'TRADING'
                and int(s.get('onboardDate', 1 << 62)) < ONBOARD_BEFORE_MS and s['symbol'] not in u50
                and s.get('baseAsset') not in STABLES):
            cands.append({'symbol': s['symbol'], 'onboard': int(s['onboardDate']), 'vol24h': vol.get(s['symbol'], 0.0)})
    cands.sort(key=lambda x: -x['vol24h'])
    out = {'rule': __doc__.split('* select: ')[1].split('* download')[0].strip(), 'n_candidates': len(cands),
           'selected': cands[:N_PICK], 'next_in_line': cands[N_PICK:N_PICK + 10]}
    json.dump(out, open(os.path.join(OUT, 'universe_n2.json'), 'w'), indent=2)
    print(json.dumps([c['symbol'] for c in out['selected']]), len(cands), 'candidates')


def _one(sym):
    try:
        p1, pf = os.path.join(OUT, f'{sym}_1h.npy'), os.path.join(OUT, f'{sym}_funding.npy')
        if not os.path.exists(p1):
            np.save(p1, dl.klines(sym, '1h'))
        if not os.path.exists(pf):
            np.save(pf, dl.funding(sym))
        a = np.load(p1)
        res = {'symbol': sym, 'h1_rows': int(len(a)), 'h1_first': int(a[0, 0]) if len(a) else None,
               'h1_last': int(a[-1, 0]) if len(a) else None, 'funding_rows': int(len(np.load(pf)))}
    except Exception as e:  # one symbol failing must not stop the others; a re-run resumes
        res = {'symbol': sym, 'error': str(e)}
    print(json.dumps(res), flush=True)
    return res


def download(workers=6):
    dl.MONTHS = MONTHS            # r52's helpers read this module global: stop at 2024-12
    sel = [c['symbol'] for c in json.load(open(os.path.join(OUT, 'universe_n2.json')))['selected']]
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(_one, sel))
    for r in res:
        assert 'error' in r or r['h1_last'] is None or r['h1_last'] < 1735689600000, 'data past 2024'
    json.dump({'symbols': res, 'months': [MONTHS[0], MONTHS[-1]]}, open(os.path.join(OUT, 'manifest.json'), 'w'), indent=1)
    print('done')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'select':
        select()
    elif a and a[0] == 'download':
        download(int(a[2]) if len(a) > 2 and a[1] == '--workers' else 6)
    else:
        print(__doc__)
