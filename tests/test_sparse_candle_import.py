import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "candle_import_sparse",
    Path(__file__).resolve().parents[1] / "jesse" / "modes" / "import_candles_mode" / "sparse.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
should_refill_sparse_window = _mod.should_refill_sparse_window


def test_refill_when_live_rows_bracket_an_empty_year():
    start = 0
    end = 400_000 * 60_000
    assert should_refill_sparse_window(114, start, end) is True


def test_keep_dense_crypto_window():
    start = 0
    end = 1440 * 60_000
    assert should_refill_sparse_window(1440, start, end) is False


def test_stock_session_hours_are_not_sparse():
    start = 0
    end = 1440 * 60_000
    assert should_refill_sparse_window(390, start, end) is False
