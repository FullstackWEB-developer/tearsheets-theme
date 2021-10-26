---
as_of_date: '2021-06-29'
figures:
  drawdown:
    alt: Drawdowns of CBLS and Benchmark
    name: Drawdowns
    src: /img/CBLS-drawdown.png
  performance:
    alt: Total Returns of $10,000
    name: Performance
    src: /img/CBLS-performance.png
  qr_code:
    alt: Live Report
    name: CBLS Report QR CODE
    src: /img/CBLS-qr-code.png
  tracking_error:
    alt: CBLS vs Benchmark
    name: Tracking Error
    src: /img/CBLS-relative-performance.png
holdings:
  as_of_date: '2021-06-29'
  buckets:
  - id: '0'
    name: all
    positions:
    - name: Direxion Daily Transportation Bull 3X Shares
      ticker: TPOR
      weight: 0.09540090159139705
    - name: ProShares UltraPro MidCap400
      ticker: UMDD
      weight: 0.12605128240245922
    - name: Impact Shares Sustainable Development Goals Global Equity ETF
      ticker: SDGA
      weight: 0.3511819044698999
    - name: Direxion Daily Financial Bull 3x Shares
      ticker: FAS
      weight: 0.06940891960846174
    - name: Goldman Sachs Equal Weight U.S. Large Cap Equity ETF
      ticker: GSEW
      weight: 0.35795699192778213
    replacement_score:
      completeness: 52.04642800316912
      confidence: 20.026860935692994
      score: 49.94771189934963
      simplicity: 30.307691320517105
      stability: 97.40986733801931
      vintage: '2021-04-01'
  levels:
  - all
  max_depth: 0
  name: TPOR + UMDD + SDGA + FAS + GSEW
  replacement_score:
    completeness: 52.04642800316912
    confidence: 20.026860935692994
    score: 49.94771189934963
    simplicity: 30.307691320517105
    stability: 97.40986733801931
    vintage: '2021-04-01'
  start_date: '2021-06-25'
kpis: []
meta:
  colors:
    accent: red
    primary: '#125470'
    secondary: red
    warn: red
  description: The Changebridge Capital Long/Short Equity ETF (the "Fund" or "Long/Short
    Equity Fund") seeks long-term capital appreciation while minimizing volatility.
    The fund also strives to generate positive alpha via both the long and short portfolios
    over the course of an entire investment cycle. The Fund has the potential to enhance
    an investor's return profile while reducing risk.
  logo: https://changebridgefunds.com/assets/img/Changebridge_Logo_FINAL_Horizontal%20White.svg
  name: Changebridge Capital Long/Short Equity ETF
  ticker: CBLS
periods:
- end_period: '2021-06-29'
  name: all
  start_period: '2020-11-13'
- end_period: '2021-03-31'
  name: in sample
  start_period: '2020-11-13'
- end_period: '2021-06-29'
  name: out sample
  start_period: '2021-04-01'
replication:
  in_sample:
    end_period: '2021-03-31'
    name: in sample
    start_period: '2020-11-13'
  out_sample:
    end_period: '2021-06-29'
    name: out sample
    start_period: '2021-04-01'
  scoring_stats:
    cluster_limit: 100
    cluster_max: 258
    has_min_completeness: 632
    is_portformer: false
    qualified_strategies: 433
    strategy_limit: 0
    total_strategies: 777
  vintage: '2021-04-01'
request_params:
  by_cluster: true
  fn: portformer_replication_report
  min_months: 12
  months: 0
  ticker: CBLS
  top_n: 5
  use_cash: false
  years: 1
statistics:
- bench_name: Benchmark
  end_period: '2021-06-29'
  name: all
  nav_name: CBLS
  num_dates: 156
  start_period: '2020-11-13'
  stats:
  - alert: -1.0
    bench: 0.7526336006232952
    bench_formatted: 75.3%
    difference: -0.2822521314693076
    difference_formatted: -28.2%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 0.4703814691539876
    value_formatted: 47.0%
  - alert: -1.0
    bench: 0.4153257754999986
    bench_formatted: 41.5%
    difference: -0.14578353406152433
    difference_formatted: -14.6%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.2695422414384743
    value_formatted: 27.0%
  - alert: 1.0
    bench: 0.22360923114485487
    bench_formatted: 22.4%
    difference: -0.030541995729113786
    difference_formatted: -3.1%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.19306723541574108
    value_formatted: 19.3%
  - alert: -1.0
    bench: 2.6232205613586275
    bench_formatted: '2.62'
    difference: -0.5286105452731631
    difference_formatted: '-0.53'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 2.0946100160854644
    value_formatted: '2.09'
  - alert: -1.0
    bench: 8.988070879748026
    bench_formatted: '8.99'
    difference: -4.1732326452768715
    difference_formatted: '-4.17'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 4.814838234471154
    value_formatted: '4.81'
  - alert: -1.0
    bench: 0.9396771123759902
    bench_formatted: '0.94'
    difference: -0.36255051469167954
    difference_formatted: '-0.36'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.5771265976843106
    value_formatted: '0.58'
  - alert: -1.0
    bench: -0.08373694541273964
    bench_formatted: -8.4%
    difference: -0.013957192219207756
    difference_formatted: -1.4%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.0976941376319474
    value_formatted: -9.8%
  - alert: -1.0
    bench: 1.543452100500536
    bench_formatted: '1.54'
    difference: -0.1347768727344616
    difference_formatted: '-0.13'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.4086752277660743
    value_formatted: '1.41'
  - alert: -1.0
    bench: 4.144990762666643
    bench_formatted: '4.14'
    difference: -1.1086629722529242
    difference_formatted: '-1.11'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 3.0363277904137185
    value_formatted: '3.04'
  - alert: -1.0
    bench: -0.17800816324460872
    bench_formatted: '-0.18'
    difference: -0.426266607777438
    difference_formatted: '-0.43'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.6042747710220467
    value_formatted: '-0.60'
  - alert: 1.0
    bench: 0.6764931855141714
    bench_formatted: '0.68'
    difference: 0.5612912367334446
    difference_formatted: '0.56'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 1.237784422247616
    value_formatted: '1.24'
  - alert: -1.0
    bench: 1.2568297164847884
    bench_formatted: '1.26'
    difference: -0.21726543879171256
    difference_formatted: '-0.22'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.0395642776930758
    value_formatted: '1.04'
  - alert: 1.0
    bench: -0.020400206019301342
    bench_formatted: -2.0%
    difference: 0.001780179550255917
    difference_formatted: 0.2%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.018620026469045425
    value_formatted: -1.9%
  - alert: 1.0
    bench: -0.0306262363869214
    bench_formatted: -3.1%
    difference: 0.0031582247122457913
    difference_formatted: 0.3%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.027468011674675608
    value_formatted: -2.7%
  - alert: -1.0
    bench: 8.988070879748026
    bench_formatted: '8.99'
    difference: -4.1732326452768715
    difference_formatted: '-4.17'
    name: Romad
    stat_id: romad
    units: ''
    value: 4.814838234471154
    value_formatted: '4.81'
  - alert: 0.0
    bench: 156
    bench_formatted: '156.00'
    difference: 0.0
    difference_formatted: '0.00'
    name: Num Days
    stat_id: num_days
    units: ''
    value: 156
    value_formatted: '156.00'
  - alert: -1.0
    bench: 0.5153426512449607
    bench_formatted: 51.5%
    difference: 0.14075558691245782
    difference_formatted: 14.1%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 0.6560982381574185
    value_formatted: 65.6%
- bench_name: Benchmark
  end_period: '2021-03-31'
  name: in sample
  nav_name: CBLS
  num_dates: 94
  start_period: '2020-11-13'
  stats:
  - alert: -1.0
    bench: 1.073317178107224
    bench_formatted: 107.3%
    difference: -0.030841719440247495
    difference_formatted: -3.1%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 1.0424754586669764
    value_formatted: 104.2%
  - alert: -1.0
    bench: 0.31256660249999935
    bench_formatted: 31.3%
    difference: -0.007317428504685086
    difference_formatted: -0.7%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.30524917399531426
    value_formatted: 30.5%
  - alert: 1.0
    bench: 0.24730497312918873
    bench_formatted: 24.7%
    difference: -0.03922420874686244
    difference_formatted: -3.9%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.20808076438232628
    value_formatted: 20.8%
  - alert: 1.0
    bench: 3.0749099551816723
    bench_formatted: '3.07'
    difference: 0.4654271158955843
    difference_formatted: '0.47'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 3.5403370710772566
    value_formatted: '3.54'
  - alert: -1.0
    bench: 12.817725471317834
    bench_formatted: '12.82'
    difference: -0.49462931912059815
    difference_formatted: '-0.49'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 12.323096152197236
    value_formatted: '12.32'
  - alert: -1.0
    bench: 0.9189128641044194
    bench_formatted: '0.92'
    difference: -0.03703026591557412
    difference_formatted: '-0.04'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.8818825981888453
    value_formatted: '0.88'
  - alert: -1.0
    bench: -0.08373694541273964
    bench_formatted: -8.4%
    difference: -0.0008583093667258873
    difference_formatted: -0.1%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.08459525477946553
    value_formatted: -8.5%
  - alert: 1.0
    bench: 1.6636683820027918
    bench_formatted: '1.66'
    difference: 0.10959696449204803
    difference_formatted: '0.11'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.7732653464948398
    value_formatted: '1.77'
  - alert: 1.0
    bench: 4.975085008355018
    bench_formatted: '4.98'
    difference: 0.37973970382571043
    difference_formatted: '0.38'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 5.354824712180728
    value_formatted: '5.35'
  - alert: -1.0
    bench: -0.19533606964295336
    bench_formatted: '-0.20'
    difference: -0.5474727450631168
    difference_formatted: '-0.55'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.7428088147060702
    value_formatted: '-0.74'
  - alert: 1.0
    bench: 0.41062567434459085
    bench_formatted: '0.41'
    difference: 0.9031787192315979
    difference_formatted: '0.90'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 1.3138043935761887
    value_formatted: '1.31'
  - alert: 1.0
    bench: 1.1252321039460011
    bench_formatted: '1.13'
    difference: 0.024010464545758392
    difference_formatted: '0.02'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.1492425684917595
    value_formatted: '1.15'
  - alert: 1.0
    bench: -0.024023332738697237
    bench_formatted: -2.4%
    difference: 0.0045740632328657195
    difference_formatted: 0.5%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.019449269505831517
    value_formatted: -1.9%
  - alert: 1.0
    bench: -0.03254226122903754
    bench_formatted: -3.3%
    difference: 0.0035197414041021197
    difference_formatted: 0.4%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.029022519824935422
    value_formatted: -2.9%
  - alert: -1.0
    bench: 12.817725471317834
    bench_formatted: '12.82'
    difference: -0.49462931912059815
    difference_formatted: '-0.49'
    name: Romad
    stat_id: romad
    units: ''
    value: 12.323096152197236
    value_formatted: '12.32'
  - alert: 0.0
    bench: 94
    bench_formatted: '94.00'
    difference: 0.0
    difference_formatted: '0.00'
    name: Num Days
    stat_id: num_days
    units: ''
    value: 94
    value_formatted: '94.00'
  - alert: -1.0
    bench: 0.35526117934210655
    bench_formatted: 35.5%
    difference: 0.7830856981344714
    difference_formatted: 78.3%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 1.138346877476578
    value_formatted: 113.8%
- bench_name: Benchmark
  end_period: '2021-06-29'
  name: out sample
  nav_name: CBLS
  num_dates: 62
  start_period: '2021-04-01'
  stats:
  - alert: -1.0
    bench: 0.3584767342854749
    bench_formatted: 35.8%
    difference: -0.465093627793701
    difference_formatted: -46.5%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: -0.10661689350822612
    value_formatted: -10.7%
  - alert: -1.0
    bench: 0.07828873049510543
    bench_formatted: 7.8%
    difference: -0.10564514126190383
    difference_formatted: -10.6%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: -0.0273564107667984
    value_formatted: -2.7%
  - alert: 1.0
    bench: 0.18260144589996158
    bench_formatted: 18.3%
    difference: -0.018268815284078227
    difference_formatted: -1.8%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.16433263061588335
    value_formatted: 16.4%
  - alert: -1.0
    bench: 1.7687471401104582
    bench_formatted: '1.77'
    difference: -2.373447099736712
    difference_formatted: '-2.37'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: -0.6046999596262538
    value_formatted: '-0.60'
  - alert: -1.0
    bench: 5.750034743344741
    bench_formatted: '5.75'
    difference: -6.841368328885916
    difference_formatted: '-6.84'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: -1.091333585541175
    value_formatted: '-1.09'
  - alert: -1.0
    bench: 0.4401393195359668
    bench_formatted: '0.44'
    difference: -0.2855862314997901
    difference_formatted: '-0.29'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.15455308803617668
    value_formatted: '0.15'
  - alert: -1.0
    bench: -0.06234340317689148
    bench_formatted: -6.2%
    difference: -0.03535073445505585
    difference_formatted: -3.5%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.09769413763194733
    value_formatted: -9.8%
  - alert: -1.0
    bench: 1.3300426397911806
    bench_formatted: '1.33'
    difference: -0.4250970290519652
    difference_formatted: '-0.43'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 0.9049456107392154
    value_formatted: '0.90'
  - alert: -1.0
    bench: 2.6399475829839045
    bench_formatted: '2.64'
    difference: -3.427058352185873
    difference_formatted: '-3.43'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: -0.7871107692019688
    value_formatted: '-0.79'
  - alert: -1.0
    bench: -0.32466071235459665
    bench_formatted: '-0.32'
    difference: -0.22549590738836994
    difference_formatted: '-0.23'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.5501566197429666
    value_formatted: '-0.55'
  - alert: 1.0
    bench: 0.5715457476585617
    bench_formatted: '0.57'
    difference: 0.4306043281595895
    difference_formatted: '0.43'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 1.0021500758181512
    value_formatted: '1.00'
  - alert: -1.0
    bench: 1.1387619735529693
    bench_formatted: '1.14'
    difference: -0.08741152487306403
    difference_formatted: '-0.09'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.0513504486799052
    value_formatted: '1.05'
  - alert: 1.0
    bench: -0.016887433788838228
    bench_formatted: -1.7%
    difference: 0.000857204286916588
    difference_formatted: 0.1%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.01603022950192164
    value_formatted: -1.6%
  - alert: 1.0
    bench: -0.023841014331515586
    bench_formatted: -2.4%
    difference: 0.0012354660936684525
    difference_formatted: 0.1%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.022605548237847134
    value_formatted: -2.3%
  - alert: -1.0
    bench: 5.750034743344741
    bench_formatted: '5.75'
    difference: -6.841368328885916
    difference_formatted: '-6.84'
    name: Romad
    stat_id: romad
    units: ''
    value: -1.091333585541175
    value_formatted: '-1.09'
  - alert: 0.0
    bench: 62
    bench_formatted: '62.00'
    difference: 0.0
    difference_formatted: '0.00'
    name: Num Days
    stat_id: num_days
    units: ''
    value: 62
    value_formatted: '62.00'
  - alert: 1.0
    bench: 0.7163995884180333
    bench_formatted: 71.6%
    difference: -0.7163995884180333
    difference_formatted: -71.6%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 0.0
    value_formatted: 0.0%
user_id: b4ff491f-948e-435e-8765-55d9e59f6d05
---
