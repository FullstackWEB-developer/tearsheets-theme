# pylint: disable=E0611
import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import BaseModel


class ReportFigureSpec(BaseModel):
    name: str
    figsize: Optional[List]
    stacked: Optional[bool]
    format: str = "png"
    kwargs: Optional[Dict[str, Any]]


class ReportFigure(BaseModel):  # https://www.w3schools.com/tags/tag_img.asp
    name: str
    alt: Optional[str]  # 	text	Specifies an alternate text for an image
    crossorigin: Optional[str]  # 	anonymous or use-credentials
    height: Optional[int]  # 	pixels	Specifies the height of an image
    ismap: Optional[str]  # 	ismap	Specifies an image as a server-side image map
    loading: Optional[str]  # 	eager, lazy
    longdesc: Optional[
        str
    ]  # 	URL	Specifies a URL to a detailed description of an image
    referrerpolicy: Optional[
        str
    ]  # no-referrer, no-referrer-when-downgrade, origin, origin-when-cross-origin, unsafe-url
    sizes: Optional[str]  # sizes	Specifies image sizes for different page layouts
    src: Optional[str]  # 	URL	Specifies the path to the image
    srcset: Optional[
        List[str]
    ]  # 	Specifies a list of image files to use in different situations
    usemap: Optional[Any]  # mapname	Specifies an image as a client-side image map
    width: Optional[int]  # pixels	Specifies the width of an image


class BenchmarkReportRequest(BaseModel):
    fn: str
    params: Optional[Dict[str, Any]]
    ticker: str
    nav: Optional[Dict[str, float]]
    os_date: Optional[str]
    use_cash: bool = False
    top_n: int = 5
    by_cluster: bool = True
    custom_score_weights: Optional[Dict[str, float]]
    years: int = 1
    months: int = 0
    min_months = 12


class ReportColors(BaseModel):
    primary: str = "#125470"
    secondary: str = "red"
    accent: str = "red"
    warn: str = "red"


class BenchmarkReportMeta(BaseModel):
    ticker: str
    name: str
    description: Optional[str]
    logo: Optional[str]
    colors: Optional[ReportColors]


class ReportHoldings(BaseModel):
    as_of_date: str


class PeriodRange(BaseModel):
    name: Optional[str]
    start_period: Optional[Union[str, datetime.datetime]]
    end_period: Optional[Union[str, datetime.datetime]]


class ReplicationStats(BaseModel):
    total_strategies: int
    has_min_completeness: int
    cluster_max: int
    cluster_limit: int
    strategy_limit: int
    qualified_strategies: int
    is_portformer: bool = False


class ReplicationDetails(BaseModel):
    vintage: str
    in_sample: PeriodRange
    out_sample: PeriodRange
    scoring_stats: ReplicationStats


class PerformanceStatistic(BaseModel):
    name: str
    units: Optional[str]
    values: Optional[Any]
    values_formatted: Optional[str]
    difference: Optional[Any]
    difference_formatted: Optional[str]
    alert: Optional[str]


class PerformanceStatistics(BaseModel):
    name: Optional[str]
    start_period: Union[str, datetime.datetime]
    end_period: Union[str, datetime.datetime]
    num_dates: int
    stats: List[PerformanceStatistic]


class PortfolioWeights(BaseModel):
    ticker: str
    name: Optional[str]
    figi: Optional[str]
    exchange: Optional[str]
    weight: float


class PortformerReplacementScore(BaseModel):
    vintage: str
    score: float
    completeness: float
    stability: float
    simplicity: float
    confidence: float


class SingleBucketOfHoldings(BaseModel):
    id: Union[str, int]
    name: Optional[str]
    positions: List[PortfolioWeights]
    replacement_score: Optional[PortformerReplacementScore]


class BucketsOfHoldings(BaseModel):
    id: Union[str, int]
    name: Optional[str]
    buckets: List[SingleBucketOfHoldings]
    replacement_score: Optional[PortformerReplacementScore]


class ParentOfBucketsOfHoldings(BaseModel):
    id: Union[str, int]
    name: Optional[str]
    buckets: List[Union[SingleBucketOfHoldings, BucketsOfHoldings]]
    replacement_score: Optional[PortformerReplacementScore]


class BucketedReportHoldings(BaseModel):
    as_of_date: Union[str, datetime.datetime]
    start_date: Optional[Union[str, datetime.datetime]]
    levels: List[str]
    max_depth: int
    buckets: List[
        Union[SingleBucketOfHoldings, BucketsOfHoldings, ParentOfBucketsOfHoldings]
    ]
    replacement_score: Optional[PortformerReplacementScore]


class BaseReportResponse(BaseModel):
    strategy_id: str
    user_id: str
    as_of_date: str
    meta: BenchmarkReportMeta
    kpis: Optional[List[str]]
    periods: Optional[List[PeriodRange]]
    statistics: Optional[List[PerformanceStatistics]]
    figures: Optional[Dict[str, ReportFigure]]


class BenchmarkReportResponse(BaseReportResponse):
    request_params: Optional[BenchmarkReportRequest]
    holdings: BucketedReportHoldings
    replication: ReplicationDetails


class BacktestReportResponse(BaseReportResponse):
    holdings: Optional[BucketedReportHoldings]
    avg_holdings: Optional[BucketedReportHoldings]
    series: Optional[Dict[str, Dict[str, float]]]

