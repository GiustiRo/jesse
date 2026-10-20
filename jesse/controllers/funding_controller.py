"""Authenticated funding import and snapshot inspection; no exchange credentials."""

from datetime import datetime, timezone
from copy import deepcopy
import json
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
import requests

from jesse.services.auth import require_auth
from jesse.services import funding, open_interest
from jesse.services.market_data_config import validate_session_options
from jesse.models.BacktestSession import BacktestSession, get_backtest_session_by_id
import jesse.helpers as jh


router = APIRouter(prefix='/funding', tags=['Funding'], dependencies=[Depends(require_auth)])
oi_router = APIRouter(prefix='/open-interest', tags=['Open interest'], dependencies=[Depends(require_auth)])


def _timestamp(date: str) -> int:
    return int(datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp() * 1000)


def _call(function, *args):
    try:
        return function(*args)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail='Market dataset not found') from exc
    except (ValueError, KeyError, TypeError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail='Binance market data request failed; no partial snapshot published') from exc


class ImportFundingRequest(BaseModel):
    start_date: str
    finish_date: str
    allow_mark_price_proxy: bool = False


class FundingDatasetRequest(BaseModel):
    dataset_id: str
    include_events: bool = False
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=50, ge=1, le=500)


class UpdateDatasetRequest(FundingDatasetRequest):
    finish_date: str


class SessionRequest(BaseModel):
    session_id: UUID
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=50, ge=1, le=500)


class SessionConfigRequest(BaseModel):
    session_id: UUID
    funding: dict | None = None
    open_interest: dict | None = None


class ImportOpenInterestRequest(ImportFundingRequest):
    period: str = '5m'
    source: str = 'rest'


@router.post('/import')
def import_history(request: ImportFundingRequest):
    return _call(lambda: funding.import_binance_history(_timestamp(request.start_date), _timestamp(request.finish_date),
                                                       request.allow_mark_price_proxy))


@router.post('/dataset')
def get_dataset(request: FundingDatasetRequest):
    def read():
        data = funding.load_dataset(request.dataset_id)
        result = funding.describe_dataset(request.dataset_id, data)
        if request.include_events:
            page = _page(data['events'], request.offset, request.limit)
            result.update({**{key: value for key, value in page.items() if key != 'ledger'}, 'events': page['ledger']})
        return result
    return _call(read)


@router.post('/datasets')
def datasets():
    return {'datasets': _call(funding.list_datasets)}


@router.post('/update')
def update(request: UpdateDatasetRequest):
    return _call(lambda: funding.update_dataset(request.dataset_id, _timestamp(request.finish_date)))


def _session(session_id: str):
    row = get_backtest_session_by_id(session_id)
    if row is None:
        raise HTTPException(status_code=404, detail='Backtest session not found')
    return row


def _page(rows: list, offset: int, limit: int) -> dict:
    page = rows[offset:offset + limit]
    return {'ledger': page, 'offset': offset, 'limit': limit, 'total': len(rows),
            'next_offset': offset + len(page) if offset + len(page) < len(rows) else None}


@router.post('/session')
def session(request: SessionRequest):
    row = _session(str(request.session_id))
    form = row.state_json.get('form', {})
    config = form.get('config', {})
    metrics = row.metrics_json or {}
    requested = config.get('funding') or {'mode': 'disabled'}
    requested_mode = requested.get('mode', 'disabled')
    # Queue failures can leave metrics from a prior run on this row. Only a
    # finished run using the selected immutable snapshot is evidence of use.
    def current_result(name, options):
        result = metrics.get(name) or {}
        if row.status != 'finished' or result.get('mode') != options.get('mode', 'disabled'):
            return {}
        if options.get('mode') == 'historical' and result.get('dataset_id') != options.get('dataset_id'):
            return {}
        return dict(result)

    data = current_result('funding', requested)
    oi_data = current_result('open_interest', config.get('open_interest') or {'mode': 'disabled'})
    applied = data.get('applied') is True
    status = data.get('status') or ('disabled' if requested_mode == 'disabled' else 'not_applied')
    return {**data, 'session_id': str(row.id), 'session_status': row.status,
            'mode': data.get('mode', requested_mode), 'requested_mode': requested_mode,
            'applied': applied, 'status': status, 'cashflow': data.get('cashflow') if applied else None,
            'event_count': data.get('event_count', 0), 'funding_config': requested,
            'open_interest_config': config.get('open_interest') or {'mode': 'disabled'},
            'route_symbols': sorted({r['symbol'] for r in form.get('routes', []) if 'symbol' in r}),
            'open_interest': oi_data or None,
            **_page(data.get('ledger') or [], request.offset, request.limit)}


@router.post('/session-config')
def session_config(request: SessionConfigRequest):
    row = _session(str(request.session_id))
    if row.status != 'draft':
        raise HTTPException(status_code=409, detail='Only a draft can change market data settings; copy the session first')
    state = deepcopy(row.state_json)
    form = state.setdefault('form', {})
    config = form.setdefault('config', {})
    if request.funding is None and request.open_interest is None:
        raise HTTPException(status_code=400, detail='Provide funding or open_interest settings')
    for name in ('funding', 'open_interest'):
        value = getattr(request, name)
        if value is not None:
            config[name] = value
    _call(validate_session_options, config, form)
    # Compare the prior state as well as status: a concurrent UI edit must not be lost.
    updated = (BacktestSession.update(state=json.dumps(state), updated_at=jh.now_to_timestamp(True))
               .where((BacktestSession.id == row.id) & (BacktestSession.status == 'draft')
                      & (BacktestSession.state == row.state)).execute())
    if updated != 1:
        raise HTTPException(status_code=409, detail='Draft changed concurrently; reload before configuring')
    return {'session_id': str(row.id), 'funding_config': config.get('funding', {'mode': 'disabled'}),
            'open_interest_config': config.get('open_interest', {'mode': 'disabled'}),
            'message': 'Saved to draft form.config. Reload its dashboard tab before running.'}


@router.post('/live-session')
def live_session(request: SessionRequest):
    # Read-only local journal: never creates an exchange client or starts a session.
    from jesse_live.funding import read_live_funding_status
    from jesse.repositories.live_session_repository import get_live_session_by_id
    row = get_live_session_by_id(str(request.session_id))
    if row is None:
        raise HTTPException(status_code=404, detail='Live session not found')
    config = row.state_json.get('form', {}).get('config', {})
    requested_mode = (config.get('funding') or {}).get('mode', 'disabled')
    data = _call(read_live_funding_status, str(request.session_id), True)
    if data.get('mode') == 'disabled' and requested_mode == 'live':
        data.update(mode='live', status='unavailable', cashflow=None)
    return {**data, 'requested_mode': requested_mode, 'session_status': row.status,
            **_page(data.get('ledger') or [], request.offset, request.limit)}


@oi_router.post('/datasets')
def oi_datasets():
    return {'datasets': _call(open_interest.list_datasets)}


@oi_router.post('/import')
def oi_import(request: ImportOpenInterestRequest):
    return _call(lambda: open_interest.import_binance_history(
        _timestamp(request.start_date), _timestamp(request.finish_date), request.period, request.source))


@oi_router.post('/dataset')
def oi_dataset(request: FundingDatasetRequest):
    def read():
        data = open_interest.load_dataset(request.dataset_id)
        result = open_interest.describe_dataset(request.dataset_id, data)
        if request.include_events:
            page = _page(data['observations'], request.offset, request.limit)
            result.update({**{key: value for key, value in page.items() if key != 'ledger'}, 'observations': page['ledger']})
        return result
    return _call(read)


@oi_router.post('/update')
def oi_update(request: UpdateDatasetRequest):
    return _call(lambda: open_interest.update_dataset(request.dataset_id, _timestamp(request.finish_date)))
