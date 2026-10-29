# Execution and Operational Readiness: Binance USDT-M Perps (crypto + TradFi), 2026

NOTE: Plan mode was active, so these notes could not be saved to the requested path
(`...\scratchpad\research_notes\Bono WTI altcoins y regularidad r51\ejecucion_perps.md`).
Copy this file there once plan mode is lifted. Research date: 2026-10-25. Most TradFi facts
come from secondary press. Binance's official FAQ and spec pages did not load through fetch.
Check them against the live Binance contract-spec page or `GET /fapi/v1/exchangeInfo` / `GET /fapi/v1/fundingInfo`.

## Fees, post-only orders, maker fill and adverse selection, stop slippage

### Takeaway
Base VIP0 USDT-M fees are most often reported as 0.02% maker / 0.05% taker, with 10% off when fees are paid in BNB (about 0.018% / 0.045%). The API supports post-only (GTX) and priceMatch. Practitioner evidence says passive entries fill selectively: they tend to fill on the losing signals. A maker backtest that assumes every limit order fills is optimistic.

### Cited Findings
- VIP0 ("Regular", under $15M 30-day volume or under 25 BNB): 0.02% maker, 0.05% taker on USDⓈ-M — [Finder](https://www.finder.com/binance-futures-fees); similar 2026 figures — [TradersUnion](https://tradersunion.com/brokers/crypto/view/binance/futures-fees/)
- 10% discount when paying USDⓈ-M fees in BNB. BNB must sit in the USDⓈ-M futures wallet. Article updated 2026-05-01 — [Binance Support 360033544231](https://www.binance.com/fr/support/articles/360033544231)
- Conflict: a Binance Square post cites 0.04% taker — [Binance Square](https://www.binance.com/ru-KZ/square/hashtag/binancefees). Unresolved, so confirm in the account's fee page or via `GET /fapi/v1/commissionRate`. TradFi perps may also carry their own fee schedules or promotions (not verified).
- GTX = post-only. On modify, a GTX order whose new price would execute immediately is cancelled. `priceMatch` (OPPONENT/QUEUE, _5/_10/_20) works only on LIMIT/STOP/TAKE_PROFIT and cannot be combined with `price` — [Binance USDⓈ-M REST API](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api)
- STP modes are EXPIRE_TAKER/EXPIRE_MAKER/EXPIRE_BOTH. New Order defaults to EXPIRE_MAKER, algo and batch endpoints default to NONE — [same](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api)
- Since 2025-12-09, conditional orders (STOP_MARKET, TAKE_PROFIT_MARKET, STOP, TAKE_PROFIT, TRAILING_STOP_MARKET) must go through the Algo Service at `POST /fapi/v1/algoOrder`. The old `/fapi/v1/order` returns -4120 STOP_ORDER_SWITCH_ALGO. Updates arrive on the `ALGO_UPDATE` WS event, and CONDITIONAL_ORDER_TRIGGER_REJECT was deprecated on 2025-12-15 — [Binance derivatives changelog](https://developers.binance.com/docs/derivatives); live breakage report — [nautilus_trader #3287](https://github.com/nautechsystems/nautilus_trader/issues/3287); SDK route `new_algo_order(algo_type="CONDITIONAL", trigger_price=...)` — [binance-connector-python issue](https://skwrus.duckdns.org/binance/binance-connector-python/issues/545)
- Order-book simulation on Binance and Hyperliquid (practitioner, not peer reviewed): limit fill rates of about 8–25% for directional signals. On Binance, the taker earned about +4.9 bps on signals where the limit would not have filled and about −4.3 bps where it would have filled. A Hyperliquid "maker" backtest of +22.4 bps shrank sharply once realistic fills were applied — [Microstructure Lab](https://themicrostructurelab.substack.com/p/execution-simulation-for-hf-directional)
- On CME futures, adverse fills (a passive order that is out of the money right after the fill) occur in the majority of executions. Fill probability depends on queue position, depth, and market-order arrival — [arXiv 2409.12721](https://arxiv.org/pdf/2409.12721); the trade-off between fill probability and post-fill returns — [arXiv 2502.18625](https://arxiv.org/pdf/2502.18625)
- Blog on FX/futures: fast limit fills (<1 min) have worse quality than slow ones ("fast fills are bad fills") — [Aligrithm](https://aligrithm.com/adverse-selection-is-adverse-selection-porting-fast-fills-are-bad-fills-to-fx-and-futures/) (methodology unclear)
- Stop-market orders fill at the best available book price. A mark-price trigger can widen the gap between trigger and fill, and in flash moves the fill can be far from the stop. A stop-limit order may not fill at all — [Binance Square post](https://www.binance.com/ar/square/post/240059)
- `priceProtect` on STOP_MARKET/TAKE_PROFIT_MARKET blocks the trigger when the gap between mark and last price exceeds the symbol's `triggerProtect` threshold from exchangeInfo — [Binance REST API](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api)

### Inferences
- For a 4h/daily breakout, the break moment carries adverse selection. A passive limit at the breakout level fills mostly when price reverts, which tends to be the losing trades, and misses the runaway winners. Model maker entry as: fill only if price trades through the limit by at least 1 tick (or by a queue proxy), plus an explicit missed-trade cost. Compare against a taker baseline of 0.05% plus half the spread plus impact. A hybrid also needs testing: post GTX for N minutes, then cross.
- The fee gap between maker and taker is only about 3 bps per side, about 6 bps round trip. For daily or 4h trades whose average gain is tens to hundreds of bps, missing winners probably costs more than the fee saving. Exits on stops are taker by nature.
- Stop slippage assumptions to stress-test (my estimates, not sourced): BTC/ETH about 1–3 bps beyond the trigger in normal conditions; thin perps and TradFi perps around reopen or news about 10–50+ bps; gap risk at a session reopen equals the full gap.

### Gaps
- No primary 2026 Binance fee table was retrieved, and no TradFi-specific fee or promo terms were found.
- No published quantitative study of Binance stop-market slippage for BTC/ETH versus thin perps. Measure it from the user's own fills or from aggTrades around stop levels.
- No peer-reviewed study of limit-entry fill rates and adverse selection for breakout entries on crypto perps.

## Binance TradFi perpetuals: launches, hours, off-hours pricing, funding, leverage, liquidity

### Takeaway
The TradFi perps launched from January 2026 (XAU/XAG) through April (energy and SPY) to July (TMF/TBT). The key operational fact: since 2026-09-15 the commodity perps (XAU, XAG, CL, BZ, NATGAS) trade 24/5 with a weekend halt (Fri 21:00 to Sun 21:00 UTC). Equity and ETF perps (SPY, TMF, TBT) appear to remain 24/7, priced off-hours from an orderbook EWMA. Funding is 4h with a ±0.5% cap for commodities and 8h with a ±2% cap for US stocks and ETFs, with the interest component set to 0%.

### Cited Findings
**Launches and specs**
- XAUUSDT on 2026-01-05 and XAGUSDT on 2026-01-07, up to 50x leverage, tick 0.01, min qty 0.001 XAU, min notional 5 USDT — [Treeofalpha](https://www.treeofalpha.com/preview_article?id=1767859201624); [The Block](https://www.theblock.co/post/384743/binance-gold-silver-perpetual-contracts-usdt-settled)
- CLUSDT (09:00 UTC), BZUSDT (09:10 UTC) and NATGASUSDT (09:20 UTC) on 2026-04-01, up to 100x. CL is based on 1,000 bbl. NATGAS size conflicts between 10,000 MMBtu and 1 MMBtu — [Binance on X](https://x.com/binance/status/2039750191708864943); [Bitcoin.com](https://news.bitcoin.com/binance-launches-oil-and-gas-perpetual-futures-with-100x-leverage-amid-iran-war-energy-crisis/); [Coin Bureau](https://x.com/coinbureau/status/2038662540566442156)
- SPYUSDT (with QQQ, AAPL, TSM) at 13:40 UTC on April 6, max 10x. Sources disagree on the year (2025 vs 2026). The 2026 date fits the TradFi program timeline — [TechFlow](https://www.techflowpost.com/en-US/newsletter/118782); [CryptoRank](https://cryptorank.io/news/feed/c82b6-binance-perpetual-futures-qqq-stocks)
- TMFUSDT (13:30 UTC), TBTUSDT (13:35 UTC) and BITOUSDT launched 2026-07-27. Up to 25x, 24/7 trading, 8h funding, 5 USDT min notional. TMF tracks Direxion 3x 20+yr Treasury Bull and TBT tracks ProShares UltraShort 20+yr (one source names a different underlying, so verify) — [crypto.news](https://crypto.news/binance-futures-launches-bito-treasury-etf-contracts/); [CoinGape](https://coingape.com/binance-launches-tradfi-perp-futures-tied-to-us-treasury-bonds-proshares-bitcoin-etf/); [Binance Academy](https://www.binance.com/en/academy/articles/how-to-trade-popmart-tmf-tbt-and-bito-on-binance-futures)
- Binance lists about 180 TradFi perps — [tv-hub](https://www.tv-hub.org/blog/crypto-exchanges-stock-perpetuals/)

**Trading hours and weekend behavior**
- From 2026-09-15 21:00 UTC, XAU, XAG, CL, BZ and NATGAS moved from 24/7 to 24/5. They halt Fri 21:00 UTC to Sun 21:00 UTC and the daily 1h maintenance pause was removed. Positions held past the Friday close "cannot be managed" until reopen. Liquidations and funding are inactive over the weekend. BTC/ETH stay 24/7. Whether equity and ETF perps also move to 24/5 was an open question — [TronWeekly](https://www.tronweekly.com/binance-ends-risky-24-7-trading-for-commodity/); also referenced in [Bitget Academy](https://www.bitget.com/academy/how-to-evaluate-tradfi-perps-liquidity)

**Index and mark price when the underlying is closed**
- At launch, the index aggregated multiple vendors, updated every second in market hours, and was held fixed at its last value outside them — [Treeofalpha](https://www.treeofalpha.com/preview_article?id=1767859201624)
- Early 2026: the index froze at close and the mark price switched to a smoothed EWMA with a ±3% deviation cap for commodities — [BitMEX Q1 2026 report, as cited in search](https://www.bitmex.com/blog/2026q1-derivatives-report) (the page returned 404 on fetch)
- From 2026-05-09 21:00 UTC, commodity TradFi perps switched from Fixed to an **Orderbook EWMA** index during weekends, holidays and maintenance windows. The EWMA index feeds margin and liquidation, so liquidation behaves more like crypto perps. Weekend margin was unchanged. Parameters were not disclosed — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/binance-weekend-pricing-tradfi-futures)
- Since 2026-05-16, equity perps also use Orderbook EWMA for the closed-session index. The mark price keeps its standard median construction — [Vozeso guide](https://vozeso.com/guides/funding-rate-on-equity-perps/)
- In FX perps, the off-hours price is set by Binance's own order book, so weekend prices reflect Binance-only flow — [crypto.news](https://crypto.news/binance-launches-24-7-fx-perpetuals-with-100x-leverage/)
- Incident: Binance removed about 3h of Blue Ocean (overnight venue) data from the US stock-perp funding calculation after a connectivity failure — [Crypto Briefing](https://cryptobriefing.com/binance-excludes-blue-ocean-data-stock-perp-funding/)

**Funding (table as of 2026-10-12)**
- US stocks and ETFs, including leveraged ETFs (SPY, TMF, TBT): 8h, cap ±2.00%. Gold, silver, platinum and palladium: 4h, ±0.50% since 2026-01-30. Copper, WTI, Brent and NatGas: 4h, ±0.50%. The interest component is 0% on TradFi notices. TradFi contracts are exempt from the rule that shortens the interval when the cap is hit, but Binance changes intervals and caps by announcement. Funding is charged on notional and only if the position is held at the settlement instant (not pro-rated) — [Vozeso](https://vozeso.com/guides/funding-rate-on-equity-perps/); exemption also noted by [Cryptonomist](https://en.cryptonomist.ch/2026/07/09/binance-perpetual-contracts-launch/)
- Conflicting figures exist: XAU was reported at ±2% / 4h at launch ([Treeofalpha](https://www.treeofalpha.com/preview_article?id=1767859201624)), and another outlet reports 8h / ±0.375% ([Crypto Briefing](https://cryptobriefing.com/binance-fx-perpetuals-weekend-pricing/)). Use the API values.

**Liquidity**
- Binance holds about 35% of crypto-exchange TradFi-perp OI, with total TradFi OI on CEXs above $2B — [Crypto Briefing](https://cryptobriefing.com/binance-crypto-oi-tradfi-perpetuals/); total RWA-perp OI hit a record $7.9B in the week of Oct 19, with Trade[XYZ] at 48% — [TokenPost](https://www.tokenpost.com/news/investing/39263)
- XAUUSDT depth within ±50 bps was about $14.1M on Binance vs $28.95M on Bitget (Bitget's own study, 2026-08-19, so possibly biased) — [Bitget Academy](https://www.bitget.com/academy/how-to-evaluate-tradfi-perps-liquidity)

### Inferences
- The backtest calendar must match the venue calendar. For XAU/CL/NATGAS on Binance after 2026-09-15 there are no weekend bars, and Sunday 21:00 UTC brings a gap. Stops cannot fire during the halt, so the full weekend gap is realized at reopen. Historical Binance candles before September include synthetic weekend prints (Fixed, then EWMA) that do not exist going forward. Rebuild history with a weekend mask, or use CME-derived data.
- SPY/TMF/TBT perps still trade 24/7 off a Binance-only EWMA index. Weekend moves are local price discovery and can snap to the cash open on Monday. Daily signals computed on 24/7 bars will differ from the underlying's 5-day bars.
- TMF (3x) and TBT (−2x) are daily-rebalanced leveraged ETFs. Perps on them inherit volatility decay relative to the bond itself, so a long TMF sleeve and a short TBT sleeve are not equivalent hedges.
- Funding on SPY/TMF/TBT can run up to ±2% per 8h. Holding through a squeeze is expensive, so include actual historical funding from `GET /fapi/v1/fundingRate` in the backtest rather than a constant.
- The 4h funding on commodities against a 4h bar strategy means each bar boundary can coincide with a settlement. Settlements at 00/04/08/12/16/20 UTC need explicit modeling, as does which side of the timestamp a fill lands on.

### Gaps
- The official Binance "Perpetual Futures on Traditional Assets" FAQ and spec pages were not retrieved, and the Sept-2026 24/5 change was confirmed only via TronWeekly.
- No observed funding-rate history or averages for XAU/CL/SPY/TMF/TBT perps.
- No spread or depth figures for CLUSDT, NATGASUSDT, SPYUSDT, TMFUSDT or TBTUSDT. Measure via `/fapi/v1/depth` snapshots over a week before sizing.
- Current max leverage per symbol (bracket tiers) is unknown. Use `GET /fapi/v1/leverageBracket`.
- EWMA parameters for the off-hours index are undisclosed.

## Backtest vs live pitfalls: funding timing, mark vs last stops, isolated liquidation, one-way vs hedge mode

### Takeaway
Most live-vs-backtest drift comes from four sources: funding counted only at the exact settlement instant; stops triggered on last price while liquidation runs on mark price; the hedge or one-way mode setting, which is account-wide and cannot change with open positions or orders; and the 2025-12 move of conditional orders to the Algo API. Multiple sleeves on one symbol need either hedge mode or an internal netting layer.

### Cited Findings
- Funding is paid or received only if the position is open at the settlement instant. It is not pro-rated and is charged on notional — [Vozeso](https://vozeso.com/guides/funding-rate-on-equity-perps/)
- `workingType` = MARK_PRICE or CONTRACT_PRICE (the default is CONTRACT_PRICE, i.e. last price) for conditional triggers — [Binance REST API](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api)
- A mark-price trigger aligns with the liquidation price, but the fill can deviate more from the trigger — [Binance Square](https://www.binance.com/ar/square/post/240059)
- The mark price combines the index with a moving average of the funding basis. Liquidation happens when the margin ratio reaches 100%, and Binance partially liquidates by IOC reduction first — [KuCoin blog/secondary summary](https://www.kucoin.com/blog/what-happens-when-you-get-liquidated-trading-futures) (secondary, not Binance-official)
- In Hedge Mode (`dualSidePosition=true`), `positionSide` LONG/SHORT is required, and `reduceOnly` cannot be sent on New Order or algo orders. `closePosition` cannot be combined with `quantity` or `reduceOnly`. A mode change is rejected with -4067 (open orders) or -4068 (open position). After the CM migration, UM and CM share the same `dualSidePosition` setting — [Binance REST API](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api)
- STP defaults to EXPIRE_MAKER on New Order. Two sleeves sending opposite orders on the same symbol in the same account can self-cancel — [same](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api)
- On commodity perps, the EWMA off-hours index drives margin and liquidation — [CoinMarketCap](https://coinmarketcap.com/academy/article/binance-weekend-pricing-tradfi-futures)

### Inferences
- **Netting:** In one-way mode, a long sleeve and a short sleeve on the same symbol net to a single position. Each sleeve's stops must then become net-aware: you cannot use `closePosition=true` per sleeve, and a sleeve's stop must be a reduce-only quantity on the net. Hedge mode keeps the legs separate, but you pay funding on both gross legs and fees on both. Margin is not offset in isolated mode, and the stop logic per positionSide is more complex. The Jesse-consistent option is to aggregate target positions across sleeves into one net target per symbol, send only the delta, and keep sleeve-level P&L attribution internally. This saves fees and spread on offsetting orders.
- **Stops:** Backtests usually trigger on the bar's last-price high/low. Live, choose workingType explicitly. MARK_PRICE avoids wick triggers on thin TradFi perps but slips more. With priceProtect=true, a stop can stay untriggered during a dislocation, which is a tail risk. Document the choice per sleeve.
- **Isolated margin:** Per-position liquidation at low leverage (≤3x) is far from the stop, so the risk is mainly the weekend gap on commodities or a flash move on thin perps. Keep effective leverage per position low enough that the worst historical gap is smaller than the distance to liquidation.
- **Funding in backtests:** Apply realized historical funding at the exact timestamps: 8h at 00/08/16 UTC for most crypto, 4h for commodities and some alts, and intervals can change. Do not use daily averages. Daily-bar strategies entering at 00:00 UTC face an ordering question: was the entry before or after the 00:00 funding settlement?
- **Algo API:** Any live connector (jesse-live included) must use `/fapi/v1/algoOrder` for stops since 2025-12-09. Verify this before paper trading.

### Gaps
- An official Binance mark-price formula page for TradFi perps was not retrieved.
- No source quantified the frequency of priceProtect blocking a stop.
- Whether jesse-live already uses the Algo endpoints was not checked in this research.

## Portfolio risk for multi-sleeve small accounts (~10k USD)

### Takeaway
Vol targeting reliably cuts tail risk and drawdowns. Its Sharpe benefit is mainly for "risk assets", with a negligible Sharpe effect on bonds, commodities and FX. Correlations of assets and strategies converge toward 1 in stress, so add a correlation-regime overlay and an independent kill switch. Exchange minimum notionals (5 USDT on TradFi perps) do not constrain a $10k account. Lot and tick rounding on larger contracts might.

### Cited Findings
- Harvey et al. (2018, JPM) tested 60+ assets with data back to 1926. Vol targeting improves Sharpe only for risk assets (equity, credit), with a negligible effect on bonds, FX and commodities. It consistently reduces extreme returns and vol-of-vol, and reduces max drawdown for balanced and risk-parity portfolios. Their setup used a 10% target with daily-return std — [Quantpedia summary](https://quantpedia.com/the-impact-of-volatility-targeting-on-equities-bonds-commodities-and-currencies); [Alpha Architect](https://alphaarchitect.com/volatility-targeting-improves-risk-adjusted-returns/)
- Crypto assets correlate more strongly when they share a high-vol regime, so diversification is least effective then — [Waikato research commons](https://researchcommons.waikato.ac.nz/handle/10289/15597)
- In crises, correlations of both assets and strategies tend toward one — [Paradigm](https://paradigm.co/blog/institutional-money-in-crypto-lessons-from-tradfi)
- Practitioner heuristic (unvalidated): when rolling 30d correlation among majors exceeds 0.85, cut gross exposure; when it is very high, use a correlation kill switch that halves gross. The kill switch should run as a separate process able to override the trading system — [PromptIndex guide](https://www.thepromptindex.com/skill/771-risk-management-crypto)
- TradFi perps carry 5 USDT minimum notional — [crypto.news](https://crypto.news/binance-futures-launches-bito-treasury-etf-contracts/)

### Inferences (design proposals, not sourced facts)
- **Layering:**
  1. Sleeve-level vol target, using EWMA vol on 4h/daily returns.
  2. Portfolio vol target using a shrunk covariance.
  3. Hard caps: gross leverage (e.g. ≤2–3x), per-symbol notional, per-asset-class (crypto beta) caps, and a cap on net same-direction crypto exposure.
  4. Correlation overlay: when average pairwise correlation or the first-PC share spikes, scale down gross.
  5. Drawdown circuit breakers: e.g. −X% daily or −Y% from peak flattens or halves exposure, with a cooldown.
  6. An operational kill switch in a separate process: API errors, position mismatch versus intended net target, missing stop (algo order absent), stale data, funding spike.
- Because the vol-target Sharpe benefit is negligible on commodities and bonds, the reason to vol-target the XAU/CL/TMF sleeves is risk control, not alpha.
- Weekend-halted commodity sleeves need a gap-risk budget, either by reducing size into the Friday close or by sizing on gap-inclusive vol.
- With about $10k, check each symbol's `stepSize` and `minNotional` against the smallest vol-scaled order. Rounding can produce zero or oversize positions in low-weight sleeves.

### Gaps
- No rigorous source on vol targeting combined with trend signals in crypto specifically, or on small-account multi-sleeve sizing.
- The kill-switch and correlation thresholds found are rules of thumb that need to be backtested.
