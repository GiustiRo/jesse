"""Durable, single-worker OI downloads without tying a job to an HTTP request.

Only public Binance data functions run here. A daemon thread cannot outlive its
Jesse process. An OS file lease prevents duplicate imports across API processes;
abandoned running records become interrupted on the next read or submission.
"""

from copy import deepcopy
import json
import math
import os
from pathlib import Path
import tempfile
import threading
import time
from typing import Callable
from uuid import UUID, uuid4

from jesse.services import open_interest

if os.name == 'nt':
    import msvcrt
else:
    import fcntl


class MarketDataJobConflict(RuntimeError):
    """Another OI import/update already owns this project's vendor-data lease."""


ACTIVE_STATUSES = {'queued', 'running'}
# Progress is metadata, not observations. These bounds keep status polls small
# even if a future provider accidentally returns its entire series in a result.
MAX_RECORD_METADATA_BYTES = 32 * 1024
PROGRESS_INTERVAL_SECONDS = 1.0
_OWNER_TOKEN = str(uuid4())
_guard = threading.RLock()
_threads: dict[str, threading.Thread] = {}
_leases: dict[str, int] = {}


def _root() -> Path:
    return Path('storage/open-interest/jobs')


def _path(job_id: str) -> Path:
    try:
        identity = str(UUID(str(job_id)))
    except (ValueError, AttributeError, TypeError) as exc:
        raise ValueError('Market data job ID must be a UUID') from exc
    return _root() / f'{identity}.json'


def _now() -> int:
    return time.time_ns() // 1_000_000


def _write(record: dict) -> None:
    path = _path(record['job_id'])
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, mode='w', encoding='utf-8', delete=False) as file:
            temporary = file.name
            json.dump(record, file, allow_nan=False, sort_keys=True, separators=(',', ':'))
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def _read(job_id: str) -> dict:
    record = json.loads(_path(job_id).read_text(encoding='utf-8'))
    if record.get('job_id') != str(UUID(str(job_id))) or record.get('schema') != 1:
        raise ValueError('Invalid market data job record')
    return record


def _acquire_lease() -> int:
    _root().mkdir(parents=True, exist_ok=True)
    descriptor = os.open(_root() / '.active.lock', os.O_CREAT | os.O_RDWR, 0o600)
    os.set_inheritable(descriptor, False)
    try:
        if os.name == 'nt':
            if os.fstat(descriptor).st_size == 0:
                os.write(descriptor, b' ')
            os.lseek(descriptor, 0, os.SEEK_SET)
            msvcrt.locking(descriptor, msvcrt.LK_NBLCK, 1)
        else:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as exc:
        os.close(descriptor)
        if exc.errno in (11, 13, 35, 36):
            raise MarketDataJobConflict('Another open-interest import/update is running') from exc
        raise
    return descriptor


def _release_lease(descriptor: int) -> None:
    # Closing the owning descriptor releases flock/byte-range locks. Explicit
    # unlocks are avoided because a fork may share the underlying file identity.
    os.close(descriptor)


def _after_fork_child() -> None:
    global _guard, _OWNER_TOKEN
    # Backtest children must not keep their parent's import lease alive after a
    # server crash. A close in the child leaves the live parent's lease intact.
    for descriptor in _leases.values():
        os.close(descriptor)
    _leases.clear()
    _threads.clear()
    _guard = threading.RLock()
    _OWNER_TOKEN = str(uuid4())


def _before_fork() -> None:
    _guard.acquire()


def _after_fork_parent() -> None:
    _guard.release()


if hasattr(os, 'register_at_fork'):
    os.register_at_fork(before=_before_fork, after_in_parent=_after_fork_parent,
                        after_in_child=_after_fork_child)


def _interrupted(record: dict) -> dict:
    updated = record | {
        'status': 'interrupted', 'updated_at': _now(), 'finished_at': _now(),
        'error': {'type': 'Interrupted', 'message': 'Jesse stopped before this import recorded completion; start a new job to retry'},
    }
    _write(updated)
    return updated


def _refresh_ownership(record: dict) -> dict:
    if record['status'] not in ACTIVE_STATUSES:
        return record
    thread = _threads.get(record['job_id'])
    if record.get('owner_token') == _OWNER_TOKEN and thread is not None and thread.is_alive():
        return record
    try:
        descriptor = _acquire_lease()
    except MarketDataJobConflict:
        try:
            owner = json.loads((_root() / '.active.lock').read_text(encoding='utf-8'))
        except (ValueError, OSError):
            # A different process may be publishing its lease identity now.
            # Retry on the next poll instead of interrupting a live worker.
            return record
        if owner.get('job_id') == record['job_id'] and owner.get('owner_token') == record.get('owner_token'):
            return record
        return _interrupted(record)
    else:
        try:
            return _interrupted(record)
        finally:
            _release_lease(descriptor)


def get_job(job_id: str) -> dict:
    with _guard:
        return deepcopy(_refresh_ownership(_read(job_id)))


def list_jobs(limit: int = 50) -> list[dict]:
    if type(limit) is not int or not 1 <= limit <= 200:
        raise ValueError('Job list limit must be between 1 and 200')
    with _guard:
        paths = sorted(_root().glob('*.json'), key=lambda path: path.stat().st_mtime, reverse=True)
        return [deepcopy(_refresh_ownership(_read(path.stem))) for path in paths[:limit]]


def _metadata(value: dict) -> dict:
    if not isinstance(value, dict):
        raise ValueError('Market data worker must return metadata as an object')
    def bounded(item, depth=0):
        if item is None or type(item) in (bool, int, float):
            return item
        if isinstance(item, str):
            return item[:2000]
        if depth >= 2:
            return {'metadata_omitted': True}
        if isinstance(item, dict):
            return {str(key)[:100]: bounded(child, depth + 1) for key, child in list(item.items())[:40]}
        if isinstance(item, (list, tuple)):
            return [bounded(child, depth + 1) for child in item[:20]] if len(item) <= 20 else {'omitted_items': len(item)}
        raise ValueError('Market data metadata must be JSON serializable')

    summary = {key: bounded(item) for key, item in value.items()
               if key not in {'observations', 'events', 'ledger', 'rows'}}
    encoded = json.dumps(summary, allow_nan=False)
    if len(encoded.encode('utf-8')) > MAX_RECORD_METADATA_BYTES:
        summary = {key: bounded(value[key]) for key in ('dataset_id', 'source', 'start', 'finish', 'observation_count',
                                                       'coverage_complete', 'status') if key in value}
        summary['metadata_truncated'] = True
        summary['details_tool'] = 'get_open_interest_dataset'
    return summary


def _progress(value: dict) -> dict:
    if not isinstance(value, dict):
        raise ValueError('Market data progress must be an object')
    accepted = {}
    for key in ('phase', 'source', 'fetched_days', 'total_days', 'current_date',
                'processed_buckets', 'total_buckets', 'message'):
        item = value.get(key)
        if item is None or type(item) in (bool, int) or (isinstance(item, float) and math.isfinite(item)):
            accepted[key] = item
        elif isinstance(item, str):
            accepted[key] = item[:2000]
    return accepted


def _run(job_id: str, operation: Callable[[Callable[[dict], None]], dict], descriptor: int) -> None:
    last_progress_time = 0.0
    last_phase = None

    def progress(value: dict):
        nonlocal last_progress_time, last_phase
        data = _progress(value)
        now = time.monotonic()
        if now - last_progress_time < PROGRESS_INTERVAL_SECONDS and data.get('phase') == last_phase:
            return
        with _guard:
            record = _read(job_id)
            _write(record | {'progress': data, 'updated_at': _now()})
        last_progress_time, last_phase = now, data.get('phase')

    try:
        with _guard:
            record = _read(job_id)
            _write(record | {'status': 'running', 'updated_at': _now()})
        result = _metadata(operation(progress))
        with _guard:
            record = _read(job_id)
            _write(record | {'status': 'finished', 'result': result, 'updated_at': _now(),
                             'finished_at': _now(), 'progress': record['progress'] | {'phase': 'complete'}})
    except Exception as exc:
        with _guard:
            record = _read(job_id)
            _write(record | {'status': 'failed', 'updated_at': _now(), 'finished_at': _now(),
                             'error': {'type': type(exc).__name__, 'message': str(exc)[:2000]}})
    finally:
        with _guard:
            _threads.pop(job_id, None)
            _leases.pop(job_id, None)
            _release_lease(descriptor)


def _start(operation_name: str, options: dict, operation: Callable[[Callable[[dict], None]], dict]) -> dict:
    with _guard:
        descriptor = _acquire_lease()
        job_id = str(uuid4())
        record = {'schema': 1, 'job_id': job_id, 'status': 'queued', 'operation': operation_name,
                  'options': options, 'progress': {'phase': 'queued'}, 'result': None, 'error': None,
                  'created_at': _now(), 'updated_at': _now(), 'finished_at': None,
                  'owner_pid': os.getpid(), 'owner_token': _OWNER_TOKEN}
        try:
            # Owning the lease proves every prior running record is abandoned.
            for path in _root().glob('*.json'):
                previous = _read(path.stem)
                if previous['status'] in ACTIVE_STATUSES:
                    _interrupted(previous)
            identity = json.dumps({'job_id': job_id, 'owner_pid': os.getpid(), 'owner_token': _OWNER_TOKEN}).encode()
            os.lseek(descriptor, 0, os.SEEK_SET)
            os.ftruncate(descriptor, 0)
            os.write(descriptor, identity)
            os.fsync(descriptor)
            _write(record)
            thread = threading.Thread(target=_run, args=(job_id, operation, descriptor),
                                      name=f'oi-import-{job_id}', daemon=True)
            _threads[job_id], _leases[job_id] = thread, descriptor
            thread.start()
        except Exception:
            _threads.pop(job_id, None)
            _leases.pop(job_id, None)
            _release_lease(descriptor)
            raise
        return deepcopy(record)


def _validate_range(start: int, finish: int) -> None:
    if type(start) is not int or type(finish) is not int or not 0 <= start < finish <= _now():
        raise ValueError('Expected a nonempty past UTC millisecond interval')


def start_import(start: int, finish: int, period: str = '5m', source: str = 'rest',
                 allow_archive_assumptions: bool = False) -> dict:
    _validate_range(start, finish)
    if period != '5m' or source not in {'rest', 'archive', 'auto'}:
        raise ValueError('OI jobs support five-minute rest, archive or auto sources only')
    if type(allow_archive_assumptions) is not bool:
        raise ValueError('allow_archive_assumptions must be a boolean')
    if source in {'archive', 'auto'} and not allow_archive_assumptions:
        raise ValueError('Archive imports require explicit allow_archive_assumptions=true consent')
    if source == 'rest' and start < _now() - open_interest.REST_RETENTION_MS:
        raise ValueError('Binance OI REST covers only the latest 30 days')
    options = {'start': start, 'finish': finish, 'period': period, 'source': source,
               'allow_archive_assumptions': allow_archive_assumptions}
    return _start('import', options, lambda callback: open_interest.import_binance_history(
        start, finish, period, source, allow_archive_assumptions=allow_archive_assumptions,
        progress_callback=callback))


def start_update(dataset_id: str, finish: int) -> dict:
    # Do not deserialize years of observations in the request thread. The worker
    # validates their contents and extension range before downloading anything.
    path = open_interest._path(dataset_id)
    if not path.is_file():
        raise FileNotFoundError('Open-interest dataset not found')
    if type(finish) is not int or not 0 < finish <= _now():
        raise ValueError('Updated finish must be a past UTC millisecond timestamp')
    return _start('update', {'dataset_id': dataset_id, 'finish': finish},
                  lambda callback: open_interest.update_dataset(dataset_id, finish, progress_callback=callback))
