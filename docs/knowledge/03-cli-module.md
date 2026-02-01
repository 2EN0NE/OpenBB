# CLI 模块详解

## 模块概述

`cli` 模块是 OpenBB 的命令行界面，提供交互式终端访问 OpenBB Platform 的功能。它基于 `prompt-toolkit` 和 `rich` 构建，提供自动补全、语法高亮和美观的输出格式。

## 目录结构

```
cli/
├── openbb_cli/                 # CLI 主包
│   ├── argparse_translator/    # 参数解析翻译
│   │   ├── argparse_argument.py
│   │   ├── argparse_class_processor.py
│   │   ├── argparse_translator.py
│   │   ├── obbject_registry.py
│   │   ├── reference_processor.py
│   │   └── utils.py
│   ├── assets/                 # 资源文件
│   │   ├── routines/           # 例程脚本
│   │   └── styles/             # 样式配置
│   ├── config/                 # 配置模块
│   │   ├── completer.py        # 自动补全
│   │   ├── console.py          # 控制台
│   │   ├── constants.py        # 常量
│   │   ├── menu_text.py        # 菜单文本
│   │   ├── setup.py            # 设置
│   │   └── style.py            # 样式
│   ├── controllers/            # 控制器
│   │   ├── base_controller.py
│   │   ├── base_platform_controller.py
│   │   ├── cli_controller.py
│   │   ├── platform_controller_factory.py
│   │   ├── script_parser.py
│   │   ├── settings_controller.py
│   │   ├── choices.py
│   │   └── utils.py
│   ├── models/                 # 数据模型
│   │   └── settings.py
│   ├── utils/                  # 工具函数
│   │   └── utils.py
│   ├── cli.py                  # 主入口
│   └── session.py              # 会话管理
├── tests/                      # 测试
├── integration/                # 集成测试
├── pyproject.toml              # 包配置
└── README.md                   # 文档
```

## 核心组件

### 1. 主入口 (`cli.py`)

CLI 的启动入口，定义了 `main()` 函数。

**启动方式：**
```bash
# 安装后使用命令
openbb

# 或从源码运行
python -m openbb_cli.cli
```

### 2. 控制器层 (`controllers/`)

#### 2.1 CLI Controller (`cli_controller.py`)

主控制器，管理顶级菜单和路由：
- 处理用户输入
- 导航到子菜单
- 管理会话状态

#### 2.2 Base Controller (`base_controller.py`)

所有控制器的基类，提供：
- 命令解析
- 菜单切换
- 通用命令（help、quit、reset 等）

#### 2.3 Base Platform Controller (`base_platform_controller.py`)

OpenBB Platform 命令的控制器基类，处理：
- 动态命令生成
- 参数处理
- 结果展示

#### 2.4 Platform Controller Factory (`platform_controller_factory.py`)

动态创建平台控制器，基于 OpenBB Platform 的路由结构自动生成菜单。

#### 2.5 Settings Controller (`settings_controller.py`)

管理 CLI 设置：
- 主题切换（dark/light）
- 输出格式
- 表格样式

#### 2.6 Script Parser (`script_parser.py`)

解析和执行 `.openbb` 脚本文件。

### 3. 参数解析 (`argparse_translator/`)

将 OpenBB Platform 的命令定义转换为 argparse 参数：

| 文件 | 功能 |
|------|------|
| `argparse_translator.py` | 主翻译器 |
| `argparse_argument.py` | 参数定义 |
| `argparse_class_processor.py` | 类处理器 |
| `reference_processor.py` | 引用处理器 |
| `obbject_registry.py` | OBBject 注册表 |

### 4. 配置 (`config/`)

#### 4.1 Completer (`completer.py`)

命令自动补全系统：
- 命令补全
- 参数补全
- 历史记录

#### 4.2 Console (`console.py`)

Rich 控制台配置，用于美化输出。

#### 4.3 Style (`style.py`)

主题和样式管理：
- 暗色主题
- 亮色主题
- 自定义样式

### 5. 资源文件 (`assets/`)

#### 5.1 Routines (`routines/`)

存放 `.openbb` 脚本文件，用于自动化任务。

**示例脚本：**
```
# routine_example.openbb
stocks
load AAPL
candle
exit
```

#### 5.2 Styles (`styles/`)

- **default/** - 默认样式
  - `dark.*.json` - 暗色主题
  - `light.*.json` - 亮色主题
- **user/** - 用户自定义样式

## 启动流程

```
1. 用户输入 `openbb`
   ↓
2. 执行 cli.py:main()
   ↓
3. 初始化 Session
   ↓
4. 加载配置和样式
   ↓
5. 启动 CLIController
   ↓
6. 显示主菜单，等待用户输入
```

## 命令结构

### 顶级菜单

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

### 命令格式

```
/menu/command --param1 value1 --param2 value2
```

**示例：**
```
/stocks/load AAPL --start 2023-01-01
/stocks/price/historical AAPL
```

## 快捷命令

| 命令 | 功能 |
|------|------|
| `?` / `help` | 显示帮助 |
| `q` / `quit` | 退出程序 |
| `..` | 返回上级菜单 |
| `/` | 返回主菜单 |
| `reset` | 重置当前菜单 |
| `r` / `run` | 运行脚本 |
| `stop` | 停止自动补全 |

## 配置文件

### 用户设置

```
~/.openbb_cli/
├── settings.json          # CLI 设置
├── hub_credentials.json   # Hub 登录凭证
└── routines/              # 自定义脚本
```

### 设置文件示例

```json
{
  "theme": "dark",
  "table_style": "rich",
  "interactive": true,
  "version": "1.0.0"
}
```

## 脚本系统

### 脚本语法

`.openbb` 脚本使用简单的命令序列：

```
# 注释以 # 开头
stocks          # 进入股票菜单
load AAPL       # 加载 AAPL 数据
candle          # 显示 K 线图
ma 20 50        # 添加移动平均线
export data.csv # 导出数据
exit            # 退出
```

### 运行脚本

```bash
# 方式1：在 CLI 中运行
openbb > /path/to/script.openbb

# 方式2：作为参数运行
openbb -s /path/to/script.openbb

# 方式3：拖放脚本到 CLI
```

## 与 OpenBB Platform 的集成

CLI 通过以下方式与 Platform 交互：

1. **动态命令发现** - 自动检测 Platform 中注册的所有命令
2. **参数翻译** - 将 Platform 的参数定义转换为 CLI 参数
3. **结果展示** - 使用 Rich 库美化输出表格和图表

## 开发指南

### 安装开发环境

```bash
cd cli

# 使用 Poetry 安装
poetry install

# 或使用 pip
pip install -e .
```

### 添加新命令

CLI 命令是自动从 OpenBB Platform 生成的，无需手动添加。只需：

1. 在 Platform 中创建新的 Router
2. 使用 `@router.command()` 装饰器
3. 重新启动 CLI，新命令会自动出现

### 测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_cli.py

# 集成测试
pytest integration/
```

## 常用命令示例

### 股票数据

```bash
openbb

# 进入股票菜单
/stocks

# 加载股票数据
load AAPL --start 2023-01-01

# 显示 K 线图
candle

# 显示基本面数据
/fa/income

# 显示技术指标
/ta/sma --length 20 50
```

### 经济宏观数据

```bash
# 进入经济菜单
/economy

# 获取 GDP 数据
/gdp

# 获取通胀数据
/cpi

# 获取利率
/fed_rate
```

### 加密货币

```bash
# 进入加密货币菜单
/crypto

# 加载比特币数据
/load BTC-USD

# 显示 K线图
candle
```

## 故障排除

### 常见问题

**问题：命令不自动补全**
- 解决方案：按 `Tab` 键或检查 `config/completer.py`

**问题：样式不生效**
- 解决方案：检查 `~/.openbb_cli/settings.json` 中的 theme 设置

**问题：无法连接到 Platform**
- 解决方案：确保 `openbb` 包已正确安装

## 依赖项

```toml
[tool.poetry.dependencies]
python = "^3.10,<3.14"
openbb = { version = "^4.6.0", extras = ["all"] }
prompt-toolkit = "^3.0.50"
rich = "^14.0.0"
python-dotenv = "^1.0.1"
openpyxl = "^3.1.5"
pywry = "^0.6.2"
```
