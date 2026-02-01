# Yahoo Finance 数据源

OpenBB 的 Yahoo Finance 数据连接器。免费的股票、ETF 和加密货币数据。

## 从源码安装

```bash
cd openbb_platform/providers/yfinance
pip install -e .
```

## 数据覆盖

| 数据类型 | 说明 |
|----------|------|
| 股票历史价格 | 日线、周线、月线 |
| 实时报价 | 延迟 15 分钟 |
| 基本面数据 | 财务报表（部分） |
| 加密货币 | BTC、ETH 等主流币种 |

## 使用示例

```python
from openbb import obb

# 不需要 API Key
obb.equity.price.historical("AAPL", provider="yfinance")

# 加密货币
obb.crypto.price.historical("BTC-USD", provider="yfinance")

# ETF
obb.etf.price.historical("SPY", provider="yfinance")
```

## 注意事项

- Yahoo Finance 数据免费但有限制
- 频繁请求可能导致 IP 被临时封禁
- 适合个人研究，不建议生产环境高频使用

## 许可证

AGPL-3.0 License
