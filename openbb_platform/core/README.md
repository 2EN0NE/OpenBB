# OpenBB 开放数据平台 - 核心模块

OpenBB 开放数据平台（ODP）的开源工具集，帮助数据工程师集成各种数据源。

ODP 作为"一次连接，随处消费"的基础设施层，将数据暴露给多个消费端：Python 环境、OpenBB Workspace、MCP 服务器和 REST API。

## 概述

核心扩展（Core）是构建和集成 OpenBB 数据平台 Python 包的基础。它提供了标准化和处理数据所需的类和结构。

它还负责生成 REST API 和 Python 包的静态资源，这些资源独立运行并与各种消费端接口。

通常，该库将作为项目依赖使用并进行扩展。

开发入门信息请访问 [文档](https://docs.openbb.co/python/developer)。

### 环境要求

- Python >=3.10,<3.14
- 熟悉 FastAPI 和 Pydantic

### 从源码安装

```bash
cd openbb_platform/core
pip install -e .
```

> 注意：openbb-core 是 OpenBB 平台的基础设施组件，不建议作为独立包使用。

### 构建

使用已安装的扩展构建 Python 应用程序：

```bash
openbb-build
```

## 核心特性

- **标准化数据模型** (`Data` 类): 灵活且动态的 Pydantic 模型，能够处理各种数据结构
- **标准化查询参数** (`QueryParams` 类): 用于处理对不同提供商查询的 Pydantic 模型
- **动态字段支持**: 支持处理未定义的字段，提供数据处理的多功能性
- **强大的数据验证**: 利用 Pydantic 的验证特性确保数据完整性
- **API 路由机制** (`Router` 类): 简化定义 API 路由和端点的过程 - 开箱即用的 Python 和 Web 端点

## 核心架构

```
core/openbb_core/
├── api/              # REST API 实现
│   ├── rest_api.py   # FastAPI 入口
│   └── router/       # 路由定义
├── app/              # 应用逻辑
│   ├── model/        # 数据模型
│   ├── service/      # 服务层
│   └── static/       # 静态资源生成
└── provider/         # Provider 抽象层
    ├── abstract/     # 抽象基类
    └── standard_models/  # 标准数据模型
```

## 关键类说明

| 类 | 文件 | 功能 |
|----|------|------|
| `Data` | `provider/abstract/data.py` | 标准化数据模型基类 |
| `QueryParams` | `provider/abstract/query_params.py` | 标准化查询参数基类 |
| `Fetcher` | `provider/abstract/fetcher.py` | 数据获取抽象类 |
| `Router` | `app/router.py` | API 路由基类 |
| `OBBject` | `app/model/obbject.py` | 统一返回对象 |

## 开发指南

[核心模块详解](../../docs/knowledge/02-openbb-platform.md)

## 报告问题

在 [Github](https://github.com/OpenBB-finance/OpenBB/issues/new/choose) 上报告问题。

## 许可证

AGPL-3.0 License
