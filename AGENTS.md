# AGENTS.md

本文档包含项目的开发原则、规范和最佳实践，供 AI Agent 参考。

## 📋 顶级原则

### 无论来做什么，都要把计划和 todo 列表放在工程一级目录下的 todo.md 文件里。

### 每完成一个阶段的工作，就把上一阶段的经验教训更新到 AGENTS.md 里。

### 当一个计划完成并且代码合并后，把这个工作的设计文档添加到项目的知识库中docs/knowledge

### Git 提交规范（强制）
**所有代码提交必须遵循以下格式：**

```
<type>(<scope>): <subject>

<details>

-- vibecoding by <agent_name> <model_version>
```

**格式说明：**
- `<type>`: 提交类型，必须是以下之一
  - `feat`: 新功能
  - `fix`: 修复 bug
  - `refactor`: 重构代码
  - `docs`: 文档更新
  - `test`: 测试相关
  - `chore`: 构建/工具相关
- `<scope>`: 主要改动的包名或模块名（可选但推荐，一般小写）
  - 示例：`agent`, `api`, `lbma_gold`, `base`, `tool`, `workflow`
- `<subject>`: 简短描述（中文或英文，不超过 50 字符）
- `<details>`: 详细描述（可选，但推荐）
- `-- vibecoding by <model_version>`: **必须根据Agent你是用的哪个模型，来决定包含的 VibeCoding 注记**

**VibeCoding 注记规范：**
`<model_version>`可能包饭
- 当前编码Agent: 如`Kimi Code`、`openCode`、`cline`
- 当前模型: 如`Kimi k2.5`、`Minimax M2.1`、`claude-opus-4.5`
- 完整注记: 去掉可能的重复项，如`-- vibecoding by kimi code k2.5`

**提交示例：**
```bash
# 新功能
git commit -m "feat(agent): 添加 LBMA 黄金波动率 Agent" -m "-- vibecoding by kimi code k2.5"

# 修复 bug
git commit -m "fix(api): 修复 Agent 注册失败问题" -m "-- vibecoding by Minimax M2.1"

# 重构
git commit -m "refactor(base): 优化波动率计算工具性能" -m "-- vibecoding by claude-opus-4.5"

# 文档更新
git commit -m "docs: 更新 README 添加 API 使用示例" -m "-- vibecoding by gpt-5.2-codex"

# 测试相关
git commit -m "test(agent): 添加 LBMA Gold Agent 单元测试" -m "-- vibecoding by gemini-3-pro-preview"
```

**为什么需要 VibeCoding 注记？**
- 追踪代码来源，方便问题回溯
- 统计各 Agent 的贡献
- 建立 AI 编程的透明度

#### 最后的回答给出本次Git Commit Message的参考（强制）

#### 最直接的这次对话中没有说到帮提交Git，不允许进行任何Git变更操作（强制）


## 🧪 核心原则：TDD（测试驱动开发）

### 1. 测试先行

**强制要求**：所有功能开发必须遵循 TDD 流程：

1. **红**：先写测试（测试会失败）
2. **绿**：实现功能（让测试通过）
3. **重构**：优化代码（保持测试通过）

### 2. 测试覆盖要求

- **所有 public 方法必须有单元测试**
- **Agent 的 analyze() 方法必须测试**
- **API 端点必须有集成测试**
- **边界条件必须测试**（空数据、异常值等）

### 3. 测试运行规范（强制全回归）

**⚠️ 重要：每次任务完成后必须运行全回归测试，不得指定测试文件夹！**

**为什么必须全回归？**
- Agent 注册是全局状态，只测试单个文件无法发现注册问题
- API 依赖 Agent 注册，分开测试无法发现集成问题
- 修改公共工具可能影响多个 Agent

**特殊情况处理：**
- 如果确实有测试无法通过，先尝试修复
- 如果尽力了仍无法通过，在回答中如实说明原因和影响
- 永远不要隐瞒测试失败或选择性运行测试

### 4. 诚实报告原则

**禁止作假**：必须真实报告测试结果

- ✅ 如果所有测试通过，报告通过率
- ⚠️ 如果有测试失败，如实报告失败原因
- 🔍 如果尽力了但个别测试无法通过，说明分析


## 🎯 工程演进方向

### 愿景：打造类彭博终端的专业交易系统

参考彭博终端（Bloomberg Terminal）的"信息-分析-决策-执行"闭环，逐步演进为模块化专业交易系统。

### 核心架构分层

```
┌─────────────────────────────────────────────────────────────────┐
│  D. 交易执行系统 (OMS) - EMSX                                    │
│     订单路由 + 风控模块 + 执行算法(TWAP/VWAP)                    │
├─────────────────────────────────────────────────────────────────┤
│  C. 策略与回测引擎 - Strategy & Backtesting                      │
│     信号生成 + 回测验证 + 参数优化                               │
├─────────────────────────────────────────────────────────────────┤
│  B. 资产看板 (PMS) - PORT                                        │
│     持仓追踪 + 净值曲线 + 归因分析(夏普/回撤)                    │
├─────────────────────────────────────────────────────────────────┤
│  A. 数据中心 - Market Data Server                                │
│     行情接入(AkShare/Tushare) + 实时推流 + ETL清洗               │
└─────────────────────────────────────────────────────────────────┘
```

### 演进路线

| 阶段 | 目标 | 核心任务 |
|------|------|----------|
| **第一阶段** | 核心资产追踪 | 记录"时间、代码、方向、价格、手续费"，生成净值曲线 |
| **第二阶段** | 分析与策略化 | 接入历史行情，验证投资直觉，回测验证 |
| **第三阶段** | 自动化与风控 | 对接券商 API，机器下单，风控规则(止损/仓位限制) |

### 界面设计原则

1. **多窗口联动（Grouping）**: 选中标的，研报、股价图、财报同步切换
2. **指令驱动（Command-driven）**: 输入简码快速操作（如 `AAPL EQUITY CP`）
3. **可定制看板**: 关键指标（当日盈亏、风险敞口）固定在显眼位置

### 技术演进路径

- **当前**: Python + FastAPI + Pydantic 数据标准化
- **近期**: 增加实时数据 WebSocket 推送、本地数据库存储
- **中期**: 集成 Backtrader/VeighNa 回测框架
- **远期**: OMS 订单管理系统、风控引擎

---

## 📝 经验教训记录（按提交时间从新到老排序）
**只填写本次提交所导致问题的经验教训，只提关键项，与之前的经验有类似问题的需要抽取共性，把新的问题作为案例举例，避免内容过长**

### 2026-02-01 - 工程分析与文档翻译

**任务**: 全面分析 OpenBB 工程结构，创建知识文档，翻译 README 等文档为中文

**关键经验**:

1. **工程分析策略**
   - 先读取 README 和 CONTRIBUTING 文档了解项目概况
   - 使用 `glob` 工具快速探索目录结构
   - 重点关注 `pyproject.toml` 文件理解包依赖关系
   - 示例：`openbb_platform` 使用 Poetry 管理依赖，`dev_install.py` 是开发安装的关键脚本

2. **知识文档组织**
   - 按模块拆分文档：project-overview、openbb-platform、cli-module、frontend-components、desktop-module
   - 每个文档包含：目录结构、核心组件、使用方法、开发指南
   - 添加 README 作为知识库入口索引
   - 文档放在 `docs/knowledge/` 目录下便于维护

3. **文档翻译要点**
   - 去除冗余图片，保留功能性徽章（如 PyPI、Discord）
   - 强调"如何启动"和"如何使用"
   - 保持代码示例的可运行性
   - 添加中文说明但不破坏原有链接

4. **OpenBB 架构理解**
   - 核心三层：Providers（数据源）→ Core（核心）→ Extensions（扩展）
   - 多接口暴露：Python API、REST API、CLI、Desktop GUI
   - 扩展机制：通过 Cookiecutter 模板创建新扩展
   - 数据标准化：TET 模式（Transform-Extract-Transform）

5. **文件备份策略**
   - 中文翻译直接覆盖原文件（因为用户要求"全部变成中文"）
   - 如需保留英文版，应创建 `README_CN.md` 而非 `README_EN.md`
   - 原文档内容已阅读并提取关键信息
