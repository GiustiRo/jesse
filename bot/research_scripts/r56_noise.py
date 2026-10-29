"""r56 F6: market-derived switching tolerance f_mkt for the amended bridge (PROTOCOL_R56, r56-B).

No detector is involved. Each label is measured a second time from the same market data:
* vol: realised variance from 2h returns ending on even hours and on odd hours instead of 1h
  returns (two independent subsamplings of the same quantity);
* trend and range: daily bars cut at 12:00 UTC instead of 00:00 UTC.
For every development coin, ratio = label switches per year of the second measurement over those
of the official label, on eligible days whose label window closes by 2023-12-31. f_mkt per axis
and horizon = median ratio (vol pools the even and odd ratios). It measures how many regime changes
appear from measurement noise alone, which no forecast can remove; the amended bridge criterion 4a
allows the operable state at most f_mkt times the switches of its own label.

    python research_scripts/r56_noise.py run

writes data/r56/f6_noise.json.
"""
import json
import os
import sys

import numpy as np
import pandas as pd

import r56_panel as pn

OUT = pn.OUT


def _switch_rates(y, mask):
    out = np.full(y.shape[1], np.nan)
    for j in range(y.shape[1]):
        v = y[mask[:, j], j]
        v = v[np.isfinite(v)]
        if len(v) > 200:
            out[j] = (np.diff(v) != 0).sum() / len(v) * 365
    return out


def run():
    day_ms, syms, P = pn._official()
    hold = json.load(open(os.path.join(OUT, 'holdout.json')))['holdout']
    dev = np.array([s not in hold for s in syms])
    end = int(pd.Timestamp(pn.DEV_LABEL_END, tz='UTC').value // 10**6)
    t20 = json.load(open(os.path.join(OUT, 'f0_labels.json')))['thresholds']
    t40 = json.load(open(os.path.join(OUT, 'f6_labels_h40.json')))['thresholds']
    thr = {20: (t20['a'], t20['e'], t20['k']), 40: (t20['a'], t40['e'], t40['k'])}
    alt = {}
    for name, kw in (('2h_even', {'rv_mode': '2h_even'}), ('2h_odd', {'rv_mode': '2h_odd'}),
                     ('noon', {'offset_hours': 12})):
        d, s, Pa = pn.load_panel(**kw)
        assert s == syms and np.array_equal(d, day_ms)
        alt[name] = Pa
    res = {}
    for h, (a, e, k) in thr.items():
        mask = P['elig'] & dev[None, :] & ((day_ms + h * 86_400_000) <= end)[:, None]
        off = pn.classify(pn.raw_scores(P, h), a, e, k, 'fut')
        res[h] = {}
        for ax, sources in (('vol', ('2h_even', '2h_odd')), ('trend', ('noon',)), ('range', ('noon',))):
            base = _switch_rates(off[ax], mask)
            ratios, rates = [], {}
            for src in sources:
                ya = pn.classify(pn.raw_scores(alt[src], h), a, e, k, 'fut')[ax]
                r = _switch_rates(ya, mask)
                ok = np.isfinite(r) & np.isfinite(base) & (base > 0)
                ratios += list(r[ok] / base[ok])
                rates[src] = round(float(np.nanmedian(r)), 2)
            res[h][ax] = {'label_switches_median': round(float(np.nanmedian(base)), 2), 'alt_switches_median': rates,
                          'f_mkt': round(float(np.median(ratios)), 3), 'n_ratios': len(ratios)}
    json.dump(res, open(os.path.join(OUT, 'f6_noise.json'), 'w'), indent=2)
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)
