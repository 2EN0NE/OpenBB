# OpenBB Plotly 图表组件

基于 React + TypeScript + Plotly 的图表组件，用于 OpenBB 平台的数据可视化。

## 技术栈

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Plotly.js

## 从源码安装

```bash
cd frontend-components/plotly

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

## 组件列表

| 组件 | 路径 | 功能 |
|------|------|------|
| Chart | `components/Chart.tsx` | 主图表组件 |
| AutoScaling | `components/AutoScaling.tsx` | 自动缩放 |
| Config | `components/Config.tsx` | 配置面板 |
| PlotlyConfig | `components/PlotlyConfig.tsx` | Plotly 配置 |

### Dialog 组件

| 组件 | 路径 | 功能 |
|------|------|------|
| AlertDialog | `components/Dialogs/AlertDialog.tsx` | 警告对话框 |
| CommonDialog | `components/Dialogs/CommonDialog.tsx` | 通用对话框 |
| OverlayChartDialog | `components/Dialogs/OverlayChartDialog.tsx` | 叠加图表 |

## 与 OpenBB Platform 集成

构建后的文件被复制到：

```
openbb_platform/obbject_extensions/charting/openbb_charting/core/assets/
```

在 Python 中使用：

```python
from openbb import obb

# 显示图表
obb.equity.price.historical("AAPL", chart=True)
```

## 开发

```bash
# 类型检查
npx tsc --noEmit

# 代码检查
npx eslint src/

# 运行测试
npm test
```

## 许可证

AGPL-3.0 License
