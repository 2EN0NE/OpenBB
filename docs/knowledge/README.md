# OpenBB 工程知识库

本目录包含 OpenBB 项目的工程结构、模块设计和开发指南文档。

## 文档索引

| 文档 | 内容 |
|------|------|
| [01-project-overview.md](./01-project-overview.md) | 项目概览和整体架构 |
| [02-openbb-platform.md](./02-openbb-platform.md) | 核心平台模块详解 |
| [03-cli-module.md](./03-cli-module.md) | 命令行界面模块详解 |
| [04-frontend-components.md](./04-frontend-components.md) | 前端组件模块详解 |
| [05-desktop-module.md](./05-desktop-module.md) | 桌面应用模块详解 |

## 快速导航

### 开始使用

1. **安装 OpenBB**
   ```bash
   pip install openbb
   ```

2. **启动 API 服务器**
   ```bash
   openbb-api
   ```

3. **启动 CLI**
   ```bash
   pip install openbb-cli
   openbb
   ```

### 开发设置

1. **克隆仓库**
   ```bash
   git clone https://github.com/OpenBB-finance/OpenBB.git
   cd OpenBB
   ```

2. **安装开发环境**
   ```bash
   cd openbb_platform
   python dev_install.py -e
   ```

3. **运行测试**
   ```bash
   pytest openbb_platform
   ```

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

## 技术栈

| 模块 | 技术 |
|------|------|
| OpenBB Platform | Python, FastAPI, Pydantic, Poetry |
| CLI | Python, prompt-toolkit, rich |
| Desktop | Tauri (Rust), React, TypeScript |
| Frontend | React, TypeScript, Plotly, Tailwind CSS |

## 相关链接

- [项目 README](../../README.md)
- [行为准则](../../CODE_OF_CONDUCT.md)
- [安全政策](../../SECURITY.md)
- [官方文档](https://docs.openbb.co)
- [GitHub 仓库](https://github.com/OpenBB-finance/OpenBB)
