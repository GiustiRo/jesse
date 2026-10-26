# Modern ML / DL for return prediction in liquid markets: what has real out-of-sample evidence (as of Oct 2026)

Context for the reader: small team, Binance USDT-M perps (crypto + some TradFi perps), 4h/1h bars, ~10k USD, Python/Jesse, CPU plus maybe one GPU. They already run a Donchian trend ensemble and crypto 4h breakouts (portfolio Sharpe ~1.5). Their universe was 7 assets and could grow to 100+ perps.

Source-quality legend: [PR] peer-reviewed; [WP] working paper or preprint; [PRESS] press or practitioner summary; [MEM] number recalled from the paper and not re-checked in this session (verify before quoting).

---

## 1. Cross-sectional ML return prediction (Gu-Kelly-Xiu and successors, crypto cross-sections)

### Takeaway
Cross-sectional ML on crypto (weekly rebalance, hundreds to thousands of coins) has peer-reviewed evidence of large gross spreads, and part of it survives 30-60 bps costs, including in the top 100 coins. The signal is mostly an ML-aggregated trend/momentum plus volume signal ("CTREND"), and it is strongest in small, volatile coins. In equities, ML profits sit largely in hard-to-trade stocks and shrink sharply after realistic frictions. For this team the plausible edge is a weekly or daily cross-sectional ranker on 100+ perps, overlapping heavily with trend and needing a long-short, market-neutral structure. It is not an hourly directional model.

### Cited Findings
- **Gu, Kelly, Xiu (2020, RFS) [PR]:** about 30,000 US stocks, 1957-2016, 94 characteristics, monthly horizon. Trees and neural nets beat linear models, and the dominant predictors are price trends (momentum, short-term reversal), liquidity and volatility — [NBER WP w25398](https://www.nber.org/system/files/working_papers/w25398/w25398.pdf). [MEM] Monthly OOS R² is about 0.4% for the best NN. The value-weighted NN long-short decile Sharpe is about 1.35, and the equal-weighted one is much higher, gross of costs.
- An open replication by Tidy Finance exists for checking the pipeline — [Tidy Finance replication](https://www.tidy-finance.org/blog/gu-kelly-xiu-replication/).
- **Avramov, Cheng, Metzker (2023, Management Science) [PR]:** deep-learning stock-return signals earn most of their profits in hard-to-trade stocks. Excluding microcaps, distressed firms or high-volatility periods "considerably attenuates profitability", and performance worsens further with reasonable trading costs because of high turnover and extreme positions. The signals stay profitable in long positions and recent years, with low downside risk — [SSRN 3450322](https://papers.ssrn.com/abstract=3450322); [HUJI record](https://cris.huji.ac.il/en/publications/machine-learning-vs-economic-restrictions-evidence-from-stock-ret/).
- Per CUHK press coverage [PRESS], the payoff drops 62% without microcaps, 68% without non-rated firms and 80% without distressed firms around downgrades — [CUHK Business School](https://cbk.bschool.cuhk.edu.hk/the-limitations-of-using-ai-to-pick-stocks/).
- **Net-of-cost ML anomaly strategies (AFA listing, authors and sample not confirmed) [WP]:** they stay profitable OOS with net returns up to about 1.42% per month, despite turnover above 50% — [AFA](https://afajof.org/management/viewp.php?n=75544).
- **"Anachronistic testing-date bias" (AFA poster, status unverified) [WP]:** full-sample ML backtests mix in profits earned before the technique existed. After a neural-net approach is public, its short signal tracks later short interest, while boosted trees show no such pattern — [AFA](https://afajof.org/management/viewp.php?n=265916).
- **McLean and Pontiff (2016):** anomaly returns fall by roughly half after publication but stay positive on average. This is cited secondhand in the search results; see the JF original.
- **CTREND, Fieberg, Liedtke, Poddig, Walker, Zaremba (JFQA 60(7), Nov 2025, open access) [PR]** — [JFQA](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/trend-factor-for-the-cross-section-of-cryptocurrency-returns/4C1509ACBA33D5DCAF0AC24379148178):
  - Design: more than 3,000 coins (market cap above USD 1m), Apr 2015 to May 2022 (423 weeks), weekly rebalance. ML (a cross-sectional elastic net, "CS-C-ENet", among others) combines many price and volume technical indicators across horizons.
  - Value-weighted quintile long-short: 3.87% per week (t = 5.19), annualized Sharpe 1.94.
  - Decay: second-half returns are lower (3.26% per week in recent years), but the LTW 3-factor alphas are "almost unchanged".
  - Returns are higher in stable markets (5.46% per week) than in volatile ones (2.27%), and positive in bear markets (3.25%).
  - Design robustness: across 55,296 research-design combinations, most Sharpe ratios fall between 0.5 and 2.5 (0.5 to 2 value-weighted). The factor is significant in 79% of combinations. The baseline sits at the upper edge of that distribution, and the right tail comes from designs that emphasize small, volatile coins.
  - Costs: turnover is about 68% per week. With 30/40 bps (long/short) costs, net long-short returns are 2.35% to 2.90% per week. In the largest 100 coins the net figure is 1.90% to 2.45% per week, still significant.
  - Holding period: 2-week rebalancing cuts returns by about 1.5 percentage points to 2.34% per week. Returns stay significant up to a 4-week holding period.
  - Liquidity: controlling for Amihud illiquidity causes the largest drop, with the LTW alpha falling to 0.62% (significant only at 10%).
- **Cakici, Shahzad, Będowska-Sójka, Zaremba (International Review of Financial Analysis 2024) [PR]:** eight ML models, 40 characteristics, 2017-2023. A forecast-combination long-short earns 2.37% per week with Sharpe 1.66, and the authors say it survives high turnover and costs. The working-paper version reported a value-weighted Sharpe of 5.37 (4.72% per week). The published figure is much lower, a warning on version drift — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1057521924001765); [AFFI 2023 WP](https://affi2023.eventsadmin.com/Papers/ViewContribution?cid=8390&h=A0CBBA4C296557EB2205D3ECCD9DBD7F). Search snippets say profits concentrate in the top quintile while the rest of the portfolios are mediocre.
- **Crypto cross-sectional interactions (IRFA 2024) [PR]:** a value-weighted long-short has Sharpe of about 1.06, against 1.54 equal-weighted — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1057521924007415?via=ihub).
- **Jaquart, Köpke, Weinhardt (2022, J. Finance & Data Science) [PR]:** daily direction for the 100 largest coins. Accuracy is 52.9% to 54.1%, and 57.5% to 59.5% on the most confident predictions — [DOAJ](https://doaj.org/article/cfc09801314441198e3e1c92a3914e54).
- **Sebastião and Godinho (2021, Financial Innovation) [PR]:** linear models, random forests and SVMs on BTC, ETH and LTC. An ensemble stays positive after 0.5% costs, but 5 of 18 individual models have hit rates below 50% — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7785332/).
- **LSTM/GRU crypto ensemble [PR, lower quality]:** reports an OOS Sharpe after costs of 3.23 (LSTM) and 3.12 (GRU), against 1.33 for buy-and-hold. Sample details are unclear, so treat this as hype-prone — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405918822000174).
- **"From Predictability to Tradability" (Kim and Lim, SSRN 7115197) [WP]:** per the search snippet, models on daily OHLCV produce "weak but statistically detectable" cross-sectional ranking signals, especially at short and intermediate horizons, but "economic survival is narrow". The full text was not accessible (HTTP 403) — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7115197).
- **Quarter-hour effect on six Binance perps [WP, arXiv Jul 2026]:** order imbalance at quarter-hour marks forecasts 4-to-12-hour returns OOS, and the effect is weaker at finer marks. This is an intraday perp-specific microstructure signal relevant to 1h/4h bars — [arXiv 2607.09426](https://arxiv.org/html/2607.09426v1).
- A public GitHub project builds daily cross-sectional ML portfolios on Binance USDT-M perps (24h horizon, point-in-time). It is a template, not evidence — [GitHub](https://github.com/SmartR168/Predict-crypto-returns-in-the-cross-section-public).

### Inferences
- The robust part of crypto ML cross-sections is ML-combined trend and volume information at a weekly horizon. That overlaps conceptually with the team's Donchian ensemble. The incremental value would come from making it cross-sectional and market-neutral (long-short ranks) rather than time-series directional, which should lower correlation with existing trend P&L.
- On Binance perps, round-trip taker costs are about 8-10 bps plus slippage, and funding flows on both legs. That is below the 30-60 bps the papers assume, so a weekly or twice-weekly CTREND-style ranker over the top 50-150 perps is cost-feasible. The paper samples (2015-2022, spot, over 3,000 coins) include an illiquid tail that perps do not offer, so expect the gross spread to be much smaller than the headline: something like the top-100 or 10%-largest numbers, minus post-2022 decay.
- A realistic expectation is a standalone Sharpe of 0.5-1.0 net, inferred from the design-choice distribution and the value-weighted, large-coin subsets. Its main value would be as a diversifier.
- Hourly cross-sectional ML on perps has no peer-reviewed support found. The only intraday evidence is a microstructure timing effect.

### Gaps
- No peer-reviewed study was found of ML cross-sectional prediction specifically on Binance USDT-M perps with funding included, at a 1h/4h horizon.
- Post-2022 out-of-sample performance of CTREND (after its sample end) is not reported.
- The exact GKX table values were not re-verified in this session (marked [MEM]).
- Kaiko and Amberdata research on ML return prediction was not found in searches. Their public research focuses on liquidity and market structure.

---

## 2. "Virtue of complexity" (Kelly, Malamud, Zhou 2024) and random-feature / ridge approaches

### Takeaway
KMZ (JF 2024) claim that heavily over-parameterized ridge(less) regressions on random Fourier features (RFF) beat simple models for market timing, even with 12-month training windows. Strong critiques (Nagel 2025, Buncic 2025, Berk, Fallahgoul, Cartea-Jin-Shi) show that in small samples the method mechanically reduces to a volatility-timed momentum strategy that happened to work, rather than learning from the data. For a small-data team this is not a reason to build giant RFF models. The useful lessons are shrinkage (ridge), ensembling, and the fact that simple volatility-scaled time-series momentum (which they already run) is what the machinery rediscovers.

### Cited Findings
- **KMZ claim [PR, JF]:** theory shows that simple models "severely understate" return predictability relative to complex models where parameters exceed observations. Empirically they report a virtue of complexity in US market timing — [JF PDF via Yale](https://economics.yale.edu/sites/default/files/2024-01/The%20Journal%20of%20Finance%20-%202023%20-%20KELLY%20-%20The%20Virtue%20of%20Complexity%20in%20Return%20Prediction%20(1).pdf); [NBER w30217](https://www.nber.org/system/files/working_papers/w30217/w30217.pdf).
- **KMZ setup:** P = 12,000 RFF built from K = 15 predictors (Goyal-Welch plus lagged returns), rolling T = 12 months, ridgeless regression — [Nagel 2025](https://voices.uchicago.edu/stefannagel/files/2025/07/Complexity_2.pdf).
- **Nagel, "Seemingly Virtuous Complexity in Return Prediction" (Jul 2025) [WP]** — [PDF](https://voices.uchicago.edu/stefannagel/files/2025/07/Complexity_2.pdf):
  - When P is much larger than T, the RFF forecast becomes a similarity-weighted average of the T training returns.
  - In short windows, similarity mostly reflects temporal proximity, so the forecast is a recency-weighted average, essentially momentum. Because similarity declines with predictor volatility, it is volatility-timed momentum.
  - The RFF forecast correlates 0.93 with a plain Gaussian-kernel forecast.
  - On artificial data with return reversals, the method builds the same volatility-timed momentum and performs poorly.
  - The result also holds for T = 60 and T = 120.
  - The same logic extends partly to cross-sectional RFF SDFs (Didisheim-Ke-Kelly-Malamud) with short windows, but is less acute with T = 360.
- **Other critiques, as summarized in Nagel's literature review:**
  - Berk (2023): KMZ's Sharpe ratios are averages over 1,000 random-weight draws, so they are not achievable by a single implementation.
  - Buncic (2025): the rising complexity-performance relation disappears if forecasts are aggregated across draws before evaluation.
  - Cartea, Jin and Shi (2025): measurement error in predictors limits the virtue of complexity.
  - Fallahgoul (2025): information-theoretic bounds imply that learning complex relations is impossible at KMZ's sample sizes.
  - Source: [Nagel 2025](https://voices.uchicago.edu/stefannagel/files/2025/07/Complexity_2.pdf).
- **Buncic's i.i.d. noise experiment (per a summary):** running the KMZ machinery on i.i.d. normal data still produces the VoC curve — [Systematically Biased substack](https://systematicallybiased.substack.com/p/pockets-of-replicability-post-2).
- **"Simplified: A Closer Look at the VoC" [WP]:** calls the result an artefact of user choices and flags look-ahead from current-month inflation, which is released the following month — [Aalto GSF PDF](https://gsf.projectsites.aalto.fi/wp-content/uploads/sites/10/2025/09/kmz.pdf).
- **Kılıç, Fed FEDS 2025-089 [WP]:** in FX forecasting, VoC gains are localized to very small samples with rich fundamentals and are fragile as windows expand — [Federal Reserve](https://www.federalreserve.gov/econres/feds/files/2025089pap.pdf).
- **Kelly and Malamud reply, "Understanding the Virtue of Complexity" (2025) [WP]:** the challenges "have little bearing" on the theory or evidence. They stress effective vs nominal complexity, implicit regularization, limits to learning, and "the virtue of ensemble complexity" — [SSRN 5346842](https://papers.ssrn.com/abstract=5346842); [AQR](https://www.aqr.com/Insights/Research/Working-Paper/Understanding-The-Virtue-of-Complexity).

### Inferences
- With 7 assets, or even 100 perps at 4h bars, a high-P random-feature model will behave like a kernel smoother. In short windows it re-creates vol-scaled momentum, which the team already trades. Expected incremental edge is low and the false-discovery risk is high.
- What transfers: ridge shrinkage on a moderate feature set, ensembles over seeds and feature subsets, and evaluation of the ensemble forecast (Buncic's point), never averaged per-draw Sharpe.

### Gaps
- No application of RFF/VoC to crypto or perps was found.
- The exact KMZ market-timing Sharpe figures were not extracted.

---

## 3. Time-series foundation models (Chronos, TimesFM, Moirai, Lag-Llama, TimeGPT)

### Takeaway
Rigorous evidence says zero-shot TSFMs do not predict daily returns better than simple or tree baselines. Only TSFMs pre-trained from scratch on huge financial return panels become competitive, and even then gradient boosting (CatBoost) matches or beats them. Gains over a random walk on single assets are small and rarely significant. TSFMs are more defensible for volatility than for returns. This is hype-heavy; do not expect alpha from off-the-shelf Chronos or TimesFM on 4h crypto bars.

### Cited Findings
- **Rahimikia, Ni, Wang, "Re(Visiting) TSFMs in Finance" (arXiv 2511.18578, Nov 2025) [WP]** — [arXiv](https://arxiv.org/html/2511.18578v1); [IDEAS](https://ideas.repec.org/p/arx/papers/2511.18578.html):
  - Design: daily excess returns in 94 countries, 1990-2023, OOS 2001-2023, about 18M forecasts. Daily-rebalanced equal-weighted decile long-short, before costs.
  - Zero-shot: Chronos-large (window 512) has OOS R² of −1.37% and about 51% directional accuracy. TimesFM-500M has R² of −2.80%, below 50% accuracy and a −1.47% annual long-short return.
  - Pre-trained from scratch on finance: Chronos-small reaches Sharpe 5.42 and TimesFM-20M Sharpe 3.66.
  - CatBoost (window 252) reaches Sharpe 6.79, the best US result, and an R² of about −0.03%.
  - Scaled up (global data, JKP factors, synthetic data): Chronos-small reaches 51.74% accuracy and Sharpe 6.78, against CatBoost at Sharpe 6.46.
  - These Sharpes are equal-weighted, daily, gross, and dominated by small and illiquid stocks; the transaction-cost section was not read.
  - The authors released 613 finance-pretrained models (FinText-TSFM) — [FinText](https://fintext-readme.static.hf.space/).
- **"Pretrained TSFMs for Financial Return Forecasting" (arXiv 2606.27100, Jun 2026) [WP]:** five large US stocks. TimeGPT, TimesFM-2.5, Moirai-2.0, Chronos and Chronos-2 win 8 of 10 tasks against PatchTST and iTransformer. Against a random walk, gains are "small and sparse": only 2 cases pass a one-sided Diebold-Mariano test. The authors call TSFMs "practical priors", not "alpha generators" — [arXiv](https://arxiv.org/html/2606.27100).
- A volatility study compares nine zero-shot TSFMs (including Chronos-Bolt and TimesFM 2.5) with econometric benchmarks on realized volatility for 50 assets. The ranking was not extracted — [arXiv 2607.05291](https://arxiv.org/html/2607.05291v1).
- Chronos-2 multivariate (Magnificent-7 plus rates): the multivariate version beats the univariate one, with no trading evaluation found — [arXiv 2605.21504](https://arxiv.org/pdf/2605.21504).
- On noisy periodic synthetic series, a linear AR model beat all TSFMs on one dataset group — [arXiv 2501.00889](https://arxiv.org/pdf/2501.00889).

### Inferences
- For 4h crypto returns, zero-shot TSFMs should be treated as roughly random-walk forecasters. Pre-training a finance TSFM from scratch needs panel sizes (billions of observations) and compute far beyond this team.
- LightGBM or CatBoost on engineered features is the evidence-backed baseline that TSFMs struggle to beat.
- A possible niche: TSFMs as zero-shot volatility forecasters, or as a feature to combine with HAR. The evidence there is pending.

### Gaps
- No rigorous crypto-return evaluation of TSFMs was found.
- Net-of-cost results in Rahimikia et al. were not read.
- No study was found of Lag-Llama or Moirai on crypto returns.

---

## 4. Deep learning on limit order books and trades (DeepLOB etc.)

### Takeaway
LOB deep learning predicts mid-price direction at sub-second to roughly minute horizons, measured in book events. Predictability decays fast with horizon, is much weaker for small-tick assets (most crypto perps relative to price), and "high forecasting power does not necessarily translate into actionable trading signals". No credible evidence was found that raw-LOB DL signals persist to 1h/4h. The aggregated order-flow and imbalance features that do reach hours (e.g. the quarter-hour effect, 4-12h) are simple statistics, not deep models.

### Cited Findings
- **DeepLOB (Zhang, Zohren, Roberts 2019) [PR]:** CNN-LSTM on LSE LOBs. Its trading simulation used mid-prices without transaction costs — [arXiv 1808.03668](https://arxiv.org/pdf/1808.03668).
- **Briola, Bartolucci, Aste, "Deep limit order book forecasting: a microstructural guide" (Quant Finance 2025, 25(7)) [PR]:** NASDAQ stocks, horizons of 10, 50 and 100 LOB updates. Average MCC at H = 10 is 0.29 for large-tick stocks and 0.11 for small-tick stocks, and at H = 100 small-tick MCC is near zero. Standard ML metrics mislead, and forecast power does not equal tradability — [arXiv 2403.09267](https://arxiv.org/pdf/2403.09267); [T&F](https://www.tandfonline.com/doi/pdf/10.1080/14697688.2025.2522911).
- A volume-representation study finds predictability of mid-price returns "ubiquitous" up to 500 ms ahead — [arXiv 2211.13777](https://arxiv.org/pdf/2211.13777).
- DeepLOB transfers to BTCUSD books with similar accuracy, for next mid-price move direction — [arXiv 2010.01241](https://arxiv.org/pdf/2010.01241). For Coinbase BTC at 100 ms snapshots, most value sits in the top 10 levels — [arXiv 2003.00803](https://arxiv.org/pdf/2003.00803).
- Order-imbalance-based return predictability in Binance perps extends to 4-12h at quarter-hour marks, but it is a periodic algorithmic-trading effect — [arXiv 2607.09426](https://arxiv.org/html/2607.09426v1).

### Inferences
- LOB DL is the wrong tool for a 10k account trading 1h/4h bars. It requires tick data, co-location-grade latency and maker-fee economics.
- What survives to their horizon is aggregated flow features (imbalance, taker buy/sell ratio, open interest changes, funding). These can be fed into a tree model at 1h/4h without DL.

### Gaps
- No peer-reviewed study was found that shows LOB-derived DL signals remain profitable at horizons of 1h or more after fees.
- Kolm, Turiel and Westray's "Deep order flow imbalance" (Math Finance 2023), which reportedly finds order-flow inputs beat raw LOB and that predictability lasts about two average price changes, was not verified in this session.

---

## 5. Volatility forecasting with ML (HAR vs ML) and its use for sizing

### Takeaway
For realized volatility, linear HAR-type models are hard to beat. ML wins sometimes (LSTM for BTC, high-dimensional models with order-book and news data), but the economic value in volatility-timing portfolios favors simple models. Separately, out-of-sample volatility-managed portfolios often fail to raise Sharpe in equities (Cederburg et al. 2020), although vol scaling does reduce momentum crash risk, including in crypto. Upgrading HAR to ML for sizing is a low-priority, small-gain item.

### Cited Findings
- **Branco, Rubesam, Zevallos, "Forecasting realized volatility: Does anything beat linear models?" (J. Empirical Finance 2024) [PR]:** ten global stock indices. Simpler models without extra predictors deliver more economic value in volatility-timing portfolios, with no evidence that nonlinear ML statistically beats linear models in general — [ScienceDirect AM](https://www.sciencedirect.com/science/article/am/pii/S0927539824000598).
- **Crypto RV (BTC, ETH, LTC, XRP, 5-minute data) [PR]:** HAR "consistently" outperforms ML. LSTM wins some cases but overfits — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S156849462301150X). Note: the search snippets attribute the "HAR consistently wins" sentence and the "ML does not beat classical; HAR-RV beats GARCH" finding to overlapping sources, so the attribution is uncertain.
- **Bitcoin (Int. Fin. Markets, Inst. & Money 2024) [PR]:** LSTM dominates HAR across horizons, though ML does not always beat HAR — [Reading Centaur PDF](https://centaur.reading.ac.uk/118950/9/1-s2.0-S1042443124001306-main.pdf).
- **High-dimensional ML with LOB and news data (J. Empirical Finance 2026) [PR]:** beats HAR in 90% of the OOS period, except during extreme volatility. This is stocks — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S092753982600054X).
- **Cederburg, O'Doherty, Wang, Yan (JFE 2020) [PR]:** 103 equity strategies. Real-time OOS volatility-managed versions have lower Sharpe and CER than unmanaged ones for most strategies (72 of 103 underperform). Volatility-managed versions win on gross Sharpe in 53 of 103, with 8 significant — [Lehigh PDF](https://www.lehigh.edu/~xuy219/research/COWY.pdf); [CXO summary](https://www.cxoadvisory.com/?p=32455).
- **Large-cap crypto momentum (Financial Markets and Portfolio Management 2025) [PR]:** severe crashes, which volatility management mitigates — [Springer](https://link.springer.com/article/10.1007/s11408-025-00474-9).

### Inferences
- The gain from vol targeting comes mostly from scaling by any reasonable forecast (EWMA or HAR on 1h realized variance), not from ML accuracy. For trend and breakout systems, vol scaling mainly cuts tail and crash risk. That is valuable but already standard.
- A cheap, defensible upgrade is HAR on intraday realized variance from 1h or 5m data across their perps. ML-vol should be adopted only if it improves a portfolio-level OOS metric, not RMSE.

### Gaps
- No crypto study was found that directly shows ML-vol forecasts raise trend-strategy Sharpe relative to HAR or EWMA scaling.

---

## 6. Meta-labeling and ML filters on top of rule-based signals

### Takeaway
Meta-labeling (a secondary classifier deciding whether, and how much, to act on a primary rule signal) is conceptually well suited to a team with existing Donchian and breakout rules. However, the published evidence is thin: mostly author frameworks, single backtests and theses, with no peer-reviewed, out-of-sample, net-of-cost replication on crypto. Expect modest gains (better sizing or drawdown) at best. The key risk is that filtering trend trades cuts the right-tail winners that pay for trend following.

### Cited Findings
- **Joubert (J. Financial Data Science 2022), "Meta-Labeling: Theory and Framework" [PR, framework]:** meta-labeling sits on top of a primary strategy to size positions, filter false positives and improve Sharpe and max drawdown. It consolidates earlier ideas and is not a new empirical test — [Wikipedia summary with refs](https://en.wikipedia.org/wiki/Meta-Labeling).
- **arXiv 2005.12483 [WP]:** a baseline strategy's Sharpe rises from 0.36 to 0.74 with meta-labeling, and to 0.83 with feature selection. This is a single backtest — [arXiv](https://arxiv.org/pdf/2005.12483).
- **Insper thesis [thesis]:** backtest metrics improved over the primary model in all cases tested, but the ML models were weak, and the author calls for more testing — [Insper](https://repositorio.insper.edu.br/entities/publication/14261761-ee4f-4466-91e4-771dd445f258/full).
- López de Prado (2018), *Advances in Financial Machine Learning*, is the original source (triple-barrier labels, meta-labels, purged CV). It is a book, not an OOS study. No URL was checked in this session.

### Inferences
- With few trades per asset (Donchian on 7 assets yields perhaps a few hundred trades over years), a meta-model has too few labels. Pooling 100+ perps and both systems could give thousands of labeled events.
- Use meta-labeling probability for sizing, not hard filtering, to preserve trend right tails. Evaluate on portfolio Sharpe and skew with purged walk-forward.

### Gaps
- No peer-reviewed crypto meta-labeling OOS study was found.
- Hudson & Thames' published claims were not found or verified.

---

## 7. Image-based CNN (Jiang, Kelly, Xiu 2023) and crypto replications

### Takeaway
JKX (JF 2023) show that CNNs on OHLC chart images predict short-horizon (weekly or monthly) US stock return direction and transfer to other markets. Several code replications exist (US, China A-shares, a Russell 1000/ETF extension), but no rigorous crypto replication was found. The signal is a nonlinear price-trend and reversal pattern, again overlapping with trend.

### Cited Findings
- **Jiang, Kelly, Xiu, "(Re-)Imag(in)ing Price Trends" (JF 2023) [PR]:** CNN on price-chart images, with a binary label for a positive return over the forward horizon — [NUS PDF](https://www.aidf.nus.edu.sg/wp-content/uploads/2022/02/Xiu-Re-Imagining-Price-Trends.pdf); [ResearchGate](https://www.researchgate.net/publication/372876068_Re-Imagining_Price_Trends). [MEM] Very high Sharpe for equal-weighted 1-week decile long-short (gross) and much lower value-weighted; transfer to international markets. Verify the exact values.
- Replications: US plus China A-shares, including transfer and fine-tuning — [GitHub](https://github.com/George-hardworking/reimaging-price-trends-replication-and-extension). A production-scale extension on Russell 1000, ETFs and Nikkei 225 — [GitHub](https://github.com/ArjunDivecha/Pattern). A PyTorch implementation — [GitHub](https://github.com/lich99/Stock_CNN). A practitioner review — [LinkedIn, Rubesam](https://www.linkedin.com/pulse/re-imagin-price-trends-jiang-kelly-xiu-2023-alexandre-rubesam-bpfbe).

### Inferences
- The equal-weighted headline Sharpe in equities is driven by small stocks and short horizons, the same pattern as Avramov et al. In a 100-perp universe, a CNN is unlikely to beat gradient boosting on hand-built multi-horizon trend and volume features (the CTREND recipe) and is costlier to validate. Low priority.

### Gaps
- No crypto replication with OOS and costs was found.

---

## 8. Practical pitfalls: leakage, purged CV, multiple testing, regime shift, minimum data

### Takeaway
Most published ML-trading "edges" shrink because of design choices, version drift, small illiquid assets, backtest-date anachronism and multiple testing. For this team the binding constraint is data: 7 assets is far too few, and even 100 perps at 4h give a modest effective sample because cross-sectional returns are highly correlated (one dominant crypto beta factor) and regimes are short. Use purged and embargoed walk-forward, deflated Sharpe, and preregistration (which they already do in r51), and judge ML only by marginal contribution to the existing portfolio.

### Cited Findings
- **Design-choice dispersion:** CTREND Sharpe ranges roughly from 0.5 to 2.5 across 55,296 specifications, with a fat right tail from small, volatile coins — [JFQA](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/trend-factor-for-the-cross-section-of-cryptocurrency-returns/4C1509ACBA33D5DCAF0AC24379148178).
- **Version drift:** the Cakici et al. WP reported Sharpe 5.37, the published paper 1.66 — [AFFI](https://affi2023.eventsadmin.com/Papers/ViewContribution?cid=8390&h=A0CBBA4C296557EB2205D3ECCD9DBD7F); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1057521924001765).
- **Anachronistic testing-date bias** in full-sample ML backtests — [AFA](https://afajof.org/management/viewp.php?n=265916).
- **Hidden look-ahead:** the critique of KMZ flags current-month inflation data that is only released the following month — [Aalto GSF](https://gsf.projectsites.aalto.fi/wp-content/uploads/sites/10/2025/09/kmz.pdf).
- **Small-sample learning limits:** with short training windows, "little can be learned from the training data about the expected return function". Even decades of data are small relative to nonlinear predictor spaces — [Nagel 2025](https://voices.uchicago.edu/stefannagel/files/2025/07/Complexity_2.pdf).
- **Friction concentration:** ML profits concentrate in microcaps and distressed firms — [SSRN 3450322](https://papers.ssrn.com/abstract=3450322).
- **Meaningless metrics:** in LOB work, standard ML metrics mislead — [arXiv 2403.09267](https://arxiv.org/pdf/2403.09267).
- **Tiny R² is normal:** best-in-class daily OOS R² is near zero or negative (CatBoost about −0.03%, OLS about −0.47%), even when long-short Sharpe is high, so rank-based evaluation matters — [arXiv 2511.18578](https://arxiv.org/html/2511.18578v1).

### Inferences
Inferred minimum data conditions for ML to be worth trying:
1. **Universe:** at least 50-100 liquid perps with point-in-time listing and delisting, including dead perps to avoid survivorship.
2. **History:** at least 3-4 years of 1h data per asset where possible.
3. **Labels:** weekly or daily horizons, so that labels are numerous and not dominated by costs.
4. **Features:** a moderate feature set (multi-horizon returns, volatility, volume, funding, OI, basis) rather than thousands of features.
5. **Model:** a shrinkage linear model (ridge or elastic net, as CTREND does) or LightGBM with strong regularization.
6. **Validation:** walk-forward with a purge and embargo of at least the label horizon.
7. **Comparison:** against a plain multi-horizon momentum rank. ML must beat this, not just zero.
8. **Multiple testing:** account for the number of trials with a deflated Sharpe (Bailey and López de Prado).
9. **Live check:** a paper-trading or holdout period before capital.

### Gaps
- No source quantified the minimum crypto-perp sample for ML to beat a simple momentum rank OOS.
- The deflated Sharpe and Harvey-Liu-Zhu t > 3 references were not re-fetched in this session; they are standard (Bailey and López de Prado 2014; Harvey, Liu, Zhu 2016 RFS).
