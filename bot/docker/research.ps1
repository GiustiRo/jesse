param(
    [ValidateSet("start", "stop", "status", "logs", "import", "reset")]
    [string]$Action = "status",
    [string]$Dump = ""
)

$ErrorActionPreference = "Stop"
$DockerDir = $PSScriptRoot
$BotDir = Split-Path $DockerDir -Parent
$EnvFile = Join-Path $BotDir ".env.research"
$ExampleEnv = Join-Path $BotDir ".env.research.example"
$ComposeFile = Join-Path $DockerDir "docker-compose.research.yml"

if (-not (Test-Path $EnvFile)) {
    Copy-Item $ExampleEnv $EnvFile
    Write-Host "Created $EnvFile from the safe research template."
}

function Compose {
    docker compose --env-file $EnvFile -f $ComposeFile @args
    if ($LASTEXITCODE -ne 0) {
        throw "docker compose failed with exit code $LASTEXITCODE"
    }
}

switch ($Action) {
    "start" {
        Compose up -d
        Write-Host "Research dashboard: http://localhost:9200"
    }
    "stop" {
        Compose stop
    }
    "status" {
        Compose ps
    }
    "logs" {
        Compose logs --tail 100 jesse
    }
    "import" {
        if (-not $Dump -or -not (Test-Path $Dump)) {
            throw "Pass -Dump <path-to-candles.sql.gz>."
        }
        Compose up -d
        $resolvedDump = (Resolve-Path $Dump).Path
        Write-Host "Importing 2020-2025 candle data. Existing matching rows are not expected."
        docker compose --env-file $EnvFile -f $ComposeFile cp $resolvedDump postgres:/tmp/candles.sql.gz
        if ($LASTEXITCODE -ne 0) {
            throw "Could not copy the candle dump into Postgres."
        }
        docker compose --env-file $EnvFile -f $ComposeFile exec -T postgres `
            sh -c "gzip -dc /tmp/candles.sql.gz | psql -v ON_ERROR_STOP=1 -U jesse_research -d jesse_research; result=`$?; rm -f /tmp/candles.sql.gz; exit `$result"
        if ($LASTEXITCODE -ne 0) {
            throw "Candle import failed with exit code $LASTEXITCODE"
        }
    }
    "reset" {
        $answer = Read-Host "Delete the entire local research database volume? Type DELETE"
        if ($answer -ne "DELETE") {
            Write-Host "Cancelled."
            exit 0
        }
        Compose down -v
    }
}
