# OpenBB 项目概览

## 项目简介

OpenBB（Open Data Platform by OpenBB）是一个开源的金融数据基础设施平台，帮助数据工程师将专有、授权和公共数据源集成到下游应用程序中，如 AI copilots 和研究仪表板。

### 核心理念

ODP 作为"一次连接，随处消费"的基础设施层，将数据整合并暴露给多个消费端：
- **Python 环境** - 供量化分析师使用
- **OpenBB Workspace 和 Excel** - 供分析师使用
- **MCP 服务器** - 供 AI 代理使用
- **REST API** - 供其他应用程序使用

## 项目架构

```
OpenBB/
├── openbb_platform/    # 核心数据平台（Python）
├── cli/                # 命令行界面
├── desktop/            # 桌面应用程序（Tauri + React）
├── frontend-components/# 前端组件（图表、表格）
├── examples/           # 示例和教程
├── cookiecutter/       # 扩展生成模板
└── images/             # 项目图片资源
```

## 技术栈

| 模块 | 技术栈 |
|------|--------|
| OpenBB Platform | Python, FastAPI, Pydantic, Poetry |
| CLI | Python, prompt-toolkit, rich |
| Desktop | Tauri (Rust), React, TypeScript |
| Frontend | React, TypeScript, Plotly, Tailwind CSS |

## 主要功能模块

### 1. OpenBB Platform（核心平台）

提供金融数据访问的 Python 包和 REST API。

**快速开始：**
```bash
pip install openbb
```

```python
from openbb import obb
output = obb.equity.price.historical("AAPL")
df = output.to_dataframe()
```

**启动 API 服务器：**
```bash
openbb-api
# 或
uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000
```

### 2. OpenBB CLI（命令行工具）

通过命令行与 OpenBB Platform 交互。

**安装：**
```bash
pip install openbb-cli
```

**启动：**
```bash
openbb
```

### 3. OpenBB Desktop（桌面应用）

基于 Tauri 和 React 的桌面应用程序，提供图形界面管理环境、后端和 API 密钥。

**特点：**
- 系统托盘应用
- 环境管理（基于 Conda）
- 后端服务管理
- Jupyter Lab 集成

### 4. Frontend Components（前端组件）

可复用的图表和表格组件。

- **plotly/** - 基于 Plotly 的图表组件
- **tables/** - 数据表格组件

## 模块关系图

```
┌─────────────────────────────────────────────────────────────┐
│                      OpenBB Desktop                          │
│                 (Tauri + React GUI)                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌─────────────┐ ┌──────────────┐
│   OpenBB     │ │   OpenBB    │ │  Frontend    │
│     CLI      │ │  Platform   │ │ Components   │
│              │ │             │ │              │
│  命令行界面   │ │  Python API │ │ 图表/表格    │
│              │ │  REST API   │ │              │
└──────┬───────┘ └──────┬──────┘ └──────────────┘
       │                │
       └────────┬───────┘
                │
       ┌────────▼────────┐
       │  Data Providers │
       │  - Yahoo Finance│
       │  - FRED         │
       │  - Polygon      │
       │  - ...          │
       └─────────────────┘
```

## 开发环境要求

- **Python**: 3.10 - 3.13
- **Node.js**: 最新稳定版
- **Rust**: 1.90.0+ (用于 Desktop)
- **Poetry**: 依赖管理
- **Conda**: 环境管理

## 本地开发设置

### 1. 克隆仓库
```bash
git clone https://github.com/OpenBB-finance/OpenBB.git
cd OpenBB
```

### 2. 安装 OpenBB Platform
```bash
cd openbb_platform
python dev_install.py -e
```

### 3. 安装 CLI（可选）
```bash
python dev_install.py -e --cli
```

### 4. 启动 Desktop（可选）
```bash
cd desktop
npm install
npm run tauri dev
```

## 许可证

AGPLv3 License

## 相关链接

- 官方文档: https://docs.openbb.co
- 官网: https://www.openbb.co
- PyPI: https://pypi.org/project/openbb/
- Discord: https://discord.com/invite/xPHTuHCmuV
