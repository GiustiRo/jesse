# Crypto-native data signals for 1h/4h trading of Binance USDT-M perpetuals: evidence and 2020-2025 history availability (as of Oct 2026)

Scope note: the team already tested funding rate and open interest as stand-alone directional entry signals on BTC and found nothing. These notes focus on what is new relative to that. "Evidence quality" grades used below: **A** = peer-reviewed or central-bank working paper with tests; **B** = arXiv/SSRN preprint or dissertation with formal tests (not yet peer-reviewed); **C** = practitioner/vendor research with some quantification; **D** = anecdote/commentary only. Unverified items are flagged **[UNVERIFIED]**.

Research budget caveat: about 20 searches and fetches. Several vendor documentation pages were reached only through third-party summaries. Re-check every history-start date against the vendor before building on it.

## Order flow (taker buy/sell volume, CVD, trade-size imbalance, OFI, VPIN)

### Takeaway
The data is free and complete for 2020-2025 on Binance (klines carry taker-buy volume, and aggTrades dumps allow CVD and trade-size splits). The evidence for *plain* taker imbalance predicting the next hour is weak. The most credible recent result (a 2026 preprint on Binance perps) finds that order imbalance measured at quarter-hour clock boundaries predicts returns 4 to 12 hours ahead, with a short reversal in the first ~30 minutes. That is a genuinely new, testable angle.

### Cited Findings
- Kim and Hansen (arXiv 2607.09426, July 2026), "The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures". Binance perpetual futures, six assets including BTC, sample 2021-07 to 2024-10. Order flow from periodic algorithms clusters at quarter-hour boundaries. Opening order imbalance at those boundaries predicts returns over **4 to 12 hours**, with much weaker effects at finer clock frequencies. Baseline imbalance and imbalance at one-minute openings show "little predictive association" with later returns. The effect is negative over the first half hour (a short-run reversal). The predictive block adds significant forecasting power for BTC in walk-forward LASSO with Diebold-Mariano tests. The authors warn it is not causal price impact. Evidence **B** — [arXiv 2607.09426](https://arxiv.org/pdf/2607.09426); [alphaXiv listing](https://www.alphaxiv.org/abs/2607.09426)
- The fragmentation and cross-impact paper on Bitcoin markets predicts returns 500ms ahead on a Bybit BTC perp using trade-flow imbalance. A new imbalance measure raises R² by about 0.019 over the classical one. This is sub-second microstructure and not usable at 1h/4h. Evidence **B** — [arXiv 2108.09750](https://arxiv.org/pdf/2108.09750)
- The classic Cont et al. OFI work explains *contemporaneous* price changes, not future ones. Multi-level OFI cross-impact helps intraday forecasting only in equities. Evidence **A/B**, not crypto — [arXiv 2112.13213](https://arxiv.org/abs/2112.13213v2)
- A limit-order-book Hawkes model for crypto reports that a base imbalance measure beats benchmarks on return-sign accuracy. It needs L2 book data (Tardis, paid), not taker flow. Evidence **B** — [arXiv 2312.16190](https://arxiv.org/pdf/2312.16190)
- VPIN: the canonical work is Easley, López de Prado and O'Hara (RFS 2012). Andersen and Bondarenko criticise VPIN built on bulk-volume classification. I found **no peer-reviewed crypto study** showing that VPIN predicts BTC jumps or returns, only a Padua master's thesis (findings not visible in the snippet) and an informal Substack piece. Evidence **D** for crypto — [NYU Stern summary](https://www.stern.nyu.edu/sites/default/files/assets/documents/con_035928.pdf); [Andersen-Bondarenko critique via NEP](https://nep.repec.org/nep-mst/2013-12-29); [Padua thesis](https://thesis.unipd.it/retrieve/efd7c112-cea5-4e38-84ab-f5fc2e093be8/Cianini_Alessio.pdf); [Microstructure Lab Substack](https://themicrostructurelab.substack.com/p/toxic-flow-segmentation-measuring)
- Kraken defines taker imbalance (taker buy volume minus taker sell volume per sampling interval) and frames a positive value as potentially bullish. This is an interpretation, not a test. Evidence **D** — [Kraken Pro analytics](https://support.kraken.com/ca/articles/12975108557588-kraken-pro-analytics)
- Related intraday-momentum evidence: the first half-hour's return predicts the last half-hour's (Shen, Urquhart and Wang, Financial Review 2022), driven by liquidity provision. Evidence **A** — [Birmingham research portal](https://research.birmingham.ac.uk/en/publications/bitcoin-intraday-time-series-momentum/)
- **Availability:** Binance Public Data (data.binance.vision) publishes USD-M futures klines and mark, premium and index klines for all symbols from 2020-01-01. Cost: free. Granularity: down to 1m — [Binance public data repo (via Algolia docsearch)](https://docsearch.algolia.com/mcp/docs/repo/binance/binance-public-data). The REST endpoint `/fapi/v1/aggTrades` only serves the past 48 hours, so historical trade-level work must use the bulk dumps — [Binance USDⓈ-M market data docs](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio)

### Inferences
- The kline `taker_buy_base_volume` field gives taker buy and sell volume and a CVD proxy at 1m resolution for free from 2020 (BTCUSDT perp listed 2019). Quarter-hour boundary imbalance can be built from 1m klines without trade data: sum taker imbalance over the first minute(s) after :00/:15/:30/:45. That makes the Kim-Hansen result cheap to replicate on Jesse data.
- Trade-size imbalance (large-trade versus small-trade taker flow) needs aggTrades or trades dumps (free on data.binance.vision, but tens of GB per year for BTC). No crypto-specific 1h/4h evidence for it was found.
- Plain "taker ratio > threshold leads to a move in the next hour" is very likely already priced. The literature found supports only clock-structured or conditional versions.

### Gaps
- I could not confirm independent replication of the quarter-hour result, or its net-of-cost profitability at 4h.
- Not found: peer-reviewed crypto VPIN results at hourly horizons; trade-size-segmented flow studies.
- The `taker_buy_base_volume` column and the history start of aggTrades on data.binance.vision were not fetched directly in this session. Both are standard Binance kline fields and believed to start at symbol listing **[UNVERIFIED in this session]**.

## Liquidations (history availability, reversal versus continuation after cascades)

### Takeaway
Clean free history is the main obstacle. Binance cut its liquidation reporting on 2021-04-27, since then its `forceOrder` stream only shows a sampled subset, and the data cannot be backfilled. The rigorous evidence on post-cascade *returns* is thin. What exists is descriptive (fast intraday recovery after Oct 10, 2025) or finds that precursors are not stable across events.

### Cited Findings
- Coin Metrics: a Binance API change on **2021-04-27** reduced liquidation reporting, and Binance does not allow historical liquidation collection. Data "between 2021-05-11 and 2021-08-31 will remain underreported and there is no way for us to recover the data". Liquidations before 2021-04-27 are accurate — [Coin Metrics, Market Level Liquidations](https://docs.coinmetrics.io/market-data/market-data-overview/liquidations/futures-liquidations)
- CryptoQuant also flags the Binance policy change of 2021-04-27 and lists Binance liquidation data from late 2019 for several symbols (paid API) — [CryptoQuant BTC liquidations docs](https://docs.cryptoquant.com/api-reference/btc-market-data/liquidations)
- CoinGlass API (official pricing page): no free tier. Hobbyist costs $29/month (30 requests/min, personal use) with 1m history of 6 days and Startup ($79/month) 12 days. 1h and 4h intervals were listed at 180 days for Hobbyist in a search summary of the same page, but my direct fetch could not map them cleanly to plans. **Daily** liquidation history is all-time on every plan. Standard costs $299/month and Professional $699/month — [CoinGlass pricing](https://coinglass.com/pricing). A third-party spec claims Hobbyist is limited to intervals of 4h or more and that liquidation orders are Standard-tier — [Glama coinglass-mcp spec](https://glama.ai/mcp/servers/@forgequant/coinglass-mcp/blob/3ff015e428d99f013e3e7fe363b98d82adeb00a3/docs/02-api-specification.md) **[CONFLICT/UNVERIFIED]**
- Coinalyze: free API at about 40 calls/min (third-party listing), with liquidation history candles available. The **retention depth for intraday intervals is not documented** in the sources found — [NexusFi listing](https://nexusfi.com/d/data-providers/coinalyze/); [StockSharp connector](https://nuget.stocksharp.com/packages/StockSharp.Coinalyze) **[UNVERIFIED depth]**
- Tardis.dev announced historical liquidation CSV downloads in 2021 — [Tardis Substack sitemap 2021](https://tardis.substack.com/sitemap/2021). For Binance, Tardis captures the same post-2021-04 sampled `forceOrder` stream (inference from the Coin Metrics note).
- Evidence: Garcia Seuma (arXiv 2607.27070) studies seven BTC perp liquidation cascades from 2022 to 2025, including Oct 10, 2025. Early-warning indicators (rolling variance, lag-1 autocorrelation) are **event-heterogeneous**, and no variable is event-invariant. Evidence **B** — [arXiv 2607.27070](https://arxiv.org/pdf/2607.27070)
- Cheng et al. (arXiv 2102.04591, BitMEX): daily forced liquidations average 3.51% of outstanding futures for longs and 1.89% for shorts. Normal-return margin models underestimate the margins needed. Evidence **B** — [arXiv 2102.04591](https://arxiv.org/pdf/2102.04591)
- Lim Boon Chuan (JFDA 2026, Hyperliquid order book, Oct 10, 2025): the cascade was compressed intraday, with recovery well under way by end of day. It studies liquidity and spreads, not returns. Evidence **A/B** — [JFDA article](https://journals.lincoln.ac.nz/index.php/JFDA/article/view/1395)
- CoinShares describes the self-reinforcing cascade and the "recovery wick" after positions are flushed out. Evidence **D** — [CoinShares](https://coinshares.com/se/insights/knowledge/billions-in-liquidations-what-happened)

### Inferences
- For a 2020-2025 backtest, Binance's own liquidation prints are **structurally broken after April 2021** (a sampled subset). Any liquidation signal built on them has a regime break in 2021. Aggregators (CoinGlass, Coinalyze) inherit the same undercount for Binance.
- A practical free proxy: detect "cascade-like" bars from price and volume (large range plus a taker-sell spike plus an OI drop) using free klines and metrics data, then test a post-flush mean-reversion rule. This avoids buying liquidation history but measures something different.
- The direction after a cascade (reversal versus continuation) remains an **open empirical question** without credible published 1h/4h tests.

### Gaps
- No peer-reviewed event study of 1h/4h returns after liquidation spikes on Binance was found.
- Coinalyze's intraday liquidation retention, and CoinGlass's exact 1h/4h depth per plan, need checking directly with a key.

## Open interest dynamics with price, long/short ratios and top-trader positioning

### Takeaway
The REST endpoints keep only the last 30 days. However, Binance's bulk "metrics" files on data.binance.vision include OI, OI value, top-trader account and position ratios, the global account ratio and the taker long/short volume ratio. That makes OI-price divergence and positioning features feasible for free, though the history start (likely late 2021 or later, not 2020) is unconfirmed. I found no rigorous published evidence that these predict 1h/4h returns.

### Cited Findings
- Binance USDⓈ-M REST: `/futures/data/openInterestHist`: "Only the data of the latest 1 month is available". `globalLongShortAccountRatio` and `/futures/data/basis`: "Only the data of the latest 30 days is available". Periods 5m to 1d, max 500 rows per call — [Binance market data docs](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio). A 2021 community gist says the top-trader account and position ratio endpoints have the same 30-day limit — [gist](https://gist.github.com/tudorelu/3e3cb48dc759f9cf29c6cace0771b27e)
- The bulk daily files at `data/futures/um/daily/metrics/<SYMBOL>/` contain these columns: create_time, symbol, sum_open_interest, sum_open_interest_value, count_toptrader_long_short_ratio, sum_toptrader_long_short_ratio, count_long_short_ratio, sum_taker_long_short_vol_ratio. The sample row in the issue is dated 2023-01-21. A Binance maintainer said finer-granularity OI was expected "likely in Q2" 2023 — [binance-public-data issue #211](https://github.com/binance/binance-public-data/issues/211). The earliest date and the in-file row frequency were **not confirmed** **[UNVERIFIED; my prior belief is 5-minute rows starting around late 2021 for BTCUSDT, so check by listing the bucket]**
- Definition: the top-trader *account* ratio counts the top 20% of traders by account, one vote per account regardless of size. The *position* ratio is size-weighted. These metrics are Binance-only — [Amberdata LSR docs](https://docs.amberdata.io/changelog/lsr-metric-type)
- K33 practitioner commentary links OI growth in a neutral-funding environment to positioning regimes. Evidence **C/D** — [K33 Research](https://k33.com/research/archive/articles/open-interest-in-btc-perpetuals-is-growing-in-a-neutral-funding-environment)
- No SSRN or arXiv paper testing funding plus OI crowding as a return predictor surfaced. The results were explainers and dashboards saying funding "doesn't directly predict price" but flags crowding — [LuxAlgo funding concept](https://www.luxalgo.com/library/concept/funding-rate.md); [Trading Strategy glossary](https://tradingstrategy.ai/glossary/funding-rate). Evidence **D**

### Inferences
- New angles beyond the failed "funding/OI as entry": (1) **OI-price divergence** as a regime or filter (price up with OI down means short covering; price up with OI up means new leverage); (2) the **gap between top-trader position and account ratios** (whales versus the retail count); (3) the **taker long/short volume ratio** from metrics as a second order-flow source. All are cheap if the metrics files cover the needed years.
- If the metrics files start in late 2021, a 2020-2021 backtest window is impossible for these features without a paid vendor. CoinGlass gives OI and LSR history at daily frequency all-time; intraday depth on cheap plans is limited.

### Gaps
- The first date, and any gaps, in `daily/metrics` files per symbol.
- No credible 1h/4h predictive evidence for long/short ratios was found; treat any vendor claims as unverified.

## Basis / term structure (quarterly basis, perp premium index, cross-exchange funding dispersion)

### Takeaway
The best-documented signal in this whole survey is the BIS "Crypto Carry" paper: high futures carry (basis) predicts future price crashes. It is a crash and regime signal, which suits a short-side or risk-off filter rather than an hourly timing tool. The free data needed (premium index klines and quarterly futures klines) exists on data.binance.vision from 2020.

### Cited Findings
- Schmeling, Schrimpf and Todorov, "Crypto Carry", BIS Working Paper 1087 (2023): futures-spot carry reaches up to 60% p.a. It is driven by retail demand for leveraged upside and scarce arbitrage capital. "A high crypto carry predicts future price crashes", and rises in carry coincide with higher prices for crash-risk insurance. Arbitrage is risky because of margin spikes and liquidations in drawdowns. Evidence **A** (central-bank WP) — [BIS WP 1087](https://www.bis.org/publ/work1087.pdf). Horizons and statistics were not extracted (the fetch returned only the summary) **[check the full text]**
- Binance premium index klines (perp vs index) and mark and index klines: bulk files from 2020-01-01, free. The REST `premiumIndexKlines` returns the most recent klines if no range is given — [Binance Premium Index Kline docs](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data); [Binance public data repo](https://docsearch.algolia.com/mcp/docs/repo/binance/binance-public-data)
- The REST `/futures/data/basis` endpoint keeps only 30 days — [Binance market data docs](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio)
- No study of cross-exchange funding dispersion as a return predictor was found.

### Inferences
- An annualised basis (quarterly delivery or perp premium versus spot) above a high percentile can serve as a **"crowded-long" regime flag for the short side**. It differs from the funding signal already tried: the premium index is the input to funding but is available at 1m, and the quarterly basis captures term demand.
- The quarterly basis series requires stitching Binance delivery contracts (BTCUSDT_YYMMDD klines) from data.binance.vision; the premium index is a direct perp proxy.

### Gaps
- No 1h/4h test of the premium index or basis found; the BIS result is likely at daily or weekly horizon.
- Funding dispersion across Binance, Bybit and OKX: no evidence found. Free history exists per exchange but was not verified here.

## On-chain (exchange flows, stablecoin supply and mints, whales, miners)

### Takeaway
The one formal intraday study found shows that BTC exchange net inflows mostly *do not* predict BTC returns (except at 4h) but do predict lower volatility. USDT inflows to exchanges positively predict BTC and ETH returns at several intraday intervals, the most interesting on-chain lead. Evidence that stablecoin issuance predicts prices is mixed to negative. Free on-chain history is mostly daily (Coin Metrics community); intraday exchange-flow history is paid (CryptoQuant, Glassnode).

### Cited Findings
- Chi, Chu, Hao et al. (arXiv 2411.06327), 2017-2023, 1-6h intervals: BTC net inflows "generally lack predictive power for BTC returns (except at 4 hours)" and are negatively associated with volatility at all intraday intervals. ETH inflows negatively predict ETH returns at every interval. **USDT inflows to exchanges positively predict BTC and ETH returns** at several intervals. Evidence **B** — [arXiv 2411.06327](https://arxiv.org/pdf/2411.06327); [RePEc](https://ideas.repec.org/p/arx/papers/2411.06327.html)
- Griffin and Shams (2018) say Tether issuances are followed by Bitcoin purchases (manipulation hypothesis). Wei (2018) finds that issuances do not predict BTC returns, only volume. Lyons and Viswanath-Natraj find no systematic price effect, with issuance linked to arbitrage when USDT trades above par. Grobys and Huynh (2022), using hourly Bitfinex data from Nov 2018 to Jun 2021, find that positive *USDT price* jumps predict negative BTC price changes (a price-jump measure, not issuance). Evidence **A**, mixed — [Economics Letters (Wei 2018) via IDEAS](https://ideas.repec.org/a/eee/ecolet/v171y2018icp19-22.html); [VoxEU, Lyons and Viswanath-Natraj](https://cepr.org/voxeu/columns/stable-coins-dont-inflate-crypto-markets); [Grobys and Huynh, Univ. Vaasa](https://osuva.uwasa.fi/handle/11111/2600); [Griffin-Shams SSRN copy](https://www.smallake.kr/wp-content/uploads/2018/12/SSRN-id3175876.pdf)
- A BRL event study of 565 stablecoin issuances of $1M or more finds market downturns in the week before issuance and positive abnormal returns ±24h around it. Evidence **B/C** — [Blockchain Research Lab WP 11](https://www.blockchainresearchlab.org/wp-content/uploads/2020/05/The_Influence_of_Stablecoin_Issuances_on_Cryptocurrency_Markets_BRL_Working_Paper_No_11.pdf)
- Coin Metrics Community API: free, no key, 10 requests per 6 seconds per IP, non-commercial Creative Commons licence. Network data is a subset of Pro, and community market candles have full history at **daily** frequency only — [Coin Metrics community data docs](https://docs.coinmetrics.io/packages/coin-metrics-community-data). Whether exchange-flow metrics (e.g. FlowInExNtv/FlowNetXNtv) are in the free tier was **not confirmed**. Net Transfer Flow metrics were released for the Pro end-of-day feed — [Coin Metrics release](https://coinmetrics.io/?p=12631) **[UNVERIFIED free availability]**
- Glassnode and CryptoQuant pricing and intraday-history tiers were not checked in this session **[GAP]**. My general understanding is that hourly or 10-minute exchange-flow history needs paid plans.

### Inferences
- On-chain is better suited as a **daily regime filter** than a 1h/4h trigger. The only intraday signal with formal support (USDT exchange inflows leading to BTC up) needs hourly stablecoin exchange-flow data, which in practice means a paid CryptoQuant or Glassnode plan or building your own from Ethereum and Tron transfer logs plus exchange-address labels (labels are the hard part).
- The negative link between BTC inflows and volatility could serve as a volatility or position-sizing input rather than a direction signal.

### Gaps
- No replication of the 2411.06327 results was found; it is a preprint.
- Free intraday exchange-flow data sources and the cost of hourly CryptoQuant or Glassnode history for 2020-2025 were not verified.
- Miner flows and whale transfers: no 1h/4h predictive study was found in this session.

## Options (Deribit DVOL, skew/risk reversal, put/call, max pain)

### Takeaway
DVOL history starts around April 2021, not 2020, and is free from Deribit's public API. The evidence on implied volatility forecasting realised volatility is weak, and directional evidence comes mostly from a 2026 dissertation showing that 25-delta risk reversals predicted BTC returns at multi-day or longer horizons, with the signal decaying after the 2024 ETF launch. I found no credible evidence for max pain or put/call at 1h/4h.

### Cited Findings
- Deribit's `public/get_volatility_index_data` returns DVOL candles with a `resolution` parameter (free, public) — [Deribit API reference](https://docs.deribit.com/api-reference/market-data/public-get_volatility_index_data.md). Tardis lists DVOL data from **2021-04-01** — [Tardis Deribit details](https://docs.tardis.dev/historical-data-details/deribit.md). The exact launch date and the earliest date the Deribit API returns are **[UNVERIFIED]**
- DVOL is the 30-day expected implied volatility from BTC options and is non-directional — [TradingView DVOL explainer](https://www.tradingview.com/ideas/dvol)
- A horse-race study (Deribit, Aug 2018 to Mar 2020) found that ATM implied volatility from quarterly options does **not** forecast next-day realised volatility well, with GARCH and EGARCH better. Evidence **B** — [arXiv 2010.07402](https://arxiv.org/pdf/2010.07402)
- Neo (SMU dissertation, 2026), daily Deribit data Apr 2021 to Dec 2025 (1,723 observations): the 25-delta, 90-day risk reversal is significant at 1% with Newey-West errors in a 13-variable regression, strongest at 30-180 day maturities, and the butterfly also predicts returns. The signals deteriorated after spot-ETF approval in early 2024. Evidence **B** (unpublished dissertation) — [SMU InK](https://ink.library.smu.edu.sg/etd_coll/887)
- A practitioner post says low implied volatility is followed by lower BTC returns. Methodology undocumented. Evidence **D** — [Unravel Substack](https://unexpectedcorrelations.substack.com/p/the-vix-of-crypto-and-how-options)
- Deribit Insights and Anchorage pieces discuss skew and the term structure qualitatively. Evidence **C/D** — [Deribit Insights, volatility regimes](https://insights.deribit.com/industry/bitcoin-options-finding-edge-in-four-years-of-volatility-regimes/); [Anchorage](https://www.anchorage.com/research/the-anchorage-digital-prime-signal-what-skew-wings-and-the-term-structure-are-telling-us-about-bitcoin-and-its-adjacent-markets)

### Inferences
- DVOL suits a **regime or volatility filter** (from 2021-04 onwards) more than 1h/4h entries. The risk reversal is the only options feature with formal directional evidence, at daily-plus horizons and with post-2024 decay. A long-only versus short-allowed regime switch on the risk-reversal sign is plausible but risks being stale.
- Free skew and risk-reversal history requires rebuilding implied volatilities from Deribit option trade and quote data. Tardis sells this, and the Deribit public API does not offer historical option chains in bulk **[UNVERIFIED]**.

### Gaps
- No credible 1h/4h options-to-perp-return study was found, and nothing on max pain or put/call.
- Exact Tardis pricing for the Deribit options chain and the free first-of-month sample policy were not verified.

## Cross-exchange and spot-perp lead-lag (Coinbase premium, Kimchi premium, stablecoin premium)

### Takeaway
The Coinbase premium (Coinbase BTC-USD minus Binance BTC-USDT) is widely cited by practitioners, but I found no rigorous predictive test. It is easy to compute for free from 1m klines from both exchanges since 2020. The Kimchi premium literature explains *why* it exists and shows threshold mean reversion of the premium itself, not BTC return prediction. The closest academic analogue (the Grayscale GBTC premium) was a strong daily return predictor.

### Cited Findings
- Coinbase Premium Index = percentage price difference between Coinbase BTC-USD and Binance BTC-USDT. Claims that it is a "leading indicator" come from CryptoQuant-based commentary without out-of-sample tests. Evidence **D** — [CoinDesk, Jul 2024](https://coindesk.com/markets/2024/07/01/bitcoins-bottom-in-price-could-be-near-or-already-in-the-coinbase-premium-index-suggests); [Cointelegraph](https://cointelegraph.com/markets/bitcoin-coinbase-premium-returns-is-90-k-btc-price-in-the-cards); [Axel Adler definition](https://axeladlerjr.com/charts/bitcoin-coinbase-premium-index/)
- An SMU working paper finds that changes in the Grayscale Bitcoin Trust premium were the single most significant predictor of daily BTC returns (a sentiment proxy for traditional investors). Evidence **B** — [SMU InK](https://ink.library.smu.edu.sg/lkcsb_research/7447)
- Choi, Lehar and Stauffer, "Bitcoin Microstructure and the Kimchi Premium" (Jan 2016 to Feb 2018): the average Korean premium was about 4.73%. It is positively related to transaction costs, blockchain confirmation time and volatility, and negatively related to volume. Capital controls amplify the frictions. Evidence **A/B** — [SNB seminar PDF](https://snb.ch/dam/jcr:474400ba-255b-49a4-b2b8-5e3626719730/sem_2019_05_31_lehar.n.pdf)
- A Monash paper finds the Kimchi premium mean-reverts above a threshold and follows a random walk inside the band, with a long-run premium of about 1.24% — [Monash](https://researchmgt.monash.edu/ws/files/590976616/586624035_oa.pdf). A Finance Research Letters paper links the Kimchi premium to speculative trading — [IDEAS](https://ideas.repec.org/a/eee/finlet/v38y2021ics1544612319301357.html)

### Inferences
- The Coinbase premium is a **cheap, untested, new angle**: 1m Coinbase candles (public API, free) and Binance spot and perp klines from 2020 allow an hourly premium z-score. Since the spot-ETF launch (2024), US demand shows up through Coinbase custody flows, so the premium may have shifted regime. Test pre-2024 and post-2024 separately.
- The USDT/USD premium (e.g. Kraken USDT/USD deviation from 1, or the USDT/KRW-implied premium) is a possible risk-appetite proxy. No direct evidence was found.

### Gaps
- No peer-reviewed or preprint test of Coinbase-premium-to-BTC returns at 1h/4h was found.
- Upbit and Bithumb historical 1m data access for the Kimchi premium was not verified.

## Short-side edge (crowded longs, funding+OI extremes)

### Takeaway
The best-supported short-side or risk-off conditioning variable is **high futures carry/basis**, which the BIS paper ties to subsequent crashes. Weaker support comes from crash mechanics: long liquidations far outweigh short liquidations (BitMEX: 3.51% versus 1.89% of OI daily), so crowded-long states tend to unwind violently. Evidence that funding+OI extremes produce a *timeable* 1h/4h short edge was not found, which matches the team's own negative result.

### Cited Findings
- High crypto carry predicts future price crashes, and crash-insurance prices rise with carry — [BIS WP 1087](https://www.bis.org/publ/work1087.pdf)
- Daily forced liquidations average 3.51% of OI for longs versus 1.89% for shorts on BitMEX, so long-side forced selling dominates — [arXiv 2102.04591](https://arxiv.org/pdf/2102.04591)
- Precursor signals before cascades (variance, autocorrelation) are not consistent across events, which argues against timing short entries on generic early-warning stats — [arXiv 2607.27070](https://arxiv.org/pdf/2607.27070)
- Option risk-reversal skew had predictive power for BTC returns 2021-2025 (decaying after 2024) and could flag skew-implied downside demand — [SMU dissertation](https://ink.library.smu.edu.sg/etd_coll/887)
- ETH exchange inflows negatively predict ETH returns at 1-6h intervals, a potential short-side intraday signal for ETH perps — [arXiv 2411.06327](https://arxiv.org/pdf/2411.06327)
- Funding extremes "may signal" crowding and reversal risk, which is only a qualitative claim — [LuxAlgo](https://www.luxalgo.com/library/concept/funding-rate.md)

### Inferences
- A sensible design is a **two-stage short filter**: regime gate = premium-index or quarterly-basis percentile high (plus optionally DVOL low or an OI-up/price-flat divergence). Trigger = price/order-flow break (e.g. negative quarter-hour taker imbalance, or a price breakdown with an OI drop). The gate uses the best-evidenced variable and the trigger avoids relying on funding as the timing signal (already rejected).
- Short-side signals are naturally sparse (crashes are few), so multiple-testing control and event counts matter more than for long signals.

### Gaps
- No published 1h/4h short-only backtest using basis, OI or ratio extremes with costs was found.
- The BIS horizon (days or weeks) versus the 1h/4h usability of the carry-crash link is unconfirmed.

## Summary availability table (for the report writer; each row is sourced in the sections above)

| Source | History start (free) | Cost | Granularity | Evidence quality at 1h/4h |
|---|---|---|---|---|
| Binance klines incl. taker buy volume (data.binance.vision) | 2020-01-01 (repo scripts) | Free | 1m+ | B (quarter-hour imbalance → 4-12h) |
| Binance aggTrades / trades dumps (CVD, trade size) | Bulk files; REST only 48h | Free | Tick | D for trade-size; B for OFI microstructure (sub-second) |
| Binance premium / mark / index klines | 2020-01-01 | Free | 1m+ | A for basis→crash (horizon unclear); none at 1h |
| Binance metrics files (OI, top-trader & global L/S, taker L/S ratio) | Start unconfirmed (sample 2023; likely ~late 2021) [UNVERIFIED] | Free | Daily files; row frequency unconfirmed | D |
| Binance REST OI hist / L/S ratios / basis | Last 30 days only | Free | 5m-1d | — |
| Binance forceOrder liquidations | Accurate only before 2021-04-27; sampled after, no backfill | Free live; vendors paid | Event | B/D, descriptive |
| CoinGlass | Daily all-time; 1m 6-12 days on cheap plans | $29-$699/mo, no free tier | 1m-1d | — |
| Coinalyze | Depth undocumented [UNVERIFIED] | Free API ~40 calls/min | Intraday candles | — |
| Coin Metrics Community | Full daily history | Free (non-commercial) | Daily | Daily only |
| CryptoQuant / Glassnode exchange flows | 2017+ in studies | Paid for intraday [UNVERIFIED tiers] | Hourly or finer | B (USDT inflows → BTC/ETH up; BTC inflows → lower vol) |
| Deribit DVOL | ~2021-04-01 | Free (public API) | Candles | B (IV weak for RV) |
| Deribit option chains (skew, RR) | 2021+ in studies; via Tardis | Paid (Tardis) [UNVERIFIED pricing] | Tick / daily | B (RR predicts returns, daily+, decaying post-2024) |
| Coinbase premium (Coinbase vs Binance klines) | 2020 (both exchanges' public candles) | Free | 1m | D |
