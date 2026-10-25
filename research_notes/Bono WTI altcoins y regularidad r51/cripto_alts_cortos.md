# Crypto alt trend/breakout, short side, and validation on SOL/XRP/BNB (Binance USDT-M, 2018–2025)

NOTE: Plan mode was active, so these notes were written here instead of the requested path
(`...\scratchpad\research_notes\Bono WTI altcoins y regularidad r51\cripto_alts_cortos.md`).
Copy this file there once plan mode is lifted.

## Q1. Published evidence on TSMOM / breakouts in altcoins vs BTC/ETH; transfer to large alts; Sharpe/DD; survivorship; idiosyncratic events

### Takeaway
Published work consistently finds time-series momentum / Donchian-style trend edge in crypto, including in a survivorship-free multi-coin universe (Zarattini-Pagani-Barbon 2025: long-only Donchian ensemble, net Sharpe >1.5, alpha 10.8%/yr vs BTC). Evidence is long-only or long-biased. Momentum is crash-prone, and the alt-specific evidence comes mainly from rotational baskets of top-20 coins, not single-coin tests on SOL/XRP/BNB. Single-name idiosyncratic shocks (XRP -63% on the SEC suit, SOL about -41% in one week on FTX) are large enough to dominate a 5-year single-coin test.

### Cited Findings
- Zarattini, Pagani, Barbon, "Catching Crypto Trends; A Tactical Approach for Bitcoin and Altcoins" (2025). The method is an ensemble of Donchian channel models over several lookbacks, with volatility-based sizing, run as a rotational portfolio of the top 20 most liquid cryptos. Reported net-of-fees Sharpe is above 1.5, with annualized alpha of 10.8% vs Bitcoin — [Concretum](https://concretumgroup.com/catching-crypto-trends-a-tactical-approach-for-bitcoin-and-altcoins/); [Barbon paper page](https://abarbon.com/papers/catching-crypto-trends); [RePEc](https://ideas.repec.org/p/chf/rpseri/rp2580.html)
- Same paper, design details: sample Jan 2010 to mid-Mar 2025 covering 21,616 crypto-assets. It uses survivorship-bias-free OHLCV aggregated across exchanges. Eligible coins have been listed at least 1 year, since 2015, with 30-day median daily volume of at least $2M. The strategy is long-only. Lookbacks are 5/10/20/30/60/90/150/250/360 days. Entry is a close above the lookback max close; exit is a trailing stop at the higher of the prior stop and the channel midpoint. Sizing targets 25% annualized vol on a 90-day stdev, with leverage capped at 200%. Costs are tested at 0.10/0.25/0.50%. Drawdown and per-coin results are not visible in the public summary — [CXO Advisory](https://www.cxoadvisory.com/technical-trading/crypto-asset-trend-following-strategies/)
- Liu & Tsyvinski, "Risks and Returns of Cryptocurrency" (RFS 2021, 34(6):2689–2727) find significant time-series momentum at daily and weekly horizons for BTC, XRP and ETH, weaker for ETH. Example: the average next-week BTC return is 11.2% for the top quintile of last-week returns vs 2.6% for the bottom quintile. Crypto returns have no exposure to most equity, macro, FX or commodity factors — [NBER w24877](https://www.nber.org/system/files/working_papers/w24877/w24877.pdf); [RePEc](https://ideas.repec.org/a/oup/rfinst/v34y2021i6p2689-2727..html)
- Liu, Tsyvinski & Wu, "Common Risk Factors in Cryptocurrency": market, size and momentum capture cross-sectional expected crypto returns — [NBER w25882](https://www.nber.org/papers/w25882.pdf); [Yale Cowles PDF](https://cowles.yale.edu/sites/default/files/2022-10/LiuTsyvinskiWu2019%20COMMON%20RISK%20FACTORS.pdf)
- Grobys, Kolari, Sandretto, Shahzad, Äijö, "Cryptocurrency momentum has (not) its moments" (FMPM 2025): crypto momentum suffers severe crashes, and volatility management mitigates them. The effect is associated with large-cap cryptos — [Univ. Vaasa repository](https://osuva.uwasa.fi/server/api/core/bitstreams/c9b4eafc-561e-439e-905b-1e1c1edb8adb/content)
- Han, Kang & Ryu: under realistic assumptions (costs), crypto time-series momentum evidence is strong and cross-sectional evidence weak. The effect is concentrated in large winners, and losers often rebound and inflict losses, which is relevant to short legs — [AUT ACFR PDF](https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf)
- Borgards (2021, NAJEF), 20 cryptos: momentum periods are significantly larger and longer than in US stocks — [EconPapers](https://econpapers.repec.org/RePEc:eee:ecofin:v:57:y:2021:i:c:s1062940821000590)
- Rozario, Holt, West, Ng (2020), "A Decade of Evidence of Trend Following Investing in Cryptocurrencies": reports 255% walk-forward annualized returns and bear-market diversification vs equities. Treat this as an optimistic, early-sample figure — [arXiv 2009.12155](https://arxiv.org/abs/2009.12155v1); [PapersWithCode](https://paperswithcode.com/paper/a-decade-of-evidence-of-trend-following)
- Monash MCFS: shorter-lookback crypto trend rules give high Sharpe, but transaction costs reduce profits — [Monash](https://www.monash.edu/business/mcfs/our-research/all-projects/investment-strategy/trend-following-strategies-for-crypto-investors)
- Man AHL, "In crypto we trend" (Dec 2024): for MA crossovers, Sharpe is optimized with about 10–15 coins; breakout models peak at about 10 coins. Liquidity is ample for the top 15 coins and falls sharply beyond that, with altcoin slippage rising. Sharpe levels are "higher than expected for a concentrated trend-following system," likely due to the short history. Coins were added as they launched — [Man Group](https://www.man.com/insights/in-crypto-we-trend)
- AdaptiveTrend (arXiv 2602.11708, 2026): 6h trend-following over 150+ pairs with monthly portfolio construction and an asymmetric 70/30 long-short allocation. Out-of-sample 2022–2024 results are Sharpe 2.41, MDD -12.7% and Calmar 3.18. The abstract does not name the exchange, funding treatment or survivorship handling — [arXiv](https://arxiv.org/abs/2602.11708v1). A promotional summary says it was nearly flat in the bear market — [Substack note](https://substack.com/@quantitativo/note/c-216039933)
- Early-sample momentum: an Erasmus thesis (15 coins, 2016–2017) reports momentum Sharpe above 3 on raw returns, and finds long-only winners beat winners-minus-losers — [EUR thesis](https://thesis.eur.nl/pub/39587/Stoffels-J-450577-MA-thesis.pdf)
- Rohrbach, Suremann, Osterrieder (2017): crypto TSMOM Sharpe 1.62 vs cross-sectional 1.48, gross, 1974–2017 sample (crypto portion much shorter) — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/currency-and-cryptocurrency-exchange-rate-momentum-tests); [ZHAW](https://digitalcollection.zhaw.ch/handle/11475/15965?mode=full)
- XRP / SEC event: the suit was announced Dec 21, 2020, and XRP market cap fell about 63% (about $16B) — [Decrypt](https://decrypt.co/52812/xrps-market-cap-fell-63-after-sec-lawsuit-heres-how-that-happened). It fell 24% in 24h and 41% on Binance over 3 days — [Cointelegraph](https://cointelegraph.com/markets/xrp-price-falls-24-in-24-hours-as-exchanges-begin-delisting). Price went from about $0.64 in mid-December to about $0.20 — [Decrypt](https://decrypt.co/53397/xrp-price-rebounds-30-in-24-hours-despite-legal-challenges). Coinbase went limit-only Dec 28 and fully suspended Jan 19, 2021 — [TechRadar](https://www.techradar.com/news/coinbase-has-stopped-trading-one-of-one-of-the-worlds-largest-cryptocurrencies). XRP then rebounded 30% in 24h — [Decrypt](https://decrypt.co/53397/xrp-price-rebounds-30-in-24-hours-despite-legal-challenges)
- SOL / FTX event: SOL lost about 41.2% in one week (from $20.16 on Nov 9, 2022) and was the worst top-100 performer — [Decrypt](https://decrypt.co/114767/solana-plummet-week-amid-ftx-collapse). Reuters measures -51% from Nov 2 vs ETH -21% and BTC -18% over the same window — [Cyprus Mail/Reuters](https://www.cyprus-mail.com/2022/12/30/solana-crypto-token-loses-most-of-its-value-in-2022-ftx-collapse-weighs)

### Inferences
- Edge transfer to large alts is plausible in principle: TSMOM shows up in XRP in Liu-Tsyvinski, and Zarattini et al. run a top-20 basket. But no source isolates single-coin Sharpe for SOL, XRP or BNB. A frozen BTC/ETH sleeve should be expected to deliver a lower and noisier Sharpe per alt than on BTC/ETH, because idiosyncratic jump risk is higher.
- The XRP and SOL shocks were downside gaps. A long-biased breakout sleeve was likely flat or stopped out on XRP in Dec 2020: XRP had rallied in Nov 2020, so a long may have been open and hit with gap risk. That requires checking in your own data. On SOL in Nov 2022 the sleeve was likely already flat (bear market). These events test stop and gap handling more than signal quality. Report results both with and without each event window rather than excluding them.
- Survivorship: SOL, XRP and BNB are all ex-post survivors chosen in 2026. Choosing them because they are top-5 today embeds look-ahead. Mitigations: (a) state this explicitly; (b) add ex-ante-chosen coins, e.g. the top-N Binance perps by volume as of each Jan 1, including later-faded names such as LTC, BCH, EOS, LINK, ADA, DOGE, DOT; (c) compare with Zarattini's survivorship-free basket result.
- Published Sharpe figures (1.5 to 2.4+) come from short histories concentrated in bull markets, and Man AHL flags this explicitly. A realistic out-of-sample expectation for a single-alt breakout sleeve is well below published basket Sharpes (judgment, not sourced).

### Gaps
- No public numbers for Zarattini et al. drawdowns or per-coin breakdowns. The full PDF on SSRN or the Barbon page needs reading.
- No Fičura paper was found in searches. No "Huang et al." crypto TSMOM paper was identified; need the exact citation.
- No sourced quantification of the BNB 2023 regulatory event (SEC v. Binance, June 5, 2023; Binance/CZ DOJ settlement, Nov 21, 2023). Those dates are from prior knowledge and were not verified this session.

## Q2. Data facts: Binance USDT-M listing dates, spot history, funding behavior

### Takeaway
USDT-M perps launched Jan 6, 2020 (XRPUSDT), Feb 10, 2020 (BNBUSDT) and Sep 14, 2020 (SOLUSDT). Any 2018–2019 test therefore needs spot data (with no funding), and SOL has no meaningful history before 2020. Funding signed means are near zero on average, but absolute deviations are 60–90%/yr and the regime swings are large. Longs paid heavily in early 2021, and shorts were paid or neutral through much of 2022.

### Cited Findings
- XRP/USDT perpetual launched on Binance Futures Jan 6, 2020, with up to 75x leverage — [The Block](https://www.theblock.co/linked/52102/)
- BNB/USDT perpetual opened Feb 10, 2020 at 08:00 UTC (announced Feb 7), with 50x maximum leverage; it was the 17th asset on Binance Futures — [Tron Weekly](https://www.tronweekly.com/binance-futures-set-to-launch-bnb-futures-contracts-with-50x-max-leverage/); [Cointelegraph](https://regional-front.cointelegraph.com/news/continuing-its-crypto-market-takeover-binance-fires-up-bnb-futures); [CoinCodex](https://coincodex.com/article/6881/binance-futures-bnb-50x-leverage). He et al. independently start the BNB perp sample on 2020-02-10 — [arXiv 2212.06888](https://arxiv.org/html/2212.06888v5)
- SOL/USDT (and EGLD/USDT) perpetual opened Sep 14, 2020 at 07:00 UTC with 1–50x leverage. The secondary report mislabels SOL as "Sola," but the date matches the Solana contract — [Crowdfund Insider](https://www.crowdfundinsider.com/?p=166789)
- SOL spot on Binance global: listing was announced Mar 2020, with initial pairs SOL/BNB, SOL/BTC and SOL/BUSD (not USDT) — [Shrimpy blog](https://blog.shrimpy.io/news/binance-lists-solana-sol). Binance.US SOL/USD and SOL/USDT started Sep 18, 2020 — [Solana Foundation](https://solana.com/news/binance-us-announces-support-for-sol--making-it-the-second-us-exchange-within-one-day)
- He, Manela, Ross, von Wachter, "Fundamentals of Perpetual Futures" (Binance hourly, 2020 to Mar 2024; BTC, ETH, BNB, DOGE, ADA). Funding is paid every 8h and roughly equals the prior 8h's average futures-spot spread. Inside a clamp region it is fixed at 0.01% per 8h. The futures-spot deviation ρ has a near-zero mean (BNB -0.10, BTC -0.06 annualized) but a large mean |ρ| (BTC 0.57, ETH 0.63, BNB 0.88, DOGE 0.86, ADA 0.83 per year). |ρ| shrinks about 11%/yr as the market matures. Funding was strongly negative in Mar 2020 and after FTX (Nov 2022), and highly positive in early 2021. Past 120-day returns positively predict ρ, so futures are rich after rallies. XRP and SOL are not covered — [arXiv 2212.06888v5](https://arxiv.org/html/2212.06888v5)
- In the same paper's carry/arb decomposition for BTC, about 8.64% of return came from price convergence and 5.06% from funding. The funding channel's role diminishes over time — [arXiv](https://arxiv.org/html/2212.06888v5)
- Binance's 0.01%/8h floor is about 10.95% APR (0.0001 × 1095). One vendor reports Binance BTC funding sits at the 0.01% clamp about 31% of the time, with a global average of 66% annualized in Jan 2024 and 5.1% in May 2024. These are vendor figures with undocumented methodology — [Spark](https://www.spark.money/tools/funding-rate-comparison); [Sharpe.ai methodology](https://www.sharpe.ai/funding-rates)
- 2019 cross-exchange funding was 14–26% annualized (Sep–Nov 2019) — [Deribit Insights](https://insights.deribit.com/market-research/perpetual-swaps-comparisons-and-findings/)
- In 2022, funding was mostly negative or neutral after the June credit crisis, and perps traded at a discount to spot — [K33 Research](https://k33.com/research/archive/articles/funding-rates-neutral-open-interest-to-new-highs)

### Inferences
- Holding cost asymmetry: in trending-up regimes, funding is positive and often elevated (well above the 10.95% floor in 2021 and early 2024), so trend longs pay carry, potentially 10–60%+ APR during the strongest legs. In bear regimes, funding is near the floor or negative, so trend shorts usually earn small carry or pay little, but pay when shorts crowd (negative funding). Net effect: funding is a headwind for long trend and a mild tailwind for short trend on average. Its magnitude is concentrated in exactly the bull months that generate most long-side P&L.
- Backtests must load the actual Binance funding history from `/fapi/v1/fundingRate` per symbol (8h; some symbols later moved to shorter intervals). A constant 0.01% assumption understates long costs in 2021.
- For 2018–2019 (pre-perp), use spot (XRPUSDT, BNBUSDT) with no funding and flag it as non-tradable on USDT-M. SOL's validation window effectively starts Sep 2020, or Aug 2020 using spot.

### Gaps
- No sourced mean or extreme annualized funding for SOLUSDT or XRPUSDT. Compute it directly from the Binance API (the jesse-local `import_funding` / `get_funding_dataset` tools exist in this environment).
- Exact Binance global spot start dates for XRPUSDT (believed 2018) and BNBUSDT (believed late 2017) were not verified this session.
- No verification of when Binance moved specific alt perps from 8h to 4h or 1h funding intervals.

## Q3. Crypto shorts: evidence for short-side trend/breakout, regime filters, funding, squeezes

### Takeaway
There is no rigorous published evidence that symmetric short-side trend/breakout in crypto has standalone positive expectancy. The literature is long-only (Zarattini), long-biased (AdaptiveTrend's 70/30 beats 50/50), or finds losers rebound sharply (Han et al.). Shorts help mainly as crash hedges in sustained bears (2018, 2022). They face squeeze risk when funding is negative and shorts crowd.

### Cited Findings
- AdaptiveTrend's asymmetric 70/30 long/short allocation beat the dollar-neutral 50/50 variant by 29 bp of Sharpe. Out-of-sample covers 2022–2025 and includes the 2022 bear — [arXiv 2602.11708](https://arxiv.org/pdf/2602.11708); [Substack summary](https://substack.com/@quantitativo/note/c-216039933)
- Losers often rebound and inflict significant losses, with momentum profits concentrated in large winners — [Han, Kang, Ryu](https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf)
- Long-only winners beat winners-minus-losers in a 2016–2017 sample — [EUR thesis](https://thesis.eur.nl/pub/39587/Stoffels-J-450577-MA-thesis.pdf)
- Crypto momentum crashes are severe and volatility scaling mitigates them — [Grobys et al. 2025](https://osuva.uwasa.fi/server/api/core/bitstreams/c9b4eafc-561e-439e-905b-1e1c1edb8adb/content)
- Negative funding means shorts pay longs and signals crowded shorts. Santiment says that when funding shows heavy shorting, liquidations and surprise bounces are more common — [Cointelegraph](https://cointelegraph.com/markets/multi-day-negative-bitcoin-funding-signals-overcrowded-short-trade-time-for-a-reversal). BTC 30-day funding was negative for 46 straight days in 2026, the longest streak since post-FTX 2022 — [Yellow](https://yellow.com/it/news/bitcoin-funding-rate-bottom-signal-2022)
- Man AHL models include shorting costs and shorting availability but do not report the short leg separately — [Man Group](https://www.man.com/insights/in-crypto-we-trend)
- A 200-day MA regime filter (e.g. "bear when BTC is below its 200d MA, then shift to cash or shorts") is widely used by practitioners, but only glossary and TradingView-level descriptions turned up, with no published OOS evidence — [Trading Strategy glossary](https://tradingstrategy.ai/glossary/regime-filter)

### Inferences
- Expected behavior of symmetric Donchian shorts on SOL, XRP and BNB: profitable in 2018 (spot only, no SOL) and 2022 (Nov 2021 to Dec 2022). Losing in 2019 (Q2 rally), 2020–21 and 2023–24, from whipsaw and violent bear-market rallies (e.g. Jul–Aug 2022, Jan 2023, Oct 2023). On average across 2018–2025, symmetric shorts likely lose or roughly break even because crypto drift is strongly positive. Their value is in reducing the long sleeve's drawdown and lowering correlation in bears. This is judgment from the sourced evidence, to be tested.
- If shorts are tested, preregister: (1) short only when the regime filter is bearish, e.g. BTC or the coin below its 200d SMA and 200d slope negative; (2) a smaller short size, e.g. 30–50% of long risk, consistent with AdaptiveTrend's 70/30; (3) a funding-crowding veto, e.g. skip new shorts when 3-day mean funding is below a negative threshold; (4) a faster exit or tighter time stop on shorts, since bear rallies are sharp; (5) a pass criterion based on the portfolio-level drawdown and Sharpe contribution, not standalone short Sharpe.
- Funding for shorts: mostly a small tailwind (about the 0.01% floor, roughly 11% APR received when funding is positive) in early bear legs, but it can turn into a cost exactly when shorts are crowded near bottoms.

### Gaps
- No peer-reviewed study isolating short-leg Sharpe or drawdown of crypto TSMOM/breakout across 2018 and 2022 was found.
- No quantified squeeze-loss statistics for SOL, XRP or BNB perps were found.

## Q4. Cross-sectional momentum vs time-series in a small universe (5 coins)

### Takeaway
Evidence favors time-series over cross-sectional momentum in crypto, especially among a few highly correlated large caps. A 5-coin cross-sectional momentum (XSMOM) sleeve is probably not worth adding.

### Cited Findings
- Time-series momentum evidence is strong and cross-sectional weak once costs are included — [Han, Kang, Ryu](https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf)
- A 2025/26 study of 8 major coins (2020 to Oct 2025) found TSMOM superior. Cross-sectional momentum had a higher max drawdown (55.0%) and lower profitability, partly due to high inter-coin correlations — [Vilnius BATP journal](https://www.journals.vu.lt/BATP/lt/article/download/44540/42590/138419) (as summarized in search results; full text could not be fetched because of a redirect loop)
- In a broad universe of 143 coins (2014–2018), winner-minus-loser returns were near zero and insignificant — search summary of EUR thesis work ([EUR thesis](https://thesis.eur.nl/pub/45268/Kroft-L.C.-van-der-432770-.pdf))
- Momentum is more significant in small coins (Liu, Liang, Cui, 78 cryptos), i.e. not in the large caps a Binance-perp universe would contain — search summary ([EUR thesis](https://thesis.eur.nl/pub/59629/Final_Thesis_Draft_494850-1-.pdf))
- Rohrbach et al.: crypto TSMOM Sharpe 1.62 vs XSMOM 1.48 (gross) — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/currency-and-cryptocurrency-exchange-rate-momentum-tests)

### Inferences
- With 5 coins, a cross-sectional rank has 1–2 names per leg. It is dominated by idiosyncratic noise and events (e.g. the XRP SEC suit, SOL's 2021 run and FTX crash) and offers very little breadth. Use cross-sectional info at most as a tie-breaker or allocation tilt inside the TSMOM sleeve, not as a separate sleeve.

### Gaps
- The Vilnius paper's authors and exact Sharpe values were not obtained.

## Q5. Correlation of alt trend sleeves with BTC/ETH sleeves

### Takeaway
Raw return correlation of large alts with BTC is high (about 0.6 pairwise on average over the last decade; SOL about 0.93 in a 2023 estimate). Trend-sleeve P&L correlation will be lower than raw return correlation, because entry and exit timing differs, but a large diversification benefit is unlikely. Expect a modest Sharpe uplift from adding 3 alts, mostly via timing differences and idiosyncratic trends (e.g. SOL 2021, XRP Nov 2024).

### Cited Findings
- Average high-frequency pairwise crypto correlation is about 0.6 over the last decade, with "limited diversification potential." Diversification benefits rise with coin count only up to about 10–15 coins — [Man Group](https://www.man.com/insights/in-crypto-we-trend)
- A Sistine Research figure (2023) puts Solana's correlation with BTC at 0.93 (highest among those cited), vs Monero 0.68 and Tron 0.72 — [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/not-bitcoin-ethereum-or-cardano-but-these-crypto-assets-hold-the-potential-for-a-bull-run-202310130025)
- Co-movement of futures-spot gaps (hence funding) across cryptos is strong — [He et al.](https://arxiv.org/html/2212.06888v5)
- High inter-coin correlation is cited as a reason XSMOM underperforms in 8 major coins — [Vilnius BATP](https://www.journals.vu.lt/BATP/lt/article/download/44540/42590/138419)

### Inferences
- With an average pairwise correlation ρ of about 0.6 and N=5 equally risk-weighted sleeves of equal Sharpe S, portfolio Sharpe is about S·sqrt(N/(1+(N−1)ρ)), roughly S·1.15. So BTC+ETH alone at ρ 0.8 to 5 coins gives only a modest uplift. Trend P&L correlations are typically lower than price correlations, so in-sample sleeve correlation must be measured directly. A practical gate: alt-sleeve P&L correlation to the BTC/ETH sleeve below about 0.7, and a positive marginal Sharpe contribution.
- Funding co-moves across coins, so the carry drag on longs is also correlated. Diversification across alts does not diversify the funding headwind.

### Gaps
- No sourced figures for trend-strategy P&L correlation between alt and BTC/ETH sleeves; compute it in-house. No Kaiko or CF Benchmarks numbers on XRP/BNB–BTC correlations were retrieved.

## Q6. Recommended validation design

### Takeaway
Treat SOL/XRP/BNB as a frozen out-of-sample transfer test of the BTC/ETH sleeve: no reoptimization, identical parameters, real Binance funding and costs. Preregister pass/fail gates on pooled and per-coin metrics, split by regime, with the 2020–21 bull reported separately. Add ex-ante-selected coins to counter survivorship.

### Cited Findings (inputs to the design)
- Ensemble lookbacks and vol targeting reduce parameter dependence and momentum crash risk — [CXO on Zarattini et al.](https://www.cxoadvisory.com/technical-trading/crypto-asset-trend-following-strategies/); [Grobys et al.](https://osuva.uwasa.fi/server/api/core/bitstreams/c9b4eafc-561e-439e-905b-1e1c1edb8adb/content)
- The breakout optimum is about 10 coins, and liquidity limits sit around the top 15 — [Man Group](https://www.man.com/insights/in-crypto-we-trend)
- Survivorship-free universe construction: coins listed at least 1 year, with 30-day median volume of at least $2M — [CXO](https://www.cxoadvisory.com/technical-trading/crypto-asset-trend-following-strategies/)
- Perp availability: XRP from Jan 2020, BNB from Feb 2020, SOL from Sep 2020 (see Q2 sources)
- Funding regimes differ sharply (early 2021 highly positive, 2022 negative or neutral) — [He et al.](https://arxiv.org/html/2212.06888v5); [K33](https://k33.com/research/archive/articles/funding-rates-neutral-open-interest-to-new-highs)

### Inferences (design proposal, judgment)
- **Universe:** primary SOL/XRP/BNB, with 4h bars on USDT-M perps from listing plus a 1-year warm-up rule, mirroring Zarattini's 1-year seasoning. Add a survivorship control: the top-N (about 8–10) Binance USDT-M perps by trailing 30-day volume, selected point-in-time each year, including later-declined coins (e.g. LTC, BCH, EOS, LINK, ADA, DOT, DOGE). The question is whether the sleeve works on alts chosen ex ante, not on 2026 winners.
- **Windows:** 2020-09 (or listing) to 2025-12 on perps with real funding. Optionally add 2018–2019 spot-only for XRP and BNB as a no-funding robustness check, flagged as not USDT-M tradable.
- **Regime slices (reported separately):** 2020Q4–2021Q4 bull, 2022 bear, 2023–2024 recovery, 2025. Bull-bias control: require the gate to pass excluding the 2020-10 to 2021-11 window, because a long-biased breakout on SOL (about 100x then) will look spectacular there.
- **Pass/fail gates (preregistered):** (1) pooled alt-sleeve net Sharpe of at least about 0.5–0.6, i.e. about half the BTC/ETH Sharpe, after costs and real funding; (2) at least 2 of 3 coins with positive net expectancy, and no single coin contributing more than about 60% of P&L; (3) positive net result excluding the 2020-10 to 2021-11 bull; (4) MDD per coin within about 1.5x the BTC/ETH sleeve's MDD at equal vol target; (5) a pooled trade-level bootstrap or permutation p-value below 0.05; (6) results stable when the event windows (XRP Dec 2020 to Jan 2021, SOL Nov 2022, BNB Jun 2023) are dropped; (7) a positive marginal contribution to combined portfolio Sharpe, with sleeve P&L correlation to BTC/ETH below about 0.7.
- **No tuning:** keep parameters frozen. If the per-coin vol target is the only adaptation, fix it ex ante (e.g. 25% annualized as in Zarattini).
- **Shorts:** test as a separate, preregistered add-on (regime-gated, reduced size, funding-crowding veto). Accept only if it improves portfolio Calmar or MDD in 2022 without reducing full-period Sharpe by more than a small tolerance.
- **Costs:** taker fees of about 0.04–0.05%, plus slippage that scales with alt liquidity, plus actual 8h funding per symbol from the Binance API.

### Gaps
- The gate thresholds are proposals, not literature-derived. No source gives standardized pass/fail thresholds for crypto sleeve transfer tests.
