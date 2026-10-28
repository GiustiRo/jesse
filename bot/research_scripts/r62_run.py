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


def _dir(run):
    return os.path.join(RUNS, run)


def _load(run):
    with open(os.path.join(_dir(run), 'state.pkl'), 'rb') as f:
        st = pickle.load(f)
    E = evaluator(st['kind'], st['seed'])
    arch = fx.Archive(E, log_path=os.path.join(_dir(run), 'log.jsonl'),
                      series_round='r62' if st['kind'] == 'real' else None)
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
    if int(tool_uses) > 0:
        rec['discarded'] = 'subagent used tools (§5)'
    else:
        progs = fx.ingest(text, al)
        rec['parsed'] = len(progs)
        for q in progs:
            if arch.add(q, 'llm', int(gen)) is not None:
                rec['new'] += 1
    st['gens'].setdefault(str(gen), {})['llm'] = rec
    _save(run, st, arch)
    print(json.dumps(rec))


def ga(run, gen):
    st, arch = _load(run)
    rng = np.random.default_rng([SEED, int(gen), st['seed'], 11])
    made = fx.ga_step(arch, rng, fx.GA_PER_GEN, int(gen))
    st['gens'].setdefault(str(gen), {})['ga'] = made
    _save(run, st, arch)
    if st['kind'] == 'real':
        fx.write_counter(arch.n(), gen, f'run {run}')
    _status(run, st, arch)


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
