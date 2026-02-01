# Financial Modeling Prep 数据源

OpenBB 的 FMP 数据连接器。提供免费和付费的金融数据 API。

## 从源码安装

```bash
cd openbb_platform/providers/fmp
pip install -e .
```

## API 密钥

FMP 需要 API Key。免费版有请求限制，付费版提供更多数据。

配置方式：

```json
# ~/.openbb_platform/user_settings.json
{
  "credentials": {
    "fmp_api_key": "your_api_key"
  }
}
```

或在运行时设置：

```python
from openbb import obb
obb.user.credentials.fmp_api_key = "your_api_key"
```

## 数据覆盖

| 数据类型 | 免费版 | 付费版 |
|----------|--------|--------|
| 股票历史价格 | ✅ | ✅ |
| 财务报表 | 有限 | 完整 |
| 实时报价 | ✅ | ✅ |
| 加密货币 | ✅ | ✅ |
| 期权数据 | ❌ | ✅ |
| 高级指标 | ❌ | ✅ |

## 使用示例

```python
from openbb import obb

# 历史价格
obb.equity.price.historical("AAPL", provider="fmp")

# 财务报表
obb.equity.fundamental.balance("AAPL", provider="fmp")

# 公司新闻
obb.equity.fundamental.news("AAPL", provider="fmp")
```

## 获取 API Key

访问 [https://site.financialmodelingprep.com/developer](https://site.financialmodelingprep.com/developer) 注册获取。

## 许可证

AGPL-3.0 License
