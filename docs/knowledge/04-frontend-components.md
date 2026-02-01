# Frontend Components 模块详解

## 模块概述

`frontend-components` 包含可复用的前端组件，用于在 OpenBB Platform 中渲染图表和表格。这些组件基于 React、TypeScript 和 Plotly 构建，提供交互式的数据可视化功能。

## 目录结构

```
frontend-components/
├── fonts/                      # 字体文件
│   ├── FiraCode-Regular.ttf
│   └── FiraCode-VF.ttf
├── plotly/                     # 图表组件
│   ├── src/
│   │   ├── components/         # React 组件
│   │   ├── data/               # 模拟数据
│   │   ├── utils/              # 工具函数
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── tailwind.config.cjs
└── tables/                     # 表格组件
    ├── src/
    │   ├── components/         # React 组件
    │   ├── data/               # 模拟数据
    │   ├── utils/              # 工具函数
    │   ├── App.tsx
    │   ├── index.css
    │   └── main.tsx
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── tailwind.config.cjs
```

## 技术栈

| 技术 | 用途 |
|------|------|
| React 18 | UI 框架 |
| TypeScript | 类型安全 |
| Vite | 构建工具 |
| Tailwind CSS | 样式 |
| Plotly.js | 图表库 |
| TanStack Table | 表格组件 |

## Plotly 图表组件

路径：`frontend-components/plotly/`

### 组件列表

| 组件 | 路径 | 功能 |
|------|------|------|
| Chart | `components/Chart.tsx` | 主图表组件 |
| AutoScaling | `components/AutoScaling.tsx` | 自动缩放 |
| ChangeColor | `components/ChangeColor.tsx` | 颜色切换 |
| Config | `components/Config.tsx` | 配置面板 |
| PlotlyConfig | `components/PlotlyConfig.tsx` | Plotly 配置 |
| ResizeHandler | `components/ResizeHandler.tsx` | 调整大小 |

### Dialog 组件

| 组件 | 路径 | 功能 |
|------|------|------|
| AlertDialog | `components/Dialogs/AlertDialog.tsx` | 警告对话框 |
| CommonDialog | `components/Dialogs/CommonDialog.tsx` | 通用对话框 |
| OverlayChartDialog | `components/Dialogs/OverlayChartDialog.tsx` | 叠加图表 |
| TextChartDialog | `components/Dialogs/TextChartDialog.tsx` | 文本图表 |
| TitleChartDialog | `components/Dialogs/TitleChartDialog.tsx` | 标题编辑 |

### 图标组件

| 组件 | 路径 |
|------|------|
| Close | `components/Icons/Close.tsx` |
| CloseCircle | `components/Icons/CloseCircle.tsx` |
| Info | `components/Icons/Info.tsx` |
| Success | `components/Icons/Success.tsx` |
| Warning | `components/Icons/Warning.tsx` |

### 开发

```bash
cd frontend-components/plotly

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建
npm run build
```

### 与 OpenBB Platform 集成

图表组件通过 `openbb-charting` 扩展与 Platform 集成：

```python
from openbb import obb

# 获取数据
output = obb.equity.price.historical("AAPL")

# 显示图表
output.show()
```

## Tables 表格组件

路径：`frontend-components/tables/`

### 组件列表

| 组件 | 路径 | 功能 |
|------|------|------|
| Chart | `components/Chart.tsx` | 图表组件 |
| Select | `components/Select.tsx` | 选择器 |
| Toast | `components/Toast.tsx` | 提示消息 |

### Table 组件

| 组件 | 路径 | 功能 |
|------|------|------|
| Table | `components/Table/index.tsx` | 主表格组件 |
| ColumnHeader | `components/Table/ColumnHeader.tsx` | 列头 |
| DebouncedInput | `components/Table/DebouncedInput.tsx` | 防抖输入 |
| DownloadFinishedDialog | `components/Table/DownloadFinishedDialog.tsx` | 下载完成提示 |
| Export | `components/Table/Export.tsx` | 导出功能 |
| FilterColumns | `components/Table/FilterColumns.tsx` | 列过滤 |
| InderterminateCheckbox | `components/Table/InderterminateCheckbox.tsx` | 复选框 |
| Pagination | `components/Table/Pagination.tsx` | 分页 |
| Timestamp | `components/Table/Timestamp.tsx` | 时间戳 |

### 开发

```bash
cd frontend-components/tables

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建
npm run build
```

### 功能特性

- **排序** - 点击列头排序
- **过滤** - 列级别过滤
- **分页** - 大数据集分页
- **导出** - 导出为 CSV/Excel
- **列选择** - 显示/隐藏列
- **搜索** - 全局搜索

## 样式系统

### Tailwind 配置

两个组件共享相同的 Tailwind 配置：

```javascript
// tailwind.config.cjs
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // 自定义主题
    },
  },
  plugins: [],
}
```

### CSS 变量

```css
/* index.css */
:root {
  --bb-background-color: #ffffff;
  --bb-text-color: #000000;
  /* ... */
}

.dark {
  --bb-background-color: #000000;
  --bb-text-color: #ffffff;
  /* ... */
}
```

## 构建输出

构建后的文件被 Platform 使用：

```
frontend-components/plotly/dist/
├── index.html
├── assets/
│   ├── index.js
│   └── index.css
```

这些文件被复制到 `openbb_platform/obbject_extensions/charting/` 中。

## 在 Platform 中使用

### 图表

```python
from openbb import obb

# 股票历史价格图表
obb.equity.price.historical("AAPL", chart=True)

# 或获取后显示
output = obb.equity.price.historical("AAPL")
output.show()
```

### 表格

```python
# 数据自动以表格形式显示
output = obb.equity.price.historical("AAPL")
print(output.to_dataframe())
```

## 开发指南

### 添加新图表类型

1. 在 `plotly/src/components/` 创建新组件
2. 在 `App.tsx` 中注册
3. 更新 `openbb_charting` 扩展
4. 测试并构建

### 添加表格功能

1. 在 `tables/src/components/Table/` 修改
2. 使用 TanStack Table API
3. 测试并构建

### 测试

```bash
# 运行测试
npm test

# 类型检查
npx tsc --noEmit

# 代码检查
npx eslint src/
```

## 依赖关系

```
frontend-components/
    ↓ (构建后复制)
openbb_platform/obbject_extensions/charting/openbb_charting/core/assets/
    ↓ (通过 openbb-charting 扩展)
OpenBB Platform (Python)
    ↓ (用户调用 .show())
用户界面
```

## 注意事项

1. **构建顺序** - 修改 frontend-components 后需要重新构建 Platform
2. **样式一致性** - 保持与 OpenBB Desktop 的样式一致
3. **性能优化** - 大数据集需要虚拟滚动
4. **兼容性** - 支持主流浏览器的最新两个版本
