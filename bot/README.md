# Jesse bot workspace (Pi 24/7)

This folder is the runnable Jesse **project**. The MIT framework lives in `../jesse/`. Our live adapter lives in `../jesse_live/`.

Do not run `jesse install-live`. Do not set `LICENSE_API_TOKEN`. The dashboard Live tab appears because `import jesse_live` succeeds.

## Layout

- `strategies/Idle` — default strategy: connects, never opens a position
- `strategies/TemaTrendFollowing` — Saleh TEMA trend strategy (needs a 4h data route; the live adapter adds it)
- Add more folders under `strategies/` and pick one in the Live tab
- `.env` — dashboard password, Postgres, Binance SOCKS proxy, optional Discord webhook

## Raspberry Pi 5

```bash
cd /opt/jesse/bot/docker
cp ../.env.example ../.env
# edit PASSWORD, BINANCE_*, DISCORD_*, DASHBOARD_URL
docker compose up -d
```

Dashboard: `http://192.168.1.10:9100` (host 9100 because Portainer already uses 9000)

SSH, passwords, and Pi paths for another agent: `docs/raspberry-pi.md` (local file, gitignored).

Password lives in `.env` (`PASSWORD=`). There is no change-password screen; edit `.env` and recreate the container.

## Local research replica

Run backtests, optimizations, walk-forward and Monte Carlo on the desktop instead of loading
the Pi. The isolated research stack uses port 9200, contains no exchange credentials and has
its own Postgres volume:

```powershell
cd bot\docker
.\research.ps1 start
```

Setup, candle synchronization, MCP routing and the reason for this separation are documented
in `docs/local-research.md`.

Then in the UI:

1. Settings / Exchange API Keys — Binance Perpetual Futures
2. Notification API Keys — Discord webhook
3. Import Candles — `Binance Perpetual Futures` / `BTC-USDT` (hyphen, not `BTCUSD`). 15m and 1D are both native Binance timeframes.
4. Live — same exchange / `BTC-USDT` / `15m` or `1D` / **TemaTrendFollowing**, then Start. The adapter also loads 4h candles for the long-term TEMA.

Selecting a strategy in the Strategies tab does **not** start trading. Live Start is what runs the adapter.

Arming is not an env var. The red **ARMAS** sidebar tab (password = dashboard `PASSWORD`) has two switches, both default on, applied without recreating the container:

- **Operar** — off pauses new strategy signals; the live session stays up
- **Órdenes reales** — off is dry-run (no Binance orders)

`BINANCE_ALLOCATION_PCT=10` is the slice of the USDT futures wallet the strategy sees as `available_margin`. TemaTrendFollowing then risks 3% of that slice (and multiplies qty by 3). It is not a 10% notional slider.

Massive is only for stocks/FX/indices. Crypto candles come from Binance; no Massive key needed.

Stop the session or switch to Idle to halt entries.

## Signals

Start on the Live tab loads `strategies/<Name>`. On each closed trading candle the adapter runs `Strategy._execute`. Idle never enters.

Binance calls leave the Pi through `BINANCE_SOCKS5_PROXY_URL`. The address Binance must see is the Reserved IP `209.38.180.165`. See `docs/socks-proxy.md`.
