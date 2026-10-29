# X03 R2 — conditional baseline bootstrap, calendar and arithmetic year deletion

Job 11b3b51b8d2e4f8395c622b1ac986b0c. All four reference results and four price anchors reconstructed with existing audited fill-to-MTM code. Fixed 10,000 circular block resamples, blocks3 primary/6 sensitivity, seed20261019, same month indices across B/C and costs. Main61 complete months, secondary63 including boundaries. USDT values are differences in observed monthly MTM PNL increments; return differences are percentage points, and their sum is arithmetic rather than compounded excess return.

These distributions are conditional descriptions of reused development observations. Positive bootstrap fraction is not probability of no overfitting; intervals do not correct prior searches, create unseen observations, model alternative capital/sizing paths or imply simulated DD. B/C are dependent. Year deletion is arithmetic, never OOS.

```json
{
  "bootstrap": [
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 48.92256349234433,
      "observed_sum": 2984.2763730330043,
      "mean_percentiles_2p5_50_97p5": [
        9.268033130894004,
        49.44526749884737,
        90.72661618600839
      ],
      "sum_percentiles_2p5_50_97p5": [
        565.3500209845342,
        3016.16131742969,
        5534.323587346512
      ],
      "fraction_bootstrap_mean_positive": 0.9927
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.2362100707469004,
      "observed_sum": 14.408814315560925,
      "mean_percentiles_2p5_50_97p5": [
        -0.018423299316279042,
        0.23755426067761498,
        0.5046748749870803
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.1238212582930214,
        14.490809901334513,
        30.785167374211895
      ],
      "fraction_bootstrap_mean_positive": 0.9669
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 44.382650457341505,
      "observed_sum": 2707.3416778978317,
      "mean_percentiles_2p5_50_97p5": [
        4.869213644925113,
        44.85853961718355,
        86.00739603144027
      ],
      "sum_percentiles_2p5_50_97p5": [
        297.02203234043185,
        2736.3709166481967,
        5246.451157917855
      ],
      "fraction_bootstrap_mean_positive": 0.9864
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.22359428524016972,
      "observed_sum": 13.639251399650353,
      "mean_percentiles_2p5_50_97p5": [
        -0.03620924302912034,
        0.2247308144403216,
        0.496490655481715
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.2087638247763413,
        13.70857968085962,
        30.285929984384612
      ],
      "fraction_bootstrap_mean_positive": 0.9565
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 39.842737422338914,
      "observed_sum": 2430.4069827626736,
      "mean_percentiles_2p5_50_97p5": [
        0.5472779147697613,
        40.39106643834705,
        81.25051051045573
      ],
      "sum_percentiles_2p5_50_97p5": [
        33.38395280095544,
        2463.85505273917,
        4956.2811411378
      ],
      "fraction_bootstrap_mean_positive": 0.9762
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.2098937774612897,
      "observed_sum": 12.803520425138672,
      "mean_percentiles_2p5_50_97p5": [
        -0.05470830110780479,
        0.21166172338251904,
        0.48902130330274385
      ],
      "sum_percentiles_2p5_50_97p5": [
        -3.337206367576092,
        12.911365126333662,
        29.830299501467373
      ],
      "fraction_bootstrap_mean_positive": 0.9445
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 49.220291417266886,
      "observed_sum": 3002.43777645328,
      "mean_percentiles_2p5_50_97p5": [
        9.765137472767723,
        49.690265115366614,
        90.55587401181143
      ],
      "sum_percentiles_2p5_50_97p5": [
        595.673385838831,
        3031.1061720373636,
        5523.908314720497
      ],
      "fraction_bootstrap_mean_positive": 0.9934
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.23536719180745336,
      "observed_sum": 14.357398700254654,
      "mean_percentiles_2p5_50_97p5": [
        -0.018769067050833095,
        0.23659511197071115,
        0.5024935187296273
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.1449130901008187,
        14.43230183021338,
        30.65210464250726
      ],
      "fraction_bootstrap_mean_positive": 0.9672
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 44.66413335149878,
      "observed_sum": 2724.5121344414256,
      "mean_percentiles_2p5_50_97p5": [
        5.546213117740542,
        45.19659337069264,
        85.66675812727657
      ],
      "sum_percentiles_2p5_50_97p5": [
        338.31900018217306,
        2756.9921956122507,
        5225.67224576387
      ],
      "fraction_bootstrap_mean_positive": 0.9872
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.22326946752384239,
      "observed_sum": 13.619437518954385,
      "mean_percentiles_2p5_50_97p5": [
        -0.03611902567528488,
        0.224662256209804,
        0.49533703933772083
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.2032605661923776,
        13.704397628798045,
        30.215559399600973
      ],
      "fraction_bootstrap_mean_positive": 0.9572
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 40.10797528573085,
      "observed_sum": 2446.586492429582,
      "mean_percentiles_2p5_50_97p5": [
        1.1815085146868398,
        40.5827602530853,
        80.89511545894158
      ],
      "sum_percentiles_2p5_50_97p5": [
        72.07201939589723,
        2475.548375438203,
        4934.602042995436
      ],
      "fraction_bootstrap_mean_positive": 0.9781
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21009658072272483,
      "observed_sum": 12.815891424086214,
      "mean_percentiles_2p5_50_97p5": [
        -0.05361607947595799,
        0.2119049783176443,
        0.488875872347041
      ],
      "sum_percentiles_2p5_50_97p5": [
        -3.270580848033438,
        12.926203677376302,
        29.8214282131695
      ],
      "fraction_bootstrap_mean_positive": 0.9453
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 48.92256349234433,
      "observed_sum": 2984.2763730330043,
      "mean_percentiles_2p5_50_97p5": [
        11.457283864187074,
        48.300528568673826,
        89.7662160279353
      ],
      "sum_percentiles_2p5_50_97p5": [
        698.8943157154116,
        2946.3322426891036,
        5475.739177704054
      ],
      "fraction_bootstrap_mean_positive": 0.9952
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.2362100707469004,
      "observed_sum": 14.408814315560925,
      "mean_percentiles_2p5_50_97p5": [
        0.010961365689759443,
        0.2324037827067614,
        0.48349212083904236
      ],
      "sum_percentiles_2p5_50_97p5": [
        0.668643307075326,
        14.176630745112446,
        29.493019371181582
      ],
      "fraction_bootstrap_mean_positive": 0.9818
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 44.382650457341505,
      "observed_sum": 2707.3416778978317,
      "mean_percentiles_2p5_50_97p5": [
        7.1032909058550455,
        43.89018593068796,
        84.86405481952616
      ],
      "sum_percentiles_2p5_50_97p5": [
        433.3007452571578,
        2677.301341771966,
        5176.707343991096
      ],
      "fraction_bootstrap_mean_positive": 0.9905
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.22359428524016972,
      "observed_sum": 13.639251399650353,
      "mean_percentiles_2p5_50_97p5": [
        -0.00588854843516005,
        0.21980722853648504,
        0.4747127055133152
      ],
      "sum_percentiles_2p5_50_97p5": [
        -0.35920145454476304,
        13.408240940725587,
        28.957475036312225
      ],
      "fraction_bootstrap_mean_positive": 0.9715
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 39.842737422338914,
      "observed_sum": 2430.4069827626736,
      "mean_percentiles_2p5_50_97p5": [
        2.7120495115152856,
        39.42444652086249,
        80.16346522668088
      ],
      "sum_percentiles_2p5_50_97p5": [
        165.4350202024324,
        2404.891237772612,
        4889.971378827534
      ],
      "fraction_bootstrap_mean_positive": 0.9836
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.2098937774612897,
      "observed_sum": 12.803520425138672,
      "mean_percentiles_2p5_50_97p5": [
        -0.023677993688124198,
        0.20620090447935982,
        0.4647062133828058
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.4443576149755761,
        12.578255173240949,
        28.347079016351156
      ],
      "fraction_bootstrap_mean_positive": 0.959
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 49.220291417266886,
      "observed_sum": 3002.43777645328,
      "mean_percentiles_2p5_50_97p5": [
        12.27977736512529,
        48.57860310623687,
        89.85578602874772
      ],
      "sum_percentiles_2p5_50_97p5": [
        749.0664192726425,
        2963.2947894804493,
        5481.202947753611
      ],
      "fraction_bootstrap_mean_positive": 0.9963
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.23536719180745336,
      "observed_sum": 14.357398700254654,
      "mean_percentiles_2p5_50_97p5": [
        0.011431028781668393,
        0.23136965736505888,
        0.48174528942722133
      ],
      "sum_percentiles_2p5_50_97p5": [
        0.6972927556817721,
        14.11354909926859,
        29.3864626550605
      ],
      "fraction_bootstrap_mean_positive": 0.9818
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 44.66413335149878,
      "observed_sum": 2724.5121344414256,
      "mean_percentiles_2p5_50_97p5": [
        7.801426257218345,
        44.10667609874511,
        84.6329712681911
      ],
      "sum_percentiles_2p5_50_97p5": [
        475.887001690319,
        2690.507242023452,
        5162.611247359657
      ],
      "fraction_bootstrap_mean_positive": 0.9919
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.22326946752384239,
      "observed_sum": 13.619437518954385,
      "mean_percentiles_2p5_50_97p5": [
        -0.00502745991490163,
        0.21949493334750475,
        0.4734126625269669
      ],
      "sum_percentiles_2p5_50_97p5": [
        -0.3066750548089994,
        13.389190934197789,
        28.87817241414498
      ],
      "fraction_bootstrap_mean_positive": 0.972
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 40.10797528573085,
      "observed_sum": 2446.586492429582,
      "mean_percentiles_2p5_50_97p5": [
        3.399331594674279,
        39.66306386387133,
        79.64549045780464
      ],
      "sum_percentiles_2p5_50_97p5": [
        207.35922727513102,
        2419.446895696151,
        4858.374917926082
      ],
      "fraction_bootstrap_mean_positive": 0.9858
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "full61",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21009658072272483,
      "observed_sum": 12.815891424086214,
      "mean_percentiles_2p5_50_97p5": [
        -0.02279301102327131,
        0.20609762304066503,
        0.4641489727156747
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.39037367241955,
        12.571955005480568,
        28.313087335656157
      ],
      "fraction_bootstrap_mean_positive": 0.9599
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 43.33402762213732,
      "observed_sum": 2730.043740194651,
      "mean_percentiles_2p5_50_97p5": [
        3.835059035461954,
        43.33487464377774,
        84.82241756228512
      ],
      "sum_percentiles_2p5_50_97p5": [
        241.6087192341031,
        2730.0971025579975,
        5343.812306423963
      ],
      "fraction_bootstrap_mean_positive": 0.9852
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21511795115579116,
      "observed_sum": 13.552430922814843,
      "mean_percentiles_2p5_50_97p5": [
        -0.032443170519340724,
        0.21458900415963603,
        0.47803922179017033
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.043919742718465,
        13.51910726205707,
        30.11647097278073
      ],
      "fraction_bootstrap_mean_positive": 0.957
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.78744120896463,
      "observed_sum": 2443.608796164772,
      "mean_percentiles_2p5_50_97p5": [
        -0.5996870438162174,
        38.736030662706504,
        79.92331976506755
      ],
      "sum_percentiles_2p5_50_97p5": [
        -37.780283760421696,
        2440.3699317505097,
        5035.169145199256
      ],
      "fraction_bootstrap_mean_positive": 0.9733
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.20153736127756955,
      "observed_sum": 12.696853760486881,
      "mean_percentiles_2p5_50_97p5": [
        -0.05182105559835485,
        0.20072877258315805,
        0.46820991437397463
      ],
      "sum_percentiles_2p5_50_97p5": [
        -3.2647265026963557,
        12.645912672738957,
        29.4972246055604
      ],
      "fraction_bootstrap_mean_positive": 0.9419
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 34.24085479579212,
      "observed_sum": 2157.1738521349034,
      "mean_percentiles_2p5_50_97p5": [
        -4.813877127678648,
        34.26344348061288,
        75.33111029778387
      ],
      "sum_percentiles_2p5_50_97p5": [
        -303.2742590437548,
        2158.596939278611,
        4745.859948760384
      ],
      "fraction_bootstrap_mean_positive": 0.9584
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.1867193649500412,
      "observed_sum": 11.763319991852596,
      "mean_percentiles_2p5_50_97p5": [
        -0.07175017838388612,
        0.18640785887874714,
        0.45722945586446906
      ],
      "sum_percentiles_2p5_50_97p5": [
        -4.520261238184825,
        11.74369510936107,
        28.80545571946155
      ],
      "fraction_bootstrap_mean_positive": 0.9252
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 43.3023906105346,
      "observed_sum": 2728.05060846368,
      "mean_percentiles_2p5_50_97p5": [
        4.12808218177029,
        43.34520627526412,
        84.34175257366871
      ],
      "sum_percentiles_2p5_50_97p5": [
        260.0691774515283,
        2730.7479953416396,
        5313.530412141129
      ],
      "fraction_bootstrap_mean_positive": 0.9856
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21438852403827002,
      "observed_sum": 13.506477014411011,
      "mean_percentiles_2p5_50_97p5": [
        -0.032785302782288785,
        0.21372397371610768,
        0.4765528384627351
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.0654740752841936,
        13.464610344114785,
        30.02282882315231
      ],
      "fraction_bootstrap_mean_positive": 0.9568
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.7105836267739,
      "observed_sum": 2438.7667684867556,
      "mean_percentiles_2p5_50_97p5": [
        -0.3822780138855005,
        38.72911543705013,
        79.73108954456566
      ],
      "sum_percentiles_2p5_50_97p5": [
        -24.083514874786534,
        2439.9342725341585,
        5023.058641307637
      ],
      "fraction_bootstrap_mean_positive": 0.9738
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.20123338428199092,
      "observed_sum": 12.677703209765427,
      "mean_percentiles_2p5_50_97p5": [
        -0.050635455951813534,
        0.2004134307436607,
        0.4664828068856995
      ],
      "sum_percentiles_2p5_50_97p5": [
        -3.1900337249642523,
        12.626046136850622,
        29.388416833799067
      ],
      "fraction_bootstrap_mean_positive": 0.942
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 34.11877664301331,
      "observed_sum": 2149.4829285098385,
      "mean_percentiles_2p5_50_97p5": [
        -4.859864362574936,
        34.11948323823793,
        74.9710155010255
      ],
      "sum_percentiles_2p5_50_97p5": [
        -306.171454842221,
        2149.5274440089897,
        4723.173976564606
      ],
      "fraction_bootstrap_mean_positive": 0.9584
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 3,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.18681573409987892,
      "observed_sum": 11.769391248292372,
      "mean_percentiles_2p5_50_97p5": [
        -0.07009831553842064,
        0.18676547064928245,
        0.4562384456521036
      ],
      "sum_percentiles_2p5_50_97p5": [
        -4.4161938789205,
        11.766224650904793,
        28.743022076082525
      ],
      "fraction_bootstrap_mean_positive": 0.9256
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 43.33402762213732,
      "observed_sum": 2730.043740194651,
      "mean_percentiles_2p5_50_97p5": [
        5.642167122113051,
        42.421894463795894,
        84.1271820215557
      ],
      "sum_percentiles_2p5_50_97p5": [
        355.45652869312215,
        2672.5793512191412,
        5300.012467358009
      ],
      "fraction_bootstrap_mean_positive": 0.9891
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21511795115579116,
      "observed_sum": 13.552430922814843,
      "mean_percentiles_2p5_50_97p5": [
        -0.007868498241609933,
        0.20999816180452632,
        0.46333469331616195
      ],
      "sum_percentiles_2p5_50_97p5": [
        -0.49571538922142583,
        13.229884193685159,
        29.1900856789182
      ],
      "fraction_bootstrap_mean_positive": 0.9701
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.78744120896463,
      "observed_sum": 2443.608796164772,
      "mean_percentiles_2p5_50_97p5": [
        1.3493279899151132,
        37.89988564985076,
        78.99474086558754
      ],
      "sum_percentiles_2p5_50_97p5": [
        85.00766336465212,
        2387.6927959405975,
        4976.668674532015
      ],
      "fraction_bootstrap_mean_positive": 0.9793
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.20153736127756955,
      "observed_sum": 12.696853760486881,
      "mean_percentiles_2p5_50_97p5": [
        -0.025752055869105634,
        0.19661142536800053,
        0.4530677431629963
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.6223795197536548,
        12.386519798184032,
        28.543267819268767
      ],
      "fraction_bootstrap_mean_positive": 0.9548
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 34.24085479579212,
      "observed_sum": 2157.1738521349034,
      "mean_percentiles_2p5_50_97p5": [
        -3.1837543407010864,
        33.42941198674657,
        73.8819208200118
      ],
      "sum_percentiles_2p5_50_97p5": [
        -200.57652346416845,
        2106.0529551650343,
        4654.561011660744
      ],
      "fraction_bootstrap_mean_positive": 0.9616
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.1867193649500412,
      "observed_sum": 11.763319991852596,
      "mean_percentiles_2p5_50_97p5": [
        -0.0464235070882713,
        0.18215823994934136,
        0.4415332178586228
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.924680946561092,
        11.475969116808505,
        27.816592725093237
      ],
      "fraction_bootstrap_mean_positive": 0.9366
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 43.3023906105346,
      "observed_sum": 2728.05060846368,
      "mean_percentiles_2p5_50_97p5": [
        5.938629399596859,
        42.40260867608644,
        83.62545248128637
      ],
      "sum_percentiles_2p5_50_97p5": [
        374.13365217460216,
        2671.3643465934456,
        5268.403506321042
      ],
      "fraction_bootstrap_mean_positive": 0.9903
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.21438852403827002,
      "observed_sum": 13.506477014411011,
      "mean_percentiles_2p5_50_97p5": [
        -0.008254216126320508,
        0.20898953689172106,
        0.46193227109734575
      ],
      "sum_percentiles_2p5_50_97p5": [
        -0.520015615958192,
        13.166340824178427,
        29.10173307913278
      ],
      "fraction_bootstrap_mean_positive": 0.9696
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 38.7105836267739,
      "observed_sum": 2438.7667684867556,
      "mean_percentiles_2p5_50_97p5": [
        1.703100124310412,
        37.7857708114487,
        78.40973826748896
      ],
      "sum_percentiles_2p5_50_97p5": [
        107.29530783155595,
        2380.503561121268,
        4939.8135108518045
      ],
      "fraction_bootstrap_mean_positive": 0.9799
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.20123338428199092,
      "observed_sum": 12.677703209765427,
      "mean_percentiles_2p5_50_97p5": [
        -0.025293307998499544,
        0.19647259568198155,
        0.4522607604335235
      ],
      "sum_percentiles_2p5_50_97p5": [
        -1.5934784039054712,
        12.377773527964838,
        28.49242790731198
      ],
      "fraction_bootstrap_mean_positive": 0.9551
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "USDT_MTM_increment",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 34.11877664301331,
      "observed_sum": 2149.4829285098385,
      "mean_percentiles_2p5_50_97p5": [
        -2.6430428237497807,
        33.30558636061977,
        73.51190049847193
      ],
      "sum_percentiles_2p5_50_97p5": [
        -166.5116978962362,
        2098.2519407190457,
        4631.249731403732
      ],
      "fraction_bootstrap_mean_positive": 0.9632
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "sample": "partial63",
      "unit": "percentage_point_return",
      "block_months": 6,
      "replicates": 10000,
      "seed": 20261019,
      "observed_mean": 0.18681573409987892,
      "observed_sum": 11.769391248292372,
      "mean_percentiles_2p5_50_97p5": [
        -0.04587995856732032,
        0.18256826122092634,
        0.44104681807778173
      ],
      "sum_percentiles_2p5_50_97p5": [
        -2.89043738974118,
        11.50180045691836,
        27.78594953890025
      ],
      "fraction_bootstrap_mean_positive": 0.9376
    }
  ],
  "year_MTM_increment": [
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -69.1767798562214,
      "positive_increment_months": 0
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 463.2037964637584,
      "positive_increment_months": 9
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 839.2603489450357,
      "positive_increment_months": 7
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 389.1685348422743,
      "positive_increment_months": 5
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -163.77106361111692,
      "positive_increment_months": 6
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 1271.358903410921,
      "positive_increment_months": 8
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -69.85041449406344,
      "positive_increment_months": 0
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 453.2211511861042,
      "positive_increment_months": 9
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 798.6530264827725,
      "positive_increment_months": 7
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 300.31696388758064,
      "positive_increment_months": 5
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -209.72864037916588,
      "positive_increment_months": 6
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 1170.9967094815438,
      "positive_increment_months": 8
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -70.52404913190367,
      "positive_increment_months": 0
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 443.23850590844995,
      "positive_increment_months": 8
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 758.0457040205129,
      "positive_increment_months": 7
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 211.46539293288697,
      "positive_increment_months": 5
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -255.6862171472112,
      "positive_increment_months": 6
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 1070.6345155521685,
      "positive_increment_months": 8
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -69.1767798562214,
      "positive_increment_months": 0
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 453.97773426413005,
      "positive_increment_months": 9
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 827.3224761687961,
      "positive_increment_months": 7
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 428.6087661823094,
      "positive_increment_months": 5
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -169.9190418682956,
      "positive_increment_months": 6
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 1257.2374535729614,
      "positive_increment_months": 8
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -69.85041449406344,
      "positive_increment_months": 0
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 444.4164916259706,
      "positive_increment_months": 9
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 787.3210748301954,
      "positive_increment_months": 7
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 340.2914948812522,
      "positive_increment_months": 5
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -217.18315584127959,
      "positive_increment_months": 6
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 1153.7712774846805,
      "positive_increment_months": 8
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "year": 2020,
      "months": 3,
      "incremental_MTM_USDT": -70.52404913190367,
      "positive_increment_months": 0
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "year": 2021,
      "months": 12,
      "incremental_MTM_USDT": 434.8552489878075,
      "positive_increment_months": 8
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "year": 2022,
      "months": 12,
      "incremental_MTM_USDT": 747.3196734915982,
      "positive_increment_months": 7
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "year": 2023,
      "months": 12,
      "incremental_MTM_USDT": 251.9742235802005,
      "positive_increment_months": 5
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "year": 2024,
      "months": 12,
      "incremental_MTM_USDT": -264.4472698142672,
      "positive_increment_months": 6
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "year": 2025,
      "months": 12,
      "incremental_MTM_USDT": 1050.3051013964032,
      "positive_increment_months": 8
    }
  ],
  "leave_one_year_out": [
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2799.2205200508724,
      "remaining_mean_increment_MTM_USDT": 46.65367533418121,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2266.8399437308926,
      "remaining_mean_increment_MTM_USDT": 44.44784203393907,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1890.7833912496153,
      "remaining_mean_increment_MTM_USDT": 37.07418414214932,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2340.8752053523767,
      "remaining_mean_increment_MTM_USDT": 45.89951383043876,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2893.814803805768,
      "remaining_mean_increment_MTM_USDT": 56.74146674128957,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 0,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1458.6848367837301,
      "remaining_mean_increment_MTM_USDT": 28.60166346634765,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2513.459210658835,
      "remaining_mean_increment_MTM_USDT": 41.89098684431392,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1990.3876449786676,
      "remaining_mean_increment_MTM_USDT": 39.027208725071915,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1644.9557696819993,
      "remaining_mean_increment_MTM_USDT": 32.25403469964704,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2143.291832277191,
      "remaining_mean_increment_MTM_USDT": 42.02533004465081,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2653.3374365439377,
      "remaining_mean_increment_MTM_USDT": 52.02622424595956,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 5,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1272.612086683228,
      "remaining_mean_increment_MTM_USDT": 24.95317817025937,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2227.697901266807,
      "remaining_mean_increment_MTM_USDT": 37.128298354446784,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1713.9353462264535,
      "remaining_mean_increment_MTM_USDT": 33.60657541620497,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1399.1281481143906,
      "remaining_mean_increment_MTM_USDT": 27.43388525714491,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1945.7084592020165,
      "remaining_mean_increment_MTM_USDT": 38.151146258863065,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2412.8600692821146,
      "remaining_mean_increment_MTM_USDT": 47.3109817506297,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "B",
      "cost_bps_RT": 10,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1086.539336582735,
      "remaining_mean_increment_MTM_USDT": 21.304692874171273,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2797.2273883199014,
      "remaining_mean_increment_MTM_USDT": 46.62045647199836,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2274.07287419955,
      "remaining_mean_increment_MTM_USDT": 44.58966419999118,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1900.7281322948838,
      "remaining_mean_increment_MTM_USDT": 37.26917906460557,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2299.4418422813706,
      "remaining_mean_increment_MTM_USDT": 45.08709494669354,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2897.9696503319756,
      "remaining_mean_increment_MTM_USDT": 56.822934320234815,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 0,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1470.8131548907186,
      "remaining_mean_increment_MTM_USDT": 28.83947362530821,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2508.617182980819,
      "remaining_mean_increment_MTM_USDT": 41.810286383013654,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1994.350276860785,
      "remaining_mean_increment_MTM_USDT": 39.104907389427154,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1651.4456936565603,
      "remaining_mean_increment_MTM_USDT": 32.38128811091295,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2098.4752736055034,
      "remaining_mean_increment_MTM_USDT": 41.14657399226477,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2655.949924328035,
      "remaining_mean_increment_MTM_USDT": 52.07744949662814,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 5,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1284.9954910020751,
      "remaining_mean_increment_MTM_USDT": 25.195990019648534,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "excluded_year": 2020,
      "remaining_months": 60,
      "remaining_increment_MTM_USDT": 2220.006977641742,
      "remaining_mean_increment_MTM_USDT": 37.000116294029034,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "excluded_year": 2021,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1714.627679522031,
      "remaining_mean_increment_MTM_USDT": 33.62015057886335,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "excluded_year": 2022,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1402.1632550182403,
      "remaining_mean_increment_MTM_USDT": 27.493397157220397,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "excluded_year": 2023,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1897.508704929638,
      "remaining_mean_increment_MTM_USDT": 37.20605303783604,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "excluded_year": 2024,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 2413.9301983241057,
      "remaining_mean_increment_MTM_USDT": 47.33196467302168,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    },
    {
      "portfolio": "C",
      "cost_bps_RT": 10,
      "excluded_year": 2025,
      "remaining_months": 51,
      "remaining_increment_MTM_USDT": 1099.1778271134353,
      "remaining_mean_increment_MTM_USDT": 21.55250641398893,
      "interpretation": "Arithmetic deletion of calendar buckets; no strategy rerun, no OOS, capital paths remain observed."
    }
  ],
  "limits": "Conditional empirical variability only. Reused development sample and multiple prior searches remain. Bands do not establish probability of no overfitting, confirmatory p-values, OOS performance, alternate sizing paths or simulated drawdown."
}
```
