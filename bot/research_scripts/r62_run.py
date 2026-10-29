"""r62: one factory run, step by step, so the Claude Code session can put a subagent between steps.

    python r62_run.py init   <run> <kind> <seed>    # kind: real | noise | planted
    python r62_run.py pkg    <run> <gen>            # -> runs/<run>/pkg_<gen>.json (+ aliases)
    python r62_run.py ingest <run> <gen> <answer>   # LLM answer file -> evaluations (origin 'llm')
    python r62_run.py ga     <run> <gen>            # local genetic search, GA_PER_GEN evaluations
    python r62_run.py final  <run>                  # finalists + SPA over every series of the run

State lives in data/r62/runs/<run>/state.pkl. Only `real` runs write the r59 series store and
TRIAL_REGISTRY (N_fab); synthetic runs keep their series in the run folder (§0: they do not count).
"""
import json
import os
import pickle
import sys

import numpy as np

import r59  # noqa: F401  (holdout guard)
import r62_dsl as dsl
import r62_eval as ev
import r62_factory as fx

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, 'data', 'r62', 'runs')
SEED = 62
# F1 calibration of the planted edges (data/r62/f1_calib_grid.json, seeds 101-106): kappa 0.20 gives
# the P1 oracle a mean net Sharpe of 0.80; P2 tops out at ~0.5 (alpha 50) under taker costs (E3).
PLANTED = {'kappa': 0.20, 'alpha': 50.0}
SPA_ALPHA = 0.05
MAX_TOOL_USES = 3
ROT_WORKERS = 5                      # per run; four runs in parallel stay within the 22 cores                    # E3.4: Read its package, Write its answer, and the hand-back


def _dir(run):
    return os.path.join(RUNS, run)


_W = {}


def _winit(kind, seed):
    _W['E'] = evaluator(kind, seed)


def _wrot(args):
    q, chunk = args
    return [_W['E'].rot_sharpe(q, f) for f in chunk]


def parallel_rot(E, kind, seed, workers=ROT_WORKERS):
    """rot_fn for the Archive: the 200 rotations of a cell winner spread over a process pool."""
    import multiprocessing as mp
    pool = mp.get_context('spawn').Pool(workers, initializer=_winit, initargs=(kind, seed))

    def mapper(q, fracs):
        chunks = [fracs[i::workers] for i in range(workers)]
        res = pool.map(_wrot, [(q, c) for c in chunks])
        out = [None] * len(fracs)
        for i, r in enumerate(res):
            out[i::workers] = r
        return out
    return (lambda q: E.rotation_p(q, mapper=mapper)), pool


def _load(run):
    with open(os.path.join(_dir(run), 'state.pkl'), 'rb') as f:
        st = pickle.load(f)
    E = evaluator(st['kind'], st['seed'])
    rot, _ = parallel_rot(E, st['kind'], st['seed'])
    arch = fx.Archive(E, log_path=os.path.join(_dir(run), 'log.jsonl'),
                      series_round='r62' if st['kind'] == 'real' else None, rot_fn=rot)
    arch.cells, arch.seen, arch.series = st['cells'], st['seen'], st['series']
    return st, arch


def _save(run, st, arch):
    st.update(cells=arch.cells, seen=arch.seen, series=arch.series)
    tmp = os.path.join(_dir(run), 'state.tmp')
    with open(tmp, 'wb') as f:
        pickle.dump(st, f)
    os.replace(tmp, os.path.join(_dir(run), 'state.pkl'))


def evaluator(kind, seed):
    dsl.CASCADE_ENABLED = ev.cascade_gate()
    p55, r1 = ev.load_bench('BENCH_P55_long'), ev.load_bench('BENCH_R1_long')
    if kind == 'real':
        P = ev.real_panel(with_oi=dsl.CASCADE_ENABLED)
    else:
        import r62_synth as sy
        P = sy.panel(kind, seed, planted=PLANTED if kind == 'planted' else None)
        # E2 applies to the synthetic OI feed too (same availability as the real one)
        P._a.clear()
    return ev.Evaluator(P, p55, r1)


def init(run, kind, seed):
    os.makedirs(_dir(run), exist_ok=True)
    assert not os.path.exists(os.path.join(_dir(run), 'state.pkl')), f'{run} exists'
    st = {'kind': kind, 'seed': int(seed), 'cells': {}, 'seen': {}, 'series': {}, 'gens': {}}
    E = evaluator(kind, int(seed))
    arch = fx.Archive(E, log_path=os.path.join(_dir(run), 'log.jsonl'),
                      series_round='r62' if kind == 'real' else None)
    rng = np.random.default_rng(SEED)
    for _ in range(fx.N_SEED):
        arch.add(dsl.random_program(rng), 'seed', -1)
    st['gens']['seed'] = {'n': arch.n()}
    _save(run, st, arch)
    _status(run, st, arch)


def pkg(run, gen):
    st, arch = _load(run)
    rng = np.random.default_rng([SEED, int(gen), st['seed'], 7])
    text, al = fx.package(arch, arch.E.panel, int(gen), rng)
    with open(os.path.join(_dir(run), f'pkg_{gen}.json'), 'w', encoding='utf-8') as f:
        f.write(text)
    with open(os.path.join(_dir(run), f'aliases_{gen}.pkl'), 'wb') as f:
        pickle.dump(al, f)
    print(os.path.join(_dir(run), f'pkg_{gen}.json'), len(text))


def ingest(run, gen, answer_path, tool_uses='0'):
    st, arch = _load(run)
    with open(os.path.join(_dir(run), f'aliases_{gen}.pkl'), 'rb') as f:
        al = pickle.load(f)
    with open(answer_path, encoding='utf-8') as f:
        text = f.read()
    rec = {'tool_uses': int(tool_uses), 'parsed': 0, 'new': 0}
    if int(tool_uses) > MAX_TOOL_USES:
        rec['discarded'] = 'subagent used tools beyond Read pkg + Write answer + hand-back (E3.4)'
    else:
        progs = fx.ingest(text, al)
        rec['parsed'] = len(progs)
        for q in progs:
            if arch.add(q, 'llm', int(gen)) is not None:
                rec['new'] += 1
    g = st['gens'].setdefault(str(gen), {})
    g['llm_reingest' if 'llm' in g else 'llm'] = rec
    _save(run, st, arch)
    print(json.dumps(rec))


def ga(run, gen):
    st, arch = _load(run)
    rng = np.random.default_rng([SEED, int(gen), st['seed'], 11])
    made = fx.ga_step(arch, rng, fx.GA_PER_GEN, int(gen))
    st['gens'].setdefault(str(gen), {})['ga'] = made
    _save(run, st, arch)
    if st['kind'] == 'real':
        save_series_batch(arch, st)
        fx.write_counter(arch.n(), gen, f'run {run}')
    _status(run, st, arch)


def save_series_batch(arch, st):
    """Every not-yet-stored series of a real run into the r59 store (round 'r62', ids R62_P_<hash10>),
    float32 to keep the file small (§0); the manifest carries the sha256 of the stored bytes, so
    r59.load_series verifies them unchanged. One write per generation instead of one per program."""
    import hashlib
    import r59
    root = r59.SERIES
    path = os.path.join(root, 'r62.npz')
    cur = dict(np.load(path)) if os.path.exists(path) else {}
    mpath = os.path.join(root, 'manifest.json')
    with open(mpath) as f:
        man = json.load(f)
    new = 0
    for h, (d, r) in arch.series.items():
        tid = f'R62_P_{h[:10]}'
        if tid in man['series']:
            continue
        d = np.asarray(d, np.int64)
        r = np.asarray(r, np.float32)
        assert (np.diff(d) > 0).all() and d[-1] < 1_735_689_600_000
        cur[f'{tid}__days'], cur[f'{tid}__ret'] = d, r
        man['series'][tid] = {'file': 'r62.npz', 'script': 'r62_run.py (factory)', 'window': 'r62 dev',
                              'n_days': int(len(d)), 'dtype': 'float32',
                              'sha256': hashlib.sha256(d.tobytes() + r.tobytes()).hexdigest()}
        new += 1
    if new:
        np.savez_compressed(path, **cur)
        with open(path, 'rb') as f:
            man['files']['r62.npz'] = hashlib.sha256(f.read()).hexdigest()
        with open(mpath, 'w') as f:
            json.dump(man, f, indent=1)
    st['series_saved'] = len([k for k in man['series'] if k.startswith('R62_P_')])


def _status(run, st, arch):
    cells = {c: (round(r['score'], 3), r['origin'], round(r['sharpe'], 2)) for c, r in arch.cells.items()}
    out = {'run': run, 'kind': st['kind'], 'n': arch.n(), 'cells': cells}
    print(json.dumps(out))


def spa_matrices(arch, p55):
    """Columns = every program of the run on P55's days (0 when flat): (a) the series itself,
    (b) the vol-matched combination 0.85 P55 + 0.15 x~ rescaled to P55's vol, minus P55 (E3)."""
    pd_, pr = p55
    hs = sorted(arch.series)
    A = np.zeros((len(pd_), len(hs)))
    B = np.zeros_like(A)
    for i, h in enumerate(hs):
        d, r = arch.series[h]
        x = ev.align(d, r, pd_, pr)
        A[:, i] = x
        if x.std() > 0:
            xs = x * pr.std() / x.std()
            c = (1 - ev.W_MARG) * pr + ev.W_MARG * xs
            B[:, i] = c * pr.std() / c.std() - pr
        else:
            B[:, i] = -pr * 0                      # a flat program adds nothing
    return hs, A, B


def final(run):
    st, arch = _load(run)
    fins = arch.finalists()
    hs, A, B = spa_matrices(arch, arch.E.p55)
    out = {'run': run, 'kind': st['kind'], 'n_programs': len(hs), 'n_cells': len(arch.cells), 'finalists': []}
    for name, G in (('cash', A), ('marginal', B)):
        p, imax, Tb, t = ev.spa_fast(G, seed=SEED)
        crit = float(np.quantile(Tb, 1 - SPA_ALPHA))
        out[f'spa_{name}'] = {'p': p, 'argmax': hs[imax], 'crit_t': crit}
        out[f'_t_{name}'] = {h: float(t[i]) for i, h in enumerate(hs)}
    for r in fins:
        h = r['hash']
        row = {'hash': h, 'cell': r['cell'], 'score': r['score'], 'sharpe': r['sharpe'],
               'marginal': r['marginal'], 'rot_p': r['rot_p'], 'origin': r['origin'], 'gen': r['gen'],
               'program': r['program']}
        for name in ('cash', 'marginal'):
            s = out[f'spa_{name}']
            ti = out[f'_t_{name}'][h]
            row[f'spa_{name}_p'] = s['p']
            row[f't_{name}'] = ti
            row[f'spa_{name}_pass'] = bool(s['p'] < SPA_ALPHA and (s['argmax'] == h or ti > s['crit_t']))
        row['spa_pass'] = row['spa_cash_pass'] and row['spa_marginal_pass']
        row['planted_piece'] = _planted_piece(r['program'])
        out['finalists'].append(row)
    out.pop('_t_cash')
    out.pop('_t_marginal')
    with open(os.path.join(_dir(run), 'final.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1, default=fx._json_default)
    print(json.dumps(out, indent=1, default=fx._json_default))


def _planted_piece(q):
    kinds = [s['kind'] for s in q['signal']]
    if q['universe'] in ('crypto_1h', 'core_1h') and any(
            s['kind'] == 'shock' and s['params']['mode'] == 'fade' for s in q['signal']):
        return 'P1'
    if q['universe'] == 'pair_WTI_GAS' and 'spread_z' in kinds:
        return 'P2'
    return None


if __name__ == '__main__':
    cmd, args = sys.argv[1], sys.argv[2:]
    {'init': init, 'pkg': pkg, 'ingest': ingest, 'ga': ga, 'final': final}[cmd](*args)
