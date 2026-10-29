# X03 R2 — bootstrap con comisión real del motor

Job809888acac864660ade19b1600668978 SUCCEEDED. Las cuatro referencias finished tienen fee.00070 por lado, fechas2020-10-15→2025-12-31exclusivo. Sin overlays adicionales. Mismo protocolo10.000réplicas/bloquescirculares3primario6sensibilidad/seed20261019/61mesescompletos y63incluyendofronteras; mismos índices B/C sin agruparlos.

El incremento total X03−sinX03 concilia2137.238797USDT B y2098.091703USDT C. Las bandas de bloques3 incluyen0 con63bins; con61bins son positivas, y con63/bloque6 apenaspositivas. No seleccionar la especificación favorable. Dependencia temporal y fronteras influyen en esta descripción.

Fuente de estrategia idéntica, pero elevar comisión altera sizing y gestión dependiente de fees en toda la cartera; en PAXG, root verificó que el BE adelantó un runner largo. La comparación actual al mismo fee evita atribuir toda la penalidad nominal→stress a BTC, y sigue incluyendo capital y ocupación endógenos. No es identificación causal de alpha.

| B/C | Muestra | Bloque | MediaΔMTM USDT/mes | Percentiles2.5/50/97.5 |
|---|---|---:|---:|---|
| B | full61 | 3 | 38.72 | 2.78 / 39.30 / 76.31 |
| C | full61 | 3 | 38.34 | 2.52 / 38.89 / 75.54 |
| B | full61 | 6 | 38.72 | 5.40 / 38.28 / 74.68 |
| C | full61 | 6 | 38.34 | 5.50 / 37.87 / 73.70 |
| B | partial63 | 3 | 33.92 | -1.74 / 33.98 / 70.96 |
| C | partial63 | 3 | 33.30 | -2.22 / 33.28 / 70.16 |
| B | partial63 | 6 | 33.92 | 0.35 / 33.21 / 69.97 |
| C | partial63 | 6 | 33.30 | 0.13 / 32.59 / 68.97 |

Bandas condicionadas a muestra de desarrollo intensamente reutilizada y a los caminos observados; no pvalues confirmatorios, probabilidad de no sobreajuste, OOS, DD simulado ni garantía futura. B/C dependen del mismo mecanismo y datos. 2026 cerrado. Root conserva auditoría completa de fills/MTM/calendario; este informe añade sólo bootstrap y diagnósticos aritméticos.

```json
{
  "bootstrap": [
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.719909534048725,
      "observed_sum": 2361.9144815769723,
      "mean_percentiles_2p5_50_97p5": [
        2.779577424040301,
        39.29714304513281,
        76.3102142306559
      ],
      "sum_percentiles_2p5_50_97p5": [
        169.55422286645836,
        2397.1257257531015,
        4654.923068070009
      ],
      "fraction_bootstrap_mean_positive": 0.9829
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21010087004384898,
      "observed_sum": 12.816153072674787,
      "mean_percentiles_2p5_50_97p5": [
        -0.039284102273919985,
        0.2114487446086038,
        0.47192600099077037
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.3963302387091185,
        12.898373421124832,
        28.78748606043699
      ],
      "fraction_bootstrap_mean_positive": 0.9548
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.33930566827329,
      "observed_sum": 2338.6976457646706,
      "mean_percentiles_2p5_50_97p5": [
        2.5153074375155517,
        38.88594255294735,
        75.54028340431468
      ],
      "sum_percentiles_2p5_50_97p5": [
        153.43375368844866,
        2372.0424957297882,
        4607.957287663195
      ],
      "fraction_bootstrap_mean_positive": 0.9815
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.20652729742769904,
      "observed_sum": 12.598165143089641,
      "mean_percentiles_2p5_50_97p5": [
        -0.04273471587584191,
        0.2076200335028287,
        0.4691915291092103
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.6068176684263564,
        12.664822043672551,
        28.62068327566183
      ],
      "fraction_bootstrap_mean_positive": 0.9514
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.719909534048725,
      "observed_sum": 2361.9144815769723,
      "mean_percentiles_2p5_50_97p5": [
        5.398132670504795,
        38.27806723232598,
        74.67773261973417
      ],
      "sum_percentiles_2p5_50_97p5": [
        329.2860929007925,
        2334.9621011718846,
        4555.341689803784
      ],
      "fraction_bootstrap_mean_positive": 0.9893
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21010087004384898,
      "observed_sum": 12.816153072674787,
      "mean_percentiles_2p5_50_97p5": [
        -0.006147392608026975,
        0.20622848508082153,
        0.44735442837340894
      ],
      "sum_percentiles_2p5_50_97p5": [
        -0.3749909490896455,
        12.579937589930113,
        27.288620130777947
      ],
      "fraction_bootstrap_mean_positive": 0.9706
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.33930566827329,
      "observed_sum": 2338.6976457646706,
      "mean_percentiles_2p5_50_97p5": [
        5.5009232964971115,
        37.86902677729858,
        73.70312634658112
      ],
      "sum_percentiles_2p5_50_97p5": [
        335.5563210863238,
        2310.0106334152133,
        4495.890707141448
      ],
      "fraction_bootstrap_mean_positive": 0.9898
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.20652729742769904,
      "observed_sum": 12.598165143089641,
      "mean_percentiles_2p5_50_97p5": [
        -0.011445409074140352,
        0.20286222945565882,
        0.4445450302795087
      ],
      "sum_percentiles_2p5_50_97p5": [
        -0.6981699535225615,
        12.374595996795188,
        27.117246847050033
      ],
      "fraction_bootstrap_mean_positive": 0.9669
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 33.92442534359286,
      "observed_sum": 2137.2387966463502,
      "mean_percentiles_2p5_50_97p5": [
        -1.7386440461328891,
        33.984029302436184,
        70.96266729900728
      ],
      "sum_percentiles_2p5_50_97p5": [
        -109.53457490637203,
        2140.9938460534795,
        4470.648039837459
      ],
      "fraction_bootstrap_mean_positive": 0.9696
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.1893977411480625,
      "observed_sum": 11.932057692327938,
      "mean_percentiles_2p5_50_97p5": [
        -0.05102279443360322,
        0.1892955582482292,
        0.4440854720545688
      ],
      "sum_percentiles_2p5_50_97p5": [
        -3.214436049317003,
        11.925620169638439,
        27.97738473943783
      ],
      "fraction_bootstrap_mean_positive": 0.9393
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 33.30304290524122,
      "observed_sum": 2098.091703030197,
      "mean_percentiles_2p5_50_97p5": [
        -2.2202369569816476,
        33.28104705799118,
        70.16037096742467
      ],
      "sum_percentiles_2p5_50_97p5": [
        -139.8749282898438,
        2096.7059646534444,
        4420.103370947753
      ],
      "fraction_bootstrap_mean_positive": 0.9679
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.18595531940702678,
      "observed_sum": 11.715185122642687,
      "mean_percentiles_2p5_50_97p5": [
        -0.05600537606625218,
        0.1859469279351651,
        0.44077657217398686
      ],
      "sum_percentiles_2p5_50_97p5": [
        -3.5283386921738873,
        11.714656459915403,
        27.768924046961175
      ],
      "fraction_bootstrap_mean_positive": 0.9361
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 33.92442534359286,
      "observed_sum": 2137.2387966463502,
      "mean_percentiles_2p5_50_97p5": [
        0.3482160668963191,
        33.21342972474014,
        69.97373806635461
      ],
      "sum_percentiles_2p5_50_97p5": [
        21.937612214468103,
        2092.4460726586285,
        4408.345498180341
      ],
      "fraction_bootstrap_mean_positive": 0.9764
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.1893977411480625,
      "observed_sum": 11.932057692327938,
      "mean_percentiles_2p5_50_97p5": [
        -0.02594963336755067,
        0.18471796213385455,
        0.42814176051917296
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.6348269021556923,
        11.637231614432835,
        26.9729309127079
      ],
      "fraction_bootstrap_mean_positive": 0.9537
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 33.30304290524122,
      "observed_sum": 2098.091703030197,
      "mean_percentiles_2p5_50_97p5": [
        0.12754664177194047,
        32.586997700355866,
        68.96624245743708
      ],
      "sum_percentiles_2p5_50_97p5": [
        8.03543843163225,
        2052.9808551224196,
        4344.873274818536
      ],
      "fraction_bootstrap_mean_positive": 0.9756
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.18595531940702678,
      "observed_sum": 11.715185122642687,
      "mean_percentiles_2p5_50_97p5": [
        -0.03074250569946422,
        0.1809582900181077,
        0.4263197671190959
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.9367778590662457,
        11.400372271140785,
        26.858145328503046
      ],
      "fraction_bootstrap_mean_positive": 0.949
    }
  ],
  "year_MTM_increment": [
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -72.13139701642285,
      "positive_increment_months": 0
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 454.6020478364844,
      "positive_increment_months": 9
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 747.6676705914106,
      "positive_increment_months": 6
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 282.2030327389348,
      "positive_increment_months": 5
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -216.49798680903587,
      "positive_increment_months": 6
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 941.3954293049792,
      "positive_increment_months": 8
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -72.13139701642103,
      "positive_increment_months": 0
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 444.6892675887957,
      "positive_increment_months": 9
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 738.0495922262689,
      "positive_increment_months": 7
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 310.389520467319,
      "positive_increment_months": 5
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -254.49272767621733,
      "positive_increment_months": 6
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 931.5874474404518,
      "positive_increment_months": 7
    }
  ],
  "leave_one_year_out": [
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2209.370193662773,
      "remaining_mean_increment_MTM_USDT": 36.822836561046216,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1682.6367488098658,
      "remaining_mean_increment_MTM_USDT": 32.99287742764443,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1389.5711260549397,
      "remaining_mean_increment_MTM_USDT": 27.246492667743915,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1855.0357639074155,
      "remaining_mean_increment_MTM_USDT": 36.37325027269442,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2353.736783455386,
      "remaining_mean_increment_MTM_USDT": 46.15170163638012,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1195.843367341371,
      "remaining_mean_increment_MTM_USDT": 23.447909163556297,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2170.223100046618,
      "remaining_mean_increment_MTM_USDT": 36.17038500077697,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1653.4024354414014,
      "remaining_mean_increment_MTM_USDT": 32.41965559689022,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1360.0421108039282,
      "remaining_mean_increment_MTM_USDT": 26.667492368704472,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1787.702182562878,
      "remaining_mean_increment_MTM_USDT": 35.05298397182114,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2352.5844307064144,
      "remaining_mean_increment_MTM_USDT": 46.1291064844395,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "engine_fee_per_side": 0.0007,
      "overlay_extra_bps_RT": 0,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1166.5042555897453,
      "remaining_mean_increment_MTM_USDT": 22.872632462544026,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    }
  ],
  "limits": "Conditional empirical variability only. Reused development sample and multiple prior searches remain. Bands do not establish probability of no overfitting, confirmatory p-values, OOS performance, alternate sizing paths or simulated drawdown."
}
```
