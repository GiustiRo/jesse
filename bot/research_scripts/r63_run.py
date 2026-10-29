"""r63: one factory run end to end in a single native process (PROTOCOL_R63 §5-§6).

    python -P r63_run.py run   <run> <kind> <seed> [--kappa K] [--workers W]   # kind: real | noise | planted
    python -P r63_run.py final <run>                                           # finalists + SPA of every series

No LLM proposer (§0). A generation draws its ~160 children from the archive as it stood when the
generation began (rng seeded by run seed and generation), evaluates them in a process pool, and then
inserts them in draw order; so the result does not depend on the number of workers. State is saved
after every generation and a re-run resumes from the last finished one. Only `real` runs write the
r59 series store and TRIAL_REGISTRY (N_fab).
"""
import argparse
import hashlib
import json
import multiprocessing as mp
import os
import pickle
import sys
import time

import numpy as np

import r62_dsl as dsl
import r62_eval as ev
import r62_factory as fx
import r63_eval as E6

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, 'data', 'r63', 'runs')
SEED = 63
GENERATIONS, N_SEED, PER_GEN = 10, 20, 160
N_FAB_CEILING = 2000                  # §0: new real programs of r63
SPA_ALPHA = 0.05
ROT_BATCH = 40                        # rotations evaluated per pool round
# e3 needs p = (1 + #{rot >= obs}) / 201 < 0.10, i.e. at most 19 rotated Sharpes >= the real one;
# once 20 are reached the program fails whatever the remaining rotations give, so they are skipped.
ROT_FAIL_AT = 20


def _dir(run):
    return os.path.join(RUNS, run)


# ----------------------------------------------------------------------------------------------
# Panels (built identically in the parent and in every worker)
# ----------------------------------------------------------------------------------------------
def build_src(kind, seed, kappa):
    real = E6.load_src(E6.dev_syms())
    if kind == 'real':
        return real
    import r63_synth as sy
    return sy.panel_src(real, int(seed), kappa=kappa if kind == 'planted' else 0.0)


_W = {}


def _winit(kind, seed, kappa):
    _W['E'] = E6.evaluator(build_src(kind, seed, kappa))


def _weval(q):
    rec = _W['E'].evaluate(q)
    return rec


def _wrot(args):
    q, fracs = args
    return [_W['E'].rot_sharpe(q, f) for f in fracs]


# ----------------------------------------------------------------------------------------------
# Generation step
# ----------------------------------------------------------------------------------------------
def draw_children(arch, rng, n, pending):
    """Up to n new legal programs (unique hashes) from the elites, then random fill (r62 E4)."""
    elites = arch.elites()
    pool = elites or fx._top_seen(arch)
    out, tries = [], 0

    def take(q, origin):
        try:
            q = dsl.validate(q)
        except dsl.DslError:
            return False
        h = dsl.phash(q)
        if h in arch.seen or h in pending:
            return False
        pending.add(h)
        out.append((q, origin))
        return True
    while len(out) < n and tries < 10 * n:
        tries += 1
        if not pool:
            take(dsl.random_program(rng), 'ga')
            continue
        u = rng.random()
        parent = pool[int(rng.integers(len(pool)))]['program']
        if u < fx.OPS[0][1]:
            child = fx.mutate(parent, rng)
        elif u < fx.OPS[0][1] + fx.OPS[1][1]:
            child = fx.swap(parent, rng)
        else:
            same = [r for r in pool if r['cell'][:4] == pool[0]['cell'][:4]] or pool
            other = same[int(rng.integers(len(same)))]['program']
            child = fx.cross(parent, other, rng) if other['universe'] == parent['universe'] else fx.mutate(parent, rng)
        take(child, 'ga')
    while len(out) < n:
        take(dsl.random_program(rng), 'ga_random')
    return out


def rotation_p(pool, E, q, workers):
    """e3 with the r63 seed; rotations in pool rounds with the exact early stop of ROT_FAIL_AT."""
    q = dsl.validate(q)
    per, _, _ = ev.run_program(q, E.panel)
    obs = ev.sharpe(ev.basket(per)[1])
    rng = np.random.default_rng(E6.SEED)
    lo = ev.ROT_MIN_DAYS / (365 * 4.5)
    fracs = [float(rng.uniform(lo, 1 - lo)) for _ in range(ev.N_ROT)]
    ge, done = 0, 0
    for b in range(0, ev.N_ROT, ROT_BATCH):
        chunk = fracs[b:b + ROT_BATCH]
        parts = [chunk[i::workers] for i in range(workers)]
        res = pool.map(_wrot, [(q, p) for p in parts if p])
        null = np.nan_to_num(np.array([x for r in res for x in r], float), nan=-np.inf)
        ge += int((null >= obs).sum())
        done += len(chunk)
        if ge >= ROT_FAIL_AT:
            break
    return float((1 + ge) / (1 + ev.N_ROT)), obs, done


def insert(arch, q, rec, origin, gen, pool, workers):
    """r62 Archive.add with a precomputed record (cell competition, e3 only for would-be winners)."""
    h = dsl.phash(q)
    days, r = rec.pop('series')
    arch.series[h] = (days, r)
    rec.update(origin=origin, gen=gen, e3=None, rot_p=None, rot_n=None, kept=False)
    cell = rec['cell']
    cur = arch.cells.get(cell)
    if (np.isfinite(rec['score']) and rec['e1'] and rec['e2'] and not ev.blocked(cell)
            and (cur is None or rec['score'] > cur['score'])):
        p, _, nrot = rotation_p(pool, arch.E, q, workers)
        rec['rot_p'], rec['rot_n'] = p, nrot
        rec['e3'] = bool(p < ev.ROT_P)
        if rec['e3']:
            arch.cells[cell] = rec
            rec['kept'] = True
    arch.seen[h] = {k: rec[k] for k in ('score', 'cell', 'e1', 'e2', 'e3', 'kept', 'origin', 'gen', 'program')}
    arch._log(rec, days, r)


def _save(run, st, arch):
    st.update(cells=arch.cells, seen=arch.seen, series=arch.series)
    tmp = os.path.join(_dir(run), 'state.tmp')
    with open(tmp, 'wb') as f:
        pickle.dump(st, f)
    os.replace(tmp, os.path.join(_dir(run), 'state.pkl'))


def _archive(E, run, st):
    arch = fx.Archive(E, log_path=os.path.join(_dir(run), 'log.jsonl'))
    arch.cells, arch.seen, arch.series = st['cells'], st['seen'], st['series']
    return arch


def run(name, kind, seed, kappa=0.0, workers=None):
    os.makedirs(_dir(name), exist_ok=True)
    sp = os.path.join(_dir(name), 'state.pkl')
    if os.path.exists(sp):
        with open(sp, 'rb') as f:
            st = pickle.load(f)
        assert (st['kind'], st['seed'], st['kappa']) == (kind, int(seed), float(kappa)), 'run exists with other args'
    else:
        st = {'kind': kind, 'seed': int(seed), 'kappa': float(kappa), 'cells': {}, 'seen': {}, 'series': {},
              'gens': {}}
    workers = workers or max(1, mp.cpu_count() - 2)
    t0 = time.time()
    E = E6.evaluator(build_src(kind, seed, kappa))
    arch = _archive(E, name, st)
    ctx = mp.get_context('spawn')
    with ctx.Pool(workers, initializer=_winit, initargs=(kind, int(seed), float(kappa))) as pool:
        print(json.dumps({'run': name, 'kind': kind, 'seed': seed, 'kappa': kappa, 'workers': workers,
                          'tramos': len(E.panel.src), 'setup_s': round(time.time() - t0, 1)}), flush=True)
        for g in ['seed'] + list(range(GENERATIONS)):
            if str(g) in st['gens']:
                continue
            tg = time.time()
            rng = np.random.default_rng([SEED, 10_000 if g == 'seed' else g, int(seed), 11])
            room = N_FAB_CEILING - arch.n() if kind == 'real' else 10 ** 9
            n = min(N_SEED if g == 'seed' else PER_GEN, room)
            if g == 'seed':
                kids, pend = [], set()
                rs = np.random.default_rng(SEED)
                while len(kids) < n:
                    q = dsl.random_program(rs)
                    h = dsl.phash(q)
                    if h not in pend:
                        pend.add(h)
                        kids.append((q, 'seed'))
            else:
                kids = draw_children(arch, rng, n, set())
            recs = pool.map(_weval, [q for q, _ in kids], chunksize=1)
            te = time.time() - tg
            for (q, origin), rec in zip(kids, recs):
                insert(arch, dsl.validate(q), rec, origin, -1 if g == 'seed' else g, pool, workers)
            st['gens'][str(g)] = {'n': len(kids), 'eval_s': round(te, 1), 'total_s': round(time.time() - tg, 1),
                                  'n_fab_run': arch.n(), 'cells': len(arch.cells)}
            _save(name, st, arch)
            if kind == 'real':
                save_series_batch(arch, st)
                write_counter(arch.n(), g, f'r63 run {name}')
                _save(name, st, arch)
            print(json.dumps({'gen': g, **st['gens'][str(g)],
                              'best': max((round(r['score'], 3) for r in arch.cells.values()), default=None)}),
                  flush=True)
            if kind == 'real' and arch.n() >= N_FAB_CEILING:
                break
    print(json.dumps({'run': name, 'done': True, 'n': arch.n(), 'hours': round((time.time() - t0) / 3600, 2)}),
          flush=True)


# ----------------------------------------------------------------------------------------------
# Real runs: series store and counter
# ----------------------------------------------------------------------------------------------
def save_series_batch(arch, st):
    """New series of a real run into the r59 store (round 'r63', ids R63_P_<hash10>, float32 + sha)."""
    import r59
    root = r59.SERIES
    path = os.path.join(root, 'r63.npz')
    cur = dict(np.load(path)) if os.path.exists(path) else {}
    mpath = os.path.join(root, 'manifest.json')
    with open(mpath) as f:
        man = json.load(f)
    new = 0
    for h, (d, r) in arch.series.items():
        tid = f'R63_P_{h[:10]}'
        if tid in man['series']:
            continue
        d = np.asarray(d, np.int64)
        r = np.asarray(r, np.float32)
        assert len(d) == 0 or ((np.diff(d) > 0).all() and d[-1] < 1_735_689_600_000)
        cur[f'{tid}__days'], cur[f'{tid}__ret'] = d, r
        man['series'][tid] = {'file': 'r63.npz', 'script': 'r63_run.py (factory)', 'window': 'r63 D63 2020-2024',
                              'n_days': int(len(d)), 'dtype': 'float32',
                              'sha256': hashlib.sha256(d.tobytes() + r.tobytes()).hexdigest()}
        new += 1
    if new:
        np.savez_compressed(path, **cur)
        with open(path, 'rb') as f:
            man['files']['r63.npz'] = hashlib.sha256(f.read()).hexdigest()
        with open(mpath, 'w') as f:
            json.dump(man, f, indent=1)
    st['series_saved'] = len([k for k in man['series'] if k.startswith('R63_P_')])


def write_counter(n_new, gen, note):
    """TRIAL_REGISTRY.json -> factory_trials: N_fab = r62's 1,614 + r63's real programs."""
    path = os.path.join(HERE, '..', 'strategies', 'FundingOiPilot4h', 'reports', 'TRIAL_REGISTRY.json')
    with open(path, encoding='utf-8') as f:
        reg = json.load(f)
    ft = reg['factory_trials']
    if 'n_fab_r62' not in ft:                      # first r63 write: freeze r62's count
        ft['n_fab_r62'] = int(ft['n_fab'])
    r62_n = ft['n_fab_r62']
    ft.setdefault('r63', {'protocol': 'strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261029-r63/'
                                      'PROTOCOL_R63.md', 'ceiling': N_FAB_CEILING, 'by_generation': {}})
    ft['r63']['n_fab'] = int(n_new)
    ft['r63']['by_generation'][str(gen)] = {'n_fab': int(n_new), 'note': note}
    ft['n_fab'] = int(r62_n) + int(n_new)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)


# ----------------------------------------------------------------------------------------------
# Finalists and SPA over every series of the run
# ----------------------------------------------------------------------------------------------
def planted_piece(q):
    return 'P1' if q['universe'] == 'alts_1h' and any(
        s['kind'] == 'shock' and s['params']['mode'] == 'fade' for s in q['signal']) else None


def final(name):
    import r62_run
    with open(os.path.join(_dir(name), 'state.pkl'), 'rb') as f:
        st = pickle.load(f)
    p55 = ev.load_bench('BENCH_P55_long')
    E = type('E', (), {'p55': p55})()
    arch = fx.Archive(E, rot_fn=lambda q: None)
    arch.cells, arch.seen, arch.series = st['cells'], st['seen'], st['series']
    fins = arch.finalists()
    hs, A, B = r62_run.spa_matrices(arch, p55)
    out = {'run': name, 'kind': st['kind'], 'seed': st['seed'], 'kappa': st['kappa'], 'n_programs': len(hs),
           'n_cells': len(arch.cells), 'gens': st['gens'], 'finalists': []}
    tt = {}
    for nm, G in (('cash', A), ('marginal', B)):
        p, imax, Tb, t = ev.spa_fast(G, seed=SEED)
        out[f'spa_{nm}'] = {'p': p, 'argmax': hs[imax], 'crit_t': float(np.quantile(Tb, 1 - SPA_ALPHA))}
        tt[nm] = {h: float(t[i]) for i, h in enumerate(hs)}
    for r in fins:
        h = r['hash']
        row = {k: r.get(k) for k in ('hash', 'cell', 'score', 'sharpe', 'sharpe_cost2', 'marginal', 'rot_p',
                                     'rot_n', 'origin', 'gen', 'trades', 'top5_share', 'program')}
        for nm in ('cash', 'marginal'):
            s = out[f'spa_{nm}']
            row[f'spa_{nm}_p'], row[f't_{nm}'] = s['p'], tt[nm][h]
            row[f'spa_{nm}_pass'] = bool(s['p'] < SPA_ALPHA and (s['argmax'] == h or tt[nm][h] > s['crit_t']))
        row['spa_pass'] = row['spa_cash_pass'] and row['spa_marginal_pass']
        row['planted_piece'] = planted_piece(r['program'])
        out['finalists'].append(row)
    best = sorted((r for r in st['seen'].values() if r['score'] is not None and np.isfinite(r['score'])),
                  key=lambda r: -r['score'])[:1]
    sh = [ev.sharpe(r) for _, r in arch.series.values()]
    out['max_dev_sharpe'] = float(np.nanmax(sh)) if sh else None
    out['best_score'] = best[0]['score'] if best else None
    with open(os.path.join(_dir(name), 'final.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1, default=fx._json_default)
    print(json.dumps({k: v for k, v in out.items() if k != 'gens'}, indent=1, default=fx._json_default))
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd')
    ap.add_argument('run')
    ap.add_argument('kind', nargs='?')
    ap.add_argument('seed', nargs='?', type=int)
    ap.add_argument('--kappa', type=float, default=0.0)
    ap.add_argument('--workers', type=int, default=None)
    a = ap.parse_args()
    if a.cmd == 'run':
        run(a.run, a.kind, a.seed, a.kappa, a.workers)
    elif a.cmd == 'final':
        final(a.run)
    else:
        print(__doc__)
        sys.exit(1)
