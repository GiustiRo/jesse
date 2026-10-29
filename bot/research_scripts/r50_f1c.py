"""r50 F1c: class-assignment portfolio (C0) and six families (C1-C6) on the 7-asset core.

Rules, defaults and gates are fixed in
`strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1C_PROTOCOL.md`,
committed before this file was written. Sleeves reused from F1/F1b (R1, R2, R3, M2a, N1) are
re-run with the same code, so their numbers match the F1b output.

    python research_scripts/r50_f1c.py screen

writes research_scripts/data/r50/f1c_screen.json.
"""
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)
import jesse.indicators as ta

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
from r50_harness import T, O, C, H, L, DAY_MS
from r50_engines import (ASSETS, COMMON, MEASURE_FROM, TAKER, MAKER, STOP_SLIP, TARGET_VOL, MAX_X,
                         rsi2, ann_vol, rebalance, _trade, simulate, calendar, metrics, daily_returns)

N_DECLARED = 80
CORE = fb.CORE
CRYPTO = ['BTC', 'ETH']
CFD = ['XAU', 'SPX', 'WTI', 'GAS', 'BOND']
# C0 class mapping (protocol section 2): per-asset sleeve = mean of these daily return series.
C0_MAP = {'BTC': ['R2', 'R3'], 'ETH': ['R2', 'R3'], 'SPX': ['R1', 'M2a'], 'XAU': ['R1'],
          'WTI': ['N1', 'M2a'], 'GAS': ['N1', 'M2a'], 'BOND': ['R1']}
ASSETS_OF = {'C1': CRYPTO, 'C2': CORE, 'C3': ['SPX', 'XAU'], 'C4': CFD, 'C5': CORE, 'C6': CRYPTO}


def c1_decider(bars, cfd):
    c = bars[:, C]
    vol = ann_vol(c, cfd)

    def decide(i, acct, ts):
        if i < 7 or not np.isfinite(vol[i]) or vol[i] <= 0:
            return
        target = acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i] if c[i] > c[i - 7] else 0.0
        rebalance(acct, target, c[i], ts)
    return decide


def monthly_decider(bars, cfd, rule):
    """C2 (12-1 momentum) and C3 (always long), evaluated at the last daily close of a month."""
    c = bars[:, C]
    vol = ann_vol(c, cfd)
    is_me, _ = fb._month_end_flags(bars)
    me = []

    def decide(i, acct, ts):
        if not is_me[i]:
            return
        me.append(c[i])
        if not np.isfinite(vol[i]) or vol[i] <= 0:
            return
        if rule == 'c2':
            if len(me) < 14:
                return
            long_ = me[-2] / me[-14] - 1 > 0  # month-end 13 months ago -> month-end 1 month ago
        else:
            long_ = True
        target = acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i] if long_ else 0.0
        rebalance(acct, target, c[i], ts)
    return decide


def c5_decider(h4, daily, cfd):
    c, l, o = h4[:, C], h4[:, L], h4[:, O]
    r2 = rsi2(c)
    a14 = ta.atr(h4, period=14, sequential=True)
    frac = fb.daily_ensemble_frac(daily)
    d_close_ts = daily[:, T].astype(np.int64) + DAY_MS
    d_vol = ann_vol(daily[:, C], cfd)
    st = {'limit': None}

    def dctx(i):
        j = int(np.searchsorted(d_close_ts, int(h4[i, T]) + fb.H4_MS, side='right')) - 1
        return (frac[j], d_vol[j]) if j >= 0 else (0.0, np.nan)

    def decide(i, acct, ts):
        f, vol = dctx(i)
        if acct.is_open:
            if fb.stop_exit(acct, st, o, l, i, ts):
                return
            if f < 0.5:
                _trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if st['limit'] is not None:
            px, qty, dist = st['limit']
            st['limit'] = None
            if l[i] < px:
                _trade(acct, qty, px, ts, MAKER)
                st['stop'] = px - dist
                if l[i] <= st['stop']:
                    _trade(acct, -acct.qty, st['stop'] * (1 - STOP_SLIP), ts, TAKER)
                return
        if f >= 0.5 and np.isfinite(r2[i]) and r2[i] < 10 and np.isfinite(vol) and vol > 0 \
                and np.isfinite(a14[i]) and 0 < 3 * a14[i] < c[i]:
            st['limit'] = (c[i], acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol) / c[i], 3 * a14[i])
    return decide


def mean_curve(curves):
    """Daily mean of several sleeves' returns, as a 10k-based equity curve on common days."""
    series = [daily_returns(*cv) for cv in curves]
    days = sorted(set.intersection(*[set(s) for s in series]))
    r = np.array([np.mean([s[d] for s in series]) for d in days])
    return np.r_[days[0] - DAY_MS, days], en.BALANCE * np.r_[1.0, np.cumprod(1 + r)]


def screen():
    out = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1C_PROTOCOL.md', 'n_declared': N_DECLARED,
           'assets': {}, 'baskets': {}}
    curves, trades = {}, {}
    for window in ('common', 'long'):
        for name in CORE:
            if ASSETS[name][window] is None:
                out['assets'].setdefault(name, {})[window] = {'status': 'sin lente larga (límite declarado)'}
                continue
            d = fb.load_both(name, window)
            if d is None:
                continue
            runs = {'R1': lambda: fb.r1_run(name, d),
                    'C2': lambda: simulate(d['daily'], d['start_ms'], monthly_decider(d['daily'], d['cfd'], 'c2'), name, d['funding']),
                    'C5': lambda: simulate(d['h4'], d['start_ms'], c5_decider(d['h4'], d['daily'], d['cfd']), name, d['funding'], fb.H4_MS)}
            if name in CRYPTO:
                runs['R2'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], False), name, d['funding'], fb.H4_MS)
                runs['R3'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], True), name, d['funding'], fb.H4_MS)
                runs['C1'] = lambda: simulate(d['daily'], d['start_ms'], c1_decider(d['daily'], d['cfd']), name, d['funding'])
            else:
                runs['C4'] = lambda: simulate(d['daily'], d['start_ms'], fb.r2_r3_decider(d['daily'], False, None), name, d['funding'])
            if name in ('SPX', 'XAU'):
                runs['C3'] = lambda: simulate(d['daily'], d['start_ms'], monthly_decider(d['daily'], d['cfd'], 'c3'), name, d['funding'])
            if name in ('SPX', 'WTI', 'GAS'):
                runs['M2a'] = lambda: simulate(d['daily'], d['start_ms'], en.m2_decider(d['daily'], d['cfd'], 'a'), name, d['funding'])
            if name in ('WTI', 'GAS'):
                runs['N1'] = lambda: simulate(d['daily'], d['start_ms'], fb.n1_decider(d['daily'], d['cfd']), name, d['funding'])
            rec = {'source': d['source']}
            last = d['daily'][-1, C]
            for cand, fn in runs.items():
                ts, eq, acct = fn()
                days, vals = calendar(ts, eq, d['mfrom'], COMMON[1])
                tr = acct.trades + ([{'opened': 0, 'closed': int(ts[-1]), 'pnl': acct.upnl(last), 'side': 1.0}]
                                    if acct.is_open else [])
                mt = metrics(days, vals, tr, d['mfrom']) or {'error': 'too short'}
                mt.update(fees_paid=acct.fees_paid, funding_paid=acct.funding_paid)
                rec[cand] = mt
                curves[(cand, window, name)] = (days, vals)
                trades[(cand, window, name)] = [t['pnl'] for t in tr if t['closed'] >= hz._ms(d['mfrom'])]
            # Composite sleeves: C6 (crypto R2+R3) and the C0 class sleeve of this asset.
            if name in CRYPTO:
                curves[('C6', window, name)] = mean_curve([curves[('R2', window, name)], curves[('R3', window, name)]])
                trades[('C6', window, name)] = trades[('R2', window, name)] + trades[('R3', window, name)]
            parts = [p for p in C0_MAP[name] if (p, window, name) in curves]
            if parts:
                curves[('C0', window, name)] = mean_curve([curves[(p, window, name)] for p in parts])
                trades[('C0', window, name)] = sum((trades[(p, window, name)] for p in parts), [])
            out['assets'].setdefault(name, {})[window] = rec
            hz.jh.debug(f'{name} {window}: ' + json.dumps({k: round(v['sharpe'], 2) for k, v in rec.items()
                                                           if isinstance(v, dict) and 'sharpe' in v}))
        # Baskets.
        groups = dict(ASSETS_OF, C0=CORE, R1=CORE)
        for cand, members in groups.items():
            keys = [(cand, window, n) for n in members if (cand, window, n) in curves]
            if not keys:
                continue
            bk = fb.basket(curves, keys)
            m = metrics(bk[0], bk[1], [], datetime.fromtimestamp(bk[0][0] / 1000, tz=timezone.utc).date().isoformat())
            pnl = sum((trades[k] for k in keys), [])
            tot = sum(pnl)
            per_year = [out['assets'][k[2]][window][cand]['trades_per_year'] for k in keys
                        if cand in out['assets'][k[2]][window] and 'trades_per_year' in out['assets'][k[2]][window][cand]]
            m.update(members=[k[2] for k in keys], top5_share=(sum(sorted(pnl, reverse=True)[:5]) / tot) if tot > 0 else None,
                     trades_per_year=sum(per_year) if per_year else None, dsr=fb.dsr(bk[1], N_DECLARED))
            out['baskets'].setdefault(cand, {})[window] = m
            curves[(cand, window, 'BASKET')] = bk
            # R1 on the same assets, for the "beats R1" gate of class-specific candidates.
            r1keys = [('R1', window, k[2]) for k in keys if ('R1', window, k[2]) in curves]
            if cand != 'R1' and r1keys:
                r1b = fb.basket(curves, r1keys)
                r1m = metrics(r1b[0], r1b[1], [], datetime.fromtimestamp(r1b[0][0] / 1000, tz=timezone.utc).date().isoformat())
                m['r1_same_assets'] = {'sharpe': r1m['sharpe'], 'quarters_pos': r1m['quarters_pos']}
                c_, nl = fb.corr_in_losing(r1b, bk)
                m['corr_r1_losing_quarters'] = c_
    out['gates'] = gates(out['baskets'])
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1c_screen.json'), 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    hz.jh.debug(json.dumps(out['gates'], indent=1, default=bool))


def gates(b):
    """PHASE1C_PROTOCOL.md section 3 (plain Python bools)."""
    res = {}
    r1_7 = b['R1']['common']
    for cand in ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']:
        if cand not in b or 'common' not in b[cand]:
            res[cand] = {'error': 'missing'}
            continue
        c, l = b[cand]['common'], b[cand].get('long')
        g = {}
        top5 = c.get('top5_share')
        g['top5_lt_60pct'] = None if (cand == 'C3' or top5 is None) else bool(top5 < 0.6)
        if cand == 'C0':
            g['sharpe_gt_r1'] = bool(c['sharpe'] > r1_7['sharpe'])
            g['q_ge_r1'] = bool(c['quarters_pos'] >= r1_7['quarters_pos'])
            core = g['sharpe_gt_r1'] and g['q_ge_r1'] and g['top5_lt_60pct'] is not False
        else:
            ref = c.get('r1_same_assets', r1_7)
            g['sharpe_ge_0_8'] = bool(c['sharpe'] >= 0.8)
            g['beats_r1_same_assets'] = bool(c['sharpe'] > ref['sharpe'] or c['quarters_pos'] > ref['quarters_pos'])
            core = g['sharpe_ge_0_8'] and g['beats_r1_same_assets'] and g['top5_lt_60pct'] is not False
        g['long_veto'] = bool(l is None or l['sharpe'] < 0 or l['max_dd'] < -0.25)
        g['pass'] = bool(core and not g['long_veto'])
        res[cand] = g
    return res


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'screen':
        screen()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
