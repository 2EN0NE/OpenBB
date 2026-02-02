"""Akshare Equity Quote Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import TYPE_CHECKING, Any

import pandas as pd
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_quote import (
    EquityQuoteData,
    EquityQuoteQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_akshare.utils.helpers import normalize_symbol
from pydantic import Field

if TYPE_CHECKING:
    from pandas import DataFrame


class AkshareEquityQuoteQueryParams(EquityQuoteQueryParams):
    """Akshare Equity Quote Query.

    Source: https://akshare.akfamily.xyz/
    """

    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
    }


class AkshareEquityQuoteData(EquityQuoteData):
    """Akshare Equity Quote Data."""

    turnover: float | None = Field(
        default=None, description="Turnover (成交额)."
    )
    amplitude: float | None = Field(
        default=None, description="Amplitude (振幅)."
    )
    turnover_rate: float | None = Field(
        default=None, description="Turnover rate (换手率)."
    )


class AkshareEquityQuoteFetcher(
    Fetcher[
        AkshareEquityQuoteQueryParams,
        list[AkshareEquityQuoteData],
    ]
):
    """Transform the query, extract and transform the data from the Akshare endpoints."""

    require_credentials = False

    @staticmethod
    def transform_query(params: dict[str, Any]) -> AkshareEquityQuoteQueryParams:
        """Transform the query."""
        transformed_params = params.copy()

        # Normalize symbol
        if "symbol" in transformed_params:
            transformed_params["symbol"] = normalize_symbol(
                transformed_params["symbol"]
            )

        return AkshareEquityQuoteQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: AkshareEquityQuoteQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> "DataFrame":
        """Return the raw data from the Akshare endpoint."""
        # pylint: disable=import-outside-toplevel
        import akshare as ak
        from pandas import DataFrame

        symbol = query.symbol

        # stock_zh_a_spot_em: A股实时行情数据（东方财富）
        try:
            data = ak.stock_zh_a_spot_em()
        except Exception as exc:
            raise EmptyDataError(f"Failed to fetch quote data: {exc}") from exc

        if data.empty:
            raise EmptyDataError("No quote data available")

        # Filter for the requested symbol(s)
        # Akshare returns all A-shares, we need to filter
        symbols = symbol.upper().split(",")
        data = data[data["代码"].isin(symbols)]

        if data.empty:
            raise EmptyDataError(f"No data found for symbol(s): {symbol}")

        return DataFrame(data)

    @staticmethod
    def transform_data(
        query: AkshareEquityQuoteQueryParams,
        data: "DataFrame",
        **kwargs: Any,
    ) -> list[AkshareEquityQuoteData]:
        """Transform the data to the standard format."""
        # Column mapping from Akshare (stock_zh_a_spot_em)
        # 东方财富的A股票实时行情数据列名
        column_mapping = {
            "代码": "symbol",
            "名称": "name",
            "最新价": "last_price",
            "涨跌幅": "change_percent",
            "涨跌额": "change",
            "成交量": "volume",
            "成交额": "turnover",
            "振幅": "amplitude",
            "最高": "high",
            "最低": "low",
            "今开": "open",
            "昨收": "prev_close",
            "换手率": "turnover_rate",
        }

        # Rename columns
        data = data.rename(columns=column_mapping)

        # Convert numeric columns
        numeric_columns = [
            "last_price",
            "change_percent",
            "change",
            "volume",
            "turnover",
            "amplitude",
            "high",
            "low",
            "open",
            "prev_close",
            "turnover_rate",
        ]

        for col in numeric_columns:
            if col in data.columns:
                # Handle '-' values as None
                data[col] = data[col].replace("-", None)
                data[col] = pd.to_numeric(data[col], errors="coerce")

        # Convert change_percent from percentage string to float
        # Akshare returns like "2.35%" or "-1.23%"
        if "change_percent" in data.columns:
            data["change_percent"] = data["change_percent"].apply(
                lambda x: float(str(x).replace("%", "")) if pd.notna(x) and x != "-" else None
            )

        # Add exchange info (Akshare returns Shanghai and Shenzhen)
        data["exchange"] = "SSE" if data["symbol"].str.startswith(("6", "5")) else "SZSE"

        return [
            AkshareEquityQuoteData.model_validate(d)
            for d in data.to_dict("records")
        ]
