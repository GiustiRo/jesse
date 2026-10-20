"""Bounded asynchronous public-data imports; no vendor HTTP or project data."""

import json
import os
from pathlib import Path
import subprocess
import sys
import threading
import time
from uuid import uuid4

import pytest

from jesse.services import market_data_jobs as jobs


NOW = 1_790_000_000_000
DAY = 86_400_000
DATASET = 'a' * 64


@pytest.fixture(autouse=True)
def isolated_jobs(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(jobs, '_now', lambda: NOW)
    yield
    # No daemon may retain a temp-directory lease after this test's cwd changes.
    for thread in list(jobs._threads.values()):
        thread.join(timeout=5)
        assert not thread.is_alive()
    assert jobs._leases == {}


def wait_for(job_id, status='finished'):
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        record = jobs.get_job(job_id)
        if record['status'] not in jobs.ACTIVE_STATUSES:
            assert record['status'] == status, record
            return record
        time.sleep(.01)
    pytest.fail('Market data worker did not finish')


def metadata(**extra):
    return {'dataset_id': DATASET, 'observation_count': 288, 'coverage_complete': True,
            'source': 'binance-public-archive', **extra}


def test_long_import_returns_immediately_and_rejects_another_until_finished(monkeypatch):
    entered, release = threading.Event(), threading.Event()

    def worker(start, finish, period, source, **kwargs):
        assert (start, finish, period, source) == (NOW - 365 * DAY, NOW, '5m', 'archive')
        assert kwargs['allow_archive_assumptions'] is True
        kwargs['progress_callback']({'phase': 'archive', 'source': 'archive', 'fetched_days': 1,
                                     'total_days': 365, 'current_date': '2025-01-01'})
        entered.set()
        assert release.wait(5)
        return metadata()

    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', worker)
    started = time.monotonic()
    result = jobs.start_import(NOW - 365 * DAY, NOW, source='archive', allow_archive_assumptions=True)
    assert time.monotonic() - started < 1
    assert result['status'] == 'queued'
    try:
        assert entered.wait(2)
        running = jobs.get_job(result['job_id'])
        assert running['status'] == 'running'
        assert running['progress']['fetched_days'] == 1
        with pytest.raises(jobs.MarketDataJobConflict):
            jobs.start_import(NOW - DAY, NOW)
    finally:
        release.set()
    completed = wait_for(result['job_id'])
    assert completed['result'] == metadata()
    assert completed['progress']['phase'] == 'complete'
    assert completed['owner_pid'] == os.getpid()
    assert jobs.list_jobs()[0]['job_id'] == result['job_id']


def test_worker_failure_is_persisted_and_does_not_poison_the_next_job(monkeypatch):
    def fail(*args, **kwargs):
        raise ValueError('Archive day failed checksum validation')

    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', fail)
    first = jobs.start_import(NOW - DAY, NOW)
    failed = wait_for(first['job_id'], 'failed')
    assert failed['result'] is None
    assert failed['error'] == {'type': 'ValueError', 'message': 'Archive day failed checksum validation'}
    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', lambda *args, **kwargs: metadata())
    second = jobs.start_import(NOW - DAY, NOW)
    assert wait_for(second['job_id'])['result']['dataset_id'] == DATASET


@pytest.mark.parametrize('options', [
    {'start': NOW, 'finish': NOW}, {'start': True, 'finish': NOW},
    {'start': NOW - DAY, 'finish': NOW + 1}, {'start': -1, 'finish': NOW},
    {'start': NOW - DAY, 'finish': NOW, 'source': 'other'},
    {'start': NOW - DAY, 'finish': NOW, 'period': '1h'},
    {'start': NOW - DAY, 'finish': NOW, 'source': 'archive'},
    {'start': NOW - DAY, 'finish': NOW, 'source': 'auto'},
    {'start': NOW - DAY, 'finish': NOW, 'allow_archive_assumptions': 'true'},
    {'start': NOW - 31 * DAY, 'finish': NOW, 'source': 'rest'},
])
def test_invalid_parameters_fail_before_creating_a_job(monkeypatch, options):
    calls = []
    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', lambda *args, **kwargs: calls.append(args))
    with pytest.raises(ValueError):
        jobs.start_import(**options)
    assert calls == []
    assert jobs.list_jobs() == []


def test_update_validates_identity_without_deserializing_the_archive(monkeypatch):
    path = Path('storage/open-interest') / f'{DATASET}.json'
    path.parent.mkdir(parents=True)
    # Metadata loading belongs to the background provider, not the HTTP thread.
    path.write_text('fake test archive, never parsed by job submission')
    calls = []

    def worker(identifier, finish, progress_callback):
        calls.append((identifier, finish))
        progress_callback({'phase': 'rest', 'processed_buckets': 500, 'total_buckets': 1000})
        return metadata()

    monkeypatch.setattr(jobs.open_interest, 'update_dataset', worker)
    result = jobs.start_update(DATASET, NOW)
    completed = wait_for(result['job_id'])
    assert calls == [(DATASET, NOW)]
    assert completed['operation'] == 'update'
    assert completed['options'] == {'dataset_id': DATASET, 'finish': NOW}
    assert completed['progress']['processed_buckets'] == 500
    with pytest.raises(FileNotFoundError):
        jobs.start_update('b' * 64, NOW)
    with pytest.raises(ValueError):
        jobs.start_update('../escape', NOW)


def test_status_never_returns_observation_arrays_or_unbounded_metadata(monkeypatch):
    result = metadata(observations=[{'x': 1}] * 100_000, details=[{'x': 1}] * 100_000,
                      message='x' * 100_000)
    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', lambda *args, **kwargs: result)
    job = jobs.start_import(NOW - DAY, NOW)
    completed = wait_for(job['job_id'])
    assert 'observations' not in completed['result']
    assert completed['result']['details'] == {'omitted_items': 100_000}
    assert len(json.dumps(completed)) < 5000


def test_progress_is_bounded_and_final_metadata_is_not_replaced_by_progress(monkeypatch):
    def worker(*args, progress_callback, **kwargs):
        progress_callback({'phase': 'archive', 'fetched_days': 2, 'total_days': 3,
                           'observations': list(range(100_000)), 'message': 'x' * 10_000})
        return metadata()

    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', worker)
    completed = wait_for(jobs.start_import(NOW - DAY, NOW)['job_id'])
    assert completed['progress']['fetched_days'] == 2
    assert 'observations' not in completed['progress']
    assert len(completed['progress']['message']) == 2000
    assert completed['result']['dataset_id'] == DATASET


def test_abandoned_running_status_is_interrupted_and_a_new_job_can_run(monkeypatch):
    identity = str(uuid4())
    jobs._write({'schema': 1, 'job_id': identity, 'status': 'running', 'owner_pid': os.getpid(),
                 'owner_token': 'old-process-token', 'created_at': NOW - DAY, 'updated_at': NOW - DAY})
    assert jobs.get_job(identity)['status'] == 'interrupted'
    assert jobs.get_job(identity)['error']['type'] == 'Interrupted'
    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', lambda *args, **kwargs: metadata())
    assert wait_for(jobs.start_import(NOW - DAY, NOW)['job_id'])['status'] == 'finished'


def test_thread_start_failure_releases_the_global_lease(monkeypatch):
    def cannot_start(thread):
        raise RuntimeError('Thread startup failed')

    with monkeypatch.context() as local:
        local.setattr(threading.Thread, 'start', cannot_start)
        with pytest.raises(RuntimeError, match='Thread startup failed'):
            jobs.start_import(NOW - DAY, NOW)
    previous = jobs.list_jobs()
    assert len(previous) == 1 and previous[0]['status'] == 'interrupted'
    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', lambda *args, **kwargs: metadata())
    assert wait_for(jobs.start_import(NOW - DAY, NOW)['job_id'])['status'] == 'finished'


def test_initial_status_write_failure_does_not_start_the_worker_or_retain_a_lease(monkeypatch):
    calls = []
    monkeypatch.setattr(jobs.open_interest, 'import_binance_history', lambda *args, **kwargs: calls.append(args))
    with monkeypatch.context() as local:
        local.setattr(jobs, '_write', lambda record: (_ for _ in ()).throw(OSError('disk full')))
        with pytest.raises(OSError, match='disk full'):
            jobs.start_import(NOW - DAY, NOW)
    assert calls == []
    descriptor = jobs._acquire_lease()
    jobs._release_lease(descriptor)


def test_job_identity_cannot_escape_storage_and_list_limits_are_bounded():
    with pytest.raises(ValueError):
        jobs.get_job('../escape')
    with pytest.raises(ValueError):
        jobs.list_jobs(201)


def test_cross_process_lease_and_restart_interruption(tmp_path):
    root = str(Path(__file__).resolve().parents[1])
    ready = tmp_path / 'ready.json'
    code = '''
import json, pathlib, threading, time
from jesse.services import market_data_jobs as jobs
def work(*args, **kwargs):
    threading.Event().wait(30)
jobs.open_interest.import_binance_history=work
now=int(time.time()*1000)
job=jobs.start_import(now-86400000,now)
pathlib.Path('ready.json').write_text(json.dumps(job))
threading.Event().wait(30)
'''
    environment = {**os.environ, 'PYTHONPATH': root + os.pathsep + os.environ.get('PYTHONPATH', '')}
    child = subprocess.Popen([sys.executable, '-c', code], cwd=tmp_path, env=environment,
                             stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    try:
        deadline = time.monotonic() + 10
        while not ready.exists() and child.poll() is None and time.monotonic() < deadline:
            time.sleep(.02)
        assert ready.exists(), child.stderr.read().decode() if child.poll() is not None else 'Child did not start'
        identity = json.loads(ready.read_text())['job_id']
        assert jobs.get_job(identity)['status'] in jobs.ACTIVE_STATUSES
        with pytest.raises(jobs.MarketDataJobConflict):
            jobs.start_import(NOW - DAY, NOW)
    finally:
        child.terminate()
        child.wait(timeout=5)
        child.stderr.close()
    assert jobs.get_job(identity)['status'] == 'interrupted'
