# OpenBB 图表扩展

集成 Plotly 图表库和专用窗口渲染的 OpenBB 扩展。

## 从源码安装

```bash
cd openbb_platform/obbject_extensions/charting

# 开发安装
pip install -e .

# 重新构建 OpenBB 包
openbb-build
```

## 使用方法

安装后，可以通过以下方式使用图表功能：

```python
from openbb import obb

# 获取数据并显示图表
obb.equity.price.historical("AAPL", chart=True)

# 或获取后显示
output = obb.equity.price.historical("AAPL")
output.show()
```

## 功能特性

- **K 线图**: 股票历史价格可视化
- **技术指标**: 移动平均线、布林带等
- **多图表布局**: 支持子图和叠加
- **交互式操作**: 缩放、平移、悬停提示

## 前端组件

图表渲染依赖 `frontend-components/plotly` 构建的静态资源。

构建流程：
1. 在 `frontend-components/plotly` 中运行 `npm run build`
2. 将 `dist/` 目录复制到本扩展的 `core/assets/`

## 技术细节

| 文件 | 功能 |
|------|------|
| `charting.py` | 主图表模块 |
| `core/backend.py` | 图表后端渲染 |
| `core/openbb_figure.py` | OpenBB 图形对象 |
| `charts/` | 各类图表实现 |
| `styles/` | 样式配置 |

## 开发指南

更多详情见 [前端组件文档](../../../docs/knowledge/04-frontend-components.md)

## 许可证

AGPL-3.0 License
