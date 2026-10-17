# SOCKS5 DigitalOcean (validado)

El Droplet FRA1 ya está bien:

- Sale por la Reserved IP `209.38.180.165`
- Binance `fapi` responde HTTP 200
- Dante escucha en el anchor `10.19.0.5:1080` (`internal`/`external` = `10.19.0.5`)
- User SOCKS: `botproxy`

`192.3.13.44` era el **otro VPS**. Mismo puerto 1080, otro user. Binance lo corta con HTTP 451. No usarlo.

En `bot/.env`:

```
BINANCE_ALLOWED_EGRESS_IP=209.38.180.165
BINANCE_SOCKS5_PROXY_URL=socks5h://botproxy:CLAVE@209.38.180.165:1080
BINANCE_PROXY_REQUIRED=true
```

Comprobar desde la Pi:

```bash
curl --proxy "$BINANCE_SOCKS5_PROXY_URL" -4 -sS https://api.ipify.org && echo
curl --proxy "$BINANCE_SOCKS5_PROXY_URL" -4 -sS -D- https://fapi.binance.com/fapi/v1/time -o /dev/null | head
```

Tiene que imprimir `209.38.180.165` y HTTP 200. Recrear el contenedor Jesse después de cambiar el `.env`.
