"""Akshare ETF Historical Price Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal
from warnings import warn

import pandas as pd
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.etf_historical import (
    EtfHistoricalData,
    EtfHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_akshare.utils.helpers import format_date, map_interval, normalize_symbol
from pydantic import Field, PrivateAttr

if TYPE_CHECKING:
    from pandas import DataFrame


class AkshareETFHistoricalQueryParams(EtfHistoricalQueryParams):
    """Akshare ETF Historical Price Query.

    Source: https://akshare.akfamily.xyz/
    """

    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
        "interval": {
            "choices": [
                "1d",
                "1W",
                "1M",
            ]
        },
    }

    interval: Literal[
        "1d",
        "1W",
        "1M",
    ] = Field(
        default="1d",
        description=QUERY_DESCRIPTIONS.get("interval", ""),
    )

    _period: str = PrivateAttr(default="max")


class AkshareETFHistoricalData(EtfHistoricalData):
    """Akshare ETF Historical Price Data."""

    pass


class AkshareETFHistoricalFetcher(
    Fetcher[
        AkshareETFHistoricalQueryParams,
        list[AkshareETFHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the Akshare endpoints."""

    require_credentials = False

    @staticmethod
    def transform_query(params: dict[str, Any]) -> AkshareETFHistoricalQueryParams:
        """Transform the query."""
        # pylint: disable=import-outside-toplevel
        from dateutil.relativedelta import relativedelta

        transformed_params = params.copy()
        now = datetime.now().date()

        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        # Normalize symbol
        if "symbol" in transformed_params:
            transformed_params["symbol"] = normalize_symbol(
                transformed_params["symbol"]
            )

        return AkshareETFHistoricalQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: AkshareETFHistoricalQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> "DataFrame":
        """Return the raw data from the Akshare endpoint."""
        # pylint: disable=import-outside-toplevel
        import akshare as ak
        from pandas import DataFrame

        symbol = query.symbol
        start_date = format_date(query.start_date)
        end_date = format_date(query.end_date)
        interval = map_interval(query.interval)

        # fund_etf_hist_sina: ETF历史行情数据（新浪）
        try:
            data = ak.fund_etf_hist_sina(
                symbol=symbol,
                period=interval,
                start_date=start_date,
                end_date=end_date,
            )
        except Exception as exc:
            raise EmptyDataError(f"Failed to fetch ETF data for {symbol}: {exc}") from exc

        if data.empty:
            raise EmptyDataError(f"No ETF data found for symbol: {symbol}")

        return DataFrame(data)

    @staticmethod
    def transform_data(
        query: AkshareETFHistoricalQueryParams,
        data: "DataFrame",
        **kwargs: Any,
    ) -> list[AkshareETFHistoricalData]:
        """Transform the data to the standard format."""
        # Rename columns to match OpenBB standard
        # Akshare fund_etf_hist_sina returns: date, open, high, low, close, volume
        column_mapping = {
            "date": "date",
            "open": "open",
            "high": "high",
            "low": "low",
            "close": "close",
            "volume": "volume",
        }

        # Handle if columns are named differently
        # Sometimes Akshare returns Chinese column names
        chinese_mapping = {
            "日期": "date",
            "开盘": "open",
            "最高": "high",
            "最低": "low",
            "收盘": "close",
            "成交量": "volume",
        }

        # Try to find the right column names
        data_columns = list(data.columns)
        used_columns = {}

        for eng_col, chi_col in chinese_mapping.items():
            if chi_col in data_columns:
                used_columns[chi_col] = column_mapping.get(eng_col, eng_col)
            elif eng_col in data_columns:
                used_columns[eng_col] = column_mapping.get(eng_col, eng_col)

        # Rename columns
        data = data.rename(columns=used_columns)

        # Ensure date column is properly formatted
        if "date" in data.columns:
            data["date"] = data["date"].apply(
                lambda x: datetime.strptime(str(x), "%Y-%m-%d").date()
                if isinstance(x, str)
                else x
            )

        # Convert numeric columns
        numeric_columns = ["open", "high", "low", "close", "volume"]
        for col in numeric_columns:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col], errors="coerce")

        # Handle multiple symbols
        query_symbols = query.symbol.upper().split(",")

        if len(query_symbols) > 1:
            symbols = data["symbol"].unique().tolist() if "symbol" in data.columns else []
            for symbol in query_symbols:
                if symbol not in symbols:
                    warn(f"ETF data for '{symbol}' was not found.")

        return [
            AkshareETFHistoricalData.model_validate(d)
            for d in data.to_dict("records")
        ]
