"""r59 F1: rebuild the daily curves of past variants by re-running their frozen entrypoints and
recording every curve that reaches a metrics function (PROTOCOL_R59.md §2).

Run ONLY in a throwaway container with the checkout mounted read-only and data/r59/capture
writable, so the frozen scripts cannot overwrite their committed outputs:
    docker run --rm -v <repo>:/src:ro -v <repo>/bot/research_scripts/data/r59/capture:/src/bot/research_scripts/data/r59/capture \
        -w /src/bot -e PYTHONPATH=/src salehmir/jesse:latest python research_scripts/r59_capture.py <tag> <module> <argv...>

The recorder wraps r50_f2.r9, r50_engines.metrics and the pandas-series stats of r52_xs/r52_q in
every loaded module (scripts import them by name). Each call is logged in order with the short
scalar locals of the calling r5* frames (cand, window, name, ...) so a curve can be tied to its
trial id; a curve identical to an earlier one is logged as `dup_of` without storing it again.
Writes under /src are redirected to a sink in /tmp (and read back from there), so a script runs to
its end without touching its committed outputs on the read-only mount. The holdout guard stays on,
so a script that reaches N2/N3 stops there and its later curves are reported missing.
"""
import builtins
import contextlib
import hashlib
import importlib
import inspect
import io
import json
import os
import sys

import numpy as np

import r59_holdout as hg

hg.install()

CAP = os.path.join(hg.OUT, 'capture')
CUT_MS = 1735689600000                    # 2025-01-01 00:00 UTC, exclusive
SINK = '/tmp/r59_sink'
_REC = {'calls': [], 'curves': [], 'seen': {}}
_SCALAR = (str, int, float, bool, np.integer, np.floating)


def _short(v):
    if isinstance(v, _SCALAR) and len(str(v)) <= 60:
        return v if isinstance(v, (str, bool)) else float(v)
    if isinstance(v, tuple) and len(v) <= 4 and all(isinstance(x, _SCALAR) for x in v):
        return [_short(x) for x in v]
    return None


def _ctx():
    """Stack and short scalar locals of the innermost r5* frames (r59 excluded): the loop variables
    that name the variant (cand, window, name, key, ...)."""
    stack, ctx = [], []
    for fi in inspect.stack(0)[3:]:
        f = os.path.basename(fi.filename)
        if f.startswith('r5') and not f.startswith('r59'):
            stack.append(f'{f[:-3]}.{fi.function}:{fi.lineno}')
            if len(ctx) < 3:
                loc = {k: _short(v) for k, v in fi.frame.f_locals.items() if not k.startswith('_')}
                ctx.append({k: v for k, v in loc.items() if v is not None})
    return stack[:5][::-1], ctx


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
    stack, ctx = _ctx()
    call = {'j': len(_REC['calls']), 'kind': kind, 'stack': stack, 'ctx': ctx, 'extra': extra,
            'sharpe': None if sharpe is None else float(sharpe)}
    if key in _REC['seen']:
        call['dup_of'] = _REC['seen'][key]
    else:
        i = len(_REC['curves'])
        _REC['seen'][key] = i
        _REC['curves'].append({'i': i, 'days': d, 'vals': v})
        call.update({'i': i, 'from': int(d[0]), 'to': int(d[-1]), 'n': int(len(d))})
    _REC['calls'].append(call)


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


def _wrap_series(fn, kind):
    """r52_xs.stats(r, frm, to) / r52_q.stats(r, w): a pandas daily-return series, recorded as the
    equity curve over the measured window (the same days the script measures)."""
    def w(r, *a, **k):
        res = fn(r, *a, **k)
        try:
            import pandas as pd
            frm, to = (a[0], a[1]) if len(a) >= 2 else tuple(a[0])
            x = r[(r.index >= pd.Timestamp(frm, tz='UTC')) & (r.index <= pd.Timestamp(to, tz='UTC'))]
            if len(x) >= 30:
                days = (x.index.view('int64') // 10**6).astype(np.int64)
                _record(kind, days, np.cumprod(1 + x.values), [f'{frm}..{to}'], res)
        except Exception as e:
            print('capture error', e, file=sys.stderr)
        return res
    w._r59 = True
    return w


def _redirect_writes():
    """Send writes under /src to SINK (read back from there), so frozen scripts finish without
    altering their committed outputs; the read-only mount stays the backstop."""
    real_open, real_makedirs = builtins.open, os.makedirs
    written = set()

    def sink(p):
        return os.path.join(SINK, os.path.abspath(os.fspath(p)).lstrip('/'))

    def op(file, mode='r', *a, **k):
        if isinstance(file, (str, os.PathLike)):
            p = os.path.abspath(os.fspath(file))
            if p.startswith('/src/') and not p.startswith(CAP) and any(c in mode for c in 'wax+'):
                real_makedirs(os.path.dirname(sink(p)), exist_ok=True)
                written.add(p)
                return real_open(sink(p), mode, *a, **k)
            if p in written:
                return real_open(sink(p), mode, *a, **k)
        return real_open(file, mode, *a, **k)

    def mk(name, *a, **k):
        p = os.path.abspath(os.fspath(name))
        if p.startswith('/src/') and not p.startswith(CAP):
            return real_makedirs(sink(p), exist_ok=True)
        return real_makedirs(name, *a, **k)

    builtins.open = io.open = op
    os.makedirs = mk


def patch():
    import r50_engines as en
    import r50_f2 as f2
    orig = {'r9': f2.r9, 'metrics': en.metrics}
    wrapped = {'r9': _wrap(f2.r9, 'r9'), 'metrics': _wrap(en.metrics, 'metrics')}
    for mod, kind in (('r52_xs', 'xs_stats'), ('r52_q', 'q_stats')):
        try:
            m = importlib.import_module(mod)
        except Exception:
            continue
        orig[mod] = m.stats
        wrapped[mod] = _wrap_series(m.stats, kind)
    rebind(orig, wrapped)
    return orig, wrapped


def rebind(orig, wrapped):
    for m in list(sys.modules.values()):
        for name, fn in orig.items():
            attr = 'stats' if name.startswith('r52') else name
            if getattr(m, attr, None) is fn:
                setattr(m, attr, wrapped[name])


def main():
    tag, modname, argv = sys.argv[1], sys.argv[2], sys.argv[3:]
    _redirect_writes()
    orig, wrapped = patch()
    mod = importlib.import_module(modname)
    rebind(orig, wrapped)                                # modules imported by the target after patch()
    sys.argv = [modname + '.py', *argv]
    err = None
    # The scripts' own prints are discarded: r50/r51 print metrics that include 2025.
    with open(os.devnull, 'w') as null, contextlib.redirect_stdout(null):
        try:
            mod.main()
        except BaseException as e:                       # SystemExit, HoldoutAccess
            err = f'{type(e).__name__}: {str(e)[:300]}'
    os.makedirs(CAP, exist_ok=True)
    np.savez_compressed(os.path.join(CAP, f'{tag}.npz'),
                        **{f"c{c['i']}__days": c['days'] for c in _REC['curves']},
                        **{f"c{c['i']}__vals": c['vals'] for c in _REC['curves']})
    idx = {'tag': tag, 'module': modname, 'argv': argv, 'error': err, 'n_curves': len(_REC['curves']),
           'calls': _REC['calls']}
    with open(os.path.join(CAP, f'{tag}.json'), 'w') as fh:
        json.dump(idx, fh, indent=1, default=str)
    print(f'{tag}: {len(_REC["calls"])} calls, {len(_REC["curves"])} curves; error: {err}')


if __name__ == '__main__':
    main()
