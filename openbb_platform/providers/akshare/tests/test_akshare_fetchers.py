"""Tests for Akshare fetchers."""

from datetime import date

import pytest
from openbb_akshare.models.equity_historical import AkshareEquityHistoricalFetcher
from openbb_akshare.models.equity_quote import AkshareEquityQuoteFetcher
from openbb_akshare.models.etf_historical import AkshareETFHistoricalFetcher

test_credentials = {}


def scrub_string(key, value):
    """Scrub a string from the response."""

    def before_record_response(response):
        if key in response["headers"]:
            response["headers"][key] = value
        return response

    return before_record_response


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "allow_playback_repeats": True,
        "match_on": ["method", "uri"],
        "filter_headers": [
            ("User-Agent", None),
        ],
        "filter_query_parameters": [
            ("start_date", "MOCK_START_DATE"),
            ("end_date", "MOCK_END_DATE"),
        ],
        "before_record_response": [
            scrub_string("set-cookie", "MOCK_COOKIE"),
        ],
        "decode_compressed_response": True,
    }


@pytest.mark.record_curl
def test_akshare_equity_historical_fetcher(credentials=test_credentials):
    """Test AkshareEquityHistoricalFetcher."""
    params = {
        "symbol": "600000",
        "start_date": date(2024, 1, 1),
        "end_date": date(2024, 1, 10),
        "interval": "1d",
    }

    fetcher = AkshareEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_curl
def test_akshare_equity_quote_fetcher(credentials=test_credentials):
    """Test AkshareEquityQuoteFetcher."""
    params = {
        "symbol": "600000",
    }

    fetcher = AkshareEquityQuoteFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_curl
def test_akshare_etf_historical_fetcher(credentials=test_credentials):
    """Test AkshareETFHistoricalFetcher."""
    params = {
        "symbol": "510300",
        "start_date": date(2024, 1, 1),
        "end_date": date(2024, 1, 10),
        "interval": "1d",
    }

    fetcher = AkshareETFHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_akshare_equity_historical_multiple_symbols(credentials=test_credentials):
    """Test AkshareEquityHistoricalFetcher with multiple symbols."""
    params = {
        "symbol": "600000,000001",
        "start_date": date(2024, 1, 1),
        "end_date": date(2024, 1, 10),
        "interval": "1d",
    }

    fetcher = AkshareEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_akshare_equity_historical_weekly_interval(credentials=test_credentials):
    """Test AkshareEquityHistoricalFetcher with weekly interval."""
    params = {
        "symbol": "600000",
        "start_date": date(2024, 1, 1),
        "end_date": date(2024, 3, 1),
        "interval": "1W",
    }

    fetcher = AkshareEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_akshare_equity_historical_monthly_interval(credentials=test_credentials):
    """Test AkshareEquityHistoricalFetcher with monthly interval."""
    params = {
        "symbol": "600000",
        "start_date": date(2023, 1, 1),
        "end_date": date(2024, 1, 1),
        "interval": "1M",
    }

    fetcher = AkshareEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
