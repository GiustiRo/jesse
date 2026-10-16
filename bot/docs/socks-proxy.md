# Binance IP whitelist via SOCKS5

The Pi talks to Binance USD-M futures through a DigitalOcean droplet with a reserved IPv4 (`192.3.13.44`). That IP is the one whitelisted on the API key.

Set in `bot/.env`:

```
BINANCE_SOCKS5_PROXY_URL=socks5h://USER:PASS@192.3.13.44:1080
BINANCE_PROXY_REQUIRED=true
```

The live adapter uses that proxy for REST. If the proxy is required and missing, it refuses to start.

Validated topology (from the legacy bot): Raspberry runs Jesse; the droplet only provides SOCKS5 egress. Dante listens on port 1080. Host default route on the droplet must use the reserved-IP anchor gateway so Binance sees `192.3.13.44`.
