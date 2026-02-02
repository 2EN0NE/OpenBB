"""Akshare models."""

from openbb_akshare.models.equity_historical import (
    AkshareEquityHistoricalData,
    AkshareEquityHistoricalFetcher,
    AkshareEquityHistoricalQueryParams,
)
from openbb_akshare.models.equity_quote import (
    AkshareEquityQuoteData,
    AkshareEquityQuoteFetcher,
    AkshareEquityQuoteQueryParams,
)
from openbb_akshare.models.etf_historical import (
    AkshareETFHistoricalData,
    AkshareETFHistoricalFetcher,
    AkshareETFHistoricalQueryParams,
)

__all__ = [
    "AkshareEquityHistoricalData",
    "AkshareEquityHistoricalFetcher",
    "AkshareEquityHistoricalQueryParams",
    "AkshareEquityQuoteData",
    "AkshareEquityQuoteFetcher",
    "AkshareEquityQuoteQueryParams",
    "AkshareETFHistoricalData",
    "AkshareETFHistoricalFetcher",
    "AkshareETFHistoricalQueryParams",
]
