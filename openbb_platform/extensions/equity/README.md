# OpenBB 股票扩展

提供股票数据访问的 OpenBB 扩展，包括价格、基本面、期权等数据。

## 从源码安装

```bash
cd openbb_platform/extensions/equity
pip install -e .
```

## 功能模块

| 模块 | 路径 | 功能 |
|------|------|------|
| price | `price/` | 股票价格数据（历史价格、实时报价） |
| fundamental | `fundamental/` | 基本面数据（财务报表、指标） |
| calendar | `calendar/` | 日历事件（分红、财报、拆股） |
| ownership | `ownership/` | 持股数据（机构持股、内幕交易） |
| options | `options/` | 期权数据 |
| shorts | `shorts/` | 做空数据 |

## 使用示例

```python
from openbb import obb

# 历史价格
obb.equity.price.historical("AAPL", provider="yfinance")

# 财务报表
obb.equity.fundamental.balance("AAPL", provider="fmp")

# 日历事件
obb.equity.calendar.earnings("AAPL")
```

## 支持的数据源

- Yahoo Finance (yfinance)
- Financial Modeling Prep (fmp)
- Polygon
- Intrinio

## 开发

添加新功能：
1. 在相应子目录创建 router
2. 实现命令函数
3. 添加测试
4. 运行 `openbb-build`

## 许可证

AGPL-3.0 License
