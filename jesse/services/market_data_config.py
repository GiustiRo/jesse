"""Validate optional historical feeds before queueing a backtest worker."""

from datetime import datetime, timezone
from types import SimpleNamespace

from jesse.services.funding import FundingState
from jesse.services.open_interest import OpenInterestState


def validate_session_options(config: dict, form: dict) -> None:
    options = ((FundingState, config.get('funding')), (OpenInterestState, config.get('open_interest')))
    if all(value is None or (isinstance(value, dict) and value.get('mode') == 'disabled')
           for _, value in options):
        return
    routes = [SimpleNamespace(exchange=form.get('exchange'), symbol=r['symbol']) for r in form['routes']]
    start, finish = (int(datetime.strptime(form[name], '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp() * 1000)
                     for name in ('start_date', 'finish_date'))
    for state_class, value in options:
        try:
            state_class().configure(value, start, finish, routes)
        except FileNotFoundError as exc:
            raise ValueError('Configured market dataset does not exist on this Jesse host') from exc
