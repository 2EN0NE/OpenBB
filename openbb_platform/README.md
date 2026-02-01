# OpenBB 开放数据平台

[![Downloads](https://static.pepy.tech/badge/openbb)](https://pepy.tech/project/openbb)
[![LatestRelease](https://badge.fury.io/py/openbb.svg)](https://github.com/OpenBB-finance/OpenBB)

OpenBB 开放数据平台（ODP）是一个开源工具集，帮助数据工程师将专有、授权和公共数据源集成到下游应用程序中。

ODP 作为"一次连接，随处消费"的基础设施层，将数据暴露给多个消费端：Python 环境、OpenBB Workspace、MCP 服务器和 REST API。

## 概述

OpenBB 平台提供了一种便捷的方式来访问多个数据提供商的原始金融数据。该包附带了一个即用的 REST API - 允许来自任何语言的开发人员轻松地在 OpenBB 平台之上创建应用程序。

完整文档请访问 [docs.openbb.co](https://docs.openbb.co/platform)。

## 从源码安装

### 环境要求

- Python 3.10 - 3.13
- Poetry (`pip install poetry`)

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/OpenBB-finance/OpenBB.git
cd OpenBB/openbb_platform

# 开发安装（安装所有核心包、扩展和数据源）
python dev_install.py -e

# 可选：同时安装 CLI
python dev_install.py -e --cli
```

## 快速开始

### Python 使用示例

```python
from openbb import obb

# 获取股票历史价格
output = obb.equity.price.historical("AAPL")
df = output.to_dataframe()
print(df.tail())
```

### 启动 REST API 服务器

```bash
# 方式1：使用 openbb-api 命令
openbb-api

# 方式2：使用 uvicorn 直接启动
uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload
```

API 文档可在 `http://127.0.0.1:8000/docs` 查看。

### 启动 CLI

```bash
openbb
```

## API 密钥配置

创建文件 `~/.openbb_platform/user_settings.json`：

```json
{
  "credentials": {
    "fmp_api_key": "你的密钥",
    "polygon_api_key": "你的密钥",
    "fred_api_key": "你的密钥",
    "benzinga_api_key": "你的密钥"
  }
}
```

或在运行时设置：

```python
from openbb import obb
obb.user.credentials.fred_api_key = "你的密钥"
```

## 数据源提供商

### 主要免费数据源

| 提供商 | 包名 | 描述 |
|--------|------|------|
| Yahoo Finance | openbb-yfinance | 免费股票数据 |
| FRED | openbb-fred | 美联储经济数据 |
| SEC | openbb-sec | 美国证监会数据 |
| FMP | openbb-fmp | Financial Modeling Prep |
| Polygon | openbb-polygon | 股票和加密货币数据 |

### 安装特定数据源

```bash
# 开发模式下安装（从本地源码）
pip install -e ./providers/yfinance

# 或在安装后启用
openbb-build
```

## 运行测试

```bash
# 单元测试
pytest openbb_platform -m "not integration"

# 集成测试（需要 API 服务器运行）
pytest openbb_platform -m integration

# 全部测试
pytest openbb_platform
```

## 模块结构

```
openbb_platform/
├── core/               # 核心功能（FastAPI、Pydantic 模型、Provider 接口）
├── extensions/         # 扩展模块（股票、加密、经济等）
├── providers/          # 数据源提供商
├── obbject_extensions/ # 对象扩展（图表）
└── dev_install.py      # 开发安装脚本
```

## 开发指南

- [工程知识文档](../docs/knowledge/02-openbb-platform.md)
- [核心模块详解](../docs/knowledge/02-openbb-platform.md)
- [扩展开发指南](./CONTRIBUTING.md)

## 许可证

AGPL-3.0 License
