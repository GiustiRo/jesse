# Live adapter (this fork)

`jesse_live/` is our open-source live hook so the Jesse dashboard Live tab works without the commercial plugin.

Runnable 24/7 project: [`bot/README.md`](bot/README.md)

- Do not run `jesse install-live`
- Do not set `LICENSE_API_TOKEN` (the dashboard reports a local lifetime plan)
- Strategies: `bot/strategies/Idle` (no entries) and `bot/strategies/TemaTrendFollowing`
- Dashboard password: `PASSWORD` in `bot/.env`
- Binance whitelist / expected egress: Reserved IP `209.38.180.165`. Dante still listens on original IPv4 `192.3.13.44` (see `bot/docs/socks-proxy.md`).
- Real orders are armed from the red **ARMAS** sidebar tab (password = dashboard `PASSWORD`). Defaults on.
- Wallet slice: `BINANCE_ALLOCATION_PCT` (default 10)
