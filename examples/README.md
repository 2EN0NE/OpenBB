# 使用 OpenBB 平台的 Jupyter Notebook 示例

本文件夹收集了展示如何开始使用 OpenBB 平台的示例 Notebook。要运行它们，请确保选择的内核与安装 OpenBB 的 Python 虚拟环境相同。

## 目录

### googleColab

此 Notebook 在 Google Colab 环境中安装 OpenBB 平台，包含以下示例：

- 登录 OpenBB Hub
- 设置输出偏好
- 获取期权和公司基本面数据
- 创建条形图可视化

### findSymbols

此 Notebook 介绍如何发现、查找和搜索股票代码。

- 搜索
- 查找公司和机构文件
- 按地区和指标筛选股票

### loadHistoricalPriceData

此 Notebook 介绍如何收集历史价格数据，使用不同的间隔和多种数据源。

- 使用不同间隔加载数据，更换数据源
- 股票代码符号简要说明
- 重采样时间序列索引
- 不同提供商之间的差异，比较输出

### financialStatements

这组示例介绍 OpenBB 平台中的财务报表，并比较大型零售行业公司的自由现金流收益率。

- 财务报表
- 不同数据源的数据预期
- 财务属性
- 比率和其他指标

### copperToGoldRatio

此 Notebook 解释如何计算和绘制铜金比率。

- 加载历史近月期货价格
- 从 FRED 获取 10 年期美国国债的历史序列
- 执行基本的 DataFrame 操作
- 使用 Plotly Graph Objects 创建图表

### openbbPlatformAsLLMTools

此 Notebook 展示如何通过函数调用将 OpenBB 平台用作 LLM 中的函数。

- 从 OpenBB 平台函数创建 LLM 工具
- 将所有 OpenBB 平台函数转换为 LLM 工具
- 构建可利用函数调用的基础 Langchain 代理
- 运行代理

### usdLiquidityIndex

此 Notebook 演示如何查询美联储经济数据库并重新创建美元流动性指数。

- 搜索 FRED 序列 ID
- 将多个序列作为单次调用加载
- 解包 FRED 查询的数据响应
- 对 DataFrame 执行算术运算
- 序列或 DataFrame 的标准化方法
- 创建图表的简单流程

### impliedEarningsMove

此 Notebook 演示如何使用来自免费来源的期权价格计算隐含收益变动。

- 获取即将到来的收益日历
- 获取期权链数据
- 获取标的股票的最后价格
- 找到最接近股票最后价格的看涨和看跌行权价
- 使用跨式期权价格计算隐含日波动

### streamlit/news

这是一个新闻标题的 Streamlit 仪表板示例，数据来自 Biztoc、Benzinga、FMP、Intrinio 和 Tiingo。

:::warning
至少需要一个 API 密钥。你可以 [在此](https://rapidapi.com/thma/api/biztoc) 获取免费的 Biztoc API 密钥
:::

要运行，将文件复制到你的系统，打开终端，导航到文件所在位置，并在 `obb` Python 环境激活状态下输入：

```bash
pip install streamlit
pip install openbb-biztoc
streamlit run news.py
```
