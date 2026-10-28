"""r62: MAP-Elites factory (PROTOCOL_R62 §4-§5): archive, local genetic search, anonymised package
for the Claude Code proposer, leak check, log and counter.

The LLM proposer runs as a Claude Code subagent outside this module: `package(...)` writes the
anonymised brief, the session hands it to the subagent, and `ingest(...)` parses its JSON answer
back through the DSL parser (anything illegal is dropped). Universe and asset names are aliased
per generation, so the proposer never sees tickers, dates or price levels.
"""
import copy
import json
import math
import os
import re

import numpy as np

import r62_dsl as dsl
import r62_eval as ev

HERE = os.path.dirname(os.path.abspath(__file__))
GENERATIONS = 10
N_SEED = 20
GA_PER_GEN = 150
OPS = (('mutate', 0.60), ('swap', 0.25), ('cross', 0.15))
N_FAB_CEILING = 3000
MAX_FINALISTS = 5
LLM_MIN, LLM_MAX = 8, 12


# ----------------------------------------------------------------------------------------------
# Archive
# ----------------------------------------------------------------------------------------------
class Archive:
    """Best eligible program per cell; every evaluation is logged whether or not it is kept."""

    def __init__(self, evaluator, log_path=None, series_round=None, rot_fn=None):
        self.E = evaluator
        self.cells = {}                  # cell -> record
        self.seen = {}                   # hash -> compact record
        self.log_path = log_path
        self.series_round = series_round
        self.rot_fn = rot_fn or evaluator.rotation_p
        self.series = {}                 # hash -> (days, rets): the SPA matrix of the run

    def n(self):
        return len(self.seen)

    def add(self, q, origin, gen):
        try:
            q = dsl.validate(q)
        except dsl.DslError:
            return None
        h = dsl.phash(q)
        if h in self.seen or self.n() >= N_FAB_CEILING:
            return None
        rec = self.E.evaluate(q)
        days, r = rec.pop('series')
        self.series[h] = (days, r)
        rec.update(origin=origin, gen=gen, e3=None, rot_p=None, kept=False)
        cell = rec['cell']
        cur = self.cells.get(cell)
        wins = (np.isfinite(rec['score']) and rec['e1'] and rec['e2'] and not ev.blocked(cell)
                and (cur is None or rec['score'] > cur['score']))
        if wins:
            p, _ = self.rot_fn(q)
            rec['rot_p'] = p
            rec['e3'] = bool(p < ev.ROT_P)
            if rec['e3']:
                self.cells[cell] = rec
                rec['kept'] = True
        self.seen[h] = {k: rec[k] for k in ('score', 'cell', 'e1', 'e2', 'e3', 'kept', 'origin', 'gen', 'program')}
        self._log(rec, days, r)
        return rec

    def _log(self, rec, days, r):
        if self.log_path:
            line = {k: v for k, v in rec.items() if k != 'folds'}
            line['folds'] = {k: [None if not np.isfinite(v['sharpe']) else round(v['sharpe'], 4), v['trades']]
                             for k, v in rec['folds'].items()}
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(line, default=_json_default) + '\n')
        if self.series_round:
            import r59
            r59.save_series(self.series_round, f'R62_P_{rec["hash"][:10]}', days, r,
                            'r62_factory.py', 'r62 dev (2018-10-01/2020-01-01 -> 2024-12-31)')

    def elites(self):
        return sorted(self.cells.values(), key=lambda r: -r['score'])

    def finalists(self):
        """§5: best elite per non-blocked cell, at most one per (holding, direction), at most 5."""
        out, used = [], set()
        for r in self.elites():
            key = r['cell'].split('|', 1)[1]
            if key in used:
                continue
            used.add(key)
            out.append(r)
            if len(out) == MAX_FINALISTS:
                break
        return out


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.bool_):
        return bool(o)
    raise TypeError(type(o))


# ----------------------------------------------------------------------------------------------
# Local genetic search
# ----------------------------------------------------------------------------------------------
def mutate(q, rng):
    """Move one parameter to a neighbouring grid value."""
    q = copy.deepcopy(q)
    slots = [(x, tbl) for x, tbl in ([(s, dsl.SIGNALS) for s in q['signal']] +
                                     [(f, dsl.FILTERS) for f in q['filters']] +
                                     [(q['exit'], dsl.EXITS), (q['exec'], dsl.EXECS), (q['size'], dsl.SIZES)])
             if x['params']]
    if not slots:
        return swap(q, rng)
    x, tbl = slots[int(rng.integers(len(slots)))]
    k = sorted(x['params'])[int(rng.integers(len(x['params'])))]
    grid = tbl[x['kind']][k]
    i = grid.index(x['params'][k])
    j = min(max(i + (1 if rng.random() < 0.5 else -1), 0), len(grid) - 1)
    if j == i:
        j = (i + 1) % len(grid)
    x['params'][k] = grid[j]
    return q


def swap(q, rng):
    """Replace one piece (signal, filter, exit or exec) by a random one from the catalogue."""
    q = copy.deepcopy(q)
    donor = dsl.random_program(rng, q['universe'])
    what = rng.choice(['signal', 'filter', 'exit', 'exec'])
    if what == 'signal':
        q['signal'][int(rng.integers(len(q['signal'])))] = donor['signal'][0]
    elif what == 'filter':
        if q['filters'] and rng.random() < 0.3:
            q['filters'].pop(int(rng.integers(len(q['filters']))))
        elif donor['filters']:
            if len(q['filters']) < 2:
                q['filters'].append(donor['filters'][0])
            else:
                q['filters'][int(rng.integers(2))] = donor['filters'][0]
    else:
        q[what] = donor[what]
    return q


def cross(a, b, rng):
    """Child with the universe/signal of `a` and filters/exit/exec drawn from either parent."""
    c = copy.deepcopy(a)
    for k in ('filters', 'exit', 'exec'):
        if rng.random() < 0.5:
            c[k] = copy.deepcopy(b[k])
    return c


def ga_step(arch, rng, n, gen):
    """~n new evaluations from the elites (random legal programs when the archive is empty)."""
    elites = arch.elites()
    pool = elites or [r for r in _top_seen(arch)]
    made, tries = 0, 0
    while made < n and tries < 10 * n and arch.n() < N_FAB_CEILING:
        tries += 1
        if not pool:
            child = dsl.random_program(rng)
        else:
            u = rng.random()
            parent = pool[int(rng.integers(len(pool)))]['program']
            if u < OPS[0][1]:
                child = mutate(parent, rng)
            elif u < OPS[0][1] + OPS[1][1]:
                child = swap(parent, rng)
            else:
                same = [r for r in pool if r['cell'][:4] == pool[0]['cell'][:4]] or pool
                other = same[int(rng.integers(len(same)))]['program']
                child = cross(parent, other, rng) if other['universe'] == parent['universe'] else mutate(parent, rng)
        if arch.add(child, 'ga', gen) is not None:
            made += 1
    # E4: a small elite pool can exhaust its grid neighbourhood; fill the budget with random programs
    while made < n and arch.n() < N_FAB_CEILING:
        if arch.add(dsl.random_program(rng), 'ga_random', gen) is not None:
            made += 1
    return made


def _top_seen(arch, k=10):
    """When no cell has an elite yet, breed from the best finite scores seen so far."""
    fin = [r for r in arch.seen.values() if r['score'] is not None and np.isfinite(r['score'])]
    return sorted(fin, key=lambda r: -r['score'])[:k]


# ----------------------------------------------------------------------------------------------
# Anonymised package for the proposer
# ----------------------------------------------------------------------------------------------
LEAK_WORDS = ['BTC', 'ETH', 'XAU', 'GOLD', 'SPX', 'S&P', 'WTI', 'OIL', 'BRENT', 'GAS', 'BOND', 'TREASUR',
              'NASDAQ', 'NDX', 'LUNA', 'FTX', 'COVID', 'BITCOIN', 'ETHER', 'USDT', 'BINANCE', 'CME',
              'COPPER', 'SILVER', 'XAG', 'DEU', 'DAX', 'EWJ', 'EWY', 'FUNDING', 'FOMC']
DATE_RE = re.compile(r'\b(19|20)\d{2}\b|\d{4}-\d{2}-\d{2}')


def leak_check(text):
    """Raise if the package names an asset/market event, carries a year or ISO date, or a number
    > 1000 (price levels). Returns the text unchanged otherwise."""
    up = text.upper()
    for w in LEAK_WORDS:
        if re.search(r'(?<![A-Z])' + re.escape(w) + r'(?![A-Z])', up):
            raise ValueError(f'leak: {w}')
    if DATE_RE.search(text):
        raise ValueError('leak: year/date')
    for m in re.finditer(r'(?<![\w.])\d+(?:\.\d+)?', text):
        if float(m.group()) > 1000:
            raise ValueError(f'leak: number {m.group()}')
    return text


class Aliases:
    """Per-generation random letters for assets and U-codes for universes (and the fold groups)."""

    def __init__(self, rng):
        assets = ['BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']
        letters = list('ABCDEFG')
        rng.shuffle(letters)
        self.asset = dict(zip(assets, letters))
        us = sorted(dsl.UNIVERSES)
        codes = [f'U{i + 1}' for i in range(len(us))]
        rng.shuffle(codes)
        self.univ = dict(zip(us, codes))
        self.inv_univ = {v: k for k, v in self.univ.items()}
        grp = ['crypto', 'commod', 'eqbond']
        gl = ['G1', 'G2', 'G3']
        rng.shuffle(gl)
        self.group = dict(zip(grp, gl))
        self.fold_perm = None
        # Event names that would reveal the market (funding hours, the CME weekend gap) are aliased.
        self.event = {'funding_hour': 'E1', 'cme_gap': 'E2', 'month_end': 'E3'}
        self.inv_event = {v: k for k, v in self.event.items()}

    def program_out(self, q):
        q = copy.deepcopy(q)
        q['universe'] = self.univ[q['universe']]
        for f in q['filters']:
            if f['kind'] == 'btcstate':        # the name would reveal the lead market
                f['kind'] = 'leadstate'
        for s in q['signal']:
            if s['kind'] == 'clock':
                s['params']['event'] = self.event[s['params']['event']]
        return q

    def program_in(self, q):
        q = copy.deepcopy(q)
        q['universe'] = self.inv_univ.get(q.get('universe'), q.get('universe'))
        for f in q.get('filters', []) or []:
            if isinstance(f, dict) and f.get('kind') == 'leadstate':
                f['kind'] = 'btcstate'
        for s in q.get('signal', []):
            if isinstance(s, dict) and s.get('kind') == 'clock':
                s.setdefault('params', {})
                s['params']['event'] = self.inv_event.get(s['params'].get('event'), s['params'].get('event'))
        return q


def asset_stats(panel, al):
    """Standardised-return statistics per aliased asset: ACF lags 1-24, skew, kurtosis, hour-of-day
    mean profile in sigma units (24 values), and the cross-correlation matrix of daily returns."""
    out = {}
    daily = {}
    for name, letter in al.asset.items():
        a = panel.asset(name, '1h')
        z = a.lr / a.sig
        z = z[np.isfinite(z)]
        z = (z - z.mean()) / z.std()
        acf = [float(np.corrcoef(z[:-k], z[k:])[0, 1]) for k in range(1, 25)]
        prof = []
        zz = a.lr / a.sig
        for h in range(24):
            m = (a.hour == h) & np.isfinite(zz)
            prof.append(float(zz[m].mean()) if m.sum() > 100 else None)
        out[letter] = {'acf_1_24': [round(x, 3) for x in acf], 'skew': round(float((z ** 3).mean()), 2),
                       'kurt': round(float((z ** 4).mean()), 1),
                       'hour_profile_mean_z': [None if p is None else round(p, 3) for p in prof]}
        d, r = ev.basket({name: dsl.daily(a, np.nan_to_num(a.lr))})
        daily[letter] = (d, r)
    letters = sorted(daily)
    days = np.unique(np.concatenate([daily[k][0] for k in letters]))
    m = np.zeros((len(days), len(letters)))
    for i, k in enumerate(letters):
        m[np.searchsorted(days, daily[k][0]), i] = daily[k][1]
    cc = np.corrcoef(m.T)
    return out, {'assets': letters, 'corr_daily': [[round(float(x), 2) for x in row] for row in cc]}


def package(arch, panel, gen, rng, recent_fail=12):
    """The proposer's brief (JSON text), leak-checked. Universe membership is given by letters."""
    al = Aliases(rng)
    univ = {}
    for u, (tf, names) in dsl.UNIVERSES.items():
        mem = ['/'.join(al.asset[x] for x in n) if isinstance(n, tuple) else al.asset[n] for n in names]
        univ[al.univ[u]] = {'tf': tf, 'members': sorted(mem)}   # listing order would reveal identity
    # group:year -> Gx:Fn, with the years shuffled per generation
    perm = list(rng.permutation(6))
    year_alias = {str(y): f'F{p + 1}' for y, p in zip(range(2019, 2025), perm)}

    def folds_out(fl):
        out = {}
        for k, v in fl.items():
            g, y = k.split(':')
            sh = v['sharpe']
            out[f'{al.group[g]}:{year_alias[y]}'] = [None if sh is None or not np.isfinite(sh) else round(sh, 2),
                                                     _hund(v["trades"])]
        return out

    def compact(r):
        return {'program': al.program_out(r['program']), 'score': round(r['score'], 3),
                'cell': r['cell'], 'sharpe': round(r['sharpe'], 2), 'sharpe_cost2': round(r['sharpe_cost2'], 2),
                'marginal_vs_book': round(r['marginal'], 3), 'trades_hundreds': _hund(r['trades']),
                'maker_unfilled_hundreds': _hund(r['unfilled']), 'folds': folds_out(r['folds'])}

    logs = _recent_failures(arch, recent_fail)
    stats, corr = asset_stats(panel, al)
    pkg = {
        'task': ('Propose 8 to 12 NEW programs in the DSL below, as a JSON list only. Goal: a return '
                 'engine that is NOT long trend-following, adds to an existing book (marginal_vs_book '
                 '> 0), survives costs x2, and has a good WORST fold. Score = worst fold Sharpe - '
                 f'{ev.LAMBDA} x complexity. Cells with rho_to_book > 0.3 and long bias are blocked.'),
        'dsl': _dsl_spec(al),
        'universes': univ,
        'elites': [compact(r) for r in arch.elites()],
        'recent_failures': logs,
        'assets_standardised_stats': stats,
        'cross_correlation': corr,
        'generation': gen,
    }
    text = json.dumps(pkg, default=_json_default)
    leak_check(text)
    return text, al


def _hund(n):
    """Counts in hundreds: the leak check rejects any number > 1000 (price levels), so counts are
    scaled rather than exempted."""
    return round(n / 100, 1)


def _recent_failures(arch, n):
    """The last n evaluated programs that failed, with the gate that failed (from the log file)."""
    if not arch.log_path or not os.path.exists(arch.log_path):
        return []
    with open(arch.log_path, encoding='utf-8') as f:
        lines = f.readlines()[-400:]
    out = []
    for ln in reversed(lines):
        r = json.loads(ln)
        if r.get('kept'):
            continue
        why = ('score=-inf (too few valid folds)' if r['score'] is None or r['score'] == -math.inf else
               'e1 costs' if not r['e1'] else 'e2 marginal' if not r['e2'] else
               'e3 rotation' if r.get('e3') is False else 'lower score than cell elite')
        out.append({'why': why, 'score': r['score'], 'cell': r['cell'], 'trades_hundreds': _hund(r['trades']),
                    'kind': [s['kind'] for s in r['program']['signal']], 'exit': r['program']['exit']['kind'],
                    'exec': r['program']['exec']['kind']})
        if len(out) == n:
            break
    return out


def _dsl_spec(al):
    sig = copy.deepcopy(dsl.SIGNALS)
    sig['clock']['event'] = [al.event[e] for e in sig['clock']['event']]
    return {
        'program': '{"universe": U?, "signal": [1-2 pieces], "filters": [0-2 pieces], "exit": piece, '
                   '"size": {"kind": "voltgt", "params": {"side": both|long|short}}, "exec": piece}; '
                   'piece = {"kind": ..., "params": {...}} with every listed param, values from the grid only',
        'signals': sig, 'filters': {('leadstate' if k == 'btcstate' else k): v for k, v in dsl.FILTERS.items()},
        'exits': dsl.EXITS, 'execs': dsl.EXECS,
        'rules': ['spread_z is the only (and mandatory) signal of pair universes; pairs execute taker',
                  'clock E1/E2 and cascade are only legal on the 2-asset 1h universe of derivative '
                  'contracts (the one with positioning data); clock/cascade/session need 1h bars',
                  'second signal = confirmation within 6 bars, same direction',
                  'maker: limit off x ATR away, life bars to fill, must be crossed by 1 bp; '
                  'maker fee 0.018%, taker 0.045% + slippage',
                  f'complexity = pieces + params; max {dsl.MAX_PIECES} pieces, {dsl.MAX_PARAMS} params'],
        'signal_notes': {'zrev': 'fade a k-bar z-score beyond z', 'rsi2': 'RSI(2) extreme, fade',
                         'shock': '1-bar return beyond z sigma', 'spread_z': 'fade the pair log-spread z',
                         'voljump': '24-bar vol / 30-day vol above ratio; direction from 24-bar move',
                         'clock': 'E1 three fixed daily hours, E2 a weekly reopening hour, E3 month-end; '
                                  'direction from the prior move',
                         'cascade': 'open-interest drop beyond z_oi sigma with |return| beyond z_ret'},
        'filter_notes': {'volreg': 'tercile of 30-day vol vs the prior year', 'trendveto': 'skip entries against '
                         'a k-day move beyond 1 sigma', 'session': 'UTC hour blocks', 'leadstate': 'trend state '
                         '(90-day) of the lead asset of the market'},
    }


def ingest(text, al):
    """Parse the proposer's answer: a JSON list (optionally inside a ```json fence) of programs in
    aliased form. Returns legal de-aliased programs; illegal ones are dropped silently."""
    m = re.search(r'\[.*\]', text, re.S)
    if not m:
        return []
    try:
        items = json.loads(m.group())
    except json.JSONDecodeError:
        return []
    out = []
    for it in items[:LLM_MAX]:
        try:
            out.append(dsl.validate(al.program_in(it)))
        except (dsl.DslError, AttributeError, TypeError, KeyError):
            continue
    return out


def write_counter(n_fab, gen, note):
    """TRIAL_REGISTRY.json -> factory_trials (N_fab), rewritten at the end of each generation."""
    path = os.path.join(HERE, '..', 'strategies', 'FundingOiPilot4h', 'reports', 'TRIAL_REGISTRY.json')
    with open(path, encoding='utf-8') as f:
        reg = json.load(f)
    ft = reg.setdefault('factory_trials', {
        'note': ('N_fab (r62+): unique DSL programs (canonical hash) evaluated on real development data '
                 'by the r62 factory. Separate counter; global N only adds finalists (PROTOCOL_R62 §0).'),
        'protocol': 'strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261028-r62/PROTOCOL_R62.md',
        'ceiling': N_FAB_CEILING, 'n_fab': 0, 'by_generation': {}})
    ft['n_fab'] = int(n_fab)
    ft['by_generation'][str(gen)] = {'n_fab': int(n_fab), 'note': note}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
