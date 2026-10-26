"""r51 F1: confirm the frozen P1 sleeves (R1 per asset, C6 = R2 + R3 on BTC/ETH) in Jesse.

Protocol: `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261025-r51/PROTOCOL_R51.md`
section F1. Each Jesse session runs one sleeve (routes in one session share the wallet, the
harness gives every sleeve its own 10k). The harness side is the frozen r50 code (5caf4a53),
run twice:
* `protocol`: exactly as P1 was measured (extra slippage on bond/gas, 5 bp on stops, maker fee
  on R3's limit fills);
* `jesse_like`: the costs Jesse models (no slippage, one fee for every fill). This is the run
  the tolerance applies to; the gap between both runs is the cost model, not a code mismatch.

    python research_scripts/r51_f1_confirm.py run

writes research_scripts/data/r51/f1_confirm.json.
"""
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
from r50_harness import DonchianEnsR49

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r51')
# Preregistered tolerance (PROTOCOL_R51.md F1): daily Sharpe, CAGR and max DD.
TOL_SHARPE, TOL_CAGR, TOL_DD = 0.10, 0.01, 0.01

# Jesse sessions per sleeve. R1 BTC and WTI reuse identical earlier sessions (no run spent).
SESSIONS = {
    ('R1', 'BTC'): 'b4792187-8847-450d-9f52-320edb4a61dd',
    ('R1', 'WTI'): '063c2564-80c9-4e19-9b64-4add88e660a0',
    ('R2', 'BTC'): '4324b19d-24df-4a5d-b22d-59c4a689b94c',
    ('R2', 'ETH'): '53d66160-5393-4d94-8f43-a1a9d643b506',
    ('R3', 'BTC'): '14fd70de-d056-42f2-a5c6-0f6e9d97dc61',
    ('R3', 'ETH'): '575f5766-7831-4489-9015-e9c21d671532',
    ('R1', 'ETH'): '88349011-dd9b-432f-a381-90fedf1dd7ef',
    ('R1', 'XAU'): '5663eced-0a44-4bbc-b6f0-6c7757c25f53',
    ('R1', 'SPX'): '66ad8b9c-683f-4088-b450-c413c9fba88b',
    ('R1', 'GAS'): '8c9cf609-05c0-4945-ad6b-aa5086e60183',
    ('R1', 'BOND'): '1ad8071b-8f11-4a0f-9211-2891e087ab1d',
}


def harness(sleeve, name, jesse_like):
    """Daily bar-close equity of one sleeve on the common window with the frozen r50 code."""
    d = fb.load_both(name, 'common')
    if sleeve == 'R1':
        h4 = d['h4']
        k = int(np.searchsorted(h4[:, hz.T], d['start_ms'], side='left'))
        slip = 0.0 if jesse_like else en.SLIP_BPS.get(name, 0.0)
        acct = fb.SlipAccount(en.BALANCE, en.TAKER, 3, slip)
        fund = hz.load_funding(en.FUNDING[name]) if d['funding'] and name in en.FUNDING else None
        ts, eq = hz.run(DonchianEnsR49(**fb.R1_CFG[name]), h4[max(0, k - 1520):k], h4[k:], fb.H4_MS, acct, fund)
    else:
        saved = (fb.STOP_SLIP, fb.MAKER)
        if jesse_like:
            # Jesse fills stops at the stop price and charges the single configured fee.
            fb.STOP_SLIP, fb.MAKER = 0.0, en.TAKER
        try:
            ts, eq, acct = en.simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], sleeve == 'R3'),
                                       name, d['funding'], fb.H4_MS)
        finally:
            fb.STOP_SLIP, fb.MAKER = saved
    return hz.daily(ts, eq), acct


def jesse_daily(session_id):
    """Jesse Portfolio points keyed by the UTC day whose close they sample (00:01 or 04:00 of
    the next day maps back to the previous day, as in r50 repro)."""
    pts, metrics = hz.jesse_curve(session_id)
    by_day = {datetime.fromtimestamp((t - 5 * 3_600_000) / 1000, tz=timezone.utc).date().isoformat(): v
              for t, v in sorted(pts.items())}
    return by_day, metrics


def stats(days, values):
    v = np.asarray(values, dtype=float)
    span = (datetime.fromisoformat(days[-1]) - datetime.fromisoformat(days[0])).days or 1
    return {'sharpe': hz.sharpe(v), 'cagr': hz.cagr(v, span), 'max_dd': hz.max_dd(v),
            'final': float(v[-1]), 'q_pos': hz.quarters_positive(days, v)}


def compare(sleeve, name, session_id):
    theirs, metrics = jesse_daily(session_id)
    out = {'sleeve': sleeve, 'asset': name, 'session': session_id,
           'dashboard_url': f'http://localhost:9200/#/backtest/{session_id}',
           'jesse_engine_sharpe': metrics.get('sharpe_ratio'), 'jesse_trades': metrics.get('total'),
           'jesse_fees': metrics.get('fee'), 'jesse_funding': (metrics.get('funding') or {}).get('cashflow')}
    for label, jl in (('jesse_like', True), ('protocol', False)):
        mine, acct = harness(sleeve, name, jl)
        days = sorted(set(mine) & set(theirs))
        a = [mine[x] for x in days]
        b = [theirs[x] for x in days]
        sa, sb = stats(days, a), stats(days, b)
        rel = np.abs(np.array(a) / np.array(b) - 1)
        out[label] = {'harness': sa, 'jesse': sb, 'days': len(days), 'max_rel_err': float(rel.max()),
                      'trades_harness': len(acct.trades) + (1 if acct.is_open else 0),
                      'd_sharpe': sa['sharpe'] - sb['sharpe'], 'd_cagr': sa['cagr'] - sb['cagr'],
                      'd_dd': sa['max_dd'] - sb['max_dd']}
    j = out['jesse_like']
    out['pass'] = bool(abs(j['d_sharpe']) <= TOL_SHARPE and abs(j['d_cagr']) <= TOL_CAGR
                       and abs(j['d_dd']) <= TOL_DD)
    return out


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    extra = {}
    for arg in sys.argv[2:]:  # sleeve:asset=session, for sessions created after this file
        key, sid = arg.split('=')
        s, a = key.split(':')
        extra[(s, a)] = sid
    os.makedirs(OUT, exist_ok=True)
    from jesse.models.BacktestSession import get_backtest_session_by_id
    rows = []
    for (s, a), sid in {**SESSIONS, **extra}.items():
        status = get_backtest_session_by_id(sid).status
        if status != 'finished':
            print(f'{s} {a}: session {sid} is {status}, skipped')
            continue
        rows.append(compare(s, a, sid))
    for r in rows:
        j = r['jesse_like']
        print(f"{r['sleeve']} {r['asset']}: Sharpe H {j['harness']['sharpe']:.3f} J {j['jesse']['sharpe']:.3f} "
              f"CAGR H {j['harness']['cagr']:.4f} J {j['jesse']['cagr']:.4f} DD H {j['harness']['max_dd']:.4f} "
              f"J {j['jesse']['max_dd']:.4f} trades H {j['trades_harness']} J {r['jesse_trades']} pass={r['pass']}")
    path = os.path.join(OUT, 'f1_confirm.json')
    with open(path, 'w') as fh:
        json.dump(rows, fh, indent=2)
    print(path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
