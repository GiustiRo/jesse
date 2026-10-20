"""Authenticated UI/MCP contracts against an isolated in-memory session database."""

import json
from types import SimpleNamespace
from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient
from peewee import SqliteDatabase
import pytest

from jesse.controllers import funding_controller as controller
from jesse.models.BacktestSession import BacktestSession, get_backtest_sessions
from jesse.services.auth import require_auth
from jesse.services import funding, session_results
from jesse.mcp.tools.services.session_config import (
    backtest_engine_config, resolve_session_run_config, live_session_defaults,
    normalize_live_run_config, live_engine_config,
)
from jesse.mcp.tools.services.live import _parse_config, _Failure
from jesse.services.web import BacktestRequestJson
from jesse.services.web import LiveRequestJson
from tests.test_funding import START, EXCHANGE, dataset


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(funding, '_root', lambda: tmp_path / 'funding')
    app = FastAPI()
    app.include_router(controller.router)
    app.include_router(controller.oi_router)
    app.dependency_overrides[require_auth] = lambda: None
    database = SqliteDatabase(':memory:', check_same_thread=False)
    with database.bind_ctx([BacktestSession]):
        database.connect()
        database.create_tables([BacktestSession])
        # Keep controller calls on the test thread: SQLite :memory: is connection-local.
        yield SimpleNamespace(app=app, http=TestClient(app), database=database)
        database.close()


def create(status='draft', metrics=None, config=None):
    return BacktestSession.create(id=uuid4(), status=status, state=json.dumps({'form': {
        'exchange': EXCHANGE, 'routes': [{'symbol': 'BTC-USDT', 'strategy': 'Test19', 'timeframe': '1m'}],
        'start_date': '2020-01-01', 'finish_date': '2020-01-02', 'config': config or {},
    }}), metrics=json.dumps(metrics) if metrics is not None else None, created_at=START, updated_at=START)


def request(row, **kwargs):
    return controller.SessionRequest(session_id=row.id, **kwargs)


def test_api_authentication_required(monkeypatch):
    from jesse.services import auth
    # Unit environment intentionally has no project credentials.
    monkeypatch.setitem(auth.ENV_VALUES, 'PASSWORD', 'unit-fixture-password')
    app = FastAPI()
    app.include_router(controller.router)
    response = TestClient(app).post('/funding/datasets', json={})
    assert response.status_code == 401


def test_requested_is_not_evidence_but_zero_cashflow_can_be_applied(client):
    row = create(config={'funding': {'mode': 'historical', 'dataset_id': 'a' * 64}})
    result = controller.session(request(row))
    assert result['requested_mode'] == 'historical'
    assert result['applied'] is False
    assert result['status'] == 'not_applied'
    assert result['cashflow'] is None
    row.metrics = json.dumps({'funding': {'mode': 'historical', 'status': 'applied', 'applied': True,
                                         'dataset_id': 'a' * 64,
                                         'cashflow': 0, 'event_count': 0, 'ledger': []}})
    row.status = 'finished'
    row.save()
    result = controller.session(request(row))
    assert result['applied'] is True
    assert result['cashflow'] == 0


def test_paginated_ledger_is_distinct_from_fees(client):
    rows = [{'cashflow': -1, 'settled_at': START + i * 60_000} for i in range(3)]
    row = create(status='finished', metrics={'fee': 5, 'funding': {
        'mode': 'historical', 'dataset_id': 'a' * 64, 'applied': True, 'cashflow': -3, 'ledger': rows, 'event_count': 3}},
        config={'funding': {'mode': 'historical', 'dataset_id': 'a' * 64}})
    result = controller.session(request(row, limit=2))
    assert result['total'] == 3
    assert result['next_offset'] == 2
    assert result['ledger'] == rows[:2]
    assert controller.session(request(row, offset=2))['ledger'] == rows[2:]


@pytest.mark.parametrize('status,dataset_id', [('stopped', 'a' * 64), ('running', 'a' * 64),
                                               ('finished', 'b' * 64)])
def test_prior_run_metrics_cannot_prove_current_feed_was_applied(client, status, dataset_id):
    old = {'mode': 'historical', 'dataset_id': 'a' * 64, 'applied': True,
           'status': 'applied', 'cashflow': -3, 'ledger': [{'cashflow': -3}]}
    row = create(status=status, config={name: {'mode': 'historical', 'dataset_id': dataset_id}
                                       for name in ('funding', 'open_interest')},
                 metrics={'funding': old, 'open_interest': old})
    result = controller.session(request(row))
    assert result['applied'] is False
    assert result['status'] == 'not_applied'
    assert result['cashflow'] is None
    assert result['ledger'] == []
    assert result['open_interest'] is None


def test_draft_config_saved_only_after_full_coverage_preflight(client):
    events = [(START + i * 8 * 3_600_000, .0001, 10_000) for i in range(3)]
    identifier = dataset(events, finish=START + 24 * 3_600_000)
    row = create()
    saved = controller.session_config(controller.SessionConfigRequest(
        session_id=row.id, funding={'mode': 'historical', 'dataset_id': identifier}))
    assert saved['funding_config']['dataset_id'] == identifier
    assert BacktestSession.get_by_id(row.id).state_json['form']['config']['funding']['mode'] == 'historical'
    assert get_backtest_sessions(status_filter='draft')[0].id == row.id
    assert get_backtest_sessions() == []
    row.status = 'finished'
    row.save(only=[BacktestSession.status])
    with pytest.raises(controller.HTTPException) as error:
        controller.session_config(controller.SessionConfigRequest(session_id=row.id, funding={'mode': 'disabled'}))
    assert error.value.status_code == 409


def test_config_refuses_missing_and_uncovered_datasets(client):
    row = create()
    with pytest.raises(controller.HTTPException) as error:
        controller.session_config(controller.SessionConfigRequest(
            session_id=row.id, funding={'mode': 'historical', 'dataset_id': 'a' * 64}))
    assert error.value.status_code == 400
    assert BacktestSession.get_by_id(row.id).state_json['form']['config'] == {}


def test_raw_funding_data_read_is_bounded_paginated_and_checksum_verified(client):
    identifier = dataset([(START + i * 60_000, .0001, 10_000) for i in range(3)])
    metadata = controller.get_dataset(controller.FundingDatasetRequest(dataset_id=identifier))
    assert 'events' not in metadata
    first = controller.get_dataset(controller.FundingDatasetRequest(dataset_id=identifier, include_events=True, limit=2))
    assert len(first['events']) == 2
    assert first['total'] == 3
    assert first['next_offset'] == 2
    last = controller.get_dataset(controller.FundingDatasetRequest(dataset_id=identifier, include_events=True, offset=2))
    assert last['events'][0]['settled_at'] == START + 2 * 60_000
    assert last['next_offset'] is None


def test_existing_mcp_run_config_retains_selected_feeds():
    selected = {'mode': 'historical', 'dataset_id': 'a' * 64}
    run = resolve_session_run_config({}, 'backtest', EXCHANGE, {'funding': selected, 'open_interest': selected})
    engine = backtest_engine_config(run)
    assert engine['funding'] == selected
    assert engine['open_interest'] == selected
    live = normalize_live_run_config({'funding': {'mode': 'live'}, 'open_interest': {'mode': 'live'}},
                                     live_session_defaults({})['fallback'])
    assert live_engine_config(live)['funding']['mode'] == 'live'
    assert live_engine_config(live)['open_interest']['mode'] == 'live'
    assert _parse_config({'funding': {'mode': 'live'}})['funding']['mode'] == 'live'
    with pytest.raises(_Failure):
        _parse_config({'funding': {'mode': 'historical'}})


def test_backtest_request_recovers_dashboard_optional_fields_and_validates(client):
    identifier = dataset([(START + i * 8 * 3_600_000, .0001, 10_000) for i in range(3)],
                         finish=START + 24 * 3_600_000)
    payload = dict(id=str(uuid4()), exchange=EXCHANGE, routes=[{'symbol': 'BTC-USDT'}], data_routes=[],
                   config={}, start_date='2020-01-01', finish_date='2020-01-02', debug_mode=False,
                   export_csv=False, export_json=False, export_chart=False, fast_mode=True, benchmark=False,
                   state={'form': {'config': {'funding': {'mode': 'historical', 'dataset_id': identifier}}}})
    parsed = BacktestRequestJson(**payload)
    assert parsed.config['funding']['dataset_id'] == identifier


def test_session_results_summary_omits_bulky_ledger_but_section_and_export_retain_it(client, monkeypatch):
    rows = [{'cashflow': -1, 'settled_at': START}]
    row = create(status='finished', metrics={'funding': {'mode': 'historical', 'applied': True, 'ledger': rows}})
    monkeypatch.setattr(session_results, '_load_backtest', lambda identity: row)
    result = session_results.get_results('backtest', str(row.id))
    assert 'ledger' not in result['metrics']['funding']
    page = session_results.get_results('backtest', str(row.id), section='funding')
    assert page['items'] == rows
    assert session_results._backtest_parts(row)['metrics']['funding']['ledger'] == rows


def test_live_model_rejects_paper_features_before_queuing_a_worker():
    payload = dict(id=str(uuid4()), exchange=EXCHANGE, exchange_api_key_id='key-id',
                   notification_api_key_id='', routes=[{'symbol': 'BTC-USDT', 'timeframe': '1m', 'strategy': 'Test19'}],
                   data_routes=[], config={'funding': {'mode': 'live'}}, debug_mode=False, paper_mode=False)
    assert LiveRequestJson(**payload).config['funding']['mode'] == 'live'
    with pytest.raises(ValueError, match='paper'):
        LiveRequestJson(**{**payload, 'paper_mode': True})


def test_live_strategy_properties_use_distinct_fresh_sources(monkeypatch):
    import jesse.helpers as jh
    from jesse.models import Position
    position = Position({'exchange': SimpleNamespace(type='futures'), 'exchange_name': EXCHANGE,
                         'symbol': 'BTC-USDT', '_funding_rate': .0002,
                         '_funding_rate_timestamp': START, '_next_funding_timestamp': START + 8 * 3_600_000,
                         '_settled_funding_rate': .0001, '_settled_funding_timestamp': START - 8 * 3_600_000,
                         '_settled_funding_observed_at': START, '_open_interest': 1234.5,
                         '_open_interest_timestamp': START})
    monkeypatch.setattr(jh, 'is_live', lambda: True)
    monkeypatch.setattr(jh, 'now_to_timestamp', lambda: START)
    assert position.funding_rate == .0002
    assert position.settled_funding_rate == .0001
    assert position.open_interest == 1234.5
    assert position.open_interest_timestamp == START
    monkeypatch.setattr(jh, 'now_to_timestamp', lambda: START + 90_001)
    assert position.funding_rate is None
    assert position.next_funding_timestamp is None
    assert position.settled_funding_rate is None
    assert position.settled_funding_timestamp is None
    assert position.open_interest is None
    assert position.open_interest_timestamp is None


def test_dashboard_live_start_preserves_saved_feed_optins_and_revalidates_paper(monkeypatch):
    from jesse.controllers import live_controller
    from jesse.enums import live_session_statuses
    from jesse.services.web import LiveRequestJson
    import jesse.helpers as jh
    saved = SimpleNamespace(status=live_session_statuses.DRAFT,
                            state_json={'form': {'config': {'funding': {'mode': 'live'}}}})
    captured = []
    monkeypatch.setattr(jh, 'validate_cwd', lambda: None)
    monkeypatch.setattr(live_controller.live_session_repository, 'get_live_session_by_id', lambda _: saved)
    monkeypatch.setattr(live_controller, '_store_and_start', lambda request, *args: captured.append(request.config))
    payload = dict(id=str(uuid4()), exchange=EXCHANGE, exchange_api_key_id='fake-id',
                   notification_api_key_id='', routes=[{'symbol': 'BTC-USDT', 'timeframe': '1m', 'strategy': 'Test19'}],
                   data_routes=[], config={}, debug_mode=False, paper_mode=False)
    assert live_controller.live(LiveRequestJson(**payload)).status_code == 202
    assert captured[-1]['funding']['mode'] == 'live'
    assert live_controller.live(LiveRequestJson(**{**payload, 'config': {'funding': {'mode': 'disabled'}}})).status_code == 202
    assert captured[-1]['funding']['mode'] == 'disabled'
    with pytest.raises(controller.HTTPException) as error:
        live_controller.live(LiveRequestJson(**{**payload, 'paper_mode': True}))
    assert error.value.status_code == 422
    assert len(captured) == 2  # Invalid paper request did not queue anything.
