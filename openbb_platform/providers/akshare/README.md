# Akshare 数据源

OpenBB 的 Akshare 数据连接器。中国金融市场数据源，提供 A 股、ETF、期货等数据。

## 特点

- **免费无需认证**：Akshare 完全免费，无需 API 密钥
- **中国市场专注**：专注于中国 A 股、ETF、期货等市场数据
- **实时数据**：提供股票实时行情数据

## 数据覆盖

| 数据类型 | 说明 | OpenBB 接口 |
|----------|------|-------------|
| A 股历史行情 | 日线/周线/月线数据 | `obb.equity.price.historical` |
| A 股实时报价 | 实时行情数据 | `obb.equity.quote` |
| ETF 历史行情 | 场内基金历史净值 | `obb.etf.price.historical` |

## 安装

### 从源码安装

```bash
cd openbb_platform/providers/akshare
pip install -e .
```

## 使用示例

### A 股历史行情

```python
from openbb import obb

# 获取A股历史行情（浦发银行）
obb.equity.price.historical("600000", provider="akshare")

# 指定日期范围
obb.equity.price.historical(
    symbol="600000",
    start_date="2024-01-01",
    end_date="2024-12-31",
    provider="akshare"
)

# 周线数据
obb.equity.price.historical(
    symbol="600000",
    interval="1W",
    provider="akshare"
)

# 多股票查询
obb.equity.price.historical("600000,000001", provider="akshare")
```

### A 股实时报价

```python
from openbb import obb

# 获取实时报价
obb.equity.quote("600000", provider="akshare")

# 多股票查询
obb.equity.quote("600000,000001", provider="akshare")
```

### ETF 历史行情

```python
from openbb import obb

# 获取ETF历史行情（沪深300ETF）
obb.etf.price.historical("510300", provider="akshare")

# 宽基ETF（日线）
obb.etf.price.historical(
    symbol="510300",
    start_date="2024-01-01",
    end_date="2024-12-31",
    provider="akshare"
)
```

## 股票代码说明

Akshare 使用沪深交易所的标准股票代码：

- **上海证券交易所**：6 开头（如 `600000`）
- **深圳证券交易所**：0 开头（如 `000001`）
- **创业板**：3 开头（如 `300001`）
- **科创板**：6 开头（如 `688001`）

## 支持的交易所

- **SSE**：上海证券交易所
- **SZSE**：深圳证券交易所

## 注意事项

- Akshare 数据来源于东方财富等公开渠道
- 实时行情数据有 15 分钟延迟
- 历史数据覆盖范围取决于具体股票上市时间
- 部分股票可能因停牌等原因无数据

## 依赖

- `akshare>=1.11.0`
- `openbb-core`

## 许可证

AGPL-3.0 License
