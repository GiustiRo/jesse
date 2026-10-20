"""Funding operations go through the same authenticated API as other MCP tools."""

import requests

import jesse.mcp.mcp_config as mcp_config
from .offload import run_blocking
from .services.auth import hash_password


def _request(path: str, payload: dict) -> dict:
    response = requests.post(
        f'{mcp_config.JESSE_API_URL}/funding/{path}', json=payload,
        headers={'Authorization': hash_password(mcp_config.JESSE_PASSWORD)},
        # Multi-year history requires several bounded vendor requests.
        timeout=300,
    )
    if response.status_code >= 400:
        detail = response.json().get('detail', 'Funding API request failed')
        raise ValueError(f'Funding API {response.status_code}: {detail}')
    return response.json()


def register_funding_tools(mcp):
    @mcp.tool()
    async def import_funding(start_date: str, finish_date: str, allow_mark_price_proxy: bool = False) -> dict:
        """Import public Binance USD-M BTC-USDT settled funding, UTC [start,finish).

        Returns an immutable dataset_id and coverage/gap diagnostics. No keys, live
        session or orders. Inspect coverage before research. Opt into a backtest via
        form.config.funding={mode:'historical',dataset_id:'returned digest'}.
        Rates are decimal fractions; mark prices are settlement marks. Other
        instruments and simulated/predicted rates are deliberately unsupported.

        Older Binance rows may omit settlement marks. Default refuses them;
        allow_mark_price_proxy=True explicitly uses hourly mark-candle OPEN as
        an approximation, recorded per event and in dataset metadata.
        """
        return await run_blocking(_request, 'import', {'start_date': start_date, 'finish_date': finish_date,
                                                      'allow_mark_price_proxy': allow_mark_price_proxy})

    @mcp.tool()
    async def get_funding_dataset(dataset_id: str, include_events: bool = False, offset: int = 0, limit: int = 50) -> dict:
        """Read verified metadata; optionally inspect one bounded page of raw settlements.

        include_events=True adds events,total,next_offset (1..500 rows/page).
        This is a research data read, not a promise that future rates were known.
        """
        payload = {'dataset_id': dataset_id}
        if include_events:
            payload.update(include_events=True, offset=offset, limit=limit)
        return await run_blocking(_request, 'dataset', payload)

    @mcp.tool()
    async def list_funding_datasets() -> dict:
        """List local immutable BTC funding snapshots with source, coverage and quality."""
        return await run_blocking(_request, 'datasets', {})

    @mcp.tool()
    async def update_funding_dataset(dataset_id: str, finish_date: str) -> dict:
        """Refresh Binance history to an exclusive UTC finish date, preserving the old ID."""
        return await run_blocking(_request, 'update', {'dataset_id': dataset_id, 'finish_date': finish_date})

    @mcp.tool()
    async def configure_session_market_data(session_id: str, funding: dict | None = None,
                                            open_interest: dict | None = None) -> dict:
        """Configure a BACKTEST DRAFT, never start it. mode=disabled or historical+dataset_id.

        Finished/running sessions are immutable here; copy one to a draft first.
        Config is saved in form.config; normal run_backtest consumes it. Historical
        funding forces exact minute replay even if fast_mode was requested.
        OI is a signal with explicit missing/stale values, not a trading cost.
        BTC funding only: other route symbols require explicit funding.exclude_symbols.
        """
        return await run_blocking(_request, 'session-config', {
            'session_id': session_id, 'funding': funding, 'open_interest': open_interest})

    @mcp.tool()
    async def get_session_funding(session_id: str, live: bool = False, offset: int = 0, limit: int = 50) -> dict:
        """Read funding evidence and one ledger page. Never starts or contacts an account.

        Historical backtests: requested mode vs applied, cashflow, dataset/version,
        settlement ledger and OI metadata. live=True: persisted adapter journal,
        account-scope actual income, estimate freshness, no second wallet debit.
        """
        return await run_blocking(_request, 'live-session' if live else 'session', {
            'session_id': session_id, 'offset': offset, 'limit': limit})

    def oi_request(path: str, payload: dict) -> dict:
        response = requests.post(f'{mcp_config.JESSE_API_URL}/open-interest/{path}', json=payload,
                                 headers={'Authorization': hash_password(mcp_config.JESSE_PASSWORD)}, timeout=300)
        if response.status_code >= 400:
            detail = response.json().get('detail', 'Open-interest API request failed')
            raise ValueError(f'Open-interest API {response.status_code}: {detail}')
        return response.json()

    @mcp.tool()
    async def import_open_interest(start_date: str, finish_date: str) -> dict:
        """Import Binance BTC five-minute OI over UTC [start,finish), recent30days ONLY.

        No account keys. Older windows are refused rather than invented. Original
        publication timestamps are unknown: strategy availability uses the explicit
        six-minute lag assumption. Does not provide causal OI history for2020–25.
        """
        return await run_blocking(oi_request, 'import', {'start_date': start_date, 'finish_date': finish_date})

    @mcp.tool()
    async def list_open_interest_datasets() -> dict:
        """List local OI snapshot coverage and availability assumptions."""
        return await run_blocking(oi_request, 'datasets', {})

    @mcp.tool()
    async def get_open_interest_dataset(dataset_id: str, include_events: bool = False, offset: int = 0, limit: int = 50) -> dict:
        """Read verified OI metadata, optionally a page of observations and availability times."""
        payload = {'dataset_id': dataset_id}
        if include_events:
            payload.update(include_events=True, offset=offset, limit=limit)
        return await run_blocking(oi_request, 'dataset', payload)

    @mcp.tool()
    async def update_open_interest_dataset(dataset_id: str, finish_date: str) -> dict:
        """Append fresh recent OI with conflict checks and preserve the original snapshot."""
        return await run_blocking(oi_request, 'update', {'dataset_id': dataset_id, 'finish_date': finish_date})
