"""r50 close: P1 (frozen at 5caf4a53) revalidated on the already-used validation assets, sleeve
behaviour, and every candidate portfolio against the original r9 goals.

User decision (2026-10-25): close r50 with option c — revalidate on the validation assets already
seen in F3 (silver, Nasdaq, copper, EWJ, EWY). This is NOT an independent test (those assets were
looked at once); it shows how the frozen candidate behaves on them. New-asset validation is
deferred to a later round.

    python research_scripts/r50_close.py run

writes research_scripts/data/r50/close.json.
"""
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r50_f2 as f2
import r50_f3 as f3
import r50_f1f as ff
from r50_harness import C, DAY_MS
from r50_engines import COMMON, ASSETS, simulate, calendar, daily_returns

VALIDATION = list(f3.VAL)
OUT = os.path.join(hz.OUT_DIR, 'close.json')


def _date(t):
    return datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat()


def yearly(cv):
    days, vals = cv
    y = {}
    for d, v in zip(days, vals):
        y[_date(int(d))[:4]] = v
    yv = [vals[0]] + list(y.values())
    return dict(zip(y, (np.array(yv[1:]) / np.array(yv[:-1]) - 1).round(4).tolist()))


def sleeves(window):
    """R1 per asset (core 7 + 5 validation) and C6 per coin, calendar curves from the window start."""
    r1, r1_tr, info = ff.r1_sleeves(window)
    r1 = {k: v for k, v in r1.items() if k in fb.CORE or k in VALIDATION}
    r1_tr = {k: v for k, v in r1_tr.items() if k in r1}
    c6, c6_tr = {}, {}
    for name in fc.CRYPTO:
        d = fb.load_both(name, window)
        cur = []
        tr = []
        for retest in (False, True):
            ts, eq, acct = simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], retest), name, d['funding'], fb.H4_MS)
            cur.append(calendar(ts, eq, _date(d['start_ms']), COMMON[1]))
            tr += [t['pnl'] for t in acct.trades]
        c6[name] = fc.mean_curve(cur)
        c6_tr[name] = tr
    return r1, r1_tr, info, c6, c6_tr


def r9_eval(comps, names, trades):
    days, vals, info = f2.portfolio(comps, names)
    out = f2.r9(days, vals, trades)
    out.update(info)
    return out


def run():
    f2.N_DECLARED = 98
    res = {'frozen_at': '5caf4a53', 'option': 'c: revalidación en activos de validación ya usados (no independiente)',
           'sleeves': {}, 'portfolios': {}, 'correlation_common': {}}
    for window in ('common', 'long'):
        r1, r1_tr, info, c6, c6_tr = sleeves(window)
        for n, cv in r1.items():
            m = en.metrics(cv[0], cv[1], [], info[n]['mfrom'])
            res['sleeves'].setdefault(f'R1/{n}', {})[window] = dict(
                {k: m[k] for k in ('sharpe', 'cagr', 'max_dd', 'quarters_pos')}, by_year=yearly(cv), from_=info[n]['mfrom'])
        for n, cv in c6.items():
            frm = '2021-01-01' if window == 'common' else _date(int(cv[0][0]))
            m = en.metrics(cv[0], cv[1], [], frm)
            res['sleeves'].setdefault(f'C6/{n}', {})[window] = dict(
                {k: m[k] for k in ('sharpe', 'cagr', 'max_dd', 'quarters_pos')}, by_year=yearly(cv), from_=frm)
        core = {k: v for k, v in r1.items() if k in fb.CORE}
        r1_core = fb.basket(core, list(core))
        r1_all = fb.basket(r1, list(r1))
        c6b = fb.basket(c6, list(c6))
        tr_core = sum((r1_tr[k] for k in core), [])
        tr_all = sum(r1_tr.values(), [])
        tr_c6 = sum(c6_tr.values(), [])
        res['portfolios'].setdefault('P1', {})[window] = r9_eval({'R1': r1_core, 'C6': c6b}, ['R1', 'C6'], tr_core + tr_c6)
        res['portfolios'].setdefault('P1_val', {})[window] = r9_eval({'R1': r1_all, 'C6': c6b}, ['R1', 'C6'], tr_all + tr_c6)
        res['portfolios'].setdefault('R1_core_only', {})[window] = r9_eval({'R1': r1_core}, ['R1'], tr_core)
        res['portfolios'].setdefault('C6_only', {})[window] = r9_eval({'C6': c6b}, ['C6'], tr_c6)
        if window == 'common':
            series = {f'R1/{k}': daily_returns(*v) for k, v in r1.items()}
            series.update({f'C6/{k}': daily_returns(*v) for k, v in c6.items()})
            names = sorted(series)
            ds = sorted(set.intersection(*[{t for t in s if t >= hz._ms('2021-01-01')} for s in series.values()]))
            mat = np.array([[series[n][t] for n in names] for t in ds])
            cm = np.corrcoef(mat, rowvar=False)
            res['correlation_common'] = {'names': names, 'matrix': cm.round(3).tolist(),
                                         'mean_offdiag': float((cm.sum() - len(names)) / (len(names) * (len(names) - 1)))}
        hz.jh.debug(f'{window}: done')
    with open(OUT, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({k: {w: {x: v[w][x] for x in ('cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'dsr')}
                                for w in v} for k, v in res['portfolios'].items()}, default=float, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
