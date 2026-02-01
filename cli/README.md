# OpenBB 平台命令行界面 (CLI)

[![Downloads](https://static.pepy.tech/badge/openbb)](https://pepy.tech/project/openbb)
[![LatestRelease](https://badge.fury.io/py/openbb.svg)](https://github.com/OpenBB-finance/OpenBB)

## 概述

OpenBB 平台 CLI 是一个命令行界面，包装了 [OpenBB 平台](https://docs.openbb.co/platform)。

它提供了一种便捷的方式来与 OpenBB 平台及其扩展进行交互，以及通过 OpenBB 例程脚本实现自动化数据收集。

## 从源码安装

### 环境要求

- Python 3.10 - 3.13
- Poetry (`pip install poetry`)

### 安装步骤

```bash
# 进入 CLI 目录
cd cli

# 使用 Poetry 安装
poetry install

# 或使用 pip 开发安装
pip install -e .
```

### 从 Platform 目录一起安装

```bash
cd openbb_platform
python dev_install.py -e --cli
```

## 启动 CLI

安装完成后，运行以下命令启动 CLI：

```bash
openbb
```

## CLI 特点

- **自动补全**: 命令和参数的智能补全
- **语法高亮**: 美观的命令输出
- **交互式导航**: 菜单式界面，支持 `..` 返回上级
- **例程脚本**: 支持 `.openbb` 脚本文件自动化

## 命令结构

```
OpenBB CLI
├── stocks/          # 股票
├── crypto/          # 加密货币
├── etf/             # ETF
├── forex/           # 外汇
├── economy/         # 经济
├── fixedincome/     # 固定收益
├── alternative/     # 另类数据
├── portfolio/       # 投资组合
└── settings/        # 设置
```

## 使用示例

```bash
# 启动 CLI
openbb

# 进入股票菜单
/stocks

# 加载股票数据
load AAPL --start 2023-01-01

# 显示 K 线图
candle

# 显示基本面数据
/fa/income

# 返回上级菜单
..

# 退出
exit
```

## 快捷命令

| 命令 | 功能 |
|------|------|
| `?` / `help` | 显示帮助 |
| `q` / `quit` | 退出程序 |
| `..` | 返回上级菜单 |
| `/` | 返回主菜单 |
| `reset` | 重置当前菜单 |

## 例程脚本

创建 `.openbb` 脚本文件自动化任务：

```
# 示例: routine.openbb
stocks
load AAPL
candle
ma 20 50
export data.csv
exit
```

运行脚本：
```bash
openbb -s routine.openbb
```

## 配置

CLI 配置文件位于 `~/.openbb_cli/settings.json`：

```json
{
  "theme": "dark",
  "table_style": "rich",
  "interactive": true
}
```

## 开发指南

[CLI 模块详解](../docs/knowledge/03-cli-module.md)

## 运行测试

```bash
# 单元测试
pytest cli/tests/

# 集成测试
pytest cli/integration/
```

## 许可证

AGPL-3.0 License
