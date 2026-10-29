# Systematic SHORT strategies that pay on their own: crypto perps (Binance USDT-M, 1h-4h-daily), commodities and bonds (as of Oct 2026)

Scope note: about 14 search/fetch calls. Several primary PDFs (SSRN, AUT) returned 403 or unreadable binary, so some numbers come from search snippets and are marked as such. No figure below was invented. Anything without a source is in Inferences or Gaps.

## 1. Cross-sectional crypto factors on the short leg (momentum, reversal, size, illiquidity, volatility)

### Takeaway
The academic crypto factors (market, size, 1-4 week momentum) are real, but their short legs contribute little or lose money. Momentum losers do not keep falling (the weekly P1 return is about 0), and momentum's short leg carries the crash/jump risk. On a liquid Binance perp universe, a recent out-of-sample test finds no exploitable cross-sectional alpha net of costs. A standalone "short the factor losers" sleeve has no credible OOS support.

### Cited Findings
- Liu, Tsyvinski and Wu (JF 2022) find that three factors (crypto market, size, momentum) explain the cross-section. Their long-shorts are weekly quintile sorts (Q5 minus Q1), and 9 (WP version) or 10 (published abstract) characteristics give significant long-short returns, all spanned by the 3-factor model — [NBER w25882](https://www.nber.org/system/files/working_papers/w25882/w25882.pdf); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3379131)
- Borri, Liu, Tsyvinski and Wu (arXiv 2510.14435, v4, 2025) report weekly P5-P1 returns, roughly Jan 2014 to Sep 2025:
  - CMOM (2-week momentum): +2.6%/wk full sample (t=3.89) and +2.1%/wk post-2020 (t=3.70).
  - CSIZE: -2.3%/wk (t=-2.66) full sample and -0.9%/wk post-2020 (t=-1.69).
  - CVALUE: -3.5%/wk full sample and -2.3%/wk post-2020.
  - The momentum short-side portfolio (P1) earns -0.2%/wk full sample and +0.1%/wk post-2020, i.e. about zero. Momentum's spread comes from winners, not from losers falling.
  - No transaction costs are reported for the factor strategies.
  - [arXiv 2510.14435 HTML](https://arxiv.org/html/2510.14435)
- An AUT working paper on TS and CS crypto momentum (date not verified) says, per the search snippet, that CS momentum profit comes mostly from the long leg and the short leg faces high jump risk and loses money. Its best configuration is a 14-day lookback with 7-day hold, Sharpe 1.28 vs 1.01 for the market. Shorts are typically implemented via perps — [AUT ACFR PDF](https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf) (403 on fetch, snippet only)
- Crypto CS momentum over 147 coins, Jan 2015 to Jun 2022: mean -8.02%/month, vol 34.28%, skewness -4.135 (snippet). Crashes come from an extreme price jump in a single short-leg coin, not from market rebounds as in equities. Momentum yields no significant payoff after fat tails, and risk management only partly helps — [Financial Markets and Portfolio Management 2025, "Cryptocurrency momentum has (not) its moments"](https://link.springer.com/article/10.1007/s11408-025-00474-9); [Stop-loss rules and momentum payoffs in cryptocurrencies](https://www.sciencedirect.com/science/article/abs/pii/S2214635023000473)
- Over 2,000 coins, momentum is positive up to 2-4 weeks and reverses at longer horizons (snippet) — [Dobrynskaya, Cryptocurrency Momentum and Reversal](https://conference.hse.ru/files/download_file_ex?hash=FAE0AB2DC7A67656E89A0B1CB27D8C7D&id=3B5EE9A5-0B18-458A-9458-B4ED0F6C6664)
- Short-term reversal (daily, weekly, monthly) across 200 coins, 2015-2019, survives size, turnover and illiquidity controls. It is strongest in small, illiquid coins, and the authors interpret it as inefficiency plus compensation for liquidity provision — [Cryptocurrency return reversals, Fairfield](https://digitalcommons.fairfield.edu/cgi/viewcontent.cgi?article=1249&context=business-facultypubs); [Zaremba et al. 2021, "Up or down?"](https://www.researchgate.net/publication/354881251_Up_or_down_Short-term_reversal_momentum_and_liquidity_effects_in_cryptocurrency_markets)
- Crypto short-term-reversal returns concentrate in smaller, less liquid, more volatile assets and proxy for liquidity-provision earnings — [J. Banking & Finance 2025, Returns from liquidity provision in crypto](https://www.sciencedirect.com/science/article/pii/S0378426625000317)
- In equities, the reversal short leg comes from sentiment-driven overpricing that persists because of short-sale constraints, while the long leg reflects liquidity shocks/fire sales — [Short-Term Return Reversal: The Long and the Short of It](https://econ.sufe.edu.cn/_upload/article/files/d9/42/ca203afb44b38fcefab0073159b6/f6215523-0e6a-4121-a857-52a82a650aea.pdf)
- A 2026 SSRN post-mortem (Fayez Junior) tests 10 Binance USDT-M perps, Jul 2022 to Apr 2026. Long-short CS models on OHLCV plus funding at an 8h horizon show no exploitable alpha: the naive linear model's net Sharpe is -3.22, and the best model has a weakly positive IC but net Sharpe -2.91 — [SSRN 6701738](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6701738)
- Wang and Pang ("Predictability on the Move", SSRN) test 1,043 signals on a point-in-time Binance universe. Predictability migrates across signals and sample periods rather than residing in a stable factor set (snippet; full text 403) — [SSRN 7556359](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7556359)
- A non-peer-reviewed course project on hourly perp CS ML finds a "real but fast-decaying microstructure edge" that is sensitive to costs and lag — [GitHub crypto-perps-alpha](https://github.com/IliassSjm/crypto-perps-alpha)

### Inferences
- The short leg of size, momentum and reversal sorts sits in small, illiquid, high-vol alts. That is exactly where perp availability, funding (often negative, so shorts pay when shorts are crowded), borrow, slippage and listing/delisting survivorship are worst. Gross academic spreads (built on CoinMarketCap-style spot data, weekly, without costs) should not be read as perp-implementable short alpha.
- Momentum's short leg has negative skew from idiosyncratic squeezes. A short-losers sleeve is structurally exposed to the same squeeze risk that hurts the team's breakdown shorts.
- If anything is usable, it is short-term reversal applied to *winners* (short recent extreme outperformers). The literature's interpretation (liquidity provision, sentiment overpricing protected by short constraints) gives the short leg a mechanism. Costs are the binding constraint, though, and no source quantified net-of-cost perp results.
- The post-2020 decay of size and value, the 2026 negative perp CS result, and the "migrating predictability" finding all point to data-mining and decay risk. Treat any single-period CS short signal as suspect without a frozen holdout.

### Gaps
- I found no paper that reports the short leg of crypto factor portfolios net of perp funding and trading costs on Binance USDT-M specifically.
- Illiquidity and idiosyncratic-volatility factor short-leg numbers in crypto were not retrieved (the arXiv 2211.13274 IVOL paper appeared but was not read).
- The AUT paper's date and exact short-leg numbers are unverified (403).

## 2. Overextension / exhaustion shorts at 1h-4h (intraday reversal after extreme moves)

### Takeaway
Intraday crypto shows statistically robust short-horizon reversal, concentrated after aggressive taker-flow moves. The best recent measurement (15-min bars, 183 Binance pairs, 2021+) puts the gross edge at about 1.3 bp per trade against about 5 bp round-trip costs, so it is not tradable at that horizon. At 1-4h, older BTC evidence shows negative autocorrelation that grows with move size, but evidence is mixed: some studies find momentum on overreaction days, and the strongest reversals follow *negative* shocks, which favours longs, not shorts.

### Cited Findings
- Kitron and Wengrowicz (arXiv 2608.21888, Aug 2026) measure 15-min reversal across 183 Binance pairs, every coin-year since 2021, with a frozen 6-month holdout:
  - About 90% of pairs show significant directional reversal, vs 2.7% of 187 US stocks/ETFs.
  - The signal lies in sign, not magnitude, and concentrates after aggressive taker-flow moves, growing with flow intensity. Book depth consumed does not condition it, consistent with compensated liquidity provision.
  - The gross edge peaks near 1.3 bp/trade vs a 5 bp round trip, "too small to clear" costs.
  - Replication code is public.
  - [arXiv 2608.21888](https://arxiv.org/abs/2608.21888)
- BTC shows significant negative first-order autocorrelation at 1h, 2h and 4h, and bigger moves are followed by bigger reversals, partly attributed to overreaction — [Ledger 2021, On the Intraday Behavior of Bitcoin](https://ledger.pitt.edu/ojs/ledger/article/download/213/212/1232)
- Intraday reversal is described as unique to crypto and linked to overreaction to non-fundamental information and overconfidence — [On the intraday return curves of Bitcoin, IRFA](https://www.sciencedirect.com/science/article/abs/pii/S1057521921001228)
- Caporale and Plastun (2019) find that on one-day overreaction days, prices tend to continue in the direction of the move until the day closes (momentum, not reversal) — [CESifo WP 7917](https://ideas.repec.org/p/ces/ceswps/_7917.html)
- Contrarian profit in crypto peaks at a formation window of about 10 minutes and declines toward 60 minutes (snippet) — [Intraday return predictability in crypto: momentum, reversal, or both, NAJEF 2022](https://www.sciencedirect.com/science/article/abs/pii/S1062940822000833)
- After a 5% intraday BTC drop, the average cumulative return is about +2.4% six hours later (overreaction to negative shocks). The reversal is on the downside, which supports buying dips — [Intraday Bitcoin price shocks: when bad news is good news, T&F 2022](https://www.tandfonline.com/doi/full/10.1080/15140326.2022.2151253)
- Per snippets: for BTC daily (2026 study), moderate positive shocks continue, while extreme negative moves reverse more. For ETH, predictability after extremes appears only after positive shocks, with no comparable BTC effect — [ResearchGate, lagged momentum/reversal BTC-ETH day/overnight](https://www.researchgate.net/publication/414070255_On_the_Performance_of_Lagged_Momentum_and_Reversal_Strategies_Across_Daytime_and_Overnight_Sessions_in_Bitcoin_and_Ethereum_Cryptocurrencies)

### Inferences
- The asymmetry matters for the team. Upside extremes in BTC tend to *continue* short-term, while downside extremes revert. A naive "short after a large up-hour" fades the side with weaker reversal evidence. An exhaustion short would need extra conditioning, such as taker-flow intensity (per Kitron-Wengrowicz) plus crowding (funding/OI, section 3), and probably works better on alts than BTC (the ETH positive-shock result hints at this, but the evidence is thin).
- At 15-min the edge is below cost. Going to 1h-4h must raise the gross edge per trade by an order of magnitude to be viable on Binance taker fees (about 4-5 bp per side for VIP0 USDT-M taker; Binance fee schedule not fetched here). Using maker entries could change the economics.

### Gaps
- I found no study of 1h-4h reversal conditioned on OI change or funding for altcoin perps with net-of-cost results.
- The exact effect sizes for the Ledger 1-4h autocorrelation were not retrieved.

## 3. Crowding indicators (funding extremes + OI growth, basis, long/short ratio) predicting down moves

### Takeaway
I found no peer-reviewed cross-asset (beyond BTC/ETH) evidence that funding plus OI extremes predict altcoin declines out of sample. The documented, monetisable "crowding" edge is the carry/funding premium (short perp, long spot). That premium has decayed sharply: Sharpe 6.45 over 2020-25, 4.06 from 2024, negative in 2025. Practitioner sources agree that funding signals positioning cost, not timing.

### Cited Findings
- Crypto carry (short Binance perp, long spot, 8h funding), Aug 2020 to May 2025: Sharpe 6.45 full sample, 4.06 from 2024, negative in 2025. Funding averages about 8%/yr with about 0.8% vol, and the paper attributes the decline to compressed or more volatile funding premia (e.g., the growth of Ethena) — [Borri et al. arXiv 2510.14435](https://arxiv.org/html/2510.14435)
- Funding-rate *level* forecasting for BTC on Binance/Bybit is OOS-predictable, but this concerns the funding rate itself, not the cross-section of returns — [Inan, SSRN 5576424 (Oct 2025)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5576424)
- Binance OHLCV + funding cross-sectional signals on 10 large perps (2022-2026) give a negative net Sharpe, i.e. no exploitable alpha at 8h — [SSRN 6701738](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6701738)
- An open GitHub backtest of an altcoin OI crowding/unwind signal on Binance fired only 3 times OOS, which its author calls far too few to conclude anything. It uses one venue and no funding filter — [kentsmallt/alt-oi-signal](https://github.com/kentsmallt/alt-oi-signal)
- Funding is computed from the premium only, with OI, L/S ratio and liquidations absent. Funding often sits at the 0.01% floor (78% of a quarter), so it registers crowding only once it starts lifting offers — [Coincub](https://coincub.com/blog/perpetual-futures-funding-rates-78-of-a-quarter-at-0-01/)
- Practitioner views:
  - MetaMask: funding is not a standalone predictor and gains signal when paired with OI, volume and depth — [MetaMask](https://metamask.io/news/monitoring-perps-funding-rate-trends-signals)
  - BloFin: funding shows positioning cost, not timing — [BloFin](https://blofin.com/en/academy/education/trading/crypto-funding-rates)
- Coin Metrics provides OI-weighted aggregated funding (8h/1d/30d/1y) and liquidation buy/sell volume (5m/1h/1d aggregated; pair-level 1h/1d), positioned for gauging crowding and squeezes — [Coin Metrics funding docs](https://docs.coinmetrics.io/market-data/market-data-overview/funding-rate-metrics); [liquidation docs](https://docs.coinmetrics.io/market-data/market-data-overview/liquidation-metrics)
- In the Oct 2025 tariff-shock deleveraging, about $19B was liquidated — [21Shares](https://www.21shares.com//research/record-crypto-liquidations-amid-tariff-shock)

### Inferences
- The only robust, published "short" edge tied to crowding is being *paid* funding while delta-hedged. That is market-neutral but is now near zero or negative after the 2024-25 compression. Its tail risk is episodic funding flips and basis blowouts.
- Funding plus OI as a *directional* short trigger remains a hypothesis. The floor at 0.01% means funding is uninformative most of the time. Only rare extremes carry information, so samples are small (cf. the 3-event OOS above). This is a classic data-mining trap, and preregistration plus a pooled multi-coin event study would be needed.
- The mechanism is plausible: crowded leveraged longs plus thin alt liquidity lead to liquidation cascades on small shocks (Oct 2025). Timing the shock is the hard part, so the crowding signal is better used as a *sizing/permission* filter for shorts than as an entry.

### Gaps
- I found no academic study using Binance long/short-ratio extremes or basis extremes to predict altcoin returns OOS.
- No Kaiko research on this was retrieved. The BIS "crypto carry" WP (Schmeling-Schrimpf-Todorov) findings on carry predicting crashes and liquidations could not be verified in this pass.

## 4. Token supply events (unlocks/vesting)

### Takeaway
The pre-unlock drift is the best-supported short-side "event" in crypto, but it is concentrated in **newly listed, thin-float tokens with large non-insider/cliff unlocks**, about -16% vs matched peers. It is insignificant for established tokens. The drift occurs mostly in the month *before* the unlock, since schedules are public. Evidence is vendor-produced, single-cycle and correlational.

### Cited Findings
- Tokenomist study:
  - One-month pre-event median -14.7% (p<0.001, n=164) and two-week pre-event median -9.1% (descriptive, uncontrolled). Against BTC, the 1-month median is -16.26% (n=236), and 72.5% of events are lower one month later.
  - Matched-peer overall median -4.85%. Established tokens -2.57% (p=0.42, not significant). Newly listed tokens -16.02%. A placebo control -1.07% (p=0.47).
  - The effect tracks unlock size relative to thin float, not insider status, and non-insider tranches fall more than insider ones.
  - Single market cycle, and the study explicitly says it cannot establish a tradable edge after costs and timing.
  - [Tokenomist, Unlock Price Impact](https://tokenomist.ai/learn/glossary-term/unlock-price-impact)
- Streamflow finds a similar split: thin-float tokens fall about 15% vs age-matched peers, with no significant effect for high-liquidity tokens. Cliff unlocks hit harder than linear ones — [Streamflow report](https://streamflow.finance/blog/token-unlock-report); [Streamflow: do unlocks cause drops](https://streamflow.finance/blog/do-token-unlocks-cause-price-drops)
- The widely quoted Keyrock "90% of 16,000+ unlocks create negative pressure" claim is reproduced by Gate, which also notes the overall price impact is not significant. Keyrock's methodology was not available to verify — [Gate](https://www.gate.com/news/detail/8097004)
- Counter-examples: ApeCoin gained about 16% (size-weighted) in the 15 days before cliff unlocks, and TRUMP rose through a >20% supply increase after a short squeeze — [Tokenomist](https://tokenomist.ai/learn/glossary-term/unlock-price-impact)

### Inferences
- Tradable form: short newly listed, low-float perps about 30 days before a large (relative to circulating float) cliff unlock, hedged with BTC or a sector basket, and exit at or around the unlock. The mechanism is anticipated supply plus the hedging/pre-selling of recipients (perp shorts by unlock recipients), plus thin float.
- Risks:
  - Squeezes in thin-float names, where crowded shorts produce negative funding that the short pays (TRUMP example).
  - Look-ahead bias in unlock calendars, since schedules get revised.
  - Survivorship, since delisted tokens drop out.
  - The overlap with "new listing underperformance" generally. The -16% may be a new-listing effect rather than an unlock effect, so it must be controlled.
- This is the candidate with the clearest mechanism and a market-neutral form, but it needs an in-house event study on Binance perps with funding and costs.

### Gaps
- No peer-reviewed academic paper on crypto unlock event returns was found in this pass (equity lockup analogue: Field-Hanka, Gompers; not examined).
- No net-of-funding perp backtest was found.
- Messari data coverage was not checked.

## 5. Downside asymmetry / volatility-of-volatility: do fast short models capture crashes?

### Takeaway
Crypto return distributions and momentum strategies are strongly negatively skewed, and crashes are fast and jumpy. The intraday evidence, however, says downside extremes tend to *revert* (dip-buying pays) rather than continue. I found no published OOS evidence that a fast (intraday or short-lookback) short-side trend model is profitable on its own outside bear markets.

### Cited Findings
- Crypto CS momentum has skew of about -4.1 and crashes driven by single-coin jumps in the short leg — [FMPM 2025](https://link.springer.com/article/10.1007/s11408-025-00474-9)
- After a 5% intraday BTC drop, the market is about +2.4% after 6h on average (negative-shock overreaction) — [T&F 2022](https://www.tandfonline.com/doi/full/10.1080/15140326.2022.2151253)
- Negative extreme moves show stronger reversal than positive ones in BTC daily data (2026 study, snippet) — [ResearchGate](https://www.researchgate.net/publication/414070255_On_the_Performance_of_Lagged_Momentum_and_Reversal_Strategies_Across_Daytime_and_Overnight_Sessions_in_Bitcoin_and_Ethereum_Cryptocurrencies)
- A practitioner analysis argues that a skewness signal adds information beyond volatility for daily momentum timing, and survives costs for cheap traders — [Bianchi Substack](https://danielebianchi.substack.com/p/what-volatility-misses-in-momentum)
- Momentum's crypto crash pattern is described qualitatively as "beautiful returns and catastrophic crashes" — [Tommi Johnsen Substack](https://tommijohnsen.substack.com/p/crypto-momentum-has-beautiful-returns)

### Inferences
- "Crypto falls faster than it rises" means a short model must react within hours. But the fastest drops (liquidation cascades) also mean-revert within hours (+2.4% after 6h for -5% shocks). A fast short therefore tends to enter late into a cascade and get stopped by the rebound. This is consistent with the team's experience that breakdown shorts act only as crisis insurance.
- A more coherent use of the asymmetry is to *sell premium against crowding* (funding carry) or *fade upside overextension* in crowded alts. Chasing downside breakdowns is the less supported option.

### Gaps
- I found no paper testing short-lookback, intraday time-series short-only models on Binance perps with OOS and costs.
- No vol-of-vol (e.g., DVOL-based) short-timing evidence was retrieved.

## 6. Bonds and oil: systematic short-side approaches (brief)

### Takeaway
I found no source showing a standalone *short-only* systematic edge in Treasuries or crude. What exists is (a) trend following, where shorts are one side of a diversified CTA book, and (b) oil term-structure carry, where being short the front month in contango earns the negative roll that longs pay. Both are regime-dependent.

### Cited Findings
- Crude was in contango about 42% and backwardation about 58% of the time since 1985 (front vs 6th month). Since 2008, contango (negative roll for longs) has been more common, whereas from 1985 to 2008 a rolled long front-month beat spot — [CME Group 2026](https://www.cmegroup.com/insights/economic-research/2026/implications-of-wti-oil-futures-in-backwardation-amid-the-supply-crunch.html)
- Long crude during contango "often (but not always)" loses, and long during backwardation typically gains. Backwardation reflects tight supply, contango reflects oversupply and storage costs — [CME OpenMarkets Q&A 2026](https://www.cmegroup.com/openmarkets/economics/2026/What-Backwardation-in-Oil-Futures-Reveals-About-Market-Expectations.html)
- An unverified secondary claim says USO lost about 80% from 2010 to 2025 while spot was roughly flat, from contango drag — [USCF Substack](https://uscfinvestments.substack.com/p/understanding-contango-and-backwardation) (flagged unverified)
- Large net shorts in Treasury futures are mostly the futures leg of the cash-futures basis trade (relative value), not directional bets — [US Treasury TBAC 2024](https://home.treasury.gov/system/files/221/TBACCharge1Q12024.pdf); [Investing.com/Reuters](https://www.investing.com/news/economy-news/analysishedge-funds-sour-on-basis-trade-as-treasury-selloff-continues-4914832)
- CTAs short trending-down markets, including 10y Treasury futures, inside diversified books — [Return Stacked](https://www.returnstacked.com/managed-futures-trend-following/); [arXiv 2607.19497 trend-following review](https://arxiv.org/pdf/2607.19497)

### Inferences
- For oil, the short sleeve with a mechanism is "short when in contango (negative carry for longs) AND trend down". Carry and trend agree in oversupplied regimes. Outside them, the short loses roll in backwardation.
- For bonds, the 2022 episode shows trend shorts can pay big, but bond shorts carry negative carry when the curve is upward sloping. A standalone short sleeve is regime insurance (inflation shock), similar to the team's crypto shorts.

### Gaps
- No backtest numbers (Sharpe, sample) were retrieved for oil carry-short or Treasury trend-short sleeves. The classic references (Koijen-Moskowitz-Pedersen-Vrugt "Carry", Moskowitz-Ooi-Pedersen TSMOM, Erb-Harvey) were not fetched in this pass.
- No intraday bond/oil short evidence was found.

## Cross-cutting caveats (survivorship / data-mining)
- Academic crypto factor papers use spot data with dead coins handled variably. Perp universes on Binance are survivor-heavy, since perps list after success and delist after collapse. — [Inference; universe-construction concern echoed by point-in-time Binance universe in SSRN 7556359](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7556359)
- Predictability migrates across signals and periods (SSRN 7556359), and carry decayed to negative in 2025 (arXiv 2510.14435). Any short sleeve needs a frozen holdout, as Kitron-Wengrowicz used.
- Vendor unlock studies (Tokenomist, Streamflow, Keyrock) cover a single cycle, are uncontrolled or matched-peer only, and are not peer-reviewed.
