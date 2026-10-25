# Short-side trend by asset family and regularity of a trend portfolio (r51 research notes)

> NOTE: Plan mode was active, so these notes could not be written to the requested path
> (`...\scratchpad\research_notes\Bono WTI altcoins y regularidad r51\cortos_regularidad.md`).
> They are stored here; copy them there once plan mode is off.

## Q1. Long/short vs long-only trend per asset class: where do shorts add value?

### Takeaway
The evidence is that shorts in equities and bonds work as crisis insurance rather than as standalone return sources. Over the long run the short legs earn little or nothing, because of positive drift (equities) and positive roll/carry (bonds 1985–2020). Shorts look most defensible where the term structure pays the short (contango commodities, especially nat gas) and in bonds during rising-rate regimes. I found no primary per-asset-class Sharpe split of the long and short legs.

### Cited Findings
- Moskowitz-Ooi-Pedersen (JFE 2012): TSMOM across 58 futures (equity indices, FX, commodities, bonds). The 12-month TSMOM was profitable for every contract examined, 1985–2009. The diversified portfolio performs best in extreme markets. The paper reports the long/short factor, not separate legs. — [AQR data page](https://www.aqr.com/insights/datasets/time-series-momentum-original-paper-data); [SSRN](https://papers.ssrn.com/abstract=2089463)
- Kim, Tse and Wald (2013) critique: much of the MOP alpha comes from volatility scaling. Alpha falls from 1.27% to 0.41% without vol scaling, and the edge vanishes in 2009–2013. — [Quantpedia summary](https://quantpedia.com/?p=637)
- Hurst-Ooi-Pedersen "A Century of Evidence on Trend Following": equal-weighted 1/3/12-month TSMOM on 67 markets in 4 asset classes. Positive on average since 1985 for nearly all equity, bond, commodity and FX markets. No long/short leg split in the excerpts. — [AQR PDF mirror](https://www.TrendFollowing.com/whitepaper/Century_Evidence_Trend_Following.pdf)
- 1800–2014 study (CXO summary): vol-scaled long-and-short EMA trend gave steadier gross risk-adjusted returns than long-only. The results are gross of costs. — [CXO Advisory](https://www.cxoadvisory.com/technical-trading/trend-following-over-the-very-long-run/)
- Hamill, Rattray and Van Hemert (Man, 2016), "Trend Following: Equity and Bond Crisis Alpha", 1960–2015:
  - Trend performed well both before 1985 (bond bear) and after 1985 (bond bull).
  - Returns are positively skewed, more so for fast trend.
  - There is an "equity smile" and a stronger "bond smile".
  - Restricting equity/bond positions to non-positive (short-only or flat) improves crisis performance but reduces the average return. It also worsens protection in the other asset's sell-off.
  - Lags of 1–4 and 9–11 months work; lags of 5–8 months underperform.
  - The summary page gives no Sharpe numbers.
  - [Man Institute](https://www.man.com/maninstitute/trend-following-equity-and-bond-crisis-alpha)
- Peltomäki, Sinclair and Agerbäck (2016), "The Long & Short of Trend Followers":
  - Long legs make money long-term, while short legs "fail to generate any significant positive long term performance".
  - Short equity signals diversified well in the 2000–02 and 2008 crises.
  - Short bond positions gave brief gains, then reverted to losses when stopped out.
  - Bond roll yield is "almost always positive", so shorting bond futures carries a large carry cost.
  - [Hedge Fund Journal](https://thehedgefundjournal.com/the-two-tales-of-trend-followers/)
- Same authors, rates sensitivity, 1984–2015: long (short) bond trend does very poorly (well) when rates rise. In equities the long side is hurt more by rising rates. The effect is weak in commodities and FX. Overall, futures trend behaves partly like a long-bond strategy. — [CXO Advisory](https://www.cxoadvisory.com/economic-indicators/risk-aspects-of-long-and-short-futures-trend-following)
- Crypto: an Erasmus thesis finds 85% of long-only crypto TSMOM portfolios had significant positive excess returns, while long-short ones did not. Han-Kang-Ryu find strong crypto TSMOM but warn that losers often rebound sharply, which is the risk the short leg carries. These are theses and working papers, so the evidence is weak. — [Erasmus thesis](https://thesis.eur.nl/pub/44390/); [Han-Kang-Ryu PDF](https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf)
- Conditional roll: for energy futures, going long in backwardation and short in contango gives the highest Sharpe among the rollover strategies tested, for all commodities (Ghoddusi). — [Quantpedia](https://quantpedia.com/effect-of-maturity-structure-of-roll-yields-in-commodity-futures-strategies/)

### Inferences
- **Equities (S&P500) and gold:** shorts are an insurance leg with a negative or near-zero long-run return. Add them only if the goal is crisis convexity, not monthly regularity. A short leg in a positive-drift asset lowers the hit rate in most years, through whipsaw around bear-market rallies.
- **Long bond:** the short leg historically paid in the 2022-type regime, but bleeds carry in normal regimes. A carry or curve-slope gate is the natural condition (short only when roll yield is negative or small).
- **WTI and nat gas:** these are the best case for shorts when contango is present. A curve-conditioned short (short only in contango) is supported by the roll literature. On a perpetual, funding replaces roll (see Q5).
- **BTC and ETH:** the evidence leans against crypto shorts (the rebound risk). Shorting is not recommended beyond maybe a small, fast, regime-gated sleeve.

### Gaps
- I could not retrieve a primary per-asset-class Sharpe table for the long and short legs. MOP and HOP do not report one in the parts I could read; the HOP PDF was encrypted and could not be parsed.
- I did not find the specific paper titled "Does trend following work on shorts?".
- I found no primary AQR or Man AHL "long-only trend" whitepaper with numbers.
- Research Affiliates (Feb 2026), "Should Trend Follow Carry: Lessons from Bonds, Gold, and 2022", looks directly relevant to gating bond and gold trend by carry, but the fetch returned 403. — [Advisor Perspectives](https://www.advisorperspectives.com/commentaries/2026/02/26/trend-follow-carry-lessons-bonds-gold-2022?topic=insurance-annuities)

## Q2. Regime-conditioned shorts (price < 200d MA, falling 50d): evidence, skew and crash risk

### Takeaway
I found no direct OOS study of 200d/50d-gated short trend. Indirect evidence says short legs have worse skew than long legs in drifting assets, because bear-market rallies are violent. Restricting to short-only improves crisis returns at the cost of average return.

### Cited Findings
- Non-positive restriction: better crisis alpha, lower average return (Hamill-Rattray-Van Hemert). — [Man Institute](https://www.man.com/maninstitute/trend-following-equity-and-bond-crisis-alpha)
- Short bond trades are repeatedly stopped out after brief gains. — [Hedge Fund Journal](https://thehedgefundjournal.com/the-two-tales-of-trend-followers/)
- Slow signals suffer turning-point losses, while fast signals give false alarms (Goulding, Harvey and Mazzoleni, 2023). — [Quantpedia](https://quantpedia.com/?p=34662)
- Crypto losers often rebound and inflict large losses on shorts. — [Han-Kang-Ryu](https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/918729/Time_Series_and_Cross_Sectional_Momentum_in_the_Cryptocurrency_Market_with_IA.pdf)

### Inferences
- A double gate (price < 200d and 50d falling) reduces whipsaw but enters late and exits late. The short P&L becomes concentrated in a few crash episodes (2008, 2020, 2022), which gives low monthly regularity even when the full-sample result is positive. For a regularity objective, these shorts are likely to lower the hit rate in months.

### Gaps
- No quantified OOS data for MA-gated shorts per asset class. This has to be tested in-house (preregistered).

## Q3. Sharpe vs % positive months/quarters; is 80% positive quarters realistic?

### Takeaway
Under a normal i.i.d. model, P(period > 0) = Φ(SR·√(T/12)), with T in months. At SR 1.5 that gives about 67% positive months and 77% positive quarters. An 80% quarter rate needs SR ≈ 1.68, and a 65% month rate needs SR ≈ 1.33. Positive skew in trend pulls the median below the mean, so the observed hit rate falls short of the normal value. The team's 58%/70% at SR 1.5 fits a strongly positively skewed return stream.

### Cited Findings
- Trend returns are positively skewed, especially for fast trend. — [Man Institute](https://www.man.com/maninstitute/trend-following-equity-and-bond-crisis-alpha)
- SG Trend Index since 2000: CAGR ≈ 5.23% and max drawdown ≈ 20.6% (as of Oct 2025). The source does not give a positive-month figure. — [Top Traders Unplugged](https://www.toptradersunplugged.com/trend-following-performance-report-october-2025/)
- Barclay CTA Index: 27 positive years vs 5 losing years, 1980–2011. No monthly or quarterly hit rate given. — [BarclayHedge PR](https://barclayhedge.com/insider/pr_jan_16_2014)

### Inferences (my computation, normal approx, not sourced)

| SR | % months > 0 | % quarters > 0 |
|---|---|---|
| 1.4 | 65.7% | 75.8% |
| 1.5 | 66.7% | 77.3% |
| 1.6 | 67.8% | 78.8% |

- Implied "median Sharpe" from the observed rates:
  - 58% months → z = 0.20 → implied SR ≈ 0.70.
  - 70% quarters → z = 0.52 → implied SR ≈ 1.05.
  - Together these say the median return is well below the mean, which is the skew signature.
- Raising the hit rate therefore means either raising SR (to about 1.7+ for 80% quarters even with normal returns) or reducing positive skew, by adding negatively or neutrally skewed sleeves. Reducing skew trades away crisis convexity.
- My prior is that diversified CTA indices with SR around 0.3–0.6 have roughly 50–55% positive months. An 80% positive-quarter rate is unlikely for any pure trend program over long samples, but this prior is not sourced (see Gaps).

### Gaps
- No sourced long-run % positive months/quarters for the SG Trend, SG CTA or Barclay CTA indices. This needs the index factsheets or the BarclayHedge historical data.

## Q4. Levers that raise regularity

### Takeaway
The strongest documented lever is blending lowly correlated trend speeds. Vol targeting mainly trims tails, with a Sharpe gain only in risk assets. Carry or uncorrelated low-skew sleeves raise the hit rate most directly, but they reintroduce negative skew.

### Cited Findings
- Man AHL: trend models at different speeds have positive long-term returns and low mutual correlation, so trading all speeds raises risk-adjusted return. Slower speeds have higher average return, while faster speeds give more crisis alpha. — [Man, "Need for speed"](https://www.man.com/maninstitute/need-for-speed-trend-following)
- Harvey et al. (JPM 2018), 60 assets back to 1926:
  - Vol targeting raises Sharpe only for equity and credit. For example, US equity goes from 0.40 to 0.48–0.51.
  - The Sharpe effect is negligible for bonds, FX and commodities.
  - Vol targeting reduces extreme returns and left tails across all asset classes.
  - [Duke PDF](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf); [Alpha Architect](https://alphaarchitect.com/volatility-targeting-improves-risk-adjusted-returns/)
- Vol scaling explains a large part of TSMOM alpha. — [Quantpedia on Kim-Tse-Wald](https://quantpedia.com/?p=637)
- Conditional carry (curve-based) gives the best Sharpe among the commodity roll strategies tested. — [Quantpedia](https://quantpedia.com/effect-of-maturity-structure-of-roll-yields-in-commodity-futures-strategies/)
- Self-run, non-peer-reviewed backtest of daily L/S trend: net Sharpe 0.73 on futures and 0.56 on crypto. — [Delphic Alpha](https://delphicalpha.substack.com/p/daily-longshort-trend-following-parameters)

### Inferences
- Ranked by expected effect on the hit rate per unit of CAGR given up:
  1. Blend speeds and lookbacks inside each Donchian sleeve.
  2. Equal-risk (risk-parity) sleeve weights with vol targeting, which lowers concentration in crypto and so the variance of monthly P&L.
  3. A bounded carry sleeve (commodity curve, funding-rate carry on perps).
  4. Correlation-aware sizing (cap the cluster risk of BTC/ETH/4h-crypto).
- Rebalancing frequency should matter little for the hit rate, beyond cost and turnover effects (not sourced).

### Gaps
- No sourced quantitative evidence on the effect on % positive months of rebalancing frequency, dynamic correlation control or short-vol sleeves.

## Q5. Natural gas: trend vs seasonality vs short bias; perpetual funding

### Takeaway
Front-month nat gas futures had a strongly negative excess return, about -25%/yr over 2010–2022, from structural contango, punctuated by winter spikes. This favors a short bias or contango-gated shorts in the futures market. A perpetual (NATGASUSDT) does not roll, so this edge only carries over if the perp tracks the front future and funding does not offset it.

### Cited Findings
- Nat gas front contract: average return close to -25% p.a. from 2010 to the 2022 energy crisis. Vontobel attributes this to shale-driven structural contango. Winter cold shocks (Dec 2013, Dec 2018, Mar 2023) briefly pushed excess returns positive. — [Vontobel](https://am.vontobel.com/en/insights/costa-de-roll-how-to-ride-the-commodity-curve)
- Contango commodities, including gas, delivered worse returns in Q2 2026 (commentary only). — [XTB](https://www.xtb.com/sca-en/market-analysis/news-and-research/commodity-summary-for-half-year-and-quarter-main-losers-and-winners)
- Conditional short-in-contango, long-in-backwardation is the best roll strategy. — [Quantpedia](https://quantpedia.com/effect-of-maturity-structure-of-roll-yields-in-commodity-futures-strategies/)

### Inferences
- On a perpetual, the "roll yield" is embedded only if the index or mark price is a front-month futures price that rolls (the perp then inherits roll drift in its price). If the perp's index tracks spot or a constant-maturity price, the contango drift does not appear and funding becomes the carry term. Verify from the exchange's NATGASUSDT index methodology and the history of funding rates.
- Winter spike risk makes naked shorts high-kurtosis. Pair the shorts with a seasonal filter (avoid Nov–Feb) or a tight vol stop.

### Gaps
- I found no study of NATGASUSDT funding vs futures roll, and no peer-reviewed net-of-cost study of short nat gas. I ran out of tool budget before searching the exchange's index methodology.
