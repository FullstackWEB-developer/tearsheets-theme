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
    - name: Pacer Trendpilot US Mid Cap ETF
      ticker: PTMC
      weight: 0.5344914031806653
    - name: Direxion Daily S&P Biotech Bull 3X Shares
      ticker: LABU
      weight: 0.05647193180610416
    - name: Direxion Daily Pharmaceutical & Medical Bull 3X Shares
      ticker: PILL
      weight: 0.12845509273723232
    - name: Invesco WilderHill Clean Energy ETF
      ticker: PBW
      weight: 0.13840760011144135
    - name: Alpha Architect U.S. Quantitative Momentum ETF
      ticker: QMOM
      weight: 0.14217397216455693
    replacement_score:
      completeness: 53.711546585335945
      confidence: 0.0
      score: 58.587311833642055
      simplicity: 83.22783341121297
      stability: 97.40986733801931
      vintage: '2021-04-01'
  levels:
  - all
  max_depth: 0
  name: PTMC + LABU + PILL + PBW + QMOM
  replacement_score:
    completeness: 53.711546585335945
    confidence: 0.0
    score: 58.587311833642055
    simplicity: 83.22783341121297
    stability: 97.40986733801931
    vintage: '2021-04-01'
  start_date: '2021-06-21'
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
    cluster_max: 256
    has_min_completeness: 581
    is_portformer: false
    qualified_strategies: 369
    strategy_limit: 0
    total_strategies: 778
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
  - alert: 1.0
    bench: 0.3097770834672673
    bench_formatted: 31.0%
    difference: 0.1606043856867203
    difference_formatted: 16.1%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 0.4703814691539876
    value_formatted: 47.0%
  - alert: 1.0
    bench: 0.1818184445650015
    bench_formatted: 18.2%
    difference: 0.08772379687347276
    difference_formatted: 8.8%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.2695422414384743
    value_formatted: 27.0%
  - alert: 1.0
    bench: 0.24320393721913777
    bench_formatted: 24.3%
    difference: -0.05013670180339669
    difference_formatted: -5.0%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.19306723541574108
    value_formatted: 19.3%
  - alert: 1.0
    bench: 1.231357292776354
    bench_formatted: '1.23'
    difference: 0.8632527233091103
    difference_formatted: '0.86'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 2.0946100160854644
    value_formatted: '2.09'
  - alert: 1.0
    bench: 1.5430029202990245
    bench_formatted: '1.54'
    difference: 3.27183531417213
    difference_formatted: '3.27'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 4.814838234471154
    value_formatted: '4.81'
  - alert: 1.0
    bench: 0.008671377411943623
    bench_formatted: '0.01'
    difference: 0.5684552202723671
    difference_formatted: '0.57'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.5771265976843106
    value_formatted: '0.58'
  - alert: 1.0
    bench: -0.2007624738696116
    bench_formatted: -20.1%
    difference: 0.1030683362376642
    difference_formatted: 10.3%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.0976941376319474
    value_formatted: -9.8%
  - alert: 1.0
    bench: 1.2229285118520965
    bench_formatted: '1.22'
    difference: 0.18574671591397784
    difference_formatted: '0.19'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.4086752277660743
    value_formatted: '1.41'
  - alert: 1.0
    bench: 1.7515788382814168
    bench_formatted: '1.75'
    difference: 1.2847489521323017
    difference_formatted: '1.28'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 3.0363277904137185
    value_formatted: '3.04'
  - alert: -1.0
    bench: -0.3700012224247149
    bench_formatted: '-0.37'
    difference: -0.23427354859733185
    difference_formatted: '-0.23'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.6042747710220467
    value_formatted: '-0.60'
  - alert: 1.0
    bench: 0.2199781411010342
    bench_formatted: '0.22'
    difference: 1.0178062811465818
    difference_formatted: '1.02'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 1.237784422247616
    value_formatted: '1.24'
  - alert: 1.0
    bench: 0.8930750792781859
    bench_formatted: '0.89'
    difference: 0.14648919841488994
    difference_formatted: '0.15'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.0395642776930758
    value_formatted: '1.04'
  - alert: 1.0
    bench: -0.028471974935429023
    bench_formatted: -2.8%
    difference: 0.009851948466383598
    difference_formatted: 1.0%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.018620026469045425
    value_formatted: -1.9%
  - alert: 1.0
    bench: -0.034603167474960145
    bench_formatted: -3.5%
    difference: 0.007135155800284537
    difference_formatted: 0.7%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.027468011674675608
    value_formatted: -2.7%
  - alert: 1.0
    bench: 1.5430029202990245
    bench_formatted: '1.54'
    difference: 3.27183531417213
    difference_formatted: '3.27'
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
    bench: 0.5038150398491439
    bench_formatted: 50.4%
    difference: 0.15228319830827464
    difference_formatted: 15.2%
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
  - alert: 1.0
    bench: 0.5121858589179338
    bench_formatted: 51.2%
    difference: 0.5302895997490427
    difference_formatted: 53.0%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 1.0424754586669764
    value_formatted: 104.2%
  - alert: 1.0
    bench: 0.1667977425650009
    bench_formatted: 16.7%
    difference: 0.13845143143031335
    difference_formatted: 13.8%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.30524917399531426
    value_formatted: 30.5%
  - alert: 1.0
    bench: 0.27395743075869233
    bench_formatted: 27.4%
    difference: -0.06587666637636605
    difference_formatted: -6.6%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.20808076438232628
    value_formatted: 20.8%
  - alert: 1.0
    bench: 1.646870249222171
    bench_formatted: '1.65'
    difference: 1.8934668218550856
    difference_formatted: '1.89'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 3.5403370710772566
    value_formatted: '3.54'
  - alert: 1.0
    bench: 3.2309293819664124
    bench_formatted: '3.23'
    difference: 9.092166770230824
    difference_formatted: '9.09'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 12.323096152197236
    value_formatted: '12.32'
  - alert: 1.0
    bench: 0.39976647531836446
    bench_formatted: '0.40'
    difference: 0.48211612287048083
    difference_formatted: '0.48'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.8818825981888453
    value_formatted: '0.88'
  - alert: 1.0
    bench: -0.15852586001313546
    bench_formatted: -15.9%
    difference: 0.07393060523366993
    difference_formatted: 7.4%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.08459525477946553
    value_formatted: -8.5%
  - alert: 1.0
    bench: 1.299232295472835
    bench_formatted: '1.30'
    difference: 0.47403305102200477
    difference_formatted: '0.47'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.7732653464948398
    value_formatted: '1.77'
  - alert: 1.0
    bench: 2.3377203942599136
    bench_formatted: '2.34'
    difference: 3.017104317920815
    difference_formatted: '3.02'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 5.354824712180728
    value_formatted: '5.35'
  - alert: -1.0
    bench: -0.477988024342072
    bench_formatted: '-0.48'
    difference: -0.2648207903639982
    difference_formatted: '-0.26'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.7428088147060702
    value_formatted: '-0.74'
  - alert: 1.0
    bench: -0.056052565228172035
    bench_formatted: '-0.06'
    difference: 1.3698569588043608
    difference_formatted: '1.37'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 1.3138043935761887
    value_formatted: '1.31'
  - alert: 1.0
    bench: 0.8056175305566188
    bench_formatted: '0.81'
    difference: 0.34362503793514076
    difference_formatted: '0.34'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.1492425684917595
    value_formatted: '1.15'
  - alert: 1.0
    bench: -0.03329378996848707
    bench_formatted: -3.3%
    difference: 0.013844520462655555
    difference_formatted: 1.4%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.019449269505831517
    value_formatted: -1.9%
  - alert: 1.0
    bench: -0.036995975904616854
    bench_formatted: -3.7%
    difference: 0.007973456079681432
    difference_formatted: 0.8%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.029022519824935422
    value_formatted: -2.9%
  - alert: 1.0
    bench: 3.2309293819664124
    bench_formatted: '3.23'
    difference: 9.092166770230824
    difference_formatted: '9.09'
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
    bench: 0.45077108956781314
    bench_formatted: 45.1%
    difference: 0.6875757879087647
    difference_formatted: 68.8%
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
    bench: 0.05336560366176979
    bench_formatted: 5.3%
    difference: -0.1599824971699959
    difference_formatted: -16.0%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: -0.10661689350822612
    value_formatted: -10.7%
  - alert: -1.0
    bench: 0.012873441087553061
    bench_formatted: 1.3%
    difference: -0.04022985185435146
    difference_formatted: -4.0%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: -0.0273564107667984
    value_formatted: -2.7%
  - alert: 1.0
    bench: 0.18845646021283793
    bench_formatted: 18.8%
    difference: -0.024123829596954582
    difference_formatted: -2.4%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.16433263061588335
    value_formatted: 16.4%
  - alert: -1.0
    bench: 0.3686371061549505
    bench_formatted: '0.37'
    difference: -0.9733370657812043
    difference_formatted: '-0.97'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: -0.6046999596262538
    value_formatted: '-0.60'
  - alert: -1.0
    bench: 0.4982744186283804
    bench_formatted: '0.50'
    difference: -1.5896080041695555
    difference_formatted: '-1.59'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: -1.091333585541175
    value_formatted: '-1.09'
  - alert: 1.0
    bench: 0.016753781545656328
    bench_formatted: '0.02'
    difference: 0.13779930649052036
    difference_formatted: '0.14'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.15455308803617668
    value_formatted: '0.15'
  - alert: 1.0
    bench: -0.1071008297168283
    bench_formatted: -10.7%
    difference: 0.009406692084880972
    difference_formatted: 0.9%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.09769413763194733
    value_formatted: -9.8%
  - alert: -1.0
    bench: 1.0634985468018214
    bench_formatted: '1.06'
    difference: -0.158552936062606
    difference_formatted: '-0.16'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 0.9049456107392154
    value_formatted: '0.90'
  - alert: -1.0
    bench: 0.5316131452841972
    bench_formatted: '0.53'
    difference: -1.318723914486166
    difference_formatted: '-1.32'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: -0.7871107692019688
    value_formatted: '-0.79'
  - alert: -1.0
    bench: -0.047010861855427646
    bench_formatted: '-0.05'
    difference: -0.5031457578875389
    difference_formatted: '-0.50'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.5501566197429666
    value_formatted: '-0.55'
  - alert: 1.0
    bench: 0.11983602649960323
    bench_formatted: '0.12'
    difference: 0.882314049318548
    difference_formatted: '0.88'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 1.0021500758181512
    value_formatted: '1.00'
  - alert: 1.0
    bench: 0.8915575425501062
    bench_formatted: '0.89'
    difference: 0.15979290612979902
    difference_formatted: '0.16'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.0513504486799052
    value_formatted: '1.05'
  - alert: 1.0
    bench: -0.019964852389072276
    bench_formatted: -2.0%
    difference: 0.003934622887150636
    difference_formatted: 0.4%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.01603022950192164
    value_formatted: -1.6%
  - alert: 1.0
    bench: -0.024322483689369984
    bench_formatted: -2.4%
    difference: 0.0017169354515228497
    difference_formatted: 0.2%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.022605548237847134
    value_formatted: -2.3%
  - alert: -1.0
    bench: 0.4982744186283804
    bench_formatted: '0.50'
    difference: -1.5896080041695555
    difference_formatted: '-1.59'
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
    bench: 0.5909121698388967
    bench_formatted: 59.1%
    difference: -0.5909121698388967
    difference_formatted: -59.1%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 0.0
    value_formatted: 0.0%
user_id: 920fc9f2-4370-45e8-813e-53345d0ae6f2
---
