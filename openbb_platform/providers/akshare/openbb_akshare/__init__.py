"""Akshare Provider module."""

from openbb_core.provider.abstract.provider import Provider

from openbb_akshare.models.equity_historical import AkshareEquityHistoricalFetcher
from openbb_akshare.models.equity_quote import AkshareEquityQuoteFetcher
from openbb_akshare.models.etf_historical import AkshareETFHistoricalFetcher

akshare_provider = Provider(
    name="akshare",
    website="https://akshare.akfamily.xyz/",
    description="Akshare - 中国金融市场数据源，提供A股、ETF、期货等数据",
    credentials=[],
    fetcher_dict={
        "EquityHistorical": AkshareEquityHistoricalFetcher,
        "EquityQuote": AkshareEquityQuoteFetcher,
        "ETFHistorical": AkshareETFHistoricalFetcher,
    },
)

__all__ = ["akshare_provider"]
