"""r62: CLI of the guarded strategy factory (PROTOCOL_R62).

    python r62.py selftest          # §8 checks -> data/r62/f0_selftest.json
    python r62.py q4_selftest       # q4 template on a fake holdout (r60 CV half 1 of U50)
    python r62.py gen0_package      # writes the generation-0 package (leak-checked) for inspection

H = N2 ∪ N3 is only read through r59_oracle (q4); r59_holdout's guard is installed by r59.
"""
import json
import math
import os
import sys

import numpy as np

import r59  # noqa: F401  (installs the holdout guard before any loader runs)
import r62_dsl as dsl
import r62_eval as ev
import r62_factory as fx

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r62')
SEED = 62
Q4_FROM_MS = 1_625_184_000_000        # 2021-07-02 (§7.3.5)
Q4_PROGRAM = os.path.join(OUT, 'q4_program.json')
Q4_BOOT, Q4_BLOCK = 1000, 20


def _dump(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=1, default=fx._json_default)


def evaluator(with_oi=True):
    dsl.CASCADE_ENABLED = ev.cascade_gate()
    P = ev.real_panel(with_oi=with_oi and dsl.CASCADE_ENABLED)
    return ev.Evaluator(P, ev.load_bench('BENCH_P55_long'), ev.load_bench('BENCH_R1_long'))


# ----------------------------------------------------------------------------------------------
# §8 selftests
# ----------------------------------------------------------------------------------------------
def _toy_bars(n=3000, seed=0):
    rng = np.random.default_rng(seed)
    lr = rng.normal(0, 0.01, n)
    c = 100 * np.exp(np.cumsum(lr))
    o = np.r_[100, c[:-1]]
    h = np.maximum(o, c) * (1 + np.abs(rng.normal(0, 0.003, n)))
    l = np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.003, n)))
    t = 1_577_836_800_000 + np.arange(n) * dsl.HOUR
    return np.c_[t, o, h, l, c, np.ones(n)]


def selftest():
    res = {}
    rng = np.random.default_rng(SEED)
    # 1. parser and canonical hash
    q = dsl.random_program(rng, 'core_1h')
    bad = []
    for mut in (lambda x: x.update(universe='alts_1h'),
                lambda x: x['signal'][0]['params'].update(bogus=1),
                lambda x: x['exit'].update(kind='trailing'),
                lambda x: x.update(code='import os')):
        y = json.loads(json.dumps(q))
        mut(y)
        try:
            dsl.validate(y)
            bad.append('accepted')
        except dsl.DslError:
            bad.append('rejected')
    y = json.loads(json.dumps(q))
    y['signal'][0]['params'][sorted(y['signal'][0]['params'])[0]] = 999
    try:
        dsl.validate(y)
        bad.append('accepted')
    except dsl.DslError:
        bad.append('rejected')
    q2 = dict(universe='crypto_1h', signal=[{'kind': 'shock', 'params': {'z': 3, 'mode': 'fade'}}],
              filters=[{'kind': 'volreg', 'params': {'band': 'high'}}, {'kind': 'session', 'params': {'s': 'us'}}],
              exit={'kind': 'time', 'params': {'h': 6}}, exec={'kind': 'taker', 'params': {}})
    q3 = json.loads(json.dumps(q2))
    q3['filters'] = q3['filters'][::-1]
    res['1_parser'] = {'mutations': bad, 'hash_order_invariant': dsl.phash(q2) == dsl.phash(q3),
                       'ok': all(b == 'rejected' for b in bad) and dsl.phash(q2) == dsl.phash(q3)}
    # 2. maker fills and causality
    bars = _toy_bars()
    a = dsl.Asset('BTC', bars, '1h')
    qm = dict(universe='crypto_1h', signal=[{'kind': 'shock', 'params': {'z': 2, 'mode': 'fade'}}],
              exit={'kind': 'time', 'params': {'h': 6}}, exec={'kind': 'maker', 'params': {'off': 0.25, 'life': 1}})
    qm = dsl.validate(qm)
    i = 2000
    ev_ = np.zeros(len(bars), bool)
    ev_[i] = True
    d = np.ones(len(bars))
    lim = bars[i, 4] - 0.25 * a.atr[i]
    b2 = bars.copy()
    b2[i, 3] = lim * 0.5                                   # the signal bar itself trades far below
    b2[i + 1, 3] = lim * (1 - 0.5e-4)                      # next bar touches but does not cross 1 bp
    b2[i + 1, 2] = max(b2[i + 1, 2], b2[i + 1, 1])
    a2 = dsl.Asset('BTC', b2, '1h')
    a2.atr = a.atr                                         # keep the same limit level
    _, tr, uf = dsl.simulate(a2, qm, ev_, d)
    b3 = b2.copy()
    b3[i + 1, 3] = lim * (1 - 2e-4)                        # now it crosses by 2 bp
    a3 = dsl.Asset('BTC', b3, '1h')
    a3.atr = a.atr
    _, tr3, _ = dsl.simulate(a3, qm, ev_, d)
    fill_ok = (len(tr) == 0 and uf == 1 and len(tr3) == 1 and tr3[0][1] == i + 1 and abs(tr3[0][5] - lim) < 1e-9)
    caus = {}
    for s in ([{'kind': k, 'params': dsl._draw(dsl.SIGNALS[k], np.random.default_rng(k_))}
               for k_, k in enumerate(['zrev', 'rsi2', 'shock', 'voljump'])]):
        e1, d1 = dsl.signal_events(dsl.Asset('BTC', bars, '1h'), s)
        b4 = bars.copy()
        b4[i + 1:, 1:5] *= 1.3
        e2, d2 = dsl.signal_events(dsl.Asset('BTC', b4, '1h'), s)
        caus[s['kind']] = bool((e1[:i + 1] == e2[:i + 1]).all() and np.allclose(d1[:i + 1], d2[:i + 1]))
    for f in ({'kind': 'volreg', 'params': {'band': 'mid'}}, {'kind': 'trendveto', 'params': {'k': 20}}):
        m1 = dsl.filter_mask(dsl.Asset('BTC', bars, '1h'), f, np.ones(len(bars)))
        b4 = bars.copy()
        b4[i + 1:, 1:5] *= 1.3
        m2 = dsl.filter_mask(dsl.Asset('BTC', b4, '1h'), f, np.ones(len(bars)))
        caus[f['kind']] = bool((m1[:i + 1] == m2[:i + 1]).all())
    res['2_maker_causal'] = {'fill_rule_ok': bool(fill_ok), 'causal': caus, 'ok': bool(fill_ok and all(caus.values()))}
    # 3. spa_fast == r59.spa_pvalue
    g = np.random.default_rng(1).normal(0.0, 0.01, (600, 6)) + np.r_[0.0008, 0, 0, 0, 0, 0]
    p_ref, i_ref = r59.spa_pvalue(g, n_boot=300, seed=SEED)
    p_new, i_new, _, _ = ev.spa_fast(g, n_boot=300, seed=SEED)
    res['3_spa'] = {'r59': p_ref, 'fast': p_new, 'ok': abs(p_ref - p_new) < 1e-12 and i_ref == i_new}
    # 4. leak check on a contaminated text and on the real generation-0 package
    E = evaluator()
    leaks = {}
    for txt in ('{"x": "BTC"}', '{"year": 2022}', '{"d": "2021-05-19"}', '{"p": 43000.5}', '{"a": "luna crash"}'):
        try:
            fx.leak_check(txt)
            leaks[txt] = 'passed (FAIL)'
        except ValueError:
            leaks[txt] = 'stopped'
    arch = fx.Archive(E)
    try:
        pkg, _ = fx.package(arch, E.panel, 0, np.random.default_rng(SEED))
        real_ok = True
    except ValueError as e:
        real_ok, pkg = f'leak {e}', ''
    res['4_leak'] = {'contaminated': leaks, 'gen0_package_ok': real_ok, 'gen0_chars': len(pkg),
                     'ok': all(v == 'stopped' for v in leaks.values()) and real_ok is True}
    # 5. cells control: Donchian long (55-day high in, 20-day low out) on core daily
    res['5_donchian'] = donchian_control(E)
    # 6. data cut
    cut_ok = all((E.panel.src[n][k][:, 0] < 1_735_689_600_000).all() for n in E.panel.src for k in E.panel.src[n])
    res['6_cut'] = {'ok': bool(cut_ok)}
    res['cascade_enabled'] = dsl.CASCADE_ENABLED
    res['ok'] = all(v['ok'] for k, v in res.items() if isinstance(v, dict) and 'ok' in v)
    _dump('f0_selftest.json', res)
    print(json.dumps(res, indent=1, default=fx._json_default))
    return res


def donchian_control(E):
    """§8.5: a long-only Donchian 55/20 built outside the DSL with the same accounting must correlate
    with R1 (> 0.6) and land in a blocked cell; this checks the descriptors, not the factory."""
    per, trades = {}, {}
    for name in dsl.UNIVERSES['core_1d'][1]:
        a = E.panel.asset(name, '1d')
        c = a.b[:, dsl.C]
        hi55 = np.r_[[np.nan] * 55, [c[i - 55:i].max() for i in range(55, len(c))]]
        lo20 = np.r_[[np.nan] * 20, [c[i - 20:i].min() for i in range(20, len(c))]]
        tr, i, n = [], 56, len(c)
        while i < n - 1:
            if c[i] > hi55[i] and np.isfinite(a.sig_ann[i]):
                j = i + 1
                k = j
                while k < n - 1 and not (c[k] < lo20[k]):
                    k += 1
                k = min(k + 1, n - 1)
                sz = min(dsl.TARGET_VOL / a.sig_ann[i], dsl.MAX_LEV)
                tr.append((i, j, k, 1.0, sz, a.b[j, dsl.O] * (1 + a.slip), a.b[k, dsl.O] * (1 - a.slip),
                           dsl.TAKER_FEE, dsl.TAKER_FEE, 'taker'))
                i = k + 1
            else:
                i += 1
        br = dsl._pnl(a, tr)
        days, r = dsl.daily(a, br)
        start = ev.WINDOW_FROM['crypto' if ev.group_of(name) == 'crypto' else 'cfd']
        per[name] = (days[days >= start], r[days >= start])
        trades[name] = tr
    days, r = ev.basket(per)
    x1 = ev.align(days, r, *E.r1)
    q = dict(universe='core_1d', signal=[{'kind': 'zrev', 'params': {'k': 24, 'z': 2.0}}],
             exit={'kind': 'time', 'params': {'h': 24}}, exec={'kind': 'taker', 'params': {}},
             size={'kind': 'voltgt', 'params': {'side': 'long'}})
    desc = ev.descriptors(dsl.validate(q), per, trades, E.panel, (x1, E.r1[1]))
    cell = ev.cell_of(desc)
    return {'rho_r1': desc['rho_r1'], 'hold_days': desc['hold_days'], 'dir': desc['dir'], 'cell': cell,
            'sharpe': ev.sharpe(r), 'ok': bool(desc['rho_r1'] > 0.6 and ev.blocked(cell))}


# ----------------------------------------------------------------------------------------------
# q4 (§7.3.5): a crypto finalist on the 50 alts of H, committed before the query
# ----------------------------------------------------------------------------------------------
def bank_src(syms, dir_of):
    src = {}
    for s in syms:
        d = dir_of(s)
        h = np.load(os.path.join(d, f'{s}_1h.npy'))
        h = h[h[:, 0] < 1_735_689_600_000][:, :6]
        f = np.load(os.path.join(d, f'{s}_funding.npy'))
        f = f[f[:, 0] < 1_735_689_600_000]
        import r62_data
        src[s] = {'h1': h, 'd1': r62_data.hours_to_days(h, cfd=False), 'funding': f}
    return src


def q4_compute(h_syms, dir_of, program):
    """Margins (a) Sharpe - 0.3, (b) Sharpe with costs x2, (c) marginal vs P55 (0.85/0.15), each with
    a stationary-bootstrap SE (block 20, 1,000 draws, seed 62)."""
    q = dsl.validate(program)
    assert q['universe'] == 'crypto_1h', 'q4 only takes crypto_1h finalists'
    assert not any(s['kind'] == 'cascade' for s in q['signal']), 'no OI feed for the alts: cascade not applicable'
    src = bank_src(h_syms, dir_of)
    st = np.load(os.path.join(HERE, 'data', 'r55', 'f0_states.npy'))
    panel = ev.Panel(src, (st[:, 0].astype(np.int64), st[:, 2]))
    per, tr, _ = ev.run_program(q, panel, names=list(h_syms))
    per2, _, _ = ev.run_program(q, panel, cost_mult=2.0, cross=2 * dsl.CROSS, names=list(h_syms))
    days, r = ev.basket(per)
    d2, r2 = ev.basket(per2)
    p55d, p55 = ev.load_bench('BENCH_P55_common')
    keep = p55d >= Q4_FROM_MS
    p55d, p55 = p55d[keep], p55[keep]
    x, x2 = ev.align(days, r, p55d, p55), ev.align(d2, r2, p55d, p55)
    stats = lambda ix: (ev.sharpe(x[ix]), ev.sharpe(x2[ix]), ev.marginal(x[ix], p55[ix]))  # noqa: E731
    obs = stats(np.arange(len(x)))
    rng = np.random.default_rng(SEED)
    bs = np.array([stats(r59.stationary_idx(len(x), rng, Q4_BLOCK)) for _ in range(Q4_BOOT)])
    se = np.nanstd(bs, axis=0)
    st_ = {'sharpe': obs[0], 'sharpe_cost2': obs[1], 'marginal': obs[2], 'se': se.tolist(), 'days': int(len(x)),
           'n_coins': len(h_syms), 'trades': int(sum(len(v) for v in tr.values())), 'program': q}
    margins = [('a_sharpe_minus_0_3', obs[0] - 0.3, float(se[0])),
               ('b_cost2_sharpe', obs[1], float(se[1])),
               ('c_marginal_vs_p55', obs[2], float(se[2]))]
    return {'margins': margins, 'stats': st_}


def q4_power(sharpe_d, n_days):
    """§7.3.5: P(pass a) for half the development effect; Lo (2002) SE with normal moments."""
    from statistics import NormalDist
    se = math.sqrt((1 + 0.5 * (sharpe_d / math.sqrt(365)) ** 2) / n_days) * math.sqrt(365)
    return NormalDist().cdf((0.5 * sharpe_d - 0.3) / se), se


def q4_selftest():
    """Fake holdout = r60 CV half 1 (U50 alts); r59's oracle checks on q4's real computation with a
    fixed demo program. H and the real log are never touched."""
    import tempfile
    import r59_oracle as orc
    import r60
    fake = json.load(open(os.path.join(r60.OUT, 'cv_halves.json')))['halves']['1']
    prog = dict(universe='crypto_1h', signal=[{'kind': 'shock', 'params': {'z': 3, 'mode': 'fade'}}],
                exit={'kind': 'time', 'params': {'h': 6}}, exec={'kind': 'maker', 'params': {'off': 0.5, 'life': 3}})
    direct = q4_compute(fake, lambda s: r60.U50_DIR, prog)
    crits = {'st_q4': {'fn': lambda c: q4_compute(fake, lambda s: r60.U50_DIR, prog), 'alpha': 0.05, 'desc': 'q4 fake'},
             'st_true': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'},
             'st_false': {'fn': lambda c: {'margins': [('f', -1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 'f'}}
    tmp = tempfile.mkdtemp(prefix='r62_q4_selftest_')
    kw = dict(log_path=os.path.join(tmp, 'log.jsonl'), sealed_dir=os.path.join(tmp, 'sealed'), commit='selftest',
              dirty_fn=lambda: '', sync=False)
    ans = {q: orc.run_query(q, crits, {}, noise=0.0, **kw) for q in ('st_q4', 'st_true', 'st_false')}
    exp = {'st_q4': 'PASA' if all(m > 0 for _, m, _ in direct['margins']) else 'NO PASA', 'st_true': 'PASA',
           'st_false': 'NO PASA'}
    res = {'fake_holdout_n': len(fake), 'direct_margins': direct['margins'],
           'direct_stats': {k: v for k, v in direct['stats'].items() if k != 'program'},
           'answers': ans, 'ok': ans == exp}
    _dump('f0_q4_selftest.json', res)
    print(json.dumps(res, indent=1, default=fx._json_default))
    return res


def gen0_package():
    E = evaluator()
    pkg, _ = fx.package(fx.Archive(E), E.panel, 0, np.random.default_rng(SEED))
    with open(os.path.join(OUT, 'gen0_package_example.json'), 'w', encoding='utf-8') as f:
        f.write(pkg)
    print(len(pkg))


if __name__ == '__main__':
    {'selftest': selftest, 'q4_selftest': q4_selftest, 'gen0_package': gen0_package}[sys.argv[1]]()
