# Jesse bot workspace (Pi 24/7)

This folder is the runnable Jesse **project**. The MIT framework lives in `../jesse/`. Our live adapter lives in `../jesse_live/`.

Do not run `jesse install-live`. Do not set `LICENSE_API_TOKEN`. The dashboard Live tab appears because `import jesse_live` succeeds.

## Layout

- `strategies/Idle` — default strategy: connects, never opens a position
- Add more folders under `strategies/` and pick one in the Live tab
- `.env` — dashboard password, Postgres, Binance SOCKS proxy, optional Discord webhook

## Raspberry Pi 5

```bash
cd /opt/jesse/bot/docker
cp ../.env.example ../.env
# edit PASSWORD, BINANCE_*, DISCORD_*, DASHBOARD_URL
docker compose up -d
```

Dashboard: `http://192.168.1.10:9000`

Then in the UI:

1. Settings / Exchange API Keys — Binance Perpetual Futures
2. Notification API Keys — Discord webhook
3. Live — route `Binance Perpetual Futures` / `BTC-USDT` / timeframe / **Idle**
4. Keep `BINANCE_ALLOW_TRADING=false` until a real strategy is selected

Stop the session or switch to Idle to halt entries.

## Signals

Start on the Live tab loads `strategies/<Name>`. On each heartbeat the adapter calls `should_long` / `should_short`. Idle always returns false. A future strategy in this folder is what produces entries.

Binance authenticated calls leave the Pi through `BINANCE_SOCKS5_PROXY_URL` (DigitalOcean reserved IP whitelist). See `docs/socks-proxy.md`.
