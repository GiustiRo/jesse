import pytest

from jesse.mcp.tools.services.session_config import (
    backtest_engine_config,
    resolve_session_run_config,
)
from jesse.services.backtest_slippage import validate_slippage_bps


@pytest.mark.parametrize('value', [-1, 10000, float('nan'), float('inf'), True, '5', None])
def test_invalid_slippage_is_rejected_instead_of_silently_disabled(value):
    with pytest.raises(ValueError, match='slippage_bps'):
        validate_slippage_bps(value)


def test_session_slippage_reaches_engine_without_changing_global_defaults():
    overrides = {'exchange': {'slippage_bps': 5}}
    result = resolve_session_run_config({}, 'backtest', 'Binance Perpetual Futures', overrides)
    engine = backtest_engine_config(result)
    assert engine['exchanges']['Binance Perpetual Futures']['slippage_bps'] == 5
    assert overrides == {'exchange': {'slippage_bps': 5}}
    assert 'slippage_bps' not in resolve_session_run_config({}, 'backtest', 'Binance Perpetual Futures')['exchange']


@pytest.mark.parametrize('mode,exchange', [
    ('optimization', 'Binance Perpetual Futures'),
    ('monte_carlo', 'Binance Perpetual Futures'),
    ('significance_test', 'Binance Perpetual Futures'),
    ('backtest', 'Binance Spot'),
])
def test_slippage_refuses_unsupported_simulation_modes(mode, exchange):
    with pytest.raises(ValueError, match='only in futures backtests'):
        resolve_session_run_config({}, mode, exchange, {'exchange': {'slippage_bps': 5}})
