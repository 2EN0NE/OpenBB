"""Akshare helper functions."""

from datetime import date, datetime
from typing import Any


def normalize_symbol(symbol: str) -> str:
    """Normalize stock symbol for Akshare.

    Akshare uses stock codes directly without exchange suffix for most APIs.
    Shanghai stocks: 6-digit code (e.g., 600000)
    Shenzhen stocks: 6-digit code (e.g., 000001)

    For ETFs, we may need to handle differently.
    """
    return symbol.upper().strip()


def parse_akshare_date(date_str: str | datetime | date) -> date:
    """Parse Akshare date format to Python date.

    Akshare typically returns dates as 'YYYY-MM-DD' strings.
    """
    if isinstance(date_str, (datetime, date)):
        return date_str if isinstance(date_str, date) else date_str.date()
    return datetime.strptime(str(date_str), "%Y-%m-%d").date()


def format_date(date_obj: date | datetime | None) -> str | None:
    """Format date to Akshare expected format."""
    if date_obj is None:
        return None
    if isinstance(date_obj, datetime):
        return date_obj.strftime("%Y%m%d")
    return date_obj.strftime("%Y%m%d")


def map_interval(interval: str) -> str:
    """Map OpenBB interval to Akshare interval.

    OpenBB: 1d, 1W, 1M, etc.
    Akshare: daily, weekly, monthly
    """
    interval_map = {
        "1d": "daily",
        "1W": "weekly",
        "1M": "monthly",
        "5d": "weekly",  # Approximate
    }
    return interval_map.get(interval, "daily")


def clean_float(value: Any) -> float | None:
    """Clean and convert value to float."""
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def clean_int(value: Any) -> int | None:
    """Clean and convert value to int."""
    if value is None:
        return None
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return None
