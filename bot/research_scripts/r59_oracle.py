"""r59: blind oracle over the reusable holdout H = N2 ∪ N3 (PROTOCOL_R59.md §1.2).

Research container (needs git; /src is the checkout):
    python research_scripts/r59_oracle.py init        # writes q0 (r58 F2, revealed) once into the log
    python research_scripts/r59_oracle.py selftest    # fake holdout of 12 U50 alts; never touches H or the real log
    python research_scripts/r59_oracle.py count_q1    # label counts on H for q1's power (no outcomes, no budget)
    python research_scripts/r59_oracle.py query <qid> # prints only PASA / NO PASA

A query refuses to run on a dirty tree (r59 code or protocol), on a qid already logged or past the
budget. Each margin gets Laplace(0, 0.1 * scale) noise seeded by sha256(HEAD + qid), so asking the
same query again cannot draw a different answer. Full statistics go sealed to
data/r59/oracle_sealed/<qid>.json (gitignored); the log keeps only the answer and the sealed hash.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

import numpy as np

import r59_holdout as hg

hg.install()

HERE = hg.HERE
REPO = os.path.dirname(os.path.dirname(HERE))
REPORTS = os.path.join(HERE, '..', 'strategies', 'FundingOiPilot4h', 'reports')
PROTOCOL = os.path.join(REPORTS, 'RESEARCH_HUB', 'revisions', '20261027-r59', 'PROTOCOL_R59.md')
LOG = os.path.join(REPORTS, 'RESEARCH_HUB', 'holdout', 'ORACLE_LOG.jsonl')
REGISTRY = os.path.join(REPORTS, 'TRIAL_REGISTRY.json')
SEALED = os.path.join(hg.OUT, 'oracle_sealed')
BUDGET = 5                         # q0 (r58 F2) + q1..q4
NOISE = 0.1                        # Laplace scale as a fraction of each margin's own scale
TRACKED = ('bot/research_scripts/r59_criteria.py', 'bot/research_scripts/r59_oracle.py',
           'bot/research_scripts/r59_holdout.py', 'bot/research_scripts/r59.py',
           'bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261027-r59/PROTOCOL_R59.md')


def _git(*args):
    # autocrlf: the checkout is a Windows working tree mounted in Linux; without it every file looks modified.
    return subprocess.run(['git', '-c', 'safe.directory=*', '-c', 'core.autocrlf=true', '-C', REPO, *args],
                          capture_output=True, text=True, check=True).stdout.strip()


def head():
    return _git('rev-parse', 'HEAD')


def dirty():
    return _git('status', '--porcelain', '--', *TRACKED)


def sha_file(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def read_log(path):
    if not os.path.exists(path):
        return []
    return [json.loads(x) for x in open(path, encoding='utf-8') if x.strip()]


def append_log(path, rec):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n')


def noisy(margins, commit, qid, noise=NOISE):
    seed = int(hashlib.sha256((commit + qid).encode()).hexdigest()[:16], 16)
    rng = np.random.default_rng(seed)
    return [(n, m, s, float(m + rng.laplace(0.0, noise * s)) if noise > 0 else float(m)) for n, m, s in margins]


def run_query(qid, criteria, ctx, log_path=LOG, sealed_dir=SEALED, commit=None, dirty_fn=dirty, noise=NOISE,
              protocol=PROTOCOL, sync=True):
    """Checks, computes inside the oracle context, seals, logs; returns 'PASA' or 'NO PASA'."""
    log = read_log(log_path)
    if dirty_fn():
        raise SystemExit('oracle: r59 code or protocol not committed; commit before querying')
    if any(r['qid'] == qid for r in log):
        raise SystemExit(f'oracle: {qid} already answered; the answer stands')
    if len(log) >= BUDGET:
        raise SystemExit(f'oracle: budget of {BUDGET} queries exhausted')
    if qid not in criteria:
        raise SystemExit(f'oracle: no committed criterion {qid}')
    commit = commit or head()
    crit = criteria[qid]
    with hg.oracle_context():
        out = crit['fn'](ctx)
    rows = noisy(out['margins'], commit, qid, noise)
    ok = all(nm > 0 for _, _, _, nm in rows)
    answer = 'PASA' if ok else 'NO PASA'
    os.makedirs(sealed_dir, exist_ok=True)
    sealed = os.path.join(sealed_dir, f'{qid}.json')
    json.dump({'qid': qid, 'commit': commit, 'answer': answer, 'stats': out.get('stats', {}),
               'margins': [{'name': n, 'margin': m, 'scale': s, 'noisy': nm} for n, m, s, nm in rows]},
              open(sealed, 'w'), indent=1, default=float)
    rec = {'qid': qid, 'date_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), 'commit': commit,
           'protocol_sha256': sha_file(protocol), 'criterion': crit['desc'], 'alpha': crit['alpha'],
           'answer': answer, 'sealed_sha256': sha_file(sealed), 'budget_used': len(log) + 1, 'budget': BUDGET,
           'revealed': False}
    append_log(log_path, rec)
    if sync:
        sync_registry()
    return answer


def sync_registry():
    """Mirror of the log in TRIAL_REGISTRY.json -> holdout_oracle (the log is the source of truth)."""
    d = json.load(open(REGISTRY, encoding='utf-8'))
    log = read_log(LOG)
    d['holdout_oracle'] = {'protocol': 'strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261027-r59/PROTOCOL_R59.md',
                           'log': 'strategies/FundingOiPilot4h/reports/RESEARCH_HUB/holdout/ORACLE_LOG.jsonl',
                           'holdout': 'N2 ∪ N3', 'budget': BUDGET, 'used': len(log),
                           'queries': [{k: r[k] for k in ('qid', 'date_utc', 'alpha', 'answer', 'revealed')} for r in log]}
    open(REGISTRY, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2))


def init():
    """q0 = r58 F2, logged backwards: alpha 0.10, no noise, everything revealed in f2_confirm.json."""
    if read_log(LOG):
        raise SystemExit('oracle: log already initialised')
    conf = os.path.join(hg.DATA, 'r58', 'f2_confirm.json')
    c = json.load(open(conf))
    assert c['pass'] is True
    append_log(LOG, {'qid': 'q0', 'date_utc': '2026-10-27 (r58 F2, registrada en r59 F0)', 'commit': '61df21a7',
                     'protocol_sha256': None, 'criterion': 'r58 F2: V1 ∧ V2 en N2 ∪ N3, 5 criterios (PROTOCOL_R58 §3)',
                     'alpha': 0.10, 'answer': 'PASA', 'sealed_sha256': sha_file(conf), 'budget_used': 1,
                     'budget': BUDGET, 'revealed': True})
    sync_registry()
    print('q0 logged')


# ----------------------------------------------------------------------------------------------
# Label counts on H (no outcomes, no budget): q1's expected trade count
# ----------------------------------------------------------------------------------------------
def count_q1():
    """Coin-days 2021-07-02..2024 where V1 exists and where V1 = 1 (compression), per bank, from the
    daily states only. No trade, price or return of H is read."""
    import r58
    with hg.oracle_context():
        d = np.load(os.path.join(hg.DATA, 'r58', 'f0_days.npz'))
        out = {}
        for b in ('u50', 'n2', 'n3'):
            days, pe = d[f'{b}__days'], d[f'{b}__persist']
            rows = (days >= r58.CONF_FROM) & (days < r58.CUT_MS)
            out[b] = {'v1_days': int(np.isfinite(pe[rows]).sum()), 'compression_days': int((pe[rows] == 0).sum())}
    print(json.dumps(out))
    return out


# ----------------------------------------------------------------------------------------------
# Selftest: fake holdout of 12 U50 alts (seed 59), temporary log, H never read
# ----------------------------------------------------------------------------------------------
def selftest():
    import pandas as pd
    import r58
    import r59_criteria as rc
    res = {}
    # Guard: every protected route must refuse outside the oracle and open inside it.
    probes = {'np.load f0_bars_n2': lambda: np.load(os.path.join(hg.DATA, 'r58', 'f0_bars_n2.npz')),
              'read_csv f2_trades_n2n3': lambda: pd.read_csv(os.path.join(hg.DATA, 'r58', 'f2_trades_n2n3.csv')),
              'open n2 1h': lambda: open(os.path.join(hg.DATA, 'r56', 'n2', 'CHZUSDT_1h.npy'), 'rb').close(),
              'np.load panel70': lambda: np.load(os.path.join(hg.DATA, 'r56', 'panel70.npz')),
              'r58.load_bank n3': lambda: r58.load_bank('n3'),
              'r58.h4_bars N2 coin': lambda: r58.h4_bars(r58.N2_DIR, 'CHZUSDT'),
              'r58.c6_bank n2': lambda: r58.c6_bank('n2')}
    g = {}
    for k, f in probes.items():
        try:
            f()
            g[k] = 'OPEN (FAIL)'
        except hg.HoldoutAccess:
            g[k] = 'refused'
    with hg.oracle_context():
        open(os.path.join(hg.DATA, 'r58', 'f0_bars_n2.npz'), 'rb').close()
        g['inside oracle open f0_bars_n2'] = 'opened'
    np.load(os.path.join(hg.DATA, 'r58', 'f0_bars_u50.npz')).close()
    g['U50 f0_bars outside oracle'] = 'opened'
    res['guard'] = g
    res['guard_ok'] = all(v != 'OPEN (FAIL)' for v in g.values())

    # Fake holdout and its criteria.
    df = pd.read_csv(os.path.join(hg.DATA, 'r58', 'f1_trades_u50.csv'))
    alts = sorted(df['sym'].unique())
    fake = sorted(np.random.default_rng(59).choice(alts, 12, replace=False).tolist())
    ctx = {'df': df[df['sym'].isin(fake)].reset_index(drop=True)}

    def crit_true(c):
        return {'margins': [('mean_R_plus_100', float(c['df']['R'].mean() + 100), 1.0)], 'stats': {}}

    def crit_false(c):
        return {'margins': [('minus_one', -1.0, 1.0)], 'stats': {}}

    def crit_rule(c):
        sub = c['df'][c['df']['V1'].notna() & c['df']['V2'].notna()].reset_index(drop=True)
        keep = ((sub['V1'] == 1) & (sub['V2'] == 1)).values
        d, bs = rc.d_boot(sub, keep, 1000, 59)
        return {'margins': [('D_p10', float(np.nanpercentile(bs, 10)), float(np.nanstd(bs)))], 'stats': {'D': d}}
    crits = {f'st_{k}': {'fn': f, 'alpha': 0.0, 'desc': k} for k, f in
             (('true', crit_true), ('false', crit_false), ('rule', crit_rule), ('extra1', crit_true), ('extra2', crit_true))}
    direct = {'st_true': True, 'st_false': False}
    with hg.oracle_context():
        direct['st_rule'] = crit_rule(ctx)['margins'][0][1] > 0
    tmp = tempfile.mkdtemp(prefix='r59_oracle_selftest_')
    lp, sd = os.path.join(tmp, 'log.jsonl'), os.path.join(tmp, 'sealed')
    clean = lambda: ''
    kw = dict(log_path=lp, sealed_dir=sd, commit='selftest', dirty_fn=clean, sync=False)
    # (i) zero noise equals the direct computation
    ans = {q: run_query(q, crits, ctx, noise=0.0, **kw) for q in ('st_true', 'st_false', 'st_rule')}
    res['i_zero_noise'] = {q: {'oracle': a, 'direct': 'PASA' if direct[q] else 'NO PASA'} for q, a in ans.items()}
    res['i_ok'] = all(v['oracle'] == v['direct'] for v in res['i_zero_noise'].values())
    # (ii) determinism of the noise for the same commit + qid, and different for another qid
    m = [('x', 0.01, 1.0)]
    res['ii_ok'] = noisy(m, 'abc', 'q9') == noisy(m, 'abc', 'q9') and noisy(m, 'abc', 'q9') != noisy(m, 'abc', 'q8')
    # (iii) refusals: repeated qid, dirty tree, budget
    before = open(lp, 'rb').read()
    refusals = {}
    for name, call in (('repeated', lambda: run_query('st_true', crits, ctx, **kw)),
                       ('dirty', lambda: run_query('st_extra1', crits, ctx, **{**kw, 'dirty_fn': lambda: ' M r59.py'}))):
        try:
            call()
            refusals[name] = 'ran (FAIL)'
        except SystemExit as e:
            refusals[name] = str(e)
    run_query('st_extra1', crits, ctx, **kw)
    run_query('st_extra2', crits, ctx, **kw)            # 5th entry: budget now full
    crits['st_over'] = crits['st_true']
    try:
        run_query('st_over', crits, ctx, **kw)
        refusals['budget'] = 'ran (FAIL)'
    except SystemExit as e:
        refusals['budget'] = str(e)
    res['iii_refusals'] = refusals
    res['iii_ok'] = all('FAIL' not in v for v in refusals.values())
    # (iv) append-only: earlier bytes unchanged, 5 lines
    after = open(lp, 'rb').read()
    res['iv_ok'] = after.startswith(before) and len(read_log(lp)) == BUDGET
    res['real_log_untouched'] = not os.path.exists(LOG) or all(r['qid'][:3] != 'st_' for r in read_log(LOG))
    res['fake_holdout'] = fake
    res['pass'] = bool(res['guard_ok'] and res['i_ok'] and res['ii_ok'] and res['iii_ok'] and res['iv_ok']
                       and res['real_log_untouched'])
    os.makedirs(hg.OUT, exist_ok=True)
    json.dump(res, open(os.path.join(hg.OUT, 'f0_oracle_selftest.json'), 'w'), indent=1, default=str)
    print(json.dumps(res, indent=1, default=str))
    return res


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'query' and len(sys.argv) == 3:
        import r59_criteria as rc
        print(run_query(sys.argv[2], rc.CRITERIA, {}))
    elif cmd in ('init', 'selftest', 'count_q1', 'sync_registry'):
        globals()[cmd]()
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
