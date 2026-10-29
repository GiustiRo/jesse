"""r63 F3: funnel after the factory (PROTOCOL_R63 §7).

    python -P r63_f3.py voljump_dev      # §7.4 descriptive: the frozen r62 voljump on D63 (+ its SE for the power)
    python -P r63_f3.py voljump_power    # §7.4 power on L63, written before L63 is read
    python -P r63_f3.py voljump_l63      # §7.4 the pre-registered test on L63 (N + 1)
    python -P r63_f3.py funnel <run>     # §7.1-§7.3 for the finalists of a real run (stops at the first failed step)

The L63 panel is only built inside `l63_test`, after the power file of that program exists.
"""
import json
import math
import os
import sys

import numpy as np

import r59
import r62_dsl as dsl
import r62_eval as ev
import r63_eval as E6

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r63')
SEED = 63
N_BOOT, BLOCK = 2000, 20
POWER_MIN = 0.4
# §7.4: the best-scoring r62 finalist (runs/real_f2/final.json, hash 1521f048...), frozen; only the
# universe changes from crypto_1h (BTC/ETH) to alts_1h. Its r62 development Sharpe is S_D.
VOLJUMP = {'universe': 'alts_1h', 'signal': [{'kind': 'voljump', 'params': {'mode': 'follow', 'ratio': 1.5}}],
           'filters': [{'kind': 'session', 'params': {'s': 'us'}}], 'exit': {'kind': 'time', 'params': {'h': 24}},
           'size': {'kind': 'voltgt', 'params': {'side': 'long'}}, 'exec': {'kind': 'taker', 'params': {}}}
VOLJUMP_R62 = {'hash': '1521f048f29e0403cdc1e6be0b6c9ac91455721b', 'sharpe_d': 1.5348043953483959}


def _dump(name, obj):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))


def boot_sharpes(r, n_boot=N_BOOT, seed=SEED, center=False):
    """Stationary-bootstrap Sharpe draws (block 20); `center` resamples r - mean(r) (the H0 world)."""
    r = np.asarray(r, float)
    x = r - r.mean() if center else r
    rng = np.random.default_rng(seed)
    out = np.empty(n_boot)
    for b in range(n_boot):
        out[b] = ev.sharpe(x[r59.stationary_idx(len(x), rng, BLOCK)])
    return out


def participation_ratio(per, min_overlap=60):
    """N_eff = (sum lambda)^2 / sum lambda^2 of the per-asset daily return correlation (pairwise,
    0 where two assets share fewer than `min_overlap` days); negative eigenvalues clipped at 0."""
    names = [n for n, (d, r) in per.items() if len(d) >= min_overlap and np.std(r) > 0]
    if len(names) < 2:
        return float(len(names))
    days = np.unique(np.concatenate([per[n][0] for n in names]))
    M = np.full((len(days), len(names)), np.nan)
    for i, n in enumerate(names):
        d, r = per[n]
        M[np.searchsorted(days, d), i] = r
    ok = np.isfinite(M)
    Z = np.where(ok, M, 0.0)
    cnt = ok.T.astype(float) @ ok.astype(float)
    s1 = Z.T @ ok.astype(float)                       # sum of x_i over days where j is present
    s2 = (Z * Z).T @ ok.astype(float)
    sxy = Z.T @ Z
    with np.errstate(invalid='ignore', divide='ignore'):
        mx, my = s1 / cnt, s1.T / cnt
        cov = sxy / cnt - mx * my
        vx, vy = s2 / cnt - mx ** 2, s2.T / cnt - my ** 2
        R = cov / np.sqrt(vx * vy)
    R[(cnt < min_overlap) | ~np.isfinite(R)] = 0.0
    np.fill_diagonal(R, 1.0)
    lam = np.clip(np.linalg.eigvalsh((R + R.T) / 2), 0, None)
    return float(lam.sum() ** 2 / (lam ** 2).sum())


def dev_stats(q, sharpe_d=None):
    """Program on D63: basket Sharpe, its bootstrap SE and N_eff (inputs of the L63 power)."""
    E = E6.evaluator(E6.load_src(E6.dev_syms()))
    q = dsl.validate(q)
    per, tr, _ = ev.run_program(q, E.panel)
    days, r = ev.basket(per)
    s = ev.sharpe(r)
    se = float(np.nanstd(boot_sharpes(r)))
    neff = participation_ratio(per)
    return {'program': q, 'sharpe_d63': s, 'se_d63': se, 'n_eff_d63': neff, 'n_days': int(len(r)),
            'trades': int(sum(len(v) for v in tr.values())), 'n_tramos': len(per),
            'sharpe_d_for_power': sharpe_d if sharpe_d is not None else s,
            'years': {str(y): ev.sharpe(r[E6._year(days) == y]) for y in E6.YEARS}}


def power(dev, n_dev=197, n_loc=98):
    """§7.3: EE_L = EE_D sqrt(N_eff_D / N_eff_L), N_eff_L = N_eff_D * n_loc/n_dev; one-sided 5%."""
    neff_l = dev['n_eff_d63'] * n_loc / n_dev
    se_l = dev['se_d63'] * math.sqrt(dev['n_eff_d63'] / neff_l)
    s = dev['sharpe_d_for_power']
    pw = 0.5 * (1 + math.erf(((0.5 * s - 1.645 * se_l) / se_l) / math.sqrt(2)))
    return {'n_eff_l63': neff_l, 'se_l63': se_l, 'half_s_d': 0.5 * s, 'power': pw, 'power_ok': pw >= POWER_MIN}


def l63_test(q, power_file):
    """§7.3 criterion on L63: Sharpe > 0, one-sided bootstrap p < 0.05, >= 3 of 5 years positive."""
    assert os.path.exists(os.path.join(OUT, power_file)), 'power must be written before L63 is read'
    E = E6.evaluator(E6.load_src(E6.local_syms()))
    q = dsl.validate(q)
    per, tr, _ = ev.run_program(q, E.panel)
    days, r = ev.basket(per)
    s = ev.sharpe(r)
    null = boot_sharpes(r, center=True)
    p = float((1 + np.sum(np.nan_to_num(null, nan=-np.inf) >= s)) / (1 + len(null)))
    yrs = {str(y): ev.sharpe(r[E6._year(days) == y]) for y in E6.YEARS}
    npos = sum(1 for v in yrs.values() if np.isfinite(v) and v > 0)
    per2, _, _ = ev.run_program(q, E.panel, cost_mult=2.0, cross=2 * dsl.CROSS)
    # descriptive (§2): survivors only, i.e. without the tramos of delisted symbols
    surv = {n: v for n, v in per.items() if not E.panel.src[n]['delisted']}
    return {'program': q, 'sharpe_l63': s, 'p_one_sided': p, 'years': yrs, 'years_positive': npos,
            'pass': bool(s > 0 and p < 0.05 and npos >= 3), 'n_days': int(len(r)), 'n_tramos': len(per),
            'trades': int(sum(len(v) for v in tr.values())), 'sharpe_cost2': ev.sharpe(ev.basket(per2)[1]),
            'sharpe_survivors_only': ev.sharpe(ev.basket(surv)[1]) if surv else None,
            'n_delisted_tramos': len(per) - len(surv)}


def main():
    cmd = sys.argv[1]
    if cmd == 'voljump_dev':
        d = dev_stats(VOLJUMP, sharpe_d=VOLJUMP_R62['sharpe_d'])
        d['r62'] = VOLJUMP_R62
        _dump('f3_voljump_d63.json', d)
        print(json.dumps(d, indent=1, default=str))
    elif cmd == 'voljump_power':
        with open(os.path.join(OUT, 'f3_voljump_d63.json')) as f:
            d = json.load(f)
        pw = power(d)
        _dump('f3_voljump_power.json', pw)
        print(json.dumps(pw, indent=1))
    elif cmd == 'voljump_l63':
        res = l63_test(VOLJUMP, 'f3_voljump_power.json')
        _dump('f3_voljump_l63.json', res)
        print(json.dumps(res, indent=1, default=str))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()
