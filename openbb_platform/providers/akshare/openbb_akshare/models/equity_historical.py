"""Akshare Equity Historical Price Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_historical import (
    EquityHistoricalData,
    EquityHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_akshare.utils.helpers import format_date, map_interval, normalize_symbol
from pydantic import Field, PrivateAttr

if TYPE_CHECKING:
    from pandas import DataFrame


class AkshareEquityHistoricalQueryParams(EquityHistoricalQueryParams):
    """Akshare Equity Historical Price Query.

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
    adjustment: Literal["splits_only", "splits_and_dividends"] = Field(
        default="splits_only",
        description="The adjustment factor to apply.",
    )

    _period: str = PrivateAttr(default="max")


class AkshareEquityHistoricalData(EquityHistoricalData):
    """Akshare Equity Historical Price Data."""

    pass


class AkshareEquityHistoricalFetcher(
    Fetcher[
        AkshareEquityHistoricalQueryParams,
        list[AkshareEquityHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the Akshare endpoints."""

    require_credentials = False

    @staticmethod
    def transform_query(params: dict[str, Any]) -> AkshareEquityHistoricalQueryParams:
        """Transform the query."""
        # pylint: disable=import-outside-toplevel
        from dateutil.relativedelta import relativedelta

        transformed_params = params.copy()
        now = datetime.now().date()

        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        # Normalize symbol - remove exchange suffix if present
        if "symbol" in transformed_params:
            transformed_params["symbol"] = normalize_symbol(transformed_params["symbol"])

        return AkshareEquityHistoricalQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: AkshareEquityHistoricalQueryParams,
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

        # Map OpenBB adjustment parameter to Akshare format
        # Akshare expects: "" (no adjustment), "qfq" (forward adjustment), "hfq" (backward adjustment)
        adjustment_map = {
            "splits_only": "",
            "splits_and_dividends": "qfq",
        }
        adjust = adjustment_map.get(query.adjustment, "")

        # Fetch data from Akshare
        # stock_zh_a_hist: A股历史行情
        try:
            data = ak.stock_zh_a_hist(
                symbol=symbol,
                period=interval,
                start_date=start_date,
                end_date=end_date,
                adjust=adjust,
            )
        except Exception as exc:
            raise EmptyDataError(f"Failed to fetch data for {symbol}: {exc}") from exc

        if data.empty:
            raise EmptyDataError(f"No data found for symbol: {symbol}")

        return DataFrame(data)

    @staticmethod
    def transform_data(
        query: AkshareEquityHistoricalQueryParams,
        data: "DataFrame",
        **kwargs: Any,
    ) -> list[AkshareEquityHistoricalData]:
        """Transform the data to the standard format."""
        # Rename columns to match OpenBB standard
        column_mapping = {
            "日期": "date",
            "开盘": "open",
            "收盘": "close",
            "最高": "high",
            "最低": "low",
            "成交量": "volume",
            "成交额": "turnover",  # Additional field
            "振幅": "amplitude",  # Additional field
            "涨跌幅": "change_percent",  # Additional field
            "涨跌额": "change",  # Additional field
            "换手率": "turnover_rate",  # Additional field
        }

        # Rename columns
        data = data.rename(columns=column_mapping)

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
                data[col] = data[col].astype(float)

        # Handle multiple symbols
        query_symbols = query.symbol.upper().split(",")

        if len(query_symbols) > 1:
            symbols = data["symbol"].unique().tolist() if "symbol" in data.columns else []
            for symbol in query_symbols:
                if symbol not in symbols:
                    warn(f"Data for '{symbol}' was not found.")

        return [
            AkshareEquityHistoricalData.model_validate(d)
            for d in data.to_dict("records")
        ]
