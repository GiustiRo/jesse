"""r63: CLI of the last factory round on the full Binance USDT-M universe (PROTOCOL_R63).

    python -P r63.py partition      # F0a: universe + D63/L63 split from the S3 listing only (no prices)

H = N2 ∪ N3 and U50 never enter r63: they are dropped from the listing before anything is downloaded.
"""
import hashlib
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r63')
SEED = 63
CUT_MONTH = '2024-12'                 # last month read; 2025 is sealed and 2026 reserved
# Index and stablecoin contracts (no single underlying coin). TUSDT is the Threshold token, not TUSD.
EXCLUDE = {'BLUEBIRDUSDT', 'BTCDOMUSDT', 'DEFIUSDT', 'FOOTBALLUSDT', 'USDCUSDT'}
DEV_SHARE = 2 / 3


def _json(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=1)


def excluded_seen():
    """U50 (r52-r61 development) and H = N2 ∪ N3 (r59 oracle), read from their list files only."""
    u50 = [u['symbol'] for u in json.load(open(os.path.join(HERE, 'data', 'r52', 'universe50.json')))]
    n2 = [u['symbol'] for u in json.load(open(os.path.join(HERE, 'data', 'r56', 'n2', 'universe_n2.json')))['selected']]
    n3 = json.load(open(os.path.join(HERE, 'data', 'r58', 'n3_panel.json')))['n3_syms']
    return set(u50), set(n2) | set(n3)


def universe():
    """{symbol: (first month, last month)} of the r63 universe (PROTOCOL_R63 §1)."""
    raw = json.load(open(os.path.join(OUT, 'listing_raw.json')))['symbols']
    u50, h = excluded_seen()
    out = {}
    for s, months in raw.items():
        # USDT-margined perpetuals, including contracts archived as <SYM>USDT(_)SETTLED after a delisting
        if not re.fullmatch(r'[A-Z0-9]+USDT(_?SETTLED)*', s) or s in EXCLUDE or s in u50 or s in h:
            continue
        m = [x for x in months if x <= CUT_MONTH]
        if m:
            out[s] = (m[0], m[-1])
    return out


def partition():
    uni = universe()
    rng = np.random.default_rng(SEED)
    # strata: listing year x whether the archive stops before the cut (delisted inside the window)
    strata = {}
    for s, (a, b) in sorted(uni.items()):
        strata.setdefault((a[:4], b < CUT_MONTH), []).append(s)
    dev, loc = [], []
    for key in sorted(strata):
        syms = sorted(strata[key])
        perm = [syms[i] for i in rng.permutation(len(syms))]
        k = int(round(DEV_SHARE * len(perm)))
        dev += perm[:k]
        loc += perm[k:]
    dev, loc = sorted(dev), sorted(loc)
    body = {'D63': dev, 'L63': loc}
    sha = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    summary = {'/'.join(map(str, k)): {'n': len(v), 'D63': sum(s in set(dev) for s in v)} for k, v in sorted(strata.items())}
    _json('partition.json', {'protocol': 'PROTOCOL_R63 §1', 'seed': SEED, 'cut_month': CUT_MONTH,
                             'n_universe': len(uni), 'n_D63': len(dev), 'n_L63': len(loc),
                             'strata_year_endedbeforecut': summary, 'sha256': sha,
                             'months': {s: list(uni[s]) for s in sorted(uni)}, **body})
    print(f'universe {len(uni)}: D63 {len(dev)}, L63 {len(loc)}, sha256 {sha}')
    print(json.dumps(summary))


def load_partition():
    with open(os.path.join(OUT, 'partition.json')) as f:
        p = json.load(f)
    body = {'D63': p['D63'], 'L63': p['L63']}
    assert hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest() == p['sha256'], 'partition sha'
    return p


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'partition':
        partition()
    else:
        print(__doc__)
