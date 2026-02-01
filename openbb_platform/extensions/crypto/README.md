# OpenBB 加密货币扩展

提供加密货币数据访问的 OpenBB 扩展。

## 从源码安装

```bash
cd openbb_platform/extensions/crypto
pip install -e .
```

## 功能

| 模块 | 路径 | 功能 |
|------|------|------|
| price | `price/` | 加密货币价格数据 |

## 使用示例

```python
from openbb import obb

# 加密货币历史价格
obb.crypto.price.historical("BTC-USD", provider="yfinance")

# 或使用 FMP
obb.crypto.price.historical("BTCUSD", provider="fmp")
```

## 支持的数据源

- Yahoo Finance (yfinance)
- FMP
- Binance (通过 ccxt)

## 许可证

AGPL-3.0 License
