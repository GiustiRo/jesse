# Jesse local para investigación

## Motivo

La Raspberry Pi queda reservada para operar y mantener el dashboard 24/7. Las
optimizaciones, walk-forward y Monte Carlo de velas ejecutan muchos backtests completos:
en la Pi un backtest de seis años tardó unos 37 segundos y un Monte Carlo de 200 escenarios
no completó ninguno después de decenas de minutos. Además, esa carga puede competir con una
sesión live por CPU y memoria.

La PC local tiene más CPU y RAM, permite iterar más rápido y evita afectar el bot. Esta
réplica es **solo para investigación**: no contiene claves de Binance y no se deben iniciar
sesiones live en ella.

## Separación respecto de la Pi

- Compose local: `bot/docker/docker-compose.research.yml`.
- Entorno local: `bot/.env.research` (gitignored), creado desde `.env.research.example`.
- Dashboard: <http://localhost:9200>.
- Postgres: volumen Docker `jesse-research-postgres`.
- La Pi sigue usando `bot/docker/docker-compose.yml`, el puerto 9100 y su propia base.
- El código y `bot/strategies/` se montan desde este checkout, por lo que los cambios locales
  se ven al crear un backtest nuevo.
- No copiar la base completa de la Pi: contiene sesiones y configuración que no hacen falta.
  Solo se exporta la tabla `candle`.

## Estado inicial preparado

El archivo local (gitignored)
`bot/backups/btcusdt-binance-perpetual-2020-2025.sql.gz` contiene únicamente velas
BTC-USDT de Binance Perpetual Futures anteriores a `2026-01-01 00:00 UTC`.
El año 2026 se excluye deliberadamente porque está reservado como out-of-sample.

Dump actual: 149.582.073 bytes; SHA-256
`102d264383da7a964f28b96381fb679867e288b9805ccbcfc7a329a4a68549c0`.

La copia local validada debe contener:

- 3.156.480 velas de 1 minuto.
- Primera vela: `2020-01-01 00:00 UTC`.
- Última vela: `2025-12-31 23:59 UTC`.
- Ningún salto en la serie de 1 hora (validación realizada por `edge_study.py`).

## Uso diario

Desde PowerShell:

```powershell
cd C:\dev\trading\regime-trade\jesse\bot\docker

.\research.ps1 start
.\research.ps1 status
.\research.ps1 logs
.\research.ps1 stop
```

Abrir <http://localhost:9200>. La contraseña local inicial es `local_research`; puede
cambiarse en `bot/.env.research`, recreando después el servicio.

El stack usa el código de este checkout, la imagen oficial de Jesse y TimescaleDB. Omite la
descarga del language server porque no interviene en backtests y puede bloquear un primer
arranque si GitHub está lento.

### Reimportar el dump existente

Solo hacerlo con una base vacía; una segunda importación chocará con las claves primarias.

```powershell
.\research.ps1 import `
  -Dump ..\backups\btcusdt-binance-perpetual-2020-2025.sql.gz
```

Para borrar únicamente la base local y empezar de cero:

```powershell
.\research.ps1 reset
```

El comando exige escribir `DELETE`. Nunca afecta la Pi.

## Renovar las velas desde la Pi

Consultar primero `bot/docs/raspberry-pi.md` para la conexión y las rutas. Ese documento es
local y contiene información sensible: no copiarlo a commits ni repetir credenciales en el
chat.

Reglas para agentes:

1. Verificar que no haya una importación ni mantenimiento de Postgres en curso.
2. Crear un script temporal de Paramiko fuera del repo; no poner la contraseña en comandos,
   archivos versionados ni salida.
3. Exportar **solo** `candle`, filtrando `exchange`, `symbol` y el límite temporal aprobado.
   No hacer un `pg_dump` completo: copiaría sesiones/configuración y podría filtrar claves.
4. Para conservar 2026 como OOS, usar estrictamente:

   ```sql
   WHERE exchange = 'Binance Perpetual Futures'
     AND symbol = 'BTC-USDT'
     AND timestamp < 1767225600000
   ```

5. Transferir el `.sql.gz` a `bot/backups/`, verificar tamaño/contenido, eliminar el archivo
   temporal de la Pi y borrar el script local que incluía la contraseña.
6. Vaciar el volumen local antes de reimportar o implementar una carga idempotente explícita.

El formato usado es una transacción con:

```sql
COPY candle
  (id,timestamp,open,close,high,low,volume,exchange,symbol,timeframe)
FROM stdin;
```

No se exportan `.env`, API keys, sesiones live, órdenes ni trades.

## MCP para agentes locales

El endpoint local es `http://localhost:9200/mcp`. Usa como bearer token el SHA-256 del
`PASSWORD` de `.env.research`. El archivo `.cursor/mcp.json` puede mantener dos servidores:
`jesse-local` para investigación y `jesse-pi` para administración remota. Usar
`jesse-local` por defecto al buscar o validar estrategias; usar la Pi solo cuando la tarea
diga explícitamente desplegar, consultar o administrar la Pi.

Si se cambia `PASSWORD`, regenerar el token sin imprimir la contraseña:

```powershell
python -c "from hashlib import sha256; print(sha256(b'local_research').hexdigest())"
```

Reiniciar Cursor después de cambiar `.cursor/mcp.json`.

## Monte Carlo y capacidad

El tiempo crece aproximadamente con:

`duración del backtest × escenarios ÷ núcleos efectivos`, más el costo de generar velas.

En esta PC Docker dispone de 22 CPU lógicas y 16 GB de RAM. Recomendación:

- Primer diagnóstico: 50 escenarios y 4-6 cores.
- Validación normal: 200 escenarios y 8-12 cores.
- Colas finales: 500-1000 escenarios solo para candidatos ya aprobados.
- Mantener `fast_mode=true` y `moving_block_bootstrap`.
- Ejecutar primero Monte Carlo de trades; es barato y detecta riesgo de secuencia.
- No paralelizar varios Monte Carlo grandes con optimizaciones.

Medir una corrida real antes de estimar tiempos. Si `completed_scenarios` sigue en cero más
de dos veces la duración esperada de un backtest por tanda, revisar logs, memoria de Docker y
CPU; no dejar un proceso indefinidamente en la Pi.

## Flujo recomendado de investigación

1. Investigación/calibración exclusivamente con 2020-2025.
2. Walk-forward por año y estabilidad de parámetros vecinos.
3. Costos realistas: fee taker VIP0 con BNB `0.00045`; no asumir maker sin modelar fills.
4. Monte Carlo de trades y luego de velas en la PC.
5. Congelar estrategia y criterios antes de mirar 2026.
6. El usuario ejecuta la validación 2026 una sola vez.
7. Solo después, sincronizar el archivo de estrategia a la Pi y considerar paper/live.

La configuración live de la Pi y la base local son independientes. No copiar volúmenes,
`.env` ni sesiones entre ambas.
