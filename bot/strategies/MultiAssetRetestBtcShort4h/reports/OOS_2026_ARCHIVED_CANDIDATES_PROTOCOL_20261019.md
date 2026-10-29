# Comparación ampliada2026 — lista congelada antes de nuevos resultados

Usuario solicita probar N204 y otras candidatas que quedaron en el camino. Lista fijada por evidencia de desarrollo2020–2025: N204 referencia; N503 (ER0<ER≤1/3, mejora nominal pero regularidadC insuficiente); P604 (liberar suplemento tras confirmación de precio, mejora nominal pequeña y regularidadC insuficiente); C504 (recuperación bajoAcongelado, mejora nominal marginal pero falla regularidad trimestralB); K1005 (trailing persistente tras1R, mayor neto nominal sin validación propia completa de costes). No se añade ninguna receta tras ver nuevos resultados. Y902 se mantiene excluida por instrucción previa. Controles económicos duplicados y variantes claramente inferiores no se presentan como candidatas adicionales.

## Alcance y tratamiento OOS
Las cinco fuentes de señal existían antes de abrir2026. Es una comparación exploratoria ampliada DESPUÉS de observar K1001; no una nueva selección confirmatoria ciega. Probar más candidatas aumenta selección múltiple. Un eventual ganador2026 deberá evaluarse con datos posteriores no usados; no declarar ausencia de sobreajuste. No se retocan señales, stops, targets ni umbrales.

## Matriz fija
20corridas nuevas:5recetas×B/C×fee.00045/.00095porlado. Capital10000USDTcompartido, riesgo objetivo2%trade/6%agregado, isolated3x, cap4.4, buffer90%,reserva.001sizing, warmup240, fastfalse,debugtrue. Ventana2026-01-01 inclusiva→2026-10-19 exclusiva (hasta18octUTC), sin ampliar al nuevo díaUTC. Mismas rutasBTC/PAXG/SPY4h+M1, ordenoriginal. Auxiliares CapitalR12PaxgR2A6 y CapitalR12SpyB/CR2A6 del perfil anterior. N204 reutiliza CapitalR12N204R2A6. N503/P604/C504/K1005 requieren copias con ÚNICOS cambios ejecutables: nombreclase y constantes1%/8%→2%/6%, por perfil humano elegido antes de abrir2026. Sólo comentarios aclaran normalización/cap. Verificar reversibilidad exacta contra snapshots de desarrollo; originales intactos. No barrido de sizing. DatosBTC/PAXG completos y SPXproxy corregido exactamente como K1001, sin reimportar ni modificar datos. Máximo2backtests/1analysis simultáneos.

## Criterios y comparación
Por cada receta, ambas carteras nominales:neto>0,PF≥1.2,DD≥−25%,≥20trades. Estrés:neto>0 en ambas. Informar cumplimiento individual y conjunto, sin flexibilizar puertas. K1001 se reutiliza como comparador en sus4sesiones DEFINITIVAS conPAXG completo, no las4invalidas. No se suman B/C como muestrasindependientes. Analizar meses/Q y activos, concentración en mejortrade/mes, costes, drawdown y trazabilidad de firmas de entradas/salidas. Distinguir patrones iguales en2026 de identidades universales. No escoger ni combinar mecanismos después de ver rendimientos.

## Auditoría y límites
ConciliarPNLtrades/netomotor/balance/equityterminal y formularios/fuentes. La corrección PAXG y caché previa ya está documentada; usar sólo datos corregidos. PAXG deBinanceSpot bajo simulaciónperpetual;SPXHistData BID/10 no certificaSPY24/7. SPXobservadohasta16octviernes;fin18octdomingo conservado. No funding/slippage/liquidez; mayorfee no los modela. Sinlive/paper, configuración global, reinicios ni cambiosframework.

## Fuentes de desarrollo
N204_T403_R5_FINAL_RESULTS_20261019.md;N503_R6_FINAL_RESULTS_20261019.md;BTC_R9_K_FAMILY_FINAL_RESULTS_20261019.md;BTC_TODAY_PROGRESS_ALL_METRICS_20261019.md. Snapshots originales de cada copia:
```json
[
  {
    "label": "N204",
    "name": "CapitalR12N204R2A6",
    "existing": true
  },
  {
    "label": "N503",
    "name": "OosN503R2A6",
    "from": "N204ExploreR503",
    "anchor": "a0db99e9-2638-4a58-a407-11fa8442f752"
  },
  {
    "label": "P604",
    "name": "OosP604R2A6",
    "from": "N503CapacityR604",
    "anchor": "bf8cf6df-8055-4e88-a52d-5cb3d12d8b52"
  },
  {
    "label": "C504",
    "name": "OosC504R2A6",
    "from": "T403ExploreR504",
    "anchor": "2ce5ecba-4ae6-4fd1-9917-4bf8117b09c8"
  },
  {
    "label": "K1005",
    "name": "OosK1005R2A6",
    "from": "BtcY902ExploreR1005",
    "anchor": "3f979db7-44e2-44c6-9b82-7c3362084f62"
  }
]
```
