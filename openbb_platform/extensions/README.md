# 扩展模块

本文件夹包含由 OpenBB 创建或支持的扩展。

## 什么是扩展？

扩展为 OpenBB 平台添加功能，可以是新的数据源、新的命令、新的可视化等。

## 扩展类型

### 资产类别扩展

| 扩展 | 路径 | 功能 |
|------|------|------|
| openbb-equity | `equity/` | 股票数据（价格、基本面、期权等） |
| openbb-crypto | `crypto/` | 加密货币数据 |
| openbb-currency | `currency/` | 外汇数据 |
| openbb-etf | `etf/` | ETF 数据 |
| openbb-index | `index/` | 指数数据 |
| openbb-commodity | `commodity/` | 大宗商品数据 |
| openbb-fixedincome | `fixedincome/` | 固定收益数据 |
| openbb-derivatives | `derivatives/` | 衍生品数据（期货、期权） |

### 功能扩展

| 扩展 | 路径 | 功能 |
|------|------|------|
| openbb-economy | `economy/` | 宏观经济数据 |
| openbb-news | `news/` | 新闻数据 |
| openbb-regulators | `regulators/` | 监管机构数据 |
| openbb-quantitative | `quantitative/` | 量化分析工具 |
| openbb-technical | `technical/` | 技术分析指标 |
| openbb-econometrics | `econometrics/` | 计量经济学工具 |

### 服务扩展

| 扩展 | 路径 | 功能 |
|------|------|------|
| openbb-platform-api | `platform_api/` | 平台 API 服务 |
| openbb-mcp-server | `mcp_server/` | MCP 协议服务器 |

## 开发扩展

使用 Cookiecutter 模板快速开始：

```bash
cookiecutter https://github.com/OpenBB-finance/openbb-cookiecutter
```

更多详情见 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 从源码安装扩展

```bash
cd openbb_platform/extensions/<extension_name>
pip install -e .
```

安装后运行 `openbb-build` 重新构建包。

## 许可证

AGPL-3.0 License
