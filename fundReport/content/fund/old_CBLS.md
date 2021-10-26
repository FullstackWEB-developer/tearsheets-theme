---
date: 2021-06-08T22:33:29-04:00
draft: false
strategy_id: asdf-asdf-asdf-asdf
user_id: skruzel
as_of_date: 2021-06-15T22:33:29-04:00
request_params: BenchmarkReportRequest
meta: # BenchmarkReportMeta
    ticker: CBLS
    name: Changebridge Capital Long/Short Equity ETF
    description: "The Changebridge Capital Long/Short Equity ETF (the \"Fund\" or \"Long/Short Equity Fund\") seeks long-term capital appreciation while minimizing volatility. The fund also strives to generate positive alpha via both the long and short portfolios over the course of an entire investment cycle. The Fund has the potential to enhance an investor's return profile while reducing risk."
    fund_family: Changebridge Funds
    url: https://changebridgefunds.com/
    logo: https://changebridgefunds.com/assets/img/Changebridge_Logo_FINAL_Horizontal%20White.svg
    colors: ReportColors
replication: # ReplicationDetails
    vintage: 2021-03-31
    in_sample: # PeriodRange
        name: in sample
        start_period: 2020-11-16
        end_period: 2021-03-31
    out_sample: # PeriodRange
        name: out sample
        start_period: 2021-04-01
        end_period: 2021-06-15
    scoring_stats: # ReplicationStats
        initial_factors: 2222
        total_strategies: 778
        has_min_completeness: 581
        cluster_max: 256
        cluster_limit: 100
        strategy_limit: 1000
        qualified_strategies: 369
        is_portformer: False
kpis: Optional[List[str]]
statistics:
  - period_name: all
    start_period: 2020-11-16
    end_period: 2021-06-15
    num_dates: 146
    nav_name: CBLS
    bench_name: Benchmark
    stats:
      -  name: Returns
         units: annualized
         value: 0.5795144120701958
         bench: 0.3059194475614502
         difference: 0.27359496450874565
         alert: 1.0
         value_formatted: 58.0%
         bench_formatted: 30.6%
         difference_formatted: 27.4%
      -  name: Volatility
         units: annualized
         value: 0.1949149146013529
         bench: 0.24849396098782842
         difference: -0.05357904638647551
         alert: 1.0
         value_formatted: 19.5%
         bench_formatted: 24.8%
         difference_formatted: -5.4%
      -  name: Sharpe Ratio
         value: 2.4445018714278484
         bench: 1.1984320444346006
         difference: 1.2460698269932478
         alert: 1.0
         value_formatted: 2.44
         bench_formatted: 1.20
         difference_formatted: 1.25
      -  name: Max Drawdown
         value: -0.0976941376319474
         bench: -0.2007624738696116
         difference: 0.1030683362376642
         alert: 1.0
         value_formatted: -9.8%
         bench_formatted: -20.1%
         difference_formatted: 10.3%
figures:
    performance:
        name: Performance
        alt: Total Returns of $10,000
        src: /img/cbls_performance.png
    tracking_error:
        name: Tracking Error
        alt: CBLS vs Benchmark
        src: /img/cbls_relative_performance.png
    drawdown:
        name: Drawdowns
        alt: Drawdowns of CBLS and Benchmark
        src: /img/cbls_drawdown.png
    qr_code:
        name: CBLS Report QR CODE
        alt: Live Report
        src: /img/cbls_qr.png
holdings: # BucketedReportHoldings
    name: PTMC + LABU + PILL + PBW + QMOM
    as_of_date: 2021-06-30
    levels:
     - Top ETF Replacements
    max_depth: 2
    buckets: # SingleBucketOfHoldings
      - id: 0
        name: $PTMC
        positions:
          - ticker: PTMC
            name: Pacer Trendpilot US Mid Cap ETF
            figi: Optional[str]
            exchange: Optional[str]
            weight: 0.57
        replacement_score:
          vintage: 2020-03-31
          score: 58.6
          completeness: float
          stability: float
          simplicity: float
          confidence: float
      - id: 1
        name: $LABU
        positions:
          - ticker: LABU
            name: Direxion Daily S&P Biotech Bull 3x Shares
            figi: Optional[str]
            exchange: Optional[str]
            weight: 0.06
        replacement_score:
          vintage: 2020-03-31
          score: 55.7
          completeness: float
          stability: float
          simplicity: float
          confidence: float
      - id: 2
        name: $PILL
        positions:
          - ticker: PILL
            name: Direxion Daily Pharmaceutical & Medical Bull 3x Shares
            figi: Optional[str]
            exchange: Optional[str]
            weight: 0.094
        replacement_score:
          vintage: 2020-03-31
          score: 51.7
          completeness: float
          stability: float
          simplicity: float
          confidence: float
      - id: 3
        name: $PBW
        positions:
          - ticker: PBW
            name: Invesco WilderHill Clean Energy ETF
            figi: Optional[str]
            exchange: Optional[str]
            weight: 0.11
        replacement_score:
          vintage: 2020-03-31
          score: 49.9
          completeness: float
          stability: float
          simplicity: float
          confidence: float
      - id: 4
        name: $QMOM
        positions:
          - ticker: QMOM
            name: Alpha Architect U.S. Quantitative Momentum ETF
            figi: Optional[str]
            exchange: Optional[str]
            weight: 0.162
        replacement_score:
          vintage: 2020-03-31
          score: 48.5
          completeness: float
          stability: float
          simplicity: float
          confidence: float
    replacement_score: 58.6
---


