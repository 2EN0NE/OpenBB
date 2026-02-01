# 数据源提供商

本文件夹包含由 OpenBB 创建或支持的数据源提供商。

## 什么是 Provider？

Provider 是数据获取的适配器，负责：
1. 对接外部数据 API
2. 将外部数据转换为标准格式
3. 处理认证和错误

## 推荐结构

每个提供商位于一个目录内，具有以下结构：

```
openbb_platform
└───providers
    └───<provider_name>
        │   README.md
        │   pyproject.toml
        │   poetry.lock
        |───tests
        └───openbb_<provider_name>
            │   __init__.py
            |───models
            │   |───<some model>.py
            │   └───...
            └───utils
                |───<some helper>.py
                └───...
```

模型定义了用于查询提供商端点和存储响应数据的数据结构。

## 主要提供商

### 免费数据源

| 提供商 | 目录 | 描述 |
|--------|------|------|
| Yahoo Finance | `yfinance/` | 免费股票数据 |
| FRED | `fred/` | 美联储经济数据 |
| SEC | `sec/` | 美国证监会数据 |
| FMP | `fmp/` | Financial Modeling Prep |
| Cboe | `cboe/` | 期权数据 |

### 需要 API Key

| 提供商 | 目录 | 描述 |
|--------|------|------|
| Polygon | `polygon/` | 股票和加密货币数据 |
| Benzinga | `benzinga/` | 财经新闻和数据 |
| Alpha Vantage | `alpha_vantage/` | 股票和外汇数据 |

## 从源码安装 Provider

```bash
cd openbb_platform/providers/<provider_name>
pip install -e .
```

## 开发新 Provider

详见 [CONTRIBUTING.md](../CONTRIBUTING.md)。

关键步骤：
1. 在 `providers/` 下创建新目录
2. 实现 `QueryParams` 和 `Data` 模型
3. 实现 `Fetcher` 类（遵循 TET 模式）
4. 在 `__init__.py` 中注册 Provider

## TET 模式

数据获取遵循 **Transform-Extract-Transform** 模式：

```python
class ExampleFetcher(Fetcher[QueryParams, List[Data]]):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> QueryParams:
        """转换查询参数"""
        pass
    
    @staticmethod
    def extract_data(query: QueryParams, credentials: Optional[Dict[str, str]], **kwargs) -> dict:
        """提取原始数据"""
        pass
    
    @staticmethod
    def transform_data(query: QueryParams, data: dict, **kwargs) -> List[Data]:
        """转换数据为标准格式"""
        pass
```

## 许可证

AGPL-3.0 License
