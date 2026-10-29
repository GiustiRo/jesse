"""r63: CLI of the last factory round on the full Binance USDT-M universe (PROTOCOL_R63).

    python -P r63.py partition      # F0a: universe + D63/L63 split from the S3 listing only (no prices)
    python -P r63.py selftest       # F0b §8 checks -> data/r63/f0_selftest.json
    python -P r63.py coverage       # F0b coverage tables -> data/r63/f0_coverage.json
    python -P r63.py bench          # F0b timing / CPU / memory of the evaluator on the full D63 panel

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


# ----------------------------------------------------------------------------------------------
# F0b: selftests (§8), coverage and benchmark
# ----------------------------------------------------------------------------------------------
def _toy_tramo(n=2400, seed=0, t0=1_640_995_200_000):
    """Hourly bars [t, o, h, l, c, vol, qvol, taker] of a random walk with 5M USDT a day."""
    rng = np.random.default_rng(seed)
    c = 10 * np.exp(np.cumsum(rng.normal(0, 0.01, n)))
    o = np.r_[10, c[:-1]]
    h = np.maximum(o, c) * (1 + np.abs(rng.normal(0, 0.003, n)))
    lo = np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.003, n)))
    t = t0 + np.arange(n) * 3_600_000
    return np.c_[t, o, h, lo, c, np.full(n, 1e4), np.full(n, 5e6 / 24), np.full(n, 5e3)]


def _asset(g, elig=True, end_slip=0.0):
    import r63_dsl as d63
    e = np.full(len(g), bool(elig))
    return d63.AltAsset('T#0', g, '1h', None, None, e, np.full(len(g), 5e-4), end_slip)


def selftest():
    import r59
    import r62_dsl as dsl
    import r62_eval as ev
    import r63_data as rd
    import r63_dsl as d63
    import r63_eval as E6
    res = {}
    p = load_partition()                                 # asserts the committed sha
    dev, loc = set(p['D63']), set(p['L63'])
    u50, h = excluded_seen()
    # 3. data: partition, exclusions, cut
    files = [f for f in os.listdir(rd.BARS) if f.endswith('_1h.npy')]
    syms = {f[:-len('_1h.npy')] for f in files}
    last = max(float(np.load(os.path.join(rd.BARS, f))[:, 0].max(initial=0)) for f in files)
    lastf = max(float(np.load(os.path.join(rd.BARS, f))[:, 0].max(initial=0))
                for f in os.listdir(rd.BARS) if f.endswith('_funding.npy'))
    res['data'] = {'disjoint': not (dev & loc), 'all_in_universe': syms <= dev | loc,
                   'no_u50_no_h': not (syms & (u50 | h)), 'last_bar_before_cut': last < rd.CUT_MS,
                   'last_funding_before_cut': lastf < rd.CUT_MS}
    res['n_files'] = len(syms)
    # 1. eligibility without look-ahead: changing volume from day d on leaves days <= d unchanged
    g = _toy_tramo(24 * 200)
    days, e1, m1 = rd.eligibility([g], int(g[0, 0]))
    cut = 150
    g2 = g.copy()
    later = g2[:, 0] >= days[cut]
    g2[later, 6] *= np.random.default_rng(1).uniform(0, 3, later.sum())
    _, e2, m2 = rd.eligibility([g2], int(g[0, 0]))
    res['elig_causal'] = bool((e1[:cut + 1] == e2[:cut + 1]).all()
                              and np.allclose(m1[:cut + 1], m2[:cut + 1], equal_nan=True)
                              and not np.allclose(m1[cut + 1:], m2[cut + 1:]))
    res['elig_age'] = bool(not e1[:90].any() and e1[90:].all())
    res['slip_tiers'] = rd.slip_of(np.array([np.nan, 1e6, 2e7, 6e7])).tolist() == [20e-4, 20e-4, 10e-4, 5e-4]
    # cleaning: a 10h gap is filled flat, a 30h gap splits, the dead tail is trimmed
    a = _toy_tramo(24 * 120)
    a = np.delete(a, np.r_[100:110, 1500:1530], axis=0)
    a[-50:, 5] = 0
    tr = rd.clean(a)
    res['clean'] = bool(len(tr) == 2 and len(tr[0]) == 1500 and (tr[0][100:110, 5] == 0).all()
                        and (tr[0][100:110, 4] == tr[0][99, 4]).all() and tr[1][-1, 0] == a[-51, 0])
    # 4. parser on the r63 catalogue
    d63.configure(['T#0'])
    bad = []
    for q in ({'universe': 'alts_1h', 'signal': [{'kind': 'spread_z', 'params': {'k': 24, 'z': 2.0}}]},
              {'universe': 'alts_1h', 'signal': [{'kind': 'cascade', 'params': {'z_oi': 2, 'z_ret': 2, 'mode': 'fade'}}]},
              {'universe': 'alts_1h', 'signal': [{'kind': 'clock', 'params': {'event': 'cme_gap', 'mode': 'fade'}}]},
              {'universe': 'core_1h', 'signal': [{'kind': 'shock', 'params': {'z': 3, 'mode': 'fade'}}]},
              {'universe': 'alts_1d', 'signal': [{'kind': 'clock', 'params': {'event': 'month_end', 'mode': 'fade'}}]}):
        q.update(exit={'kind': 'time', 'params': {'h': 6}}, exec={'kind': 'taker', 'params': {}})
        try:
            dsl.validate(q)
            bad.append(q['signal'][0]['kind'])
        except dsl.DslError:
            pass
    rng = np.random.default_rng(SEED)
    qs = [dsl.random_program(rng) for _ in range(200)]
    res['parser'] = {'rejects_out_of_catalogue': not bad,
                     'random_ok': all(q['universe'] in ('alts_1h', 'alts_1d') for q in qs),
                     'hash_order_free': dsl.phash(qs[0]) == dsl.phash(dict(reversed(list(qs[0].items()))))}
    # 2. end of tramo: an open position closes at the last close (delisted: taker + 100 bp)
    g = _toy_tramo(24 * 60)
    q = dsl.validate({'universe': 'alts_1h', 'signal': [{'kind': 'shock', 'params': {'z': 2, 'mode': 'fade'}}],
                      'exit': {'kind': 'time', 'params': {'h': 120}}, 'exec': {'kind': 'taker', 'params': {}}})
    out = {}
    for kind, es in (('delisted', rd.DELIST_SLIP), ('cut', 0.0)):
        ev_ = np.zeros(len(g), bool)
        ev_[len(g) - 30] = True
        _, trades, _ = d63.simulate(_asset(g, end_slip=es), q, ev_, np.ones(len(g)))
        t = trades[-1]
        out[kind] = bool(t[2] == len(g) - 1 and t[9] == 'end' and t[8] == dsl.TAKER_FEE
                         and abs(t[6] - g[-1, 4] * (1 - max(es, 5e-4))) < 1e-12)
    res['end_of_tramo'] = out
    res['elig_blocks_entries'] = not d63.entry_events(_asset(g, elig=False), q)[0].any()
    # maker: a bar touching the limit within 1 bp does not fill; one crossing it fills on that bar
    g = _toy_tramo(24 * 40)
    a = _asset(g)
    qm = dsl.validate({'universe': 'alts_1h', 'signal': [{'kind': 'shock', 'params': {'z': 2, 'mode': 'fade'}}],
                       'exit': {'kind': 'time', 'params': {'h': 6}},
                       'exec': {'kind': 'maker', 'params': {'off': 0.25, 'life': 1}}})
    i = 900
    ev_ = np.zeros(len(g), bool)
    ev_[i] = True
    lim = g[i, 4] - 0.25 * a.atr[i]
    mk = {}
    for name, pen in (('touch_no_fill', 0.5e-4), ('cross_fills', 3e-4)):
        gx = g.copy()
        gx[i + 1, 3] = lim * (1 - pen)
        ax = _asset(gx)
        ax.atr = a.atr
        _, trx, ufx = d63.simulate(ax, qm, ev_, np.ones(len(g)))
        mk[name] = bool((ufx == 1 and not trx) if pen < 1e-4 else (trx and trx[0][1] == i + 1))
    res['maker'] = mk
    # signals at t use data <= t only
    gg = g.copy()
    gg[i + 1:, 1:5] *= 1.7
    b = _asset(gg)
    ok = True
    for k in dsl.SIGNALS:
        for _ in range(3):
            s = {'kind': k, 'params': dsl._draw(dsl.SIGNALS[k], rng)}
            x1, y1 = d63._R62_SIGNAL_EVENTS(a, s)
            x2, y2 = d63._R62_SIGNAL_EVENTS(b, s)
            ok &= bool((x1[:i + 1] == x2[:i + 1]).all() and np.allclose(y1[:i + 1], y2[:i + 1]))
    res['signals_causal'] = ok
    per = {'a': (np.array([0, 1, 2]), np.array([1.0, 2.0, 3.0])), 'b': (np.array([1, 2]), np.array([4.0, 5.0]))}
    res['basket_active_mean'] = E6.basket(per)[1].tolist() == [1.0, 3.0, 4.0]
    G = np.random.default_rng(3).normal(0.0005, 0.01, (400, 6))
    res['spa_equal'] = abs(ev.spa_fast(G, n_boot=300, seed=7)[0] - r59.spa_pvalue(G, n_boot=300, seed=7)[0]) < 1e-12
    flags = [v for v in res.values() if isinstance(v, bool)]
    flags += [v for d in res.values() if isinstance(d, dict) for v in d.values()]
    res['all_pass'] = all(flags)
    _json('f0_selftest.json', res)
    print(json.dumps(res, indent=1))


def coverage():
    man = json.load(open(os.path.join(OUT, 'manifest.json')))
    out = {}
    yrs = [str(y) for y in range(2020, 2025)]
    for st in ('D63', 'L63'):
        rows = [r for r in man.values() if r['set'] == st]
        us = [r for r in rows if r.get('usable')]
        out[st] = {'symbols': len(rows), 'usable': len(us),
                   'eligible_symbols_by_year': {y: sum(r['elig_by_year'][y] > 0 for r in us) for y in yrs},
                   'mean_eligible_per_day_by_year': {y: round(sum(r['elig_by_year'][y] for r in us) / 365, 1) for y in yrs},
                   'tramos': sum(r['n_tramos'] for r in us), 'split_symbols': sum(r['n_tramos'] > 1 for r in us),
                   'delisted_in_window': sum(r['delisted'] for r in us),
                   'delisted_list': sorted(s for s, r in man.items() if r['set'] == st and r.get('delisted')),
                   'never_eligible': sum(r['elig_days'] == 0 for r in us),
                   'filled_hours': sum(r['filled_h'] for r in us)}
    _json('f0_coverage.json', out)
    print(json.dumps(out, indent=1))


def bench(n=24):
    """Timing / CPU / memory of evaluate() on the full D63 panel; no score or Sharpe is printed."""
    import time
    import psutil
    import r62_dsl as dsl
    import r63_eval as E6
    t0 = time.time()
    src = E6.load_src(E6.dev_syms())
    t_load = time.time() - t0
    E = E6.evaluator(src)
    pr = psutil.Process()
    rng = np.random.default_rng(1234)
    qs = [dsl.random_program(rng) for _ in range(n)]
    t1 = time.time()
    for q in qs[:n // 2]:
        E.evaluate(q)
    cold = (time.time() - t1) / (n // 2)
    t2 = time.time()
    for q in qs[n // 2:]:
        E.evaluate(q)
    warm = (time.time() - t2) / (n - n // 2)
    t3 = time.time()
    E.rot_sharpe(qs[0], 0.3)
    vm = psutil.virtual_memory()
    out = {'tramos': len(src), 'bars_1h': int(sum(len(v['h1']) for v in src.values())), 'load_s': round(t_load, 1),
           'eval_s_cold': round(cold, 2), 'eval_s_warm': round(warm, 2), 'rotation_s': round(time.time() - t3, 2),
           'rss_mb_one_worker': pr.memory_info().rss >> 20, 'ram_total_mb': vm.total >> 20,
           'ram_available_mb': vm.available >> 20, 'cpu_logical': psutil.cpu_count(),
           'cpu_percent_now': psutil.cpu_percent(1)}
    _json('f0_bench.json', out)
    print(json.dumps(out, indent=1))


# ----------------------------------------------------------------------------------------------
# F1: kappa of the planted P1 edge (§6), seeds 6301-6306, before any factory run
# ----------------------------------------------------------------------------------------------
KAPPA_GRID = (0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)
# E1: with P1 in every D63 symbol the 0.8 target falls between the first grid values 0.15 and 0.20.
KAPPA_GRID_E1 = (0.16, 0.165, 0.17, 0.175, 0.18)   # E1: fine grid between 0.15 (0.45) and 0.20 (1.51), 100% share
KAPPA_SEEDS = tuple(range(6301, 6307))
_K = {}


def _kinit():
    import r63_eval as E6
    _K['real'] = E6.load_src(E6.dev_syms())


def _kjob(args):
    import r62_eval as ev
    import r63_eval as E6
    import r63_synth as sy
    kappa, seed = args
    E = E6.evaluator(sy.panel_src(_K['real'], seed, kappa=kappa))
    per, tr, _ = E6.run_program(sy.ORACLE, E.panel)
    return kappa, seed, ev.sharpe(E6.basket(per)[1]), sum(len(v) for v in tr.values())


def kappa(workers=6, grid=KAPPA_GRID):
    import multiprocessing as mp
    jobs = [(k, s) for k in grid for s in KAPPA_SEEDS]
    with mp.get_context('spawn').Pool(workers, initializer=_kinit) as pool:
        res = pool.map(_kjob, jobs, chunksize=1)
    prev = os.path.join(OUT, 'f1_kappa.json')
    out = json.load(open(prev))['grid'] if os.path.exists(prev) else {}
    for k, s, sh, nt in res:
        out.setdefault(f'kappa_{k}', []).append({'seed': s, 'sharpe': sh, 'trades': nt})
    summ = {k: float(np.mean([x['sharpe'] for x in v])) for k, v in out.items()}
    ok = [float(k.split('_')[1]) for k, m in summ.items() if abs(m - 0.8) <= 0.1]
    # §6: the grid value whose mean is within 0.8 +- 0.1, the one closest to 0.8 if several
    pick = min(ok, key=lambda k: abs(summ[f'kappa_{k}'] - 0.8)) if ok else None
    _json('f1_kappa.json', {'grid': out, 'mean_sharpe': summ, 'kappa': pick, 'oracle': __import__('r63_synth').ORACLE})
    print(json.dumps({'mean_sharpe': summ, 'kappa': pick}, indent=1))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'kappa':
        kappa(int(sys.argv[2]) if len(sys.argv) > 2 else 6,
              KAPPA_GRID_E1 if sys.argv[3:] == ['e1'] else KAPPA_GRID)
        sys.exit(0)
    if cmd == 'partition':
        partition()
    elif cmd == 'selftest':
        selftest()
    elif cmd == 'coverage':
        coverage()
    elif cmd == 'bench':
        bench()
    else:
        print(__doc__)
