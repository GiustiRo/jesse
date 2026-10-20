"""Opt-in live market inputs and a durable, account-scoped funding audit journal.

Binance already books funding in wallet balance. The journal never debits the
wallet, scales an account payment by allocation, or invents per-strategy attribution.
"""

from __future__ import annotations

from copy import deepcopy
from decimal import Decimal
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import tempfile
import time
from uuid import UUID


EXCHANGE = 'Binance Perpetual Futures'
POLL_MS = 30_000
INCOME_POLL_MS = 60_000
STALE_MS = 90_000
# Re-read the retained window to catch delayed venue income postings. Binance
# exposes only three calendar months; 89 days fits even a non-leap February.
RETENTION_MS = 89 * 86_400_000


def feature_mode(options: dict | None, name: str) -> str:
    if options is None:
        return 'disabled'
    if not isinstance(options, dict) or options.get('mode') not in {'disabled', 'live'}:
        raise ValueError(f'{name}.mode must be disabled or live in the live adapter')
    return options['mode']


def validate_live_features(conf: dict | None, trading_mode: str, exchange: str, routes: list) -> tuple[bool, bool]:
    conf = conf or {}
    funding = feature_mode(conf.get('funding'), 'funding') == 'live'
    interest = feature_mode(conf.get('open_interest'), 'open_interest') == 'live'
    if funding or interest:
        # Paper funding must use simulated position sizes and a simulated wallet.
        # Reading a real account's payments would silently misstate paper PNL.
        if trading_mode != 'livetrade':
            raise ValueError('Live funding/open-interest is unavailable in paper mode; use historical backtests')
        if (exchange != EXCHANGE or not routes
                or any(route.get('symbol') != 'BTC-USDT' for route in routes)):
            raise ValueError('Live funding/open-interest currently supports Binance USD-M BTC-USDT only')
    return funding, interest


def _journal_path(session_id: str) -> Path:
    # A session ID is a storage identity, never an assistant-provided file path.
    identity = str(UUID(str(session_id)))
    return Path('storage/live-funding') / f'{identity}.json'


def _write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, mode='w', encoding='utf-8', delete=False) as file:
            temporary = file.name
            json.dump(payload, file, allow_nan=False, sort_keys=True, separators=(',', ':'))
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def read_live_funding_status(session_id: str, include_ledger: bool = False) -> dict:
    path = _journal_path(session_id)
    if not path.exists():
        return {'mode': 'disabled', 'status': 'disabled', 'event_count': 0,
                'cashflow': 0.0, 'cashflow_decimal': '0', 'wallet_debit_applied': False}
    payload = json.loads(path.read_text(encoding='utf-8'))
    if payload.get('schema') != 1 or payload.get('session_id') != str(UUID(str(session_id))):
        raise ValueError('Invalid live funding journal')
    result = dict(payload['funding'])
    result['open_interest'] = dict(payload['open_interest'])
    result['entry_cancellations'] = payload.get('entry_cancellations', {})
    result['position_reconciliation'] = payload.get('position_reconciliation')
    now = int(time.time() * 1000)
    for state in (result, result['open_interest']):
        if state.get('status') == 'ready' and not LiveFunding._fresh(state.get('observed_at'), now):
            state['status'] = 'stale'
    if (result.get('status') == 'ready'
            and (not LiveFunding._fresh(result.get('last_reconciled_at'), now)
                 or result.get('next_funding_timestamp', 0) <= now)):
        result['status'] = 'stale'
    if include_ledger:
        result['ledger'] = payload['ledger']
    return result


class LiveFunding:
    """Resume audit data only for the same account and the same feature modes.

    Changing modes needs a new session identity. This does not restore ownership
    of exchange positions/orders: the live adapter separately requires a clean,
    flat one-way account symbol before startup.
    """
    def __init__(self, session_id: str, started_at: int, funding: bool, open_interest: bool,
                 account_key: str = ''):
        self.path = _journal_path(session_id)
        self.enabled = funding
        self.interest_enabled = open_interest
        self.account_fingerprint = sha256(account_key.encode()).hexdigest() if account_key else None
        self.payload = {
            'schema': 1, 'session_id': str(UUID(str(session_id))), 'started_at': int(started_at),
            'account_fingerprint': self.account_fingerprint, 'ledger': [],
            'entry_cancellations': {'pending_count': 0, 'canceled_count': 0, 'race_fill_count': 0, 'errors': []},
            'funding': {'mode': 'live' if funding else 'disabled',
                        'status': 'initializing' if funding else 'disabled',
                        'source': 'binance-usdm', 'rate_kind': 'estimate',
                        'rate_decimal': None, 'mark_price': None, 'next_funding_timestamp': None,
                        'settled_rate_decimal': None, 'settled_funding_timestamp': None,
                        'observed_at': None, 'last_reconciled_at': None, 'event_count': 0,
                        'cashflow': 0.0, 'cashflow_decimal': '0', 'currency': 'USDT',
                        'account_scope': True, 'wallet_debit_applied': False, 'error': None},
            'open_interest': {'mode': 'live' if open_interest else 'disabled',
                              'status': 'initializing' if open_interest else 'disabled',
                              'source': 'binance-usdm', 'value': None, 'observed_at': None,
                              'units': 'BTC', 'error': None},
        }
        if self.path.exists():
            old = json.loads(self.path.read_text(encoding='utf-8'))
            if old.get('schema') != 1 or old.get('session_id') != self.payload['session_id']:
                raise ValueError('Invalid live funding journal')
            if old.get('account_fingerprint') != self.account_fingerprint:
                raise ValueError('Live funding journal belongs to another account')
            if (old.get('funding', {}).get('mode') != self.payload['funding']['mode']
                    or old.get('open_interest', {}).get('mode') != self.payload['open_interest']['mode']):
                raise ValueError('Live input configuration changed; create a new session instead of rewriting its audit history')
            # Retain the original start and transactions when a process resumes.
            self.payload['started_at'] = old['started_at']
            self.payload['ledger'] = old['ledger']
            self.payload['entry_cancellations'] = old.get('entry_cancellations', self.payload['entry_cancellations'])
            self.payload['funding']['last_reconciled_at'] = old['funding'].get('last_reconciled_at')
            self._totals(self.payload)
        self._last_public = -POLL_MS
        self._last_interest = -POLL_MS
        self._last_income = -INCOME_POLL_MS
        self._errors = {'funding': None, 'open_interest': None, 'income': None}
        self._persisted = None

    @staticmethod
    def _totals(payload: dict):
        total = sum((Decimal(row['cashflow_decimal']) for row in payload['ledger']), Decimal(0))
        payload['funding'].update(event_count=len(payload['ledger']), cashflow=float(total),
                                  cashflow_decimal=str(total))

    def _save(self, payload: dict):
        # Publish in-memory progress only after the atomic durable write succeeds.
        _write(self.path, payload)
        self.payload = payload
        self._persisted = deepcopy(payload)

    @staticmethod
    def _clear(position, interest: bool = False):
        if interest:
            position._open_interest = None
            position._open_interest_timestamp = None
        else:
            position._funding_rate = None
            position._next_funding_timestamp = None
            position._funding_rate_timestamp = None
            position._mark_price = None
            position._settled_funding_rate = None
            position._settled_funding_timestamp = None
            position._settled_funding_observed_at = None

    @staticmethod
    def _fresh(observed: int | None, now: int) -> bool:
        # A small positive clock skew is tolerated; stale or wildly future data
        # cannot drive entries. The client also synchronizes the Binance clock.
        return observed is not None and -5_000 <= now - observed <= STALE_MS

    def _refresh_public(self, client, position, now: int):
        row = client.premium_index('BTC-USDT')
        if not isinstance(row, dict) or row.get('symbol') != 'BTCUSDT':
            raise ValueError('Unexpected Binance premium-index instrument')
        rate, mark = float(row['lastFundingRate']), float(row['markPrice'])
        observed, next_time = int(row['time']), int(row['nextFundingTime'])
        if not math.isfinite(rate) or not math.isfinite(mark) or mark <= 0:
            raise ValueError('Invalid funding rate or mark price')
        if not self._fresh(observed, now) or next_time <= now:
            raise ValueError('Stale Binance funding observation')
        history = client.latest_funding_settlements('BTC-USDT')
        if not isinstance(history, list) or not history:
            raise ValueError('Missing final Binance funding settlement')
        settled = {}
        for item in history:
            stamp, final_rate = int(item['fundingTime']), float(item['fundingRate'])
            if (item.get('symbol') != 'BTCUSDT' or item.get('rateType', 'Regular') != 'Regular'
                    or not math.isfinite(final_rate) or stamp < 0 or stamp > now):
                raise ValueError('Invalid final Binance funding settlement')
            if stamp in settled and settled[stamp] != final_rate:
                raise ValueError('Conflicting final Binance funding settlements')
            # Match historical strategy availability: final rates become usable
            # at the next minute boundary, never in their settlement callback.
            if stamp - stamp % 60_000 + 60_000 <= now:
                settled[stamp] = final_rate
        if not settled:
            raise ValueError('No final funding settlement has passed its publication delay')
        settled_at = max(settled)
        settled_rate = settled[settled_at]
        updated = deepcopy(self.payload)
        updated['funding'].update(rate_decimal=rate, mark_price=mark,
                                  next_funding_timestamp=next_time, observed_at=observed,
                                  settled_rate_decimal=settled_rate, settled_funding_timestamp=settled_at,
                                  error=None)
        self._save(updated)
        position._funding_rate, position._mark_price = rate, mark
        position._next_funding_timestamp = next_time
        position._funding_rate_timestamp = observed
        position._settled_funding_rate = settled_rate
        position._settled_funding_timestamp = settled_at
        position._settled_funding_observed_at = now

    def _refresh_interest(self, client, position, now: int):
        row = client.open_interest('BTC-USDT')
        if not isinstance(row, dict) or row.get('symbol') != 'BTCUSDT':
            raise ValueError('Unexpected Binance open-interest instrument')
        value, observed = float(row['openInterest']), int(row['time'])
        if not math.isfinite(value) or value < 0 or not self._fresh(observed, now):
            raise ValueError('Invalid or stale Binance open-interest observation')
        updated = deepcopy(self.payload)
        updated['open_interest'].update(value=value, observed_at=observed, status='ready', error=None)
        self._save(updated)
        position._open_interest, position._open_interest_timestamp = value, observed

    def _income_rows(self, client, start: int, finish: int) -> list[dict]:
        rows = client.funding_income('BTC-USDT', start, finish)
        if not isinstance(rows, list):
            raise ValueError('Unexpected Binance funding income response')
        if len(rows) < 1000:
            return rows
        # No ordering or page parameter is guaranteed by this endpoint. Bisect
        # inclusive time windows to exhaust dense responses without losing ties.
        if start >= finish:
            raise ValueError('Funding income exceeds endpoint capacity at one timestamp')
        middle = (start + finish) // 2
        return self._income_rows(client, start, middle) + self._income_rows(client, middle + 1, finish)

    def _reconcile(self, client, now: int):
        last = self.payload['funding'].get('last_reconciled_at')
        if (last or self.payload['started_at']) < now - RETENTION_MS:
            raise ValueError('Funding reconciliation gap exceeds Binance three-month retention')
        start = max(self.payload['started_at'], now - RETENTION_MS)
        rows = self._income_rows(client, start, now)
        updated = deepcopy(self.payload)
        known = {row['transaction_id']: row for row in updated['ledger']}
        for row in rows:
            stamp = int(row['time'])
            amount = Decimal(str(row['income']))
            transaction = str(row['tranId'])
            if (row.get('incomeType') != 'FUNDING_FEE' or row.get('asset') != 'USDT'
                    or row.get('symbol') != 'BTCUSDT' or not start <= stamp <= now
                    or not transaction.isdigit() or not amount.is_finite()):
                raise ValueError('Invalid funding income instrument, currency, amount or time')
            if not math.isfinite(float(amount)):
                raise ValueError('Funding income exceeds finite accounting range')
            decimal_text = format(amount.normalize(), 'f') if amount != 0 else '0'
            event = {'transaction_id': transaction, 'settled_at': stamp, 'cashflow': float(amount),
                     'cashflow_decimal': decimal_text, 'currency': 'USDT', 'symbol': 'BTC-USDT',
                     'income_type': 'FUNDING_FEE', 'source': 'binance-usdm-income',
                     'account_scope': True, 'wallet_debit_applied': False}
            existing = known.get(transaction)
            if existing is not None and existing != event:
                raise ValueError('Conflicting funding income transaction')
            known[transaction] = event
        updated['ledger'] = sorted(known.values(), key=lambda row: (row['settled_at'], row['transaction_id']))
        updated['funding']['last_reconciled_at'] = now
        self._totals(updated)
        self._save(updated)

    def refresh(self, client, position, now: int) -> bool:
        """Refresh inputs; a failure blocks entries while allowing protective exits."""
        for enabled, key, attribute, cadence, operation in (
            (self.enabled, 'funding', '_last_public', POLL_MS, self._refresh_public),
            (self.interest_enabled, 'open_interest', '_last_interest', POLL_MS, self._refresh_interest),
        ):
            if not enabled:
                continue
            next_due = self.payload[key].get('next_funding_timestamp')
            expired_funding = (key == 'funding' and next_due is not None
                               and getattr(self, attribute) < next_due <= now)
            if now - getattr(self, attribute) >= cadence or expired_funding:
                try:
                    operation(client, position, now)
                    self._errors[key] = None
                except Exception as exc:
                    # Vendor HTTP errors may contain request details; persist a
                    # bounded category instead of API credentials or response text.
                    self._errors[key] = str(exc) if isinstance(exc, ValueError) else type(exc).__name__
                    self._clear(position, interest=key == 'open_interest')
                setattr(self, attribute, now)
            observed = self.payload[key].get('observed_at')
            if self._errors[key] is None:
                self.payload[key]['status'] = 'ready' if self._fresh(observed, now) else 'stale'
                if self.payload[key]['status'] != 'ready':
                    self._clear(position, interest=key == 'open_interest')
        if self.enabled and now - self._last_income >= INCOME_POLL_MS:
            try:
                self._reconcile(client, now)
                self._errors['income'] = None
            except Exception as exc:
                self._errors['income'] = str(exc) if isinstance(exc, ValueError) else type(exc).__name__
            self._last_income = now
        for key in ('funding', 'open_interest'):
            if self.payload[key]['mode'] != 'live':
                continue
            error = self._errors[key] or (self._errors['income'] if key == 'funding' else None)
            self.payload[key]['error'] = error
            if error:
                self.payload[key]['status'] = 'error'
        # Errors/status changes must be visible after a process exits too. A
        # journal failure remains an entry-blocking condition, never a success.
        try:
            if self.payload != self._persisted:
                self._save(deepcopy(self.payload))
        except OSError as exc:
            for key in ('funding', 'open_interest'):
                if self.payload[key]['mode'] == 'live':
                    self.payload[key].update(status='error', error=f'Journal write failed: {type(exc).__name__}')
            self._clear(position)
            self._clear(position, interest=True)
        return self.ready

    @property
    def ready(self) -> bool:
        return all(self.payload[key]['status'] == 'ready'
                   for key in ('funding', 'open_interest') if self.payload[key]['mode'] == 'live')

    def snapshot(self) -> dict:
        return deepcopy(self.payload['funding']) | {
            'entry_cancellations': deepcopy(self.payload['entry_cancellations']),
            'position_reconciliation': deepcopy(self.payload.get('position_reconciliation')),
        }

    def interest_snapshot(self) -> dict:
        return deepcopy(self.payload['open_interest']) | {'entry_cancellations': deepcopy(self.payload['entry_cancellations'])}

    def record_entry_cancellations(self, result: dict):
        """Keep unresolved venue cancellations entry-blocking after feeds recover."""
        updated = deepcopy(self.payload)
        previous = updated['entry_cancellations']
        updated['entry_cancellations'] = dict(result)
        for count in ('canceled_count', 'race_fill_count'):
            updated['entry_cancellations'][count] += previous.get(count, 0)
        if updated != self.payload:
            self._save(updated)

    def record_position_status(self, state: dict):
        previous = self.payload.get('position_reconciliation') or {}
        old_values = {key: value for key, value in previous.items() if key != 'observed_at'}
        new_values = {key: value for key, value in state.items() if key != 'observed_at'}
        if (old_values == new_values
                and state.get('observed_at', 0) - previous.get('observed_at', 0) < POLL_MS):
            # Persist immediately on meaningful changes; steady one-second REST
            # heartbeats need not fsync an SD card on every live-loop tick.
            return
        updated = deepcopy(self.payload)
        updated['position_reconciliation'] = deepcopy(state)
        self._save(updated)
