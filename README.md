# OpenBB 开放数据平台

本工程clone自OpenBB 开放数据平台（ODP）是一个开源工具集，帮助数据工程师将专有、授权和公共数据源集成到下游应用程序中，如 AI Copilots 和研究仪表板。

ODP 作为"一次连接，随处消费"的基础设施层，将数据整合并同时暴露给多个消费端：
- **Python 环境** - 供量化分析师使用
- **OpenBB Workspace 和 Excel** - 供分析师使用
- **MCP 服务器** - 供 AI 代理使用
- **REST API** - 供其他应用程序使用

---

## 工程演进方向：打造类彭博终端的专业交易系统

本项目的设计愿景是参考彭博终端（Bloomberg Terminal）的"信息-分析-决策-执行"闭环，逐步演进为一套模块化的专业交易系统。

### 核心架构分层

系统按以下四个核心模块演进，模块间通过 API 或消息队列（Redis/RabbitMQ）通信：

```
┌─────────────────────────────────────────────────────────────────┐
│                    交易执行系统 (OMS)                             │
│              Order Management System - EMSX                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │   订单路由    │  │   风控模块    │  │   执行算法(TWAP/VWAP) │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ 信号
┌─────────────────────────────────────────────────────────────────┐
│                    策略与回测引擎                                │
│         Strategy & Backtesting - 逻辑判断中心                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │  信号生成    │  │  回测验证    │  │   参数优化            │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ 数据
┌─────────────────────────────────────────────────────────────────┐
│                    资产看板 (PMS)                                │
│      Portfolio Management System - PORT 命令                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │  持仓追踪    │  │  净值曲线    │  │  归因分析(夏普/回撤)  │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ 行情
┌─────────────────────────────────────────────────────────────────┐
│                    数据中心 (Market Data Server)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │  行情接入    │  │  实时推流    │  │   ETL/数据清洗       │   │
│  │ AkShare/     │  │  WebSocket   │  │                      │   │
│  │ Tushare/     │  │  Level 2     │  │                      │   │
│  │ Binance      │  │  逐笔数据    │  │                      │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

#### A. 数据中心（Market Data Server）
- **当前**: 定时抓取收盘价（AkShare、Tushare、Yahoo Finance）
- **演进**: WebSocket 实时推流、Level 2 逐笔数据、ETL 清洗管道

#### B. 资产看板（Portfolio Management System）
- **当前**: 基础持仓记录
- **演进**: 完整的 PORT 功能（净值曲线、夏普比率、回撤归因、交易流水分析）

#### C. 策略与回测引擎（Strategy & Backtesting）
- **当前**: Jupyter Notebook 研究环境
- **演进**: Backtrader/VeighNa 多品种多周期回测框架

#### D. 交易执行系统（Order Management System）
- **当前**: 手动下单、弹窗提醒
- **演进**: EMSX 式订单路由、风控模块（单笔限制、总仓位限制、自动平仓）

### 演进路线图

| 阶段 | 目标 | 核心任务 | 参考工具 |
|------|------|----------|----------|
| **第一阶段** | 核心资产追踪 | 记录"时间、代码、方向、价格、手续费"，生成净值曲线 | AkShare, 本地数据库 |
| **第二阶段** | 分析与策略化 | 接入历史行情，验证投资直觉，回测验证 | Backtrader, QuantConnect |
| **第三阶段** | 自动化与风控 | 对接券商 API，机器下单，风控规则 | VeighNa (VN.py) |

### 界面设计参考

借鉴彭博终端的"工作区管理（Workspace）"理念：

1. **多窗口联动（Grouping）**: 选中某只股票，研报、股价图、财务报表同步切换
2. **指令驱动（Command-driven）**: 输入简码快速操作（如 `AAPL EQUITY CP` 查看股价）
3. **高度可定制的看板**: 关键指标（当日盈亏、风险敞口）固定在最显眼位置

---

## 当前工程安装指南

> 本指南面向从源码构建和开发，而非安装 PyPI 发布的版本。

### 环境要求

- **Git**
- **Python** 3.10 - 3.13
- **Poetry** (`pip install poetry`)
- **Node.js** 和 **NPM** (用于 Desktop 和前端组件)
- **Rust** 1.90.0+ (用于 Desktop)

### 1. 克隆仓库

```bash
git clone https://github.com/OpenBB-finance/OpenBB.git
cd OpenBB
```

### 2. 安装 OpenBB Platform（核心）

```bash
cd openbb_platform

# 安装所有核心包、扩展和数据源（开发模式）
python dev_install.py -e

# 可选：同时安装 CLI
python dev_install.py -e --cli
```

安装完成后，项目将以 editable 模式安装，你可以在本地修改代码并立即生效。

### 3. 启动服务

**启动 API 服务器:**
```bash
openbb-api
# 或
uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 6900 --reload
```

**启动 CLI:**
```bash
openbb
```

### 4. 安装 Desktop（可选）

```bash
cd desktop

# 安装依赖
npm install

# 启动开发服务器
npm run tauri dev
```

### 5. 构建前端组件（可选）

```bash
cd frontend-components/plotly
npm install
npm run build

cd ../tables
npm install
npm run build
```

### 6. 运行测试

```bash
# 单元测试（快速）
pytest openbb_platform -m "not integration"

# 集成测试（需要 API 服务器运行）
pytest openbb_platform -m integration

# 全部测试
pytest openbb_platform
```

---

## 快速使用示例

### Python API

```python
from openbb import obb

# 股票数据
output = obb.equity.price.historical("AAPL", provider="yfinance")
df = output.to_dataframe()

# 加密货币
obb.crypto.price.historical("BTC-USD")

# 经济指标
obb.economy.gdp()

# 使用图表功能
obb.equity.price.historical("AAPL", chart=True)
```

### CLI

```bash
# 启动 CLI
openbb

# 进入股票菜单
/stocks

# 加载股票
load AAPL

# 显示 K 线图
candle
```

### REST API

```bash
# 启动服务器后访问
curl "http://127.0.0.1:6900/api/v1/equity/price/historical?symbol=AAPL"
```

---

## 配置 API 密钥

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

---

## 项目结构

```
OpenBB/
├── openbb_platform/    # 核心数据平台（Python + FastAPI）
│   ├── core/          # 核心功能（Router、Data Model、Provider Interface）
│   ├── extensions/    # 扩展模块（股票、加密、经济等）
│   ├── providers/     # 数据源（Yahoo、FRED、Polygon 等）
│   └── obbject_extensions/  # 图表扩展
├── cli/               # 命令行界面（Python + prompt-toolkit）
├── desktop/           # 桌面应用（Tauri + React）
├── frontend-components/  # 前端组件（Plotly 图表、Tables）
├── examples/          # 示例 Notebook
└── docs/knowledge/    # 工程知识文档
```

---

## 开发指南

- [工程知识文档](./docs/knowledge/README.md)
- [开发架构](./docs/knowledge/02-openbb-platform.md)
- [CLI 模块](./docs/knowledge/03-cli-module.md)
- [Desktop 模块](./docs/knowledge/05-desktop-module.md)

---

## 社区

- [Discord](https://openbb.co/discord)
- [Twitter/X](https://x.com/openbb_finance)

---

## 许可证

AGPLv3 License. 详见 [LICENSE](LICENSE) 文件。

---

## 免责声明

金融工具交易涉及高风险，包括可能损失部分或全部投资金额，可能不适合所有投资者。

在决定进行金融工具交易之前，您应充分了解交易金融市场的风险和成本，仔细考虑您的投资目标、经验水平和风险偏好，并在需要时寻求专业建议。
