"""r59 F1: rebuild the daily curves of past variants by re-running their frozen entrypoints and
recording every curve that reaches a metrics function (PROTOCOL_R59.md §2).

Run ONLY in a throwaway container with the checkout mounted read-only and data/r59/capture
writable, so the frozen scripts cannot overwrite their committed outputs:
    docker run --rm -v <repo>:/src:ro -v <repo>/bot/research_scripts/data/r59/capture:/src/bot/research_scripts/data/r59/capture \
        -w /src/bot -e PYTHONPATH=/src salehmir/jesse:latest python research_scripts/r59_capture.py <tag> <module> <argv...>

The recorder wraps r50_f2.r9 and r50_engines.metrics in every loaded module (scripts import them by
name), keeps each distinct curve once with its call stack, and lets the script fail on its final
write: the curves recorded before that failure are what matters. The holdout guard stays on, so a
script that reaches N2/N3 stops there and its later curves are reported missing.
"""
import hashlib
import importlib
import json
import os
import sys
import traceback

import numpy as np

import r59_holdout as hg

hg.install()

CAP = os.path.join(hg.OUT, 'capture')
CUT_MS = 1735689600000                    # 2025-01-01 00:00 UTC, exclusive
_REC = {'curves': [], 'seen': set()}


def _stack():
    out = []
    for fr in traceback.extract_stack()[:-2]:
        f = os.path.basename(fr.filename)
        if f.startswith('r5') and not f.startswith('r59'):
            out.append(f'{f[:-3]}.{fr.name}:{fr.lineno}')
    return out[-5:]


def _record(kind, days, vals, extra, result):
    d, v = np.asarray(days, np.int64), np.asarray(vals, float)
    key = hashlib.sha256(d.tobytes() + v.tobytes()).hexdigest()
    sharpe = result.get('sharpe') if isinstance(result, dict) else None
    # r50/r51 measured through 2025: keep only days before the seal and drop any metric computed
    # over 2025, so nothing of 2025 is stored or seen (2025 sealed, PROTOCOL_R59 §0).
    if len(d) and d[-1] >= CUT_MS:
        keep = d < CUT_MS
        d, v, sharpe = d[keep], v[keep], None
        if len(d) < 30:
            return
    if key in _REC['seen']:
        return
    _REC['seen'].add(key)
    _REC['curves'].append({'i': len(_REC['curves']), 'kind': kind, 'key': key, 'stack': _stack(), 'extra': extra,
                           'sharpe': None if sharpe is None else float(sharpe), 'days': d, 'vals': v})


def _wrap(fn, kind):
    def w(days, vals, *a, **k):
        res = fn(days, vals, *a, **k)
        try:
            _record(kind, days, vals, [str(x) for x in a[1:2]], res)
        except Exception as e:        # recording must never change the script's behaviour
            print('capture error', e, file=sys.stderr)
        return res
    w._r59 = True
    return w


def patch():
    import r50_engines as en
    import r50_f2 as f2
    orig = {'r9': f2.r9, 'metrics': en.metrics}
    wrapped = {'r9': _wrap(f2.r9, 'r9'), 'metrics': _wrap(en.metrics, 'metrics')}
    for m in list(sys.modules.values()):
        for name in ('r9', 'metrics'):
            if getattr(m, name, None) is orig[name]:
                setattr(m, name, wrapped[name])
    return orig, wrapped


def main():
    tag, modname, argv = sys.argv[1], sys.argv[2], sys.argv[3:]
    orig, wrapped = patch()
    mod = importlib.import_module(modname)
    for m in list(sys.modules.values()):                 # modules imported by the target after patch()
        for name in ('r9', 'metrics'):
            if getattr(m, name, None) is orig[name]:
                setattr(m, name, wrapped[name])
    sys.argv = [modname + '.py', *argv]
    err = None
    import contextlib
    # The scripts' own prints are discarded: r50/r51 print metrics that include 2025.
    with open(os.devnull, 'w') as null, contextlib.redirect_stdout(null):
        try:
            mod.main()
        except BaseException as e:                       # SystemExit, the read-only final write, HoldoutAccess
            err = f'{type(e).__name__}: {str(e)[:300]}'
    os.makedirs(CAP, exist_ok=True)
    np.savez_compressed(os.path.join(CAP, f'{tag}.npz'),
                        **{f"c{c['i']}__days": c['days'] for c in _REC['curves']},
                        **{f"c{c['i']}__vals": c['vals'] for c in _REC['curves']})
    idx = {'tag': tag, 'module': modname, 'argv': argv, 'error': err,
           'curves': [{k: v for k, v in c.items() if k not in ('days', 'vals')} | {
               'from': int(c['days'][0]), 'to': int(c['days'][-1]), 'n': int(len(c['days']))} for c in _REC['curves']]}
    json.dump(idx, open(os.path.join(CAP, f'{tag}.json'), 'w'), indent=1)
    print(f'{tag}: {len(_REC["curves"])} curves; error: {err}')


if __name__ == '__main__':
    main()
