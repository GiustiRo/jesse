"""r59: guard of the reusable holdout H = N2 ∪ N3 (PROTOCOL_R59.md §1.1).

`install()` wraps builtins.open (np.load and pd.read_csv resolve it at call time) and the r58
loaders that take a bank or a symbol. Outside `oracle_context()`, touching a protected file, bank
or symbol raises HoldoutAccess. Every r59 script calls install() at import. This guards against
accidents only: anyone can still read a file by hand. The real protection is the protocol committed
before each query plus the append-only oracle log.

    python research_scripts/r59_holdout.py manifest   # writes data/r59/holdout.json (list + sha256)
"""
import builtins
import contextlib
import functools
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
OUT = os.path.join(DATA, 'r59')
BANKS = ('n2', 'n3')

# Protected files and folders (§1.1): N2/N3 raw data, everything derived from their prices, and the
# r58 confirmation trades. Mixed panels (panel70 = U50 + N2) are protected whole.
_DIRS = (os.path.join(DATA, 'r56', 'n2'), os.path.join(DATA, 'r58', 'n3'))
_FILES = tuple(os.path.join(DATA, *p) for p in (
    ('r58', 'f0_bars_n2.npz'), ('r58', 'f0_bars_n3.npz'), ('r58', 'pred_n3_P5_range40.npy'),
    ('r58', 'f2_trades_n2n3.csv'), ('r56', 'panel70.npz'), ('r56', 'labels70.npz'),
    ('r56', 'panel_n3.npz'), ('r56', 'labels_n3.npz')))
_PATTERNS = ((os.path.join(DATA, 'r56'), 'feat_', '_70.npz'), (os.path.join(DATA, 'r56'), 'feat_', '_n3.npz'),
             (os.path.join(DATA, 'r56'), 'chronos_', '_panel70.npy'), (os.path.join(DATA, 'r56'), 'pred_n2_', '.npy'))
# The manifest files that only list N2/N3 symbols carry no outcomes and stay readable.
_LIST_FILES = (os.path.join(DATA, 'r56', 'n2', 'universe_n2.json'), os.path.join(DATA, 'r56', 'n2', 'manifest.json'))


class HoldoutAccess(RuntimeError):
    pass


_STATE = {'oracle': 0, 'installed': False}
_open = builtins.open


def _norm(p):
    return os.path.normcase(os.path.realpath(os.fspath(p)))


def _protected(path):
    p = _norm(path)
    if p in {_norm(f) for f in _LIST_FILES}:
        return False
    if any(p == _norm(f) for f in _FILES):
        return True
    if any(p.startswith(_norm(d) + os.sep) for d in _DIRS):
        return True
    for d, pre, suf in _PATTERNS:
        if os.path.dirname(p) == _norm(d) and os.path.basename(p).startswith(pre) and p.endswith(suf):
            return True
    return False


def holdout_syms():
    n2 = [u['symbol'] for u in json.load(_open(_LIST_FILES[0]))['selected']]
    n3 = json.load(_open(os.path.join(DATA, 'r58', 'n3_panel.json')))['n3_syms']
    return sorted(n2 + n3)


def in_oracle():
    return _STATE['oracle'] > 0


def _deny(what):
    if not in_oracle():
        raise HoldoutAccess(f'r59 holdout: {what} is protected (PROTOCOL_R59.md §1.1); only r59_oracle reads it')


def guard_path(path):
    if isinstance(path, (str, bytes, os.PathLike)) and _protected(path):
        _deny(os.fspath(path))


def guard_bank(bank):
    if bank in BANKS:
        _deny(f'bank {bank}')


_HSYMS = None


def guard_sym(sym):
    global _HSYMS
    if _HSYMS is None:
        _HSYMS = set(holdout_syms())
    if sym in _HSYMS:
        _deny(f'symbol {sym}')


@contextlib.contextmanager
def oracle_context():
    """Entered only by r59_oracle while it computes a query or a label count."""
    _STATE['oracle'] += 1
    try:
        yield
    finally:
        _STATE['oracle'] -= 1


def _guarded_open(file, *a, **k):
    guard_path(file)
    return _open(file, *a, **k)


def _wrap_bank(fn, pos):
    @functools.wraps(fn)
    def w(*a, **k):
        guard_bank(k['bank'] if 'bank' in k else a[pos])
        return fn(*a, **k)
    return w


def install():
    """Idempotent. Wraps open and the r58 entry points that take a bank (or a symbol)."""
    if _STATE['installed']:
        return
    import r58
    builtins.open = _guarded_open
    for name, pos in (('load_bank', 0), ('c6_bank', 0), ('make_gate', 0), ('trade_table', 1), ('_valid_coin_days', 0)):
        setattr(r58, name, _wrap_bank(getattr(r58, name), pos))
    h4 = r58.h4_bars

    @functools.wraps(h4)
    def h4_bars(src, sym):
        guard_sym(sym)
        return h4(src, sym)
    r58.h4_bars = h4_bars
    _STATE['installed'] = True


def manifest():
    syms = holdout_syms()
    os.makedirs(OUT, exist_ok=True)
    out = {'protocol': 'PROTOCOL_R59.md §0', 'holdout': 'N2 ∪ N3', 'n': len(syms), 'symbols': syms,
           'sha256': hashlib.sha256(json.dumps(syms).encode()).hexdigest()}
    json.dump(out, _open(os.path.join(OUT, 'holdout.json'), 'w'), indent=1)
    print(f"{out['n']} symbols, sha256 {out['sha256']}")


if __name__ == '__main__':
    if sys.argv[1:] == ['manifest']:
        manifest()
    else:
        print(__doc__)
