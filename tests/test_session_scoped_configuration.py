import asyncio
import sys
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from jesse.controllers import backtest_controller, live_controller, monte_carlo_controller
from jesse.enums import live_session_statuses
from jesse.info import exchange_info
from jesse.mcp.tools.services import backtest as mcp_backtest_service
from jesse.services import funding, open_interest
from jesse.services.web import (
    BacktestRequestJson,
    LiveRequestJson,
    MonteCarloRequestJson,
    SignificanceTestRequestJson,
)


def _backtest_request(state: dict) -> BacktestRequestJson:
    return BacktestRequestJson(
        id='backtest-id',
        exchange='Binance Spot',
        routes=[],
        data_routes=[],
        config={'warm_up_candles': 210},
        start_date='2024-01-01',
        finish_date='2024-02-01',
        debug_mode=False,
        export_csv=False,
        export_json=False,
        export_chart=False,
        fast_mode=True,
        benchmark=False,
        state=state,
    )


def _live_request() -> LiveRequestJson:
    return LiveRequestJson(
        id='live-id',
        config={'warm_up_candles': 321},
        exchange='Binance Spot',
        exchange_api_key_id='',
        notification_api_key_id='',
        routes=[],
        data_routes=[],
        debug_mode=True,
        paper_mode=True,
    )


def _monte_carlo_request() -> MonteCarloRequestJson:
    return MonteCarloRequestJson(
        id='monte-carlo-id',
        exchange='Binance Spot',
        routes=[],
        data_routes=[],
        config={'cpu_cores': 1, 'warm_up_candles': 210},
        start_date='2024-01-01',
        finish_date='2024-02-01',
        run_trades=True,
        run_candles=False,
        num_scenarios=200,
        fast_mode=True,
        cpu_cores=1,
        state={'form': {'config': {'cpu_cores': 1}}},
    )


def _significance_test_request(state: dict) -> SignificanceTestRequestJson:
    return SignificanceTestRequestJson(
        id='significance-test-id',
        exchange='Binance Spot',
        routes=[
            {
                'exchange': 'Binance Spot',
                'symbol': 'BTC-USDT',
                'timeframe': '1m',
                'strategy': 'TestStrategy',
            }
        ],
        data_routes=[],
        config={'warm_up_candles': 210},
        start_date='2024-01-01',
        finish_date='2024-02-01',
        state=state,
    )


def test_spot_exchange_metadata_does_not_advertise_leverage_modes():
    spot_exchanges = [metadata for metadata in exchange_info.values() if metadata['type'] == 'spot']

    assert spot_exchanges
    assert all(metadata['supported_leverage_modes'] == [] for metadata in spot_exchanges)


def test_backtest_persists_the_accepted_form_before_starting_worker(monkeypatch):
    calls = []
    state = {'form': {'config': {'warm_up_candles': 432}}}
    monkeypatch.setattr(backtest_controller.jh, 'validate_cwd', lambda: None)
    monkeypatch.setattr(
        backtest_controller,
        'update_backtest_session_state',
        lambda session_id, saved_state: calls.append(('state', session_id, saved_state)),
    )
    monkeypatch.setattr(
        backtest_controller,
        'update_backtest_session_status',
        lambda session_id, status: calls.append(('status', session_id, status)),
    )
    monkeypatch.setattr(
        backtest_controller.process_manager,
        'add_task',
        lambda *args: calls.append(('worker', args)),
    )

    response = backtest_controller.backtest(_backtest_request(state))

    assert response.status_code == 202
    assert calls[0] == ('state', 'backtest-id', state)
    assert calls[1] == ('status', 'backtest-id', 'running')
    assert calls[2][0] == 'worker'


def test_backtest_request_requires_session_state():
    payload = _backtest_request({}).model_dump()
    payload.pop('state')

    with pytest.raises(ValidationError, match='state'):
        BacktestRequestJson(**payload)


def test_significance_test_request_requires_session_state():
    payload = _significance_test_request({}).model_dump()
    payload.pop('state')

    with pytest.raises(ValidationError, match='state'):
        SignificanceTestRequestJson(**payload)


@pytest.mark.parametrize('historical', [False, True], ids=['market-data-disabled', 'market-data-historical'])
def test_mcp_backtest_launch_sends_final_state_in_start_request(monkeypatch, tmp_path, historical):
    request_payload = _backtest_request({}).model_dump()
    features = {'funding': {'mode': 'disabled'}, 'open_interest': {'mode': 'disabled'}}
    exchange, exchange_type = 'Binance Spot', 'spot'
    if historical:
        # Synthetic, fully validated snapshots exercise the actual preflight;
        # enabled feeds must neither bypass it nor use invented dataset IDs.
        monkeypatch.setattr(funding, '_root', lambda: tmp_path / 'funding')
        monkeypatch.setattr(open_interest, '_root', lambda: tmp_path / 'open-interest')
        start, finish = 1_704_067_200_000, 1_706_745_600_000  # January 2024 UTC
        exchange, exchange_type = funding.EXCHANGE, 'futures'
        funding_id = funding.save_dataset({
            'schema': 1, 'source': funding.SOURCE, 'exchange': exchange, 'symbol': 'BTC-USDT',
            'start': start, 'finish': finish,
            'events': [{'exchange': exchange, 'symbol': 'BTC-USDT', 'settled_at': timestamp,
                        'rate_decimal': .0001, 'mark_price': 10_000}
                       for timestamp in range(start, finish, funding.MAX_INTERVAL_MS)],
        })
        oi_id = open_interest.save_dataset({
            'schema': 1, 'source': open_interest.SOURCE, 'exchange': exchange, 'symbol': 'BTC-USDT',
            'start': start, 'finish': finish, 'period_ms': open_interest.PERIOD_MS,
            'availability_lag_ms': open_interest.AVAILABILITY_LAG_MS,
            'observations': [{'exchange': exchange, 'symbol': 'BTC-USDT', 'observed_at': start,
                              'available_at': start + open_interest.AVAILABILITY_LAG_MS,
                              'quantity_base': 20_000., 'value_quote': 200_000_000.}],
        })
        features = {'funding': {'mode': 'historical', 'dataset_id': funding_id},
                    'open_interest': {'mode': 'historical', 'dataset_id': oi_id, 'max_age_ms': 600_000}}
        request_payload['exchange'] = exchange
    form = {
        key: value
        for key, value in request_payload.items()
        if key not in {'id', 'config', 'state'}
    }
    form['routes'] = [
        {
            'exchange': 'stale-exchange',
            'symbol': 'BTC-USDT',
            'timeframe': '1m',
            'strategy': 'TestStrategy',
        }
    ]
    state = {'form': form, 'results': {}}
    http_calls = []

    def post(url, **kwargs):
        # The launch flow may fetch the draft and start the run; any third URL
        # catches a regression to saving state through a separate request.
        http_calls.append((url, kwargs))
        if url.endswith('/backtest/sessions/backtest-id'):
            return SimpleNamespace(
                status_code=200,
                text='',
                json=lambda: {'session': {'state': state}},
            )
        if url.endswith('/backtest'):
            return SimpleNamespace(status_code=202, text='')
        raise AssertionError(f'Unexpected MCP request: {url}')

    monkeypatch.setattr(mcp_backtest_service, 'hash_password', lambda password: 'hashed')
    monkeypatch.setattr(mcp_backtest_service.requests, 'post', post)
    monkeypatch.setattr(
        mcp_backtest_service,
        'load_session_run_config',
        lambda mode, exchange, overrides: {
            **features,
            'logging': {},
            'warm_up_candles': 210,
            'exchange': {
                'name': exchange,
                'type': exchange_type,
                'balance': 10_000,
                'fee': 0.001,
            },
        },
    )

    response = mcp_backtest_service.run_backtest_service('backtest-id')

    assert response['status'] == 'started'
    assert len(http_calls) == 2
    launch_state = http_calls[-1][1]['json']['state']
    assert launch_state is state
    assert launch_state['form']['routes'][0]['exchange'] == exchange
    assert launch_state['form']['config']['exchange']['type'] == exchange_type
    assert launch_state['results']['selectedRoute']['symbol'] == 'BTC-USDT'
    # The engine-shaped request must preserve both disabled defaults and the
    # selected immutable history IDs; neither may disappear during conversion.
    for name, expected in features.items():
        assert launch_state['form']['config'][name] == expected
        assert http_calls[-1][1]['json']['config'][name] == expected


def test_live_rejects_reusing_a_terminal_session_id(monkeypatch):
    monkeypatch.setitem(
        sys.modules,
        'jesse_live',
        SimpleNamespace(live_mode=SimpleNamespace(run=lambda: None)),
    )
    monkeypatch.setattr(live_controller.jh, 'validate_cwd', lambda: None)
    monkeypatch.setattr(
        live_controller.live_session_repository,
        'get_live_session_by_id',
        lambda session_id: SimpleNamespace(status='finished'),
    )
    monkeypatch.setattr(
        live_controller.process_manager,
        'add_task',
        lambda *args: (_ for _ in ()).throw(AssertionError('terminal session must not start')),
    )

    response = live_controller.live(_live_request())

    assert response.status_code == 409


def test_live_draft_stores_its_config_snapshot(monkeypatch):
    stored = {}
    monkeypatch.setitem(
        sys.modules,
        'jesse_live',
        SimpleNamespace(live_mode=SimpleNamespace(run=lambda: None)),
    )
    monkeypatch.setattr(live_controller.jh, 'validate_cwd', lambda: None)
    monkeypatch.setattr(
        live_controller.live_session_repository,
        'get_live_session_by_id',
        lambda session_id: SimpleNamespace(status=live_session_statuses.DRAFT),
    )
    monkeypatch.setattr(
        live_controller.live_session_repository,
        'store_live_session',
        lambda **kwargs: stored.update(kwargs),
    )
    monkeypatch.setattr(live_controller.process_manager, 'add_task', lambda *args: None)

    response = live_controller.live(_live_request())

    assert response.status_code == 202
    assert stored['state']['form']['config'] == {'warm_up_candles': 321}


def test_monte_carlo_resume_uses_the_stored_config_and_state(monkeypatch):
    stored_state = {'form': {'config': {'cpu_cores': 5, 'warm_up_candles': 987}}}
    session = SimpleNamespace(state='serialized', state_json=stored_state)
    worker_args = []
    monkeypatch.setattr(monte_carlo_controller.jh, 'validate_cwd', lambda: None)
    monkeypatch.setattr(
        monte_carlo_controller,
        'get_monte_carlo_session_by_id',
        lambda session_id: session,
    )
    monkeypatch.setattr(
        monte_carlo_controller,
        'get_monte_carlo_session_for_load_more',
        lambda value: {'id': 'monte-carlo-id'},
    )
    monkeypatch.setattr(
        monte_carlo_controller.process_manager,
        'add_task',
        lambda *args: worker_args.extend(args),
    )

    response = asyncio.run(monte_carlo_controller.resume_monte_carlo(_monte_carlo_request()))

    assert response.status_code == 200
    assert worker_args[2] == stored_state['form']['config']
    assert worker_args[12] == 5
    assert worker_args[-1] == stored_state
