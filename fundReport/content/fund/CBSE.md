---
as_of_date: '2021-06-29'
figures:
  drawdown:
    alt: Drawdowns of CBSE and Benchmark
    name: Drawdowns
    src: /img/CBSE-drawdown.png
  performance:
    alt: Total Returns of $10,000
    name: Performance
    src: /img/CBSE-performance.png
  qr_code:
    alt: Live Report
    name: CBSE Report QR CODE
    src: /img/CBSE-qr-code.png
  tracking_error:
    alt: CBSE vs Benchmark
    name: Tracking Error
    src: /img/CBSE-relative-performance.png
holdings:
  as_of_date: '2021-06-29'
  buckets:
  - id: '0'
    name: all
    positions:
    - name: Schwab U.S. Mid-Cap ETF
      ticker: SCHM
      weight: 0.20975453685257192
    - name: FlexShares Morningstar US Market Factors Tilt Index Fund
      ticker: TILT
      weight: 0.2111754640887241
    - name: Barron`s 400 ETF
      ticker: BFOR
      weight: 0.16784619356979663
    - name: Pacer WealthShield ETF
      ticker: PWS
      weight: 0.20613249730509775
    - name: Main Sector Rotation ETF
      ticker: SECT
      weight: 0.20509130818380966
    replacement_score:
      completeness: 95.07853051699361
      confidence: 0.0
      score: 70.58876761941463
      simplicity: 89.86667262264558
      stability: 97.40986733801931
      vintage: '2021-04-01'
  levels:
  - all
  max_depth: 0
  name: SCHM + TILT + BFOR + PWS + SECT
  replacement_score:
    completeness: 95.07853051699361
    confidence: 0.0
    score: 70.58876761941463
    simplicity: 89.86667262264558
    stability: 97.40986733801931
    vintage: '2021-04-01'
  start_date: '2021-06-24'
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
  name: Changebridge Capital Sustainable Equity ETF
  ticker: CBSE
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
    cluster_max: 32
    has_min_completeness: 729
    is_portformer: false
    qualified_strategies: 729
    strategy_limit: 0
    total_strategies: 1066
  vintage: '2021-04-01'
request_params:
  by_cluster: true
  fn: portformer_replication_report
  min_months: 12
  months: 0
  ticker: CBSE
  top_n: 5
  use_cash: false
  years: 1
statistics:
- bench_name: Benchmark
  end_period: '2021-06-29'
  name: all
  nav_name: CBSE
  num_dates: 156
  start_period: '2020-11-13'
  stats:
  - alert: 1.0
    bench: 0.4415461679020254
    bench_formatted: 44.2%
    difference: 0.4097962498183372
    difference_formatted: 41.0%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 0.8513424177203626
    value_formatted: 85.1%
  - alert: 1.0
    bench: 0.2540719077359985
    bench_formatted: 25.4%
    difference: 0.21008303116195748
    difference_formatted: 21.0%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.464154938897956
    value_formatted: 46.4%
  - alert: -1.0
    bench: 0.1471414916662691
    bench_formatted: 14.7%
    difference: 0.05600184055328056
    difference_formatted: 5.6%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.20314333221954967
    value_formatted: 20.3%
  - alert: 1.0
    bench: 2.560414903183963
    bench_formatted: '2.56'
    difference: 0.5764447975067921
    difference_formatted: '0.58'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 3.136859700690755
    value_formatted: '3.14'
  - alert: -1.0
    bench: 9.67618967085657
    bench_formatted: '9.68'
    difference: -1.242753115953363
    difference_formatted: '-1.24'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 8.433436554903206
    value_formatted: '8.43'
  - alert: -1.0
    bench: 0.9155847959337508
    bench_formatted: '0.92'
    difference: -0.16096150812870025
    difference_formatted: '-0.16'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.7546232878050505
    value_formatted: '0.75'
  - alert: -1.0
    bench: -0.045632235716906756
    bench_formatted: -4.6%
    difference: -0.05531622250388717
    difference_formatted: -5.5%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.10094845822079393
    value_formatted: -10.1%
  - alert: 1.0
    bench: 1.5263787904719832
    bench_formatted: '1.53'
    difference: 0.12609139825801652
    difference_formatted: '0.13'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.6524701887299997
    value_formatted: '1.65'
  - alert: 1.0
    bench: 3.949425571310135
    bench_formatted: '3.95'
    difference: 0.7552537018546515
    difference_formatted: '0.76'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 4.704679273164786
    value_formatted: '4.70'
  - alert: -1.0
    bench: -0.3063386449193139
    bench_formatted: '-0.31'
    difference: -0.34317167983088087
    difference_formatted: '-0.34'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.6495103247501948
    value_formatted: '-0.65'
  - alert: 1.0
    bench: 0.5515099627564686
    bench_formatted: '0.55'
    difference: 0.23487074789765128
    difference_formatted: '0.23'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 0.7863807106541199
    value_formatted: '0.79'
  - alert: -1.0
    bench: 1.1708935943995953
    bench_formatted: '1.17'
    difference: -0.10849745861767746
    difference_formatted: '-0.11'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.0623961357819178
    value_formatted: '1.06'
  - alert: -1.0
    bench: -0.013442936891209567
    bench_formatted: -1.3%
    difference: -0.004643138745009157
    difference_formatted: -0.5%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.018086075636218724
    value_formatted: -1.8%
  - alert: -1.0
    bench: -0.020314382202043818
    bench_formatted: -2.0%
    difference: -0.008700620764134692
    difference_formatted: -0.9%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.02901500296617851
    value_formatted: -2.9%
  - alert: -1.0
    bench: 9.67618967085657
    bench_formatted: '9.68'
    difference: -1.242753115953363
    difference_formatted: '-1.24'
    name: Romad
    stat_id: romad
    units: ''
    value: 8.433436554903206
    value_formatted: '8.43'
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
    bench: 0.1477409498617114
    bench_formatted: 14.8%
    difference: 0.4646878555588496
    difference_formatted: 46.5%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 0.612428805420561
    value_formatted: 61.2%
- bench_name: Benchmark
  end_period: '2021-03-31'
  name: in sample
  nav_name: CBSE
  num_dates: 94
  start_period: '2020-11-13'
  stats:
  - alert: 1.0
    bench: 0.5802798298403029
    bench_formatted: 58.0%
    difference: 0.9274467419135706
    difference_formatted: 92.7%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 1.5077265717538735
    value_formatted: 150.8%
  - alert: 1.0
    bench: 0.18612629928499924
    bench_formatted: 18.6%
    difference: 0.22296082198282363
    difference_formatted: 22.3%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.4090871212678229
    value_formatted: 40.9%
  - alert: -1.0
    bench: 0.1606194358048179
    bench_formatted: 16.1%
    difference: 0.05515912368003356
    difference_formatted: 5.5%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.21577855948485147
    value_formatted: 21.6%
  - alert: 1.0
    bench: 2.9310779449768867
    bench_formatted: '2.93'
    difference: 1.4445645975957064
    difference_formatted: '1.44'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 4.375642542572593
    value_formatted: '4.38'
  - alert: 1.0
    bench: 12.716445309413343
    bench_formatted: '12.72'
    difference: 9.413114142036763
    difference_formatted: '9.41'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 22.129559451450106
    value_formatted: '22.13'
  - alert: 1.0
    bench: 0.8923801109983068
    bench_formatted: '0.89'
    difference: 0.02617369312408946
    difference_formatted: '0.03'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.9185538041223963
    value_formatted: '0.92'
  - alert: -1.0
    bench: -0.045632235716906756
    bench_formatted: -4.6%
    difference: -0.022499557645797315
    difference_formatted: -2.2%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.06813179336270407
    value_formatted: -6.8%
  - alert: 1.0
    bench: 1.6201736031529996
    bench_formatted: '1.62'
    difference: 0.3790559000207485
    difference_formatted: '0.38'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.9992295031737481
    value_formatted: '2.00'
  - alert: 1.0
    bench: 4.579214313292811
    bench_formatted: '4.58'
    difference: 2.1988318681328005
    difference_formatted: '2.20'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 6.778046181425611
    value_formatted: '6.78'
  - alert: -1.0
    bench: -0.3549643396766681
    bench_formatted: '-0.35'
    difference: -0.422794225518796
    difference_formatted: '-0.42'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.777758565195464
    value_formatted: '-0.78'
  - alert: 1.0
    bench: 0.3702234842511922
    bench_formatted: '0.37'
    difference: 0.5576782444991739
    difference_formatted: '0.56'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 0.9279017287503661
    value_formatted: '0.93'
  - alert: 1.0
    bench: 1.0652444211901593
    bench_formatted: '1.07'
    difference: 0.04303273233862104
    difference_formatted: '0.04'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.1082771535287803
    value_formatted: '1.11'
  - alert: -1.0
    bench: -0.015759222433677132
    bench_formatted: -1.6%
    difference: -0.002772124804318807
    difference_formatted: -0.3%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.01853134723799594
    value_formatted: -1.9%
  - alert: -1.0
    bench: -0.02181095188869342
    bench_formatted: -2.2%
    difference: -0.008381733297503403
    difference_formatted: -0.8%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.030192685186196822
    value_formatted: -3.0%
  - alert: 1.0
    bench: 12.716445309413343
    bench_formatted: '12.72'
    difference: 9.413114142036763
    difference_formatted: '9.41'
    name: Romad
    stat_id: romad
    units: ''
    value: 22.129559451450106
    value_formatted: '22.13'
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
    bench: 0.07850150068611039
    bench_formatted: 7.9%
    difference: 1.0094832147377888
    difference_formatted: 100.9%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 1.0879847154238993
    value_formatted: 108.8%
- bench_name: Benchmark
  end_period: '2021-06-29'
  name: out sample
  nav_name: CBSE
  num_dates: 62
  start_period: '2021-04-01'
  stats:
  - alert: -1.0
    bench: 0.2540843790817229
    bench_formatted: 25.4%
    difference: -0.08547085960642264
    difference_formatted: -8.5%
    name: Returns
    stat_id: annualized_returns
    units: annualized
    value: 0.16861351947530023
    value_formatted: 16.9%
  - alert: -1.0
    bench: 0.0572836202114031
    bench_formatted: 5.7%
    difference: -0.018203128452606077
    difference_formatted: -1.8%
    name: Returns
    stat_id: cumulative_returns
    units: cumulative
    value: 0.03908049175879702
    value_formatted: 3.9%
  - alert: -1.0
    bench: 0.12468154801128367
    bench_formatted: 12.5%
    difference: 0.05538583623254881
    difference_formatted: 5.5%
    name: Volatility
    stat_id: annualized_volatility
    units: annualized
    value: 0.18006738424383248
    value_formatted: 18.0%
  - alert: -1.0
    bench: 1.8780580883955746
    bench_formatted: '1.88'
    difference: -0.9235545494486006
    difference_formatted: '-0.92'
    name: Sharpe Ratio
    stat_id: sharpe_ratio
    units: ''
    value: 0.954503538946974
    value_formatted: '0.95'
  - alert: -1.0
    bench: 5.979082992546647
    bench_formatted: '5.98'
    difference: -4.308789830599491
    difference_formatted: '-4.31'
    name: Calmar Ratio
    stat_id: calmar_ratio
    units: ''
    value: 1.670293161947155
    value_formatted: '1.67'
  - alert: -1.0
    bench: 0.5600035870779315
    bench_formatted: '0.56'
    difference: -0.498770956211453
    difference_formatted: '-0.50'
    name: Stability
    stat_id: stability
    units: ''
    value: 0.06123263086647853
    value_formatted: '0.06'
  - alert: -1.0
    bench: -0.04249554311228949
    bench_formatted: -4.2%
    difference: -0.058452915108504484
    difference_formatted: -5.8%
    name: Max Drawdown
    stat_id: max_drawdown
    units: ''
    value: -0.10094845822079397
    value_formatted: -10.1%
  - alert: -1.0
    bench: 1.3602827097072248
    bench_formatted: '1.36'
    difference: -0.19256369814292285
    difference_formatted: '-0.19'
    name: Omega Ratio
    stat_id: omega_ratio
    units: ''
    value: 1.167719011564302
    value_formatted: '1.17'
  - alert: -1.0
    bench: 2.8249806840124814
    bench_formatted: '2.82'
    difference: -1.4966135513234058
    difference_formatted: '-1.50'
    name: Sortino Ratio
    stat_id: sortino_ratio
    units: ''
    value: 1.3283671326890756
    value_formatted: '1.33'
  - alert: -1.0
    bench: -0.2709957125700204
    bench_formatted: '-0.27'
    difference: -0.2803814408806684
    difference_formatted: '-0.28'
    name: Skew
    stat_id: skew
    units: ''
    value: -0.5513771534506888
    value_formatted: '-0.55'
  - alert: 1.0
    bench: 0.5241086791290739
    bench_formatted: '0.52'
    difference: 0.004772217319421568
    difference_formatted: '0.00'
    name: Kurtosis
    stat_id: kurtosis
    units: ''
    value: 0.5288808964484955
    value_formatted: '0.53'
  - alert: -1.0
    bench: 1.2508213407732398
    bench_formatted: '1.25'
    difference: -0.08080301656193334
    difference_formatted: '-0.08'
    name: Tail Ratio
    stat_id: tail_ratio
    units: ''
    value: 1.1700183242113065
    value_formatted: '1.17'
  - alert: -1.0
    bench: -0.010841231535719587
    bench_formatted: -1.1%
    difference: -0.005538220864264792
    difference_formatted: -0.6%
    name: Daily Var
    stat_id: daily_var
    units: ''
    value: -0.016379452399984378
    value_formatted: -1.6%
  - alert: -1.0
    bench: -0.015226247461533643
    bench_formatted: -1.5%
    difference: -0.009077438693935125
    difference_formatted: -0.9%
    name: Daily Cvar
    stat_id: daily_cvar
    units: ''
    value: -0.024303686155468768
    value_formatted: -2.4%
  - alert: -1.0
    bench: 5.979082992546647
    bench_formatted: '5.98'
    difference: -4.308789830599491
    difference_formatted: '-4.31'
    name: Romad
    stat_id: romad
    units: ''
    value: 1.670293161947155
    value_formatted: '1.67'
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
    bench: 0.24170821890386732
    bench_formatted: 24.2%
    difference: -0.24170821890386732
    difference_formatted: -24.2%
    name: Turnover
    stat_id: turnover
    units: pct
    value: 0.0
    value_formatted: 0.0%
user_id: 48cd16a9-cff9-4710-904b-cb101fe12b1c
---
