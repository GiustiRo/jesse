"""r50 F3: frozen engines and class rules on the five validation assets.

Fixed in `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE3_PROTOCOL.md`
(committed before any validation asset was loaded). Engines, class rules and the F2
construction are imported unchanged from the modules frozen at commit 8e6b82e0.

    python research_scripts/r50_f3.py run

writes research_scripts/data/r50/f3_validation.json.
"""
import csv
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)
from jesse.services.candle_service import generate_completed_candles_from_observed_minutes

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r50_f2 as f2
from r50_harness import T, O, C, H, L, V, DAY_MS, DonchianEnsR49
from r50_engines import COMMON, MEASURE_FROM, TAKER, BALANCE, SLIP_BPS, simulate, calendar, metrics, daily_returns

HERE = os.path.dirname(os.path.abspath(__file__))
# Validation assets (protocol section 2). `r1` is the R1 4h configuration of the analogous core
# asset; ETFs only have daily bars, so R1 runs on daily candles there (declared adaptation).
VAL = {
    'XAG': dict(cls='metals', src=('Custom Data', 'XAG-USDT'), r1=fb.R1_CFG['XAU']),
    'COPPER': dict(cls='metals', src=('Custom Data', 'COPPER-USDT'), r1=fb.R1_CFG['XAU']),
    'NDX': dict(cls='equities', src=('Custom Data', 'NDX-USDT'), r1=fb.R1_CFG['SPX']),
    'EWJ': dict(cls='equities', src=('csv', 'EWJ_daily_2000-01-01_2025-12-31.csv'), r1=None),
    'EWY': dict(cls='equities', src=('csv', 'EWY_daily_2000-01-01_2025-12-31.csv'), r1=None),
}
CLASS_RULE = {'equities': ['R1', 'M2a'], 'metals': ['R1']}
COLLAPSE_DD, COLLAPSE_SHARPE = -0.30, -0.5


def _etf_daily(fname):
    rows = []
    with open(os.path.join(HERE, 'data', 'r50', 'etf', fname)) as fh:
        for r in csv.DictReader(fh):
            if r['date'] > '2025-12-31':
                continue
            t = int(datetime.fromisoformat(r['date']).replace(tzinfo=timezone.utc).timestamp() * 1000)
            rows.append([t, float(r['open']), float(r['close']), float(r['high']), float(r['low']), float(r['volume'] or 0)])
    return np.array(rows)


def load(name, window):
    spec = VAL[name]
    f_ms = hz._ms(COMMON[1])
    if spec['src'][0] == 'csv':
        daily, h4 = _etf_daily(spec['src'][1]), None
    else:
        m = hz._minutes(spec['src'][0], spec['src'][1], hz._ms('2008-01-01'), f_ms)
        daily = en.daily_from_minutes(m, True, f_ms)
        h4 = generate_completed_candles_from_observed_minutes('4h', m, f_ms)
    if len(daily) < 300:
        return None
    if window == 'common':
        start_ms, mfrom = hz._ms(COMMON[0]), MEASURE_FROM
    else:
        start_ms = int(daily[260, T])
        mfrom = datetime.fromtimestamp(start_ms / 1000, tz=timezone.utc).date().isoformat()
    return {'daily': daily, 'h4': h4, 'start_ms': start_ms, 'mfrom': mfrom,
            'first': hz._date(int(daily[0, T])), 'last': hz._date(int(daily[-1, T]))}


def r1_daily_run(name, d):
    """R1 on daily candles for daily-only ETFs: same ensemble, 1 candle per day, 252."""
    b = d['daily']
    k = int(np.searchsorted(b[:, T], d['start_ms'], side='left'))
    acct = fb.SlipAccount(BALANCE, TAKER, 3, SLIP_BPS.get(name, 0.0))
    ts, eq = hz.run(DonchianEnsR49(candles_per_day=1, ann_days=252), b[max(0, k - 260):k], b[k:], DAY_MS, acct, None)
    return ts, eq, acct


def r1_4h_run(name, d, cfg):
    h4 = d['h4']
    k = int(np.searchsorted(h4[:, T], d['start_ms'], side='left'))
    acct = fb.SlipAccount(BALANCE, TAKER, 3, SLIP_BPS.get(name, 0.0))
    ts, eq = hz.run(DonchianEnsR49(**cfg), h4[max(0, k - 1520):k], h4[k:], fb.H4_MS, acct, None)
    return ts, eq, acct


def run():
    out = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE3_PROTOCOL.md', 'frozen_at': '8e6b82e0',
           'assets': {}, 'A': {}, 'B': {}, 'C': {}}
    curves = {}
    for window in ('common', 'long'):
        for name, spec in VAL.items():
            d = load(name, window)
            if d is None:
                out['assets'].setdefault(name, {})[window] = {'error': 'insufficient data'}
                continue
            runs = {'M2a': lambda: simulate(d['daily'], d['start_ms'], en.m2_decider(d['daily'], True, 'a'), name, False),
                    'N1': lambda: simulate(d['daily'], d['start_ms'], fb.n1_decider(d['daily'], True), name, False)}
            if d['h4'] is not None:
                runs['R1'] = lambda: r1_4h_run(name, d, spec['r1'])
                runs['R2'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], False), name, False, fb.H4_MS)
                runs['R3'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], True), name, False, fb.H4_MS)
            else:
                runs['R1'] = lambda: r1_daily_run(name, d)
            rec = {'class': spec['cls'], 'first': d['first'], 'last': d['last'],
                   'r1_bars': '4h' if d['h4'] is not None else '1D (adaptación declarada)'}
            last = d['daily'][-1, C]
            for eng, fn in runs.items():
                ts, eq, acct = fn()
                days, vals = calendar(ts, eq, d['mfrom'], COMMON[1])
                tr = acct.trades + ([{'opened': 0, 'closed': int(ts[-1]), 'pnl': acct.upnl(last), 'side': 1.0}]
                                    if acct.is_open else [])
                mt = metrics(days, vals, tr, d['mfrom']) or {'error': 'too short'}
                rec[eng] = mt
                curves[(eng, window, name)] = (days, vals)
                # Calendar curve from the window start, for the portfolio diagnostic (C).
                curves[(eng, window, name, 'full')] = calendar(ts, eq, hz._date(d['start_ms'])[:10], COMMON[1])
            parts = CLASS_RULE[spec['cls']]
            curves[('CLASS', window, name)] = fc.mean_curve([curves[(p, window, name)] for p in parts])
            curves[('CLASS', window, name, 'full')] = fc.mean_curve([curves[(p, window, name, 'full')] for p in parts])
            cm = metrics(*curves[('CLASS', window, name)], [], d['mfrom'])
            rec['CLASS_RULE'] = cm
            out['assets'].setdefault(name, {})[window] = rec
            hz.jh.debug(f'{name} {window}: ' + json.dumps({k: round(v['sharpe'], 2) for k, v in rec.items()
                                                           if isinstance(v, dict) and 'sharpe' in v}))
    # A: engine x asset, common window.
    combos = [(n, e, m) for n, r in out['assets'].items() for e, m in r.get('common', {}).items()
              if e in ('R1', 'R2', 'R3', 'M2a', 'N1') and isinstance(m, dict) and 'sharpe' in m]
    pos = [c for c in combos if c[2]['sharpe'] > 0]
    collapses = [f'{n}/{e}' for n, e, m in combos if m['max_dd'] < COLLAPSE_DD or m['sharpe'] < COLLAPSE_SHARPE]
    out['A'] = {'combos': len(combos), 'sharpe_pos': len(pos), 'share_pos': len(pos) / len(combos) if combos else 0,
                'collapses': collapses, 'pass': bool(combos and len(pos) / len(combos) > 0.5 and not collapses),
                'table': {f'{n}/{e}': {'common': round(m['sharpe'], 3),
                                       'long': round(out['assets'][n].get('long', {}).get(e, {}).get('sharpe', float('nan')), 3)}
                          for n, e, m in combos}}
    # B: class rule on each validation asset.
    cls = {n: out['assets'][n]['common']['CLASS_RULE']['sharpe'] for n in VAL if 'common' in out['assets'].get(n, {})}
    bk = fb.basket(curves, [('CLASS', 'common', n) for n in cls])
    bkl = fb.basket(curves, [('CLASS', 'long', n) for n in VAL if ('CLASS', 'long', n) in curves])
    out['B'] = {'per_asset_sharpe': cls, 'pass': bool(len(cls) == len(VAL) and all(v > 0 for v in cls.values())),
                'basket_common': metrics(bk[0], bk[1], [], hz._date(int(bk[0][0]))[:10]),
                'basket_long': metrics(bkl[0], bkl[1], [], hz._date(int(bkl[0][0]))[:10]) if bkl else None}
    # C: F2 portfolio with C0 extended by the five validation class sleeves (diagnostic only).
    for window in ('common', 'long'):
        comp, _ = f2.components(window)
        c0 = daily_returns(*comp['C0'])
        vs = [daily_returns(*curves[('CLASS', window, n, 'full')]) for n in VAL if ('CLASS', window, n, 'full') in curves]
        days = sorted(c0)
        r = []
        for t in days:
            extra = [s[t] for s in vs if t in s]
            r.append((7 * c0[t] + sum(extra)) / (7 + len(extra)))
        ext = (np.array([days[0] - DAY_MS] + days), BALANCE * np.r_[1.0, np.cumprod(1 + np.array(r))])
        port = {'C0x': ext, 'C6': comp['C6']}
        pdays, pvals, info = f2.portfolio(port, ['C0x', 'C6'])
        res = f2.r9(pdays, pvals, [])
        res.update(info)
        base_days, base_vals, _ = f2.portfolio(comp, ['C0', 'C6'])
        res['f2_reference'] = f2.r9(base_days, base_vals, [])
        out['C'][window] = res
    out['pass'] = bool(out['A']['pass'] and out['B']['pass'])
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f3_validation.json'), 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({'A': {k: out['A'][k] for k in ('combos', 'sharpe_pos', 'collapses', 'pass')},
                            'B': {k: out['B'][k] for k in ('per_asset_sharpe', 'pass')}, 'pass': out['pass']},
                           default=float, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
