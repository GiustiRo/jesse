# Regime detection, adaptive allocation and ensemble methods for a portfolio of rule-based sleeves (state of evidence, Oct 2026)

Context: trend ensemble on 7 assets plus crypto 4h breakouts. Portfolio Sharpe is about 1.5 and about 70% of quarters are positive. The weak spots are crypto bear and sideways markets, where the long trend sleeves lose 1-2% per quarter.

Source budget note: about 15 searches and fetches were made. Several primary PDFs were not opened: Goulding-Harvey-Mazzoleni, Baltas-Kosowski and Lopez de Prado HRP. Alpha Architect and IBKR returned HTTP 403. Where a figure comes from a secondary summary, these notes say so.

## 1. Regime detection (HMM, Markov-switching, statistical jump models, change-point, clustering): OOS evidence for timing trend or risk exposure

### Takeaway
Statistical jump models (JM) have the cleanest out-of-sample evidence among regime detectors. They beat both buy-and-hold and HMMs on equity indices after costs and delays. The gain shows up mostly as much shallower drawdowns and a Sharpe gain of +0.14 to +0.20. Every published test applies regimes to long-only beta (risk-on/risk-off), not to a trend portfolio. No peer-reviewed OOS test was found that uses a jump model to switch crypto trend sleeves, or to switch between trend and mean reversion.

### Cited Findings
- Shu, Yu and Mulvey, "Downside Risk Reduction Using Regime-Switching Signals: A Statistical Jump Model Approach". The strategy is 0/1: hold the asset or the risk-free asset. Features come only from the asset's own returns. The jump penalty, which favours persistent regimes, is chosen by time-series cross-validation that optimizes strategy performance. The test is out of sample on S&P 500, DAX and Nikkei from 1990 to 2023, with 10 bp one-way cost and a 1-day delay — [arXiv 2402.05272v3](https://arxiv.org/html/2402.05272v3)
- OOS results from the same paper (Table 4):
  - **S&P 500:** buy-and-hold Sharpe 0.48, MaxDD -55.2%. HMM 0.54, -28.9%. JM 0.68, -26.6%, CAGR 11.2% vs 10.2% for buy-and-hold.
  - **DAX:** buy-and-hold 0.30. HMM 0.35. JM 0.44, MaxDD -39.4% vs -72.7%.
  - **Nikkei:** buy-and-hold 0.12. HMM 0.19. JM 0.31.
  - **Effect sizes:** JM vs buy-and-hold adds +0.14 to +0.20 Sharpe and cuts MaxDD by 29-34 pp. JM vs HMM adds +0.09 to +0.14 Sharpe and +2.2 to +2.7 pp CAGR.
  - Source: [arXiv 2402.05272v3](https://arxiv.org/html/2402.05272v3)
- Delay robustness (Table 5): with 5- and 10-day delays the JM Sharpe stays above buy-and-hold on every index. For example, DAX JM goes 0.44 → 0.38 → 0.29. The HMM decays below buy-and-hold on DAX and Nikkei (DAX HMM 0.35 → 0.12 at 10 days). The paper reports no significance tests; each result is a single backtest path — [arXiv 2402.05272v3](https://arxiv.org/html/2402.05272v3)
- Shu and Mulvey follow-up, "Dynamic Asset Allocation with Asset-Specific Regime Forecasts". Sparse-JM labels are used to train an XGBoost classifier. The universe is 12 assets (equity, bond, REIT, commodity), with OOS from 2007 to 2023 and 5 bp cost. Each regime-aware portfolio is compared with the same portfolio without regimes:
  - **Equal weight:** Sharpe 0.51 → 0.91, MaxDD -37.5% → -17.6%.
  - **Min-variance:** 0.70 → 1.12, MaxDD -19.3% → -7.1%.
  - **Mean-variance:** 0.37 → 1.02.
  - **Turnover:** up sharply, for example EW 0.81 → 11.70. The cost sensitivity section was not read.
  - Source: [arXiv 2406.09578v1](https://arxiv.org/html/2406.09578v1)
- Aydinhan, Kolm, Mulvey and Shu extend the JM to continuous (soft) regime probabilities, published in Annals of Operations Research. Trading results were not checked — [SSRN 4556048](https://papers.ssrn.com/abstract=4556048)
- Nystrup (DTU thesis, 2014): an adaptively estimated 2-state Gaussian HMM strategy beats a rebalancing strategy OOS, after transaction costs and with a realistic delay. Only the abstract was read, so there are no Sharpe numbers — [DTU](https://www2.imm.dtu.dk/pubdb/pubs/6808-full.html)
- MPRA regime-based allocation paper (US, Japanese and German equity indices): the strategy is profitable OOS after costs, and volatility falls by 41% on average — [MPRA 21154](https://mpra.ub.uni-muenchen.de/21154/1/MPRA_paper_21154.pdf)
- Change-point detection inside a trend model: Wood, Roberts and Zohren, "Slow Momentum with Fast Reversion" (Journal of Financial Data Science). They add Bayesian online change-point features (GP-based) to a deep momentum network on futures. The CPD module raises Sharpe by about one-third over 1995-2020 and by about two-thirds over 2015-2020, when classic TSMOM underperformed — [arXiv 2105.13727](https://arxiv.org/abs/2105.13727); [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:b3a07fa5-b249-4b0b-894d-7545252ca258). The DeepAI aggregator quotes different figures (+33% over 1990-2020, about +400% for 2015-2020), which conflict with the arXiv and ORA versions — [DeepAI](https://deepai.org/publication/slow-momentum-with-fast-reversion-a-trading-strategy-using-deep-learning-and-changepoint-detection)
- The underlying online CPD algorithm (BOCPD) computes the exact posterior over the current run length online — [Adams & MacKay 2007](https://arxiv.org/abs/0710.3742)
- Kaminski and Lo, "When Do Stop-Loss Rules Stop Losses?" (J. Financial Markets 2014):
  - Under a random walk, 0/1 stop-loss rules always lower expected return. They add value only when returns have momentum or regime switching.
  - On monthly US data from 1950 to 2004, some stop-loss rules add 50-100 bp per month during stop-out periods.
  - The authors explain this with a regime-switching "flight-to-quality" model.
  - Source: [MIT DSpace](https://dspace.mit.edu/handle/1721.1/114876)
- A 2026 arXiv paper uses a 3-state HMM plus RL on SPY/TLT/GLD (2004-2025, 30% OOS) and beats passive SPY. It is weak evidence: there is no static-mix benchmark — [arXiv 2605.27848](https://arxiv.org/pdf/2605.27848)
- Crypto: no peer-reviewed JM/HMM regime-timing study of crypto trend strategies was found. Search hits were about Bitcoin volatility jumps (HAR-type forecasting), not trading regimes — [arXiv 1912.05228](https://ar5iv.arxiv.org/html/1912.05228)

### Inferences
- The robust mechanism is a persistence penalty: the JM jump cost, or equivalently hysteresis. It cuts whipsaw relative to an HMM, which is why the JM survives 5-10 day delays and the HMM does not. For a 4h crypto breakout sleeve, any regime filter should be judged on the same point: does it still help with a 1-5 bar delay and realistic costs?
- In these papers the regime gain is mostly drawdown avoidance in long-only beta. A trend sleeve already exits in persistent bears. So the marginal value of a regime overlay on trend is likely smaller than the +0.2 Sharpe seen on buy-and-hold. The most plausible target is the sideways, high-noise regime, where trend whipsaws. No paper found tests that directly.
- The Shu-Mulvey gains are inflated by comparison with naive no-regime baselines and depend on tuning the penalty by CV on strategy performance. That is a researcher degree of freedom, and it should be pre-registered if replicated.

### Gaps
- No OOS evidence was found for regime-switching between trend and mean reversion in crypto or equities from a peer-reviewed source.
- Nystrup et al. jump-model papers (2020-2021, e.g. "Learning hidden Markov models with persistent states by penalizing jumps", "Feature selection in jump models") were not retrieved, so their numbers are not reported.
- No significance tests or deflated-Sharpe adjustments were reported in the JM papers that were read.

## 2. Trend strategy improvements: dynamic leverage by trend strength, vol-of-vol, correlation de-risking, drawdown control, speed-mixing (Goulding-Harvey-Mazzoleni)

### Takeaway
Two improvements have the best evidence: correlation-adjusted leverage (Baltas-Kosowski) and blending slow and fast trend speeds (Goulding-Harvey-Mazzoleni). Volatility targeting helps tails everywhere, but it lifts Sharpe only for "risk assets" (equity, credit, and plausibly crypto). Trend-strength leverage should saturate rather than scale linearly. Stop-loss and drawdown rules help only when returns have momentum.

### Cited Findings
- **Baltas and Kosowski (Demystifying TSMOM):**
  - **Turnover:** better volatility estimators (e.g. Yang-Zhang) and better trend detection cut turnover by more than one-third, with no significant performance penalty.
  - **Post-2008 weakness:** the poor post-2008 TSMOM performance is explained by higher pairwise correlations across assets.
  - **Correlation-adjusted leverage:** a dynamic leverage mechanism based on signed pairwise correlations beats naive TSMOM, more so after 2008, and holds after costs.
  - **Sample:** 1974-2013 in the SSRN version, 1984-2013 in the 2017 version.
  - Source: [SSRN 2140091](https://papers.ssrn.com/abstract=2140091); [Imperial PDF](https://spiral.imperial.ac.uk/bitstream/10044/1/41472/4/SSRN-id2140091.pdf)
- Goulding, Harvey and Mazzoleni, "Momentum Turning Points" (JFE 2023, vol. 149(3), 378-406). Slow (about 12m) and fast (about 1m) TSMOM define four cycle states: Bull, Correction, Bear and Rebound. Intermediate-speed portfolios that blend slow and fast signals turn the predictive information about the cycle into positive unconditional alpha. A dynamic version re-weights speeds after Correction or Rebound states. When slow and fast signals disagree, a turning point is more likely — [Duke Scholars](https://scholars.duke.edu/publication/1586630); [SUFE abstract](https://academicnewsletter.sufe.edu.cn/info/354804); [Alpha Architect summary](https://alphaarchitect.com/trendfollowing/) (403 on fetch, snippet only). Specific Sharpe numbers were not retrieved.
- **Volatility targeting (Harvey, Hoyle, Korgaonkar, Rattray, Sargaison, Van Hemert, JPM Fall 2018; 60 assets):**
  - **Sharpe:** improves only for risk assets (equity, credit), which the authors tie to the leverage effect. The impact is negligible for bonds, FX and commodities.
  - **Tails:** extreme returns become less likely, and vol-of-vol falls, in every asset class.
  - **US equities:** Sharpe rises from 0.40 to 0.48-0.51 (this figure is from a secondary summary).
  - Source: [Duke PDF](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf); [Quantpedia](https://quantpedia.com/the-impact-of-volatility-targeting-on-equities-bonds-commodities-and-currencies)
- **Trend-strength sizing (Lempérière et al., "Two centuries of trend following", CFM 2014):**
  - **Long-run evidence:** the t-stat of trend excess returns is about 5 since 1960 and about 10 since 1800.
  - **Saturation:** returns show a clear saturation effect for large signals. Above some signal level, more strength adds no expected return.
  - **Decay:** long trends show no statistical degradation, but shorter trends have significantly withered.
  - Source: [arXiv/TrendFollowing PDF](https://www.TrendFollowing.com/whitepaper/Two_Centuries_Trend_Following.pdf); [CXO summary](https://www.cxoadvisory.com/technical-trading/trend-following-over-the-very-long-run/)
- **Drawdown and stop-loss control:** stop-loss rules add value only when returns have momentum. In daily futures data, some volatility-based stop rules raise return and cut volatility substantially — [Kaminski & Lo, MIT DSpace](https://dspace.mit.edu/bitstream/handle/1721.1/114876/Lo_When%20Do%20Stop-Loss.pdf). A secondary summary quotes about +1.5% per month on 1993-2011 futures, which is not verified — [CXO](https://www.cxoadvisory.com/?p=1809)
- **Crypto trend:** Zarattini, Pagani and Barbon, "Catching Crypto Trends" (SFI RP 25-80, 2025), aggregate Donchian-channel models across several lookbacks with vol-based sizing. Applied to a rotation over the top-20 liquid coins, the result is net Sharpe above 1.5 and 10.8% annual alpha vs BTC — [IDEAS/SFI](https://ideas.repec.org/p/chf/rpseri/rp2580.html); [Concretum](https://concretumgroup.com/catching-crypto-trends-a-tactical-approach-for-bitcoin-and-altcoins/). A separate intraday BTC long-short trend ensemble has gross Sharpe of about 1.6 over 2018-2025 — [Concretum](https://concretumgroup.com/seasonality-in-bitcoin-intraday-trend-trading/)
- A 2025 arXiv paper on trend signal design ("Breaking the Trend: How to Avoid Cherry-Picked Signals") cites the Sepp-Lucic taxonomy, in which "European" trend following uses continuous positions proportional to signal strength — [arXiv 2504.10914](https://arxiv.org/html/2504.10914v4)

### Inferences
- For bleeding in sideways markets, speed-mixing is the best-supported structural fix. Holding slow and fast blends, and cutting size when slow and fast disagree, targets exactly the whipsaw and turning-point losses. It also needs no fitted regime model.
- Correlation-aware leverage matters when the 7 assets plus crypto become highly correlated, as in 2022 risk-off. In the Baltas-Kosowski framework, high signed correlation among the active trend positions means less diversification, so leverage should drop.
- Crypto behaves like a risk asset with a leverage effect. Vol targeting on the crypto sleeve should therefore plausibly lift Sharpe, not just trim tails, based on the Harvey et al. asset-class split (an inference that has not been tested on crypto here).
- Sizing positions linearly with breakout or trend strength is not supported. Capped or saturating sizing is the evidence-consistent choice.

### Gaps
- No primary source was found for a vol-of-vol filter on trend (enter or size only when vol-of-vol is low) with OOS numbers.
- Sharpe figures for the GHM intermediate and dynamic strategies were not retrieved, because the paper and summaries could not be fetched.
- No peer-reviewed evidence was found that drawdown-based de-risking of a trend portfolio (e.g. cutting exposure after an X% drawdown) improves OOS Sharpe. Kaminski-Lo concerns stop-losses on buy-and-hold.

## 3. Online learning / bandits / Bayesian model averaging / performance-based ensemble weighting vs equal weight

### Takeaway
The default is equal weight (or equal risk). Estimated combination weights usually lose out of sample to equal weights because of estimation error: this is the "forecast combination puzzle" and DeMiguel's 1/N result. Weighting sleeves by recent performance has mixed evidence. Short-horizon factor momentum shows some persistence, but long-horizon performance chasing reverses. No credible OOS evidence was found that bandit allocation among trading strategies beats equal weight.

### Cited Findings
- **DeMiguel, Garlappi and Uppal (RFS 2009):**
  - **Main result:** across 14 optimized models and 7 datasets, none consistently beats 1/N on Sharpe, certainty-equivalent return or turnover. Estimation error offsets the gains from optimization.
  - **Window needed:** for optimization to win, the estimation window must be about 3,000 months for 25 assets and more than 6,000 months for 50 assets.
  - Source: [LBS](https://london.edu/faculty-and-research/academic-research/o/optimal-versus-naive-diversification-how-inefficient-is-the-1n-portfolio-strategy-p7805); [NBER draft](https://conference.nber.org/confer/2006/si2006/ap%5Cuppal.pdf)
- A 2024 replication with 20 years of data still finds 1/N hard to beat. More strategies beat it than in the original, but changing window length or limiting costs does not beat it systematically — [Gelmini & Uberti 2024](https://boa.unimib.it/handle/10281/488299). Critics such as Kritzman et al. argue that the 1/N edge comes from short rolling estimation windows — [Collins blog summary](https://jasoncollins.blog/posts/the-1-n-portfolio-versus-the-optimal-strategy)
- **Forecast combination puzzle:** a simple equal-weight average often beats estimated "optimal" combination weights (Stock & Watson 2004). Smith and Wallis (2009) blame estimation error in the weights. Claeskens et al. show that random estimated weights can bias combinations of unbiased forecasts. Some studies find optimal weights can win (Genre et al. 2013; Hsiao & Wan 2014) — [Forecast combinations: 50-year review, arXiv 2205.04216](https://arxiv.org/pdf/2205.04216)
- **Performance-based timing:**
  - **Short-horizon persistence:** Gupta and Kelly time 65 factors on their own past returns. 61 of 65 earn positive timing returns, 47 have significant alpha, and the combined Sharpe is 0.84. Dimensional argues that costs and fees remove the benefit — [Institutional Investor](https://www.institutionalinvestor.com/article/2bswk7762zwxielme1t6o/portfolio/factor-momentum-is-real-researchers-argue)
  - **Long-horizon reversal:** Ali, Daniel and Hirshleifer, "One Brief Shining Moment(um)", find that after strong 2-year momentum performance, momentum portfolios earn strongly negative returns 2-5 years later. This is a style-chasing reversal — [Alpha Architect](https://alphaarchitect.com/?p=96947) (search snippet)
- Fund-level evidence: momentum trading alone does not lead to better performance, but funds with momentum-timing ability do outperform — [vLex abstract](https://eu.vlex.com/vid/do-fund-managers-time-1049455133)

### Inferences
- With 2 sleeve families and a few sub-sleeves, the expected gain from learned weights is small and the estimation-error cost is large. Risk-budgeted equal weighting (equal vol contribution) is the evidence-consistent baseline. Any adaptive scheme should shrink heavily toward it, e.g. at most ±25% tilts, slow updates of 12m or more, and an out-of-sample holdout.
- Down-weighting the crypto long sleeve after recent losses is performance chasing on a 1-2 quarter horizon. The evidence for persistence at that horizon exists only for factors (Gupta-Kelly), not for trend sleeves, and reversals occur. Prefer state-based de-risking (trend agreement, correlation, vol) over P&L-based de-risking.

### Gaps
- No peer-reviewed OOS study was found comparing bandit or online-learning allocation (EXP3, Thompson sampling, exponentiated gradient) among trading strategies against equal weight. Online portfolio selection literature exists (Universal Portfolios, EG) but was not retrieved here.
- No source was found on Bayesian model averaging specifically across trading strategies with OOS Sharpe.

## 4. Conformal prediction / uncertainty-aware position sizing

### Takeaway
The evidence is thin and so far negative or neutral. The only direct pre-registered test of conformal-interval-scaled Kelly sizing underperformed equal weight out of sample. Non-conformal uncertainty sizing helped in one ML futures study. Conformal methods give calibrated coverage, not alpha.

### Cited Findings
- **Conformal Kelly (arXiv 2608.01494, pre-registered):** the half-width of a 75% conformal interval scales a capped fractional-Kelly rule.
  - **Data:** developed on 8 US ETFs over 2016-2021, with a sealed test on 2022-2024.
  - **Coverage:** 0.745 vs the 0.750 target.
  - **Growth:** net log growth of 8.5% and 7.0%, vs 9.5% for equal weight and 15.6-16.8% for leveraged passive.
  - **Ranking:** both configurations ranked last of 11 on Sharpe and Calmar.
  - **Drawdown:** the drawdown control failed its registered criterion.
  - Source: [arXiv 2608.01494](https://arxiv.org/pdf/2608.01494)
- Conformal Predictive Portfolio Selection (Kato) uses conformal intervals for asset selection and weighting. It is a framework paper — [arXiv 2410.16333](https://arxiv.org/html/2410.16333v2)
- Conformal stock selection (PMLR 2025) reaches near-nominal coverage but implements no sizing rule — [PMLR v266](https://proceedings.mlr.press/v266/kaya25a.html)
- Spears, Zohren and Roberts scale Eurodollar futures positions by deep-learning prediction uncertainty and report better Sharpe than uncertainty-agnostic sizing. This is not conformal — [arXiv 2007.15982](https://arxiv.org/abs/2007.15982)

### Inferences
- For rule-based sleeves without a return-forecasting model, conformal sizing has nothing to calibrate. Volatility targeting already provides a crude uncertainty scaling with stronger evidence.

### Gaps
- No independent replication was found, and no crypto application of conformal sizing.

## 5. Hierarchical risk parity / correlation-regime-aware allocation vs inverse-vol

### Takeaway
HRP's OOS edge over inverse-vol or equal risk contribution is not established. Results depend on data and covariance estimates, and with crude covariance estimates inverse-vol is the more robust choice. With fewer than about 10 sleeves, hierarchical clustering adds little.

### Cited Findings
- An Indian study finds that with crude covariance estimates, inverse-volatility portfolios are the most robust, followed by the ML-based portfolios. HRP sits between minimum variance and inverse vol — [IISc](https://eprints.iisc.ac.in/77367/1/ris_7-3_2019.pdf)
- A Brazilian OOS study finds HRP generally does not perform best but matches other approaches on some measures — [RBFin/FGV](https://periodicos.fgv.br/rbfin/article/download/89848/84802/201368)
- A Monte Carlo critique (not peer-reviewed) argues that HRP's partial neglect of correlations gives worse OOS results than an ERC benchmark, and that recursive bisection can split assets of the same cluster — [Substack essay](https://symbolmanipulation.substack.com/p/essay-6-a-better-benchmark-for-hierarchical)
- Raffinot, HCAA (JPM 2018): uses a bootstrap model-confidence-set procedure against data snooping and claims statistically better risk-adjusted OOS performance than common optimizers across 3 datasets — [SSRN 2840729](https://papers.ssrn.com/abstract=2840729)
- The correlation-regime angle is covered by Baltas-Kosowski correlation-adjusted leverage in section 2 — [SSRN 2140091](https://papers.ssrn.com/abstract=2140091)

### Inferences
- Use inverse-vol or ERC across sleeves. Spend the correlation information on total leverage (de-risk when the sleeves' P&L correlation spikes) rather than on HRP's cross-weights.

### Gaps
- The original Lopez de Prado (2016) HRP OOS Monte Carlo figures were not retrieved, nor any large head-to-head HRP vs inverse-vol meta-analysis.

## 6. What actually lifts hit-rate/regularity of a trend portfolio without killing returns

### Takeaway
The best-evidenced levers for regularity, in rough order, are:
1. Diversifying across speeds and lookbacks (ensembles, slow/fast blends).
2. Volatility targeting, which lifts Sharpe in risk assets like crypto.
3. Correlation-aware leverage.
4. A persistence-penalized regime filter (jump model) to avoid whipsaw states.

Fitted, performance-chasing weights and conformal or bandit schemes lack OOS support.

### Cited Findings
- Blending slow and fast momentum turns turning-point information into positive unconditional alpha — [Goulding, Harvey & Mazzoleni, JFE 2023](https://scholars.duke.edu/publication/1586630)
- Aggregating Donchian models across lookbacks with vol sizing gives net Sharpe above 1.5 in crypto — [Zarattini et al. 2025](https://ideas.repec.org/p/chf/rpseri/rp2580.html)
- Volatility targeting lowers the likelihood of extreme returns in all asset classes and raises Sharpe in risk assets — [Harvey et al. 2018](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf)
- Correlation-adjusted leverage fixes post-2008 TSMOM underperformance after costs — [Baltas & Kosowski](https://papers.ssrn.com/abstract=2140091)
- A jump-model 0/1 filter cuts MaxDD by about 30 pp and adds +0.14 to +0.20 Sharpe on equity indices OOS, and survives 10-day delays — [Shu, Yu & Mulvey](https://arxiv.org/html/2402.05272v3)
- Change-point features raise deep-momentum Sharpe by about 1/3 (about 2/3 over 2015-2020) — [Wood, Roberts & Zohren](https://arxiv.org/abs/2105.13727)
- Equal-weight combinations are hard to beat OOS — [DeMiguel et al.](https://london.edu/faculty-and-research/academic-research/o/optimal-versus-naive-diversification-how-inefficient-is-the-1n-portfolio-strategy-p7805); [Forecast-combination review](https://arxiv.org/pdf/2205.04216)

### Inferences
These are hypotheses to test under pre-registration with costs and delay. None was tested by these sources on this portfolio.
- **(a) Crypto long sleeves: fast/slow agreement gate.** Cut size by about 50% when a fast trend (around 20 bars on 4h, or 1m daily) disagrees with a slow one (around 12m-equivalent). This is GHM-style and targets the sideways bleed.
- **(b) BTC-only jump-model filter.** Use 2 states on BTC daily return features, with the jump penalty fixed ex ante (not CV-optimized on the same data), applied as a risk-off overlay for the crypto long sleeves only.
- **(c) Sizing.** Vol-target each crypto sleeve and cap signal-strength scaling.
- **(d) Correlation de-risking.** Scale portfolio leverage down when the average pairwise correlation of active positions is high (Baltas-Kosowski).
- **(e) Sleeve weights.** Keep equal risk across sleeves.

Expected effect sizes from the literature are modest: about +0.1 to +0.2 Sharpe from a regime filter on a beta-like exposure, less on trend. Regularity gains come mostly from cutting losing quarters, not from adding winning ones. Shallower drawdowns are much better documented than higher hit rates.

### Gaps
- No source quantified a regime method's effect on the share of positive months or quarters of a trend portfolio. All the evidence is on Sharpe and MaxDD.
- No OOS evidence was found for regime switching between trend and mean-reversion sleeves in crypto.
